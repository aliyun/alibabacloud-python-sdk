# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateCredentialProviderDescriptionRequest(DaraModel):
    def __init__(
        self,
        credential_provider_id: str = None,
        description: str = None,
        instance_id: str = None,
    ):
        # 认证令牌提供商ID。
        # 
        # This parameter is required.
        self.credential_provider_id = credential_provider_id
        # 描述。
        self.description = description
        # IDaaS EIAM实例的ID。
        # 
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.credential_provider_id is not None:
            result['CredentialProviderId'] = self.credential_provider_id

        if self.description is not None:
            result['Description'] = self.description

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialProviderId') is not None:
            self.credential_provider_id = m.get('CredentialProviderId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

