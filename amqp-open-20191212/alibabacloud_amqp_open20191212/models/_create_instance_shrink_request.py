# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateInstanceShrinkRequest(DaraModel):
    def __init__(
        self,
        auto_renew: bool = None,
        auto_renew_period: int = None,
        client_token: str = None,
        edition: str = None,
        encrypted_instance: bool = None,
        instance_name: str = None,
        instance_type: str = None,
        kms_key_id: str = None,
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
        serverless_charge_type: str = None,
        storage_size: int = None,
        support_eip: bool = None,
        support_tracing: bool = None,
        tags_shrink: str = None,
        tracing_storage_time: int = None,
    ):
        # Specifies whether to enable auto-renewal. Valid values:
        # 
        # *   true: enables auto-renewal.
        # *   false: disables auto-renewal. If you select this value, you must manually renew the instance.
        self.auto_renew = auto_renew
        # The auto-renewal period. The unit of the auto-renewal period is specified by RenewalDurationUnit. Default value: Month.
        # 
        # >  This parameter takes effect only if you set AutoRenew to true. Default value: 1.
        self.auto_renew_period = auto_renew_period
        # The client token.
        self.client_token = client_token
        self.edition = edition
        # Specifies whether to enable storage encryption for the instance. This parameter is available only for exclusive instances.
        self.encrypted_instance = encrypted_instance
        # The name of the instance. We recommend that you specify a name that does not exceed 64 characters in length.
        self.instance_name = instance_name
        # The instance edition. Valid values if you create a subscription instance:
        # 
        # *   professional: Professional Edition.
        # *   enterprise: Enterprise Edition
        # *   vip: Enterprise Platinum Edition
        # 
        # If you create a serverless instance, you do not need to specify this parameter.
        self.instance_type = instance_type
        # The ID of the Key Management Service (KMS)-managed key used for storage encryption. This parameter is available only for exclusive instances and required only if you set EncryptedInstance to true. The key must meet the following conditions:
        # 
        # *   The key cannot be a service key.
        # *   The key must be in the Enabled state.
        # *   The key must be a symmetric key.
        # *   The key must be used for encryption and decryption.
        # *   After the key is expired or deleted, you cannot read or write data and exceptions can occur in the ApsaraMQ for RabbitMQ instance.
        self.kms_key_id = kms_key_id
        # The maximum number of connections that can be established to the instance.
        # 
        # Configure this parameter based on the values provided on the [ApsaraMQ for RocketMQ buy page](https://common-buy.aliyun.com/?commodityCode=ons_onsproxy_pre).
        self.max_connections = max_connections
        # The maximum number of Internet-based TPS on the instance.
        # 
        # Configure this parameter based on the values provided on the [ApsaraMQ for RocketMQ buy page](https://common-buy.aliyun.com/?commodityCode=ons_onsproxy_pre).
        self.max_eip_tps = max_eip_tps
        # The maximum number of virtual private cloud (VPC)-based transactions per second (TPS) on the instance.
        # 
        # Configure this parameter based on the values provided on the [ApsaraMQ for RocketMQ buy page](https://common-buy.aliyun.com/?commodityCode=ons_onsproxy_pre).
        self.max_private_tps = max_private_tps
        # The billing method of the instance. Valid values:
        # 
        # *   Subscription: subscription instance
        # *   PayAsYouGo: serverless instance
        # 
        # This parameter is required.
        self.payment_type = payment_type
        # The subscription period. The unit of the subscription period is specified by periodCycle.
        # 
        # >  This parameter takes effect only if you set PaymentType to Subscription. Default value: 1.
        self.period = period
        # The unit of the subscription period. Valid values:
        # 
        # *   Month
        # *   Year
        # 
        # This parameter is valid only if you set PaymentType to Subscription. Default value: Month.
        self.period_cycle = period_cycle
        self.provisioned_capacity = provisioned_capacity
        # The number of queues on the instance.
        # 
        # Configure this parameter based on the values provided on the [ApsaraMQ for RocketMQ buy page](https://common-buy.aliyun.com/?commodityCode=ons_onsproxy_pre).
        self.queue_capacity = queue_capacity
        # The renewal status. This parameter is the same as AutoRenew. You can configure one of these parameters. Valid value:
        # 
        # *   AutoRenewal
        # 
        # >  If you configure both this parameter and AutoRenew, the value of this parameter is used.
        self.renew_status = renew_status
        # The unit of the auto-renewal period. Valid values:
        # 
        # *   Month
        # *   Year
        self.renewal_duration_unit = renewal_duration_unit
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id
        # The billing method of the serverless instance. Valid value:
        # 
        # *   onDemand: You are charged based on your actual usage.
        self.serverless_charge_type = serverless_charge_type
        # The storage capacity. Unit: GB. Valid values:
        # 
        # *   Professional Edition and Enterprise Edition instances: Set the value to 0.
        # 
        # >  The value 0 specifies that storage space is available for Professional Edition and Enterprise Edition instances, but no storage fees are generated.
        # 
        # *   Enterprise Platinum Edition instances: Set the value to m × 100, where m is an integer that ranges from 7 to 28.
        self.storage_size = storage_size
        # Specifies whether elastic IP addresses (EIPs) are supported. Valid values:
        # 
        # *   True
        # *   False
        self.support_eip = support_eip
        # Specifies whether to enable the message trace feature. Valid values:
        # 
        # *   true
        # *   false
        # 
        # > 
        # 
        # *   Enterprise Platinum Edition instances allow you to retain message traces for 15 days free of charge. If you create an Enterprise Platinum Edition instance, you can set this parameter only to true and TracingStorageTime only to 15.
        # 
        # *   For instances of other editions, you can set this parameter to true or false.
        self.support_tracing = support_tracing
        self.tags_shrink = tags_shrink
        # The retention period of messages. Unit: days. Valid values:
        # 
        # *   3
        # *   7
        # *   15
        # 
        # This parameter is valid only if you set SupportTracing to true.
        self.tracing_storage_time = tracing_storage_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        if self.serverless_charge_type is not None:
            result['ServerlessChargeType'] = self.serverless_charge_type

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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

        if m.get('ServerlessChargeType') is not None:
            self.serverless_charge_type = m.get('ServerlessChargeType')

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

        return self

