# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_amqp_open20191212 import models as main_models
from darabonba.model import DaraModel

class ListInstancesResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListInstancesResponseBodyData = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The request ID.
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
            temp_model = main_models.ListInstancesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListInstancesResponseBodyData(DaraModel):
    def __init__(
        self,
        instances: List[main_models.ListInstancesResponseBodyDataInstances] = None,
        max_results: int = None,
        next_token: str = None,
    ):
        # The instances.
        self.instances = instances
        # The maximum number of entries returned.
        self.max_results = max_results
        # The token that marks the end of the current returned page. If this parameter is empty, all data is retrieved.
        self.next_token = next_token

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

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instances = []
        if m.get('Instances') is not None:
            for k1 in m.get('Instances'):
                temp_model = main_models.ListInstancesResponseBodyDataInstances()
                self.instances.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        return self

class ListInstancesResponseBodyDataInstances(DaraModel):
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
        status: str = None,
        storage_size: int = None,
        support_eip: bool = None,
        tags: List[main_models.ListInstancesResponseBodyDataInstancesTags] = None,
    ):
        # Indicates whether the instance is automatically renewed.
        self.auto_renew_instance = auto_renew_instance
        # The endpoint that is used to access the instance over the classic network. This parameter is no longer available.
        self.classic_endpoint = classic_endpoint
        self.edition = edition
        # Indicates whether the encryption at rest feature is enabled for the instance.
        self.encrypted_instance = encrypted_instance
        # The timestamp that indicates when the instance expires. Unit: milliseconds.
        self.expire_time = expire_time
        # The instance ID
        self.instance_id = instance_id
        # The instance name.
        self.instance_name = instance_name
        # The instance type.
        # 
        # *   PROFESSIONAL: Professional Edition
        # *   ENTERPRISE: Enterprise Edition
        # *   VIP: Enterprise Platinum Edition
        self.instance_type = instance_type
        # The ID of the Key Management Service (KMS) key used for the data disk.
        self.kms_key_id = kms_key_id
        # The maximum number of Internet-based transactions per second (TPS) for the instance.
        self.max_eip_tps = max_eip_tps
        # The maximum number of queues on the instance.
        self.max_queue = max_queue
        # The maximum number of VPC-based TPS for the instance.
        self.max_tps = max_tps
        # The maximum number of vhosts on the instance.
        self.max_vhost = max_vhost
        # The timestamp that indicates when the order was created. Unit: milliseconds.
        self.order_create_time = order_create_time
        # The billing method. Valid values:
        # 
        # *   PrePaid: the subscription billing method.
        # *   POST_PAID: the pay-as-you-go billing method.
        self.order_type = order_type
        # The virtual private cloud (VPC) endpoint of the instance.
        self.private_endpoint = private_endpoint
        self.provisioned_capacity = provisioned_capacity
        # The public endpoint of the instance.
        self.public_endpoint = public_endpoint
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id
        # The instance status. Valid values:
        # 
        # *   DEPLOYING: The instance is being deployed.
        # *   EXPIRED: The instance is expired.
        # *   SERVING: The instance is running.
        # *   RELEASED: The instance is released.
        self.status = status
        # The disk size. Unit: GB.
        # 
        # >  For Professional Edition instances and Enterprise Edition instances, this parameter is unavailable and \\*\\*-1\\*\\* is returned.
        self.storage_size = storage_size
        # Indicates whether the instance supports elastic IP addresses (EIPs).
        self.support_eip = support_eip
        # The tags that are added to the instance.
        self.tags = tags

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

        if self.status is not None:
            result['Status'] = self.status

        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size

        if self.support_eip is not None:
            result['SupportEIP'] = self.support_eip

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

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

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')

        if m.get('SupportEIP') is not None:
            self.support_eip = m.get('SupportEIP')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListInstancesResponseBodyDataInstancesTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class ListInstancesResponseBodyDataInstancesTags(DaraModel):
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

