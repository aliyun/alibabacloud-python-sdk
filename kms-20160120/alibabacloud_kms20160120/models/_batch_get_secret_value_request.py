# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_kms20160120 import models as main_models
from darabonba.model import DaraModel

class BatchGetSecretValueRequest(DaraModel):
    def __init__(
        self,
        secrets_list: List[main_models.BatchGetSecretValueRequestSecretsList] = None,
    ):
        # The list of secret information. You can query up to 20 different secrets at a time.
        self.secrets_list = secrets_list

    def validate(self):
        if self.secrets_list:
            for v1 in self.secrets_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SecretsList'] = []
        if self.secrets_list is not None:
            for k1 in self.secrets_list:
                result['SecretsList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.secrets_list = []
        if m.get('SecretsList') is not None:
            for k1 in m.get('SecretsList'):
                temp_model = main_models.BatchGetSecretValueRequestSecretsList()
                self.secrets_list.append(temp_model.from_map(k1))

        return self



class BatchGetSecretValueRequestSecretsList(DaraModel):
    def __init__(
        self,
        fetch_extended_config: str = None,
        secret_name: str = None,
        version_id: str = None,
        version_stage: str = None,
    ):
        # Specifies whether to retrieve the extended configuration of the secret. Valid values:
        # 
        # - true: Retrieve the extended configuration.
        # - false (default): Do not retrieve the extended configuration.
        # 
        # > Generic secrets do not support extended configurations. This parameter is ignored for generic secrets.
        self.fetch_extended_config = fetch_extended_config
        # The secret name or secret Alibaba Cloud Resource Name (ARN).
        # >When accessing a secret in another Alibaba Cloud account, you must specify the secret ARN. The format of a secret ARN is `acs:kms:${region}:${account}:secret/${secret-name}`.
        # 
        # This parameter is required.
        self.secret_name = secret_name
        # The version number.
        self.version_id = version_id
        # The version stage. Default value: ACSCurrent.
        # 
        # If you specify this parameter, the secret value of the specified version stage is returned. If you do not specify this parameter, the secret value of the ACSCurrent version stage is returned.
        # > For ApsaraDB RDS secrets, PolarDB secrets, Redis/Tair secrets, RAM secrets, and ECS secrets, you can retrieve only the secret values of the ACSPrevious and ACSCurrent versions.
        self.version_stage = version_stage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fetch_extended_config is not None:
            result['FetchExtendedConfig'] = self.fetch_extended_config

        if self.secret_name is not None:
            result['SecretName'] = self.secret_name

        if self.version_id is not None:
            result['VersionId'] = self.version_id

        if self.version_stage is not None:
            result['VersionStage'] = self.version_stage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FetchExtendedConfig') is not None:
            self.fetch_extended_config = m.get('FetchExtendedConfig')

        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')

        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')

        if m.get('VersionStage') is not None:
            self.version_stage = m.get('VersionStage')

        return self

