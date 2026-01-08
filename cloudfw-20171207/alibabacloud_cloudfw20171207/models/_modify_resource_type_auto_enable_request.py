# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyResourceTypeAutoEnableRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        resource_type_auto_enable: str = None,
    ):
        self.lang = lang
        self.resource_type_auto_enable = resource_type_auto_enable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.resource_type_auto_enable is not None:
            result['ResourceTypeAutoEnable'] = self.resource_type_auto_enable

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('ResourceTypeAutoEnable') is not None:
            self.resource_type_auto_enable = m.get('ResourceTypeAutoEnable')

        return self

