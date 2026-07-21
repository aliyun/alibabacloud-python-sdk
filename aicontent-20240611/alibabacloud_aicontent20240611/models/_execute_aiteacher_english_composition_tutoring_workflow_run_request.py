# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExecuteAITeacherEnglishCompositionTutoringWorkflowRunRequest(DaraModel):
    def __init__(
        self,
        essay_outline: str = None,
        essay_requirements: str = None,
        essay_topic: str = None,
        essay_type: str = None,
        essay_word_count: int = None,
        grade: int = None,
        response_mode: str = None,
        user_id: str = None,
    ):
        # The essay outline.
        self.essay_outline = essay_outline
        # The essay requirements.
        # 
        # This parameter is required.
        self.essay_requirements = essay_requirements
        # The essay topic.
        # 
        # This parameter is required.
        self.essay_topic = essay_topic
        # The essay type. Valid values:
        # 
        # `outline`: an outline
        # 
        # essay: essay
        # 
        # This parameter is required.
        self.essay_type = essay_type
        # The required word count.
        self.essay_word_count = essay_word_count
        # The student\\"s grade level.
        # 
        # This parameter is required.
        self.grade = grade
        # The response mode. For example, set this value to `streaming` to receive server-sent events.
        # 
        # This parameter is required.
        self.response_mode = response_mode
        # The user ID.
        # 
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.essay_outline is not None:
            result['essayOutline'] = self.essay_outline

        if self.essay_requirements is not None:
            result['essayRequirements'] = self.essay_requirements

        if self.essay_topic is not None:
            result['essayTopic'] = self.essay_topic

        if self.essay_type is not None:
            result['essayType'] = self.essay_type

        if self.essay_word_count is not None:
            result['essayWordCount'] = self.essay_word_count

        if self.grade is not None:
            result['grade'] = self.grade

        if self.response_mode is not None:
            result['responseMode'] = self.response_mode

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('essayOutline') is not None:
            self.essay_outline = m.get('essayOutline')

        if m.get('essayRequirements') is not None:
            self.essay_requirements = m.get('essayRequirements')

        if m.get('essayTopic') is not None:
            self.essay_topic = m.get('essayTopic')

        if m.get('essayType') is not None:
            self.essay_type = m.get('essayType')

        if m.get('essayWordCount') is not None:
            self.essay_word_count = m.get('essayWordCount')

        if m.get('grade') is not None:
            self.grade = m.get('grade')

        if m.get('responseMode') is not None:
            self.response_mode = m.get('responseMode')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

