# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateVirusScanOnceTaskRequest(DaraModel):
    def __init__(
        self,
        param: str = None,
        scan_path: List[str] = None,
        scan_type: str = None,
        selection_key: str = None,
    ):
        # Additional information fields: 
        # - **additionType**: The type of extended scan
        self.param = param
        # The information about the scan path that is required for a custom scan.
        self.scan_path = scan_path
        # The type of the virus scan. Valid values:
        # 
        # *   **system**: system scan.
        # *   **user**: custom scan.
        self.scan_type = scan_type
        # The key that stores the asset information.
        # 
        # > You can call the [GetAssetSelectionConfig](~~GetAssetSelectionConfig~~) operation to obtain the key value.
        self.selection_key = selection_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.param is not None:
            result['Param'] = self.param

        if self.scan_path is not None:
            result['ScanPath'] = self.scan_path

        if self.scan_type is not None:
            result['ScanType'] = self.scan_type

        if self.selection_key is not None:
            result['SelectionKey'] = self.selection_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Param') is not None:
            self.param = m.get('Param')

        if m.get('ScanPath') is not None:
            self.scan_path = m.get('ScanPath')

        if m.get('ScanType') is not None:
            self.scan_type = m.get('ScanType')

        if m.get('SelectionKey') is not None:
            self.selection_key = m.get('SelectionKey')

        return self

