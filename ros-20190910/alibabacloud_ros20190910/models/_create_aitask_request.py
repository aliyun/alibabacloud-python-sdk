# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAITaskRequest(DaraModel):
    def __init__(
        self,
        prompt: str = None,
        task_type: str = None,
        template: str = None,
        template_type: str = None,
    ):
        # The input description for the AI task.
        # 
        # - When the task type is Generate Template, this parameter specifies the functionality of the template to be generated.
        # - When the task type is FixTemplate, this parameter can describe how the template should be repaired.
        self.prompt = prompt
        # The type of AI task. Values:
        # - GenerateTemplate: AI template generation
        # - FixTemplate: AI template repair
        self.task_type = task_type
        # When the task type is AI template repair, specify the original template that needs to be fixed or modified.
        self.template = template
        # The type of the template to be generated or repaired. Default is ROS.
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.prompt is not None:
            result['Prompt'] = self.prompt

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.template is not None:
            result['Template'] = self.template

        if self.template_type is not None:
            result['TemplateType'] = self.template_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')

        return self

