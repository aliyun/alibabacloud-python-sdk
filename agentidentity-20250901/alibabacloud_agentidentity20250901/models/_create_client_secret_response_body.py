# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentidentity20250901 import models as main_models
from darabonba.model import DaraModel

class CreateClientSecretResponseBody(DaraModel):
    def __init__(
        self,
        client_secret: main_models.CreateClientSecretResponseBodyClientSecret = None,
        request_id: str = None,
    ):
        self.client_secret = client_secret
        self.request_id = request_id

    def validate(self):
        if self.client_secret:
            self.client_secret.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_secret is not None:
            result['ClientSecret'] = self.client_secret.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientSecret') is not None:
            temp_model = main_models.CreateClientSecretResponseBodyClientSecret()
            self.client_secret = temp_model.from_map(m.get('ClientSecret'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateClientSecretResponseBodyClientSecret(DaraModel):
    def __init__(
        self,
        client_id: str = None,
        client_name: str = None,
        client_secret_id: str = None,
        client_secret_value: str = None,
        create_time: str = None,
        user_pool_name: str = None,
    ):
        self.client_id = client_id
        self.client_name = client_name
        self.client_secret_id = client_secret_id
        self.client_secret_value = client_secret_value
        self.create_time = create_time
        self.user_pool_name = user_pool_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.client_name is not None:
            result['ClientName'] = self.client_name

        if self.client_secret_id is not None:
            result['ClientSecretId'] = self.client_secret_id

        if self.client_secret_value is not None:
            result['ClientSecretValue'] = self.client_secret_value

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.user_pool_name is not None:
            result['UserPoolName'] = self.user_pool_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('ClientName') is not None:
            self.client_name = m.get('ClientName')

        if m.get('ClientSecretId') is not None:
            self.client_secret_id = m.get('ClientSecretId')

        if m.get('ClientSecretValue') is not None:
            self.client_secret_value = m.get('ClientSecretValue')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('UserPoolName') is not None:
            self.user_pool_name = m.get('UserPoolName')

        return self

