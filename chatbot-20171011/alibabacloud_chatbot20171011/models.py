# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class ActivatePerspectiveRequest(TeaModel):
    def __init__(
        self,
        perspective_id: str = None,
    ):
        self.perspective_id = perspective_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.perspective_id is not None:
            result['PerspectiveId'] = self.perspective_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PerspectiveId') is not None:
            self.perspective_id = m.get('PerspectiveId')
        return self


class ActivatePerspectiveResponseBody(TeaModel):
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


class ActivatePerspectiveResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ActivatePerspectiveResponseBody = None,
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
            temp_model = ActivatePerspectiveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddSynonymRequest(TeaModel):
    def __init__(
        self,
        core_word_name: str = None,
        synonym: str = None,
    ):
        self.core_word_name = core_word_name
        self.synonym = synonym

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.core_word_name is not None:
            result['CoreWordName'] = self.core_word_name
        if self.synonym is not None:
            result['Synonym'] = self.synonym
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoreWordName') is not None:
            self.core_word_name = m.get('CoreWordName')
        if m.get('Synonym') is not None:
            self.synonym = m.get('Synonym')
        return self


class AddSynonymResponseBody(TeaModel):
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


class AddSynonymResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddSynonymResponseBody = None,
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
            temp_model = AddSynonymResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AppendEntityMemberRequest(TeaModel):
    def __init__(
        self,
        entity_id: int = None,
        apply_type: str = None,
        member: str = None,
    ):
        self.entity_id = entity_id
        self.apply_type = apply_type
        self.member = member

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.apply_type is not None:
            result['ApplyType'] = self.apply_type
        if self.member is not None:
            result['Member'] = self.member
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('ApplyType') is not None:
            self.apply_type = m.get('ApplyType')
        if m.get('Member') is not None:
            self.member = m.get('Member')
        return self


class AppendEntityMemberResponseBody(TeaModel):
    def __init__(
        self,
        entity_id: str = None,
        request_id: str = None,
    ):
        self.entity_id = entity_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
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


class AppendEntityMemberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AppendEntityMemberResponseBody = None,
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
            temp_model = AppendEntityMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssociateRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        utterance: str = None,
        session_id: str = None,
        business_scope: str = None,
        recommend_num: int = None,
        perspective: List[str] = None,
    ):
        self.instance_id = instance_id
        self.utterance = utterance
        self.session_id = session_id
        self.business_scope = business_scope
        self.recommend_num = recommend_num
        self.perspective = perspective

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.utterance is not None:
            result['Utterance'] = self.utterance
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.business_scope is not None:
            result['BusinessScope'] = self.business_scope
        if self.recommend_num is not None:
            result['RecommendNum'] = self.recommend_num
        if self.perspective is not None:
            result['Perspective'] = self.perspective
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Utterance') is not None:
            self.utterance = m.get('Utterance')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('BusinessScope') is not None:
            self.business_scope = m.get('BusinessScope')
        if m.get('RecommendNum') is not None:
            self.recommend_num = m.get('RecommendNum')
        if m.get('Perspective') is not None:
            self.perspective = m.get('Perspective')
        return self


class AssociateResponseBodyAssociate(TeaModel):
    def __init__(
        self,
        title: str = None,
    ):
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class AssociateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        associate: List[AssociateResponseBodyAssociate] = None,
        session_id: str = None,
        message_id: str = None,
    ):
        self.request_id = request_id
        self.associate = associate
        self.session_id = session_id
        self.message_id = message_id

    def validate(self):
        if self.associate:
            for k in self.associate:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Associate'] = []
        if self.associate is not None:
            for k in self.associate:
                result['Associate'].append(k.to_map() if k else None)
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.associate = []
        if m.get('Associate') is not None:
            for k in m.get('Associate'):
                temp_model = AssociateResponseBodyAssociate()
                self.associate.append(temp_model.from_map(k))
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        return self


class AssociateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AssociateResponseBody = None,
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
            temp_model = AssociateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChatRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        session_id: str = None,
        knowledge_id: str = None,
        sender_id: str = None,
        sender_nick: str = None,
        tag: str = None,
        utterance: str = None,
        recommend: bool = None,
        recommend_num: int = None,
        intent_name: str = None,
        default_perspective: str = None,
        business_scope: str = None,
        vendor_param: str = None,
        emotion: bool = None,
        sand_box: bool = None,
        perspective: List[str] = None,
    ):
        self.instance_id = instance_id
        self.session_id = session_id
        self.knowledge_id = knowledge_id
        self.sender_id = sender_id
        self.sender_nick = sender_nick
        self.tag = tag
        self.utterance = utterance
        self.recommend = recommend
        self.recommend_num = recommend_num
        self.intent_name = intent_name
        self.default_perspective = default_perspective
        self.business_scope = business_scope
        self.vendor_param = vendor_param
        self.emotion = emotion
        self.sand_box = sand_box
        self.perspective = perspective

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        if self.sender_id is not None:
            result['SenderId'] = self.sender_id
        if self.sender_nick is not None:
            result['SenderNick'] = self.sender_nick
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.utterance is not None:
            result['Utterance'] = self.utterance
        if self.recommend is not None:
            result['Recommend'] = self.recommend
        if self.recommend_num is not None:
            result['RecommendNum'] = self.recommend_num
        if self.intent_name is not None:
            result['IntentName'] = self.intent_name
        if self.default_perspective is not None:
            result['DefaultPerspective'] = self.default_perspective
        if self.business_scope is not None:
            result['BusinessScope'] = self.business_scope
        if self.vendor_param is not None:
            result['VendorParam'] = self.vendor_param
        if self.emotion is not None:
            result['Emotion'] = self.emotion
        if self.sand_box is not None:
            result['SandBox'] = self.sand_box
        if self.perspective is not None:
            result['Perspective'] = self.perspective
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        if m.get('SenderId') is not None:
            self.sender_id = m.get('SenderId')
        if m.get('SenderNick') is not None:
            self.sender_nick = m.get('SenderNick')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Utterance') is not None:
            self.utterance = m.get('Utterance')
        if m.get('Recommend') is not None:
            self.recommend = m.get('Recommend')
        if m.get('RecommendNum') is not None:
            self.recommend_num = m.get('RecommendNum')
        if m.get('IntentName') is not None:
            self.intent_name = m.get('IntentName')
        if m.get('DefaultPerspective') is not None:
            self.default_perspective = m.get('DefaultPerspective')
        if m.get('BusinessScope') is not None:
            self.business_scope = m.get('BusinessScope')
        if m.get('VendorParam') is not None:
            self.vendor_param = m.get('VendorParam')
        if m.get('Emotion') is not None:
            self.emotion = m.get('Emotion')
        if m.get('SandBox') is not None:
            self.sand_box = m.get('SandBox')
        if m.get('Perspective') is not None:
            self.perspective = m.get('Perspective')
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
        hit_statement: str = None,
        summary: str = None,
        related_knowledges: List[ChatResponseBodyMessagesKnowledgeRelatedKnowledges] = None,
        category: str = None,
        title: str = None,
        content: str = None,
        answer_source: str = None,
        id: str = None,
    ):
        self.hit_statement = hit_statement
        self.summary = summary
        self.related_knowledges = related_knowledges
        self.category = category
        self.title = title
        self.content = content
        self.answer_source = answer_source
        self.id = id

    def validate(self):
        if self.related_knowledges:
            for k in self.related_knowledges:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.hit_statement is not None:
            result['HitStatement'] = self.hit_statement
        if self.summary is not None:
            result['Summary'] = self.summary
        result['RelatedKnowledges'] = []
        if self.related_knowledges is not None:
            for k in self.related_knowledges:
                result['RelatedKnowledges'].append(k.to_map() if k else None)
        if self.category is not None:
            result['Category'] = self.category
        if self.title is not None:
            result['Title'] = self.title
        if self.content is not None:
            result['Content'] = self.content
        if self.answer_source is not None:
            result['AnswerSource'] = self.answer_source
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HitStatement') is not None:
            self.hit_statement = m.get('HitStatement')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        self.related_knowledges = []
        if m.get('RelatedKnowledges') is not None:
            for k in m.get('RelatedKnowledges'):
                temp_model = ChatResponseBodyMessagesKnowledgeRelatedKnowledges()
                self.related_knowledges.append(temp_model.from_map(k))
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('AnswerSource') is not None:
            self.answer_source = m.get('AnswerSource')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ChatResponseBodyMessagesTextSlots(TeaModel):
    def __init__(
        self,
        value: str = None,
        origin: str = None,
        name: str = None,
        is_hit: bool = None,
    ):
        self.value = value
        self.origin = origin
        self.name = name
        self.is_hit = is_hit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.origin is not None:
            result['Origin'] = self.origin
        if self.name is not None:
            result['Name'] = self.name
        if self.is_hit is not None:
            result['IsHit'] = self.is_hit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Origin') is not None:
            self.origin = m.get('Origin')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('IsHit') is not None:
            self.is_hit = m.get('IsHit')
        return self


