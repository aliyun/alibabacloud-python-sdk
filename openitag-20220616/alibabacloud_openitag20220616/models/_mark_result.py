# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MarkResult(DaraModel):
    def __init__(
        self,
        is_need_vote_judge: bool = None,
        mark_result: str = None,
        mark_result_id: str = None,
        mark_time: str = None,
        mark_title: str = None,
        progress: str = None,
        question_id: str = None,
        result_type: str = None,
        user_mark_result_id: str = None,
        version: str = None,
    ):
        # Indicates whether voting is required. Valid values:  
        # - True: Yes  
        # - False: No
        self.is_need_vote_judge = is_need_vote_judge
        # Question result.
        self.mark_result = mark_result
        # Question ID.
        self.mark_result_id = mark_result_id
        # Annotation time.
        self.mark_time = mark_time
        # Question name.
        self.mark_title = mark_title
        # Progress. The return value is either None or data of JSON type. It includes:  
        # - Total: total number of results.  
        # - Finished: number of completed results.
        self.progress = progress
        # Attached question.
        self.question_id = question_id
        # Result type. Valid values:  
        # - RADIO: Radio  
        # - SLOT: Segment  
        # - INPUT: Fill-in-the-blank  
        # - CHECKBOX: Multiple Choice
        self.result_type = result_type
        # User annotation result ID.
        self.user_mark_result_id = user_mark_result_id
        # Version.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_need_vote_judge is not None:
            result['IsNeedVoteJudge'] = self.is_need_vote_judge

        if self.mark_result is not None:
            result['MarkResult'] = self.mark_result

        if self.mark_result_id is not None:
            result['MarkResultId'] = self.mark_result_id

        if self.mark_time is not None:
            result['MarkTime'] = self.mark_time

        if self.mark_title is not None:
            result['MarkTitle'] = self.mark_title

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.question_id is not None:
            result['QuestionId'] = self.question_id

        if self.result_type is not None:
            result['ResultType'] = self.result_type

        if self.user_mark_result_id is not None:
            result['UserMarkResultId'] = self.user_mark_result_id

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsNeedVoteJudge') is not None:
            self.is_need_vote_judge = m.get('IsNeedVoteJudge')

        if m.get('MarkResult') is not None:
            self.mark_result = m.get('MarkResult')

        if m.get('MarkResultId') is not None:
            self.mark_result_id = m.get('MarkResultId')

        if m.get('MarkTime') is not None:
            self.mark_time = m.get('MarkTime')

        if m.get('MarkTitle') is not None:
            self.mark_title = m.get('MarkTitle')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('QuestionId') is not None:
            self.question_id = m.get('QuestionId')

        if m.get('ResultType') is not None:
            self.result_type = m.get('ResultType')

        if m.get('UserMarkResultId') is not None:
            self.user_mark_result_id = m.get('UserMarkResultId')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

