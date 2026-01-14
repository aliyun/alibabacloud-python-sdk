# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAICoachTaskSessionReportResponseBody(DaraModel):
    def __init__(
        self,
        duration: int = None,
        end_time: str = None,
        evaluation_rating: str = None,
        evaluation_result: str = None,
        feedback: bool = None,
        request_id: str = None,
        script_name: str = None,
        start_time: str = None,
        status: str = None,
        uid: str = None,
    ):
        self.duration = duration
        self.end_time = end_time
        self.evaluation_rating = evaluation_rating
        self.evaluation_result = evaluation_result
        self.feedback = feedback
        self.request_id = request_id
        self.script_name = script_name
        self.start_time = start_time
        self.status = status
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration is not None:
            result['duration'] = self.duration

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.evaluation_rating is not None:
            result['evaluationRating'] = self.evaluation_rating

        if self.evaluation_result is not None:
            result['evaluationResult'] = self.evaluation_result

        if self.feedback is not None:
            result['feedback'] = self.feedback

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.script_name is not None:
            result['scriptName'] = self.script_name

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.status is not None:
            result['status'] = self.status

        if self.uid is not None:
            result['uid'] = self.uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('duration') is not None:
            self.duration = m.get('duration')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('evaluationRating') is not None:
            self.evaluation_rating = m.get('evaluationRating')

        if m.get('evaluationResult') is not None:
            self.evaluation_result = m.get('evaluationResult')

        if m.get('feedback') is not None:
            self.feedback = m.get('feedback')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('scriptName') is not None:
            self.script_name = m.get('scriptName')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('uid') is not None:
            self.uid = m.get('uid')

        return self

