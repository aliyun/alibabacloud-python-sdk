# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListResourceTypesRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        query: List[str] = None,
        resource_type: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # - zh-CN: Chinese
        # 
        # - en-US: English
        self.accept_language = accept_language
        # The query conditions.
        self.query = query
        # The resource type.
        # 
        # For more information about the resource types that are supported by Resource Center, see [Services that work with Resource Center](https://help.aliyun.com/document_detail/477798.html).
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.query is not None:
            result['Query'] = self.query

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

