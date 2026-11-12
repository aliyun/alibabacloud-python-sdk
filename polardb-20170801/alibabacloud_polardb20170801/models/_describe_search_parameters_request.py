# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSearchParametersRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
    ):
        # The ID of the PolarDB primary cluster. This ID is used to locate the Search cluster associated with the current account. Only PolarDB for MySQL clusters are supported. Search is not supported for PostgreSQL or Oracle-compatible clusters. Before you call this operation, enable the Search engine for the target cluster in the PolarDB console. If the Search engine is not enabled, the InvalidDBClusterId.NotFound error may be returned.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        return self

