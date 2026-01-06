# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExecuteBatchTaskResponseBody(DaraModel):
    def __init__(
        self,
        fail_number: int = None,
        request_id: str = None,
        success_number: int = None,
        total: int = None,
        vendor_request_id: str = None,
        vendor_type: str = None,
    ):
        self.fail_number = fail_number
        self.request_id = request_id
        self.success_number = success_number
        self.total = total
        self.vendor_request_id = vendor_request_id
        self.vendor_type = vendor_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fail_number is not None:
            result['failNumber'] = self.fail_number

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success_number is not None:
            result['successNumber'] = self.success_number

        if self.total is not None:
            result['total'] = self.total

        if self.vendor_request_id is not None:
            result['vendorRequestId'] = self.vendor_request_id

        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('failNumber') is not None:
            self.fail_number = m.get('failNumber')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('successNumber') is not None:
            self.success_number = m.get('successNumber')

        if m.get('total') is not None:
            self.total = m.get('total')

        if m.get('vendorRequestId') is not None:
            self.vendor_request_id = m.get('vendorRequestId')

        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')

        return self

