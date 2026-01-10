# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CredentialListItem(DaraModel):
    def __init__(
        self,
        created_at: str = None,
        credential_auth_type: str = None,
        credential_id: str = None,
        credential_name: str = None,
        credential_source_type: str = None,
        enabled: bool = None,
        related_resource_count: int = None,
        updated_at: str = None,
    ):
        self.created_at = created_at
        self.credential_auth_type = credential_auth_type
        self.credential_id = credential_id
        self.credential_name = credential_name
        self.credential_source_type = credential_source_type
        self.enabled = enabled
        self.related_resource_count = related_resource_count
        self.updated_at = updated_at

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.credential_auth_type is not None:
            result['credentialAuthType'] = self.credential_auth_type

        if self.credential_id is not None:
            result['credentialId'] = self.credential_id

        if self.credential_name is not None:
            result['credentialName'] = self.credential_name

        if self.credential_source_type is not None:
            result['credentialSourceType'] = self.credential_source_type

        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.related_resource_count is not None:
            result['relatedResourceCount'] = self.related_resource_count

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('credentialAuthType') is not None:
            self.credential_auth_type = m.get('credentialAuthType')

        if m.get('credentialId') is not None:
            self.credential_id = m.get('credentialId')

        if m.get('credentialName') is not None:
            self.credential_name = m.get('credentialName')

        if m.get('credentialSourceType') is not None:
            self.credential_source_type = m.get('credentialSourceType')

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('relatedResourceCount') is not None:
            self.related_resource_count = m.get('relatedResourceCount')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        return self

