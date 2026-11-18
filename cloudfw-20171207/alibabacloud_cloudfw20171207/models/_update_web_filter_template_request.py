# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateWebFilterTemplateRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        status: str = None,
        web_filter_template_id: str = None,
    ):
        # The description of the web filtering template. The description can be up to 128 characters in length. If this parameter is not specified, the original value is retained. If an empty string is specified, the description is cleared.
        self.description = description
        # The name of the web filtering template. The name must be 1 to 64 characters in length and can contain Chinese characters, English letters, digits, hyphens (-), underscores (_), and periods (.). It cannot contain spaces. If this parameter is not specified or is left empty, the original value is retained.
        self.name = name
        # The status of the web filtering template. Valid values:
        # - **Enable**: Enabled.
        # - **Disable**: Disabled.
        # If this parameter is not specified or is left empty, the original value is retained.
        self.status = status
        # The ID of the web filtering template to be modified. The template must exist within the current Alibaba Cloud account.
        # 
        # This parameter is required.
        self.web_filter_template_id = web_filter_template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.status is not None:
            result['Status'] = self.status

        if self.web_filter_template_id is not None:
            result['WebFilterTemplateId'] = self.web_filter_template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('WebFilterTemplateId') is not None:
            self.web_filter_template_id = m.get('WebFilterTemplateId')

        return self

