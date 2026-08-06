# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_milvusknowledgebase20260604 import models as main_models
from darabonba.model import DaraModel

class GetKnowledgeBasePreSignedUrlRequest(DaraModel):
    def __init__(
        self,
        documents: List[main_models.GetKnowledgeBasePreSignedUrlRequestDocuments] = None,
        expires_in: int = None,
        knowledge_base_id: str = None,
    ):
        self.documents = documents
        self.expires_in = expires_in
        self.knowledge_base_id = knowledge_base_id

    def validate(self):
        if self.documents:
            for v1 in self.documents:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Documents'] = []
        if self.documents is not None:
            for k1 in self.documents:
                result['Documents'].append(k1.to_map() if k1 else None)

        if self.expires_in is not None:
            result['ExpiresIn'] = self.expires_in

        if self.knowledge_base_id is not None:
            result['KnowledgeBaseId'] = self.knowledge_base_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.documents = []
        if m.get('Documents') is not None:
            for k1 in m.get('Documents'):
                temp_model = main_models.GetKnowledgeBasePreSignedUrlRequestDocuments()
                self.documents.append(temp_model.from_map(k1))

        if m.get('ExpiresIn') is not None:
            self.expires_in = m.get('ExpiresIn')

        if m.get('KnowledgeBaseId') is not None:
            self.knowledge_base_id = m.get('KnowledgeBaseId')

        return self

class GetKnowledgeBasePreSignedUrlRequestDocuments(DaraModel):
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

