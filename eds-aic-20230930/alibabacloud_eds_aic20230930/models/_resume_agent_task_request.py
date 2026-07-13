# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_aic20230930 import models as main_models
from darabonba.model import DaraModel

class ResumeAgentTaskRequest(DaraModel):
    def __init__(
        self,
        additional_prompt: str = None,
        clarification_answers: List[main_models.ResumeAgentTaskRequestClarificationAnswers] = None,
        task_ids: List[str] = None,
        tool_call_id: str = None,
    ):
        # The additional prompt to append. This parameter takes effect only when the task is passively paused, such as when the task is paused and waiting for user confirmation.
        self.additional_prompt = additional_prompt
        self.clarification_answers = clarification_answers
        # The list of task IDs.
        # 
        # This parameter is required.
        self.task_ids = task_ids
        self.tool_call_id = tool_call_id

    def validate(self):
        if self.clarification_answers:
            for v1 in self.clarification_answers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.additional_prompt is not None:
            result['AdditionalPrompt'] = self.additional_prompt

        result['ClarificationAnswers'] = []
        if self.clarification_answers is not None:
            for k1 in self.clarification_answers:
                result['ClarificationAnswers'].append(k1.to_map() if k1 else None)

        if self.task_ids is not None:
            result['TaskIds'] = self.task_ids

        if self.tool_call_id is not None:
            result['ToolCallId'] = self.tool_call_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdditionalPrompt') is not None:
            self.additional_prompt = m.get('AdditionalPrompt')

        self.clarification_answers = []
        if m.get('ClarificationAnswers') is not None:
            for k1 in m.get('ClarificationAnswers'):
                temp_model = main_models.ResumeAgentTaskRequestClarificationAnswers()
                self.clarification_answers.append(temp_model.from_map(k1))

        if m.get('TaskIds') is not None:
            self.task_ids = m.get('TaskIds')

        if m.get('ToolCallId') is not None:
            self.tool_call_id = m.get('ToolCallId')

        return self

class ResumeAgentTaskRequestClarificationAnswers(DaraModel):
    def __init__(
        self,
        custom_value: str = None,
        id: str = None,
        selected_ids: List[str] = None,
    ):
        self.custom_value = custom_value
        self.id = id
        self.selected_ids = selected_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_value is not None:
            result['CustomValue'] = self.custom_value

        if self.id is not None:
            result['Id'] = self.id

        if self.selected_ids is not None:
            result['SelectedIds'] = self.selected_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomValue') is not None:
            self.custom_value = m.get('CustomValue')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('SelectedIds') is not None:
            self.selected_ids = m.get('SelectedIds')

        return self

