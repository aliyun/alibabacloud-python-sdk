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
        # The Alibaba Cloud account ID. You do not need to specify this parameter because it will be deprecated.
        self.account_id = account_id
        self.owner_id = owner_id
        # The region ID. Specify this parameter to indicate the region where the instance resides. For more information, see [Supported regions](https://help.aliyun.com/document_detail/141033.html).
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The synchronization direction. Valid values:
        # - **Forward**: forward.
        # - **Reverse**: reverse.
        # 
        # > Default value: **Forward**. The value **Reverse** takes effect only when the synchronization topology of the data synchronization instance is two-way synchronization.
        self.synchronization_direction = synchronization_direction
        # Instance ID of the data synchronization instance. You can call the DescribeSynchronizationJobs operation to query instance ID.
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
        # 当源实例与目标实例所属阿里云账号不同时，您需要传入该参数指定源实例的所属阿里云账号的ID。
        self.owner_id = owner_id
        # 当源实例与目标实例所属阿里云账号不同时，需传入该参数，来指定源实例的授权角色，以允许目标实例阿里云账号访问源实例的实例信息。
        # > 角色所需的权限及授权方式，请参见[跨阿里云账号数据迁移或同步时如何配置RAM授权](https://help.aliyun.com/document_detail/48468.html)。
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
        # 新数据库的IP地址。
        # > 当**Endpoint.InstanceType**取值为**Express**时，本参数才可用且必须传入。
        self.ip = ip
        # ECS或专有网络的实例ID。
        # > - 当**Endpoint.InstanceType**取值为**ECS**时，本参数需传入ECS实例的ID。
        # - 当**Endpoint.InstanceType**取值为**Express**时，本参数需传入专有网络ID。
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # 新数据库所属的实例类型，取值：
        # 
        # - **LocalInstance**：有公网IP的自建数据库；
        # - **ECS**：ECS上的自建数据库。
        # - **Express**：通过专线接入的自建数据库。
        # 
        # This parameter is required.
        self.instance_type = instance_type
        # 新的数据库服务端口。
        # 
        # This parameter is required.
        self.port = port
        # 待调整连接信息的实例，取值：
        # 
        # - **Source**：源实例。
        # - **Destination**：目标实例。
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

