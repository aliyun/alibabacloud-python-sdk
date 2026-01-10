# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CAPConfig(DaraModel):
    def __init__(
        self,
        function_name: str = None,
        name: str = None,
        template_id: int = None,
    ):
        self.function_name = function_name
        self.name = name
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.function_name is not None:
            result['functionName'] = self.function_name

        if self.name is not None:
            result['name'] = self.name

        if self.template_id is not None:
            result['templateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('functionName') is not None:
            self.function_name = m.get('functionName')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')

        return self

