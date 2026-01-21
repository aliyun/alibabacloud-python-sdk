# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_yundun_bastionhost20191209 import models as main_models
from darabonba.model import DaraModel

class DescribeInstancesResponseBody(DaraModel):
    def __init__(
        self,
        instances: List[main_models.DescribeInstancesResponseBodyInstances] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # An array that consists of the bastion hosts returned.
        self.instances = instances
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The total number of bastion hosts that are queried.
        self.total_count = total_count

    def validate(self):
        if self.instances:
            for v1 in self.instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Instances'] = []
        if self.instances is not None:
            for k1 in self.instances:
                result['Instances'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instances = []
        if m.get('Instances') is not None:
            for k1 in m.get('Instances'):
                temp_model = main_models.DescribeInstancesResponseBodyInstances()
                self.instances.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeInstancesResponseBodyInstances(DaraModel):
    def __init__(
        self,
        band_width: int = None,
        description: str = None,
        expire_time: int = None,
        image_version: str = None,
        instance_id: str = None,
        instance_status: str = None,
        internet_endpoint: str = None,
        intranet_endpoint: str = None,
        legacy: bool = None,
        license_code: str = None,
        plan_code: str = None,
        public_network_access: bool = None,
        region_id: str = None,
        resource_group_id: str = None,
        slave_vswitch_id: str = None,
        start_time: int = None,
        vpc_id: str = None,
        vswitch_id: str = None,
    ):
        self.band_width = band_width
        # The remarks of the bastion host.
        self.description = description
        # The timestamp when the bastion host expires. Unit: milliseconds.
        self.expire_time = expire_time
        # The image version of the bastion host.
        self.image_version = image_version
        # The bastion host ID.
        self.instance_id = instance_id
        # The status of the bastion host. Valid values:
        # 
        # *   **PENDING**: The bastion host is not initialized.
        # *   **CREATING**: The bastion host is being created.
        # *   **RUNNING**: The bastion host is running.
        # *   **EXPIRED**: The bastion host expired.
        # *   **CREATE_FAILED**: The bastion host fails to be created.
        # *   **UPGRADING**: The configurations of the bastion host are being changed.
        # *   **UPGRADE_FAILED**: The configurations of the bastion host fail to be changed.
        self.instance_status = instance_status
        # The public O\\&M address of the bastion host.
        self.internet_endpoint = internet_endpoint
        # The private O\\&M address of the bastion host.
        self.intranet_endpoint = intranet_endpoint
        # Indicates whether the bastion host runs an earlier version. Valid values:
        # 
        # *   **true**: The bastion host runs V2 or V3.1.
        # *   **false**: The bastion host runs V3.2.
        self.legacy = legacy
        # The license code of the bastion host.
        self.license_code = license_code
        # The edition of the bastion host. Valid values:
        # 
        # *   **cloudbastion**: Basic Edition.
        # *   **cloudbastion_ha**: Enterprise Edition.
        self.plan_code = plan_code
        # Indicates whether the bastion host can be accessed from the Internet. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.public_network_access = public_network_access
        # The region ID of the bastion host.
        self.region_id = region_id
        # The ID of the resource group to which the bastion host belongs.
        self.resource_group_id = resource_group_id
        self.slave_vswitch_id = slave_vswitch_id
        # The timestamp when the bastion host is purchased or renewed. Unit: milliseconds.
        self.start_time = start_time
        # The ID of the virtual private cloud (VPC) to which the bastion host belongs.
        self.vpc_id = vpc_id
        # The ID of the vSwitch to which the bastion host belongs.
        self.vswitch_id = vswitch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.band_width is not None:
            result['BandWidth'] = self.band_width

        if self.description is not None:
            result['Description'] = self.description

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.image_version is not None:
            result['ImageVersion'] = self.image_version

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status

        if self.internet_endpoint is not None:
            result['InternetEndpoint'] = self.internet_endpoint

        if self.intranet_endpoint is not None:
            result['IntranetEndpoint'] = self.intranet_endpoint

        if self.legacy is not None:
            result['Legacy'] = self.legacy

        if self.license_code is not None:
            result['LicenseCode'] = self.license_code

        if self.plan_code is not None:
            result['PlanCode'] = self.plan_code

        if self.public_network_access is not None:
            result['PublicNetworkAccess'] = self.public_network_access

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.slave_vswitch_id is not None:
            result['SlaveVswitchId'] = self.slave_vswitch_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandWidth') is not None:
            self.band_width = m.get('BandWidth')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('ImageVersion') is not None:
            self.image_version = m.get('ImageVersion')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')

        if m.get('InternetEndpoint') is not None:
            self.internet_endpoint = m.get('InternetEndpoint')

        if m.get('IntranetEndpoint') is not None:
            self.intranet_endpoint = m.get('IntranetEndpoint')

        if m.get('Legacy') is not None:
            self.legacy = m.get('Legacy')

        if m.get('LicenseCode') is not None:
            self.license_code = m.get('LicenseCode')

        if m.get('PlanCode') is not None:
            self.plan_code = m.get('PlanCode')

        if m.get('PublicNetworkAccess') is not None:
            self.public_network_access = m.get('PublicNetworkAccess')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SlaveVswitchId') is not None:
            self.slave_vswitch_id = m.get('SlaveVswitchId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')

        return self

