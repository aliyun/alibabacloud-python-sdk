# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hitsdb20200615 import models as main_models
from darabonba.model import DaraModel

class GetEngineDefaultAuthResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        auth_infos: List[main_models.GetEngineDefaultAuthResponseBodyAuthInfos] = None,
        instance_id: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.auth_infos = auth_infos
        self.instance_id = instance_id
        self.request_id = request_id

    def validate(self):
        if self.auth_infos:
            for v1 in self.auth_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        result['AuthInfos'] = []
        if self.auth_infos is not None:
            for k1 in self.auth_infos:
                result['AuthInfos'].append(k1.to_map() if k1 else None)

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        self.auth_infos = []
        if m.get('AuthInfos') is not None:
            for k1 in m.get('AuthInfos'):
                temp_model = main_models.GetEngineDefaultAuthResponseBodyAuthInfos()
                self.auth_infos.append(temp_model.from_map(k1))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetEngineDefaultAuthResponseBodyAuthInfos(DaraModel):
    def __init__(
        self,
        engine: str = None,
        password: str = None,
        username: str = None,
    ):
        self.engine = engine
        self.password = password
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.engine is not None:
            result['Engine'] = self.engine

        if self.password is not None:
            result['Password'] = self.password

        if self.username is not None:
            result['Username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        return self

