# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_fc20230330 import models as main_models
from darabonba.model import DaraModel

class ResidentResourcePool(DaraModel):
    def __init__(
        self,
        allocation_status: main_models.ResidentResourceAllocationStatus = None,
        associated_pool_id: str = None,
        created_time: str = None,
        expire_time: str = None,
        last_modified_time: str = None,
        pool_type: str = None,
        resident_resource_pool_id: str = None,
        resident_resource_pool_name: str = None,
        resource_pool_capacity: main_models.ResidentResourceCapacity = None,
        resource_pool_config: main_models.ResidentResourceCapacity = None,
        timed_config: main_models.TimedPoolConfig = None,
    ):
        # The real-time allocation status of the resource pool, including the specific allocation details for each function.
        self.allocation_status = allocation_status
        self.associated_pool_id = associated_pool_id
        # The resource property field that represents the creation time.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.created_time = created_time
        # The expiration time of the resource pool.
        self.expire_time = expire_time
        # The last modification time, including operations such as scaling, renewal, and renaming.
        self.last_modified_time = last_modified_time
        self.pool_type = pool_type
        self.resident_resource_pool_id = resident_resource_pool_id
        # The resource property field that represents the resource name.
        self.resident_resource_pool_name = resident_resource_pool_name
        # The overall specifications of the resource pool.
        self.resource_pool_capacity = resource_pool_capacity
        self.resource_pool_config = resource_pool_config
        self.timed_config = timed_config

    def validate(self):
        if self.allocation_status:
            self.allocation_status.validate()
        if self.resource_pool_capacity:
            self.resource_pool_capacity.validate()
        if self.resource_pool_config:
            self.resource_pool_config.validate()
        if self.timed_config:
            self.timed_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allocation_status is not None:
            result['allocationStatus'] = self.allocation_status.to_map()

        if self.associated_pool_id is not None:
            result['associatedPoolId'] = self.associated_pool_id

        if self.created_time is not None:
            result['createdTime'] = self.created_time

        if self.expire_time is not None:
            result['expireTime'] = self.expire_time

        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time

        if self.pool_type is not None:
            result['poolType'] = self.pool_type

        if self.resident_resource_pool_id is not None:
            result['residentResourcePoolId'] = self.resident_resource_pool_id

        if self.resident_resource_pool_name is not None:
            result['residentResourcePoolName'] = self.resident_resource_pool_name

        if self.resource_pool_capacity is not None:
            result['resourcePoolCapacity'] = self.resource_pool_capacity.to_map()

        if self.resource_pool_config is not None:
            result['resourcePoolConfig'] = self.resource_pool_config.to_map()

        if self.timed_config is not None:
            result['timedConfig'] = self.timed_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('allocationStatus') is not None:
            temp_model = main_models.ResidentResourceAllocationStatus()
            self.allocation_status = temp_model.from_map(m.get('allocationStatus'))

        if m.get('associatedPoolId') is not None:
            self.associated_pool_id = m.get('associatedPoolId')

        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')

        if m.get('expireTime') is not None:
            self.expire_time = m.get('expireTime')

        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')

        if m.get('poolType') is not None:
            self.pool_type = m.get('poolType')

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

        if m.get('timedConfig') is not None:
            temp_model = main_models.TimedPoolConfig()
            self.timed_config = temp_model.from_map(m.get('timedConfig'))

        return self

