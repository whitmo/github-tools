"""
:Description: PasteScript Template to generate a GitHub hosted python package.


Let you set the package name, a one line description, the Licence (support
GPL, LGPL, AGPL and BSD - GPLv3 by default) and the author name, email and
organisation variables::

    paster create -t gh_package <project name>


The result::

    <project name>/
        docs/
            
            _static
            _templates/
            conf.py
            index.rst
        <package name>/
            __init__.py
        .gitignore
        bootstrap.py
        LICENCE
        MANIFEST.in
        pavement.py
        README.rst

* <project name>/pavement.py is the paver configuration file. All the setuptools
  tasks are available with paver. Paver make the creation of of new task easy.
  See `paver documentation <http://www.blueskyonmars.com/projects/paver/>`_
  for more details::

    paver paverdocs
  
* <project name>/docs/ will contains your documentation source. conf.py
  is Sphinx' configuration file.
  Check `Sphinx' documentation <http://sphinx.pocoo.org/>`_ for more details.
  
.. note::
    The version number, the project name and author name(s) are set in 
    ``pavement.py`` and shared with ``docs/conf.py``.
    
    However licence and copyright information are hard coded into ``LICENCE``,
    ``pavement.py``, ``docs/conf`` and ``<package>/__init__.py``.
    
"""

import os
from paste.script.templates import Template
from github.tools.gh_pages import GitHubProject


OPTIONAL_IMPORT = """from github.tools.task import *
"""

VIRTUAL_PACKAGES_TO_INSTALL = """'github-tools',
"""

DEVELOPMENT_HELP = """


Help and development
====================

If you'd like to help out, you can fork the project
at %(project_url)s and report any bugs 
at %(issue_url)s.


"""


class GithubTemplate(Template):
    """Paver template for a GitHub hosted Python package."""
    _template_dir = 'tmpl/gh'
    summary = ("A basic layout for project hosted on GitHub "
        "and managed with Paver")
    use_cheetah = True
    required_templates = ['paver-templates#paver_package']
    
    def pre(self, command, output_dir, vars):
        """
        Set extra template variables:
        
        * "year", current year.
        * "gitignore", set to ".gitignore".
        * "licence_body", licence notice of the package.
        * "gpl_type", for gpl licences
        """
        vars['gitignore'] = '.gitignore'
<<<<<<< HEAD:github/tools/template.py
        licence = vars.get('licence')
        vars['licence_body'] = ''
        vars['gpl_type'] = ''
        vars['gpl_version'] = ''
        if licence:
            if licence == 'BSD':
                licence_tmpl = BSD
            elif licence == 'LGPLv2':
                vars['gpl_type'] = ' Lesser'
                vars['gpl_version'] = '2'
                vars['licence'] = 'LGPLv2'
                licence_tmpl = GPL
            elif licence == 'LGPLv3':
                vars['gpl_type'] = ' Lesser'
                vars['gpl_version'] = '3'
                vars['licence'] = 'LGPLv3'
                licence_tmpl = GPL
            elif licence == 'AGPLv3':
                vars['gpl_type'] = ' Affero'
                vars['gpl_version'] = '3'
                vars['licence'] = 'AGPLv3'
                licence_tmpl = GPL
            elif licence == 'GPLv2':
                vars['gpl_type'] = ''
                vars['gpl_version'] = '2'
                vars['licence'] = 'GPLv2'
                licence_tmpl = GPL
            else:
                vars['gpl_type'] = ''
                vars['gpl_version'] = '3'
                vars['licence'] = 'GPL'
                licence_tmpl = GPL
            vars['licence_body'] = (LICENCE_HEADER + licence_tmpl) % vars


class AltGithubTemplate(GithubTemplate):
    """
    An alternate spelling for paver enabled github project
    """
    _template_dir = 'tmpl/gh_alt'
=======
        try :
            project = GitHubProject(name=vars['project'])
            vars['project_url'] = project.url.http
            vars['issue_url'] = project.url.issue
        except AttributeError:
            vars['project_url'] = (
                'http://github.com/<GITHUB USER NAME>/%s' % vars['project']
                ) 
            vars['issue_url'] = (
                'http://github.com/<GITHUB USER NAME>/%s/issues' % vars['project']
                )
            
        
    def post(self, command, output_dir, vars):
        """
        Add extra settings to pavement.py
        """
        # Edit pavement.py
        pavement_py = os.path.join(output_dir, 'pavement.py')
        command.insert_into_file(
            filename=pavement_py,
            marker_name='Optional import',
            text=OPTIONAL_IMPORT,
            indent=True
            )
        command.insert_into_file(
            filename=pavement_py,
            marker_name='Virtualenv packages to install',
            text=VIRTUAL_PACKAGES_TO_INSTALL,
            indent=True
            )
        
        # Append README.rst with development info
        readme = open(os.path.join(output_dir, 'README.rst'), 'a')
        try:
            readme.write(DEVELOPMENT_HELP % vars)
        finally:
            readme.close()
>>>>>>> 055e5379ad96cac9165b39d7202c38dfc69740e4:src/github/tools/template.py
