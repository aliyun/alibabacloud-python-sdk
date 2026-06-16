# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListFederatedCredentialProvidersRequest(DaraModel):
    def __init__(
        self,
        federated_credential_provider_name: str = None,
        federated_credential_provider_type: str = None,
        instance_id: str = None,
        max_results: int = None,
        next_token: str = None,
        previous_token: str = None,
    ):
        # The name of the federated credential provider.
        self.federated_credential_provider_name = federated_credential_provider_name
        # The type of the federated credential provider.
        self.federated_credential_provider_type = federated_credential_provider_type
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The maximum number of entries to return on each page.
        self.max_results = max_results
        # The token to retrieve the next page of results.
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
        if self.federated_credential_provider_name is not None:
            result['FederatedCredentialProviderName'] = self.federated_credential_provider_name

        if self.federated_credential_provider_type is not None:
            result['FederatedCredentialProviderType'] = self.federated_credential_provider_type

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
        if m.get('FederatedCredentialProviderName') is not None:
            self.federated_credential_provider_name = m.get('FederatedCredentialProviderName')

        if m.get('FederatedCredentialProviderType') is not None:
            self.federated_credential_provider_type = m.get('FederatedCredentialProviderType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PreviousToken') is not None:
            self.previous_token = m.get('PreviousToken')

        return self

