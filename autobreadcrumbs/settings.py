# -*- coding: utf-8 -*-
"""
Settings
========

"""
#: Initial project crumbs where you can add initial crumbs for your project
#: views.
AUTOBREADCRUMBS_TITLES = {}

#: Optional project level crumbs file, this have to be a correct Python path to
#: a crumb module.
AUTOBREADCRUMBS_ROOT_CRUMB = None

#: Template string for crumb item in tag ``{% autobreadcrumbs_links %}``
AUTOBREADCRUMBS_HTML_LINK = u'<a href="{link}">{title}</a>'

#: Template string for separator item in tag ``{% autobreadcrumbs_links %}``
AUTOBREADCRUMBS_HTML_SEPARATOR = u' &gt; '

#: Template string for crumb without href and for model title ``{% autobreadcrumbs_links %}``
AUTOBREADCRUMBS_HTML_WITHOUT_LINK = u'<a href="#">{title}</a>'

#: Cut title filed of Model for ``{% autobreadcrumbs_links %}``
AUTOBREADCRUMBS_TITLE_LENGTH = 20

#: Is last crumbs is link
AUTOBREADCRUMBS_LAST_IS_LINK = False
