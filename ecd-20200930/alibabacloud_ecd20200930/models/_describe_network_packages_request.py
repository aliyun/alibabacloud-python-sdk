# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeNetworkPackagesRequest(DaraModel):
    def __init__(
        self,
        internet_charge_type: str = None,
        max_results: int = None,
        network_package_id: List[str] = None,
        next_token: str = None,
        region_id: str = None,
    ):
        # The charge type of the pay-as-you-go premium bandwidth plan.
        # 
        # Valid values:
        # 
        # *   PayByTraffic: charges by data transfer.
        # 
        # *   PayByBandwidth: charges by fixed bandwidth.
        self.internet_charge_type = internet_charge_type
        # The number of entries to return on each page.
        # 
        # *   Maximum value: 100
        # *   Default value: 10
        self.max_results = max_results
        # The ID of the premium bandwidth plan. You can specify 1 to 100 IDs.
        self.network_package_id = network_package_id
        # The token that determines the start point of the next query.
        self.next_token = next_token
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
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.network_package_id is not None:
            result['NetworkPackageId'] = self.network_package_id

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NetworkPackageId') is not None:
            self.network_package_id = m.get('NetworkPackageId')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

