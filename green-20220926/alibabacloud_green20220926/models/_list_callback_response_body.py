# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_green20220926 import models as main_models
from darabonba.model import DaraModel

class ListCallbackResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListCallbackResponseBodyData] = None,
        request_id: str = None,
    ):
        # Returned data.
        self.data = data
        # Backend-assigned ID, used to uniquely identify a request. Can be used for troubleshooting.
        self.request_id = request_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListCallbackResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListCallbackResponseBodyData(DaraModel):
    def __init__(
        self,
        crypt_type: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        name: str = None,
        scope: str = None,
        seed: str = None,
        uid: str = None,
        url: str = None,
    ):
        # Encryption algorithm.
        self.crypt_type = crypt_type
        # Creation time.
        self.gmt_create = gmt_create
        # Modification time.
        self.gmt_modified = gmt_modified
        # Primary key ID.
        self.id = id
        # Name.
        self.name = name
        # Result scope.
        self.scope = scope
        # Seed.
        self.seed = seed
        # UID.
        self.uid = uid
        # Callback URL.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.crypt_type is not None:
            result['CryptType'] = self.crypt_type

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.scope is not None:
            result['Scope'] = self.scope

        if self.seed is not None:
            result['Seed'] = self.seed

        if self.uid is not None:
            result['Uid'] = self.uid

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CryptType') is not None:
            self.crypt_type = m.get('CryptType')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        if m.get('Seed') is not None:
            self.seed = m.get('Seed')

        if m.get('Uid') is not None:
            self.uid = m.get('Uid')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

