# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class CreateKnowledgeBaseInput(DaraModel):
    def __init__(
        self,
        credential_name: str = None,
        description: str = None,
        knowledge_base_name: str = None,
        provider: str = None,
        provider_settings: Dict[str, Any] = None,
        retrieve_settings: Dict[str, Any] = None,
    ):
        self.credential_name = credential_name
        self.description = description
        # This parameter is required.
        self.knowledge_base_name = knowledge_base_name
        # This parameter is required.
        self.provider = provider
        # This parameter is required.
        self.provider_settings = provider_settings
        self.retrieve_settings = retrieve_settings

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.credential_name is not None:
            result['credentialName'] = self.credential_name

        if self.description is not None:
            result['description'] = self.description

        if self.knowledge_base_name is not None:
            result['knowledgeBaseName'] = self.knowledge_base_name

        if self.provider is not None:
            result['provider'] = self.provider

        if self.provider_settings is not None:
            result['providerSettings'] = self.provider_settings

        if self.retrieve_settings is not None:
            result['retrieveSettings'] = self.retrieve_settings

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('credentialName') is not None:
            self.credential_name = m.get('credentialName')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('knowledgeBaseName') is not None:
            self.knowledge_base_name = m.get('knowledgeBaseName')

        if m.get('provider') is not None:
            self.provider = m.get('provider')

        if m.get('providerSettings') is not None:
            self.provider_settings = m.get('providerSettings')

        if m.get('retrieveSettings') is not None:
            self.retrieve_settings = m.get('retrieveSettings')

        return self

