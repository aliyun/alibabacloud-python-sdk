# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetInterceptionSummaryRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        exclude_cluster_types: List[str] = None,
    ):
        # The ID of the cluster to query. This parameter takes effect only on the InterceptionCountInDays response parameter.
        # > You can call the [DescribeGroupedContainerInstances](~~DescribeGroupedContainerInstances~~) operation to obtain this parameter.
        self.cluster_id = cluster_id
        # The list of cluster types to exclude.
        self.exclude_cluster_types = exclude_cluster_types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.exclude_cluster_types is not None:
            result['ExcludeClusterTypes'] = self.exclude_cluster_types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ExcludeClusterTypes') is not None:
            self.exclude_cluster_types = m.get('ExcludeClusterTypes')

        return self

