# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class CreateSecretRequest(DaraModel):
    def __init__(
        self,
        namespace_id: str = None,
        secret_data: main_models.CreateSecretRequestSecretData = None,
        secret_name: str = None,
        secret_type: str = None,
    ):
        # The ID of the namespace where the Secret instance resides. If the namespace is the default namespace, you only need to specify RegionId, such as `cn-beijing`.
        # 
        # This parameter is required.
        self.namespace_id = namespace_id
        # The data of the Secret.
        # 
        # This parameter is required.
        self.secret_data = secret_data
        # The name of the Secret instance. The name can contain digits, letters, and underscores (_), and must start with a letter.
        # 
        # This parameter is required.
        self.secret_name = secret_name
        # The type of the Secret instance. Valid values:
        # 
        # - **kubernetes.io/dockerconfigjson**: stores the username and password of an image repository. It is used for authentication when pulling images during deployment.
        # 
        # This parameter is required.
        self.secret_type = secret_type

    def validate(self):
        if self.secret_data:
            self.secret_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.secret_data is not None:
            result['SecretData'] = self.secret_data.to_map()

        if self.secret_name is not None:
            result['SecretName'] = self.secret_name

        if self.secret_type is not None:
            result['SecretType'] = self.secret_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('SecretData') is not None:
            temp_model = main_models.CreateSecretRequestSecretData()
            self.secret_data = temp_model.from_map(m.get('SecretData'))

        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')

        if m.get('SecretType') is not None:
            self.secret_type = m.get('SecretType')

        return self

class CreateSecretRequestSecretData(DaraModel):
    def __init__(
        self,
        secret_data: str = None,
    ):
        # The key-value pair data of the Secret. This parameter is required. Format:
        # 
        # {"Data":"{\\"k1\\":\\"v1\\", \\"k2\\":\\"v2\\"}"}
        # 
        # k represents the key, and v represents the value.
        # 
        # This parameter is required.
        self.secret_data = secret_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.secret_data is not None:
            result['SecretData'] = self.secret_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecretData') is not None:
            self.secret_data = m.get('SecretData')

        return self

