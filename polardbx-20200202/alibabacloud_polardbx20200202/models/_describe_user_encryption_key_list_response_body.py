# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardbx20200202 import models as main_models
from darabonba.model import DaraModel

class DescribeUserEncryptionKeyListResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeUserEncryptionKeyListResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeUserEncryptionKeyListResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeUserEncryptionKeyListResponseBodyData(DaraModel):
    def __init__(
        self,
        key_ids: List[str] = None,
    ):
        self.key_ids = key_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key_ids is not None:
            result['KeyIds'] = self.key_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyIds') is not None:
            self.key_ids = m.get('KeyIds')

        return self

