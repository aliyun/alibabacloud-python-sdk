# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RevokeAuthenticationTokenByConsumerRequest(DaraModel):
    def __init__(
        self,
        consumer_id: str = None,
        credential_provider_identifier: str = None,
    ):
        # This parameter is required.
        self.consumer_id = consumer_id
        # This parameter is required.
        self.credential_provider_identifier = credential_provider_identifier

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('consumerId') is not None:
            self.consumer_id = m.get('consumerId')

        if m.get('credentialProviderIdentifier') is not None:
            self.credential_provider_identifier = m.get('credentialProviderIdentifier')

        return self

