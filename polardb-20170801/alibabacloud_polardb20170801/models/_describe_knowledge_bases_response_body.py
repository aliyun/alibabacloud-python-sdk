# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeKnowledgeBasesResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribeKnowledgeBasesResponseBodyItems] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_record_count: int = None,
    ):
        # The list of knowledge bases.
        self.items = items
        # The page number.
        self.page_number = page_number
        # The number of entries per page. Valid values: **30**, **50**, and **100**.
        #                               
        # Default value: **30**.
        self.page_size = page_size
        # Id of the request
        self.request_id = request_id
        # The total number of records.
        self.total_record_count = total_record_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeKnowledgeBasesResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribeKnowledgeBasesResponseBodyItems(DaraModel):
    def __init__(
        self,
        binding_app_count: int = None,
        creation_time: str = None,
        description: str = None,
        knowledge_base_id: str = None,
        knowledge_space_id: str = None,
        name: str = None,
        status: str = None,
        total_docs: int = None,
        total_size_bytes: int = None,
    ):
        # The number of AI applications bound to the knowledge base.
        self.binding_app_count = binding_app_count
        # The creation time.
        self.creation_time = creation_time
        # The description of the knowledge base.
        self.description = description
        # The unique identifier of the knowledge base.
        self.knowledge_base_id = knowledge_base_id
        # The ID of the knowledge space.
        self.knowledge_space_id = knowledge_space_id
        # The name of the knowledge base.
        self.name = name
        # The status of the knowledge base.
        self.status = status
        # The total number of documents.
        self.total_docs = total_docs
        # The total size in bytes.
        self.total_size_bytes = total_size_bytes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.binding_app_count is not None:
            result['BindingAppCount'] = self.binding_app_count

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        if self.knowledge_base_id is not None:
            result['KnowledgeBaseId'] = self.knowledge_base_id

        if self.knowledge_space_id is not None:
            result['KnowledgeSpaceId'] = self.knowledge_space_id

        if self.name is not None:
            result['Name'] = self.name

        if self.status is not None:
            result['Status'] = self.status

        if self.total_docs is not None:
            result['TotalDocs'] = self.total_docs

        if self.total_size_bytes is not None:
            result['TotalSizeBytes'] = self.total_size_bytes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindingAppCount') is not None:
            self.binding_app_count = m.get('BindingAppCount')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('KnowledgeBaseId') is not None:
            self.knowledge_base_id = m.get('KnowledgeBaseId')

        if m.get('KnowledgeSpaceId') is not None:
            self.knowledge_space_id = m.get('KnowledgeSpaceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TotalDocs') is not None:
            self.total_docs = m.get('TotalDocs')

        if m.get('TotalSizeBytes') is not None:
            self.total_size_bytes = m.get('TotalSizeBytes')

        return self

