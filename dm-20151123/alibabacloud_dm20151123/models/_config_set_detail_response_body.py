# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dm20151123 import models as main_models
from darabonba.model import DaraModel

class ConfigSetDetailResponseBody(DaraModel):
    def __init__(
        self,
        detail: main_models.ConfigSetDetailResponseBodyDetail = None,
        request_id: str = None,
    ):
        self.detail = detail
        self.request_id = request_id

    def validate(self):
        if self.detail:
            self.detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.detail is not None:
            result['Detail'] = self.detail.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Detail') is not None:
            temp_model = main_models.ConfigSetDetailResponseBodyDetail()
            self.detail = temp_model.from_map(m.get('Detail'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ConfigSetDetailResponseBodyDetail(DaraModel):
    def __init__(
        self,
        description: str = None,
        id: str = None,
        ip_pool: main_models.ConfigSetDetailResponseBodyDetailIpPool = None,
        name: str = None,
    ):
        self.description = description
        self.id = id
        self.ip_pool = ip_pool
        self.name = name

    def validate(self):
        if self.ip_pool:
            self.ip_pool.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.ip_pool is not None:
            result['IpPool'] = self.ip_pool.to_map()

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IpPool') is not None:
            temp_model = main_models.ConfigSetDetailResponseBodyDetailIpPool()
            self.ip_pool = temp_model.from_map(m.get('IpPool'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self



class ConfigSetDetailResponseBodyDetailIpPool(DaraModel):
    def __init__(
        self,
        ip_pool_id: str = None,
        ip_pool_name: str = None,
    ):
        self.ip_pool_id = ip_pool_id
        self.ip_pool_name = ip_pool_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip_pool_id is not None:
            result['IpPoolId'] = self.ip_pool_id

        if self.ip_pool_name is not None:
            result['IpPoolName'] = self.ip_pool_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpPoolId') is not None:
            self.ip_pool_id = m.get('IpPoolId')

        if m.get('IpPoolName') is not None:
            self.ip_pool_name = m.get('IpPoolName')

        return self

