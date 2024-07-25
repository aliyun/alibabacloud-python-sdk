# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class AddChatappPhoneNumberRequest(TeaModel):
    def __init__(
        self,
        cc: str = None,
        cust_space_id: str = None,
        owner_id: int = None,
        phone_number: str = None,
        pre_validate_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        verified_name: str = None,
    ):
        # This parameter is required.
        self.cc = cc
        # This parameter is required.
        self.cust_space_id = cust_space_id
        self.owner_id = owner_id
        # This parameter is required.
        self.phone_number = phone_number
        self.pre_validate_id = pre_validate_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # This parameter is required.
        self.verified_name = verified_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cc is not None:
            result['Cc'] = self.cc
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.pre_validate_id is not None:
            result['PreValidateId'] = self.pre_validate_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.verified_name is not None:
            result['VerifiedName'] = self.verified_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cc') is not None:
            self.cc = m.get('Cc')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('PreValidateId') is not None:
            self.pre_validate_id = m.get('PreValidateId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('VerifiedName') is not None:
            self.verified_name = m.get('VerifiedName')
        return self


class AddChatappPhoneNumberResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   Other values indicate that the request failed. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddChatappPhoneNumberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddChatappPhoneNumberResponseBody = None,
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
            temp_model = AddChatappPhoneNumberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


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
        # 
        # This parameter is required.
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
        # 
        # This parameter is required.
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
        access_denied_detail: str = None,
        code: str = None,
        data: BeeBotAssociateResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
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
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
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
        # 
        # This parameter is required.
        self.chat_bot_instance_id = chat_bot_instance_id
        self.cust_space_id = cust_space_id
        # The name of the intent in the dialog flow. When this parameter is specified, the bot conducts a Q\\&A based on the intent.
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
        # 
        # This parameter is required.
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
        # 
        # This parameter is required.
        self.chat_bot_instance_id = chat_bot_instance_id
        self.cust_space_id = cust_space_id
        # The name of the intent in the dialog flow. When this parameter is specified, the bot conducts a Q\\&A based on the intent.
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
        # 
        # This parameter is required.
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
        access_denied_detail: str = None,
        code: str = None,
        data: BeeBotChatResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
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
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
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
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        waba_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # This parameter is required.
        self.waba_id = waba_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.waba_id is not None:
            result['WabaId'] = self.waba_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
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
        access_denied_detail: str = None,
        code: str = None,
        data: ChatappBindWabaResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        # The data returned.
        self.data = data
        # The error message returned.
        self.message = message
        # The ID of the request.
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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
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
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ChatappBindWabaResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
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
        # 
        # This parameter is required.
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
        # The review state of the WABA.
        self.account_review_status = account_review_status
        # The currency.
        self.currency = currency
        # The ID of the WABA.
        self.id = id
        # The namespace of the message template.
        self.message_template_namespace = message_template_namespace
        # The name of the WABA.
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
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        wabas: List[ChatappEmbedSignUpResponseBodyWabas] = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
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
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
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
        # 
        # This parameter is required.
        self.cust_space_id = cust_space_id
        # The phone number.
        # 
        # This parameter is required.
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
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
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
        # 
        # This parameter is required.
        self.cust_space_id = cust_space_id
        # The phone number.
        # 
        # This parameter is required.
        self.phone_number = phone_number
        # The verification code.
        # 
        # This parameter is required.
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
        access_denied_detail: str = None,
        code: str = None,
        data: ChatappMigrationVerifiedResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
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
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
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


class ChatappPhoneNumberDeregisterRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        phone_number: str = None,
    ):
        # The space ID of the user within the independent software vendor (ISV) account.
        # 
        # This parameter is required.
        self.cust_space_id = cust_space_id
        # The phone number.
        # 
        # This parameter is required.
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


class ChatappPhoneNumberDeregisterResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   Other values indicate that the request failed. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ChatappPhoneNumberDeregisterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ChatappPhoneNumberDeregisterResponseBody = None,
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
            temp_model = ChatappPhoneNumberDeregisterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChatappPhoneNumberRegisterRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        owner_id: int = None,
        phone_number: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # This parameter is required.
        self.cust_space_id = cust_space_id
        self.owner_id = owner_id
        # This parameter is required.
        self.phone_number = phone_number
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ChatappPhoneNumberRegisterResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        # The error message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
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
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The space ID of the user under the independent software vendor (ISV) account.
        # 
        # This parameter is required.
        self.cust_space_id = cust_space_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
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
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        phone_numbers: List[ChatappSyncPhoneNumberResponseBodyPhoneNumbers] = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        # The error message returned.
        self.message = message
        # Details of the phone numbers.
        self.phone_numbers = phone_numbers
        # The ID of the request.
        self.request_id = request_id
        self.success = success

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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
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
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
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
        if m.get('Success') is not None:
            self.success = m.get('Success')
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
        owner_id: int = None,
        phone_number: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        verify_code: str = None,
    ):
        # This parameter is required.
        self.cust_space_id = cust_space_id
        self.owner_id = owner_id
        # This parameter is required.
        self.phone_number = phone_number
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # This parameter is required.
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
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.verify_code is not None:
            result['VerifyCode'] = self.verify_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('VerifyCode') is not None:
            self.verify_code = m.get('VerifyCode')
        return self


class ChatappVerifyAndRegisterResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        # The error message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
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
        # This parameter is required.
        self.country_code = country_code
        # This parameter is required.
        self.cust_space_id = cust_space_id
        # This parameter is required.
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
        access_denied_detail: str = None,
        code: str = None,
        data: CreateChatappMigrationInitiateResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
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
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
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


class CreateChatappTemplateRequestComponentsButtonsSupportedApps(TeaModel):
    def __init__(
        self,
        package_name: str = None,
        signature_hash: str = None,
    ):
        self.package_name = package_name
        self.signature_hash = signature_hash

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.package_name is not None:
            result['PackageName'] = self.package_name
        if self.signature_hash is not None:
            result['SignatureHash'] = self.signature_hash
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PackageName') is not None:
            self.package_name = m.get('PackageName')
        if m.get('SignatureHash') is not None:
            self.signature_hash = m.get('SignatureHash')
        return self


class CreateChatappTemplateRequestComponentsButtons(TeaModel):
    def __init__(
        self,
        autofill_text: str = None,
        coupon_code: str = None,
        flow_action: str = None,
        flow_id: str = None,
        is_opt_out: bool = None,
        navigate_screen: str = None,
        package_name: str = None,
        phone_number: str = None,
        signature_hash: str = None,
        supported_apps: List[CreateChatappTemplateRequestComponentsButtonsSupportedApps] = None,
        text: str = None,
        type: str = None,
        url: str = None,
        url_type: str = None,
    ):
        # The text of the one-tap autofill button. This parameter is required if Category is set to AUTHENTICATION and the Type sub-parameter of the Buttons parameter is set to ONE_TAP for a WhatsApp message template.
        self.autofill_text = autofill_text
        self.coupon_code = coupon_code
        self.flow_action = flow_action
        self.flow_id = flow_id
        # The unsubscribe button. This parameter is valid if Category is set to MARKETING and the Type sub-parameter of the Buttons parameter is set to QUICK_REPLY for a WhatsApp message template. After you configure message sending in the ChatApp Message Service console, marketing messages are not sent to customers if they click this button.
        self.is_opt_out = is_opt_out
        self.navigate_screen = navigate_screen
        # The app package name that WhatsApp uses to load your app. This parameter is required if Category is set to AUTHENTICATION and the Type sub-parameter of the Buttons parameter is set to ONE_TAP for a WhatsApp message template.
        self.package_name = package_name
        # The phone number. This parameter is valid only if the Type sub-parameter of the Buttons parameter is set to **PHONE_NUMBER**.
        self.phone_number = phone_number
        # The app signing key hash that WhatsApp uses to load your app. This parameter is required if Category is set to AUTHENTICATION and the Type sub-parameter of the Buttons parameter is set to ONE_TAP for a WhatsApp message template.
        self.signature_hash = signature_hash
        self.supported_apps = supported_apps
        # The display name of the button.
        self.text = text
        # The type of the button. Valid values:
        # 
        # *   **PHONE_NUMBER**: phone call button
        # *   **URL**: URL button
        # *   **QUICK_REPLY**: quick reply button
        # *   **COPY_CODE**: copy code button if Category is set to AUTHENTICATION
        # *   **ONE_TAP**: one-tap autofill button if Category is set to AUTHENTICATION
        # 
        # > 
        # 
        # *   In a WhatsApp message template, a quick reply button cannot be used together with a phone call button or a URL button.
        # 
        # *   You can add a combination of two URL buttons or a combination of a URL button and a phone call button to a WhatsApp message template.
        # 
        # *   If Category is set to AUTHENTICATION for a WhatsApp message template, you can add only one button to the WhatsApp message template and you must set the Type sub-parameter of the Buttons parameter to COPY_CODE or ONE_TAP. If the Type sub-parameter of the Buttons parameter is set to COPY_CODE, the Text sub-parameter of the Buttons parameter is required. If the Type sub-parameter of the Buttons parameter is set to ONE_TAP, the Text, SignatureHash, PackageName, and AutofillText sub-parameters of the Buttons parameter are required. The value of Text is displayed if the desired app is not installed on the device. The value of Text indicates that you must manually copy the verification code.
        # 
        # *   You can add only one button to a Viber message template, and you must set the Type sub-parameter of the Buttons parameter to URL.
        # 
        # This parameter is required.
        self.type = type
        # The URL to which you are redirected when you click the URL button.
        self.url = url
        # The type of the URL. Valid values:
        # 
        # *   **static**\
        # *   **dynamic**\
        self.url_type = url_type

    def validate(self):
        if self.supported_apps:
            for k in self.supported_apps:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.autofill_text is not None:
            result['AutofillText'] = self.autofill_text
        if self.coupon_code is not None:
            result['CouponCode'] = self.coupon_code
        if self.flow_action is not None:
            result['FlowAction'] = self.flow_action
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.is_opt_out is not None:
            result['IsOptOut'] = self.is_opt_out
        if self.navigate_screen is not None:
            result['NavigateScreen'] = self.navigate_screen
        if self.package_name is not None:
            result['PackageName'] = self.package_name
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.signature_hash is not None:
            result['SignatureHash'] = self.signature_hash
        result['SupportedApps'] = []
        if self.supported_apps is not None:
            for k in self.supported_apps:
                result['SupportedApps'].append(k.to_map() if k else None)
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
        if m.get('CouponCode') is not None:
            self.coupon_code = m.get('CouponCode')
        if m.get('FlowAction') is not None:
            self.flow_action = m.get('FlowAction')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('IsOptOut') is not None:
            self.is_opt_out = m.get('IsOptOut')
        if m.get('NavigateScreen') is not None:
            self.navigate_screen = m.get('NavigateScreen')
        if m.get('PackageName') is not None:
            self.package_name = m.get('PackageName')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('SignatureHash') is not None:
            self.signature_hash = m.get('SignatureHash')
        self.supported_apps = []
        if m.get('SupportedApps') is not None:
            for k in m.get('SupportedApps'):
                temp_model = CreateChatappTemplateRequestComponentsButtonsSupportedApps()
                self.supported_apps.append(temp_model.from_map(k))
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('UrlType') is not None:
            self.url_type = m.get('UrlType')
        return self


class CreateChatappTemplateRequestComponentsCardsCardComponentsButtons(TeaModel):
    def __init__(
        self,
        phone_number: str = None,
        text: str = None,
        type: str = None,
        url: str = None,
        url_type: str = None,
    ):
        self.phone_number = phone_number
        self.text = text
        # This parameter is required.
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
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
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
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('UrlType') is not None:
            self.url_type = m.get('UrlType')
        return self


class CreateChatappTemplateRequestComponentsCardsCardComponents(TeaModel):
    def __init__(
        self,
        buttons: List[CreateChatappTemplateRequestComponentsCardsCardComponentsButtons] = None,
        format: str = None,
        text: str = None,
        type: str = None,
        url: str = None,
    ):
        self.buttons = buttons
        self.format = format
        self.text = text
        # This parameter is required.
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
        result['Buttons'] = []
        if self.buttons is not None:
            for k in self.buttons:
                result['Buttons'].append(k.to_map() if k else None)
        if self.format is not None:
            result['Format'] = self.format
        if self.text is not None:
            result['Text'] = self.text
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.buttons = []
        if m.get('Buttons') is not None:
            for k in m.get('Buttons'):
                temp_model = CreateChatappTemplateRequestComponentsCardsCardComponentsButtons()
                self.buttons.append(temp_model.from_map(k))
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class CreateChatappTemplateRequestComponentsCards(TeaModel):
    def __init__(
        self,
        card_components: List[CreateChatappTemplateRequestComponentsCardsCardComponents] = None,
    ):
        # This parameter is required.
        self.card_components = card_components

    def validate(self):
        if self.card_components:
            for k in self.card_components:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CardComponents'] = []
        if self.card_components is not None:
            for k in self.card_components:
                result['CardComponents'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.card_components = []
        if m.get('CardComponents') is not None:
            for k in m.get('CardComponents'):
                temp_model = CreateChatappTemplateRequestComponentsCardsCardComponents()
                self.card_components.append(temp_model.from_map(k))
        return self


class CreateChatappTemplateRequestComponents(TeaModel):
    def __init__(
        self,
        add_secret_recommendation: bool = None,
        buttons: List[CreateChatappTemplateRequestComponentsButtons] = None,
        caption: str = None,
        cards: List[CreateChatappTemplateRequestComponentsCards] = None,
        code_expiration_minutes: int = None,
        duration: int = None,
        file_name: str = None,
        file_type: str = None,
        format: str = None,
        has_expiration: bool = None,
        text: str = None,
        thumb_url: str = None,
        type: str = None,
        url: str = None,
    ):
        # The note indicating that customers cannot share verification codes with others. The note is displayed in the message body. This parameter is valid only if Category is set to AUTHENTICATION and the Type sub-parameter of the Components parameter is set to BODY for a WhatsApp message template.
        self.add_secret_recommendation = add_secret_recommendation
        # The buttons. Specify this parameter only if you set the Type sub-parameter of the Components parameter to **BUTTONS**.
        # 
        # >  The following section describes the limits on the number of buttons in a WhatsApp message.
        # 
        # *   A marketing or utility WhatsApp message template supports up to 10 buttons.
        # 
        # *   A WhatsApp message template can contain only one phone call button.
        # 
        # *   A WhatsApp message template can contain up to two URL buttons.
        # 
        # *   In a WhatsApp message template, the quick reply button cannot be used together with the phone call button or the URL button.
        self.buttons = buttons
        # The description of the document.
        self.caption = caption
        self.cards = cards
        # The validity period of the verification code in the WhatsApp authentication template. Unit: minutes. This parameter is valid only when Category is set to AUTHENTICATION and the Type sub-parameter of the Components parameter is set to FOOTER in a WhatsApp message template. The validity period of the verification code is displayed in the footer.
        self.code_expiration_minutes = code_expiration_minutes
        # The length of the video in the Viber message template. Unit: seconds. Valid values: 0 to 600.
        self.duration = duration
        # The name of the document.
        self.file_name = file_name
        # The type of the document attached in the Viber message template.
        self.file_type = file_type
        # The type of the media resources that are included in the message. Valid values:
        # 
        # *   **TEXT**\
        # *   **IMAGE**\
        # *   **DOCUMENT**\
        # *   **VIDEO**\
        self.format = format
        self.has_expiration = has_expiration
        # The text of the message that you want to send.
        # 
        # >  If Category is set to AUTHENTICATION, the Text sub-parameter of the Components parameter is empty.
        self.text = text
        # The thumbnail URL of the video in the Viber message template.
        self.thumb_url = thumb_url
        # The type of the component. Valid values:
        # 
        # *   **BODY**\
        # *   **HEADER**\
        # *   **FOOTER**\
        # *   **BUTTONS**\
        # 
        # > 
        # 
        # *   In WhatsApp message templates, a **BODY** component cannot exceed 1,024 characters in length, and a **HEADER** or **FOOTER** component cannot exceed 60 characters in length.
        # 
        # *   **FOOTER** components are not supported in Viber message templates.
        # 
        # *   In Viber message templates, media resources such as images, videos, and documents are placed in the **HEADER** component. If a Viber message contains both text and an image, the image is placed below the text in the message received on a device.
        # 
        # This parameter is required.
        self.type = type
        # The URL of the media resource.
        # 
        # >  We recommend that you use 800 × 800 images in Viber message templates.
        self.url = url

    def validate(self):
        if self.buttons:
            for k in self.buttons:
                if k:
                    k.validate()
        if self.cards:
            for k in self.cards:
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
        result['Cards'] = []
        if self.cards is not None:
            for k in self.cards:
                result['Cards'].append(k.to_map() if k else None)
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
        if self.has_expiration is not None:
            result['HasExpiration'] = self.has_expiration
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
        self.cards = []
        if m.get('Cards') is not None:
            for k in m.get('Cards'):
                temp_model = CreateChatappTemplateRequestComponentsCards()
                self.cards.append(temp_model.from_map(k))
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
        if m.get('HasExpiration') is not None:
            self.has_expiration = m.get('HasExpiration')
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
        message_send_ttl_seconds: int = None,
        name: str = None,
        template_type: str = None,
    ):
        # Specifies whether to allow Facebook to automatically change the directory of the template. If you set this parameter to true, the review success rate of the template is improved. This parameter is valid only when TemplateType is set to WHATSAPP.
        self.allow_category_change = allow_category_change
        # The category of the template if TemplateType is set to WHATSAPP. Valid values:
        # 
        # *   **UTILITY**: the transaction template
        # *   **MARKETING**: the marketing template
        # *   **AUTHENTICATION**: the authentication template
        # 
        # The category of the template if TemplateType is set to VIBER. Valid values:
        # 
        # *   **text**: the template that contains only text
        # *   **image**: the template that contains only images
        # *   **text_image_button**: the template that contains text, images, and buttons
        # *   **text_button**: the template that contains text and buttons
        # *   **document**: the template that contains only documents
        # *   **video**: the template that contains only videos
        # *   **text_video**: the template that contains text and videos
        # *   **text_video_button**: the template that contains text, videos, and buttons
        # *   **text_image**: the template that contains text and images
        # 
        # This parameter is required.
        self.category = category
        # The components of the message template.
        # 
        # >  If Category is set to AUTHENTICATION, the Type sub-parameter of the Components parameter cannot be set to HEADER. If the Type sub-parameter is set to BODY or FOOTER, the Text sub-parameter of the Components parameter must be empty.
        # 
        # This parameter is required.
        self.components = components
        # The space ID of the user within the ISV account.
        self.cust_space_id = cust_space_id
        # The WhatsApp Business account (WABA) ID of the user within the independent software vendor (ISV) account.
        # 
        # > CustWabaId is an obsolete parameter. Use CustSpaceId instead.
        self.cust_waba_id = cust_waba_id
        # The examples of variables that are used when you create the message template.
        self.example = example
        # The independent software vendor (ISV) verification code, which is used to verify whether the user is authorized by the ISV account.
        self.isv_code = isv_code
        # The language that is used in the message template. For more information, see [Language codes](https://help.aliyun.com/document_detail/463420.html).
        # 
        # This parameter is required.
        self.language = language
        # Validity period of authentication template message sending in WhatsApp
        # 
        # > This attribute requires providing waba in advance to Alibaba operators to open the whitelist, otherwise it will result in template submission failure
        self.message_send_ttl_seconds = message_send_ttl_seconds
        # The name of the message template.
        # 
        # This parameter is required.
        self.name = name
        # The type of the message template.
        # 
        # *   **WHATSAPP**\
        # *   **VIBER**\
        # *   LINE: the Line message template. This type of message template will be released later.
        # 
        # This parameter is required.
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
        if self.message_send_ttl_seconds is not None:
            result['MessageSendTtlSeconds'] = self.message_send_ttl_seconds
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
        if m.get('MessageSendTtlSeconds') is not None:
            self.message_send_ttl_seconds = m.get('MessageSendTtlSeconds')
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
        message_send_ttl_seconds: int = None,
        name: str = None,
        template_type: str = None,
    ):
        # Specifies whether to allow Facebook to automatically change the directory of the template. If you set this parameter to true, the review success rate of the template is improved. This parameter is valid only when TemplateType is set to WHATSAPP.
        self.allow_category_change = allow_category_change
        # The category of the template if TemplateType is set to WHATSAPP. Valid values:
        # 
        # *   **UTILITY**: the transaction template
        # *   **MARKETING**: the marketing template
        # *   **AUTHENTICATION**: the authentication template
        # 
        # The category of the template if TemplateType is set to VIBER. Valid values:
        # 
        # *   **text**: the template that contains only text
        # *   **image**: the template that contains only images
        # *   **text_image_button**: the template that contains text, images, and buttons
        # *   **text_button**: the template that contains text and buttons
        # *   **document**: the template that contains only documents
        # *   **video**: the template that contains only videos
        # *   **text_video**: the template that contains text and videos
        # *   **text_video_button**: the template that contains text, videos, and buttons
        # *   **text_image**: the template that contains text and images
        # 
        # This parameter is required.
        self.category = category
        # The components of the message template.
        # 
        # >  If Category is set to AUTHENTICATION, the Type sub-parameter of the Components parameter cannot be set to HEADER. If the Type sub-parameter is set to BODY or FOOTER, the Text sub-parameter of the Components parameter must be empty.
        # 
        # This parameter is required.
        self.components_shrink = components_shrink
        # The space ID of the user within the ISV account.
        self.cust_space_id = cust_space_id
        # The WhatsApp Business account (WABA) ID of the user within the independent software vendor (ISV) account.
        # 
        # > CustWabaId is an obsolete parameter. Use CustSpaceId instead.
        self.cust_waba_id = cust_waba_id
        # The examples of variables that are used when you create the message template.
        self.example_shrink = example_shrink
        # The independent software vendor (ISV) verification code, which is used to verify whether the user is authorized by the ISV account.
        self.isv_code = isv_code
        # The language that is used in the message template. For more information, see [Language codes](https://help.aliyun.com/document_detail/463420.html).
        # 
        # This parameter is required.
        self.language = language
        # Validity period of authentication template message sending in WhatsApp
        # 
        # > This attribute requires providing waba in advance to Alibaba operators to open the whitelist, otherwise it will result in template submission failure
        self.message_send_ttl_seconds = message_send_ttl_seconds
        # The name of the message template.
        # 
        # This parameter is required.
        self.name = name
        # The type of the message template.
        # 
        # *   **WHATSAPP**\
        # *   **VIBER**\
        # *   LINE: the Line message template. This type of message template will be released later.
        # 
        # This parameter is required.
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
        if self.message_send_ttl_seconds is not None:
            result['MessageSendTtlSeconds'] = self.message_send_ttl_seconds
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
        if m.get('MessageSendTtlSeconds') is not None:
            self.message_send_ttl_seconds = m.get('MessageSendTtlSeconds')
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
        # The code of the message template.
        self.template_code = template_code
        # The name of the message template.
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
        access_denied_detail: str = None,
        code: str = None,
        data: CreateChatappTemplateResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
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
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
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


