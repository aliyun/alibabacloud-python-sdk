# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_milvusknowledgebase20260604 import models as main_models
from darabonba.model import DaraModel

class AddDocumentsRequest(DaraModel):
    def __init__(
        self,
        dedup: main_models.AddDocumentsRequestDedup = None,
        documents: List[main_models.AddDocumentsRequestDocuments] = None,
        import_type: str = None,
        knowledge_base_id: str = None,
        meta_fields: Any = None,
        strategy_id: str = None,
        ding_talk_configuration: main_models.AddDocumentsRequestDingTalkConfiguration = None,
        parent_id: str = None,
    ):
        # The deduplication configuration.
        self.dedup = dedup
        # The list of documents.
        self.documents = documents
        # The import type.
        self.import_type = import_type
        # The ID of the knowledge base.
        self.knowledge_base_id = knowledge_base_id
        # The batch label configuration. The key must be a label field defined in the knowledge base. The value supports string, int64, float32, bool, and list types.
        self.meta_fields = meta_fields
        # The ID of the processing strategy.
        self.strategy_id = strategy_id
        # Not supported. Ignore this parameter.
        self.ding_talk_configuration = ding_talk_configuration
        # Defaults to root when omitted.
        self.parent_id = parent_id

    def validate(self):
        if self.dedup:
            self.dedup.validate()
        if self.documents:
            for v1 in self.documents:
                 if v1:
                    v1.validate()
        if self.ding_talk_configuration:
            self.ding_talk_configuration.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dedup is not None:
            result['Dedup'] = self.dedup.to_map()

        result['Documents'] = []
        if self.documents is not None:
            for k1 in self.documents:
                result['Documents'].append(k1.to_map() if k1 else None)

        if self.import_type is not None:
            result['ImportType'] = self.import_type

        if self.knowledge_base_id is not None:
            result['KnowledgeBaseId'] = self.knowledge_base_id

        if self.meta_fields is not None:
            result['MetaFields'] = self.meta_fields

        if self.strategy_id is not None:
            result['StrategyId'] = self.strategy_id

        if self.ding_talk_configuration is not None:
            result['dingTalkConfiguration'] = self.ding_talk_configuration.to_map()

        if self.parent_id is not None:
            result['parentId'] = self.parent_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dedup') is not None:
            temp_model = main_models.AddDocumentsRequestDedup()
            self.dedup = temp_model.from_map(m.get('Dedup'))

        self.documents = []
        if m.get('Documents') is not None:
            for k1 in m.get('Documents'):
                temp_model = main_models.AddDocumentsRequestDocuments()
                self.documents.append(temp_model.from_map(k1))

        if m.get('ImportType') is not None:
            self.import_type = m.get('ImportType')

        if m.get('KnowledgeBaseId') is not None:
            self.knowledge_base_id = m.get('KnowledgeBaseId')

        if m.get('MetaFields') is not None:
            self.meta_fields = m.get('MetaFields')

        if m.get('StrategyId') is not None:
            self.strategy_id = m.get('StrategyId')

        if m.get('dingTalkConfiguration') is not None:
            temp_model = main_models.AddDocumentsRequestDingTalkConfiguration()
            self.ding_talk_configuration = temp_model.from_map(m.get('dingTalkConfiguration'))

        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')

        return self

class AddDocumentsRequestDingTalkConfiguration(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_password: str = None,
        ding_doc_mcp_link: str = None,
        ding_table_mcp_link: str = None,
        knowledge_id: str = None,
        knowledge_type: str = None,
        user_id: str = None,
    ):
        # Not supported. Ignore this parameter.
        self.app_id = app_id
        # Not supported. Ignore this parameter.
        self.app_password = app_password
        # Not supported. Ignore this parameter.
        self.ding_doc_mcp_link = ding_doc_mcp_link
        # Not supported. Ignore this parameter.
        self.ding_table_mcp_link = ding_table_mcp_link
        # Not supported. Ignore this parameter.
        self.knowledge_id = knowledge_id
        # Not supported. Ignore this parameter.
        self.knowledge_type = knowledge_type
        # Not supported. Ignore this parameter.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['appId'] = self.app_id

        if self.app_password is not None:
            result['appPassword'] = self.app_password

        if self.ding_doc_mcp_link is not None:
            result['dingDocMcpLink'] = self.ding_doc_mcp_link

        if self.ding_table_mcp_link is not None:
            result['dingTableMcpLink'] = self.ding_table_mcp_link

        if self.knowledge_id is not None:
            result['knowledgeId'] = self.knowledge_id

        if self.knowledge_type is not None:
            result['knowledgeType'] = self.knowledge_type

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')

        if m.get('appPassword') is not None:
            self.app_password = m.get('appPassword')

        if m.get('dingDocMcpLink') is not None:
            self.ding_doc_mcp_link = m.get('dingDocMcpLink')

        if m.get('dingTableMcpLink') is not None:
            self.ding_table_mcp_link = m.get('dingTableMcpLink')

        if m.get('knowledgeId') is not None:
            self.knowledge_id = m.get('knowledgeId')

        if m.get('knowledgeType') is not None:
            self.knowledge_type = m.get('knowledgeType')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

class AddDocumentsRequestDocuments(DaraModel):
    def __init__(
        self,
        name: str = None,
        path: str = None,
        size: int = None,
    ):
        # The name of the document.
        self.name = name
        # The document path. This is the file name or relative path used during upload, which must be consistent with the pre-signed request.
        self.path = path
        # The size of the file.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.path is not None:
            result['Path'] = self.path

        if self.size is not None:
            result['Size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        return self



class AddDocumentsRequestDedup(DaraModel):
    def __init__(
        self,
        content_dedup: bool = None,
        doc_name_dedup: bool = None,
    ):
        # Specifies whether to enable content deduplication.
        self.content_dedup = content_dedup
        # Specifies whether to enable document name deduplication.
        self.doc_name_dedup = doc_name_dedup

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content_dedup is not None:
            result['ContentDedup'] = self.content_dedup

        if self.doc_name_dedup is not None:
            result['DocNameDedup'] = self.doc_name_dedup

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContentDedup') is not None:
            self.content_dedup = m.get('ContentDedup')

        if m.get('DocNameDedup') is not None:
            self.doc_name_dedup = m.get('DocNameDedup')

        return self

