# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class RunRCInstancesRequest(DaraModel):
    def __init__(
        self,
        acu_type: str = None,
        amount: int = None,
        auto_pay: bool = None,
        auto_renew: bool = None,
        auto_use_coupon: bool = None,
        client_token: str = None,
        create_ack_edge_param: main_models.RunRCInstancesRequestCreateAckEdgeParam = None,
        create_extra_param: str = None,
        create_mode: str = None,
        data_disk: List[main_models.RunRCInstancesRequestDataDisk] = None,
        deletion_protection: bool = None,
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
        password: str = None,
        password_inherit: bool = None,
        period: int = None,
        period_unit: str = None,
        promotion_code: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        scheduled_rule: str = None,
        security_enhancement_strategy: str = None,
        security_group_id: str = None,
        spot_strategy: str = None,
        support_case: str = None,
        system_disk: main_models.RunRCInstancesRequestSystemDisk = None,
        tag: List[main_models.RunRCInstancesRequestTag] = None,
        user_data: str = None,
        user_data_in_base_64: bool = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        self.acu_type = acu_type
        # The number of RDS Custom instances that you want to create. The parameter is available if you want to create multiple RDS Custom instances at a time.
        # 
        # Valid values: **1** to **10**. Default value: **1**.
        self.amount = amount
        # Specifies whether to enable the automatic payment feature. Valid values:
        # 
        # *   **true** (default): enables the feature. Make sure that your account balance is sufficient.
        # *   **false**: disables the feature. An unpaid order is generated.
        # 
        # >  If your account balance is insufficient, you can set the AutoPay parameter to false. In this case, an unpaid order is generated. You can complete the payment in the Expenses and Costs console.
        self.auto_pay = auto_pay
        # Specifies whether to enable auto-renewal for the instance. Valid values:
        # 
        # *   **true** (default)
        # *   **false**
        self.auto_renew = auto_renew
        self.auto_use_coupon = auto_use_coupon
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        self.create_ack_edge_param = create_ack_edge_param
        self.create_extra_param = create_extra_param
        self.create_mode = create_mode
        # The information about the data disks.
        self.data_disk = data_disk
        self.deletion_protection = deletion_protection
        # The deployment set ID.
        self.deployment_set_id = deployment_set_id
        # The instance description. The description must be 2 to 256 characters in length and cannot start with http:// or https://.
        self.description = description
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, service limits, and insufficient inventory errors.
        # *   **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, the instance is directly created.
        self.dry_run = dry_run
        self.host_name = host_name
        # The ID of the image used by the instance.
        self.image_id = image_id
        # The billing method of the instance. Set the value to **Prepaid**, which indicates the subscription billing method.
        self.instance_charge_type = instance_charge_type
        # The instance name.
        self.instance_name = instance_name
        # The instance type. For more information about the instance types that are supported by RDS Custom instances, see [Instance types for RDS Custom instances](https://help.aliyun.com/document_detail/2844823.html).
        # 
        # This parameter is required.
        self.instance_type = instance_type
        # The reserved parameter. This parameter is not supported.
        self.internet_charge_type = internet_charge_type
        # The reserved parameter. This parameter is not supported.
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        # The reserved parameter. This parameter is not supported.
        self.io_optimized = io_optimized
        # The name of the AccessKey pair. You can specify only one name.
        self.key_pair_name = key_pair_name
        # The password of the account that is used to log on to the instance.
        self.password = password
        self.password_inherit = password_inherit
        # The subscription duration of the instance. Default value: **1**.
        self.period = period
        # The unit of the subscription duration. Valid values:
        # 
        # *   **Year**
        # *   **Month** (default)
        self.period_unit = period_unit
        self.promotion_code = promotion_code
        # The region ID. You can call the DescribeRegions operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.scheduled_rule = scheduled_rule
        # The reserved parameter. This parameter is not supported.
        self.security_enhancement_strategy = security_enhancement_strategy
        # The ID of the security group to which you want to add the new instance. Instances in the same security group can communicate with each other. The maximum number of instances allowed in a security group varies based on the type of the security group. For more information, see the "Security group limits" section in [Limits](https://help.aliyun.com/document_detail/25412.html).
        # 
        # >  The network type of the instance is determined by the security group specified by the SecurityGroupId parameter. For example, if the network type of the specified security group is VPC, the instance is a VPC-type instance. In this case, you must specify the VSwitchId parameter.
        self.security_group_id = security_group_id
        self.spot_strategy = spot_strategy
        self.support_case = support_case
        # The specification of the system disk.
        self.system_disk = system_disk
        self.tag = tag
        self.user_data = user_data
        self.user_data_in_base_64 = user_data_in_base_64
        # The vSwitch ID of the instance. You must specify this parameter when you create an instance of the virtual private cloud (VPC) type. The specified vSwitch and security group must belong to the same VPC.
        # 
        # >  If you specify the VSwitchId parameter, the zone specified by the ZoneId parameter must be the same as the zone in which the specified vSwitch resides. You can leave the ZoneId parameter empty. In this case, the system uses the zone in which the specified vSwitch resides.
        # 
        # This parameter is required.
        self.v_switch_id = v_switch_id
        # The zone ID of the instance. You can call the DescribeZones operation to query the zone IDs.
        # 
        # >  If you specify the VSwitchId parameter, the zone specified by the ZoneId parameter must be the same as the zone in which the specified vSwitch resides. You can leave the ZoneId parameter empty. In this case, the system uses the zone in which the specified vSwitch resides.
        self.zone_id = zone_id

    def validate(self):
        if self.create_ack_edge_param:
            self.create_ack_edge_param.validate()
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
        if self.acu_type is not None:
            result['AcuType'] = self.acu_type

        if self.amount is not None:
            result['Amount'] = self.amount

        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.auto_use_coupon is not None:
            result['AutoUseCoupon'] = self.auto_use_coupon

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.create_ack_edge_param is not None:
            result['CreateAckEdgeParam'] = self.create_ack_edge_param.to_map()

        if self.create_extra_param is not None:
            result['CreateExtraParam'] = self.create_extra_param

        if self.create_mode is not None:
            result['CreateMode'] = self.create_mode

        result['DataDisk'] = []
        if self.data_disk is not None:
            for k1 in self.data_disk:
                result['DataDisk'].append(k1.to_map() if k1 else None)

        if self.deletion_protection is not None:
            result['DeletionProtection'] = self.deletion_protection

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

        if self.password is not None:
            result['Password'] = self.password

        if self.password_inherit is not None:
            result['PasswordInherit'] = self.password_inherit

        if self.period is not None:
            result['Period'] = self.period

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.promotion_code is not None:
            result['PromotionCode'] = self.promotion_code

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.scheduled_rule is not None:
            result['ScheduledRule'] = self.scheduled_rule

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

        if self.user_data_in_base_64 is not None:
            result['UserDataInBase64'] = self.user_data_in_base_64

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcuType') is not None:
            self.acu_type = m.get('AcuType')

        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('AutoUseCoupon') is not None:
            self.auto_use_coupon = m.get('AutoUseCoupon')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('CreateAckEdgeParam') is not None:
            temp_model = main_models.RunRCInstancesRequestCreateAckEdgeParam()
            self.create_ack_edge_param = temp_model.from_map(m.get('CreateAckEdgeParam'))

        if m.get('CreateExtraParam') is not None:
            self.create_extra_param = m.get('CreateExtraParam')

        if m.get('CreateMode') is not None:
            self.create_mode = m.get('CreateMode')

        self.data_disk = []
        if m.get('DataDisk') is not None:
            for k1 in m.get('DataDisk'):
                temp_model = main_models.RunRCInstancesRequestDataDisk()
                self.data_disk.append(temp_model.from_map(k1))

        if m.get('DeletionProtection') is not None:
            self.deletion_protection = m.get('DeletionProtection')

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

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('PasswordInherit') is not None:
            self.password_inherit = m.get('PasswordInherit')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('PromotionCode') is not None:
            self.promotion_code = m.get('PromotionCode')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ScheduledRule') is not None:
            self.scheduled_rule = m.get('ScheduledRule')

        if m.get('SecurityEnhancementStrategy') is not None:
            self.security_enhancement_strategy = m.get('SecurityEnhancementStrategy')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')

        if m.get('SupportCase') is not None:
            self.support_case = m.get('SupportCase')

        if m.get('SystemDisk') is not None:
            temp_model = main_models.RunRCInstancesRequestSystemDisk()
            self.system_disk = temp_model.from_map(m.get('SystemDisk'))

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.RunRCInstancesRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        if m.get('UserDataInBase64') is not None:
            self.user_data_in_base_64 = m.get('UserDataInBase64')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class RunRCInstancesRequestTag(DaraModel):
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

class RunRCInstancesRequestSystemDisk(DaraModel):
    def __init__(
        self,
        category: str = None,
        performance_level: str = None,
        size: int = None,
    ):
        # The type of the system disk. Set the value to **cloud_essd**, which indicates ESSDs.
        self.category = category
        self.performance_level = performance_level
        # The size of the system disk. Unit: GiB. Only performance level 1 (PL1) ESSDs are supported. Valid values: 20 to 2048.
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

class RunRCInstancesRequestDataDisk(DaraModel):
    def __init__(
        self,
        category: str = None,
        delete_with_instance: bool = None,
        device: str = None,
        encrypted: str = None,
        performance_level: str = None,
        size: int = None,
        snapshot_id: str = None,
    ):
        # The type of the data disk. Set the value to **cloud_essd**, which indicates Enterprise SSDs (ESSDs).
        self.category = category
        # The reserved parameter. This parameter is not supported.
        self.delete_with_instance = delete_with_instance
        self.device = device
        # Specifies whether to encrypt the cloud disk. Valid values:
        # 
        # *   **true**
        # *   **false** (default)
        self.encrypted = encrypted
        # The reserved parameter. This parameter is not supported.
        self.performance_level = performance_level
        # The size of the data disk. Unit: GiB.
        self.size = size
        self.snapshot_id = snapshot_id

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

        if self.device is not None:
            result['Device'] = self.device

        if self.encrypted is not None:
            result['Encrypted'] = self.encrypted

        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level

        if self.size is not None:
            result['Size'] = self.size

        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('DeleteWithInstance') is not None:
            self.delete_with_instance = m.get('DeleteWithInstance')

        if m.get('Device') is not None:
            self.device = m.get('Device')

        if m.get('Encrypted') is not None:
            self.encrypted = m.get('Encrypted')

        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')

        return self

class RunRCInstancesRequestCreateAckEdgeParam(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        node_pool_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.node_pool_id = node_pool_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.node_pool_id is not None:
            result['NodePoolId'] = self.node_pool_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('NodePoolId') is not None:
            self.node_pool_id = m.get('NodePoolId')

        return self

