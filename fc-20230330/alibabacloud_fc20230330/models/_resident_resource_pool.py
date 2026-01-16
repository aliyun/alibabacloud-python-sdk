# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_fc20230330 import models as main_models
from darabonba.model import DaraModel

class ResidentResourcePool(DaraModel):
    def __init__(
        self,
        allocation_status: main_models.ResidentResourceAllocationStatus = None,
        created_time: str = None,
        expire_time: str = None,
        last_modified_time: str = None,
        resident_resource_pool_id: str = None,
        resident_resource_pool_name: str = None,
        resource_pool_capacity: main_models.ResidentResourceCapacity = None,
        resource_pool_config: main_models.ResidentResourceCapacity = None,
    ):
        # 资源池实时分配情况，包含每个函数的具体分配情况
        self.allocation_status = allocation_status
        # 代表创建时间的资源属性字段
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.created_time = created_time
        # 资源池过期时间
        self.expire_time = expire_time
        # 上次修改时间，包含扩容、续费、更名等操作
        self.last_modified_time = last_modified_time
        self.resident_resource_pool_id = resident_resource_pool_id
        # 代表资源名称的资源属性字段
        self.resident_resource_pool_name = resident_resource_pool_name
        # 资源池总体规格
        self.resource_pool_capacity = resource_pool_capacity
        self.resource_pool_config = resource_pool_config

    def validate(self):
        if self.allocation_status:
            self.allocation_status.validate()
        if self.resource_pool_capacity:
            self.resource_pool_capacity.validate()
        if self.resource_pool_config:
            self.resource_pool_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allocation_status is not None:
            result['allocationStatus'] = self.allocation_status.to_map()

        if self.created_time is not None:
            result['createdTime'] = self.created_time

        if self.expire_time is not None:
            result['expireTime'] = self.expire_time

        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time

        if self.resident_resource_pool_id is not None:
            result['residentResourcePoolId'] = self.resident_resource_pool_id

        if self.resident_resource_pool_name is not None:
            result['residentResourcePoolName'] = self.resident_resource_pool_name

        if self.resource_pool_capacity is not None:
            result['resourcePoolCapacity'] = self.resource_pool_capacity.to_map()

        if self.resource_pool_config is not None:
            result['resourcePoolConfig'] = self.resource_pool_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('allocationStatus') is not None:
            temp_model = main_models.ResidentResourceAllocationStatus()
            self.allocation_status = temp_model.from_map(m.get('allocationStatus'))

        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')

        if m.get('expireTime') is not None:
            self.expire_time = m.get('expireTime')

        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')

        if m.get('residentResourcePoolId') is not None:
            self.resident_resource_pool_id = m.get('residentResourcePoolId')

        if m.get('residentResourcePoolName') is not None:
            self.resident_resource_pool_name = m.get('residentResourcePoolName')

        if m.get('resourcePoolCapacity') is not None:
            temp_model = main_models.ResidentResourceCapacity()
            self.resource_pool_capacity = temp_model.from_map(m.get('resourcePoolCapacity'))

        if m.get('resourcePoolConfig') is not None:
            temp_model = main_models.ResidentResourceCapacity()
            self.resource_pool_config = temp_model.from_map(m.get('resourcePoolConfig'))

        return self

