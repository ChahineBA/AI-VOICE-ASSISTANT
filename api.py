import enum
from typing import Annotated
from livekit.agents import llm
import logging

# Set up a logger for temperature control with an INFO log level
logger = logging.getLogger("temperature-control")
logger.setLevel(logging.INFO)

# Define a Zone enumeration for different areas in a building
class Zone(enum.Enum):
    LIVING_ROOM = "living_room"
    BEDROOM = "bedroom"
    KITCHEN = "kitchen"
    BATHROOM = "bathroom"
    OFFICE = "office"

# Define a custom FunctionContext for handling temperature control logic
class AssistantFnc(llm.FunctionContext):
    def __init__(self) -> None:
        super().__init__()
        
        # Initialize a dictionary to store default temperatures for each zone
        self._temperature = {
            Zone.LIVING_ROOM: 22,
            Zone.BEDROOM: 20,
            Zone.KITCHEN: 24,
            Zone.BATHROOM: 23,
            Zone.OFFICE: 21
        }

    # Define a callable function to get the temperature of a specific zone
    @llm.ai_callable(description="Get the temperature in a specific room")
    def get_temperature(
        self, 
        zone: Annotated[Zone, llm.TypeInfo(description="The specific zone")]
    ):
        # Log the action and zone for tracking
        logger.info("get temp - zone %s", zone)
        # Retrieve the temperature for the specified zone
        temp = self._temperature[Zone(zone)]
        # Return a formatted string with the temperature information
        return f"The Temperature in the {zone} is {temp}C"
    
    # Define a callable function to set the temperature of a specific zone
    @llm.ai_callable(description="Set the temperature in a specific room")
    def set_temperature(
        self, 
        zone: Annotated[Zone, llm.TypeInfo(description="The specific zone")],
        temp: Annotated[int, llm.TypeInfo(description="The temperature to set")]
    ):
        # Log the action, zone, and temperature for tracking
        logger.info("set temp - zone: %s temp: %s", zone, temp)
        # Update the temperature for the specified zone
        self._temperature[Zone(zone)] = temp
        # Return a formatted string confirming the updated temperature
        return f"The Temperature in the {zone} is now {temp}C"
