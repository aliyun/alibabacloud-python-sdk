# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

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
        doc_id: str = None,
        doc_uuid: str = None,
        title: str = None,
    ):
        self.doc_id = doc_id
        self.doc_uuid = doc_uuid
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.doc_id is not None:
            result['DocId'] = self.doc_id

        if self.doc_uuid is not None:
            result['DocUuid'] = self.doc_uuid

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DocId') is not None:
            self.doc_id = m.get('DocId')

        if m.get('DocUuid') is not None:
            self.doc_uuid = m.get('DocUuid')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

