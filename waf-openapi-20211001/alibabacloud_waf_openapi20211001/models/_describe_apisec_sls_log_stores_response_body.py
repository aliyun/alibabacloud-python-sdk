# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeApisecSlsLogStoresResponseBody(DaraModel):
    def __init__(
        self,
        log_stores: List[str] = None,
        request_id: str = None,
    ):
        # The names of the Logstores in Simple Log Service.
        self.log_stores = log_stores
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.log_stores is not None:
            result['LogStores'] = self.log_stores

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogStores') is not None:
            self.log_stores = m.get('LogStores')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

