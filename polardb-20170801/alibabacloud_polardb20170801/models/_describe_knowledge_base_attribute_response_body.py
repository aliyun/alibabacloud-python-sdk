# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeKnowledgeBaseAttributeResponseBody(DaraModel):
    def __init__(
        self,
        binding_app_count: int = None,
        creation_time: str = None,
        description: str = None,
        knowledge_base_id: str = None,
        knowledge_base_type: str = None,
        knowledge_space_id: str = None,
        name: str = None,
        request_id: str = None,
        search_mode: str = None,
        shard_count: int = None,
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
        # The type of the knowledge base. Valid values:
        # - PUBLIC
        # - PERSONAL
        self.knowledge_base_type = knowledge_base_type
        # The ID of the knowledge space.
        self.knowledge_space_id = knowledge_space_id
        # The name of the knowledge base.
        self.name = name
        # Id of the request
        self.request_id = request_id
        # The search mode. Valid values:
        # * balanced (default)
        # * precise
        # * semantic
        # * knn
        # * rrf
        self.search_mode = search_mode
        # The number of shards.
        self.shard_count = shard_count
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

        if self.knowledge_base_type is not None:
            result['KnowledgeBaseType'] = self.knowledge_base_type

        if self.knowledge_space_id is not None:
            result['KnowledgeSpaceId'] = self.knowledge_space_id

        if self.name is not None:
            result['Name'] = self.name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.search_mode is not None:
            result['SearchMode'] = self.search_mode

        if self.shard_count is not None:
            result['ShardCount'] = self.shard_count

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

        if m.get('KnowledgeBaseType') is not None:
            self.knowledge_base_type = m.get('KnowledgeBaseType')

        if m.get('KnowledgeSpaceId') is not None:
            self.knowledge_space_id = m.get('KnowledgeSpaceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SearchMode') is not None:
            self.search_mode = m.get('SearchMode')

        if m.get('ShardCount') is not None:
            self.shard_count = m.get('ShardCount')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TotalDocs') is not None:
            self.total_docs = m.get('TotalDocs')

        if m.get('TotalSizeBytes') is not None:
            self.total_size_bytes = m.get('TotalSizeBytes')

        return self

