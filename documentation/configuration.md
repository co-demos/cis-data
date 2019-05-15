(Work in progress/en cours de rédaction)

Notes for the configuration of various elements in `config_app`: the examples or pre-existing configurations should be sufficient to understand the basic arguments and build your configuration by copy/pasting the various elements.

(Notes pour la configuration des éléments de `config_app` : les exemples ou configurations pré-existantes devraient suffire pour comprendre les arguments de base et construire une configuration par copier/coller et adaptation.)

# Steps/Étapes suivies + Final state/État final (CIS, mid-May 2019)
## Data endpoints
- add the following endpoints for CIS:
  - cis_data_API_filters
    - :arrow_right: filters values are to be matched with corresponding columns (from Solidata) in order for the interface to behave properly
  - cis_data_API_list
  - cis_data_API_map
  - cis_data_API_detail
  - cis_data_API_stats
  - :arrow_right: these endpoint share the same URL for now, but they could have individual URL to get only necessary information depending on use case: only coordinates for map purposes, …)
- other new endpoints are related to user management and would work with a TokTok instance (or another system?) for authentication purposes

## Footer
- replace links and titles by CIS content

## Global
- replace various items, translations,… by CIS content

## Navbar
- add CIS navbar similar to previous CIS-front design
- add dropdown menus to access sub-pages

## Routes
- add each of the pages/routes from CIS-front
  - add template URLs
  - add external scripts
  - update `content_fields` to match columns titles from Solidata with fields in components `ProjectCard` and `DynamicDetail`
- update/adapt search pages to work with CIS data

## Socials
- replace with CIS values (from CIS-front)

## Styles
- add proper colors, in reference to [previous stylesheet](https://github.com/entrepreneur-interet-general/CIS-front/blob/master/cis/app/frontend/styles/cis-colors.scss)
- add images (for default backgrounds)

# Some tips/Astuces
## Footer
- `active_columns` should correspond to the columns with `is_visible` set to `True`.
- "Social" buttons (ie. Facebook, Twitter, Github…) are automatically added at the end of the last block.

## Routes
- :warning: do not use `is_activated : False` to de-activate a route: see [issue #88](https://github.com/co-demos/ApiViz/issues/88), it would remain active! Comment the whole route instead, or cut it from the file (even more so if it contains critical pages, such as login, configuration, debug or setup pages).
- to test the proper inclusion of HTML templates:
  - write or copy/paste the HTML into the component `DynamicStaticTest`
  - :warning: the templating engine of Vue.js is stricter regarding HTML syntax (missing </li> for example)
  - change the `dynamic_template` value to `DynamicStaticTest`
  - once done, copy/paste the HTML back to the dedicated file or repository
  - if loaded from GitHub, the HTML pages are available quickly (a minute or so)
- to test external scripts:
  - replace the `ext_script_url` by a static URL for a script in the folder `static` of your ApiViz instance (such as `static/test_script.js`)
  - debug, update, do what is necessary
  - once done, copy/paste the JS back to the dedicated file or repository
  - if loaded from GitHub, the scripts may not appear/load immediately (a minute or so for a new file, 10 min or so for an update to an existing file)
