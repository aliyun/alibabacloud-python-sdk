# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


class BeeBotAssociateRequest(TeaModel):
    def __init__(
        self,
        chat_bot_instance_id: str = None,
        cust_space_id: str = None,
        isv_code: str = None,
        perspective: List[str] = None,
        recommend_num: int = None,
        session_id: str = None,
        utterance: str = None,
    ):
        # The ID of a bot instance.
        self.chat_bot_instance_id = chat_bot_instance_id
        self.cust_space_id = cust_space_id
        # The ISV verification code, which is used to verify whether the user is authorized by ISV.
        self.isv_code = isv_code
        # The list of codes for answers from different perspectives.
        self.perspective = perspective
        # The number of recommended questions. The value ranges from 1 to 10.
        self.recommend_num = recommend_num
        # The ID of the session, which is used to identify the session and store context information in the session.
        self.session_id = session_id
        # The input of the visitor.
        self.utterance = utterance

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chat_bot_instance_id is not None:
            result['ChatBotInstanceId'] = self.chat_bot_instance_id
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.isv_code is not None:
            result['IsvCode'] = self.isv_code
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
        if m.get('ChatBotInstanceId') is not None:
            self.chat_bot_instance_id = m.get('ChatBotInstanceId')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('IsvCode') is not None:
            self.isv_code = m.get('IsvCode')
        if m.get('Perspective') is not None:
            self.perspective = m.get('Perspective')
        if m.get('RecommendNum') is not None:
            self.recommend_num = m.get('RecommendNum')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('Utterance') is not None:
            self.utterance = m.get('Utterance')
        return self


class BeeBotAssociateShrinkRequest(TeaModel):
    def __init__(
        self,
        chat_bot_instance_id: str = None,
        cust_space_id: str = None,
        isv_code: str = None,
        perspective_shrink: str = None,
        recommend_num: int = None,
        session_id: str = None,
        utterance: str = None,
    ):
        # The ID of a bot instance.
        self.chat_bot_instance_id = chat_bot_instance_id
        self.cust_space_id = cust_space_id
        # The ISV verification code, which is used to verify whether the user is authorized by ISV.
        self.isv_code = isv_code
        # The list of codes for answers from different perspectives.
        self.perspective_shrink = perspective_shrink
        # The number of recommended questions. The value ranges from 1 to 10.
        self.recommend_num = recommend_num
        # The ID of the session, which is used to identify the session and store context information in the session.
        self.session_id = session_id
        # The input of the visitor.
        self.utterance = utterance

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chat_bot_instance_id is not None:
            result['ChatBotInstanceId'] = self.chat_bot_instance_id
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.isv_code is not None:
            result['IsvCode'] = self.isv_code
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
        if m.get('ChatBotInstanceId') is not None:
            self.chat_bot_instance_id = m.get('ChatBotInstanceId')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('IsvCode') is not None:
            self.isv_code = m.get('IsvCode')
        if m.get('Perspective') is not None:
            self.perspective_shrink = m.get('Perspective')
        if m.get('RecommendNum') is not None:
            self.recommend_num = m.get('RecommendNum')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('Utterance') is not None:
            self.utterance = m.get('Utterance')
        return self


class BeeBotAssociateResponseBodyDataAssociate(TeaModel):
    def __init__(
        self,
        meta: str = None,
        title: str = None,
    ):
        # The additional information.
        self.meta = meta
        # The title of the associated question.
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


class BeeBotAssociateResponseBodyData(TeaModel):
    def __init__(
        self,
        associate: List[BeeBotAssociateResponseBodyDataAssociate] = None,
        message_id: str = None,
        session_id: str = None,
    ):
        # The list of associated recommendations.
        self.associate = associate
        # The ID of the response message.
        self.message_id = message_id
        # The ID of the session.
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
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.associate = []
        if m.get('Associate') is not None:
            for k in m.get('Associate'):
                temp_model = BeeBotAssociateResponseBodyDataAssociate()
                self.associate.append(temp_model.from_map(k))
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class BeeBotAssociateResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: BeeBotAssociateResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # If OK is returned, the request is successful.
        self.code = code
        # The data returned.
        self.data = data
        # The error message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

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
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = BeeBotAssociateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BeeBotAssociateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BeeBotAssociateResponseBody = None,
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
            temp_model = BeeBotAssociateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BeeBotChatRequest(TeaModel):
    def __init__(
        self,
        chat_bot_instance_id: str = None,
        cust_space_id: str = None,
        intent_name: str = None,
        isv_code: str = None,
        knowledge_id: str = None,
        perspective: List[str] = None,
        sender_id: str = None,
        sender_nick: str = None,
        session_id: str = None,
        utterance: str = None,
        vendor_param: Dict[str, Any] = None,
    ):
        # The ID of the bot instance.
        self.chat_bot_instance_id = chat_bot_instance_id
        self.cust_space_id = cust_space_id
        # The name of the intent in the dialog flow. When this parameter is specified, the bot conducts a Q\&A based on the intent.
        self.intent_name = intent_name
        # The ISV verification code, which is used to verify whether the user is authorized by the ISV account.
        self.isv_code = isv_code
        # The ID of the knowledge title in the knowledge base.
        self.knowledge_id = knowledge_id
        # The list of codes for answers from different perspectives.
        self.perspective = perspective
        # The ID of the visitor, which is used to identify users in the current session.
        self.sender_id = sender_id
        # The nickname of the visitor in the current session.
        self.sender_nick = sender_nick
        # The ID of the session, which is used to identify the session and store context information of the session.
        self.session_id = session_id
        # The input of the visitor.
        self.utterance = utterance
        # The user-defined parameter set in JSON format. You can specify user-defined parameters for conversation engines.
        self.vendor_param = vendor_param

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chat_bot_instance_id is not None:
            result['ChatBotInstanceId'] = self.chat_bot_instance_id
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.intent_name is not None:
            result['IntentName'] = self.intent_name
        if self.isv_code is not None:
            result['IsvCode'] = self.isv_code
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
        if m.get('ChatBotInstanceId') is not None:
            self.chat_bot_instance_id = m.get('ChatBotInstanceId')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('IntentName') is not None:
            self.intent_name = m.get('IntentName')
        if m.get('IsvCode') is not None:
            self.isv_code = m.get('IsvCode')
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


class BeeBotChatShrinkRequest(TeaModel):
    def __init__(
        self,
        chat_bot_instance_id: str = None,
        cust_space_id: str = None,
        intent_name: str = None,
        isv_code: str = None,
        knowledge_id: str = None,
        perspective_shrink: str = None,
        sender_id: str = None,
        sender_nick: str = None,
        session_id: str = None,
        utterance: str = None,
        vendor_param_shrink: str = None,
    ):
        # The ID of the bot instance.
        self.chat_bot_instance_id = chat_bot_instance_id
        self.cust_space_id = cust_space_id
        # The name of the intent in the dialog flow. When this parameter is specified, the bot conducts a Q\&A based on the intent.
        self.intent_name = intent_name
        # The ISV verification code, which is used to verify whether the user is authorized by the ISV account.
        self.isv_code = isv_code
        # The ID of the knowledge title in the knowledge base.
        self.knowledge_id = knowledge_id
        # The list of codes for answers from different perspectives.
        self.perspective_shrink = perspective_shrink
        # The ID of the visitor, which is used to identify users in the current session.
        self.sender_id = sender_id
        # The nickname of the visitor in the current session.
        self.sender_nick = sender_nick
        # The ID of the session, which is used to identify the session and store context information of the session.
        self.session_id = session_id
        # The input of the visitor.
        self.utterance = utterance
        # The user-defined parameter set in JSON format. You can specify user-defined parameters for conversation engines.
        self.vendor_param_shrink = vendor_param_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chat_bot_instance_id is not None:
            result['ChatBotInstanceId'] = self.chat_bot_instance_id
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.intent_name is not None:
            result['IntentName'] = self.intent_name
        if self.isv_code is not None:
            result['IsvCode'] = self.isv_code
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
        if self.vendor_param_shrink is not None:
            result['VendorParam'] = self.vendor_param_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChatBotInstanceId') is not None:
            self.chat_bot_instance_id = m.get('ChatBotInstanceId')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('IntentName') is not None:
            self.intent_name = m.get('IntentName')
        if m.get('IsvCode') is not None:
            self.isv_code = m.get('IsvCode')
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
            self.vendor_param_shrink = m.get('VendorParam')
        return self


class BeeBotChatResponseBodyDataMessagesKnowledgeRelatedKnowledges(TeaModel):
    def __init__(
        self,
        knowledge_id: str = None,
        title: str = None,
    ):
        # The ID of the related knowledge.
        self.knowledge_id = knowledge_id
        # The title of the related knowledge.
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


class BeeBotChatResponseBodyDataMessagesKnowledge(TeaModel):
    def __init__(
        self,
        answer_source: str = None,
        category: str = None,
        content: str = None,
        content_type: str = None,
        hit_statement: str = None,
        id: str = None,
        related_knowledges: List[BeeBotChatResponseBodyDataMessagesKnowledgeRelatedKnowledges] = None,
        summary: str = None,
        title: str = None,
    ):
        # The source of the answer.
        self.answer_source = answer_source
        # The category of the knowledge.
        self.category = category
        # The content of the hit question.
        self.content = content
        # Indicates whether the answer is in plain text or rich text.
        self.content_type = content_type
        # The hit text.
        self.hit_statement = hit_statement
        # The ID of the hit question in the knowledge base.
        self.id = id
        # The list of the related knowledge.
        self.related_knowledges = related_knowledges
        # The summary to the hit question.
        self.summary = summary
        # The title of the hit question.
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
                temp_model = BeeBotChatResponseBodyDataMessagesKnowledgeRelatedKnowledges()
                self.related_knowledges.append(temp_model.from_map(k))
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class BeeBotChatResponseBodyDataMessagesRecommends(TeaModel):
    def __init__(
        self,
        answer_source: str = None,
        knowledge_id: str = None,
        title: str = None,
    ):
        # The source of the recommended answer.
        self.answer_source = answer_source
        # The ID of the recommended knowledge.
        self.knowledge_id = knowledge_id
        # The title of the recommended knowledge. Valid values: the entity in graph-based question answering, the knowledge title in knowledge-based question answering, or the column value in table-based question answering.
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
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnswerSource') is not None:
            self.answer_source = m.get('AnswerSource')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class BeeBotChatResponseBodyDataMessagesTextSlots(TeaModel):
    def __init__(
        self,
        hit: bool = None,
        name: str = None,
        origin: str = None,
        value: str = None,
    ):
        # Indicates whether the slot is hit.
        self.hit = hit
        # The name.
        self.name = name
        # The original value.
        self.origin = origin
        # The specific value.
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


class BeeBotChatResponseBodyDataMessagesText(TeaModel):
    def __init__(
        self,
        answer_source: str = None,
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
        slots: List[BeeBotChatResponseBodyDataMessagesTextSlots] = None,
        user_defined_chat_title: str = None,
    ):
        # The source of the answer.
        self.answer_source = answer_source
        # The content of the text message.
        self.content = content
        # Indicates whether the answer is in plain text or rich text.
        self.content_type = content_type
        # The name of the dialog. When the AnswerSource parameter is set to BotFramework, the value of this parameter is returned.
        self.dialog_name = dialog_name
        # The passthrough parameters are returned.
        self.ext = ext
        # When the AnswerSource parameter is set to BotFramework, the value of this parameter is returned.
        self.external_flags = external_flags
        # The hit text.
        self.hit_statement = hit_statement
        # The name of the intent. When the AnswerSource parameter is set to BotFramework, the value of this parameter is returned.
        self.intent_name = intent_name
        # The metadata.
        self.meta_data = meta_data
        # The ID of the node. When the AnswerSource parameter is set to BotFramework, the value of this parameter is returned.
        self.node_id = node_id
        # The name of the node. When the AnswerSource parameter is set to BotFramework, the value of this parameter is returned.
        self.node_name = node_name
        # The list of slots.
        self.slots = slots
        # The title of the chitchat.
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
        self.slots = []
        if m.get('Slots') is not None:
            for k in m.get('Slots'):
                temp_model = BeeBotChatResponseBodyDataMessagesTextSlots()
                self.slots.append(temp_model.from_map(k))
        if m.get('UserDefinedChatTitle') is not None:
            self.user_defined_chat_title = m.get('UserDefinedChatTitle')
        return self


class BeeBotChatResponseBodyDataMessages(TeaModel):
    def __init__(
        self,
        answer_source: str = None,
        answer_type: str = None,
        knowledge: BeeBotChatResponseBodyDataMessagesKnowledge = None,
        recommends: List[BeeBotChatResponseBodyDataMessagesRecommends] = None,
        text: BeeBotChatResponseBodyDataMessagesText = None,
    ):
        # When the AnswerType parameter is set to Recommend, this parameter indicates the source of the recommended answer.
        self.answer_source = answer_source
        # The type of the answer.
        self.answer_type = answer_type
        # When the AnswerType parameter is set to Knowledge, this parameter contains the Knowledge object returned by the bot.
        self.knowledge = knowledge
        # The list of recommended knowledge. When the AnswerType parameter is set to Recommend, this parameter is returned.
        self.recommends = recommends
        # When the AnswerType parameter is set to Text, this parameter contains the Text object returned by the bot.
        self.text = text

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnswerSource') is not None:
            self.answer_source = m.get('AnswerSource')
        if m.get('AnswerType') is not None:
            self.answer_type = m.get('AnswerType')
        if m.get('Knowledge') is not None:
            temp_model = BeeBotChatResponseBodyDataMessagesKnowledge()
            self.knowledge = temp_model.from_map(m['Knowledge'])
        self.recommends = []
        if m.get('Recommends') is not None:
            for k in m.get('Recommends'):
                temp_model = BeeBotChatResponseBodyDataMessagesRecommends()
                self.recommends.append(temp_model.from_map(k))
        if m.get('Text') is not None:
            temp_model = BeeBotChatResponseBodyDataMessagesText()
            self.text = temp_model.from_map(m['Text'])
        return self


