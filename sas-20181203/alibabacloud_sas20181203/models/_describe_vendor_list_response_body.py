# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeVendorListResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        vendor_name_list: List[str] = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # An array that consists of the service providers.
        self.vendor_name_list = vendor_name_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.vendor_name_list is not None:
            result['VendorNameList'] = self.vendor_name_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('VendorNameList') is not None:
            self.vendor_name_list = m.get('VendorNameList')

        return self

