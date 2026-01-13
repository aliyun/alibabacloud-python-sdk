# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr_serverless_spark20230808 import models as main_models
from darabonba.model import DaraModel

class GetKyuubiTokenResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetKyuubiTokenResponseBodyData = None,
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
            result['data'] = self.data.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.GetKyuubiTokenResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetKyuubiTokenResponseBodyData(DaraModel):
    def __init__(
        self,
        auto_expire_configuration: main_models.GetKyuubiTokenResponseBodyDataAutoExpireConfiguration = None,
        create_time: int = None,
        created_by: str = None,
        expire_time: int = None,
        last_used_time: int = None,
        member_arns: List[str] = None,
        name: str = None,
        token: str = None,
        token_id: str = None,
    ):
        self.auto_expire_configuration = auto_expire_configuration
        self.create_time = create_time
        self.created_by = created_by
        self.expire_time = expire_time
        self.last_used_time = last_used_time
        self.member_arns = member_arns
        self.name = name
        self.token = token
        # Token ID。
        self.token_id = token_id

    def validate(self):
        if self.auto_expire_configuration:
            self.auto_expire_configuration.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_expire_configuration is not None:
            result['autoExpireConfiguration'] = self.auto_expire_configuration.to_map()

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.created_by is not None:
            result['createdBy'] = self.created_by

        if self.expire_time is not None:
            result['expireTime'] = self.expire_time

        if self.last_used_time is not None:
            result['lastUsedTime'] = self.last_used_time

        if self.member_arns is not None:
            result['memberArns'] = self.member_arns

        if self.name is not None:
            result['name'] = self.name

        if self.token is not None:
            result['token'] = self.token

        if self.token_id is not None:
            result['tokenId'] = self.token_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoExpireConfiguration') is not None:
            temp_model = main_models.GetKyuubiTokenResponseBodyDataAutoExpireConfiguration()
            self.auto_expire_configuration = temp_model.from_map(m.get('autoExpireConfiguration'))

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('createdBy') is not None:
            self.created_by = m.get('createdBy')

        if m.get('expireTime') is not None:
            self.expire_time = m.get('expireTime')

        if m.get('lastUsedTime') is not None:
            self.last_used_time = m.get('lastUsedTime')

        if m.get('memberArns') is not None:
            self.member_arns = m.get('memberArns')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('token') is not None:
            self.token = m.get('token')

        if m.get('tokenId') is not None:
            self.token_id = m.get('tokenId')

        return self

class GetKyuubiTokenResponseBodyDataAutoExpireConfiguration(DaraModel):
    def __init__(
        self,
        enable: bool = None,
        expire_days: int = None,
    ):
        self.enable = enable
        self.expire_days = expire_days

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable is not None:
            result['enable'] = self.enable

        if self.expire_days is not None:
            result['expireDays'] = self.expire_days

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')

        if m.get('expireDays') is not None:
            self.expire_days = m.get('expireDays')

        return self

