# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class ApplyForStreamAccessTokenRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
    ):
        self.agent_key = agent_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        return self


class ApplyForStreamAccessTokenResponseBody(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        channel_id: str = None,
        request_id: str = None,
        stream_secret: str = None,
    ):
        self.access_token = access_token
        self.channel_id = channel_id
        # Id of the request
        self.request_id = request_id
        self.stream_secret = stream_secret

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.stream_secret is not None:
            result['StreamSecret'] = self.stream_secret
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StreamSecret') is not None:
            self.stream_secret = m.get('StreamSecret')
        return self


class ApplyForStreamAccessTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ApplyForStreamAccessTokenResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ApplyForStreamAccessTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssociateRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        instance_id: str = None,
        perspective: List[str] = None,
        recommend_num: int = None,
        session_id: str = None,
        utterance: str = None,
    ):
        self.agent_key = agent_key
        self.instance_id = instance_id
        self.perspective = perspective
        self.recommend_num = recommend_num
        self.session_id = session_id
        self.utterance = utterance

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.perspective is not None:
            result['Perspective'] = self.perspective
        if self.recommend_num is not None:
            result['RecommendNum'] = self.recommend_num
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.utterance is not None:
            result['Utterance'] = self.utterance
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Perspective') is not None:
            self.perspective = m.get('Perspective')
        if m.get('RecommendNum') is not None:
            self.recommend_num = m.get('RecommendNum')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('Utterance') is not None:
            self.utterance = m.get('Utterance')
        return self


class AssociateShrinkRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        instance_id: str = None,
        perspective_shrink: str = None,
        recommend_num: int = None,
        session_id: str = None,
        utterance: str = None,
    ):
        self.agent_key = agent_key
        self.instance_id = instance_id
        self.perspective_shrink = perspective_shrink
        self.recommend_num = recommend_num
        self.session_id = session_id
        self.utterance = utterance

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.perspective_shrink is not None:
            result['Perspective'] = self.perspective_shrink
        if self.recommend_num is not None:
            result['RecommendNum'] = self.recommend_num
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.utterance is not None:
            result['Utterance'] = self.utterance
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Perspective') is not None:
            self.perspective_shrink = m.get('Perspective')
        if m.get('RecommendNum') is not None:
            self.recommend_num = m.get('RecommendNum')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('Utterance') is not None:
            self.utterance = m.get('Utterance')
        return self


class AssociateResponseBodyAssociate(TeaModel):
    def __init__(
        self,
        meta: str = None,
        title: str = None,
    ):
        self.meta = meta
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.meta is not None:
            result['Meta'] = self.meta
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Meta') is not None:
            self.meta = m.get('Meta')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class AssociateResponseBody(TeaModel):
    def __init__(
        self,
        associate: List[AssociateResponseBodyAssociate] = None,
        message_id: str = None,
        request_id: str = None,
        session_id: str = None,
    ):
        self.associate = associate
        self.message_id = message_id
        self.request_id = request_id
        self.session_id = session_id

    def validate(self):
        if self.associate:
            for k in self.associate:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Associate'] = []
        if self.associate is not None:
            for k in self.associate:
                result['Associate'].append(k.to_map() if k else None)
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.associate = []
        if m.get('Associate') is not None:
            for k in m.get('Associate'):
                temp_model = AssociateResponseBodyAssociate()
                self.associate.append(temp_model.from_map(k))
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class AssociateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AssociateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = AssociateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BeginSessionRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        instance_id: str = None,
        sand_box: bool = None,
        vendor_param: str = None,
    ):
        self.agent_key = agent_key
        self.instance_id = instance_id
        self.sand_box = sand_box
        self.vendor_param = vendor_param

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.sand_box is not None:
            result['SandBox'] = self.sand_box
        if self.vendor_param is not None:
            result['VendorParam'] = self.vendor_param
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SandBox') is not None:
            self.sand_box = m.get('SandBox')
        if m.get('VendorParam') is not None:
            self.vendor_param = m.get('VendorParam')
        return self


class BeginSessionResponseBody(TeaModel):
    def __init__(
        self,
        asr_max_end_silence: int = None,
        interruptible: bool = None,
        request_id: str = None,
        silence_reply_timeout: int = None,
        welcome_message: str = None,
    ):
        self.asr_max_end_silence = asr_max_end_silence
        self.interruptible = interruptible
        self.request_id = request_id
        # 静默超时时间
        self.silence_reply_timeout = silence_reply_timeout
        self.welcome_message = welcome_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asr_max_end_silence is not None:
            result['AsrMaxEndSilence'] = self.asr_max_end_silence
        if self.interruptible is not None:
            result['Interruptible'] = self.interruptible
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.silence_reply_timeout is not None:
            result['SilenceReplyTimeout'] = self.silence_reply_timeout
        if self.welcome_message is not None:
            result['WelcomeMessage'] = self.welcome_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsrMaxEndSilence') is not None:
            self.asr_max_end_silence = m.get('AsrMaxEndSilence')
        if m.get('Interruptible') is not None:
            self.interruptible = m.get('Interruptible')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SilenceReplyTimeout') is not None:
            self.silence_reply_timeout = m.get('SilenceReplyTimeout')
        if m.get('WelcomeMessage') is not None:
            self.welcome_message = m.get('WelcomeMessage')
        return self


class BeginSessionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BeginSessionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = BeginSessionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelInstancePublishTaskRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        id: int = None,
        instance_id: str = None,
    ):
        self.agent_key = agent_key
        self.id = id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class CancelInstancePublishTaskResponseBody(TeaModel):
    def __init__(
        self,
        biz_type_list: List[str] = None,
        create_time: str = None,
        error: str = None,
        id: int = None,
        modify_time: str = None,
        request_id: str = None,
        response: str = None,
        status: str = None,
    ):
        self.biz_type_list = biz_type_list
        self.create_time = create_time
        self.error = error
        self.id = id
        self.modify_time = modify_time
        self.request_id = request_id
        self.response = response
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type_list is not None:
            result['BizTypeList'] = self.biz_type_list
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.error is not None:
            result['Error'] = self.error
        if self.id is not None:
            result['Id'] = self.id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response is not None:
            result['Response'] = self.response
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizTypeList') is not None:
            self.biz_type_list = m.get('BizTypeList')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Response') is not None:
            self.response = m.get('Response')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CancelInstancePublishTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelInstancePublishTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CancelInstancePublishTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelPublishTaskRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        id: int = None,
    ):
        self.agent_key = agent_key
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class CancelPublishTaskResponseBody(TeaModel):
    def __init__(
        self,
        biz_type_list: List[str] = None,
        create_time: str = None,
        error: str = None,
        id: int = None,
        modify_time: str = None,
        request_id: str = None,
        response: str = None,
        status: str = None,
    ):
        self.biz_type_list = biz_type_list
        self.create_time = create_time
        self.error = error
        self.id = id
        self.modify_time = modify_time
        self.request_id = request_id
        self.response = response
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type_list is not None:
            result['BizTypeList'] = self.biz_type_list
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.error is not None:
            result['Error'] = self.error
        if self.id is not None:
            result['Id'] = self.id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response is not None:
            result['Response'] = self.response
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizTypeList') is not None:
            self.biz_type_list = m.get('BizTypeList')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Response') is not None:
            self.response = m.get('Response')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CancelPublishTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelPublishTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CancelPublishTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChatRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        instance_id: str = None,
        intent_name: str = None,
        knowledge_id: str = None,
        perspective: List[str] = None,
        sand_box: bool = None,
        sender_id: str = None,
        sender_nick: str = None,
        session_id: str = None,
        utterance: str = None,
        vendor_param: str = None,
    ):
        self.agent_key = agent_key
        self.instance_id = instance_id
        self.intent_name = intent_name
        self.knowledge_id = knowledge_id
        self.perspective = perspective
        self.sand_box = sand_box
        self.sender_id = sender_id
        self.sender_nick = sender_nick
        self.session_id = session_id
        self.utterance = utterance
        self.vendor_param = vendor_param

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.intent_name is not None:
            result['IntentName'] = self.intent_name
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        if self.perspective is not None:
            result['Perspective'] = self.perspective
        if self.sand_box is not None:
            result['SandBox'] = self.sand_box
        if self.sender_id is not None:
            result['SenderId'] = self.sender_id
        if self.sender_nick is not None:
            result['SenderNick'] = self.sender_nick
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.utterance is not None:
            result['Utterance'] = self.utterance
        if self.vendor_param is not None:
            result['VendorParam'] = self.vendor_param
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IntentName') is not None:
            self.intent_name = m.get('IntentName')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        if m.get('Perspective') is not None:
            self.perspective = m.get('Perspective')
        if m.get('SandBox') is not None:
            self.sand_box = m.get('SandBox')
        if m.get('SenderId') is not None:
            self.sender_id = m.get('SenderId')
        if m.get('SenderNick') is not None:
            self.sender_nick = m.get('SenderNick')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('Utterance') is not None:
            self.utterance = m.get('Utterance')
        if m.get('VendorParam') is not None:
            self.vendor_param = m.get('VendorParam')
        return self


class ChatShrinkRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        instance_id: str = None,
        intent_name: str = None,
        knowledge_id: str = None,
        perspective_shrink: str = None,
        sand_box: bool = None,
        sender_id: str = None,
        sender_nick: str = None,
        session_id: str = None,
        utterance: str = None,
        vendor_param: str = None,
    ):
        self.agent_key = agent_key
        self.instance_id = instance_id
        self.intent_name = intent_name
        self.knowledge_id = knowledge_id
        self.perspective_shrink = perspective_shrink
        self.sand_box = sand_box
        self.sender_id = sender_id
        self.sender_nick = sender_nick
        self.session_id = session_id
        self.utterance = utterance
        self.vendor_param = vendor_param

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.intent_name is not None:
            result['IntentName'] = self.intent_name
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        if self.perspective_shrink is not None:
            result['Perspective'] = self.perspective_shrink
        if self.sand_box is not None:
            result['SandBox'] = self.sand_box
        if self.sender_id is not None:
            result['SenderId'] = self.sender_id
        if self.sender_nick is not None:
            result['SenderNick'] = self.sender_nick
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.utterance is not None:
            result['Utterance'] = self.utterance
        if self.vendor_param is not None:
            result['VendorParam'] = self.vendor_param
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IntentName') is not None:
            self.intent_name = m.get('IntentName')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        if m.get('Perspective') is not None:
            self.perspective_shrink = m.get('Perspective')
        if m.get('SandBox') is not None:
            self.sand_box = m.get('SandBox')
        if m.get('SenderId') is not None:
            self.sender_id = m.get('SenderId')
        if m.get('SenderNick') is not None:
            self.sender_nick = m.get('SenderNick')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('Utterance') is not None:
            self.utterance = m.get('Utterance')
        if m.get('VendorParam') is not None:
            self.vendor_param = m.get('VendorParam')
        return self


class ChatResponseBodyMessagesKnowledgeRelatedKnowledges(TeaModel):
    def __init__(
        self,
        knowledge_id: str = None,
        title: str = None,
    ):
        self.knowledge_id = knowledge_id
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class ChatResponseBodyMessagesKnowledge(TeaModel):
    def __init__(
        self,
        answer_source: str = None,
        category: str = None,
        content: str = None,
        content_type: str = None,
        hit_statement: str = None,
        id: str = None,
        related_knowledges: List[ChatResponseBodyMessagesKnowledgeRelatedKnowledges] = None,
        score: float = None,
        summary: str = None,
        title: str = None,
    ):
        self.answer_source = answer_source
        self.category = category
        self.content = content
        self.content_type = content_type
        self.hit_statement = hit_statement
        self.id = id
        self.related_knowledges = related_knowledges
        self.score = score
        self.summary = summary
        self.title = title

    def validate(self):
        if self.related_knowledges:
            for k in self.related_knowledges:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answer_source is not None:
            result['AnswerSource'] = self.answer_source
        if self.category is not None:
            result['Category'] = self.category
        if self.content is not None:
            result['Content'] = self.content
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.hit_statement is not None:
            result['HitStatement'] = self.hit_statement
        if self.id is not None:
            result['Id'] = self.id
        result['RelatedKnowledges'] = []
        if self.related_knowledges is not None:
            for k in self.related_knowledges:
                result['RelatedKnowledges'].append(k.to_map() if k else None)
        if self.score is not None:
            result['Score'] = self.score
        if self.summary is not None:
            result['Summary'] = self.summary
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnswerSource') is not None:
            self.answer_source = m.get('AnswerSource')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('HitStatement') is not None:
            self.hit_statement = m.get('HitStatement')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        self.related_knowledges = []
        if m.get('RelatedKnowledges') is not None:
            for k in m.get('RelatedKnowledges'):
                temp_model = ChatResponseBodyMessagesKnowledgeRelatedKnowledges()
                self.related_knowledges.append(temp_model.from_map(k))
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class ChatResponseBodyMessagesRecommends(TeaModel):
    def __init__(
        self,
        answer_source: str = None,
        knowledge_id: str = None,
        score: float = None,
        title: str = None,
    ):
        self.answer_source = answer_source
        self.knowledge_id = knowledge_id
        self.score = score
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answer_source is not None:
            result['AnswerSource'] = self.answer_source
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        if self.score is not None:
            result['Score'] = self.score
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnswerSource') is not None:
            self.answer_source = m.get('AnswerSource')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class ChatResponseBodyMessagesTextSlots(TeaModel):
    def __init__(
        self,
        hit: bool = None,
        name: str = None,
        origin: str = None,
        value: str = None,
    ):
        self.hit = hit
        self.name = name
        self.origin = origin
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hit is not None:
            result['Hit'] = self.hit
        if self.name is not None:
            result['Name'] = self.name
        if self.origin is not None:
            result['Origin'] = self.origin
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Hit') is not None:
            self.hit = m.get('Hit')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Origin') is not None:
            self.origin = m.get('Origin')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ChatResponseBodyMessagesText(TeaModel):
    def __init__(
        self,
        answer_source: str = None,
        article_title: str = None,
        commands: Dict[str, Any] = None,
        content: str = None,
        content_type: str = None,
        dialog_name: str = None,
        ext: Dict[str, Any] = None,
        external_flags: Dict[str, Any] = None,
        hit_statement: str = None,
        intent_name: str = None,
        meta_data: str = None,
        node_id: str = None,
        node_name: str = None,
        response_type: str = None,
        score: float = None,
        slots: List[ChatResponseBodyMessagesTextSlots] = None,
        user_defined_chat_title: str = None,
    ):
        self.answer_source = answer_source
        self.article_title = article_title
        self.commands = commands
        self.content = content
        self.content_type = content_type
        self.dialog_name = dialog_name
        self.ext = ext
        self.external_flags = external_flags
        self.hit_statement = hit_statement
        self.intent_name = intent_name
        self.meta_data = meta_data
        self.node_id = node_id
        self.node_name = node_name
        self.response_type = response_type
        self.score = score
        self.slots = slots
        self.user_defined_chat_title = user_defined_chat_title

    def validate(self):
        if self.slots:
            for k in self.slots:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answer_source is not None:
            result['AnswerSource'] = self.answer_source
        if self.article_title is not None:
            result['ArticleTitle'] = self.article_title
        if self.commands is not None:
            result['Commands'] = self.commands
        if self.content is not None:
            result['Content'] = self.content
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.dialog_name is not None:
            result['DialogName'] = self.dialog_name
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.external_flags is not None:
            result['ExternalFlags'] = self.external_flags
        if self.hit_statement is not None:
            result['HitStatement'] = self.hit_statement
        if self.intent_name is not None:
            result['IntentName'] = self.intent_name
        if self.meta_data is not None:
            result['MetaData'] = self.meta_data
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.response_type is not None:
            result['ResponseType'] = self.response_type
        if self.score is not None:
            result['Score'] = self.score
        result['Slots'] = []
        if self.slots is not None:
            for k in self.slots:
                result['Slots'].append(k.to_map() if k else None)
        if self.user_defined_chat_title is not None:
            result['UserDefinedChatTitle'] = self.user_defined_chat_title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnswerSource') is not None:
            self.answer_source = m.get('AnswerSource')
        if m.get('ArticleTitle') is not None:
            self.article_title = m.get('ArticleTitle')
        if m.get('Commands') is not None:
            self.commands = m.get('Commands')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('DialogName') is not None:
            self.dialog_name = m.get('DialogName')
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('ExternalFlags') is not None:
            self.external_flags = m.get('ExternalFlags')
        if m.get('HitStatement') is not None:
            self.hit_statement = m.get('HitStatement')
        if m.get('IntentName') is not None:
            self.intent_name = m.get('IntentName')
        if m.get('MetaData') is not None:
            self.meta_data = m.get('MetaData')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('ResponseType') is not None:
            self.response_type = m.get('ResponseType')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        self.slots = []
        if m.get('Slots') is not None:
            for k in m.get('Slots'):
                temp_model = ChatResponseBodyMessagesTextSlots()
                self.slots.append(temp_model.from_map(k))
        if m.get('UserDefinedChatTitle') is not None:
            self.user_defined_chat_title = m.get('UserDefinedChatTitle')
        return self


class ChatResponseBodyMessages(TeaModel):
    def __init__(
        self,
        answer_source: str = None,
        answer_type: str = None,
        knowledge: ChatResponseBodyMessagesKnowledge = None,
        recommends: List[ChatResponseBodyMessagesRecommends] = None,
        text: ChatResponseBodyMessagesText = None,
        title: str = None,
        voice_title: str = None,
    ):
        self.answer_source = answer_source
        self.answer_type = answer_type
        self.knowledge = knowledge
        self.recommends = recommends
        self.text = text
        self.title = title
        self.voice_title = voice_title

    def validate(self):
        if self.knowledge:
            self.knowledge.validate()
        if self.recommends:
            for k in self.recommends:
                if k:
                    k.validate()
        if self.text:
            self.text.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answer_source is not None:
            result['AnswerSource'] = self.answer_source
        if self.answer_type is not None:
            result['AnswerType'] = self.answer_type
        if self.knowledge is not None:
            result['Knowledge'] = self.knowledge.to_map()
        result['Recommends'] = []
        if self.recommends is not None:
            for k in self.recommends:
                result['Recommends'].append(k.to_map() if k else None)
        if self.text is not None:
            result['Text'] = self.text.to_map()
        if self.title is not None:
            result['Title'] = self.title
        if self.voice_title is not None:
            result['VoiceTitle'] = self.voice_title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnswerSource') is not None:
            self.answer_source = m.get('AnswerSource')
        if m.get('AnswerType') is not None:
            self.answer_type = m.get('AnswerType')
        if m.get('Knowledge') is not None:
            temp_model = ChatResponseBodyMessagesKnowledge()
            self.knowledge = temp_model.from_map(m['Knowledge'])
        self.recommends = []
        if m.get('Recommends') is not None:
            for k in m.get('Recommends'):
                temp_model = ChatResponseBodyMessagesRecommends()
                self.recommends.append(temp_model.from_map(k))
        if m.get('Text') is not None:
            temp_model = ChatResponseBodyMessagesText()
            self.text = temp_model.from_map(m['Text'])
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('VoiceTitle') is not None:
            self.voice_title = m.get('VoiceTitle')
        return self


class ChatResponseBody(TeaModel):
    def __init__(
        self,
        message_id: str = None,
        messages: List[ChatResponseBodyMessages] = None,
        query_seg_list: List[str] = None,
        request_id: str = None,
        session_id: str = None,
    ):
        self.message_id = message_id
        self.messages = messages
        self.query_seg_list = query_seg_list
        self.request_id = request_id
        self.session_id = session_id

    def validate(self):
        if self.messages:
            for k in self.messages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        result['Messages'] = []
        if self.messages is not None:
            for k in self.messages:
                result['Messages'].append(k.to_map() if k else None)
        if self.query_seg_list is not None:
            result['QuerySegList'] = self.query_seg_list
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        self.messages = []
        if m.get('Messages') is not None:
            for k in m.get('Messages'):
                temp_model = ChatResponseBodyMessages()
                self.messages.append(temp_model.from_map(k))
        if m.get('QuerySegList') is not None:
            self.query_seg_list = m.get('QuerySegList')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class ChatResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ChatResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ChatResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ContinueInstancePublishTaskRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        id: int = None,
        instance_id: str = None,
    ):
        self.agent_key = agent_key
        self.id = id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ContinueInstancePublishTaskResponseBody(TeaModel):
    def __init__(
        self,
        biz_type_list: List[str] = None,
        create_time: str = None,
        error: str = None,
        errors: Dict[str, Any] = None,
        id: int = None,
        modify_time: str = None,
        request_id: str = None,
        response: str = None,
        status: str = None,
        warnings: Dict[str, Any] = None,
    ):
        self.biz_type_list = biz_type_list
        self.create_time = create_time
        self.error = error
        self.errors = errors
        self.id = id
        self.modify_time = modify_time
        self.request_id = request_id
        self.response = response
        self.status = status
        self.warnings = warnings

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type_list is not None:
            result['BizTypeList'] = self.biz_type_list
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.error is not None:
            result['Error'] = self.error
        if self.errors is not None:
            result['Errors'] = self.errors
        if self.id is not None:
            result['Id'] = self.id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response is not None:
            result['Response'] = self.response
        if self.status is not None:
            result['Status'] = self.status
        if self.warnings is not None:
            result['Warnings'] = self.warnings
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizTypeList') is not None:
            self.biz_type_list = m.get('BizTypeList')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('Errors') is not None:
            self.errors = m.get('Errors')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Response') is not None:
            self.response = m.get('Response')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Warnings') is not None:
            self.warnings = m.get('Warnings')
        return self


class ContinueInstancePublishTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ContinueInstancePublishTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ContinueInstancePublishTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCategoryRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        biz_code: str = None,
        knowledge_type: int = None,
        name: str = None,
        parent_category_id: int = None,
    ):
        self.agent_key = agent_key
        self.biz_code = biz_code
        self.knowledge_type = knowledge_type
        # This parameter is required.
        self.name = name
        self.parent_category_id = parent_category_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.knowledge_type is not None:
            result['KnowledgeType'] = self.knowledge_type
        if self.name is not None:
            result['Name'] = self.name
        if self.parent_category_id is not None:
            result['ParentCategoryId'] = self.parent_category_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('KnowledgeType') is not None:
            self.knowledge_type = m.get('KnowledgeType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParentCategoryId') is not None:
            self.parent_category_id = m.get('ParentCategoryId')
        return self


class CreateCategoryResponseBodyCategory(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
        category_id: int = None,
        name: str = None,
        parent_category_id: int = None,
        status: int = None,
    ):
        self.biz_code = biz_code
        self.category_id = category_id
        self.name = name
        self.parent_category_id = parent_category_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.name is not None:
            result['Name'] = self.name
        if self.parent_category_id is not None:
            result['ParentCategoryId'] = self.parent_category_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParentCategoryId') is not None:
            self.parent_category_id = m.get('ParentCategoryId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateCategoryResponseBody(TeaModel):
    def __init__(
        self,
        category: CreateCategoryResponseBodyCategory = None,
        request_id: str = None,
    ):
        self.category = category
        self.request_id = request_id

    def validate(self):
        if self.category:
            self.category.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            temp_model = CreateCategoryResponseBodyCategory()
            self.category = temp_model.from_map(m['Category'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateCategoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateCategoryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CreateCategoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateConnQuestionRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        conn_question_id: int = None,
        knowledge_id: int = None,
    ):
        self.agent_key = agent_key
        # This parameter is required.
        self.conn_question_id = conn_question_id
        # This parameter is required.
        self.knowledge_id = knowledge_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.conn_question_id is not None:
            result['ConnQuestionId'] = self.conn_question_id
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('ConnQuestionId') is not None:
            self.conn_question_id = m.get('ConnQuestionId')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        return self


class CreateConnQuestionResponseBody(TeaModel):
    def __init__(
        self,
        outline_id: int = None,
        request_id: str = None,
    ):
        self.outline_id = outline_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.outline_id is not None:
            result['OutlineId'] = self.outline_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OutlineId') is not None:
            self.outline_id = m.get('OutlineId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateConnQuestionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateConnQuestionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CreateConnQuestionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDSEntityRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        entity_name: str = None,
        entity_type: str = None,
        instance_id: str = None,
    ):
        self.agent_key = agent_key
        # This parameter is required.
        self.entity_name = entity_name
        self.entity_type = entity_type
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.entity_name is not None:
            result['EntityName'] = self.entity_name
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class CreateDSEntityResponseBody(TeaModel):
    def __init__(
        self,
        entity_id: int = None,
        request_id: str = None,
    ):
        self.entity_id = entity_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDSEntityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDSEntityResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CreateDSEntityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDSEntityValueRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        content: str = None,
        entity_id: int = None,
        instance_id: str = None,
        synonyms: List[str] = None,
    ):
        self.agent_key = agent_key
        # This parameter is required.
        self.content = content
        # This parameter is required.
        self.entity_id = entity_id
        # This parameter is required.
        self.instance_id = instance_id
        self.synonyms = synonyms

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.content is not None:
            result['Content'] = self.content
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.synonyms is not None:
            result['Synonyms'] = self.synonyms
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Synonyms') is not None:
            self.synonyms = m.get('Synonyms')
        return self


class CreateDSEntityValueShrinkRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        content: str = None,
        entity_id: int = None,
        instance_id: str = None,
        synonyms_shrink: str = None,
    ):
        self.agent_key = agent_key
        # This parameter is required.
        self.content = content
        # This parameter is required.
        self.entity_id = entity_id
        # This parameter is required.
        self.instance_id = instance_id
        self.synonyms_shrink = synonyms_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.content is not None:
            result['Content'] = self.content
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.synonyms_shrink is not None:
            result['Synonyms'] = self.synonyms_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Synonyms') is not None:
            self.synonyms_shrink = m.get('Synonyms')
        return self


class CreateDSEntityValueResponseBody(TeaModel):
    def __init__(
        self,
        entity_value_id: int = None,
        request_id: str = None,
    ):
        self.entity_value_id = entity_value_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_value_id is not None:
            result['EntityValueId'] = self.entity_value_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityValueId') is not None:
            self.entity_value_id = m.get('EntityValueId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDSEntityValueResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDSEntityValueResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CreateDSEntityValueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDocRequestDocMetadataMetaCellInfoDTOList(TeaModel):
    def __init__(
        self,
        field_code: str = None,
        field_name: str = None,
        value: str = None,
    ):
        self.field_code = field_code
        self.field_name = field_name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_code is not None:
            result['FieldCode'] = self.field_code
        if self.field_name is not None:
            result['FieldName'] = self.field_name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldCode') is not None:
            self.field_code = m.get('FieldCode')
        if m.get('FieldName') is not None:
            self.field_name = m.get('FieldName')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateDocRequestDocMetadata(TeaModel):
    def __init__(
        self,
        business_view_id: str = None,
        business_view_name: str = None,
        meta_cell_info_dtolist: List[CreateDocRequestDocMetadataMetaCellInfoDTOList] = None,
    ):
        self.business_view_id = business_view_id
        self.business_view_name = business_view_name
        self.meta_cell_info_dtolist = meta_cell_info_dtolist

    def validate(self):
        if self.meta_cell_info_dtolist:
            for k in self.meta_cell_info_dtolist:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_view_id is not None:
            result['BusinessViewId'] = self.business_view_id
        if self.business_view_name is not None:
            result['BusinessViewName'] = self.business_view_name
        result['MetaCellInfoDTOList'] = []
        if self.meta_cell_info_dtolist is not None:
            for k in self.meta_cell_info_dtolist:
                result['MetaCellInfoDTOList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessViewId') is not None:
            self.business_view_id = m.get('BusinessViewId')
        if m.get('BusinessViewName') is not None:
            self.business_view_name = m.get('BusinessViewName')
        self.meta_cell_info_dtolist = []
        if m.get('MetaCellInfoDTOList') is not None:
            for k in m.get('MetaCellInfoDTOList'):
                temp_model = CreateDocRequestDocMetadataMetaCellInfoDTOList()
                self.meta_cell_info_dtolist.append(temp_model.from_map(k))
        return self


class CreateDocRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        category_id: int = None,
        config: str = None,
        content: str = None,
        doc_metadata: List[CreateDocRequestDocMetadata] = None,
        end_date: str = None,
        meta: str = None,
        start_date: str = None,
        tag_ids: List[int] = None,
        title: str = None,
        url: str = None,
    ):
        self.agent_key = agent_key
        # This parameter is required.
        self.category_id = category_id
        self.config = config
        self.content = content
        self.doc_metadata = doc_metadata
        self.end_date = end_date
        self.meta = meta
        self.start_date = start_date
        self.tag_ids = tag_ids
        # This parameter is required.
        self.title = title
        self.url = url

    def validate(self):
        if self.doc_metadata:
            for k in self.doc_metadata:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.config is not None:
            result['Config'] = self.config
        if self.content is not None:
            result['Content'] = self.content
        result['DocMetadata'] = []
        if self.doc_metadata is not None:
            for k in self.doc_metadata:
                result['DocMetadata'].append(k.to_map() if k else None)
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.meta is not None:
            result['Meta'] = self.meta
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.tag_ids is not None:
            result['TagIds'] = self.tag_ids
        if self.title is not None:
            result['Title'] = self.title
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        self.doc_metadata = []
        if m.get('DocMetadata') is not None:
            for k in m.get('DocMetadata'):
                temp_model = CreateDocRequestDocMetadata()
                self.doc_metadata.append(temp_model.from_map(k))
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('Meta') is not None:
            self.meta = m.get('Meta')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('TagIds') is not None:
            self.tag_ids = m.get('TagIds')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class CreateDocShrinkRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        category_id: int = None,
        config: str = None,
        content: str = None,
        doc_metadata_shrink: str = None,
        end_date: str = None,
        meta: str = None,
        start_date: str = None,
        tag_ids_shrink: str = None,
        title: str = None,
        url: str = None,
    ):
        self.agent_key = agent_key
        # This parameter is required.
        self.category_id = category_id
        self.config = config
        self.content = content
        self.doc_metadata_shrink = doc_metadata_shrink
        self.end_date = end_date
        self.meta = meta
        self.start_date = start_date
        self.tag_ids_shrink = tag_ids_shrink
        # This parameter is required.
        self.title = title
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.config is not None:
            result['Config'] = self.config
        if self.content is not None:
            result['Content'] = self.content
        if self.doc_metadata_shrink is not None:
            result['DocMetadata'] = self.doc_metadata_shrink
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.meta is not None:
            result['Meta'] = self.meta
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.tag_ids_shrink is not None:
            result['TagIds'] = self.tag_ids_shrink
        if self.title is not None:
            result['Title'] = self.title
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('DocMetadata') is not None:
            self.doc_metadata_shrink = m.get('DocMetadata')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('Meta') is not None:
            self.meta = m.get('Meta')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('TagIds') is not None:
            self.tag_ids_shrink = m.get('TagIds')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class CreateDocResponseBody(TeaModel):
    def __init__(
        self,
        knowledge_id: int = None,
        request_id: str = None,
    ):
        self.knowledge_id = knowledge_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDocResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDocResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CreateDocResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFaqRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        category_id: int = None,
        end_date: str = None,
        solution_content: str = None,
        solution_type: int = None,
        start_date: str = None,
        tag_id_list: List[int] = None,
        title: str = None,
    ):
        self.agent_key = agent_key
        # This parameter is required.
        self.category_id = category_id
        self.end_date = end_date
        self.solution_content = solution_content
        self.solution_type = solution_type
        self.start_date = start_date
        self.tag_id_list = tag_id_list
        # This parameter is required.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.solution_content is not None:
            result['SolutionContent'] = self.solution_content
        if self.solution_type is not None:
            result['SolutionType'] = self.solution_type
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.tag_id_list is not None:
            result['TagIdList'] = self.tag_id_list
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('SolutionContent') is not None:
            self.solution_content = m.get('SolutionContent')
        if m.get('SolutionType') is not None:
            self.solution_type = m.get('SolutionType')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('TagIdList') is not None:
            self.tag_id_list = m.get('TagIdList')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class CreateFaqShrinkRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        category_id: int = None,
        end_date: str = None,
        solution_content: str = None,
        solution_type: int = None,
        start_date: str = None,
        tag_id_list_shrink: str = None,
        title: str = None,
    ):
        self.agent_key = agent_key
        # This parameter is required.
        self.category_id = category_id
        self.end_date = end_date
        self.solution_content = solution_content
        self.solution_type = solution_type
        self.start_date = start_date
        self.tag_id_list_shrink = tag_id_list_shrink
        # This parameter is required.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.solution_content is not None:
            result['SolutionContent'] = self.solution_content
        if self.solution_type is not None:
            result['SolutionType'] = self.solution_type
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.tag_id_list_shrink is not None:
            result['TagIdList'] = self.tag_id_list_shrink
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('SolutionContent') is not None:
            self.solution_content = m.get('SolutionContent')
        if m.get('SolutionType') is not None:
            self.solution_type = m.get('SolutionType')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('TagIdList') is not None:
            self.tag_id_list_shrink = m.get('TagIdList')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class CreateFaqResponseBody(TeaModel):
    def __init__(
        self,
        knowledge_id: int = None,
        request_id: str = None,
    ):
        self.knowledge_id = knowledge_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateFaqResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateFaqResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CreateFaqResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateInstanceRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        introduction: str = None,
        language_code: str = None,
        name: str = None,
        robot_type: str = None,
    ):
        self.agent_key = agent_key
        self.introduction = introduction
        self.language_code = language_code
        self.name = name
        self.robot_type = robot_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.introduction is not None:
            result['Introduction'] = self.introduction
        if self.language_code is not None:
            result['LanguageCode'] = self.language_code
        if self.name is not None:
            result['Name'] = self.name
        if self.robot_type is not None:
            result['RobotType'] = self.robot_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Introduction') is not None:
            self.introduction = m.get('Introduction')
        if m.get('LanguageCode') is not None:
            self.language_code = m.get('LanguageCode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RobotType') is not None:
            self.robot_type = m.get('RobotType')
        return self


class CreateInstanceResponseBody(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        request_id: str = None,
    ):
        self.instance_id = instance_id
        # Id of the request
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


class CreateInstancePublishTaskRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        instance_id: str = None,
    ):
        self.agent_key = agent_key
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class CreateInstancePublishTaskResponseBody(TeaModel):
    def __init__(
        self,
        biz_type_list: List[str] = None,
        create_time: str = None,
        error: str = None,
        id: int = None,
        modify_time: str = None,
        request_id: str = None,
        response: str = None,
        status: str = None,
    ):
        self.biz_type_list = biz_type_list
        self.create_time = create_time
        self.error = error
        self.id = id
        self.modify_time = modify_time
        self.request_id = request_id
        self.response = response
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type_list is not None:
            result['BizTypeList'] = self.biz_type_list
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.error is not None:
            result['Error'] = self.error
        if self.id is not None:
            result['Id'] = self.id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response is not None:
            result['Response'] = self.response
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizTypeList') is not None:
            self.biz_type_list = m.get('BizTypeList')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Response') is not None:
            self.response = m.get('Response')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateInstancePublishTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateInstancePublishTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CreateInstancePublishTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateIntentRequestIntentDefinitionSlotInfos(TeaModel):
    def __init__(
        self,
        array: bool = None,
        encrypt: bool = None,
        interactive: bool = None,
        name: str = None,
        slot_id: str = None,
        value: str = None,
    ):
        self.array = array
        self.encrypt = encrypt
        self.interactive = interactive
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.slot_id = slot_id
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.array is not None:
            result['Array'] = self.array
        if self.encrypt is not None:
            result['Encrypt'] = self.encrypt
        if self.interactive is not None:
            result['Interactive'] = self.interactive
        if self.name is not None:
            result['Name'] = self.name
        if self.slot_id is not None:
            result['SlotId'] = self.slot_id
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Array') is not None:
            self.array = m.get('Array')
        if m.get('Encrypt') is not None:
            self.encrypt = m.get('Encrypt')
        if m.get('Interactive') is not None:
            self.interactive = m.get('Interactive')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SlotId') is not None:
            self.slot_id = m.get('SlotId')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateIntentRequestIntentDefinition(TeaModel):
    def __init__(
        self,
        alias_name: str = None,
        intent_name: str = None,
        slot_infos: List[CreateIntentRequestIntentDefinitionSlotInfos] = None,
    ):
        self.alias_name = alias_name
        # This parameter is required.
        self.intent_name = intent_name
        self.slot_infos = slot_infos

    def validate(self):
        if self.slot_infos:
            for k in self.slot_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name
        if self.intent_name is not None:
            result['IntentName'] = self.intent_name
        result['SlotInfos'] = []
        if self.slot_infos is not None:
            for k in self.slot_infos:
                result['SlotInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')
        if m.get('IntentName') is not None:
            self.intent_name = m.get('IntentName')
        self.slot_infos = []
        if m.get('SlotInfos') is not None:
            for k in m.get('SlotInfos'):
                temp_model = CreateIntentRequestIntentDefinitionSlotInfos()
                self.slot_infos.append(temp_model.from_map(k))
        return self


class CreateIntentRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        instance_id: str = None,
        intent_definition: CreateIntentRequestIntentDefinition = None,
    ):
        self.agent_key = agent_key
        # This parameter is required.
        self.instance_id = instance_id
        self.intent_definition = intent_definition

    def validate(self):
        if self.intent_definition:
            self.intent_definition.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.intent_definition is not None:
            result['IntentDefinition'] = self.intent_definition.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IntentDefinition') is not None:
            temp_model = CreateIntentRequestIntentDefinition()
            self.intent_definition = temp_model.from_map(m['IntentDefinition'])
        return self


class CreateIntentShrinkRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        instance_id: str = None,
        intent_definition_shrink: str = None,
    ):
        self.agent_key = agent_key
        # This parameter is required.
        self.instance_id = instance_id
        self.intent_definition_shrink = intent_definition_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.intent_definition_shrink is not None:
            result['IntentDefinition'] = self.intent_definition_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IntentDefinition') is not None:
            self.intent_definition_shrink = m.get('IntentDefinition')
        return self


class CreateIntentResponseBody(TeaModel):
    def __init__(
        self,
        intent_id: int = None,
        request_id: str = None,
    ):
        self.intent_id = intent_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateIntentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateIntentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CreateIntentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLgfRequestLgfDefinition(TeaModel):
    def __init__(
        self,
        intent_id: int = None,
        rule_text: str = None,
    ):
        # This parameter is required.
        self.intent_id = intent_id
        # This parameter is required.
        self.rule_text = rule_text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        if self.rule_text is not None:
            result['RuleText'] = self.rule_text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        if m.get('RuleText') is not None:
            self.rule_text = m.get('RuleText')
        return self


class CreateLgfRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        instance_id: str = None,
        lgf_definition: CreateLgfRequestLgfDefinition = None,
    ):
        self.agent_key = agent_key
        # This parameter is required.
        self.instance_id = instance_id
        self.lgf_definition = lgf_definition

    def validate(self):
        if self.lgf_definition:
            self.lgf_definition.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lgf_definition is not None:
            result['LgfDefinition'] = self.lgf_definition.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LgfDefinition') is not None:
            temp_model = CreateLgfRequestLgfDefinition()
            self.lgf_definition = temp_model.from_map(m['LgfDefinition'])
        return self


class CreateLgfShrinkRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        instance_id: str = None,
        lgf_definition_shrink: str = None,
    ):
        self.agent_key = agent_key
        # This parameter is required.
        self.instance_id = instance_id
        self.lgf_definition_shrink = lgf_definition_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lgf_definition_shrink is not None:
            result['LgfDefinition'] = self.lgf_definition_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LgfDefinition') is not None:
            self.lgf_definition_shrink = m.get('LgfDefinition')
        return self


class CreateLgfResponseBody(TeaModel):
    def __init__(
        self,
        lgf_id: int = None,
        request_id: str = None,
    ):
        # LGF ID
        self.lgf_id = lgf_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lgf_id is not None:
            result['LgfId'] = self.lgf_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LgfId') is not None:
            self.lgf_id = m.get('LgfId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateLgfResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateLgfResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CreateLgfResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePerspectiveRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        description: str = None,
        name: str = None,
    ):
        self.agent_key = agent_key
        self.description = description
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreatePerspectiveResponseBody(TeaModel):
    def __init__(
        self,
        perspective_id: str = None,
        request_id: str = None,
    ):
        self.perspective_id = perspective_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.perspective_id is not None:
            result['PerspectiveId'] = self.perspective_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PerspectiveId') is not None:
            self.perspective_id = m.get('PerspectiveId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreatePerspectiveResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreatePerspectiveResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CreatePerspectiveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePublishTaskRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        biz_type: str = None,
        data_id_list: List[str] = None,
    ):
        self.agent_key = agent_key
        self.biz_type = biz_type
        self.data_id_list = data_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.data_id_list is not None:
            result['DataIdList'] = self.data_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('DataIdList') is not None:
            self.data_id_list = m.get('DataIdList')
        return self


class CreatePublishTaskShrinkRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        biz_type: str = None,
        data_id_list_shrink: str = None,
    ):
        self.agent_key = agent_key
        self.biz_type = biz_type
        self.data_id_list_shrink = data_id_list_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.data_id_list_shrink is not None:
            result['DataIdList'] = self.data_id_list_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('DataIdList') is not None:
            self.data_id_list_shrink = m.get('DataIdList')
        return self


class CreatePublishTaskResponseBody(TeaModel):
    def __init__(
        self,
        biz_type_list: List[str] = None,
        create_time: str = None,
        error: str = None,
        id: int = None,
        modify_time: str = None,
        request_id: str = None,
        response: str = None,
        status: str = None,
    ):
        self.biz_type_list = biz_type_list
        self.create_time = create_time
        self.error = error
        self.id = id
        self.modify_time = modify_time
        self.request_id = request_id
        self.response = response
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type_list is not None:
            result['BizTypeList'] = self.biz_type_list
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.error is not None:
            result['Error'] = self.error
        if self.id is not None:
            result['Id'] = self.id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response is not None:
            result['Response'] = self.response
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizTypeList') is not None:
            self.biz_type_list = m.get('BizTypeList')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Response') is not None:
            self.response = m.get('Response')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreatePublishTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreatePublishTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CreatePublishTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSimQuestionRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        knowledge_id: int = None,
        title: str = None,
    ):
        self.agent_key = agent_key
        # This parameter is required.
        self.knowledge_id = knowledge_id
        # This parameter is required.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class CreateSimQuestionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        sim_question_id: int = None,
    ):
        self.request_id = request_id
        self.sim_question_id = sim_question_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sim_question_id is not None:
            result['SimQuestionId'] = self.sim_question_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SimQuestionId') is not None:
            self.sim_question_id = m.get('SimQuestionId')
        return self


class CreateSimQuestionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateSimQuestionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CreateSimQuestionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSolutionRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        content: str = None,
        content_type: int = None,
        knowledge_id: int = None,
        perspective_codes: List[str] = None,
        tag_id_list: List[int] = None,
    ):
        self.agent_key = agent_key
        # This parameter is required.
        self.content = content
        self.content_type = content_type
        # This parameter is required.
        self.knowledge_id = knowledge_id
        # This parameter is required.
        self.perspective_codes = perspective_codes
        self.tag_id_list = tag_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.content is not None:
            result['Content'] = self.content
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        if self.perspective_codes is not None:
            result['PerspectiveCodes'] = self.perspective_codes
        if self.tag_id_list is not None:
            result['TagIdList'] = self.tag_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        if m.get('PerspectiveCodes') is not None:
            self.perspective_codes = m.get('PerspectiveCodes')
        if m.get('TagIdList') is not None:
            self.tag_id_list = m.get('TagIdList')
        return self


class CreateSolutionShrinkRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        content: str = None,
        content_type: int = None,
        knowledge_id: int = None,
        perspective_codes: List[str] = None,
        tag_id_list_shrink: str = None,
    ):
        self.agent_key = agent_key
        # This parameter is required.
        self.content = content
        self.content_type = content_type
        # This parameter is required.
        self.knowledge_id = knowledge_id
        # This parameter is required.
        self.perspective_codes = perspective_codes
        self.tag_id_list_shrink = tag_id_list_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.content is not None:
            result['Content'] = self.content
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        if self.perspective_codes is not None:
            result['PerspectiveCodes'] = self.perspective_codes
        if self.tag_id_list_shrink is not None:
            result['TagIdList'] = self.tag_id_list_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        if m.get('PerspectiveCodes') is not None:
            self.perspective_codes = m.get('PerspectiveCodes')
        if m.get('TagIdList') is not None:
            self.tag_id_list_shrink = m.get('TagIdList')
        return self


class CreateSolutionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        solution_id: int = None,
    ):
        self.request_id = request_id
        self.solution_id = solution_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.solution_id is not None:
            result['SolutionId'] = self.solution_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SolutionId') is not None:
            self.solution_id = m.get('SolutionId')
        return self


class CreateSolutionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateSolutionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CreateSolutionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTagRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        client_token: str = None,
        group_id: int = None,
        tag_name: str = None,
    ):
        self.agent_key = agent_key
        self.client_token = client_token
        # This parameter is required.
        self.group_id = group_id
        # This parameter is required.
        self.tag_name = tag_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        return self


class CreateTagResponseBody(TeaModel):
    def __init__(
        self,
        id: int = None,
        request_id: str = None,
    ):
        self.id = id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateTagResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateTagResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CreateTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTagGroupRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        client_token: str = None,
        group_name: str = None,
    ):
        self.agent_key = agent_key
        self.client_token = client_token
        # This parameter is required.
        self.group_name = group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        return self


class CreateTagGroupResponseBody(TeaModel):
    def __init__(
        self,
        id: int = None,
        request_id: str = None,
    ):
        self.id = id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateTagGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateTagGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CreateTagGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUserSayRequestUserSayDefinitionSlotInfos(TeaModel):
    def __init__(
        self,
        end_index: int = None,
        slot_id: str = None,
        start_index: int = None,
    ):
        self.end_index = end_index
        self.slot_id = slot_id
        self.start_index = start_index

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_index is not None:
            result['EndIndex'] = self.end_index
        if self.slot_id is not None:
            result['SlotId'] = self.slot_id
        if self.start_index is not None:
            result['StartIndex'] = self.start_index
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndIndex') is not None:
            self.end_index = m.get('EndIndex')
        if m.get('SlotId') is not None:
            self.slot_id = m.get('SlotId')
        if m.get('StartIndex') is not None:
            self.start_index = m.get('StartIndex')
        return self


class CreateUserSayRequestUserSayDefinition(TeaModel):
    def __init__(
        self,
        content: str = None,
        intent_id: int = None,
        slot_infos: List[CreateUserSayRequestUserSayDefinitionSlotInfos] = None,
    ):
        # This parameter is required.
        self.content = content
        # This parameter is required.
        self.intent_id = intent_id
        self.slot_infos = slot_infos

    def validate(self):
        if self.slot_infos:
            for k in self.slot_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        result['SlotInfos'] = []
        if self.slot_infos is not None:
            for k in self.slot_infos:
                result['SlotInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        self.slot_infos = []
        if m.get('SlotInfos') is not None:
            for k in m.get('SlotInfos'):
                temp_model = CreateUserSayRequestUserSayDefinitionSlotInfos()
                self.slot_infos.append(temp_model.from_map(k))
        return self


class CreateUserSayRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        instance_id: str = None,
        user_say_definition: CreateUserSayRequestUserSayDefinition = None,
    ):
        self.agent_key = agent_key
        # This parameter is required.
        self.instance_id = instance_id
        self.user_say_definition = user_say_definition

    def validate(self):
        if self.user_say_definition:
            self.user_say_definition.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.user_say_definition is not None:
            result['UserSayDefinition'] = self.user_say_definition.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('UserSayDefinition') is not None:
            temp_model = CreateUserSayRequestUserSayDefinition()
            self.user_say_definition = temp_model.from_map(m['UserSayDefinition'])
        return self


class CreateUserSayShrinkRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        instance_id: str = None,
        user_say_definition_shrink: str = None,
    ):
        self.agent_key = agent_key
        # This parameter is required.
        self.instance_id = instance_id
        self.user_say_definition_shrink = user_say_definition_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.user_say_definition_shrink is not None:
            result['UserSayDefinition'] = self.user_say_definition_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('UserSayDefinition') is not None:
            self.user_say_definition_shrink = m.get('UserSayDefinition')
        return self


class CreateUserSayResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        user_say_id: int = None,
    ):
        self.request_id = request_id
        self.user_say_id = user_say_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user_say_id is not None:
            result['UserSayId'] = self.user_say_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UserSayId') is not None:
            self.user_say_id = m.get('UserSayId')
        return self


class CreateUserSayResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateUserSayResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CreateUserSayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCategoryRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        category_id: int = None,
    ):
        self.agent_key = agent_key
        # This parameter is required.
        self.category_id = category_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        return self


class DeleteCategoryResponseBody(TeaModel):
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


class DeleteCategoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteCategoryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeleteCategoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteConnQuestionRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        outline_id: int = None,
    ):
        self.agent_key = agent_key
        # This parameter is required.
        self.outline_id = outline_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.outline_id is not None:
            result['OutlineId'] = self.outline_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('OutlineId') is not None:
            self.outline_id = m.get('OutlineId')
        return self


class DeleteConnQuestionResponseBody(TeaModel):
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


class DeleteConnQuestionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteConnQuestionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeleteConnQuestionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDSEntityRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        entity_id: int = None,
        instance_id: str = None,
    ):
        self.agent_key = agent_key
        # This parameter is required.
        self.entity_id = entity_id
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DeleteDSEntityResponseBody(TeaModel):
    def __init__(
        self,
        entity_id: int = None,
        request_id: str = None,
    ):
        self.entity_id = entity_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteDSEntityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDSEntityResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeleteDSEntityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDSEntityValueRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        entity_id: int = None,
        entity_value_id: int = None,
        instance_id: str = None,
    ):
        self.agent_key = agent_key
        # This parameter is required.
        self.entity_id = entity_id
        # This parameter is required.
        self.entity_value_id = entity_value_id
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.entity_value_id is not None:
            result['EntityValueId'] = self.entity_value_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('EntityValueId') is not None:
            self.entity_value_id = m.get('EntityValueId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DeleteDSEntityValueResponseBody(TeaModel):
    def __init__(
        self,
        entity_value_id: int = None,
        request_id: str = None,
    ):
        self.entity_value_id = entity_value_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_value_id is not None:
            result['EntityValueId'] = self.entity_value_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityValueId') is not None:
            self.entity_value_id = m.get('EntityValueId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteDSEntityValueResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDSEntityValueResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeleteDSEntityValueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDocRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        knowledge_id: int = None,
    ):
        self.agent_key = agent_key
        # This parameter is required.
        self.knowledge_id = knowledge_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        return self


class DeleteDocResponseBody(TeaModel):
    def __init__(
        self,
        knowledge_id: int = None,
        request_id: str = None,
    ):
        self.knowledge_id = knowledge_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteDocResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDocResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeleteDocResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFaqRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        knowledge_id: int = None,
    ):
        self.agent_key = agent_key
        # This parameter is required.
        self.knowledge_id = knowledge_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        return self


class DeleteFaqResponseBody(TeaModel):
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


class DeleteFaqResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteFaqResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeleteFaqResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteInstanceRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        instance_id: str = None,
    ):
        self.agent_key = agent_key
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DeleteInstanceResponseBody(TeaModel):
    def __init__(
        self,
        biz_type_list: List[str] = None,
        create_time: str = None,
        create_user_id: int = None,
        create_user_name: str = None,
        error: str = None,
        id: int = None,
        request_id: str = None,
        response: int = None,
        status: str = None,
    ):
        self.biz_type_list = biz_type_list
        self.create_time = create_time
        self.create_user_id = create_user_id
        self.create_user_name = create_user_name
        self.error = error
        self.id = id
        self.request_id = request_id
        self.response = response
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type_list is not None:
            result['BizTypeList'] = self.biz_type_list
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.error is not None:
            result['Error'] = self.error
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response is not None:
            result['Response'] = self.response
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizTypeList') is not None:
            self.biz_type_list = m.get('BizTypeList')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Response') is not None:
            self.response = m.get('Response')
        if m.get('Status') is not None:
            self.status = m.get('Status')
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


class DeleteIntentRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        instance_id: str = None,
        intent_id: int = None,
    ):
        self.agent_key = agent_key
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.intent_id = intent_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        return self


class DeleteIntentResponseBody(TeaModel):
    def __init__(
        self,
        intent_id: int = None,
        request_id: str = None,
    ):
        self.intent_id = intent_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteIntentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteIntentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeleteIntentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteLgfRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        instance_id: str = None,
        intent_id: int = None,
        lgf_id: int = None,
    ):
        self.agent_key = agent_key
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.intent_id = intent_id
        # lgf Id
        # 
        # This parameter is required.
        self.lgf_id = lgf_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        if self.lgf_id is not None:
            result['LgfId'] = self.lgf_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        if m.get('LgfId') is not None:
            self.lgf_id = m.get('LgfId')
        return self


class DeleteLgfResponseBody(TeaModel):
    def __init__(
        self,
        lgf_id: int = None,
        request_id: str = None,
    ):
        # LGF ID
        self.lgf_id = lgf_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lgf_id is not None:
            result['LgfId'] = self.lgf_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LgfId') is not None:
            self.lgf_id = m.get('LgfId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteLgfResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteLgfResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeleteLgfResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePerspectiveRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        perspective_id: str = None,
    ):
        self.agent_key = agent_key
        self.perspective_id = perspective_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.perspective_id is not None:
            result['PerspectiveId'] = self.perspective_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('PerspectiveId') is not None:
            self.perspective_id = m.get('PerspectiveId')
        return self


class DeletePerspectiveResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class DeletePerspectiveResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeletePerspectiveResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeletePerspectiveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSimQuestionRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        sim_question_id: int = None,
    ):
        self.agent_key = agent_key
        # This parameter is required.
        self.sim_question_id = sim_question_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.sim_question_id is not None:
            result['SimQuestionId'] = self.sim_question_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('SimQuestionId') is not None:
            self.sim_question_id = m.get('SimQuestionId')
        return self


class DeleteSimQuestionResponseBody(TeaModel):
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


class DeleteSimQuestionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteSimQuestionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeleteSimQuestionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSolutionRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        solution_id: int = None,
    ):
        self.agent_key = agent_key
        # This parameter is required.
        self.solution_id = solution_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.solution_id is not None:
            result['SolutionId'] = self.solution_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('SolutionId') is not None:
            self.solution_id = m.get('SolutionId')
        return self


class DeleteSolutionResponseBody(TeaModel):
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


class DeleteSolutionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteSolutionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeleteSolutionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTagRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        client_token: str = None,
        group_id: int = None,
        id: int = None,
    ):
        self.agent_key = agent_key
        self.client_token = client_token
        # This parameter is required.
        self.group_id = group_id
        # This parameter is required.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteTagResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteTagResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteTagResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeleteTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTagGroupRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        client_token: str = None,
        id: int = None,
    ):
        self.agent_key = agent_key
        self.client_token = client_token
        # This parameter is required.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteTagGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteTagGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteTagGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeleteTagGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUserSayRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        instance_id: str = None,
        intent_id: int = None,
        user_say_id: int = None,
    ):
        self.agent_key = agent_key
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.intent_id = intent_id
        # This parameter is required.
        self.user_say_id = user_say_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        if self.user_say_id is not None:
            result['UserSayId'] = self.user_say_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        if m.get('UserSayId') is not None:
            self.user_say_id = m.get('UserSayId')
        return self


class DeleteUserSayResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        user_say_id: int = None,
    ):
        self.request_id = request_id
        self.user_say_id = user_say_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user_say_id is not None:
            result['UserSayId'] = self.user_say_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UserSayId') is not None:
            self.user_say_id = m.get('UserSayId')
        return self


class DeleteUserSayResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteUserSayResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeleteUserSayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCategoryRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        category_id: int = None,
    ):
        self.agent_key = agent_key
        # This parameter is required.
        self.category_id = category_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        return self


