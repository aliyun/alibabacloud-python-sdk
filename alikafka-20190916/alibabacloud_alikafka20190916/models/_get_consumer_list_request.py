# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetConsumerListRequest(DaraModel):
    def __init__(
        self,
        consumer_id: str = None,
        current_page: int = None,
        instance_id: str = None,
        page_size: int = None,
        region_id: str = None,
    ):
        # The name of the consumer group. If you do not configure this parameter, all consumer groups are queried.
        self.consumer_id = consumer_id
        # The page number.
        self.current_page = current_page
        # The ID of the instance to which the consumer group belongs.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The number of entries to be returned per page.
        self.page_size = page_size
        # The region ID of the instance to which the consumer group belongs.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.consumer_id is not None:
            result['ConsumerId'] = self.consumer_id

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsumerId') is not None:
            self.consumer_id = m.get('ConsumerId')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

