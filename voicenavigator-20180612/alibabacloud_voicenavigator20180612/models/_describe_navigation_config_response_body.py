# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_voicenavigator20180612 import models as main_models
from darabonba.model import DaraModel

class DescribeNavigationConfigResponseBody(DaraModel):
    def __init__(
        self,
        greeting_config: main_models.DescribeNavigationConfigResponseBodyGreetingConfig = None,
        request_id: str = None,
        silence_timeout_config: main_models.DescribeNavigationConfigResponseBodySilenceTimeoutConfig = None,
        unrecognizing_config: main_models.DescribeNavigationConfigResponseBodyUnrecognizingConfig = None,
    ):
        # The greeting configuration.
        self.greeting_config = greeting_config
        # The request ID.
        self.request_id = request_id
        # The silence timeout configuration.
        self.silence_timeout_config = silence_timeout_config
        # The configuration for handling unrecognized input.
        self.unrecognizing_config = unrecognizing_config

    def validate(self):
        if self.greeting_config:
            self.greeting_config.validate()
        if self.silence_timeout_config:
            self.silence_timeout_config.validate()
        if self.unrecognizing_config:
            self.unrecognizing_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.greeting_config is not None:
            result['GreetingConfig'] = self.greeting_config.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.silence_timeout_config is not None:
            result['SilenceTimeoutConfig'] = self.silence_timeout_config.to_map()

        if self.unrecognizing_config is not None:
            result['UnrecognizingConfig'] = self.unrecognizing_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GreetingConfig') is not None:
            temp_model = main_models.DescribeNavigationConfigResponseBodyGreetingConfig()
            self.greeting_config = temp_model.from_map(m.get('GreetingConfig'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SilenceTimeoutConfig') is not None:
            temp_model = main_models.DescribeNavigationConfigResponseBodySilenceTimeoutConfig()
            self.silence_timeout_config = temp_model.from_map(m.get('SilenceTimeoutConfig'))

        if m.get('UnrecognizingConfig') is not None:
            temp_model = main_models.DescribeNavigationConfigResponseBodyUnrecognizingConfig()
            self.unrecognizing_config = temp_model.from_map(m.get('UnrecognizingConfig'))

        return self

class DescribeNavigationConfigResponseBodyUnrecognizingConfig(DaraModel):
    def __init__(
        self,
        final_action: str = None,
        final_action_params: str = None,
        final_prompt: str = None,
        prompt: str = None,
        threshold: int = None,
    ):
        # The action to take when the number of unrecognized inputs reaches the threshold. Valid values: `TransferToAgent`, `TransferToIVR`, `RedirectToPage`, or `HangUp`.
        self.final_action = final_action
        # Parameters for the final action, such as a redirection target.
        self.final_action_params = final_action_params
        # The prompt that is played when the unrecognized input threshold is reached.
        self.final_prompt = final_prompt
        # The prompt that is played when user input is not recognized.
        self.prompt = prompt
        # The maximum number of times the user\\"s input is not recognized.
        self.threshold = threshold

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.final_action is not None:
            result['FinalAction'] = self.final_action

        if self.final_action_params is not None:
            result['FinalActionParams'] = self.final_action_params

        if self.final_prompt is not None:
            result['FinalPrompt'] = self.final_prompt

        if self.prompt is not None:
            result['Prompt'] = self.prompt

        if self.threshold is not None:
            result['Threshold'] = self.threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FinalAction') is not None:
            self.final_action = m.get('FinalAction')

        if m.get('FinalActionParams') is not None:
            self.final_action_params = m.get('FinalActionParams')

        if m.get('FinalPrompt') is not None:
            self.final_prompt = m.get('FinalPrompt')

        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        return self

class DescribeNavigationConfigResponseBodySilenceTimeoutConfig(DaraModel):
    def __init__(
        self,
        final_action: str = None,
        final_action_params: str = None,
        final_prompt: str = None,
        intent_trigger: str = None,
        prompt: str = None,
        source_type: str = None,
        threshold: int = None,
        timeout: int = None,
    ):
        # The action to perform after the final silence prompt is played. Valid values: `TransferToAgent`, `TransferToIVR`, `RedirectToPage`, or `HangUp`.
        self.final_action = final_action
        # Parameters for the final action, such as a redirection target.
        self.final_action_params = final_action_params
        # The prompt that is played when the silence timeout threshold is reached.
        self.final_prompt = final_prompt
        # ""
        self.intent_trigger = intent_trigger
        # The prompt that is played when a silence timeout occurs.
        self.prompt = prompt
        # The source of the configuration.
        self.source_type = source_type
        # The maximum number of silence timeouts.
        self.threshold = threshold
        # The duration of the silence timeout.
        self.timeout = timeout

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.final_action is not None:
            result['FinalAction'] = self.final_action

        if self.final_action_params is not None:
            result['FinalActionParams'] = self.final_action_params

        if self.final_prompt is not None:
            result['FinalPrompt'] = self.final_prompt

        if self.intent_trigger is not None:
            result['IntentTrigger'] = self.intent_trigger

        if self.prompt is not None:
            result['Prompt'] = self.prompt

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.threshold is not None:
            result['Threshold'] = self.threshold

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FinalAction') is not None:
            self.final_action = m.get('FinalAction')

        if m.get('FinalActionParams') is not None:
            self.final_action_params = m.get('FinalActionParams')

        if m.get('FinalPrompt') is not None:
            self.final_prompt = m.get('FinalPrompt')

        if m.get('IntentTrigger') is not None:
            self.intent_trigger = m.get('IntentTrigger')

        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        return self



class DescribeNavigationConfigResponseBodyGreetingConfig(DaraModel):
    def __init__(
        self,
        greeting_words: str = None,
        intent_trigger: str = None,
        source_type: str = None,
    ):
        # The greeting message.
        self.greeting_words = greeting_words
        # The intent trigger.
        self.intent_trigger = intent_trigger
        # The source of the configuration.
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.greeting_words is not None:
            result['GreetingWords'] = self.greeting_words

        if self.intent_trigger is not None:
            result['IntentTrigger'] = self.intent_trigger

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GreetingWords') is not None:
            self.greeting_words = m.get('GreetingWords')

        if m.get('IntentTrigger') is not None:
            self.intent_trigger = m.get('IntentTrigger')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        return self

