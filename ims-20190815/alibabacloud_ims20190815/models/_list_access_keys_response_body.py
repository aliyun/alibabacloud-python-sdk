# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ims20190815 import models as main_models
from darabonba.model import DaraModel

class ListAccessKeysResponseBody(DaraModel):
    def __init__(
        self,
        access_keys: main_models.ListAccessKeysResponseBodyAccessKeys = None,
        request_id: str = None,
    ):
        self.access_keys = access_keys
        self.request_id = request_id

    def validate(self):
        if self.access_keys:
            self.access_keys.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_keys is not None:
            result['AccessKeys'] = self.access_keys.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKeys') is not None:
            temp_model = main_models.ListAccessKeysResponseBodyAccessKeys()
            self.access_keys = temp_model.from_map(m.get('AccessKeys'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListAccessKeysResponseBodyAccessKeys(DaraModel):
    def __init__(
        self,
        access_key: List[main_models.ListAccessKeysResponseBodyAccessKeysAccessKey] = None,
    ):
        self.access_key = access_key

    def validate(self):
        if self.access_key:
            for v1 in self.access_key:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AccessKey'] = []
        if self.access_key is not None:
            for k1 in self.access_key:
                result['AccessKey'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.access_key = []
        if m.get('AccessKey') is not None:
            for k1 in m.get('AccessKey'):
                temp_model = main_models.ListAccessKeysResponseBodyAccessKeysAccessKey()
                self.access_key.append(temp_model.from_map(k1))

        return self

class ListAccessKeysResponseBodyAccessKeysAccessKey(DaraModel):
    def __init__(
        self,
        access_key_id: str = None,
        create_date: str = None,
        status: str = None,
        update_date: str = None,
    ):
        self.access_key_id = access_key_id
        self.create_date = create_date
        self.status = status
        self.update_date = update_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id

        if self.create_date is not None:
            result['CreateDate'] = self.create_date

        if self.status is not None:
            result['Status'] = self.status

        if self.update_date is not None:
            result['UpdateDate'] = self.update_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')

        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')

        return self

