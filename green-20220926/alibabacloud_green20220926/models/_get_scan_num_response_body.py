# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetScanNumResponseBody(DaraModel):
    def __init__(
        self,
        limit_number: int = None,
        request_id: str = None,
        scan_number: int = None,
        sum_number: int = None,
        tag: bool = None,
    ):
        # Upper limit of the quantity.
        self.limit_number = limit_number
        # ID assigned by the backend, used to uniquely identify a request. Can be used for troubleshooting.
        self.request_id = request_id
        # Total number of files pending inspection.
        self.scan_number = scan_number
        # Total number of files.
        self.sum_number = sum_number
        # Whether it is a whitelist user.
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.limit_number is not None:
            result['LimitNumber'] = self.limit_number

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.scan_number is not None:
            result['ScanNumber'] = self.scan_number

        if self.sum_number is not None:
            result['SumNumber'] = self.sum_number

        if self.tag is not None:
            result['Tag'] = self.tag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LimitNumber') is not None:
            self.limit_number = m.get('LimitNumber')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ScanNumber') is not None:
            self.scan_number = m.get('ScanNumber')

        if m.get('SumNumber') is not None:
            self.sum_number = m.get('SumNumber')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        return self

