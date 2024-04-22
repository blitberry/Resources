import pkg_resources
import sys

directory = sys.argv[1]
pkg_resources.working_set.add_entry(directory)

for dist in pkg_resources.working_set:
    if directory in dist.location:
        print(f"{dist.project_name}=={dist.version}")
