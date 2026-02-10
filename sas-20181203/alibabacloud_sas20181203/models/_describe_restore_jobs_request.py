# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeRestoreJobsRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        machine_remark: str = None,
        page_size: int = None,
        status: str = None,
    ):
        # The number of the page to return. Default value: **1**.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The unique identifier of the server on which the restoration task is run. For example, you can use the IP address or the name of the server.
        self.machine_remark = machine_remark
        # The number of entries to return on each page. Default value: **10**.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The status of the restoration task. Valid values:
        # 
        # *   **RUNNING**: The task is running.
        # *   **COMPLETE**: The task is complete.
        # *   **FAILED**: The task fails.
        # *   **CANCELING**: The task is being canceled.
        # *   **CANCELED**: The task is canceled.
        # *   **PARTIAL_COMPLETE**: The task is partially successful.
        # *   **CREATED**: The task is created but is not run.
        # *   **EXPIRED**: The task is not updated.
        # *   **QUEUED**: The task is waiting to be run.
        # *   **CLIENT_DELETED**: The task fails because the anti-ransomware agent is uninstalled.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.machine_remark is not None:
            result['MachineRemark'] = self.machine_remark

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('MachineRemark') is not None:
            self.machine_remark = m.get('MachineRemark')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

