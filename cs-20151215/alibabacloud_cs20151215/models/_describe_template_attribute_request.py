# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeTemplateAttributeRequest(DaraModel):
    def __init__(
        self,
        template_type: str = None,
    ):
        # The templatetype.
        # 
        # - If this parameter is set to `kubernetes`, the template is displayed on the Orchestration Templates page in the console.
        # 
        # - If this parameter is not specified or is set to another value, the template is not displayed on the Orchestration Templates page in the console.
        # 
        # Recommended Settings: `kubernetes`.
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.template_type is not None:
            result['template_type'] = self.template_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('template_type') is not None:
            self.template_type = m.get('template_type')

        return self

