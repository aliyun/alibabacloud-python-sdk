# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class AssociateChatbotInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        chatbot_instance_id: str = None,
        chatbot_name: str = None,
    ):
        self.instance_id = instance_id
        self.chatbot_instance_id = chatbot_instance_id
        self.chatbot_name = chatbot_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.chatbot_instance_id is not None:
            result['ChatbotInstanceId'] = self.chatbot_instance_id
        if self.chatbot_name is not None:
            result['ChatbotName'] = self.chatbot_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ChatbotInstanceId') is not None:
            self.chatbot_instance_id = m.get('ChatbotInstanceId')
        if m.get('ChatbotName') is not None:
            self.chatbot_name = m.get('ChatbotName')
        return self


class AssociateChatbotInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AssociateChatbotInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AssociateChatbotInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AssociateChatbotInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AuditTTSVoiceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        voice: str = None,
        text: str = None,
        speech_rate: str = None,
        volume: str = None,
    ):
        self.instance_id = instance_id
        self.voice = voice
        self.text = text
        self.speech_rate = speech_rate
        self.volume = volume

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.voice is not None:
            result['Voice'] = self.voice
        if self.text is not None:
            result['Text'] = self.text
        if self.speech_rate is not None:
            result['SpeechRate'] = self.speech_rate
        if self.volume is not None:
            result['Volume'] = self.volume
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Voice') is not None:
            self.voice = m.get('Voice')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('SpeechRate') is not None:
            self.speech_rate = m.get('SpeechRate')
        if m.get('Volume') is not None:
            self.volume = m.get('Volume')
        return self


class AuditTTSVoiceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        audition_url: str = None,
    ):
        self.request_id = request_id
        self.audition_url = audition_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.audition_url is not None:
            result['AuditionUrl'] = self.audition_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AuditionUrl') is not None:
            self.audition_url = m.get('AuditionUrl')
        return self


class AuditTTSVoiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AuditTTSVoiceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AuditTTSVoiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BeginDialogueRequest(TeaModel):
    def __init__(
        self,
        called_number: str = None,
        calling_number: str = None,
        conversation_id: str = None,
        initial_context: str = None,
        instance_id: str = None,
    ):
        self.called_number = called_number
        self.calling_number = calling_number
        self.conversation_id = conversation_id
        self.initial_context = initial_context
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.called_number is not None:
            result['CalledNumber'] = self.called_number
        if self.calling_number is not None:
            result['CallingNumber'] = self.calling_number
        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id
        if self.initial_context is not None:
            result['InitialContext'] = self.initial_context
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')
        if m.get('CallingNumber') is not None:
            self.calling_number = m.get('CallingNumber')
        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')
        if m.get('InitialContext') is not None:
            self.initial_context = m.get('InitialContext')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class BeginDialogueResponseBody(TeaModel):
    def __init__(
        self,
        action: str = None,
        interruptible: bool = None,
        request_id: str = None,
        action_params: str = None,
        text_response: str = None,
    ):
        self.action = action
        self.interruptible = interruptible
        self.request_id = request_id
        self.action_params = action_params
        self.text_response = text_response

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.interruptible is not None:
            result['Interruptible'] = self.interruptible
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.action_params is not None:
            result['ActionParams'] = self.action_params
        if self.text_response is not None:
            result['TextResponse'] = self.text_response
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Interruptible') is not None:
            self.interruptible = m.get('Interruptible')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ActionParams') is not None:
            self.action_params = m.get('ActionParams')
        if m.get('TextResponse') is not None:
            self.text_response = m.get('TextResponse')
        return self


class BeginDialogueResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BeginDialogueResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = BeginDialogueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CollectedNumberRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        conversation_id: str = None,
        number: str = None,
    ):
        self.instance_id = instance_id
        self.conversation_id = conversation_id
        self.number = number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id
        if self.number is not None:
            result['Number'] = self.number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        return self


class CollectedNumberResponseBody(TeaModel):
    def __init__(
        self,
        action: str = None,
        interruptible: bool = None,
        request_id: str = None,
        action_params: str = None,
        text_response: str = None,
    ):
        self.action = action
        self.interruptible = interruptible
        self.request_id = request_id
        self.action_params = action_params
        self.text_response = text_response

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.interruptible is not None:
            result['Interruptible'] = self.interruptible
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.action_params is not None:
            result['ActionParams'] = self.action_params
        if self.text_response is not None:
            result['TextResponse'] = self.text_response
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Interruptible') is not None:
            self.interruptible = m.get('Interruptible')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ActionParams') is not None:
            self.action_params = m.get('ActionParams')
        if m.get('TextResponse') is not None:
            self.text_response = m.get('TextResponse')
        return self


class CollectedNumberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CollectedNumberResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CollectedNumberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateInstanceRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        description: str = None,
        concurrency: int = None,
        chatbot_instance_id: str = None,
        nlu_service_type: str = None,
        chatbot_name: str = None,
    ):
        self.name = name
        self.description = description
        self.concurrency = concurrency
        self.chatbot_instance_id = chatbot_instance_id
        self.nlu_service_type = nlu_service_type
        self.chatbot_name = chatbot_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.concurrency is not None:
            result['Concurrency'] = self.concurrency
        if self.chatbot_instance_id is not None:
            result['ChatbotInstanceId'] = self.chatbot_instance_id
        if self.nlu_service_type is not None:
            result['NluServiceType'] = self.nlu_service_type
        if self.chatbot_name is not None:
            result['ChatbotName'] = self.chatbot_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Concurrency') is not None:
            self.concurrency = m.get('Concurrency')
        if m.get('ChatbotInstanceId') is not None:
            self.chatbot_instance_id = m.get('ChatbotInstanceId')
        if m.get('NluServiceType') is not None:
            self.nlu_service_type = m.get('NluServiceType')
        if m.get('ChatbotName') is not None:
            self.chatbot_name = m.get('ChatbotName')
        return self


class CreateInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        instance_id: str = None,
    ):
        self.request_id = request_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class CreateInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DebugBeginDialogueRequest(TeaModel):
    def __init__(
        self,
        called_number: str = None,
        calling_number: str = None,
        conversation_id: str = None,
        initial_context: str = None,
        instance_id: str = None,
    ):
        self.called_number = called_number
        self.calling_number = calling_number
        self.conversation_id = conversation_id
        self.initial_context = initial_context
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.called_number is not None:
            result['CalledNumber'] = self.called_number
        if self.calling_number is not None:
            result['CallingNumber'] = self.calling_number
        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id
        if self.initial_context is not None:
            result['InitialContext'] = self.initial_context
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')
        if m.get('CallingNumber') is not None:
            self.calling_number = m.get('CallingNumber')
        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')
        if m.get('InitialContext') is not None:
            self.initial_context = m.get('InitialContext')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DebugBeginDialogueResponseBody(TeaModel):
    def __init__(
        self,
        action: str = None,
        interruptible: bool = None,
        request_id: str = None,
        action_params: str = None,
        text_response: str = None,
    ):
        self.action = action
        self.interruptible = interruptible
        self.request_id = request_id
        self.action_params = action_params
        self.text_response = text_response

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.interruptible is not None:
            result['Interruptible'] = self.interruptible
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.action_params is not None:
            result['ActionParams'] = self.action_params
        if self.text_response is not None:
            result['TextResponse'] = self.text_response
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Interruptible') is not None:
            self.interruptible = m.get('Interruptible')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ActionParams') is not None:
            self.action_params = m.get('ActionParams')
        if m.get('TextResponse') is not None:
            self.text_response = m.get('TextResponse')
        return self


class DebugBeginDialogueResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DebugBeginDialogueResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DebugBeginDialogueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DebugCollectedNumberRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        conversation_id: str = None,
        number: str = None,
    ):
        self.instance_id = instance_id
        self.conversation_id = conversation_id
        self.number = number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id
        if self.number is not None:
            result['Number'] = self.number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        return self


class DebugCollectedNumberResponseBody(TeaModel):
    def __init__(
        self,
        action: str = None,
        interruptible: bool = None,
        request_id: str = None,
        action_params: str = None,
        text_response: str = None,
    ):
        self.action = action
        self.interruptible = interruptible
        self.request_id = request_id
        self.action_params = action_params
        self.text_response = text_response

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.interruptible is not None:
            result['Interruptible'] = self.interruptible
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.action_params is not None:
            result['ActionParams'] = self.action_params
        if self.text_response is not None:
            result['TextResponse'] = self.text_response
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Interruptible') is not None:
            self.interruptible = m.get('Interruptible')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ActionParams') is not None:
            self.action_params = m.get('ActionParams')
        if m.get('TextResponse') is not None:
            self.text_response = m.get('TextResponse')
        return self


class DebugCollectedNumberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DebugCollectedNumberResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DebugCollectedNumberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DebugDialogueRequest(TeaModel):
    def __init__(
        self,
        conversation_id: str = None,
        additional_context: str = None,
        instance_id: str = None,
        utterance: str = None,
    ):
        self.conversation_id = conversation_id
        self.additional_context = additional_context
        self.instance_id = instance_id
        self.utterance = utterance

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id
        if self.additional_context is not None:
            result['AdditionalContext'] = self.additional_context
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.utterance is not None:
            result['Utterance'] = self.utterance
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')
        if m.get('AdditionalContext') is not None:
            self.additional_context = m.get('AdditionalContext')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Utterance') is not None:
            self.utterance = m.get('Utterance')
        return self


class DebugDialogueResponseBody(TeaModel):
    def __init__(
        self,
        action: str = None,
        interruptible: bool = None,
        request_id: str = None,
        action_params: str = None,
        text_response: str = None,
    ):
        self.action = action
        self.interruptible = interruptible
        self.request_id = request_id
        self.action_params = action_params
        self.text_response = text_response

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.interruptible is not None:
            result['Interruptible'] = self.interruptible
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.action_params is not None:
            result['ActionParams'] = self.action_params
        if self.text_response is not None:
            result['TextResponse'] = self.text_response
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Interruptible') is not None:
            self.interruptible = m.get('Interruptible')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ActionParams') is not None:
            self.action_params = m.get('ActionParams')
        if m.get('TextResponse') is not None:
            self.text_response = m.get('TextResponse')
        return self


class DebugDialogueResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DebugDialogueResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DebugDialogueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DeleteInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeConversationRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        conversation_id: str = None,
    ):
        self.instance_id = instance_id
        self.conversation_id = conversation_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')
        return self


class DescribeConversationResponseBody(TeaModel):
    def __init__(
        self,
        effective_answer_count: int = None,
        conversation_id: str = None,
        transferred_to_agent: bool = None,
        end_time: int = None,
        request_id: str = None,
        begin_time: int = None,
        skill_group_id: str = None,
        calling_number: str = None,
        user_utterance_count: int = None,
    ):
        self.effective_answer_count = effective_answer_count
        self.conversation_id = conversation_id
        self.transferred_to_agent = transferred_to_agent
        self.end_time = end_time
        self.request_id = request_id
        self.begin_time = begin_time
        self.skill_group_id = skill_group_id
        self.calling_number = calling_number
        self.user_utterance_count = user_utterance_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.effective_answer_count is not None:
            result['EffectiveAnswerCount'] = self.effective_answer_count
        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id
        if self.transferred_to_agent is not None:
            result['TransferredToAgent'] = self.transferred_to_agent
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.skill_group_id is not None:
            result['SkillGroupId'] = self.skill_group_id
        if self.calling_number is not None:
            result['CallingNumber'] = self.calling_number
        if self.user_utterance_count is not None:
            result['UserUtteranceCount'] = self.user_utterance_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EffectiveAnswerCount') is not None:
            self.effective_answer_count = m.get('EffectiveAnswerCount')
        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')
        if m.get('TransferredToAgent') is not None:
            self.transferred_to_agent = m.get('TransferredToAgent')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('SkillGroupId') is not None:
            self.skill_group_id = m.get('SkillGroupId')
        if m.get('CallingNumber') is not None:
            self.calling_number = m.get('CallingNumber')
        if m.get('UserUtteranceCount') is not None:
            self.user_utterance_count = m.get('UserUtteranceCount')
        return self


class DescribeConversationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeConversationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeConversationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeConversationContextRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        conversation_id: str = None,
    ):
        self.instance_id = instance_id
        self.conversation_id = conversation_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')
        return self


class DescribeConversationContextResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        conversation_context: str = None,
    ):
        self.request_id = request_id
        self.conversation_context = conversation_context

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.conversation_context is not None:
            result['ConversationContext'] = self.conversation_context
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ConversationContext') is not None:
            self.conversation_context = m.get('ConversationContext')
        return self


class DescribeConversationContextResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeConversationContextResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeConversationContextResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeExportProgressRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        export_task_id: str = None,
    ):
        self.instance_id = instance_id
        self.export_task_id = export_task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.export_task_id is not None:
            result['ExportTaskId'] = self.export_task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ExportTaskId') is not None:
            self.export_task_id = m.get('ExportTaskId')
        return self


class DescribeExportProgressResponseBody(TeaModel):
    def __init__(
        self,
        status: str = None,
        request_id: str = None,
        file_http_url: str = None,
    ):
        self.status = status
        self.request_id = request_id
        self.file_http_url = file_http_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.file_http_url is not None:
            result['FileHttpUrl'] = self.file_http_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('FileHttpUrl') is not None:
            self.file_http_url = m.get('FileHttpUrl')
        return self


class DescribeExportProgressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeExportProgressResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeExportProgressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeInstanceResponseBody(TeaModel):
    def __init__(
        self,
        status: str = None,
        modify_time: int = None,
        description: str = None,
        request_id: str = None,
        instance_id: str = None,
        concurrency: int = None,
        applicable_operations: List[str] = None,
        modify_user_name: str = None,
        name: str = None,
    ):
        self.status = status
        self.modify_time = modify_time
        self.description = description
        self.request_id = request_id
        self.instance_id = instance_id
        self.concurrency = concurrency
        self.applicable_operations = applicable_operations
        self.modify_user_name = modify_user_name
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.description is not None:
            result['Description'] = self.description
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.concurrency is not None:
            result['Concurrency'] = self.concurrency
        if self.applicable_operations is not None:
            result['ApplicableOperations'] = self.applicable_operations
        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Concurrency') is not None:
            self.concurrency = m.get('Concurrency')
        if m.get('ApplicableOperations') is not None:
            self.applicable_operations = m.get('ApplicableOperations')
        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNavigationConfigRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeNavigationConfigResponseBodySilenceTimeoutConfig(TeaModel):
    def __init__(
        self,
        timeout: int = None,
        intent_trigger: str = None,
        final_prompt: str = None,
        source_type: str = None,
        final_action: str = None,
        prompt: str = None,
        threshold: int = None,
        final_action_params: str = None,
    ):
        self.timeout = timeout
        self.intent_trigger = intent_trigger
        self.final_prompt = final_prompt
        self.source_type = source_type
        self.final_action = final_action
        self.prompt = prompt
        self.threshold = threshold
        self.final_action_params = final_action_params

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        if self.intent_trigger is not None:
            result['IntentTrigger'] = self.intent_trigger
        if self.final_prompt is not None:
            result['FinalPrompt'] = self.final_prompt
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.final_action is not None:
            result['FinalAction'] = self.final_action
        if self.prompt is not None:
            result['Prompt'] = self.prompt
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.final_action_params is not None:
            result['FinalActionParams'] = self.final_action_params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        if m.get('IntentTrigger') is not None:
            self.intent_trigger = m.get('IntentTrigger')
        if m.get('FinalPrompt') is not None:
            self.final_prompt = m.get('FinalPrompt')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('FinalAction') is not None:
            self.final_action = m.get('FinalAction')
        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('FinalActionParams') is not None:
            self.final_action_params = m.get('FinalActionParams')
        return self


class DescribeNavigationConfigResponseBodyGreetingConfig(TeaModel):
    def __init__(
        self,
        intent_trigger: str = None,
        greeting_words: str = None,
        source_type: str = None,
    ):
        self.intent_trigger = intent_trigger
        self.greeting_words = greeting_words
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.intent_trigger is not None:
            result['IntentTrigger'] = self.intent_trigger
        if self.greeting_words is not None:
            result['GreetingWords'] = self.greeting_words
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IntentTrigger') is not None:
            self.intent_trigger = m.get('IntentTrigger')
        if m.get('GreetingWords') is not None:
            self.greeting_words = m.get('GreetingWords')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        return self


class DescribeNavigationConfigResponseBodyUnrecognizingConfig(TeaModel):
    def __init__(
        self,
        final_prompt: str = None,
        final_action: str = None,
        final_action_params: str = None,
        threshold: int = None,
        prompt: str = None,
    ):
        self.final_prompt = final_prompt
        self.final_action = final_action
        self.final_action_params = final_action_params
        self.threshold = threshold
        self.prompt = prompt

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.final_prompt is not None:
            result['FinalPrompt'] = self.final_prompt
        if self.final_action is not None:
            result['FinalAction'] = self.final_action
        if self.final_action_params is not None:
            result['FinalActionParams'] = self.final_action_params
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.prompt is not None:
            result['Prompt'] = self.prompt
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FinalPrompt') is not None:
            self.final_prompt = m.get('FinalPrompt')
        if m.get('FinalAction') is not None:
            self.final_action = m.get('FinalAction')
        if m.get('FinalActionParams') is not None:
            self.final_action_params = m.get('FinalActionParams')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')
        return self


class DescribeNavigationConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        silence_timeout_config: DescribeNavigationConfigResponseBodySilenceTimeoutConfig = None,
        greeting_config: DescribeNavigationConfigResponseBodyGreetingConfig = None,
        unrecognizing_config: DescribeNavigationConfigResponseBodyUnrecognizingConfig = None,
    ):
        self.request_id = request_id
        self.silence_timeout_config = silence_timeout_config
        self.greeting_config = greeting_config
        self.unrecognizing_config = unrecognizing_config

    def validate(self):
        if self.silence_timeout_config:
            self.silence_timeout_config.validate()
        if self.greeting_config:
            self.greeting_config.validate()
        if self.unrecognizing_config:
            self.unrecognizing_config.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.silence_timeout_config is not None:
            result['SilenceTimeoutConfig'] = self.silence_timeout_config.to_map()
        if self.greeting_config is not None:
            result['GreetingConfig'] = self.greeting_config.to_map()
        if self.unrecognizing_config is not None:
            result['UnrecognizingConfig'] = self.unrecognizing_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SilenceTimeoutConfig') is not None:
            temp_model = DescribeNavigationConfigResponseBodySilenceTimeoutConfig()
            self.silence_timeout_config = temp_model.from_map(m['SilenceTimeoutConfig'])
        if m.get('GreetingConfig') is not None:
            temp_model = DescribeNavigationConfigResponseBodyGreetingConfig()
            self.greeting_config = temp_model.from_map(m['GreetingConfig'])
        if m.get('UnrecognizingConfig') is not None:
            temp_model = DescribeNavigationConfigResponseBodyUnrecognizingConfig()
            self.unrecognizing_config = temp_model.from_map(m['UnrecognizingConfig'])
        return self


class DescribeNavigationConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeNavigationConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeNavigationConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRecordingRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        conversation_id: str = None,
    ):
        self.instance_id = instance_id
        self.conversation_id = conversation_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')
        return self


class DescribeRecordingResponseBody(TeaModel):
    def __init__(
        self,
        file_path: str = None,
        request_id: str = None,
        file_name: str = None,
    ):
        self.file_path = file_path
        self.request_id = request_id
        self.file_name = file_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.file_path is not None:
            result['FilePath'] = self.file_path
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.file_name is not None:
            result['FileName'] = self.file_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        return self


class DescribeRecordingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRecordingResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRecordingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeStatisticalDataRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        time_unit: str = None,
        begin_time_left_range: int = None,
        begin_time_right_range: int = None,
    ):
        self.instance_id = instance_id
        self.time_unit = time_unit
        self.begin_time_left_range = begin_time_left_range
        self.begin_time_right_range = begin_time_right_range

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.time_unit is not None:
            result['TimeUnit'] = self.time_unit
        if self.begin_time_left_range is not None:
            result['BeginTimeLeftRange'] = self.begin_time_left_range
        if self.begin_time_right_range is not None:
            result['BeginTimeRightRange'] = self.begin_time_right_range
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TimeUnit') is not None:
            self.time_unit = m.get('TimeUnit')
        if m.get('BeginTimeLeftRange') is not None:
            self.begin_time_left_range = m.get('BeginTimeLeftRange')
        if m.get('BeginTimeRightRange') is not None:
            self.begin_time_right_range = m.get('BeginTimeRightRange')
        return self


class DescribeStatisticalDataResponseBodyStatisticalDataReports(TeaModel):
    def __init__(
        self,
        knowledge_hit_rate: str = None,
        resolved_question_num: int = None,
        resolution_rate: str = None,
        statistical_date: str = None,
        total_conversation_num: int = None,
        valid_answer_rate: str = None,
        dialogue_pass_rate: str = None,
    ):
        self.knowledge_hit_rate = knowledge_hit_rate
        self.resolved_question_num = resolved_question_num
        self.resolution_rate = resolution_rate
        self.statistical_date = statistical_date
        self.total_conversation_num = total_conversation_num
        self.valid_answer_rate = valid_answer_rate
        self.dialogue_pass_rate = dialogue_pass_rate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.knowledge_hit_rate is not None:
            result['KnowledgeHitRate'] = self.knowledge_hit_rate
        if self.resolved_question_num is not None:
            result['ResolvedQuestionNum'] = self.resolved_question_num
        if self.resolution_rate is not None:
            result['ResolutionRate'] = self.resolution_rate
        if self.statistical_date is not None:
            result['StatisticalDate'] = self.statistical_date
        if self.total_conversation_num is not None:
            result['TotalConversationNum'] = self.total_conversation_num
        if self.valid_answer_rate is not None:
            result['ValidAnswerRate'] = self.valid_answer_rate
        if self.dialogue_pass_rate is not None:
            result['DialoguePassRate'] = self.dialogue_pass_rate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KnowledgeHitRate') is not None:
            self.knowledge_hit_rate = m.get('KnowledgeHitRate')
        if m.get('ResolvedQuestionNum') is not None:
            self.resolved_question_num = m.get('ResolvedQuestionNum')
        if m.get('ResolutionRate') is not None:
            self.resolution_rate = m.get('ResolutionRate')
        if m.get('StatisticalDate') is not None:
            self.statistical_date = m.get('StatisticalDate')
        if m.get('TotalConversationNum') is not None:
            self.total_conversation_num = m.get('TotalConversationNum')
        if m.get('ValidAnswerRate') is not None:
            self.valid_answer_rate = m.get('ValidAnswerRate')
        if m.get('DialoguePassRate') is not None:
            self.dialogue_pass_rate = m.get('DialoguePassRate')
        return self


