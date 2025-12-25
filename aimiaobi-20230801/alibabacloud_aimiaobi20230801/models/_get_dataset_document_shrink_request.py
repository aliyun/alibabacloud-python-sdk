# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDatasetDocumentShrinkRequest(DaraModel):
    def __init__(
        self,
        dataset_id: int = None,
        dataset_name: str = None,
        doc_id: str = None,
        doc_uuid: str = None,
        include_fields_shrink: str = None,
        workspace_id: str = None,
    ):
        self.dataset_id = dataset_id
        self.dataset_name = dataset_name
        self.doc_id = doc_id
        self.doc_uuid = doc_uuid
        self.include_fields_shrink = include_fields_shrink
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id

        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name

        if self.doc_id is not None:
            result['DocId'] = self.doc_id

        if self.doc_uuid is not None:
            result['DocUuid'] = self.doc_uuid

        if self.include_fields_shrink is not None:
            result['IncludeFields'] = self.include_fields_shrink

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')

        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')

        if m.get('DocId') is not None:
            self.doc_id = m.get('DocId')

        if m.get('DocUuid') is not None:
            self.doc_uuid = m.get('DocUuid')

        if m.get('IncludeFields') is not None:
            self.include_fields_shrink = m.get('IncludeFields')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

