# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListCredentialsRequest(DaraModel):
    def __init__(
        self,
        credential_auth_type: str = None,
        credential_name: str = None,
        credential_source_type: str = None,
        enabled: bool = None,
        page_number: int = None,
        page_size: int = None,
        provider: str = None,
    ):
        # credentialAuthType
        self.credential_auth_type = credential_auth_type
        # credentialName
        self.credential_name = credential_name
        # credentialSourceType
        self.credential_source_type = credential_source_type
        self.enabled = enabled
        self.page_number = page_number
        self.page_size = page_size
        self.provider = provider

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.credential_auth_type is not None:
            result['credentialAuthType'] = self.credential_auth_type

        if self.credential_name is not None:
            result['credentialName'] = self.credential_name

        if self.credential_source_type is not None:
            result['credentialSourceType'] = self.credential_source_type

        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.provider is not None:
            result['provider'] = self.provider

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('credentialAuthType') is not None:
            self.credential_auth_type = m.get('credentialAuthType')

        if m.get('credentialName') is not None:
            self.credential_name = m.get('credentialName')

        if m.get('credentialSourceType') is not None:
            self.credential_source_type = m.get('credentialSourceType')

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('provider') is not None:
            self.provider = m.get('provider')

        return self