class ChatResponseBodyMessagesText(TeaModel):
    def __init__(
        self,
        hit_statement: str = None,
        dialog_name: str = None,
        article_title: str = None,
        answer_source: str = None,
        slots: List[ChatResponseBodyMessagesTextSlots] = None,
        intent_name: str = None,
        meta_data: str = None,
        node_name: str = None,
        external_flags: Dict[str, Any] = None,
        ext: Dict[str, Any] = None,
        user_defined_chat_title: str = None,
        content: str = None,
        node_id: str = None,
    ):
        self.hit_statement = hit_statement
        self.dialog_name = dialog_name
        self.article_title = article_title
        self.answer_source = answer_source
        self.slots = slots
        self.intent_name = intent_name
        self.meta_data = meta_data
        self.node_name = node_name
        self.external_flags = external_flags
        self.ext = ext
        self.user_defined_chat_title = user_defined_chat_title
        self.content = content
        self.node_id = node_id

    def validate(self):
        if self.slots:
            for k in self.slots:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.hit_statement is not None:
            result['HitStatement'] = self.hit_statement
        if self.dialog_name is not None:
            result['DialogName'] = self.dialog_name
        if self.article_title is not None:
            result['ArticleTitle'] = self.article_title
        if self.answer_source is not None:
            result['AnswerSource'] = self.answer_source
        result['Slots'] = []
        if self.slots is not None:
            for k in self.slots:
                result['Slots'].append(k.to_map() if k else None)
        if self.intent_name is not None:
            result['IntentName'] = self.intent_name
        if self.meta_data is not None:
            result['MetaData'] = self.meta_data
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.external_flags is not None:
            result['ExternalFlags'] = self.external_flags
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.user_defined_chat_title is not None:
            result['UserDefinedChatTitle'] = self.user_defined_chat_title
        if self.content is not None:
            result['Content'] = self.content
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HitStatement') is not None:
            self.hit_statement = m.get('HitStatement')
        if m.get('DialogName') is not None:
            self.dialog_name = m.get('DialogName')
        if m.get('ArticleTitle') is not None:
            self.article_title = m.get('ArticleTitle')
        if m.get('AnswerSource') is not None:
            self.answer_source = m.get('AnswerSource')
        self.slots = []
        if m.get('Slots') is not None:
            for k in m.get('Slots'):
                temp_model = ChatResponseBodyMessagesTextSlots()
                self.slots.append(temp_model.from_map(k))
        if m.get('IntentName') is not None:
            self.intent_name = m.get('IntentName')
        if m.get('MetaData') is not None:
            self.meta_data = m.get('MetaData')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('ExternalFlags') is not None:
            self.external_flags = m.get('ExternalFlags')
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('UserDefinedChatTitle') is not None:
            self.user_defined_chat_title = m.get('UserDefinedChatTitle')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        return self


class ChatResponseBodyMessagesRecommends(TeaModel):
    def __init__(
        self,
        summary: str = None,
        knowledge_id: str = None,
        category: str = None,
        title: str = None,
        answer_source: str = None,
        content: str = None,
    ):
        self.summary = summary
        self.knowledge_id = knowledge_id
        self.category = category
        self.title = title
        self.answer_source = answer_source
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.summary is not None:
            result['Summary'] = self.summary
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        if self.category is not None:
            result['Category'] = self.category
        if self.title is not None:
            result['Title'] = self.title
        if self.answer_source is not None:
            result['AnswerSource'] = self.answer_source
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('AnswerSource') is not None:
            self.answer_source = m.get('AnswerSource')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class ChatResponseBodyMessages(TeaModel):
    def __init__(
        self,
        type: str = None,
        knowledge: ChatResponseBodyMessagesKnowledge = None,
        text: ChatResponseBodyMessagesText = None,
        recommends: List[ChatResponseBodyMessagesRecommends] = None,
    ):
        self.type = type
        self.knowledge = knowledge
        self.text = text
        self.recommends = recommends

    def validate(self):
        if self.knowledge:
            self.knowledge.validate()
        if self.text:
            self.text.validate()
        if self.recommends:
            for k in self.recommends:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.knowledge is not None:
            result['Knowledge'] = self.knowledge.to_map()
        if self.text is not None:
            result['Text'] = self.text.to_map()
        result['Recommends'] = []
        if self.recommends is not None:
            for k in self.recommends:
                result['Recommends'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Knowledge') is not None:
            temp_model = ChatResponseBodyMessagesKnowledge()
            self.knowledge = temp_model.from_map(m['Knowledge'])
        if m.get('Text') is not None:
            temp_model = ChatResponseBodyMessagesText()
            self.text = temp_model.from_map(m['Text'])
        self.recommends = []
        if m.get('Recommends') is not None:
            for k in m.get('Recommends'):
                temp_model = ChatResponseBodyMessagesRecommends()
                self.recommends.append(temp_model.from_map(k))
        return self


class ChatResponseBody(TeaModel):
    def __init__(
        self,
        messages: List[ChatResponseBodyMessages] = None,
        request_id: str = None,
        tag: str = None,
        session_id: str = None,
        message_id: str = None,
    ):
        self.messages = messages
        self.request_id = request_id
        self.tag = tag
        self.session_id = session_id
        self.message_id = message_id

    def validate(self):
        if self.messages:
            for k in self.messages:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Messages'] = []
        if self.messages is not None:
            for k in self.messages:
                result['Messages'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.messages = []
        if m.get('Messages') is not None:
            for k in m.get('Messages'):
                temp_model = ChatResponseBodyMessages()
                self.messages.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        return self


class ChatResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ChatResponseBody = None,
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
            temp_model = ChatResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateBotRequest(TeaModel):
    def __init__(
        self,
        language_code: str = None,
        time_zone: str = None,
        name: str = None,
        avatar: str = None,
        introduction: str = None,
        robot_type: str = None,
    ):
        self.language_code = language_code
        self.time_zone = time_zone
        self.name = name
        self.avatar = avatar
        self.introduction = introduction
        self.robot_type = robot_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.language_code is not None:
            result['LanguageCode'] = self.language_code
        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone
        if self.name is not None:
            result['Name'] = self.name
        if self.avatar is not None:
            result['Avatar'] = self.avatar
        if self.introduction is not None:
            result['Introduction'] = self.introduction
        if self.robot_type is not None:
            result['RobotType'] = self.robot_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LanguageCode') is not None:
            self.language_code = m.get('LanguageCode')
        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Avatar') is not None:
            self.avatar = m.get('Avatar')
        if m.get('Introduction') is not None:
            self.introduction = m.get('Introduction')
        if m.get('RobotType') is not None:
            self.robot_type = m.get('RobotType')
        return self


class CreateBotResponseBody(TeaModel):
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


class CreateBotResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateBotResponseBody = None,
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
            temp_model = CreateBotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCategoryRequest(TeaModel):
    def __init__(
        self,
        parent_category_id: int = None,
        name: str = None,
    ):
        self.parent_category_id = parent_category_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.parent_category_id is not None:
            result['ParentCategoryId'] = self.parent_category_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParentCategoryId') is not None:
            self.parent_category_id = m.get('ParentCategoryId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateCategoryResponseBody(TeaModel):
    def __init__(
        self,
        category_id: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.category_id = category_id
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateCategoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateCategoryResponseBody = None,
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
            temp_model = CreateCategoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCoreWordRequest(TeaModel):
    def __init__(
        self,
        core_word_name: str = None,
    ):
        self.core_word_name = core_word_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.core_word_name is not None:
            result['CoreWordName'] = self.core_word_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoreWordName') is not None:
            self.core_word_name = m.get('CoreWordName')
        return self


class CreateCoreWordResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        core_word_code: str = None,
    ):
        self.request_id = request_id
        self.core_word_code = core_word_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.core_word_code is not None:
            result['CoreWordCode'] = self.core_word_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CoreWordCode') is not None:
            self.core_word_code = m.get('CoreWordCode')
        return self


class CreateCoreWordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateCoreWordResponseBody = None,
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
            temp_model = CreateCoreWordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDialogRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        dialog_name: str = None,
        description: str = None,
    ):
        self.instance_id = instance_id
        self.dialog_name = dialog_name
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.dialog_name is not None:
            result['DialogName'] = self.dialog_name
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DialogName') is not None:
            self.dialog_name = m.get('DialogName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class CreateDialogResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        dialog_id: str = None,
    ):
        self.request_id = request_id
        self.dialog_id = dialog_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')
        return self


class CreateDialogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDialogResponseBody = None,
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
            temp_model = CreateDialogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEntityRequest(TeaModel):
    def __init__(
        self,
        dialog_id: int = None,
        entity_name: str = None,
        entity_type: str = None,
        regex: str = None,
        members: str = None,
    ):
        self.dialog_id = dialog_id
        self.entity_name = entity_name
        self.entity_type = entity_type
        self.regex = regex
        self.members = members

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        if self.entity_name is not None:
            result['EntityName'] = self.entity_name
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.regex is not None:
            result['Regex'] = self.regex
        if self.members is not None:
            result['Members'] = self.members
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')
        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('Regex') is not None:
            self.regex = m.get('Regex')
        if m.get('Members') is not None:
            self.members = m.get('Members')
        return self


class CreateEntityResponseBody(TeaModel):
    def __init__(
        self,
        entity_id: str = None,
        request_id: str = None,
    ):
        self.entity_id = entity_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
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


class CreateEntityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateEntityResponseBody = None,
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
            temp_model = CreateEntityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateIntentRequest(TeaModel):
    def __init__(
        self,
        intent_definition: str = None,
        dialog_id: int = None,
    ):
        self.intent_definition = intent_definition
        self.dialog_id = dialog_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.intent_definition is not None:
            result['IntentDefinition'] = self.intent_definition
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IntentDefinition') is not None:
            self.intent_definition = m.get('IntentDefinition')
        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')
        return self


class CreateIntentResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        intent_id: str = None,
    ):
        self.request_id = request_id
        self.intent_id = intent_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        return self


class CreateIntentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateIntentResponseBody = None,
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
            temp_model = CreateIntentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateKnowledgeRequest(TeaModel):
    def __init__(
        self,
        knowledge: str = None,
    ):
        self.knowledge = knowledge

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.knowledge is not None:
            result['Knowledge'] = self.knowledge
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Knowledge') is not None:
            self.knowledge = m.get('Knowledge')
        return self


class CreateKnowledgeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        knowledge_id: int = None,
    ):
        self.request_id = request_id
        self.knowledge_id = knowledge_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        return self


class CreateKnowledgeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateKnowledgeResponseBody = None,
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
            temp_model = CreateKnowledgeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteBotRequest(TeaModel):
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


class DeleteBotResponseBody(TeaModel):
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


class DeleteBotResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteBotResponseBody = None,
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
            temp_model = DeleteBotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCategoryRequest(TeaModel):
    def __init__(
        self,
        category_id: int = None,
    ):
        self.category_id = category_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        return self


class DeleteCategoryResponseBody(TeaModel):
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


class DeleteCategoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteCategoryResponseBody = None,
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
            temp_model = DeleteCategoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCoreWordRequest(TeaModel):
    def __init__(
        self,
        core_word_name: str = None,
    ):
        self.core_word_name = core_word_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.core_word_name is not None:
            result['CoreWordName'] = self.core_word_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoreWordName') is not None:
            self.core_word_name = m.get('CoreWordName')
        return self


class DeleteCoreWordResponseBody(TeaModel):
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


class DeleteCoreWordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteCoreWordResponseBody = None,
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
            temp_model = DeleteCoreWordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDialogRequest(TeaModel):
    def __init__(
        self,
        dialog_id: int = None,
    ):
        self.dialog_id = dialog_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')
        return self


class DeleteDialogResponseBody(TeaModel):
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


class DeleteDialogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteDialogResponseBody = None,
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
            temp_model = DeleteDialogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEntityRequest(TeaModel):
    def __init__(
        self,
        entity_id: int = None,
    ):
        self.entity_id = entity_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        return self


class DeleteEntityResponseBody(TeaModel):
    def __init__(
        self,
        entity_id: str = None,
        request_id: str = None,
    ):
        self.entity_id = entity_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
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


class DeleteEntityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteEntityResponseBody = None,
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
            temp_model = DeleteEntityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteIntentRequest(TeaModel):
    def __init__(
        self,
        intent_id: int = None,
    ):
        self.intent_id = intent_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        return self


class DeleteIntentResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        intent_id: str = None,
    ):
        self.request_id = request_id
        self.intent_id = intent_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        return self


class DeleteIntentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteIntentResponseBody = None,
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
            temp_model = DeleteIntentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteKnowledgeRequest(TeaModel):
    def __init__(
        self,
        knowledge_id: int = None,
    ):
        self.knowledge_id = knowledge_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        return self


class DeleteKnowledgeResponseBody(TeaModel):
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


class DeleteKnowledgeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteKnowledgeResponseBody = None,
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
            temp_model = DeleteKnowledgeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBotRequest(TeaModel):
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


class DescribeBotResponseBodyCategories(TeaModel):
    def __init__(
        self,
        category_id: int = None,
        name: str = None,
        parent_category_id: int = None,
    ):
        self.category_id = category_id
        self.name = name
        self.parent_category_id = parent_category_id

    def validate(self):
        pass

    def to_map(self):
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


