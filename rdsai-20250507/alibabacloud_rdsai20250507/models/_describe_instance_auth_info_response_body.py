# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rdsai20250507 import models as main_models
from darabonba.model import DaraModel

class DescribeInstanceAuthInfoResponseBody(DaraModel):
    def __init__(
        self,
        api_keys: main_models.DescribeInstanceAuthInfoResponseBodyApiKeys = None,
        config_list: List[main_models.DescribeInstanceAuthInfoResponseBodyConfigList] = None,
        instance_name: str = None,
        jwt_secret: str = None,
        request_id: str = None,
    ):
        # API Keys
        self.api_keys = api_keys
        self.config_list = config_list
        self.instance_name = instance_name
        self.jwt_secret = jwt_secret
        self.request_id = request_id

    def validate(self):
        if self.api_keys:
            self.api_keys.validate()
        if self.config_list:
            for v1 in self.config_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_keys is not None:
            result['ApiKeys'] = self.api_keys.to_map()

        result['ConfigList'] = []
        if self.config_list is not None:
            for k1 in self.config_list:
                result['ConfigList'].append(k1.to_map() if k1 else None)

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.jwt_secret is not None:
            result['JwtSecret'] = self.jwt_secret

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKeys') is not None:
            temp_model = main_models.DescribeInstanceAuthInfoResponseBodyApiKeys()
            self.api_keys = temp_model.from_map(m.get('ApiKeys'))

        self.config_list = []
        if m.get('ConfigList') is not None:
            for k1 in m.get('ConfigList'):
                temp_model = main_models.DescribeInstanceAuthInfoResponseBodyConfigList()
                self.config_list.append(temp_model.from_map(k1))

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('JwtSecret') is not None:
            self.jwt_secret = m.get('JwtSecret')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeInstanceAuthInfoResponseBodyConfigList(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeInstanceAuthInfoResponseBodyApiKeys(DaraModel):
    def __init__(
        self,
        anon_key: str = None,
        service_key: str = None,
    ):
        # Supabase ANON_KEY
        self.anon_key = anon_key
        # Supabase SERVICE_ROLE_KEY
        self.service_key = service_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.anon_key is not None:
            result['AnonKey'] = self.anon_key

        if self.service_key is not None:
            result['ServiceKey'] = self.service_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnonKey') is not None:
            self.anon_key = m.get('AnonKey')

        if m.get('ServiceKey') is not None:
            self.service_key = m.get('ServiceKey')

        return self

