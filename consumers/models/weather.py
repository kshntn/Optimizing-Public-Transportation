"""Contains functionality related to Weather"""
import logging


logger = logging.getLogger(__name__)


class Weather:
    """Defines the Weather model"""

    def __init__(self):
        """Creates the weather model"""
        self.temperature = 70.0
        self.status = "sunny"

    def process_message(self, message):
        """Handles incoming weather data"""
        logger.info("weather process_message is incomplete - skipping")
        #
        #
        # TODO: Process incoming weather messages. Set the temperature and status.
        #
        #
        print("topic", message.topic())
        print("message_value", message.value())
        value = message.value()
        self.temperature = value["temperature"]
        self.status = value["status"]
        logger.debug(
            "weather is now %sf and %s", self.temperature, self.status.replace("_", " ")
        )
