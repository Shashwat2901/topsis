from setuptools import setup
setup(
  name = 'mytopsis503',         # How you named your package folder (MyLib)
  packages = ['mytopsis503'],   # Chose the same as "name"
  version = '0.5',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Topsis package to check which model is better',   # Give a short description about your library
  author = 'Shashwat Srivastava',                   # Type in your name
  author_email = 'shashwatsrivastava348@gmail.com',      # Type in your E-Mail
  #url = 'https://github.com/user/reponame',   # Provide either the link to your github or to your website
  #download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['topsis', 'Thapar', 'Data_analytics'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'numpy',
          'pandas'
  
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.7'
  ],
  include_package_data = True,
  entry_points = {
		  "console_scripts" : [
				  "mytopsis503 = mytopsis503.topsis:do_work",
				  ]
			  },
  
)