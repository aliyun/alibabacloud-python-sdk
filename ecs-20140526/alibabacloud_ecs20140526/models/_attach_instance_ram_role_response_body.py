# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class AttachInstanceRamRoleResponseBody(DaraModel):
    def __init__(
        self,
        attach_instance_ram_role_results: main_models.AttachInstanceRamRoleResponseBodyAttachInstanceRamRoleResults = None,
        fail_count: int = None,
        ram_role_name: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Details about the results of attaching the instance RAM role.
        self.attach_instance_ram_role_results = attach_instance_ram_role_results
        # The number of instances to which the instance RAM role failed to be attached.
        self.fail_count = fail_count
        # The name of the instance RAM role.
        self.ram_role_name = ram_role_name
        # The request ID.
        self.request_id = request_id
        # The total number of instances to which you attempted to attach the instance RAM role.
        self.total_count = total_count

    def validate(self):
        if self.attach_instance_ram_role_results:
            self.attach_instance_ram_role_results.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attach_instance_ram_role_results is not None:
            result['AttachInstanceRamRoleResults'] = self.attach_instance_ram_role_results.to_map()

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
        if m.get('AttachInstanceRamRoleResults') is not None:
            temp_model = main_models.AttachInstanceRamRoleResponseBodyAttachInstanceRamRoleResults()
            self.attach_instance_ram_role_results = temp_model.from_map(m.get('AttachInstanceRamRoleResults'))

        if m.get('FailCount') is not None:
            self.fail_count = m.get('FailCount')

        if m.get('RamRoleName') is not None:
            self.ram_role_name = m.get('RamRoleName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class AttachInstanceRamRoleResponseBodyAttachInstanceRamRoleResults(DaraModel):
    def __init__(
        self,
        attach_instance_ram_role_result: List[main_models.AttachInstanceRamRoleResponseBodyAttachInstanceRamRoleResultsAttachInstanceRamRoleResult] = None,
    ):
        self.attach_instance_ram_role_result = attach_instance_ram_role_result

    def validate(self):
        if self.attach_instance_ram_role_result:
            for v1 in self.attach_instance_ram_role_result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AttachInstanceRamRoleResult'] = []
        if self.attach_instance_ram_role_result is not None:
            for k1 in self.attach_instance_ram_role_result:
                result['AttachInstanceRamRoleResult'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attach_instance_ram_role_result = []
        if m.get('AttachInstanceRamRoleResult') is not None:
            for k1 in m.get('AttachInstanceRamRoleResult'):
                temp_model = main_models.AttachInstanceRamRoleResponseBodyAttachInstanceRamRoleResultsAttachInstanceRamRoleResult()
                self.attach_instance_ram_role_result.append(temp_model.from_map(k1))

        return self

class AttachInstanceRamRoleResponseBodyAttachInstanceRamRoleResultsAttachInstanceRamRoleResult(DaraModel):
    def __init__(
        self,
        code: str = None,
        instance_id: str = None,
        message: str = None,
        success: bool = None,
    ):
        # Indicates whether the instance RAM role was attached. If the instance RAM role was attached, 200 is returned. If the instance RAM role failed to be attached, any other value is returned. For more information, see the "Error codes" section.
        self.code = code
        # The ID of the instance.
        self.instance_id = instance_id
        # Indicates whether the instance RAM role was attached. If the instance RAM role was attached, success is returned. If the instance RAM role failed to be attached, any other value is returned. For more information, see the "Error codes" section.
        self.message = message
        # Indicates whether the instance RAM role was attached.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

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

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

