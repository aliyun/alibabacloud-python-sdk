# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeKnowledgeBaseFilesRequest(DaraModel):
    def __init__(
        self,
        file_ids: str = None,
        keyword: str = None,
        knowledge_base_id: str = None,
        link_id: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        source_type: str = None,
    ):
        # The list of file IDs, separated by commas (,).
        self.file_ids = file_ids
        # The keyword used to filter file names.
        self.keyword = keyword
        # The unique ID of the knowledge base.
        # 
        # This parameter is required.
        self.knowledge_base_id = knowledge_base_id
        # The unique ID of the synchronization link.
        self.link_id = link_id
        # The page number.
        self.page_number = page_number
        # The number of records per page.
        self.page_size = page_size
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The source type.
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_ids is not None:
            result['FileIds'] = self.file_ids

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.knowledge_base_id is not None:
            result['KnowledgeBaseId'] = self.knowledge_base_id

        if self.link_id is not None:
            result['LinkId'] = self.link_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileIds') is not None:
            self.file_ids = m.get('FileIds')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('KnowledgeBaseId') is not None:
            self.knowledge_base_id = m.get('KnowledgeBaseId')

        if m.get('LinkId') is not None:
            self.link_id = m.get('LinkId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        return self

