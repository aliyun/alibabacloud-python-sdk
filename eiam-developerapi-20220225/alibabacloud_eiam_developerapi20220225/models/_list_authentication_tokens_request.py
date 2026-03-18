# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAuthenticationTokensRequest(DaraModel):
    def __init__(
        self,
        consumer_id: str = None,
        credential_provider_identifier: str = None,
        expired: bool = None,
        max_results: int = None,
        next_token: str = None,
        revoked: bool = None,
    ):
        # This parameter is required.
        self.consumer_id = consumer_id
        # This parameter is required.
        self.credential_provider_identifier = credential_provider_identifier
        self.expired = expired
        self.max_results = max_results
        self.next_token = next_token
        self.revoked = revoked

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.consumer_id is not None:
            result['consumerId'] = self.consumer_id

        if self.credential_provider_identifier is not None:
            result['credentialProviderIdentifier'] = self.credential_provider_identifier

        if self.expired is not None:
            result['expired'] = self.expired

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.revoked is not None:
            result['revoked'] = self.revoked

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('consumerId') is not None:
            self.consumer_id = m.get('consumerId')

        if m.get('credentialProviderIdentifier') is not None:
            self.credential_provider_identifier = m.get('credentialProviderIdentifier')

        if m.get('expired') is not None:
            self.expired = m.get('expired')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('revoked') is not None:
            self.revoked = m.get('revoked')

        return self

