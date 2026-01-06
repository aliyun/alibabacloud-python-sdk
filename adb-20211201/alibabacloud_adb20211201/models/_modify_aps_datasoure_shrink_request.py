# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyApsDatasoureShrinkRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        datasource_description: str = None,
        datasource_id: int = None,
        datasource_name: str = None,
        kafka_info_shrink: str = None,
        lakehouse_id_shrink: str = None,
        polar_dbmysql_info_shrink: str = None,
        rds_mysql_info_shrink: str = None,
        region_id: str = None,
        sls_info_shrink: str = None,
    ):
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The description of the data source.
        self.datasource_description = datasource_description
        # The data source ID.
        # 
        # This parameter is required.
        self.datasource_id = datasource_id
        # The name of the data source.
        self.datasource_name = datasource_name
        # The information about the Kafka instance.
        self.kafka_info_shrink = kafka_info_shrink
        # The lakehouse ID.
        self.lakehouse_id_shrink = lakehouse_id_shrink
        # The parameter is no longer supported.
        self.polar_dbmysql_info_shrink = polar_dbmysql_info_shrink
        # The parameter is no longer supported.
        self.rds_mysql_info_shrink = rds_mysql_info_shrink
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The information about Simple Log Service (SLS).
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

        if self.datasource_description is not None:
            result['DatasourceDescription'] = self.datasource_description

        if self.datasource_id is not None:
            result['DatasourceId'] = self.datasource_id

        if self.datasource_name is not None:
            result['DatasourceName'] = self.datasource_name

        if self.kafka_info_shrink is not None:
            result['KafkaInfo'] = self.kafka_info_shrink

        if self.lakehouse_id_shrink is not None:
            result['LakehouseId'] = self.lakehouse_id_shrink

        if self.polar_dbmysql_info_shrink is not None:
            result['PolarDBMysqlInfo'] = self.polar_dbmysql_info_shrink

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

        if m.get('DatasourceDescription') is not None:
            self.datasource_description = m.get('DatasourceDescription')

        if m.get('DatasourceId') is not None:
            self.datasource_id = m.get('DatasourceId')

        if m.get('DatasourceName') is not None:
            self.datasource_name = m.get('DatasourceName')

        if m.get('KafkaInfo') is not None:
            self.kafka_info_shrink = m.get('KafkaInfo')

        if m.get('LakehouseId') is not None:
            self.lakehouse_id_shrink = m.get('LakehouseId')

        if m.get('PolarDBMysqlInfo') is not None:
            self.polar_dbmysql_info_shrink = m.get('PolarDBMysqlInfo')

        if m.get('RdsMysqlInfo') is not None:
            self.rds_mysql_info_shrink = m.get('RdsMysqlInfo')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SlsInfo') is not None:
            self.sls_info_shrink = m.get('SlsInfo')

        return self

