# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListApiMcpServersRequest(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        id: str = None,
        keyword: str = None,
        language: str = None,
        max_results: int = None,
        next_token: str = None,
        skip: int = None,
        source_type: str = None,
        update_time: str = None,
    ):
        # The time when the API MCP server was created.
        self.create_time = create_time
        # The description of the API MCP service.
        self.description = description
        # The ID of the API MCP service.
        self.id = id
        # The search keyword. Supports fuzzy search by API name and exact search by API ID.
        self.keyword = keyword
        # The language of the API reference for the API MCP service. The language of the prompt can affect the response from the AI. Valid values: \\`ZH_CN\\`, \\`EN_US\\`.
        self.language = language
        # The maximum number of entries to return on each page for a paged query. The maximum value is 100. The default value is 20.
        self.max_results = max_results
        # The token that is used to start the next query. Set this parameter to the \\`nextToken\\` value that was returned from the previous API call.
        # 
        # > This parameter is not required for the first query. If a query does not return all results, pass the \\`nextToken\\` value from the previous query to continue.
        self.next_token = next_token
        # The number of data entries to skip.
        self.skip = skip
        # The type of the API MCP service.
        # 
        # - custom: a custom service
        # 
        # - system: a system service
        self.source_type = source_type
        # The time when the API MCP server was last updated.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.description is not None:
            result['description'] = self.description

        if self.id is not None:
            result['id'] = self.id

        if self.keyword is not None:
            result['keyword'] = self.keyword

        if self.language is not None:
            result['language'] = self.language

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.skip is not None:
            result['skip'] = self.skip

        if self.source_type is not None:
            result['sourceType'] = self.source_type

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')

        if m.get('language') is not None:
            self.language = m.get('language')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('skip') is not None:
            self.skip = m.get('skip')

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        return self

