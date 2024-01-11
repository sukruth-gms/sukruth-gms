import csv
import pkg_resources

def get_devops_modules():
    devops_keywords = ['ansible', 'docker', 'kubernetes', 'terraform', 'jenkins', 'git', 'chef', 'puppet']

    installed_modules = []
    for dist in pkg_resources.working_set:
        for keyword in devops_keywords:
            if keyword in dist.key.lower():
                installed_modules.append({'Module': dist.key, 'Version': dist.version})

    return installed_modules

def export_to_csv(data, filename='devops_modules.csv'):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['Module', 'Version']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(data)

if __name__ == "__main__":
    devops_modules = get_devops_modules()
    export_to_csv(devops_modules)
    print(f'DevOps modules exported to devops_modules.csv')
