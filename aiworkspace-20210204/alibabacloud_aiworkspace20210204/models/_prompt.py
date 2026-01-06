# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Prompt(DaraModel):
    def __init__(
        self,
        accessibility: str = None,
        create_time: str = None,
        description: str = None,
        framework_content: str = None,
        framework_type: str = None,
        modify_time: str = None,
        prompt_id: str = None,
        prompt_name: str = None,
    ):
        self.accessibility = accessibility
        self.create_time = create_time
        self.description = description
        self.framework_content = framework_content
        self.framework_type = framework_type
        self.modify_time = modify_time
        self.prompt_id = prompt_id
        self.prompt_name = prompt_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.framework_content is not None:
            result['FrameworkContent'] = self.framework_content

        if self.framework_type is not None:
            result['FrameworkType'] = self.framework_type

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.prompt_id is not None:
            result['PromptId'] = self.prompt_id

        if self.prompt_name is not None:
            result['PromptName'] = self.prompt_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FrameworkContent') is not None:
            self.framework_content = m.get('FrameworkContent')

        if m.get('FrameworkType') is not None:
            self.framework_type = m.get('FrameworkType')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('PromptId') is not None:
            self.prompt_id = m.get('PromptId')

        if m.get('PromptName') is not None:
            self.prompt_name = m.get('PromptName')

        return self

