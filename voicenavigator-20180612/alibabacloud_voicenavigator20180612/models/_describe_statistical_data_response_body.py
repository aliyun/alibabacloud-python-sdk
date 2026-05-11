# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_voicenavigator20180612 import models as main_models
from darabonba.model import DaraModel

class DescribeStatisticalDataResponseBody(DaraModel):
    def __init__(
        self,
        conversation_total_num: int = None,
        request_id: str = None,
        resolved_question_total_num: int = None,
        statistical_data_reports: List[main_models.DescribeStatisticalDataResponseBodyStatisticalDataReports] = None,
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
            for v1 in self.statistical_data_reports:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.conversation_total_num is not None:
            result['ConversationTotalNum'] = self.conversation_total_num

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resolved_question_total_num is not None:
            result['ResolvedQuestionTotalNum'] = self.resolved_question_total_num

        result['StatisticalDataReports'] = []
        if self.statistical_data_reports is not None:
            for k1 in self.statistical_data_reports:
                result['StatisticalDataReports'].append(k1.to_map() if k1 else None)

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
            for k1 in m.get('StatisticalDataReports'):
                temp_model = main_models.DescribeStatisticalDataResponseBodyStatisticalDataReports()
                self.statistical_data_reports.append(temp_model.from_map(k1))

        if m.get('TotalDialoguePassRate') is not None:
            self.total_dialogue_pass_rate = m.get('TotalDialoguePassRate')

        if m.get('TotalKnowledgeHitRate') is not None:
            self.total_knowledge_hit_rate = m.get('TotalKnowledgeHitRate')

        if m.get('TotalResolutionRate') is not None:
            self.total_resolution_rate = m.get('TotalResolutionRate')

        if m.get('TotalValidAnswerRate') is not None:
            self.total_valid_answer_rate = m.get('TotalValidAnswerRate')

        return self

class DescribeStatisticalDataResponseBodyStatisticalDataReports(DaraModel):
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