class BeeBotChatResponseBodyData(TeaModel):
    def __init__(
        self,
        message_id: str = None,
        messages: List[BeeBotChatResponseBodyDataMessages] = None,
        session_id: str = None,
    ):
        # The ID of the response message.
        self.message_id = message_id
        # The list of messages.
        self.messages = messages
        # The ID of the session.
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
                temp_model = BeeBotChatResponseBodyDataMessages()
                self.messages.append(temp_model.from_map(k))
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class BeeBotChatResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: BeeBotChatResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # If OK is returned, the request is successful.
        self.code = code
        # The data returned.
        self.data = data
        # The error message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

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
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = BeeBotChatResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BeeBotChatResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BeeBotChatResponseBody = None,
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
            temp_model = BeeBotChatResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChatappBindWabaRequest(TeaModel):
    def __init__(
        self,
        waba_id: str = None,
    ):
        # The ID of the WhatsApp Business account.
        self.waba_id = waba_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.waba_id is not None:
            result['WabaId'] = self.waba_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WabaId') is not None:
            self.waba_id = m.get('WabaId')
        return self


class ChatappBindWabaResponseBodyData(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        waba_id: str = None,
    ):
        # The space ID of the user.
        self.cust_space_id = cust_space_id
        # The ID of the WhatsApp Business account.
        self.waba_id = waba_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.waba_id is not None:
            result['WabaId'] = self.waba_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('WabaId') is not None:
            self.waba_id = m.get('WabaId')
        return self


class ChatappBindWabaResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ChatappBindWabaResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](~~196974~~).
        self.code = code
        # The data returned.
        self.data = data
        # The error message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

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
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ChatappBindWabaResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ChatappBindWabaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ChatappBindWabaResponseBody = None,
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
            temp_model = ChatappBindWabaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChatappEmbedSignUpRequest(TeaModel):
    def __init__(
        self,
        input_token: str = None,
    ):
        # The InputToken returned after the embedded signup flow is complete.
        self.input_token = input_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.input_token is not None:
            result['InputToken'] = self.input_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputToken') is not None:
            self.input_token = m.get('InputToken')
        return self


class ChatappEmbedSignUpResponseBodyWabas(TeaModel):
    def __init__(
        self,
        account_review_status: str = None,
        currency: str = None,
        id: str = None,
        message_template_namespace: str = None,
        name: str = None,
    ):
        # The review status of the WhatsApp Business account.
        self.account_review_status = account_review_status
        # The currency.
        self.currency = currency
        # The ID of the WhatsApp Business account.
        self.id = id
        # The namespace of the message template.
        self.message_template_namespace = message_template_namespace
        # The name of the WhatsApp Business account.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_review_status is not None:
            result['AccountReviewStatus'] = self.account_review_status
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.id is not None:
            result['Id'] = self.id
        if self.message_template_namespace is not None:
            result['MessageTemplateNamespace'] = self.message_template_namespace
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountReviewStatus') is not None:
            self.account_review_status = m.get('AccountReviewStatus')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MessageTemplateNamespace') is not None:
            self.message_template_namespace = m.get('MessageTemplateNamespace')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ChatappEmbedSignUpResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        wabas: List[ChatappEmbedSignUpResponseBodyWabas] = None,
    ):
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](~~196974~~).
        self.code = code
        # The error message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # The list of the WhatsApp Business accounts.
        self.wabas = wabas

    def validate(self):
        if self.wabas:
            for k in self.wabas:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Wabas'] = []
        if self.wabas is not None:
            for k in self.wabas:
                result['Wabas'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.wabas = []
        if m.get('Wabas') is not None:
            for k in m.get('Wabas'):
                temp_model = ChatappEmbedSignUpResponseBodyWabas()
                self.wabas.append(temp_model.from_map(k))
        return self


class ChatappEmbedSignUpResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ChatappEmbedSignUpResponseBody = None,
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
            temp_model = ChatappEmbedSignUpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChatappMigrationRegisterRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        phone_number: str = None,
    ):
        # The space ID of the user under the independent software vendor (ISV) account.
        self.cust_space_id = cust_space_id
        # The phone number.
        self.phone_number = phone_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        return self


class ChatappMigrationRegisterResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](~~196974~~).
        self.code = code
        # The error message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ChatappMigrationRegisterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ChatappMigrationRegisterResponseBody = None,
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
            temp_model = ChatappMigrationRegisterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChatappMigrationVerifiedRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        phone_number: str = None,
        verify_code: str = None,
    ):
        # The space ID of the user under the independent software vendor (ISV) account.
        self.cust_space_id = cust_space_id
        # The phone number.
        self.phone_number = phone_number
        # The verification code.
        self.verify_code = verify_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.verify_code is not None:
            result['VerifyCode'] = self.verify_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('VerifyCode') is not None:
            self.verify_code = m.get('VerifyCode')
        return self


class ChatappMigrationVerifiedResponseBodyData(TeaModel):
    def __init__(
        self,
        id: str = None,
        phone_number: str = None,
    ):
        # The ID of the phone number.
        self.id = id
        # The phone number.
        self.phone_number = phone_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        return self


class ChatappMigrationVerifiedResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ChatappMigrationVerifiedResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](~~196974~~).
        self.code = code
        # The data returned.
        self.data = data
        # The error message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

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
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ChatappMigrationVerifiedResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ChatappMigrationVerifiedResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ChatappMigrationVerifiedResponseBody = None,
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
            temp_model = ChatappMigrationVerifiedResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChatappPhoneNumberRegisterRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        phone_number: str = None,
    ):
        # The space ID of the user under the independent software vendor (ISV) account.
        self.cust_space_id = cust_space_id
        # The phone number.
        self.phone_number = phone_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        return self


class ChatappPhoneNumberRegisterResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](~~196974~~).
        self.code = code
        # The error message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ChatappPhoneNumberRegisterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ChatappPhoneNumberRegisterResponseBody = None,
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
            temp_model = ChatappPhoneNumberRegisterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChatappSyncPhoneNumberRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
    ):
        # The space ID of the user under the independent software vendor (ISV) account.
        self.cust_space_id = cust_space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        return self


class ChatappSyncPhoneNumberResponseBodyPhoneNumbers(TeaModel):
    def __init__(
        self,
        code_verification_status: str = None,
        messaging_limit_tier: str = None,
        name_status: str = None,
        new_name_status: str = None,
        phone_number: str = None,
        quality_rating: str = None,
        status: str = None,
        status_callback_url: str = None,
        status_queue: str = None,
        up_callback_url: str = None,
        up_queue: str = None,
        verified_name: str = None,
    ):
        # The verification status.
        self.code_verification_status = code_verification_status
        # The number of phone numbers to which messages can be sent in a day.
        self.messaging_limit_tier = messaging_limit_tier
        # The review status of the business display name.
        self.name_status = name_status
        # The review status of the new business display name.
        self.new_name_status = new_name_status
        # The phone number.
        self.phone_number = phone_number
        # The quality rating of the phone number. Valid values: GREEN, YELLOW, and RED.
        self.quality_rating = quality_rating
        # The status of the phone number.
        self.status = status
        # The callback URL to which status reports are sent by using HTTP callbacks.
        self.status_callback_url = status_callback_url
        # The status report queue.
        self.status_queue = status_queue
        # The callback URL to which MO messages are sent by using HTTP callbacks.
        self.up_callback_url = up_callback_url
        # The mobile originated (MO) message queue.
        self.up_queue = up_queue
        # The display name of the business to which the phone number belongs.
        self.verified_name = verified_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code_verification_status is not None:
            result['CodeVerificationStatus'] = self.code_verification_status
        if self.messaging_limit_tier is not None:
            result['MessagingLimitTier'] = self.messaging_limit_tier
        if self.name_status is not None:
            result['NameStatus'] = self.name_status
        if self.new_name_status is not None:
            result['NewNameStatus'] = self.new_name_status
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.quality_rating is not None:
            result['QualityRating'] = self.quality_rating
        if self.status is not None:
            result['Status'] = self.status
        if self.status_callback_url is not None:
            result['StatusCallbackUrl'] = self.status_callback_url
        if self.status_queue is not None:
            result['StatusQueue'] = self.status_queue
        if self.up_callback_url is not None:
            result['UpCallbackUrl'] = self.up_callback_url
        if self.up_queue is not None:
            result['UpQueue'] = self.up_queue
        if self.verified_name is not None:
            result['VerifiedName'] = self.verified_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CodeVerificationStatus') is not None:
            self.code_verification_status = m.get('CodeVerificationStatus')
        if m.get('MessagingLimitTier') is not None:
            self.messaging_limit_tier = m.get('MessagingLimitTier')
        if m.get('NameStatus') is not None:
            self.name_status = m.get('NameStatus')
        if m.get('NewNameStatus') is not None:
            self.new_name_status = m.get('NewNameStatus')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('QualityRating') is not None:
            self.quality_rating = m.get('QualityRating')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusCallbackUrl') is not None:
            self.status_callback_url = m.get('StatusCallbackUrl')
        if m.get('StatusQueue') is not None:
            self.status_queue = m.get('StatusQueue')
        if m.get('UpCallbackUrl') is not None:
            self.up_callback_url = m.get('UpCallbackUrl')
        if m.get('UpQueue') is not None:
            self.up_queue = m.get('UpQueue')
        if m.get('VerifiedName') is not None:
            self.verified_name = m.get('VerifiedName')
        return self


class ChatappSyncPhoneNumberResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        phone_numbers: List[ChatappSyncPhoneNumberResponseBodyPhoneNumbers] = None,
        request_id: str = None,
    ):
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](~~196974~~).
        self.code = code
        # The error message returned.
        self.message = message
        # Details of the phone numbers.
        self.phone_numbers = phone_numbers
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.phone_numbers:
            for k in self.phone_numbers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        result['PhoneNumbers'] = []
        if self.phone_numbers is not None:
            for k in self.phone_numbers:
                result['PhoneNumbers'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.phone_numbers = []
        if m.get('PhoneNumbers') is not None:
            for k in m.get('PhoneNumbers'):
                temp_model = ChatappSyncPhoneNumberResponseBodyPhoneNumbers()
                self.phone_numbers.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ChatappSyncPhoneNumberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ChatappSyncPhoneNumberResponseBody = None,
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
            temp_model = ChatappSyncPhoneNumberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChatappVerifyAndRegisterRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        phone_number: str = None,
        verify_code: str = None,
    ):
        # The space ID of the user under the independent software vendor (ISV) account.
        self.cust_space_id = cust_space_id
        # The phone number.
        self.phone_number = phone_number
        # The verification code.
        self.verify_code = verify_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.verify_code is not None:
            result['VerifyCode'] = self.verify_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('VerifyCode') is not None:
            self.verify_code = m.get('VerifyCode')
        return self


class ChatappVerifyAndRegisterResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](~~196974~~).
        self.code = code
        # The error message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ChatappVerifyAndRegisterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ChatappVerifyAndRegisterResponseBody = None,
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
            temp_model = ChatappVerifyAndRegisterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateChatappMigrationInitiateRequest(TeaModel):
    def __init__(
        self,
        country_code: str = None,
        cust_space_id: str = None,
        mobile_number: str = None,
    ):
        self.country_code = country_code
        self.cust_space_id = cust_space_id
        self.mobile_number = mobile_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.country_code is not None:
            result['CountryCode'] = self.country_code
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.mobile_number is not None:
            result['MobileNumber'] = self.mobile_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CountryCode') is not None:
            self.country_code = m.get('CountryCode')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('MobileNumber') is not None:
            self.mobile_number = m.get('MobileNumber')
        return self


