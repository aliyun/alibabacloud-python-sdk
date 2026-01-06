# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class CreateApsDatasoureRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        databricks_info: main_models.CreateApsDatasoureRequestDatabricksInfo = None,
        datasource_description: str = None,
        datasource_name: str = None,
        datasource_type: str = None,
        hive_info: main_models.CreateApsDatasoureRequestHiveInfo = None,
        kafka_info: main_models.CreateApsDatasoureRequestKafkaInfo = None,
        mode: str = None,
        polar_dbmysql_info: main_models.CreateApsDatasoureRequestPolarDBMysqlInfo = None,
        polar_dbxinfo: main_models.CreateApsDatasoureRequestPolarDBXInfo = None,
        rds_mysql_info: main_models.CreateApsDatasoureRequestRdsMysqlInfo = None,
        region_id: str = None,
        sls_info: main_models.CreateApsDatasoureRequestSlsInfo = None,
    ):
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The information about the Databricks data source.
        self.databricks_info = databricks_info
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
        self.hive_info = hive_info
        # The information about the source Apache Kafka instance.
        self.kafka_info = kafka_info
        # The mode.
        self.mode = mode
        # The information about the source PolarDB for MySQL cluster.
        self.polar_dbmysql_info = polar_dbmysql_info
        # The information about the source PolarDB-X instance.
        self.polar_dbxinfo = polar_dbxinfo
        # The information about the source ApsaraDB RDS for MySQL instance.
        self.rds_mysql_info = rds_mysql_info
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The information about the source Simple Log Service (SLS) instance or cluster.
        self.sls_info = sls_info

    def validate(self):
        if self.databricks_info:
            self.databricks_info.validate()
        if self.hive_info:
            self.hive_info.validate()
        if self.kafka_info:
            self.kafka_info.validate()
        if self.polar_dbmysql_info:
            self.polar_dbmysql_info.validate()
        if self.polar_dbxinfo:
            self.polar_dbxinfo.validate()
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

        if self.databricks_info is not None:
            result['DatabricksInfo'] = self.databricks_info.to_map()

        if self.datasource_description is not None:
            result['DatasourceDescription'] = self.datasource_description

        if self.datasource_name is not None:
            result['DatasourceName'] = self.datasource_name

        if self.datasource_type is not None:
            result['DatasourceType'] = self.datasource_type

        if self.hive_info is not None:
            result['HiveInfo'] = self.hive_info.to_map()

        if self.kafka_info is not None:
            result['KafkaInfo'] = self.kafka_info.to_map()

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.polar_dbmysql_info is not None:
            result['PolarDBMysqlInfo'] = self.polar_dbmysql_info.to_map()

        if self.polar_dbxinfo is not None:
            result['PolarDBXInfo'] = self.polar_dbxinfo.to_map()

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

        if m.get('DatabricksInfo') is not None:
            temp_model = main_models.CreateApsDatasoureRequestDatabricksInfo()
            self.databricks_info = temp_model.from_map(m.get('DatabricksInfo'))

        if m.get('DatasourceDescription') is not None:
            self.datasource_description = m.get('DatasourceDescription')

        if m.get('DatasourceName') is not None:
            self.datasource_name = m.get('DatasourceName')

        if m.get('DatasourceType') is not None:
            self.datasource_type = m.get('DatasourceType')

        if m.get('HiveInfo') is not None:
            temp_model = main_models.CreateApsDatasoureRequestHiveInfo()
            self.hive_info = temp_model.from_map(m.get('HiveInfo'))

        if m.get('KafkaInfo') is not None:
            temp_model = main_models.CreateApsDatasoureRequestKafkaInfo()
            self.kafka_info = temp_model.from_map(m.get('KafkaInfo'))

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('PolarDBMysqlInfo') is not None:
            temp_model = main_models.CreateApsDatasoureRequestPolarDBMysqlInfo()
            self.polar_dbmysql_info = temp_model.from_map(m.get('PolarDBMysqlInfo'))

        if m.get('PolarDBXInfo') is not None:
            temp_model = main_models.CreateApsDatasoureRequestPolarDBXInfo()
            self.polar_dbxinfo = temp_model.from_map(m.get('PolarDBXInfo'))

        if m.get('RdsMysqlInfo') is not None:
            temp_model = main_models.CreateApsDatasoureRequestRdsMysqlInfo()
            self.rds_mysql_info = temp_model.from_map(m.get('RdsMysqlInfo'))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SlsInfo') is not None:
            temp_model = main_models.CreateApsDatasoureRequestSlsInfo()
            self.sls_info = temp_model.from_map(m.get('SlsInfo'))

        return self

