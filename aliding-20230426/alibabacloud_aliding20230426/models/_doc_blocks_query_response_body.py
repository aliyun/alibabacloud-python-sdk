# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class DocBlocksQueryResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.DocBlocksQueryResponseBodyResult = None,
        success: bool = None,
        vendor_request_id: str = None,
        vendor_type: str = None,
    ):
        self.request_id = request_id
        self.result = result
        self.success = success
        self.vendor_request_id = vendor_request_id
        self.vendor_type = vendor_type

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.result is not None:
            result['result'] = self.result.to_map()

        if self.success is not None:
            result['success'] = self.success

        if self.vendor_request_id is not None:
            result['vendorRequestId'] = self.vendor_request_id

        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('result') is not None:
            temp_model = main_models.DocBlocksQueryResponseBodyResult()
            self.result = temp_model.from_map(m.get('result'))

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('vendorRequestId') is not None:
            self.vendor_request_id = m.get('vendorRequestId')

        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')

        return self

class DocBlocksQueryResponseBodyResult(DaraModel):
    def __init__(
        self,
        data: List[Any] = None,
    ):
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')

        return self

