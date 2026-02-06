# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAITemplateRequest(DaraModel):
    def __init__(
        self,
        template_type: str = None,
    ):
        # The type of the AI template. Valid values:
        # 
        # *   **AIMediaAudit**: automated review
        # *   **AIImage**: smart thumbnail
        # 
        # This parameter is required.
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.template_type is not None:
            result['TemplateType'] = self.template_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')

        return self

