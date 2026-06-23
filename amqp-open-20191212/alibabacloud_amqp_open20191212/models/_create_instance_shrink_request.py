# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateInstanceShrinkRequest(DaraModel):
    def __init__(
        self,
        auth_model: str = None,
        auto_renew: bool = None,
        auto_renew_period: int = None,
        client_token: str = None,
        edition: str = None,
        encrypted_instance: bool = None,
        instance_name: str = None,
        instance_type: str = None,
        kms_key_id: str = None,
        listener_mode: str = None,
        max_connections: int = None,
        max_eip_tps: int = None,
        max_private_tps: int = None,
        payment_type: str = None,
        period: int = None,
        period_cycle: str = None,
        provisioned_capacity: int = None,
        queue_capacity: int = None,
        renew_status: str = None,
        renewal_duration_unit: str = None,
        resource_group_id: str = None,
        security_group_id: str = None,
        serverless_charge_type: str = None,
        serverless_switch: bool = None,
        storage_size: int = None,
        support_eip: bool = None,
        support_tracing: bool = None,
        tags_shrink: str = None,
        tracing_storage_time: int = None,
        vpc_id: str = None,
        vswitch_ids_shrink: str = None,
    ):
        self.auth_model = auth_model
        # The renewal method. Valid values:
        # 
        # - `true`: Enables auto-renewal.
        # 
        # - `false`: Disables auto-renewal.
        self.auto_renew = auto_renew
        # The auto-renewal duration. The `RenewalDurationUnit` parameter specifies the unit, which defaults to month.
        # 
        # > This parameter is required if you set `AutoRenew` to `true`. The default value is 1.
        self.auto_renew_period = auto_renew_period
        # The client token used to ensure request idempotence.
        self.client_token = client_token
        # The deployment architecture for the serverless instance. Valid values:
        # 
        # - `shared`: The shared architecture, which is applicable to reserved and elastic (shared) instances and pay-as-you-go instances.
        # 
        # - `dedicated`: The dedicated architecture, which is applicable to reserved and elastic (dedicated) instances.
        self.edition = edition
        # This parameter is applicable only to dedicated instances. Specifies whether to enable data-at-rest encryption for the instance.
        self.encrypted_instance = encrypted_instance
        # The name of the instance. The name can be up to 64 characters long.
        self.instance_name = instance_name
        # The instance type.
        # This parameter is required for subscription instances. Valid values:
        # 
        # - `professional`: Professional Edition
        # 
        # - `enterprise`: Enterprise Edition
        # 
        # - `vip`: Platinum Edition
        # 
        # You do not need to specify this parameter for serverless instances.
        self.instance_type = instance_type
        # This parameter applies only to dedicated instances and is required if `EncryptedInstance` is set to `true`. It specifies the ID of the KMS key used for data-at-rest encryption. The key must meet the following requirements:
        # 
        # - The key cannot be a service key.
        # 
        # - The key must be in the Enabled state.
        # 
        # - The key must be a symmetric key, not an asymmetric key.
        # 
        # - The key usage must be for encryption and decryption.
        # 
        # - If the KMS key expires or is deleted, data reads and writes will become unavailable, and the ApsaraMQ for RabbitMQ instance may become inoperable.
        self.kms_key_id = kms_key_id
        # Specifies whether to enable only the TLS-encrypted port. This parameter applies only to reserved and elastic (dedicated) instances, and Platinum Edition instances.
        self.listener_mode = listener_mode
        # The maximum number of connections.
        # 
        # For information about the valid values, see the instance specifications on the [ApsaraMQ for RabbitMQ](https://common-buy.aliyun.com/?commodityCode=ons_onsproxy_pre) product page.
        self.max_connections = max_connections
        # The peak transactions per second (TPS) of the instance over the public network.
        # 
        # For information about the valid values, see the instance specifications on the [ApsaraMQ for RabbitMQ](https://common-buy.aliyun.com/?commodityCode=ons_onsproxy_pre) product page.
        self.max_eip_tps = max_eip_tps
        # The peak transactions per second (TPS) of the instance over a private network.
        # 
        # For information about the valid values, see the instance specifications on the [ApsaraMQ for RabbitMQ](https://common-buy.aliyun.com/?commodityCode=ons_onsproxy_pre) product page.
        self.max_private_tps = max_private_tps
        # The billing method of the instance. Valid values:
        # 
        # - `Subscription`: The subscription-based billing method.
        # 
        # - `PayAsYouGo`: The pay-as-you-go method for serverless instances.
        # 
        # This parameter is required.
        self.payment_type = payment_type
        # The subscription duration. The `PeriodCycle` parameter specifies the unit.
        # 
        # > This parameter is required if you set `PaymentType` to `Subscription`. The default value is 1.
        self.period = period
        # The unit of the subscription duration. Valid values:
        # 
        # - `Month`: month
        # 
        # - `Year`: year
        # 
        # This parameter is required if you set `PaymentType` to `Subscription`. The default value is `Month`.
        self.period_cycle = period_cycle
        # The provisioned TPS capacity for a reserved and elastic instance.
        self.provisioned_capacity = provisioned_capacity
        # The queue capacity of the instance.
        # 
        # For information about the valid values, see the instance specifications on the [ApsaraMQ for RabbitMQ](https://common-buy.aliyun.com/?commodityCode=ons_onsproxy_pre) product page.
        self.queue_capacity = queue_capacity
        # The renewal status. This parameter is equivalent to `AutoRenew`. Valid value:
        # 
        # - `AutoRenewal`: Enables auto-renewal.
        # 
        # > Both `AutoRenew` and `RenewStatus` specify the renewal method. If you specify both parameters, the value of `RenewStatus` takes precedence.
        self.renew_status = renew_status
        # The unit of the auto-renewal duration. Valid values:
        # 
        # - `Month`: month
        # 
        # - `Year`: year
        self.renewal_duration_unit = renewal_duration_unit
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id
        # The ID of the security group. This security group is used for the PrivateLink-based endpoint. The security group must meet the following requirements:
        # 
        # 1. Add an inbound rule to allow traffic on TCP ports 5672 and 5671.
        # 
        # 2. Managed security groups are not supported.
        # 
        # 3. The security group must belong to the specified VPC.
        # 
        # This parameter is required.
        self.security_group_id = security_group_id
        # The billing type of the serverless instance. Valid value:
        # 
        # - `onDemand`: pay-as-you-go
        self.serverless_charge_type = serverless_charge_type
        self.serverless_switch = serverless_switch
        # The message storage space. Unit: GB. Valid values:
        # 
        # - Professional Edition and Enterprise Edition instances: The value is fixed at 0.
        # 
        # > A value of 0 means storage is not charged for Professional Edition and Enterprise Edition instances; it does not mean the instances lack storage space.
        # 
        # - Platinum Edition instances: m × 100, where m is an integer from 7 to 28.
        self.storage_size = storage_size
        # Specifies whether to enable access over the public network. Valid values:
        # 
        # - `true`: Enables access over the public network.
        # 
        # - `false`: Disables access over the public network.
        self.support_eip = support_eip
        # Specifies whether to enable the message trace feature. Valid values:
        # 
        # - `true`: Enables the message trace feature.
        # 
        # - `false`: Disables the message trace feature.
        # 
        # > * The message trace feature is included for 15 days at no charge on Platinum Edition instances. For these instances, you must enable this feature and set the retention period to 15 days.
        # 
        # - For other instance types, you can enable or disable this feature.
        self.support_tracing = support_tracing
        # The resource tags.
        self.tags_shrink = tags_shrink
        # The retention period of message traces. Unit: days. Valid values:
        # 
        # - `3`
        # 
        # - `7`
        # 
        # - `15`
        # 
        # This parameter is required if you set `SupportTracing` to `true`.
        self.tracing_storage_time = tracing_storage_time
        # The ID of the VPC. This parameter is used to create a PrivateLink-based endpoint.
        # 
        # This parameter is required.
        self.vpc_id = vpc_id
        # The vSwitch IDs used to create a PrivateLink-based endpoint when you create the instance. The vSwitches must meet the following requirements:
        # 
        # 1. You must specify two vSwitches that reside in different availability zones, except for regions that have only a single availability zone.
        # 
        # 2. The vSwitches must belong to the specified VPC.
        # 
        # 3. The vSwitches must be in the Available state.
        # 
        # 4. Each vSwitch must have at least 20 available IP addresses.
        # 
        # 5. The availability zones for the specified vSwitches must support NLB instance creation.
        # 
        # This parameter is required.
        self.vswitch_ids_shrink = vswitch_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_model is not None:
            result['AuthModel'] = self.auth_model

        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.auto_renew_period is not None:
            result['AutoRenewPeriod'] = self.auto_renew_period

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.edition is not None:
            result['Edition'] = self.edition

        if self.encrypted_instance is not None:
            result['EncryptedInstance'] = self.encrypted_instance

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.kms_key_id is not None:
            result['KmsKeyId'] = self.kms_key_id

        if self.listener_mode is not None:
            result['ListenerMode'] = self.listener_mode

        if self.max_connections is not None:
            result['MaxConnections'] = self.max_connections

        if self.max_eip_tps is not None:
            result['MaxEipTps'] = self.max_eip_tps

        if self.max_private_tps is not None:
            result['MaxPrivateTps'] = self.max_private_tps

        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type

        if self.period is not None:
            result['Period'] = self.period

        if self.period_cycle is not None:
            result['PeriodCycle'] = self.period_cycle

        if self.provisioned_capacity is not None:
            result['ProvisionedCapacity'] = self.provisioned_capacity

        if self.queue_capacity is not None:
            result['QueueCapacity'] = self.queue_capacity

        if self.renew_status is not None:
            result['RenewStatus'] = self.renew_status

        if self.renewal_duration_unit is not None:
            result['RenewalDurationUnit'] = self.renewal_duration_unit

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.serverless_charge_type is not None:
            result['ServerlessChargeType'] = self.serverless_charge_type

        if self.serverless_switch is not None:
            result['ServerlessSwitch'] = self.serverless_switch

        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size

        if self.support_eip is not None:
            result['SupportEip'] = self.support_eip

        if self.support_tracing is not None:
            result['SupportTracing'] = self.support_tracing

        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink

        if self.tracing_storage_time is not None:
            result['TracingStorageTime'] = self.tracing_storage_time

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vswitch_ids_shrink is not None:
            result['VswitchIds'] = self.vswitch_ids_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthModel') is not None:
            self.auth_model = m.get('AuthModel')

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('AutoRenewPeriod') is not None:
            self.auto_renew_period = m.get('AutoRenewPeriod')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Edition') is not None:
            self.edition = m.get('Edition')

        if m.get('EncryptedInstance') is not None:
            self.encrypted_instance = m.get('EncryptedInstance')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('KmsKeyId') is not None:
            self.kms_key_id = m.get('KmsKeyId')

        if m.get('ListenerMode') is not None:
            self.listener_mode = m.get('ListenerMode')

        if m.get('MaxConnections') is not None:
            self.max_connections = m.get('MaxConnections')

        if m.get('MaxEipTps') is not None:
            self.max_eip_tps = m.get('MaxEipTps')

        if m.get('MaxPrivateTps') is not None:
            self.max_private_tps = m.get('MaxPrivateTps')

        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodCycle') is not None:
            self.period_cycle = m.get('PeriodCycle')

        if m.get('ProvisionedCapacity') is not None:
            self.provisioned_capacity = m.get('ProvisionedCapacity')

        if m.get('QueueCapacity') is not None:
            self.queue_capacity = m.get('QueueCapacity')

        if m.get('RenewStatus') is not None:
            self.renew_status = m.get('RenewStatus')

        if m.get('RenewalDurationUnit') is not None:
            self.renewal_duration_unit = m.get('RenewalDurationUnit')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('ServerlessChargeType') is not None:
            self.serverless_charge_type = m.get('ServerlessChargeType')

        if m.get('ServerlessSwitch') is not None:
            self.serverless_switch = m.get('ServerlessSwitch')

        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')

        if m.get('SupportEip') is not None:
            self.support_eip = m.get('SupportEip')

        if m.get('SupportTracing') is not None:
            self.support_tracing = m.get('SupportTracing')

        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')

        if m.get('TracingStorageTime') is not None:
            self.tracing_storage_time = m.get('TracingStorageTime')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VswitchIds') is not None:
            self.vswitch_ids_shrink = m.get('VswitchIds')

        return self

