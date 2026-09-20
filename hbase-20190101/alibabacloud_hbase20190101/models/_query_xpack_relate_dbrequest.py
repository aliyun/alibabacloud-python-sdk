# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryXpackRelateDBRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        has_single_node: bool = None,
        relate_db_type: str = None,
    ):
        # The instance ID of the current Spark instance.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # This parameter is valid only when bds queries associated HBase instances.
        # 
        # - true: Single-node HBase instances are included.
        # 
        # - false: Single-node HBase instances are not included. This parameter is optional. For backward compatibility, single-node HBase instances are included when this parameter is left empty.
        self.has_single_node = has_single_node
        # The type of database to query for association.
        # 
        # - spark can be associated with hdfs, hbase, mongodb, mysql, polardb_mysql, redis, and geomesa.
        # - bds can be associated with hbase, spark, and hbaseue.
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

        if self.has_single_node is not None:
            result['HasSingleNode'] = self.has_single_node

        if self.relate_db_type is not None:
            result['RelateDbType'] = self.relate_db_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('HasSingleNode') is not None:
            self.has_single_node = m.get('HasSingleNode')

        if m.get('RelateDbType') is not None:
            self.relate_db_type = m.get('RelateDbType')

        return self

