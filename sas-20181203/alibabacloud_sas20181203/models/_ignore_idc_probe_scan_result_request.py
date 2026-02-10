# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class IgnoreIdcProbeScanResultRequest(DaraModel):
    def __init__(
        self,
        ignore_action: int = None,
        scan_result_ids: str = None,
    ):
        # The operation that you want to perform. Valid values:
        # 
        # *   **1**: adds the scan result to the whitelist.
        # *   **2**: ignores the scan result.
        # 
        # This parameter is required.
        self.ignore_action = ignore_action
        # The ID of the scan result. Separate multiple IDs with commas (,).
        # 
        # >  You can call the [DescribeIdcProbeScanResultList](~~DescribeIdcProbeScanResultList~~) operation to query the ID.
        # 
        # This parameter is required.
        self.scan_result_ids = scan_result_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ignore_action is not None:
            result['IgnoreAction'] = self.ignore_action

        if self.scan_result_ids is not None:
            result['ScanResultIds'] = self.scan_result_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IgnoreAction') is not None:
            self.ignore_action = m.get('IgnoreAction')

        if m.get('ScanResultIds') is not None:
            self.scan_result_ids = m.get('ScanResultIds')

        return self

