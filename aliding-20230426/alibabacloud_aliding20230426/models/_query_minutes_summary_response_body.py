# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class QueryMinutesSummaryResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        summary: main_models.QueryMinutesSummaryResponseBodySummary = None,
        vendor_request_id: str = None,
        vendor_type: str = None,
    ):
        self.request_id = request_id
        self.summary = summary
        self.vendor_request_id = vendor_request_id
        self.vendor_type = vendor_type

    def validate(self):
        if self.summary:
            self.summary.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.summary is not None:
            result['summary'] = self.summary.to_map()

        if self.vendor_request_id is not None:
            result['vendorRequestId'] = self.vendor_request_id

        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('summary') is not None:
            temp_model = main_models.QueryMinutesSummaryResponseBodySummary()
            self.summary = temp_model.from_map(m.get('summary'))

        if m.get('vendorRequestId') is not None:
            self.vendor_request_id = m.get('vendorRequestId')

        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')

        return self

class QueryMinutesSummaryResponseBodySummary(DaraModel):
    def __init__(
        self,
        actions: main_models.QueryMinutesSummaryResponseBodySummaryActions = None,
        auto_chapters: List[main_models.QueryMinutesSummaryResponseBodySummaryAutoChapters] = None,
        conversational_summary: List[main_models.QueryMinutesSummaryResponseBodySummaryConversationalSummary] = None,
        key_sentences: main_models.QueryMinutesSummaryResponseBodySummaryKeySentences = None,
        keywords: List[str] = None,
        paragraph_summary: str = None,
        questions_answering_summary: List[main_models.QueryMinutesSummaryResponseBodySummaryQuestionsAnsweringSummary] = None,
    ):
        self.actions = actions
        self.auto_chapters = auto_chapters
        self.conversational_summary = conversational_summary
        self.key_sentences = key_sentences
        self.keywords = keywords
        self.paragraph_summary = paragraph_summary
        self.questions_answering_summary = questions_answering_summary

    def validate(self):
        if self.actions:
            self.actions.validate()
        if self.auto_chapters:
            for v1 in self.auto_chapters:
                 if v1:
                    v1.validate()
        if self.conversational_summary:
            for v1 in self.conversational_summary:
                 if v1:
                    v1.validate()
        if self.key_sentences:
            self.key_sentences.validate()
        if self.questions_answering_summary:
            for v1 in self.questions_answering_summary:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.actions is not None:
            result['Actions'] = self.actions.to_map()

        result['AutoChapters'] = []
        if self.auto_chapters is not None:
            for k1 in self.auto_chapters:
                result['AutoChapters'].append(k1.to_map() if k1 else None)

        result['ConversationalSummary'] = []
        if self.conversational_summary is not None:
            for k1 in self.conversational_summary:
                result['ConversationalSummary'].append(k1.to_map() if k1 else None)

        if self.key_sentences is not None:
            result['KeySentences'] = self.key_sentences.to_map()

        if self.keywords is not None:
            result['Keywords'] = self.keywords

        if self.paragraph_summary is not None:
            result['ParagraphSummary'] = self.paragraph_summary

        result['QuestionsAnsweringSummary'] = []
        if self.questions_answering_summary is not None:
            for k1 in self.questions_answering_summary:
                result['QuestionsAnsweringSummary'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Actions') is not None:
            temp_model = main_models.QueryMinutesSummaryResponseBodySummaryActions()
            self.actions = temp_model.from_map(m.get('Actions'))

        self.auto_chapters = []
        if m.get('AutoChapters') is not None:
            for k1 in m.get('AutoChapters'):
                temp_model = main_models.QueryMinutesSummaryResponseBodySummaryAutoChapters()
                self.auto_chapters.append(temp_model.from_map(k1))

        self.conversational_summary = []
        if m.get('ConversationalSummary') is not None:
            for k1 in m.get('ConversationalSummary'):
                temp_model = main_models.QueryMinutesSummaryResponseBodySummaryConversationalSummary()
                self.conversational_summary.append(temp_model.from_map(k1))

        if m.get('KeySentences') is not None:
            temp_model = main_models.QueryMinutesSummaryResponseBodySummaryKeySentences()
            self.key_sentences = temp_model.from_map(m.get('KeySentences'))

        if m.get('Keywords') is not None:
            self.keywords = m.get('Keywords')

        if m.get('ParagraphSummary') is not None:
            self.paragraph_summary = m.get('ParagraphSummary')

        self.questions_answering_summary = []
        if m.get('QuestionsAnsweringSummary') is not None:
            for k1 in m.get('QuestionsAnsweringSummary'):
                temp_model = main_models.QueryMinutesSummaryResponseBodySummaryQuestionsAnsweringSummary()
                self.questions_answering_summary.append(temp_model.from_map(k1))

        return self

class QueryMinutesSummaryResponseBodySummaryQuestionsAnsweringSummary(DaraModel):
    def __init__(
        self,
        answer: str = None,
        question: str = None,
        sentence_ids_of_answer: List[int] = None,
        sentence_ids_of_question: List[int] = None,
    ):
        self.answer = answer
        self.question = question
        self.sentence_ids_of_answer = sentence_ids_of_answer
        self.sentence_ids_of_question = sentence_ids_of_question

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.answer is not None:
            result['Answer'] = self.answer

        if self.question is not None:
            result['Question'] = self.question

        if self.sentence_ids_of_answer is not None:
            result['SentenceIdsOfAnswer'] = self.sentence_ids_of_answer

        if self.sentence_ids_of_question is not None:
            result['SentenceIdsOfQuestion'] = self.sentence_ids_of_question

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Answer') is not None:
            self.answer = m.get('Answer')

        if m.get('Question') is not None:
            self.question = m.get('Question')

        if m.get('SentenceIdsOfAnswer') is not None:
            self.sentence_ids_of_answer = m.get('SentenceIdsOfAnswer')

        if m.get('SentenceIdsOfQuestion') is not None:
            self.sentence_ids_of_question = m.get('SentenceIdsOfQuestion')

        return self

class QueryMinutesSummaryResponseBodySummaryKeySentences(DaraModel):
    def __init__(
        self,
        end: int = None,
        id: int = None,
        sentence_id: int = None,
        start: int = None,
        text: str = None,
    ):
        self.end = end
        self.id = id
        self.sentence_id = sentence_id
        self.start = start
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end is not None:
            result['End'] = self.end

        if self.id is not None:
            result['Id'] = self.id

        if self.sentence_id is not None:
            result['SentenceId'] = self.sentence_id

        if self.start is not None:
            result['Start'] = self.start

        if self.text is not None:
            result['Text'] = self.text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('End') is not None:
            self.end = m.get('End')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('SentenceId') is not None:
            self.sentence_id = m.get('SentenceId')

        if m.get('Start') is not None:
            self.start = m.get('Start')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        return self

class QueryMinutesSummaryResponseBodySummaryConversationalSummary(DaraModel):
    def __init__(
        self,
        speaker_id: str = None,
        speaker_name: str = None,
        summary: str = None,
    ):
        self.speaker_id = speaker_id
        self.speaker_name = speaker_name
        self.summary = summary

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.speaker_id is not None:
            result['SpeakerId'] = self.speaker_id

        if self.speaker_name is not None:
            result['SpeakerName'] = self.speaker_name

        if self.summary is not None:
            result['Summary'] = self.summary

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpeakerId') is not None:
            self.speaker_id = m.get('SpeakerId')

        if m.get('SpeakerName') is not None:
            self.speaker_name = m.get('SpeakerName')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        return self

class QueryMinutesSummaryResponseBodySummaryAutoChapters(DaraModel):
    def __init__(
        self,
        end: int = None,
        headline: str = None,
        id: int = None,
        start: int = None,
        summary: str = None,
    ):
        self.end = end
        self.headline = headline
        self.id = id
        self.start = start
        self.summary = summary

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end is not None:
            result['End'] = self.end

        if self.headline is not None:
            result['Headline'] = self.headline

        if self.id is not None:
            result['Id'] = self.id

        if self.start is not None:
            result['Start'] = self.start

        if self.summary is not None:
            result['Summary'] = self.summary

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('End') is not None:
            self.end = m.get('End')

        if m.get('Headline') is not None:
            self.headline = m.get('Headline')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Start') is not None:
            self.start = m.get('Start')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        return self

class QueryMinutesSummaryResponseBodySummaryActions(DaraModel):
    def __init__(
        self,
        end: int = None,
        id: int = None,
        sentence_id: int = None,
        start: int = None,
        text: str = None,
    ):
        self.end = end
        self.id = id
        self.sentence_id = sentence_id
        self.start = start
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end is not None:
            result['End'] = self.end

        if self.id is not None:
            result['Id'] = self.id

        if self.sentence_id is not None:
            result['SentenceId'] = self.sentence_id

        if self.start is not None:
            result['Start'] = self.start

        if self.text is not None:
            result['Text'] = self.text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('End') is not None:
            self.end = m.get('End')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('SentenceId') is not None:
            self.sentence_id = m.get('SentenceId')

        if m.get('Start') is not None:
            self.start = m.get('Start')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        return self

