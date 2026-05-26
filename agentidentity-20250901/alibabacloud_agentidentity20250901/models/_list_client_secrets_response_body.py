# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentidentity20250901 import models as main_models
from darabonba.model import DaraModel

class ListClientSecretsResponseBody(DaraModel):
    def __init__(
        self,
        client_secrets: List[main_models.ListClientSecretsResponseBodyClientSecrets] = None,
        request_id: str = None,
    ):
        self.client_secrets = client_secrets
        self.request_id = request_id

    def validate(self):
        if self.client_secrets:
            for v1 in self.client_secrets:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ClientSecrets'] = []
        if self.client_secrets is not None:
            for k1 in self.client_secrets:
                result['ClientSecrets'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.client_secrets = []
        if m.get('ClientSecrets') is not None:
            for k1 in m.get('ClientSecrets'):
                temp_model = main_models.ListClientSecretsResponseBodyClientSecrets()
                self.client_secrets.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListClientSecretsResponseBodyClientSecrets(DaraModel):
    def __init__(
        self,
        client_id: str = None,
        client_name: str = None,
        client_secret_id: str = None,
        create_time: str = None,
        user_pool_name: str = None,
    ):
        self.client_id = client_id
        self.client_name = client_name
        self.client_secret_id = client_secret_id
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

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('UserPoolName') is not None:
            self.user_pool_name = m.get('UserPoolName')

        return self

