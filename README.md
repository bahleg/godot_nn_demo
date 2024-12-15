# godot_nn_demo

This is a demo sowing how to integrate Godot with teenygrad. It's working with `Godot 4.3` and `pyodide 0.26.3`.

To run it use the following steps:
1. Import teenygrad git submodule:
```
cd nn_demo/export
git submodule update
```
2. Run make_html.py:
```
python make_html.py
```
This will create an `filled_template.html` file that can be used for shell in Godot html export.

3. Load godot project, select `filled_template.html` as HTML shell in the export page and perform export.

[The demo can be found here](https://bahleg.itch.io/nn-godot)
