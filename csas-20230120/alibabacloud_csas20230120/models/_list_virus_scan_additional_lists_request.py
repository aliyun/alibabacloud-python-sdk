# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListVirusScanAdditionalListsRequest(DaraModel):
    def __init__(
        self,
        additional_types: List[str] = None,
        dev_type: str = None,
        list_detail: str = None,
        list_ids: List[str] = None,
        list_type: str = None,
    ):
        # Filters by matching dimension. Duplicate values are not allowed. If this parameter is not specified, all matching dimensions are returned.
        self.additional_types = additional_types
        # The operating system type for which the list takes effect. Valid values:
        # - **windows**: Windows.
        # - **macOS**: macOS.
        # 
        # This parameter is required.
        self.dev_type = dev_type
        # The content of the list entry, using exact match. This parameter is used to locate a specific list entry by content and does not support fuzzy match.
        self.list_detail = list_detail
        # Filters by list entry ID. Duplicate values are not allowed. If this parameter is not specified, no filtering by list entry ID is applied.
        self.list_ids = list_ids
        # Filters by list type. If this parameter is not specified, both blacklists and whitelists are returned. Valid values:
        # - **Blacklist**: Blacklist. Files that match are directly identified as virus files.
        # - **Whitelist**: Whitelist. Files that match are excluded from virus detection.
        self.list_type = list_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.additional_types is not None:
            result['AdditionalTypes'] = self.additional_types

        if self.dev_type is not None:
            result['DevType'] = self.dev_type

        if self.list_detail is not None:
            result['ListDetail'] = self.list_detail

        if self.list_ids is not None:
            result['ListIds'] = self.list_ids

        if self.list_type is not None:
            result['ListType'] = self.list_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdditionalTypes') is not None:
            self.additional_types = m.get('AdditionalTypes')

        if m.get('DevType') is not None:
            self.dev_type = m.get('DevType')

        if m.get('ListDetail') is not None:
            self.list_detail = m.get('ListDetail')

        if m.get('ListIds') is not None:
            self.list_ids = m.get('ListIds')

        if m.get('ListType') is not None:
            self.list_type = m.get('ListType')

        return self

