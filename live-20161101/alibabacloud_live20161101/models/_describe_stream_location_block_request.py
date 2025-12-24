# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeStreamLocationBlockRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        block_type: str = None,
        domain_name: str = None,
        owner_id: int = None,
        page_num: int = None,
        page_size: int = None,
        region_id: str = None,
        stream_name: str = None,
    ):
        # The name of the application to which the live stream belongs.
        self.app_name = app_name
        # The blocking type. Valid values:
        # 
        # *   blacklist
        # *   whitelist
        self.block_type = block_type
        # The streaming domain.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        self.owner_id = owner_id
        # The page number. Default value: 1.
        self.page_num = page_num
        # The number of entries per page. Valid values: integers from 1 to 100.
        self.page_size = page_size
        self.region_id = region_id
        # The name of the live stream.
        self.stream_name = stream_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.block_type is not None:
            result['BlockType'] = self.block_type

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.stream_name is not None:
            result['StreamName'] = self.stream_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('BlockType') is not None:
            self.block_type = m.get('BlockType')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        return self

