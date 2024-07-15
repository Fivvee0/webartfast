import argparse
import os
import zipfile

def main():
    parser = argparse.ArgumentParser(description='Tool for creating web apps.')
    subparsers = parser.add_subparsers(dest='command')

    create_parser = subparsers.add_parser('create', help='Creates a new web app.')
    create_parser.add_argument('--name', required=True, help='Name of app.')
    create_parser.add_argument('--dir', required=True, help='Directory.')

    args = parser.parse_args()

    if args.command == 'create':
        create_website(args.name, args.dir)

def create_website(name, output_dir):
    app_dir = os.path.join(output_dir, name)
    os.makedirs(app_dir, exist_ok=True)

    template_zip_path = 'template.zip'

    with zipfile.ZipFile(template_zip_path, 'r') as zip_ref:
        zip_ref.extractall(app_dir)

    print(f'Utworzono aplikację webową o nazwie: {name} w katalogu: {app_dir} z plikami z {template_zip_path}.')

if __name__ == '__main__':
    main()