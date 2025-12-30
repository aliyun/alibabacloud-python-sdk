# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListClustersShrinkRequest(DaraModel):
    def __init__(
        self,
        cluster_ids_shrink: str = None,
        cluster_names_shrink: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The cluster IDs. You can specify up to 20 IDs.
        self.cluster_ids_shrink = cluster_ids_shrink
        # The cluster names. You can specify up to 20 names.
        self.cluster_names_shrink = cluster_names_shrink
        # The page number of the page to return. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 10 to 100. Default value: 10
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_ids_shrink is not None:
            result['ClusterIds'] = self.cluster_ids_shrink

        if self.cluster_names_shrink is not None:
            result['ClusterNames'] = self.cluster_names_shrink

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterIds') is not None:
            self.cluster_ids_shrink = m.get('ClusterIds')

        if m.get('ClusterNames') is not None:
            self.cluster_names_shrink = m.get('ClusterNames')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

