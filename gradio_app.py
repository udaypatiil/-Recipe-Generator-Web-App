import gradio as gr

def identify_ingredients(image_path):
    return "Hear are the recipe"


demo = gr.Interface(
    fn=identify_ingredients,
    inputs=gr.Image(),
    outputs=gr.Markdown(),
    title="Recipe Generator",
    description="Upload an image with ingredients",
    flagging_mode="never"
)

demo.launch(debug=True)