class DescribeBotResponseBody(TeaModel):
    def __init__(
        self,
        language_code: str = None,
        time_zone: str = None,
        request_id: str = None,
        introduction: str = None,
        instance_id: str = None,
        categories: List[DescribeBotResponseBodyCategories] = None,
        create_time: str = None,
        avatar: str = None,
        logo: str = None,
        name: str = None,
    ):
        self.language_code = language_code
        self.time_zone = time_zone
        self.request_id = request_id
        self.introduction = introduction
        self.instance_id = instance_id
        self.categories = categories
        self.create_time = create_time
        self.avatar = avatar
        self.logo = logo
        self.name = name

    def validate(self):
        if self.categories:
            for k in self.categories:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.language_code is not None:
            result['LanguageCode'] = self.language_code
        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.introduction is not None:
            result['Introduction'] = self.introduction
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        result['Categories'] = []
        if self.categories is not None:
            for k in self.categories:
                result['Categories'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.avatar is not None:
            result['Avatar'] = self.avatar
        if self.logo is not None:
            result['Logo'] = self.logo
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LanguageCode') is not None:
            self.language_code = m.get('LanguageCode')
        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Introduction') is not None:
            self.introduction = m.get('Introduction')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        self.categories = []
        if m.get('Categories') is not None:
            for k in m.get('Categories'):
                temp_model = DescribeBotResponseBodyCategories()
                self.categories.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Avatar') is not None:
            self.avatar = m.get('Avatar')
        if m.get('Logo') is not None:
            self.logo = m.get('Logo')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeBotResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeBotResponseBody = None,
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
            temp_model = DescribeBotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCategoryRequest(TeaModel):
    def __init__(
        self,
        category_id: int = None,
    ):
        self.category_id = category_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        return self


class DescribeCategoryResponseBody(TeaModel):
    def __init__(
        self,
        category_id: int = None,
        request_id: str = None,
        parent_category_id: int = None,
        name: str = None,
    ):
        self.category_id = category_id
        self.request_id = request_id
        self.parent_category_id = parent_category_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.parent_category_id is not None:
            result['ParentCategoryId'] = self.parent_category_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ParentCategoryId') is not None:
            self.parent_category_id = m.get('ParentCategoryId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeCategoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCategoryResponseBody = None,
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
            temp_model = DescribeCategoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCoreWordRequest(TeaModel):
    def __init__(
        self,
        core_word_name: str = None,
    ):
        self.core_word_name = core_word_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.core_word_name is not None:
            result['CoreWordName'] = self.core_word_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoreWordName') is not None:
            self.core_word_name = m.get('CoreWordName')
        return self


class DescribeCoreWordResponseBody(TeaModel):
    def __init__(
        self,
        core_word_name: str = None,
        synonyms: List[str] = None,
        modify_time: str = None,
        request_id: str = None,
        create_time: str = None,
        core_word_code: str = None,
    ):
        self.core_word_name = core_word_name
        self.synonyms = synonyms
        self.modify_time = modify_time
        self.request_id = request_id
        self.create_time = create_time
        self.core_word_code = core_word_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.core_word_name is not None:
            result['CoreWordName'] = self.core_word_name
        if self.synonyms is not None:
            result['Synonyms'] = self.synonyms
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.core_word_code is not None:
            result['CoreWordCode'] = self.core_word_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoreWordName') is not None:
            self.core_word_name = m.get('CoreWordName')
        if m.get('Synonyms') is not None:
            self.synonyms = m.get('Synonyms')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CoreWordCode') is not None:
            self.core_word_code = m.get('CoreWordCode')
        return self


class DescribeCoreWordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCoreWordResponseBody = None,
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
            temp_model = DescribeCoreWordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDialogRequest(TeaModel):
    def __init__(
        self,
        dialog_id: int = None,
    ):
        self.dialog_id = dialog_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')
        return self


class DescribeDialogResponseBody(TeaModel):
    def __init__(
        self,
        status: int = None,
        modify_time: str = None,
        description: str = None,
        request_id: str = None,
        create_time: str = None,
        create_user_id: str = None,
        dialog_id: int = None,
        create_user_name: str = None,
        is_online: bool = None,
        dialog_name: str = None,
        modify_user_id: str = None,
        modify_user_name: str = None,
        is_sample_dialog: bool = None,
    ):
        self.status = status
        self.modify_time = modify_time
        self.description = description
        self.request_id = request_id
        self.create_time = create_time
        self.create_user_id = create_user_id
        self.dialog_id = dialog_id
        self.create_user_name = create_user_name
        self.is_online = is_online
        self.dialog_name = dialog_name
        self.modify_user_id = modify_user_id
        self.modify_user_name = modify_user_name
        self.is_sample_dialog = is_sample_dialog

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
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.is_online is not None:
            result['IsOnline'] = self.is_online
        if self.dialog_name is not None:
            result['DialogName'] = self.dialog_name
        if self.modify_user_id is not None:
            result['ModifyUserId'] = self.modify_user_id
        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name
        if self.is_sample_dialog is not None:
            result['IsSampleDialog'] = self.is_sample_dialog
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
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('IsOnline') is not None:
            self.is_online = m.get('IsOnline')
        if m.get('DialogName') is not None:
            self.dialog_name = m.get('DialogName')
        if m.get('ModifyUserId') is not None:
            self.modify_user_id = m.get('ModifyUserId')
        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')
        if m.get('IsSampleDialog') is not None:
            self.is_sample_dialog = m.get('IsSampleDialog')
        return self


class DescribeDialogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDialogResponseBody = None,
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
            temp_model = DescribeDialogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePerspectiveRequest(TeaModel):
    def __init__(
        self,
        perspective_id: str = None,
    ):
        self.perspective_id = perspective_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.perspective_id is not None:
            result['PerspectiveId'] = self.perspective_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PerspectiveId') is not None:
            self.perspective_id = m.get('PerspectiveId')
        return self


class DescribePerspectiveResponseBody(TeaModel):
    def __init__(
        self,
        status: int = None,
        perspective_code: str = None,
        modify_time: str = None,
        request_id: str = None,
        self_define: bool = None,
        create_time: str = None,
        modify_user_name: str = None,
        perspective_id: str = None,
        create_user_name: str = None,
        name: str = None,
    ):
        self.status = status
        self.perspective_code = perspective_code
        self.modify_time = modify_time
        self.request_id = request_id
        self.self_define = self_define
        self.create_time = create_time
        self.modify_user_name = modify_user_name
        self.perspective_id = perspective_id
        self.create_user_name = create_user_name
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.perspective_code is not None:
            result['PerspectiveCode'] = self.perspective_code
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.self_define is not None:
            result['SelfDefine'] = self.self_define
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name
        if self.perspective_id is not None:
            result['PerspectiveId'] = self.perspective_id
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('PerspectiveCode') is not None:
            self.perspective_code = m.get('PerspectiveCode')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SelfDefine') is not None:
            self.self_define = m.get('SelfDefine')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')
        if m.get('PerspectiveId') is not None:
            self.perspective_id = m.get('PerspectiveId')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribePerspectiveResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribePerspectiveResponseBody = None,
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
            temp_model = DescribePerspectiveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableDialogFlowRequest(TeaModel):
    def __init__(
        self,
        dialog_id: int = None,
    ):
        self.dialog_id = dialog_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')
        return self


class DisableDialogFlowResponseBody(TeaModel):
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


class DisableDialogFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DisableDialogFlowResponseBody = None,
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
            temp_model = DisableDialogFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableKnowledgeRequest(TeaModel):
    def __init__(
        self,
        knowledge_id: int = None,
    ):
        self.knowledge_id = knowledge_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        return self


class DisableKnowledgeResponseBody(TeaModel):
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


class DisableKnowledgeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DisableKnowledgeResponseBody = None,
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
            temp_model = DisableKnowledgeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FeedbackRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        session_id: str = None,
        message_id: str = None,
        feedback: str = None,
    ):
        self.instance_id = instance_id
        self.session_id = session_id
        self.message_id = message_id
        self.feedback = feedback

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        if self.feedback is not None:
            result['Feedback'] = self.feedback
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        if m.get('Feedback') is not None:
            self.feedback = m.get('Feedback')
        return self


class FeedbackResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        feedback: str = None,
        message_id: str = None,
    ):
        self.request_id = request_id
        self.feedback = feedback
        self.message_id = message_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.feedback is not None:
            result['Feedback'] = self.feedback
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Feedback') is not None:
            self.feedback = m.get('Feedback')
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        return self


class FeedbackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: FeedbackResponseBody = None,
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
            temp_model = FeedbackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBotChatDataRequest(TeaModel):
    def __init__(
        self,
        cube_id: str = None,
        measures: str = None,
        start_time: str = None,
        end_time: str = None,
        robot_instance_id: str = None,
    ):
        self.cube_id = cube_id
        self.measures = measures
        self.start_time = start_time
        self.end_time = end_time
        self.robot_instance_id = robot_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cube_id is not None:
            result['CubeId'] = self.cube_id
        if self.measures is not None:
            result['Measures'] = self.measures
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.robot_instance_id is not None:
            result['RobotInstanceId'] = self.robot_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CubeId') is not None:
            self.cube_id = m.get('CubeId')
        if m.get('Measures') is not None:
            self.measures = m.get('Measures')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RobotInstanceId') is not None:
            self.robot_instance_id = m.get('RobotInstanceId')
        return self


class GetBotChatDataResponseBody(TeaModel):
    def __init__(
        self,
        cost_time: str = None,
        request_id: str = None,
        datas: List[Dict[str, Any]] = None,
    ):
        self.cost_time = cost_time
        self.request_id = request_id
        self.datas = datas

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cost_time is not None:
            result['CostTime'] = self.cost_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.datas is not None:
            result['Datas'] = self.datas
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostTime') is not None:
            self.cost_time = m.get('CostTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Datas') is not None:
            self.datas = m.get('Datas')
        return self


class GetBotChatDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetBotChatDataResponseBody = None,
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
            temp_model = GetBotChatDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBotDsStatDataRequest(TeaModel):
    def __init__(
        self,
        cube_id: str = None,
        measures: str = None,
        start_time: str = None,
        end_time: str = None,
        robot_instance_id: str = None,
    ):
        self.cube_id = cube_id
        self.measures = measures
        self.start_time = start_time
        self.end_time = end_time
        self.robot_instance_id = robot_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cube_id is not None:
            result['CubeId'] = self.cube_id
        if self.measures is not None:
            result['Measures'] = self.measures
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.robot_instance_id is not None:
            result['RobotInstanceId'] = self.robot_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CubeId') is not None:
            self.cube_id = m.get('CubeId')
        if m.get('Measures') is not None:
            self.measures = m.get('Measures')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RobotInstanceId') is not None:
            self.robot_instance_id = m.get('RobotInstanceId')
        return self


class GetBotDsStatDataResponseBody(TeaModel):
    def __init__(
        self,
        cost_time: str = None,
        request_id: str = None,
        datas: List[Dict[str, Any]] = None,
    ):
        self.cost_time = cost_time
        self.request_id = request_id
        self.datas = datas

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cost_time is not None:
            result['CostTime'] = self.cost_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.datas is not None:
            result['Datas'] = self.datas
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostTime') is not None:
            self.cost_time = m.get('CostTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Datas') is not None:
            self.datas = m.get('Datas')
        return self


class GetBotDsStatDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetBotDsStatDataResponseBody = None,
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
            temp_model = GetBotDsStatDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBotKnowledgeStatDataRequest(TeaModel):
    def __init__(
        self,
        cube_id: str = None,
        measures: str = None,
        start_time: str = None,
        end_time: str = None,
        robot_instance_id: str = None,
    ):
        self.cube_id = cube_id
        self.measures = measures
        self.start_time = start_time
        self.end_time = end_time
        self.robot_instance_id = robot_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cube_id is not None:
            result['CubeId'] = self.cube_id
        if self.measures is not None:
            result['Measures'] = self.measures
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.robot_instance_id is not None:
            result['RobotInstanceId'] = self.robot_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CubeId') is not None:
            self.cube_id = m.get('CubeId')
        if m.get('Measures') is not None:
            self.measures = m.get('Measures')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RobotInstanceId') is not None:
            self.robot_instance_id = m.get('RobotInstanceId')
        return self


