# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class XpackRelateDBRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        db_cluster_ids: str = None,
        relate_db_type: str = None,
    ):
        # The instance ID of the current Spark instance.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The instance ID of the cluster to associate.
        # 
        # This parameter is required.
        self.db_cluster_ids = db_cluster_ids
        # The type of database to associate. Valid values:
        # - **hdfs**
        # - **hbase**
        # - **mongodb**
        # - **mysql**
        # - **polardb_mysql**
        # - **redis**
        # - **geomesa**.
        # 
        # This parameter is required.
        self.relate_db_type = relate_db_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.db_cluster_ids is not None:
            result['DbClusterIds'] = self.db_cluster_ids

        if self.relate_db_type is not None:
            result['RelateDbType'] = self.relate_db_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('DbClusterIds') is not None:
            self.db_cluster_ids = m.get('DbClusterIds')

        if m.get('RelateDbType') is not None:
            self.relate_db_type = m.get('RelateDbType')

        return self

