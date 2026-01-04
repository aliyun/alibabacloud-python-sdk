# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateApplicationFederatedCredentialDescriptionRequest(DaraModel):
    def __init__(
        self,
        application_federated_credential_id: str = None,
        application_id: str = None,
        description: str = None,
        instance_id: str = None,
    ):
        # 应用联邦凭证Id
        # 
        # This parameter is required.
        self.application_federated_credential_id = application_federated_credential_id
        # IDaaS的应用资源ID。
        # 
        # This parameter is required.
        self.application_id = application_id
        # 联邦凭证描述
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
        if self.application_federated_credential_id is not None:
            result['ApplicationFederatedCredentialId'] = self.application_federated_credential_id

        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.description is not None:
            result['Description'] = self.description

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationFederatedCredentialId') is not None:
            self.application_federated_credential_id = m.get('ApplicationFederatedCredentialId')

        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

