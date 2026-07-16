# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EnableApplicationFederatedCredentialRequest(DaraModel):
    def __init__(
        self,
        application_federated_credential_id: str = None,
        application_id: str = None,
        instance_id: str = None,
    ):
        # The ID of the application federated credential.
        # 
        # This parameter is required.
        self.application_federated_credential_id = application_federated_credential_id
        # The ID of the application.
        # 
        # This parameter is required.
        self.application_id = application_id
        # The ID of the instance.
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

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationFederatedCredentialId') is not None:
            self.application_federated_credential_id = m.get('ApplicationFederatedCredentialId')

        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

