# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeClusterVulStatisticsRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        types: str = None,
    ):
        # The ID of the container cluster.
        self.cluster_id = cluster_id
        # The type of the vulnerabilities. Valid values:
        # 
        # *   **cve**: Linux software vulnerabilities
        # *   **app**: application vulnerabilities
        # *   **sca**: vulnerabilities that are detected based on software component analysis
        self.types = types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.types is not None:
            result['Types'] = self.types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('Types') is not None:
            self.types = m.get('Types')

        return self

