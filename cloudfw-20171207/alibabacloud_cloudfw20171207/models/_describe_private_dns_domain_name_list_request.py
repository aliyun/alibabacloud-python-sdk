# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePrivateDnsDomainNameListRequest(DaraModel):
    def __init__(
        self,
        access_instance_id: str = None,
        domain_name: str = None,
        page_no: int = None,
        page_size: int = None,
        region_no: str = None,
    ):
        # This parameter is required.
        self.access_instance_id = access_instance_id
        self.domain_name = domain_name
        self.page_no = page_no
        self.page_size = page_size
        # This parameter is required.
        self.region_no = region_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_instance_id is not None:
            result['AccessInstanceId'] = self.access_instance_id

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessInstanceId') is not None:
            self.access_instance_id = m.get('AccessInstanceId')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        return self

