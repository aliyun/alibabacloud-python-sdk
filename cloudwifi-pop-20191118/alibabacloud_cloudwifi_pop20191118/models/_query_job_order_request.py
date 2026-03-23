# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryJobOrderRequest(DaraModel):
    def __init__(
        self,
        app_code: str = None,
        app_name: str = None,
        order_id: int = None,
        request_id: str = None,
    ):
        self.app_code = app_code
        self.app_name = app_name
        # This parameter is required.
        self.order_id = order_id
        # This parameter is required.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_code is not None:
            result['AppCode'] = self.app_code

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

