# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DescribeNetworkPackagesRequest(DaraModel):
    def __init__(
        self,
        internet_charge_type: str = None,
        max_results: int = None,
        network_package_id: List[str] = None,
        next_token: str = None,
        region_id: str = None,
        tag: List[main_models.DescribeNetworkPackagesRequestTag] = None,
    ):
        # The billing method of the pay-as-you-go premium Internet bandwidth plan.
        self.internet_charge_type = internet_charge_type
        # The number of entries per page in a paged query.    
        # 
        # - Maximum value: 100.    
        # - Default value: 10.
        self.max_results = max_results
        # The IDs of the premium Internet bandwidth plans. You can specify 1 to 100 IDs.
        self.network_package_id = network_package_id
        # The token for the next query.
        self.next_token = next_token
        # The region ID. You can call [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) to query the regions supported by Elastic Desktop Service.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

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

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

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

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeNetworkPackagesRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeNetworkPackagesRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

