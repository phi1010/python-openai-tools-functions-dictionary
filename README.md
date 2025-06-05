A simple tool to create the OpenAI tools parameter value from a list of annotated functions, as used in: 
```py

openaitools = OpenAiTools()


class Location(BaseModel):
    city: str = Field(description="english city name")
    country: str = Field(description="english country name")


@openaitools
def get_weather(location: Location):
    "Get current temperature for a given location."
    return dict(temperature="9°C", humidity="20%")


@openaitools
def get_culture(location: Location):
    "Get current culture for a given location."
    return dict(culture="funny")

print(openaitools.tools)


client.responses.create(
    model="gpt-4.1",
    input=input_messages,
    tools=openaitools.tools,
)
```
Can be used with https://platform.openai.com/docs/guides/function-calling?api-mode=responses&lang=python