class CreateFlowRequest(TeaModel):
    def __init__(
        self,
        categories: List[str] = None,
        cust_space_id: str = None,
        flow_name: str = None,
    ):
        # The categories of the Flow.
        # 
        # This parameter is required.
        self.categories = categories
        # The space ID of the user within the independent software vendor (ISV) account.
        self.cust_space_id = cust_space_id
        # The name of the Flow.
        # 
        # This parameter is required.
        self.flow_name = flow_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.categories is not None:
            result['Categories'] = self.categories
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        return self


class CreateFlowShrinkRequest(TeaModel):
    def __init__(
        self,
        categories_shrink: str = None,
        cust_space_id: str = None,
        flow_name: str = None,
    ):
        # The categories of the Flow.
        # 
        # This parameter is required.
        self.categories_shrink = categories_shrink
        # The space ID of the user within the independent software vendor (ISV) account.
        self.cust_space_id = cust_space_id
        # The name of the Flow.
        # 
        # This parameter is required.
        self.flow_name = flow_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.categories_shrink is not None:
            result['Categories'] = self.categories_shrink
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories_shrink = m.get('Categories')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        return self


class CreateFlowResponseBodyData(TeaModel):
    def __init__(
        self,
        categories: List[str] = None,
        flow_id: str = None,
        flow_name: str = None,
    ):
        # The categories of the Flow.
        self.categories = categories
        # The Flow ID.
        self.flow_id = flow_id
        # The name of the Flow.
        self.flow_name = flow_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.categories is not None:
            result['Categories'] = self.categories
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        return self


class CreateFlowResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateFlowResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # If OK is returned, the request was successful.
        self.code = code
        # The returned data.
        self.data = data
        # The error message.
        self.message = message
        # The request ID.
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
            temp_model = CreateFlowResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateFlowResponseBody = None,
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
            temp_model = CreateFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePhoneMessageQrdlRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        generate_qr_image: str = None,
        phone_number: str = None,
        prefilled_message: str = None,
    ):
        self.cust_space_id = cust_space_id
        # This parameter is required.
        self.generate_qr_image = generate_qr_image
        # This parameter is required.
        self.phone_number = phone_number
        # This parameter is required.
        self.prefilled_message = prefilled_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.generate_qr_image is not None:
            result['GenerateQrImage'] = self.generate_qr_image
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.prefilled_message is not None:
            result['PrefilledMessage'] = self.prefilled_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('GenerateQrImage') is not None:
            self.generate_qr_image = m.get('GenerateQrImage')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('PrefilledMessage') is not None:
            self.prefilled_message = m.get('PrefilledMessage')
        return self


class CreatePhoneMessageQrdlResponseBodyData(TeaModel):
    def __init__(
        self,
        deep_link_url: str = None,
        generate_qr_image: str = None,
        phone_number: str = None,
        prefilled_message: str = None,
        qr_image_url: str = None,
        qrdl_code: str = None,
    ):
        self.deep_link_url = deep_link_url
        self.generate_qr_image = generate_qr_image
        self.phone_number = phone_number
        self.prefilled_message = prefilled_message
        self.qr_image_url = qr_image_url
        self.qrdl_code = qrdl_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deep_link_url is not None:
            result['DeepLinkUrl'] = self.deep_link_url
        if self.generate_qr_image is not None:
            result['GenerateQrImage'] = self.generate_qr_image
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.prefilled_message is not None:
            result['PrefilledMessage'] = self.prefilled_message
        if self.qr_image_url is not None:
            result['QrImageUrl'] = self.qr_image_url
        if self.qrdl_code is not None:
            result['QrdlCode'] = self.qrdl_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeepLinkUrl') is not None:
            self.deep_link_url = m.get('DeepLinkUrl')
        if m.get('GenerateQrImage') is not None:
            self.generate_qr_image = m.get('GenerateQrImage')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('PrefilledMessage') is not None:
            self.prefilled_message = m.get('PrefilledMessage')
        if m.get('QrImageUrl') is not None:
            self.qr_image_url = m.get('QrImageUrl')
        if m.get('QrdlCode') is not None:
            self.qrdl_code = m.get('QrdlCode')
        return self


class CreatePhoneMessageQrdlResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreatePhoneMessageQrdlResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request。
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
            temp_model = CreatePhoneMessageQrdlResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreatePhoneMessageQrdlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreatePhoneMessageQrdlResponseBody = None,
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
            temp_model = CreatePhoneMessageQrdlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteChatappTemplateRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        cust_waba_id: str = None,
        isv_code: str = None,
        language: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        template_code: str = None,
        template_name: str = None,
        template_type: str = None,
    ):
        # The space ID of the user under the ISV account.
        self.cust_space_id = cust_space_id
        # The WhatsApp Business account (WABA) ID of the user within the independent software vendor (ISV) account.
        # 
        # >  CustWabaId is an obsolete parameter. Use CustSpaceId instead.
        self.cust_waba_id = cust_waba_id
        # The independent software vendor (ISV) verification code, which is used to verify whether the user is authorized by the ISV account.
        self.isv_code = isv_code
        self.language = language
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The code of the message template.
        self.template_code = template_code
        self.template_name = template_name
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
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
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
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class DeleteChatappTemplateResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        # The error message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
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


class DeleteFlowRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        flow_id: str = None,
    ):
        # The space ID of the user within the independent software vendor (ISV) account.
        self.cust_space_id = cust_space_id
        # The Flow ID.
        # 
        # This parameter is required.
        self.flow_id = flow_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        return self


class DeleteFlowResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # If OK is returned, the request was successful.
        self.code = code
        # The error message.
        self.message = message
        # The request ID.
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


class DeleteFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteFlowResponseBody = None,
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
            temp_model = DeleteFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePhoneMessageQrdlRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        phone_number: str = None,
        qrdl_code: str = None,
    ):
        self.cust_space_id = cust_space_id
        # This parameter is required.
        self.phone_number = phone_number
        # This parameter is required.
        self.qrdl_code = qrdl_code

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
        if self.qrdl_code is not None:
            result['QrdlCode'] = self.qrdl_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('QrdlCode') is not None:
            self.qrdl_code = m.get('QrdlCode')
        return self


class DeletePhoneMessageQrdlResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        # Id of the request。
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


class DeletePhoneMessageQrdlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeletePhoneMessageQrdlResponseBody = None,
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
            temp_model = DeletePhoneMessageQrdlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeprecateFlowRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        flow_id: str = None,
    ):
        self.cust_space_id = cust_space_id
        # Flow ID。
        # 
        # This parameter is required.
        self.flow_id = flow_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        return self


class DeprecateFlowResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        # Id of the request。
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


class DeprecateFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeprecateFlowResponseBody = None,
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
            temp_model = DeprecateFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableWhatsappROIMetricRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        isv_code: str = None,
    ):
        # The space ID of the user within the ISV account.
        self.cust_space_id = cust_space_id
        # The verification code used to verify whether the RAM user is authorized by the independent software vendor (ISV) account.
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


class EnableWhatsappROIMetricResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The value OK indicates that the request was successful.
        self.code = code
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EnableWhatsappROIMetricResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnableWhatsappROIMetricResponseBody = None,
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
            temp_model = EnableWhatsappROIMetricResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetChatappPhoneNumberMetricRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        end: int = None,
        granularity: str = None,
        isv_code: str = None,
        phone_number: str = None,
        start: int = None,
    ):
        # The space ID of the user within the ISV account.
        self.cust_space_id = cust_space_id
        # The end of the time range to query.
        # 
        # This parameter is required.
        self.end = end
        # The metric granularity.
        self.granularity = granularity
        # The verification code used to verify whether the RAM user is authorized by the independent software vendor (ISV) account.
        self.isv_code = isv_code
        # The business phone number.
        self.phone_number = phone_number
        # The beginning of the time range to query.
        # 
        # This parameter is required.
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.end is not None:
            result['End'] = self.end
        if self.granularity is not None:
            result['Granularity'] = self.granularity
        if self.isv_code is not None:
            result['IsvCode'] = self.isv_code
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.start is not None:
            result['Start'] = self.start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('Granularity') is not None:
            self.granularity = m.get('Granularity')
        if m.get('IsvCode') is not None:
            self.isv_code = m.get('IsvCode')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        return self


class GetChatappPhoneNumberMetricResponseBodyData(TeaModel):
    def __init__(
        self,
        delivered_count: int = None,
        end: int = None,
        granularity: str = None,
        phone_number: str = None,
        sent_count: int = None,
        start: int = None,
    ):
        # The number of delivered messages.
        self.delivered_count = delivered_count
        # The end of the time range that you queried.
        self.end = end
        # The metric granularity.
        # 
        # >  Valid values:
        # 
        # *   DAILY
        # 
        # *   HALF_HOUR
        self.granularity = granularity
        # The business phone number.
        self.phone_number = phone_number
        # The number of sent messages.
        self.sent_count = sent_count
        # The beginning of the time range that you queried.
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delivered_count is not None:
            result['DeliveredCount'] = self.delivered_count
        if self.end is not None:
            result['End'] = self.end
        if self.granularity is not None:
            result['Granularity'] = self.granularity
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.sent_count is not None:
            result['SentCount'] = self.sent_count
        if self.start is not None:
            result['Start'] = self.start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeliveredCount') is not None:
            self.delivered_count = m.get('DeliveredCount')
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('Granularity') is not None:
            self.granularity = m.get('Granularity')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('SentCount') is not None:
            self.sent_count = m.get('SentCount')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        return self


class GetChatappPhoneNumberMetricResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: List[GetChatappPhoneNumberMetricResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The value OK indicates that the request was successful.
        self.code = code
        # The returned data.
        self.data = data
        # The error message.
        self.message = message
        # The request ID.
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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetChatappPhoneNumberMetricResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetChatappPhoneNumberMetricResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetChatappPhoneNumberMetricResponseBody = None,
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
            temp_model = GetChatappPhoneNumberMetricResponseBody()
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
        template_name: str = None,
        template_type: str = None,
    ):
        # The space ID of the user within the ISV account.
        self.cust_space_id = cust_space_id
        # The WhatsApp Business account (WABA) ID of the user within the independent software vendor (ISV) account.
        # 
        # >  CustWabaId is an obsolete parameter. Use CustSpaceId instead.
        self.cust_waba_id = cust_waba_id
        # The independent software vendor (ISV) verification code. This parameter is used to verify whether the user is authorized by the ISV account.
        self.isv_code = isv_code
        # The language that is used in the message template. For more information, see [Language codes](https://help.aliyun.com/document_detail/463420.html).
        # 
        # This parameter is required.
        self.language = language
        # The code of the message template.
        self.template_code = template_code
        self.template_name = template_name
        # The type of the message template. Valid values:
        # 
        # *   **WHATSAPP**\
        # *   **VIBER**\
        # *   LINE (developing)
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
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
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
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
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
        # The event type.
        self.action = action
        # The intent code.
        self.intent_code = intent_code
        # The language of the next template.
        self.next_language_code = next_language_code
        # The code of the next template.
        self.next_template_code = next_template_code
        # The name of the next template.
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


class GetChatappTemplateDetailResponseBodyDataComponentsButtonsSupportedApps(TeaModel):
    def __init__(
        self,
        package_name: str = None,
        signature_hash: str = None,
    ):
        self.package_name = package_name
        self.signature_hash = signature_hash

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.package_name is not None:
            result['PackageName'] = self.package_name
        if self.signature_hash is not None:
            result['SignatureHash'] = self.signature_hash
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PackageName') is not None:
            self.package_name = m.get('PackageName')
        if m.get('SignatureHash') is not None:
            self.signature_hash = m.get('SignatureHash')
        return self


