# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateInstanceRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        edition: str = None,
        encrypted_instance: bool = None,
        instance_id: str = None,
        instance_type: str = None,
        kms_key_id: str = None,
        max_connections: int = None,
        max_eip_tps: int = None,
        max_private_tps: int = None,
        modify_type: str = None,
        provisioned_capacity: int = None,
        queue_capacity: int = None,
        serverless_charge_type: str = None,
        storage_size: int = None,
        support_eip: bool = None,
        support_tracing: bool = None,
        tracing_storage_time: int = None,
    ):
        # The client token.
        self.client_token = client_token
        # The deployment architecture of the Serverless instance. Valid values:
        # 
        # - shared: A shared architecture. This applies to reserved plus elastic (shared) and pay-as-you-go instances.
        # 
        # - dedicated: A dedicated architecture. This applies to reserved plus elastic (dedicated) instances.
        self.edition = edition
        # This feature is for dedicated instances only. Specifies whether to enable data encryption.
        # 
        # - You cannot change the EncryptedInstance and KmsKeyId properties of a dedicated instance. This includes changing its encryption status or downgrading it to a shared instance. Do not include the EncryptedInstance and KmsKeyId parameters when you call UpdateInstance to upgrade or downgrade a dedicated instance.
        # 
        # - The EncryptedInstance and KmsKeyId parameters are used only when you upgrade a shared instance to an encrypted dedicated instance.
        self.encrypted_instance = encrypted_instance
        # The ID of the ApsaraMQ for RabbitMQ instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The instance type. This parameter is required for subscription instances. Valid values:
        # 
        # - professional: Professional Edition
        # 
        # - enterprise: Enterprise Edition
        # 
        # - vip: Platinum Edition
        # 
        # You do not need to specify this parameter for pay-as-you-go instances.
        self.instance_type = instance_type
        # This feature is for dedicated instances only. This parameter is required if EncryptedInstance is set to true.
        # It specifies the ID of the KMS key used for data encryption.
        # The key must meet the following requirements:
        # 
        # - The KMS key must be in the same region as the ApsaraMQ for RabbitMQ instance.
        # 
        # - The key cannot be a service key.
        # 
        # - The key must be active.
        # 
        # - The key must be a symmetric key.
        # 
        # - The key must be used for encryption and decryption.
        # 
        # - If the KMS key expires or is deleted, data reads and writes will fail, and the ApsaraMQ for RabbitMQ instance will become unavailable.
        self.kms_key_id = kms_key_id
        # The maximum number of connections.
        self.max_connections = max_connections
        # The peak TPS for public network traffic.
        self.max_eip_tps = max_eip_tps
        # The peak transactions per second (TPS) for private network traffic.
        self.max_private_tps = max_private_tps
        # The type of specification change. Valid values:
        # 
        # - UPGRADE: Upgrade
        # 
        # - DOWNGRADE: Downgrade
        # 
        # This parameter is required.
        self.modify_type = modify_type
        # The provisioned TPS capacity for a reserved plus elastic instance.
        self.provisioned_capacity = provisioned_capacity
        # The maximum number of queues.
        self.queue_capacity = queue_capacity
        # The billing method of the pay-as-you-go (Serverless) instance. Valid value:
        # 
        # - onDemand: Pay-as-you-go
        self.serverless_charge_type = serverless_charge_type
        # The message storage capacity. Unit: GB.
        self.storage_size = storage_size
        # Specifies whether to enable Internet access.
        self.support_eip = support_eip
        # Specifies whether to enable the message trace feature.
        self.support_tracing = support_tracing
        # The retention period for message traces. Unit: days.
        self.tracing_storage_time = tracing_storage_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.edition is not None:
            result['Edition'] = self.edition

        if self.encrypted_instance is not None:
            result['EncryptedInstance'] = self.encrypted_instance

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

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

        if self.modify_type is not None:
            result['ModifyType'] = self.modify_type

        if self.provisioned_capacity is not None:
            result['ProvisionedCapacity'] = self.provisioned_capacity

        if self.queue_capacity is not None:
            result['QueueCapacity'] = self.queue_capacity

        if self.serverless_charge_type is not None:
            result['ServerlessChargeType'] = self.serverless_charge_type

        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size

        if self.support_eip is not None:
            result['SupportEip'] = self.support_eip

        if self.support_tracing is not None:
            result['SupportTracing'] = self.support_tracing

        if self.tracing_storage_time is not None:
            result['TracingStorageTime'] = self.tracing_storage_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Edition') is not None:
            self.edition = m.get('Edition')

        if m.get('EncryptedInstance') is not None:
            self.encrypted_instance = m.get('EncryptedInstance')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

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

        if m.get('ModifyType') is not None:
            self.modify_type = m.get('ModifyType')

        if m.get('ProvisionedCapacity') is not None:
            self.provisioned_capacity = m.get('ProvisionedCapacity')

        if m.get('QueueCapacity') is not None:
            self.queue_capacity = m.get('QueueCapacity')

        if m.get('ServerlessChargeType') is not None:
            self.serverless_charge_type = m.get('ServerlessChargeType')

        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')

        if m.get('SupportEip') is not None:
            self.support_eip = m.get('SupportEip')

        if m.get('SupportTracing') is not None:
            self.support_tracing = m.get('SupportTracing')

        if m.get('TracingStorageTime') is not None:
            self.tracing_storage_time = m.get('TracingStorageTime')

        return self

