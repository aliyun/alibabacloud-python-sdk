# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTodoOpsTaskApprovalsRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        keyword: str = None,
        page_number: str = None,
        page_size: str = None,
        region_id: str = None,
        schedule_type: str = None,
    ):
        # The instance ID of the bastion host.
        # > You can invoke the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to obtain this parameter.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The task name or task remarks to query. Fuzzy match is supported.
        self.keyword = keyword
        # The page number of the page to return in a paging query. Default value: **1**.
        self.page_number = page_number
        # The maximum number of entries per page in a paging query.  
        # The maximum value of the PageSize parameter is 100. The default number of entries per page is 20. If PageSize is left empty, 20 entries are returned by default.
        # > Do not leave PageSize empty.
        self.page_size = page_size
        # The region ID of the bastion host.
        # > For the mapping between region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        self.region_id = region_id
        # The task scheduling type used to filter results. Valid values:
        # - **FixTime**: scheduled execution.
        # - **CycleInterval**: periodic execution.
        # - **Manual**: manually triggered by a user.
        self.schedule_type = schedule_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.schedule_type is not None:
            result['ScheduleType'] = self.schedule_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ScheduleType') is not None:
            self.schedule_type = m.get('ScheduleType')

        return self

