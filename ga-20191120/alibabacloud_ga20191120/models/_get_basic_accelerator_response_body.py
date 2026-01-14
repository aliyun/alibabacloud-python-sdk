# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ga20191120 import models as main_models
from darabonba.model import DaraModel

class GetBasicAcceleratorResponseBody(DaraModel):
    def __init__(
        self,
        accelerator_id: str = None,
        bandwidth_billing_type: str = None,
        basic_bandwidth_package: main_models.GetBasicAcceleratorResponseBodyBasicBandwidthPackage = None,
        basic_endpoint_group_id: str = None,
        basic_ip_set_id: str = None,
        cen_id: str = None,
        create_time: int = None,
        cross_border_status: bool = None,
        cross_domain_bandwidth_package: main_models.GetBasicAcceleratorResponseBodyCrossDomainBandwidthPackage = None,
        cross_private_state: str = None,
        description: str = None,
        expired_time: int = None,
        instance_charge_type: str = None,
        name: str = None,
        region_id: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        state: str = None,
        tags: List[main_models.GetBasicAcceleratorResponseBodyTags] = None,
    ):
        # The ID of the basic GA instance.
        self.accelerator_id = accelerator_id
        # The bandwidth metering method.
        # 
        # *   **BandwidthPackage**: billed based on bandwidth plans.
        # *   **CDT**: billed by Cloud Data Transfer (CDT) and based on data transfer.
        # *   **CDT95**: billed by CDT and based on the 95th percentile bandwidth. This bandwidth metering method is available only to users that are included in the whitelist.
        self.bandwidth_billing_type = bandwidth_billing_type
        # The details about the basic bandwidth plan that is associated with the basic GA instance.
        self.basic_bandwidth_package = basic_bandwidth_package
        # The ID of the endpoint group.
        self.basic_endpoint_group_id = basic_endpoint_group_id
        # The ID of the acceleration region.
        self.basic_ip_set_id = basic_ip_set_id
        # The ID of the Cloud Enterprise Network (CEN) instance to which the basic GA instance is attached.
        self.cen_id = cen_id
        # The timestamp that indicates when the basic GA instance is created.
        self.create_time = create_time
        # Indicates whether cross-border acceleration is enabled for the basic GA instance. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.cross_border_status = cross_border_status
        # The details about the cross-border acceleration bandwidth plan that is associated with the GA instance.
        # 
        # This array is returned only for GA instances that are created on the international site (alibabacloud.com).
        self.cross_domain_bandwidth_package = cross_domain_bandwidth_package
        # Indicates whether cross-border acceleration is enabled.
        # 
        # *   **true**: yes
        # *   **false**: no
        self.cross_private_state = cross_private_state
        # The description of the basic GA instance.
        self.description = description
        # The timestamp that indicates when the basic GA instance expires.
        # 
        # The time follows the UNIX time format. It is the number of seconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC.
        self.expired_time = expired_time
        # The billing method of the basic GA instance. Only **PREPAY** is returned, which indicates the subscription billing method.
        self.instance_charge_type = instance_charge_type
        # The name of the basic GA instance.
        self.name = name
        # The ID of the region where the basic GA instance is deployed.
        self.region_id = region_id
        # The ID of the request.
        self.request_id = request_id
        # The ID of the resource group to which the basic GA instance belongs.
        self.resource_group_id = resource_group_id
        # The status of the basic GA instance.
        # 
        # *   **init**: The GA instance is being initialized.
        # *   **active**: The GA instance is available.
        # *   **configuring**: The GA instance is being configured.
        # *   **binding**: The GA instance is being associated.
        # *   **unbinding**: The GA instance is being disassociated.
        # *   **deleting**: The GA instance is being deleted.
        # *   **finacialLocked**: The GA instance is locked due to overdue payments.
        self.state = state
        # The tags of the basic GA instance.
        self.tags = tags

    def validate(self):
        if self.basic_bandwidth_package:
            self.basic_bandwidth_package.validate()
        if self.cross_domain_bandwidth_package:
            self.cross_domain_bandwidth_package.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id

        if self.bandwidth_billing_type is not None:
            result['BandwidthBillingType'] = self.bandwidth_billing_type

        if self.basic_bandwidth_package is not None:
            result['BasicBandwidthPackage'] = self.basic_bandwidth_package.to_map()

        if self.basic_endpoint_group_id is not None:
            result['BasicEndpointGroupId'] = self.basic_endpoint_group_id

        if self.basic_ip_set_id is not None:
            result['BasicIpSetId'] = self.basic_ip_set_id

        if self.cen_id is not None:
            result['CenId'] = self.cen_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.cross_border_status is not None:
            result['CrossBorderStatus'] = self.cross_border_status

        if self.cross_domain_bandwidth_package is not None:
            result['CrossDomainBandwidthPackage'] = self.cross_domain_bandwidth_package.to_map()

        if self.cross_private_state is not None:
            result['CrossPrivateState'] = self.cross_private_state

        if self.description is not None:
            result['Description'] = self.description

        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type

        if self.name is not None:
            result['Name'] = self.name

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')

        if m.get('BandwidthBillingType') is not None:
            self.bandwidth_billing_type = m.get('BandwidthBillingType')

        if m.get('BasicBandwidthPackage') is not None:
            temp_model = main_models.GetBasicAcceleratorResponseBodyBasicBandwidthPackage()
            self.basic_bandwidth_package = temp_model.from_map(m.get('BasicBandwidthPackage'))

        if m.get('BasicEndpointGroupId') is not None:
            self.basic_endpoint_group_id = m.get('BasicEndpointGroupId')

        if m.get('BasicIpSetId') is not None:
            self.basic_ip_set_id = m.get('BasicIpSetId')

        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CrossBorderStatus') is not None:
            self.cross_border_status = m.get('CrossBorderStatus')

        if m.get('CrossDomainBandwidthPackage') is not None:
            temp_model = main_models.GetBasicAcceleratorResponseBodyCrossDomainBandwidthPackage()
            self.cross_domain_bandwidth_package = temp_model.from_map(m.get('CrossDomainBandwidthPackage'))

        if m.get('CrossPrivateState') is not None:
            self.cross_private_state = m.get('CrossPrivateState')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

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
                temp_model = main_models.GetBasicAcceleratorResponseBodyTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class GetBasicAcceleratorResponseBodyTags(DaraModel):
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

class GetBasicAcceleratorResponseBodyCrossDomainBandwidthPackage(DaraModel):
    def __init__(
        self,
        bandwidth: int = None,
        instance_id: str = None,
    ):
        # The bandwidth value of the cross-border acceleration bandwidth plan. Unit: Mbit/s.
        self.bandwidth = bandwidth
        # The ID of the cross-border acceleration bandwidth plan.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

class GetBasicAcceleratorResponseBodyBasicBandwidthPackage(DaraModel):
    def __init__(
        self,
        bandwidth: int = None,
        bandwidth_type: str = None,
        instance_id: str = None,
    ):
        # The bandwidth value of the basic bandwidth plan. Unit: Mbit/s.
        self.bandwidth = bandwidth
        # The type of the bandwidth that is provided by the basic bandwidth plan.
        # 
        # *   **Basic**: basic
        # *   **Enhanced**: enhanced
        # *   **Advanced**: premium
        self.bandwidth_type = bandwidth_type
        # The ID of the basic bandwidth plan.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.bandwidth_type is not None:
            result['BandwidthType'] = self.bandwidth_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('BandwidthType') is not None:
            self.bandwidth_type = m.get('BandwidthType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

