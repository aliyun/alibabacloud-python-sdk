# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetSkillGroupAgentStatusDetailsRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        dep_ids: List[int] = None,
        end_date: int = None,
        exist_department_grouping: bool = None,
        exist_skill_group_grouping: bool = None,
        group_ids: List[int] = None,
        instance_id: str = None,
        page_size: int = None,
        start_date: int = None,
    ):
        self.current_page = current_page
        self.dep_ids = dep_ids
        self.end_date = end_date
        self.exist_department_grouping = exist_department_grouping
        self.exist_skill_group_grouping = exist_skill_group_grouping
        self.group_ids = group_ids
        # This parameter is required.
        self.instance_id = instance_id
        self.page_size = page_size
        self.start_date = start_date

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

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.exist_department_grouping is not None:
            result['ExistDepartmentGrouping'] = self.exist_department_grouping

        if self.exist_skill_group_grouping is not None:
            result['ExistSkillGroupGrouping'] = self.exist_skill_group_grouping

        if self.group_ids is not None:
            result['GroupIds'] = self.group_ids

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('DepIds') is not None:
            self.dep_ids = m.get('DepIds')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('ExistDepartmentGrouping') is not None:
            self.exist_department_grouping = m.get('ExistDepartmentGrouping')

        if m.get('ExistSkillGroupGrouping') is not None:
            self.exist_skill_group_grouping = m.get('ExistSkillGroupGrouping')

        if m.get('GroupIds') is not None:
            self.group_ids = m.get('GroupIds')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        return self

