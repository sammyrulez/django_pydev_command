from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
import os

def related_projects_formatter(elements):
    out = ""
    for element in elements:
        out = out + "\n\t<project>%s</project>" % element
    return out

def target_path_formatter(elements):
    return str(elements[0])
        

REL_PRJ_KEY = 'related-projects'
SRC_OPT_KEY = 'src'
TARGET_PATH_KEY = 'target_path'
extra_formatters = {REL_PRJ_KEY:related_projects_formatter, TARGET_PATH_KEY:target_path_formatter }

class Command(BaseCommand):
   
    args = "interpreter python_version" # < related-projects = ... extra-path =
    help = 'Creates eclipse and pydev project files'
    can_import_settings = True
    
    option_list = BaseCommand.option_list + (
        make_option('--src',
            action='store_true',
            dest=SRC_OPT_KEY,
            default=False,
            help='Use \'pydev src\' folder struture'),)
    
    

           # help='Python interpreter definition to use ( must be definied in the target eclipse workspace) '),
                                             
    

    def parse_extra_element(self, extra_registry, extra, elements_list):        
        extra_registry[extra] = extra_formatters[extra](elements_list)

    def handle(self, *args, **options):
   
        interpreter = args[0] 
        python_version = args[1]
        extra_registry = {REL_PRJ_KEY:'', TARGET_PATH_KEY:''}
        if len(args) > 2 :
            extra_args = args[2:]
            for extra in extra_args:
                extra_param = extra.split('=')
                extra_key = extra_param[0]
                elements = extra_param[1]
                if ',' in elements:
                    elements_list = elements.split(',')
                else:
                    elements_list = [elements]
                self.parse_extra_element(extra_registry, extra_key, elements_list)
        
        from django.conf import settings
        
        prjname = settings.ROOT_URLCONF.split('.')[0]
        prj_path = '/' + prjname
        meta_prj_path = ".project"
        meta_pydev_path = ".pydevproject"        
        manage_location = 'manage.py'
        base_path = extra_registry[TARGET_PATH_KEY]
         
        if SRC_OPT_KEY in options and options[SRC_OPT_KEY]:
            SRC_FLODER = 'src'
            manage_location = SRC_FLODER+ '/' + manage_location
            prj_path = prj_path + '/' + SRC_FLODER
            base_path = os.path.dirname(base_path)
            
        meta_pydev_path = os.path.join(base_path ,meta_pydev_path)
        meta_prj_path = os.path.join(base_path , meta_prj_path   )        

              
        self.write_config_file("prj_template.xml",meta_prj_path,(prjname,extra_registry[REL_PRJ_KEY], ))
        self.write_config_file("pydev_template.xml",meta_pydev_path,(manage_location,prj_path , python_version, interpreter))
       
        
        
        
    def write_config_file(self , template_name,dest_file_name,filling_data):   
    
        resources_dir = os.path.join(os.path.dirname(__file__), 'resources')   
         
        prj_file = open(os.path.join(resources_dir , template_name), "r")
        prj_out_txt = prj_file.read()
        prj_file.close()
        
        prj_out_txt = prj_out_txt % filling_data
        prj_out_file = open(dest_file_name, 'w')
        prj_out_file.write(prj_out_txt)
        print("Generated "  , os.path.abspath(dest_file_name))
        prj_out_file.close()
