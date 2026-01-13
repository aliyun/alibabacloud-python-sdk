# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr_serverless_spark20230808 import models as main_models
from darabonba.model import DaraModel

class ListLivyComputeTokenResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListLivyComputeTokenResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.ListLivyComputeTokenResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListLivyComputeTokenResponseBodyData(DaraModel):
    def __init__(
        self,
        tokens: List[main_models.ListLivyComputeTokenResponseBodyDataTokens] = None,
    ):
        self.tokens = tokens

    def validate(self):
        if self.tokens:
            for v1 in self.tokens:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['tokens'] = []
        if self.tokens is not None:
            for k1 in self.tokens:
                result['tokens'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tokens = []
        if m.get('tokens') is not None:
            for k1 in m.get('tokens'):
                temp_model = main_models.ListLivyComputeTokenResponseBodyDataTokens()
                self.tokens.append(temp_model.from_map(k1))

        return self

class ListLivyComputeTokenResponseBodyDataTokens(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        createdby: str = None,
        expire_time: int = None,
        last_used_time: int = None,
        name: str = None,
        token: str = None,
        token_id: str = None,
    ):
        self.create_time = create_time
        self.createdby = createdby
        self.expire_time = expire_time
        self.last_used_time = last_used_time
        self.name = name
        self.token = token
        # Token ID。
        self.token_id = token_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.createdby is not None:
            result['createdby'] = self.createdby

        if self.expire_time is not None:
            result['expireTime'] = self.expire_time

        if self.last_used_time is not None:
            result['lastUsedTime'] = self.last_used_time

        if self.name is not None:
            result['name'] = self.name

        if self.token is not None:
            result['token'] = self.token

        if self.token_id is not None:
            result['tokenId'] = self.token_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('createdby') is not None:
            self.createdby = m.get('createdby')

        if m.get('expireTime') is not None:
            self.expire_time = m.get('expireTime')

        if m.get('lastUsedTime') is not None:
            self.last_used_time = m.get('lastUsedTime')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('token') is not None:
            self.token = m.get('token')

        if m.get('tokenId') is not None:
            self.token_id = m.get('tokenId')

        return self

