# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class ModifyApsDatasoureRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        datasource_description: str = None,
        datasource_id: int = None,
        datasource_name: str = None,
        kafka_info: main_models.ModifyApsDatasoureRequestKafkaInfo = None,
        lakehouse_id: main_models.ModifyApsDatasoureRequestLakehouseId = None,
        polar_dbmysql_info: main_models.ModifyApsDatasoureRequestPolarDBMysqlInfo = None,
        rds_mysql_info: main_models.ModifyApsDatasoureRequestRdsMysqlInfo = None,
        region_id: str = None,
        sls_info: main_models.ModifyApsDatasoureRequestSlsInfo = None,
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
        self.kafka_info = kafka_info
        # The lakehouse ID.
        self.lakehouse_id = lakehouse_id
        # The parameter is no longer supported.
        self.polar_dbmysql_info = polar_dbmysql_info
        # The parameter is no longer supported.
        self.rds_mysql_info = rds_mysql_info
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The information about Simple Log Service (SLS).
        self.sls_info = sls_info

    def validate(self):
        if self.kafka_info:
            self.kafka_info.validate()
        if self.lakehouse_id:
            self.lakehouse_id.validate()
        if self.polar_dbmysql_info:
            self.polar_dbmysql_info.validate()
        if self.rds_mysql_info:
            self.rds_mysql_info.validate()
        if self.sls_info:
            self.sls_info.validate()

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

        if self.kafka_info is not None:
            result['KafkaInfo'] = self.kafka_info.to_map()

        if self.lakehouse_id is not None:
            result['LakehouseId'] = self.lakehouse_id.to_map()

        if self.polar_dbmysql_info is not None:
            result['PolarDBMysqlInfo'] = self.polar_dbmysql_info.to_map()

        if self.rds_mysql_info is not None:
            result['RdsMysqlInfo'] = self.rds_mysql_info.to_map()

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.sls_info is not None:
            result['SlsInfo'] = self.sls_info.to_map()

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
            temp_model = main_models.ModifyApsDatasoureRequestKafkaInfo()
            self.kafka_info = temp_model.from_map(m.get('KafkaInfo'))

        if m.get('LakehouseId') is not None:
            temp_model = main_models.ModifyApsDatasoureRequestLakehouseId()
            self.lakehouse_id = temp_model.from_map(m.get('LakehouseId'))

        if m.get('PolarDBMysqlInfo') is not None:
            temp_model = main_models.ModifyApsDatasoureRequestPolarDBMysqlInfo()
            self.polar_dbmysql_info = temp_model.from_map(m.get('PolarDBMysqlInfo'))

        if m.get('RdsMysqlInfo') is not None:
            temp_model = main_models.ModifyApsDatasoureRequestRdsMysqlInfo()
            self.rds_mysql_info = temp_model.from_map(m.get('RdsMysqlInfo'))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SlsInfo') is not None:
            temp_model = main_models.ModifyApsDatasoureRequestSlsInfo()
            self.sls_info = temp_model.from_map(m.get('SlsInfo'))

        return self

class ModifyApsDatasoureRequestSlsInfo(DaraModel):
    def __init__(
        self,
        across: bool = None,
        across_role: str = None,
        across_uid: str = None,
        source_region_id: str = None,
    ):
        # Specifies whether to use a cross-account resource as the data source. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.across = across
        # The name of the cross-account role.
        self.across_role = across_role
        # The cross-account UID.
        self.across_uid = across_uid
        # The region ID.
        self.source_region_id = source_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.across is not None:
            result['Across'] = self.across

        if self.across_role is not None:
            result['AcrossRole'] = self.across_role

        if self.across_uid is not None:
            result['AcrossUid'] = self.across_uid

        if self.source_region_id is not None:
            result['SourceRegionId'] = self.source_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Across') is not None:
            self.across = m.get('Across')

        if m.get('AcrossRole') is not None:
            self.across_role = m.get('AcrossRole')

        if m.get('AcrossUid') is not None:
            self.across_uid = m.get('AcrossUid')

        if m.get('SourceRegionId') is not None:
            self.source_region_id = m.get('SourceRegionId')

        return self

class ModifyApsDatasoureRequestRdsMysqlInfo(DaraModel):
    def __init__(
        self,
        connect_url: str = None,
        password: str = None,
        region_id: str = None,
        user_name: str = None,
    ):
        # The parameter is no longer supported.
        self.connect_url = connect_url
        # The parameter is no longer supported.
        self.password = password
        # The parameter is no longer supported.
        self.region_id = region_id
        # The parameter is no longer supported.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connect_url is not None:
            result['ConnectUrl'] = self.connect_url

        if self.password is not None:
            result['Password'] = self.password

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectUrl') is not None:
            self.connect_url = m.get('ConnectUrl')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

class ModifyApsDatasoureRequestPolarDBMysqlInfo(DaraModel):
    def __init__(
        self,
        connect_url: str = None,
        password: str = None,
        region_id: str = None,
        user_name: str = None,
    ):
        # The parameter is no longer supported.
        self.connect_url = connect_url
        # The parameter is no longer supported.
        self.password = password
        # The parameter is no longer supported.
        self.region_id = region_id
        # The parameter is no longer supported.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connect_url is not None:
            result['ConnectUrl'] = self.connect_url

        if self.password is not None:
            result['Password'] = self.password

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectUrl') is not None:
            self.connect_url = m.get('ConnectUrl')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

class ModifyApsDatasoureRequestLakehouseId(DaraModel):
    def __init__(
        self,
        security_group: str = None,
        vpc_id: str = None,
        vswitch: str = None,
    ):
        # The name of the security group.
        self.security_group = security_group
        # The virtual private cloud (VPC) ID.
        self.vpc_id = vpc_id
        # The name of the vSwitch.
        self.vswitch = vswitch

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.security_group is not None:
            result['SecurityGroup'] = self.security_group

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vswitch is not None:
            result['Vswitch'] = self.vswitch

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityGroup') is not None:
            self.security_group = m.get('SecurityGroup')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('Vswitch') is not None:
            self.vswitch = m.get('Vswitch')

        return self

class ModifyApsDatasoureRequestKafkaInfo(DaraModel):
    def __init__(
        self,
        kafka_cluster_id: str = None,
        kafka_topic: str = None,
    ):
        # The ID of the Kafka instance.
        self.kafka_cluster_id = kafka_cluster_id
        # The topic of the Kafka instance.
        self.kafka_topic = kafka_topic

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.kafka_cluster_id is not None:
            result['KafkaClusterId'] = self.kafka_cluster_id

        if self.kafka_topic is not None:
            result['KafkaTopic'] = self.kafka_topic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KafkaClusterId') is not None:
            self.kafka_cluster_id = m.get('KafkaClusterId')

        if m.get('KafkaTopic') is not None:
            self.kafka_topic = m.get('KafkaTopic')

        return self

