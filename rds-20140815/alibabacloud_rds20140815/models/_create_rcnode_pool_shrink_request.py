# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class CreateRCNodePoolShrinkRequest(DaraModel):
    def __init__(
        self,
        amount: int = None,
        auto_pay: bool = None,
        auto_renew: bool = None,
        client_token: str = None,
        cluster_id: str = None,
        create_mode: str = None,
        data_disk_shrink: str = None,
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
        system_disk_shrink: str = None,
        tag: List[main_models.CreateRCNodePoolShrinkRequestTag] = None,
        user_data: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        # The number of RDS Custom instances that you want to create. The parameter is available if you want to create multiple RDS Custom instances at a time.
        # 
        # Valid values: **1** to **5**. Default value: **1**.
        self.amount = amount
        # Specifies whether to enable automatic payment. Valid values:
        # 
        # *   **true**: enables the feature. Make sure that your account balance is sufficient when you enable automatic payment.
        # *   **false**: does not automatically complete the payment. An unpaid order is generated.
        # 
        # >  Default value: true. If your account balance is insufficient, you can set AutoPay to false to generate an unpaid order. Then, you can log on to the ApsaraDB RDS console to complete the payment.
        self.auto_pay = auto_pay
        # Specifies whether to enable auto-renewal for the instance. If you specify the subscription billing method for the instance, you must specify this parameter. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # > 
        # 
        # *   Monthly subscription: The auto-renewal period is one month.
        # 
        # *   Annually: The auto-renewal period is one year.
        self.auto_renew = auto_renew
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The ID of the ACK cluster to which the RDS Custom instance belongs.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # Specifies whether to add the instance to the ACK cluster. If this parameter is set to **1**, the created instances can be added to the ACK cluster. This allows you to efficiently manage container applications. Valid values:
        # 
        # *   **1**: adds the instance to the ACK cluster.
        # *   **0** (default): does not add the instance to the ACK cluster.
        self.create_mode = create_mode
        # The data disks.
        self.data_disk_shrink = data_disk_shrink
        # The ID of the deployment set.
        self.deployment_set_id = deployment_set_id
        # The instance description. The description must be 2 to 256 characters in length and cannot start with http:// or https://.
        self.description = description
        # Specifies whether to perform a dry run. Default value: false. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, service limits, and insufficient inventory errors.
        # *   **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, the instance is directly created.
        self.dry_run = dry_run
        # The instance hostname.
        self.host_name = host_name
        # The ID of the image used by the instance.
        self.image_id = image_id
        # The billing method of the instance. Valid values:
        # 
        # *   **Prepaid**: subscription.
        # *   **Postpaid**: pay-as-you-go.
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
        # The name of the node pool.
        self.node_pool_name = node_pool_name
        # The password for the root account of the instance.
        self.password = password
        # The subscription duration of the instance. Default value: **1**.
        self.period = period
        # The unit of the subscription duration. Valid values:
        # 
        # *   **Year**
        # *   **Month** (default)
        self.period_unit = period_unit
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The reserved parameter. This parameter is not supported.
        self.security_enhancement_strategy = security_enhancement_strategy
        # The ID of the security group. You can enter an existing security group ID. If no security groups exist, a security group is automatically created.
        self.security_group_id = security_group_id
        # The reserved parameter. This parameter is not supported.
        self.spot_strategy = spot_strategy
        # The supported scenario. If you set the **createMode** parameter to **1**, you must also specify the SupportCase parameter. Valid value: **edge**.
        self.support_case = support_case
        # The specification of the system disk.
        self.system_disk_shrink = system_disk_shrink
        # The tags.
        self.tag = tag
        # The reserved parameter. This parameter is not supported.
        self.user_data = user_data
        # The vSwitch ID.
        # 
        # >  The vSwitch must belong to the same zone as the instance.
        # 
        # This parameter is required.
        self.v_switch_id = v_switch_id
        # The zone ID of the instance.
        # 
        # >  If you specify the VSwitchId parameter, the zone specified by the ZoneId parameter must be the same as the zone in which the specified vSwitch resides. You can leave the ZoneId parameter empty. In this case, the system uses the zone in which the specified vSwitch resides.
        self.zone_id = zone_id

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

        if self.data_disk_shrink is not None:
            result['DataDisk'] = self.data_disk_shrink

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

        if self.system_disk_shrink is not None:
            result['SystemDisk'] = self.system_disk_shrink

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

        if m.get('DataDisk') is not None:
            self.data_disk_shrink = m.get('DataDisk')

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
            self.system_disk_shrink = m.get('SystemDisk')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateRCNodePoolShrinkRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class CreateRCNodePoolShrinkRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag. You can create N tag keys at a time. Valid values of N: **1 to 20**. This parameter cannot be an empty string.
        self.key = key
        # The tag value. You can create N tag values at a time. Valid values of N: **1** to **20**. This parameter can be an empty string.
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

