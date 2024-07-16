import argparse
import os
import shutil

def main():
    parser = argparse.ArgumentParser(description='Tool for creating web apps.')
    subparsers = parser.add_subparsers(dest='command')

    create_parser = subparsers.add_parser('create', help='Creates a new web app.')
    create_parser.add_argument('--name', required=True, help='Name of app.')
    create_parser.add_argument('--dir', required=True, help='Directory.')

    args = parser.parse_args()

    if args.command == 'create':
        script_dir = os.path.dirname(os.path.abspath(__file__))
        template_dir = os.path.join(script_dir, 'template')

        create_website(args.name, args.dir, template_dir)

def create_website(name, output_dir, template_dir):
    app_dir = os.path.join(output_dir, name)
    os.makedirs(app_dir, exist_ok=True)

    shutil.copytree(template_dir, app_dir, dirs_exist_ok=True)

    print(f'Created Web App: {name} in directory: {app_dir}.')

if __name__ == '__main__':
    main()