class CreateChatappMigrationInitiateResponseBodyData(TeaModel):
    def __init__(
        self,
        id: str = None,
        phone_number: str = None,
        status: str = None,
    ):
        self.id = id
        self.phone_number = phone_number
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateChatappMigrationInitiateResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateChatappMigrationInitiateResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

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
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreateChatappMigrationInitiateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateChatappMigrationInitiateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateChatappMigrationInitiateResponseBody = None,
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
            temp_model = CreateChatappMigrationInitiateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateChatappTemplateRequestComponentsButtons(TeaModel):
    def __init__(
        self,
        autofill_text: str = None,
        is_opt_out: bool = None,
        package_name: str = None,
        phone_number: str = None,
        signature_hash: str = None,
        text: str = None,
        type: str = None,
        url: str = None,
        url_type: str = None,
    ):
        self.autofill_text = autofill_text
        self.is_opt_out = is_opt_out
        self.package_name = package_name
        self.phone_number = phone_number
        self.signature_hash = signature_hash
        self.text = text
        self.type = type
        self.url = url
        self.url_type = url_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.autofill_text is not None:
            result['AutofillText'] = self.autofill_text
        if self.is_opt_out is not None:
            result['IsOptOut'] = self.is_opt_out
        if self.package_name is not None:
            result['PackageName'] = self.package_name
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.signature_hash is not None:
            result['SignatureHash'] = self.signature_hash
        if self.text is not None:
            result['Text'] = self.text
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        if self.url_type is not None:
            result['UrlType'] = self.url_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutofillText') is not None:
            self.autofill_text = m.get('AutofillText')
        if m.get('IsOptOut') is not None:
            self.is_opt_out = m.get('IsOptOut')
        if m.get('PackageName') is not None:
            self.package_name = m.get('PackageName')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('SignatureHash') is not None:
            self.signature_hash = m.get('SignatureHash')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('UrlType') is not None:
            self.url_type = m.get('UrlType')
        return self


class CreateChatappTemplateRequestComponents(TeaModel):
    def __init__(
        self,
        add_secret_recommendation: bool = None,
        buttons: List[CreateChatappTemplateRequestComponentsButtons] = None,
        caption: str = None,
        code_expiration_minutes: int = None,
        duration: int = None,
        file_name: str = None,
        file_type: str = None,
        format: str = None,
        text: str = None,
        thumb_url: str = None,
        type: str = None,
        url: str = None,
    ):
        self.add_secret_recommendation = add_secret_recommendation
        self.buttons = buttons
        self.caption = caption
        self.code_expiration_minutes = code_expiration_minutes
        self.duration = duration
        self.file_name = file_name
        self.file_type = file_type
        self.format = format
        self.text = text
        self.thumb_url = thumb_url
        self.type = type
        self.url = url

    def validate(self):
        if self.buttons:
            for k in self.buttons:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_secret_recommendation is not None:
            result['AddSecretRecommendation'] = self.add_secret_recommendation
        result['Buttons'] = []
        if self.buttons is not None:
            for k in self.buttons:
                result['Buttons'].append(k.to_map() if k else None)
        if self.caption is not None:
            result['Caption'] = self.caption
        if self.code_expiration_minutes is not None:
            result['CodeExpirationMinutes'] = self.code_expiration_minutes
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.format is not None:
            result['Format'] = self.format
        if self.text is not None:
            result['Text'] = self.text
        if self.thumb_url is not None:
            result['ThumbUrl'] = self.thumb_url
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddSecretRecommendation') is not None:
            self.add_secret_recommendation = m.get('AddSecretRecommendation')
        self.buttons = []
        if m.get('Buttons') is not None:
            for k in m.get('Buttons'):
                temp_model = CreateChatappTemplateRequestComponentsButtons()
                self.buttons.append(temp_model.from_map(k))
        if m.get('Caption') is not None:
            self.caption = m.get('Caption')
        if m.get('CodeExpirationMinutes') is not None:
            self.code_expiration_minutes = m.get('CodeExpirationMinutes')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('ThumbUrl') is not None:
            self.thumb_url = m.get('ThumbUrl')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class CreateChatappTemplateRequest(TeaModel):
    def __init__(
        self,
        allow_category_change: bool = None,
        category: str = None,
        components: List[CreateChatappTemplateRequestComponents] = None,
        cust_space_id: str = None,
        cust_waba_id: str = None,
        example: Dict[str, str] = None,
        isv_code: str = None,
        language: str = None,
        name: str = None,
        template_type: str = None,
    ):
        # 是否允许facebook自动变更模板的目录（这样能提高模板的审核通过率）此属性只对TemplateType=WHATSAPP有效
        self.allow_category_change = allow_category_change
        # The returned data.
        self.category = category
        # The name of the message template.
        self.components = components
        self.cust_space_id = cust_space_id
        self.cust_waba_id = cust_waba_id
        self.example = example
        self.isv_code = isv_code
        self.language = language
        self.name = name
        self.template_type = template_type

    def validate(self):
        if self.components:
            for k in self.components:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_category_change is not None:
            result['AllowCategoryChange'] = self.allow_category_change
        if self.category is not None:
            result['Category'] = self.category
        result['Components'] = []
        if self.components is not None:
            for k in self.components:
                result['Components'].append(k.to_map() if k else None)
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.cust_waba_id is not None:
            result['CustWabaId'] = self.cust_waba_id
        if self.example is not None:
            result['Example'] = self.example
        if self.isv_code is not None:
            result['IsvCode'] = self.isv_code
        if self.language is not None:
            result['Language'] = self.language
        if self.name is not None:
            result['Name'] = self.name
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowCategoryChange') is not None:
            self.allow_category_change = m.get('AllowCategoryChange')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        self.components = []
        if m.get('Components') is not None:
            for k in m.get('Components'):
                temp_model = CreateChatappTemplateRequestComponents()
                self.components.append(temp_model.from_map(k))
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('CustWabaId') is not None:
            self.cust_waba_id = m.get('CustWabaId')
        if m.get('Example') is not None:
            self.example = m.get('Example')
        if m.get('IsvCode') is not None:
            self.isv_code = m.get('IsvCode')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class CreateChatappTemplateShrinkRequest(TeaModel):
    def __init__(
        self,
        allow_category_change: bool = None,
        category: str = None,
        components_shrink: str = None,
        cust_space_id: str = None,
        cust_waba_id: str = None,
        example_shrink: str = None,
        isv_code: str = None,
        language: str = None,
        name: str = None,
        template_type: str = None,
    ):
        # 是否允许facebook自动变更模板的目录（这样能提高模板的审核通过率）此属性只对TemplateType=WHATSAPP有效
        self.allow_category_change = allow_category_change
        # The returned data.
        self.category = category
        # The name of the message template.
        self.components_shrink = components_shrink
        self.cust_space_id = cust_space_id
        self.cust_waba_id = cust_waba_id
        self.example_shrink = example_shrink
        self.isv_code = isv_code
        self.language = language
        self.name = name
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_category_change is not None:
            result['AllowCategoryChange'] = self.allow_category_change
        if self.category is not None:
            result['Category'] = self.category
        if self.components_shrink is not None:
            result['Components'] = self.components_shrink
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.cust_waba_id is not None:
            result['CustWabaId'] = self.cust_waba_id
        if self.example_shrink is not None:
            result['Example'] = self.example_shrink
        if self.isv_code is not None:
            result['IsvCode'] = self.isv_code
        if self.language is not None:
            result['Language'] = self.language
        if self.name is not None:
            result['Name'] = self.name
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowCategoryChange') is not None:
            self.allow_category_change = m.get('AllowCategoryChange')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Components') is not None:
            self.components_shrink = m.get('Components')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('CustWabaId') is not None:
            self.cust_waba_id = m.get('CustWabaId')
        if m.get('Example') is not None:
            self.example_shrink = m.get('Example')
        if m.get('IsvCode') is not None:
            self.isv_code = m.get('IsvCode')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class CreateChatappTemplateResponseBodyData(TeaModel):
    def __init__(
        self,
        template_code: str = None,
        template_name: str = None,
    ):
        self.template_code = template_code
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class CreateChatappTemplateResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateChatappTemplateResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

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
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreateChatappTemplateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateChatappTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateChatappTemplateResponseBody = None,
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
            temp_model = CreateChatappTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteChatappTemplateRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        cust_waba_id: str = None,
        isv_code: str = None,
        template_code: str = None,
    ):
        # The space ID of the user under the ISV account.
        self.cust_space_id = cust_space_id
        # The ID of the WhatsApp account that you register.
        self.cust_waba_id = cust_waba_id
        # The independent software vendor (ISV) verification code, which is used to verify whether the user is authorized by the ISV account.
        self.isv_code = isv_code
        # The code of the message template.
        self.template_code = template_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.cust_waba_id is not None:
            result['CustWabaId'] = self.cust_waba_id
        if self.isv_code is not None:
            result['IsvCode'] = self.isv_code
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('CustWabaId') is not None:
            self.cust_waba_id = m.get('CustWabaId')
        if m.get('IsvCode') is not None:
            self.isv_code = m.get('IsvCode')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        return self


class DeleteChatappTemplateResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](~~196974~~).
        self.code = code
        # The error message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteChatappTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteChatappTemplateResponseBody = None,
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
            temp_model = DeleteChatappTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetChatappTemplateDetailRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        cust_waba_id: str = None,
        isv_code: str = None,
        language: str = None,
        template_code: str = None,
        template_type: str = None,
    ):
        self.cust_space_id = cust_space_id
        self.cust_waba_id = cust_waba_id
        self.isv_code = isv_code
        self.language = language
        # The type of the message template. Valid values:
        # 
        # *   **WHATSAPP**\
        # *   **VIBER**\
        # *   LINE (developing)
        self.template_code = template_code
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.cust_waba_id is not None:
            result['CustWabaId'] = self.cust_waba_id
        if self.isv_code is not None:
            result['IsvCode'] = self.isv_code
        if self.language is not None:
            result['Language'] = self.language
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('CustWabaId') is not None:
            self.cust_waba_id = m.get('CustWabaId')
        if m.get('IsvCode') is not None:
            self.isv_code = m.get('IsvCode')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class GetChatappTemplateDetailResponseBodyDataComponentsButtonsExtendAttrs(TeaModel):
    def __init__(
        self,
        action: str = None,
        intent_code: str = None,
        next_language_code: str = None,
        next_template_code: str = None,
        next_template_name: str = None,
    ):
        # 事件类型
        self.action = action
        # 意图编码
        self.intent_code = intent_code
        # 下一个模板语言
        self.next_language_code = next_language_code
        # 下一个模板编码
        self.next_template_code = next_template_code
        # 下一个模板名称
        self.next_template_name = next_template_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.intent_code is not None:
            result['IntentCode'] = self.intent_code
        if self.next_language_code is not None:
            result['NextLanguageCode'] = self.next_language_code
        if self.next_template_code is not None:
            result['NextTemplateCode'] = self.next_template_code
        if self.next_template_name is not None:
            result['NextTemplateName'] = self.next_template_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('IntentCode') is not None:
            self.intent_code = m.get('IntentCode')
        if m.get('NextLanguageCode') is not None:
            self.next_language_code = m.get('NextLanguageCode')
        if m.get('NextTemplateCode') is not None:
            self.next_template_code = m.get('NextTemplateCode')
        if m.get('NextTemplateName') is not None:
            self.next_template_name = m.get('NextTemplateName')
        return self


class GetChatappTemplateDetailResponseBodyDataComponentsButtons(TeaModel):
    def __init__(
        self,
        autofill_text: str = None,
        extend_attrs: GetChatappTemplateDetailResponseBodyDataComponentsButtonsExtendAttrs = None,
        is_opt_out: bool = None,
        package_name: str = None,
        phone_number: str = None,
        signature_hash: str = None,
        text: str = None,
        type: str = None,
        url: str = None,
        url_type: str = None,
    ):
        # Whatsapp模板，Category为Authentication，并且Button Type为ONE_TAP时必填，Whatsap Autofill操作的按钮文本
        self.autofill_text = autofill_text
        # 扩展字段
        self.extend_attrs = extend_attrs
        # Whatsapp模板，在Category为Marketing,并且Button type为QUICK_REPLY时有效，表示按钮为营销退订按钮，客户如果点击了此按钮，并且在chatapp平台上配置了发送控制操作，则后续Marketing消息则不会发送到客户
        self.is_opt_out = is_opt_out
        # Whatsapp模板，Category为Authentication，并且Button Type为ONE_TAP时必填，表示Whatsapp调起应用的包名
        self.package_name = package_name
        self.phone_number = phone_number
        # Whatsapp模板，Category为Authentication，并且Button Type为ONE_TAP时必填，表示Whatsapp调起应用的签名Hash值
        self.signature_hash = signature_hash
        self.text = text
        self.type = type
        self.url = url
        self.url_type = url_type

    def validate(self):
        if self.extend_attrs:
            self.extend_attrs.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.autofill_text is not None:
            result['AutofillText'] = self.autofill_text
        if self.extend_attrs is not None:
            result['ExtendAttrs'] = self.extend_attrs.to_map()
        if self.is_opt_out is not None:
            result['IsOptOut'] = self.is_opt_out
        if self.package_name is not None:
            result['PackageName'] = self.package_name
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.signature_hash is not None:
            result['SignatureHash'] = self.signature_hash
        if self.text is not None:
            result['Text'] = self.text
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        if self.url_type is not None:
            result['UrlType'] = self.url_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutofillText') is not None:
            self.autofill_text = m.get('AutofillText')
        if m.get('ExtendAttrs') is not None:
            temp_model = GetChatappTemplateDetailResponseBodyDataComponentsButtonsExtendAttrs()
            self.extend_attrs = temp_model.from_map(m['ExtendAttrs'])
        if m.get('IsOptOut') is not None:
            self.is_opt_out = m.get('IsOptOut')
        if m.get('PackageName') is not None:
            self.package_name = m.get('PackageName')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('SignatureHash') is not None:
            self.signature_hash = m.get('SignatureHash')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('UrlType') is not None:
            self.url_type = m.get('UrlType')
        return self


