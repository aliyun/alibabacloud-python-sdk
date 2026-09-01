# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitCheckRequest(DaraModel):
    def __init__(
        self,
        resource_directory_account_id: int = None,
        scan_range: str = None,
        task_source: str = None,
    ):
        self.resource_directory_account_id = resource_directory_account_id
        # The scan range. Valid values:
        # - **FULL**: scans all check items
        # - **POLICY**: scans custom-configured check items
        self.scan_range = scan_range
        # The task source. Valid values:
        # 
        # - **YAO_CHI**: Alibaba Cloud ApsaraDB console.
        self.task_source = task_source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_directory_account_id is not None:
            result['ResourceDirectoryAccountId'] = self.resource_directory_account_id

        if self.scan_range is not None:
            result['ScanRange'] = self.scan_range

        if self.task_source is not None:
            result['TaskSource'] = self.task_source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceDirectoryAccountId') is not None:
            self.resource_directory_account_id = m.get('ResourceDirectoryAccountId')

        if m.get('ScanRange') is not None:
            self.scan_range = m.get('ScanRange')

        if m.get('TaskSource') is not None:
            self.task_source = m.get('TaskSource')

        return self

