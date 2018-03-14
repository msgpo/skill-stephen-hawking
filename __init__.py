from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler
from mycroft.tts.espeak_tts import ESpeak


class StephenHawkingSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.espeak = ESpeak("english-us", "m1")

    def hawking_speak(self, utterance):
        self.espeak.execute(utterance)

    @intent_handler(IntentBuilder("StephenHawkingQuote").require(
        'StephenHawking').require(
        'quote'))
    def handle_quote(self, message):
        utterance = self.dialog_renderer.render("quote", {})
        self.hawking_speak(utterance)

    @intent_handler(IntentBuilder("StephenHawkingbirth").require(
        'StephenHawking').require(
        'birth'))
    def handle_birth(self, message):
        self.speak_dialog('birth')

    @intent_handler(IntentBuilder("StephenHawkingQuote").require(
        'StephenHawking').require(
        'death'))
    def handle_death(self, message):
        self.speak_dialog('death')


def create_skill():
    return StephenHawkingSkill()

