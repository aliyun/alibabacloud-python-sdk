# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class CreateRCNodePoolRequest(DaraModel):
    def __init__(
        self,
        amount: int = None,
        auto_pay: bool = None,
        auto_renew: bool = None,
        client_token: str = None,
        cluster_id: str = None,
        create_mode: str = None,
        data_disk: List[main_models.CreateRCNodePoolRequestDataDisk] = None,
        deployment_set_id: str = None,
        description: str = None,
        dry_run: bool = None,
        host_name: str = None,
        image_id: str = None,
        instance_charge_type: str = None,
        instance_name: str = None,
        instance_type: str = None,
        internet_charge_type: str = None,
        internet_max_bandwidth_out: int = None,
        io_optimized: str = None,
        key_pair_name: str = None,
        node_pool_name: str = None,
        password: str = None,
        period: int = None,
        period_unit: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        security_enhancement_strategy: str = None,
        security_group_id: str = None,
        spot_strategy: str = None,
        support_case: str = None,
        system_disk: main_models.CreateRCNodePoolRequestSystemDisk = None,
        tag: List[main_models.CreateRCNodePoolRequestTag] = None,
        user_data: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        # The number of RDS Custom instances to create. This parameter is applicable only to batch creation of RDS Custom instances.
        # 
        # Valid values: **1** to **5**. Default value: **1**.
        self.amount = amount
        # Specifies whether to enable automatic payment.
        # Valid values:
        # 
        # - **true**: Automatic payment is enabled. Make sure that your account balance is sufficient.
        # - **false**: Only an order is generated. No payment is made.
        # 
        # 
        # > The default value is true. If your payment method has an insufficient balance, set AutoPay to false. In this case, an unpaid order is generated. You can log on to the ApsaraDB RDS console to complete the payment.
        # >
        self.auto_pay = auto_pay
        # Specifies whether to enable auto-renewal. This parameter is valid only when you create subscription instances. Valid values:
        # * **true**
        # * **false**
        # 
        # > * If you purchase on a monthly basis, the auto-renewal epoch is 1 month.
        # > * If you purchase on a yearly basis, the auto-renewal epoch is 1 year.
        self.auto_renew = auto_renew
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The ID of the RDS Custom container cluster.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # Specifies whether to allow the instance to join an ACK cluster. If this parameter settings is set to **1**, the created instance can be added to an ACK cluster for efficient container application management.
        # 
        # - **1**: Yes.
        # - **0** (default): No.
        self.create_mode = create_mode
        # The list of data cloud disks.
        self.data_disk = data_disk
        # The deployment set ID.
        self.deployment_set_id = deployment_set_id
        # The instance description. The description must be 2 to 256 characters in length and can contain letters and Chinese characters. The description cannot start with http:// or https://.
        self.description = description
        # Specifies whether to perform a dry run for this request. Valid values:
        # * **true**: performs a dry run without creating the instance. The system checks the request parameters, request format, service limits, and available stock.
        # * **false** (default): sends the request. If the request passes the check, the instance is created.
        self.dry_run = dry_run
        # The hostname of the instance.
        self.host_name = host_name
        # The image ID used by the instance.
        self.image_id = image_id
        # The billing method. Valid values:
        # * **Prepaid**: subscription.
        # * **Postpaid**: pay-as-you-go.
        self.instance_charge_type = instance_charge_type
        # The instance name.
        self.instance_name = instance_name
        # The instance type. For the instance types supported by RDS Custom instances, see [RDS Custom instance types](https://help.aliyun.com/document_detail/2844823.html).
        # 
        # This parameter is required.
        self.instance_type = instance_type
        # A reserved parameter. This parameter is not supported.
        self.internet_charge_type = internet_charge_type
        # A reserved parameter. This parameter is not supported.
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        # A reserved parameter. This parameter is not supported.
        self.io_optimized = io_optimized
        # The name of the key pair. Only a single name is supported.
        self.key_pair_name = key_pair_name
        # The name of the node pool.
        self.node_pool_name = node_pool_name
        # The password of the root account of the instance.
        self.password = password
        # The subscription duration of the resource. Default value: **1**.
        self.period = period
        # The unit of the subscription duration for the subscription billable methods. Valid values:
        # - **Year**
        # - **Month** (default)
        self.period_unit = period_unit
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # A reserved parameter. This parameter is not supported.
        self.security_enhancement_strategy = security_enhancement_strategy
        # The security group ID. You can specify an existing security group ID. If the security group does not exist, automatic creation of a security group is performed.
        self.security_group_id = security_group_id
        # A reserved parameter. This parameter is not supported.
        self.spot_strategy = spot_strategy
        # The supported scenario. This parameter is required when **createMode** is set to **1**. Currently, only **edge** is supported.
        self.support_case = support_case
        # The system cloud disk specifications.
        self.system_disk = system_disk
        # The list of tags.
        self.tag = tag
        # A reserved parameter. This parameter is not supported.
        self.user_data = user_data
        # The vSwitch ID.
        # 
        # > The vSwitch must be in the same zone as the ApsaraDB RDS instance.
        # 
        # This parameter is required.
        self.v_switch_id = v_switch_id
        # The zone ID of the instance.
        # > If you specify the VSwitchId parameter, the ZoneId parameter must match the zone of the specified vSwitch. You can also leave this parameter empty, and the system automatically selects the zone of the specified vSwitch.
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
        if self.amount is not None:
            result['Amount'] = self.amount

        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

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

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

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

        if self.support_case is not None:
            result['SupportCase'] = self.support_case

        if self.system_disk is not None:
            result['SystemDisk'] = self.system_disk.to_map()

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.user_data is not None:
            result['UserData'] = self.user_data

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('CreateMode') is not None:
            self.create_mode = m.get('CreateMode')

        self.data_disk = []
        if m.get('DataDisk') is not None:
            for k1 in m.get('DataDisk'):
                temp_model = main_models.CreateRCNodePoolRequestDataDisk()
                self.data_disk.append(temp_model.from_map(k1))

        if m.get('DeploymentSetId') is not None:
            self.deployment_set_id = m.get('DeploymentSetId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

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

        if m.get('SupportCase') is not None:
            self.support_case = m.get('SupportCase')

        if m.get('SystemDisk') is not None:
            temp_model = main_models.CreateRCNodePoolRequestSystemDisk()
            self.system_disk = temp_model.from_map(m.get('SystemDisk'))

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateRCNodePoolRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class CreateRCNodePoolRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. You can create up to N tag keys at a time. Valid values of N: **1 to 20**. The tag key cannot be an empty string.
        self.key = key
        # The tag value that corresponds to the tag key. You can create up to N tag values at a time. Valid values of N: **1** to **20**. The tag value can be an empty string.
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

class CreateRCNodePoolRequestSystemDisk(DaraModel):
    def __init__(
        self,
        category: str = None,
        performance_level: str = None,
        size: int = None,
    ):
        # The category of the system cloud disk. Only **cloud_essd** (Enterprise SSD) is supported.
        self.category = category
        # The performance level (PL) of the ESSD cloud disk. For standard SSDs and other cloud disk types, this parameter is not applicable. Valid values:
        # 
        # - **PL0**: A single cloud disk can deliver up to 10,000 random read/write IOPS.
        # - **PL1**: A single cloud disk can deliver up to 50,000 random read/write IOPS.
        # - **PL2**: A single cloud disk can deliver up to 100,000 random read/write IOPS.
        # - **PL3**: A single cloud disk can deliver up to 1,000,000 random read/write IOPS.
        self.performance_level = performance_level
        # The size of the system cloud disk. Unit: GiB. Valid values: 20 to 2048.
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

class CreateRCNodePoolRequestDataDisk(DaraModel):
    def __init__(
        self,
        category: str = None,
        delete_with_instance: bool = None,
        encrypted: str = None,
        performance_level: str = None,
        size: int = None,
    ):
        # The type of the data cloud disk. Only **cloud_essd** (ESSD cloud disk) is supported. For more information about standard SSDs and other cloud disk types, see the related documentation.
        self.category = category
        # A reserved parameter. This parameter is not supported.
        self.delete_with_instance = delete_with_instance
        # Specifies whether to encrypt the data cloud disk. Valid values:
        # 
        # - **true**
        # - **false** (default)
        self.encrypted = encrypted
        # The performance level (PL) of the ESSD cloud disk. For standard SSDs and other cloud disk types, this parameter is not applicable. Valid values:
        # 
        # - **PL0**: A single cloud disk can deliver up to 10,000 random read/write IOPS.
        # - **PL1**: A single cloud disk can deliver up to 50,000 random read/write IOPS.
        # - **PL2**: A single cloud disk can deliver up to 100,000 random read/write IOPS.
        # - **PL3**: A single cloud disk can deliver up to 1,000,000 random read/write IOPS.
        self.performance_level = performance_level
        # The size of the data cloud disk. Unit: GiB. Valid values: 20 to 65536.
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

