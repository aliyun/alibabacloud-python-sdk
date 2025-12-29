# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_oos20190601 import models as main_models
from darabonba.model import DaraModel

class ListInstancePatchStatesResponseBody(DaraModel):
    def __init__(
        self,
        instance_patch_states: List[main_models.ListInstancePatchStatesResponseBodyInstancePatchStates] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The details of patches of the instance.
        self.instance_patch_states = instance_patch_states
        # The number of entries returned on each page.
        self.max_results = max_results
        # The token that is used to retrieve the next page of results.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.instance_patch_states:
            for v1 in self.instance_patch_states:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstancePatchStates'] = []
        if self.instance_patch_states is not None:
            for k1 in self.instance_patch_states:
                result['InstancePatchStates'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_patch_states = []
        if m.get('InstancePatchStates') is not None:
            for k1 in m.get('InstancePatchStates'):
                temp_model = main_models.ListInstancePatchStatesResponseBodyInstancePatchStates()
                self.instance_patch_states.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListInstancePatchStatesResponseBodyInstancePatchStates(DaraModel):
    def __init__(
        self,
        baseline_id: str = None,
        failed_count: str = None,
        installed_count: str = None,
        installed_other_count: str = None,
        installed_pending_reboot_count: str = None,
        installed_rejected_count: str = None,
        instance_id: str = None,
        missing_count: str = None,
        operation_end_time: str = None,
        operation_start_time: str = None,
        operation_type: str = None,
        owner_information: str = None,
        patch_group: str = None,
    ):
        # The ID of the patch baseline.
        self.baseline_id = baseline_id
        # The number of patches that failed to be installed.
        self.failed_count = failed_count
        # The number of installed patches.
        self.installed_count = installed_count
        # The number of patches that do not meet the baseline.
        self.installed_other_count = installed_other_count
        # The number of patches that have been installed but require a restart to take effect.
        self.installed_pending_reboot_count = installed_pending_reboot_count
        # The number of patches that are rejected by the user.
        self.installed_rejected_count = installed_rejected_count
        # The ID of the ECS instance.
        self.instance_id = instance_id
        # The number of patches that are not installed.
        self.missing_count = missing_count
        # The time when the operation ended.
        self.operation_end_time = operation_end_time
        # The time when the operation was initiated.
        self.operation_start_time = operation_start_time
        # The operation type.
        self.operation_type = operation_type
        # The information about the user.
        self.owner_information = owner_information
        # The patch group.
        self.patch_group = patch_group

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.baseline_id is not None:
            result['BaselineId'] = self.baseline_id

        if self.failed_count is not None:
            result['FailedCount'] = self.failed_count

        if self.installed_count is not None:
            result['InstalledCount'] = self.installed_count

        if self.installed_other_count is not None:
            result['InstalledOtherCount'] = self.installed_other_count

        if self.installed_pending_reboot_count is not None:
            result['InstalledPendingRebootCount'] = self.installed_pending_reboot_count

        if self.installed_rejected_count is not None:
            result['InstalledRejectedCount'] = self.installed_rejected_count

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.missing_count is not None:
            result['MissingCount'] = self.missing_count

        if self.operation_end_time is not None:
            result['OperationEndTime'] = self.operation_end_time

        if self.operation_start_time is not None:
            result['OperationStartTime'] = self.operation_start_time

        if self.operation_type is not None:
            result['OperationType'] = self.operation_type

        if self.owner_information is not None:
            result['OwnerInformation'] = self.owner_information

        if self.patch_group is not None:
            result['PatchGroup'] = self.patch_group

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaselineId') is not None:
            self.baseline_id = m.get('BaselineId')

        if m.get('FailedCount') is not None:
            self.failed_count = m.get('FailedCount')

        if m.get('InstalledCount') is not None:
            self.installed_count = m.get('InstalledCount')

        if m.get('InstalledOtherCount') is not None:
            self.installed_other_count = m.get('InstalledOtherCount')

        if m.get('InstalledPendingRebootCount') is not None:
            self.installed_pending_reboot_count = m.get('InstalledPendingRebootCount')

        if m.get('InstalledRejectedCount') is not None:
            self.installed_rejected_count = m.get('InstalledRejectedCount')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MissingCount') is not None:
            self.missing_count = m.get('MissingCount')

        if m.get('OperationEndTime') is not None:
            self.operation_end_time = m.get('OperationEndTime')

        if m.get('OperationStartTime') is not None:
            self.operation_start_time = m.get('OperationStartTime')

        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')

        if m.get('OwnerInformation') is not None:
            self.owner_information = m.get('OwnerInformation')

        if m.get('PatchGroup') is not None:
            self.patch_group = m.get('PatchGroup')

        return self

