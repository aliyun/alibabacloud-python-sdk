# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateApsDatasoureShrinkRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        databricks_info_shrink: str = None,
        datasource_description: str = None,
        datasource_name: str = None,
        datasource_type: str = None,
        hive_info_shrink: str = None,
        kafka_info_shrink: str = None,
        mode: str = None,
        polar_dbmysql_info_shrink: str = None,
        polar_dbxinfo_shrink: str = None,
        rds_mysql_info_shrink: str = None,
        region_id: str = None,
        sls_info_shrink: str = None,
    ):
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The information about the Databricks data source.
        self.databricks_info_shrink = databricks_info_shrink
        # The description of the data source.
        self.datasource_description = datasource_description
        # The name of the data source.
        # 
        # This parameter is required.
        self.datasource_name = datasource_name
        # The type of the data source.
        # 
        # This parameter is required.
        self.datasource_type = datasource_type
        # The information about the Hive data source.
        self.hive_info_shrink = hive_info_shrink
        # The information about the source Apache Kafka instance.
        self.kafka_info_shrink = kafka_info_shrink
        # The mode.
        self.mode = mode
        # The information about the source PolarDB for MySQL cluster.
        self.polar_dbmysql_info_shrink = polar_dbmysql_info_shrink
        # The information about the source PolarDB-X instance.
        self.polar_dbxinfo_shrink = polar_dbxinfo_shrink
        # The information about the source ApsaraDB RDS for MySQL instance.
        self.rds_mysql_info_shrink = rds_mysql_info_shrink
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The information about the source Simple Log Service (SLS) instance or cluster.
        self.sls_info_shrink = sls_info_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.databricks_info_shrink is not None:
            result['DatabricksInfo'] = self.databricks_info_shrink

        if self.datasource_description is not None:
            result['DatasourceDescription'] = self.datasource_description

        if self.datasource_name is not None:
            result['DatasourceName'] = self.datasource_name

        if self.datasource_type is not None:
            result['DatasourceType'] = self.datasource_type

        if self.hive_info_shrink is not None:
            result['HiveInfo'] = self.hive_info_shrink

        if self.kafka_info_shrink is not None:
            result['KafkaInfo'] = self.kafka_info_shrink

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.polar_dbmysql_info_shrink is not None:
            result['PolarDBMysqlInfo'] = self.polar_dbmysql_info_shrink

        if self.polar_dbxinfo_shrink is not None:
            result['PolarDBXInfo'] = self.polar_dbxinfo_shrink

        if self.rds_mysql_info_shrink is not None:
            result['RdsMysqlInfo'] = self.rds_mysql_info_shrink

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.sls_info_shrink is not None:
            result['SlsInfo'] = self.sls_info_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DatabricksInfo') is not None:
            self.databricks_info_shrink = m.get('DatabricksInfo')

        if m.get('DatasourceDescription') is not None:
            self.datasource_description = m.get('DatasourceDescription')

        if m.get('DatasourceName') is not None:
            self.datasource_name = m.get('DatasourceName')

        if m.get('DatasourceType') is not None:
            self.datasource_type = m.get('DatasourceType')

        if m.get('HiveInfo') is not None:
            self.hive_info_shrink = m.get('HiveInfo')

        if m.get('KafkaInfo') is not None:
            self.kafka_info_shrink = m.get('KafkaInfo')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('PolarDBMysqlInfo') is not None:
            self.polar_dbmysql_info_shrink = m.get('PolarDBMysqlInfo')

        if m.get('PolarDBXInfo') is not None:
            self.polar_dbxinfo_shrink = m.get('PolarDBXInfo')

        if m.get('RdsMysqlInfo') is not None:
            self.rds_mysql_info_shrink = m.get('RdsMysqlInfo')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SlsInfo') is not None:
            self.sls_info_shrink = m.get('SlsInfo')

        return self

