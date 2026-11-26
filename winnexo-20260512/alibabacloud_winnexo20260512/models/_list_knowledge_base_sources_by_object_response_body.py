# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class ListKnowledgeBaseSourcesByObjectResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        page: int = None,
        page_size: int = None,
        request_id: str = None,
        sources: List[main_models.ListKnowledgeBaseSourcesByObjectResponseBodySources] = None,
        total_count: int = None,
    ):
        # The status code.
        self.code = code
        # The description of the status code.
        self.message = message
        # The number of entries per page.
        self.page = page
        # The subject type filter.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The referenced sources. The key is the project name, and the value is the list of selected Logstores under the project, which is consistent with the structure submitted during creation. `["*"]` indicates all Logstores under the project. Otherwise, it is a list of exact Logstore names. If no sources are referenced, an empty object `{}` is returned.
        self.sources = sources
        # The total number of results.
        self.total_count = total_count

    def validate(self):
        if self.sources:
            for v1 in self.sources:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        if self.page is not None:
            result['page'] = self.page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['sources'] = []
        if self.sources is not None:
            for k1 in self.sources:
                result['sources'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.sources = []
        if m.get('sources') is not None:
            for k1 in m.get('sources'):
                temp_model = main_models.ListKnowledgeBaseSourcesByObjectResponseBodySources()
                self.sources.append(temp_model.from_map(k1))

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListKnowledgeBaseSourcesByObjectResponseBodySources(DaraModel):
    def __init__(
        self,
        description: str = None,
        directory_id: str = None,
        name: str = None,
        scope: str = None,
        source_id: str = None,
        source_type: str = None,
        status: str = None,
    ):
        # The description of the to-do card type.
        self.description = description
        # The directory ID.
        self.directory_id = directory_id
        # The file name.
        self.name = name
        # The permission scope.
        self.scope = scope
        # The ID of the enterprise knowledge base FILE data source to be replaced.
        self.source_id = source_id
        # The data source type.
        self.source_type = source_type
        # The data source status after re-parsing.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.directory_id is not None:
            result['directoryId'] = self.directory_id

        if self.name is not None:
            result['name'] = self.name

        if self.scope is not None:
            result['scope'] = self.scope

        if self.source_id is not None:
            result['sourceId'] = self.source_id

        if self.source_type is not None:
            result['sourceType'] = self.source_type

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('directoryId') is not None:
            self.directory_id = m.get('directoryId')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('scope') is not None:
            self.scope = m.get('scope')

        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

