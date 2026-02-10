# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListBackupRecordRequest(DaraModel):
    def __init__(
        self,
        backup_end_time: int = None,
        backup_start_time: int = None,
        current_page: int = None,
        machine_remark: str = None,
        page_size: int = None,
        status_list: List[str] = None,
    ):
        # The timestamp when the backup task ended. Unit: milliseconds.
        self.backup_end_time = backup_end_time
        # The timestamp when the backup task started. Unit: milliseconds.
        self.backup_start_time = backup_start_time
        # The page number. Default value: **1**. Pages start from page 1.
        self.current_page = current_page
        # The information that you want to use to identify the servers protected by the anti-ransomware policy. You can enter the IP address or ID of a server.
        self.machine_remark = machine_remark
        # The number of entries per page. Default value: 20. If you leave this parameter empty, 20 entries are returned on each page.
        # 
        # >  We recommend that you do not leave this parameter empty.
        self.page_size = page_size
        # The backup task status. Valid values:
        # 
        # *   **BACKUP_COMPLETE**: The backup task is successful.
        # *   **BACKUP_FAILED**: The backup task failed.
        # *   **PARTIAL_COMPLETE**: The backup task is partially successful.
        self.status_list = status_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_end_time is not None:
            result['BackupEndTime'] = self.backup_end_time

        if self.backup_start_time is not None:
            result['BackupStartTime'] = self.backup_start_time

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.machine_remark is not None:
            result['MachineRemark'] = self.machine_remark

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.status_list is not None:
            result['StatusList'] = self.status_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupEndTime') is not None:
            self.backup_end_time = m.get('BackupEndTime')

        if m.get('BackupStartTime') is not None:
            self.backup_start_time = m.get('BackupStartTime')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('MachineRemark') is not None:
            self.machine_remark = m.get('MachineRemark')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')

        return self

