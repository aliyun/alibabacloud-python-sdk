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
        # The list of files to be uploaded. You can specify 1 to 100 files.
        self.documents = documents
        # The validity period of the pre-signed URL in seconds. Default value: `3600`.
        self.expires_in = expires_in
        # The ID of the knowledge base. This parameter and datasetId are mutually exclusive. If both are specified, this parameter takes precedence.
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
        # The display name of the file. If not specified, the file name from Path is used by default.
        self.name = name
        # The **file name or relative path** for local upload scenarios. The path cannot start with `direct_upload/` or `uploaded/`, cannot contain empty segments, `.`, or `..`, and must be less than or equal to 1,024 bytes in length.
        self.path = path
        # The size of the file in bytes.
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

