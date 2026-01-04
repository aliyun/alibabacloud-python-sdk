# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateFederatedCredentialProviderDescriptionRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        federated_credential_provider_id: str = None,
        instance_id: str = None,
    ):
        # 联邦凭证提供方描述
        self.description = description
        # 联邦凭证提供方ID
        # 
        # This parameter is required.
        self.federated_credential_provider_id = federated_credential_provider_id
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
        if self.description is not None:
            result['Description'] = self.description

        if self.federated_credential_provider_id is not None:
            result['FederatedCredentialProviderId'] = self.federated_credential_provider_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FederatedCredentialProviderId') is not None:
            self.federated_credential_provider_id = m.get('FederatedCredentialProviderId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

