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
    ):
        self.dedup = dedup
        self.documents = documents
        # 当前支持 LOCAL_UPLOAD；OSS_IMPORT 和 PUBLIC_URL 为后续导入方式预留。
        self.import_type = import_type
        self.knowledge_base_id = knowledge_base_id
        # 导入时批量设置到本批次所有知识数据的标签键值。Key 必须为知识库已定义标签字段；Value 支持 string、int64、float32、bool、list。
        self.meta_fields = meta_fields
        self.strategy_id = strategy_id
        self.ding_talk_configuration = ding_talk_configuration

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
        self.app_id = app_id
        self.app_password = app_password
        self.ding_doc_mcp_link = ding_doc_mcp_link
        self.ding_table_mcp_link = ding_table_mcp_link
        self.knowledge_id = knowledge_id
        self.knowledge_type = knowledge_type
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
        self.name = name
        # 本地上传时为预签名上传使用的批次相对路径；不同 ImportType 下含义由导入类型定义。
        self.path = path
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
        self.content_dedup = content_dedup
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

