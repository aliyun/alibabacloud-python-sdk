# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitResultExportJobRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        engine: str = None,
        export_type: str = None,
        region_id: str = None,
        resource_group: str = None,
        sql: str = None,
        schema: str = None,
    ):
        # The ID of the AnalyticDB for MySQL Data Lakehouse Edition cluster.
        # 
        # >  You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/129857.html) operation to query the IDs of all AnalyticDB for MySQL Data Lakehouse Edition clusters within a region.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The engine that is used to run the result set export job. Set the value to XIHE.
        self.engine = engine
        # The type of the result set export job.
        self.export_type = export_type
        # The region ID.
        # 
        # >  You can call the [DescribeRegions](https://help.aliyun.com/document_detail/143074.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The name of the resource group that runs the result set export job.
        self.resource_group = resource_group
        # The SQL statement that is used in the result set export job. You can specify only SELECT statements. If you specify other SQL statements, the request fails.
        # 
        # This parameter is required.
        self.sql = sql
        # The name of the database.
        # 
        # This parameter is required.
        self.schema = schema

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.export_type is not None:
            result['ExportType'] = self.export_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group is not None:
            result['ResourceGroup'] = self.resource_group

        if self.sql is not None:
            result['SQL'] = self.sql

        if self.schema is not None:
            result['Schema'] = self.schema

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('ExportType') is not None:
            self.export_type = m.get('ExportType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroup') is not None:
            self.resource_group = m.get('ResourceGroup')

        if m.get('SQL') is not None:
            self.sql = m.get('SQL')

        if m.get('Schema') is not None:
            self.schema = m.get('Schema')

        return self

