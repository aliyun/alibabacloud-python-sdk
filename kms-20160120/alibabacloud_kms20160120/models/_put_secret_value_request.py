# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PutSecretValueRequest(DaraModel):
    def __init__(
        self,
        secret_data: str = None,
        secret_data_type: str = None,
        secret_name: str = None,
        version_id: str = None,
        version_stages: str = None,
    ):
        # The secret value. The value is encrypted and stored in the specified new version.
        # 
        # This parameter is required.
        self.secret_data = secret_data
        # The type of the secret value. Valid values:
        # 
        # - text (default)
        # 
        # - binary
        self.secret_data_type = secret_data_type
        # The name or Alibaba Cloud Resource Name (ARN) of the secret.
        # 
        # > When you access a secret in another Alibaba Cloud account, you must specify the ARN of the secret. The ARN of a secret is in the format of `acs:kms:${region}:${account}:secret/${secret-name}`.
        # 
        # This parameter is required.
        self.secret_name = secret_name
        # The version number of the secret. The value must be unique in the secret.
        # 
        # This parameter is required.
        self.version_id = version_id
        # The stage labels that are used to mark the new version. If you do not specify this parameter, KMS marks the new version with ACSCurrent.
        self.version_stages = version_stages

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.secret_data is not None:
            result['SecretData'] = self.secret_data

        if self.secret_data_type is not None:
            result['SecretDataType'] = self.secret_data_type

        if self.secret_name is not None:
            result['SecretName'] = self.secret_name

        if self.version_id is not None:
            result['VersionId'] = self.version_id

        if self.version_stages is not None:
            result['VersionStages'] = self.version_stages

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecretData') is not None:
            self.secret_data = m.get('SecretData')

        if m.get('SecretDataType') is not None:
            self.secret_data_type = m.get('SecretDataType')

        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')

        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')

        if m.get('VersionStages') is not None:
            self.version_stages = m.get('VersionStages')

        return self

