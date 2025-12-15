import marimo

__generated_with = "0.15.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pathlib
    return mo, pathlib


@app.cell
def _(pathlib):
    out_plot_path  = pathlib.Path('plots').absolute()
    pic_list =sorted([sp for sp in out_plot_path.glob('*.png')])

    return (pic_list,)


@app.cell
def _(mo, pic_list):
    slider = mo.ui.slider(start=0, stop=len(pic_list)-1, show_value=True, full_width= True,label="Slider", value=3)
    return (slider,)


@app.cell
def _():
    #mo.hstack([slider, mo.md(f"Has value: {slider.value}")])
    return


@app.cell
def _(mo, pic_list, slider):
    mo.vstack([slider, mo.image(src=pic_list[slider.value], width="360px", height="360px", rounded=True)])

    return


if __name__ == "__main__":
    app.run()