class GetChatappTemplateDetailResponseBodyDataComponents(TeaModel):
    def __init__(
        self,
        add_secret_recommendation: bool = None,
        buttons: List[GetChatappTemplateDetailResponseBodyDataComponentsButtons] = None,
        caption: str = None,
        code_expiration_minutes: int = None,
        duration: int = None,
        file_name: str = None,
        file_type: str = None,
        format: str = None,
        latitude: str = None,
        location_address: str = None,
        location_name: str = None,
        longitude: str = None,
        text: str = None,
        thumb_url: str = None,
        type: str = None,
        url: str = None,
    ):
        # Whatsapp类型模板，Category为Authentication，并且Component Type为Body时有效，表示在Body上面显示不要将验证码信息提供给其它人的提示信息
        self.add_secret_recommendation = add_secret_recommendation
        self.buttons = buttons
        self.caption = caption
        # Whatsapp Authentication模板验证码有效期（分钟），只在Whatsapp类型消息，Category为Authentication并且Component Type为Footer时有效（此信息显示在Footer位置）
        self.code_expiration_minutes = code_expiration_minutes
        self.duration = duration
        self.file_name = file_name
        self.file_type = file_type
        self.format = format
        # 位置纬度属性
        self.latitude = latitude
        # 位置地址
        self.location_address = location_address
        # 位置名称
        self.location_name = location_name
        # 位置经度属性
        self.longitude = longitude
        self.text = text
        self.thumb_url = thumb_url
        self.type = type
        self.url = url

    def validate(self):
        if self.buttons:
            for k in self.buttons:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_secret_recommendation is not None:
            result['AddSecretRecommendation'] = self.add_secret_recommendation
        result['Buttons'] = []
        if self.buttons is not None:
            for k in self.buttons:
                result['Buttons'].append(k.to_map() if k else None)
        if self.caption is not None:
            result['Caption'] = self.caption
        if self.code_expiration_minutes is not None:
            result['CodeExpirationMinutes'] = self.code_expiration_minutes
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.format is not None:
            result['Format'] = self.format
        if self.latitude is not None:
            result['Latitude'] = self.latitude
        if self.location_address is not None:
            result['LocationAddress'] = self.location_address
        if self.location_name is not None:
            result['LocationName'] = self.location_name
        if self.longitude is not None:
            result['Longitude'] = self.longitude
        if self.text is not None:
            result['Text'] = self.text
        if self.thumb_url is not None:
            result['ThumbUrl'] = self.thumb_url
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddSecretRecommendation') is not None:
            self.add_secret_recommendation = m.get('AddSecretRecommendation')
        self.buttons = []
        if m.get('Buttons') is not None:
            for k in m.get('Buttons'):
                temp_model = GetChatappTemplateDetailResponseBodyDataComponentsButtons()
                self.buttons.append(temp_model.from_map(k))
        if m.get('Caption') is not None:
            self.caption = m.get('Caption')
        if m.get('CodeExpirationMinutes') is not None:
            self.code_expiration_minutes = m.get('CodeExpirationMinutes')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('Latitude') is not None:
            self.latitude = m.get('Latitude')
        if m.get('LocationAddress') is not None:
            self.location_address = m.get('LocationAddress')
        if m.get('LocationName') is not None:
            self.location_name = m.get('LocationName')
        if m.get('Longitude') is not None:
            self.longitude = m.get('Longitude')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('ThumbUrl') is not None:
            self.thumb_url = m.get('ThumbUrl')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetChatappTemplateDetailResponseBodyData(TeaModel):
    def __init__(
        self,
        audit_status: str = None,
        category: str = None,
        components: List[GetChatappTemplateDetailResponseBodyDataComponents] = None,
        example: Dict[str, str] = None,
        language: str = None,
        name: str = None,
        template_code: str = None,
        template_type: str = None,
    ):
        self.audit_status = audit_status
        self.category = category
        self.components = components
        self.example = example
        self.language = language
        self.name = name
        self.template_code = template_code
        self.template_type = template_type

    def validate(self):
        if self.components:
            for k in self.components:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status
        if self.category is not None:
            result['Category'] = self.category
        result['Components'] = []
        if self.components is not None:
            for k in self.components:
                result['Components'].append(k.to_map() if k else None)
        if self.example is not None:
            result['Example'] = self.example
        if self.language is not None:
            result['Language'] = self.language
        if self.name is not None:
            result['Name'] = self.name
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        self.components = []
        if m.get('Components') is not None:
            for k in m.get('Components'):
                temp_model = GetChatappTemplateDetailResponseBodyDataComponents()
                self.components.append(temp_model.from_map(k))
        if m.get('Example') is not None:
            self.example = m.get('Example')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class GetChatappTemplateDetailResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetChatappTemplateDetailResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

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
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetChatappTemplateDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetChatappTemplateDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetChatappTemplateDetailResponseBody = None,
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
            temp_model = GetChatappTemplateDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetChatappUploadAuthorizationRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
    ):
        # The space ID of the user under the independent software vendor (ISV) account.
        self.cust_space_id = cust_space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        return self


class GetChatappUploadAuthorizationResponseBodyData(TeaModel):
    def __init__(
        self,
        access_key_id: str = None,
        access_key_secret: str = None,
        bucket_name: str = None,
        dir: str = None,
        end_point: str = None,
        expire: int = None,
        security_token: str = None,
    ):
        # The AccessKey ID that is used to authorize a user to upload a file to Object Storage Service (OSS).
        self.access_key_id = access_key_id
        # The AccessKey secret that is used to authorize a user to upload a file to OSS.
        self.access_key_secret = access_key_secret
        # The name of the bucket to which a file is uploaded in OSS.
        self.bucket_name = bucket_name
        # The directory to which a file is uploaded in OSS.
        self.dir = dir
        # The address of the OSS server to which a file is uploaded.
        self.end_point = end_point
        # The timeout period.
        self.expire = expire
        # The security token.
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        if self.access_key_secret is not None:
            result['AccessKeySecret'] = self.access_key_secret
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.dir is not None:
            result['Dir'] = self.dir
        if self.end_point is not None:
            result['EndPoint'] = self.end_point
        if self.expire is not None:
            result['Expire'] = self.expire
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        if m.get('AccessKeySecret') is not None:
            self.access_key_secret = m.get('AccessKeySecret')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('Dir') is not None:
            self.dir = m.get('Dir')
        if m.get('EndPoint') is not None:
            self.end_point = m.get('EndPoint')
        if m.get('Expire') is not None:
            self.expire = m.get('Expire')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class GetChatappUploadAuthorizationResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetChatappUploadAuthorizationResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](~~196974~~).
        self.code = code
        # The data returned.
        self.data = data
        # The error message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

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
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetChatappUploadAuthorizationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetChatappUploadAuthorizationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetChatappUploadAuthorizationResponseBody = None,
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
            temp_model = GetChatappUploadAuthorizationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetChatappVerifyCodeRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        locale: str = None,
        method: str = None,
        phone_number: str = None,
    ):
        # The space ID of the user under the independent software vendor (ISV) account.
        self.cust_space_id = cust_space_id
        # The language.
        self.locale = locale
        # The method to obtain the verification code. Valid values: SMS and VOICE.
        self.method = method
        # The phone number.
        self.phone_number = phone_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.locale is not None:
            result['Locale'] = self.locale
        if self.method is not None:
            result['Method'] = self.method
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('Locale') is not None:
            self.locale = m.get('Locale')
        if m.get('Method') is not None:
            self.method = m.get('Method')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        return self


class GetChatappVerifyCodeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](~~196974~~).
        self.code = code
        # The error message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetChatappVerifyCodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetChatappVerifyCodeResponseBody = None,
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
            temp_model = GetChatappVerifyCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMigrationVerifyCodeRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        locale: str = None,
        method: str = None,
        phone_number: str = None,
    ):
        self.cust_space_id = cust_space_id
        self.locale = locale
        self.method = method
        self.phone_number = phone_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.locale is not None:
            result['Locale'] = self.locale
        if self.method is not None:
            result['Method'] = self.method
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('Locale') is not None:
            self.locale = m.get('Locale')
        if m.get('Method') is not None:
            self.method = m.get('Method')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        return self


class GetMigrationVerifyCodeResponseBodyData(TeaModel):
    def __init__(
        self,
        id: str = None,
        phone_number: str = None,
    ):
        self.id = id
        self.phone_number = phone_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        return self


class GetMigrationVerifyCodeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetMigrationVerifyCodeResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

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
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetMigrationVerifyCodeResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetMigrationVerifyCodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetMigrationVerifyCodeResponseBody = None,
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
            temp_model = GetMigrationVerifyCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPhoneNumberVerificationStatusRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        phone_number: str = None,
    ):
        # The space ID of the user under the ISV account.
        self.cust_space_id = cust_space_id
        # The phone number.
        self.phone_number = phone_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        return self


class GetPhoneNumberVerificationStatusResponseBodyData(TeaModel):
    def __init__(
        self,
        code_verification_status: str = None,
        id: str = None,
        phone_number: str = None,
    ):
        # The verification status.
        self.code_verification_status = code_verification_status
        # The ID of the number.
        self.id = id
        # The phone number.
        self.phone_number = phone_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code_verification_status is not None:
            result['CodeVerificationStatus'] = self.code_verification_status
        if self.id is not None:
            result['Id'] = self.id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CodeVerificationStatus') is not None:
            self.code_verification_status = m.get('CodeVerificationStatus')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        return self


class GetPhoneNumberVerificationStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetPhoneNumberVerificationStatusResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](~~196974~~).
        self.code = code
        # The data returned.
        self.data = data
        # The error message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

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
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetPhoneNumberVerificationStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPhoneNumberVerificationStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPhoneNumberVerificationStatusResponseBody = None,
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
            temp_model = GetPhoneNumberVerificationStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class IsvGetAppIdRequest(TeaModel):
    def __init__(
        self,
        type: str = None,
    ):
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class IsvGetAppIdResponseBody(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.app_id = app_id
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class IsvGetAppIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: IsvGetAppIdResponseBody = None,
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
            temp_model = IsvGetAppIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListChatappTemplateRequestPage(TeaModel):
    def __init__(
        self,
        index: int = None,
        size: int = None,
    ):
        # The number of the page to return. Pages start from page 1. Default value: 1.
        self.index = index
        # The number of message templates to return on each page. Default value: 10.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class ListChatappTemplateRequest(TeaModel):
    def __init__(
        self,
        audit_status: str = None,
        cust_space_id: str = None,
        cust_waba_id: str = None,
        isv_code: str = None,
        language: str = None,
        name: str = None,
        page: ListChatappTemplateRequestPage = None,
        template_type: str = None,
    ):
        # The review status of the message template. Valid values:
        # 
        # *   **pass**: The message template is approved.
        # *   **fail**: The message template is rejected.
        # *   **auditing**: The message template is being reviewed.
        # *   **unaudit**: The review is suspended.
        self.audit_status = audit_status
        # The space ID of the user under the ISV account.
        self.cust_space_id = cust_space_id
        # The ID of the WhatsApp account that you register.
        self.cust_waba_id = cust_waba_id
        # The independent software vendor (ISV) verification code, which is used to verify whether the user is authorized by the ISV account.
        self.isv_code = isv_code
        # The language that is used in the message template. For more information, see [Language codes](~~463420~~).
        self.language = language
        # The name of the message template.
        self.name = name
        # The paging settings.
        self.page = page
        # The type of the message template.
        # 
        # *   **WHATSAPP**\
        # *   **VIBER**\
        # *   LINE: the Line message template. This type of message template will be released later.
        self.template_type = template_type

    def validate(self):
        if self.page:
            self.page.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.cust_waba_id is not None:
            result['CustWabaId'] = self.cust_waba_id
        if self.isv_code is not None:
            result['IsvCode'] = self.isv_code
        if self.language is not None:
            result['Language'] = self.language
        if self.name is not None:
            result['Name'] = self.name
        if self.page is not None:
            result['Page'] = self.page.to_map()
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('CustWabaId') is not None:
            self.cust_waba_id = m.get('CustWabaId')
        if m.get('IsvCode') is not None:
            self.isv_code = m.get('IsvCode')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Page') is not None:
            temp_model = ListChatappTemplateRequestPage()
            self.page = temp_model.from_map(m['Page'])
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class ListChatappTemplateShrinkRequest(TeaModel):
    def __init__(
        self,
        audit_status: str = None,
        cust_space_id: str = None,
        cust_waba_id: str = None,
        isv_code: str = None,
        language: str = None,
        name: str = None,
        page_shrink: str = None,
        template_type: str = None,
    ):
        # The review status of the message template. Valid values:
        # 
        # *   **pass**: The message template is approved.
        # *   **fail**: The message template is rejected.
        # *   **auditing**: The message template is being reviewed.
        # *   **unaudit**: The review is suspended.
        self.audit_status = audit_status
        # The space ID of the user under the ISV account.
        self.cust_space_id = cust_space_id
        # The ID of the WhatsApp account that you register.
        self.cust_waba_id = cust_waba_id
        # The independent software vendor (ISV) verification code, which is used to verify whether the user is authorized by the ISV account.
        self.isv_code = isv_code
        # The language that is used in the message template. For more information, see [Language codes](~~463420~~).
        self.language = language
        # The name of the message template.
        self.name = name
        # The paging settings.
        self.page_shrink = page_shrink
        # The type of the message template.
        # 
        # *   **WHATSAPP**\
        # *   **VIBER**\
        # *   LINE: the Line message template. This type of message template will be released later.
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.cust_waba_id is not None:
            result['CustWabaId'] = self.cust_waba_id
        if self.isv_code is not None:
            result['IsvCode'] = self.isv_code
        if self.language is not None:
            result['Language'] = self.language
        if self.name is not None:
            result['Name'] = self.name
        if self.page_shrink is not None:
            result['Page'] = self.page_shrink
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('CustWabaId') is not None:
            self.cust_waba_id = m.get('CustWabaId')
        if m.get('IsvCode') is not None:
            self.isv_code = m.get('IsvCode')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Page') is not None:
            self.page_shrink = m.get('Page')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class ListChatappTemplateResponseBodyListTemplate(TeaModel):
    def __init__(
        self,
        audit_status: str = None,
        category: str = None,
        language: str = None,
        template_code: str = None,
        template_name: str = None,
        template_type: str = None,
    ):
        # The review status of the message template. Valid values:
        # 
        # *   **pass**: The message template is approved.
        # *   **fail**: The message template is rejected.
        # *   **auditing**: The message template is being reviewed.
        # *   **unaudit**: The review is suspended.
        self.audit_status = audit_status
        # The category of the message template. Valid values:
        # 
        # *   **TRANSACTIONAL**: a transactional template
        # *   **MARKETING**: a marketing template
        # *   **OTP**: a one-time password template
        self.category = category
        # The language that is used in the message template. For more information, see [Language codes](~~463420~~).
        self.language = language
        # The code of the message template.
        self.template_code = template_code
        # The name of the message template.
        self.template_name = template_name
        # The type of the template. Valid values: WHATSAPP and VIBER.
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status
        if self.category is not None:
            result['Category'] = self.category
        if self.language is not None:
            result['Language'] = self.language
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class ListChatappTemplateResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        list_template: List[ListChatappTemplateResponseBodyListTemplate] = None,
        message: str = None,
        request_id: str = None,
        total: int = None,
    ):
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](~~196974~~).
        self.code = code
        # The message templates.
        self.list_template = list_template
        # The error message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # 总记录条数。
        self.total = total

    def validate(self):
        if self.list_template:
            for k in self.list_template:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['ListTemplate'] = []
        if self.list_template is not None:
            for k in self.list_template:
                result['ListTemplate'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.list_template = []
        if m.get('ListTemplate') is not None:
            for k in m.get('ListTemplate'):
                temp_model = ListChatappTemplateResponseBodyListTemplate()
                self.list_template.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListChatappTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListChatappTemplateResponseBody = None,
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
            temp_model = ListChatappTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyChatappTemplateRequestComponentsButtons(TeaModel):
    def __init__(
        self,
        autofill_text: str = None,
        is_opt_out: bool = None,
        package_name: str = None,
        phone_number: str = None,
        signature_hash: str = None,
        text: str = None,
        type: str = None,
        url: str = None,
        url_type: str = None,
    ):
        self.autofill_text = autofill_text
        self.is_opt_out = is_opt_out
        self.package_name = package_name
        self.phone_number = phone_number
        self.signature_hash = signature_hash
        self.text = text
        self.type = type
        self.url = url
        self.url_type = url_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.autofill_text is not None:
            result['AutofillText'] = self.autofill_text
        if self.is_opt_out is not None:
            result['IsOptOut'] = self.is_opt_out
        if self.package_name is not None:
            result['PackageName'] = self.package_name
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.signature_hash is not None:
            result['SignatureHash'] = self.signature_hash
        if self.text is not None:
            result['Text'] = self.text
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        if self.url_type is not None:
            result['UrlType'] = self.url_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutofillText') is not None:
            self.autofill_text = m.get('AutofillText')
        if m.get('IsOptOut') is not None:
            self.is_opt_out = m.get('IsOptOut')
        if m.get('PackageName') is not None:
            self.package_name = m.get('PackageName')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('SignatureHash') is not None:
            self.signature_hash = m.get('SignatureHash')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('UrlType') is not None:
            self.url_type = m.get('UrlType')
        return self


class ModifyChatappTemplateRequestComponents(TeaModel):
    def __init__(
        self,
        add_secret_recommendation: bool = None,
        buttons: List[ModifyChatappTemplateRequestComponentsButtons] = None,
        caption: str = None,
        code_expiration_minutes: int = None,
        duration: int = None,
        file_name: str = None,
        file_type: str = None,
        format: str = None,
        text: str = None,
        thumb_url: str = None,
        type: str = None,
        url: str = None,
    ):
        self.add_secret_recommendation = add_secret_recommendation
        self.buttons = buttons
        self.caption = caption
        self.code_expiration_minutes = code_expiration_minutes
        self.duration = duration
        self.file_name = file_name
        self.file_type = file_type
        self.format = format
        self.text = text
        self.thumb_url = thumb_url
        self.type = type
        self.url = url

    def validate(self):
        if self.buttons:
            for k in self.buttons:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_secret_recommendation is not None:
            result['AddSecretRecommendation'] = self.add_secret_recommendation
        result['Buttons'] = []
        if self.buttons is not None:
            for k in self.buttons:
                result['Buttons'].append(k.to_map() if k else None)
        if self.caption is not None:
            result['Caption'] = self.caption
        if self.code_expiration_minutes is not None:
            result['CodeExpirationMinutes'] = self.code_expiration_minutes
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.format is not None:
            result['Format'] = self.format
        if self.text is not None:
            result['Text'] = self.text
        if self.thumb_url is not None:
            result['ThumbUrl'] = self.thumb_url
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddSecretRecommendation') is not None:
            self.add_secret_recommendation = m.get('AddSecretRecommendation')
        self.buttons = []
        if m.get('Buttons') is not None:
            for k in m.get('Buttons'):
                temp_model = ModifyChatappTemplateRequestComponentsButtons()
                self.buttons.append(temp_model.from_map(k))
        if m.get('Caption') is not None:
            self.caption = m.get('Caption')
        if m.get('CodeExpirationMinutes') is not None:
            self.code_expiration_minutes = m.get('CodeExpirationMinutes')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('ThumbUrl') is not None:
            self.thumb_url = m.get('ThumbUrl')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class ModifyChatappTemplateRequest(TeaModel):
    def __init__(
        self,
        category: str = None,
        components: List[ModifyChatappTemplateRequestComponents] = None,
        cust_space_id: str = None,
        cust_waba_id: str = None,
        example: Dict[str, str] = None,
        isv_code: str = None,
        language: str = None,
        template_code: str = None,
        template_type: str = None,
    ):
        self.category = category
        self.components = components
        self.cust_space_id = cust_space_id
        self.cust_waba_id = cust_waba_id
        self.example = example
        self.isv_code = isv_code
        self.language = language
        self.template_code = template_code
        self.template_type = template_type

    def validate(self):
        if self.components:
            for k in self.components:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        result['Components'] = []
        if self.components is not None:
            for k in self.components:
                result['Components'].append(k.to_map() if k else None)
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.cust_waba_id is not None:
            result['CustWabaId'] = self.cust_waba_id
        if self.example is not None:
            result['Example'] = self.example
        if self.isv_code is not None:
            result['IsvCode'] = self.isv_code
        if self.language is not None:
            result['Language'] = self.language
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        self.components = []
        if m.get('Components') is not None:
            for k in m.get('Components'):
                temp_model = ModifyChatappTemplateRequestComponents()
                self.components.append(temp_model.from_map(k))
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('CustWabaId') is not None:
            self.cust_waba_id = m.get('CustWabaId')
        if m.get('Example') is not None:
            self.example = m.get('Example')
        if m.get('IsvCode') is not None:
            self.isv_code = m.get('IsvCode')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class ModifyChatappTemplateShrinkRequest(TeaModel):
    def __init__(
        self,
        category: str = None,
        components_shrink: str = None,
        cust_space_id: str = None,
        cust_waba_id: str = None,
        example_shrink: str = None,
        isv_code: str = None,
        language: str = None,
        template_code: str = None,
        template_type: str = None,
    ):
        self.category = category
        self.components_shrink = components_shrink
        self.cust_space_id = cust_space_id
        self.cust_waba_id = cust_waba_id
        self.example_shrink = example_shrink
        self.isv_code = isv_code
        self.language = language
        self.template_code = template_code
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.components_shrink is not None:
            result['Components'] = self.components_shrink
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.cust_waba_id is not None:
            result['CustWabaId'] = self.cust_waba_id
        if self.example_shrink is not None:
            result['Example'] = self.example_shrink
        if self.isv_code is not None:
            result['IsvCode'] = self.isv_code
        if self.language is not None:
            result['Language'] = self.language
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Components') is not None:
            self.components_shrink = m.get('Components')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('CustWabaId') is not None:
            self.cust_waba_id = m.get('CustWabaId')
        if m.get('Example') is not None:
            self.example_shrink = m.get('Example')
        if m.get('IsvCode') is not None:
            self.isv_code = m.get('IsvCode')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class ModifyChatappTemplateResponseBodyData(TeaModel):
    def __init__(
        self,
        template_code: str = None,
        template_name: str = None,
    ):
        self.template_code = template_code
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class ModifyChatappTemplateResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ModifyChatappTemplateResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

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
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ModifyChatappTemplateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyChatappTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyChatappTemplateResponseBody = None,
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
            temp_model = ModifyChatappTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyPhoneBusinessProfileRequest(TeaModel):
    def __init__(
        self,
        address: str = None,
        cust_space_id: str = None,
        description: str = None,
        email: str = None,
        phone_number: str = None,
        profile_picture_url: str = None,
        vertical: str = None,
        websites: List[str] = None,
    ):
        # The address.
        self.address = address
        # The space ID of the user under the independent software vendor (ISV) account.
        self.cust_space_id = cust_space_id
        # The description.
        self.description = description
        # The email address.
        self.email = email
        # The phone number.
        self.phone_number = phone_number
        # The URL of the profile picture.
        self.profile_picture_url = profile_picture_url
        # The industry.
        self.vertical = vertical
        # The websites.
        self.websites = websites

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.description is not None:
            result['Description'] = self.description
        if self.email is not None:
            result['Email'] = self.email
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.profile_picture_url is not None:
            result['ProfilePictureUrl'] = self.profile_picture_url
        if self.vertical is not None:
            result['Vertical'] = self.vertical
        if self.websites is not None:
            result['Websites'] = self.websites
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('ProfilePictureUrl') is not None:
            self.profile_picture_url = m.get('ProfilePictureUrl')
        if m.get('Vertical') is not None:
            self.vertical = m.get('Vertical')
        if m.get('Websites') is not None:
            self.websites = m.get('Websites')
        return self


class ModifyPhoneBusinessProfileShrinkRequest(TeaModel):
    def __init__(
        self,
        address: str = None,
        cust_space_id: str = None,
        description: str = None,
        email: str = None,
        phone_number: str = None,
        profile_picture_url: str = None,
        vertical: str = None,
        websites_shrink: str = None,
    ):
        # The address.
        self.address = address
        # The space ID of the user under the independent software vendor (ISV) account.
        self.cust_space_id = cust_space_id
        # The description.
        self.description = description
        # The email address.
        self.email = email
        # The phone number.
        self.phone_number = phone_number
        # The URL of the profile picture.
        self.profile_picture_url = profile_picture_url
        # The industry.
        self.vertical = vertical
        # The websites.
        self.websites_shrink = websites_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.description is not None:
            result['Description'] = self.description
        if self.email is not None:
            result['Email'] = self.email
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.profile_picture_url is not None:
            result['ProfilePictureUrl'] = self.profile_picture_url
        if self.vertical is not None:
            result['Vertical'] = self.vertical
        if self.websites_shrink is not None:
            result['Websites'] = self.websites_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('ProfilePictureUrl') is not None:
            self.profile_picture_url = m.get('ProfilePictureUrl')
        if m.get('Vertical') is not None:
            self.vertical = m.get('Vertical')
        if m.get('Websites') is not None:
            self.websites_shrink = m.get('Websites')
        return self


class ModifyPhoneBusinessProfileResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](~~196974~~).
        self.code = code
        # The error message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyPhoneBusinessProfileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyPhoneBusinessProfileResponseBody = None,
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
            temp_model = ModifyPhoneBusinessProfileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryChatappBindWabaRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        isv_code: str = None,
    ):
        # The space ID of the user under the ISV account.
        self.cust_space_id = cust_space_id
        # The ISV verification code, which is used to verify whether the user is authorized by the ISV account.
        self.isv_code = isv_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.isv_code is not None:
            result['IsvCode'] = self.isv_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('IsvCode') is not None:
            self.isv_code = m.get('IsvCode')
        return self


