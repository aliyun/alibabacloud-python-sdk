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
        self.create_time = create_time
        self.description = description
        self.id = id
        self.keyword = keyword
        self.language = language
        self.max_results = max_results
        self.next_token = next_token
        self.skip = skip
        self.source_type = source_type
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

