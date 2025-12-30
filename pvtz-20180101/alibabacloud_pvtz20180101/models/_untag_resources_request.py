# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UntagResourcesRequest(DaraModel):
    def __init__(
        self,
        all: bool = None,
        lang: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag_key: List[str] = None,
    ):
        # Specifies whether to remove all tags of the specified zones. Valid values:
        # 
        # *   true: removes all tags of the specified zones.
        # *   false: removes only the tags with the specified tag keys.
        # 
        # Default value: false.
        self.all = all
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        # 
        # Default value: en.
        self.lang = lang
        # The resource IDs, which are zone IDs. You can specify up to 50 zone IDs.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The resource type. The value of ResourceType can only be ZONE.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The keys of tags that you want to remove. You can specify up to 20 tag keys.
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.all is not None:
            result['All'] = self.all

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        return self

