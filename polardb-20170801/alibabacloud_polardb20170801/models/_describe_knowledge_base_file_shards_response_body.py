# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeKnowledgeBaseFileShardsResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_record_count: int = None,
        page_size: int = None,
        request_id: str = None,
        shards: List[main_models.DescribeKnowledgeBaseFileShardsResponseBodyShards] = None,
        total_record_count: int = None,
    ):
        # The current page number.
        self.page_number = page_number
        # The number of records on the current page.
        self.page_record_count = page_record_count
        # The number of entries per page in a paged query.
        self.page_size = page_size
        # Id of the request
        self.request_id = request_id
        # The shard information.
        self.shards = shards
        # The total number of records.
        self.total_record_count = total_record_count

    def validate(self):
        if self.shards:
            for v1 in self.shards:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Shards'] = []
        if self.shards is not None:
            for k1 in self.shards:
                result['Shards'].append(k1.to_map() if k1 else None)

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.shards = []
        if m.get('Shards') is not None:
            for k1 in m.get('Shards'):
                temp_model = main_models.DescribeKnowledgeBaseFileShardsResponseBodyShards()
                self.shards.append(temp_model.from_map(k1))

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribeKnowledgeBaseFileShardsResponseBodyShards(DaraModel):
    def __init__(
        self,
        captions: List[str] = None,
        doc_items: List[str] = None,
        headings: List[str] = None,
        image_resources: List[main_models.DescribeKnowledgeBaseFileShardsResponseBodyShardsImageResources] = None,
        page_numbers: List[str] = None,
        shard_content: str = None,
        shard_index: int = None,
    ):
        # The list of figure or table captions associated with the shard.
        self.captions = captions
        # The list of Docling source document structured element references associated with the shard. You can use these references to precisely locate original document elements.
        self.doc_items = doc_items
        # The chain of section headings to which the shard belongs.
        self.headings = headings
        # The list of image resources referenced by the shard.
        self.image_resources = image_resources
        # The list of page numbers to which the shard belongs.
        self.page_numbers = page_numbers
        # The text content of the shard.
        self.shard_content = shard_content
        # The index of the shard.
        self.shard_index = shard_index

    def validate(self):
        if self.image_resources:
            for v1 in self.image_resources:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.captions is not None:
            result['Captions'] = self.captions

        if self.doc_items is not None:
            result['DocItems'] = self.doc_items

        if self.headings is not None:
            result['Headings'] = self.headings

        result['ImageResources'] = []
        if self.image_resources is not None:
            for k1 in self.image_resources:
                result['ImageResources'].append(k1.to_map() if k1 else None)

        if self.page_numbers is not None:
            result['PageNumbers'] = self.page_numbers

        if self.shard_content is not None:
            result['ShardContent'] = self.shard_content

        if self.shard_index is not None:
            result['ShardIndex'] = self.shard_index

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Captions') is not None:
            self.captions = m.get('Captions')

        if m.get('DocItems') is not None:
            self.doc_items = m.get('DocItems')

        if m.get('Headings') is not None:
            self.headings = m.get('Headings')

        self.image_resources = []
        if m.get('ImageResources') is not None:
            for k1 in m.get('ImageResources'):
                temp_model = main_models.DescribeKnowledgeBaseFileShardsResponseBodyShardsImageResources()
                self.image_resources.append(temp_model.from_map(k1))

        if m.get('PageNumbers') is not None:
            self.page_numbers = m.get('PageNumbers')

        if m.get('ShardContent') is not None:
            self.shard_content = m.get('ShardContent')

        if m.get('ShardIndex') is not None:
            self.shard_index = m.get('ShardIndex')

        return self

class DescribeKnowledgeBaseFileShardsResponseBodyShardsImageResources(DaraModel):
    def __init__(
        self,
        document_index: int = None,
        id: str = None,
        item_ref: str = None,
        mime_type: str = None,
        uri: str = None,
    ):
        # The index of the source document to which the image belongs, starting from 0.
        self.document_index = document_index
        # The unique ID of the image resource.
        self.id = id
        # The element reference of the image in the Docling source document structure.
        self.item_ref = item_ref
        # The media type of the image resource.
        self.mime_type = mime_type
        # The OSS URI of the image resource.
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.document_index is not None:
            result['DocumentIndex'] = self.document_index

        if self.id is not None:
            result['Id'] = self.id

        if self.item_ref is not None:
            result['ItemRef'] = self.item_ref

        if self.mime_type is not None:
            result['MimeType'] = self.mime_type

        if self.uri is not None:
            result['Uri'] = self.uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DocumentIndex') is not None:
            self.document_index = m.get('DocumentIndex')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ItemRef') is not None:
            self.item_ref = m.get('ItemRef')

        if m.get('MimeType') is not None:
            self.mime_type = m.get('MimeType')

        if m.get('Uri') is not None:
            self.uri = m.get('Uri')

        return self

