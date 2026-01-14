# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ga20191120 import models as main_models
from darabonba.model import DaraModel

class DescribeBandwidthPackageResponseBody(DaraModel):
    def __init__(
        self,
        accelerators: List[str] = None,
        bandwidth: int = None,
        bandwidth_package_id: str = None,
        bandwidth_type: str = None,
        billing_type: str = None,
        cbn_geographic_region_id_a: str = None,
        cbn_geographic_region_id_b: str = None,
        charge_type: str = None,
        create_time: str = None,
        description: str = None,
        expired_time: str = None,
        name: str = None,
        ratio: int = None,
        region_id: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        state: str = None,
        tags: List[main_models.DescribeBandwidthPackageResponseBodyTags] = None,
        type: str = None,
    ):
        # The ID of the GA instance that is associated with the bandwidth plan.
        self.accelerators = accelerators
        # The bandwidth value of the bandwidth plan. Unit: Mbit/s.
        self.bandwidth = bandwidth
        # The ID of the bandwidth plan.
        self.bandwidth_package_id = bandwidth_package_id
        # The type of the bandwidth. Valid values:
        # 
        # *   **Basic**: basic bandwidth
        # *   **Enhanced**: enhanced bandwidth
        # *   **Advanced**: premium bandwidth
        self.bandwidth_type = bandwidth_type
        # The metering method that is used when you use the pay-as-you-go billing method. Valid values:
        # 
        # *   **PayByTraffic**: pay-by-data-transfer
        # *   **PayBY95**: pay-by-95th-percentile
        self.billing_type = billing_type
        # Area A specified in the cross-region acceleration bandwidth plan. Only **China-mainland** (the Chinese mainland) is returned.
        # 
        # This parameter is returned only if you call this operation on the International site (alibabacloud.com).
        self.cbn_geographic_region_id_a = cbn_geographic_region_id_a
        # Area B specified in the cross-region acceleration bandwidth plan. Only **Global** (global) is returned.
        # 
        # This parameter is returned only if you call this operation on the International site (alibabacloud.com).
        self.cbn_geographic_region_id_b = cbn_geographic_region_id_b
        # The billing method of the bandwidth plan.
        # 
        # *   **PREPAY**: subscription. This is the default value.
        # *   **POSTPAY**: pay-as-you-go.
        self.charge_type = charge_type
        # The timestamp that indicates when the bandwidth plan was created.
        self.create_time = create_time
        # The description of the bandwidth plan.
        self.description = description
        # The timestamp that indicates when the bandwidth plan expires.
        self.expired_time = expired_time
        # The name of the bandwidth plan.
        self.name = name
        # The percentage of the minimum bandwidth guaranteed if the pay-by-95th-percentile-bandwidth metering method is used. Valid values: **30** to **100**.
        self.ratio = ratio
        # The ID of the region where GA instance is deployed. **cn-hangzhou** is returned.
        self.region_id = region_id
        # The ID of the request.
        self.request_id = request_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The state of the bandwidth plan. Valid values:
        # 
        # *   **init**: The bandwidth plan is being initialized.
        # *   **active**: The bandwidth plan is available.
        # *   **binded**: The bandwidth plan is associated with a GA instance.
        # *   **binding**: The bandwidth plan is being associated.
        # *   **unbinding**: The bandwidth plan is being disassociated.
        # *   **updating**: The bandwidth plan is being updated.
        # *   **finacialLocked**: The bandwidth plan is locked due to overdue payments.
        # *   **Locked**: The bandwidth plan is locked.
        self.state = state
        # Tag objects.
        self.tags = tags
        # The type of the bandwidth plan. Valid values:
        # 
        # *   **Basic**: a basic bandwidth plan
        # *   **CrossDomain**: a cross-region acceleration bandwidth plan
        # 
        # If you call this operation on the Alibaba Cloud China Site (aliyun.com), only **Basic** is returned.
        self.type = type

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

        if self.bandwidth_type is not None:
            result['BandwidthType'] = self.bandwidth_type

        if self.billing_type is not None:
            result['BillingType'] = self.billing_type

        if self.cbn_geographic_region_id_a is not None:
            result['CbnGeographicRegionIdA'] = self.cbn_geographic_region_id_a

        if self.cbn_geographic_region_id_b is not None:
            result['CbnGeographicRegionIdB'] = self.cbn_geographic_region_id_b

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

        if self.ratio is not None:
            result['Ratio'] = self.ratio

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.state is not None:
            result['State'] = self.state

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accelerators') is not None:
            self.accelerators = m.get('Accelerators')

        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')

        if m.get('BandwidthType') is not None:
            self.bandwidth_type = m.get('BandwidthType')

        if m.get('BillingType') is not None:
            self.billing_type = m.get('BillingType')

        if m.get('CbnGeographicRegionIdA') is not None:
            self.cbn_geographic_region_id_a = m.get('CbnGeographicRegionIdA')

        if m.get('CbnGeographicRegionIdB') is not None:
            self.cbn_geographic_region_id_b = m.get('CbnGeographicRegionIdB')

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

        if m.get('Ratio') is not None:
            self.ratio = m.get('Ratio')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('State') is not None:
            self.state = m.get('State')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeBandwidthPackageResponseBodyTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DescribeBandwidthPackageResponseBodyTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N that is added to the bandwidth plan.
        self.key = key
        # The value of tag N that is added to the bandwidth plan.
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

