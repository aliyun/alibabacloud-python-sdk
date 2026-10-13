# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_chatbot20220408 import models as main_models
from darabonba.model import DaraModel

class ChatResponseBody(DaraModel):
    def __init__(
        self,
        message_id: str = None,
        messages: List[main_models.ChatResponseBodyMessages] = None,
        query_seg_list: List[str] = None,
        request_id: str = None,
        session_id: str = None,
    ):
        # The ID of the response message in the current session.
        self.message_id = message_id
        # The list of messages.
        self.messages = messages
        # The tokenization results of the query, which may be empty.
        self.query_seg_list = query_seg_list
        # The request ID.
        self.request_id = request_id
        # The ID of the current session.
        self.session_id = session_id

    def validate(self):
        if self.messages:
            for v1 in self.messages:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message_id is not None:
            result['MessageId'] = self.message_id

        result['Messages'] = []
        if self.messages is not None:
            for k1 in self.messages:
                result['Messages'].append(k1.to_map() if k1 else None)

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
            for k1 in m.get('Messages'):
                temp_model = main_models.ChatResponseBodyMessages()
                self.messages.append(temp_model.from_map(k1))

        if m.get('QuerySegList') is not None:
            self.query_seg_list = m.get('QuerySegList')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        return self

class ChatResponseBodyMessages(DaraModel):
    def __init__(
        self,
        answer_source: str = None,
        answer_type: str = None,
        knowledge: main_models.ChatResponseBodyMessagesKnowledge = None,
        recommends: List[main_models.ChatResponseBodyMessagesRecommends] = None,
        text: main_models.ChatResponseBodyMessagesText = None,
        title: str = None,
        voice_title: str = None,
    ):
        # The source of the recommended answer when AnswerType is Recommend.
        # [_single.resp.200.props.Messages.items.AnswerSource.enum. INTENT_FAQ_CLARIFY]mixed clarification from FAQ and dialog flow
        self.answer_source = answer_source
        # The type of this message.
        self.answer_type = answer_type
        # When AnswerType is Knowledge, this field contains the Knowledge object returned by the chatbot.
        self.knowledge = knowledge
        # The list of recommendations returned by the bot when AnswerType is Recommend.
        self.recommends = recommends
        # When AnswerType is Text, this field contains the Text object returned by the chatbot.
        self.text = text
        # The counter-question title in online scenarios.
        self.title = title
        # The clarification content in voice scenarios.
        self.voice_title = voice_title

    def validate(self):
        if self.knowledge:
            self.knowledge.validate()
        if self.recommends:
            for v1 in self.recommends:
                 if v1:
                    v1.validate()
        if self.text:
            self.text.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.answer_source is not None:
            result['AnswerSource'] = self.answer_source

        if self.answer_type is not None:
            result['AnswerType'] = self.answer_type

        if self.knowledge is not None:
            result['Knowledge'] = self.knowledge.to_map()

        result['Recommends'] = []
        if self.recommends is not None:
            for k1 in self.recommends:
                result['Recommends'].append(k1.to_map() if k1 else None)

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
            temp_model = main_models.ChatResponseBodyMessagesKnowledge()
            self.knowledge = temp_model.from_map(m.get('Knowledge'))

        self.recommends = []
        if m.get('Recommends') is not None:
            for k1 in m.get('Recommends'):
                temp_model = main_models.ChatResponseBodyMessagesRecommends()
                self.recommends.append(temp_model.from_map(k1))

        if m.get('Text') is not None:
            temp_model = main_models.ChatResponseBodyMessagesText()
            self.text = temp_model.from_map(m.get('Text'))

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('VoiceTitle') is not None:
            self.voice_title = m.get('VoiceTitle')

        return self

