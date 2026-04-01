# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeRCNodePoolResponseBody(DaraModel):
    def __init__(
        self,
        node_pool_list: List[main_models.DescribeRCNodePoolResponseBodyNodePoolList] = None,
        request_id: str = None,
    ):
        # The node pool information.
        self.node_pool_list = node_pool_list
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.node_pool_list:
            for v1 in self.node_pool_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['NodePoolList'] = []
        if self.node_pool_list is not None:
            for k1 in self.node_pool_list:
                result['NodePoolList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.node_pool_list = []
        if m.get('NodePoolList') is not None:
            for k1 in m.get('NodePoolList'):
                temp_model = main_models.DescribeRCNodePoolResponseBodyNodePoolList()
                self.node_pool_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeRCNodePoolResponseBodyNodePoolList(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        auto_renew: bool = None,
        cluster_id: str = None,
        create_mode: str = None,
        data_disk: List[main_models.DescribeRCNodePoolResponseBodyNodePoolListDataDisk] = None,
        deployment_set_id: str = None,
        description: str = None,
        host_name: str = None,
        image_id: str = None,
        instance_charge_type: str = None,
        instance_name: str = None,
        instance_type: str = None,
        internet_charge_type: str = None,
        internet_max_bandwidth_out: int = None,
        io_optimized: str = None,
        key_pair_name: str = None,
        node_pool_id: str = None,
        node_pool_name: str = None,
        password: str = None,
        period: int = None,
        period_unit: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        security_enhancement_strategy: str = None,
        security_group_id: str = None,
        spot_strategy: str = None,
        system_disk: main_models.DescribeRCNodePoolResponseBodyNodePoolListSystemDisk = None,
        tag: List[main_models.DescribeRCNodePoolResponseBodyNodePoolListTag] = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        # Indicates whether to enable automatic payment. Valid values:
        # 
        # *   **true** (default): enables the feature. You must make sure that your account balance is sufficient.
        # *   **false**: disables the feature. An unpaid order is generated.
        self.auto_pay = auto_pay
        # Indicates whether to enable auto-renewal for the instance. Valid values:
        # 
        # *   **true** (default)
        # *   **false**
        self.auto_renew = auto_renew
        # The ID of the container cluster in which the RDS Custom instance resides.
        self.cluster_id = cluster_id
        # Indicates whether to add the instance to the ACK cluster.
        self.create_mode = create_mode
        # The data disks.
        self.data_disk = data_disk
        # The ID of the deployment set.
        self.deployment_set_id = deployment_set_id
        # The instance description.
        self.description = description
        # The instance hostname.
        self.host_name = host_name
        # The ID of the image used by the instance.
        self.image_id = image_id
        # The billing method. Valid value:
        # 
        # *   **Prepaid**: subscription
        # *   **Postpaid**: pay-as-you-go
        self.instance_charge_type = instance_charge_type
        # The instance name.
        self.instance_name = instance_name
        # The instance type.
        self.instance_type = instance_type
        # The reserved parameter. This parameter is not supported.
        self.internet_charge_type = internet_charge_type
        # The reserved parameter. This parameter is not supported.
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        # The reserved parameter. This parameter is not supported.
        self.io_optimized = io_optimized
        # The key pair name.
        self.key_pair_name = key_pair_name
        # The node pool ID.
        self.node_pool_id = node_pool_id
        # The name of the node pool.
        self.node_pool_name = node_pool_name
        # The password of the root user of the instance.
        self.password = password
        # The subscription duration.
        self.period = period
        # The unit of the subscription period. Valid values:
        # 
        # *   **Year**
        # *   **Month** (default)
        self.period_unit = period_unit
        # The region ID of the instance.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The reserved parameter. This parameter is not supported.
        self.security_enhancement_strategy = security_enhancement_strategy
        # The security group ID.
        self.security_group_id = security_group_id
        # The reserved parameter. This parameter is not supported.
        self.spot_strategy = spot_strategy
        # The specification of the system disk.
        self.system_disk = system_disk
        # The tags.
        self.tag = tag
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        if self.data_disk:
            for v1 in self.data_disk:
                 if v1:
                    v1.validate()
        if self.system_disk:
            self.system_disk.validate()
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.create_mode is not None:
            result['CreateMode'] = self.create_mode

        result['DataDisk'] = []
        if self.data_disk is not None:
            for k1 in self.data_disk:
                result['DataDisk'].append(k1.to_map() if k1 else None)

        if self.deployment_set_id is not None:
            result['DeploymentSetId'] = self.deployment_set_id

        if self.description is not None:
            result['Description'] = self.description

        if self.host_name is not None:
            result['HostName'] = self.host_name

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type

        if self.internet_max_bandwidth_out is not None:
            result['InternetMaxBandwidthOut'] = self.internet_max_bandwidth_out

        if self.io_optimized is not None:
            result['IoOptimized'] = self.io_optimized

        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name

        if self.node_pool_id is not None:
            result['NodePoolId'] = self.node_pool_id

        if self.node_pool_name is not None:
            result['NodePoolName'] = self.node_pool_name

        if self.password is not None:
            result['Password'] = self.password

        if self.period is not None:
            result['Period'] = self.period

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.security_enhancement_strategy is not None:
            result['SecurityEnhancementStrategy'] = self.security_enhancement_strategy

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy

        if self.system_disk is not None:
            result['SystemDisk'] = self.system_disk.to_map()

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('CreateMode') is not None:
            self.create_mode = m.get('CreateMode')

        self.data_disk = []
        if m.get('DataDisk') is not None:
            for k1 in m.get('DataDisk'):
                temp_model = main_models.DescribeRCNodePoolResponseBodyNodePoolListDataDisk()
                self.data_disk.append(temp_model.from_map(k1))

        if m.get('DeploymentSetId') is not None:
            self.deployment_set_id = m.get('DeploymentSetId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')

        if m.get('InternetMaxBandwidthOut') is not None:
            self.internet_max_bandwidth_out = m.get('InternetMaxBandwidthOut')

        if m.get('IoOptimized') is not None:
            self.io_optimized = m.get('IoOptimized')

        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')

        if m.get('NodePoolId') is not None:
            self.node_pool_id = m.get('NodePoolId')

        if m.get('NodePoolName') is not None:
            self.node_pool_name = m.get('NodePoolName')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SecurityEnhancementStrategy') is not None:
            self.security_enhancement_strategy = m.get('SecurityEnhancementStrategy')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')

        if m.get('SystemDisk') is not None:
            temp_model = main_models.DescribeRCNodePoolResponseBodyNodePoolListSystemDisk()
            self.system_disk = temp_model.from_map(m.get('SystemDisk'))

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeRCNodePoolResponseBodyNodePoolListTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeRCNodePoolResponseBodyNodePoolListTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag keys.
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

class DescribeRCNodePoolResponseBodyNodePoolListSystemDisk(DaraModel):
    def __init__(
        self,
        category: str = None,
        performance_level: str = None,
        size: int = None,
    ):
        # The type of the system disk. Set the value to **cloud_essd**, which indicates ESSDs.
        self.category = category
        # The performance level of the ESSD. Valid values:
        # 
        # *   **PL0**: A single ESSD delivers up to 10,000 random read/write IOPS.
        # *   **PL1**: A single ESSD delivers up to 50,000 random read/write IOPS.
        # *   **PL2**: A single ESSD delivers up to 100,000 random read/write IOPS.
        # *   **PL3**: A single ESSD delivers up to 1,000,000 random read/write IOPS.
        self.performance_level = performance_level
        # The size of the system disk. Unit: GiB.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level

        if self.size is not None:
            result['Size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        return self

class DescribeRCNodePoolResponseBodyNodePoolListDataDisk(DaraModel):
    def __init__(
        self,
        category: str = None,
        delete_with_instance: bool = None,
        encrypted: str = None,
        performance_level: str = None,
        size: int = None,
    ):
        # The type of the data disk. Set the value to **cloud_essd**, which indicates Enterprise SSDs (ESSDs).
        self.category = category
        # The reserved parameter. This parameter is not supported.
        self.delete_with_instance = delete_with_instance
        # Indicates whether to encrypt the cloud disk. Valid values:
        # 
        # *   **true**
        # *   **false** (default)
        self.encrypted = encrypted
        # The performance level of the ESSD. Valid values:
        # 
        # *   **PL0**: A single ESSD delivers up to 10,000 random read/write IOPS.
        # *   **PL1**: A single ESSD delivers up to 50,000 random read/write IOPS.
        # *   **PL2**: A single ESSD delivers up to 100,000 random read/write IOPS.
        # *   **PL3**: A single ESSD delivers up to 1,000,000 random read/write IOPS.
        self.performance_level = performance_level
        # The data disk size. Unit: GiB.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.delete_with_instance is not None:
            result['DeleteWithInstance'] = self.delete_with_instance

        if self.encrypted is not None:
            result['Encrypted'] = self.encrypted

        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level

        if self.size is not None:
            result['Size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('DeleteWithInstance') is not None:
            self.delete_with_instance = m.get('DeleteWithInstance')

        if m.get('Encrypted') is not None:
            self.encrypted = m.get('Encrypted')

        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        return self

