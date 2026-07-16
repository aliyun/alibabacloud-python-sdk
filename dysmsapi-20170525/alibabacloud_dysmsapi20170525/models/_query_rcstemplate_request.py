# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryRCSTemplateRequest(DaraModel):
    def __init__(
        self,
        template_code: str = None,
    ):
        # This parameter is required.
        self.template_code = template_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')

        return self