class ChatResponseBodyMessagesText(DaraModel):
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
        slots: List[main_models.ChatResponseBodyMessagesTextSlots] = None,
        user_defined_chat_title: str = None,
    ):
        # Distinguishes the answer type.
        self.answer_source = answer_source
        # When AnswerSource is MACHINE_READ, this field returns the title of the hit article.
        self.article_title = article_title
        # The instruction parameters, such as the skill group for a transfer-to-agent instruction.
        self.commands = commands
        # The content of the text message.
        self.content = content
        # The indicator of whether the answer is plain text or rich text.
        self.content_type = content_type
        # When AnswerSource is BotFramework, this field returns the dialog flow unit name.
        self.dialog_name = dialog_name
        # The pass-through parameters returned in this field.
        self.ext = ext
        # The pass-through parameters returned when AnswerSource is BotFramework.
        self.external_flags = external_flags
        # The hit statement.
        self.hit_statement = hit_statement
        # When AnswerSource is BotFramework, this field returns the intent name.
        self.intent_name = intent_name
        # The metadata.
        self.meta_data = meta_data
        # The node ID returned when AnswerSource is BotFramework.
        self.node_id = node_id
        # When AnswerSource is BotFramework, this field returns the node name.
        self.node_name = node_name
        # When AnswerSource is BotFramework and ResponseType is SSML, this field indicates that a dialog flow interactive slot filling is hit. Otherwise, this field does not exist.
        self.response_type = response_type
        # The score.
        self.score = score
        # When AnswerSource is BotFramework, this field returns the list of named entities.
        self.slots = slots
        # The title of the custom chitchat topic.
        self.user_defined_chat_title = user_defined_chat_title

    def validate(self):
        if self.slots:
            for v1 in self.slots:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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
            for k1 in self.slots:
                result['Slots'].append(k1.to_map() if k1 else None)

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
            for k1 in m.get('Slots'):
                temp_model = main_models.ChatResponseBodyMessagesTextSlots()
                self.slots.append(temp_model.from_map(k1))

        if m.get('UserDefinedChatTitle') is not None:
            self.user_defined_chat_title = m.get('UserDefinedChatTitle')

        return self

class ChatResponseBodyMessagesTextSlots(DaraModel):
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class ChatResponseBodyMessagesRecommends(DaraModel):
    def __init__(
        self,
        answer_source: str = None,
        knowledge_id: str = None,
        score: float = None,
        title: str = None,
    ):
        # The identifier of the clarification source.
        self.answer_source = answer_source
        # The knowledge ID for clarification.
        self.knowledge_id = knowledge_id
        # The score of the recommended content. This field has a value when AnswerSource is KNOWLEDGE.
        self.score = score
        # The clarification content, which can be an entity from knowledge graph Q&A, a knowledge title from knowledge-based Q&A, or a column value from table-based Q&A.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class ChatResponseBodyMessagesKnowledge(DaraModel):
    def __init__(
        self,
        answer_source: str = None,
        category: str = None,
        content: str = None,
        content_type: str = None,
        hit_statement: str = None,
        id: str = None,
        related_knowledges: List[main_models.ChatResponseBodyMessagesKnowledgeRelatedKnowledges] = None,
        score: float = None,
        summary: str = None,
        title: str = None,
    ):
        # Distinguishes the answer type.
        # KnowledgeBase: knowledge base.
        self.answer_source = answer_source
        # The knowledge category.
        self.category = category
        # The content of the hit question.
        self.content = content
        # The indicator of whether the answer is plain text or rich text.
        self.content_type = content_type
        # The hit statement.
        self.hit_statement = hit_statement
        # The ID of the hit question in the knowledge base.
        self.id = id
        # The list of related knowledge entries.
        self.related_knowledges = related_knowledges
        # The score.
        self.score = score
        # The summary of the hit question.
        self.summary = summary
        # The title of the hit question.
        self.title = title

    def validate(self):
        if self.related_knowledges:
            for v1 in self.related_knowledges:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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
            for k1 in self.related_knowledges:
                result['RelatedKnowledges'].append(k1.to_map() if k1 else None)

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
            for k1 in m.get('RelatedKnowledges'):
                temp_model = main_models.ChatResponseBodyMessagesKnowledgeRelatedKnowledges()
                self.related_knowledges.append(temp_model.from_map(k1))

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

class ChatResponseBodyMessagesKnowledgeRelatedKnowledges(DaraModel):
    def __init__(
        self,
        knowledge_id: str = None,
        title: str = None,
    ):
        # The ID of the related knowledge entry.
        self.knowledge_id = knowledge_id
        # The title of the related knowledge entry.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

