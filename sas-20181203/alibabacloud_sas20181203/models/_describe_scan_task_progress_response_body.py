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
        # The request ID. Alibaba Cloud generates a unique ID for each request. You can use the ID to troubleshoot issues.
        self.request_id = request_id
        # The progress of the virus scan task. Valid values:
        # - **init**: The scan task is being initialized.
        # - **Processing**: The scan task is in progress.
        # - **Success**: The scan task is complete.
        # - **Failed**: The scan task failed.
        self.scan_task_progress = scan_task_progress
        # The asset information scanned by the virus scan node. This parameter is a string converted from a JSON array in character format. The following fields are included:
        # - **type**: The Asset Type on which the virus scan is executed. Valid values:
        #     - **groupId**: server group.
        #     - **uuid**: server.
        # - **name**: The name of the server group or server.
        # - **target**: The asset on which the virus scan is executed. The following describes the values of this field:
        #     - If **type** is set to **groupId**, this field specifies the server group ID.
        #     - If **type** is set to **uuid**, this field specifies the UUID of the server.
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

