# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class UpdateDatasetDocumentRequest(DaraModel):
    def __init__(
        self,
        dataset_id: int = None,
        dataset_name: str = None,
        document: main_models.UpdateDatasetDocumentRequestDocument = None,
        workspace_id: str = None,
    ):
        self.dataset_id = dataset_id
        self.dataset_name = dataset_name
        # This parameter is required.
        self.document = document
        self.workspace_id = workspace_id

    def validate(self):
        if self.document:
            self.document.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id

        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name

        if self.document is not None:
            result['Document'] = self.document.to_map()

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')

        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')

        if m.get('Document') is not None:
            temp_model = main_models.UpdateDatasetDocumentRequestDocument()
            self.document = temp_model.from_map(m.get('Document'))

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class UpdateDatasetDocumentRequestDocument(DaraModel):
    def __init__(
        self,
        category_uuid: str = None,
        doc_id: str = None,
        doc_uuid: str = None,
        extend_1: str = None,
        extend_2: str = None,
        extend_3: str = None,
        tags: List[str] = None,
        title: str = None,
    ):
        self.category_uuid = category_uuid
        self.doc_id = doc_id
        self.doc_uuid = doc_uuid
        self.extend_1 = extend_1
        self.extend_2 = extend_2
        self.extend_3 = extend_3
        self.tags = tags
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_uuid is not None:
            result['CategoryUuid'] = self.category_uuid

        if self.doc_id is not None:
            result['DocId'] = self.doc_id

        if self.doc_uuid is not None:
            result['DocUuid'] = self.doc_uuid

        if self.extend_1 is not None:
            result['Extend1'] = self.extend_1

        if self.extend_2 is not None:
            result['Extend2'] = self.extend_2

        if self.extend_3 is not None:
            result['Extend3'] = self.extend_3

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryUuid') is not None:
            self.category_uuid = m.get('CategoryUuid')

        if m.get('DocId') is not None:
            self.doc_id = m.get('DocId')

        if m.get('DocUuid') is not None:
            self.doc_uuid = m.get('DocUuid')

        if m.get('Extend1') is not None:
            self.extend_1 = m.get('Extend1')

        if m.get('Extend2') is not None:
            self.extend_2 = m.get('Extend2')

        if m.get('Extend3') is not None:
            self.extend_3 = m.get('Extend3')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

