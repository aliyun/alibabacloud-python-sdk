# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dds20151201 import models as main_models
from darabonba.model import DaraModel

class DescribeUserEncryptionKeyListResponseBody(DaraModel):
    def __init__(
        self,
        key_ids: main_models.DescribeUserEncryptionKeyListResponseBodyKeyIds = None,
        request_id: str = None,
    ):
        # The list of custom keys.
        self.key_ids = key_ids
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.key_ids:
            self.key_ids.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key_ids is not None:
            result['KeyIds'] = self.key_ids.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyIds') is not None:
            temp_model = main_models.DescribeUserEncryptionKeyListResponseBodyKeyIds()
            self.key_ids = temp_model.from_map(m.get('KeyIds'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeUserEncryptionKeyListResponseBodyKeyIds(DaraModel):
    def __init__(
        self,
        key_id: List[str] = None,
    ):
        self.key_id = key_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key_id is not None:
            result['KeyId'] = self.key_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')

        return self

