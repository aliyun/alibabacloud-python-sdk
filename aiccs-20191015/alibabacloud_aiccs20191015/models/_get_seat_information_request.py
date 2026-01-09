# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetSeatInformationRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        current_page: int = None,
        dep_ids: List[int] = None,
        end_date: int = None,
        exist_department_grouping: bool = None,
        page_size: int = None,
        start_date: int = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        self.current_page = current_page
        self.dep_ids = dep_ids
        self.end_date = end_date
        self.exist_department_grouping = exist_department_grouping
        self.page_size = page_size
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.current_page is not None:
            result['currentPage'] = self.current_page

        if self.dep_ids is not None:
            result['depIds'] = self.dep_ids

        if self.end_date is not None:
            result['endDate'] = self.end_date

        if self.exist_department_grouping is not None:
            result['existDepartmentGrouping'] = self.exist_department_grouping

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.start_date is not None:
            result['startDate'] = self.start_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')

        if m.get('depIds') is not None:
            self.dep_ids = m.get('depIds')

        if m.get('endDate') is not None:
            self.end_date = m.get('endDate')

        if m.get('existDepartmentGrouping') is not None:
            self.exist_department_grouping = m.get('existDepartmentGrouping')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('startDate') is not None:
            self.start_date = m.get('startDate')

        return self

