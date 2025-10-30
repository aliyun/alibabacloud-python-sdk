# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class EnableCollectionGraphRAGRequest(DaraModel):
    def __init__(
        self,
        collection: str = None,
        dbinstance_id: str = None,
        entity_types: List[str] = None,
        llmmodel: str = None,
        language: str = None,
        manager_account: str = None,
        manager_account_password: str = None,
        namespace: str = None,
        namespace_password: str = None,
        owner_id: int = None,
        region_id: str = None,
        relationship_types: List[str] = None,
    ):
        # This parameter is required.
        self.collection = collection
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # This parameter is required.
        self.entity_types = entity_types
        self.llmmodel = llmmodel
        self.language = language
        # This parameter is required.
        self.manager_account = manager_account
        # This parameter is required.
        self.manager_account_password = manager_account_password
        self.namespace = namespace
        # This parameter is required.
        self.namespace_password = namespace_password
        self.owner_id = owner_id
        # This parameter is required.
        self.region_id = region_id
        # This parameter is required.
        self.relationship_types = relationship_types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.collection is not None:
            result['Collection'] = self.collection

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.entity_types is not None:
            result['EntityTypes'] = self.entity_types

        if self.llmmodel is not None:
            result['LLMModel'] = self.llmmodel

        if self.language is not None:
            result['Language'] = self.language

        if self.manager_account is not None:
            result['ManagerAccount'] = self.manager_account

        if self.manager_account_password is not None:
            result['ManagerAccountPassword'] = self.manager_account_password

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.namespace_password is not None:
            result['NamespacePassword'] = self.namespace_password

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.relationship_types is not None:
            result['RelationshipTypes'] = self.relationship_types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Collection') is not None:
            self.collection = m.get('Collection')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('EntityTypes') is not None:
            self.entity_types = m.get('EntityTypes')

        if m.get('LLMModel') is not None:
            self.llmmodel = m.get('LLMModel')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('ManagerAccount') is not None:
            self.manager_account = m.get('ManagerAccount')

        if m.get('ManagerAccountPassword') is not None:
            self.manager_account_password = m.get('ManagerAccountPassword')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('NamespacePassword') is not None:
            self.namespace_password = m.get('NamespacePassword')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RelationshipTypes') is not None:
            self.relationship_types = m.get('RelationshipTypes')

        return self