class DescribeCategoryResponseBodyCategory(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
        category_id: int = None,
        name: str = None,
        parent_category_id: int = None,
        status: int = None,
    ):
        self.biz_code = biz_code
        self.category_id = category_id
        self.name = name
        self.parent_category_id = parent_category_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.name is not None:
            result['Name'] = self.name
        if self.parent_category_id is not None:
            result['ParentCategoryId'] = self.parent_category_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParentCategoryId') is not None:
            self.parent_category_id = m.get('ParentCategoryId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeCategoryResponseBody(TeaModel):
    def __init__(
        self,
        category: DescribeCategoryResponseBodyCategory = None,
        request_id: str = None,
    ):
        self.category = category
        self.request_id = request_id

    def validate(self):
        if self.category:
            self.category.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            temp_model = DescribeCategoryResponseBodyCategory()
            self.category = temp_model.from_map(m['Category'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCategoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCategoryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeCategoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDSEntityRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        entity_id: int = None,
        instance_id: str = None,
    ):
        self.agent_key = agent_key
        # This parameter is required.
        self.entity_id = entity_id
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeDSEntityResponseBody(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        create_user_id: str = None,
        create_user_name: str = None,
        entity_id: int = None,
        entity_name: str = None,
        entity_type: str = None,
        modify_time: str = None,
        modify_user_id: str = None,
        modify_user_name: str = None,
        request_id: str = None,
        sys_entity_code: str = None,
    ):
        self.create_time = create_time
        self.create_user_id = create_user_id
        self.create_user_name = create_user_name
        self.entity_id = entity_id
        self.entity_name = entity_name
        self.entity_type = entity_type
        self.modify_time = modify_time
        self.modify_user_id = modify_user_id
        self.modify_user_name = modify_user_name
        self.request_id = request_id
        self.sys_entity_code = sys_entity_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.entity_name is not None:
            result['EntityName'] = self.entity_name
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.modify_user_id is not None:
            result['ModifyUserId'] = self.modify_user_id
        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sys_entity_code is not None:
            result['SysEntityCode'] = self.sys_entity_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ModifyUserId') is not None:
            self.modify_user_id = m.get('ModifyUserId')
        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SysEntityCode') is not None:
            self.sys_entity_code = m.get('SysEntityCode')
        return self


class DescribeDSEntityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDSEntityResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeDSEntityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDocRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        knowledge_id: int = None,
        show_detail: bool = None,
    ):
        self.agent_key = agent_key
        # This parameter is required.
        self.knowledge_id = knowledge_id
        self.show_detail = show_detail

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        if self.show_detail is not None:
            result['ShowDetail'] = self.show_detail
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        if m.get('ShowDetail') is not None:
            self.show_detail = m.get('ShowDetail')
        return self


class DescribeDocResponseBodyDocInfoDocParas(TeaModel):
    def __init__(
        self,
        para_level: int = None,
        para_no: int = None,
        para_text: str = None,
        para_type: str = None,
    ):
        self.para_level = para_level
        self.para_no = para_no
        self.para_text = para_text
        self.para_type = para_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.para_level is not None:
            result['ParaLevel'] = self.para_level
        if self.para_no is not None:
            result['ParaNo'] = self.para_no
        if self.para_text is not None:
            result['ParaText'] = self.para_text
        if self.para_type is not None:
            result['ParaType'] = self.para_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParaLevel') is not None:
            self.para_level = m.get('ParaLevel')
        if m.get('ParaNo') is not None:
            self.para_no = m.get('ParaNo')
        if m.get('ParaText') is not None:
            self.para_text = m.get('ParaText')
        if m.get('ParaType') is not None:
            self.para_type = m.get('ParaType')
        return self


class DescribeDocResponseBodyDocInfo(TeaModel):
    def __init__(
        self,
        doc_paras: List[DescribeDocResponseBodyDocInfoDocParas] = None,
    ):
        self.doc_paras = doc_paras

    def validate(self):
        if self.doc_paras:
            for k in self.doc_paras:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DocParas'] = []
        if self.doc_paras is not None:
            for k in self.doc_paras:
                result['DocParas'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.doc_paras = []
        if m.get('DocParas') is not None:
            for k in m.get('DocParas'):
                temp_model = DescribeDocResponseBodyDocInfoDocParas()
                self.doc_paras.append(temp_model.from_map(k))
        return self


class DescribeDocResponseBodyDocMetadataMetaCellInfoDTOList(TeaModel):
    def __init__(
        self,
        field_code: str = None,
        field_name: str = None,
        value: str = None,
    ):
        self.field_code = field_code
        self.field_name = field_name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_code is not None:
            result['FieldCode'] = self.field_code
        if self.field_name is not None:
            result['FieldName'] = self.field_name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldCode') is not None:
            self.field_code = m.get('FieldCode')
        if m.get('FieldName') is not None:
            self.field_name = m.get('FieldName')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDocResponseBodyDocMetadata(TeaModel):
    def __init__(
        self,
        business_view_id: str = None,
        business_view_name: str = None,
        meta_cell_info_dtolist: List[DescribeDocResponseBodyDocMetadataMetaCellInfoDTOList] = None,
    ):
        self.business_view_id = business_view_id
        self.business_view_name = business_view_name
        self.meta_cell_info_dtolist = meta_cell_info_dtolist

    def validate(self):
        if self.meta_cell_info_dtolist:
            for k in self.meta_cell_info_dtolist:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_view_id is not None:
            result['BusinessViewId'] = self.business_view_id
        if self.business_view_name is not None:
            result['BusinessViewName'] = self.business_view_name
        result['MetaCellInfoDTOList'] = []
        if self.meta_cell_info_dtolist is not None:
            for k in self.meta_cell_info_dtolist:
                result['MetaCellInfoDTOList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessViewId') is not None:
            self.business_view_id = m.get('BusinessViewId')
        if m.get('BusinessViewName') is not None:
            self.business_view_name = m.get('BusinessViewName')
        self.meta_cell_info_dtolist = []
        if m.get('MetaCellInfoDTOList') is not None:
            for k in m.get('MetaCellInfoDTOList'):
                temp_model = DescribeDocResponseBodyDocMetadataMetaCellInfoDTOList()
                self.meta_cell_info_dtolist.append(temp_model.from_map(k))
        return self


class DescribeDocResponseBodyDocTags(TeaModel):
    def __init__(
        self,
        default_tag: bool = None,
        group_id: int = None,
        group_name: str = None,
        tag_id: int = None,
        tag_name: str = None,
    ):
        self.default_tag = default_tag
        self.group_id = group_id
        self.group_name = group_name
        self.tag_id = tag_id
        self.tag_name = tag_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_tag is not None:
            result['DefaultTag'] = self.default_tag
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultTag') is not None:
            self.default_tag = m.get('DefaultTag')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        return self


class DescribeDocResponseBody(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
        category_id: int = None,
        config: str = None,
        create_time: str = None,
        create_user_id: int = None,
        create_user_name: str = None,
        doc_info: DescribeDocResponseBodyDocInfo = None,
        doc_metadata: List[DescribeDocResponseBodyDocMetadata] = None,
        doc_name: str = None,
        doc_tags: List[DescribeDocResponseBodyDocTags] = None,
        effect_status: int = None,
        end_date: str = None,
        knowledge_id: int = None,
        meta: str = None,
        modify_time: str = None,
        modify_user_id: int = None,
        modify_user_name: str = None,
        process_can_retry: bool = None,
        process_message: str = None,
        process_status: int = None,
        request_id: str = None,
        start_date: str = None,
        status: int = None,
        title: str = None,
        url: str = None,
    ):
        self.biz_code = biz_code
        self.category_id = category_id
        self.config = config
        self.create_time = create_time
        self.create_user_id = create_user_id
        self.create_user_name = create_user_name
        self.doc_info = doc_info
        self.doc_metadata = doc_metadata
        self.doc_name = doc_name
        self.doc_tags = doc_tags
        self.effect_status = effect_status
        self.end_date = end_date
        self.knowledge_id = knowledge_id
        self.meta = meta
        self.modify_time = modify_time
        self.modify_user_id = modify_user_id
        self.modify_user_name = modify_user_name
        self.process_can_retry = process_can_retry
        self.process_message = process_message
        self.process_status = process_status
        # Id of the request
        self.request_id = request_id
        self.start_date = start_date
        self.status = status
        self.title = title
        self.url = url

    def validate(self):
        if self.doc_info:
            self.doc_info.validate()
        if self.doc_metadata:
            for k in self.doc_metadata:
                if k:
                    k.validate()
        if self.doc_tags:
            for k in self.doc_tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.config is not None:
            result['Config'] = self.config
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.doc_info is not None:
            result['DocInfo'] = self.doc_info.to_map()
        result['DocMetadata'] = []
        if self.doc_metadata is not None:
            for k in self.doc_metadata:
                result['DocMetadata'].append(k.to_map() if k else None)
        if self.doc_name is not None:
            result['DocName'] = self.doc_name
        result['DocTags'] = []
        if self.doc_tags is not None:
            for k in self.doc_tags:
                result['DocTags'].append(k.to_map() if k else None)
        if self.effect_status is not None:
            result['EffectStatus'] = self.effect_status
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        if self.meta is not None:
            result['Meta'] = self.meta
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.modify_user_id is not None:
            result['ModifyUserId'] = self.modify_user_id
        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name
        if self.process_can_retry is not None:
            result['ProcessCanRetry'] = self.process_can_retry
        if self.process_message is not None:
            result['ProcessMessage'] = self.process_message
        if self.process_status is not None:
            result['ProcessStatus'] = self.process_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('DocInfo') is not None:
            temp_model = DescribeDocResponseBodyDocInfo()
            self.doc_info = temp_model.from_map(m['DocInfo'])
        self.doc_metadata = []
        if m.get('DocMetadata') is not None:
            for k in m.get('DocMetadata'):
                temp_model = DescribeDocResponseBodyDocMetadata()
                self.doc_metadata.append(temp_model.from_map(k))
        if m.get('DocName') is not None:
            self.doc_name = m.get('DocName')
        self.doc_tags = []
        if m.get('DocTags') is not None:
            for k in m.get('DocTags'):
                temp_model = DescribeDocResponseBodyDocTags()
                self.doc_tags.append(temp_model.from_map(k))
        if m.get('EffectStatus') is not None:
            self.effect_status = m.get('EffectStatus')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        if m.get('Meta') is not None:
            self.meta = m.get('Meta')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ModifyUserId') is not None:
            self.modify_user_id = m.get('ModifyUserId')
        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')
        if m.get('ProcessCanRetry') is not None:
            self.process_can_retry = m.get('ProcessCanRetry')
        if m.get('ProcessMessage') is not None:
            self.process_message = m.get('ProcessMessage')
        if m.get('ProcessStatus') is not None:
            self.process_status = m.get('ProcessStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DescribeDocResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDocResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeDocResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFaqRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        knowledge_id: int = None,
    ):
        self.agent_key = agent_key
        # This parameter is required.
        self.knowledge_id = knowledge_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        return self


class DescribeFaqResponseBodyOutlines(TeaModel):
    def __init__(
        self,
        conn_question_id: int = None,
        create_time: str = None,
        modify_time: str = None,
        outline_id: int = None,
        title: str = None,
    ):
        self.conn_question_id = conn_question_id
        self.create_time = create_time
        self.modify_time = modify_time
        self.outline_id = outline_id
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conn_question_id is not None:
            result['ConnQuestionId'] = self.conn_question_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.outline_id is not None:
            result['OutlineId'] = self.outline_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnQuestionId') is not None:
            self.conn_question_id = m.get('ConnQuestionId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('OutlineId') is not None:
            self.outline_id = m.get('OutlineId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class DescribeFaqResponseBodySimQuestions(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        modify_time: str = None,
        sim_question_id: int = None,
        title: str = None,
    ):
        self.create_time = create_time
        self.modify_time = modify_time
        self.sim_question_id = sim_question_id
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.sim_question_id is not None:
            result['SimQuestionId'] = self.sim_question_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('SimQuestionId') is not None:
            self.sim_question_id = m.get('SimQuestionId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class DescribeFaqResponseBodySolutions(TeaModel):
    def __init__(
        self,
        content: str = None,
        content_type: int = None,
        create_time: str = None,
        modify_time: str = None,
        perspective_codes: List[str] = None,
        plain_text: str = None,
        solution_id: int = None,
        tag_id_list: List[int] = None,
    ):
        self.content = content
        self.content_type = content_type
        self.create_time = create_time
        self.modify_time = modify_time
        self.perspective_codes = perspective_codes
        self.plain_text = plain_text
        self.solution_id = solution_id
        self.tag_id_list = tag_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.perspective_codes is not None:
            result['PerspectiveCodes'] = self.perspective_codes
        if self.plain_text is not None:
            result['PlainText'] = self.plain_text
        if self.solution_id is not None:
            result['SolutionId'] = self.solution_id
        if self.tag_id_list is not None:
            result['TagIdList'] = self.tag_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('PerspectiveCodes') is not None:
            self.perspective_codes = m.get('PerspectiveCodes')
        if m.get('PlainText') is not None:
            self.plain_text = m.get('PlainText')
        if m.get('SolutionId') is not None:
            self.solution_id = m.get('SolutionId')
        if m.get('TagIdList') is not None:
            self.tag_id_list = m.get('TagIdList')
        return self


class DescribeFaqResponseBody(TeaModel):
    def __init__(
        self,
        category_id: int = None,
        create_time: str = None,
        create_user_name: str = None,
        effect_status: int = None,
        end_date: str = None,
        knowledge_id: int = None,
        modify_time: str = None,
        modify_user_name: str = None,
        outlines: List[DescribeFaqResponseBodyOutlines] = None,
        request_id: str = None,
        sim_questions: List[DescribeFaqResponseBodySimQuestions] = None,
        solutions: List[DescribeFaqResponseBodySolutions] = None,
        start_date: str = None,
        status: int = None,
        tag_id_list: List[int] = None,
        title: str = None,
    ):
        self.category_id = category_id
        self.create_time = create_time
        self.create_user_name = create_user_name
        self.effect_status = effect_status
        self.end_date = end_date
        self.knowledge_id = knowledge_id
        self.modify_time = modify_time
        self.modify_user_name = modify_user_name
        self.outlines = outlines
        self.request_id = request_id
        self.sim_questions = sim_questions
        self.solutions = solutions
        self.start_date = start_date
        self.status = status
        self.tag_id_list = tag_id_list
        self.title = title

    def validate(self):
        if self.outlines:
            for k in self.outlines:
                if k:
                    k.validate()
        if self.sim_questions:
            for k in self.sim_questions:
                if k:
                    k.validate()
        if self.solutions:
            for k in self.solutions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.effect_status is not None:
            result['EffectStatus'] = self.effect_status
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name
        result['Outlines'] = []
        if self.outlines is not None:
            for k in self.outlines:
                result['Outlines'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SimQuestions'] = []
        if self.sim_questions is not None:
            for k in self.sim_questions:
                result['SimQuestions'].append(k.to_map() if k else None)
        result['Solutions'] = []
        if self.solutions is not None:
            for k in self.solutions:
                result['Solutions'].append(k.to_map() if k else None)
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.status is not None:
            result['Status'] = self.status
        if self.tag_id_list is not None:
            result['TagIdList'] = self.tag_id_list
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('EffectStatus') is not None:
            self.effect_status = m.get('EffectStatus')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')
        self.outlines = []
        if m.get('Outlines') is not None:
            for k in m.get('Outlines'):
                temp_model = DescribeFaqResponseBodyOutlines()
                self.outlines.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.sim_questions = []
        if m.get('SimQuestions') is not None:
            for k in m.get('SimQuestions'):
                temp_model = DescribeFaqResponseBodySimQuestions()
                self.sim_questions.append(temp_model.from_map(k))
        self.solutions = []
        if m.get('Solutions') is not None:
            for k in m.get('Solutions'):
                temp_model = DescribeFaqResponseBodySolutions()
                self.solutions.append(temp_model.from_map(k))
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TagIdList') is not None:
            self.tag_id_list = m.get('TagIdList')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class DescribeFaqResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeFaqResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeFaqResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        instance_id: str = None,
    ):
        self.agent_key = agent_key
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeInstanceResponseBodyCategories(TeaModel):
    def __init__(
        self,
        ability_type: str = None,
        category_id: int = None,
        name: str = None,
        parent_category_id: int = None,
    ):
        self.ability_type = ability_type
        self.category_id = category_id
        self.name = name
        self.parent_category_id = parent_category_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ability_type is not None:
            result['AbilityType'] = self.ability_type
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.name is not None:
            result['Name'] = self.name
        if self.parent_category_id is not None:
            result['ParentCategoryId'] = self.parent_category_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AbilityType') is not None:
            self.ability_type = m.get('AbilityType')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParentCategoryId') is not None:
            self.parent_category_id = m.get('ParentCategoryId')
        return self


class DescribeInstanceResponseBody(TeaModel):
    def __init__(
        self,
        avatar: str = None,
        categories: List[DescribeInstanceResponseBodyCategories] = None,
        create_time: str = None,
        edit_status: str = None,
        instance_id: str = None,
        introduction: str = None,
        language_code: str = None,
        name: str = None,
        request_id: str = None,
        robot_type: str = None,
        time_zone: str = None,
    ):
        self.avatar = avatar
        self.categories = categories
        self.create_time = create_time
        self.edit_status = edit_status
        self.instance_id = instance_id
        self.introduction = introduction
        self.language_code = language_code
        self.name = name
        self.request_id = request_id
        self.robot_type = robot_type
        self.time_zone = time_zone

    def validate(self):
        if self.categories:
            for k in self.categories:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar is not None:
            result['Avatar'] = self.avatar
        result['Categories'] = []
        if self.categories is not None:
            for k in self.categories:
                result['Categories'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.edit_status is not None:
            result['EditStatus'] = self.edit_status
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.introduction is not None:
            result['Introduction'] = self.introduction
        if self.language_code is not None:
            result['LanguageCode'] = self.language_code
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.robot_type is not None:
            result['RobotType'] = self.robot_type
        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Avatar') is not None:
            self.avatar = m.get('Avatar')
        self.categories = []
        if m.get('Categories') is not None:
            for k in m.get('Categories'):
                temp_model = DescribeInstanceResponseBodyCategories()
                self.categories.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EditStatus') is not None:
            self.edit_status = m.get('EditStatus')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Introduction') is not None:
            self.introduction = m.get('Introduction')
        if m.get('LanguageCode') is not None:
            self.language_code = m.get('LanguageCode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RobotType') is not None:
            self.robot_type = m.get('RobotType')
        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')
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


class DescribeIntentRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        instance_id: str = None,
        intent_id: int = None,
    ):
        self.agent_key = agent_key
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.intent_id = intent_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        return self


class DescribeIntentResponseBodySlotInfos(TeaModel):
    def __init__(
        self,
        array: bool = None,
        encrypt: bool = None,
        interactive: bool = None,
        name: str = None,
        slot_id: str = None,
        value: str = None,
    ):
        self.array = array
        self.encrypt = encrypt
        self.interactive = interactive
        self.name = name
        self.slot_id = slot_id
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.array is not None:
            result['Array'] = self.array
        if self.encrypt is not None:
            result['Encrypt'] = self.encrypt
        if self.interactive is not None:
            result['Interactive'] = self.interactive
        if self.name is not None:
            result['Name'] = self.name
        if self.slot_id is not None:
            result['SlotId'] = self.slot_id
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Array') is not None:
            self.array = m.get('Array')
        if m.get('Encrypt') is not None:
            self.encrypt = m.get('Encrypt')
        if m.get('Interactive') is not None:
            self.interactive = m.get('Interactive')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SlotId') is not None:
            self.slot_id = m.get('SlotId')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeIntentResponseBody(TeaModel):
    def __init__(
        self,
        alias_name: str = None,
        create_time: str = None,
        create_user_id: str = None,
        create_user_name: str = None,
        intent_id: int = None,
        intent_name: str = None,
        modify_time: str = None,
        modify_user_id: str = None,
        modify_user_name: str = None,
        request_id: str = None,
        slot_infos: List[DescribeIntentResponseBodySlotInfos] = None,
    ):
        self.alias_name = alias_name
        self.create_time = create_time
        self.create_user_id = create_user_id
        self.create_user_name = create_user_name
        self.intent_id = intent_id
        self.intent_name = intent_name
        self.modify_time = modify_time
        self.modify_user_id = modify_user_id
        self.modify_user_name = modify_user_name
        self.request_id = request_id
        self.slot_infos = slot_infos

    def validate(self):
        if self.slot_infos:
            for k in self.slot_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        if self.intent_name is not None:
            result['IntentName'] = self.intent_name
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.modify_user_id is not None:
            result['ModifyUserId'] = self.modify_user_id
        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SlotInfos'] = []
        if self.slot_infos is not None:
            for k in self.slot_infos:
                result['SlotInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        if m.get('IntentName') is not None:
            self.intent_name = m.get('IntentName')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ModifyUserId') is not None:
            self.modify_user_id = m.get('ModifyUserId')
        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.slot_infos = []
        if m.get('SlotInfos') is not None:
            for k in m.get('SlotInfos'):
                temp_model = DescribeIntentResponseBodySlotInfos()
                self.slot_infos.append(temp_model.from_map(k))
        return self


class DescribeIntentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeIntentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeIntentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePerspectiveRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        perspective_id: str = None,
    ):
        self.agent_key = agent_key
        self.perspective_id = perspective_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.perspective_id is not None:
            result['PerspectiveId'] = self.perspective_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('PerspectiveId') is not None:
            self.perspective_id = m.get('PerspectiveId')
        return self


class DescribePerspectiveResponseBody(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        modify_time: str = None,
        name: str = None,
        perspective_code: str = None,
        perspective_id: str = None,
        request_id: str = None,
        self_define: bool = None,
        status: int = None,
    ):
        self.create_time = create_time
        self.modify_time = modify_time
        self.name = name
        self.perspective_code = perspective_code
        self.perspective_id = perspective_id
        self.request_id = request_id
        self.self_define = self_define
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.name is not None:
            result['Name'] = self.name
        if self.perspective_code is not None:
            result['PerspectiveCode'] = self.perspective_code
        if self.perspective_id is not None:
            result['PerspectiveId'] = self.perspective_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.self_define is not None:
            result['SelfDefine'] = self.self_define
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PerspectiveCode') is not None:
            self.perspective_code = m.get('PerspectiveCode')
        if m.get('PerspectiveId') is not None:
            self.perspective_id = m.get('PerspectiveId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SelfDefine') is not None:
            self.self_define = m.get('SelfDefine')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribePerspectiveResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribePerspectiveResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribePerspectiveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTagRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        client_token: str = None,
        group_id: int = None,
        id: int = None,
    ):
        self.agent_key = agent_key
        self.client_token = client_token
        # This parameter is required.
        self.group_id = group_id
        # This parameter is required.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribeTagResponseBody(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        create_user_id: int = None,
        create_user_name: str = None,
        group_id: int = None,
        id: int = None,
        modify_time: str = None,
        modify_user_id: int = None,
        modify_user_name: str = None,
        request_id: str = None,
        tag_name: str = None,
    ):
        self.create_time = create_time
        self.create_user_id = create_user_id
        self.create_user_name = create_user_name
        self.group_id = group_id
        self.id = id
        self.modify_time = modify_time
        self.modify_user_id = modify_user_id
        self.modify_user_name = modify_user_name
        self.request_id = request_id
        self.tag_name = tag_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.id is not None:
            result['Id'] = self.id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.modify_user_id is not None:
            result['ModifyUserId'] = self.modify_user_id
        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ModifyUserId') is not None:
            self.modify_user_id = m.get('ModifyUserId')
        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        return self


class DescribeTagResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeTagResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTagGroupRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        client_token: str = None,
        id: int = None,
    ):
        self.agent_key = agent_key
        self.client_token = client_token
        # This parameter is required.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribeTagGroupResponseBody(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        create_user_id: int = None,
        create_user_name: str = None,
        default_tag_id: int = None,
        group_name: str = None,
        id: int = None,
        modify_time: str = None,
        modify_user_id: int = None,
        modify_user_name: str = None,
        request_id: str = None,
    ):
        self.create_time = create_time
        self.create_user_id = create_user_id
        self.create_user_name = create_user_name
        self.default_tag_id = default_tag_id
        self.group_name = group_name
        self.id = id
        self.modify_time = modify_time
        self.modify_user_id = modify_user_id
        self.modify_user_name = modify_user_name
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.default_tag_id is not None:
            result['DefaultTagId'] = self.default_tag_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.id is not None:
            result['Id'] = self.id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.modify_user_id is not None:
            result['ModifyUserId'] = self.modify_user_id
        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('DefaultTagId') is not None:
            self.default_tag_id = m.get('DefaultTagId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ModifyUserId') is not None:
            self.modify_user_id = m.get('ModifyUserId')
        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeTagGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeTagGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeTagGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FeedbackRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        feedback: str = None,
        feedback_content: str = None,
        instance_id: str = None,
        message_id: str = None,
        session_id: str = None,
    ):
        self.agent_key = agent_key
        self.feedback = feedback
        self.feedback_content = feedback_content
        self.instance_id = instance_id
        self.message_id = message_id
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.feedback is not None:
            result['Feedback'] = self.feedback
        if self.feedback_content is not None:
            result['FeedbackContent'] = self.feedback_content
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Feedback') is not None:
            self.feedback = m.get('Feedback')
        if m.get('FeedbackContent') is not None:
            self.feedback_content = m.get('FeedbackContent')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class FeedbackResponseBody(TeaModel):
    def __init__(
        self,
        feedback: str = None,
        message_id: str = None,
        request_id: str = None,
    ):
        self.feedback = feedback
        self.message_id = message_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feedback is not None:
            result['Feedback'] = self.feedback
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Feedback') is not None:
            self.feedback = m.get('Feedback')
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class FeedbackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: FeedbackResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = FeedbackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateUserAccessTokenRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        email: str = None,
        expire_time: int = None,
        extra_info: str = None,
        foreign_id: str = None,
        nick: str = None,
        telephone: str = None,
    ):
        self.agent_key = agent_key
        self.email = email
        self.expire_time = expire_time
        self.extra_info = extra_info
        # This parameter is required.
        self.foreign_id = foreign_id
        # This parameter is required.
        self.nick = nick
        self.telephone = telephone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.email is not None:
            result['Email'] = self.email
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info
        if self.foreign_id is not None:
            result['ForeignId'] = self.foreign_id
        if self.nick is not None:
            result['Nick'] = self.nick
        if self.telephone is not None:
            result['Telephone'] = self.telephone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('ExtraInfo') is not None:
            self.extra_info = m.get('ExtraInfo')
        if m.get('ForeignId') is not None:
            self.foreign_id = m.get('ForeignId')
        if m.get('Nick') is not None:
            self.nick = m.get('Nick')
        if m.get('Telephone') is not None:
            self.telephone = m.get('Telephone')
        return self


class GenerateUserAccessTokenResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
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
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GenerateUserAccessTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GenerateUserAccessTokenResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GenerateUserAccessTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAgentInfoRequest(TeaModel):
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


class GetAgentInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        agent_name: str = None,
    ):
        self.agent_key = agent_key
        self.agent_name = agent_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.agent_name is not None:
            result['AgentName'] = self.agent_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')
        return self


class GetAgentInfoResponseBody(TeaModel):
    def __init__(
        self,
        data: GetAgentInfoResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.message = message
        # Id of the request
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
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetAgentInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAgentInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAgentInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetAgentInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAsyncResultRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        task_id: str = None,
    ):
        self.agent_key = agent_key
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetAsyncResultResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
        status: str = None,
    ):
        self.data = data
        self.request_id = request_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetAsyncResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAsyncResultResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetAsyncResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBotSessionDataRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        end_time: str = None,
        robot_instance_id: str = None,
        start_time: str = None,
    ):
        self.agent_key = agent_key
        # This parameter is required.
        self.end_time = end_time
        # This parameter is required.
        self.robot_instance_id = robot_instance_id
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.robot_instance_id is not None:
            result['RobotInstanceId'] = self.robot_instance_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RobotInstanceId') is not None:
            self.robot_instance_id = m.get('RobotInstanceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class GetBotSessionDataResponseBody(TeaModel):
    def __init__(
        self,
        cost_time: str = None,
        datas: List[Dict[str, Any]] = None,
        request_id: str = None,
    ):
        self.cost_time = cost_time
        self.datas = datas
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost_time is not None:
            result['CostTime'] = self.cost_time
        if self.datas is not None:
            result['Datas'] = self.datas
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostTime') is not None:
            self.cost_time = m.get('CostTime')
        if m.get('Datas') is not None:
            self.datas = m.get('Datas')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetBotSessionDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetBotSessionDataResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetBotSessionDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstancePublishTaskStateRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        id: int = None,
        instance_id: str = None,
    ):
        self.agent_key = agent_key
        self.id = id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetInstancePublishTaskStateResponseBody(TeaModel):
    def __init__(
        self,
        biz_type_list: List[str] = None,
        create_time: str = None,
        error: str = None,
        errors: Dict[str, Any] = None,
        id: int = None,
        modify_time: str = None,
        request_id: str = None,
        response: str = None,
        status: str = None,
        warnings: Dict[str, Any] = None,
    ):
        self.biz_type_list = biz_type_list
        self.create_time = create_time
        self.error = error
        self.errors = errors
        self.id = id
        self.modify_time = modify_time
        self.request_id = request_id
        self.response = response
        self.status = status
        self.warnings = warnings

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type_list is not None:
            result['BizTypeList'] = self.biz_type_list
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.error is not None:
            result['Error'] = self.error
        if self.errors is not None:
            result['Errors'] = self.errors
        if self.id is not None:
            result['Id'] = self.id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response is not None:
            result['Response'] = self.response
        if self.status is not None:
            result['Status'] = self.status
        if self.warnings is not None:
            result['Warnings'] = self.warnings
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizTypeList') is not None:
            self.biz_type_list = m.get('BizTypeList')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('Errors') is not None:
            self.errors = m.get('Errors')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Response') is not None:
            self.response = m.get('Response')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Warnings') is not None:
            self.warnings = m.get('Warnings')
        return self


class GetInstancePublishTaskStateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetInstancePublishTaskStateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetInstancePublishTaskStateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPublishTaskStateRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        id: int = None,
    ):
        self.agent_key = agent_key
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetPublishTaskStateResponseBody(TeaModel):
    def __init__(
        self,
        biz_type_list: List[str] = None,
        create_time: str = None,
        error: str = None,
        errors: Dict[str, Any] = None,
        id: int = None,
        modify_time: str = None,
        request_id: str = None,
        response: str = None,
        status: str = None,
        warnings: Dict[str, Any] = None,
    ):
        self.biz_type_list = biz_type_list
        self.create_time = create_time
        self.error = error
        self.errors = errors
        self.id = id
        self.modify_time = modify_time
        self.request_id = request_id
        self.response = response
        self.status = status
        self.warnings = warnings

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type_list is not None:
            result['BizTypeList'] = self.biz_type_list
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.error is not None:
            result['Error'] = self.error
        if self.errors is not None:
            result['Errors'] = self.errors
        if self.id is not None:
            result['Id'] = self.id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response is not None:
            result['Response'] = self.response
        if self.status is not None:
            result['Status'] = self.status
        if self.warnings is not None:
            result['Warnings'] = self.warnings
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizTypeList') is not None:
            self.biz_type_list = m.get('BizTypeList')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('Errors') is not None:
            self.errors = m.get('Errors')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Response') is not None:
            self.response = m.get('Response')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Warnings') is not None:
            self.warnings = m.get('Warnings')
        return self


class GetPublishTaskStateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPublishTaskStateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetPublishTaskStateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InitIMConnectRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        from_: str = None,
        user_access_token: str = None,
    ):
        self.agent_key = agent_key
        # This parameter is required.
        self.from_ = from_
        self.user_access_token = user_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.from_ is not None:
            result['From'] = self.from_
        if self.user_access_token is not None:
            result['UserAccessToken'] = self.user_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('UserAccessToken') is not None:
            self.user_access_token = m.get('UserAccessToken')
        return self


class InitIMConnectResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
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
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class InitIMConnectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InitIMConnectResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = InitIMConnectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LinkInstanceCategoryRequest(TeaModel):
    def __init__(
        self,
        ability_type: str = None,
        agent_key: str = None,
        category_ids: str = None,
        instance_id: str = None,
    ):
        self.ability_type = ability_type
        self.agent_key = agent_key
        self.category_ids = category_ids
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ability_type is not None:
            result['AbilityType'] = self.ability_type
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.category_ids is not None:
            result['CategoryIds'] = self.category_ids
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AbilityType') is not None:
            self.ability_type = m.get('AbilityType')
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('CategoryIds') is not None:
            self.category_ids = m.get('CategoryIds')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class LinkInstanceCategoryResponseBody(TeaModel):
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


class LinkInstanceCategoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: LinkInstanceCategoryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = LinkInstanceCategoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAgentRequest(TeaModel):
    def __init__(
        self,
        agent_name: str = None,
        goods_codes: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.agent_name = agent_name
        self.goods_codes = goods_codes
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_name is not None:
            result['AgentName'] = self.agent_name
        if self.goods_codes is not None:
            result['GoodsCodes'] = self.goods_codes
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')
        if m.get('GoodsCodes') is not None:
            self.goods_codes = m.get('GoodsCodes')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListAgentResponseBodyData(TeaModel):
    def __init__(
        self,
        agent_id: int = None,
        agent_key: str = None,
        agent_name: str = None,
        instance_infos: Dict[str, Any] = None,
    ):
        self.agent_id = agent_id
        self.agent_key = agent_key
        self.agent_name = agent_name
        self.instance_infos = instance_infos

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.agent_name is not None:
            result['AgentName'] = self.agent_name
        if self.instance_infos is not None:
            result['InstanceInfos'] = self.instance_infos
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')
        if m.get('InstanceInfos') is not None:
            self.instance_infos = m.get('InstanceInfos')
        return self


class ListAgentResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListAgentResponseBodyData] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.data = data
        self.page_number = page_number
        self.page_size = page_size
        # Id of the request
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListAgentResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAgentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAgentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListAgentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCategoryRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        knowledge_type: int = None,
        parent_category_id: int = None,
    ):
        self.agent_key = agent_key
        self.knowledge_type = knowledge_type
        self.parent_category_id = parent_category_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.knowledge_type is not None:
            result['KnowledgeType'] = self.knowledge_type
        if self.parent_category_id is not None:
            result['ParentCategoryId'] = self.parent_category_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('KnowledgeType') is not None:
            self.knowledge_type = m.get('KnowledgeType')
        if m.get('ParentCategoryId') is not None:
            self.parent_category_id = m.get('ParentCategoryId')
        return self