class GetChatappTemplateDetailResponseBodyDataComponentsButtons(TeaModel):
    def __init__(
        self,
        autofill_text: str = None,
        coupon_code: str = None,
        extend_attrs: GetChatappTemplateDetailResponseBodyDataComponentsButtonsExtendAttrs = None,
        flow_action: str = None,
        flow_id: str = None,
        is_opt_out: bool = None,
        navigate_screen: str = None,
        package_name: str = None,
        phone_number: str = None,
        signature_hash: str = None,
        supported_apps: List[GetChatappTemplateDetailResponseBodyDataComponentsButtonsSupportedApps] = None,
        text: str = None,
        type: str = None,
        url: str = None,
        url_type: str = None,
    ):
        # The text of the one-tap autofill button. This parameter is required if Category is set to AUTHENTICATION and the Type sub-parameter of the Buttons parameter is set to ONE_TAP in a WhatsApp message template.
        self.autofill_text = autofill_text
        # The coupon code.
        self.coupon_code = coupon_code
        # The extended fields.
        self.extend_attrs = extend_attrs
        # flow 数据事件类型
        # 取值范围：NAVIGATE/DATA_EXCHANGE
        self.flow_action = flow_action
        # Flow ID
        self.flow_id = flow_id
        # The unsubscribe button. This parameter is valid if Category is set to MARKETING and the Type sub-parameter of the Buttons parameter is set to QUICK_REPLY in a WhatsApp message template. After you configure message sending in the ChatApp Message Service console, marketing messages will not be sent to customers if they click this button.
        self.is_opt_out = is_opt_out
        # 跳转屏 
        # 在FlowAction=NAVIGATE时必填
        self.navigate_screen = navigate_screen
        # The app package name that WhatsApp uses to load your app. This parameter is required if Category is set to AUTHENTICATION and the Type sub-parameter of the Buttons parameter is set to ONE_TAP in a WhatsApp message template.
        self.package_name = package_name
        # The phone number. This parameter is valid only if the Type sub-parameter of the Buttons parameter is set to **PHONE_NUMBER**.
        self.phone_number = phone_number
        # The app signing key hash that WhatsApp uses to load your app. This parameter is required if Category is set to AUTHENTICATION and the Type sub-parameter of the Buttons parameter is set to ONE_TAP in a WhatsApp message template.
        self.signature_hash = signature_hash
        self.supported_apps = supported_apps
        # The display name of the button.
        self.text = text
        # The type of the button. Valid values:
        # 
        # *   **PHONE_NUMBER**: phone call button
        # *   **URL**: URL button
        # *   **QUICK_REPLY**: quick reply button
        # 
        # > 
        # 
        # *   In a message template, a quick reply button cannot be used together with a phone call button or a URL button.
        # 
        # *   You can add a combination of two URL buttons or a combination of a URL button and a phone call button to a message template.
        # 
        # *   You can add only one button to a Viber message template, and you must set the Type sub-parameter of the Buttons parameter to URL.
        self.type = type
        # The URL to which you are redirected when you click the URL button.
        self.url = url
        # The type of the URL. Valid values:
        # 
        # *   **static**\
        # *   **dynamic**\
        self.url_type = url_type

    def validate(self):
        if self.extend_attrs:
            self.extend_attrs.validate()
        if self.supported_apps:
            for k in self.supported_apps:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.autofill_text is not None:
            result['AutofillText'] = self.autofill_text
        if self.coupon_code is not None:
            result['CouponCode'] = self.coupon_code
        if self.extend_attrs is not None:
            result['ExtendAttrs'] = self.extend_attrs.to_map()
        if self.flow_action is not None:
            result['FlowAction'] = self.flow_action
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.is_opt_out is not None:
            result['IsOptOut'] = self.is_opt_out
        if self.navigate_screen is not None:
            result['NavigateScreen'] = self.navigate_screen
        if self.package_name is not None:
            result['PackageName'] = self.package_name
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.signature_hash is not None:
            result['SignatureHash'] = self.signature_hash
        result['SupportedApps'] = []
        if self.supported_apps is not None:
            for k in self.supported_apps:
                result['SupportedApps'].append(k.to_map() if k else None)
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
        if m.get('CouponCode') is not None:
            self.coupon_code = m.get('CouponCode')
        if m.get('ExtendAttrs') is not None:
            temp_model = GetChatappTemplateDetailResponseBodyDataComponentsButtonsExtendAttrs()
            self.extend_attrs = temp_model.from_map(m['ExtendAttrs'])
        if m.get('FlowAction') is not None:
            self.flow_action = m.get('FlowAction')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('IsOptOut') is not None:
            self.is_opt_out = m.get('IsOptOut')
        if m.get('NavigateScreen') is not None:
            self.navigate_screen = m.get('NavigateScreen')
        if m.get('PackageName') is not None:
            self.package_name = m.get('PackageName')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('SignatureHash') is not None:
            self.signature_hash = m.get('SignatureHash')
        self.supported_apps = []
        if m.get('SupportedApps') is not None:
            for k in m.get('SupportedApps'):
                temp_model = GetChatappTemplateDetailResponseBodyDataComponentsButtonsSupportedApps()
                self.supported_apps.append(temp_model.from_map(k))
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('UrlType') is not None:
            self.url_type = m.get('UrlType')
        return self


class GetChatappTemplateDetailResponseBodyDataComponentsCardsCardComponentsButtons(TeaModel):
    def __init__(
        self,
        phone_number: str = None,
        text: str = None,
        type: str = None,
        url: str = None,
        url_type: str = None,
    ):
        # The phone number.
        self.phone_number = phone_number
        # The button content.
        self.text = text
        # The type of the button in the carousel template. Valid values: URL, PHONE_NUMBER, and QUICK_REQLY.
        self.type = type
        # The URL to be accessed when you click the URL button.
        self.url = url
        # The type of the URL. Valid values: static and dynamic.
        self.url_type = url_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
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
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('UrlType') is not None:
            self.url_type = m.get('UrlType')
        return self


class GetChatappTemplateDetailResponseBodyDataComponentsCardsCardComponents(TeaModel):
    def __init__(
        self,
        buttons: List[GetChatappTemplateDetailResponseBodyDataComponentsCardsCardComponentsButtons] = None,
        format: str = None,
        text: str = None,
        type: str = None,
        url: str = None,
    ):
        # The card buttons.
        self.buttons = buttons
        # The type of the header in the carousel template. The header can only be an image or a video. The headers of all cards must be the same.
        self.format = format
        # The card text.
        self.text = text
        # The type of the component.
        self.type = type
        # The URL address.
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
        result['Buttons'] = []
        if self.buttons is not None:
            for k in self.buttons:
                result['Buttons'].append(k.to_map() if k else None)
        if self.format is not None:
            result['Format'] = self.format
        if self.text is not None:
            result['Text'] = self.text
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.buttons = []
        if m.get('Buttons') is not None:
            for k in m.get('Buttons'):
                temp_model = GetChatappTemplateDetailResponseBodyDataComponentsCardsCardComponentsButtons()
                self.buttons.append(temp_model.from_map(k))
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetChatappTemplateDetailResponseBodyDataComponentsCards(TeaModel):
    def __init__(
        self,
        card_components: List[GetChatappTemplateDetailResponseBodyDataComponentsCardsCardComponents] = None,
    ):
        # The card components.
        self.card_components = card_components

    def validate(self):
        if self.card_components:
            for k in self.card_components:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CardComponents'] = []
        if self.card_components is not None:
            for k in self.card_components:
                result['CardComponents'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.card_components = []
        if m.get('CardComponents') is not None:
            for k in m.get('CardComponents'):
                temp_model = GetChatappTemplateDetailResponseBodyDataComponentsCardsCardComponents()
                self.card_components.append(temp_model.from_map(k))
        return self


class GetChatappTemplateDetailResponseBodyDataComponents(TeaModel):
    def __init__(
        self,
        add_secret_recommendation: bool = None,
        buttons: List[GetChatappTemplateDetailResponseBodyDataComponentsButtons] = None,
        caption: str = None,
        cards: List[GetChatappTemplateDetailResponseBodyDataComponentsCards] = None,
        code_expiration_minutes: int = None,
        duration: int = None,
        file_name: str = None,
        file_type: str = None,
        format: str = None,
        latitude: str = None,
        location_address: str = None,
        location_name: str = None,
        longitude: str = None,
        offer_expiration_time_ms: str = None,
        text: str = None,
        thumb_url: str = None,
        type: str = None,
        url: str = None,
        has_expiration: bool = None,
    ):
        # The note indicating that customers cannot share verification codes with others. The note is displayed in the message body. This parameter is valid if Category is set to AUTHENTICATION and the Type sub-parameter of the Components parameter is set to BODY in a WhatsApp message template.
        self.add_secret_recommendation = add_secret_recommendation
        # The buttons. Specify this parameter only if you set the Type sub-parameter of the Components parameter to **BUTTONS**. Before you specify this parameter, the format of the value must be changed from JSON to String.
        self.buttons = buttons
        # The description of the document.
        self.caption = caption
        # The carousel cards.
        self.cards = cards
        # The validity period of the verification code in the WhatsApp authentication template. Unit: minutes. This parameter is valid only when Category is set to AUTHENTICATION and the Type sub-parameter of the Components parameter is set to FOOTER in a WhatsApp message template. The validity period of the verification code is displayed in the footer.
        self.code_expiration_minutes = code_expiration_minutes
        # The length of the video in the Viber message template. Valid values: 0 to 600. Unit: seconds.
        self.duration = duration
        # The name of the document.
        self.file_name = file_name
        # The type of the document attached in the Viber message template.
        self.file_type = file_type
        # The format.
        self.format = format
        # The latitude of the location.
        self.latitude = latitude
        # The address of the location.
        self.location_address = location_address
        # The name of the location.
        self.location_name = location_name
        # The longitude of the location.
        self.longitude = longitude
        # The variable when the coupon code expires in the limited-time offer template.
        self.offer_expiration_time_ms = offer_expiration_time_ms
        # The text of the message that you want to send.
        self.text = text
        # The thumbnail URL of the video in the Viber message template.
        self.thumb_url = thumb_url
        # The type of the component. Valid values:
        # 
        # *   **BODY**\
        # *   **HEADER**\
        # *   **FOOTER**\
        # *   **BUTTONS**\
        # 
        # > 
        # 
        # *   The following limits apply to components in WhatsApp message templates: A **BODY** component cannot exceed 1,024 characters in length. A **HEADER** or **FOOTER** component cannot exceed 60 characters in length.
        # 
        # *   **FOOTER** components are not supported in Viber message templates.
        # 
        # *   In a Viber message template, media resources such as images, videos, and documents are placed in the **HEADER** component. If a Viber message contains both text and an image, the image is placed below the text in the message received on a device.
        self.type = type
        # The URL of the media resource.
        self.url = url
        # Indicates whether the coupon code will expire in the limited-time offer template.
        self.has_expiration = has_expiration

    def validate(self):
        if self.buttons:
            for k in self.buttons:
                if k:
                    k.validate()
        if self.cards:
            for k in self.cards:
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
        result['Cards'] = []
        if self.cards is not None:
            for k in self.cards:
                result['Cards'].append(k.to_map() if k else None)
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
        if self.offer_expiration_time_ms is not None:
            result['OfferExpirationTimeMs'] = self.offer_expiration_time_ms
        if self.text is not None:
            result['Text'] = self.text
        if self.thumb_url is not None:
            result['ThumbUrl'] = self.thumb_url
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        if self.has_expiration is not None:
            result['hasExpiration'] = self.has_expiration
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
        self.cards = []
        if m.get('Cards') is not None:
            for k in m.get('Cards'):
                temp_model = GetChatappTemplateDetailResponseBodyDataComponentsCards()
                self.cards.append(temp_model.from_map(k))
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
        if m.get('OfferExpirationTimeMs') is not None:
            self.offer_expiration_time_ms = m.get('OfferExpirationTimeMs')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('ThumbUrl') is not None:
            self.thumb_url = m.get('ThumbUrl')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('hasExpiration') is not None:
            self.has_expiration = m.get('hasExpiration')
        return self


class GetChatappTemplateDetailResponseBodyData(TeaModel):
    def __init__(
        self,
        audit_status: str = None,
        category: str = None,
        components: List[GetChatappTemplateDetailResponseBodyDataComponents] = None,
        example: Dict[str, str] = None,
        language: str = None,
        message_send_ttl_seconds: int = None,
        name: str = None,
        quality_score: str = None,
        reason: str = None,
        template_code: str = None,
        template_type: str = None,
    ):
        # The review status of the message template. Valid values:
        # 
        # *   **pass**: The message template is approved.
        # *   **fail**: The message template is rejected.
        # *   **auditing**: The message template is being reviewed.
        # *   **unaudit**: The review is suspended.
        self.audit_status = audit_status
        # The category of the template when the returned value of TemplateType is WHATSAPP. Valid values:
        # 
        # *   **UTILITY**: a transactional template
        # *   **MARKETING**: a marketing template
        # *   **AUTHENTICATION**: an identity authentication template
        # 
        # The category of the template when the returned value of the TemplateType parameter is VIBER. Valid values:
        # 
        # *   **text**: a template that contains only text
        # *   **image**: a template that contains only images
        # *   **text_image_button**: a template that contains text, images, and buttons
        # *   **text_button**: a template that contains text and buttons
        # *   **document**: a template that contains only files
        # *   **video**: a template that contains only videos
        # *   **text_video**: a template that contains text and videos
        # *   **text_video_button**: a template that contains text, videos, and buttons
        # *   **text_image**: a template that contains text and images
        # 
        # > If Category is set to text_video_button, users cannot open a web page by clicking the button. Users can open only the video in the message. In this case, you do not need to specify the Url parameter for the URL button in the template.
        self.category = category
        # The components of the message template.
        self.components = components
        # The examples of variables.
        self.example = example
        # The language that is used in the message template. For more information, see [Language codes](https://help.aliyun.com/document_detail/463420.html).
        self.language = language
        # The validity period of the WhatsApp authentication message.
        self.message_send_ttl_seconds = message_send_ttl_seconds
        # The name of the message template.
        self.name = name
        # The quality of the template.
        self.quality_score = quality_score
        # The reason why the template was rejected.
        self.reason = reason
        # The code of the message template.
        self.template_code = template_code
        # The type of the message template. Valid values:
        # 
        # *   **WHATSAPP**\
        # *   **VIBER**\
        # *   LINE (developing)
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
        if self.message_send_ttl_seconds is not None:
            result['MessageSendTtlSeconds'] = self.message_send_ttl_seconds
        if self.name is not None:
            result['Name'] = self.name
        if self.quality_score is not None:
            result['QualityScore'] = self.quality_score
        if self.reason is not None:
            result['Reason'] = self.reason
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
        if m.get('MessageSendTtlSeconds') is not None:
            self.message_send_ttl_seconds = m.get('MessageSendTtlSeconds')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('QualityScore') is not None:
            self.quality_score = m.get('QualityScore')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class GetChatappTemplateDetailResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: GetChatappTemplateDetailResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        # The HTTP status code.
        # 
        # *   Example: OK. This value indicates that the request is successful.
        # *   Other codes indicate that the request fails. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        # The returned data.
        self.data = data
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
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
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
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


class GetChatappTemplateMetricRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        end: int = None,
        granularity: str = None,
        isv_code: str = None,
        language: str = None,
        start: int = None,
        template_code: str = None,
        template_type: str = None,
    ):
        # The space ID of the user within the ISV account.
        self.cust_space_id = cust_space_id
        # The end of the time range to query.
        # 
        # This parameter is required.
        self.end = end
        # The metric granularity.
        # 
        # >  Valid values:
        # 
        # *   DAILY
        self.granularity = granularity
        # The verification code used to verify whether the RAM user is authorized by the independent software vendor (ISV) account.
        self.isv_code = isv_code
        # The template language.
        self.language = language
        # The beginning of the time range to query.
        # 
        # This parameter is required.
        self.start = start
        # The template code.
        # 
        # This parameter is required.
        self.template_code = template_code
        # The template type. Valid values: WHATSAPP and VIBER. If you do not specify this parameter, WHATSAPP is used by default.
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
        if self.end is not None:
            result['End'] = self.end
        if self.granularity is not None:
            result['Granularity'] = self.granularity
        if self.isv_code is not None:
            result['IsvCode'] = self.isv_code
        if self.language is not None:
            result['Language'] = self.language
        if self.start is not None:
            result['Start'] = self.start
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('Granularity') is not None:
            self.granularity = m.get('Granularity')
        if m.get('IsvCode') is not None:
            self.isv_code = m.get('IsvCode')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class GetChatappTemplateMetricResponseBodyDataCliented(TeaModel):
    def __init__(
        self,
        button_content: str = None,
        count: int = None,
        type: str = None,
    ):
        # The text on the button.
        self.button_content = button_content
        # The number of clicks.
        self.count = count
        # The button type.
        # 
        # >  Valid values:
        # 
        # *   url_button
        # 
        # *   quick_relpy_button
        # 
        # *   phone_number_button
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.button_content is not None:
            result['ButtonContent'] = self.button_content
        if self.count is not None:
            result['Count'] = self.count
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ButtonContent') is not None:
            self.button_content = m.get('ButtonContent')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetChatappTemplateMetricResponseBodyData(TeaModel):
    def __init__(
        self,
        cliented: List[GetChatappTemplateMetricResponseBodyDataCliented] = None,
        delivered_count: int = None,
        end: int = None,
        language: str = None,
        read_count: int = None,
        sent_count: int = None,
        start: int = None,
        template_code: str = None,
    ):
        # The statistics on button clicks.
        self.cliented = cliented
        # The number of delivered messages.
        self.delivered_count = delivered_count
        # The end of the time range you queried.
        self.end = end
        # The template language.
        self.language = language
        # The number of read messages.
        self.read_count = read_count
        # The number of sent messages.
        self.sent_count = sent_count
        # The beginning of the time range you queried.
        self.start = start
        # The template code.
        self.template_code = template_code

    def validate(self):
        if self.cliented:
            for k in self.cliented:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Cliented'] = []
        if self.cliented is not None:
            for k in self.cliented:
                result['Cliented'].append(k.to_map() if k else None)
        if self.delivered_count is not None:
            result['DeliveredCount'] = self.delivered_count
        if self.end is not None:
            result['End'] = self.end
        if self.language is not None:
            result['Language'] = self.language
        if self.read_count is not None:
            result['ReadCount'] = self.read_count
        if self.sent_count is not None:
            result['SentCount'] = self.sent_count
        if self.start is not None:
            result['Start'] = self.start
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cliented = []
        if m.get('Cliented') is not None:
            for k in m.get('Cliented'):
                temp_model = GetChatappTemplateMetricResponseBodyDataCliented()
                self.cliented.append(temp_model.from_map(k))
        if m.get('DeliveredCount') is not None:
            self.delivered_count = m.get('DeliveredCount')
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('ReadCount') is not None:
            self.read_count = m.get('ReadCount')
        if m.get('SentCount') is not None:
            self.sent_count = m.get('SentCount')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        return self


class GetChatappTemplateMetricResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: List[GetChatappTemplateMetricResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The value OK indicates that the request was successful.
        self.code = code
        # The returned data.
        self.data = data
        # The error message.
        self.message = message
        # The request ID.
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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetChatappTemplateMetricResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetChatappTemplateMetricResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetChatappTemplateMetricResponseBody = None,
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
            temp_model = GetChatappTemplateMetricResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetChatappUploadAuthorizationRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
    ):
        # The space ID of the user under the independent software vendor (ISV) account.
        # 
        # This parameter is required.
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
        access_denied_detail: str = None,
        code: str = None,
        data: GetChatappUploadAuthorizationResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
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
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
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
        owner_id: int = None,
        phone_number: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # This parameter is required.
        self.cust_space_id = cust_space_id
        # This parameter is required.
        self.locale = locale
        # This parameter is required.
        self.method = method
        self.owner_id = owner_id
        # This parameter is required.
        self.phone_number = phone_number
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

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
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('Locale') is not None:
            self.locale = m.get('Locale')
        if m.get('Method') is not None:
            self.method = m.get('Method')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class GetChatappVerifyCodeResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        # The error message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
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


class GetCommerceSettingRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        owner_id: int = None,
        phone_number: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The space ID of the user within the independent software vendor (ISV) account.
        # 
        # This parameter is required.
        self.cust_space_id = cust_space_id
        self.owner_id = owner_id
        # The phone number.
        # 
        # This parameter is required.
        self.phone_number = phone_number
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class GetCommerceSettingResponseBodyData(TeaModel):
    def __init__(
        self,
        cart_enable: bool = None,
        catalog_visible: bool = None,
    ):
        # Indicates whether the shopping cart button is displayed.
        self.cart_enable = cart_enable
        # Indicates whether the catalog button is displayed.
        self.catalog_visible = catalog_visible

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cart_enable is not None:
            result['CartEnable'] = self.cart_enable
        if self.catalog_visible is not None:
            result['CatalogVisible'] = self.catalog_visible
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CartEnable') is not None:
            self.cart_enable = m.get('CartEnable')
        if m.get('CatalogVisible') is not None:
            self.catalog_visible = m.get('CatalogVisible')
        return self


class GetCommerceSettingResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: GetCommerceSettingResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   Other values indicate that the request failed. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        # The returned data.
        self.data = data
        # The error message.
        self.message = message
        # The request ID.
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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
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
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetCommerceSettingResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetCommerceSettingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCommerceSettingResponseBody = None,
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
            temp_model = GetCommerceSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetConversationalAutomationRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        owner_id: int = None,
        phone_number: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # This parameter is required.
        self.cust_space_id = cust_space_id
        self.owner_id = owner_id
        # This parameter is required.
        self.phone_number = phone_number
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class GetConversationalAutomationResponseBodyDataCommands(TeaModel):
    def __init__(
        self,
        command_description: str = None,
        command_name: str = None,
    ):
        self.command_description = command_description
        self.command_name = command_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command_description is not None:
            result['CommandDescription'] = self.command_description
        if self.command_name is not None:
            result['CommandName'] = self.command_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommandDescription') is not None:
            self.command_description = m.get('CommandDescription')
        if m.get('CommandName') is not None:
            self.command_name = m.get('CommandName')
        return self


class GetConversationalAutomationResponseBodyData(TeaModel):
    def __init__(
        self,
        commands: List[GetConversationalAutomationResponseBodyDataCommands] = None,
        enable_welcome_message: bool = None,
        phone_number: str = None,
        prompts: List[str] = None,
    ):
        self.commands = commands
        self.enable_welcome_message = enable_welcome_message
        self.phone_number = phone_number
        self.prompts = prompts

    def validate(self):
        if self.commands:
            for k in self.commands:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Commands'] = []
        if self.commands is not None:
            for k in self.commands:
                result['Commands'].append(k.to_map() if k else None)
        if self.enable_welcome_message is not None:
            result['EnableWelcomeMessage'] = self.enable_welcome_message
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.prompts is not None:
            result['Prompts'] = self.prompts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.commands = []
        if m.get('Commands') is not None:
            for k in m.get('Commands'):
                temp_model = GetConversationalAutomationResponseBodyDataCommands()
                self.commands.append(temp_model.from_map(k))
        if m.get('EnableWelcomeMessage') is not None:
            self.enable_welcome_message = m.get('EnableWelcomeMessage')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('Prompts') is not None:
            self.prompts = m.get('Prompts')
        return self


class GetConversationalAutomationResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: GetConversationalAutomationResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
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
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetConversationalAutomationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetConversationalAutomationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetConversationalAutomationResponseBody = None,
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
            temp_model = GetConversationalAutomationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFlowRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        flow_id: str = None,
    ):
        # The space ID of the user within the independent software vendor (ISV) account.
        self.cust_space_id = cust_space_id
        # The Flow ID.
        # 
        # This parameter is required.
        self.flow_id = flow_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        return self


class GetFlowResponseBodyData(TeaModel):
    def __init__(
        self,
        categories: List[str] = None,
        data_api_version: str = None,
        flow_id: str = None,
        flow_name: str = None,
        jsonversion: str = None,
        preview_url: str = None,
        preview_url_expires: int = None,
        status: str = None,
    ):
        # The categories of the Flow.
        self.categories = categories
        # The API version.
        self.data_api_version = data_api_version
        # The Flow ID.
        self.flow_id = flow_id
        # The name of the Flow.
        self.flow_name = flow_name
        # The JSON version.
        self.jsonversion = jsonversion
        # The temporary preview URL.
        self.preview_url = preview_url
        # The time when the preview URL expires. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.preview_url_expires = preview_url_expires
        # The state of the Flow.
        # 
        # Valid values:
        # 
        # *   PUBLISHED
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   DRAFT
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   DEPRECATED
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.categories is not None:
            result['Categories'] = self.categories
        if self.data_api_version is not None:
            result['DataApiVersion'] = self.data_api_version
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.jsonversion is not None:
            result['JSONVersion'] = self.jsonversion
        if self.preview_url is not None:
            result['PreviewUrl'] = self.preview_url
        if self.preview_url_expires is not None:
            result['PreviewUrlExpires'] = self.preview_url_expires
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        if m.get('DataApiVersion') is not None:
            self.data_api_version = m.get('DataApiVersion')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('JSONVersion') is not None:
            self.jsonversion = m.get('JSONVersion')
        if m.get('PreviewUrl') is not None:
            self.preview_url = m.get('PreviewUrl')
        if m.get('PreviewUrlExpires') is not None:
            self.preview_url_expires = m.get('PreviewUrlExpires')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetFlowResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetFlowResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # If OK is returned, the request was successful.
        self.code = code
        # The returned data.
        self.data = data
        # The error message.
        self.message = message
        # The request ID.
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
            temp_model = GetFlowResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFlowResponseBody = None,
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
            temp_model = GetFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFlowJSONAssestRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        flow_id: str = None,
    ):
        self.cust_space_id = cust_space_id
        # Flow ID。
        # 
        # This parameter is required.
        self.flow_id = flow_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        return self


class GetFlowJSONAssestResponseBodyData(TeaModel):
    def __init__(
        self,
        file_path: str = None,
        flow_id: str = None,
    ):
        self.file_path = file_path
        # flow ID。
        self.flow_id = flow_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_path is not None:
            result['FilePath'] = self.file_path
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        return self


class GetFlowJSONAssestResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetFlowJSONAssestResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request。
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
            temp_model = GetFlowJSONAssestResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetFlowJSONAssestResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFlowJSONAssestResponseBody = None,
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
            temp_model = GetFlowJSONAssestResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFlowPreviewUrlRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        flow_id: str = None,
    ):
        # The space ID of the user within the independent software vendor (ISV) account.
        self.cust_space_id = cust_space_id
        # The Flow ID.
        # 
        # This parameter is required.
        self.flow_id = flow_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        return self


class GetFlowPreviewUrlResponseBodyData(TeaModel):
    def __init__(
        self,
        flow_id: str = None,
        preview_url: str = None,
        preview_url_expires: int = None,
    ):
        # The Flow ID.
        self.flow_id = flow_id
        # The temporary preview URL.
        self.preview_url = preview_url
        # The time when the preview URL expires. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.preview_url_expires = preview_url_expires

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.preview_url is not None:
            result['PreviewUrl'] = self.preview_url
        if self.preview_url_expires is not None:
            result['PreviewUrlExpires'] = self.preview_url_expires
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('PreviewUrl') is not None:
            self.preview_url = m.get('PreviewUrl')
        if m.get('PreviewUrlExpires') is not None:
            self.preview_url_expires = m.get('PreviewUrlExpires')
        return self


class GetFlowPreviewUrlResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetFlowPreviewUrlResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # If OK is returned, the request was successful.
        self.code = code
        # The returned data.
        self.data = data
        # The error message.
        self.message = message
        # The request ID.
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
            temp_model = GetFlowPreviewUrlResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetFlowPreviewUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFlowPreviewUrlResponseBody = None,
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
            temp_model = GetFlowPreviewUrlResponseBody()
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
        # This parameter is required.
        self.cust_space_id = cust_space_id
        # This parameter is required.
        self.locale = locale
        # This parameter is required.
        self.method = method
        # This parameter is required.
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
        access_denied_detail: str = None,
        code: str = None,
        data: GetMigrationVerifyCodeResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
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
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
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


class GetPermissionByCodeRequest(TeaModel):
    def __init__(
        self,
        code: str = None,
        cust_space_id: str = None,
        permissions: List[str] = None,
    ):
        # This parameter is required.
        self.code = code
        self.cust_space_id = cust_space_id
        self.permissions = permissions

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.permissions is not None:
            result['Permissions'] = self.permissions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('Permissions') is not None:
            self.permissions = m.get('Permissions')
        return self


class GetPermissionByCodeShrinkRequest(TeaModel):
    def __init__(
        self,
        code: str = None,
        cust_space_id: str = None,
        permissions_shrink: str = None,
    ):
        # This parameter is required.
        self.code = code
        self.cust_space_id = cust_space_id
        self.permissions_shrink = permissions_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.permissions_shrink is not None:
            result['Permissions'] = self.permissions_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('Permissions') is not None:
            self.permissions_shrink = m.get('Permissions')
        return self


class GetPermissionByCodeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        # Id of the request。
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


class GetPermissionByCodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPermissionByCodeResponseBody = None,
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
            temp_model = GetPermissionByCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPhoneEncryptionPublicKeyRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        phone_number: str = None,
    ):
        self.cust_space_id = cust_space_id
        # This parameter is required.
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


class GetPhoneEncryptionPublicKeyResponseBodyData(TeaModel):
    def __init__(
        self,
        encryption_public_key: str = None,
        encryption_public_key_status: str = None,
        phone_number: str = None,
    ):
        self.encryption_public_key = encryption_public_key
        self.encryption_public_key_status = encryption_public_key_status
        self.phone_number = phone_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encryption_public_key is not None:
            result['EncryptionPublicKey'] = self.encryption_public_key
        if self.encryption_public_key_status is not None:
            result['EncryptionPublicKeyStatus'] = self.encryption_public_key_status
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncryptionPublicKey') is not None:
            self.encryption_public_key = m.get('EncryptionPublicKey')
        if m.get('EncryptionPublicKeyStatus') is not None:
            self.encryption_public_key_status = m.get('EncryptionPublicKeyStatus')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        return self


class GetPhoneEncryptionPublicKeyResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetPhoneEncryptionPublicKeyResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request。
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
            temp_model = GetPhoneEncryptionPublicKeyResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPhoneEncryptionPublicKeyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPhoneEncryptionPublicKeyResponseBody = None,
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
            temp_model = GetPhoneEncryptionPublicKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPhoneNumberVerificationStatusRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        phone_number: str = None,
    ):
        # The space ID of the user under the ISV account.
        # 
        # This parameter is required.
        self.cust_space_id = cust_space_id
        # The phone number.
        # 
        # This parameter is required.
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
        # *   Other values indicate that the call fails. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
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


class GetPreValidatePhoneIdRequest(TeaModel):
    def __init__(
        self,
        phone_number: str = None,
        verify_code: str = None,
    ):
        # The phone number.
        # 
        # This parameter is required.
        self.phone_number = phone_number
        # The verification code provided when you purchased the pre-registered phone number.
        # 
        # This parameter is required.
        self.verify_code = verify_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.verify_code is not None:
            result['VerifyCode'] = self.verify_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('VerifyCode') is not None:
            self.verify_code = m.get('VerifyCode')
        return self


class GetPreValidatePhoneIdResponseBodyData(TeaModel):
    def __init__(
        self,
        phone_number: str = None,
        phone_number_id: str = None,
    ):
        # The phone number.
        self.phone_number = phone_number
        # The ID of the phone number.
        self.phone_number_id = phone_number_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.phone_number_id is not None:
            result['PhoneNumberId'] = self.phone_number_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('PhoneNumberId') is not None:
            self.phone_number_id = m.get('PhoneNumberId')
        return self


class GetPreValidatePhoneIdResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetPreValidatePhoneIdResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response code. The value OK indicates the request was successful.
        self.code = code
        # The returned data.
        self.data = data
        # The error message.
        self.message = message
        # The request ID.
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
            temp_model = GetPreValidatePhoneIdResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPreValidatePhoneIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPreValidatePhoneIdResponseBody = None,
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
            temp_model = GetPreValidatePhoneIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWhatsappConnectionCatalogRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        waba_id: str = None,
    ):
        # The space ID of the user within the ISV account.
        self.cust_space_id = cust_space_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The WABA ID.
        # 
        # This parameter is required.
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
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.waba_id is not None:
            result['WabaId'] = self.waba_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('WabaId') is not None:
            self.waba_id = m.get('WabaId')
        return self


class GetWhatsappConnectionCatalogResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        model: Dict[str, Any] = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   Other values indicate that the request failed. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        # The error message.
        self.message = message
        # The returned data.
        self.model = model
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetWhatsappConnectionCatalogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetWhatsappConnectionCatalogResponseBody = None,
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
            temp_model = GetWhatsappConnectionCatalogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWhatsappHealthStatusRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        language: str = None,
        node_type: str = None,
        owner_id: int = None,
        phone_number: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        template_code: str = None,
        waba_id: str = None,
    ):
        # This parameter is required.
        self.cust_space_id = cust_space_id
        self.language = language
        # This parameter is required.
        self.node_type = node_type
        self.owner_id = owner_id
        self.phone_number = phone_number
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.template_code = template_code
        # WabaId
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
        if self.language is not None:
            result['Language'] = self.language
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.waba_id is not None:
            result['WabaId'] = self.waba_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('WabaId') is not None:
            self.waba_id = m.get('WabaId')
        return self


class GetWhatsappHealthStatusResponseBodyDataEntitiesErrors(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_description: str = None,
        possible_solution: str = None,
    ):
        self.error_code = error_code
        self.error_description = error_description
        self.possible_solution = possible_solution

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_description is not None:
            result['ErrorDescription'] = self.error_description
        if self.possible_solution is not None:
            result['PossibleSolution'] = self.possible_solution
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorDescription') is not None:
            self.error_description = m.get('ErrorDescription')
        if m.get('PossibleSolution') is not None:
            self.possible_solution = m.get('PossibleSolution')
        return self


class GetWhatsappHealthStatusResponseBodyDataEntities(TeaModel):
    def __init__(
        self,
        business_id: str = None,
        can_send_message: str = None,
        entity_type: str = None,
        errors: List[GetWhatsappHealthStatusResponseBodyDataEntitiesErrors] = None,
        language: str = None,
        phone_number: str = None,
        template_code: str = None,
        waba_id: str = None,
    ):
        self.business_id = business_id
        self.can_send_message = can_send_message
        self.entity_type = entity_type
        self.errors = errors
        self.language = language
        self.phone_number = phone_number
        self.template_code = template_code
        self.waba_id = waba_id

    def validate(self):
        if self.errors:
            for k in self.errors:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_id is not None:
            result['BusinessId'] = self.business_id
        if self.can_send_message is not None:
            result['CanSendMessage'] = self.can_send_message
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        result['Errors'] = []
        if self.errors is not None:
            for k in self.errors:
                result['Errors'].append(k.to_map() if k else None)
        if self.language is not None:
            result['Language'] = self.language
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.waba_id is not None:
            result['WabaId'] = self.waba_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessId') is not None:
            self.business_id = m.get('BusinessId')
        if m.get('CanSendMessage') is not None:
            self.can_send_message = m.get('CanSendMessage')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        self.errors = []
        if m.get('Errors') is not None:
            for k in m.get('Errors'):
                temp_model = GetWhatsappHealthStatusResponseBodyDataEntitiesErrors()
                self.errors.append(temp_model.from_map(k))
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('WabaId') is not None:
            self.waba_id = m.get('WabaId')
        return self


