# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dianjin20240628 import models as main_models
from darabonba.model import DaraModel

class QueryApiKeysResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.QueryApiKeysResponseBodyData] = None,
        message: str = None,
        retry_able: bool = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.retry_able = retry_able
        self.success = success

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
        if self.code is not None:
            result['code'] = self.code

        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['message'] = self.message

        if self.retry_able is not None:
            result['retryAble'] = self.retry_able

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.QueryApiKeysResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('retryAble') is not None:
            self.retry_able = m.get('retryAble')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class QueryApiKeysResponseBodyData(DaraModel):
    def __init__(
        self,
        expires_at: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        key_hash: str = None,
        key_id: str = None,
        status: str = None,
        tenant_id: str = None,
    ):
        self.expires_at = expires_at
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.key_hash = key_hash
        # **API Key ID**
        self.key_id = key_id
        self.status = status
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expires_at is not None:
            result['expiresAt'] = self.expires_at

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.key_hash is not None:
            result['keyHash'] = self.key_hash

        if self.key_id is not None:
            result['keyId'] = self.key_id

        if self.status is not None:
            result['status'] = self.status

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('expiresAt') is not None:
            self.expires_at = m.get('expiresAt')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('keyHash') is not None:
            self.key_hash = m.get('keyHash')

        if m.get('keyId') is not None:
            self.key_id = m.get('keyId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

