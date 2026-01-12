# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pai_dlc20201203 import models as main_models
from darabonba.model import DaraModel

class CredentialConfig(DaraModel):
    def __init__(
        self,
        aliyun_env_role_key: str = None,
        credential_config_items: List[main_models.CredentialConfigItem] = None,
        enable_credential_inject: bool = None,
    ):
        self.aliyun_env_role_key = aliyun_env_role_key
        self.credential_config_items = credential_config_items
        self.enable_credential_inject = enable_credential_inject

    def validate(self):
        if self.credential_config_items:
            for v1 in self.credential_config_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_env_role_key is not None:
            result['AliyunEnvRoleKey'] = self.aliyun_env_role_key

        result['CredentialConfigItems'] = []
        if self.credential_config_items is not None:
            for k1 in self.credential_config_items:
                result['CredentialConfigItems'].append(k1.to_map() if k1 else None)

        if self.enable_credential_inject is not None:
            result['EnableCredentialInject'] = self.enable_credential_inject

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunEnvRoleKey') is not None:
            self.aliyun_env_role_key = m.get('AliyunEnvRoleKey')

        self.credential_config_items = []
        if m.get('CredentialConfigItems') is not None:
            for k1 in m.get('CredentialConfigItems'):
                temp_model = main_models.CredentialConfigItem()
                self.credential_config_items.append(temp_model.from_map(k1))

        if m.get('EnableCredentialInject') is not None:
            self.enable_credential_inject = m.get('EnableCredentialInject')

        return self

