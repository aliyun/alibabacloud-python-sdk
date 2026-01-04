# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class ObtainApplicationClientSecretResponseBody(DaraModel):
    def __init__(
        self,
        application_client_secret: main_models.ObtainApplicationClientSecretResponseBodyApplicationClientSecret = None,
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
            temp_model = main_models.ObtainApplicationClientSecretResponseBodyApplicationClientSecret()
            self.application_client_secret = temp_model.from_map(m.get('ApplicationClientSecret'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ObtainApplicationClientSecretResponseBodyApplicationClientSecret(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        client_id: str = None,
        client_secret: str = None,
        expiration_time: int = None,
        instance_id: str = None,
        last_used_time: int = None,
        secret_id: str = None,
        status: str = None,
    ):
        # The ID of the application whose client key you want to query.
        self.application_id = application_id
        # The client ID of the application.
        self.client_id = client_id
        # The client key secret of the application.
        self.client_secret = client_secret
        self.expiration_time = expiration_time
        # The ID of the instance.
        self.instance_id = instance_id
        # The time when the client key was last used. The value is a UNIX timestamp. Unit: milliseconds.
        self.last_used_time = last_used_time
        # The client key ID of the application.
        self.secret_id = secret_id
        # The status of the client key. Valid values:
        # 
        # *   Enabled: The client key is enabled.
        # *   Disabled: The client key is disabled.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.client_secret is not None:
            result['ClientSecret'] = self.client_secret

        if self.expiration_time is not None:
            result['ExpirationTime'] = self.expiration_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.last_used_time is not None:
            result['LastUsedTime'] = self.last_used_time

        if self.secret_id is not None:
            result['SecretId'] = self.secret_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('ClientSecret') is not None:
            self.client_secret = m.get('ClientSecret')

        if m.get('ExpirationTime') is not None:
            self.expiration_time = m.get('ExpirationTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LastUsedTime') is not None:
            self.last_used_time = m.get('LastUsedTime')

        if m.get('SecretId') is not None:
            self.secret_id = m.get('SecretId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

