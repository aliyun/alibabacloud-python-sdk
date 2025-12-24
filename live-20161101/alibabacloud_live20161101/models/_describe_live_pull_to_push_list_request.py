# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeLivePullToPushListRequest(DaraModel):
    def __init__(
        self,
        dst_url: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region: str = None,
        region_id: str = None,
        task_id: str = None,
        task_name: str = None,
    ):
        # The destination URL. Fuzzy search is performed based on the destination URL.
        self.dst_url = dst_url
        self.owner_id = owner_id
        # The page number.
        # 
        # >  The value must be greater than 0 and not greater than the maximum value of the Integer data type. Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        # 
        # >  Valid values: [1,100]. Default value: 10.
        self.page_size = page_size
        # The region of the live center. Valid values:
        # 
        # *   ap-southeast-1: Singapore
        # *   ap-southeast-5: Indonesia (Jakarta)
        # *   cn-beijing: China (Beijing)
        # *   cn-shanghai: China (Shanghai)
        # 
        # This parameter is required.
        self.region = region
        self.region_id = region_id
        # The task ID. Fuzzy search is performed based on the task ID.
        # 
        # >  The ID can be up to 55 characters in length and can contain letters, digits, underscores (_), and hyphens (-).
        self.task_id = task_id
        # The task name. Fuzzy search is performed based on the task name.
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dst_url is not None:
            result['DstUrl'] = self.dst_url

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region is not None:
            result['Region'] = self.region

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DstUrl') is not None:
            self.dst_url = m.get('DstUrl')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        return self

