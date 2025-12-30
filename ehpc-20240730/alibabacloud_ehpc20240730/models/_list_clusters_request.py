# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListClustersRequest(DaraModel):
    def __init__(
        self,
        cluster_ids: List[str] = None,
        cluster_names: List[str] = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The cluster IDs. You can specify up to 20 IDs.
        self.cluster_ids = cluster_ids
        # The cluster names. You can specify up to 20 names.
        self.cluster_names = cluster_names
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
        if self.cluster_ids is not None:
            result['ClusterIds'] = self.cluster_ids

        if self.cluster_names is not None:
            result['ClusterNames'] = self.cluster_names

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterIds') is not None:
            self.cluster_ids = m.get('ClusterIds')

        if m.get('ClusterNames') is not None:
            self.cluster_names = m.get('ClusterNames')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

