# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_amqp_open20191212 import models as main_models
from darabonba.model import DaraModel

class GetInstanceResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetInstanceResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The unique ID generated for the request. You can use this ID to troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetInstanceResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetInstanceResponseBodyData(DaraModel):
    def __init__(
        self,
        auto_renew_instance: bool = None,
        classic_endpoint: str = None,
        edition: str = None,
        encrypted_instance: bool = None,
        expire_time: int = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_type: str = None,
        kms_key_id: str = None,
        listener_mode: str = None,
        max_connections: int = None,
        max_eip_tps: int = None,
        max_queue: int = None,
        max_tps: int = None,
        max_vhost: int = None,
        order_create_time: int = None,
        order_type: str = None,
        private_endpoint: str = None,
        provisioned_capacity: int = None,
        public_endpoint: str = None,
        resource_group_id: str = None,
        security_group_id: str = None,
        serverless_switch: bool = None,
        status: str = None,
        storage_size: int = None,
        support_eip: bool = None,
        support_tracing: bool = None,
        tags: List[main_models.GetInstanceResponseBodyDataTags] = None,
        tracing_storage_time: int = None,
        vpc_id: str = None,
        vswitch_ids: List[str] = None,
    ):
        # Indicates whether auto-renewal is enabled for the instance.
        self.auto_renew_instance = auto_renew_instance
        # The classic network endpoint. This parameter is deprecated.
        self.classic_endpoint = classic_endpoint
        # The deployment architecture. Valid values:
        # 
        # - shared: shared architecture, which is suitable for reserved and elastic (shared) instances and pay-as-you-go instances.
        # 
        # - dedicated: dedicated architecture, which is suitable for reserved and elastic (dedicated) instances.
        self.edition = edition
        # Indicates whether storage encryption is enabled for the instance data.
        self.encrypted_instance = encrypted_instance
        # The timestamp that indicates when the instance expires, in milliseconds.
        # 
        # > The value is a long integer. Handle it with care in certain programming languages to prevent precision loss.
        self.expire_time = expire_time
        # The ID of the instance.
        self.instance_id = instance_id
        # The name of the instance. A length of 64 characters or less is recommended.
        self.instance_name = instance_name
        # The instance type.
        # 
        # - PROFESSIONAL: Professional Edition
        # 
        # - ENTERPRISE: Enterprise Edition
        # 
        # - VIP: Platinum Edition
        # 
        # - SERVERLESS: Serverless Edition
        self.instance_type = instance_type
        # The KMS key ID of the cloud disk.
        self.kms_key_id = kms_key_id
        # The listener mode. A value of tcp_and_ssl enables both port 5672 and 5671, while ssl_only enables only port 5671.
        self.listener_mode = listener_mode
        # The maximum number of connections.
        # 
        # For valid values, see the [ApsaraMQ for RabbitMQ purchase page](https://common-buy.aliyun.com/?commodityCode=ons_onsproxy_pre).
        self.max_connections = max_connections
        # The peak public TPS.
        # 
        # For valid values, see the [ApsaraMQ for RabbitMQ purchase page](https://common-buy.aliyun.com/?commodityCode=ons_onsproxy_pre).
        self.max_eip_tps = max_eip_tps
        # The maximum number of queues for the instance.
        self.max_queue = max_queue
        # The peak private TPS.
        self.max_tps = max_tps
        # The maximum number of vhosts for the instance.
        self.max_vhost = max_vhost
        # The timestamp that indicates when the order was created, in milliseconds.
        # 
        # > The value is a long integer. Handle it with care in certain programming languages to prevent precision loss.
        self.order_create_time = order_create_time
        # The billing method.
        # 
        # - PRE_PAID: subscription
        # 
        # - POST_PAID: pay-as-you-go
        self.order_type = order_type
        # The VPC endpoint of the instance.
        self.private_endpoint = private_endpoint
        # The reserved TPS capacity for reserved and elastic instances.
        self.provisioned_capacity = provisioned_capacity
        # The public endpoint of the instance.
        self.public_endpoint = public_endpoint
        # The ID of the resource group for the instance.
        self.resource_group_id = resource_group_id
        # The security group ID used to create a PrivateLink endpoint for the instance.
        self.security_group_id = security_group_id
        self.serverless_switch = serverless_switch
        # The instance status. Valid values:
        # 
        # - DEPLOYING: The instance is being deployed.
        # 
        # - EXPIRED: The instance has expired.
        # 
        # - SERVING: The instance is in service.
        # 
        # - RELEASED: The instance has been released.
        self.status = status
        # The disk capacity. Unit: GB.
        # 
        # > For Professional and Enterprise Edition instances, this parameter returns **-1**.
        self.storage_size = storage_size
        # Indicates whether the instance supports EIPs.
        self.support_eip = support_eip
        # Indicates whether the message trace feature is enabled.
        self.support_tracing = support_tracing
        # The list of tags.
        self.tags = tags
        # The retention period of message traces. Unit: days. Valid values:
        # 
        # - 3: 3 days
        # 
        # - 7: 7 days
        # 
        # - 15: 15 days
        # 
        # This parameter applies only when `SupportTracing` is set to true.
        self.tracing_storage_time = tracing_storage_time
        # The VPC ID used to create a PrivateLink endpoint for the instance.
        self.vpc_id = vpc_id
        # The VSwitch IDs used to create a PrivateLink endpoint for the instance.
        self.vswitch_ids = vswitch_ids

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_renew_instance is not None:
            result['AutoRenewInstance'] = self.auto_renew_instance

        if self.classic_endpoint is not None:
            result['ClassicEndpoint'] = self.classic_endpoint

        if self.edition is not None:
            result['Edition'] = self.edition

        if self.encrypted_instance is not None:
            result['EncryptedInstance'] = self.encrypted_instance

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

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

        if self.max_queue is not None:
            result['MaxQueue'] = self.max_queue

        if self.max_tps is not None:
            result['MaxTps'] = self.max_tps

        if self.max_vhost is not None:
            result['MaxVhost'] = self.max_vhost

        if self.order_create_time is not None:
            result['OrderCreateTime'] = self.order_create_time

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.private_endpoint is not None:
            result['PrivateEndpoint'] = self.private_endpoint

        if self.provisioned_capacity is not None:
            result['ProvisionedCapacity'] = self.provisioned_capacity

        if self.public_endpoint is not None:
            result['PublicEndpoint'] = self.public_endpoint

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.serverless_switch is not None:
            result['ServerlessSwitch'] = self.serverless_switch

        if self.status is not None:
            result['Status'] = self.status

        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size

        if self.support_eip is not None:
            result['SupportEIP'] = self.support_eip

        if self.support_tracing is not None:
            result['SupportTracing'] = self.support_tracing

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.tracing_storage_time is not None:
            result['TracingStorageTime'] = self.tracing_storage_time

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vswitch_ids is not None:
            result['VswitchIds'] = self.vswitch_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenewInstance') is not None:
            self.auto_renew_instance = m.get('AutoRenewInstance')

        if m.get('ClassicEndpoint') is not None:
            self.classic_endpoint = m.get('ClassicEndpoint')

        if m.get('Edition') is not None:
            self.edition = m.get('Edition')

        if m.get('EncryptedInstance') is not None:
            self.encrypted_instance = m.get('EncryptedInstance')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

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

        if m.get('MaxQueue') is not None:
            self.max_queue = m.get('MaxQueue')

        if m.get('MaxTps') is not None:
            self.max_tps = m.get('MaxTps')

        if m.get('MaxVhost') is not None:
            self.max_vhost = m.get('MaxVhost')

        if m.get('OrderCreateTime') is not None:
            self.order_create_time = m.get('OrderCreateTime')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('PrivateEndpoint') is not None:
            self.private_endpoint = m.get('PrivateEndpoint')

        if m.get('ProvisionedCapacity') is not None:
            self.provisioned_capacity = m.get('ProvisionedCapacity')

        if m.get('PublicEndpoint') is not None:
            self.public_endpoint = m.get('PublicEndpoint')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('ServerlessSwitch') is not None:
            self.serverless_switch = m.get('ServerlessSwitch')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')

        if m.get('SupportEIP') is not None:
            self.support_eip = m.get('SupportEIP')

        if m.get('SupportTracing') is not None:
            self.support_tracing = m.get('SupportTracing')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.GetInstanceResponseBodyDataTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TracingStorageTime') is not None:
            self.tracing_storage_time = m.get('TracingStorageTime')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VswitchIds') is not None:
            self.vswitch_ids = m.get('VswitchIds')

        return self

class GetInstanceResponseBodyDataTags(DaraModel):
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

