# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteDentryResponseBody(DaraModel):
    def __init__(
        self,
        async_: bool = None,
        request_id: str = None,
        task_id: str = None,
        vendor_request_id: str = None,
        vendor_type: str = None,
    ):
        self.async_ = async_
        self.request_id = request_id
        self.task_id = task_id
        self.vendor_request_id = vendor_request_id
        self.vendor_type = vendor_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.async_ is not None:
            result['async'] = self.async_

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.task_id is not None:
            result['taskId'] = self.task_id

        if self.vendor_request_id is not None:
            result['vendorRequestId'] = self.vendor_request_id

        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('async') is not None:
            self.async_ = m.get('async')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        if m.get('vendorRequestId') is not None:
            self.vendor_request_id = m.get('vendorRequestId')

        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')

        return self

