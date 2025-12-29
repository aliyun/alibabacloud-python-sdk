# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class UpdateSecretRequest(DaraModel):
    def __init__(
        self,
        namespace_id: str = None,
        secret_data: main_models.UpdateSecretRequestSecretData = None,
        secret_id: int = None,
    ):
        # The ID of the namespace where the Secret resides. If the namespace is the default namespace, you need to only enter the region ID, such as `cn-beijing`.
        # 
        # This parameter is required.
        self.namespace_id = namespace_id
        # The Secret data.
        # 
        # This parameter is required.
        self.secret_data = secret_data
        # This parameter is required.
        self.secret_id = secret_id

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

        if self.secret_id is not None:
            result['SecretId'] = self.secret_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('SecretData') is not None:
            temp_model = main_models.UpdateSecretRequestSecretData()
            self.secret_data = temp_model.from_map(m.get('SecretData'))

        if m.get('SecretId') is not None:
            self.secret_id = m.get('SecretId')

        return self

class UpdateSecretRequestSecretData(DaraModel):
    def __init__(
        self,
        secret_data: str = None,
    ):
        # The information about the key-value pairs of the Secret. This parameter is required. The following formats are supported:
        # 
        # {"Data":"{"k1":"v1", "k2":"v2"}"}
        # 
        # k specifies a key and v specifies a value. For more information, see [Manage a Kubernetes Secret](https://help.aliyun.com/document_detail/463383.html).
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