class ListCategoryResponseBodyCategories(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
        category_id: int = None,
        name: str = None,
        parent_category_id: int = None,
        status: int = None,
    ):
        self.biz_code = biz_code
        self.category_id = category_id
        self.name = name
        self.parent_category_id = parent_category_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.name is not None:
            result['Name'] = self.name
        if self.parent_category_id is not None:
            result['ParentCategoryId'] = self.parent_category_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParentCategoryId') is not None:
            self.parent_category_id = m.get('ParentCategoryId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListCategoryResponseBody(TeaModel):
    def __init__(
        self,
        categories: List[ListCategoryResponseBodyCategories] = None,
        request_id: str = None,
    ):
        self.categories = categories
        self.request_id = request_id

    def validate(self):
        if self.categories:
            for k in self.categories:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Categories'] = []
        if self.categories is not None:
            for k in self.categories:
                result['Categories'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.categories = []
        if m.get('Categories') is not None:
            for k in m.get('Categories'):
                temp_model = ListCategoryResponseBodyCategories()
                self.categories.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListCategoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCategoryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListCategoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListConnQuestionRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        knowledge_id: int = None,
    ):
        self.agent_key = agent_key
        # This parameter is required.
        self.knowledge_id = knowledge_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        return self


class ListConnQuestionResponseBodyOutlines(TeaModel):
    def __init__(
        self,
        conn_question_id: int = None,
        create_time: str = None,
        modify_time: str = None,
        outline_id: int = None,
        title: str = None,
    ):
        self.conn_question_id = conn_question_id
        self.create_time = create_time
        self.modify_time = modify_time
        self.outline_id = outline_id
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conn_question_id is not None:
            result['ConnQuestionId'] = self.conn_question_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.outline_id is not None:
            result['OutlineId'] = self.outline_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnQuestionId') is not None:
            self.conn_question_id = m.get('ConnQuestionId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('OutlineId') is not None:
            self.outline_id = m.get('OutlineId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class ListConnQuestionResponseBody(TeaModel):
    def __init__(
        self,
        outlines: List[ListConnQuestionResponseBodyOutlines] = None,
        request_id: str = None,
    ):
        self.outlines = outlines
        self.request_id = request_id

    def validate(self):
        if self.outlines:
            for k in self.outlines:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Outlines'] = []
        if self.outlines is not None:
            for k in self.outlines:
                result['Outlines'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.outlines = []
        if m.get('Outlines') is not None:
            for k in m.get('Outlines'):
                temp_model = ListConnQuestionResponseBodyOutlines()
                self.outlines.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListConnQuestionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListConnQuestionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListConnQuestionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDSEntityRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        entity_type: str = None,
        instance_id: str = None,
        keyword: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.agent_key = agent_key
        self.entity_type = entity_type
        # This parameter is required.
        self.instance_id = instance_id
        self.keyword = keyword
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListDSEntityResponseBodyEntities(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        create_user_id: str = None,
        create_user_name: str = None,
        entity_id: int = None,
        entity_name: str = None,
        entity_type: str = None,
        modify_time: str = None,
        modify_user_id: str = None,
        modify_user_name: str = None,
        sys_entity_code: str = None,
    ):
        self.create_time = create_time
        self.create_user_id = create_user_id
        self.create_user_name = create_user_name
        self.entity_id = entity_id
        self.entity_name = entity_name
        self.entity_type = entity_type
        self.modify_time = modify_time
        self.modify_user_id = modify_user_id
        self.modify_user_name = modify_user_name
        self.sys_entity_code = sys_entity_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.entity_name is not None:
            result['EntityName'] = self.entity_name
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.modify_user_id is not None:
            result['ModifyUserId'] = self.modify_user_id
        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name
        if self.sys_entity_code is not None:
            result['SysEntityCode'] = self.sys_entity_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ModifyUserId') is not None:
            self.modify_user_id = m.get('ModifyUserId')
        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')
        if m.get('SysEntityCode') is not None:
            self.sys_entity_code = m.get('SysEntityCode')
        return self


class ListDSEntityResponseBody(TeaModel):
    def __init__(
        self,
        entities: List[ListDSEntityResponseBodyEntities] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.entities = entities
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.entities:
            for k in self.entities:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Entities'] = []
        if self.entities is not None:
            for k in self.entities:
                result['Entities'].append(k.to_map() if k else None)
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
        self.entities = []
        if m.get('Entities') is not None:
            for k in m.get('Entities'):
                temp_model = ListDSEntityResponseBodyEntities()
                self.entities.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListDSEntityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDSEntityResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListDSEntityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDSEntityValueRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        entity_id: int = None,
        entity_value_id: int = None,
        instance_id: str = None,
        keyword: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.agent_key = agent_key
        # This parameter is required.
        self.entity_id = entity_id
        self.entity_value_id = entity_value_id
        # This parameter is required.
        self.instance_id = instance_id
        self.keyword = keyword
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.entity_value_id is not None:
            result['EntityValueId'] = self.entity_value_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('EntityValueId') is not None:
            self.entity_value_id = m.get('EntityValueId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListDSEntityValueResponseBodyEntityValues(TeaModel):
    def __init__(
        self,
        content: str = None,
        create_time: str = None,
        entity_id: int = None,
        entity_value_id: int = None,
        modify_time: str = None,
        synonyms: List[str] = None,
    ):
        self.content = content
        self.create_time = create_time
        self.entity_id = entity_id
        self.entity_value_id = entity_value_id
        self.modify_time = modify_time
        self.synonyms = synonyms

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.entity_value_id is not None:
            result['EntityValueId'] = self.entity_value_id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.synonyms is not None:
            result['Synonyms'] = self.synonyms
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('EntityValueId') is not None:
            self.entity_value_id = m.get('EntityValueId')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('Synonyms') is not None:
            self.synonyms = m.get('Synonyms')
        return self


class ListDSEntityValueResponseBody(TeaModel):
    def __init__(
        self,
        entity_values: List[ListDSEntityValueResponseBodyEntityValues] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.entity_values = entity_values
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.entity_values:
            for k in self.entity_values:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EntityValues'] = []
        if self.entity_values is not None:
            for k in self.entity_values:
                result['EntityValues'].append(k.to_map() if k else None)
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
        self.entity_values = []
        if m.get('EntityValues') is not None:
            for k in m.get('EntityValues'):
                temp_model = ListDSEntityValueResponseBodyEntityValues()
                self.entity_values.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListDSEntityValueResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDSEntityValueResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListDSEntityValueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstanceRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        robot_type: str = None,
    ):
        self.agent_key = agent_key
        self.name = name
        self.page_number = page_number
        self.page_size = page_size
        self.robot_type = robot_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.name is not None:
            result['Name'] = self.name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.robot_type is not None:
            result['RobotType'] = self.robot_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RobotType') is not None:
            self.robot_type = m.get('RobotType')
        return self


class ListInstanceResponseBodyInstances(TeaModel):
    def __init__(
        self,
        avatar: str = None,
        create_time: str = None,
        instance_id: str = None,
        introduction: str = None,
        language_code: str = None,
        name: str = None,
        robot_type: str = None,
    ):
        self.avatar = avatar
        self.create_time = create_time
        self.instance_id = instance_id
        self.introduction = introduction
        self.language_code = language_code
        self.name = name
        self.robot_type = robot_type

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
        if self.robot_type is not None:
            result['RobotType'] = self.robot_type
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
        if m.get('RobotType') is not None:
            self.robot_type = m.get('RobotType')
        return self


class ListInstanceResponseBody(TeaModel):
    def __init__(
        self,
        instances: List[ListInstanceResponseBodyInstances] = None,
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
                temp_model = ListInstanceResponseBodyInstances()
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


class ListInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListIntentRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        instance_id: str = None,
        intent_name: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.agent_key = agent_key
        # This parameter is required.
        self.instance_id = instance_id
        self.intent_name = intent_name
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.intent_name is not None:
            result['IntentName'] = self.intent_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IntentName') is not None:
            self.intent_name = m.get('IntentName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListIntentResponseBodyIntentsSlotInfos(TeaModel):
    def __init__(
        self,
        array: bool = None,
        encrypt: bool = None,
        interactive: bool = None,
        name: str = None,
        slot_id: str = None,
        value: str = None,
    ):
        self.array = array
        self.encrypt = encrypt
        self.interactive = interactive
        self.name = name
        self.slot_id = slot_id
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.array is not None:
            result['Array'] = self.array
        if self.encrypt is not None:
            result['Encrypt'] = self.encrypt
        if self.interactive is not None:
            result['Interactive'] = self.interactive
        if self.name is not None:
            result['Name'] = self.name
        if self.slot_id is not None:
            result['SlotId'] = self.slot_id
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Array') is not None:
            self.array = m.get('Array')
        if m.get('Encrypt') is not None:
            self.encrypt = m.get('Encrypt')
        if m.get('Interactive') is not None:
            self.interactive = m.get('Interactive')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SlotId') is not None:
            self.slot_id = m.get('SlotId')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListIntentResponseBodyIntents(TeaModel):
    def __init__(
        self,
        alias_name: str = None,
        create_time: str = None,
        create_user_id: str = None,
        create_user_name: str = None,
        intent_id: int = None,
        intent_name: str = None,
        modify_time: str = None,
        modify_user_id: str = None,
        modify_user_name: str = None,
        slot_infos: List[ListIntentResponseBodyIntentsSlotInfos] = None,
    ):
        self.alias_name = alias_name
        self.create_time = create_time
        self.create_user_id = create_user_id
        self.create_user_name = create_user_name
        self.intent_id = intent_id
        self.intent_name = intent_name
        self.modify_time = modify_time
        self.modify_user_id = modify_user_id
        self.modify_user_name = modify_user_name
        self.slot_infos = slot_infos

    def validate(self):
        if self.slot_infos:
            for k in self.slot_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        if self.intent_name is not None:
            result['IntentName'] = self.intent_name
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.modify_user_id is not None:
            result['ModifyUserId'] = self.modify_user_id
        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name
        result['SlotInfos'] = []
        if self.slot_infos is not None:
            for k in self.slot_infos:
                result['SlotInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        if m.get('IntentName') is not None:
            self.intent_name = m.get('IntentName')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ModifyUserId') is not None:
            self.modify_user_id = m.get('ModifyUserId')
        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')
        self.slot_infos = []
        if m.get('SlotInfos') is not None:
            for k in m.get('SlotInfos'):
                temp_model = ListIntentResponseBodyIntentsSlotInfos()
                self.slot_infos.append(temp_model.from_map(k))
        return self


class ListIntentResponseBody(TeaModel):
    def __init__(
        self,
        intents: List[ListIntentResponseBodyIntents] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.intents = intents
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.intents:
            for k in self.intents:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Intents'] = []
        if self.intents is not None:
            for k in self.intents:
                result['Intents'].append(k.to_map() if k else None)
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
        self.intents = []
        if m.get('Intents') is not None:
            for k in m.get('Intents'):
                temp_model = ListIntentResponseBodyIntents()
                self.intents.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListIntentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListIntentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListIntentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLgfRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        instance_id: str = None,
        intent_id: int = None,
        lgf_text: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.agent_key = agent_key
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.intent_id = intent_id
        self.lgf_text = lgf_text
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        if self.lgf_text is not None:
            result['LgfText'] = self.lgf_text
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        if m.get('LgfText') is not None:
            self.lgf_text = m.get('LgfText')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListLgfResponseBodyLgfs(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        intent_id: int = None,
        lgf_id: int = None,
        modify_time: str = None,
        rule_text: str = None,
    ):
        self.create_time = create_time
        self.intent_id = intent_id
        # LGF ID
        self.lgf_id = lgf_id
        self.modify_time = modify_time
        self.rule_text = rule_text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        if self.lgf_id is not None:
            result['LgfId'] = self.lgf_id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.rule_text is not None:
            result['RuleText'] = self.rule_text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        if m.get('LgfId') is not None:
            self.lgf_id = m.get('LgfId')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('RuleText') is not None:
            self.rule_text = m.get('RuleText')
        return self


class ListLgfResponseBody(TeaModel):
    def __init__(
        self,
        lgfs: List[ListLgfResponseBodyLgfs] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.lgfs = lgfs
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.lgfs:
            for k in self.lgfs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Lgfs'] = []
        if self.lgfs is not None:
            for k in self.lgfs:
                result['Lgfs'].append(k.to_map() if k else None)
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
        self.lgfs = []
        if m.get('Lgfs') is not None:
            for k in m.get('Lgfs'):
                temp_model = ListLgfResponseBodyLgfs()
                self.lgfs.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListLgfResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListLgfResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListLgfResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSaasInfoRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        saas_group_codes: str = None,
        saas_name: str = None,
    ):
        self.agent_key = agent_key
        self.saas_group_codes = saas_group_codes
        # This parameter is required.
        self.saas_name = saas_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.saas_group_codes is not None:
            result['SaasGroupCodes'] = self.saas_group_codes
        if self.saas_name is not None:
            result['SaasName'] = self.saas_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('SaasGroupCodes') is not None:
            self.saas_group_codes = m.get('SaasGroupCodes')
        if m.get('SaasName') is not None:
            self.saas_name = m.get('SaasName')
        return self


class ListSaasInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        code: str = None,
        en_name: str = None,
        name: str = None,
        service_url: str = None,
        url: str = None,
    ):
        self.code = code
        self.en_name = en_name
        self.name = name
        self.service_url = service_url
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.en_name is not None:
            result['EnName'] = self.en_name
        if self.name is not None:
            result['Name'] = self.name
        if self.service_url is not None:
            result['ServiceUrl'] = self.service_url
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('EnName') is not None:
            self.en_name = m.get('EnName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ServiceUrl') is not None:
            self.service_url = m.get('ServiceUrl')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class ListSaasInfoResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListSaasInfoResponseBodyData] = None,
        request_id: str = None,
        saas_token: str = None,
    ):
        self.data = data
        # Id of the request
        self.request_id = request_id
        self.saas_token = saas_token

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.saas_token is not None:
            result['SaasToken'] = self.saas_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListSaasInfoResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SaasToken') is not None:
            self.saas_token = m.get('SaasToken')
        return self


class ListSaasInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSaasInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListSaasInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSaasPermissionGroupInfosRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        return self


class ListSaasPermissionGroupInfosResponseBodyDataPgInfos(TeaModel):
    def __init__(
        self,
        pg_code: str = None,
        pg_en_name: str = None,
        pg_name: str = None,
    ):
        self.pg_code = pg_code
        self.pg_en_name = pg_en_name
        self.pg_name = pg_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pg_code is not None:
            result['PgCode'] = self.pg_code
        if self.pg_en_name is not None:
            result['PgEnName'] = self.pg_en_name
        if self.pg_name is not None:
            result['PgName'] = self.pg_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PgCode') is not None:
            self.pg_code = m.get('PgCode')
        if m.get('PgEnName') is not None:
            self.pg_en_name = m.get('PgEnName')
        if m.get('PgName') is not None:
            self.pg_name = m.get('PgName')
        return self


class ListSaasPermissionGroupInfosResponseBodyData(TeaModel):
    def __init__(
        self,
        en_name: str = None,
        name: str = None,
        pg_infos: List[ListSaasPermissionGroupInfosResponseBodyDataPgInfos] = None,
        saas_code: str = None,
    ):
        self.en_name = en_name
        self.name = name
        self.pg_infos = pg_infos
        self.saas_code = saas_code

    def validate(self):
        if self.pg_infos:
            for k in self.pg_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.en_name is not None:
            result['EnName'] = self.en_name
        if self.name is not None:
            result['Name'] = self.name
        result['PgInfos'] = []
        if self.pg_infos is not None:
            for k in self.pg_infos:
                result['PgInfos'].append(k.to_map() if k else None)
        if self.saas_code is not None:
            result['SaasCode'] = self.saas_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnName') is not None:
            self.en_name = m.get('EnName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.pg_infos = []
        if m.get('PgInfos') is not None:
            for k in m.get('PgInfos'):
                temp_model = ListSaasPermissionGroupInfosResponseBodyDataPgInfos()
                self.pg_infos.append(temp_model.from_map(k))
        if m.get('SaasCode') is not None:
            self.saas_code = m.get('SaasCode')
        return self


class ListSaasPermissionGroupInfosResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListSaasPermissionGroupInfosResponseBodyData] = None,
        request_id: str = None,
    ):
        self.data = data
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListSaasPermissionGroupInfosResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListSaasPermissionGroupInfosResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSaasPermissionGroupInfosResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListSaasPermissionGroupInfosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSimQuestionRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        knowledge_id: int = None,
    ):
        self.agent_key = agent_key
        # This parameter is required.
        self.knowledge_id = knowledge_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        return self


class ListSimQuestionResponseBodySimQuestions(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        modify_time: str = None,
        sim_question_id: int = None,
        title: str = None,
    ):
        self.create_time = create_time
        self.modify_time = modify_time
        self.sim_question_id = sim_question_id
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.sim_question_id is not None:
            result['SimQuestionId'] = self.sim_question_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('SimQuestionId') is not None:
            self.sim_question_id = m.get('SimQuestionId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class ListSimQuestionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        sim_questions: List[ListSimQuestionResponseBodySimQuestions] = None,
    ):
        self.request_id = request_id
        self.sim_questions = sim_questions

    def validate(self):
        if self.sim_questions:
            for k in self.sim_questions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SimQuestions'] = []
        if self.sim_questions is not None:
            for k in self.sim_questions:
                result['SimQuestions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.sim_questions = []
        if m.get('SimQuestions') is not None:
            for k in m.get('SimQuestions'):
                temp_model = ListSimQuestionResponseBodySimQuestions()
                self.sim_questions.append(temp_model.from_map(k))
        return self


class ListSimQuestionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSimQuestionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListSimQuestionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSolutionRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        knowledge_id: int = None,
    ):
        self.agent_key = agent_key
        # This parameter is required.
        self.knowledge_id = knowledge_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        return self


class ListSolutionResponseBodySolutions(TeaModel):
    def __init__(
        self,
        content: str = None,
        content_type: int = None,
        create_time: str = None,
        modify_time: str = None,
        perspective_codes: List[str] = None,
        plain_text: str = None,
        solution_id: int = None,
        tag_id_list: List[int] = None,
    ):
        self.content = content
        self.content_type = content_type
        self.create_time = create_time
        self.modify_time = modify_time
        self.perspective_codes = perspective_codes
        self.plain_text = plain_text
        self.solution_id = solution_id
        self.tag_id_list = tag_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.perspective_codes is not None:
            result['PerspectiveCodes'] = self.perspective_codes
        if self.plain_text is not None:
            result['PlainText'] = self.plain_text
        if self.solution_id is not None:
            result['SolutionId'] = self.solution_id
        if self.tag_id_list is not None:
            result['TagIdList'] = self.tag_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('PerspectiveCodes') is not None:
            self.perspective_codes = m.get('PerspectiveCodes')
        if m.get('PlainText') is not None:
            self.plain_text = m.get('PlainText')
        if m.get('SolutionId') is not None:
            self.solution_id = m.get('SolutionId')
        if m.get('TagIdList') is not None:
            self.tag_id_list = m.get('TagIdList')
        return self


class ListSolutionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        solutions: List[ListSolutionResponseBodySolutions] = None,
    ):
        self.request_id = request_id
        self.solutions = solutions

    def validate(self):
        if self.solutions:
            for k in self.solutions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Solutions'] = []
        if self.solutions is not None:
            for k in self.solutions:
                result['Solutions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.solutions = []
        if m.get('Solutions') is not None:
            for k in m.get('Solutions'):
                temp_model = ListSolutionResponseBodySolutions()
                self.solutions.append(temp_model.from_map(k))
        return self


class ListSolutionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSolutionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListSolutionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        client_token: str = None,
        group_id: int = None,
        page_number: int = None,
        page_size: int = None,
        tag_name: str = None,
    ):
        self.agent_key = agent_key
        self.client_token = client_token
        self.group_id = group_id
        self.page_number = page_number
        self.page_size = page_size
        self.tag_name = tag_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        return self


class ListTagResponseBodyTagGroups(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        create_user_id: int = None,
        create_user_name: str = None,
        group_id: int = None,
        id: int = None,
        modify_time: str = None,
        modify_user_id: int = None,
        modify_user_name: str = None,
        tag_name: str = None,
    ):
        self.create_time = create_time
        self.create_user_id = create_user_id
        self.create_user_name = create_user_name
        self.group_id = group_id
        self.id = id
        self.modify_time = modify_time
        self.modify_user_id = modify_user_id
        self.modify_user_name = modify_user_name
        self.tag_name = tag_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.id is not None:
            result['Id'] = self.id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.modify_user_id is not None:
            result['ModifyUserId'] = self.modify_user_id
        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ModifyUserId') is not None:
            self.modify_user_id = m.get('ModifyUserId')
        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        return self


class ListTagResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        tag_groups: List[ListTagResponseBodyTagGroups] = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.tag_groups = tag_groups
        self.total_count = total_count

    def validate(self):
        if self.tag_groups:
            for k in self.tag_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TagGroups'] = []
        if self.tag_groups is not None:
            for k in self.tag_groups:
                result['TagGroups'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tag_groups = []
        if m.get('TagGroups') is not None:
            for k in m.get('TagGroups'):
                temp_model = ListTagResponseBodyTagGroups()
                self.tag_groups.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListTagResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTagResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagGroupRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        client_token: str = None,
        group_name: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.agent_key = agent_key
        self.client_token = client_token
        self.group_name = group_name
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListTagGroupResponseBodyTagGroups(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        create_user_id: int = None,
        create_user_name: str = None,
        default_tag_id: int = None,
        group_name: str = None,
        id: int = None,
        modify_time: str = None,
        modify_user_id: int = None,
        modify_user_name: str = None,
    ):
        self.create_time = create_time
        self.create_user_id = create_user_id
        self.create_user_name = create_user_name
        self.default_tag_id = default_tag_id
        self.group_name = group_name
        self.id = id
        self.modify_time = modify_time
        self.modify_user_id = modify_user_id
        self.modify_user_name = modify_user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.default_tag_id is not None:
            result['DefaultTagId'] = self.default_tag_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.id is not None:
            result['Id'] = self.id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.modify_user_id is not None:
            result['ModifyUserId'] = self.modify_user_id
        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('DefaultTagId') is not None:
            self.default_tag_id = m.get('DefaultTagId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ModifyUserId') is not None:
            self.modify_user_id = m.get('ModifyUserId')
        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')
        return self


class ListTagGroupResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        tag_groups: List[ListTagGroupResponseBodyTagGroups] = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.tag_groups = tag_groups
        self.total_count = total_count

    def validate(self):
        if self.tag_groups:
            for k in self.tag_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TagGroups'] = []
        if self.tag_groups is not None:
            for k in self.tag_groups:
                result['TagGroups'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tag_groups = []
        if m.get('TagGroups') is not None:
            for k in m.get('TagGroups'):
                temp_model = ListTagGroupResponseBodyTagGroups()
                self.tag_groups.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListTagGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTagGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListTagGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTongyiChatHistorysRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        end_time: str = None,
        limit: int = None,
        robot_instance_id: str = None,
        start_time: str = None,
    ):
        self.agent_key = agent_key
        # This parameter is required.
        self.end_time = end_time
        self.limit = limit
        # This parameter is required.
        self.robot_instance_id = robot_instance_id
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.robot_instance_id is not None:
            result['RobotInstanceId'] = self.robot_instance_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('RobotInstanceId') is not None:
            self.robot_instance_id = m.get('RobotInstanceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ListTongyiChatHistorysResponseBody(TeaModel):
    def __init__(
        self,
        cost_time: str = None,
        datas: List[Dict[str, Any]] = None,
        request_id: str = None,
    ):
        self.cost_time = cost_time
        self.datas = datas
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost_time is not None:
            result['CostTime'] = self.cost_time
        if self.datas is not None:
            result['Datas'] = self.datas
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostTime') is not None:
            self.cost_time = m.get('CostTime')
        if m.get('Datas') is not None:
            self.datas = m.get('Datas')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListTongyiChatHistorysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTongyiChatHistorysResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListTongyiChatHistorysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTongyiConversationLogsRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        robot_instance_id: str = None,
        session_id: str = None,
    ):
        self.agent_key = agent_key
        # This parameter is required.
        self.robot_instance_id = robot_instance_id
        # This parameter is required.
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.robot_instance_id is not None:
            result['RobotInstanceId'] = self.robot_instance_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('RobotInstanceId') is not None:
            self.robot_instance_id = m.get('RobotInstanceId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class ListTongyiConversationLogsResponseBody(TeaModel):
    def __init__(
        self,
        cost_time: str = None,
        datas: List[Dict[str, Any]] = None,
        request_id: str = None,
    ):
        self.cost_time = cost_time
        self.datas = datas
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost_time is not None:
            result['CostTime'] = self.cost_time
        if self.datas is not None:
            result['Datas'] = self.datas
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostTime') is not None:
            self.cost_time = m.get('CostTime')
        if m.get('Datas') is not None:
            self.datas = m.get('Datas')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListTongyiConversationLogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTongyiConversationLogsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListTongyiConversationLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserSayRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        content: str = None,
        instance_id: str = None,
        intent_id: int = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.agent_key = agent_key
        self.content = content
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.intent_id = intent_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.content is not None:
            result['Content'] = self.content
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListUserSayResponseBodyUserSaysSlotInfos(TeaModel):
    def __init__(
        self,
        end_index: int = None,
        slot_id: str = None,
        start_index: int = None,
    ):
        self.end_index = end_index
        self.slot_id = slot_id
        self.start_index = start_index

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_index is not None:
            result['EndIndex'] = self.end_index
        if self.slot_id is not None:
            result['SlotId'] = self.slot_id
        if self.start_index is not None:
            result['StartIndex'] = self.start_index
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndIndex') is not None:
            self.end_index = m.get('EndIndex')
        if m.get('SlotId') is not None:
            self.slot_id = m.get('SlotId')
        if m.get('StartIndex') is not None:
            self.start_index = m.get('StartIndex')
        return self


class ListUserSayResponseBodyUserSays(TeaModel):
    def __init__(
        self,
        content: str = None,
        create_time: str = None,
        intent_id: int = None,
        modify_time: str = None,
        slot_infos: List[ListUserSayResponseBodyUserSaysSlotInfos] = None,
        user_say_id: int = None,
    ):
        self.content = content
        self.create_time = create_time
        self.intent_id = intent_id
        self.modify_time = modify_time
        self.slot_infos = slot_infos
        self.user_say_id = user_say_id

    def validate(self):
        if self.slot_infos:
            for k in self.slot_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        result['SlotInfos'] = []
        if self.slot_infos is not None:
            for k in self.slot_infos:
                result['SlotInfos'].append(k.to_map() if k else None)
        if self.user_say_id is not None:
            result['UserSayId'] = self.user_say_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        self.slot_infos = []
        if m.get('SlotInfos') is not None:
            for k in m.get('SlotInfos'):
                temp_model = ListUserSayResponseBodyUserSaysSlotInfos()
                self.slot_infos.append(temp_model.from_map(k))
        if m.get('UserSayId') is not None:
            self.user_say_id = m.get('UserSayId')
        return self


class ListUserSayResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        user_says: List[ListUserSayResponseBodyUserSays] = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count
        self.user_says = user_says

    def validate(self):
        if self.user_says:
            for k in self.user_says:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['UserSays'] = []
        if self.user_says is not None:
            for k in self.user_says:
                result['UserSays'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.user_says = []
        if m.get('UserSays') is not None:
            for k in m.get('UserSays'):
                temp_model = ListUserSayResponseBodyUserSays()
                self.user_says.append(temp_model.from_map(k))
        return self


class ListUserSayResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListUserSayResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListUserSayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class NluRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        instance_id: str = None,
        utterance: str = None,
    ):
        self.agent_key = agent_key
        self.instance_id = instance_id
        self.utterance = utterance

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.utterance is not None:
            result['Utterance'] = self.utterance
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Utterance') is not None:
            self.utterance = m.get('Utterance')
        return self


class NluResponseBodyMessagesDialogHubNluInfoGlobalDictList(TeaModel):
    def __init__(
        self,
        standard_word: str = None,
        word: str = None,
    ):
        self.standard_word = standard_word
        self.word = word

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.standard_word is not None:
            result['StandardWord'] = self.standard_word
        if self.word is not None:
            result['Word'] = self.word
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StandardWord') is not None:
            self.standard_word = m.get('StandardWord')
        if m.get('Word') is not None:
            self.word = m.get('Word')
        return self


class NluResponseBodyMessagesDialogHubNluInfoGlobalSensitiveWordList(TeaModel):
    def __init__(
        self,
        standard_word: str = None,
        word: str = None,
    ):
        self.standard_word = standard_word
        self.word = word

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.standard_word is not None:
            result['StandardWord'] = self.standard_word
        if self.word is not None:
            result['Word'] = self.word
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StandardWord') is not None:
            self.standard_word = m.get('StandardWord')
        if m.get('Word') is not None:
            self.word = m.get('Word')
        return self


class NluResponseBodyMessagesDialogHubNluInfo(TeaModel):
    def __init__(
        self,
        global_dict_list: List[NluResponseBodyMessagesDialogHubNluInfoGlobalDictList] = None,
        global_sensitive_word_list: List[NluResponseBodyMessagesDialogHubNluInfoGlobalSensitiveWordList] = None,
    ):
        self.global_dict_list = global_dict_list
        self.global_sensitive_word_list = global_sensitive_word_list

    def validate(self):
        if self.global_dict_list:
            for k in self.global_dict_list:
                if k:
                    k.validate()
        if self.global_sensitive_word_list:
            for k in self.global_sensitive_word_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['GlobalDictList'] = []
        if self.global_dict_list is not None:
            for k in self.global_dict_list:
                result['GlobalDictList'].append(k.to_map() if k else None)
        result['GlobalSensitiveWordList'] = []
        if self.global_sensitive_word_list is not None:
            for k in self.global_sensitive_word_list:
                result['GlobalSensitiveWordList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.global_dict_list = []
        if m.get('GlobalDictList') is not None:
            for k in m.get('GlobalDictList'):
                temp_model = NluResponseBodyMessagesDialogHubNluInfoGlobalDictList()
                self.global_dict_list.append(temp_model.from_map(k))
        self.global_sensitive_word_list = []
        if m.get('GlobalSensitiveWordList') is not None:
            for k in m.get('GlobalSensitiveWordList'):
                temp_model = NluResponseBodyMessagesDialogHubNluInfoGlobalSensitiveWordList()
                self.global_sensitive_word_list.append(temp_model.from_map(k))
        return self


class NluResponseBodyMessagesDsNluInfoEntityList(TeaModel):
    def __init__(
        self,
        name: str = None,
        origin: str = None,
        type: str = None,
        value: str = None,
    ):
        self.name = name
        self.origin = origin
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.origin is not None:
            result['Origin'] = self.origin
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Origin') is not None:
            self.origin = m.get('Origin')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class NluResponseBodyMessagesDsNluInfoIntentListSlotList(TeaModel):
    def __init__(
        self,
        name: str = None,
        origin: str = None,
        type: str = None,
        value: str = None,
    ):
        self.name = name
        self.origin = origin
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.origin is not None:
            result['Origin'] = self.origin
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Origin') is not None:
            self.origin = m.get('Origin')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class NluResponseBodyMessagesDsNluInfoIntentList(TeaModel):
    def __init__(
        self,
        intent_id: int = None,
        match_detail: str = None,
        match_type: str = None,
        name: str = None,
        score: float = None,
        slot_list: List[NluResponseBodyMessagesDsNluInfoIntentListSlotList] = None,
    ):
        self.intent_id = intent_id
        self.match_detail = match_detail
        self.match_type = match_type
        self.name = name
        self.score = score
        self.slot_list = slot_list

    def validate(self):
        if self.slot_list:
            for k in self.slot_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        if self.match_detail is not None:
            result['MatchDetail'] = self.match_detail
        if self.match_type is not None:
            result['MatchType'] = self.match_type
        if self.name is not None:
            result['Name'] = self.name
        if self.score is not None:
            result['Score'] = self.score
        result['SlotList'] = []
        if self.slot_list is not None:
            for k in self.slot_list:
                result['SlotList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        if m.get('MatchDetail') is not None:
            self.match_detail = m.get('MatchDetail')
        if m.get('MatchType') is not None:
            self.match_type = m.get('MatchType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        self.slot_list = []
        if m.get('SlotList') is not None:
            for k in m.get('SlotList'):
                temp_model = NluResponseBodyMessagesDsNluInfoIntentListSlotList()
                self.slot_list.append(temp_model.from_map(k))
        return self


class NluResponseBodyMessagesDsNluInfo(TeaModel):
    def __init__(
        self,
        entity_list: List[NluResponseBodyMessagesDsNluInfoEntityList] = None,
        intent_list: List[NluResponseBodyMessagesDsNluInfoIntentList] = None,
    ):
        self.entity_list = entity_list
        self.intent_list = intent_list

    def validate(self):
        if self.entity_list:
            for k in self.entity_list:
                if k:
                    k.validate()
        if self.intent_list:
            for k in self.intent_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EntityList'] = []
        if self.entity_list is not None:
            for k in self.entity_list:
                result['EntityList'].append(k.to_map() if k else None)
        result['IntentList'] = []
        if self.intent_list is not None:
            for k in self.intent_list:
                result['IntentList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.entity_list = []
        if m.get('EntityList') is not None:
            for k in m.get('EntityList'):
                temp_model = NluResponseBodyMessagesDsNluInfoEntityList()
                self.entity_list.append(temp_model.from_map(k))
        self.intent_list = []
        if m.get('IntentList') is not None:
            for k in m.get('IntentList'):
                temp_model = NluResponseBodyMessagesDsNluInfoIntentList()
                self.intent_list.append(temp_model.from_map(k))
        return self


class NluResponseBodyMessages(TeaModel):
    def __init__(
        self,
        dialog_hub_nlu_info: NluResponseBodyMessagesDialogHubNluInfo = None,
        ds_nlu_info: NluResponseBodyMessagesDsNluInfo = None,
    ):
        self.dialog_hub_nlu_info = dialog_hub_nlu_info
        self.ds_nlu_info = ds_nlu_info

    def validate(self):
        if self.dialog_hub_nlu_info:
            self.dialog_hub_nlu_info.validate()
        if self.ds_nlu_info:
            self.ds_nlu_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dialog_hub_nlu_info is not None:
            result['DialogHubNluInfo'] = self.dialog_hub_nlu_info.to_map()
        if self.ds_nlu_info is not None:
            result['DsNluInfo'] = self.ds_nlu_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DialogHubNluInfo') is not None:
            temp_model = NluResponseBodyMessagesDialogHubNluInfo()
            self.dialog_hub_nlu_info = temp_model.from_map(m['DialogHubNluInfo'])
        if m.get('DsNluInfo') is not None:
            temp_model = NluResponseBodyMessagesDsNluInfo()
            self.ds_nlu_info = temp_model.from_map(m['DsNluInfo'])
        return self


class NluResponseBody(TeaModel):
    def __init__(
        self,
        message_id: str = None,
        messages: List[NluResponseBodyMessages] = None,
        request_id: str = None,
    ):
        self.message_id = message_id
        self.messages = messages
        self.request_id = request_id

    def validate(self):
        if self.messages:
            for k in self.messages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        result['Messages'] = []
        if self.messages is not None:
            for k in self.messages:
                result['Messages'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        self.messages = []
        if m.get('Messages') is not None:
            for k in m.get('Messages'):
                temp_model = NluResponseBodyMessages()
                self.messages.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class NluResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: NluResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = NluResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPerspectivesRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
    ):
        self.agent_key = agent_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        return self


class QueryPerspectivesResponseBodyPerspectives(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        modify_time: str = None,
        name: str = None,
        perspective_code: str = None,
        perspective_id: str = None,
        self_define: bool = None,
        status: int = None,
    ):
        self.create_time = create_time
        self.modify_time = modify_time
        self.name = name
        self.perspective_code = perspective_code
        self.perspective_id = perspective_id
        self.self_define = self_define
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.name is not None:
            result['Name'] = self.name
        if self.perspective_code is not None:
            result['PerspectiveCode'] = self.perspective_code
        if self.perspective_id is not None:
            result['PerspectiveId'] = self.perspective_id
        if self.self_define is not None:
            result['SelfDefine'] = self.self_define
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PerspectiveCode') is not None:
            self.perspective_code = m.get('PerspectiveCode')
        if m.get('PerspectiveId') is not None:
            self.perspective_id = m.get('PerspectiveId')
        if m.get('SelfDefine') is not None:
            self.self_define = m.get('SelfDefine')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class QueryPerspectivesResponseBody(TeaModel):
    def __init__(
        self,
        perspectives: List[QueryPerspectivesResponseBodyPerspectives] = None,
        request_id: str = None,
    ):
        self.perspectives = perspectives
        self.request_id = request_id

    def validate(self):
        if self.perspectives:
            for k in self.perspectives:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Perspectives'] = []
        if self.perspectives is not None:
            for k in self.perspectives:
                result['Perspectives'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.perspectives = []
        if m.get('Perspectives') is not None:
            for k in m.get('Perspectives'):
                temp_model = QueryPerspectivesResponseBodyPerspectives()
                self.perspectives.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryPerspectivesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryPerspectivesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = QueryPerspectivesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RetryDocRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        knowledge_id: int = None,
    ):
        self.agent_key = agent_key
        # This parameter is required.
        self.knowledge_id = knowledge_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        return self


class RetryDocResponseBody(TeaModel):
    def __init__(
        self,
        knowledge_id: int = None,
        request_id: str = None,
    ):
        self.knowledge_id = knowledge_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RetryDocResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RetryDocResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = RetryDocResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchDocRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        category_ids: List[int] = None,
        create_time_begin: str = None,
        create_time_end: str = None,
        create_user_name: str = None,
        end_time_begin: str = None,
        end_time_end: str = None,
        keyword: str = None,
        modify_time_begin: str = None,
        modify_time_end: str = None,
        modify_user_name: str = None,
        page_number: int = None,
        page_size: int = None,
        process_status: int = None,
        search_scope: int = None,
        start_time_begin: str = None,
        start_time_end: str = None,
        status: int = None,
        tag_ids: List[int] = None,
    ):
        self.agent_key = agent_key
        self.category_ids = category_ids
        self.create_time_begin = create_time_begin
        self.create_time_end = create_time_end
        self.create_user_name = create_user_name
        self.end_time_begin = end_time_begin
        self.end_time_end = end_time_end
        self.keyword = keyword
        self.modify_time_begin = modify_time_begin
        self.modify_time_end = modify_time_end
        self.modify_user_name = modify_user_name
        self.page_number = page_number
        self.page_size = page_size
        self.process_status = process_status
        self.search_scope = search_scope
        self.start_time_begin = start_time_begin
        self.start_time_end = start_time_end
        self.status = status
        self.tag_ids = tag_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.category_ids is not None:
            result['CategoryIds'] = self.category_ids
        if self.create_time_begin is not None:
            result['CreateTimeBegin'] = self.create_time_begin
        if self.create_time_end is not None:
            result['CreateTimeEnd'] = self.create_time_end
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.end_time_begin is not None:
            result['EndTimeBegin'] = self.end_time_begin
        if self.end_time_end is not None:
            result['EndTimeEnd'] = self.end_time_end
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.modify_time_begin is not None:
            result['ModifyTimeBegin'] = self.modify_time_begin
        if self.modify_time_end is not None:
            result['ModifyTimeEnd'] = self.modify_time_end
        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.process_status is not None:
            result['ProcessStatus'] = self.process_status
        if self.search_scope is not None:
            result['SearchScope'] = self.search_scope
        if self.start_time_begin is not None:
            result['StartTimeBegin'] = self.start_time_begin
        if self.start_time_end is not None:
            result['StartTimeEnd'] = self.start_time_end
        if self.status is not None:
            result['Status'] = self.status
        if self.tag_ids is not None:
            result['TagIds'] = self.tag_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('CategoryIds') is not None:
            self.category_ids = m.get('CategoryIds')
        if m.get('CreateTimeBegin') is not None:
            self.create_time_begin = m.get('CreateTimeBegin')
        if m.get('CreateTimeEnd') is not None:
            self.create_time_end = m.get('CreateTimeEnd')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('EndTimeBegin') is not None:
            self.end_time_begin = m.get('EndTimeBegin')
        if m.get('EndTimeEnd') is not None:
            self.end_time_end = m.get('EndTimeEnd')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('ModifyTimeBegin') is not None:
            self.modify_time_begin = m.get('ModifyTimeBegin')
        if m.get('ModifyTimeEnd') is not None:
            self.modify_time_end = m.get('ModifyTimeEnd')
        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProcessStatus') is not None:
            self.process_status = m.get('ProcessStatus')
        if m.get('SearchScope') is not None:
            self.search_scope = m.get('SearchScope')
        if m.get('StartTimeBegin') is not None:
            self.start_time_begin = m.get('StartTimeBegin')
        if m.get('StartTimeEnd') is not None:
            self.start_time_end = m.get('StartTimeEnd')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TagIds') is not None:
            self.tag_ids = m.get('TagIds')
        return self


class SearchDocShrinkRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        category_ids_shrink: str = None,
        create_time_begin: str = None,
        create_time_end: str = None,
        create_user_name: str = None,
        end_time_begin: str = None,
        end_time_end: str = None,
        keyword: str = None,
        modify_time_begin: str = None,
        modify_time_end: str = None,
        modify_user_name: str = None,
        page_number: int = None,
        page_size: int = None,
        process_status: int = None,
        search_scope: int = None,
        start_time_begin: str = None,
        start_time_end: str = None,
        status: int = None,
        tag_ids_shrink: str = None,
    ):
        self.agent_key = agent_key
        self.category_ids_shrink = category_ids_shrink
        self.create_time_begin = create_time_begin
        self.create_time_end = create_time_end
        self.create_user_name = create_user_name
        self.end_time_begin = end_time_begin
        self.end_time_end = end_time_end
        self.keyword = keyword
        self.modify_time_begin = modify_time_begin
        self.modify_time_end = modify_time_end
        self.modify_user_name = modify_user_name
        self.page_number = page_number
        self.page_size = page_size
        self.process_status = process_status
        self.search_scope = search_scope
        self.start_time_begin = start_time_begin
        self.start_time_end = start_time_end
        self.status = status
        self.tag_ids_shrink = tag_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.category_ids_shrink is not None:
            result['CategoryIds'] = self.category_ids_shrink
        if self.create_time_begin is not None:
            result['CreateTimeBegin'] = self.create_time_begin
        if self.create_time_end is not None:
            result['CreateTimeEnd'] = self.create_time_end
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.end_time_begin is not None:
            result['EndTimeBegin'] = self.end_time_begin
        if self.end_time_end is not None:
            result['EndTimeEnd'] = self.end_time_end
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.modify_time_begin is not None:
            result['ModifyTimeBegin'] = self.modify_time_begin
        if self.modify_time_end is not None:
            result['ModifyTimeEnd'] = self.modify_time_end
        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.process_status is not None:
            result['ProcessStatus'] = self.process_status
        if self.search_scope is not None:
            result['SearchScope'] = self.search_scope
        if self.start_time_begin is not None:
            result['StartTimeBegin'] = self.start_time_begin
        if self.start_time_end is not None:
            result['StartTimeEnd'] = self.start_time_end
        if self.status is not None:
            result['Status'] = self.status
        if self.tag_ids_shrink is not None:
            result['TagIds'] = self.tag_ids_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('CategoryIds') is not None:
            self.category_ids_shrink = m.get('CategoryIds')
        if m.get('CreateTimeBegin') is not None:
            self.create_time_begin = m.get('CreateTimeBegin')
        if m.get('CreateTimeEnd') is not None:
            self.create_time_end = m.get('CreateTimeEnd')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('EndTimeBegin') is not None:
            self.end_time_begin = m.get('EndTimeBegin')
        if m.get('EndTimeEnd') is not None:
            self.end_time_end = m.get('EndTimeEnd')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('ModifyTimeBegin') is not None:
            self.modify_time_begin = m.get('ModifyTimeBegin')
        if m.get('ModifyTimeEnd') is not None:
            self.modify_time_end = m.get('ModifyTimeEnd')
        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProcessStatus') is not None:
            self.process_status = m.get('ProcessStatus')
        if m.get('SearchScope') is not None:
            self.search_scope = m.get('SearchScope')
        if m.get('StartTimeBegin') is not None:
            self.start_time_begin = m.get('StartTimeBegin')
        if m.get('StartTimeEnd') is not None:
            self.start_time_end = m.get('StartTimeEnd')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TagIds') is not None:
            self.tag_ids_shrink = m.get('TagIds')
        return self


class SearchDocResponseBodyDocHitsDocTags(TeaModel):
    def __init__(
        self,
        default_tag: bool = None,
        group_id: int = None,
        group_name: str = None,
        tag_id: int = None,
        tag_name: str = None,
    ):
        self.default_tag = default_tag
        self.group_id = group_id
        self.group_name = group_name
        self.tag_id = tag_id
        self.tag_name = tag_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_tag is not None:
            result['DefaultTag'] = self.default_tag
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultTag') is not None:
            self.default_tag = m.get('DefaultTag')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        return self


class SearchDocResponseBodyDocHits(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
        category_id: int = None,
        config: str = None,
        create_time: str = None,
        create_user_id: int = None,
        create_user_name: str = None,
        doc_name: str = None,
        doc_tags: List[SearchDocResponseBodyDocHitsDocTags] = None,
        effect_status: int = None,
        end_date: str = None,
        knowledge_id: int = None,
        meta: str = None,
        modify_time: str = None,
        modify_user_id: int = None,
        modify_user_name: str = None,
        process_can_retry: bool = None,
        process_message: str = None,
        process_status: int = None,
        start_date: str = None,
        status: int = None,
        url: str = None,
    ):
        self.biz_code = biz_code
        self.category_id = category_id
        self.config = config
        self.create_time = create_time
        self.create_user_id = create_user_id
        self.create_user_name = create_user_name
        self.doc_name = doc_name
        self.doc_tags = doc_tags
        self.effect_status = effect_status
        self.end_date = end_date
        self.knowledge_id = knowledge_id
        self.meta = meta
        self.modify_time = modify_time
        self.modify_user_id = modify_user_id
        self.modify_user_name = modify_user_name
        self.process_can_retry = process_can_retry
        self.process_message = process_message
        self.process_status = process_status
        self.start_date = start_date
        self.status = status
        self.url = url

    def validate(self):
        if self.doc_tags:
            for k in self.doc_tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.config is not None:
            result['Config'] = self.config
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.doc_name is not None:
            result['DocName'] = self.doc_name
        result['DocTags'] = []
        if self.doc_tags is not None:
            for k in self.doc_tags:
                result['DocTags'].append(k.to_map() if k else None)
        if self.effect_status is not None:
            result['EffectStatus'] = self.effect_status
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        if self.meta is not None:
            result['Meta'] = self.meta
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.modify_user_id is not None:
            result['ModifyUserId'] = self.modify_user_id
        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name
        if self.process_can_retry is not None:
            result['ProcessCanRetry'] = self.process_can_retry
        if self.process_message is not None:
            result['ProcessMessage'] = self.process_message
        if self.process_status is not None:
            result['ProcessStatus'] = self.process_status
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.status is not None:
            result['Status'] = self.status
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('DocName') is not None:
            self.doc_name = m.get('DocName')
        self.doc_tags = []
        if m.get('DocTags') is not None:
            for k in m.get('DocTags'):
                temp_model = SearchDocResponseBodyDocHitsDocTags()
                self.doc_tags.append(temp_model.from_map(k))
        if m.get('EffectStatus') is not None:
            self.effect_status = m.get('EffectStatus')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        if m.get('Meta') is not None:
            self.meta = m.get('Meta')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ModifyUserId') is not None:
            self.modify_user_id = m.get('ModifyUserId')
        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')
        if m.get('ProcessCanRetry') is not None:
            self.process_can_retry = m.get('ProcessCanRetry')
        if m.get('ProcessMessage') is not None:
            self.process_message = m.get('ProcessMessage')
        if m.get('ProcessStatus') is not None:
            self.process_status = m.get('ProcessStatus')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class SearchDocResponseBody(TeaModel):
    def __init__(
        self,
        doc_hits: List[SearchDocResponseBodyDocHits] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.doc_hits = doc_hits
        self.page_number = page_number
        self.page_size = page_size
        # Id of the request
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.doc_hits:
            for k in self.doc_hits:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DocHits'] = []
        if self.doc_hits is not None:
            for k in self.doc_hits:
                result['DocHits'].append(k.to_map() if k else None)
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
        self.doc_hits = []
        if m.get('DocHits') is not None:
            for k in m.get('DocHits'):
                temp_model = SearchDocResponseBodyDocHits()
                self.doc_hits.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class SearchDocResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SearchDocResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = SearchDocResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchFaqRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        category_ids: List[int] = None,
        create_time_begin: str = None,
        create_time_end: str = None,
        create_user_name: str = None,
        end_time_begin: str = None,
        end_time_end: str = None,
        keyword: str = None,
        modify_time_begin: str = None,
        modify_time_end: str = None,
        modify_user_name: str = None,
        page_number: int = None,
        page_size: int = None,
        search_scope: int = None,
        start_time_begin: str = None,
        start_time_end: str = None,
        status: int = None,
    ):
        self.agent_key = agent_key
        self.category_ids = category_ids
        self.create_time_begin = create_time_begin
        self.create_time_end = create_time_end
        self.create_user_name = create_user_name
        self.end_time_begin = end_time_begin
        self.end_time_end = end_time_end
        self.keyword = keyword
        self.modify_time_begin = modify_time_begin
        self.modify_time_end = modify_time_end
        self.modify_user_name = modify_user_name
        self.page_number = page_number
        self.page_size = page_size
        self.search_scope = search_scope
        self.start_time_begin = start_time_begin
        self.start_time_end = start_time_end
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.category_ids is not None:
            result['CategoryIds'] = self.category_ids
        if self.create_time_begin is not None:
            result['CreateTimeBegin'] = self.create_time_begin
        if self.create_time_end is not None:
            result['CreateTimeEnd'] = self.create_time_end
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.end_time_begin is not None:
            result['EndTimeBegin'] = self.end_time_begin
        if self.end_time_end is not None:
            result['EndTimeEnd'] = self.end_time_end
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.modify_time_begin is not None:
            result['ModifyTimeBegin'] = self.modify_time_begin
        if self.modify_time_end is not None:
            result['ModifyTimeEnd'] = self.modify_time_end
        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_scope is not None:
            result['SearchScope'] = self.search_scope
        if self.start_time_begin is not None:
            result['StartTimeBegin'] = self.start_time_begin
        if self.start_time_end is not None:
            result['StartTimeEnd'] = self.start_time_end
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('CategoryIds') is not None:
            self.category_ids = m.get('CategoryIds')
        if m.get('CreateTimeBegin') is not None:
            self.create_time_begin = m.get('CreateTimeBegin')
        if m.get('CreateTimeEnd') is not None:
            self.create_time_end = m.get('CreateTimeEnd')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('EndTimeBegin') is not None:
            self.end_time_begin = m.get('EndTimeBegin')
        if m.get('EndTimeEnd') is not None:
            self.end_time_end = m.get('EndTimeEnd')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('ModifyTimeBegin') is not None:
            self.modify_time_begin = m.get('ModifyTimeBegin')
        if m.get('ModifyTimeEnd') is not None:
            self.modify_time_end = m.get('ModifyTimeEnd')
        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchScope') is not None:
            self.search_scope = m.get('SearchScope')
        if m.get('StartTimeBegin') is not None:
            self.start_time_begin = m.get('StartTimeBegin')
        if m.get('StartTimeEnd') is not None:
            self.start_time_end = m.get('StartTimeEnd')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class SearchFaqShrinkRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        category_ids_shrink: str = None,
        create_time_begin: str = None,
        create_time_end: str = None,
        create_user_name: str = None,
        end_time_begin: str = None,
        end_time_end: str = None,
        keyword: str = None,
        modify_time_begin: str = None,
        modify_time_end: str = None,
        modify_user_name: str = None,
        page_number: int = None,
        page_size: int = None,
        search_scope: int = None,
        start_time_begin: str = None,
        start_time_end: str = None,
        status: int = None,
    ):
        self.agent_key = agent_key
        self.category_ids_shrink = category_ids_shrink
        self.create_time_begin = create_time_begin
        self.create_time_end = create_time_end
        self.create_user_name = create_user_name
        self.end_time_begin = end_time_begin
        self.end_time_end = end_time_end
        self.keyword = keyword
        self.modify_time_begin = modify_time_begin
        self.modify_time_end = modify_time_end
        self.modify_user_name = modify_user_name
        self.page_number = page_number
        self.page_size = page_size
        self.search_scope = search_scope
        self.start_time_begin = start_time_begin
        self.start_time_end = start_time_end
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.category_ids_shrink is not None:
            result['CategoryIds'] = self.category_ids_shrink
        if self.create_time_begin is not None:
            result['CreateTimeBegin'] = self.create_time_begin
        if self.create_time_end is not None:
            result['CreateTimeEnd'] = self.create_time_end
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.end_time_begin is not None:
            result['EndTimeBegin'] = self.end_time_begin
        if self.end_time_end is not None:
            result['EndTimeEnd'] = self.end_time_end
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.modify_time_begin is not None:
            result['ModifyTimeBegin'] = self.modify_time_begin
        if self.modify_time_end is not None:
            result['ModifyTimeEnd'] = self.modify_time_end
        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_scope is not None:
            result['SearchScope'] = self.search_scope
        if self.start_time_begin is not None:
            result['StartTimeBegin'] = self.start_time_begin
        if self.start_time_end is not None:
            result['StartTimeEnd'] = self.start_time_end
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('CategoryIds') is not None:
            self.category_ids_shrink = m.get('CategoryIds')
        if m.get('CreateTimeBegin') is not None:
            self.create_time_begin = m.get('CreateTimeBegin')
        if m.get('CreateTimeEnd') is not None:
            self.create_time_end = m.get('CreateTimeEnd')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('EndTimeBegin') is not None:
            self.end_time_begin = m.get('EndTimeBegin')
        if m.get('EndTimeEnd') is not None:
            self.end_time_end = m.get('EndTimeEnd')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('ModifyTimeBegin') is not None:
            self.modify_time_begin = m.get('ModifyTimeBegin')
        if m.get('ModifyTimeEnd') is not None:
            self.modify_time_end = m.get('ModifyTimeEnd')
        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchScope') is not None:
            self.search_scope = m.get('SearchScope')
        if m.get('StartTimeBegin') is not None:
            self.start_time_begin = m.get('StartTimeBegin')
        if m.get('StartTimeEnd') is not None:
            self.start_time_end = m.get('StartTimeEnd')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class SearchFaqResponseBodyFaqHits(TeaModel):
    def __init__(
        self,
        category_id: int = None,
        create_time: str = None,
        create_user_id: int = None,
        create_user_name: str = None,
        effect_status: int = None,
        hit_similar_titles: List[str] = None,
        hit_solutions: List[str] = None,
        knowledge_id: int = None,
        modify_time: str = None,
        modify_user_id: int = None,
        modify_user_name: str = None,
        status: int = None,
        title: str = None,
    ):
        self.category_id = category_id
        self.create_time = create_time
        self.create_user_id = create_user_id
        self.create_user_name = create_user_name
        self.effect_status = effect_status
        self.hit_similar_titles = hit_similar_titles
        self.hit_solutions = hit_solutions
        self.knowledge_id = knowledge_id
        self.modify_time = modify_time
        self.modify_user_id = modify_user_id
        self.modify_user_name = modify_user_name
        self.status = status
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.effect_status is not None:
            result['EffectStatus'] = self.effect_status
        if self.hit_similar_titles is not None:
            result['HitSimilarTitles'] = self.hit_similar_titles
        if self.hit_solutions is not None:
            result['HitSolutions'] = self.hit_solutions
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.modify_user_id is not None:
            result['ModifyUserId'] = self.modify_user_id
        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('EffectStatus') is not None:
            self.effect_status = m.get('EffectStatus')
        if m.get('HitSimilarTitles') is not None:
            self.hit_similar_titles = m.get('HitSimilarTitles')
        if m.get('HitSolutions') is not None:
            self.hit_solutions = m.get('HitSolutions')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ModifyUserId') is not None:
            self.modify_user_id = m.get('ModifyUserId')
        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class SearchFaqResponseBody(TeaModel):
    def __init__(
        self,
        faq_hits: List[SearchFaqResponseBodyFaqHits] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.faq_hits = faq_hits
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.faq_hits:
            for k in self.faq_hits:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FaqHits'] = []
        if self.faq_hits is not None:
            for k in self.faq_hits:
                result['FaqHits'].append(k.to_map() if k else None)
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
        self.faq_hits = []
        if m.get('FaqHits') is not None:
            for k in m.get('FaqHits'):
                temp_model = SearchFaqResponseBodyFaqHits()
                self.faq_hits.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class SearchFaqResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SearchFaqResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = SearchFaqResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TongyiChatDebugInfoRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        instance_id: str = None,
        message_id: str = None,
    ):
        self.agent_key = agent_key
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.message_id = message_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        return self


class TongyiChatDebugInfoResponseBodyPipeline(TeaModel):
    def __init__(
        self,
        input: Any = None,
        name: str = None,
        node_type: str = None,
        output: Any = None,
    ):
        self.input = input
        self.name = name
        self.node_type = node_type
        self.output = output

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.input is not None:
            result['Input'] = self.input
        if self.name is not None:
            result['Name'] = self.name
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        if self.output is not None:
            result['Output'] = self.output
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Input') is not None:
            self.input = m.get('Input')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        return self


class TongyiChatDebugInfoResponseBody(TeaModel):
    def __init__(
        self,
        message_id: str = None,
        pipeline: List[TongyiChatDebugInfoResponseBodyPipeline] = None,
        request_id: str = None,
    ):
        self.message_id = message_id
        self.pipeline = pipeline
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.pipeline:
            for k in self.pipeline:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        result['Pipeline'] = []
        if self.pipeline is not None:
            for k in self.pipeline:
                result['Pipeline'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        self.pipeline = []
        if m.get('Pipeline') is not None:
            for k in m.get('Pipeline'):
                temp_model = TongyiChatDebugInfoResponseBodyPipeline()
                self.pipeline.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TongyiChatDebugInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TongyiChatDebugInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = TongyiChatDebugInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCategoryRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        biz_code: str = None,
        category_id: int = None,
        name: str = None,
    ):
        self.agent_key = agent_key
        self.biz_code = biz_code
        # This parameter is required.
        self.category_id = category_id
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdateCategoryResponseBody(TeaModel):
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


class UpdateCategoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateCategoryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = UpdateCategoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateConnQuestionRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        conn_question_id: int = None,
        outline_id: int = None,
    ):
        self.agent_key = agent_key
        # This parameter is required.
        self.conn_question_id = conn_question_id
        # This parameter is required.
        self.outline_id = outline_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.conn_question_id is not None:
            result['ConnQuestionId'] = self.conn_question_id
        if self.outline_id is not None:
            result['OutlineId'] = self.outline_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('ConnQuestionId') is not None:
            self.conn_question_id = m.get('ConnQuestionId')
        if m.get('OutlineId') is not None:
            self.outline_id = m.get('OutlineId')
        return self


class UpdateConnQuestionResponseBody(TeaModel):
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


class UpdateConnQuestionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateConnQuestionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = UpdateConnQuestionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDSEntityRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        entity_id: int = None,
        entity_name: str = None,
        entity_type: str = None,
        instance_id: str = None,
    ):
        self.agent_key = agent_key
        # This parameter is required.
        self.entity_id = entity_id
        # This parameter is required.
        self.entity_name = entity_name
        self.entity_type = entity_type
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.entity_name is not None:
            result['EntityName'] = self.entity_name
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class UpdateDSEntityResponseBody(TeaModel):
    def __init__(
        self,
        entity_id: int = None,
        request_id: str = None,
    ):
        self.entity_id = entity_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateDSEntityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateDSEntityResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = UpdateDSEntityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDSEntityValueRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        content: str = None,
        entity_id: int = None,
        entity_value_id: int = None,
        instance_id: str = None,
        synonyms: List[str] = None,
    ):
        self.agent_key = agent_key
        # This parameter is required.
        self.content = content
        # This parameter is required.
        self.entity_id = entity_id
        # This parameter is required.
        self.entity_value_id = entity_value_id
        # This parameter is required.
        self.instance_id = instance_id
        self.synonyms = synonyms

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.content is not None:
            result['Content'] = self.content
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.entity_value_id is not None:
            result['EntityValueId'] = self.entity_value_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.synonyms is not None:
            result['Synonyms'] = self.synonyms
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('EntityValueId') is not None:
            self.entity_value_id = m.get('EntityValueId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Synonyms') is not None:
            self.synonyms = m.get('Synonyms')
        return self


class UpdateDSEntityValueShrinkRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        content: str = None,
        entity_id: int = None,
        entity_value_id: int = None,
        instance_id: str = None,
        synonyms_shrink: str = None,
    ):
        self.agent_key = agent_key
        # This parameter is required.
        self.content = content
        # This parameter is required.
        self.entity_id = entity_id
        # This parameter is required.
        self.entity_value_id = entity_value_id
        # This parameter is required.
        self.instance_id = instance_id
        self.synonyms_shrink = synonyms_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.content is not None:
            result['Content'] = self.content
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.entity_value_id is not None:
            result['EntityValueId'] = self.entity_value_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.synonyms_shrink is not None:
            result['Synonyms'] = self.synonyms_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('EntityValueId') is not None:
            self.entity_value_id = m.get('EntityValueId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Synonyms') is not None:
            self.synonyms_shrink = m.get('Synonyms')
        return self


class UpdateDSEntityValueResponseBody(TeaModel):
    def __init__(
        self,
        entity_value_id: int = None,
        request_id: str = None,
    ):
        self.entity_value_id = entity_value_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_value_id is not None:
            result['EntityValueId'] = self.entity_value_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityValueId') is not None:
            self.entity_value_id = m.get('EntityValueId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateDSEntityValueResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateDSEntityValueResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = UpdateDSEntityValueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDocRequestDocMetadataMetaCellInfoDTOList(TeaModel):
    def __init__(
        self,
        field_code: str = None,
        field_name: str = None,
        value: str = None,
    ):
        self.field_code = field_code
        self.field_name = field_name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_code is not None:
            result['FieldCode'] = self.field_code
        if self.field_name is not None:
            result['FieldName'] = self.field_name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldCode') is not None:
            self.field_code = m.get('FieldCode')
        if m.get('FieldName') is not None:
            self.field_name = m.get('FieldName')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateDocRequestDocMetadata(TeaModel):
    def __init__(
        self,
        business_view_id: str = None,
        business_view_name: str = None,
        meta_cell_info_dtolist: List[UpdateDocRequestDocMetadataMetaCellInfoDTOList] = None,
    ):
        self.business_view_id = business_view_id
        self.business_view_name = business_view_name
        self.meta_cell_info_dtolist = meta_cell_info_dtolist

    def validate(self):
        if self.meta_cell_info_dtolist:
            for k in self.meta_cell_info_dtolist:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_view_id is not None:
            result['BusinessViewId'] = self.business_view_id
        if self.business_view_name is not None:
            result['BusinessViewName'] = self.business_view_name
        result['MetaCellInfoDTOList'] = []
        if self.meta_cell_info_dtolist is not None:
            for k in self.meta_cell_info_dtolist:
                result['MetaCellInfoDTOList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessViewId') is not None:
            self.business_view_id = m.get('BusinessViewId')
        if m.get('BusinessViewName') is not None:
            self.business_view_name = m.get('BusinessViewName')
        self.meta_cell_info_dtolist = []
        if m.get('MetaCellInfoDTOList') is not None:
            for k in m.get('MetaCellInfoDTOList'):
                temp_model = UpdateDocRequestDocMetadataMetaCellInfoDTOList()
                self.meta_cell_info_dtolist.append(temp_model.from_map(k))
        return self


class UpdateDocRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        category_id: int = None,
        config: str = None,
        content: str = None,
        doc_metadata: List[UpdateDocRequestDocMetadata] = None,
        doc_name: str = None,
        end_date: str = None,
        knowledge_id: int = None,
        meta: str = None,
        start_date: str = None,
        tag_ids: List[int] = None,
        title: str = None,
    ):
        self.agent_key = agent_key
        self.category_id = category_id
        self.config = config
        self.content = content
        self.doc_metadata = doc_metadata
        self.doc_name = doc_name
        self.end_date = end_date
        # This parameter is required.
        self.knowledge_id = knowledge_id
        self.meta = meta
        self.start_date = start_date
        self.tag_ids = tag_ids
        self.title = title

    def validate(self):
        if self.doc_metadata:
            for k in self.doc_metadata:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.config is not None:
            result['Config'] = self.config
        if self.content is not None:
            result['Content'] = self.content
        result['DocMetadata'] = []
        if self.doc_metadata is not None:
            for k in self.doc_metadata:
                result['DocMetadata'].append(k.to_map() if k else None)
        if self.doc_name is not None:
            result['DocName'] = self.doc_name
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        if self.meta is not None:
            result['Meta'] = self.meta
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.tag_ids is not None:
            result['TagIds'] = self.tag_ids
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        self.doc_metadata = []
        if m.get('DocMetadata') is not None:
            for k in m.get('DocMetadata'):
                temp_model = UpdateDocRequestDocMetadata()
                self.doc_metadata.append(temp_model.from_map(k))
        if m.get('DocName') is not None:
            self.doc_name = m.get('DocName')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        if m.get('Meta') is not None:
            self.meta = m.get('Meta')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('TagIds') is not None:
            self.tag_ids = m.get('TagIds')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class UpdateDocShrinkRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        category_id: int = None,
        config: str = None,
        content: str = None,
        doc_metadata_shrink: str = None,
        doc_name: str = None,
        end_date: str = None,
        knowledge_id: int = None,
        meta: str = None,
        start_date: str = None,
        tag_ids_shrink: str = None,
        title: str = None,
    ):
        self.agent_key = agent_key
        self.category_id = category_id
        self.config = config
        self.content = content
        self.doc_metadata_shrink = doc_metadata_shrink
        self.doc_name = doc_name
        self.end_date = end_date
        # This parameter is required.
        self.knowledge_id = knowledge_id
        self.meta = meta
        self.start_date = start_date
        self.tag_ids_shrink = tag_ids_shrink
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.config is not None:
            result['Config'] = self.config
        if self.content is not None:
            result['Content'] = self.content
        if self.doc_metadata_shrink is not None:
            result['DocMetadata'] = self.doc_metadata_shrink
        if self.doc_name is not None:
            result['DocName'] = self.doc_name
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        if self.meta is not None:
            result['Meta'] = self.meta
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.tag_ids_shrink is not None:
            result['TagIds'] = self.tag_ids_shrink
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('DocMetadata') is not None:
            self.doc_metadata_shrink = m.get('DocMetadata')
        if m.get('DocName') is not None:
            self.doc_name = m.get('DocName')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        if m.get('Meta') is not None:
            self.meta = m.get('Meta')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('TagIds') is not None:
            self.tag_ids_shrink = m.get('TagIds')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class UpdateDocResponseBody(TeaModel):
    def __init__(
        self,
        knowledge_id: int = None,
        request_id: str = None,
    ):
        self.knowledge_id = knowledge_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateDocResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateDocResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = UpdateDocResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFaqRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        category_id: int = None,
        end_date: str = None,
        knowledge_id: int = None,
        start_date: str = None,
        tag_id_list: List[int] = None,
        title: str = None,
    ):
        self.agent_key = agent_key
        # This parameter is required.
        self.category_id = category_id
        self.end_date = end_date
        # This parameter is required.
        self.knowledge_id = knowledge_id
        self.start_date = start_date
        self.tag_id_list = tag_id_list
        # This parameter is required.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.tag_id_list is not None:
            result['TagIdList'] = self.tag_id_list
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('TagIdList') is not None:
            self.tag_id_list = m.get('TagIdList')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class UpdateFaqShrinkRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        category_id: int = None,
        end_date: str = None,
        knowledge_id: int = None,
        start_date: str = None,
        tag_id_list_shrink: str = None,
        title: str = None,
    ):
        self.agent_key = agent_key
        # This parameter is required.
        self.category_id = category_id
        self.end_date = end_date
        # This parameter is required.
        self.knowledge_id = knowledge_id
        self.start_date = start_date
        self.tag_id_list_shrink = tag_id_list_shrink
        # This parameter is required.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.tag_id_list_shrink is not None:
            result['TagIdList'] = self.tag_id_list_shrink
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('TagIdList') is not None:
            self.tag_id_list_shrink = m.get('TagIdList')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class UpdateFaqResponseBody(TeaModel):
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


class UpdateFaqResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateFaqResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = UpdateFaqResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateInstanceRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        instance_id: str = None,
        introduction: str = None,
        name: str = None,
    ):
        self.agent_key = agent_key
        self.instance_id = instance_id
        self.introduction = introduction
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.introduction is not None:
            result['Introduction'] = self.introduction
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Introduction') is not None:
            self.introduction = m.get('Introduction')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdateInstanceResponseBody(TeaModel):
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


class UpdateInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = UpdateInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateIntentRequestIntentDefinitionSlotInfos(TeaModel):
    def __init__(
        self,
        array: bool = None,
        encrypt: bool = None,
        interactive: bool = None,
        name: str = None,
        slot_id: str = None,
        value: str = None,
    ):
        self.array = array
        self.encrypt = encrypt
        self.interactive = interactive
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.slot_id = slot_id
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.array is not None:
            result['Array'] = self.array
        if self.encrypt is not None:
            result['Encrypt'] = self.encrypt
        if self.interactive is not None:
            result['Interactive'] = self.interactive
        if self.name is not None:
            result['Name'] = self.name
        if self.slot_id is not None:
            result['SlotId'] = self.slot_id
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Array') is not None:
            self.array = m.get('Array')
        if m.get('Encrypt') is not None:
            self.encrypt = m.get('Encrypt')
        if m.get('Interactive') is not None:
            self.interactive = m.get('Interactive')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SlotId') is not None:
            self.slot_id = m.get('SlotId')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateIntentRequestIntentDefinition(TeaModel):
    def __init__(
        self,
        alias_name: str = None,
        intent_name: str = None,
        slot_infos: List[UpdateIntentRequestIntentDefinitionSlotInfos] = None,
    ):
        self.alias_name = alias_name
        # This parameter is required.
        self.intent_name = intent_name
        self.slot_infos = slot_infos

    def validate(self):
        if self.slot_infos:
            for k in self.slot_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name
        if self.intent_name is not None:
            result['IntentName'] = self.intent_name
        result['SlotInfos'] = []
        if self.slot_infos is not None:
            for k in self.slot_infos:
                result['SlotInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')
        if m.get('IntentName') is not None:
            self.intent_name = m.get('IntentName')
        self.slot_infos = []
        if m.get('SlotInfos') is not None:
            for k in m.get('SlotInfos'):
                temp_model = UpdateIntentRequestIntentDefinitionSlotInfos()
                self.slot_infos.append(temp_model.from_map(k))
        return self


class UpdateIntentRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        instance_id: str = None,
        intent_definition: UpdateIntentRequestIntentDefinition = None,
        intent_id: int = None,
    ):
        self.agent_key = agent_key
        # This parameter is required.
        self.instance_id = instance_id
        self.intent_definition = intent_definition
        # This parameter is required.
        self.intent_id = intent_id

    def validate(self):
        if self.intent_definition:
            self.intent_definition.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.intent_definition is not None:
            result['IntentDefinition'] = self.intent_definition.to_map()
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IntentDefinition') is not None:
            temp_model = UpdateIntentRequestIntentDefinition()
            self.intent_definition = temp_model.from_map(m['IntentDefinition'])
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        return self


class UpdateIntentShrinkRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        instance_id: str = None,
        intent_definition_shrink: str = None,
        intent_id: int = None,
    ):
        self.agent_key = agent_key
        # This parameter is required.
        self.instance_id = instance_id
        self.intent_definition_shrink = intent_definition_shrink
        # This parameter is required.
        self.intent_id = intent_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.intent_definition_shrink is not None:
            result['IntentDefinition'] = self.intent_definition_shrink
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IntentDefinition') is not None:
            self.intent_definition_shrink = m.get('IntentDefinition')
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        return self


class UpdateIntentResponseBody(TeaModel):
    def __init__(
        self,
        intent_id: int = None,
        request_id: str = None,
    ):
        self.intent_id = intent_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateIntentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateIntentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = UpdateIntentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateLgfRequestLgfDefinition(TeaModel):
    def __init__(
        self,
        intent_id: int = None,
        rule_text: str = None,
    ):
        # This parameter is required.
        self.intent_id = intent_id
        # This parameter is required.
        self.rule_text = rule_text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        if self.rule_text is not None:
            result['RuleText'] = self.rule_text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        if m.get('RuleText') is not None:
            self.rule_text = m.get('RuleText')
        return self


class UpdateLgfRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        instance_id: str = None,
        lgf_definition: UpdateLgfRequestLgfDefinition = None,
        lgf_id: int = None,
    ):
        self.agent_key = agent_key
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.lgf_definition = lgf_definition
        # LGF ID
        # 
        # This parameter is required.
        self.lgf_id = lgf_id

    def validate(self):
        if self.lgf_definition:
            self.lgf_definition.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lgf_definition is not None:
            result['LgfDefinition'] = self.lgf_definition.to_map()
        if self.lgf_id is not None:
            result['LgfId'] = self.lgf_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LgfDefinition') is not None:
            temp_model = UpdateLgfRequestLgfDefinition()
            self.lgf_definition = temp_model.from_map(m['LgfDefinition'])
        if m.get('LgfId') is not None:
            self.lgf_id = m.get('LgfId')
        return self


class UpdateLgfShrinkRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        instance_id: str = None,
        lgf_definition_shrink: str = None,
        lgf_id: int = None,
    ):
        self.agent_key = agent_key
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.lgf_definition_shrink = lgf_definition_shrink
        # LGF ID
        # 
        # This parameter is required.
        self.lgf_id = lgf_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lgf_definition_shrink is not None:
            result['LgfDefinition'] = self.lgf_definition_shrink
        if self.lgf_id is not None:
            result['LgfId'] = self.lgf_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LgfDefinition') is not None:
            self.lgf_definition_shrink = m.get('LgfDefinition')
        if m.get('LgfId') is not None:
            self.lgf_id = m.get('LgfId')
        return self


class UpdateLgfResponseBody(TeaModel):
    def __init__(
        self,
        lgf_id: int = None,
        request_id: str = None,
    ):
        self.lgf_id = lgf_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lgf_id is not None:
            result['LgfId'] = self.lgf_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LgfId') is not None:
            self.lgf_id = m.get('LgfId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateLgfResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateLgfResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = UpdateLgfResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePerspectiveRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        name: str = None,
        perspective_id: str = None,
    ):
        self.agent_key = agent_key
        self.name = name
        self.perspective_id = perspective_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.name is not None:
            result['Name'] = self.name
        if self.perspective_id is not None:
            result['PerspectiveId'] = self.perspective_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PerspectiveId') is not None:
            self.perspective_id = m.get('PerspectiveId')
        return self


class UpdatePerspectiveResponseBody(TeaModel):
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


class UpdatePerspectiveResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdatePerspectiveResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = UpdatePerspectiveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSimQuestionRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        sim_question_id: int = None,
        title: str = None,
    ):
        self.agent_key = agent_key
        # This parameter is required.
        self.sim_question_id = sim_question_id
        # This parameter is required.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.sim_question_id is not None:
            result['SimQuestionId'] = self.sim_question_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('SimQuestionId') is not None:
            self.sim_question_id = m.get('SimQuestionId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class UpdateSimQuestionResponseBody(TeaModel):
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


class UpdateSimQuestionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateSimQuestionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = UpdateSimQuestionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSolutionRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        content: str = None,
        content_type: int = None,
        perspective_codes: List[str] = None,
        solution_id: int = None,
        tag_id_list: List[int] = None,
    ):
        self.agent_key = agent_key
        # This parameter is required.
        self.content = content
        self.content_type = content_type
        # This parameter is required.
        self.perspective_codes = perspective_codes
        # This parameter is required.
        self.solution_id = solution_id
        self.tag_id_list = tag_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.content is not None:
            result['Content'] = self.content
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.perspective_codes is not None:
            result['PerspectiveCodes'] = self.perspective_codes
        if self.solution_id is not None:
            result['SolutionId'] = self.solution_id
        if self.tag_id_list is not None:
            result['TagIdList'] = self.tag_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('PerspectiveCodes') is not None:
            self.perspective_codes = m.get('PerspectiveCodes')
        if m.get('SolutionId') is not None:
            self.solution_id = m.get('SolutionId')
        if m.get('TagIdList') is not None:
            self.tag_id_list = m.get('TagIdList')
        return self


class UpdateSolutionShrinkRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        content: str = None,
        content_type: int = None,
        perspective_codes: List[str] = None,
        solution_id: int = None,
        tag_id_list_shrink: str = None,
    ):
        self.agent_key = agent_key
        # This parameter is required.
        self.content = content
        self.content_type = content_type
        # This parameter is required.
        self.perspective_codes = perspective_codes
        # This parameter is required.
        self.solution_id = solution_id
        self.tag_id_list_shrink = tag_id_list_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.content is not None:
            result['Content'] = self.content
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.perspective_codes is not None:
            result['PerspectiveCodes'] = self.perspective_codes
        if self.solution_id is not None:
            result['SolutionId'] = self.solution_id
        if self.tag_id_list_shrink is not None:
            result['TagIdList'] = self.tag_id_list_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('PerspectiveCodes') is not None:
            self.perspective_codes = m.get('PerspectiveCodes')
        if m.get('SolutionId') is not None:
            self.solution_id = m.get('SolutionId')
        if m.get('TagIdList') is not None:
            self.tag_id_list_shrink = m.get('TagIdList')
        return self


class UpdateSolutionResponseBody(TeaModel):
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


class UpdateSolutionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateSolutionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = UpdateSolutionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTagRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        client_token: str = None,
        group_id: int = None,
        id: int = None,
        tag_name: str = None,
    ):
        self.agent_key = agent_key
        self.client_token = client_token
        # This parameter is required.
        self.group_id = group_id
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.tag_name = tag_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.id is not None:
            result['Id'] = self.id
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        return self


class UpdateTagResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateTagResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateTagResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = UpdateTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTagGroupRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        client_token: str = None,
        group_name: str = None,
        id: int = None,
    ):
        self.agent_key = agent_key
        self.client_token = client_token
        # This parameter is required.
        self.group_name = group_name
        # This parameter is required.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class UpdateTagGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateTagGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateTagGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = UpdateTagGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateUserSayRequestUserSayDefinitionSlotInfos(TeaModel):
    def __init__(
        self,
        end_index: int = None,
        slot_id: str = None,
        start_index: int = None,
    ):
        self.end_index = end_index
        self.slot_id = slot_id
        self.start_index = start_index

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_index is not None:
            result['EndIndex'] = self.end_index
        if self.slot_id is not None:
            result['SlotId'] = self.slot_id
        if self.start_index is not None:
            result['StartIndex'] = self.start_index
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndIndex') is not None:
            self.end_index = m.get('EndIndex')
        if m.get('SlotId') is not None:
            self.slot_id = m.get('SlotId')
        if m.get('StartIndex') is not None:
            self.start_index = m.get('StartIndex')
        return self


class UpdateUserSayRequestUserSayDefinition(TeaModel):
    def __init__(
        self,
        content: str = None,
        intent_id: int = None,
        slot_infos: List[UpdateUserSayRequestUserSayDefinitionSlotInfos] = None,
    ):
        # This parameter is required.
        self.content = content
        # This parameter is required.
        self.intent_id = intent_id
        self.slot_infos = slot_infos

    def validate(self):
        if self.slot_infos:
            for k in self.slot_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        result['SlotInfos'] = []
        if self.slot_infos is not None:
            for k in self.slot_infos:
                result['SlotInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        self.slot_infos = []
        if m.get('SlotInfos') is not None:
            for k in m.get('SlotInfos'):
                temp_model = UpdateUserSayRequestUserSayDefinitionSlotInfos()
                self.slot_infos.append(temp_model.from_map(k))
        return self


class UpdateUserSayRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        instance_id: str = None,
        user_say_definition: UpdateUserSayRequestUserSayDefinition = None,
        user_say_id: int = None,
    ):
        self.agent_key = agent_key
        # This parameter is required.
        self.instance_id = instance_id
        self.user_say_definition = user_say_definition
        # This parameter is required.
        self.user_say_id = user_say_id

    def validate(self):
        if self.user_say_definition:
            self.user_say_definition.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.user_say_definition is not None:
            result['UserSayDefinition'] = self.user_say_definition.to_map()
        if self.user_say_id is not None:
            result['UserSayId'] = self.user_say_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('UserSayDefinition') is not None:
            temp_model = UpdateUserSayRequestUserSayDefinition()
            self.user_say_definition = temp_model.from_map(m['UserSayDefinition'])
        if m.get('UserSayId') is not None:
            self.user_say_id = m.get('UserSayId')
        return self


class UpdateUserSayShrinkRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        instance_id: str = None,
        user_say_definition_shrink: str = None,
        user_say_id: int = None,
    ):
        self.agent_key = agent_key
        # This parameter is required.
        self.instance_id = instance_id
        self.user_say_definition_shrink = user_say_definition_shrink
        # This parameter is required.
        self.user_say_id = user_say_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.user_say_definition_shrink is not None:
            result['UserSayDefinition'] = self.user_say_definition_shrink
        if self.user_say_id is not None:
            result['UserSayId'] = self.user_say_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('UserSayDefinition') is not None:
            self.user_say_definition_shrink = m.get('UserSayDefinition')
        if m.get('UserSayId') is not None:
            self.user_say_id = m.get('UserSayId')
        return self


class UpdateUserSayResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        user_say_id: int = None,
    ):
        self.request_id = request_id
        self.user_say_id = user_say_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user_say_id is not None:
            result['UserSayId'] = self.user_say_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UserSayId') is not None:
            self.user_say_id = m.get('UserSayId')
        return self


class UpdateUserSayResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateUserSayResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = UpdateUserSayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


