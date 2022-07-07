# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


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
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        # 机器人ID
        self.instance_id = instance_id
        # 视角编码，用于调用同一知识标题下不同视角的答案。在拼装请求参数时，需要以Perspective={视角编码}的格式传递参数。如：&Perspective=["FZJBY3raWr"]。使用SDK时以SDK中定义的参数为准。目前仅支持一个视角答案的调用。       （公有云）
        self.perspective = perspective
        # 推荐问题数量，1-10，当出推荐的时候才生效，返回不大于RecommendN
        self.recommend_num = recommend_num
        # 会话ID，用于标识一个访问者的会话和保持上下文信息。对于一个新的访问者，首次调用Chat接口时无需传递此字段，机器人会开启一个会话，并在Chat接口的响应中返回该会话的SessionId。对于该访问者的后续轮次的会话，调用Chat接口时传递当前会话的SessionId，机器人即可基于SessionId继续该轮次会话。
        self.session_id = session_id
        # 用户表述
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
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        # 机器人ID
        self.instance_id = instance_id
        # 视角编码，用于调用同一知识标题下不同视角的答案。在拼装请求参数时，需要以Perspective={视角编码}的格式传递参数。如：&Perspective=["FZJBY3raWr"]。使用SDK时以SDK中定义的参数为准。目前仅支持一个视角答案的调用。       （公有云）
        self.perspective_shrink = perspective_shrink
        # 推荐问题数量，1-10，当出推荐的时候才生效，返回不大于RecommendN
        self.recommend_num = recommend_num
        # 会话ID，用于标识一个访问者的会话和保持上下文信息。对于一个新的访问者，首次调用Chat接口时无需传递此字段，机器人会开启一个会话，并在Chat接口的响应中返回该会话的SessionId。对于该访问者的后续轮次的会话，调用Chat接口时传递当前会话的SessionId，机器人即可基于SessionId继续该轮次会话。
        self.session_id = session_id
        # 用户表述
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
        # 附带信息
        self.meta = meta
        # 关联问题的标题
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
        # 联想的列表
        self.associate = associate
        # 本条会话应答消息的ID
        self.message_id = message_id
        # 请求id
        self.request_id = request_id
        # 本次会话的ID
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
            temp_model = AssociateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BeginSessionRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        instance_id: str = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        # 机器人ID
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


class BeginSessionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        welcome_message: str = None,
    ):
        # 请求id
        self.request_id = request_id
        # 欢迎语
        self.welcome_message = welcome_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.welcome_message is not None:
            result['WelcomeMessage'] = self.welcome_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        # 任务ID
        self.id = id
        # 机器人ID
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
        # 业务类型列表
        self.biz_type_list = biz_type_list
        # 任务创建的 UTC 时间
        self.create_time = create_time
        # job失败信息
        self.error = error
        # 任务Id
        self.id = id
        # 任务修改的 UTC 时间
        self.modify_time = modify_time
        # 请求Id
        self.request_id = request_id
        # 任务Id
        self.response = response
        # 任务状态
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
            temp_model = CancelInstancePublishTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelPublishTaskRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        id: int = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        # 任务ID
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
        # 业务类型列表
        self.biz_type_list = biz_type_list
        # 任务创建的 UTC 时间
        self.create_time = create_time
        # job失败信息
        self.error = error
        # 任务Id
        self.id = id
        # 任务修改的 UTC 时间
        self.modify_time = modify_time
        # 请求Id
        self.request_id = request_id
        # 任务Id
        self.response = response
        # 任务状态
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
        sender_id: str = None,
        sender_nick: str = None,
        session_id: str = None,
        utterance: str = None,
        vendor_param: str = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        # 机器人实例ID。登录云小蜜控制台，机器人详情->会话接口，查看机器人实例信息，可获得该实例ID。
        self.instance_id = instance_id
        # 对话流中意图名称。 若指定此名称，机器人会直接进入此意图做问答
        self.intent_name = intent_name
        # 知识库中知识标题的ID。若指定此ID，那么机器人会直接返回指定知识标题的答案
        self.knowledge_id = knowledge_id
        # 视角编码，用于调用同一知识标题下不同视角的答案。如：Perspective=["FZJBY3raWr"]。使用SDK时以SDK中定义的参数为准
        self.perspective = perspective
        # 访问者ID。用于识别当前会话中的用户
        self.sender_id = sender_id
        # 当前会话中访问的昵称
        self.sender_nick = sender_nick
        # 会话ID，用于标识一个访问者的会话和保持上下文信息。对于一个新的访问者，首次调用Chat接口时无需传递此字段，机器人会开启一个会话，并在Chat接口的响应中返回该会话的SessionId。对于该访问者的后续轮次的会话，调用Chat接口时传递当前会话的SessionId，机器人即可基于SessionId继续该轮次会话。长度限制是64个字符
        self.session_id = session_id
        # 机器人访问者的输入
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
        sender_id: str = None,
        sender_nick: str = None,
        session_id: str = None,
        utterance: str = None,
        vendor_param: str = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        # 机器人实例ID。登录云小蜜控制台，机器人详情->会话接口，查看机器人实例信息，可获得该实例ID。
        self.instance_id = instance_id
        # 对话流中意图名称。 若指定此名称，机器人会直接进入此意图做问答
        self.intent_name = intent_name
        # 知识库中知识标题的ID。若指定此ID，那么机器人会直接返回指定知识标题的答案
        self.knowledge_id = knowledge_id
        # 视角编码，用于调用同一知识标题下不同视角的答案。如：Perspective=["FZJBY3raWr"]。使用SDK时以SDK中定义的参数为准
        self.perspective_shrink = perspective_shrink
        # 访问者ID。用于识别当前会话中的用户
        self.sender_id = sender_id
        # 当前会话中访问的昵称
        self.sender_nick = sender_nick
        # 会话ID，用于标识一个访问者的会话和保持上下文信息。对于一个新的访问者，首次调用Chat接口时无需传递此字段，机器人会开启一个会话，并在Chat接口的响应中返回该会话的SessionId。对于该访问者的后续轮次的会话，调用Chat接口时传递当前会话的SessionId，机器人即可基于SessionId继续该轮次会话。长度限制是64个字符
        self.session_id = session_id
        # 机器人访问者的输入
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
        # 知识关联知识的ID
        self.knowledge_id = knowledge_id
        # 知识的关联知识的标题
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
        # 区分答案类型。
        # KnowledgeBase:知识库条；
        self.answer_source = answer_source
        # 知识类目
        self.category = category
        # 命中问题的内容
        self.content = content
        # 纯文本/富文本答案的标示
        self.content_type = content_type
        # 命中语句
        self.hit_statement = hit_statement
        # 命中问题在知识库中的ID
        self.id = id
        # 关联知识列表
        self.related_knowledges = related_knowledges
        # 分数
        self.score = score
        # 命中问题的简介
        self.summary = summary
        # 命中问题的标题
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
        # 澄清来源的标识
        self.answer_source = answer_source
        # 澄清的知识id
        self.knowledge_id = knowledge_id
        # 推荐内容的分数，当AnswerSource为KNOWLEDGE时，此字段有值
        self.score = score
        # 澄清内容，可能是
        # 图谱问答的实体、
        # 知识问答的知识标题、
        # 表格问答的列值
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
        score: float = None,
        slots: List[ChatResponseBodyMessagesTextSlots] = None,
        user_defined_chat_title: str = None,
    ):
        # 区分答案类型
        self.answer_source = answer_source
        # 当AnswerSource为MACHINE_READ时，此字段返回命中文章标题
        self.article_title = article_title
        # 指令参数，如转人工指令的转人工技能组
        self.commands = commands
        # 文本消息的内容
        self.content = content
        # 纯文本/富文本答案的标示
        self.content_type = content_type
        # 当AnswerSource为BotFramework时，此字段返回对话单元名称
        self.dialog_name = dialog_name
        # 此字段返回透传参数
        self.ext = ext
        # 当AnswerSource为BotFramework时，此字段返回透传参数
        self.external_flags = external_flags
        # 命中语句
        self.hit_statement = hit_statement
        # 当AnswerSource为BotFramework时，此字段返回意图名称
        self.intent_name = intent_name
        self.meta_data = meta_data
        # 当AnswerSource为BotFramework时，此字段返回节点Id
        self.node_id = node_id
        # 当AnswerSource为BotFramework时，此字段返回节点名称
        self.node_name = node_name
        # 分数
        self.score = score
        # 当AnswerSource为BotFramework时，此字段返回专有名词列表
        self.slots = slots
        # 自定义闲聊主题title
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
        # 当AnswerType为Recommend时，此字段表示推荐的答案来源
        self.answer_source = answer_source
        # 本条消息的类型
        self.answer_type = answer_type
        # 当AnswerType为Knowledge时，此字段包含机器人返回的Knowledge对象
        self.knowledge = knowledge
        # 当AnswerType为Recommend时，此字段包含机器人返回的Recommend的列表
        self.recommends = recommends
        # 当AnswerType为Text时，此字段包含机器人返回的Text对象
        self.text = text
        # 当AnswerType为Recommend时，此字段表示推荐或者反问的标题话术
        self.title = title
        # 当AnswerType为Recommend时，并且问答的机器人为语音机器人，此字段表示列表型答案在语音场景渲染之后的答案内容
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
        # 本条会话应答消息的ID
        self.message_id = message_id
        # 消息的列表
        self.messages = messages
        # query的分词结果，可能为空
        self.query_seg_list = query_seg_list
        # 请求id
        self.request_id = request_id
        # 本次会话的ID
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
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        # 任务ID
        self.id = id
        # 机器人ID
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
        # 业务类型列表
        self.biz_type_list = biz_type_list
        # 任务创建的 UTC 时间
        self.create_time = create_time
        # job失败信息
        self.error = error
        # 各子发布模块的错误信息，key是子发布模块，value是错误信息
        self.errors = errors
        # 任务Id
        self.id = id
        # 任务修改的 UTC 时间
        self.modify_time = modify_time
        # 请求Id
        self.request_id = request_id
        # 任务Id
        self.response = response
        # 任务状态
        self.status = status
        # 各子发布模块的警告信息，key是子发布模块，value是警告信息
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
            temp_model = ContinueInstancePublishTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCategoryRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        name: str = None,
        parent_category_id: int = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        # 类目名称
        self.name = name
        # 父类目ID，默认-1，对应根目录
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
        if self.name is not None:
            result['Name'] = self.name
        if self.parent_category_id is not None:
            result['ParentCategoryId'] = self.parent_category_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParentCategoryId') is not None:
            self.parent_category_id = m.get('ParentCategoryId')
        return self


