# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_emr_serverless_spark20230808 import models as main_models
from darabonba.model import DaraModel

class RefreshLivyComputeTokenRequest(DaraModel):
    def __init__(
        self,
        auto_expire_configuration: main_models.RefreshLivyComputeTokenRequestAutoExpireConfiguration = None,
        name: str = None,
        token: str = None,
        region_id: str = None,
    ):
        self.auto_expire_configuration = auto_expire_configuration
        self.name = name
        self.token = token
        self.region_id = region_id

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

        if self.name is not None:
            result['name'] = self.name

        if self.token is not None:
            result['token'] = self.token

        if self.region_id is not None:
            result['regionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoExpireConfiguration') is not None:
            temp_model = main_models.RefreshLivyComputeTokenRequestAutoExpireConfiguration()
            self.auto_expire_configuration = temp_model.from_map(m.get('autoExpireConfiguration'))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('token') is not None:
            self.token = m.get('token')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        return self

class RefreshLivyComputeTokenRequestAutoExpireConfiguration(DaraModel):
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

