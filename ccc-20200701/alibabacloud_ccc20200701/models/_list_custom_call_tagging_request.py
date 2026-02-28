# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListCustomCallTaggingRequest(DaraModel):
    def __init__(
        self,
        call_tag_name_list: str = None,
        instance_id: str = None,
        page_number: int = None,
        page_size: int = None,
        search_pattern: str = None,
    ):
        self.call_tag_name_list = call_tag_name_list
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.page_number = page_number
        # This parameter is required.
        self.page_size = page_size
        self.search_pattern = search_pattern

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.call_tag_name_list is not None:
            result['CallTagNameList'] = self.call_tag_name_list

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.search_pattern is not None:
            result['SearchPattern'] = self.search_pattern

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallTagNameList') is not None:
            self.call_tag_name_list = m.get('CallTagNameList')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SearchPattern') is not None:
            self.search_pattern = m.get('SearchPattern')

        return self