class CreateCategoryResponseBodyCategory(TeaModel):
    def __init__(
        self,
        category_id: int = None,
        name: str = None,
        parent_category_id: int = None,
        status: int = None,
    ):
        # 类目ID
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
        # 类目信息
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
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.conn_question_id = conn_question_id
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
        # 关联关系ID
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
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        # 实体名称，仅支持中文、大小写字母、数字、下划线
        self.entity_name = entity_name
        # 实体类型：详见:,EntityTypeEnum[synonyms(同义词),regex(正则)]
        self.entity_type = entity_type
        # 机器人ID
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
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.content = content
        # 实体ID，修改实体成员时可为空
        self.entity_id = entity_id
        # 机器人ID
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
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.content = content
        # 实体ID，修改实体成员时可为空
        self.entity_id = entity_id
        # 机器人ID
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
            temp_model = CreateDSEntityValueResponseBody()
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
        title: str = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        # 知识的类目ID
        self.category_id = category_id
        # 失效时间
        self.end_date = end_date
        # 默认答案内容
        self.solution_content = solution_content
        # 默认答案类型
        self.solution_type = solution_type
        # 生效时间
        self.start_date = start_date
        # 知识标题
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
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class CreateFaqResponseBody(TeaModel):
    def __init__(
        self,
        knowledge_id: int = None,
        request_id: str = None,
    ):
        # 知识ID
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
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        # 机器人备注，不超过50字
        self.introduction = introduction
        # 机器人服务的语言，如zh-cn、en-us，参考 http://www.lingoes.net/zh/translator/langcode.htm   入参全小写，当前只支持 zh-cn、en-us
        self.language_code = language_code
        # 机器人名称，不超过50字
        self.name = name
        # 机器人类型
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
        # 机器人唯一标识
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


class CreateInstancePublishTaskRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        instance_id: str = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        # 机器人唯一标识
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
        # 业务类型列表
        self.biz_type_list = biz_type_list
        # 任务创建的 UTC 时间
        self.create_time = create_time
        # job失败信息
        self.error = error
        # 任务Id
        self.id = id
        # 任务修改的 UTC 时间
        self.modify_time = modify_time
        # 请求Id
        self.request_id = request_id
        # 任务Id
        self.response = response
        # 任务状态
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
        # 是否数组
        self.array = array
        # 是否脱敏
        self.encrypt = encrypt
        # 是否交互式
        self.interactive = interactive
        # 槽位名
        self.name = name
        self.slot_id = slot_id
        # 关联的实体名
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
        # 意图别名
        self.alias_name = alias_name
        # 意图名称
        self.intent_name = intent_name
        # 槽位信息
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
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        # 机器人ID
        self.instance_id = instance_id
        # 意图定义结构体
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
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        # 机器人ID
        self.instance_id = instance_id
        # 意图定义结构体
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
            temp_model = CreateIntentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLgfRequestLgfDefinition(TeaModel):
    def __init__(
        self,
        intent_id: int = None,
        rule_text: str = None,
    ):
        # 意图ID
        self.intent_id = intent_id
        # LGF配置
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
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        # 机器人ID
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
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        # 机器人ID
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
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        # 视角描述
        self.description = description
        # 视角名称，长度不超过50字
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
        # 视角主键（code_id）
        self.perspective_id = perspective_id
        # 请求Id
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
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        # 发布单元类型，机器人发布请使用 CreateInstancePublishTask API
        self.biz_type = biz_type
        # 附加发布信息，当前支持：如果BizType是faq，此字段填写类目Id，表示只发布这些类目下面的知识
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
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        # 发布单元类型，机器人发布请使用 CreateInstancePublishTask API
        self.biz_type = biz_type
        # 附加发布信息，当前支持：如果BizType是faq，此字段填写类目Id，表示只发布这些类目下面的知识
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
        # 业务类型列表
        self.biz_type_list = biz_type_list
        # 任务创建的 UTC 时间
        self.create_time = create_time
        # job失败信息
        self.error = error
        # 任务Id
        self.id = id
        # 任务修改的 UTC 时间
        self.modify_time = modify_time
        # 请求Id
        self.request_id = request_id
        # 任务Id
        self.response = response
        # 任务状态
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
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        # 知识ID
        self.knowledge_id = knowledge_id
        # 相似问标题，字数上限-120
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
        # 相似问ID
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
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        # 答案内容
        self.content = content
        # 答案类型
        self.content_type = content_type
        # 知识ID
        self.knowledge_id = knowledge_id
        # 视角code列表
        self.perspective_codes = perspective_codes

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
        return self


class CreateSolutionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        solution_id: int = None,
    ):
        self.request_id = request_id
        # 答案ID
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
            temp_model = CreateSolutionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUserSayRequestUserSayDefinitionSlotInfos(TeaModel):
    def __init__(
        self,
        end_index: int = None,
        slot_id: str = None,
        start_index: int = None,
    ):
        # 槽位在意图话术中的结束下标（不含）
        self.end_index = end_index
        # 划槽ID
        self.slot_id = slot_id
        # 槽位在意图话术中的起始下标
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
        # 用户话术
        self.content = content
        # 意图ID
        self.intent_id = intent_id
        # 划槽信息
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
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        # 机器人ID
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
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        # 机器人ID
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
            temp_model = CreateUserSayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCategoryRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        category_id: int = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        # 类目ID
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
            temp_model = DeleteCategoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteConnQuestionRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        outline_id: int = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
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
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        # 实体ID
        self.entity_id = entity_id
        # 机器人ID
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
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        # 实体ID
        self.entity_id = entity_id
        # 实体成员ID
        self.entity_value_id = entity_value_id
        # 机器人ID
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
            temp_model = DeleteDSEntityValueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFaqRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        knowledge_id: int = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        # 知识ID，创建知识该值为空
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
            temp_model = DeleteFaqResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteInstanceRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        instance_id: str = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        # 机器人ID
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
        # 业务类型列表
        self.biz_type_list = biz_type_list
        # 任务创建的 UTC 时间
        self.create_time = create_time
        # 任务创建人Id
        self.create_user_id = create_user_id
        # 任务创建人
        self.create_user_name = create_user_name
        # 错误信息
        self.error = error
        # 任务id
        self.id = id
        # 请求Id
        self.request_id = request_id
        # 任务id
        self.response = response
        # 任务状态，可以在GetInstancePublishTaskState API 了解更多的状态
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


class DeleteIntentRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        instance_id: str = None,
        intent_id: int = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        # 机器人ID
        self.instance_id = instance_id
        # 意图ID
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
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        # 机器人ID
        self.instance_id = instance_id
        self.intent_id = intent_id
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
            temp_model = DeleteLgfResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePerspectiveRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        perspective_id: str = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        # 视角主键（code_id）
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
        # 请求Id
        self.request_id = request_id
        # 删除视角的结果
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
            temp_model = DeletePerspectiveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSimQuestionRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        sim_question_id: int = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        # 相似问ID
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
            temp_model = DeleteSimQuestionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSolutionRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        solution_id: int = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        # 答案ID
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
            temp_model = DeleteSolutionResponseBody()
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
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.instance_id = instance_id
        self.intent_id = intent_id
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
            temp_model = DeleteUserSayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCategoryRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        category_id: int = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        # 类目ID
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
        category_id: int = None,
        name: str = None,
        parent_category_id: int = None,
        status: int = None,
    ):
        # 类目ID
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
        # 类目信息
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
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        # 实体ID
        self.entity_id = entity_id
        # 机器人ID
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
        # 实体ID
        self.entity_id = entity_id
        # 实体名称，仅支持中文、大小写字母、数字、下划线
        self.entity_name = entity_name
        # 实体类型：详见:,EntityTypeEnum[synonyms(同义词),regex(正则)]
        self.entity_type = entity_type
        self.modify_time = modify_time
        self.modify_user_id = modify_user_id
        self.modify_user_name = modify_user_name
        self.request_id = request_id
        # 系统实体code，如@sys.date
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
            temp_model = DescribeDSEntityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFaqRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        knowledge_id: int = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        # 知识ID
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
        # 关联知识ID
        self.conn_question_id = conn_question_id
        # 创建时间(UTC 时间)
        self.create_time = create_time
        # 修改时间(UTC 时间)
        self.modify_time = modify_time
        # 关联关系ID
        self.outline_id = outline_id
        # 关联知识标题
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
        # 创建时间(UTC 时间)
        self.create_time = create_time
        # 修改时间(UTC 时间)
        self.modify_time = modify_time
        # 相似问ID
        self.sim_question_id = sim_question_id
        # 相似问标题
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
    ):
        # 答案内容
        self.content = content
        # 答案类型(0纯文本，1富文本）
        self.content_type = content_type
        # 创建时间(UTC 时间)
        self.create_time = create_time
        # 修改时间(UTC 时间)
        self.modify_time = modify_time
        # 视角code列表
        self.perspective_codes = perspective_codes
        # 答案纯文本内容
        self.plain_text = plain_text
        # 答案ID
        self.solution_id = solution_id

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
        title: str = None,
    ):
        # 类目ID
        self.category_id = category_id
        # 创建时间（UTC时间）
        self.create_time = create_time
        # 创建人
        self.create_user_name = create_user_name
        # 知识生效状态,根据StartDate, EndDate计算出来: 20-生效中, 21-已失效, 22-待生效
        self.effect_status = effect_status
        # 失效时间（UTC时间）
        self.end_date = end_date
        # 知识ID
        self.knowledge_id = knowledge_id
        # 修改时间（UTC时间）
        self.modify_time = modify_time
        # 修改人
        self.modify_user_name = modify_user_name
        # 关联问列表
        self.outlines = outlines
        self.request_id = request_id
        # 相似问列表
        self.sim_questions = sim_questions
        # 答案列表
        self.solutions = solutions
        # 生效时间（UTC时间）
        self.start_date = start_date
        # 知识状态: -1-已删除未发布, 1-未发布, 2-已发布, 3-已更新未发布
        self.status = status
        # 标题
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
            temp_model = DescribeFaqResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        instance_id: str = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        # 机器人ID
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
        category_id: int = None,
        name: str = None,
        parent_category_id: int = None,
    ):
        # 类目id
        self.category_id = category_id
        # 类目名称
        self.name = name
        # 父类目id，-1表示根目录
        self.parent_category_id = parent_category_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.name is not None:
            result['Name'] = self.name
        if self.parent_category_id is not None:
            result['ParentCategoryId'] = self.parent_category_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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
        # 机器人头像的URL
        self.avatar = avatar
        # 类目列表
        self.categories = categories
        # 机器人创建的 UTC 时间
        self.create_time = create_time
        # 机器人状态： EDITING(编辑中)、 PUBLISHED(已发布)
        self.edit_status = edit_status
        # 机器人唯一标识
        self.instance_id = instance_id
        # 机器人备注
        self.introduction = introduction
        # 机器人服务的语言，如zh-cn、en-us
        self.language_code = language_code
        # 机器人名称
        self.name = name
        # 请求Id
        self.request_id = request_id
        # 机器人类型
        self.robot_type = robot_type
        # 机器人的时区，参考《公共-时区码》
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


class DescribeIntentRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        instance_id: str = None,
        intent_id: int = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        # 机器人ID
        self.instance_id = instance_id
        # 意图ID
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
            temp_model = DescribeIntentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePerspectiveRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        perspective_id: str = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        # 视角Id
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
        # 创建时间 UTC时间
        self.create_time = create_time
        # 修改时间 UTC时间
        self.modify_time = modify_time
        # 视角名称
        self.name = name
        # 视角编码（用于问答api）
        self.perspective_code = perspective_code
        # 视角主键（code_id）
        self.perspective_id = perspective_id
        # 请求Id
        self.request_id = request_id
        # 是否自定义
        self.self_define = self_define
        # 数据状态：3：选中；1：未选中
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
            temp_model = DescribePerspectiveResponseBody()
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
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        # good-点赞、bad-点踩
        self.feedback = feedback
        # 点赞、点踩的内容
        self.feedback_content = feedback_content
        # 机器人ID
        self.instance_id = instance_id
        # 会话窗单次会话标识
        self.message_id = message_id
        # 会话Session标识，标识：IM唯一标识会话
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
        # good-点赞、bad-点踩
        self.feedback = feedback
        # 会话窗单次会话标识
        self.message_id = message_id
        # 请求id
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
            temp_model = FeedbackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAsyncResultRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        task_id: str = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        # 从Chat接口返回参数中获取TASK_ID
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
            temp_model = GetAsyncResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstancePublishTaskStateRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        id: int = None,
        instance_id: str = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        # 任务ID
        self.id = id
        # 机器人ID
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
        # 业务类型列表
        self.biz_type_list = biz_type_list
        # 任务创建的 UTC 时间
        self.create_time = create_time
        # job失败信息
        self.error = error
        # 各子发布模块的错误信息，key是子发布模块，value是错误信息
        self.errors = errors
        # 任务Id
        self.id = id
        # 任务修改的 UTC 时间
        self.modify_time = modify_time
        # 请求Id
        self.request_id = request_id
        # 任务Id
        self.response = response
        # 任务状态
        self.status = status
        # 各子发布模块的警告信息，key是子发布模块，value是警告信息
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
            temp_model = GetInstancePublishTaskStateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPublishTaskStateRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        id: int = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        # 任务ID
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
        # 业务类型列表
        self.biz_type_list = biz_type_list
        # 任务创建的 UTC 时间
        self.create_time = create_time
        # job失败信息
        self.error = error
        # 各子发布模块的错误信息，key是子发布模块，value是错误信息
        self.errors = errors
        # 任务Id
        self.id = id
        # 任务修改的 UTC 时间
        self.modify_time = modify_time
        # 请求Id
        self.request_id = request_id
        # 任务Id
        self.response = response
        # 任务状态
        self.status = status
        # 各子发布模块的警告信息，key是子发布模块，value是警告信息
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
            temp_model = GetPublishTaskStateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LinkInstanceCategoryRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        category_ids: str = None,
        instance_id: str = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        # 知识类目Id
        self.category_ids = category_ids
        # 机器人唯一标识
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
        if self.category_ids is not None:
            result['CategoryIds'] = self.category_ids
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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
        # 请求Id
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
            temp_model = LinkInstanceCategoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAgentRequest(TeaModel):
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


