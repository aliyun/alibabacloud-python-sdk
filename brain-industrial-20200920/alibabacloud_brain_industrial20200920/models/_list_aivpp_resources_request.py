# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAivppResourcesRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        instance_type: str = None,
        max_results: int = None,
    ):
        self.current_page = current_page
        self.instance_type = instance_type
        self.max_results = max_results

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        return self

