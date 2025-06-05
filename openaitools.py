import inspect
from pydantic import BaseModel, Field

class OpenAiTools:
    def __init__(self):
        self.tools = []

    def __call__(self, f):
        self.register_tool_callback(f)
        return f

    def register_tool_callback(self, f):
        name = f.__name__
        # print(name)
        signature = inspect.signature(f)
        # print(signature)
        properties = dict()
        for pname, param in signature.parameters.items():
            # print(name,param)
            annotation = param.annotation
            # print(annotation)
            if not issubclass(annotation, BaseModel):
                raise Exception(
                    "You must annotate parameters with classes derived from pydantic.BaseModel"
                )
            schema = annotation.model_json_schema()
            # print(schema)
            properties[pname] = schema
        self.tools.append(
            {
                "type": "function",
                "name": name,
                "description": "Get current temperature for a given location.",
                "parameters": {
                    "type": "object",
                    "properties": properties,
                    "required": list(properties),
                    "additionalProperties": False,
                },
            }
        )
        print()


openaitools = OpenAiTools()


class Location(BaseModel):
    city: str = Field(description="english city name")
    country: str = Field(description="english country name")


@openaitools
def get_weather(location: Location):
    return dict(temperature="9°C", humidity="20%")


@openaitools
def get_culture(location: Location):
    return dict(type="funny")

print(openaitools.tools)
