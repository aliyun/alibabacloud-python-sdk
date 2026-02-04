# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dts20200101 import models as main_models
from darabonba.model import DaraModel

class SwitchSynchronizationEndpointRequest(DaraModel):
    def __init__(
        self,
        endpoint: main_models.SwitchSynchronizationEndpointRequestEndpoint = None,
        source_endpoint: main_models.SwitchSynchronizationEndpointRequestSourceEndpoint = None,
        account_id: str = None,
        owner_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        synchronization_direction: str = None,
        synchronization_job_id: str = None,
    ):
        self.endpoint = endpoint
        self.source_endpoint = source_endpoint
        # The ID of the Alibaba Cloud account. You do not need to specify this parameter because this parameter will be removed in the future.
        self.account_id = account_id
        self.owner_id = owner_id
        self.region_id = region_id
        # Resource group ID.
        self.resource_group_id = resource_group_id
        # The synchronization direction. Valid values:
        # 
        # *   **Forward**
        # *   **Reverse**
        # 
        # >  Default value: **Forward**.
        # 
        # The value **Reverse** takes effect only if the topology of the data synchronization instance is two-way synchronization.
        self.synchronization_direction = synchronization_direction
        # The ID of the data synchronization instance. You can call the DescribeSynchronizationJobs operation to query the instance ID.
        # 
        # This parameter is required.
        self.synchronization_job_id = synchronization_job_id

    def validate(self):
        if self.endpoint:
            self.endpoint.validate()
        if self.source_endpoint:
            self.source_endpoint.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint.to_map()

        if self.source_endpoint is not None:
            result['SourceEndpoint'] = self.source_endpoint.to_map()

        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.synchronization_direction is not None:
            result['SynchronizationDirection'] = self.synchronization_direction

        if self.synchronization_job_id is not None:
            result['SynchronizationJobId'] = self.synchronization_job_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Endpoint') is not None:
            temp_model = main_models.SwitchSynchronizationEndpointRequestEndpoint()
            self.endpoint = temp_model.from_map(m.get('Endpoint'))

        if m.get('SourceEndpoint') is not None:
            temp_model = main_models.SwitchSynchronizationEndpointRequestSourceEndpoint()
            self.source_endpoint = temp_model.from_map(m.get('SourceEndpoint'))

        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')

        if m.get('SynchronizationJobId') is not None:
            self.synchronization_job_id = m.get('SynchronizationJobId')

        return self

class SwitchSynchronizationEndpointRequestSourceEndpoint(DaraModel):
    def __init__(
        self,
        owner_id: str = None,
        role: str = None,
    ):
        # The ID of the Alibaba Cloud account to which the source instance belongs. You must specify this parameter only if the source instance and the destination instance belong to different Alibaba Cloud accounts.
        self.owner_id = owner_id
        # The authorized Resource Access Management (RAM) role of the source instance. You must specify the RAM role only if the source instance and the destination instance belong to different Alibaba Cloud accounts. You can use the RAM role to allow the Alibaba Cloud account that owns the destination instance to access the source instance.
        # 
        # >  For information about the permissions and authorization methods of the RAM role, see [Configure RAM authorization for cross-account data migration and synchronization](https://help.aliyun.com/document_detail/48468.html).
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.owner_id is not None:
            result['OwnerID'] = self.owner_id

        if self.role is not None:
            result['Role'] = self.role

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerID') is not None:
            self.owner_id = m.get('OwnerID')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        return self

class SwitchSynchronizationEndpointRequestEndpoint(DaraModel):
    def __init__(
        self,
        ip: str = None,
        instance_id: str = None,
        instance_type: str = None,
        port: str = None,
        type: str = None,
    ):
        # The IP address of the database.
        # 
        # >  You must specify the IP address only if the **Endpoint.InstanceType** parameter is set to **Express**.
        self.ip = ip
        # The ID of the ECS instance or the virtual private cloud (VPC).
        # 
        # > 
        # *   If the **Endpoint.InstanceType** parameter is set to **ECS**, you must specify the ID of the ECS instance.
        # *   If the **Endpoint.InstanceType** parameter is set to **Express**, you must specify the ID of the VPC.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The instance type of the database. Valid values:
        # 
        # *   **LocalInstance**: self-managed database with a public IP address
        # *   **ECS**: self-managed database that is hosted on ECS
        # *   **Express**: self-managed database that is connected over Express Connect
        # 
        # This parameter is required.
        self.instance_type = instance_type
        # The service port number of the database.
        # 
        # This parameter is required.
        self.port = port
        # Specifies whether to update the connection settings of the source instance or the destination instance. Valid values:
        # 
        # *   **Source**
        # *   **Destination**
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip is not None:
            result['IP'] = self.ip

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.port is not None:
            result['Port'] = self.port

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IP') is not None:
            self.ip = m.get('IP')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

