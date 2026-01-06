# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateApsCopyWorkloadRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        datasource_id: int = None,
        db_name: str = None,
        region_id: str = None,
        table_name: str = None,
        workload_id: str = None,
        workload_type: str = None,
    ):
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The data source ID.
        self.datasource_id = datasource_id
        # The name of the database.
        self.db_name = db_name
        # The region ID.
        self.region_id = region_id
        # The name of the table.
        self.table_name = table_name
        # The job ID.
        # 
        # This parameter is required.
        self.workload_id = workload_id
        # The type of the job.
        # 
        # This parameter is required.
        self.workload_type = workload_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.datasource_id is not None:
            result['DatasourceId'] = self.datasource_id

        if self.db_name is not None:
            result['DbName'] = self.db_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.workload_id is not None:
            result['WorkloadId'] = self.workload_id

        if self.workload_type is not None:
            result['WorkloadType'] = self.workload_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DatasourceId') is not None:
            self.datasource_id = m.get('DatasourceId')

        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('WorkloadId') is not None:
            self.workload_id = m.get('WorkloadId')

        if m.get('WorkloadType') is not None:
            self.workload_type = m.get('WorkloadType')

        return self

