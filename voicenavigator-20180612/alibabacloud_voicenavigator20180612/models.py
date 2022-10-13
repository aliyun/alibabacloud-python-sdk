# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class AssociateChatbotInstanceRequest(TeaModel):
    def __init__(
        self,
        chatbot_instance_id: str = None,
        chatbot_name: str = None,
        instance_id: str = None,
    ):
        self.chatbot_instance_id = chatbot_instance_id
        self.chatbot_name = chatbot_name
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chatbot_instance_id is not None:
            result['ChatbotInstanceId'] = self.chatbot_instance_id
        if self.chatbot_name is not None:
            result['ChatbotName'] = self.chatbot_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChatbotInstanceId') is not None:
            self.chatbot_instance_id = m.get('ChatbotInstanceId')
        if m.get('ChatbotName') is not None:
            self.chatbot_name = m.get('ChatbotName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: AssociateChatbotInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AssociateChatbotInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AuditTTSVoiceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        speech_rate: str = None,
        text: str = None,
        voice: str = None,
        volume: str = None,
    ):
        self.instance_id = instance_id
        self.speech_rate = speech_rate
        self.text = text
        self.voice = voice
        self.volume = volume

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.speech_rate is not None:
            result['SpeechRate'] = self.speech_rate
        if self.text is not None:
            result['Text'] = self.text
        if self.voice is not None:
            result['Voice'] = self.voice
        if self.volume is not None:
            result['Volume'] = self.volume
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SpeechRate') is not None:
            self.speech_rate = m.get('SpeechRate')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Voice') is not None:
            self.voice = m.get('Voice')
        if m.get('Volume') is not None:
            self.volume = m.get('Volume')
        return self


class AuditTTSVoiceResponseBody(TeaModel):
    def __init__(
        self,
        audition_url: str = None,
        request_id: str = None,
    ):
        self.audition_url = audition_url
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audition_url is not None:
            result['AuditionUrl'] = self.audition_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditionUrl') is not None:
            self.audition_url = m.get('AuditionUrl')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AuditTTSVoiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AuditTTSVoiceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
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
        instance_owner_id: int = None,
    ):
        self.called_number = called_number
        self.calling_number = calling_number
        self.conversation_id = conversation_id
        self.initial_context = initial_context
        self.instance_id = instance_id
        self.instance_owner_id = instance_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        if self.instance_owner_id is not None:
            result['InstanceOwnerId'] = self.instance_owner_id
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
        if m.get('InstanceOwnerId') is not None:
            self.instance_owner_id = m.get('InstanceOwnerId')
        return self


class BeginDialogueResponseBody(TeaModel):
    def __init__(
        self,
        action: str = None,
        action_params: str = None,
        interruptible: bool = None,
        request_id: str = None,
        text_response: str = None,
    ):
        self.action = action
        self.action_params = action_params
        self.interruptible = interruptible
        self.request_id = request_id
        self.text_response = text_response

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.action_params is not None:
            result['ActionParams'] = self.action_params
        if self.interruptible is not None:
            result['Interruptible'] = self.interruptible
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.text_response is not None:
            result['TextResponse'] = self.text_response
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('ActionParams') is not None:
            self.action_params = m.get('ActionParams')
        if m.get('Interruptible') is not None:
            self.interruptible = m.get('Interruptible')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TextResponse') is not None:
            self.text_response = m.get('TextResponse')
        return self


class BeginDialogueResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BeginDialogueResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BeginDialogueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CollectedNumberRequest(TeaModel):
    def __init__(
        self,
        conversation_id: str = None,
        instance_id: str = None,
        instance_owner_id: int = None,
        number: str = None,
    ):
        self.conversation_id = conversation_id
        self.instance_id = instance_id
        self.instance_owner_id = instance_owner_id
        self.number = number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_owner_id is not None:
            result['InstanceOwnerId'] = self.instance_owner_id
        if self.number is not None:
            result['Number'] = self.number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceOwnerId') is not None:
            self.instance_owner_id = m.get('InstanceOwnerId')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        return self


class CollectedNumberResponseBody(TeaModel):
    def __init__(
        self,
        action: str = None,
        action_params: str = None,
        interruptible: bool = None,
        request_id: str = None,
        text_response: str = None,
    ):
        self.action = action
        self.action_params = action_params
        self.interruptible = interruptible
        self.request_id = request_id
        self.text_response = text_response

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.action_params is not None:
            result['ActionParams'] = self.action_params
        if self.interruptible is not None:
            result['Interruptible'] = self.interruptible
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.text_response is not None:
            result['TextResponse'] = self.text_response
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('ActionParams') is not None:
            self.action_params = m.get('ActionParams')
        if m.get('Interruptible') is not None:
            self.interruptible = m.get('Interruptible')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TextResponse') is not None:
            self.text_response = m.get('TextResponse')
        return self


class CollectedNumberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CollectedNumberResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CollectedNumberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDownloadUrlRequest(TeaModel):
    def __init__(
        self,
        download_task_id: str = None,
        file_id: str = None,
    ):
        self.download_task_id = download_task_id
        self.file_id = file_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.download_task_id is not None:
            result['DownloadTaskId'] = self.download_task_id
        if self.file_id is not None:
            result['FileId'] = self.file_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownloadTaskId') is not None:
            self.download_task_id = m.get('DownloadTaskId')
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        return self


class CreateDownloadUrlResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        file_http_url: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.file_http_url = file_http_url
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.file_http_url is not None:
            result['FileHttpUrl'] = self.file_http_url
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('FileHttpUrl') is not None:
            self.file_http_url = m.get('FileHttpUrl')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateDownloadUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDownloadUrlResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateDownloadUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateInstanceRequest(TeaModel):
    def __init__(
        self,
        concurrency: int = None,
        description: str = None,
        name: str = None,
    ):
        self.concurrency = concurrency
        self.description = description
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.concurrency is not None:
            result['Concurrency'] = self.concurrency
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Concurrency') is not None:
            self.concurrency = m.get('Concurrency')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateInstanceResponseBody(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        request_id: str = None,
    ):
        self.instance_id = instance_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        action_params: str = None,
        interruptible: bool = None,
        request_id: str = None,
        text_response: str = None,
    ):
        self.action = action
        self.action_params = action_params
        self.interruptible = interruptible
        self.request_id = request_id
        self.text_response = text_response

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.action_params is not None:
            result['ActionParams'] = self.action_params
        if self.interruptible is not None:
            result['Interruptible'] = self.interruptible
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.text_response is not None:
            result['TextResponse'] = self.text_response
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('ActionParams') is not None:
            self.action_params = m.get('ActionParams')
        if m.get('Interruptible') is not None:
            self.interruptible = m.get('Interruptible')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TextResponse') is not None:
            self.text_response = m.get('TextResponse')
        return self


class DebugBeginDialogueResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DebugBeginDialogueResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DebugBeginDialogueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DebugCollectedNumberRequest(TeaModel):
    def __init__(
        self,
        conversation_id: str = None,
        instance_id: str = None,
        number: str = None,
    ):
        self.conversation_id = conversation_id
        self.instance_id = instance_id
        self.number = number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.number is not None:
            result['Number'] = self.number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        return self


class DebugCollectedNumberResponseBody(TeaModel):
    def __init__(
        self,
        action: str = None,
        action_params: str = None,
        interruptible: bool = None,
        request_id: str = None,
        text_response: str = None,
    ):
        self.action = action
        self.action_params = action_params
        self.interruptible = interruptible
        self.request_id = request_id
        self.text_response = text_response

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.action_params is not None:
            result['ActionParams'] = self.action_params
        if self.interruptible is not None:
            result['Interruptible'] = self.interruptible
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.text_response is not None:
            result['TextResponse'] = self.text_response
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('ActionParams') is not None:
            self.action_params = m.get('ActionParams')
        if m.get('Interruptible') is not None:
            self.interruptible = m.get('Interruptible')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TextResponse') is not None:
            self.text_response = m.get('TextResponse')
        return self


class DebugCollectedNumberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DebugCollectedNumberResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DebugCollectedNumberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DebugDialogueRequest(TeaModel):
    def __init__(
        self,
        additional_context: str = None,
        conversation_id: str = None,
        instance_id: str = None,
        utterance: str = None,
    ):
        self.additional_context = additional_context
        self.conversation_id = conversation_id
        self.instance_id = instance_id
        self.utterance = utterance

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.additional_context is not None:
            result['AdditionalContext'] = self.additional_context
        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.utterance is not None:
            result['Utterance'] = self.utterance
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdditionalContext') is not None:
            self.additional_context = m.get('AdditionalContext')
        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Utterance') is not None:
            self.utterance = m.get('Utterance')
        return self


class DebugDialogueResponseBody(TeaModel):
    def __init__(
        self,
        action: str = None,
        action_params: str = None,
        interruptible: bool = None,
        request_id: str = None,
        text_response: str = None,
    ):
        self.action = action
        self.action_params = action_params
        self.interruptible = interruptible
        self.request_id = request_id
        self.text_response = text_response

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.action_params is not None:
            result['ActionParams'] = self.action_params
        if self.interruptible is not None:
            result['Interruptible'] = self.interruptible
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.text_response is not None:
            result['TextResponse'] = self.text_response
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('ActionParams') is not None:
            self.action_params = m.get('ActionParams')
        if m.get('Interruptible') is not None:
            self.interruptible = m.get('Interruptible')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TextResponse') is not None:
            self.text_response = m.get('TextResponse')
        return self


class DebugDialogueResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DebugDialogueResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: DeleteInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeConversationRequest(TeaModel):
    def __init__(
        self,
        conversation_id: str = None,
        instance_id: str = None,
    ):
        self.conversation_id = conversation_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeConversationResponseBody(TeaModel):
    def __init__(
        self,
        begin_time: int = None,
        calling_number: str = None,
        conversation_id: str = None,
        effective_answer_count: int = None,
        end_time: int = None,
        request_id: str = None,
        skill_group_id: str = None,
        transferred_to_agent: bool = None,
        user_utterance_count: int = None,
    ):
        self.begin_time = begin_time
        self.calling_number = calling_number
        self.conversation_id = conversation_id
        self.effective_answer_count = effective_answer_count
        self.end_time = end_time
        self.request_id = request_id
        self.skill_group_id = skill_group_id
        self.transferred_to_agent = transferred_to_agent
        self.user_utterance_count = user_utterance_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.calling_number is not None:
            result['CallingNumber'] = self.calling_number
        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id
        if self.effective_answer_count is not None:
            result['EffectiveAnswerCount'] = self.effective_answer_count
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.skill_group_id is not None:
            result['SkillGroupId'] = self.skill_group_id
        if self.transferred_to_agent is not None:
            result['TransferredToAgent'] = self.transferred_to_agent
        if self.user_utterance_count is not None:
            result['UserUtteranceCount'] = self.user_utterance_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('CallingNumber') is not None:
            self.calling_number = m.get('CallingNumber')
        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')
        if m.get('EffectiveAnswerCount') is not None:
            self.effective_answer_count = m.get('EffectiveAnswerCount')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SkillGroupId') is not None:
            self.skill_group_id = m.get('SkillGroupId')
        if m.get('TransferredToAgent') is not None:
            self.transferred_to_agent = m.get('TransferredToAgent')
        if m.get('UserUtteranceCount') is not None:
            self.user_utterance_count = m.get('UserUtteranceCount')
        return self


class DescribeConversationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeConversationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeConversationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeConversationContextRequest(TeaModel):
    def __init__(
        self,
        conversation_id: str = None,
        instance_id: str = None,
    ):
        self.conversation_id = conversation_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeConversationContextResponseBody(TeaModel):
    def __init__(
        self,
        conversation_context: str = None,
        request_id: str = None,
    ):
        self.conversation_context = conversation_context
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conversation_context is not None:
            result['ConversationContext'] = self.conversation_context
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConversationContext') is not None:
            self.conversation_context = m.get('ConversationContext')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeConversationContextResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeConversationContextResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeConversationContextResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeExportProgressRequest(TeaModel):
    def __init__(
        self,
        export_task_id: str = None,
        instance_id: str = None,
    ):
        self.export_task_id = export_task_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.export_task_id is not None:
            result['ExportTaskId'] = self.export_task_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExportTaskId') is not None:
            self.export_task_id = m.get('ExportTaskId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeExportProgressResponseBody(TeaModel):
    def __init__(
        self,
        file_http_url: str = None,
        request_id: str = None,
        status: str = None,
    ):
        self.file_http_url = file_http_url
        self.request_id = request_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_http_url is not None:
            result['FileHttpUrl'] = self.file_http_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileHttpUrl') is not None:
            self.file_http_url = m.get('FileHttpUrl')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeExportProgressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeExportProgressResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        applicable_operations: List[str] = None,
        concurrency: int = None,
        description: str = None,
        instance_id: str = None,
        modify_time: int = None,
        modify_user_name: str = None,
        name: str = None,
        request_id: str = None,
        status: str = None,
    ):
        self.applicable_operations = applicable_operations
        self.concurrency = concurrency
        self.description = description
        self.instance_id = instance_id
        self.modify_time = modify_time
        self.modify_user_name = modify_user_name
        self.name = name
        self.request_id = request_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.applicable_operations is not None:
            result['ApplicableOperations'] = self.applicable_operations
        if self.concurrency is not None:
            result['Concurrency'] = self.concurrency
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicableOperations') is not None:
            self.applicable_operations = m.get('ApplicableOperations')
        if m.get('Concurrency') is not None:
            self.concurrency = m.get('Concurrency')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeNavigationConfigResponseBodyGreetingConfig(TeaModel):
    def __init__(
        self,
        greeting_words: str = None,
        intent_trigger: str = None,
        source_type: str = None,
    ):
        self.greeting_words = greeting_words
        self.intent_trigger = intent_trigger
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class DescribeNavigationConfigResponseBodySilenceTimeoutConfig(TeaModel):
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
        self.final_action = final_action
        self.final_action_params = final_action_params
        self.final_prompt = final_prompt
        self.intent_trigger = intent_trigger
        self.prompt = prompt
        self.source_type = source_type
        self.threshold = threshold
        self.timeout = timeout

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class DescribeNavigationConfigResponseBodyUnrecognizingConfig(TeaModel):
    def __init__(
        self,
        final_action: str = None,
        final_action_params: str = None,
        final_prompt: str = None,
        prompt: str = None,
        threshold: int = None,
    ):
        self.final_action = final_action
        self.final_action_params = final_action_params
        self.final_prompt = final_prompt
        self.prompt = prompt
        self.threshold = threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class DescribeNavigationConfigResponseBody(TeaModel):
    def __init__(
        self,
        greeting_config: DescribeNavigationConfigResponseBodyGreetingConfig = None,
        request_id: str = None,
        silence_timeout_config: DescribeNavigationConfigResponseBodySilenceTimeoutConfig = None,
        unrecognizing_config: DescribeNavigationConfigResponseBodyUnrecognizingConfig = None,
    ):
        self.greeting_config = greeting_config
        self.request_id = request_id
        self.silence_timeout_config = silence_timeout_config
        self.unrecognizing_config = unrecognizing_config

    def validate(self):
        if self.greeting_config:
            self.greeting_config.validate()
        if self.silence_timeout_config:
            self.silence_timeout_config.validate()
        if self.unrecognizing_config:
            self.unrecognizing_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = DescribeNavigationConfigResponseBodyGreetingConfig()
            self.greeting_config = temp_model.from_map(m['GreetingConfig'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SilenceTimeoutConfig') is not None:
            temp_model = DescribeNavigationConfigResponseBodySilenceTimeoutConfig()
            self.silence_timeout_config = temp_model.from_map(m['SilenceTimeoutConfig'])
        if m.get('UnrecognizingConfig') is not None:
            temp_model = DescribeNavigationConfigResponseBodyUnrecognizingConfig()
            self.unrecognizing_config = temp_model.from_map(m['UnrecognizingConfig'])
        return self


class DescribeNavigationConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeNavigationConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeNavigationConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRecordingRequest(TeaModel):
    def __init__(
        self,
        conversation_id: str = None,
        instance_id: str = None,
        need_voice_slice_recording: bool = None,
    ):
        self.conversation_id = conversation_id
        self.instance_id = instance_id
        self.need_voice_slice_recording = need_voice_slice_recording

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.need_voice_slice_recording is not None:
            result['NeedVoiceSliceRecording'] = self.need_voice_slice_recording
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NeedVoiceSliceRecording') is not None:
            self.need_voice_slice_recording = m.get('NeedVoiceSliceRecording')
        return self


class DescribeRecordingResponseBody(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        file_path: str = None,
        request_id: str = None,
        voice_slice_recording_list_json: str = None,
    ):
        self.file_name = file_name
        self.file_path = file_path
        self.request_id = request_id
        self.voice_slice_recording_list_json = voice_slice_recording_list_json

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_path is not None:
            result['FilePath'] = self.file_path
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.voice_slice_recording_list_json is not None:
            result['VoiceSliceRecordingListJson'] = self.voice_slice_recording_list_json
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VoiceSliceRecordingListJson') is not None:
            self.voice_slice_recording_list_json = m.get('VoiceSliceRecordingListJson')
        return self


class DescribeRecordingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeRecordingResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeRecordingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeStatisticalDataRequest(TeaModel):
    def __init__(
        self,
        begin_time_left_range: int = None,
        begin_time_right_range: int = None,
        instance_id: str = None,
        time_unit: str = None,
    ):
        self.begin_time_left_range = begin_time_left_range
        self.begin_time_right_range = begin_time_right_range
        self.instance_id = instance_id
        self.time_unit = time_unit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time_left_range is not None:
            result['BeginTimeLeftRange'] = self.begin_time_left_range
        if self.begin_time_right_range is not None:
            result['BeginTimeRightRange'] = self.begin_time_right_range
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.time_unit is not None:
            result['TimeUnit'] = self.time_unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTimeLeftRange') is not None:
            self.begin_time_left_range = m.get('BeginTimeLeftRange')
        if m.get('BeginTimeRightRange') is not None:
            self.begin_time_right_range = m.get('BeginTimeRightRange')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TimeUnit') is not None:
            self.time_unit = m.get('TimeUnit')
        return self


class DescribeStatisticalDataResponseBodyStatisticalDataReports(TeaModel):
    def __init__(
        self,
        dialogue_pass_rate: str = None,
        knowledge_hit_rate: str = None,
        resolution_rate: str = None,
        resolved_question_num: int = None,
        statistical_date: str = None,
        total_conversation_num: int = None,
        valid_answer_rate: str = None,
    ):
        self.dialogue_pass_rate = dialogue_pass_rate
        self.knowledge_hit_rate = knowledge_hit_rate
        self.resolution_rate = resolution_rate
        self.resolved_question_num = resolved_question_num
        self.statistical_date = statistical_date
        self.total_conversation_num = total_conversation_num
        self.valid_answer_rate = valid_answer_rate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dialogue_pass_rate is not None:
            result['DialoguePassRate'] = self.dialogue_pass_rate
        if self.knowledge_hit_rate is not None:
            result['KnowledgeHitRate'] = self.knowledge_hit_rate
        if self.resolution_rate is not None:
            result['ResolutionRate'] = self.resolution_rate
        if self.resolved_question_num is not None:
            result['ResolvedQuestionNum'] = self.resolved_question_num
        if self.statistical_date is not None:
            result['StatisticalDate'] = self.statistical_date
        if self.total_conversation_num is not None:
            result['TotalConversationNum'] = self.total_conversation_num
        if self.valid_answer_rate is not None:
            result['ValidAnswerRate'] = self.valid_answer_rate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DialoguePassRate') is not None:
            self.dialogue_pass_rate = m.get('DialoguePassRate')
        if m.get('KnowledgeHitRate') is not None:
            self.knowledge_hit_rate = m.get('KnowledgeHitRate')
        if m.get('ResolutionRate') is not None:
            self.resolution_rate = m.get('ResolutionRate')
        if m.get('ResolvedQuestionNum') is not None:
            self.resolved_question_num = m.get('ResolvedQuestionNum')
        if m.get('StatisticalDate') is not None:
            self.statistical_date = m.get('StatisticalDate')
        if m.get('TotalConversationNum') is not None:
            self.total_conversation_num = m.get('TotalConversationNum')
        if m.get('ValidAnswerRate') is not None:
            self.valid_answer_rate = m.get('ValidAnswerRate')
        return self


class DescribeStatisticalDataResponseBody(TeaModel):
    def __init__(
        self,
        conversation_total_num: int = None,
        request_id: str = None,
        resolved_question_total_num: int = None,
        statistical_data_reports: List[DescribeStatisticalDataResponseBodyStatisticalDataReports] = None,
        total_dialogue_pass_rate: str = None,
        total_knowledge_hit_rate: str = None,
        total_resolution_rate: str = None,
        total_valid_answer_rate: str = None,
    ):
        self.conversation_total_num = conversation_total_num
        self.request_id = request_id
        self.resolved_question_total_num = resolved_question_total_num
        self.statistical_data_reports = statistical_data_reports
        self.total_dialogue_pass_rate = total_dialogue_pass_rate
        self.total_knowledge_hit_rate = total_knowledge_hit_rate
        self.total_resolution_rate = total_resolution_rate
        self.total_valid_answer_rate = total_valid_answer_rate

    def validate(self):
        if self.statistical_data_reports:
            for k in self.statistical_data_reports:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conversation_total_num is not None:
            result['ConversationTotalNum'] = self.conversation_total_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resolved_question_total_num is not None:
            result['ResolvedQuestionTotalNum'] = self.resolved_question_total_num
        result['StatisticalDataReports'] = []
        if self.statistical_data_reports is not None:
            for k in self.statistical_data_reports:
                result['StatisticalDataReports'].append(k.to_map() if k else None)
        if self.total_dialogue_pass_rate is not None:
            result['TotalDialoguePassRate'] = self.total_dialogue_pass_rate
        if self.total_knowledge_hit_rate is not None:
            result['TotalKnowledgeHitRate'] = self.total_knowledge_hit_rate
        if self.total_resolution_rate is not None:
            result['TotalResolutionRate'] = self.total_resolution_rate
        if self.total_valid_answer_rate is not None:
            result['TotalValidAnswerRate'] = self.total_valid_answer_rate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConversationTotalNum') is not None:
            self.conversation_total_num = m.get('ConversationTotalNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResolvedQuestionTotalNum') is not None:
            self.resolved_question_total_num = m.get('ResolvedQuestionTotalNum')
        self.statistical_data_reports = []
        if m.get('StatisticalDataReports') is not None:
            for k in m.get('StatisticalDataReports'):
                temp_model = DescribeStatisticalDataResponseBodyStatisticalDataReports()
                self.statistical_data_reports.append(temp_model.from_map(k))
        if m.get('TotalDialoguePassRate') is not None:
            self.total_dialogue_pass_rate = m.get('TotalDialoguePassRate')
        if m.get('TotalKnowledgeHitRate') is not None:
            self.total_knowledge_hit_rate = m.get('TotalKnowledgeHitRate')
        if m.get('TotalResolutionRate') is not None:
            self.total_resolution_rate = m.get('TotalResolutionRate')
        if m.get('TotalValidAnswerRate') is not None:
            self.total_valid_answer_rate = m.get('TotalValidAnswerRate')
        return self


class DescribeStatisticalDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeStatisticalDataResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeStatisticalDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTTSConfigRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_owner_id: int = None,
    ):
        self.instance_id = instance_id
        self.instance_owner_id = instance_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_owner_id is not None:
            result['InstanceOwnerId'] = self.instance_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceOwnerId') is not None:
            self.instance_owner_id = m.get('InstanceOwnerId')
        return self


class DescribeTTSConfigResponseBody(TeaModel):
    def __init__(
        self,
        app_key: str = None,
        nls_service_type: str = None,
        request_id: str = None,
        speech_rate: int = None,
        voice: str = None,
        volume: int = None,
    ):
        self.app_key = app_key
        self.nls_service_type = nls_service_type
        self.request_id = request_id
        self.speech_rate = speech_rate
        self.voice = voice
        self.volume = volume

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.nls_service_type is not None:
            result['NlsServiceType'] = self.nls_service_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.speech_rate is not None:
            result['SpeechRate'] = self.speech_rate
        if self.voice is not None:
            result['Voice'] = self.voice
        if self.volume is not None:
            result['Volume'] = self.volume
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('NlsServiceType') is not None:
            self.nls_service_type = m.get('NlsServiceType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SpeechRate') is not None:
            self.speech_rate = m.get('SpeechRate')
        if m.get('Voice') is not None:
            self.voice = m.get('Voice')
        if m.get('Volume') is not None:
            self.volume = m.get('Volume')
        return self


class DescribeTTSConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeTTSConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeTTSConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DialogueRequest(TeaModel):
    def __init__(
        self,
        additional_context: str = None,
        called_number: str = None,
        calling_number: str = None,
        conversation_id: str = None,
        emotion: str = None,
        instance_id: str = None,
        instance_owner_id: int = None,
        utterance: str = None,
    ):
        self.additional_context = additional_context
        self.called_number = called_number
        self.calling_number = calling_number
        self.conversation_id = conversation_id
        self.emotion = emotion
        self.instance_id = instance_id
        self.instance_owner_id = instance_owner_id
        self.utterance = utterance

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.additional_context is not None:
            result['AdditionalContext'] = self.additional_context
        if self.called_number is not None:
            result['CalledNumber'] = self.called_number
        if self.calling_number is not None:
            result['CallingNumber'] = self.calling_number
        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id
        if self.emotion is not None:
            result['Emotion'] = self.emotion
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_owner_id is not None:
            result['InstanceOwnerId'] = self.instance_owner_id
        if self.utterance is not None:
            result['Utterance'] = self.utterance
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdditionalContext') is not None:
            self.additional_context = m.get('AdditionalContext')
        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')
        if m.get('CallingNumber') is not None:
            self.calling_number = m.get('CallingNumber')
        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')
        if m.get('Emotion') is not None:
            self.emotion = m.get('Emotion')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceOwnerId') is not None:
            self.instance_owner_id = m.get('InstanceOwnerId')
        if m.get('Utterance') is not None:
            self.utterance = m.get('Utterance')
        return self


class DialogueResponseBody(TeaModel):
    def __init__(
        self,
        action: str = None,
        action_params: str = None,
        interruptible: bool = None,
        request_id: str = None,
        text_response: str = None,
    ):
        self.action = action
        self.action_params = action_params
        self.interruptible = interruptible
        self.request_id = request_id
        self.text_response = text_response

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.action_params is not None:
            result['ActionParams'] = self.action_params
        if self.interruptible is not None:
            result['Interruptible'] = self.interruptible
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.text_response is not None:
            result['TextResponse'] = self.text_response
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('ActionParams') is not None:
            self.action_params = m.get('ActionParams')
        if m.get('Interruptible') is not None:
            self.interruptible = m.get('Interruptible')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TextResponse') is not None:
            self.text_response = m.get('TextResponse')
        return self


class DialogueResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DialogueResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        request_id: str = None,
        status: str = None,
    ):
        self.request_id = request_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DisableInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DisableInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        request_id: str = None,
        status: str = None,
    ):
        self.request_id = request_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class EnableInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnableInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = EnableInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EndDialogueRequest(TeaModel):
    def __init__(
        self,
        conversation_id: str = None,
        hang_up_params: str = None,
        instance_id: str = None,
        instance_owner_id: int = None,
    ):
        self.conversation_id = conversation_id
        self.hang_up_params = hang_up_params
        self.instance_id = instance_id
        self.instance_owner_id = instance_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id
        if self.hang_up_params is not None:
            result['HangUpParams'] = self.hang_up_params
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_owner_id is not None:
            result['InstanceOwnerId'] = self.instance_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')
        if m.get('HangUpParams') is not None:
            self.hang_up_params = m.get('HangUpParams')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceOwnerId') is not None:
            self.instance_owner_id = m.get('InstanceOwnerId')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: EndDialogueResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = EndDialogueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExportConversationDetailsRequest(TeaModel):
    def __init__(
        self,
        begin_time_left_range: int = None,
        begin_time_right_range: int = None,
        calling_number: str = None,
        instance_id: str = None,
        options: List[str] = None,
        rounds_left_range: int = None,
        rounds_right_range: int = None,
    ):
        self.begin_time_left_range = begin_time_left_range
        self.begin_time_right_range = begin_time_right_range
        self.calling_number = calling_number
        self.instance_id = instance_id
        self.options = options
        self.rounds_left_range = rounds_left_range
        self.rounds_right_range = rounds_right_range

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time_left_range is not None:
            result['BeginTimeLeftRange'] = self.begin_time_left_range
        if self.begin_time_right_range is not None:
            result['BeginTimeRightRange'] = self.begin_time_right_range
        if self.calling_number is not None:
            result['CallingNumber'] = self.calling_number
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.options is not None:
            result['Options'] = self.options
        if self.rounds_left_range is not None:
            result['RoundsLeftRange'] = self.rounds_left_range
        if self.rounds_right_range is not None:
            result['RoundsRightRange'] = self.rounds_right_range
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTimeLeftRange') is not None:
            self.begin_time_left_range = m.get('BeginTimeLeftRange')
        if m.get('BeginTimeRightRange') is not None:
            self.begin_time_right_range = m.get('BeginTimeRightRange')
        if m.get('CallingNumber') is not None:
            self.calling_number = m.get('CallingNumber')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('RoundsLeftRange') is not None:
            self.rounds_left_range = m.get('RoundsLeftRange')
        if m.get('RoundsRightRange') is not None:
            self.rounds_right_range = m.get('RoundsRightRange')
        return self


