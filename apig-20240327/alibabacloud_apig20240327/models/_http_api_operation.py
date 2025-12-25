# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class HttpApiOperation(DaraModel):
    def __init__(
        self,
        auth_config: main_models.AuthConfig = None,
        deploy_configs: List[main_models.HttpApiDeployConfig] = None,
        description: str = None,
        enable_auth: bool = None,
        method: str = None,
        mock: main_models.HttpApiMockContract = None,
        name: str = None,
        path: str = None,
        request: main_models.HttpApiRequestContract = None,
        response: main_models.HttpApiResponseContract = None,
    ):
        self.auth_config = auth_config
        self.deploy_configs = deploy_configs
        self.description = description
        self.enable_auth = enable_auth
        # This parameter is required.
        self.method = method
        self.mock = mock
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.path = path
        self.request = request
        self.response = response

    def validate(self):
        if self.auth_config:
            self.auth_config.validate()
        if self.deploy_configs:
            for v1 in self.deploy_configs:
                 if v1:
                    v1.validate()
        if self.mock:
            self.mock.validate()
        if self.request:
            self.request.validate()
        if self.response:
            self.response.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_config is not None:
            result['authConfig'] = self.auth_config.to_map()

        result['deployConfigs'] = []
        if self.deploy_configs is not None:
            for k1 in self.deploy_configs:
                result['deployConfigs'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['description'] = self.description

        if self.enable_auth is not None:
            result['enableAuth'] = self.enable_auth

        if self.method is not None:
            result['method'] = self.method

        if self.mock is not None:
            result['mock'] = self.mock.to_map()

        if self.name is not None:
            result['name'] = self.name

        if self.path is not None:
            result['path'] = self.path

        if self.request is not None:
            result['request'] = self.request.to_map()

        if self.response is not None:
            result['response'] = self.response.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authConfig') is not None:
            temp_model = main_models.AuthConfig()
            self.auth_config = temp_model.from_map(m.get('authConfig'))

        self.deploy_configs = []
        if m.get('deployConfigs') is not None:
            for k1 in m.get('deployConfigs'):
                temp_model = main_models.HttpApiDeployConfig()
                self.deploy_configs.append(temp_model.from_map(k1))

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('enableAuth') is not None:
            self.enable_auth = m.get('enableAuth')

        if m.get('method') is not None:
            self.method = m.get('method')

        if m.get('mock') is not None:
            temp_model = main_models.HttpApiMockContract()
            self.mock = temp_model.from_map(m.get('mock'))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('path') is not None:
            self.path = m.get('path')

        if m.get('request') is not None:
            temp_model = main_models.HttpApiRequestContract()
            self.request = temp_model.from_map(m.get('request'))

        if m.get('response') is not None:
            temp_model = main_models.HttpApiResponseContract()
            self.response = temp_model.from_map(m.get('response'))

        return self

