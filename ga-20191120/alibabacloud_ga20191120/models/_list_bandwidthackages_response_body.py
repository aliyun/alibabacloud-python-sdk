# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ga20191120 import models as main_models
from darabonba.model import DaraModel

class ListBandwidthackagesResponseBody(DaraModel):
    def __init__(
        self,
        bandwidth_packages: List[main_models.ListBandwidthackagesResponseBodyBandwidthPackages] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The details of the bandwidth plans.
        self.bandwidth_packages = bandwidth_packages
        # The current page number.
        self.page_number = page_number
        # The number of entries on each page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.bandwidth_packages:
            for v1 in self.bandwidth_packages:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BandwidthPackages'] = []
        if self.bandwidth_packages is not None:
            for k1 in self.bandwidth_packages:
                result['BandwidthPackages'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bandwidth_packages = []
        if m.get('BandwidthPackages') is not None:
            for k1 in m.get('BandwidthPackages'):
                temp_model = main_models.ListBandwidthackagesResponseBodyBandwidthPackages()
                self.bandwidth_packages.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListBandwidthackagesResponseBodyBandwidthPackages(DaraModel):
    def __init__(
        self,
        accelerators: List[str] = None,
        bandwidth: int = None,
        bandwidth_package_id: str = None,
        charge_type: str = None,
        create_time: str = None,
        description: str = None,
        expired_time: str = None,
        name: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        state: str = None,
        tags: List[main_models.ListBandwidthackagesResponseBodyBandwidthPackagesTags] = None,
    ):
        # The IDs of the Global Accelerator instances that are associated with the bandwidth plan.
        self.accelerators = accelerators
        # The bandwidth of the bandwidth plan. Unit: Mbps.
        self.bandwidth = bandwidth
        # The ID of the bandwidth plan.
        self.bandwidth_package_id = bandwidth_package_id
        # The billing method.
        # 
        # - **PREPAY** (default): subscription.
        # 
        # - **POSTPAY**: pay-as-you-go.
        self.charge_type = charge_type
        # The timestamp that indicates when the bandwidth plan was created.
        self.create_time = create_time
        # The description of the bandwidth plan.
        self.description = description
        # The timestamp that indicates when the bandwidth plan expires.
        self.expired_time = expired_time
        # The name of the bandwidth plan.
        self.name = name
        # The ID of the region.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The status of the bandwidth plan.
        # 
        # - **init**: The bandwidth plan is being initialized.
        # 
        # - **active**: The bandwidth plan is available.
        # 
        # - **binded**: The bandwidth plan is bound.
        # 
        # - **binding**: The bandwidth plan is being bound.
        # 
        # - **unbinding**: The bandwidth plan is being unbound.
        # 
        # - **updating**: The bandwidth plan is being updated.
        # 
        # - **finacialLocked**: The bandwidth plan is financially locked.
        # 
        # - **locked**: The bandwidth plan is locked.
        self.state = state
        # The tags of the resource.
        self.tags = tags

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accelerators is not None:
            result['Accelerators'] = self.accelerators

        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.name is not None:
            result['Name'] = self.name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.state is not None:
            result['State'] = self.state

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accelerators') is not None:
            self.accelerators = m.get('Accelerators')

        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('State') is not None:
            self.state = m.get('State')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListBandwidthackagesResponseBodyBandwidthPackagesTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class ListBandwidthackagesResponseBodyBandwidthPackagesTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
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

