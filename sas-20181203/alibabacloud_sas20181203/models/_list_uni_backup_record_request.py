# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListUniBackupRecordRequest(DaraModel):
    def __init__(
        self,
        backup_region_id: str = None,
        current_page: int = None,
        machine_remark: str = None,
        page_size: int = None,
        state: str = None,
    ):
        # The region where the anti-ransomware backup service is located.
        # 
        # This parameter is required.
        self.backup_region_id = backup_region_id
        # When performing a paginated query, set the page number for the current page. The default value is **1**.
        self.current_page = current_page
        # The identification information of the server protected by the anti-ransomware policy. You can enter the IP address or instance ID of the server.
        self.machine_remark = machine_remark
        # The maximum number of data entries to display per page in a paginated query.
        self.page_size = page_size
        # Backup status. Values:
        # - **completed**: Success
        # - **error**: Failure
        # - **canceled**: Closed
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_region_id is not None:
            result['BackupRegionId'] = self.backup_region_id

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.machine_remark is not None:
            result['MachineRemark'] = self.machine_remark

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupRegionId') is not None:
            self.backup_region_id = m.get('BackupRegionId')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('MachineRemark') is not None:
            self.machine_remark = m.get('MachineRemark')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

