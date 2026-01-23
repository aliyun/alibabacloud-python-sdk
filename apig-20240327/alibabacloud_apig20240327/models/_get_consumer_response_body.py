# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class GetConsumerResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetConsumerResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The status code.
        self.code = code
        # The response payload.
        self.data = data
        # The status message.
        self.message = message
        # The request ID.
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
            temp_model = main_models.GetConsumerResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetConsumerResponseBodyData(DaraModel):
    def __init__(
        self,
        ak_sk_identity_configs: List[main_models.AkSkIdentityConfig] = None,
        api_key_identity_config: main_models.ApiKeyIdentityConfig = None,
        consumer_id: str = None,
        create_timestamp: int = None,
        deploy_status: str = None,
        description: str = None,
        enable: bool = None,
        jwt_identity_config: main_models.JwtIdentityConfig = None,
        name: str = None,
        update_timestamp: int = None,
    ):
        # The AK/SK authentication configurations.
        self.ak_sk_identity_configs = ak_sk_identity_configs
        # The API key authentication configurations.
        self.api_key_identity_config = api_key_identity_config
        # The consumer ID.
        self.consumer_id = consumer_id
        # The creation timestamp.
        self.create_timestamp = create_timestamp
        # The publishing status of the API in the current environment.
        self.deploy_status = deploy_status
        # The description.
        self.description = description
        # Indicates if enabled.
        self.enable = enable
        # The JWT authentication configurations.
        self.jwt_identity_config = jwt_identity_config
        # The consumer name.
        self.name = name
        # The last update timestamp.
        self.update_timestamp = update_timestamp

    def validate(self):
        if self.ak_sk_identity_configs:
            for v1 in self.ak_sk_identity_configs:
                 if v1:
                    v1.validate()
        if self.api_key_identity_config:
            self.api_key_identity_config.validate()
        if self.jwt_identity_config:
            self.jwt_identity_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['akSkIdentityConfigs'] = []
        if self.ak_sk_identity_configs is not None:
            for k1 in self.ak_sk_identity_configs:
                result['akSkIdentityConfigs'].append(k1.to_map() if k1 else None)

        if self.api_key_identity_config is not None:
            result['apiKeyIdentityConfig'] = self.api_key_identity_config.to_map()

        if self.consumer_id is not None:
            result['consumerId'] = self.consumer_id

        if self.create_timestamp is not None:
            result['createTimestamp'] = self.create_timestamp

        if self.deploy_status is not None:
            result['deployStatus'] = self.deploy_status

        if self.description is not None:
            result['description'] = self.description

        if self.enable is not None:
            result['enable'] = self.enable

        if self.jwt_identity_config is not None:
            result['jwtIdentityConfig'] = self.jwt_identity_config.to_map()

        if self.name is not None:
            result['name'] = self.name

        if self.update_timestamp is not None:
            result['updateTimestamp'] = self.update_timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ak_sk_identity_configs = []
        if m.get('akSkIdentityConfigs') is not None:
            for k1 in m.get('akSkIdentityConfigs'):
                temp_model = main_models.AkSkIdentityConfig()
                self.ak_sk_identity_configs.append(temp_model.from_map(k1))

        if m.get('apiKeyIdentityConfig') is not None:
            temp_model = main_models.ApiKeyIdentityConfig()
            self.api_key_identity_config = temp_model.from_map(m.get('apiKeyIdentityConfig'))

        if m.get('consumerId') is not None:
            self.consumer_id = m.get('consumerId')

        if m.get('createTimestamp') is not None:
            self.create_timestamp = m.get('createTimestamp')

        if m.get('deployStatus') is not None:
            self.deploy_status = m.get('deployStatus')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('enable') is not None:
            self.enable = m.get('enable')

        if m.get('jwtIdentityConfig') is not None:
            temp_model = main_models.JwtIdentityConfig()
            self.jwt_identity_config = temp_model.from_map(m.get('jwtIdentityConfig'))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('updateTimestamp') is not None:
            self.update_timestamp = m.get('updateTimestamp')

        return self