class GetBotKnowledgeStatDataResponseBody(TeaModel):
    def __init__(
        self,
        cost_time: str = None,
        request_id: str = None,
        datas: List[Dict[str, Any]] = None,
    ):
        self.cost_time = cost_time
        self.request_id = request_id
        self.datas = datas

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cost_time is not None:
            result['CostTime'] = self.cost_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.datas is not None:
            result['Datas'] = self.datas
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostTime') is not None:
            self.cost_time = m.get('CostTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Datas') is not None:
            self.datas = m.get('Datas')
        return self


class GetBotKnowledgeStatDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetBotKnowledgeStatDataResponseBody = None,
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
            temp_model = GetBotKnowledgeStatDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBotSessionDataRequest(TeaModel):
    def __init__(
        self,
        cube_id: str = None,
        measures: str = None,
        start_time: str = None,
        end_time: str = None,
        robot_instance_id: str = None,
    ):
        self.cube_id = cube_id
        self.measures = measures
        self.start_time = start_time
        self.end_time = end_time
        self.robot_instance_id = robot_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cube_id is not None:
            result['CubeId'] = self.cube_id
        if self.measures is not None:
            result['Measures'] = self.measures
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.robot_instance_id is not None:
            result['RobotInstanceId'] = self.robot_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CubeId') is not None:
            self.cube_id = m.get('CubeId')
        if m.get('Measures') is not None:
            self.measures = m.get('Measures')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RobotInstanceId') is not None:
            self.robot_instance_id = m.get('RobotInstanceId')
        return self


class GetBotSessionDataResponseBody(TeaModel):
    def __init__(
        self,
        cost_time: str = None,
        request_id: str = None,
        datas: List[Dict[str, Any]] = None,
    ):
        self.cost_time = cost_time
        self.request_id = request_id
        self.datas = datas

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cost_time is not None:
            result['CostTime'] = self.cost_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.datas is not None:
            result['Datas'] = self.datas
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostTime') is not None:
            self.cost_time = m.get('CostTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Datas') is not None:
            self.datas = m.get('Datas')
        return self


class GetBotSessionDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetBotSessionDataResponseBody = None,
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
            temp_model = GetBotSessionDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetConversationListRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        session_id: str = None,
        sender_id: str = None,
        start_date: str = None,
        end_date: str = None,
        page_number: str = None,
        page_size: str = None,
    ):
        self.instance_id = instance_id
        self.session_id = session_id
        self.sender_id = sender_id
        self.start_date = start_date
        self.end_date = end_date
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.sender_id is not None:
            result['SenderId'] = self.sender_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('SenderId') is not None:
            self.sender_id = m.get('SenderId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class GetConversationListResponseBody(TeaModel):
    def __init__(
        self,
        messages: List[Dict[str, Any]] = None,
        request_id: str = None,
        page_size: int = None,
        page_number: int = None,
        total_counts: int = None,
    ):
        self.messages = messages
        self.request_id = request_id
        self.page_size = page_size
        self.page_number = page_number
        self.total_counts = total_counts

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.messages is not None:
            result['Messages'] = self.messages
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.total_counts is not None:
            result['TotalCounts'] = self.total_counts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Messages') is not None:
            self.messages = m.get('Messages')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('TotalCounts') is not None:
            self.total_counts = m.get('TotalCounts')
        return self


class GetConversationListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetConversationListResponseBody = None,
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
            temp_model = GetConversationListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBotChatHistorysRequest(TeaModel):
    def __init__(
        self,
        cube_id: str = None,
        start_time: str = None,
        end_time: str = None,
        robot_instance_id: str = None,
        dimensions: str = None,
        is_detail: bool = None,
        orders: str = None,
        limit: int = None,
    ):
        self.cube_id = cube_id
        self.start_time = start_time
        self.end_time = end_time
        self.robot_instance_id = robot_instance_id
        self.dimensions = dimensions
        self.is_detail = is_detail
        self.orders = orders
        self.limit = limit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cube_id is not None:
            result['CubeId'] = self.cube_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.robot_instance_id is not None:
            result['RobotInstanceId'] = self.robot_instance_id
        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions
        if self.is_detail is not None:
            result['IsDetail'] = self.is_detail
        if self.orders is not None:
            result['Orders'] = self.orders
        if self.limit is not None:
            result['Limit'] = self.limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CubeId') is not None:
            self.cube_id = m.get('CubeId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RobotInstanceId') is not None:
            self.robot_instance_id = m.get('RobotInstanceId')
        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')
        if m.get('IsDetail') is not None:
            self.is_detail = m.get('IsDetail')
        if m.get('Orders') is not None:
            self.orders = m.get('Orders')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        return self


class ListBotChatHistorysResponseBody(TeaModel):
    def __init__(
        self,
        cost_time: str = None,
        request_id: str = None,
        datas: List[Dict[str, Any]] = None,
    ):
        self.cost_time = cost_time
        self.request_id = request_id
        self.datas = datas

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cost_time is not None:
            result['CostTime'] = self.cost_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.datas is not None:
            result['Datas'] = self.datas
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostTime') is not None:
            self.cost_time = m.get('CostTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Datas') is not None:
            self.datas = m.get('Datas')
        return self


class ListBotChatHistorysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListBotChatHistorysResponseBody = None,
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
            temp_model = ListBotChatHistorysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBotColdDsDatasRequest(TeaModel):
    def __init__(
        self,
        cube_id: str = None,
        start_time: str = None,
        end_time: str = None,
        robot_instance_id: str = None,
        dimensions: str = None,
        filters: str = None,
        limit: int = None,
    ):
        self.cube_id = cube_id
        self.start_time = start_time
        self.end_time = end_time
        self.robot_instance_id = robot_instance_id
        self.dimensions = dimensions
        self.filters = filters
        self.limit = limit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cube_id is not None:
            result['CubeId'] = self.cube_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.robot_instance_id is not None:
            result['RobotInstanceId'] = self.robot_instance_id
        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions
        if self.filters is not None:
            result['Filters'] = self.filters
        if self.limit is not None:
            result['Limit'] = self.limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CubeId') is not None:
            self.cube_id = m.get('CubeId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RobotInstanceId') is not None:
            self.robot_instance_id = m.get('RobotInstanceId')
        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')
        if m.get('Filters') is not None:
            self.filters = m.get('Filters')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        return self


class ListBotColdDsDatasResponseBody(TeaModel):
    def __init__(
        self,
        cost_time: str = None,
        request_id: str = None,
        datas: List[Dict[str, Any]] = None,
    ):
        self.cost_time = cost_time
        self.request_id = request_id
        self.datas = datas

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cost_time is not None:
            result['CostTime'] = self.cost_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.datas is not None:
            result['Datas'] = self.datas
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostTime') is not None:
            self.cost_time = m.get('CostTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Datas') is not None:
            self.datas = m.get('Datas')
        return self


class ListBotColdDsDatasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListBotColdDsDatasResponseBody = None,
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
            temp_model = ListBotColdDsDatasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBotColdKnowledgesRequest(TeaModel):
    def __init__(
        self,
        cube_id: str = None,
        start_time: str = None,
        end_time: str = None,
        robot_instance_id: str = None,
        dimensions: str = None,
        filters: str = None,
        limit: int = None,
    ):
        self.cube_id = cube_id
        self.start_time = start_time
        self.end_time = end_time
        self.robot_instance_id = robot_instance_id
        self.dimensions = dimensions
        self.filters = filters
        self.limit = limit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cube_id is not None:
            result['CubeId'] = self.cube_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.robot_instance_id is not None:
            result['RobotInstanceId'] = self.robot_instance_id
        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions
        if self.filters is not None:
            result['Filters'] = self.filters
        if self.limit is not None:
            result['Limit'] = self.limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CubeId') is not None:
            self.cube_id = m.get('CubeId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RobotInstanceId') is not None:
            self.robot_instance_id = m.get('RobotInstanceId')
        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')
        if m.get('Filters') is not None:
            self.filters = m.get('Filters')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        return self


class ListBotColdKnowledgesResponseBody(TeaModel):
    def __init__(
        self,
        cost_time: str = None,
        request_id: str = None,
        datas: List[Dict[str, Any]] = None,
    ):
        self.cost_time = cost_time
        self.request_id = request_id
        self.datas = datas

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cost_time is not None:
            result['CostTime'] = self.cost_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.datas is not None:
            result['Datas'] = self.datas
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostTime') is not None:
            self.cost_time = m.get('CostTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Datas') is not None:
            self.datas = m.get('Datas')
        return self


class ListBotColdKnowledgesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListBotColdKnowledgesResponseBody = None,
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
            temp_model = ListBotColdKnowledgesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBotDsDetailsRequest(TeaModel):
    def __init__(
        self,
        cube_id: str = None,
        measures: str = None,
        start_time: str = None,
        end_time: str = None,
        robot_instance_id: str = None,
        dimensions: str = None,
        orders: str = None,
        limit: int = None,
    ):
        self.cube_id = cube_id
        self.measures = measures
        self.start_time = start_time
        self.end_time = end_time
        self.robot_instance_id = robot_instance_id
        self.dimensions = dimensions
        self.orders = orders
        self.limit = limit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cube_id is not None:
            result['CubeId'] = self.cube_id
        if self.measures is not None:
            result['Measures'] = self.measures
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.robot_instance_id is not None:
            result['RobotInstanceId'] = self.robot_instance_id
        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions
        if self.orders is not None:
            result['Orders'] = self.orders
        if self.limit is not None:
            result['Limit'] = self.limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CubeId') is not None:
            self.cube_id = m.get('CubeId')
        if m.get('Measures') is not None:
            self.measures = m.get('Measures')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RobotInstanceId') is not None:
            self.robot_instance_id = m.get('RobotInstanceId')
        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')
        if m.get('Orders') is not None:
            self.orders = m.get('Orders')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        return self


class ListBotDsDetailsResponseBody(TeaModel):
    def __init__(
        self,
        cost_time: str = None,
        request_id: str = None,
        datas: List[Dict[str, Any]] = None,
    ):
        self.cost_time = cost_time
        self.request_id = request_id
        self.datas = datas

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cost_time is not None:
            result['CostTime'] = self.cost_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.datas is not None:
            result['Datas'] = self.datas
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostTime') is not None:
            self.cost_time = m.get('CostTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Datas') is not None:
            self.datas = m.get('Datas')
        return self


class ListBotDsDetailsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListBotDsDetailsResponseBody = None,
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
            temp_model = ListBotDsDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBotHotDsDatasRequest(TeaModel):
    def __init__(
        self,
        cube_id: str = None,
        measures: str = None,
        start_time: str = None,
        end_time: str = None,
        robot_instance_id: str = None,
        orders: str = None,
        dimensions: str = None,
        filters: str = None,
        limit: int = None,
    ):
        self.cube_id = cube_id
        self.measures = measures
        self.start_time = start_time
        self.end_time = end_time
        self.robot_instance_id = robot_instance_id
        self.orders = orders
        self.dimensions = dimensions
        self.filters = filters
        self.limit = limit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cube_id is not None:
            result['CubeId'] = self.cube_id
        if self.measures is not None:
            result['Measures'] = self.measures
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.robot_instance_id is not None:
            result['RobotInstanceId'] = self.robot_instance_id
        if self.orders is not None:
            result['Orders'] = self.orders
        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions
        if self.filters is not None:
            result['Filters'] = self.filters
        if self.limit is not None:
            result['Limit'] = self.limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CubeId') is not None:
            self.cube_id = m.get('CubeId')
        if m.get('Measures') is not None:
            self.measures = m.get('Measures')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RobotInstanceId') is not None:
            self.robot_instance_id = m.get('RobotInstanceId')
        if m.get('Orders') is not None:
            self.orders = m.get('Orders')
        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')
        if m.get('Filters') is not None:
            self.filters = m.get('Filters')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        return self


class ListBotHotDsDatasResponseBody(TeaModel):
    def __init__(
        self,
        cost_time: str = None,
        request_id: str = None,
        datas: List[Dict[str, Any]] = None,
    ):
        self.cost_time = cost_time
        self.request_id = request_id
        self.datas = datas

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cost_time is not None:
            result['CostTime'] = self.cost_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.datas is not None:
            result['Datas'] = self.datas
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostTime') is not None:
            self.cost_time = m.get('CostTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Datas') is not None:
            self.datas = m.get('Datas')
        return self


class ListBotHotDsDatasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListBotHotDsDatasResponseBody = None,
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
            temp_model = ListBotHotDsDatasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBotHotKnowledgesRequest(TeaModel):
    def __init__(
        self,
        cube_id: str = None,
        start_time: str = None,
        end_time: str = None,
        robot_instance_id: str = None,
        dimensions: str = None,
        orders: str = None,
        measures: str = None,
        filters: str = None,
        limit: int = None,
    ):
        self.cube_id = cube_id
        self.start_time = start_time
        self.end_time = end_time
        self.robot_instance_id = robot_instance_id
        self.dimensions = dimensions
        self.orders = orders
        self.measures = measures
        self.filters = filters
        self.limit = limit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cube_id is not None:
            result['CubeId'] = self.cube_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.robot_instance_id is not None:
            result['RobotInstanceId'] = self.robot_instance_id
        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions
        if self.orders is not None:
            result['Orders'] = self.orders
        if self.measures is not None:
            result['Measures'] = self.measures
        if self.filters is not None:
            result['Filters'] = self.filters
        if self.limit is not None:
            result['Limit'] = self.limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CubeId') is not None:
            self.cube_id = m.get('CubeId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RobotInstanceId') is not None:
            self.robot_instance_id = m.get('RobotInstanceId')
        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')
        if m.get('Orders') is not None:
            self.orders = m.get('Orders')
        if m.get('Measures') is not None:
            self.measures = m.get('Measures')
        if m.get('Filters') is not None:
            self.filters = m.get('Filters')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        return self


class ListBotHotKnowledgesResponseBody(TeaModel):
    def __init__(
        self,
        cost_time: str = None,
        request_id: str = None,
        datas: List[Dict[str, Any]] = None,
    ):
        self.cost_time = cost_time
        self.request_id = request_id
        self.datas = datas

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cost_time is not None:
            result['CostTime'] = self.cost_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.datas is not None:
            result['Datas'] = self.datas
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostTime') is not None:
            self.cost_time = m.get('CostTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Datas') is not None:
            self.datas = m.get('Datas')
        return self


class ListBotHotKnowledgesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListBotHotKnowledgesResponseBody = None,
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
            temp_model = ListBotHotKnowledgesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBotKnowledgeDetailsRequest(TeaModel):
    def __init__(
        self,
        cube_id: str = None,
        measures: str = None,
        start_time: str = None,
        end_time: str = None,
        robot_instance_id: str = None,
        limit: str = None,
        dimensions: str = None,
        orders: str = None,
    ):
        self.cube_id = cube_id
        self.measures = measures
        self.start_time = start_time
        self.end_time = end_time
        self.robot_instance_id = robot_instance_id
        self.limit = limit
        self.dimensions = dimensions
        self.orders = orders

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cube_id is not None:
            result['CubeId'] = self.cube_id
        if self.measures is not None:
            result['Measures'] = self.measures
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.robot_instance_id is not None:
            result['RobotInstanceId'] = self.robot_instance_id
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions
        if self.orders is not None:
            result['Orders'] = self.orders
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CubeId') is not None:
            self.cube_id = m.get('CubeId')
        if m.get('Measures') is not None:
            self.measures = m.get('Measures')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RobotInstanceId') is not None:
            self.robot_instance_id = m.get('RobotInstanceId')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')
        if m.get('Orders') is not None:
            self.orders = m.get('Orders')
        return self


class ListBotKnowledgeDetailsResponseBody(TeaModel):
    def __init__(
        self,
        cost_time: str = None,
        request_id: str = None,
        datas: List[Dict[str, Any]] = None,
    ):
        self.cost_time = cost_time
        self.request_id = request_id
        self.datas = datas

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cost_time is not None:
            result['CostTime'] = self.cost_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.datas is not None:
            result['Datas'] = self.datas
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostTime') is not None:
            self.cost_time = m.get('CostTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Datas') is not None:
            self.datas = m.get('Datas')
        return self


class ListBotKnowledgeDetailsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListBotKnowledgeDetailsResponseBody = None,
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
            temp_model = ListBotKnowledgeDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBotReceptionDetailDatasRequest(TeaModel):
    def __init__(
        self,
        cube_id: str = None,
        measures: str = None,
        start_time: str = None,
        end_time: str = None,
        robot_instance_id: str = None,
        dimensions: str = None,
    ):
        self.cube_id = cube_id
        self.measures = measures
        self.start_time = start_time
        self.end_time = end_time
        self.robot_instance_id = robot_instance_id
        self.dimensions = dimensions

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cube_id is not None:
            result['CubeId'] = self.cube_id
        if self.measures is not None:
            result['Measures'] = self.measures
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.robot_instance_id is not None:
            result['RobotInstanceId'] = self.robot_instance_id
        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CubeId') is not None:
            self.cube_id = m.get('CubeId')
        if m.get('Measures') is not None:
            self.measures = m.get('Measures')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RobotInstanceId') is not None:
            self.robot_instance_id = m.get('RobotInstanceId')
        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')
        return self


class ListBotReceptionDetailDatasResponseBody(TeaModel):
    def __init__(
        self,
        cost_time: str = None,
        request_id: str = None,
        datas: List[Dict[str, Any]] = None,
    ):
        self.cost_time = cost_time
        self.request_id = request_id
        self.datas = datas

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cost_time is not None:
            result['CostTime'] = self.cost_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.datas is not None:
            result['Datas'] = self.datas
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostTime') is not None:
            self.cost_time = m.get('CostTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Datas') is not None:
            self.datas = m.get('Datas')
        return self


class ListBotReceptionDetailDatasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListBotReceptionDetailDatasResponseBody = None,
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
            temp_model = ListBotReceptionDetailDatasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListConversationLogsRequest(TeaModel):
    def __init__(
        self,
        session_id: str = None,
    ):
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class ListConversationLogsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        chat_logs: List[Dict[str, Any]] = None,
        rounds: int = None,
    ):
        self.request_id = request_id
        self.chat_logs = chat_logs
        self.rounds = rounds

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.chat_logs is not None:
            result['ChatLogs'] = self.chat_logs
        if self.rounds is not None:
            result['Rounds'] = self.rounds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ChatLogs') is not None:
            self.chat_logs = m.get('ChatLogs')
        if m.get('Rounds') is not None:
            self.rounds = m.get('Rounds')
        return self


class ListConversationLogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListConversationLogsResponseBody = None,
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
            temp_model = ListConversationLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MoveKnowledgeCategoryRequest(TeaModel):
    def __init__(
        self,
        knowledge_id: int = None,
        category_id: int = None,
    ):
        self.knowledge_id = knowledge_id
        self.category_id = category_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        return self


class MoveKnowledgeCategoryResponseBody(TeaModel):
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


class MoveKnowledgeCategoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: MoveKnowledgeCategoryResponseBody = None,
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
            temp_model = MoveKnowledgeCategoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PublishDialogFlowRequest(TeaModel):
    def __init__(
        self,
        dialog_id: int = None,
    ):
        self.dialog_id = dialog_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')
        return self


class PublishDialogFlowResponseBody(TeaModel):
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


class PublishDialogFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PublishDialogFlowResponseBody = None,
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
            temp_model = PublishDialogFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PublishKnowledgeRequest(TeaModel):
    def __init__(
        self,
        knowledge_id: int = None,
    ):
        self.knowledge_id = knowledge_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        return self


class PublishKnowledgeResponseBody(TeaModel):
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


class PublishKnowledgeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PublishKnowledgeResponseBody = None,
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
            temp_model = PublishKnowledgeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryBotsRequest(TeaModel):
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


