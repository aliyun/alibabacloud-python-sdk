# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeScanTaskProgressResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        scan_task_progress: str = None,
        target_info: str = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The progress of the virus scan task. Valid values:
        # 
        # *   **init**: The task is being initialized.
        # *   **Processing**: The task is running.
        # *   **Success**: The task is complete.
        # *   **Failed**: The task fails.
        self.scan_task_progress = scan_task_progress
        # The information about the asset on which the virus scan task runs. The value is a string that consists of JSON arrays. Each element in a JSON array is a JSON struct that contains the following fields:
        # 
        # *   **type**: the type of the asset on which you want to perform a virus scan task. Valid values:
        # 
        #     *   **groupId**: server group.
        #     *   **uuid**: server.
        # 
        # *   **name**: the name of the server group or server.
        # 
        # *   **target**: the asset on which the virus scan task runs. The value of this field varies based on the value of the type field.
        # 
        #     *   If the **type** field is set to **groupId**, the value of this field is the ID of the server group.
        #     *   If the **type** field is set to **uuid**, the value of this field is the universally unique identifier (UUID) of the server.
        self.target_info = target_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.scan_task_progress is not None:
            result['ScanTaskProgress'] = self.scan_task_progress

        if self.target_info is not None:
            result['TargetInfo'] = self.target_info

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ScanTaskProgress') is not None:
            self.scan_task_progress = m.get('ScanTaskProgress')

        if m.get('TargetInfo') is not None:
            self.target_info = m.get('TargetInfo')

        return self

