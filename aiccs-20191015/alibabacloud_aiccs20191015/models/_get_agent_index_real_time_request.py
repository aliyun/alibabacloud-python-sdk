# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetAgentIndexRealTimeRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        dep_ids: List[int] = None,
        group_ids: List[int] = None,
        instance_id: str = None,
        page_size: int = None,
    ):
        self.current_page = current_page
        self.dep_ids = dep_ids
        self.group_ids = group_ids
        # This parameter is required.
        self.instance_id = instance_id
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.dep_ids is not None:
            result['DepIds'] = self.dep_ids

        if self.group_ids is not None:
            result['GroupIds'] = self.group_ids

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('DepIds') is not None:
            self.dep_ids = m.get('DepIds')

        if m.get('GroupIds') is not None:
            self.group_ids = m.get('GroupIds')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

