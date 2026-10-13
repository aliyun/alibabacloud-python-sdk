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
        # Specifies the number of RDS Custom instances to create. This parameter is applicable only when you create multiple RDS Custom instances at a time.
        # 
        # Valid values: **1** to **5**. Default value: **1**.
        self.amount = amount
        # Specifies whether to enable automatic payment. Valid values:
        # 
        # - **true**: Automatic payment is enabled. Make sure that your account balance is sufficient.
        # - **false**: Only an order is generated and no payment is made.
        # 
        # 
        # > Default value: **true**. If the balance of your payment method is insufficient, you can set the AutoPay parameter to false. In this case, an unpaid order is generated, and you can log on to the ApsaraDB RDS console to complete the payment.
        # >
        self.auto_pay = auto_pay
        # Specifies whether to enable auto-renewal for the instance. This parameter is valid only when you create a subscription instance. Valid values:
        # * **true**: yes.
        # * **false**: no.
        # 
        # > * If the subscription duration is one month, the auto-renewal cycle is 1 month.
        # > * If the subscription duration is one year, the auto-renewal cycle is 1 year.
        self.auto_renew = auto_renew
        # The client token that is used to ensure the idempotence of the request and prevent duplicate submissions. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The RDS Custom container cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # Specifies whether the instance is allowed to join an ACK cluster. When this parameter is set to **1**, the created instance can be added to an ACK cluster for efficient management of containerized applications.
        # 
        # - **1**: yes.
        # - **0** (default): no.
        self.create_mode = create_mode
        # The data cloud disks.
        self.data_disk = data_disk
        # The deployment set ID.
        self.deployment_set_id = deployment_set_id
        # The instance description. The description must be 2 to 256 characters in length and cannot start with http:// or https://.
        self.description = description
        # Specifies whether to perform a dry run before creating the instance. Valid values:
        # * **true**: A dry run is performed and no instance is created. The system checks the request parameters, request format, service limits, and available resources.
        # * **false** (default): A normal request is sent and the instance is created if the request passes the dry run.
        self.dry_run = dry_run
        # The hostname of the instance.
        self.host_name = host_name
        # The image ID of the instance.
        self.image_id = image_id
        # The billing method. Valid values:
        # * **Prepaid**: subscription.
        # * **Postpaid**: pay-as-you-go.
        self.instance_charge_type = instance_charge_type
        # The instance name.
        self.instance_name = instance_name
        # The instance type. For the instance types supported by RDS Custom, see [RDS Custom instance types](https://help.aliyun.com/document_detail/2844823.html).
        # 
        # This parameter is required.
        self.instance_type = instance_type
        # Reserved parameter. Not supported.
        self.internet_charge_type = internet_charge_type
        # Reserved parameter. Not supported.
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        # Reserved parameter. Not supported.
        self.io_optimized = io_optimized
        # The key pair name. Only one key pair name is supported.
        self.key_pair_name = key_pair_name
        # The node pool name.
        self.node_pool_name = node_pool_name
        # The password of the root account for the instance.
        self.password = password
        # The subscription duration of the resource. Default value: **1**.
        self.period = period
        # The time unit of the subscription billing method. Valid values:
        # - **Year**: year.
        # - **Month** (default): month.
        self.period_unit = period_unit
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # Reserved parameter. Not supported.
        self.security_enhancement_strategy = security_enhancement_strategy
        # The security group ID. You can specify an existing security group ID. If the specified security group does not exist, a security group is automatically created.
        self.security_group_id = security_group_id
        # Reserved parameter. Not supported.
        self.spot_strategy = spot_strategy
        # The supported scenario. This parameter is required when the **createMode** parameter is set to **1**. Only **edge** is supported.
        self.support_case = support_case
        # The system cloud disk.
        self.system_disk = system_disk
        # The tags.
        self.tag = tag
        # Reserved parameter. Not supported.
        self.user_data = user_data
        # The vSwitch ID.
        # 
        # > The vSwitch must be in the same zone as the RDS instance.
        # 
        # This parameter is required.
        self.v_switch_id = v_switch_id
        # The zone ID of the instance.
        # > If you specify the VSwitchId parameter, the ZoneId parameter must be set to the zone where the vSwitch resides. You can also leave the ZoneId parameter empty, and the system automatically selects the zone where the specified vSwitch resides.
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
        # The tag key. You can create up to N tag keys at a time. Valid values of N: **1** to **20**. The tag key cannot be an empty string.
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
        # The category of the system cloud disk. Only **cloud_essd** (ESSD) is supported.
        self.category = category
        # The performance level of the ESSD cloud disk. Valid values:
        # 
        # - **PL0**: An ESSD can deliver up to 10,000 random read/write IOPS.
        # - **PL1**: An ESSD can deliver up to 50,000 random read/write IOPS.
        # - **PL2**: An ESSD can deliver up to 100,000 random read/write IOPS.
        # - **PL3**: An ESSD can deliver up to 1,000,000 random read/write IOPS.
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
        # The data cloud disk type. Currently, only **cloud_essd** (ESSD cloud disk) is supported.
        self.category = category
        # Reserved parameter. Not supported.
        self.delete_with_instance = delete_with_instance
        # Specifies whether to encrypt the data cloud disk. Valid values:
        # 
        # - **true**: yes.
        # - **false**: no.
        # Default value: **false**.
        self.encrypted = encrypted
        # The performance level of the ESSD cloud disk. Valid values:
        # 
        # - **PL0**: An ESSD can deliver up to 10,000 random read/write IOPS.
        # - **PL1**: An ESSD can deliver up to 50,000 random read/write IOPS.
        # - **PL2**: An ESSD can deliver up to 100,000 random read/write IOPS.
        # - **PL3**: An ESSD can deliver up to 1,000,000 random read/write IOPS.
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

