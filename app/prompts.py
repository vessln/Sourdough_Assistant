from jinja2 import Environment, FileSystemLoader
import os

# Load Jinja template from prompts folder
env = Environment(loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), '..', 'prompts')))
TEMPLATE = env.get_template('template.jinja')


def render_prompt(history: str, user_input: str, model_name: str = None) -> str:
    """
    Render the system prompt with optional history and user input.
    """
    return TEMPLATE.render(history=history, user_input=user_input)