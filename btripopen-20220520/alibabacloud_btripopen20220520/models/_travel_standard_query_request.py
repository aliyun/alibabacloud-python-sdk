# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class TravelStandardQueryRequest(DaraModel):
    def __init__(
        self,
        from_group: bool = None,
        rule_code: int = None,
        service_type_list: List[str] = None,
    ):
        # This parameter is required.
        self.from_group = from_group
        # This parameter is required.
        self.rule_code = rule_code
        # This parameter is required.
        self.service_type_list = service_type_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_group is not None:
            result['from_group'] = self.from_group

        if self.rule_code is not None:
            result['rule_code'] = self.rule_code

        if self.service_type_list is not None:
            result['service_type_list'] = self.service_type_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('from_group') is not None:
            self.from_group = m.get('from_group')

        if m.get('rule_code') is not None:
            self.rule_code = m.get('rule_code')

        if m.get('service_type_list') is not None:
            self.service_type_list = m.get('service_type_list')

        return self

