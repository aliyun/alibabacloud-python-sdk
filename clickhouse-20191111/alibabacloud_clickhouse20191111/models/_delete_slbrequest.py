# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteSLBRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        product: str = None,
    ):
        # The cluster ID. You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/170879.html) operation to view cluster IDs.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        self.product = product

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.product is not None:
            result['Product'] = self.product

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('Product') is not None:
            self.product = m.get('Product')

        return self