class GetWhatsappHealthStatusResponseBodyData(TeaModel):
    def __init__(
        self,
        can_send_message: str = None,
        entities: List[GetWhatsappHealthStatusResponseBodyDataEntities] = None,
    ):
        self.can_send_message = can_send_message
        self.entities = entities

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
        if self.can_send_message is not None:
            result['CanSendMessage'] = self.can_send_message
        result['Entities'] = []
        if self.entities is not None:
            for k in self.entities:
                result['Entities'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanSendMessage') is not None:
            self.can_send_message = m.get('CanSendMessage')
        self.entities = []
        if m.get('Entities') is not None:
            for k in m.get('Entities'):
                temp_model = GetWhatsappHealthStatusResponseBodyDataEntities()
                self.entities.append(temp_model.from_map(k))
        return self


class GetWhatsappHealthStatusResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: GetWhatsappHealthStatusResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
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
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetWhatsappHealthStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetWhatsappHealthStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetWhatsappHealthStatusResponseBody = None,
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
            temp_model = GetWhatsappHealthStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class IsvGetAppIdRequest(TeaModel):
    def __init__(
        self,
        permissions: str = None,
        type: str = None,
    ):
        # 权限
        self.permissions = permissions
        # The type of the application. Set the value to WHATSAPP.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.permissions is not None:
            result['Permissions'] = self.permissions
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Permissions') is not None:
            self.permissions = m.get('Permissions')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class IsvGetAppIdResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        app_id: str = None,
        code: str = None,
        config_id: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        # The message ID.
        self.app_id = app_id
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        self.config_id = config_id
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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.code is not None:
            result['Code'] = self.code
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
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
        # The page number. Default value: 1.
        # 
        # This parameter is required.
        self.index = index
        # The number of entries per page. Default value: 10.
        # 
        # This parameter is required.
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
        code: str = None,
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
        self.code = code
        # The space ID of the user under the ISV account.
        self.cust_space_id = cust_space_id
        # The WhatsApp Business account (WABA) ID of the user within the independent software vendor (ISV) account.
        # 
        # >  CustWabaId is an obsolete parameter. Use CustSpaceId instead.
        self.cust_waba_id = cust_waba_id
        # The independent software vendor (ISV) verification code, which is used to verify whether the user is authorized by the ISV account.
        self.isv_code = isv_code
        # The language that is used in the message template. For more information, see [Language codes](https://help.aliyun.com/document_detail/463420.html).
        self.language = language
        # The name of the message template.
        self.name = name
        # The pagination settings.
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
        if self.code is not None:
            result['Code'] = self.code
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
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
        code: str = None,
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
        self.code = code
        # The space ID of the user under the ISV account.
        self.cust_space_id = cust_space_id
        # The WhatsApp Business account (WABA) ID of the user within the independent software vendor (ISV) account.
        # 
        # >  CustWabaId is an obsolete parameter. Use CustSpaceId instead.
        self.cust_waba_id = cust_waba_id
        # The independent software vendor (ISV) verification code, which is used to verify whether the user is authorized by the ISV account.
        self.isv_code = isv_code
        # The language that is used in the message template. For more information, see [Language codes](https://help.aliyun.com/document_detail/463420.html).
        self.language = language
        # The name of the message template.
        self.name = name
        # The pagination settings.
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
        if self.code is not None:
            result['Code'] = self.code
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
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
        last_update_time: int = None,
        reason: str = None,
        template_code: str = None,
        template_name: str = None,
        template_type: str = None,
    ):
        # The review state of the message template. Valid values:
        # 
        # *   **pass**: The message template is approved.
        # *   **fail**: The message template is rejected.
        # *   **auditing**: The message template is being reviewed.
        # *   **unaudit**: The review is suspended.
        self.audit_status = audit_status
        # The category of the WhatsApp template. Valid values:
        # 
        # *   **UTILITY**: utility template
        # *   **MARKETING**: marketing template
        # *   **AUTHENTICATION**: authentication template
        # 
        # The category of the Viber template. Valid values:
        # 
        # *   **text**: template that contains only text
        # *   **image**: template that contains only an image
        # *   **text_image_button**: template that contains text, an image, and a button
        # *   **text_button**: template that contains text and a button
        # *   **document**: template that contains only a document
        # *   **video**: template that contains only a video
        # *   **text_video**: template that contains text and a video
        # *   **text_video_button**: template that contains text, a video, and a button
        # *   **text_image**: template that contains text and an image
        self.category = category
        # The language that is used in the message template. For more information, see [Language codes](https://help.aliyun.com/document_detail/463420.html).
        self.language = language
        self.last_update_time = last_update_time
        # The reason for the review failure.
        self.reason = reason
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
        if self.last_update_time is not None:
            result['LastUpdateTime'] = self.last_update_time
        if self.reason is not None:
            result['Reason'] = self.reason
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
        if m.get('LastUpdateTime') is not None:
            self.last_update_time = m.get('LastUpdateTime')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
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
        access_denied_detail: str = None,
        code: str = None,
        list_template: List[ListChatappTemplateResponseBodyListTemplate] = None,
        message: str = None,
        request_id: str = None,
        total: int = None,
    ):
        self.access_denied_detail = access_denied_detail
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        # The message templates.
        self.list_template = list_template
        # The error message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
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
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
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


class ListFlowRequestPage(TeaModel):
    def __init__(
        self,
        index: int = None,
        size: int = None,
    ):
        # The page number.
        self.index = index
        # The number of entries per page.
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


class ListFlowRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        flow_name: str = None,
        page: ListFlowRequestPage = None,
    ):
        # The space ID of the user within the independent software vendor (ISV) account.
        self.cust_space_id = cust_space_id
        # The name of the Flow.
        self.flow_name = flow_name
        # The returned pages.
        self.page = page

    def validate(self):
        if self.page:
            self.page.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.page is not None:
            result['Page'] = self.page.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('Page') is not None:
            temp_model = ListFlowRequestPage()
            self.page = temp_model.from_map(m['Page'])
        return self


class ListFlowShrinkRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        flow_name: str = None,
        page_shrink: str = None,
    ):
        # The space ID of the user within the independent software vendor (ISV) account.
        self.cust_space_id = cust_space_id
        # The name of the Flow.
        self.flow_name = flow_name
        # The returned pages.
        self.page_shrink = page_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.page_shrink is not None:
            result['Page'] = self.page_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('Page') is not None:
            self.page_shrink = m.get('Page')
        return self


class ListFlowResponseBodyData(TeaModel):
    def __init__(
        self,
        categories: List[str] = None,
        flow_id: str = None,
        flow_name: str = None,
    ):
        # The categories of the Flows.
        self.categories = categories
        # The Flow ID.
        self.flow_id = flow_id
        # The name of the Flow.
        self.flow_name = flow_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.categories is not None:
            result['Categories'] = self.categories
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        return self


class ListFlowResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListFlowResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
    ):
        # If OK is returned, the request was successful.
        self.code = code
        # The returned data.
        self.data = data
        # The error message.
        self.message = message
        # The request ID.
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
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListFlowResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFlowResponseBody = None,
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
            temp_model = ListFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPhoneMessageQrdlRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        phone_number: str = None,
    ):
        self.cust_space_id = cust_space_id
        # This parameter is required.
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


class ListPhoneMessageQrdlResponseBodyData(TeaModel):
    def __init__(
        self,
        deep_link_url: str = None,
        generate_qr_image: str = None,
        phone_number: str = None,
        prefilled_message: str = None,
        qr_image_url: str = None,
        qrdl_code: str = None,
    ):
        self.deep_link_url = deep_link_url
        self.generate_qr_image = generate_qr_image
        self.phone_number = phone_number
        self.prefilled_message = prefilled_message
        self.qr_image_url = qr_image_url
        self.qrdl_code = qrdl_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deep_link_url is not None:
            result['DeepLinkUrl'] = self.deep_link_url
        if self.generate_qr_image is not None:
            result['GenerateQrImage'] = self.generate_qr_image
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.prefilled_message is not None:
            result['PrefilledMessage'] = self.prefilled_message
        if self.qr_image_url is not None:
            result['QrImageUrl'] = self.qr_image_url
        if self.qrdl_code is not None:
            result['QrdlCode'] = self.qrdl_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeepLinkUrl') is not None:
            self.deep_link_url = m.get('DeepLinkUrl')
        if m.get('GenerateQrImage') is not None:
            self.generate_qr_image = m.get('GenerateQrImage')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('PrefilledMessage') is not None:
            self.prefilled_message = m.get('PrefilledMessage')
        if m.get('QrImageUrl') is not None:
            self.qr_image_url = m.get('QrImageUrl')
        if m.get('QrdlCode') is not None:
            self.qrdl_code = m.get('QrdlCode')
        return self


class ListPhoneMessageQrdlResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListPhoneMessageQrdlResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request。
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
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListPhoneMessageQrdlResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListPhoneMessageQrdlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPhoneMessageQrdlResponseBody = None,
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
            temp_model = ListPhoneMessageQrdlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProductRequest(TeaModel):
    def __init__(
        self,
        after: str = None,
        before: str = None,
        catalog_id: str = None,
        cust_space_id: str = None,
        fields: str = None,
        limit: int = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        waba_id: str = None,
    ):
        # The cursor that points to the end of the page of the returned data.
        self.after = after
        # The cursor that points to the beginning of the page of the returned data.
        self.before = before
        # The catalog ID.
        # 
        # This parameter is required.
        self.catalog_id = catalog_id
        # The space ID of the user within the independent software vendor (ISV) account.
        self.cust_space_id = cust_space_id
        # The fields. Separate multiple fields with commas (,).
        # 
        #  see [product fields](https://help.aliyun.com/document_detail/2579419.html)
        self.fields = fields
        # The number of products to be queried. Valid values: 1 to 1000.
        self.limit = limit
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the WhatsApp Business account (WABA).
        # 
        # This parameter is required.
        self.waba_id = waba_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.after is not None:
            result['After'] = self.after
        if self.before is not None:
            result['Before'] = self.before
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.fields is not None:
            result['Fields'] = self.fields
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.waba_id is not None:
            result['WabaId'] = self.waba_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('After') is not None:
            self.after = m.get('After')
        if m.get('Before') is not None:
            self.before = m.get('Before')
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('Fields') is not None:
            self.fields = m.get('Fields')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('WabaId') is not None:
            self.waba_id = m.get('WabaId')
        return self


class ListProductResponseBodyModelPagingCursors(TeaModel):
    def __init__(
        self,
        after: str = None,
        before: str = None,
    ):
        # The cursor that points to the end of the page of the returned data.
        self.after = after
        # The cursor that points to the beginning of the page of the returned data.
        self.before = before

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.after is not None:
            result['After'] = self.after
        if self.before is not None:
            result['Before'] = self.before
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('After') is not None:
            self.after = m.get('After')
        if m.get('Before') is not None:
            self.before = m.get('Before')
        return self


class ListProductResponseBodyModelPaging(TeaModel):
    def __init__(
        self,
        cursors: ListProductResponseBodyModelPagingCursors = None,
    ):
        # The cursors for pagination.
        self.cursors = cursors

    def validate(self):
        if self.cursors:
            self.cursors.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cursors is not None:
            result['Cursors'] = self.cursors.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cursors') is not None:
            temp_model = ListProductResponseBodyModelPagingCursors()
            self.cursors = temp_model.from_map(m['Cursors'])
        return self


class ListProductResponseBodyModel(TeaModel):
    def __init__(
        self,
        data: List[Dict[str, Any]] = None,
        paging: ListProductResponseBodyModelPaging = None,
    ):
        # The returned data.
        self.data = data
        # The pagination details.
        self.paging = paging

    def validate(self):
        if self.paging:
            self.paging.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.paging is not None:
            result['Paging'] = self.paging.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Paging') is not None:
            temp_model = ListProductResponseBodyModelPaging()
            self.paging = temp_model.from_map(m['Paging'])
        return self


class ListProductResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        model: ListProductResponseBodyModel = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   Other values indicate that the request failed. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        # The error message.
        self.message = message
        # The returned data.
        self.model = model
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.success = success

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            temp_model = ListProductResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListProductResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListProductResponseBody = None,
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
            temp_model = ListProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProductCatalogRequest(TeaModel):
    def __init__(
        self,
        after: str = None,
        before: str = None,
        business_id: int = None,
        cust_space_id: str = None,
        fields: str = None,
        limit: int = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The cursor that points to the end of the page of the returned data.
        self.after = after
        # The cursor that points to the beginning of the page of the returned data.
        self.before = before
        # The Business Manager ID.
        # 
        # This parameter is required.
        self.business_id = business_id
        # The space ID of the user within the independent software vendor (ISV) account.
        self.cust_space_id = cust_space_id
        # The fields. Separate multiple fields with commas (,).
        # see  [catalog fields](https://help.aliyun.com/document_detail/2579419.html)
        self.fields = fields
        # The number of catalogs to be queried. Valid values: 1 to 1000.
        self.limit = limit
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.after is not None:
            result['After'] = self.after
        if self.before is not None:
            result['Before'] = self.before
        if self.business_id is not None:
            result['BusinessId'] = self.business_id
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.fields is not None:
            result['Fields'] = self.fields
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('After') is not None:
            self.after = m.get('After')
        if m.get('Before') is not None:
            self.before = m.get('Before')
        if m.get('BusinessId') is not None:
            self.business_id = m.get('BusinessId')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('Fields') is not None:
            self.fields = m.get('Fields')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ListProductCatalogResponseBodyModelPagingCursors(TeaModel):
    def __init__(
        self,
        after: str = None,
        before: str = None,
    ):
        # The cursor that points to the end of the page of the returned data.
        self.after = after
        # The cursor that points to the beginning of the page of the returned data.
        self.before = before

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.after is not None:
            result['After'] = self.after
        if self.before is not None:
            result['Before'] = self.before
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('After') is not None:
            self.after = m.get('After')
        if m.get('Before') is not None:
            self.before = m.get('Before')
        return self


class ListProductCatalogResponseBodyModelPaging(TeaModel):
    def __init__(
        self,
        cursors: ListProductCatalogResponseBodyModelPagingCursors = None,
    ):
        # The cursors for pagination.
        self.cursors = cursors

    def validate(self):
        if self.cursors:
            self.cursors.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cursors is not None:
            result['Cursors'] = self.cursors.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cursors') is not None:
            temp_model = ListProductCatalogResponseBodyModelPagingCursors()
            self.cursors = temp_model.from_map(m['Cursors'])
        return self


class ListProductCatalogResponseBodyModel(TeaModel):
    def __init__(
        self,
        data: List[Dict[str, Any]] = None,
        paging: ListProductCatalogResponseBodyModelPaging = None,
    ):
        # The returned data.
        self.data = data
        # The pagination details.
        self.paging = paging

    def validate(self):
        if self.paging:
            self.paging.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.paging is not None:
            result['Paging'] = self.paging.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Paging') is not None:
            temp_model = ListProductCatalogResponseBodyModelPaging()
            self.paging = temp_model.from_map(m['Paging'])
        return self


class ListProductCatalogResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        model: ListProductCatalogResponseBodyModel = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   Other values indicate that the request failed. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        # The error message.
        self.message = message
        # The returned data.
        self.model = model
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.success = success

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            temp_model = ListProductCatalogResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListProductCatalogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListProductCatalogResponseBody = None,
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
            temp_model = ListProductCatalogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyChatappTemplateRequestComponentsButtonsSupportedApps(TeaModel):
    def __init__(
        self,
        package_name: str = None,
        signature_hash: str = None,
    ):
        self.package_name = package_name
        self.signature_hash = signature_hash

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.package_name is not None:
            result['PackageName'] = self.package_name
        if self.signature_hash is not None:
            result['SignatureHash'] = self.signature_hash
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PackageName') is not None:
            self.package_name = m.get('PackageName')
        if m.get('SignatureHash') is not None:
            self.signature_hash = m.get('SignatureHash')
        return self


class ModifyChatappTemplateRequestComponentsButtons(TeaModel):
    def __init__(
        self,
        autofill_text: str = None,
        coupon_code: str = None,
        flow_action: str = None,
        flow_id: str = None,
        is_opt_out: bool = None,
        navigate_screen: str = None,
        package_name: str = None,
        phone_number: str = None,
        signature_hash: str = None,
        supported_apps: List[ModifyChatappTemplateRequestComponentsButtonsSupportedApps] = None,
        text: str = None,
        type: str = None,
        url: str = None,
        url_type: str = None,
    ):
        # The text of the one-tap autofill button. This parameter is required if Category is set to AUTHENTICATION and the Type sub-parameter of the Buttons parameter is set to ONE_TAP for a WhatsApp message template.
        self.autofill_text = autofill_text
        self.coupon_code = coupon_code
        self.flow_action = flow_action
        self.flow_id = flow_id
        # The unsubscribe button. This parameter is valid if Category is set to MARKETING and the Type sub-parameter of the Buttons parameter is set to QUICK_REPLY for a WhatsApp message template. After you configure message sending in the ChatApp Message Service console, marketing messages are not sent to customers if they click this button.
        self.is_opt_out = is_opt_out
        self.navigate_screen = navigate_screen
        # The app package name that WhatsApp uses to load your app. This parameter is required if Category is set to AUTHENTICATION and the Type sub-parameter of the Buttons parameter is set to ONE_TAP for a WhatsApp message template.
        self.package_name = package_name
        # The phone number.
        self.phone_number = phone_number
        # The app signing key hash that WhatsApp uses to load your app. This parameter is required if Category is set to AUTHENTICATION and the Type sub-parameter of the Buttons parameter is set to ONE_TAP for a WhatsApp message template.
        self.signature_hash = signature_hash
        self.supported_apps = supported_apps
        # The text of the button.
        self.text = text
        # The type of the button. Valid values:
        # 
        # *   **PHONE_NUMBER**: phone call button
        # *   **URL**: URL button
        # *   **QUICK_REPLY**: quick reply button
        # *   **COPY_CODE**: copy code button if Category is set to AUTHENTICATION
        # *   **ONE_TAP**: one-tap autofill button if Category is set to AUTHENTICATION
        # 
        # > 
        # 
        # *   In a WhatsApp message template, a quick reply button cannot be used together with a phone call button or a URL button.
        # 
        # *   You can add a combination of two URL buttons or a combination of a URL button and a phone call button to a WhatsApp message template.
        # 
        # *   If Category is set to AUTHENTICATION for a WhatsApp message template, you can add only one button to the WhatsApp message template and you must set the Type sub-parameter of the Buttons parameter to COPY_CODE or ONE_TAP. If the Type sub-parameter of the Buttons parameter is set to COPY_CODE, the Text sub-parameter of the Buttons parameter is required. If the Type sub-parameter of the Buttons parameter is set to ONE_TAP, the Text, SignatureHash, PackageName, and AutofillText sub-parameters of the Buttons parameter are required. The value of Text is displayed if the desired app is not installed on the device. The value of Text indicates that you must manually copy the verification code.
        # 
        # *   You can add only one button to a Viber message template, and you must set the Type sub-parameter of the Buttons parameter to URL.
        # 
        # This parameter is required.
        self.type = type
        # The URL to which you are redirected when you click the URL button.
        self.url = url
        # The type of the URL. Valid values:
        # 
        # *   **static**\
        # *   **dynamic**\
        self.url_type = url_type

    def validate(self):
        if self.supported_apps:
            for k in self.supported_apps:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.autofill_text is not None:
            result['AutofillText'] = self.autofill_text
        if self.coupon_code is not None:
            result['CouponCode'] = self.coupon_code
        if self.flow_action is not None:
            result['FlowAction'] = self.flow_action
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.is_opt_out is not None:
            result['IsOptOut'] = self.is_opt_out
        if self.navigate_screen is not None:
            result['NavigateScreen'] = self.navigate_screen
        if self.package_name is not None:
            result['PackageName'] = self.package_name
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.signature_hash is not None:
            result['SignatureHash'] = self.signature_hash
        result['SupportedApps'] = []
        if self.supported_apps is not None:
            for k in self.supported_apps:
                result['SupportedApps'].append(k.to_map() if k else None)
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
        if m.get('CouponCode') is not None:
            self.coupon_code = m.get('CouponCode')
        if m.get('FlowAction') is not None:
            self.flow_action = m.get('FlowAction')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('IsOptOut') is not None:
            self.is_opt_out = m.get('IsOptOut')
        if m.get('NavigateScreen') is not None:
            self.navigate_screen = m.get('NavigateScreen')
        if m.get('PackageName') is not None:
            self.package_name = m.get('PackageName')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('SignatureHash') is not None:
            self.signature_hash = m.get('SignatureHash')
        self.supported_apps = []
        if m.get('SupportedApps') is not None:
            for k in m.get('SupportedApps'):
                temp_model = ModifyChatappTemplateRequestComponentsButtonsSupportedApps()
                self.supported_apps.append(temp_model.from_map(k))
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('UrlType') is not None:
            self.url_type = m.get('UrlType')
        return self


class ModifyChatappTemplateRequestComponentsCardsCardComponentsButtons(TeaModel):
    def __init__(
        self,
        phone_number: str = None,
        text: str = None,
        type: str = None,
        url: str = None,
        url_type: str = None,
    ):
        self.phone_number = phone_number
        self.text = text
        # This parameter is required.
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
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
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
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('UrlType') is not None:
            self.url_type = m.get('UrlType')
        return self


class ModifyChatappTemplateRequestComponentsCardsCardComponents(TeaModel):
    def __init__(
        self,
        buttons: List[ModifyChatappTemplateRequestComponentsCardsCardComponentsButtons] = None,
        format: str = None,
        text: str = None,
        type: str = None,
        url: str = None,
    ):
        self.buttons = buttons
        self.format = format
        self.text = text
        # This parameter is required.
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
        result['Buttons'] = []
        if self.buttons is not None:
            for k in self.buttons:
                result['Buttons'].append(k.to_map() if k else None)
        if self.format is not None:
            result['Format'] = self.format
        if self.text is not None:
            result['Text'] = self.text
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.buttons = []
        if m.get('Buttons') is not None:
            for k in m.get('Buttons'):
                temp_model = ModifyChatappTemplateRequestComponentsCardsCardComponentsButtons()
                self.buttons.append(temp_model.from_map(k))
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class ModifyChatappTemplateRequestComponentsCards(TeaModel):
    def __init__(
        self,
        card_components: List[ModifyChatappTemplateRequestComponentsCardsCardComponents] = None,
    ):
        # This parameter is required.
        self.card_components = card_components

    def validate(self):
        if self.card_components:
            for k in self.card_components:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CardComponents'] = []
        if self.card_components is not None:
            for k in self.card_components:
                result['CardComponents'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.card_components = []
        if m.get('CardComponents') is not None:
            for k in m.get('CardComponents'):
                temp_model = ModifyChatappTemplateRequestComponentsCardsCardComponents()
                self.card_components.append(temp_model.from_map(k))
        return self


class ModifyChatappTemplateRequestComponents(TeaModel):
    def __init__(
        self,
        add_secret_recommendation: bool = None,
        buttons: List[ModifyChatappTemplateRequestComponentsButtons] = None,
        caption: str = None,
        cards: List[ModifyChatappTemplateRequestComponentsCards] = None,
        code_expiration_minutes: int = None,
        duration: int = None,
        file_name: str = None,
        file_type: str = None,
        format: str = None,
        has_expiration: bool = None,
        text: str = None,
        thumb_url: str = None,
        type: str = None,
        url: str = None,
    ):
        # The note indicating that customers cannot share verification codes with others. The note is displayed in the message body. This parameter is valid only if Category is set to AUTHENTICATION and the Type sub-parameter of the Components parameter is set to BODY for a WhatsApp message template.
        self.add_secret_recommendation = add_secret_recommendation
        # The buttons. Specify this parameter only if you set the Type sub-parameter of the Components parameter to **BUTTONS**.
        # 
        # >  The following section describes the limits on the number of buttons in a WhatsApp message.
        # 
        # *   A marketing or utility WhatsApp message template supports up to 10 buttons.
        # 
        # *   A WhatsApp message template can contain only one phone call button.
        # 
        # *   A WhatsApp message template can contain up to two URL buttons.
        # 
        # *   In a WhatsApp message template, the quick reply button cannot be used together with the phone call button or the URL button.
        self.buttons = buttons
        # The description.
        # 
        # >  You can specify this parameter if the Type sub-parameter of the Components parameter is set to **HEADER** and the Format sub-parameter of the Components parameter is set to **IMAGE, DOCUMENT, or VIDEO**.
        self.caption = caption
        self.cards = cards
        # The validity period of the verification code in the WhatsApp authentication template. Unit: minutes. This parameter is valid only when Category is set to AUTHENTICATION and the Type sub-parameter of the Components parameter is set to FOOTER in a WhatsApp message template. The validity period of the verification code is displayed in the footer.
        self.code_expiration_minutes = code_expiration_minutes
        # The length of the video in the Viber message template. Unit: seconds. Valid values: 0 to 600.
        self.duration = duration
        # The name of the document.
        # 
        # >  You can specify this parameter if the Type sub-parameter of the Components parameter is set to **HEADER** and the Format sub-parameter of the Components parameter is set to **DOCUMENT**.
        self.file_name = file_name
        # The type of the document attached in the Viber message template.
        self.file_type = file_type
        # The type of the media resources that are included in the message. Valid values:
        # 
        # *   **TEXT**\
        # *   **IMAGE**\
        # *   **DOCUMENT**\
        # *   **VIDEO**\
        self.format = format
        self.has_expiration = has_expiration
        # The text of the message that you want to send.
        # 
        # >  If Category is set to AUTHENTICATION, the Text sub-parameter of the Components parameter is empty.
        self.text = text
        # The thumbnail URL of the video in the Viber message template.
        self.thumb_url = thumb_url
        # The type of the component. Valid values:
        # 
        # *   **BODY**\
        # *   **HEADER**\
        # *   **FOOTER**\
        # *   **BUTTONS**\
        # 
        # > 
        # 
        # *   The following limits apply to components in WhatsApp message templates: A **BODY** component cannot exceed 1,024 characters in length. A **HEADER** or **FOOTER** component cannot exceed 60 characters in length.
        # 
        # *   **FOOTER** components are not supported in Viber message templates.
        # 
        # *   In a Viber message template, media resources such as images, videos, and documents are placed in the **HEADER** component. If a Viber message contains text and images, the images are placed under the text in the message received on a device.
        # 
        # This parameter is required.
        self.type = type
        # The URL of the media resource.
        self.url = url

    def validate(self):
        if self.buttons:
            for k in self.buttons:
                if k:
                    k.validate()
        if self.cards:
            for k in self.cards:
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
        result['Cards'] = []
        if self.cards is not None:
            for k in self.cards:
                result['Cards'].append(k.to_map() if k else None)
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
        if self.has_expiration is not None:
            result['HasExpiration'] = self.has_expiration
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
        self.cards = []
        if m.get('Cards') is not None:
            for k in m.get('Cards'):
                temp_model = ModifyChatappTemplateRequestComponentsCards()
                self.cards.append(temp_model.from_map(k))
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
        if m.get('HasExpiration') is not None:
            self.has_expiration = m.get('HasExpiration')
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
        message_send_ttl_seconds: int = None,
        template_code: str = None,
        template_name: str = None,
        template_type: str = None,
    ):
        # The category of the Viber message template. Valid values:
        # 
        # *   **text**: the template that contains only text
        # *   **image**: the template that contains only images
        # *   **text_image_button**: the template that contains text, images, and buttons
        # *   **text_button**: the template that contains text and buttons
        # *   **document**: the template that contains only documents
        # *   **video**: the template that contains only videos
        # *   **text_video**: the template that contains text and videos
        # *   **text_video_button**: the template that contains text, videos, and buttons
        # *   **text_image**: the template that contains text and images
        # 
        # > This parameter applies only to Viber message templates.
        self.category = category
        # The components of the message template.
        # 
        # >  If Category is set to AUTHENTICATION, the Type sub-parameter of the Components parameter cannot be set to HEADER. If the Type sub-parameter is set to BODY or FOOTER, the Text sub-parameter of the Components parameter is empty and text in the body or footer is automatically generated.
        # 
        # This parameter is required.
        self.components = components
        # The space ID of the user within the ISV account.
        self.cust_space_id = cust_space_id
        # The WhatsApp Business account (WABA) ID of the user within the independent software vendor (ISV) account.
        # 
        # > CustWabaId is an obsolete parameter. Use CustSpaceId instead.
        self.cust_waba_id = cust_waba_id
        # The examples of variables that are used when you create the message template.
        self.example = example
        # The ISV verification code, which is used to verify whether the user is authorized by the ISV account.
        self.isv_code = isv_code
        # The language that is used in the message template. For more information, see [Language codes](https://help.aliyun.com/document_detail/463420.html).
        # 
        # This parameter is required.
        self.language = language
        # Validity period of authentication template message sending in WhatsApp
        # 
        # >This attribute requires providing waba in advance to Alibaba operators to open the whitelist, otherwise it will result in template submission failure
        self.message_send_ttl_seconds = message_send_ttl_seconds
        # The message template code.
        self.template_code = template_code
        self.template_name = template_name
        # The type of the message template.
        # 
        # *   **WHATSAPP**\
        # *   **VIBER**\
        # *   LINE: the Line message template. This type of message template will be released later.
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
        if self.message_send_ttl_seconds is not None:
            result['MessageSendTtlSeconds'] = self.message_send_ttl_seconds
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
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
        if m.get('MessageSendTtlSeconds') is not None:
            self.message_send_ttl_seconds = m.get('MessageSendTtlSeconds')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
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
        message_send_ttl_seconds: int = None,
        template_code: str = None,
        template_name: str = None,
        template_type: str = None,
    ):
        # The category of the Viber message template. Valid values:
        # 
        # *   **text**: the template that contains only text
        # *   **image**: the template that contains only images
        # *   **text_image_button**: the template that contains text, images, and buttons
        # *   **text_button**: the template that contains text and buttons
        # *   **document**: the template that contains only documents
        # *   **video**: the template that contains only videos
        # *   **text_video**: the template that contains text and videos
        # *   **text_video_button**: the template that contains text, videos, and buttons
        # *   **text_image**: the template that contains text and images
        # 
        # > This parameter applies only to Viber message templates.
        self.category = category
        # The components of the message template.
        # 
        # >  If Category is set to AUTHENTICATION, the Type sub-parameter of the Components parameter cannot be set to HEADER. If the Type sub-parameter is set to BODY or FOOTER, the Text sub-parameter of the Components parameter is empty and text in the body or footer is automatically generated.
        # 
        # This parameter is required.
        self.components_shrink = components_shrink
        # The space ID of the user within the ISV account.
        self.cust_space_id = cust_space_id
        # The WhatsApp Business account (WABA) ID of the user within the independent software vendor (ISV) account.
        # 
        # > CustWabaId is an obsolete parameter. Use CustSpaceId instead.
        self.cust_waba_id = cust_waba_id
        # The examples of variables that are used when you create the message template.
        self.example_shrink = example_shrink
        # The ISV verification code, which is used to verify whether the user is authorized by the ISV account.
        self.isv_code = isv_code
        # The language that is used in the message template. For more information, see [Language codes](https://help.aliyun.com/document_detail/463420.html).
        # 
        # This parameter is required.
        self.language = language
        # Validity period of authentication template message sending in WhatsApp
        # 
        # >This attribute requires providing waba in advance to Alibaba operators to open the whitelist, otherwise it will result in template submission failure
        self.message_send_ttl_seconds = message_send_ttl_seconds
        # The message template code.
        self.template_code = template_code
        self.template_name = template_name
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
        if self.message_send_ttl_seconds is not None:
            result['MessageSendTtlSeconds'] = self.message_send_ttl_seconds
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
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
        if m.get('MessageSendTtlSeconds') is not None:
            self.message_send_ttl_seconds = m.get('MessageSendTtlSeconds')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class ModifyChatappTemplateResponseBodyData(TeaModel):
    def __init__(
        self,
        template_code: str = None,
        template_name: str = None,
    ):
        # The code of the message template.
        self.template_code = template_code
        # The name of the message template.
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
        access_denied_detail: str = None,
        code: str = None,
        data: ModifyChatappTemplateResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
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
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
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


class ModifyFlowRequest(TeaModel):
    def __init__(
        self,
        categories: List[str] = None,
        cust_space_id: str = None,
        flow_id: str = None,
        flow_name: str = None,
    ):
        # The categories of the Flow.
        # 
        # This parameter is required.
        self.categories = categories
        # The space ID of the user within the independent software vendor (ISV) account.
        self.cust_space_id = cust_space_id
        # The Flow ID.
        self.flow_id = flow_id
        # The name of the Flow.
        # 
        # This parameter is required.
        self.flow_name = flow_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.categories is not None:
            result['Categories'] = self.categories
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        return self


class ModifyFlowShrinkRequest(TeaModel):
    def __init__(
        self,
        categories_shrink: str = None,
        cust_space_id: str = None,
        flow_id: str = None,
        flow_name: str = None,
    ):
        # The categories of the Flow.
        # 
        # This parameter is required.
        self.categories_shrink = categories_shrink
        # The space ID of the user within the independent software vendor (ISV) account.
        self.cust_space_id = cust_space_id
        # The Flow ID.
        self.flow_id = flow_id
        # The name of the Flow.
        # 
        # This parameter is required.
        self.flow_name = flow_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.categories_shrink is not None:
            result['Categories'] = self.categories_shrink
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories_shrink = m.get('Categories')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        return self


class ModifyFlowResponseBodyData(TeaModel):
    def __init__(
        self,
        categories: List[str] = None,
        flow_id: str = None,
        flow_name: str = None,
    ):
        # The categories of the Flow.
        self.categories = categories
        # The Flow ID.
        self.flow_id = flow_id
        # The name of the Flow.
        self.flow_name = flow_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.categories is not None:
            result['Categories'] = self.categories
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        return self


class ModifyFlowResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ModifyFlowResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # If OK is returned, the request was successful.
        self.code = code
        # The returned data.
        self.data = data
        # The error message.
        self.message = message
        # The request ID.
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
            temp_model = ModifyFlowResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyFlowResponseBody = None,
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
            temp_model = ModifyFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyPhoneBusinessProfileRequest(TeaModel):
    def __init__(
        self,
        about: str = None,
        address: str = None,
        cust_space_id: str = None,
        description: str = None,
        email: str = None,
        owner_id: int = None,
        phone_number: str = None,
        profile_picture_url: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        vertical: str = None,
        websites: List[str] = None,
    ):
        self.about = about
        # The space ID of the user under the independent software vendor (ISV) account.
        self.address = address
        # Modifies the business information of the account to which a specified phone number is bound.
        # 
        # This parameter is required.
        self.cust_space_id = cust_space_id
        # The address.
        self.description = description
        # The description.
        self.email = email
        self.owner_id = owner_id
        # You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        # 
        # This parameter is required.
        self.phone_number = phone_number
        # The industry.
        # 
        # > Enum: {OTHER, AUTO, BEAUTY, APPAREL, EDU, ENTERTAIN, EVENT_PLAN, FINANCE, GROCERY, GOVT, HOTEL, HEALTH, NONPROFIT, PROF_SERVICES, RETAIL, TRAVEL, RESTAURANT}
        self.profile_picture_url = profile_picture_url
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Sichuan
        self.vertical = vertical
        # The email address.
        self.websites = websites

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.about is not None:
            result['About'] = self.about
        if self.address is not None:
            result['Address'] = self.address
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.description is not None:
            result['Description'] = self.description
        if self.email is not None:
            result['Email'] = self.email
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.profile_picture_url is not None:
            result['ProfilePictureUrl'] = self.profile_picture_url
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.vertical is not None:
            result['Vertical'] = self.vertical
        if self.websites is not None:
            result['Websites'] = self.websites
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('About') is not None:
            self.about = m.get('About')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('ProfilePictureUrl') is not None:
            self.profile_picture_url = m.get('ProfilePictureUrl')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Vertical') is not None:
            self.vertical = m.get('Vertical')
        if m.get('Websites') is not None:
            self.websites = m.get('Websites')
        return self


class ModifyPhoneBusinessProfileShrinkRequest(TeaModel):
    def __init__(
        self,
        about: str = None,
        address: str = None,
        cust_space_id: str = None,
        description: str = None,
        email: str = None,
        owner_id: int = None,
        phone_number: str = None,
        profile_picture_url: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        vertical: str = None,
        websites_shrink: str = None,
    ):
        self.about = about
        # The space ID of the user under the independent software vendor (ISV) account.
        self.address = address
        # Modifies the business information of the account to which a specified phone number is bound.
        # 
        # This parameter is required.
        self.cust_space_id = cust_space_id
        # The address.
        self.description = description
        # The description.
        self.email = email
        self.owner_id = owner_id
        # You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        # 
        # This parameter is required.
        self.phone_number = phone_number
        # The industry.
        # 
        # > Enum: {OTHER, AUTO, BEAUTY, APPAREL, EDU, ENTERTAIN, EVENT_PLAN, FINANCE, GROCERY, GOVT, HOTEL, HEALTH, NONPROFIT, PROF_SERVICES, RETAIL, TRAVEL, RESTAURANT}
        self.profile_picture_url = profile_picture_url
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Sichuan
        self.vertical = vertical
        # The email address.
        self.websites_shrink = websites_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.about is not None:
            result['About'] = self.about
        if self.address is not None:
            result['Address'] = self.address
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.description is not None:
            result['Description'] = self.description
        if self.email is not None:
            result['Email'] = self.email
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.profile_picture_url is not None:
            result['ProfilePictureUrl'] = self.profile_picture_url
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.vertical is not None:
            result['Vertical'] = self.vertical
        if self.websites_shrink is not None:
            result['Websites'] = self.websites_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('About') is not None:
            self.about = m.get('About')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('ProfilePictureUrl') is not None:
            self.profile_picture_url = m.get('ProfilePictureUrl')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Vertical') is not None:
            self.vertical = m.get('Vertical')
        if m.get('Websites') is not None:
            self.websites_shrink = m.get('Websites')
        return self


class ModifyPhoneBusinessProfileResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        # The URL of the website.
        self.code = code
        # The ID of the request.
        self.message = message
        # The websites.
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
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


class PublishFlowRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        flow_id: str = None,
    ):
        # The space ID of the user within the independent software vendor (ISV) account.
        self.cust_space_id = cust_space_id
        # The Flow ID.
        # 
        # This parameter is required.
        self.flow_id = flow_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        return self


class PublishFlowResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # If OK is returned, the request was successful.
        self.code = code
        # The error message.
        self.message = message
        # The request ID.
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


class PublishFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PublishFlowResponseBody = None,
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
            temp_model = PublishFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryChatappBindWabaRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        isv_code: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The space ID of the user under the ISV account.
        self.cust_space_id = cust_space_id
        # The ISV verification code, which is used to verify whether the user is authorized by the ISV account.
        self.isv_code = isv_code
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

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
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('IsvCode') is not None:
            self.isv_code = m.get('IsvCode')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryChatappBindWabaResponseBodyData(TeaModel):
    def __init__(
        self,
        account_review_status: str = None,
        auth_international_rate_eligibility: Dict[str, Any] = None,
        currency: str = None,
        id: str = None,
        message_template_namespace: str = None,
        name: str = None,
        primary_business_location: str = None,
    ):
        # The review state of the WhatsApp Business account (WABA).
        # 
        # >  Valid values:
        # 
        # *   PENDING: The WABA is to be reviewed.
        # 
        # *   APPROVED: The WABA was approved.
        # 
        # *   REJECTED: The WABA was rejected.
        # 
        # *   DISABLED: The WABA was forbidden.
        self.account_review_status = account_review_status
        self.auth_international_rate_eligibility = auth_international_rate_eligibility
        # The currency.
        self.currency = currency
        # The ID of the WhatsApp Business account.
        self.id = id
        # The namespace of the message template.
        self.message_template_namespace = message_template_namespace
        # The name of the WhatsApp Business account.
        self.name = name
        self.primary_business_location = primary_business_location

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_review_status is not None:
            result['AccountReviewStatus'] = self.account_review_status
        if self.auth_international_rate_eligibility is not None:
            result['AuthInternationalRateEligibility'] = self.auth_international_rate_eligibility
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.id is not None:
            result['Id'] = self.id
        if self.message_template_namespace is not None:
            result['MessageTemplateNamespace'] = self.message_template_namespace
        if self.name is not None:
            result['Name'] = self.name
        if self.primary_business_location is not None:
            result['PrimaryBusinessLocation'] = self.primary_business_location
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountReviewStatus') is not None:
            self.account_review_status = m.get('AccountReviewStatus')
        if m.get('AuthInternationalRateEligibility') is not None:
            self.auth_international_rate_eligibility = m.get('AuthInternationalRateEligibility')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MessageTemplateNamespace') is not None:
            self.message_template_namespace = m.get('MessageTemplateNamespace')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PrimaryBusinessLocation') is not None:
            self.primary_business_location = m.get('PrimaryBusinessLocation')
        return self


class QueryChatappBindWabaResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: QueryChatappBindWabaResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        # The returned data.
        self.data = data
        # The error message returned.
        self.message = message
        # The ID of the request.
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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
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
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = QueryChatappBindWabaResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
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
        status: str = None,
    ):
        # The space ID of the user under the ISV account.
        self.cust_space_id = cust_space_id
        # The ISV verification code, which is used to verify whether the user is authorized by the ISV account.
        self.isv_code = isv_code
        self.status = status

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
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('IsvCode') is not None:
            self.isv_code = m.get('IsvCode')
        if m.get('Status') is not None:
            self.status = m.get('Status')
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
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        phone_numbers: List[QueryChatappPhoneNumbersResponseBodyPhoneNumbers] = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
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
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
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
        owner_id: int = None,
        phone_number: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The space ID of the user under the independent software vendor (ISV) account.
        # 
        # This parameter is required.
        self.cust_space_id = cust_space_id
        self.owner_id = owner_id
        # The phone number.
        # 
        # This parameter is required.
        self.phone_number = phone_number
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryPhoneBusinessProfileResponseBodyData(TeaModel):
    def __init__(
        self,
        about: str = None,
        address: str = None,
        description: str = None,
        email: str = None,
        profile_picture_url: str = None,
        vertical: str = None,
        websites: List[str] = None,
    ):
        self.about = about
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
        if self.about is not None:
            result['About'] = self.about
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
        if m.get('About') is not None:
            self.about = m.get('About')
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
        access_denied_detail: str = None,
        code: str = None,
        data: QueryPhoneBusinessProfileResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        # The data returned.
        self.data = data
        # The error message returned.
        self.message = message
        # The ID of the request.
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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
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
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = QueryPhoneBusinessProfileResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
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
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        waba_id: str = None,
    ):
        # The space ID of the user under the independent software vendor (ISV) account.
        # 
        # This parameter is required.
        self.cust_space_id = cust_space_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the WABA.
        # 
        # This parameter is required.
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
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.waba_id is not None:
            result['WabaId'] = self.waba_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
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
        access_denied_detail: str = None,
        code: str = None,
        data: QueryWabaBusinessInfoResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        # The business information about the WABA.
        self.data = data
        # The error message returned.
        self.message = message
        # The ID of the request.
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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
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
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = QueryWabaBusinessInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
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


class SendChatappMassMessageRequestSenderListFlowAction(TeaModel):
    def __init__(
        self,
        flow_action_data: Dict[str, str] = None,
        flow_token: str = None,
    ):
        self.flow_action_data = flow_action_data
        self.flow_token = flow_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_action_data is not None:
            result['FlowActionData'] = self.flow_action_data
        if self.flow_token is not None:
            result['FlowToken'] = self.flow_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowActionData') is not None:
            self.flow_action_data = m.get('FlowActionData')
        if m.get('FlowToken') is not None:
            self.flow_token = m.get('FlowToken')
        return self


class SendChatappMassMessageRequestSenderListProductActionSectionsProductItems(TeaModel):
    def __init__(
        self,
        product_retailer_id: str = None,
    ):
        # The retailer ID of the product.
        self.product_retailer_id = product_retailer_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_retailer_id is not None:
            result['ProductRetailerId'] = self.product_retailer_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductRetailerId') is not None:
            self.product_retailer_id = m.get('ProductRetailerId')
        return self


class SendChatappMassMessageRequestSenderListProductActionSections(TeaModel):
    def __init__(
        self,
        product_items: List[SendChatappMassMessageRequestSenderListProductActionSectionsProductItems] = None,
        title: str = None,
    ):
        # The products.
        self.product_items = product_items
        # The name of the category.
        self.title = title

    def validate(self):
        if self.product_items:
            for k in self.product_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ProductItems'] = []
        if self.product_items is not None:
            for k in self.product_items:
                result['ProductItems'].append(k.to_map() if k else None)
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.product_items = []
        if m.get('ProductItems') is not None:
            for k in m.get('ProductItems'):
                temp_model = SendChatappMassMessageRequestSenderListProductActionSectionsProductItems()
                self.product_items.append(temp_model.from_map(k))
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class SendChatappMassMessageRequestSenderListProductAction(TeaModel):
    def __init__(
        self,
        sections: List[SendChatappMassMessageRequestSenderListProductActionSections] = None,
        thumbnail_product_retailer_id: str = None,
    ):
        # The products. Up to 30 products and 10 categories can be added.
        self.sections = sections
        # The retailer ID of the product.
        self.thumbnail_product_retailer_id = thumbnail_product_retailer_id

    def validate(self):
        if self.sections:
            for k in self.sections:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Sections'] = []
        if self.sections is not None:
            for k in self.sections:
                result['Sections'].append(k.to_map() if k else None)
        if self.thumbnail_product_retailer_id is not None:
            result['ThumbnailProductRetailerId'] = self.thumbnail_product_retailer_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sections = []
        if m.get('Sections') is not None:
            for k in m.get('Sections'):
                temp_model = SendChatappMassMessageRequestSenderListProductActionSections()
                self.sections.append(temp_model.from_map(k))
        if m.get('ThumbnailProductRetailerId') is not None:
            self.thumbnail_product_retailer_id = m.get('ThumbnailProductRetailerId')
        return self


class SendChatappMassMessageRequestSenderList(TeaModel):
    def __init__(
        self,
        flow_action: SendChatappMassMessageRequestSenderListFlowAction = None,
        payload: List[str] = None,
        product_action: SendChatappMassMessageRequestSenderListProductAction = None,
        template_params: Dict[str, str] = None,
        to: str = None,
    ):
        self.flow_action = flow_action
        # The payload.
        self.payload = payload
        # The information about the product.
        self.product_action = product_action
        # The parameters of the template.
        self.template_params = template_params
        # The phone number to which the message is sent.
        # 
        # This parameter is required.
        self.to = to

    def validate(self):
        if self.flow_action:
            self.flow_action.validate()
        if self.product_action:
            self.product_action.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_action is not None:
            result['FlowAction'] = self.flow_action.to_map()
        if self.payload is not None:
            result['Payload'] = self.payload
        if self.product_action is not None:
            result['ProductAction'] = self.product_action.to_map()
        if self.template_params is not None:
            result['TemplateParams'] = self.template_params
        if self.to is not None:
            result['To'] = self.to
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowAction') is not None:
            temp_model = SendChatappMassMessageRequestSenderListFlowAction()
            self.flow_action = temp_model.from_map(m['FlowAction'])
        if m.get('Payload') is not None:
            self.payload = m.get('Payload')
        if m.get('ProductAction') is not None:
            temp_model = SendChatappMassMessageRequestSenderListProductAction()
            self.product_action = temp_model.from_map(m['ProductAction'])
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
        fall_back_rule: str = None,
        from_: str = None,
        isv_code: str = None,
        label: str = None,
        language: str = None,
        sender_list: List[SendChatappMassMessageRequestSenderList] = None,
        tag: str = None,
        task_id: str = None,
        template_code: str = None,
        template_name: str = None,
        ttl: int = None,
    ):
        # The channel type. Valid values: whatsapp, viber, and line.
        # 
        # This parameter is required.
        self.channel_type = channel_type
        # The space ID of the user.
        self.cust_space_id = cust_space_id
        # The ID of the WhatsApp Business account under the ISV account.
        self.cust_waba_id = cust_waba_id
        # The fallback content.
        self.fall_back_content = fall_back_content
        self.fall_back_duration = fall_back_duration
        # The ID of the fallback strategy.
        self.fall_back_id = fall_back_id
        # The fallback rule.
        # 
        # >  Valid values:
        # 
        # *   undelivered: A fallback is triggered if the WhatsApp message is not delivered to clients. When the WhatsApp message is being sent, the template parameters are verified. If the parameters fail to pass the verification, the message fails to be sent. Whether the template and phone number are prohibited is not verified. By default, this value is used when FallBackRule is left empty.
        # 
        # *   sentfailed: A fallback is triggered even if the template parameters including variables fail to pass the verification. If the channelType, type, messageType, to, and from parameters fail to pass the verification, a fallback is not triggered.
        self.fall_back_rule = fall_back_rule
        # The phone number of the message sender.
        # 
        # This parameter is required.
        self.from_ = from_
        # The ISV verification code, which is used to verify whether the user is authorized by the ISV account.
        self.isv_code = isv_code
        # The message type when the ChannelType parameter is set to viber. Valid values: promotion and transaction.
        self.label = label
        # The language. For more information about language codes, see [Language codes](https://help.aliyun.com/document_detail/463420.html).
        # 
        # This parameter is required.
        self.language = language
        # The phone numbers to which the message is sent.
        # 
        # This parameter is required.
        self.sender_list = sender_list
        # The tag information when the ChannelType parameter is set to viber.
        self.tag = tag
        # The ID of the task.
        self.task_id = task_id
        # The encoding of the message template.
        self.template_code = template_code
        self.template_name = template_name
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
        if self.fall_back_rule is not None:
            result['FallBackRule'] = self.fall_back_rule
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
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
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
        if m.get('FallBackRule') is not None:
            self.fall_back_rule = m.get('FallBackRule')
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
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
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
        fall_back_rule: str = None,
        from_: str = None,
        isv_code: str = None,
        label: str = None,
        language: str = None,
        sender_list_shrink: str = None,
        tag: str = None,
        task_id: str = None,
        template_code: str = None,
        template_name: str = None,
        ttl: int = None,
    ):
        # The channel type. Valid values: whatsapp, viber, and line.
        # 
        # This parameter is required.
        self.channel_type = channel_type
        # The space ID of the user.
        self.cust_space_id = cust_space_id
        # The ID of the WhatsApp Business account under the ISV account.
        self.cust_waba_id = cust_waba_id
        # The fallback content.
        self.fall_back_content = fall_back_content
        self.fall_back_duration = fall_back_duration
        # The ID of the fallback strategy.
        self.fall_back_id = fall_back_id
        # The fallback rule.
        # 
        # >  Valid values:
        # 
        # *   undelivered: A fallback is triggered if the WhatsApp message is not delivered to clients. When the WhatsApp message is being sent, the template parameters are verified. If the parameters fail to pass the verification, the message fails to be sent. Whether the template and phone number are prohibited is not verified. By default, this value is used when FallBackRule is left empty.
        # 
        # *   sentfailed: A fallback is triggered even if the template parameters including variables fail to pass the verification. If the channelType, type, messageType, to, and from parameters fail to pass the verification, a fallback is not triggered.
        self.fall_back_rule = fall_back_rule
        # The phone number of the message sender.
        # 
        # This parameter is required.
        self.from_ = from_
        # The ISV verification code, which is used to verify whether the user is authorized by the ISV account.
        self.isv_code = isv_code
        # The message type when the ChannelType parameter is set to viber. Valid values: promotion and transaction.
        self.label = label
        # The language. For more information about language codes, see [Language codes](https://help.aliyun.com/document_detail/463420.html).
        # 
        # This parameter is required.
        self.language = language
        # The phone numbers to which the message is sent.
        # 
        # This parameter is required.
        self.sender_list_shrink = sender_list_shrink
        # The tag information when the ChannelType parameter is set to viber.
        self.tag = tag
        # The ID of the task.
        self.task_id = task_id
        # The encoding of the message template.
        self.template_code = template_code
        self.template_name = template_name
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
        if self.fall_back_rule is not None:
            result['FallBackRule'] = self.fall_back_rule
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
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
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
        if m.get('FallBackRule') is not None:
            self.fall_back_rule = m.get('FallBackRule')
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
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        return self


class SendChatappMassMessageResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        group_message_id: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
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
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
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


class SendChatappMessageRequestFlowAction(TeaModel):
    def __init__(
        self,
        flow_action_data: Dict[str, str] = None,
        flow_token: str = None,
    ):
        # flow默认参数
        self.flow_action_data = flow_action_data
        # flow token信息
        self.flow_token = flow_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_action_data is not None:
            result['FlowActionData'] = self.flow_action_data
        if self.flow_token is not None:
            result['FlowToken'] = self.flow_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowActionData') is not None:
            self.flow_action_data = m.get('FlowActionData')
        if m.get('FlowToken') is not None:
            self.flow_token = m.get('FlowToken')
        return self


class SendChatappMessageRequestProductActionSectionsProductItems(TeaModel):
    def __init__(
        self,
        product_retailer_id: str = None,
    ):
        # The retailer ID of the product.
        self.product_retailer_id = product_retailer_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_retailer_id is not None:
            result['ProductRetailerId'] = self.product_retailer_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductRetailerId') is not None:
            self.product_retailer_id = m.get('ProductRetailerId')
        return self


