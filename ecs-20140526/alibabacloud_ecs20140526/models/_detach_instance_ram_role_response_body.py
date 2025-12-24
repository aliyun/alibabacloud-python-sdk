# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DetachInstanceRamRoleResponseBody(DaraModel):
    def __init__(
        self,
        detach_instance_ram_role_results: main_models.DetachInstanceRamRoleResponseBodyDetachInstanceRamRoleResults = None,
        fail_count: int = None,
        ram_role_name: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The results of the instance RAM role detachment, which include the names of the instance RAM roles and the IDs of the ECS instances from which you attempted to detach the instance RAM roles.
        self.detach_instance_ram_role_results = detach_instance_ram_role_results
        # The number of ECS instances from which instance RAM roles failed to be detached.
        self.fail_count = fail_count
        # The name of the instance RAM role.
        self.ram_role_name = ram_role_name
        # The request ID.
        self.request_id = request_id
        # The total number of ECS instances from which you attempted to detach instance RAM roles.
        self.total_count = total_count

    def validate(self):
        if self.detach_instance_ram_role_results:
            self.detach_instance_ram_role_results.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.detach_instance_ram_role_results is not None:
            result['DetachInstanceRamRoleResults'] = self.detach_instance_ram_role_results.to_map()

        if self.fail_count is not None:
            result['FailCount'] = self.fail_count

        if self.ram_role_name is not None:
            result['RamRoleName'] = self.ram_role_name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DetachInstanceRamRoleResults') is not None:
            temp_model = main_models.DetachInstanceRamRoleResponseBodyDetachInstanceRamRoleResults()
            self.detach_instance_ram_role_results = temp_model.from_map(m.get('DetachInstanceRamRoleResults'))

        if m.get('FailCount') is not None:
            self.fail_count = m.get('FailCount')

        if m.get('RamRoleName') is not None:
            self.ram_role_name = m.get('RamRoleName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DetachInstanceRamRoleResponseBodyDetachInstanceRamRoleResults(DaraModel):
    def __init__(
        self,
        detach_instance_ram_role_result: List[main_models.DetachInstanceRamRoleResponseBodyDetachInstanceRamRoleResultsDetachInstanceRamRoleResult] = None,
    ):
        self.detach_instance_ram_role_result = detach_instance_ram_role_result

    def validate(self):
        if self.detach_instance_ram_role_result:
            for v1 in self.detach_instance_ram_role_result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DetachInstanceRamRoleResult'] = []
        if self.detach_instance_ram_role_result is not None:
            for k1 in self.detach_instance_ram_role_result:
                result['DetachInstanceRamRoleResult'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.detach_instance_ram_role_result = []
        if m.get('DetachInstanceRamRoleResult') is not None:
            for k1 in m.get('DetachInstanceRamRoleResult'):
                temp_model = main_models.DetachInstanceRamRoleResponseBodyDetachInstanceRamRoleResultsDetachInstanceRamRoleResult()
                self.detach_instance_ram_role_result.append(temp_model.from_map(k1))

        return self

class DetachInstanceRamRoleResponseBodyDetachInstanceRamRoleResultsDetachInstanceRamRoleResult(DaraModel):
    def __init__(
        self,
        code: str = None,
        instance_id: str = None,
        instance_ram_role_sets: main_models.DetachInstanceRamRoleResponseBodyDetachInstanceRamRoleResultsDetachInstanceRamRoleResultInstanceRamRoleSets = None,
        message: str = None,
        success: bool = None,
    ):
        # Indicates whether the instance RAM role was detached. If 200 is returned, the instance RAM role was detached. If any other value is returned, the instance RAM role failed to be detached. For more information, see the "Error codes" section.
        self.code = code
        # The ID of the ECS instance from which you attempted to detach the instance RAM role.
        self.instance_id = instance_id
        # The name of the instance RAM role and the ID of the ECS instance.
        self.instance_ram_role_sets = instance_ram_role_sets
        # Indicates whether the instance RAM role was detached. If success is returned, the instance RAM role was detached. If any other value is returned, the instance RAM role failed to be detached. For more information, see the "Error codes" section.
        self.message = message
        # Indicates whether the instance RAM role was detached.
        self.success = success

    def validate(self):
        if self.instance_ram_role_sets:
            self.instance_ram_role_sets.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_ram_role_sets is not None:
            result['InstanceRamRoleSets'] = self.instance_ram_role_sets.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceRamRoleSets') is not None:
            temp_model = main_models.DetachInstanceRamRoleResponseBodyDetachInstanceRamRoleResultsDetachInstanceRamRoleResultInstanceRamRoleSets()
            self.instance_ram_role_sets = temp_model.from_map(m.get('InstanceRamRoleSets'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DetachInstanceRamRoleResponseBodyDetachInstanceRamRoleResultsDetachInstanceRamRoleResultInstanceRamRoleSets(DaraModel):
    def __init__(
        self,
        instance_ram_role_set: List[main_models.DetachInstanceRamRoleResponseBodyDetachInstanceRamRoleResultsDetachInstanceRamRoleResultInstanceRamRoleSetsInstanceRamRoleSet] = None,
    ):
        self.instance_ram_role_set = instance_ram_role_set

    def validate(self):
        if self.instance_ram_role_set:
            for v1 in self.instance_ram_role_set:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstanceRamRoleSet'] = []
        if self.instance_ram_role_set is not None:
            for k1 in self.instance_ram_role_set:
                result['InstanceRamRoleSet'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_ram_role_set = []
        if m.get('InstanceRamRoleSet') is not None:
            for k1 in m.get('InstanceRamRoleSet'):
                temp_model = main_models.DetachInstanceRamRoleResponseBodyDetachInstanceRamRoleResultsDetachInstanceRamRoleResultInstanceRamRoleSetsInstanceRamRoleSet()
                self.instance_ram_role_set.append(temp_model.from_map(k1))

        return self

class DetachInstanceRamRoleResponseBodyDetachInstanceRamRoleResultsDetachInstanceRamRoleResultInstanceRamRoleSetsInstanceRamRoleSet(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        ram_role_name: str = None,
    ):
        # The ID of the ECS instance.
        self.instance_id = instance_id
        # The name of the instance RAM role.
        self.ram_role_name = ram_role_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.ram_role_name is not None:
            result['RamRoleName'] = self.ram_role_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RamRoleName') is not None:
            self.ram_role_name = m.get('RamRoleName')

        return self

