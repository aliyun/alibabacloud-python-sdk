# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class CreateApplicationClientSecretResponseBody(DaraModel):
    def __init__(
        self,
        application_client_secret: main_models.CreateApplicationClientSecretResponseBodyApplicationClientSecret = None,
        request_id: str = None,
    ):
        # The information about the client key.
        self.application_client_secret = application_client_secret
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.application_client_secret:
            self.application_client_secret.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_client_secret is not None:
            result['ApplicationClientSecret'] = self.application_client_secret.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationClientSecret') is not None:
            temp_model = main_models.CreateApplicationClientSecretResponseBodyApplicationClientSecret()
            self.application_client_secret = temp_model.from_map(m.get('ApplicationClientSecret'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateApplicationClientSecretResponseBodyApplicationClientSecret(DaraModel):
    def __init__(
        self,
        client_id: str = None,
        client_secret: str = None,
        secret_id: str = None,
    ):
        # The client ID of the application.
        self.client_id = client_id
        # The client key secret of the application.
        self.client_secret = client_secret
        # The client key ID of the application.
        self.secret_id = secret_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.client_secret is not None:
            result['ClientSecret'] = self.client_secret

        if self.secret_id is not None:
            result['SecretId'] = self.secret_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('ClientSecret') is not None:
            self.client_secret = m.get('ClientSecret')

        if m.get('SecretId') is not None:
            self.secret_id = m.get('SecretId')

        return self