class SendChatappMessageRequestProductActionSections(TeaModel):
    def __init__(
        self,
        product_items: List[SendChatappMessageRequestProductActionSectionsProductItems] = None,
        title: str = None,
    ):
        # The products.
        self.product_items = product_items
        # The name of the category.
        self.title = title

    def validate(self):
        if self.product_items:
            for k in self.product_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ProductItems'] = []
        if self.product_items is not None:
            for k in self.product_items:
                result['ProductItems'].append(k.to_map() if k else None)
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.product_items = []
        if m.get('ProductItems') is not None:
            for k in m.get('ProductItems'):
                temp_model = SendChatappMessageRequestProductActionSectionsProductItems()
                self.product_items.append(temp_model.from_map(k))
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class SendChatappMessageRequestProductAction(TeaModel):
    def __init__(
        self,
        sections: List[SendChatappMessageRequestProductActionSections] = None,
        thumbnail_product_retailer_id: str = None,
    ):
        # The products. Up to 30 products can be added. The products can be divided into up to 10 categories.
        self.sections = sections
        # The retailer ID of the product.
        self.thumbnail_product_retailer_id = thumbnail_product_retailer_id

    def validate(self):
        if self.sections:
            for k in self.sections:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Sections'] = []
        if self.sections is not None:
            for k in self.sections:
                result['Sections'].append(k.to_map() if k else None)
        if self.thumbnail_product_retailer_id is not None:
            result['ThumbnailProductRetailerId'] = self.thumbnail_product_retailer_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sections = []
        if m.get('Sections') is not None:
            for k in m.get('Sections'):
                temp_model = SendChatappMessageRequestProductActionSections()
                self.sections.append(temp_model.from_map(k))
        if m.get('ThumbnailProductRetailerId') is not None:
            self.thumbnail_product_retailer_id = m.get('ThumbnailProductRetailerId')
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
        fall_back_rule: str = None,
        flow_action: SendChatappMessageRequestFlowAction = None,
        from_: str = None,
        isv_code: str = None,
        label: str = None,
        language: str = None,
        message_type: str = None,
        payload: List[str] = None,
        product_action: SendChatappMessageRequestProductAction = None,
        tag: str = None,
        task_id: str = None,
        template_code: str = None,
        template_name: str = None,
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
        # 
        # This parameter is required.
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
        # Specifies the period of time after which the fallback Short Message Service (SMS) message is sent if the message receipt that indicates the message is delivered to customers is not received. If this parameter is left empty, the fallback SMS message is sent only when the **message fails to be sent** or **the message receipt that indicates the message is not delivered to customers** is received. Valid values: 60 to 43200. Unit: seconds.
        self.fall_back_duration = fall_back_duration
        # The ID of the fallback strategy. You can create a fallback strategy and view the information in the console.
        self.fall_back_id = fall_back_id
        # 回落规则。
        # 
        # > 取值范围
        # > - undelivered  消息不能发送到端时回落（在发送状态时模板、参数需要校验通过，模板被封、号码被封等不做校验）。参数值为空时默认使用此规则
        # > - sentFailed  消息在校验模板、模板变量等参数时，校验不通过也会回落。只会强校验channelType, type, messageType, to, from(是否存在) 几个参数。
        # 
        # <props="china">
        # 
        # > 中国站此字段无效
        self.fall_back_rule = fall_back_rule
        # Flow发送数据
        self.flow_action = flow_action
        # The phone number of the message sender.
        # 
        # > You can specify a mobile phone number that is registered for a WhatsApp account and is approved in the ChatAPP console.
        # 
        # This parameter is required.
        self.from_ = from_
        # The independent software vendor (ISV) verification code, which is used to verify whether the user is authorized by the ISV account.
        self.isv_code = isv_code
        # The type of the Viber message. This parameter is required if you set the ChannelType parameter to viber. Valid values: promotion and transaction.
        self.label = label
        # The language that is used in the message template. This parameter is required only if you set the Type parameter to **template**. For more information about language codes, see [Language codes](https://help.aliyun.com/document_detail/463420.html).
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
        # > For more information, see [Parameters of a message template](https://help.aliyun.com/document_detail/454530.html).
        self.message_type = message_type
        # The payload of the button.
        self.payload = payload
        # The information about the products included in the WhatsApp catalog message or multi-product message (MPM).
        self.product_action = product_action
        # The tag information of the Viber message.
        self.tag = tag
        # The ID of the task.
        self.task_id = task_id
        # The code of the message template. This parameter is required only if you set the Type parameter to **template**.
        self.template_code = template_code
        self.template_name = template_name
        # The variables of the message template.
        self.template_params = template_params
        # The phone number that receives the message.
        # 
        # This parameter is required.
        self.to = to
        # The tracking ID of the Viber message.
        self.tracking_data = tracking_data
        # The timeout period for sending the Viber message. Valid values: 30 to 1209600. Unit: seconds.
        self.ttl = ttl
        # The type of the message. Valid values:
        # 
        # *   **template**: a template message. A template message is sent based on a template that is created in the ChatAPP console and is approved. You can send template messages at any time based on your business requirements.
        # *   **message**: a custom message. You can send a custom message to a user only within 24 hours after you receive the last message from the user.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.flow_action:
            self.flow_action.validate()
        if self.product_action:
            self.product_action.validate()

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
        if self.fall_back_rule is not None:
            result['FallBackRule'] = self.fall_back_rule
        if self.flow_action is not None:
            result['FlowAction'] = self.flow_action.to_map()
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
        if self.product_action is not None:
            result['ProductAction'] = self.product_action.to_map()
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
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
        if m.get('FallBackRule') is not None:
            self.fall_back_rule = m.get('FallBackRule')
        if m.get('FlowAction') is not None:
            temp_model = SendChatappMessageRequestFlowAction()
            self.flow_action = temp_model.from_map(m['FlowAction'])
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
        if m.get('ProductAction') is not None:
            temp_model = SendChatappMessageRequestProductAction()
            self.product_action = temp_model.from_map(m['ProductAction'])
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
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
        fall_back_rule: str = None,
        flow_action_shrink: str = None,
        from_: str = None,
        isv_code: str = None,
        label: str = None,
        language: str = None,
        message_type: str = None,
        payload_shrink: str = None,
        product_action_shrink: str = None,
        tag: str = None,
        task_id: str = None,
        template_code: str = None,
        template_name: str = None,
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
        # 
        # This parameter is required.
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
        # Specifies the period of time after which the fallback Short Message Service (SMS) message is sent if the message receipt that indicates the message is delivered to customers is not received. If this parameter is left empty, the fallback SMS message is sent only when the **message fails to be sent** or **the message receipt that indicates the message is not delivered to customers** is received. Valid values: 60 to 43200. Unit: seconds.
        self.fall_back_duration = fall_back_duration
        # The ID of the fallback strategy. You can create a fallback strategy and view the information in the console.
        self.fall_back_id = fall_back_id
        # 回落规则。
        # 
        # > 取值范围
        # > - undelivered  消息不能发送到端时回落（在发送状态时模板、参数需要校验通过，模板被封、号码被封等不做校验）。参数值为空时默认使用此规则
        # > - sentFailed  消息在校验模板、模板变量等参数时，校验不通过也会回落。只会强校验channelType, type, messageType, to, from(是否存在) 几个参数。
        # 
        # <props="china">
        # 
        # > 中国站此字段无效
        self.fall_back_rule = fall_back_rule
        # Flow发送数据
        self.flow_action_shrink = flow_action_shrink
        # The phone number of the message sender.
        # 
        # > You can specify a mobile phone number that is registered for a WhatsApp account and is approved in the ChatAPP console.
        # 
        # This parameter is required.
        self.from_ = from_
        # The independent software vendor (ISV) verification code, which is used to verify whether the user is authorized by the ISV account.
        self.isv_code = isv_code
        # The type of the Viber message. This parameter is required if you set the ChannelType parameter to viber. Valid values: promotion and transaction.
        self.label = label
        # The language that is used in the message template. This parameter is required only if you set the Type parameter to **template**. For more information about language codes, see [Language codes](https://help.aliyun.com/document_detail/463420.html).
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
        # > For more information, see [Parameters of a message template](https://help.aliyun.com/document_detail/454530.html).
        self.message_type = message_type
        # The payload of the button.
        self.payload_shrink = payload_shrink
        # The information about the products included in the WhatsApp catalog message or multi-product message (MPM).
        self.product_action_shrink = product_action_shrink
        # The tag information of the Viber message.
        self.tag = tag
        # The ID of the task.
        self.task_id = task_id
        # The code of the message template. This parameter is required only if you set the Type parameter to **template**.
        self.template_code = template_code
        self.template_name = template_name
        # The variables of the message template.
        self.template_params_shrink = template_params_shrink
        # The phone number that receives the message.
        # 
        # This parameter is required.
        self.to = to
        # The tracking ID of the Viber message.
        self.tracking_data = tracking_data
        # The timeout period for sending the Viber message. Valid values: 30 to 1209600. Unit: seconds.
        self.ttl = ttl
        # The type of the message. Valid values:
        # 
        # *   **template**: a template message. A template message is sent based on a template that is created in the ChatAPP console and is approved. You can send template messages at any time based on your business requirements.
        # *   **message**: a custom message. You can send a custom message to a user only within 24 hours after you receive the last message from the user.
        # 
        # This parameter is required.
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
        if self.fall_back_rule is not None:
            result['FallBackRule'] = self.fall_back_rule
        if self.flow_action_shrink is not None:
            result['FlowAction'] = self.flow_action_shrink
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
        if self.product_action_shrink is not None:
            result['ProductAction'] = self.product_action_shrink
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
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
        if m.get('FallBackRule') is not None:
            self.fall_back_rule = m.get('FallBackRule')
        if m.get('FlowAction') is not None:
            self.flow_action_shrink = m.get('FlowAction')
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
        if m.get('ProductAction') is not None:
            self.product_action_shrink = m.get('ProductAction')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
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
        # *   Other values indicate that the call fails. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
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
        # 
        # This parameter is required.
        self.business_desc = business_desc
        # The email address of your business.
        # 
        # This parameter is required.
        self.contact_mail = contact_mail
        # The country code.
        # 
        # This parameter is required.
        self.country_id = country_id
        # The display name of your business.
        # 
        # This parameter is required.
        self.cust_name = cust_name
        # The space ID of the user under the ISV account.
        # 
        # This parameter is required.
        self.cust_space_id = cust_space_id
        # The ISV or Client Agreement.
        # 
        # > Before you upload files to Object Storage Service (OSS) servers, you must call the GetChatappUploadAuthorization operation to obtain the authentication information required to upload files. You can use the SDK provided by OSS to upload files. When you upload a file, you must set the key parameter value. To set the value for the key parameter, concatenate the value of the Dir parameter and the file name by using a forward slash (/). You can obtain the value of the Dir parameter by calling the GetChatappUploadAuthorization operation.
        # 
        # > The value of this parameter is the name of the uploaded file.
        # 
        # This parameter is required.
        self.isv_terms = isv_terms
        # The address of your business.
        # 
        # This parameter is required.
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
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
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
        # 
        # This parameter is required.
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
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
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


class UpdateCommerceSettingRequest(TeaModel):
    def __init__(
        self,
        cart_enable: bool = None,
        catalog_visible: bool = None,
        cust_space_id: str = None,
        owner_id: int = None,
        phone_number: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # Specifies whether to display the shopping cart button.
        # 
        # This parameter is required.
        self.cart_enable = cart_enable
        # Specifies whether to display the catalog button.
        # 
        # This parameter is required.
        self.catalog_visible = catalog_visible
        # The space ID of the user within the independent software vendor (ISV) account.
        # 
        # This parameter is required.
        self.cust_space_id = cust_space_id
        self.owner_id = owner_id
        # The phone number.
        # 
        # This parameter is required.
        self.phone_number = phone_number
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cart_enable is not None:
            result['CartEnable'] = self.cart_enable
        if self.catalog_visible is not None:
            result['CatalogVisible'] = self.catalog_visible
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CartEnable') is not None:
            self.cart_enable = m.get('CartEnable')
        if m.get('CatalogVisible') is not None:
            self.catalog_visible = m.get('CatalogVisible')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class UpdateCommerceSettingResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   Other values indicate that the request failed. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateCommerceSettingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateCommerceSettingResponseBody = None,
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
            temp_model = UpdateCommerceSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateConversationalAutomationRequestCommands(TeaModel):
    def __init__(
        self,
        command_description: str = None,
        command_name: str = None,
    ):
        self.command_description = command_description
        self.command_name = command_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command_description is not None:
            result['CommandDescription'] = self.command_description
        if self.command_name is not None:
            result['CommandName'] = self.command_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommandDescription') is not None:
            self.command_description = m.get('CommandDescription')
        if m.get('CommandName') is not None:
            self.command_name = m.get('CommandName')
        return self


class UpdateConversationalAutomationRequest(TeaModel):
    def __init__(
        self,
        commands: List[UpdateConversationalAutomationRequestCommands] = None,
        cust_space_id: str = None,
        enable_welcome_message: bool = None,
        owner_id: int = None,
        phone_number: str = None,
        prompts: List[str] = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.commands = commands
        # This parameter is required.
        self.cust_space_id = cust_space_id
        self.enable_welcome_message = enable_welcome_message
        self.owner_id = owner_id
        # This parameter is required.
        self.phone_number = phone_number
        self.prompts = prompts
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        if self.commands:
            for k in self.commands:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Commands'] = []
        if self.commands is not None:
            for k in self.commands:
                result['Commands'].append(k.to_map() if k else None)
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.enable_welcome_message is not None:
            result['EnableWelcomeMessage'] = self.enable_welcome_message
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.prompts is not None:
            result['Prompts'] = self.prompts
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.commands = []
        if m.get('Commands') is not None:
            for k in m.get('Commands'):
                temp_model = UpdateConversationalAutomationRequestCommands()
                self.commands.append(temp_model.from_map(k))
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('EnableWelcomeMessage') is not None:
            self.enable_welcome_message = m.get('EnableWelcomeMessage')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('Prompts') is not None:
            self.prompts = m.get('Prompts')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class UpdateConversationalAutomationShrinkRequest(TeaModel):
    def __init__(
        self,
        commands_shrink: str = None,
        cust_space_id: str = None,
        enable_welcome_message: bool = None,
        owner_id: int = None,
        phone_number: str = None,
        prompts_shrink: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.commands_shrink = commands_shrink
        # This parameter is required.
        self.cust_space_id = cust_space_id
        self.enable_welcome_message = enable_welcome_message
        self.owner_id = owner_id
        # This parameter is required.
        self.phone_number = phone_number
        self.prompts_shrink = prompts_shrink
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commands_shrink is not None:
            result['Commands'] = self.commands_shrink
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.enable_welcome_message is not None:
            result['EnableWelcomeMessage'] = self.enable_welcome_message
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.prompts_shrink is not None:
            result['Prompts'] = self.prompts_shrink
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Commands') is not None:
            self.commands_shrink = m.get('Commands')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('EnableWelcomeMessage') is not None:
            self.enable_welcome_message = m.get('EnableWelcomeMessage')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('Prompts') is not None:
            self.prompts_shrink = m.get('Prompts')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class UpdateConversationalAutomationResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateConversationalAutomationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateConversationalAutomationResponseBody = None,
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
            temp_model = UpdateConversationalAutomationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFlowJSONAssetRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        file_path: str = None,
        flow_id: str = None,
    ):
        self.cust_space_id = cust_space_id
        # This parameter is required.
        self.file_path = file_path
        # Flow ID。
        # 
        # This parameter is required.
        self.flow_id = flow_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.file_path is not None:
            result['FilePath'] = self.file_path
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        return self


class UpdateFlowJSONAssetResponseBodyData(TeaModel):
    def __init__(
        self,
        flow_id: str = None,
    ):
        # Flow ID。
        self.flow_id = flow_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        return self


class UpdateFlowJSONAssetResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: UpdateFlowJSONAssetResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request。
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
            temp_model = UpdateFlowJSONAssetResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateFlowJSONAssetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateFlowJSONAssetResponseBody = None,
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
            temp_model = UpdateFlowJSONAssetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePhoneEncryptionPublicKeyRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        encryption_public_key: str = None,
        phone_number: str = None,
    ):
        self.cust_space_id = cust_space_id
        # This parameter is required.
        self.encryption_public_key = encryption_public_key
        # This parameter is required.
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
        if self.encryption_public_key is not None:
            result['EncryptionPublicKey'] = self.encryption_public_key
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('EncryptionPublicKey') is not None:
            self.encryption_public_key = m.get('EncryptionPublicKey')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        return self


class UpdatePhoneEncryptionPublicKeyResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        # Id of the request。
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


class UpdatePhoneEncryptionPublicKeyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdatePhoneEncryptionPublicKeyResponseBody = None,
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
            temp_model = UpdatePhoneEncryptionPublicKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePhoneMessageQrdlRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        generate_qr_image: str = None,
        phone_number: str = None,
        prefilled_message: str = None,
        qrdl_code: str = None,
    ):
        self.cust_space_id = cust_space_id
        # This parameter is required.
        self.generate_qr_image = generate_qr_image
        # This parameter is required.
        self.phone_number = phone_number
        # This parameter is required.
        self.prefilled_message = prefilled_message
        # This parameter is required.
        self.qrdl_code = qrdl_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.generate_qr_image is not None:
            result['GenerateQrImage'] = self.generate_qr_image
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.prefilled_message is not None:
            result['PrefilledMessage'] = self.prefilled_message
        if self.qrdl_code is not None:
            result['QrdlCode'] = self.qrdl_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('GenerateQrImage') is not None:
            self.generate_qr_image = m.get('GenerateQrImage')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('PrefilledMessage') is not None:
            self.prefilled_message = m.get('PrefilledMessage')
        if m.get('QrdlCode') is not None:
            self.qrdl_code = m.get('QrdlCode')
        return self


class UpdatePhoneMessageQrdlResponseBodyData(TeaModel):
    def __init__(
        self,
        deep_link_url: str = None,
        generate_qr_image: str = None,
        phone_number: str = None,
        prefilled_message: str = None,
        qr_image_url: str = None,
        qrdl_code: str = None,
    ):
        self.deep_link_url = deep_link_url
        self.generate_qr_image = generate_qr_image
        self.phone_number = phone_number
        self.prefilled_message = prefilled_message
        self.qr_image_url = qr_image_url
        self.qrdl_code = qrdl_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deep_link_url is not None:
            result['DeepLinkUrl'] = self.deep_link_url
        if self.generate_qr_image is not None:
            result['GenerateQrImage'] = self.generate_qr_image
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.prefilled_message is not None:
            result['PrefilledMessage'] = self.prefilled_message
        if self.qr_image_url is not None:
            result['QrImageUrl'] = self.qr_image_url
        if self.qrdl_code is not None:
            result['QrdlCode'] = self.qrdl_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeepLinkUrl') is not None:
            self.deep_link_url = m.get('DeepLinkUrl')
        if m.get('GenerateQrImage') is not None:
            self.generate_qr_image = m.get('GenerateQrImage')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('PrefilledMessage') is not None:
            self.prefilled_message = m.get('PrefilledMessage')
        if m.get('QrImageUrl') is not None:
            self.qr_image_url = m.get('QrImageUrl')
        if m.get('QrdlCode') is not None:
            self.qrdl_code = m.get('QrdlCode')
        return self


class UpdatePhoneMessageQrdlResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: UpdatePhoneMessageQrdlResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request。
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
            temp_model = UpdatePhoneMessageQrdlResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdatePhoneMessageQrdlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdatePhoneMessageQrdlResponseBody = None,
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
            temp_model = UpdatePhoneMessageQrdlResponseBody()
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
        # This parameter is required.
        self.cust_space_id = cust_space_id
        self.http_flag = http_flag
        # This parameter is required.
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
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
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


