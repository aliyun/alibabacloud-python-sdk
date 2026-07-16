# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_chatbot20220408 import models as main_models
from darabonba.model import DaraModel

class TongyiChatDebugInfoResponseBody(DaraModel):
    def __init__(
        self,
        answer_info: main_models.TongyiChatDebugInfoResponseBodyAnswerInfo = None,
        message_id: str = None,
        pipeline: List[main_models.TongyiChatDebugInfoResponseBodyPipeline] = None,
        request_id: str = None,
    ):
        self.answer_info = answer_info
        # The ID of the response message in the current session.
        self.message_id = message_id
        # The array of nodes that constitute the Q\\&A workflow.
        self.pipeline = pipeline
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.answer_info:
            self.answer_info.validate()
        if self.pipeline:
            for v1 in self.pipeline:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.answer_info is not None:
            result['AnswerInfo'] = self.answer_info.to_map()

        if self.message_id is not None:
            result['MessageId'] = self.message_id

        result['Pipeline'] = []
        if self.pipeline is not None:
            for k1 in self.pipeline:
                result['Pipeline'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnswerInfo') is not None:
            temp_model = main_models.TongyiChatDebugInfoResponseBodyAnswerInfo()
            self.answer_info = temp_model.from_map(m.get('AnswerInfo'))

        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')

        self.pipeline = []
        if m.get('Pipeline') is not None:
            for k1 in m.get('Pipeline'):
                temp_model = main_models.TongyiChatDebugInfoResponseBodyPipeline()
                self.pipeline.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class TongyiChatDebugInfoResponseBodyPipeline(DaraModel):
    def __init__(
        self,
        input: Any = None,
        name: str = None,
        node_type: str = None,
        output: Any = None,
    ):
        # The input data for the node.
        self.input = input
        # The name of the strategy. Possible values include:
        # 
        # - FAQ
        # 
        # - Hit Keywords
        # 
        # - Global Sensitive Words
        # 
        # This parameter is returned only when `NodeType` is set to `system_strategy`.
        self.name = name
        # The node type. Valid values:
        # 
        # - **system_strategy**: system strategy.
        # 
        # - **rewrite_query**: retrieval query.
        # 
        # - **invoke_llm**: LLM invocation.
        # 
        # - **invoke_tools**: tool invocation.
        self.node_type = node_type
        # The output data from the node.
        self.output = output

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class TongyiChatDebugInfoResponseBodyAnswerInfo(DaraModel):
    def __init__(
        self,
        answer_reference_info: main_models.TongyiChatDebugInfoResponseBodyAnswerInfoAnswerReferenceInfo = None,
        message_body: main_models.TongyiChatDebugInfoResponseBodyAnswerInfoMessageBody = None,
    ):
        self.answer_reference_info = answer_reference_info
        self.message_body = message_body

    def validate(self):
        if self.answer_reference_info:
            self.answer_reference_info.validate()
        if self.message_body:
            self.message_body.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.answer_reference_info is not None:
            result['AnswerReferenceInfo'] = self.answer_reference_info.to_map()

        if self.message_body is not None:
            result['MessageBody'] = self.message_body.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnswerReferenceInfo') is not None:
            temp_model = main_models.TongyiChatDebugInfoResponseBodyAnswerInfoAnswerReferenceInfo()
            self.answer_reference_info = temp_model.from_map(m.get('AnswerReferenceInfo'))

        if m.get('MessageBody') is not None:
            temp_model = main_models.TongyiChatDebugInfoResponseBodyAnswerInfoMessageBody()
            self.message_body = temp_model.from_map(m.get('MessageBody'))

        return self

class TongyiChatDebugInfoResponseBodyAnswerInfoMessageBody(DaraModel):
    def __init__(
        self,
        commands: Any = None,
        direct_message_body: main_models.TongyiChatDebugInfoResponseBodyAnswerInfoMessageBodyDirectMessageBody = None,
    ):
        self.commands = commands
        self.direct_message_body = direct_message_body

    def validate(self):
        if self.direct_message_body:
            self.direct_message_body.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.commands is not None:
            result['Commands'] = self.commands

        if self.direct_message_body is not None:
            result['DirectMessageBody'] = self.direct_message_body.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Commands') is not None:
            self.commands = m.get('Commands')

        if m.get('DirectMessageBody') is not None:
            temp_model = main_models.TongyiChatDebugInfoResponseBodyAnswerInfoMessageBodyDirectMessageBody()
            self.direct_message_body = temp_model.from_map(m.get('DirectMessageBody'))

        return self

class TongyiChatDebugInfoResponseBodyAnswerInfoMessageBodyDirectMessageBody(DaraModel):
    def __init__(
        self,
        content_type: str = None,
        transition_list: List[str] = None,
        related_question_list: List[str] = None,
        sentence_list: List[main_models.TongyiChatDebugInfoResponseBodyAnswerInfoMessageBodyDirectMessageBodySentenceList] = None,
    ):
        self.content_type = content_type
        self.transition_list = transition_list
        self.related_question_list = related_question_list
        self.sentence_list = sentence_list

    def validate(self):
        if self.sentence_list:
            for v1 in self.sentence_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content_type is not None:
            result['ContentType'] = self.content_type

        if self.transition_list is not None:
            result['TransitionList'] = self.transition_list

        if self.related_question_list is not None:
            result['relatedQuestionList'] = self.related_question_list

        result['sentenceList'] = []
        if self.sentence_list is not None:
            for k1 in self.sentence_list:
                result['sentenceList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')

        if m.get('TransitionList') is not None:
            self.transition_list = m.get('TransitionList')

        if m.get('relatedQuestionList') is not None:
            self.related_question_list = m.get('relatedQuestionList')

        self.sentence_list = []
        if m.get('sentenceList') is not None:
            for k1 in m.get('sentenceList'):
                temp_model = main_models.TongyiChatDebugInfoResponseBodyAnswerInfoMessageBodyDirectMessageBodySentenceList()
                self.sentence_list.append(temp_model.from_map(k1))

        return self

class TongyiChatDebugInfoResponseBodyAnswerInfoMessageBodyDirectMessageBodySentenceList(DaraModel):
    def __init__(
        self,
        content: str = None,
        refer_number: int = None,
    ):
        self.content = content
        self.refer_number = refer_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.refer_number is not None:
            result['ReferNumber'] = self.refer_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('ReferNumber') is not None:
            self.refer_number = m.get('ReferNumber')

        return self

class TongyiChatDebugInfoResponseBodyAnswerInfoAnswerReferenceInfo(DaraModel):
    def __init__(
        self,
        item_list: List[main_models.TongyiChatDebugInfoResponseBodyAnswerInfoAnswerReferenceInfoItemList] = None,
    ):
        self.item_list = item_list

    def validate(self):
        if self.item_list:
            for v1 in self.item_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ItemList'] = []
        if self.item_list is not None:
            for k1 in self.item_list:
                result['ItemList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.item_list = []
        if m.get('ItemList') is not None:
            for k1 in m.get('ItemList'):
                temp_model = main_models.TongyiChatDebugInfoResponseBodyAnswerInfoAnswerReferenceInfoItemList()
                self.item_list.append(temp_model.from_map(k1))

        return self

class TongyiChatDebugInfoResponseBodyAnswerInfoAnswerReferenceInfoItemList(DaraModel):
    def __init__(
        self,
        content_type: str = None,
        data_source: str = None,
        id: str = None,
        number: int = None,
        reference_ext: Any = None,
        title: str = None,
    ):
        self.content_type = content_type
        self.data_source = data_source
        self.id = id
        self.number = number
        self.reference_ext = reference_ext
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content_type is not None:
            result['ContentType'] = self.content_type

        if self.data_source is not None:
            result['DataSource'] = self.data_source

        if self.id is not None:
            result['Id'] = self.id

        if self.number is not None:
            result['Number'] = self.number

        if self.reference_ext is not None:
            result['ReferenceExt'] = self.reference_ext

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')

        if m.get('DataSource') is not None:
            self.data_source = m.get('DataSource')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Number') is not None:
            self.number = m.get('Number')

        if m.get('ReferenceExt') is not None:
            self.reference_ext = m.get('ReferenceExt')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

