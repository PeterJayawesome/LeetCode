import re
def fuzzyfinder(user_input, collection):
        suggestions = []
        pattern = '.*?'.join(user_input)    # Converts 'djm' to 'd.*?j.*?m'
        regex = re.compile(pattern)         # Compiles a regex.
        for item in collection:
            match = regex.search(item)      # Checks if the current item matches the regex.
            if match:
                suggestions.append((len(match.group()), match.start(), item))
        return [x for _, _, x in sorted(suggestions)]

collection = ['django_migrations.py',
                'django_admin_log.py',
                'main_generator.py',
                'migrations.py',
                'api_user.doc',
                'user_group.doc',
                'accounts.txt',
                ]
print(fuzzyfinder('user', collection))
# ['user_group.doc', 'api_user.doc']
 
print(fuzzyfinder('mig', collection))
# ['migrations.py', 'django_migrations.py', 'main_generator.py', 'django_admin_log.py']