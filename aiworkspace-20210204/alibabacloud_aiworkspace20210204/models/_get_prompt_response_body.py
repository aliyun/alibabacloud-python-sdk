# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetPromptResponseBody(DaraModel):
    def __init__(
        self,
        accessibility: str = None,
        create_time: str = None,
        description: str = None,
        framework_content: str = None,
        framework_type: str = None,
        modify_time: str = None,
        prompt_name: str = None,
        request_id: str = None,
    ):
        # The access type. Valid values:
        # 
        # - PUBLIC: All members in the current workspace can access the prompt.
        # - PRIVATE: Only the creator can access the prompt.
        self.accessibility = accessibility
        # The creation time.
        self.create_time = create_time
        # The prompt description.
        self.description = description
        # The prompt content.
        self.framework_content = framework_content
        # The prompt template framework type.
        self.framework_type = framework_type
        # The modification time.
        self.modify_time = modify_time
        # The prompt name.
        self.prompt_name = prompt_name
        # The request ID.
        self.request_id = request_id

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

        if self.prompt_name is not None:
            result['PromptName'] = self.prompt_name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

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

        if m.get('PromptName') is not None:
            self.prompt_name = m.get('PromptName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

