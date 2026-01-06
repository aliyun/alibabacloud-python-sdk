# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckAlibabaStaffResponseBody(DaraModel):
    def __init__(
        self,
        is_alibaba_staff: bool = None,
        request_id: str = None,
        vendor_request_id: str = None,
        vendor_type: str = None,
    ):
        self.is_alibaba_staff = is_alibaba_staff
        self.request_id = request_id
        self.vendor_request_id = vendor_request_id
        self.vendor_type = vendor_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_alibaba_staff is not None:
            result['isAlibabaStaff'] = self.is_alibaba_staff

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.vendor_request_id is not None:
            result['vendorRequestId'] = self.vendor_request_id

        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('isAlibabaStaff') is not None:
            self.is_alibaba_staff = m.get('isAlibabaStaff')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('vendorRequestId') is not None:
            self.vendor_request_id = m.get('vendorRequestId')

        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')

        return self

