# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeVulExportInfoRequest(DaraModel):
    def __init__(
        self,
        export_id: int = None,
        resource_directory_account_id: int = None,
    ):
        # The ID of the task.
        # 
        # This parameter is required.
        self.export_id = export_id
        self.resource_directory_account_id = resource_directory_account_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.export_id is not None:
            result['ExportId'] = self.export_id

        if self.resource_directory_account_id is not None:
            result['ResourceDirectoryAccountId'] = self.resource_directory_account_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExportId') is not None:
            self.export_id = m.get('ExportId')

        if m.get('ResourceDirectoryAccountId') is not None:
            self.resource_directory_account_id = m.get('ResourceDirectoryAccountId')

        return self

