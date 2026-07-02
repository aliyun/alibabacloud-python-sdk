# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_kms20160120 import models as main_models
from darabonba.model import DaraModel

class UpdateSecretRequest(DaraModel):
    def __init__(
        self,
        extended_config: main_models.UpdateSecretRequestExtendedConfig = None,
        description: str = None,
        secret_name: str = None,
    ):
        self.extended_config = extended_config
        # The description of the secret.
        self.description = description
        # The name of the secret.
        # 
        # This parameter is required.
        self.secret_name = secret_name

    def validate(self):
        if self.extended_config:
            self.extended_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extended_config is not None:
            result['ExtendedConfig'] = self.extended_config.to_map()

        if self.description is not None:
            result['Description'] = self.description

        if self.secret_name is not None:
            result['SecretName'] = self.secret_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtendedConfig') is not None:
            temp_model = main_models.UpdateSecretRequestExtendedConfig()
            self.extended_config = temp_model.from_map(m.get('ExtendedConfig'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')

        return self

class UpdateSecretRequestExtendedConfig(DaraModel):
    def __init__(
        self,
        custom_data: Dict[str, Any] = None,
    ):
        # The custom data in the extended configuration of the secret.
        # 
        # > *   If this parameter is specified, the existing extended configuration of the secret is updated.
        # > *   This parameter is unavailable for generic secrets.
        self.custom_data = custom_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_data is not None:
            result['CustomData'] = self.custom_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomData') is not None:
            self.custom_data = m.get('CustomData')

        return self

