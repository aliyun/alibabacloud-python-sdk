# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListAddonTemplatesRequest(DaraModel):
    def __init__(
        self,
        addon_names: List[str] = None,
        cluster_category: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
    ):
        # The addon names.
        self.addon_names = addon_names
        # The cluster type. Valid values:
        # 
        # *   Standard
        # *   Serverless
        self.cluster_category = cluster_category
        # The page number of the page to return. Pages start from page 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 20.
        self.page_size = page_size
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.addon_names is not None:
            result['AddonNames'] = self.addon_names

        if self.cluster_category is not None:
            result['ClusterCategory'] = self.cluster_category

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddonNames') is not None:
            self.addon_names = m.get('AddonNames')

        if m.get('ClusterCategory') is not None:
            self.cluster_category = m.get('ClusterCategory')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

