# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListApplicationFederatedCredentialsRequest(DaraModel):
    def __init__(
        self,
        application_federated_credential_type: str = None,
        application_id: str = None,
        instance_id: str = None,
        max_results: int = None,
        next_token: str = None,
        previous_token: str = None,
    ):
        # The type of the application federated credential.
        self.application_federated_credential_type = application_federated_credential_type
        # The application ID.
        # 
        # This parameter is required.
        self.application_id = application_id
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The number of entries to return on each page.
        self.max_results = max_results
        # The query token.
        self.next_token = next_token
        # The token to retrieve the previous page of results.
        self.previous_token = previous_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_federated_credential_type is not None:
            result['ApplicationFederatedCredentialType'] = self.application_federated_credential_type

        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.previous_token is not None:
            result['PreviousToken'] = self.previous_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationFederatedCredentialType') is not None:
            self.application_federated_credential_type = m.get('ApplicationFederatedCredentialType')

        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PreviousToken') is not None:
            self.previous_token = m.get('PreviousToken')

        return self

