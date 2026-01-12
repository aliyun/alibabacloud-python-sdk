# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_clickhouse20191111 import models as main_models
from darabonba.model import DaraModel

class ModifyDBClusterResponseBody(DaraModel):
    def __init__(
        self,
        dbcluster: main_models.ModifyDBClusterResponseBodyDBCluster = None,
        request_id: str = None,
    ):
        # The clusters.
        self.dbcluster = dbcluster
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.dbcluster:
            self.dbcluster.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster is not None:
            result['DBCluster'] = self.dbcluster.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBCluster') is not None:
            temp_model = main_models.ModifyDBClusterResponseBodyDBCluster()
            self.dbcluster = temp_model.from_map(m.get('DBCluster'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ModifyDBClusterResponseBodyDBCluster(DaraModel):
    def __init__(
        self,
        db_cluster_id: str = None,
        order_id: str = None,
    ):
        # The cluster ID.
        self.db_cluster_id = db_cluster_id
        # The order ID.
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_cluster_id is not None:
            result['dbClusterId'] = self.db_cluster_id

        if self.order_id is not None:
            result['orderId'] = self.order_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dbClusterId') is not None:
            self.db_cluster_id = m.get('dbClusterId')

        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')

        return self