class QueryChatappBindWabaResponseBodyData(TeaModel):
    def __init__(
        self,
        account_review_status: str = None,
        currency: str = None,
        id: str = None,
        message_template_namespace: str = None,
        name: str = None,
    ):
        # The review status of the WhatsApp Business account.
        self.account_review_status = account_review_status
        # The currency.
        self.currency = currency
        # The ID of the WhatsApp Business account.
        self.id = id
        # The namespace of the message template.
        self.message_template_namespace = message_template_namespace
        # The name of the WhatsApp Business account.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_review_status is not None:
            result['AccountReviewStatus'] = self.account_review_status
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.id is not None:
            result['Id'] = self.id
        if self.message_template_namespace is not None:
            result['MessageTemplateNamespace'] = self.message_template_namespace
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountReviewStatus') is not None:
            self.account_review_status = m.get('AccountReviewStatus')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MessageTemplateNamespace') is not None:
            self.message_template_namespace = m.get('MessageTemplateNamespace')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class QueryChatappBindWabaResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryChatappBindWabaResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](~~196974~~).
        self.code = code
        # The data returned.
        self.data = data
        # The error message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

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
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = QueryChatappBindWabaResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryChatappBindWabaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryChatappBindWabaResponseBody = None,
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
            temp_model = QueryChatappBindWabaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryChatappPhoneNumbersRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        isv_code: str = None,
    ):
        # The space ID of the user under the ISV account.
        self.cust_space_id = cust_space_id
        # The ISV verification code, which is used to verify whether the user is authorized by the ISV account.
        self.isv_code = isv_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.isv_code is not None:
            result['IsvCode'] = self.isv_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('IsvCode') is not None:
            self.isv_code = m.get('IsvCode')
        return self


class QueryChatappPhoneNumbersResponseBodyPhoneNumbers(TeaModel):
    def __init__(
        self,
        code_verification_status: str = None,
        messaging_limit_tier: str = None,
        name_status: str = None,
        new_name_status: str = None,
        phone_number: str = None,
        quality_rating: str = None,
        status: str = None,
        status_callback_url: str = None,
        status_queue: str = None,
        up_callback_url: str = None,
        up_queue: str = None,
        verified_name: str = None,
    ):
        # The verification status of the phone number.
        self.code_verification_status = code_verification_status
        # The maximum number of messages that can be sent to users by using the phone number.
        self.messaging_limit_tier = messaging_limit_tier
        # The status of the business name.
        self.name_status = name_status
        # The review status of the new business name.
        self.new_name_status = new_name_status
        # The phone number.
        self.phone_number = phone_number
        # The quality rating of the phone number. Valid values:
        # 
        # *   **GREEN**\
        # *   **YELLOW**\
        # *   **RED**\
        # *   **UNKNOWN**\
        self.quality_rating = quality_rating
        # The status of the phone number.
        # 
        # *   PENDING
        # *   DELETED
        # *   MIGRATED
        # *   BANNED
        # *   RESTRICTED
        # *   RATE_LIMITED
        # *   FLAGGED
        # *   CONNECTED
        # *   DISCONNECTED
        # *   UNKNOWN
        # *   UNVERIFIED
        self.status = status
        # The callback URL to which status reports are sent by using HTTP callbacks.
        self.status_callback_url = status_callback_url
        # The status report notification queue.
        self.status_queue = status_queue
        # The callback URL to which MO messages are sent by using HTTP callbacks.
        self.up_callback_url = up_callback_url
        # The mobile originated (MO) message notification queue.
        self.up_queue = up_queue
        # The name of the company with which the phone number is associated.
        self.verified_name = verified_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code_verification_status is not None:
            result['CodeVerificationStatus'] = self.code_verification_status
        if self.messaging_limit_tier is not None:
            result['MessagingLimitTier'] = self.messaging_limit_tier
        if self.name_status is not None:
            result['NameStatus'] = self.name_status
        if self.new_name_status is not None:
            result['NewNameStatus'] = self.new_name_status
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.quality_rating is not None:
            result['QualityRating'] = self.quality_rating
        if self.status is not None:
            result['Status'] = self.status
        if self.status_callback_url is not None:
            result['StatusCallbackUrl'] = self.status_callback_url
        if self.status_queue is not None:
            result['StatusQueue'] = self.status_queue
        if self.up_callback_url is not None:
            result['UpCallbackUrl'] = self.up_callback_url
        if self.up_queue is not None:
            result['UpQueue'] = self.up_queue
        if self.verified_name is not None:
            result['VerifiedName'] = self.verified_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CodeVerificationStatus') is not None:
            self.code_verification_status = m.get('CodeVerificationStatus')
        if m.get('MessagingLimitTier') is not None:
            self.messaging_limit_tier = m.get('MessagingLimitTier')
        if m.get('NameStatus') is not None:
            self.name_status = m.get('NameStatus')
        if m.get('NewNameStatus') is not None:
            self.new_name_status = m.get('NewNameStatus')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('QualityRating') is not None:
            self.quality_rating = m.get('QualityRating')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusCallbackUrl') is not None:
            self.status_callback_url = m.get('StatusCallbackUrl')
        if m.get('StatusQueue') is not None:
            self.status_queue = m.get('StatusQueue')
        if m.get('UpCallbackUrl') is not None:
            self.up_callback_url = m.get('UpCallbackUrl')
        if m.get('UpQueue') is not None:
            self.up_queue = m.get('UpQueue')
        if m.get('VerifiedName') is not None:
            self.verified_name = m.get('VerifiedName')
        return self


class QueryChatappPhoneNumbersResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        phone_numbers: List[QueryChatappPhoneNumbersResponseBodyPhoneNumbers] = None,
        request_id: str = None,
    ):
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](~~196974~~).
        self.code = code
        # The message returned.
        self.message = message
        # The list of phone numbers.
        self.phone_numbers = phone_numbers
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.phone_numbers:
            for k in self.phone_numbers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        result['PhoneNumbers'] = []
        if self.phone_numbers is not None:
            for k in self.phone_numbers:
                result['PhoneNumbers'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.phone_numbers = []
        if m.get('PhoneNumbers') is not None:
            for k in m.get('PhoneNumbers'):
                temp_model = QueryChatappPhoneNumbersResponseBodyPhoneNumbers()
                self.phone_numbers.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryChatappPhoneNumbersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryChatappPhoneNumbersResponseBody = None,
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
            temp_model = QueryChatappPhoneNumbersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPhoneBusinessProfileRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        phone_number: str = None,
    ):
        # The space ID of the user under the independent software vendor (ISV) account.
        self.cust_space_id = cust_space_id
        # The phone number.
        self.phone_number = phone_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        return self


class QueryPhoneBusinessProfileResponseBodyData(TeaModel):
    def __init__(
        self,
        address: str = None,
        description: str = None,
        email: str = None,
        profile_picture_url: str = None,
        vertical: str = None,
        websites: List[str] = None,
    ):
        # The address.
        self.address = address
        # The description.
        self.description = description
        # The email address.
        self.email = email
        # The URL of the profile picture.
        self.profile_picture_url = profile_picture_url
        # The industry.
        self.vertical = vertical
        # The websites.
        self.websites = websites

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.description is not None:
            result['Description'] = self.description
        if self.email is not None:
            result['Email'] = self.email
        if self.profile_picture_url is not None:
            result['ProfilePictureUrl'] = self.profile_picture_url
        if self.vertical is not None:
            result['Vertical'] = self.vertical
        if self.websites is not None:
            result['Websites'] = self.websites
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('ProfilePictureUrl') is not None:
            self.profile_picture_url = m.get('ProfilePictureUrl')
        if m.get('Vertical') is not None:
            self.vertical = m.get('Vertical')
        if m.get('Websites') is not None:
            self.websites = m.get('Websites')
        return self


class QueryPhoneBusinessProfileResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryPhoneBusinessProfileResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](~~196974~~).
        self.code = code
        # The data returned.
        self.data = data
        # The error message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

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
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = QueryPhoneBusinessProfileResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryPhoneBusinessProfileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryPhoneBusinessProfileResponseBody = None,
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
            temp_model = QueryPhoneBusinessProfileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryWabaBusinessInfoRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        waba_id: str = None,
    ):
        # The space ID of the user under the independent software vendor (ISV) account.
        self.cust_space_id = cust_space_id
        # The ID of the WABA.
        self.waba_id = waba_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.waba_id is not None:
            result['WabaId'] = self.waba_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('WabaId') is not None:
            self.waba_id = m.get('WabaId')
        return self


class QueryWabaBusinessInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        business_id: str = None,
        business_name: str = None,
        verification_status: str = None,
        vertical: str = None,
    ):
        # The ID of the business platform.
        self.business_id = business_id
        # The name of the business platform.
        self.business_name = business_name
        # The verification status.
        self.verification_status = verification_status
        # The industry.
        self.vertical = vertical

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_id is not None:
            result['BusinessId'] = self.business_id
        if self.business_name is not None:
            result['BusinessName'] = self.business_name
        if self.verification_status is not None:
            result['VerificationStatus'] = self.verification_status
        if self.vertical is not None:
            result['Vertical'] = self.vertical
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessId') is not None:
            self.business_id = m.get('BusinessId')
        if m.get('BusinessName') is not None:
            self.business_name = m.get('BusinessName')
        if m.get('VerificationStatus') is not None:
            self.verification_status = m.get('VerificationStatus')
        if m.get('Vertical') is not None:
            self.vertical = m.get('Vertical')
        return self


class QueryWabaBusinessInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryWabaBusinessInfoResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](~~196974~~).
        self.code = code
        # The business information about the WABA.
        self.data = data
        # The error message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

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
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = QueryWabaBusinessInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryWabaBusinessInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryWabaBusinessInfoResponseBody = None,
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
            temp_model = QueryWabaBusinessInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendChatappMassMessageRequestSenderList(TeaModel):
    def __init__(
        self,
        payload: List[str] = None,
        template_params: Dict[str, str] = None,
        to: str = None,
    ):
        # payload
        self.payload = payload
        # The parameters of the message template.
        self.template_params = template_params
        # The phone number that receives the message.
        self.to = to

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.payload is not None:
            result['Payload'] = self.payload
        if self.template_params is not None:
            result['TemplateParams'] = self.template_params
        if self.to is not None:
            result['To'] = self.to
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Payload') is not None:
            self.payload = m.get('Payload')
        if m.get('TemplateParams') is not None:
            self.template_params = m.get('TemplateParams')
        if m.get('To') is not None:
            self.to = m.get('To')
        return self


class SendChatappMassMessageRequest(TeaModel):
    def __init__(
        self,
        channel_type: str = None,
        cust_space_id: str = None,
        cust_waba_id: str = None,
        fall_back_content: str = None,
        fall_back_duration: int = None,
        fall_back_id: str = None,
        from_: str = None,
        isv_code: str = None,
        label: str = None,
        language: str = None,
        sender_list: List[SendChatappMassMessageRequestSenderList] = None,
        tag: str = None,
        task_id: str = None,
        template_code: str = None,
        ttl: int = None,
    ):
        # The channel type. Valid values: whatsapp, viber, and line.
        self.channel_type = channel_type
        # The space ID of the user.
        self.cust_space_id = cust_space_id
        # The ID of the WhatsApp Business account under the ISV account.
        self.cust_waba_id = cust_waba_id
        # The fallback content.
        self.fall_back_content = fall_back_content
        # 消息在指定时间内没有返回已到达回执时回落, 不填代表不根据此时间判断回落，只有发送失败和有失败的状态报告时才会回落。时间单位为秒 最小值为60，最大值43200
        self.fall_back_duration = fall_back_duration
        # The ID of the fallback strategy.
        self.fall_back_id = fall_back_id
        # The phone number of the message sender.
        self.from_ = from_
        # The ISV verification code, which is used to verify whether the user is authorized by the ISV account.
        self.isv_code = isv_code
        # The message type when the ChannelType parameter is set to viber. Valid values: promotion and transaction.
        self.label = label
        # The language. For more information about language codes, see [Language codes](~~463420~~).
        self.language = language
        # The list of phone numbers that receive the message.
        self.sender_list = sender_list
        # The tag information when the ChannelType parameter is set to viber.
        self.tag = tag
        # The ID of the task.
        self.task_id = task_id
        # The encoding of the message template.
        self.template_code = template_code
        # The timeout period for sending messages when the ChannelType parameter is set to viber. Valid values: 30 to 1209600. Unit: seconds.
        self.ttl = ttl

    def validate(self):
        if self.sender_list:
            for k in self.sender_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.cust_waba_id is not None:
            result['CustWabaId'] = self.cust_waba_id
        if self.fall_back_content is not None:
            result['FallBackContent'] = self.fall_back_content
        if self.fall_back_duration is not None:
            result['FallBackDuration'] = self.fall_back_duration
        if self.fall_back_id is not None:
            result['FallBackId'] = self.fall_back_id
        if self.from_ is not None:
            result['From'] = self.from_
        if self.isv_code is not None:
            result['IsvCode'] = self.isv_code
        if self.label is not None:
            result['Label'] = self.label
        if self.language is not None:
            result['Language'] = self.language
        result['SenderList'] = []
        if self.sender_list is not None:
            for k in self.sender_list:
                result['SenderList'].append(k.to_map() if k else None)
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('CustWabaId') is not None:
            self.cust_waba_id = m.get('CustWabaId')
        if m.get('FallBackContent') is not None:
            self.fall_back_content = m.get('FallBackContent')
        if m.get('FallBackDuration') is not None:
            self.fall_back_duration = m.get('FallBackDuration')
        if m.get('FallBackId') is not None:
            self.fall_back_id = m.get('FallBackId')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('IsvCode') is not None:
            self.isv_code = m.get('IsvCode')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        self.sender_list = []
        if m.get('SenderList') is not None:
            for k in m.get('SenderList'):
                temp_model = SendChatappMassMessageRequestSenderList()
                self.sender_list.append(temp_model.from_map(k))
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        return self


