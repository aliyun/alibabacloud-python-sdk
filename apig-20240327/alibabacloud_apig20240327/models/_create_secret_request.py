# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class CreateSecretRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        gateway_type: str = None,
        kms_config: main_models.KMSConfig = None,
        name: str = None,
        secret_data: str = None,
        secret_source: str = None,
    ):
        # The description of the key.
        self.description = description
        # The type of the gateway.
        self.gateway_type = gateway_type
        # The key configuration information of KMS.
        self.kms_config = kms_config
        # The key name. It can be up to 64 characters in length and can contain letters, digits, and underscores (_).
        self.name = name
        # The value of the KMS credential.
        self.secret_data = secret_data
        # The source of the key.
        self.secret_source = secret_source

    def validate(self):
        if self.kms_config:
            self.kms_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.gateway_type is not None:
            result['gatewayType'] = self.gateway_type

        if self.kms_config is not None:
            result['kmsConfig'] = self.kms_config.to_map()

        if self.name is not None:
            result['name'] = self.name

        if self.secret_data is not None:
            result['secretData'] = self.secret_data

        if self.secret_source is not None:
            result['secretSource'] = self.secret_source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('gatewayType') is not None:
            self.gateway_type = m.get('gatewayType')

        if m.get('kmsConfig') is not None:
            temp_model = main_models.KMSConfig()
            self.kms_config = temp_model.from_map(m.get('kmsConfig'))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('secretData') is not None:
            self.secret_data = m.get('secretData')

        if m.get('secretSource') is not None:
            self.secret_source = m.get('secretSource')

        return self

