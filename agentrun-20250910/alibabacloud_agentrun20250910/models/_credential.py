# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class Credential(DaraModel):
    def __init__(
        self,
        created_at: str = None,
        credential_auth_type: str = None,
        credential_id: str = None,
        credential_name: str = None,
        credential_public_config: Dict[str, str] = None,
        credential_secret: str = None,
        credential_source_type: str = None,
        description: str = None,
        enabled: bool = None,
        related_resources: List[main_models.RelatedResource] = None,
        updated_at: str = None,
    ):
        self.created_at = created_at
        self.credential_auth_type = credential_auth_type
        self.credential_id = credential_id
        self.credential_name = credential_name
        self.credential_public_config = credential_public_config
        self.credential_secret = credential_secret
        self.credential_source_type = credential_source_type
        self.description = description
        self.enabled = enabled
        self.related_resources = related_resources
        self.updated_at = updated_at

    def validate(self):
        if self.related_resources:
            for v1 in self.related_resources:
                 if v1:
                    v1.validate()

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

        if self.credential_public_config is not None:
            result['credentialPublicConfig'] = self.credential_public_config

        if self.credential_secret is not None:
            result['credentialSecret'] = self.credential_secret

        if self.credential_source_type is not None:
            result['credentialSourceType'] = self.credential_source_type

        if self.description is not None:
            result['description'] = self.description

        if self.enabled is not None:
            result['enabled'] = self.enabled

        result['relatedResources'] = []
        if self.related_resources is not None:
            for k1 in self.related_resources:
                result['relatedResources'].append(k1.to_map() if k1 else None)

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

        if m.get('credentialPublicConfig') is not None:
            self.credential_public_config = m.get('credentialPublicConfig')

        if m.get('credentialSecret') is not None:
            self.credential_secret = m.get('credentialSecret')

        if m.get('credentialSourceType') is not None:
            self.credential_source_type = m.get('credentialSourceType')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        self.related_resources = []
        if m.get('relatedResources') is not None:
            for k1 in m.get('relatedResources'):
                temp_model = main_models.RelatedResource()
                self.related_resources.append(temp_model.from_map(k1))

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        return self