class ListAgentResponseBodyData(TeaModel):
    def __init__(
        self,
        agent_id: int = None,
        agent_key: str = None,
        agent_name: str = None,
    ):
        self.agent_id = agent_id
        self.agent_key = agent_key
        self.agent_name = agent_name

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')
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
            temp_model = ListAgentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCategoryRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        parent_category_id: int = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        # 父类目ID
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
        if self.parent_category_id is not None:
            result['ParentCategoryId'] = self.parent_category_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('ParentCategoryId') is not None:
            self.parent_category_id = m.get('ParentCategoryId')
        return self


class ListCategoryResponseBodyCategories(TeaModel):
    def __init__(
        self,
        category_id: int = None,
        name: str = None,
        parent_category_id: int = None,
        status: int = None,
    ):
        # 类目ID
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
        # list结果
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
            temp_model = ListCategoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListConnQuestionRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        knowledge_id: int = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
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
        # 关联知识ID
        self.conn_question_id = conn_question_id
        # 创建时间(UTC 时间)
        self.create_time = create_time
        # 修改时间(UTC 时间)
        self.modify_time = modify_time
        # 关联关系ID
        self.outline_id = outline_id
        # 关联知识题目
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
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        # 为空：全量自定义实体（默认）
        self.entity_type = entity_type
        # 机器人ID
        self.instance_id = instance_id
        # 筛选项，contains匹配，范围：实体名称（未来扩展：实体成员、同义词）
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
        # 系统实体code，如@sys.date
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
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        # 实体ID
        self.entity_id = entity_id
        # 实体成员ID
        self.entity_value_id = entity_value_id
        # 机器人ID
        self.instance_id = instance_id
        # 实体成员名称搜索关键词
        self.keyword = keyword
        # 页码
        self.page_number = page_number
        # 分页大小
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
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        # 按机器人名称模糊搜索
        self.name = name
        # 分页-第几页，默认1
        self.page_number = page_number
        # 分页-页面大小，默认10
        self.page_size = page_size
        # 按机器人类型筛选
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
        # 机器人头像的URL
        self.avatar = avatar
        # 机器人创建的 UTC 时间
        self.create_time = create_time
        # 机器人唯一标识
        self.instance_id = instance_id
        # 机器人备注
        self.introduction = introduction
        # 机器人服务的语言
        self.language_code = language_code
        # 机器人名称
        self.name = name
        # 机器人类型
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
        # 机器人列表信息
        self.instances = instances
        # 分页-第几页
        self.page_number = page_number
        # 分页-页面大小
        self.page_size = page_size
        # 请求Id
        self.request_id = request_id
        # 总条数
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
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        # 机器人ID
        self.instance_id = instance_id
        # 意图名称
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
        # 是否数组
        self.array = array
        # 是否敏感
        self.encrypt = encrypt
        # 是否交互式收集
        self.interactive = interactive
        # 槽位名
        self.name = name
        # 槽位ID
        self.slot_id = slot_id
        # 槽位值（实体名）
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
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        # 机器人ID
        self.instance_id = instance_id
        # 意图ID
        self.intent_id = intent_id
        # 筛选语义配置内容
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
        # 创建时间
        self.create_time = create_time
        # 意图ID
        self.intent_id = intent_id
        # LGF ID
        self.lgf_id = lgf_id
        # 修改时间
        self.modify_time = modify_time
        # LGF规则
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
            temp_model = ListLgfResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSimQuestionRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        knowledge_id: int = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        # 知识ID
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
        # 创建时间(UTC 时间)
        self.create_time = create_time
        # 修改时间(UTC 时间)
        self.modify_time = modify_time
        # 相似问ID
        self.sim_question_id = sim_question_id
        # 相似问标题
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
        # 相似问列表
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
            temp_model = ListSimQuestionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSolutionRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        knowledge_id: int = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        # 知识ID
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
    ):
        # 答案内容
        self.content = content
        # 答案类型(0纯文本，1富文本）
        self.content_type = content_type
        # 创建时间(UTC 时间)
        self.create_time = create_time
        # 修改时间(UTC 时间)
        self.modify_time = modify_time
        # 视角code列表
        self.perspective_codes = perspective_codes
        # 答案纯文本内容
        self.plain_text = plain_text
        # 答案ID
        self.solution_id = solution_id

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
        return self


class ListSolutionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        solutions: List[ListSolutionResponseBodySolutions] = None,
    ):
        self.request_id = request_id
        # 答案列表
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
            temp_model = ListSolutionResponseBody()
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
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        # 筛选用户话术
        self.content = content
        # 机器人ID
        self.instance_id = instance_id
        # 意图ID
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
        # 槽位在意图话术中的下标
        self.end_index = end_index
        # 意图槽位ID
        self.slot_id = slot_id
        # 槽位在意图话术中的下标
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
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        # 机器人ID
        self.instance_id = instance_id
        # 用户表述
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
        # 名词
        self.standard_word = standard_word
        # 同义词
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
        # 名词
        self.standard_word = standard_word
        # 同义词
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
        # 全局名词列表
        self.global_dict_list = global_dict_list
        # 全局敏感词列表
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
        # 实体名称
        self.name = name
        # 实体原词（实体成员）
        self.origin = origin
        # 实体类型，当前只有text类型
        self.type = type
        # 实体同义词
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
        # 实体名称
        self.name = name
        # 实体原词（实体成员）
        self.origin = origin
        # 实体类型，当前只有text类型
        self.type = type
        # 实体同义词
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
        # 意图id
        self.intent_id = intent_id
        # 匹配详情（匹配过程）
        self.match_detail = match_detail
        # 匹配类型，其枚举值含义如下：  Similarity：query与意图通过意图话术相似度匹配 Lgf：query与意图通过LGF匹配 Classify：query与意图通过模型训练匹配 FewShotLearning：query与意图通过系统内置fewshot模型匹配 BuildIn： query与系统内置意图匹配
        self.match_type = match_type
        # 意图名称
        self.name = name
        # 分数
        self.score = score
        # 命中意图的槽位列表
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
        # 实体列表
        self.entity_list = entity_list
        # 意图列表
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
        # 对话中控的nlu信息
        self.dialog_hub_nlu_info = dialog_hub_nlu_info
        # 对话工厂的nlu信息
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
        # 本条语言理解应答消息的ID
        self.message_id = message_id
        # 消息的列表
        self.messages = messages
        # 请求id
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
            temp_model = NluResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPerspectivesRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
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
        # 创建时间 UTC时间
        self.create_time = create_time
        # 修改时间 UTC时间
        self.modify_time = modify_time
        # 视角名称
        self.name = name
        # 视角编码（用于问答api）
        self.perspective_code = perspective_code
        # 视角主键（code_id）
        self.perspective_id = perspective_id
        # 是否自定义
        self.self_define = self_define
        # 数据状态：3：选中；1：未选中
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
        # 视角列表
        self.perspectives = perspectives
        # 请求Id
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
            temp_model = QueryPerspectivesResponseBody()
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
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        # 类目唯一标识
        self.category_ids = category_ids
        # 创建开始时间
        self.create_time_begin = create_time_begin
        # 创建结束时间
        self.create_time_end = create_time_end
        # 创建人
        self.create_user_name = create_user_name
        # 失效开始时间
        self.end_time_begin = end_time_begin
        # 失效结束时间
        self.end_time_end = end_time_end
        # 关键字
        self.keyword = keyword
        # 修改开始时间
        self.modify_time_begin = modify_time_begin
        # 修改结束时间
        self.modify_time_end = modify_time_end
        # 修改人
        self.modify_user_name = modify_user_name
        # 页码 默认1
        self.page_number = page_number
        # 每页数量，默认10，最大50
        self.page_size = page_size
        # 搜索范围： 1-搜索标题相似问, 2-搜索答案, 3-搜索全部
        self.search_scope = search_scope
        # 生效开始时间
        self.start_time_begin = start_time_begin
        # 生效结束时间
        self.start_time_end = start_time_end
        # 知识状态: -1-已删除未发布, 1-未发布, 2-已发布, 3-已更新未发布
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
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        # 类目唯一标识
        self.category_ids_shrink = category_ids_shrink
        # 创建开始时间
        self.create_time_begin = create_time_begin
        # 创建结束时间
        self.create_time_end = create_time_end
        # 创建人
        self.create_user_name = create_user_name
        # 失效开始时间
        self.end_time_begin = end_time_begin
        # 失效结束时间
        self.end_time_end = end_time_end
        # 关键字
        self.keyword = keyword
        # 修改开始时间
        self.modify_time_begin = modify_time_begin
        # 修改结束时间
        self.modify_time_end = modify_time_end
        # 修改人
        self.modify_user_name = modify_user_name
        # 页码 默认1
        self.page_number = page_number
        # 每页数量，默认10，最大50
        self.page_size = page_size
        # 搜索范围： 1-搜索标题相似问, 2-搜索答案, 3-搜索全部
        self.search_scope = search_scope
        # 生效开始时间
        self.start_time_begin = start_time_begin
        # 生效结束时间
        self.start_time_end = start_time_end
        # 知识状态: -1-已删除未发布, 1-未发布, 2-已发布, 3-已更新未发布
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
        # 类目ID
        self.category_id = category_id
        # 创建时间（UTC时间）
        self.create_time = create_time
        # 创建人ID
        self.create_user_id = create_user_id
        # 创建人
        self.create_user_name = create_user_name
        # 知识生效状态,根据StartDate, EndDate计算出来: 20-生效中, 21-已失效, 22-待生效
        self.effect_status = effect_status
        # 命中的相似问
        self.hit_similar_titles = hit_similar_titles
        # 命中的答案
        self.hit_solutions = hit_solutions
        # 知识ID
        self.knowledge_id = knowledge_id
        # 修改时间（UTC时间）
        self.modify_time = modify_time
        # 修改人ID
        self.modify_user_id = modify_user_id
        # 修改人
        self.modify_user_name = modify_user_name
        # 知识状态: -1-已删除未发布, 1-未发布, 2-已发布, 3-已更新未发布
        self.status = status
        # 标题
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
        # 页码 默认1
        self.page_number = page_number
        # 每页数量，默认10，最大500
        self.page_size = page_size
        self.request_id = request_id
        # 总条数
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
            temp_model = SearchFaqResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCategoryRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        category_id: int = None,
        name: str = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        # 类目ID
        self.category_id = category_id
        # 类目名称
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
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
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
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.conn_question_id = conn_question_id
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
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        # 实体ID
        self.entity_id = entity_id
        # 实体名称，仅支持中文、大小写字母、数字、下划线
        self.entity_name = entity_name
        # 实体类型：详见:,EntityTypeEnum[synonyms(同义词),regex(正则)]
        self.entity_type = entity_type
        # 机器人ID
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
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        # 实体类型为synonyms时，表示实体归一化值；当实体类型为regex时，表示正则表达式文本
        self.content = content
        # 实体ID，修改实体成员时可为空
        self.entity_id = entity_id
        # 实体成员ID，创建实体成员时为空
        self.entity_value_id = entity_value_id
        # 机器人ID
        self.instance_id = instance_id
        # 实体同义词
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
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        # 实体类型为synonyms时，表示实体归一化值；当实体类型为regex时，表示正则表达式文本
        self.content = content
        # 实体ID，修改实体成员时可为空
        self.entity_id = entity_id
        # 实体成员ID，创建实体成员时为空
        self.entity_value_id = entity_value_id
        # 机器人ID
        self.instance_id = instance_id
        # 实体同义词
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
            temp_model = UpdateDSEntityValueResponseBody()
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
        title: str = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        # 知识的类目ID
        self.category_id = category_id
        # 失效时间
        self.end_date = end_date
        # 知识ID
        self.knowledge_id = knowledge_id
        # 生效时间
        self.start_date = start_date
        # 知识标题
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
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        # 机器人ID
        self.instance_id = instance_id
        # 要修改的机器人备注
        self.introduction = introduction
        # 要修改的机器人名称
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
        # Id of the request
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
        # 是否数组
        self.array = array
        # 是否脱敏
        self.encrypt = encrypt
        # 是否交互式
        self.interactive = interactive
        # 槽位名
        self.name = name
        self.slot_id = slot_id
        # 关联的实体名
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
        # 意图别名
        self.alias_name = alias_name
        # 意图名称
        self.intent_name = intent_name
        # 槽位信息
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
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        # 机器人ID
        self.instance_id = instance_id
        # 意图定义结构体
        self.intent_definition = intent_definition
        # 意图ID
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
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        # 机器人ID
        self.instance_id = instance_id
        # 意图定义结构体
        self.intent_definition_shrink = intent_definition_shrink
        # 意图ID
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
            temp_model = UpdateIntentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateLgfRequestLgfDefinition(TeaModel):
    def __init__(
        self,
        intent_id: int = None,
        rule_text: str = None,
    ):
        # 意图ID
        self.intent_id = intent_id
        # LGF配置
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
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        # 机器人ID
        self.instance_id = instance_id
        self.lgf_definition = lgf_definition
        # LGF ID
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
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        # 机器人ID
        self.instance_id = instance_id
        self.lgf_definition_shrink = lgf_definition_shrink
        # LGF ID
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
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        # 视角名称
        self.name = name
        # 视角主键（code_id）
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
        # 请求Id
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
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        # 相似问ID
        self.sim_question_id = sim_question_id
        # 相似问标题，字数上限-120
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
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        # 答案内容
        self.content = content
        # 答案类型
        self.content_type = content_type
        # 视角code列表
        self.perspective_codes = perspective_codes
        # 答案ID
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
        if self.content is not None:
            result['Content'] = self.content
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.perspective_codes is not None:
            result['PerspectiveCodes'] = self.perspective_codes
        if self.solution_id is not None:
            result['SolutionId'] = self.solution_id
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
            temp_model = UpdateSolutionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateUserSayRequestUserSayDefinitionSlotInfos(TeaModel):
    def __init__(
        self,
        end_index: int = None,
        slot_id: str = None,
        start_index: int = None,
    ):
        # 槽位在意图话术中的结束下标（不含）
        self.end_index = end_index
        # 划槽ID
        self.slot_id = slot_id
        # 槽位在意图话术中的起始下标
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
        # 用户话术
        self.content = content
        # 意图ID
        self.intent_id = intent_id
        # 划槽信息
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
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        # 机器人ID
        self.instance_id = instance_id
        self.user_say_definition = user_say_definition
        # 用户话术ID
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
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        # 机器人ID
        self.instance_id = instance_id
        self.user_say_definition_shrink = user_say_definition_shrink
        # 用户话术ID
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
            temp_model = UpdateUserSayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


