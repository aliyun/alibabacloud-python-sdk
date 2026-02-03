# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SearchDatasetDocumentsShrinkRequest(DaraModel):
    def __init__(
        self,
        category_uuids_shrink: str = None,
        create_time_end: int = None,
        create_time_start: int = None,
        dataset_id: int = None,
        dataset_name: str = None,
        doc_ids_shrink: str = None,
        doc_types_shrink: str = None,
        doc_uuids_shrink: str = None,
        end_time: int = None,
        extend_1: str = None,
        extend_2: str = None,
        extend_3: str = None,
        include_content: bool = None,
        page_size: str = None,
        query: str = None,
        search_mode: str = None,
        start_time: int = None,
        tags_shrink: str = None,
        workspace_id: str = None,
    ):
        self.category_uuids_shrink = category_uuids_shrink
        self.create_time_end = create_time_end
        self.create_time_start = create_time_start
        self.dataset_id = dataset_id
        self.dataset_name = dataset_name
        self.doc_ids_shrink = doc_ids_shrink
        self.doc_types_shrink = doc_types_shrink
        self.doc_uuids_shrink = doc_uuids_shrink
        self.end_time = end_time
        self.extend_1 = extend_1
        self.extend_2 = extend_2
        self.extend_3 = extend_3
        self.include_content = include_content
        self.page_size = page_size
        # This parameter is required.
        self.query = query
        self.search_mode = search_mode
        self.start_time = start_time
        self.tags_shrink = tags_shrink
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_uuids_shrink is not None:
            result['CategoryUuids'] = self.category_uuids_shrink

        if self.create_time_end is not None:
            result['CreateTimeEnd'] = self.create_time_end

        if self.create_time_start is not None:
            result['CreateTimeStart'] = self.create_time_start

        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id

        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name

        if self.doc_ids_shrink is not None:
            result['DocIds'] = self.doc_ids_shrink

        if self.doc_types_shrink is not None:
            result['DocTypes'] = self.doc_types_shrink

        if self.doc_uuids_shrink is not None:
            result['DocUuids'] = self.doc_uuids_shrink

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.extend_1 is not None:
            result['Extend1'] = self.extend_1

        if self.extend_2 is not None:
            result['Extend2'] = self.extend_2

        if self.extend_3 is not None:
            result['Extend3'] = self.extend_3

        if self.include_content is not None:
            result['IncludeContent'] = self.include_content

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.query is not None:
            result['Query'] = self.query

        if self.search_mode is not None:
            result['SearchMode'] = self.search_mode

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryUuids') is not None:
            self.category_uuids_shrink = m.get('CategoryUuids')

        if m.get('CreateTimeEnd') is not None:
            self.create_time_end = m.get('CreateTimeEnd')

        if m.get('CreateTimeStart') is not None:
            self.create_time_start = m.get('CreateTimeStart')

        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')

        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')

        if m.get('DocIds') is not None:
            self.doc_ids_shrink = m.get('DocIds')

        if m.get('DocTypes') is not None:
            self.doc_types_shrink = m.get('DocTypes')

        if m.get('DocUuids') is not None:
            self.doc_uuids_shrink = m.get('DocUuids')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Extend1') is not None:
            self.extend_1 = m.get('Extend1')

        if m.get('Extend2') is not None:
            self.extend_2 = m.get('Extend2')

        if m.get('Extend3') is not None:
            self.extend_3 = m.get('Extend3')

        if m.get('IncludeContent') is not None:
            self.include_content = m.get('IncludeContent')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        if m.get('SearchMode') is not None:
            self.search_mode = m.get('SearchMode')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

