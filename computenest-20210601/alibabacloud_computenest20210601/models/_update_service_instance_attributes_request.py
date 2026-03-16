# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_computenest20210601 import models as main_models
from darabonba.model import DaraModel

class UpdateServiceInstanceAttributesRequest(DaraModel):
    def __init__(
        self,
        enable_operation: bool = None,
        granted_permission: main_models.UpdateServiceInstanceAttributesRequestGrantedPermission = None,
        region_id: str = None,
        service_instance_id: str = None,
    ):
        # Specifies whether to authorize the service provider to perform O\\&M operations on the service instance.
        self.enable_operation = enable_operation
        self.granted_permission = granted_permission
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the service instance.
        # 
        # You can call the [ListServiceInstances](https://help.aliyun.com/document_detail/396200.html) operation to obtain the ID of the service instance.
        # 
        # This parameter is required.
        self.service_instance_id = service_instance_id

    def validate(self):
        if self.granted_permission:
            self.granted_permission.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_operation is not None:
            result['EnableOperation'] = self.enable_operation

        if self.granted_permission is not None:
            result['GrantedPermission'] = self.granted_permission.to_map()

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableOperation') is not None:
            self.enable_operation = m.get('EnableOperation')

        if m.get('GrantedPermission') is not None:
            temp_model = main_models.UpdateServiceInstanceAttributesRequestGrantedPermission()
            self.granted_permission = temp_model.from_map(m.get('GrantedPermission'))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')

        return self

class UpdateServiceInstanceAttributesRequestGrantedPermission(DaraModel):
    def __init__(
        self,
        operation_end_time: str = None,
        policy_names: str = None,
    ):
        self.operation_end_time = operation_end_time
        self.policy_names = policy_names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.operation_end_time is not None:
            result['OperationEndTime'] = self.operation_end_time

        if self.policy_names is not None:
            result['PolicyNames'] = self.policy_names

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperationEndTime') is not None:
            self.operation_end_time = m.get('OperationEndTime')

        if m.get('PolicyNames') is not None:
            self.policy_names = m.get('PolicyNames')

        return self

