# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTagResourcesRequest(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        page: int = None,
        resource_ids: str = None,
        resource_type: str = None,
        size: int = None,
        tags: str = None,
    ):
        # The number of the returned page.
        self.next_token = next_token
        # 1d2db86sca4384811e0b5e8707e\\*\\*\\*\\*\\*\\*
        self.page = page
        # The ID of the request.
        self.resource_ids = resource_ids
        # [{"key":"env","value","dev"},{"key":"dev", "value":"IT"}]
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # ["es-cn-aaa","es-cn-bbb"]
        self.size = size
        # The header of the response. This parameter is empty and is for reference only. You cannot force this parameter to be relied on in the program.
        # 
        # >  The return examples does not contain this parameter.
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page is not None:
            result['Page'] = self.page

        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.size is not None:
            result['Size'] = self.size

        if self.tags is not None:
            result['Tags'] = self.tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        return self

