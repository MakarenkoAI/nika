This is an agent added as an example to show how to add new python agents to the system.  

**Action class:**

`action_show_weather`

**Parameters:**

1. `message node` - an element of `concept_message` and `concept_message_about_weather`;

**Workflow:**

* The agent extracts an entity from the message and send request about the entity using an open weather API. 
* After receiving a response the agent processes it and generates a phrase including weather in the entity.

The letter agent rule:
<img src="../images/lr_message_about_weather.png"></img>

The letter agent template phrase:
<img src="../images/concept_phrase_about_weather.png"></img>

### Example

Example of an input structure:

<img src="../images/ShowWeatherAgentExample.png"></img>

To test you can use message like `Какая погода в Минске?`

### Result

Possible result codes:

* `SC_RESULT_OK` - agent successfully found elements and generate phrase;
* `SC_RESULT_ERROR`- `message node` or `entity` is not found.