class SendChatappMassMessageShrinkRequest(TeaModel):
    def __init__(
        self,
        channel_type: str = None,
        cust_space_id: str = None,
        cust_waba_id: str = None,
        fall_back_content: str = None,
        fall_back_duration: int = None,
        fall_back_id: str = None,
        from_: str = None,
        isv_code: str = None,
        label: str = None,
        language: str = None,
        sender_list_shrink: str = None,
        tag: str = None,
        task_id: str = None,
        template_code: str = None,
        ttl: int = None,
    ):
        # The channel type. Valid values: whatsapp, viber, and line.
        self.channel_type = channel_type
        # The space ID of the user.
        self.cust_space_id = cust_space_id
        # The ID of the WhatsApp Business account under the ISV account.
        self.cust_waba_id = cust_waba_id
        # The fallback content.
        self.fall_back_content = fall_back_content
        # 消息在指定时间内没有返回已到达回执时回落, 不填代表不根据此时间判断回落，只有发送失败和有失败的状态报告时才会回落。时间单位为秒 最小值为60，最大值43200
        self.fall_back_duration = fall_back_duration
        # The ID of the fallback strategy.
        self.fall_back_id = fall_back_id
        # The phone number of the message sender.
        self.from_ = from_
        # The ISV verification code, which is used to verify whether the user is authorized by the ISV account.
        self.isv_code = isv_code
        # The message type when the ChannelType parameter is set to viber. Valid values: promotion and transaction.
        self.label = label
        # The language. For more information about language codes, see [Language codes](~~463420~~).
        self.language = language
        # The list of phone numbers that receive the message.
        self.sender_list_shrink = sender_list_shrink
        # The tag information when the ChannelType parameter is set to viber.
        self.tag = tag
        # The ID of the task.
        self.task_id = task_id
        # The encoding of the message template.
        self.template_code = template_code
        # The timeout period for sending messages when the ChannelType parameter is set to viber. Valid values: 30 to 1209600. Unit: seconds.
        self.ttl = ttl

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.cust_waba_id is not None:
            result['CustWabaId'] = self.cust_waba_id
        if self.fall_back_content is not None:
            result['FallBackContent'] = self.fall_back_content
        if self.fall_back_duration is not None:
            result['FallBackDuration'] = self.fall_back_duration
        if self.fall_back_id is not None:
            result['FallBackId'] = self.fall_back_id
        if self.from_ is not None:
            result['From'] = self.from_
        if self.isv_code is not None:
            result['IsvCode'] = self.isv_code
        if self.label is not None:
            result['Label'] = self.label
        if self.language is not None:
            result['Language'] = self.language
        if self.sender_list_shrink is not None:
            result['SenderList'] = self.sender_list_shrink
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('CustWabaId') is not None:
            self.cust_waba_id = m.get('CustWabaId')
        if m.get('FallBackContent') is not None:
            self.fall_back_content = m.get('FallBackContent')
        if m.get('FallBackDuration') is not None:
            self.fall_back_duration = m.get('FallBackDuration')
        if m.get('FallBackId') is not None:
            self.fall_back_id = m.get('FallBackId')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('IsvCode') is not None:
            self.isv_code = m.get('IsvCode')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('SenderList') is not None:
            self.sender_list_shrink = m.get('SenderList')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        return self


class SendChatappMassMessageResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        group_message_id: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](~~196974~~).
        self.code = code
        # The ID of the group of messages.
        self.group_message_id = group_message_id
        # The error message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.group_message_id is not None:
            result['GroupMessageId'] = self.group_message_id
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('GroupMessageId') is not None:
            self.group_message_id = m.get('GroupMessageId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SendChatappMassMessageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SendChatappMassMessageResponseBody = None,
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
            temp_model = SendChatappMassMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendChatappMessageRequest(TeaModel):
    def __init__(
        self,
        channel_type: str = None,
        content: str = None,
        context_message_id: str = None,
        cust_space_id: str = None,
        cust_waba_id: str = None,
        fall_back_content: str = None,
        fall_back_duration: int = None,
        fall_back_id: str = None,
        from_: str = None,
        isv_code: str = None,
        label: str = None,
        language: str = None,
        message_type: str = None,
        payload: List[str] = None,
        tag: str = None,
        task_id: str = None,
        template_code: str = None,
        template_params: Dict[str, str] = None,
        to: str = None,
        tracking_data: str = None,
        ttl: int = None,
        type: str = None,
    ):
        # The type of the message channel. Valid values:
        # 
        # *   **whatsapp**\
        # *   **viber**\
        # *   line. The feature that ChatAPP sends messages by using Line is under development.
        self.channel_type = channel_type
        # The content of the message.
        # 
        # **Usage notes when you set the ChannelType parameter to whatsapp:**\
        # 
        # *   When you set the **MessageType** parameter to **text**, the **text** parameter is required and the **caption** parameter cannot be specified.
        # *   When you set the **MessageType** parameter to **image**, the **link** parameter is required.
        # *   When you set the **MessageType** parameter to **video**, the **link** parameter is required.
        # *   When you set the **MessageType** parameter to **audio**, the **link** parameter is required and the **caption** parameter is invalid.
        # *   When you set the **MessageType** parameter to **document**, the **link** and **fileName** parameters are required and the **caption** parameter is invalid.
        # *   When you set the **MessageType** parameter to **interactive**, the **type** and **action** parameters are required.
        # *   When you set the **MessageType** parameter to **contacts**, the **name** parameter is required.
        # *   When you set the **MessageType** parameter to **location**, the **longitude** and **latitude** parameters are required.
        # *   When you set the **MessageType** parameter to **sticker**, the **link** parameter is required, and the **caption** and **fileName** parameters are invalid.
        # *   When you set the **MessageType** parameter to **reaction**, the **messageId** and **emoji** parameters are required.
        # 
        # **Usage notes when you set the ChannelType parameter to viber:**\
        # 
        # *   When you set the **MessageType** parameter to **text**, the **text** parameter is required.
        # *   When you set the **MessageType** parameter to **image**, the **link** parameter is required.
        # *   When you set the **MessageType** parameter to **video**, the **link**, **thumbnail**, **fileSize**, and **duration** parameters are required.
        # *   When you set the **MessageType** parameter to **document**, the **link**, **fileName**, and **fileType** parameters are required.
        # *   When you set the **MessageType** parameter to **text_button**, the **text**, **caption**, and **action** parameters are required.
        # *   When you set the **MessageType** parameter to **text_image_button**, the **text**, **link**, **caption**, and **action** parameters are required.
        # *   When you set the **MessageType** parameter to **text_video**, the **text**, **link**, **thumbnail**, **fileSize**, and **duration** parameters are required.
        # *   When you set the **MessageType** parameter to **text_video_button**, the **text**, **link**, **thumbnail**, **fileSize**, **duration**, and **caption** parameters are required. The **action** parameter is invalid.
        self.content = content
        # The ID of the message to reply to.
        self.context_message_id = context_message_id
        # The space ID of the user.
        self.cust_space_id = cust_space_id
        # The ID of the WhatsApp account that you register.
        self.cust_waba_id = cust_waba_id
        # The content of the fallback message.
        self.fall_back_content = fall_back_content
        # 消息在指定时间内未返回回执回落
        self.fall_back_duration = fall_back_duration
        # The ID of the fallback strategy. You can create a fallback strategy and view the information in the console.
        self.fall_back_id = fall_back_id
        # The phone number of the message sender.
        # 
        # > You can specify a mobile phone number that is registered for a WhatsApp account and is approved in the ChatAPP console.
        self.from_ = from_
        # The independent software vendor (ISV) verification code, which is used to verify whether the user is authorized by the ISV account.
        self.isv_code = isv_code
        # The type of the Viber message. This parameter is required if you set the ChannelType parameter to viber. Valid values: promotion and transaction.
        self.label = label
        # The language that is used in the message template. This parameter is required only if you set the Type parameter to **template**. For more information about language codes, see [Language codes](~~463420~~).
        self.language = language
        # The specific type of the message. This parameter is required only if you set the Type parameter to **message**.
        # 
        # **Valid values of MessageType when you set the ChannelType parameter to whatsapp:**\
        # 
        # *   **text**: a text message.
        # *   **image**: an image message.
        # *   **video**: a video message.
        # *   **audio**: an audio message.
        # *   **document**: a document message.
        # *   **interactive**: an interactive message.
        # *   **contacts**: a contact message.
        # *   **location**: a location message.
        # *   **sticker**: a sticker message.
        # *   **reaction**: a reaction message.
        # 
        # **Valid values of MessageType when you set the ChannelType parameter to viber:**\
        # 
        # *   **text**: a text message.
        # *   **image**: an image message.
        # *   **video**: a video message.
        # *   **document**: a document message.
        # *   **text_button**: a message that contains the text and button media objects.
        # *   **text_image_button**: a message that contains multiple media objects, including the text, image, and button.
        # *   **text_video**: a message that contains the text and video media objects.
        # *   **text_video_button**: a message that contains multiple media objects, including text, video, and button.
        # *   **text_image**: a message that contains the text and image media objects.
        # 
        # > For more information, see [Parameters of a message template](~~454530~~).
        self.message_type = message_type
        # The payload of the button.
        self.payload = payload
        # The tag information of the Viber message.
        self.tag = tag
        # The ID of the task.
        self.task_id = task_id
        # The code of the message template. This parameter is required only if you set the Type parameter to **template**.
        self.template_code = template_code
        # The variables of the message template.
        self.template_params = template_params
        # The phone number that receives the message.
        self.to = to
        # The tracking ID of the Viber message.
        self.tracking_data = tracking_data
        # The timeout period for sending the Viber message. Valid values: 30 to 1209600. Unit: seconds.
        self.ttl = ttl
        # The type of the message. Valid values:
        # 
        # *   **template**: a template message. A template message is sent based on a template that is created in the ChatAPP console and is approved. You can send template messages at any time based on your business requirements.
        # *   **message**: a custom message. You can send a custom message to a user only within 24 hours after you receive the last message from the user.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type
        if self.content is not None:
            result['Content'] = self.content
        if self.context_message_id is not None:
            result['ContextMessageId'] = self.context_message_id
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.cust_waba_id is not None:
            result['CustWabaId'] = self.cust_waba_id
        if self.fall_back_content is not None:
            result['FallBackContent'] = self.fall_back_content
        if self.fall_back_duration is not None:
            result['FallBackDuration'] = self.fall_back_duration
        if self.fall_back_id is not None:
            result['FallBackId'] = self.fall_back_id
        if self.from_ is not None:
            result['From'] = self.from_
        if self.isv_code is not None:
            result['IsvCode'] = self.isv_code
        if self.label is not None:
            result['Label'] = self.label
        if self.language is not None:
            result['Language'] = self.language
        if self.message_type is not None:
            result['MessageType'] = self.message_type
        if self.payload is not None:
            result['Payload'] = self.payload
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_params is not None:
            result['TemplateParams'] = self.template_params
        if self.to is not None:
            result['To'] = self.to
        if self.tracking_data is not None:
            result['TrackingData'] = self.tracking_data
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ContextMessageId') is not None:
            self.context_message_id = m.get('ContextMessageId')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('CustWabaId') is not None:
            self.cust_waba_id = m.get('CustWabaId')
        if m.get('FallBackContent') is not None:
            self.fall_back_content = m.get('FallBackContent')
        if m.get('FallBackDuration') is not None:
            self.fall_back_duration = m.get('FallBackDuration')
        if m.get('FallBackId') is not None:
            self.fall_back_id = m.get('FallBackId')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('IsvCode') is not None:
            self.isv_code = m.get('IsvCode')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('MessageType') is not None:
            self.message_type = m.get('MessageType')
        if m.get('Payload') is not None:
            self.payload = m.get('Payload')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateParams') is not None:
            self.template_params = m.get('TemplateParams')
        if m.get('To') is not None:
            self.to = m.get('To')
        if m.get('TrackingData') is not None:
            self.tracking_data = m.get('TrackingData')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class SendChatappMessageShrinkRequest(TeaModel):
    def __init__(
        self,
        channel_type: str = None,
        content: str = None,
        context_message_id: str = None,
        cust_space_id: str = None,
        cust_waba_id: str = None,
        fall_back_content: str = None,
        fall_back_duration: int = None,
        fall_back_id: str = None,
        from_: str = None,
        isv_code: str = None,
        label: str = None,
        language: str = None,
        message_type: str = None,
        payload_shrink: str = None,
        tag: str = None,
        task_id: str = None,
        template_code: str = None,
        template_params_shrink: str = None,
        to: str = None,
        tracking_data: str = None,
        ttl: int = None,
        type: str = None,
    ):
        # The type of the message channel. Valid values:
        # 
        # *   **whatsapp**\
        # *   **viber**\
        # *   line. The feature that ChatAPP sends messages by using Line is under development.
        self.channel_type = channel_type
        # The content of the message.
        # 
        # **Usage notes when you set the ChannelType parameter to whatsapp:**\
        # 
        # *   When you set the **MessageType** parameter to **text**, the **text** parameter is required and the **caption** parameter cannot be specified.
        # *   When you set the **MessageType** parameter to **image**, the **link** parameter is required.
        # *   When you set the **MessageType** parameter to **video**, the **link** parameter is required.
        # *   When you set the **MessageType** parameter to **audio**, the **link** parameter is required and the **caption** parameter is invalid.
        # *   When you set the **MessageType** parameter to **document**, the **link** and **fileName** parameters are required and the **caption** parameter is invalid.
        # *   When you set the **MessageType** parameter to **interactive**, the **type** and **action** parameters are required.
        # *   When you set the **MessageType** parameter to **contacts**, the **name** parameter is required.
        # *   When you set the **MessageType** parameter to **location**, the **longitude** and **latitude** parameters are required.
        # *   When you set the **MessageType** parameter to **sticker**, the **link** parameter is required, and the **caption** and **fileName** parameters are invalid.
        # *   When you set the **MessageType** parameter to **reaction**, the **messageId** and **emoji** parameters are required.
        # 
        # **Usage notes when you set the ChannelType parameter to viber:**\
        # 
        # *   When you set the **MessageType** parameter to **text**, the **text** parameter is required.
        # *   When you set the **MessageType** parameter to **image**, the **link** parameter is required.
        # *   When you set the **MessageType** parameter to **video**, the **link**, **thumbnail**, **fileSize**, and **duration** parameters are required.
        # *   When you set the **MessageType** parameter to **document**, the **link**, **fileName**, and **fileType** parameters are required.
        # *   When you set the **MessageType** parameter to **text_button**, the **text**, **caption**, and **action** parameters are required.
        # *   When you set the **MessageType** parameter to **text_image_button**, the **text**, **link**, **caption**, and **action** parameters are required.
        # *   When you set the **MessageType** parameter to **text_video**, the **text**, **link**, **thumbnail**, **fileSize**, and **duration** parameters are required.
        # *   When you set the **MessageType** parameter to **text_video_button**, the **text**, **link**, **thumbnail**, **fileSize**, **duration**, and **caption** parameters are required. The **action** parameter is invalid.
        self.content = content
        # The ID of the message to reply to.
        self.context_message_id = context_message_id
        # The space ID of the user.
        self.cust_space_id = cust_space_id
        # The ID of the WhatsApp account that you register.
        self.cust_waba_id = cust_waba_id
        # The content of the fallback message.
        self.fall_back_content = fall_back_content
        # 消息在指定时间内未返回回执回落
        self.fall_back_duration = fall_back_duration
        # The ID of the fallback strategy. You can create a fallback strategy and view the information in the console.
        self.fall_back_id = fall_back_id
        # The phone number of the message sender.
        # 
        # > You can specify a mobile phone number that is registered for a WhatsApp account and is approved in the ChatAPP console.
        self.from_ = from_
        # The independent software vendor (ISV) verification code, which is used to verify whether the user is authorized by the ISV account.
        self.isv_code = isv_code
        # The type of the Viber message. This parameter is required if you set the ChannelType parameter to viber. Valid values: promotion and transaction.
        self.label = label
        # The language that is used in the message template. This parameter is required only if you set the Type parameter to **template**. For more information about language codes, see [Language codes](~~463420~~).
        self.language = language
        # The specific type of the message. This parameter is required only if you set the Type parameter to **message**.
        # 
        # **Valid values of MessageType when you set the ChannelType parameter to whatsapp:**\
        # 
        # *   **text**: a text message.
        # *   **image**: an image message.
        # *   **video**: a video message.
        # *   **audio**: an audio message.
        # *   **document**: a document message.
        # *   **interactive**: an interactive message.
        # *   **contacts**: a contact message.
        # *   **location**: a location message.
        # *   **sticker**: a sticker message.
        # *   **reaction**: a reaction message.
        # 
        # **Valid values of MessageType when you set the ChannelType parameter to viber:**\
        # 
        # *   **text**: a text message.
        # *   **image**: an image message.
        # *   **video**: a video message.
        # *   **document**: a document message.
        # *   **text_button**: a message that contains the text and button media objects.
        # *   **text_image_button**: a message that contains multiple media objects, including the text, image, and button.
        # *   **text_video**: a message that contains the text and video media objects.
        # *   **text_video_button**: a message that contains multiple media objects, including text, video, and button.
        # *   **text_image**: a message that contains the text and image media objects.
        # 
        # > For more information, see [Parameters of a message template](~~454530~~).
        self.message_type = message_type
        # The payload of the button.
        self.payload_shrink = payload_shrink
        # The tag information of the Viber message.
        self.tag = tag
        # The ID of the task.
        self.task_id = task_id
        # The code of the message template. This parameter is required only if you set the Type parameter to **template**.
        self.template_code = template_code
        # The variables of the message template.
        self.template_params_shrink = template_params_shrink
        # The phone number that receives the message.
        self.to = to
        # The tracking ID of the Viber message.
        self.tracking_data = tracking_data
        # The timeout period for sending the Viber message. Valid values: 30 to 1209600. Unit: seconds.
        self.ttl = ttl
        # The type of the message. Valid values:
        # 
        # *   **template**: a template message. A template message is sent based on a template that is created in the ChatAPP console and is approved. You can send template messages at any time based on your business requirements.
        # *   **message**: a custom message. You can send a custom message to a user only within 24 hours after you receive the last message from the user.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type
        if self.content is not None:
            result['Content'] = self.content
        if self.context_message_id is not None:
            result['ContextMessageId'] = self.context_message_id
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.cust_waba_id is not None:
            result['CustWabaId'] = self.cust_waba_id
        if self.fall_back_content is not None:
            result['FallBackContent'] = self.fall_back_content
        if self.fall_back_duration is not None:
            result['FallBackDuration'] = self.fall_back_duration
        if self.fall_back_id is not None:
            result['FallBackId'] = self.fall_back_id
        if self.from_ is not None:
            result['From'] = self.from_
        if self.isv_code is not None:
            result['IsvCode'] = self.isv_code
        if self.label is not None:
            result['Label'] = self.label
        if self.language is not None:
            result['Language'] = self.language
        if self.message_type is not None:
            result['MessageType'] = self.message_type
        if self.payload_shrink is not None:
            result['Payload'] = self.payload_shrink
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_params_shrink is not None:
            result['TemplateParams'] = self.template_params_shrink
        if self.to is not None:
            result['To'] = self.to
        if self.tracking_data is not None:
            result['TrackingData'] = self.tracking_data
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ContextMessageId') is not None:
            self.context_message_id = m.get('ContextMessageId')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('CustWabaId') is not None:
            self.cust_waba_id = m.get('CustWabaId')
        if m.get('FallBackContent') is not None:
            self.fall_back_content = m.get('FallBackContent')
        if m.get('FallBackDuration') is not None:
            self.fall_back_duration = m.get('FallBackDuration')
        if m.get('FallBackId') is not None:
            self.fall_back_id = m.get('FallBackId')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('IsvCode') is not None:
            self.isv_code = m.get('IsvCode')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('MessageType') is not None:
            self.message_type = m.get('MessageType')
        if m.get('Payload') is not None:
            self.payload_shrink = m.get('Payload')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateParams') is not None:
            self.template_params_shrink = m.get('TemplateParams')
        if m.get('To') is not None:
            self.to = m.get('To')
        if m.get('TrackingData') is not None:
            self.tracking_data = m.get('TrackingData')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class SendChatappMessageResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        message_id: str = None,
        request_id: str = None,
    ):
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](~~196974~~).
        self.code = code
        # The error message returned.
        self.message = message
        # The ID of the message that was sent.
        self.message_id = message_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SendChatappMessageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SendChatappMessageResponseBody = None,
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
            temp_model = SendChatappMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitIsvCustomerTermsRequest(TeaModel):
    def __init__(
        self,
        business_desc: str = None,
        contact_mail: str = None,
        country_id: str = None,
        cust_name: str = None,
        cust_space_id: str = None,
        isv_terms: str = None,
        office_address: str = None,
    ):
        # The use scenario.
        self.business_desc = business_desc
        # The email address of your business.
        self.contact_mail = contact_mail
        # The country code.
        self.country_id = country_id
        # The display name of your business.
        self.cust_name = cust_name
        # The space ID of the user under the ISV account.
        self.cust_space_id = cust_space_id
        # The ISV or Client Agreement.
        # 
        # > Before you upload files to Object Storage Service (OSS) servers, you must call the GetChatappUploadAuthorization operation to obtain the authentication information required to upload files. You can use the SDK provided by OSS to upload files. When you upload a file, you must set the key parameter value. To set the value for the key parameter, concatenate the value of the Dir parameter and the file name by using a forward slash (/). You can obtain the value of the Dir parameter by calling the GetChatappUploadAuthorization operation.
        # 
        # > The value of this parameter is the name of the uploaded file.
        self.isv_terms = isv_terms
        # The address of your business.
        self.office_address = office_address

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_desc is not None:
            result['BusinessDesc'] = self.business_desc
        if self.contact_mail is not None:
            result['ContactMail'] = self.contact_mail
        if self.country_id is not None:
            result['CountryId'] = self.country_id
        if self.cust_name is not None:
            result['CustName'] = self.cust_name
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.isv_terms is not None:
            result['IsvTerms'] = self.isv_terms
        if self.office_address is not None:
            result['OfficeAddress'] = self.office_address
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessDesc') is not None:
            self.business_desc = m.get('BusinessDesc')
        if m.get('ContactMail') is not None:
            self.contact_mail = m.get('ContactMail')
        if m.get('CountryId') is not None:
            self.country_id = m.get('CountryId')
        if m.get('CustName') is not None:
            self.cust_name = m.get('CustName')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('IsvTerms') is not None:
            self.isv_terms = m.get('IsvTerms')
        if m.get('OfficeAddress') is not None:
            self.office_address = m.get('OfficeAddress')
        return self


class SubmitIsvCustomerTermsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](~~196974~~).
        self.code = code
        # The error message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitIsvCustomerTermsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitIsvCustomerTermsResponseBody = None,
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
            temp_model = SubmitIsvCustomerTermsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAccountWebhookRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        http_flag: str = None,
        queue_flag: str = None,
        status_callback_url: str = None,
    ):
        # The space ID of the user under the ISV account.
        self.cust_space_id = cust_space_id
        # Specifies whether to use HTTP callbacks to receive message receipts. Valid values:
        # 
        # *   Y: indicates that HTTP callbacks are used to receive receipts.
        # *   N: indicates that HTTP callbacks are not used to receive receipts.
        self.http_flag = http_flag
        # Specifies whether to use Message Service (MNS) queues to receive receipts. Valid values:
        # 
        # *   Y: indicates that MNS queues are used to receive receipts.
        # *   N: indicates that MNS queues are not used to receive receipts.
        self.queue_flag = queue_flag
        # The callback URL to which status reports are sent by using HTTP callbacks.
        self.status_callback_url = status_callback_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.http_flag is not None:
            result['HttpFlag'] = self.http_flag
        if self.queue_flag is not None:
            result['QueueFlag'] = self.queue_flag
        if self.status_callback_url is not None:
            result['StatusCallbackUrl'] = self.status_callback_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('HttpFlag') is not None:
            self.http_flag = m.get('HttpFlag')
        if m.get('QueueFlag') is not None:
            self.queue_flag = m.get('QueueFlag')
        if m.get('StatusCallbackUrl') is not None:
            self.status_callback_url = m.get('StatusCallbackUrl')
        return self


class UpdateAccountWebhookResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](~~196974~~).
        self.code = code
        # The error message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateAccountWebhookResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateAccountWebhookResponseBody = None,
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
            temp_model = UpdateAccountWebhookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePhoneWebhookRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        http_flag: str = None,
        phone_number: str = None,
        queue_flag: str = None,
        status_callback_url: str = None,
        up_callback_url: str = None,
    ):
        self.cust_space_id = cust_space_id
        self.http_flag = http_flag
        self.phone_number = phone_number
        self.queue_flag = queue_flag
        self.status_callback_url = status_callback_url
        self.up_callback_url = up_callback_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.http_flag is not None:
            result['HttpFlag'] = self.http_flag
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.queue_flag is not None:
            result['QueueFlag'] = self.queue_flag
        if self.status_callback_url is not None:
            result['StatusCallbackUrl'] = self.status_callback_url
        if self.up_callback_url is not None:
            result['UpCallbackUrl'] = self.up_callback_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('HttpFlag') is not None:
            self.http_flag = m.get('HttpFlag')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('QueueFlag') is not None:
            self.queue_flag = m.get('QueueFlag')
        if m.get('StatusCallbackUrl') is not None:
            self.status_callback_url = m.get('StatusCallbackUrl')
        if m.get('UpCallbackUrl') is not None:
            self.up_callback_url = m.get('UpCallbackUrl')
        return self


class UpdatePhoneWebhookResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdatePhoneWebhookResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdatePhoneWebhookResponseBody = None,
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
            temp_model = UpdatePhoneWebhookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


