# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDatasetDocumentsShrinkRequest(DaraModel):
    def __init__(
        self,
        dataset_description: str = None,
        dataset_id: int = None,
        dataset_name: str = None,
        doc_type: str = None,
        exclude_fields_shrink: str = None,
        include_fields_shrink: str = None,
        page_number: int = None,
        page_size: int = None,
        query: str = None,
        status: int = None,
        workspace_id: str = None,
    ):
        self.dataset_description = dataset_description
        self.dataset_id = dataset_id
        self.dataset_name = dataset_name
        self.doc_type = doc_type
        self.exclude_fields_shrink = exclude_fields_shrink
        self.include_fields_shrink = include_fields_shrink
        self.page_number = page_number
        self.page_size = page_size
        self.query = query
        self.status = status
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dataset_description is not None:
            result['DatasetDescription'] = self.dataset_description

        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id

        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name

        if self.doc_type is not None:
            result['DocType'] = self.doc_type

        if self.exclude_fields_shrink is not None:
            result['ExcludeFields'] = self.exclude_fields_shrink

        if self.include_fields_shrink is not None:
            result['IncludeFields'] = self.include_fields_shrink

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.query is not None:
            result['Query'] = self.query

        if self.status is not None:
            result['Status'] = self.status

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetDescription') is not None:
            self.dataset_description = m.get('DatasetDescription')

        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')

        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')

        if m.get('DocType') is not None:
            self.doc_type = m.get('DocType')

        if m.get('ExcludeFields') is not None:
            self.exclude_fields_shrink = m.get('ExcludeFields')

        if m.get('IncludeFields') is not None:
            self.include_fields_shrink = m.get('IncludeFields')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

