# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TravelStandardListQueryRequest(DaraModel):
    def __init__(
        self,
        from_group: bool = None,
        page_no: int = None,
        page_size: int = None,
        rule_name: str = None,
    ):
        self.from_group = from_group
        # This parameter is required.
        self.page_no = page_no
        # This parameter is required.
        self.page_size = page_size
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_group is not None:
            result['from_group'] = self.from_group

        if self.page_no is not None:
            result['page_no'] = self.page_no

        if self.page_size is not None:
            result['page_size'] = self.page_size

        if self.rule_name is not None:
            result['rule_name'] = self.rule_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('from_group') is not None:
            self.from_group = m.get('from_group')

        if m.get('page_no') is not None:
            self.page_no = m.get('page_no')

        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')

        if m.get('rule_name') is not None:
            self.rule_name = m.get('rule_name')

        return self

