# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListScanRuleRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        page_no: int = None,
        page_size: int = None,
        scan_type: str = None,
    ):
        # The instance ID.
        self.instance_id = instance_id
        # The page number.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
        # The type of the vulnerability. Valid values:
        # 
        # *   `VUL`: Products Cloud Security Scanner.
        # *   `SBOM`: Product Content Analysis.
        # 
        # Default value: `VUL`
        self.scan_type = scan_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.scan_type is not None:
            result['ScanType'] = self.scan_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ScanType') is not None:
            self.scan_type = m.get('ScanType')

        return self