class CreateApsDatasoureRequestSlsInfo(DaraModel):
    def __init__(
        self,
        across: bool = None,
        across_role: str = None,
        across_uid: str = None,
        project: str = None,
        source_region_id: str = None,
        store: str = None,
    ):
        # Specifies whether the data source is a cross-account resource.
        self.across = across
        # The name of the cross-account role.
        self.across_role = across_role
        # The cross-account UID.
        self.across_uid = across_uid
        # The SLS project.
        self.project = project
        # The region ID.
        self.source_region_id = source_region_id
        # The name of the SLS Logstore.
        self.store = store

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

        if self.project is not None:
            result['Project'] = self.project

        if self.source_region_id is not None:
            result['SourceRegionId'] = self.source_region_id

        if self.store is not None:
            result['Store'] = self.store

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Across') is not None:
            self.across = m.get('Across')

        if m.get('AcrossRole') is not None:
            self.across_role = m.get('AcrossRole')

        if m.get('AcrossUid') is not None:
            self.across_uid = m.get('AcrossUid')

        if m.get('Project') is not None:
            self.project = m.get('Project')

        if m.get('SourceRegionId') is not None:
            self.source_region_id = m.get('SourceRegionId')

        if m.get('Store') is not None:
            self.store = m.get('Store')

        return self

class CreateApsDatasoureRequestRdsMysqlInfo(DaraModel):
    def __init__(
        self,
        connect_url: str = None,
        instance_id: str = None,
        password: str = None,
        region_id: str = None,
        security_group: str = None,
        user_name: str = None,
    ):
        # The URL used to connect to the read-only instance.
        self.connect_url = connect_url
        # The instance ID.
        self.instance_id = instance_id
        # The password of the database account of the instance.
        self.password = password
        # The region ID.
        self.region_id = region_id
        # The security group ID.
        self.security_group = security_group
        # The name of the database account of the instance.
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

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.password is not None:
            result['Password'] = self.password

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.security_group is not None:
            result['SecurityGroup'] = self.security_group

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectUrl') is not None:
            self.connect_url = m.get('ConnectUrl')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SecurityGroup') is not None:
            self.security_group = m.get('SecurityGroup')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

class CreateApsDatasoureRequestPolarDBXInfo(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # The instance ID.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

class CreateApsDatasoureRequestPolarDBMysqlInfo(DaraModel):
    def __init__(
        self,
        across: bool = None,
        across_role: str = None,
        across_uid: str = None,
        connect_url: str = None,
        instance_id: str = None,
        password: str = None,
        region_id: str = None,
        security_group: str = None,
        user_name: str = None,
    ):
        # Specifies whether the data source is a cross-account resource. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.across = across
        # The name of the cross-account role.
        self.across_role = across_role
        # The cross-account UID.
        self.across_uid = across_uid
        # The URL used to connect to the custom ApsaraDB RDS for MySQL instance.
        self.connect_url = connect_url
        # The instance ID.
        self.instance_id = instance_id
        # The password.
        self.password = password
        # The region ID.
        self.region_id = region_id
        # The security group ID.
        self.security_group = security_group
        # The username used to access the instance.
        self.user_name = user_name

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

        if self.connect_url is not None:
            result['ConnectUrl'] = self.connect_url

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.password is not None:
            result['Password'] = self.password

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.security_group is not None:
            result['SecurityGroup'] = self.security_group

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Across') is not None:
            self.across = m.get('Across')

        if m.get('AcrossRole') is not None:
            self.across_role = m.get('AcrossRole')

        if m.get('AcrossUid') is not None:
            self.across_uid = m.get('AcrossUid')

        if m.get('ConnectUrl') is not None:
            self.connect_url = m.get('ConnectUrl')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SecurityGroup') is not None:
            self.security_group = m.get('SecurityGroup')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

class CreateApsDatasoureRequestKafkaInfo(DaraModel):
    def __init__(
        self,
        kafka_cluster_id: str = None,
        kafka_topic: str = None,
    ):
        # The ID of the Apache Kafka instance.
        self.kafka_cluster_id = kafka_cluster_id
        # The topic of the Apache Kafka instance.
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

class CreateApsDatasoureRequestHiveInfo(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        host_config: str = None,
        meta_store_uri: str = None,
        security_group: str = None,
        vswitch: str = None,
    ):
        # The cluster ID.
        self.cluster_id = cluster_id
        # The configuration of the host.
        self.host_config = host_config
        # The URL of the Hive Metastore.
        self.meta_store_uri = meta_store_uri
        # The security group ID.
        self.security_group = security_group
        # The vSwitch ID.
        self.vswitch = vswitch

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.host_config is not None:
            result['HostConfig'] = self.host_config

        if self.meta_store_uri is not None:
            result['MetaStoreUri'] = self.meta_store_uri

        if self.security_group is not None:
            result['SecurityGroup'] = self.security_group

        if self.vswitch is not None:
            result['Vswitch'] = self.vswitch

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('HostConfig') is not None:
            self.host_config = m.get('HostConfig')

        if m.get('MetaStoreUri') is not None:
            self.meta_store_uri = m.get('MetaStoreUri')

        if m.get('SecurityGroup') is not None:
            self.security_group = m.get('SecurityGroup')

        if m.get('Vswitch') is not None:
            self.vswitch = m.get('Vswitch')

        return self

class CreateApsDatasoureRequestDatabricksInfo(DaraModel):
    def __init__(
        self,
        access_token: str = None,
        workspace_url: str = None,
    ):
        # The token that is used to access Databricks.
        self.access_token = access_token
        # The URL of the workspace.
        self.workspace_url = workspace_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_token is not None:
            result['AccessToken'] = self.access_token

        if self.workspace_url is not None:
            result['WorkspaceURL'] = self.workspace_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')

        if m.get('WorkspaceURL') is not None:
            self.workspace_url = m.get('WorkspaceURL')

        return self

