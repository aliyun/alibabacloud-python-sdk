# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListNacosMcpServersRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        instance_id: str = None,
        name: str = None,
        namespace_id: str = None,
        page_num: int = None,
        page_size: int = None,
        search: str = None,
    ):
        # The language of the response. Valid values: zh (default): Chinese, en: English.
        self.accept_language = accept_language
        # The instance ID.
        self.instance_id = instance_id
        # The MCP server name.
        self.name = name
        # The namespace ID.
        self.namespace_id = namespace_id
        # The page number.
        self.page_num = page_num
        # The page size.
        self.page_size = page_size
        # The query pattern.
        self.search = search

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.name is not None:
            result['Name'] = self.name

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.search is not None:
            result['Search'] = self.search

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Search') is not None:
            self.search = m.get('Search')

        return self

