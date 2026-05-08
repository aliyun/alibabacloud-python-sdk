# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20190315 import models as main_models
from darabonba.model import DaraModel

class DescribeLogStoreKeysResponseBody(DaraModel):
    def __init__(
        self,
        log_store_keys: main_models.DescribeLogStoreKeysResponseBodyLogStoreKeys = None,
        request_id: str = None,
    ):
        self.log_store_keys = log_store_keys
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.log_store_keys:
            self.log_store_keys.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.log_store_keys is not None:
            result['LogStoreKeys'] = self.log_store_keys.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogStoreKeys') is not None:
            temp_model = main_models.DescribeLogStoreKeysResponseBodyLogStoreKeys()
            self.log_store_keys = temp_model.from_map(m.get('LogStoreKeys'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeLogStoreKeysResponseBodyLogStoreKeys(DaraModel):
    def __init__(
        self,
        log_store_key: List[str] = None,
    ):
        self.log_store_key = log_store_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.log_store_key is not None:
            result['LogStoreKey'] = self.log_store_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogStoreKey') is not None:
            self.log_store_key = m.get('LogStoreKey')

        return self

