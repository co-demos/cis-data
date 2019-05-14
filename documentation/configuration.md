(Work in progress)

Notes for the configuration of various elements in `config_app`: the examples or pre-existing configurations should be sufficient to understand the basic arguments and build your configuration by copy/pasting the various elements; this file only presents things I found non-trivial to grasp, feel free to add on it!

(Notes pour la configuration des éléments de `config_app` : les exemples ou configurations pré-existantes devraient suffire pour comprendre les arguments de base et construire une configuration par copier/coller et adaptation. Je détaille ici quelques points que j’ai trouvés moins évidents à saisir, enrichissements bienvenus !)

# Footer
- `active_columns` should correspond to the columns with `is_visible` set to `True`.

# Routes
- :warning: do not use `is_activated : False` to de-activate a route: see [issue #88](https://github.com/co-demos/ApiViz/issues/88), it would remain active! Comment the whole route instead, or cut it from the file (even more so if it contains critical pages, such as login, configuration, debug or setup pages)
