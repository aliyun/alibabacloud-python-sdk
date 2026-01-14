# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_intelligentcreation20240313 import models as main_models
from darabonba.model import DaraModel

class GetAICoachTaskSessionHistoryResponseBody(DaraModel):
    def __init__(
        self,
        conversation_list: List[main_models.GetAICoachTaskSessionHistoryResponseBodyConversationList] = None,
        duration: int = None,
        end_time: str = None,
        pause_duration: int = None,
        request_id: str = None,
        script_name: str = None,
        start_time: str = None,
        status: str = None,
        total: int = None,
        uid: str = None,
    ):
        self.conversation_list = conversation_list
        self.duration = duration
        self.end_time = end_time
        self.pause_duration = pause_duration
        self.request_id = request_id
        self.script_name = script_name
        self.start_time = start_time
        self.status = status
        self.total = total
        self.uid = uid

    def validate(self):
        if self.conversation_list:
            for v1 in self.conversation_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['conversationList'] = []
        if self.conversation_list is not None:
            for k1 in self.conversation_list:
                result['conversationList'].append(k1.to_map() if k1 else None)

        if self.duration is not None:
            result['duration'] = self.duration

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.pause_duration is not None:
            result['pauseDuration'] = self.pause_duration

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.script_name is not None:
            result['scriptName'] = self.script_name

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.status is not None:
            result['status'] = self.status

        if self.total is not None:
            result['total'] = self.total

        if self.uid is not None:
            result['uid'] = self.uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.conversation_list = []
        if m.get('conversationList') is not None:
            for k1 in m.get('conversationList'):
                temp_model = main_models.GetAICoachTaskSessionHistoryResponseBodyConversationList()
                self.conversation_list.append(temp_model.from_map(k1))

        if m.get('duration') is not None:
            self.duration = m.get('duration')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('pauseDuration') is not None:
            self.pause_duration = m.get('pauseDuration')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('scriptName') is not None:
            self.script_name = m.get('scriptName')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('total') is not None:
            self.total = m.get('total')

        if m.get('uid') is not None:
            self.uid = m.get('uid')

        return self

class GetAICoachTaskSessionHistoryResponseBodyConversationList(DaraModel):
    def __init__(
        self,
        audio_url: str = None,
        date_label: str = None,
        evaluation_feedback: str = None,
        evaluation_result: str = None,
        message: str = None,
        record_id: str = None,
        role: str = None,
    ):
        self.audio_url = audio_url
        self.date_label = date_label
        self.evaluation_feedback = evaluation_feedback
        self.evaluation_result = evaluation_result
        self.message = message
        self.record_id = record_id
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audio_url is not None:
            result['audioUrl'] = self.audio_url

        if self.date_label is not None:
            result['dateLabel'] = self.date_label

        if self.evaluation_feedback is not None:
            result['evaluationFeedback'] = self.evaluation_feedback

        if self.evaluation_result is not None:
            result['evaluationResult'] = self.evaluation_result

        if self.message is not None:
            result['message'] = self.message

        if self.record_id is not None:
            result['recordId'] = self.record_id

        if self.role is not None:
            result['role'] = self.role

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('audioUrl') is not None:
            self.audio_url = m.get('audioUrl')

        if m.get('dateLabel') is not None:
            self.date_label = m.get('dateLabel')

        if m.get('evaluationFeedback') is not None:
            self.evaluation_feedback = m.get('evaluationFeedback')

        if m.get('evaluationResult') is not None:
            self.evaluation_result = m.get('evaluationResult')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('recordId') is not None:
            self.record_id = m.get('recordId')

        if m.get('role') is not None:
            self.role = m.get('role')

        return self

