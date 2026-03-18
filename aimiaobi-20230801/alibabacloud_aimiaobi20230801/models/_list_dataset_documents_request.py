# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListDatasetDocumentsRequest(DaraModel):
    def __init__(
        self,
        category_uuids: List[str] = None,
        create_time_end: int = None,
        create_time_start: int = None,
        dataset_description: str = None,
        dataset_id: int = None,
        dataset_name: str = None,
        doc_ids: List[str] = None,
        doc_type: str = None,
        doc_uuids: List[str] = None,
        end_time: int = None,
        exclude_fields: List[str] = None,
        extend_1: str = None,
        extend_2: str = None,
        extend_3: str = None,
        include_fields: List[str] = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        query: str = None,
        start_time: int = None,
        status: int = None,
        tags: List[str] = None,
        title: str = None,
        workspace_id: str = None,
    ):
        self.category_uuids = category_uuids
        self.create_time_end = create_time_end
        self.create_time_start = create_time_start
        self.dataset_description = dataset_description
        self.dataset_id = dataset_id
        self.dataset_name = dataset_name
        self.doc_ids = doc_ids
        self.doc_type = doc_type
        self.doc_uuids = doc_uuids
        self.end_time = end_time
        self.exclude_fields = exclude_fields
        self.extend_1 = extend_1
        self.extend_2 = extend_2
        self.extend_3 = extend_3
        self.include_fields = include_fields
        self.next_token = next_token
        self.page_number = page_number
        self.page_size = page_size
        self.query = query
        self.start_time = start_time
        self.status = status
        self.tags = tags
        self.title = title
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_uuids is not None:
            result['CategoryUuids'] = self.category_uuids

        if self.create_time_end is not None:
            result['CreateTimeEnd'] = self.create_time_end

        if self.create_time_start is not None:
            result['CreateTimeStart'] = self.create_time_start

        if self.dataset_description is not None:
            result['DatasetDescription'] = self.dataset_description

        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id

        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name

        if self.doc_ids is not None:
            result['DocIds'] = self.doc_ids

        if self.doc_type is not None:
            result['DocType'] = self.doc_type

        if self.doc_uuids is not None:
            result['DocUuids'] = self.doc_uuids

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.exclude_fields is not None:
            result['ExcludeFields'] = self.exclude_fields

        if self.extend_1 is not None:
            result['Extend1'] = self.extend_1

        if self.extend_2 is not None:
            result['Extend2'] = self.extend_2

        if self.extend_3 is not None:
            result['Extend3'] = self.extend_3

        if self.include_fields is not None:
            result['IncludeFields'] = self.include_fields

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.query is not None:
            result['Query'] = self.query

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.title is not None:
            result['Title'] = self.title

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryUuids') is not None:
            self.category_uuids = m.get('CategoryUuids')

        if m.get('CreateTimeEnd') is not None:
            self.create_time_end = m.get('CreateTimeEnd')

        if m.get('CreateTimeStart') is not None:
            self.create_time_start = m.get('CreateTimeStart')

        if m.get('DatasetDescription') is not None:
            self.dataset_description = m.get('DatasetDescription')

        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')

        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')

        if m.get('DocIds') is not None:
            self.doc_ids = m.get('DocIds')

        if m.get('DocType') is not None:
            self.doc_type = m.get('DocType')

        if m.get('DocUuids') is not None:
            self.doc_uuids = m.get('DocUuids')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('ExcludeFields') is not None:
            self.exclude_fields = m.get('ExcludeFields')

        if m.get('Extend1') is not None:
            self.extend_1 = m.get('Extend1')

        if m.get('Extend2') is not None:
            self.extend_2 = m.get('Extend2')

        if m.get('Extend3') is not None:
            self.extend_3 = m.get('Extend3')

        if m.get('IncludeFields') is not None:
            self.include_fields = m.get('IncludeFields')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