class QueryBotsResponseBodyBots(TeaModel):
    def __init__(
        self,
        introduction: str = None,
        avatar: str = None,
        time_zone: str = None,
        create_time: str = None,
        language_code: str = None,
        instance_id: str = None,
        name: str = None,
    ):
        self.introduction = introduction
        self.avatar = avatar
        self.time_zone = time_zone
        self.create_time = create_time
        self.language_code = language_code
        self.instance_id = instance_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.introduction is not None:
            result['Introduction'] = self.introduction
        if self.avatar is not None:
            result['Avatar'] = self.avatar
        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.language_code is not None:
            result['LanguageCode'] = self.language_code
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Introduction') is not None:
            self.introduction = m.get('Introduction')
        if m.get('Avatar') is not None:
            self.avatar = m.get('Avatar')
        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('LanguageCode') is not None:
            self.language_code = m.get('LanguageCode')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class QueryBotsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        bots: List[QueryBotsResponseBodyBots] = None,
        request_id: str = None,
        page_size: int = None,
        page_number: int = None,
    ):
        self.total_count = total_count
        self.bots = bots
        self.request_id = request_id
        self.page_size = page_size
        self.page_number = page_number

    def validate(self):
        if self.bots:
            for k in self.bots:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Bots'] = []
        if self.bots is not None:
            for k in self.bots:
                result['Bots'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.bots = []
        if m.get('Bots') is not None:
            for k in m.get('Bots'):
                temp_model = QueryBotsResponseBodyBots()
                self.bots.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class QueryBotsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryBotsResponseBody = None,
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
            temp_model = QueryBotsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDialogsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        dialog_name: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.instance_id = instance_id
        self.dialog_name = dialog_name
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.dialog_name is not None:
            result['DialogName'] = self.dialog_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DialogName') is not None:
            self.dialog_name = m.get('DialogName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryDialogsResponseBodyDialogs(TeaModel):
    def __init__(
        self,
        status: int = None,
        dialog_name: str = None,
        modify_user_id: str = None,
        is_online: bool = None,
        create_user_name: str = None,
        create_time: str = None,
        create_user_id: str = None,
        modify_user_name: str = None,
        description: str = None,
        dialog_id: int = None,
        is_sample_dialog: bool = None,
        modify_time: str = None,
    ):
        self.status = status
        self.dialog_name = dialog_name
        self.modify_user_id = modify_user_id
        self.is_online = is_online
        self.create_user_name = create_user_name
        self.create_time = create_time
        self.create_user_id = create_user_id
        self.modify_user_name = modify_user_name
        self.description = description
        self.dialog_id = dialog_id
        self.is_sample_dialog = is_sample_dialog
        self.modify_time = modify_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.dialog_name is not None:
            result['DialogName'] = self.dialog_name
        if self.modify_user_id is not None:
            result['ModifyUserId'] = self.modify_user_id
        if self.is_online is not None:
            result['IsOnline'] = self.is_online
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name
        if self.description is not None:
            result['Description'] = self.description
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        if self.is_sample_dialog is not None:
            result['IsSampleDialog'] = self.is_sample_dialog
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('DialogName') is not None:
            self.dialog_name = m.get('DialogName')
        if m.get('ModifyUserId') is not None:
            self.modify_user_id = m.get('ModifyUserId')
        if m.get('IsOnline') is not None:
            self.is_online = m.get('IsOnline')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')
        if m.get('IsSampleDialog') is not None:
            self.is_sample_dialog = m.get('IsSampleDialog')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        return self


class QueryDialogsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        page_size: int = None,
        page_number: int = None,
        dialogs: List[QueryDialogsResponseBodyDialogs] = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.page_size = page_size
        self.page_number = page_number
        self.dialogs = dialogs

    def validate(self):
        if self.dialogs:
            for k in self.dialogs:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Dialogs'] = []
        if self.dialogs is not None:
            for k in self.dialogs:
                result['Dialogs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.dialogs = []
        if m.get('Dialogs') is not None:
            for k in m.get('Dialogs'):
                temp_model = QueryDialogsResponseBodyDialogs()
                self.dialogs.append(temp_model.from_map(k))
        return self


class QueryDialogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryDialogsResponseBody = None,
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
            temp_model = QueryDialogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPerspectivesResponseBodyPerspectives(TeaModel):
    def __init__(
        self,
        status: int = None,
        modify_user_name: str = None,
        create_user_name: str = None,
        create_time: str = None,
        perspective_id: str = None,
        self_define: str = None,
        name: str = None,
        perspective_code: str = None,
        modify_time: str = None,
    ):
        self.status = status
        self.modify_user_name = modify_user_name
        self.create_user_name = create_user_name
        self.create_time = create_time
        self.perspective_id = perspective_id
        self.self_define = self_define
        self.name = name
        self.perspective_code = perspective_code
        self.modify_time = modify_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.perspective_id is not None:
            result['PerspectiveId'] = self.perspective_id
        if self.self_define is not None:
            result['SelfDefine'] = self.self_define
        if self.name is not None:
            result['Name'] = self.name
        if self.perspective_code is not None:
            result['PerspectiveCode'] = self.perspective_code
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('PerspectiveId') is not None:
            self.perspective_id = m.get('PerspectiveId')
        if m.get('SelfDefine') is not None:
            self.self_define = m.get('SelfDefine')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PerspectiveCode') is not None:
            self.perspective_code = m.get('PerspectiveCode')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        return self


class QueryPerspectivesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        perspectives: List[QueryPerspectivesResponseBodyPerspectives] = None,
    ):
        self.request_id = request_id
        self.perspectives = perspectives

    def validate(self):
        if self.perspectives:
            for k in self.perspectives:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Perspectives'] = []
        if self.perspectives is not None:
            for k in self.perspectives:
                result['Perspectives'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.perspectives = []
        if m.get('Perspectives') is not None:
            for k in m.get('Perspectives'):
                temp_model = QueryPerspectivesResponseBodyPerspectives()
                self.perspectives.append(temp_model.from_map(k))
        return self


class QueryPerspectivesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryPerspectivesResponseBody = None,
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
            temp_model = QueryPerspectivesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySystemEntitiesRequest(TeaModel):
    def __init__(
        self,
        entity_name: str = None,
    ):
        self.entity_name = entity_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.entity_name is not None:
            result['EntityName'] = self.entity_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')
        return self


class QuerySystemEntitiesResponseBodySystemEntities(TeaModel):
    def __init__(
        self,
        default_question: str = None,
        entity_code: str = None,
        entity_name: str = None,
    ):
        self.default_question = default_question
        self.entity_code = entity_code
        self.entity_name = entity_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.default_question is not None:
            result['DefaultQuestion'] = self.default_question
        if self.entity_code is not None:
            result['EntityCode'] = self.entity_code
        if self.entity_name is not None:
            result['EntityName'] = self.entity_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultQuestion') is not None:
            self.default_question = m.get('DefaultQuestion')
        if m.get('EntityCode') is not None:
            self.entity_code = m.get('EntityCode')
        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')
        return self


class QuerySystemEntitiesResponseBody(TeaModel):
    def __init__(
        self,
        system_entities: List[QuerySystemEntitiesResponseBodySystemEntities] = None,
        request_id: str = None,
    ):
        self.system_entities = system_entities
        self.request_id = request_id

    def validate(self):
        if self.system_entities:
            for k in self.system_entities:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['SystemEntities'] = []
        if self.system_entities is not None:
            for k in self.system_entities:
                result['SystemEntities'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.system_entities = []
        if m.get('SystemEntities') is not None:
            for k in m.get('SystemEntities'):
                temp_model = QuerySystemEntitiesResponseBodySystemEntities()
                self.system_entities.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QuerySystemEntitiesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QuerySystemEntitiesResponseBody = None,
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
            temp_model = QuerySystemEntitiesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveEntityMemberRequest(TeaModel):
    def __init__(
        self,
        entity_id: int = None,
        remove_type: str = None,
        member: str = None,
    ):
        self.entity_id = entity_id
        self.remove_type = remove_type
        self.member = member

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.remove_type is not None:
            result['RemoveType'] = self.remove_type
        if self.member is not None:
            result['Member'] = self.member
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('RemoveType') is not None:
            self.remove_type = m.get('RemoveType')
        if m.get('Member') is not None:
            self.member = m.get('Member')
        return self


class RemoveEntityMemberResponseBody(TeaModel):
    def __init__(
        self,
        entity_id: str = None,
        request_id: str = None,
    ):
        self.entity_id = entity_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
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


class RemoveEntityMemberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveEntityMemberResponseBody = None,
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
            temp_model = RemoveEntityMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveSynonymRequest(TeaModel):
    def __init__(
        self,
        core_word_name: str = None,
        synonym: str = None,
    ):
        self.core_word_name = core_word_name
        self.synonym = synonym

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.core_word_name is not None:
            result['CoreWordName'] = self.core_word_name
        if self.synonym is not None:
            result['Synonym'] = self.synonym
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoreWordName') is not None:
            self.core_word_name = m.get('CoreWordName')
        if m.get('Synonym') is not None:
            self.synonym = m.get('Synonym')
        return self


class RemoveSynonymResponseBody(TeaModel):
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


class RemoveSynonymResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveSynonymResponseBody = None,
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
            temp_model = RemoveSynonymResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TestDialogFlowRequest(TeaModel):
    def __init__(
        self,
        dialog_id: int = None,
    ):
        self.dialog_id = dialog_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')
        return self


class TestDialogFlowResponseBody(TeaModel):
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


class TestDialogFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: TestDialogFlowResponseBody = None,
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
            temp_model = TestDialogFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCategoryRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        category_id: int = None,
    ):
        self.name = name
        self.category_id = category_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        return self


class UpdateCategoryResponseBody(TeaModel):
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


class UpdateCategoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateCategoryResponseBody = None,
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
            temp_model = UpdateCategoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCoreWordRequest(TeaModel):
    def __init__(
        self,
        core_word_name: str = None,
        core_word_code: str = None,
    ):
        self.core_word_name = core_word_name
        self.core_word_code = core_word_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.core_word_name is not None:
            result['CoreWordName'] = self.core_word_name
        if self.core_word_code is not None:
            result['CoreWordCode'] = self.core_word_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoreWordName') is not None:
            self.core_word_name = m.get('CoreWordName')
        if m.get('CoreWordCode') is not None:
            self.core_word_code = m.get('CoreWordCode')
        return self


class UpdateCoreWordResponseBody(TeaModel):
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


class UpdateCoreWordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateCoreWordResponseBody = None,
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
            temp_model = UpdateCoreWordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDialogRequest(TeaModel):
    def __init__(
        self,
        dialog_id: int = None,
        dialog_name: str = None,
        description: str = None,
    ):
        self.dialog_id = dialog_id
        self.dialog_name = dialog_name
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        if self.dialog_name is not None:
            result['DialogName'] = self.dialog_name
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')
        if m.get('DialogName') is not None:
            self.dialog_name = m.get('DialogName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class UpdateDialogResponseBody(TeaModel):
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


class UpdateDialogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateDialogResponseBody = None,
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
            temp_model = UpdateDialogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDialogFlowRequest(TeaModel):
    def __init__(
        self,
        dialog_id: int = None,
        module_definition: str = None,
    ):
        self.dialog_id = dialog_id
        self.module_definition = module_definition

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        if self.module_definition is not None:
            result['ModuleDefinition'] = self.module_definition
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')
        if m.get('ModuleDefinition') is not None:
            self.module_definition = m.get('ModuleDefinition')
        return self


class UpdateDialogFlowResponseBody(TeaModel):
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


class UpdateDialogFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateDialogFlowResponseBody = None,
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
            temp_model = UpdateDialogFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateEntityRequest(TeaModel):
    def __init__(
        self,
        entity_id: int = None,
        entity_name: str = None,
        entity_type: str = None,
        regex: str = None,
        members: str = None,
    ):
        self.entity_id = entity_id
        self.entity_name = entity_name
        self.entity_type = entity_type
        self.regex = regex
        self.members = members

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.entity_name is not None:
            result['EntityName'] = self.entity_name
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.regex is not None:
            result['Regex'] = self.regex
        if self.members is not None:
            result['Members'] = self.members
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('Regex') is not None:
            self.regex = m.get('Regex')
        if m.get('Members') is not None:
            self.members = m.get('Members')
        return self


class UpdateEntityResponseBody(TeaModel):
    def __init__(
        self,
        entity_id: str = None,
        request_id: str = None,
    ):
        self.entity_id = entity_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
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


class UpdateEntityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateEntityResponseBody = None,
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
            temp_model = UpdateEntityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateIntentRequest(TeaModel):
    def __init__(
        self,
        intent_definition: str = None,
        intent_id: int = None,
    ):
        self.intent_definition = intent_definition
        self.intent_id = intent_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.intent_definition is not None:
            result['IntentDefinition'] = self.intent_definition
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IntentDefinition') is not None:
            self.intent_definition = m.get('IntentDefinition')
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        return self


class UpdateIntentResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        intent_id: str = None,
    ):
        self.request_id = request_id
        self.intent_id = intent_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        return self


class UpdateIntentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateIntentResponseBody = None,
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
            temp_model = UpdateIntentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateKnowledgeRequest(TeaModel):
    def __init__(
        self,
        knowledge: str = None,
    ):
        self.knowledge = knowledge

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.knowledge is not None:
            result['Knowledge'] = self.knowledge
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Knowledge') is not None:
            self.knowledge = m.get('Knowledge')
        return self


class UpdateKnowledgeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        knowledge_id: int = None,
    ):
        self.request_id = request_id
        self.knowledge_id = knowledge_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        return self


class UpdateKnowledgeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateKnowledgeResponseBody = None,
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
            temp_model = UpdateKnowledgeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePerspectiveRequest(TeaModel):
    def __init__(
        self,
        perspective_id: str = None,
        name: str = None,
    ):
        self.perspective_id = perspective_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.perspective_id is not None:
            result['PerspectiveId'] = self.perspective_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PerspectiveId') is not None:
            self.perspective_id = m.get('PerspectiveId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
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
        body: UpdatePerspectiveResponseBody = None,
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
            temp_model = UpdatePerspectiveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


