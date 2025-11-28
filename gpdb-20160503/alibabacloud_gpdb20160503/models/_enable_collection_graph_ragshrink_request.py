# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EnableCollectionGraphRAGShrinkRequest(DaraModel):
    def __init__(
        self,
        collection: str = None,
        dbinstance_id: str = None,
        entity_types_shrink: str = None,
        llmmodel: str = None,
        language: str = None,
        manager_account: str = None,
        manager_account_password: str = None,
        namespace: str = None,
        namespace_password: str = None,
        owner_id: int = None,
        region_id: str = None,
        relationship_types_shrink: str = None,
    ):
        # The name of the document collection.
        # 
        # > You can call the [CreateDocumentCollection](https://help.aliyun.com/document_detail/2618448.html) operation to create a document collection and call the [ListDocumentCollections](https://help.aliyun.com/document_detail/2618452.html) operation to query a list of document collections.
        # 
        # This parameter is required.
        self.collection = collection
        # The cluster ID.
        # 
        # > You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) operation to query the information about all AnalyticDB for PostgreSQL instances within a region, including instance IDs.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The list of entity types.
        # 
        # > If the knowledge graph construction is enabled, this parameter is required.
        # 
        # This parameter is required.
        self.entity_types_shrink = entity_types_shrink
        # The name of the LLM model.
        # 
        # > Valid values:
        # 
        # *   knowledge-extract-standard: the default value.
        # 
        # *   knowledge-extract-mini
        # 
        # > This parameter takes effect only when the knowledge graph construction is enabled.
        self.llmmodel = llmmodel
        # The language used to build the knowledge graph. Valid values:
        # 
        # *   Simplified Chinese. The default value.
        # *   English.
        # 
        # > This parameter takes effect only when the knowledge graph construction is enabled.
        self.language = language
        # The name of the privileged database account that has the rds_superuser permission.
        # 
        # > You can call the [CreateAccount](https://help.aliyun.com/document_detail/2361789.html) operation to create an account.
        # 
        # This parameter is required.
        self.manager_account = manager_account
        # The password for the privileged database account.
        # 
        # This parameter is required.
        self.manager_account_password = manager_account_password
        # The name of the namespace. Default value: public.
        # 
        # > You can call the CreateNamespace operation to create a namespace and call the ListNamespaces operation to query a list of namespaces.
        self.namespace = namespace
        # The password of the namespace.
        # 
        # > The value of this parameter is specified by [CreateNamespace](https://help.aliyun.com/document_detail/2401495.html) operation.
        # 
        # This parameter is required.
        self.namespace_password = namespace_password
        self.owner_id = owner_id
        # The region ID of the cluster.
        # 
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/86912.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The list of relationship edge types.
        # 
        # > If the knowledge graph construction is enabled, this parameter is required.
        # 
        # This parameter is required.
        self.relationship_types_shrink = relationship_types_shrink

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

        if self.entity_types_shrink is not None:
            result['EntityTypes'] = self.entity_types_shrink

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

        if self.relationship_types_shrink is not None:
            result['RelationshipTypes'] = self.relationship_types_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Collection') is not None:
            self.collection = m.get('Collection')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('EntityTypes') is not None:
            self.entity_types_shrink = m.get('EntityTypes')

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
            self.relationship_types_shrink = m.get('RelationshipTypes')

        return self

