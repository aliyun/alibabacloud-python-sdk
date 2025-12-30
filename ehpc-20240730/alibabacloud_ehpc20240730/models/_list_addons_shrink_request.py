# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAddonsShrinkRequest(DaraModel):
    def __init__(
        self,
        addon_ids_shrink: str = None,
        cluster_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The addon IDs.
        self.addon_ids_shrink = addon_ids_shrink
        # The cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The page number of the page to return. Default value: 1
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.addon_ids_shrink is not None:
            result['AddonIds'] = self.addon_ids_shrink

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddonIds') is not None:
            self.addon_ids_shrink = m.get('AddonIds')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

