# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AssociateNetworkPackageRequest(DaraModel):
    def __init__(
        self,
        network_package_id: str = None,
        office_site_id: str = None,
        region_id: str = None,
    ):
        # The ID of the premium bandwidth plan.
        # 
        # This parameter is required.
        self.network_package_id = network_package_id
        # The ID of the office network. You can call the [DescribeNetworkPackages](https://help.aliyun.com/document_detail/216079.html) to obtain the ID of the office network to which a premium bandwidth plan is bound.
        # 
        # This parameter is required.
        self.office_site_id = office_site_id
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) operation to query the most recent region list.
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
        if self.network_package_id is not None:
            result['NetworkPackageId'] = self.network_package_id

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkPackageId') is not None:
            self.network_package_id = m.get('NetworkPackageId')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