class ExportConversationDetailsResponseBody(TeaModel):
    def __init__(
        self,
        export_task_id: str = None,
        request_id: str = None,
    ):
        self.export_task_id = export_task_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.export_task_id is not None:
            result['ExportTaskId'] = self.export_task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExportTaskId') is not None:
            self.export_task_id = m.get('ExportTaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ExportConversationDetailsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExportConversationDetailsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ExportConversationDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExportStatisticalDataRequest(TeaModel):
    def __init__(
        self,
        begin_time_left_range: int = None,
        begin_time_right_range: int = None,
        export_type: str = None,
        instance_id: str = None,
        time_unit: str = None,
    ):
        self.begin_time_left_range = begin_time_left_range
        self.begin_time_right_range = begin_time_right_range
        self.export_type = export_type
        self.instance_id = instance_id
        self.time_unit = time_unit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time_left_range is not None:
            result['BeginTimeLeftRange'] = self.begin_time_left_range
        if self.begin_time_right_range is not None:
            result['BeginTimeRightRange'] = self.begin_time_right_range
        if self.export_type is not None:
            result['ExportType'] = self.export_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.time_unit is not None:
            result['TimeUnit'] = self.time_unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTimeLeftRange') is not None:
            self.begin_time_left_range = m.get('BeginTimeLeftRange')
        if m.get('BeginTimeRightRange') is not None:
            self.begin_time_right_range = m.get('BeginTimeRightRange')
        if m.get('ExportType') is not None:
            self.export_type = m.get('ExportType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TimeUnit') is not None:
            self.time_unit = m.get('TimeUnit')
        return self


class ExportStatisticalDataResponseBody(TeaModel):
    def __init__(
        self,
        export_task_id: str = None,
        request_id: str = None,
    ):
        self.export_task_id = export_task_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.export_task_id is not None:
            result['ExportTaskId'] = self.export_task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExportTaskId') is not None:
            self.export_task_id = m.get('ExportTaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ExportStatisticalDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExportStatisticalDataResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ExportStatisticalDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateUploadUrlRequest(TeaModel):
    def __init__(
        self,
        caller_bid: str = None,
        caller_ip: str = None,
        caller_parent_id: int = None,
        caller_type: str = None,
        caller_uid: int = None,
        client_ip: str = None,
        environment: int = None,
        file_name: str = None,
        instance_id: str = None,
        instance_owner_id: int = None,
        key: str = None,
        mfa_present: bool = None,
        proxy_original_security_transport: bool = None,
        proxy_original_source_ip: str = None,
        proxy_trust_transport_info: bool = None,
        request_id: str = None,
        security_token: str = None,
        security_transport: bool = None,
        tenant_id: int = None,
        tenant_name: str = None,
        user_id: int = None,
        user_name: str = None,
        xspace_servicer_id: int = None,
        xspace_tenant_bu_id: int = None,
    ):
        self.caller_bid = caller_bid
        self.caller_ip = caller_ip
        self.caller_parent_id = caller_parent_id
        self.caller_type = caller_type
        self.caller_uid = caller_uid
        self.client_ip = client_ip
        self.environment = environment
        self.file_name = file_name
        self.instance_id = instance_id
        self.instance_owner_id = instance_owner_id
        self.key = key
        self.mfa_present = mfa_present
        self.proxy_original_security_transport = proxy_original_security_transport
        self.proxy_original_source_ip = proxy_original_source_ip
        self.proxy_trust_transport_info = proxy_trust_transport_info
        self.request_id = request_id
        self.security_token = security_token
        self.security_transport = security_transport
        self.tenant_id = tenant_id
        self.tenant_name = tenant_name
        self.user_id = user_id
        self.user_name = user_name
        self.xspace_servicer_id = xspace_servicer_id
        self.xspace_tenant_bu_id = xspace_tenant_bu_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.caller_bid is not None:
            result['CallerBid'] = self.caller_bid
        if self.caller_ip is not None:
            result['CallerIp'] = self.caller_ip
        if self.caller_parent_id is not None:
            result['CallerParentId'] = self.caller_parent_id
        if self.caller_type is not None:
            result['CallerType'] = self.caller_type
        if self.caller_uid is not None:
            result['CallerUid'] = self.caller_uid
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.environment is not None:
            result['Environment'] = self.environment
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_owner_id is not None:
            result['InstanceOwnerId'] = self.instance_owner_id
        if self.key is not None:
            result['Key'] = self.key
        if self.mfa_present is not None:
            result['MfaPresent'] = self.mfa_present
        if self.proxy_original_security_transport is not None:
            result['ProxyOriginalSecurityTransport'] = self.proxy_original_security_transport
        if self.proxy_original_source_ip is not None:
            result['ProxyOriginalSourceIp'] = self.proxy_original_source_ip
        if self.proxy_trust_transport_info is not None:
            result['ProxyTrustTransportInfo'] = self.proxy_trust_transport_info
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.security_transport is not None:
            result['SecurityTransport'] = self.security_transport
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.tenant_name is not None:
            result['TenantName'] = self.tenant_name
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.xspace_servicer_id is not None:
            result['XspaceServicerId'] = self.xspace_servicer_id
        if self.xspace_tenant_bu_id is not None:
            result['XspaceTenantBuId'] = self.xspace_tenant_bu_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallerBid') is not None:
            self.caller_bid = m.get('CallerBid')
        if m.get('CallerIp') is not None:
            self.caller_ip = m.get('CallerIp')
        if m.get('CallerParentId') is not None:
            self.caller_parent_id = m.get('CallerParentId')
        if m.get('CallerType') is not None:
            self.caller_type = m.get('CallerType')
        if m.get('CallerUid') is not None:
            self.caller_uid = m.get('CallerUid')
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('Environment') is not None:
            self.environment = m.get('Environment')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceOwnerId') is not None:
            self.instance_owner_id = m.get('InstanceOwnerId')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('MfaPresent') is not None:
            self.mfa_present = m.get('MfaPresent')
        if m.get('ProxyOriginalSecurityTransport') is not None:
            self.proxy_original_security_transport = m.get('ProxyOriginalSecurityTransport')
        if m.get('ProxyOriginalSourceIp') is not None:
            self.proxy_original_source_ip = m.get('ProxyOriginalSourceIp')
        if m.get('ProxyTrustTransportInfo') is not None:
            self.proxy_trust_transport_info = m.get('ProxyTrustTransportInfo')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('SecurityTransport') is not None:
            self.security_transport = m.get('SecurityTransport')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('TenantName') is not None:
            self.tenant_name = m.get('TenantName')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('XspaceServicerId') is not None:
            self.xspace_servicer_id = m.get('XspaceServicerId')
        if m.get('XspaceTenantBuId') is not None:
            self.xspace_tenant_bu_id = m.get('XspaceTenantBuId')
        return self


class GenerateUploadUrlResponseBodyData(TeaModel):
    def __init__(
        self,
        access_id: str = None,
        expire: int = None,
        folder: str = None,
        host: str = None,
        message: str = None,
        policy: str = None,
        signature: str = None,
        success: bool = None,
    ):
        self.access_id = access_id
        self.expire = expire
        self.folder = folder
        self.host = host
        self.message = message
        self.policy = policy
        self.signature = signature
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_id is not None:
            result['AccessId'] = self.access_id
        if self.expire is not None:
            result['Expire'] = self.expire
        if self.folder is not None:
            result['Folder'] = self.folder
        if self.host is not None:
            result['Host'] = self.host
        if self.message is not None:
            result['Message'] = self.message
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.signature is not None:
            result['Signature'] = self.signature
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')
        if m.get('Expire') is not None:
            self.expire = m.get('Expire')
        if m.get('Folder') is not None:
            self.folder = m.get('Folder')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GenerateUploadUrlResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GenerateUploadUrlResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GenerateUploadUrlResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GenerateUploadUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GenerateUploadUrlResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GenerateUploadUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAsrConfigRequest(TeaModel):
    def __init__(
        self,
        config_level: int = None,
        entry_id: str = None,
    ):
        self.config_level = config_level
        self.entry_id = entry_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_level is not None:
            result['ConfigLevel'] = self.config_level
        if self.entry_id is not None:
            result['EntryId'] = self.entry_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigLevel') is not None:
            self.config_level = m.get('ConfigLevel')
        if m.get('EntryId') is not None:
            self.entry_id = m.get('EntryId')
        return self


class GetAsrConfigResponseBodyData(TeaModel):
    def __init__(
        self,
        asr_acoustic_model_id: str = None,
        asr_class_vocabulary_id: str = None,
        asr_customization_id: str = None,
        asr_vocabulary_id: str = None,
    ):
        self.asr_acoustic_model_id = asr_acoustic_model_id
        self.asr_class_vocabulary_id = asr_class_vocabulary_id
        self.asr_customization_id = asr_customization_id
        self.asr_vocabulary_id = asr_vocabulary_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asr_acoustic_model_id is not None:
            result['AsrAcousticModelId'] = self.asr_acoustic_model_id
        if self.asr_class_vocabulary_id is not None:
            result['AsrClassVocabularyId'] = self.asr_class_vocabulary_id
        if self.asr_customization_id is not None:
            result['AsrCustomizationId'] = self.asr_customization_id
        if self.asr_vocabulary_id is not None:
            result['AsrVocabularyId'] = self.asr_vocabulary_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsrAcousticModelId') is not None:
            self.asr_acoustic_model_id = m.get('AsrAcousticModelId')
        if m.get('AsrClassVocabularyId') is not None:
            self.asr_class_vocabulary_id = m.get('AsrClassVocabularyId')
        if m.get('AsrCustomizationId') is not None:
            self.asr_customization_id = m.get('AsrCustomizationId')
        if m.get('AsrVocabularyId') is not None:
            self.asr_vocabulary_id = m.get('AsrVocabularyId')
        return self


class GetAsrConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetAsrConfigResponseBodyData = None,
        error_msg: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_msg = error_msg
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetAsrConfigResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAsrConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAsrConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAsrConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRealTimeConcurrencyRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetRealTimeConcurrencyResponseBody(TeaModel):
    def __init__(
        self,
        max_concurrency: int = None,
        real_time_concurrency: int = None,
        request_id: str = None,
        timestamp: int = None,
    ):
        self.max_concurrency = max_concurrency
        self.real_time_concurrency = real_time_concurrency
        self.request_id = request_id
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_concurrency is not None:
            result['MaxConcurrency'] = self.max_concurrency
        if self.real_time_concurrency is not None:
            result['RealTimeConcurrency'] = self.real_time_concurrency
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxConcurrency') is not None:
            self.max_concurrency = m.get('MaxConcurrency')
        if m.get('RealTimeConcurrency') is not None:
            self.real_time_concurrency = m.get('RealTimeConcurrency')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class GetRealTimeConcurrencyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRealTimeConcurrencyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetRealTimeConcurrencyResponseBody()
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        avatar: str = None,
        create_time: str = None,
        instance_id: str = None,
        introduction: str = None,
        language_code: str = None,
        name: str = None,
        time_zone: str = None,
    ):
        self.avatar = avatar
        self.create_time = create_time
        self.instance_id = instance_id
        self.introduction = introduction
        self.language_code = language_code
        self.name = name
        self.time_zone = time_zone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar is not None:
            result['Avatar'] = self.avatar
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.introduction is not None:
            result['Introduction'] = self.introduction
        if self.language_code is not None:
            result['LanguageCode'] = self.language_code
        if self.name is not None:
            result['Name'] = self.name
        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Avatar') is not None:
            self.avatar = m.get('Avatar')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Introduction') is not None:
            self.introduction = m.get('Introduction')
        if m.get('LanguageCode') is not None:
            self.language_code = m.get('LanguageCode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')
        return self


class ListChatbotInstancesResponseBody(TeaModel):
    def __init__(
        self,
        bots: List[ListChatbotInstancesResponseBodyBots] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.bots = bots
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.bots:
            for k in self.bots:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Bots'] = []
        if self.bots is not None:
            for k in self.bots:
                result['Bots'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bots = []
        if m.get('Bots') is not None:
            for k in m.get('Bots'):
                temp_model = ListChatbotInstancesResponseBodyBots()
                self.bots.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListChatbotInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListChatbotInstancesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListChatbotInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListConversationDetailsRequest(TeaModel):
    def __init__(
        self,
        conversation_id: str = None,
        instance_id: str = None,
    ):
        self.conversation_id = conversation_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ListConversationDetailsResponseBodyConversationDetails(TeaModel):
    def __init__(
        self,
        action: str = None,
        action_params: str = None,
        conversation_id: str = None,
        create_time: int = None,
        sequence_id: str = None,
        speaker: str = None,
        utterance: str = None,
    ):
        self.action = action
        self.action_params = action_params
        self.conversation_id = conversation_id
        self.create_time = create_time
        self.sequence_id = sequence_id
        self.speaker = speaker
        self.utterance = utterance

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.action_params is not None:
            result['ActionParams'] = self.action_params
        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.sequence_id is not None:
            result['SequenceId'] = self.sequence_id
        if self.speaker is not None:
            result['Speaker'] = self.speaker
        if self.utterance is not None:
            result['Utterance'] = self.utterance
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('ActionParams') is not None:
            self.action_params = m.get('ActionParams')
        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('SequenceId') is not None:
            self.sequence_id = m.get('SequenceId')
        if m.get('Speaker') is not None:
            self.speaker = m.get('Speaker')
        if m.get('Utterance') is not None:
            self.utterance = m.get('Utterance')
        return self


class ListConversationDetailsResponseBody(TeaModel):
    def __init__(
        self,
        conversation_details: List[ListConversationDetailsResponseBodyConversationDetails] = None,
        request_id: str = None,
    ):
        self.conversation_details = conversation_details
        self.request_id = request_id

    def validate(self):
        if self.conversation_details:
            for k in self.conversation_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConversationDetails'] = []
        if self.conversation_details is not None:
            for k in self.conversation_details:
                result['ConversationDetails'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.conversation_details = []
        if m.get('ConversationDetails') is not None:
            for k in m.get('ConversationDetails'):
                temp_model = ListConversationDetailsResponseBodyConversationDetails()
                self.conversation_details.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListConversationDetailsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListConversationDetailsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListConversationDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListConversationsRequest(TeaModel):
    def __init__(
        self,
        begin_time_left_range: int = None,
        begin_time_right_range: int = None,
        calling_number: str = None,
        instance_id: str = None,
        is_sand_box: str = None,
        page_number: int = None,
        page_size: int = None,
        query: str = None,
        result: int = None,
        rounds_left_range: int = None,
        rounds_right_range: int = None,
    ):
        self.begin_time_left_range = begin_time_left_range
        self.begin_time_right_range = begin_time_right_range
        self.calling_number = calling_number
        self.instance_id = instance_id
        self.is_sand_box = is_sand_box
        self.page_number = page_number
        self.page_size = page_size
        self.query = query
        self.result = result
        self.rounds_left_range = rounds_left_range
        self.rounds_right_range = rounds_right_range

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time_left_range is not None:
            result['BeginTimeLeftRange'] = self.begin_time_left_range
        if self.begin_time_right_range is not None:
            result['BeginTimeRightRange'] = self.begin_time_right_range
        if self.calling_number is not None:
            result['CallingNumber'] = self.calling_number
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.is_sand_box is not None:
            result['IsSandBox'] = self.is_sand_box
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query is not None:
            result['Query'] = self.query
        if self.result is not None:
            result['Result'] = self.result
        if self.rounds_left_range is not None:
            result['RoundsLeftRange'] = self.rounds_left_range
        if self.rounds_right_range is not None:
            result['RoundsRightRange'] = self.rounds_right_range
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTimeLeftRange') is not None:
            self.begin_time_left_range = m.get('BeginTimeLeftRange')
        if m.get('BeginTimeRightRange') is not None:
            self.begin_time_right_range = m.get('BeginTimeRightRange')
        if m.get('CallingNumber') is not None:
            self.calling_number = m.get('CallingNumber')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IsSandBox') is not None:
            self.is_sand_box = m.get('IsSandBox')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RoundsLeftRange') is not None:
            self.rounds_left_range = m.get('RoundsLeftRange')
        if m.get('RoundsRightRange') is not None:
            self.rounds_right_range = m.get('RoundsRightRange')
        return self


class ListConversationsResponseBodyConversations(TeaModel):
    def __init__(
        self,
        called_number: str = None,
        calling_number: str = None,
        conversation_id: str = None,
        end_reason: int = None,
        end_time: int = None,
        has_last_playback_completed: bool = None,
        has_to_agent: bool = None,
        rounds: int = None,
        sand_box: bool = None,
        skill_group: str = None,
        start_time: int = None,
    ):
        self.called_number = called_number
        self.calling_number = calling_number
        self.conversation_id = conversation_id
        self.end_reason = end_reason
        self.end_time = end_time
        self.has_last_playback_completed = has_last_playback_completed
        self.has_to_agent = has_to_agent
        self.rounds = rounds
        self.sand_box = sand_box
        self.skill_group = skill_group
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.called_number is not None:
            result['CalledNumber'] = self.called_number
        if self.calling_number is not None:
            result['CallingNumber'] = self.calling_number
        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id
        if self.end_reason is not None:
            result['EndReason'] = self.end_reason
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.has_last_playback_completed is not None:
            result['HasLastPlaybackCompleted'] = self.has_last_playback_completed
        if self.has_to_agent is not None:
            result['HasToAgent'] = self.has_to_agent
        if self.rounds is not None:
            result['Rounds'] = self.rounds
        if self.sand_box is not None:
            result['SandBox'] = self.sand_box
        if self.skill_group is not None:
            result['SkillGroup'] = self.skill_group
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')
        if m.get('CallingNumber') is not None:
            self.calling_number = m.get('CallingNumber')
        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')
        if m.get('EndReason') is not None:
            self.end_reason = m.get('EndReason')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('HasLastPlaybackCompleted') is not None:
            self.has_last_playback_completed = m.get('HasLastPlaybackCompleted')
        if m.get('HasToAgent') is not None:
            self.has_to_agent = m.get('HasToAgent')
        if m.get('Rounds') is not None:
            self.rounds = m.get('Rounds')
        if m.get('SandBox') is not None:
            self.sand_box = m.get('SandBox')
        if m.get('SkillGroup') is not None:
            self.skill_group = m.get('SkillGroup')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ListConversationsResponseBody(TeaModel):
    def __init__(
        self,
        conversations: List[ListConversationsResponseBodyConversations] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.conversations = conversations
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.conversations:
            for k in self.conversations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Conversations'] = []
        if self.conversations is not None:
            for k in self.conversations:
                result['Conversations'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.conversations = []
        if m.get('Conversations') is not None:
            for k in m.get('Conversations'):
                temp_model = ListConversationsResponseBodyConversations()
                self.conversations.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListConversationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListConversationsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListConversationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDownloadTasksRequest(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class ListDownloadTasksResponseBodyDownloadTasksListDownloadTaskFiles(TeaModel):
    def __init__(
        self,
        file_id: str = None,
        progress: int = None,
        status: str = None,
        title: str = None,
    ):
        self.file_id = file_id
        self.progress = progress
        self.status = status
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class ListDownloadTasksResponseBodyDownloadTasksList(TeaModel):
    def __init__(
        self,
        download_task_files: List[ListDownloadTasksResponseBodyDownloadTasksListDownloadTaskFiles] = None,
        expire_time: int = None,
        status: str = None,
        task_id: str = None,
        title: str = None,
    ):
        self.download_task_files = download_task_files
        self.expire_time = expire_time
        self.status = status
        self.task_id = task_id
        self.title = title

    def validate(self):
        if self.download_task_files:
            for k in self.download_task_files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DownloadTaskFiles'] = []
        if self.download_task_files is not None:
            for k in self.download_task_files:
                result['DownloadTaskFiles'].append(k.to_map() if k else None)
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.download_task_files = []
        if m.get('DownloadTaskFiles') is not None:
            for k in m.get('DownloadTaskFiles'):
                temp_model = ListDownloadTasksResponseBodyDownloadTasksListDownloadTaskFiles()
                self.download_task_files.append(temp_model.from_map(k))
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class ListDownloadTasksResponseBodyDownloadTasks(TeaModel):
    def __init__(
        self,
        list: List[ListDownloadTasksResponseBodyDownloadTasksList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.list = list
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = ListDownloadTasksResponseBodyDownloadTasksList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListDownloadTasksResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        download_tasks: ListDownloadTasksResponseBodyDownloadTasks = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.download_tasks = download_tasks
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.download_tasks:
            self.download_tasks.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.download_tasks is not None:
            result['DownloadTasks'] = self.download_tasks.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DownloadTasks') is not None:
            temp_model = ListDownloadTasksResponseBodyDownloadTasks()
            self.download_tasks = temp_model.from_map(m['DownloadTasks'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListDownloadTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDownloadTasksResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDownloadTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstancesRequest(TeaModel):
    def __init__(
        self,
        nlu_service_type_list_json_string: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.nlu_service_type_list_json_string = nlu_service_type_list_json_string
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.nlu_service_type_list_json_string is not None:
            result['NluServiceTypeListJsonString'] = self.nlu_service_type_list_json_string
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NluServiceTypeListJsonString') is not None:
            self.nlu_service_type_list_json_string = m.get('NluServiceTypeListJsonString')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListInstancesResponseBodyInstances(TeaModel):
    def __init__(
        self,
        applicable_operations: List[str] = None,
        concurrency: int = None,
        description: str = None,
        instance_id: str = None,
        modify_time: int = None,
        modify_user_name: str = None,
        name: str = None,
        status: str = None,
    ):
        self.applicable_operations = applicable_operations
        self.concurrency = concurrency
        self.description = description
        self.instance_id = instance_id
        self.modify_time = modify_time
        self.modify_user_name = modify_user_name
        self.name = name
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.applicable_operations is not None:
            result['ApplicableOperations'] = self.applicable_operations
        if self.concurrency is not None:
            result['Concurrency'] = self.concurrency
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name
        if self.name is not None:
            result['Name'] = self.name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicableOperations') is not None:
            self.applicable_operations = m.get('ApplicableOperations')
        if m.get('Concurrency') is not None:
            self.concurrency = m.get('Concurrency')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListInstancesResponseBody(TeaModel):
    def __init__(
        self,
        instances: List[ListInstancesResponseBodyInstances] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.instances = instances
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = ListInstancesResponseBodyInstances()
                self.instances.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListInstancesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAsrConfigRequest(TeaModel):
    def __init__(
        self,
        asr_acoustic_model_id: str = None,
        asr_class_vocabulary_id: str = None,
        asr_customization_id: str = None,
        asr_vocabulary_id: str = None,
        config_level: int = None,
        entry_id: str = None,
    ):
        self.asr_acoustic_model_id = asr_acoustic_model_id
        self.asr_class_vocabulary_id = asr_class_vocabulary_id
        self.asr_customization_id = asr_customization_id
        self.asr_vocabulary_id = asr_vocabulary_id
        self.config_level = config_level
        self.entry_id = entry_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asr_acoustic_model_id is not None:
            result['AsrAcousticModelId'] = self.asr_acoustic_model_id
        if self.asr_class_vocabulary_id is not None:
            result['AsrClassVocabularyId'] = self.asr_class_vocabulary_id
        if self.asr_customization_id is not None:
            result['AsrCustomizationId'] = self.asr_customization_id
        if self.asr_vocabulary_id is not None:
            result['AsrVocabularyId'] = self.asr_vocabulary_id
        if self.config_level is not None:
            result['ConfigLevel'] = self.config_level
        if self.entry_id is not None:
            result['EntryId'] = self.entry_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsrAcousticModelId') is not None:
            self.asr_acoustic_model_id = m.get('AsrAcousticModelId')
        if m.get('AsrClassVocabularyId') is not None:
            self.asr_class_vocabulary_id = m.get('AsrClassVocabularyId')
        if m.get('AsrCustomizationId') is not None:
            self.asr_customization_id = m.get('AsrCustomizationId')
        if m.get('AsrVocabularyId') is not None:
            self.asr_vocabulary_id = m.get('AsrVocabularyId')
        if m.get('ConfigLevel') is not None:
            self.config_level = m.get('ConfigLevel')
        if m.get('EntryId') is not None:
            self.entry_id = m.get('EntryId')
        return self


class ModifyAsrConfigResponseBodyData(TeaModel):
    def __init__(
        self,
        affected_rows: int = None,
    ):
        self.affected_rows = affected_rows

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.affected_rows is not None:
            result['AffectedRows'] = self.affected_rows
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AffectedRows') is not None:
            self.affected_rows = m.get('AffectedRows')
        return self


class ModifyAsrConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ModifyAsrConfigResponseBodyData = None,
        error_msg: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_msg = error_msg
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ModifyAsrConfigResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyAsrConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyAsrConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyAsrConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyGreetingConfigRequest(TeaModel):
    def __init__(
        self,
        greeting_words: str = None,
        instance_id: str = None,
        intent_trigger: str = None,
        source_type: str = None,
    ):
        self.greeting_words = greeting_words
        self.instance_id = instance_id
        self.intent_trigger = intent_trigger
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.greeting_words is not None:
            result['GreetingWords'] = self.greeting_words
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.intent_trigger is not None:
            result['IntentTrigger'] = self.intent_trigger
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GreetingWords') is not None:
            self.greeting_words = m.get('GreetingWords')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IntentTrigger') is not None:
            self.intent_trigger = m.get('IntentTrigger')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: ModifyGreetingConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyGreetingConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceRequest(TeaModel):
    def __init__(
        self,
        concurrency: int = None,
        description: str = None,
        instance_id: str = None,
        name: str = None,
    ):
        self.concurrency = concurrency
        self.description = description
        self.instance_id = instance_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.concurrency is not None:
            result['Concurrency'] = self.concurrency
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Concurrency') is not None:
            self.concurrency = m.get('Concurrency')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: ModifyInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySilenceTimeoutConfigRequest(TeaModel):
    def __init__(
        self,
        final_action: str = None,
        final_action_params: str = None,
        final_prompt: str = None,
        instance_id: str = None,
        intent_trigger: str = None,
        prompt: str = None,
        source_type: str = None,
        threshold: int = None,
        timeout: int = None,
    ):
        self.final_action = final_action
        self.final_action_params = final_action_params
        self.final_prompt = final_prompt
        self.instance_id = instance_id
        self.intent_trigger = intent_trigger
        self.prompt = prompt
        self.source_type = source_type
        self.threshold = threshold
        self.timeout = timeout

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.final_action is not None:
            result['FinalAction'] = self.final_action
        if self.final_action_params is not None:
            result['FinalActionParams'] = self.final_action_params
        if self.final_prompt is not None:
            result['FinalPrompt'] = self.final_prompt
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
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
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
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


class ModifySilenceTimeoutConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: ModifySilenceTimeoutConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifySilenceTimeoutConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyTTSConfigRequest(TeaModel):
    def __init__(
        self,
        app_key: str = None,
        instance_id: str = None,
        nls_service_type: str = None,
        speech_rate: str = None,
        voice: str = None,
        volume: str = None,
    ):
        self.app_key = app_key
        self.instance_id = instance_id
        self.nls_service_type = nls_service_type
        self.speech_rate = speech_rate
        self.voice = voice
        self.volume = volume

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.nls_service_type is not None:
            result['NlsServiceType'] = self.nls_service_type
        if self.speech_rate is not None:
            result['SpeechRate'] = self.speech_rate
        if self.voice is not None:
            result['Voice'] = self.voice
        if self.volume is not None:
            result['Volume'] = self.volume
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NlsServiceType') is not None:
            self.nls_service_type = m.get('NlsServiceType')
        if m.get('SpeechRate') is not None:
            self.speech_rate = m.get('SpeechRate')
        if m.get('Voice') is not None:
            self.voice = m.get('Voice')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: ModifyTTSConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyTTSConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyUnrecognizingConfigRequest(TeaModel):
    def __init__(
        self,
        final_action: str = None,
        final_action_params: str = None,
        final_prompt: str = None,
        instance_id: str = None,
        prompt: str = None,
        threshold: int = None,
    ):
        self.final_action = final_action
        self.final_action_params = final_action_params
        self.final_prompt = final_prompt
        self.instance_id = instance_id
        self.prompt = prompt
        self.threshold = threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.final_action is not None:
            result['FinalAction'] = self.final_action
        if self.final_action_params is not None:
            result['FinalActionParams'] = self.final_action_params
        if self.final_prompt is not None:
            result['FinalPrompt'] = self.final_prompt
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
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
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: ModifyUnrecognizingConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyUnrecognizingConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryConversationsRequest(TeaModel):
    def __init__(
        self,
        begin_time_left_range: int = None,
        begin_time_right_range: int = None,
        calling_number: str = None,
        instance_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.begin_time_left_range = begin_time_left_range
        self.begin_time_right_range = begin_time_right_range
        self.calling_number = calling_number
        self.instance_id = instance_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time_left_range is not None:
            result['BeginTimeLeftRange'] = self.begin_time_left_range
        if self.begin_time_right_range is not None:
            result['BeginTimeRightRange'] = self.begin_time_right_range
        if self.calling_number is not None:
            result['CallingNumber'] = self.calling_number
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTimeLeftRange') is not None:
            self.begin_time_left_range = m.get('BeginTimeLeftRange')
        if m.get('BeginTimeRightRange') is not None:
            self.begin_time_right_range = m.get('BeginTimeRightRange')
        if m.get('CallingNumber') is not None:
            self.calling_number = m.get('CallingNumber')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryConversationsResponseBodyConversations(TeaModel):
    def __init__(
        self,
        begin_time: int = None,
        calling_number: str = None,
        conversation_id: str = None,
        effective_answer_count: int = None,
        end_time: int = None,
        skill_group_id: str = None,
        transferred_to_agent: bool = None,
        user_utterance_count: int = None,
    ):
        self.begin_time = begin_time
        self.calling_number = calling_number
        self.conversation_id = conversation_id
        self.effective_answer_count = effective_answer_count
        self.end_time = end_time
        self.skill_group_id = skill_group_id
        self.transferred_to_agent = transferred_to_agent
        self.user_utterance_count = user_utterance_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.calling_number is not None:
            result['CallingNumber'] = self.calling_number
        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id
        if self.effective_answer_count is not None:
            result['EffectiveAnswerCount'] = self.effective_answer_count
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.skill_group_id is not None:
            result['SkillGroupId'] = self.skill_group_id
        if self.transferred_to_agent is not None:
            result['TransferredToAgent'] = self.transferred_to_agent
        if self.user_utterance_count is not None:
            result['UserUtteranceCount'] = self.user_utterance_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('CallingNumber') is not None:
            self.calling_number = m.get('CallingNumber')
        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')
        if m.get('EffectiveAnswerCount') is not None:
            self.effective_answer_count = m.get('EffectiveAnswerCount')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('SkillGroupId') is not None:
            self.skill_group_id = m.get('SkillGroupId')
        if m.get('TransferredToAgent') is not None:
            self.transferred_to_agent = m.get('TransferredToAgent')
        if m.get('UserUtteranceCount') is not None:
            self.user_utterance_count = m.get('UserUtteranceCount')
        return self


class QueryConversationsResponseBody(TeaModel):
    def __init__(
        self,
        conversations: List[QueryConversationsResponseBodyConversations] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.conversations = conversations
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.conversations:
            for k in self.conversations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Conversations'] = []
        if self.conversations is not None:
            for k in self.conversations:
                result['Conversations'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.conversations = []
        if m.get('Conversations') is not None:
            for k in m.get('Conversations'):
                temp_model = QueryConversationsResponseBodyConversations()
                self.conversations.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QueryConversationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryConversationsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryConversationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveRecordingRequest(TeaModel):
    def __init__(
        self,
        conversation_id: str = None,
        duration: str = None,
        file_name: str = None,
        file_path: str = None,
        instance_id: str = None,
        instance_owner_id: int = None,
        start_time: int = None,
        type: str = None,
        voice_slice_recording_list: str = None,
    ):
        self.conversation_id = conversation_id
        self.duration = duration
        self.file_name = file_name
        self.file_path = file_path
        self.instance_id = instance_id
        self.instance_owner_id = instance_owner_id
        self.start_time = start_time
        self.type = type
        self.voice_slice_recording_list = voice_slice_recording_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_path is not None:
            result['FilePath'] = self.file_path
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_owner_id is not None:
            result['InstanceOwnerId'] = self.instance_owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.type is not None:
            result['Type'] = self.type
        if self.voice_slice_recording_list is not None:
            result['VoiceSliceRecordingList'] = self.voice_slice_recording_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceOwnerId') is not None:
            self.instance_owner_id = m.get('InstanceOwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('VoiceSliceRecordingList') is not None:
            self.voice_slice_recording_list = m.get('VoiceSliceRecordingList')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: SaveRecordingResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SaveRecordingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SilenceTimeoutRequest(TeaModel):
    def __init__(
        self,
        conversation_id: str = None,
        initial_context: str = None,
        instance_id: str = None,
        instance_owner_id: int = None,
    ):
        self.conversation_id = conversation_id
        self.initial_context = initial_context
        self.instance_id = instance_id
        self.instance_owner_id = instance_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id
        if self.initial_context is not None:
            result['InitialContext'] = self.initial_context
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_owner_id is not None:
            result['InstanceOwnerId'] = self.instance_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')
        if m.get('InitialContext') is not None:
            self.initial_context = m.get('InitialContext')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceOwnerId') is not None:
            self.instance_owner_id = m.get('InstanceOwnerId')
        return self


class SilenceTimeoutResponseBody(TeaModel):
    def __init__(
        self,
        action: str = None,
        action_params: str = None,
        interruptible: bool = None,
        request_id: str = None,
        text_response: str = None,
    ):
        self.action = action
        self.action_params = action_params
        self.interruptible = interruptible
        self.request_id = request_id
        self.text_response = text_response

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.action_params is not None:
            result['ActionParams'] = self.action_params
        if self.interruptible is not None:
            result['Interruptible'] = self.interruptible
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.text_response is not None:
            result['TextResponse'] = self.text_response
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('ActionParams') is not None:
            self.action_params = m.get('ActionParams')
        if m.get('Interruptible') is not None:
            self.interruptible = m.get('Interruptible')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TextResponse') is not None:
            self.text_response = m.get('TextResponse')
        return self


class SilenceTimeoutResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SilenceTimeoutResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SilenceTimeoutResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


