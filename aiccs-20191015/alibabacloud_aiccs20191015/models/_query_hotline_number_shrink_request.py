# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryHotlineNumberShrinkRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        department_id: int = None,
        group_ids_shrink: str = None,
        hotline_number: str = None,
        instance_id: str = None,
        page_size: int = None,
    ):
        # This parameter is required.
        self.current_page = current_page
        self.department_id = department_id
        self.group_ids_shrink = group_ids_shrink
        self.hotline_number = hotline_number
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
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

        if self.department_id is not None:
            result['DepartmentId'] = self.department_id

        if self.group_ids_shrink is not None:
            result['GroupIds'] = self.group_ids_shrink

        if self.hotline_number is not None:
            result['HotlineNumber'] = self.hotline_number

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('DepartmentId') is not None:
            self.department_id = m.get('DepartmentId')

        if m.get('GroupIds') is not None:
            self.group_ids_shrink = m.get('GroupIds')

        if m.get('HotlineNumber') is not None:
            self.hotline_number = m.get('HotlineNumber')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

