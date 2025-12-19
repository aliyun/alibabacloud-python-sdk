# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetResourceAPIKeyRequest(DaraModel):
    def __init__(
        self,
        resource_credential_provider_name: str = None,
        workload_access_token: str = None,
    ):
        self.resource_credential_provider_name = resource_credential_provider_name
        self.workload_access_token = workload_access_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_credential_provider_name is not None:
            result['ResourceCredentialProviderName'] = self.resource_credential_provider_name

        if self.workload_access_token is not None:
            result['WorkloadAccessToken'] = self.workload_access_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceCredentialProviderName') is not None:
            self.resource_credential_provider_name = m.get('ResourceCredentialProviderName')

        if m.get('WorkloadAccessToken') is not None:
            self.workload_access_token = m.get('WorkloadAccessToken')

        return self