class DescribeStatisticalDataResponseBody(TeaModel):
    def __init__(
        self,
        total_dialogue_pass_rate: str = None,
        total_knowledge_hit_rate: str = None,
        total_resolution_rate: str = None,
        total_valid_answer_rate: str = None,
        request_id: str = None,
        resolved_question_total_num: int = None,
        conversation_total_num: int = None,
        statistical_data_reports: List[DescribeStatisticalDataResponseBodyStatisticalDataReports] = None,
    ):
        self.total_dialogue_pass_rate = total_dialogue_pass_rate
        self.total_knowledge_hit_rate = total_knowledge_hit_rate
        self.total_resolution_rate = total_resolution_rate
        self.total_valid_answer_rate = total_valid_answer_rate
        self.request_id = request_id
        self.resolved_question_total_num = resolved_question_total_num
        self.conversation_total_num = conversation_total_num
        self.statistical_data_reports = statistical_data_reports

    def validate(self):
        if self.statistical_data_reports:
            for k in self.statistical_data_reports:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_dialogue_pass_rate is not None:
            result['TotalDialoguePassRate'] = self.total_dialogue_pass_rate
        if self.total_knowledge_hit_rate is not None:
            result['TotalKnowledgeHitRate'] = self.total_knowledge_hit_rate
        if self.total_resolution_rate is not None:
            result['TotalResolutionRate'] = self.total_resolution_rate
        if self.total_valid_answer_rate is not None:
            result['TotalValidAnswerRate'] = self.total_valid_answer_rate
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resolved_question_total_num is not None:
            result['ResolvedQuestionTotalNum'] = self.resolved_question_total_num
        if self.conversation_total_num is not None:
            result['ConversationTotalNum'] = self.conversation_total_num
        result['StatisticalDataReports'] = []
        if self.statistical_data_reports is not None:
            for k in self.statistical_data_reports:
                result['StatisticalDataReports'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalDialoguePassRate') is not None:
            self.total_dialogue_pass_rate = m.get('TotalDialoguePassRate')
        if m.get('TotalKnowledgeHitRate') is not None:
            self.total_knowledge_hit_rate = m.get('TotalKnowledgeHitRate')
        if m.get('TotalResolutionRate') is not None:
            self.total_resolution_rate = m.get('TotalResolutionRate')
        if m.get('TotalValidAnswerRate') is not None:
            self.total_valid_answer_rate = m.get('TotalValidAnswerRate')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResolvedQuestionTotalNum') is not None:
            self.resolved_question_total_num = m.get('ResolvedQuestionTotalNum')
        if m.get('ConversationTotalNum') is not None:
            self.conversation_total_num = m.get('ConversationTotalNum')
        self.statistical_data_reports = []
        if m.get('StatisticalDataReports') is not None:
            for k in m.get('StatisticalDataReports'):
                temp_model = DescribeStatisticalDataResponseBodyStatisticalDataReports()
                self.statistical_data_reports.append(temp_model.from_map(k))
        return self


class DescribeStatisticalDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeStatisticalDataResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeStatisticalDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTTSConfigRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeTTSConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        volume: int = None,
        voice: str = None,
        speech_rate: int = None,
    ):
        self.request_id = request_id
        self.volume = volume
        self.voice = voice
        self.speech_rate = speech_rate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.volume is not None:
            result['Volume'] = self.volume
        if self.voice is not None:
            result['Voice'] = self.voice
        if self.speech_rate is not None:
            result['SpeechRate'] = self.speech_rate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Volume') is not None:
            self.volume = m.get('Volume')
        if m.get('Voice') is not None:
            self.voice = m.get('Voice')
        if m.get('SpeechRate') is not None:
            self.speech_rate = m.get('SpeechRate')
        return self


class DescribeTTSConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeTTSConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeTTSConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DialogueRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        conversation_id: str = None,
        utterance: str = None,
        called_number: str = None,
        calling_number: str = None,
        additional_context: str = None,
    ):
        self.instance_id = instance_id
        self.conversation_id = conversation_id
        self.utterance = utterance
        self.called_number = called_number
        self.calling_number = calling_number
        self.additional_context = additional_context

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id
        if self.utterance is not None:
            result['Utterance'] = self.utterance
        if self.called_number is not None:
            result['CalledNumber'] = self.called_number
        if self.calling_number is not None:
            result['CallingNumber'] = self.calling_number
        if self.additional_context is not None:
            result['AdditionalContext'] = self.additional_context
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')
        if m.get('Utterance') is not None:
            self.utterance = m.get('Utterance')
        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')
        if m.get('CallingNumber') is not None:
            self.calling_number = m.get('CallingNumber')
        if m.get('AdditionalContext') is not None:
            self.additional_context = m.get('AdditionalContext')
        return self


class DialogueResponseBody(TeaModel):
    def __init__(
        self,
        action: str = None,
        interruptible: bool = None,
        request_id: str = None,
        action_params: str = None,
        text_response: str = None,
    ):
        self.action = action
        self.interruptible = interruptible
        self.request_id = request_id
        self.action_params = action_params
        self.text_response = text_response

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.interruptible is not None:
            result['Interruptible'] = self.interruptible
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.action_params is not None:
            result['ActionParams'] = self.action_params
        if self.text_response is not None:
            result['TextResponse'] = self.text_response
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Interruptible') is not None:
            self.interruptible = m.get('Interruptible')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ActionParams') is not None:
            self.action_params = m.get('ActionParams')
        if m.get('TextResponse') is not None:
            self.text_response = m.get('TextResponse')
        return self


class DialogueResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DialogueResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DialogueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DisableInstanceResponseBody(TeaModel):
    def __init__(
        self,
        status: str = None,
        request_id: str = None,
    ):
        self.status = status
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DisableInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DisableInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DisableInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class EnableInstanceResponseBody(TeaModel):
    def __init__(
        self,
        status: str = None,
        request_id: str = None,
    ):
        self.status = status
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EnableInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EnableInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = EnableInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EndDialogueRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        conversation_id: str = None,
    ):
        self.instance_id = instance_id
        self.conversation_id = conversation_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')
        return self


class EndDialogueResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EndDialogueResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EndDialogueResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = EndDialogueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExportConversationDetailsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        calling_number: str = None,
        begin_time_left_range: int = None,
        begin_time_right_range: int = None,
    ):
        self.instance_id = instance_id
        self.calling_number = calling_number
        self.begin_time_left_range = begin_time_left_range
        self.begin_time_right_range = begin_time_right_range

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.calling_number is not None:
            result['CallingNumber'] = self.calling_number
        if self.begin_time_left_range is not None:
            result['BeginTimeLeftRange'] = self.begin_time_left_range
        if self.begin_time_right_range is not None:
            result['BeginTimeRightRange'] = self.begin_time_right_range
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('CallingNumber') is not None:
            self.calling_number = m.get('CallingNumber')
        if m.get('BeginTimeLeftRange') is not None:
            self.begin_time_left_range = m.get('BeginTimeLeftRange')
        if m.get('BeginTimeRightRange') is not None:
            self.begin_time_right_range = m.get('BeginTimeRightRange')
        return self


class ExportConversationDetailsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        export_task_id: str = None,
    ):
        self.request_id = request_id
        self.export_task_id = export_task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.export_task_id is not None:
            result['ExportTaskId'] = self.export_task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ExportTaskId') is not None:
            self.export_task_id = m.get('ExportTaskId')
        return self


class ExportConversationDetailsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ExportConversationDetailsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ExportConversationDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExportStatisticalDataRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        time_unit: str = None,
        export_type: str = None,
        begin_time_left_range: int = None,
        begin_time_right_range: int = None,
    ):
        self.instance_id = instance_id
        self.time_unit = time_unit
        self.export_type = export_type
        self.begin_time_left_range = begin_time_left_range
        self.begin_time_right_range = begin_time_right_range

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.time_unit is not None:
            result['TimeUnit'] = self.time_unit
        if self.export_type is not None:
            result['ExportType'] = self.export_type
        if self.begin_time_left_range is not None:
            result['BeginTimeLeftRange'] = self.begin_time_left_range
        if self.begin_time_right_range is not None:
            result['BeginTimeRightRange'] = self.begin_time_right_range
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TimeUnit') is not None:
            self.time_unit = m.get('TimeUnit')
        if m.get('ExportType') is not None:
            self.export_type = m.get('ExportType')
        if m.get('BeginTimeLeftRange') is not None:
            self.begin_time_left_range = m.get('BeginTimeLeftRange')
        if m.get('BeginTimeRightRange') is not None:
            self.begin_time_right_range = m.get('BeginTimeRightRange')
        return self


class ExportStatisticalDataResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        export_task_id: str = None,
    ):
        self.request_id = request_id
        self.export_task_id = export_task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.export_task_id is not None:
            result['ExportTaskId'] = self.export_task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ExportTaskId') is not None:
            self.export_task_id = m.get('ExportTaskId')
        return self


class ExportStatisticalDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ExportStatisticalDataResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ExportStatisticalDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListChatbotInstancesRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.instance_id = instance_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListChatbotInstancesResponseBodyBots(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        time_zone: str = None,
        avatar: str = None,
        language_code: str = None,
        name: str = None,
        introduction: str = None,
        create_time: str = None,
    ):
        self.instance_id = instance_id
        self.time_zone = time_zone
        self.avatar = avatar
        self.language_code = language_code
        self.name = name
        self.introduction = introduction
        self.create_time = create_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone
        if self.avatar is not None:
            result['Avatar'] = self.avatar
        if self.language_code is not None:
            result['LanguageCode'] = self.language_code
        if self.name is not None:
            result['Name'] = self.name
        if self.introduction is not None:
            result['Introduction'] = self.introduction
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')
        if m.get('Avatar') is not None:
            self.avatar = m.get('Avatar')
        if m.get('LanguageCode') is not None:
            self.language_code = m.get('LanguageCode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Introduction') is not None:
            self.introduction = m.get('Introduction')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        return self


class ListChatbotInstancesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        page_number: int = None,
        total_count: int = None,
        page_size: int = None,
        bots: List[ListChatbotInstancesResponseBodyBots] = None,
    ):
        self.request_id = request_id
        self.page_number = page_number
        self.total_count = total_count
        self.page_size = page_size
        self.bots = bots

    def validate(self):
        if self.bots:
            for k in self.bots:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Bots'] = []
        if self.bots is not None:
            for k in self.bots:
                result['Bots'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.bots = []
        if m.get('Bots') is not None:
            for k in m.get('Bots'):
                temp_model = ListChatbotInstancesResponseBodyBots()
                self.bots.append(temp_model.from_map(k))
        return self


class ListChatbotInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListChatbotInstancesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListChatbotInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListConversationDetailsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        conversation_id: str = None,
    ):
        self.instance_id = instance_id
        self.conversation_id = conversation_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')
        return self


class ListConversationDetailsResponseBodyConversationDetails(TeaModel):
    def __init__(
        self,
        action: str = None,
        speaker: str = None,
        create_time: int = None,
        conversation_id: str = None,
        action_params: str = None,
        sequence_id: str = None,
        utterance: str = None,
    ):
        self.action = action
        self.speaker = speaker
        self.create_time = create_time
        self.conversation_id = conversation_id
        self.action_params = action_params
        self.sequence_id = sequence_id
        self.utterance = utterance

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.speaker is not None:
            result['Speaker'] = self.speaker
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id
        if self.action_params is not None:
            result['ActionParams'] = self.action_params
        if self.sequence_id is not None:
            result['SequenceId'] = self.sequence_id
        if self.utterance is not None:
            result['Utterance'] = self.utterance
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Speaker') is not None:
            self.speaker = m.get('Speaker')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')
        if m.get('ActionParams') is not None:
            self.action_params = m.get('ActionParams')
        if m.get('SequenceId') is not None:
            self.sequence_id = m.get('SequenceId')
        if m.get('Utterance') is not None:
            self.utterance = m.get('Utterance')
        return self


class ListConversationDetailsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        conversation_details: List[ListConversationDetailsResponseBodyConversationDetails] = None,
    ):
        self.request_id = request_id
        self.conversation_details = conversation_details

    def validate(self):
        if self.conversation_details:
            for k in self.conversation_details:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ConversationDetails'] = []
        if self.conversation_details is not None:
            for k in self.conversation_details:
                result['ConversationDetails'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.conversation_details = []
        if m.get('ConversationDetails') is not None:
            for k in m.get('ConversationDetails'):
                temp_model = ListConversationDetailsResponseBodyConversationDetails()
                self.conversation_details.append(temp_model.from_map(k))
        return self


class ListConversationDetailsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListConversationDetailsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListConversationDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListConversationsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.instance_id = instance_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListConversationsResponseBodyConversations(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        effective_answer_count: int = None,
        transferred_to_agent: bool = None,
        begin_time: int = None,
        skill_group_id: str = None,
        conversation_id: str = None,
        calling_number: str = None,
        user_utterance_count: int = None,
    ):
        self.end_time = end_time
        self.effective_answer_count = effective_answer_count
        self.transferred_to_agent = transferred_to_agent
        self.begin_time = begin_time
        self.skill_group_id = skill_group_id
        self.conversation_id = conversation_id
        self.calling_number = calling_number
        self.user_utterance_count = user_utterance_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.effective_answer_count is not None:
            result['EffectiveAnswerCount'] = self.effective_answer_count
        if self.transferred_to_agent is not None:
            result['TransferredToAgent'] = self.transferred_to_agent
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.skill_group_id is not None:
            result['SkillGroupId'] = self.skill_group_id
        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id
        if self.calling_number is not None:
            result['CallingNumber'] = self.calling_number
        if self.user_utterance_count is not None:
            result['UserUtteranceCount'] = self.user_utterance_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EffectiveAnswerCount') is not None:
            self.effective_answer_count = m.get('EffectiveAnswerCount')
        if m.get('TransferredToAgent') is not None:
            self.transferred_to_agent = m.get('TransferredToAgent')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('SkillGroupId') is not None:
            self.skill_group_id = m.get('SkillGroupId')
        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')
        if m.get('CallingNumber') is not None:
            self.calling_number = m.get('CallingNumber')
        if m.get('UserUtteranceCount') is not None:
            self.user_utterance_count = m.get('UserUtteranceCount')
        return self


class ListConversationsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
        conversations: List[ListConversationsResponseBodyConversations] = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number
        self.conversations = conversations

    def validate(self):
        if self.conversations:
            for k in self.conversations:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Conversations'] = []
        if self.conversations is not None:
            for k in self.conversations:
                result['Conversations'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.conversations = []
        if m.get('Conversations') is not None:
            for k in m.get('Conversations'):
                temp_model = ListConversationsResponseBodyConversations()
                self.conversations.append(temp_model.from_map(k))
        return self


class ListConversationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListConversationsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListConversationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstancesRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListInstancesResponseBodyInstances(TeaModel):
    def __init__(
        self,
        status: str = None,
        modify_user_name: str = None,
        description: str = None,
        applicable_operations: List[str] = None,
        instance_id: str = None,
        name: str = None,
        concurrency: int = None,
        modify_time: int = None,
    ):
        self.status = status
        self.modify_user_name = modify_user_name
        self.description = description
        self.applicable_operations = applicable_operations
        self.instance_id = instance_id
        self.name = name
        self.concurrency = concurrency
        self.modify_time = modify_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name
        if self.description is not None:
            result['Description'] = self.description
        if self.applicable_operations is not None:
            result['ApplicableOperations'] = self.applicable_operations
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.concurrency is not None:
            result['Concurrency'] = self.concurrency
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ApplicableOperations') is not None:
            self.applicable_operations = m.get('ApplicableOperations')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Concurrency') is not None:
            self.concurrency = m.get('Concurrency')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        return self


class ListInstancesResponseBody(TeaModel):
    def __init__(
        self,
        instances: List[ListInstancesResponseBodyInstances] = None,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
    ):
        self.instances = instances
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number

    def validate(self):
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = ListInstancesResponseBodyInstances()
                self.instances.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class ListInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListInstancesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyGreetingConfigRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        greeting_words: str = None,
        source_type: str = None,
        intent_trigger: str = None,
    ):
        self.instance_id = instance_id
        self.greeting_words = greeting_words
        self.source_type = source_type
        self.intent_trigger = intent_trigger

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.greeting_words is not None:
            result['GreetingWords'] = self.greeting_words
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.intent_trigger is not None:
            result['IntentTrigger'] = self.intent_trigger
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('GreetingWords') is not None:
            self.greeting_words = m.get('GreetingWords')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('IntentTrigger') is not None:
            self.intent_trigger = m.get('IntentTrigger')
        return self


class ModifyGreetingConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyGreetingConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyGreetingConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyGreetingConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        description: str = None,
        concurrency: int = None,
        chatbot_instance_id: str = None,
    ):
        self.instance_id = instance_id
        self.description = description
        self.concurrency = concurrency
        self.chatbot_instance_id = chatbot_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.description is not None:
            result['Description'] = self.description
        if self.concurrency is not None:
            result['Concurrency'] = self.concurrency
        if self.chatbot_instance_id is not None:
            result['ChatbotInstanceId'] = self.chatbot_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Concurrency') is not None:
            self.concurrency = m.get('Concurrency')
        if m.get('ChatbotInstanceId') is not None:
            self.chatbot_instance_id = m.get('ChatbotInstanceId')
        return self


class ModifyInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySilenceTimeoutConfigRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        prompt: str = None,
        timeout: int = None,
        threshold: int = None,
        final_prompt: str = None,
        final_action: str = None,
        final_action_params: str = None,
        source_type: str = None,
        intent_trigger: str = None,
    ):
        self.instance_id = instance_id
        self.prompt = prompt
        self.timeout = timeout
        self.threshold = threshold
        self.final_prompt = final_prompt
        self.final_action = final_action
        self.final_action_params = final_action_params
        self.source_type = source_type
        self.intent_trigger = intent_trigger

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.prompt is not None:
            result['Prompt'] = self.prompt
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.final_prompt is not None:
            result['FinalPrompt'] = self.final_prompt
        if self.final_action is not None:
            result['FinalAction'] = self.final_action
        if self.final_action_params is not None:
            result['FinalActionParams'] = self.final_action_params
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.intent_trigger is not None:
            result['IntentTrigger'] = self.intent_trigger
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('FinalPrompt') is not None:
            self.final_prompt = m.get('FinalPrompt')
        if m.get('FinalAction') is not None:
            self.final_action = m.get('FinalAction')
        if m.get('FinalActionParams') is not None:
            self.final_action_params = m.get('FinalActionParams')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('IntentTrigger') is not None:
            self.intent_trigger = m.get('IntentTrigger')
        return self


class ModifySilenceTimeoutConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifySilenceTimeoutConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifySilenceTimeoutConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifySilenceTimeoutConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyTTSConfigRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        voice: str = None,
        speech_rate: str = None,
        volume: str = None,
    ):
        self.instance_id = instance_id
        self.voice = voice
        self.speech_rate = speech_rate
        self.volume = volume

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.voice is not None:
            result['Voice'] = self.voice
        if self.speech_rate is not None:
            result['SpeechRate'] = self.speech_rate
        if self.volume is not None:
            result['Volume'] = self.volume
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Voice') is not None:
            self.voice = m.get('Voice')
        if m.get('SpeechRate') is not None:
            self.speech_rate = m.get('SpeechRate')
        if m.get('Volume') is not None:
            self.volume = m.get('Volume')
        return self


class ModifyTTSConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyTTSConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyTTSConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyTTSConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyUnrecognizingConfigRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        prompt: str = None,
        threshold: int = None,
        final_prompt: str = None,
        final_action: str = None,
        final_action_params: str = None,
    ):
        self.instance_id = instance_id
        self.prompt = prompt
        self.threshold = threshold
        self.final_prompt = final_prompt
        self.final_action = final_action
        self.final_action_params = final_action_params

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.prompt is not None:
            result['Prompt'] = self.prompt
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.final_prompt is not None:
            result['FinalPrompt'] = self.final_prompt
        if self.final_action is not None:
            result['FinalAction'] = self.final_action
        if self.final_action_params is not None:
            result['FinalActionParams'] = self.final_action_params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('FinalPrompt') is not None:
            self.final_prompt = m.get('FinalPrompt')
        if m.get('FinalAction') is not None:
            self.final_action = m.get('FinalAction')
        if m.get('FinalActionParams') is not None:
            self.final_action_params = m.get('FinalActionParams')
        return self


class ModifyUnrecognizingConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyUnrecognizingConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyUnrecognizingConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyUnrecognizingConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryConversationsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        calling_number: str = None,
        begin_time_left_range: int = None,
        begin_time_right_range: int = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.instance_id = instance_id
        self.calling_number = calling_number
        self.begin_time_left_range = begin_time_left_range
        self.begin_time_right_range = begin_time_right_range
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.calling_number is not None:
            result['CallingNumber'] = self.calling_number
        if self.begin_time_left_range is not None:
            result['BeginTimeLeftRange'] = self.begin_time_left_range
        if self.begin_time_right_range is not None:
            result['BeginTimeRightRange'] = self.begin_time_right_range
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('CallingNumber') is not None:
            self.calling_number = m.get('CallingNumber')
        if m.get('BeginTimeLeftRange') is not None:
            self.begin_time_left_range = m.get('BeginTimeLeftRange')
        if m.get('BeginTimeRightRange') is not None:
            self.begin_time_right_range = m.get('BeginTimeRightRange')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryConversationsResponseBodyConversations(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        effective_answer_count: int = None,
        transferred_to_agent: bool = None,
        begin_time: int = None,
        skill_group_id: str = None,
        conversation_id: str = None,
        calling_number: str = None,
        user_utterance_count: int = None,
    ):
        self.end_time = end_time
        self.effective_answer_count = effective_answer_count
        self.transferred_to_agent = transferred_to_agent
        self.begin_time = begin_time
        self.skill_group_id = skill_group_id
        self.conversation_id = conversation_id
        self.calling_number = calling_number
        self.user_utterance_count = user_utterance_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.effective_answer_count is not None:
            result['EffectiveAnswerCount'] = self.effective_answer_count
        if self.transferred_to_agent is not None:
            result['TransferredToAgent'] = self.transferred_to_agent
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.skill_group_id is not None:
            result['SkillGroupId'] = self.skill_group_id
        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id
        if self.calling_number is not None:
            result['CallingNumber'] = self.calling_number
        if self.user_utterance_count is not None:
            result['UserUtteranceCount'] = self.user_utterance_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EffectiveAnswerCount') is not None:
            self.effective_answer_count = m.get('EffectiveAnswerCount')
        if m.get('TransferredToAgent') is not None:
            self.transferred_to_agent = m.get('TransferredToAgent')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('SkillGroupId') is not None:
            self.skill_group_id = m.get('SkillGroupId')
        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')
        if m.get('CallingNumber') is not None:
            self.calling_number = m.get('CallingNumber')
        if m.get('UserUtteranceCount') is not None:
            self.user_utterance_count = m.get('UserUtteranceCount')
        return self


class QueryConversationsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
        conversations: List[QueryConversationsResponseBodyConversations] = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number
        self.conversations = conversations

    def validate(self):
        if self.conversations:
            for k in self.conversations:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Conversations'] = []
        if self.conversations is not None:
            for k in self.conversations:
                result['Conversations'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.conversations = []
        if m.get('Conversations') is not None:
            for k in m.get('Conversations'):
                temp_model = QueryConversationsResponseBodyConversations()
                self.conversations.append(temp_model.from_map(k))
        return self


class QueryConversationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryConversationsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryConversationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveRecordingRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        conversation_id: str = None,
        start_time: int = None,
        duration: str = None,
        file_name: str = None,
        file_path: str = None,
        type: str = None,
    ):
        self.instance_id = instance_id
        self.conversation_id = conversation_id
        self.start_time = start_time
        self.duration = duration
        self.file_name = file_name
        self.file_path = file_path
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_path is not None:
            result['FilePath'] = self.file_path
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class SaveRecordingResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SaveRecordingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SaveRecordingResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SaveRecordingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SilenceTimeoutRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        conversation_id: str = None,
        initial_context: str = None,
    ):
        self.instance_id = instance_id
        self.conversation_id = conversation_id
        self.initial_context = initial_context

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id
        if self.initial_context is not None:
            result['InitialContext'] = self.initial_context
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')
        if m.get('InitialContext') is not None:
            self.initial_context = m.get('InitialContext')
        return self


class SilenceTimeoutResponseBody(TeaModel):
    def __init__(
        self,
        action: str = None,
        interruptible: bool = None,
        request_id: str = None,
        action_params: str = None,
        text_response: str = None,
    ):
        self.action = action
        self.interruptible = interruptible
        self.request_id = request_id
        self.action_params = action_params
        self.text_response = text_response

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.interruptible is not None:
            result['Interruptible'] = self.interruptible
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.action_params is not None:
            result['ActionParams'] = self.action_params
        if self.text_response is not None:
            result['TextResponse'] = self.text_response
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Interruptible') is not None:
            self.interruptible = m.get('Interruptible')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ActionParams') is not None:
            self.action_params = m.get('ActionParams')
        if m.get('TextResponse') is not None:
            self.text_response = m.get('TextResponse')
        return self


class SilenceTimeoutResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SilenceTimeoutResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SilenceTimeoutResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


