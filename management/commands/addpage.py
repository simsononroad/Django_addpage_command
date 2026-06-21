from pathlib import Path
from django.core.management.base import BaseCommand, CommandError
from jinja2 import Environment, FileSystemLoader
import os



class Command(BaseCommand):
    
    def add_arguments(self, parser):
        parser.add_argument('path', help="Give the path for the url! (If you just write that the html page will be the same and in the view.py's file)")
        parser.add_argument('--viewname', default="nogiven", help="Give the function name in view.py file")
        parser.add_argument('--htmlname', default="nogiven", help="Give the name of th html page")
    
    def remove_line_by_content(filename, line_to_remove):
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        with open(filename, 'w') as file:
            for line in lines:
                # Strip newline for accurate comparison
                if line.strip('\n') != line_to_remove:
                    file.write(line)
    
    def handle(self, *args, **options):
        path = options["path"]
        viewname = options["viewname"]
        htmlname = options["htmlname"]
        script_dir = Path(__file__).resolve().parent
        file_path = os.path.join(script_dir, '..', '..', 'urls.py')
        
        if path[-1] != "/":
            raise CommandError("You need to place a '/' at the end of the path")
    
        if viewname == "nogiven": viewname = path[:-1]
        if htmlname == "nogiven": htmlname = path[:-1]
        if ".html" not in htmlname: htmlname = f"{htmlname}.html"
        
        Command.remove_line_by_content(file_path, "]")
        Command.urls_append(path, viewname, htmlname)
        Command.create_html(htmlname)
        Command.add_view(viewname, htmlname)
        self.stdout.write(self.style.SUCCESS("Everything went off without a hitch!"))
    
    

    def urls_append(path, viewname, htmlname):
        script_dir = Path(__file__).resolve().parent.parent
        a = os.path.join(script_dir, "temps")
        env = Environment(loader=FileSystemLoader(a))
        
        url_temp = env.get_template("urls_temp.jinja")
        url_cont = url_temp.render(path=path, viewname=viewname)
        
        file_dir = Path(__file__).resolve().parent.parent.parent
        file_dir = os.path.join(file_dir, "urls.py")
    
        with open(file_dir, "a") as f:
            f.write(url_cont)
        
        
        #if not os.path.isfile(path):
        #    os.mknod(path)
    
    def create_html(htmlname):
        file_dir = Path(__file__).resolve().parent.parent.parent
        file_dir = os.path.join(file_dir, f"templates/{htmlname}")
        os.mknod(file_dir)
    
    def add_view(viewname, htmlname):
        main_dir = Path(__file__).resolve().parent.parent.parent
        view_file_path = os.path.join(main_dir, "views.py")
        
        script_dir = Path(__file__).resolve().parent.parent
        a = os.path.join(script_dir, "temps")
        env = Environment(loader=FileSystemLoader(a))
        
        view_temp = env.get_template("view_temp.jinja")
        view_cont = view_temp.render(viewname=viewname, htmlname=htmlname)
        
        with open(view_file_path, "a") as f:
            f.write(view_cont)