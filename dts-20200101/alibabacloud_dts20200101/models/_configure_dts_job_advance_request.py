# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import BinaryIO

from darabonba.model import DaraModel

class ConfigureDtsJobAdvanceRequest(DaraModel):
    def __init__(
        self,
        checkpoint: str = None,
        data_check_configure: str = None,
        data_initialization: bool = None,
        data_synchronization: bool = None,
        db_list: str = None,
        dedicated_cluster_id: str = None,
        delay_notice: bool = None,
        delay_phone: str = None,
        delay_rule_time: int = None,
        dest_ca_certificate_oss_url: str = None,
        dest_ca_certificate_password: str = None,
        dest_client_cert_oss_url: str = None,
        dest_client_key_oss_url: str = None,
        dest_client_password: str = None,
        dest_primary_vsw_id: str = None,
        dest_secondary_vsw_id: str = None,
        destination_endpoint_data_base_name: str = None,
        destination_endpoint_engine_name: str = None,
        destination_endpoint_ip: str = None,
        destination_endpoint_instance_id: str = None,
        destination_endpoint_instance_type: str = None,
        destination_endpoint_oracle_sid: str = None,
        destination_endpoint_owner_id: str = None,
        destination_endpoint_password: str = None,
        destination_endpoint_port: str = None,
        destination_endpoint_region: str = None,
        destination_endpoint_role: str = None,
        destination_endpoint_user_name: str = None,
        disaster_recovery_job: bool = None,
        dts_bis_label: str = None,
        dts_instance_id: str = None,
        dts_job_id: str = None,
        dts_job_name: str = None,
        error_notice: bool = None,
        error_phone: str = None,
        file_oss_url_object: BinaryIO = None,
        job_type: str = None,
        max_du: float = None,
        min_du: float = None,
        owner_id: str = None,
        region_id: str = None,
        reserve: str = None,
        resource_group_id: str = None,
        source_endpoint_database_name: str = None,
        source_endpoint_engine_name: str = None,
        source_endpoint_ip: str = None,
        source_endpoint_instance_id: str = None,
        source_endpoint_instance_type: str = None,
        source_endpoint_oracle_sid: str = None,
        source_endpoint_owner_id: str = None,
        source_endpoint_password: str = None,
        source_endpoint_port: str = None,
        source_endpoint_region: str = None,
        source_endpoint_role: str = None,
        source_endpoint_user_name: str = None,
        source_endpoint_vswitch_id: str = None,
        src_ca_certificate_oss_url: str = None,
        src_ca_certificate_password: str = None,
        src_client_cert_oss_url: str = None,
        src_client_key_oss_url: str = None,
        src_client_password: str = None,
        src_primary_vsw_id: str = None,
        src_secondary_vsw_id: str = None,
        structure_initialization: bool = None,
        synchronization_direction: str = None,
    ):
        # The start position for incremental data migration or the synchronization checkpoint, in the format of a UNIX timestamp. Unit: seconds.
        # 
        # > If you specify the **Checkpoint** parameter, make sure that no other running DTS instance has the same source database as the destination DTS instance.
        self.checkpoint = checkpoint
        # The parameters of the data validation node, in JSON character string format, such as parameter limits and alert configuration. For more information, see [DataCheckConfigure parameter description](https://help.aliyun.com/document_detail/459023.html).
        self.data_check_configure = data_check_configure
        # Specifies whether to perform full data migration or initial full data synchronization. Valid values:
        # 
        # - **true**: Yes. This is the default value.
        # - **false**: No.
        # 
        # > If **JobType** is set to **CHECK**, this parameter can only be set to **false**.
        # 
        # This parameter is required.
        self.data_initialization = data_initialization
        # Specifies whether to perform incremental data migration or synchronization. Valid values:
        # 
        # - **false**: No. This is the default value.
        # - **true**: Yes.
        # 
        # > If **JobType** is set to **CHECK**, this parameter can only be set to **false**.
        # 
        # This parameter is required.
        self.data_synchronization = data_synchronization
        # The objects to be migrated or synchronized, in JSON format. For more information, see [Objects of migration, synchronization, or change tracking tasks](https://help.aliyun.com/document_detail/209545.html).
        # 
        # - The maximum size of the DbList value is 1 MB.
        # - If DbList contains filter conditions, the total length of DbList (including filter conditions) cannot exceed 1 MB.
        # - For distributed tasks (such as migration or synchronization tasks with PolarDB-X 1.0 as the source), DbList is split based on physical shards and multiple subtasks are generated. The maximum size of DbList for each subtask is 1 MB.
        self.db_list = db_list
        # The ID of the DTS dedicated cluster.
        # 
        # > If you specify the ID of a dedicated cluster, the task is scheduled to the corresponding cluster.
        self.dedicated_cluster_id = dedicated_cluster_id
        # Specifies whether to monitor the latency status. Valid values:
        # 
        # - **true**: Yes.
        # - **false**: No.
        self.delay_notice = delay_notice
        # The mobile phone numbers for latency alerting of the contact. Separate multiple phone numbers with commas (,).
        # > - This parameter is supported only on the China site. Only the Chinese mainland phone numbers are supported, and a maximum of 10 phone numbers can be specified.
        # - The international site does not support phone alerting. You can only [configure alert rules for DTS tasks through the CloudMonitor platform to set alert rules](https://help.aliyun.com/document_detail/175876.html).
        self.delay_phone = delay_phone
        # The threshold for triggering latency alerts. Unit: seconds. The value must be an integer. Set the threshold based on your business requirements. To avoid alert fluctuations caused by network conditions or database loads, set the threshold to 10 seconds or more.
        # > This parameter is required when **DelayNotice** is set to **true**.
        self.delay_rule_time = delay_rule_time
        # The path of the CA certificate for SSL connection to the destination database.
        # 
        # > This feature is not supported. Do not specify this parameter.
        self.dest_ca_certificate_oss_url = dest_ca_certificate_oss_url
        # The password of the CA certificate for SSL connection to the destination database.
        # 
        # > This feature is not supported. Do not specify this parameter.
        self.dest_ca_certificate_password = dest_ca_certificate_password
        # The path of the client certificate for SSL connection to the destination database.
        # 
        # > This feature is not supported. Do not specify this parameter.
        self.dest_client_cert_oss_url = dest_client_cert_oss_url
        # The path of the client certificate private key for SSL connection to the destination database.
        # 
        # > This feature is not supported. Do not specify this parameter.
        self.dest_client_key_oss_url = dest_client_key_oss_url
        # The password of the client certificate private key for SSL connection to the destination database.
        # 
        # > This feature is not supported. Do not specify this parameter.
        self.dest_client_password = dest_client_password
        # The primary vSwitch of the VPC NAT gateway on the destination side.
        self.dest_primary_vsw_id = dest_primary_vsw_id
        # The secondary vSwitch of the VPC NAT gateway on the destination side.
        self.dest_secondary_vsw_id = dest_secondary_vsw_id
        # The name of the database to which the objects to be migrated belong in the destination instance.
        # > - This parameter is available and required only when the destination instance or destination database type is PolarDB for PostgreSQL (Compatible with Oracle), AnalyticDB for PostgreSQL, PostgreSQL, MaxCompute, or MongoDB.
        # - If the destination database is MaxCompute, specify the project of the MaxCompute instance.
        self.destination_endpoint_data_base_name = destination_endpoint_data_base_name
        # The database type of the destination instance. Valid values:
        # - **MYSQL**: MySQL database (including ApsaraDB RDS for MySQL and self-managed MySQL).
        # - **MARIADB**: ApsaraDB RDS for MariaDB.
        # - **PolarDB**: PolarDB for MySQL.
        # - **POLARDB_O**: PolarDB for PostgreSQL (Compatible with Oracle).
        # - **POLARDBX10**: PolarDB-X 1.0 (formerly DRDS).
        # - **POLARDBX20**: cloud-native distributed database PolarDB-X 2.0.
        # - **ORACLE**: self-managed Oracle.
        # - **PostgreSQL**: PostgreSQL database (including ApsaraDB RDS for PostgreSQL and self-managed PostgreSQL).
        # - **MSSQL**: SQL Server database (including ApsaraDB RDS for SQL Server and self-managed SQL Server).
        # - **ADS**: AnalyticDB for MySQL 2.0.
        # - **ADB30**: AnalyticDB for MySQL 3.0.
        # - **MONGODB**: MongoDB database (including self-managed MongoDB and ApsaraDB for MongoDB).
        # - **ROCKETMQ**: ApsaraMQ for RocketMQ.
        # - **GREENPLUM**: AnalyticDB for PostgreSQL.
        # - **KAFKA**: Kafka database (including MSMQ for Apache Kafka and self-managed Kafka).
        # - **DATAHUB**: Alibaba Cloud DataHub.
        # - **DB2**: self-managed Db2 for LUW.
        # - **AS400**: Db2 for i.
        # - **ODPS**: MaxCompute.
        # - **Tablestore**: Tablestore.
        # - **ELK**: Alibaba Cloud Elasticsearch.
        # - **REDIS**: Redis database, including self-managed Redis and Tair (Redis® OSS-Compatible).
        # - **LINDORM**: cloud-native multi-model database Lindorm.
        # 
        # > - Default value: **MYSQL**.
        # - If the database type of the destination instance is set to **KAFKA**, **MONGODB**, or **PolarDB**, you must also specify additional information in the Reserve parameter. For the metric description, see [Reserve parameter description](https://help.aliyun.com/document_detail/273111.html).
        self.destination_endpoint_engine_name = destination_endpoint_engine_name
        # The IP address of the destination instance.
        # > This parameter is available and required only when **DestinationEndpointInstanceType** is set to **OTHER**, **EXPRESS**, **DG**, or **CEN**.
        self.destination_endpoint_ip = destination_endpoint_ip
        # The ID of the destination instance.
        # 
        #  If the destination instance is an Alibaba Cloud database (such as ApsaraDB RDS for MySQL), specify the ID of the Alibaba Cloud database instance (such as the ApsaraDB RDS for MySQL instance ID).
        # 
        #  If the destination instance is a self-managed database, the value of this parameter varies based on the value of **DestinationEndpointInstanceType**. Example:
        # 
        # 
        # - **ECS**: Specify the ID of the ECS instance.
        # - **DG**: Specify the ID of the database gateway.
        # - **EXPRESS** or **CEN**: Specify the ID of the VPC that is connected to the source database.
        # 
        # > If the value is **CEN**, you must also specify the CEN instance ID in the Reserve parameter. For the metric description, see [Reserve parameter description](https://help.aliyun.com/document_detail/273111.html).
        self.destination_endpoint_instance_id = destination_endpoint_instance_id
        # The target instance type. Valid values:
        # 
        # **Alibaba Cloud databases**
        # - **RDS**: ApsaraDB RDS for MySQL, ApsaraDB RDS for SQL Server, ApsaraDB RDS for PostgreSQL, or ApsaraDB RDS for MariaDB.
        # - **PolarDB**: PolarDB for MySQL.
        # - **DISTRIBUTED_POLARDBX10**: PolarDB-X 1.0 (formerly DRDS).
        # - **POLARDBX20**: PolarDB-X 2.0.
        # - **REDIS**: Tair (Redis® OSS-Compatible).
        # - **ADS**: AnalyticDB for MySQL 2.0 or 3.0.
        # - **MONGODB**: ApsaraDB for MongoDB.
        # - **ROCKETMQ**: ApsaraMQ for RocketMQ.
        # - **GREENPLUM**: AnalyticDB for PostgreSQL.
        # - **DATAHUB**: Alibaba Cloud DataHub platform.
        # - **ELK**: Alibaba Cloud Elasticsearch.
        # - **Tablestore**: Tablestore.
        # - **ODPS**: MaxCompute.
        # - **LINDORM**: cloud-native multi-model database Lindorm.
        # 
        # **Self-managed databases**
        # - **OTHER**: self-managed database with a public IP address.
        # - **ECS**: self-managed database hosted on ECS.
        # - **EXPRESS**: self-managed database connected over Express Connect.
        # - **CEN**: self-managed database connected over Cloud Enterprise Network (CEN).
        # - **DG**: self-managed database connected over Database Gateway.
        # 
        # > - If the destination instance is a PolarDB for PostgreSQL (Compatible with Oracle) cluster, set this parameter to **OTHER** or **EXPRESS** to connect the cluster as a self-managed database over a public IP address or Express Connect.
        # - If the destination instance is MSMQ for Apache Kafka, set this parameter to **ECS** or **EXPRESS** to connect the instance as a self-managed database over ECS or Express Connect.
        # - For information about supported source and destination database combinations, see <props="china">[Supported databases](https://help.aliyun.com/document_detail/131497.html)<props="intl">[Supported source and destination databases](https://help.aliyun.com/document_detail/176064.html).
        # - If the destination instance is a self-managed database, you must also execute the required preparations. For more information, see [Preparations overview](https://help.aliyun.com/document_detail/146958.html).
        # 
        # This parameter is required.
        self.destination_endpoint_instance_type = destination_endpoint_instance_type
        # The SID of the Oracle database.
        # > This parameter is available and required only when **DestinationEndpointEngineName** is set to **Oracle** and the Oracle database is a non-RAC instance.
        self.destination_endpoint_oracle_sid = destination_endpoint_oracle_sid
        # The Alibaba Cloud account ID to which the destination ApsaraDB RDS for MySQL instance belongs.
        # > - This parameter can be configured only when the destination instance is ApsaraDB RDS for MySQL.
        # - Specifying this parameter indicates you execute a cross-account data migration or synchronization. You must also specify the **DestinationEndpointRole** parameter.
        self.destination_endpoint_owner_id = destination_endpoint_owner_id
        # The password of the destination database account.
        # > If the destination database is MaxCompute, specify the AccessKey secret of the Alibaba Cloud account. For more information about how to obtain the AccessKey secret, see [Create an AccessKey pair](https://help.aliyun.com/document_detail/116401.html).
        self.destination_endpoint_password = destination_endpoint_password
        # The database service port of the destination instance.
        # > This parameter is available and required only when the destination instance is a self-managed database.
        self.destination_endpoint_port = destination_endpoint_port
        # The region of the destination instance. For more information, see [Supported regions](https://help.aliyun.com/document_detail/141033.html).
        # > If the destination instance is an Alibaba Cloud database, this parameter is required.
        self.destination_endpoint_region = destination_endpoint_region
        # The name of the RAM role configured for the Alibaba Cloud account to which the destination instance belongs.
        # > This parameter is required for cross-account data migration or synchronization. For information about the permissions and authorization method required for this role, see [Configure RAM authorization for cross-account data migration or synchronization](https://help.aliyun.com/document_detail/48468.html).
        self.destination_endpoint_role = destination_endpoint_role
        # The database account of the destination database.
        # > - In most cases, you must specify the database account of the destination database.
        # - The required permissions vary depending on the database being migrated or synchronized. For more information, see [Prepare database accounts for data migration](https://help.aliyun.com/document_detail/175878.html) and [Prepare database accounts for data synchronization](https://help.aliyun.com/document_detail/213152.html).
        # - If the destination database is MaxCompute, specify the AccessKey ID of the Alibaba Cloud account. For more information about how to obtain the AccessKey ID, see [Create an AccessKey pair](https://help.aliyun.com/document_detail/116401.html).
        self.destination_endpoint_user_name = destination_endpoint_user_name
        # Specifies whether this is a disaster recovery instance. Valid values:
        # 
        # - **true**: Yes.
        # - **false**: No.
        self.disaster_recovery_job = disaster_recovery_job
        # The environment label of the DTS instance. Valid values:
        # 
        # - **normal**: normal
        # - **online**: online.
        self.dts_bis_label = dts_bis_label
        # The ID of the migration or synchronization instance.
        # > You can call [DescribeDtsJobs](https://help.aliyun.com/document_detail/209702.html) to query the instance ID.
        self.dts_instance_id = dts_instance_id
        # The ID of the migration or synchronization task.
        # > You can call [DescribeDtsJobs](https://help.aliyun.com/document_detail/209702.html) to query the task ID.
        self.dts_job_id = dts_job_id
        # The name of the DTS instance.
        # 
        # This parameter is required.
        self.dts_job_name = dts_job_name
        # Specifies whether to monitor the error status. Valid values:
        # 
        # - **true**: Yes.
        # - **false**: No.
        self.error_notice = error_notice
        # The mobile phone numbers for error alerting of the contact. Separate multiple phone numbers with commas (,).
        # > - This parameter is supported only on the China site. Only the Chinese mainland phone numbers are supported, and a maximum of 10 phone numbers can be specified.
        # - The international site does not support phone alerting. You can only [configure alert rules for DTS tasks through the CloudMonitor platform to set alert rules](https://help.aliyun.com/document_detail/175876.html).
        self.error_phone = error_phone
        # The OSS URL of the task file.
        self.file_oss_url_object = file_oss_url_object
        # The type of the node. Valid values:
        # 
        # - **MIGRATION**: data migration.
        # - **SYNC**: data synchronization.
        # - **CHECK**: data validation (purchased separately).
        # 
        # > - If the value is **MIGRATION** or **SYNC**, you can also configure a data validation node within the migration or synchronization instance.
        # - To configure a data validation node, you must also specify the **DataCheckConfigure** parameter.
        # 
        # This parameter is required.
        self.job_type = job_type
        # The maximum number of DTS Units (DUs).
        # 
        # > This parameter is supported only for serverless instances.
        self.max_du = max_du
        # The minimum number of DTS Units (DUs).
        # 
        # > This parameter is supported only for serverless instances.
        self.min_du = min_du
        self.owner_id = owner_id
        # The region ID of the DTS instance. For more information, see [Supported regions](https://help.aliyun.com/document_detail/141033.html).
        self.region_id = region_id
        # The reserved parameter of DTS, in JSON character string format. You can specify this parameter to add information about the source and destination databases (such as the data storage format of the destination Kafka database, the CEN instance ID, and ETL feature configurations). For more information, see [Reserve parameter description](https://help.aliyun.com/document_detail/273111.html).
        self.reserve = reserve
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The name of the database to which the objects to be migrated belong in the source instance.
        # > This parameter is available and required only when the source instance or its database type is PolarDB for PostgreSQL (Compatible with Oracle), PostgreSQL, or MongoDB.
        self.source_endpoint_database_name = source_endpoint_database_name
        # The database type of the source instance. Valid values:
        # - **MYSQL**: MySQL database (including ApsaraDB RDS for MySQL and self-managed MySQL).
        # - **MARIADB**: ApsaraDB RDS for MariaDB.
        # - **PolarDB**: PolarDB for MySQL.
        # - **POLARDB_O**: PolarDB for PostgreSQL (Compatible with Oracle).
        # - **POLARDBX10**: PolarDB-X 1.0 (formerly DRDS).
        # - **POLARDBX20**: cloud-native distributed database PolarDB-X 2.0.
        # - **ADB30**: AnalyticDB for MySQL 3.0.
        # - **ORACLE**: self-managed Oracle.
        # - **POSTGRESQL**: PostgreSQL database (including ApsaraDB RDS for PostgreSQL and self-managed PostgreSQL).
        # - **MSSQL**: SQL Server database (including ApsaraDB RDS for SQL Server and self-managed SQL Server).
        # - **MONGODB**: MongoDB database (including self-managed MongoDB and ApsaraDB for MongoDB).
        # - **DB2**: self-managed Db2 for LUW.
        # - **AS400**: self-managed Db2 for i.
        # - **DMSPOLARDB**: Data Management (DMS) logical database.
        # - **HBASE**: self-managed HBase database.
        # - **TERADATA**: Teradata database.
        # - **TiDB**: TiDB database.
        # - **REDIS**: Redis database, including self-managed Redis and Tair (Redis® OSS-Compatible).
        # - **LINDORM**: Lindorm.
        # 
        # 
        # > - Default value: **MYSQL**.
        #  - If the database type of the source instance is set to **MONGODB**, you must also specify additional information in the Reserve parameter. For the metric description, see [Reserve parameter description](https://help.aliyun.com/document_detail/273111.html).
        self.source_endpoint_engine_name = source_endpoint_engine_name
        # The IP address of the source instance.
        # > This parameter is available and required only when **SourceEndpointInstanceType** is set to **OTHER**, **EXPRESS**, **DG**, or **CEN**.
        self.source_endpoint_ip = source_endpoint_ip
        # The ID of the source instance.
        # 
        # If the source instance is an Alibaba Cloud database (such as ApsaraDB RDS for MySQL), specify the ID of the Alibaba Cloud database instance (such as the ApsaraDB RDS for MySQL instance ID).
        # 
        # If the source instance is a self-managed database, the value of this parameter varies based on the value of **SourceEndpointInstanceType**. Example:
        # 
        # - **ECS**: Specify the ID of the ECS instance.
        # - **DG**: Specify the ID of the database gateway.
        # - **EXPRESS** or **CEN**: Specify the ID of the VPC that is connected to the source database.
        # 
        # > If the value is **CEN**, you must also specify the CEN instance ID in the Reserve parameter. For the metric description, see [Reserve parameter description](https://help.aliyun.com/document_detail/273111.html).
        self.source_endpoint_instance_id = source_endpoint_instance_id
        # The type of the source instance. Valid values:
        # 
        # **Alibaba Cloud databases**
        # 
        # - **RDS**: ApsaraDB RDS for MySQL, ApsaraDB RDS for SQL Server, ApsaraDB RDS for PostgreSQL, or ApsaraDB RDS for MariaDB.
        # - **PolarDB**: PolarDB for MySQL.
        # - **ADS**: AnalyticDB for MySQL.
        # - **REDIS**: Tair (Redis® OSS-Compatible).
        # - **DISTRIBUTED_POLARDBX10**: PolarDB-X 1.0 (formerly DRDS).
        # - **POLARDBX20**: PolarDB-X 2.0.
        # - **MONGODB**: ApsaraDB for MongoDB.
        # - **DISTRIBUTED_DMSLOGICDB**: Data Management (DMS) logical database.
        # - **LINDORM**: Lindorm.
        # 
        # **Self-managed databases**
        # - **OTHER**: self-managed database with a public IP address.
        # - **ECS**: self-managed database hosted on ECS.
        # - **EXPRESS**: self-managed database connected over Express Connect.
        # - **CEN**: self-managed database connected over Cloud Enterprise Network (CEN).
        # - **DG**: self-managed database connected over Database Gateway.
        # 
        # 
        # > - If the source instance is a PolarDB for PostgreSQL (Compatible with Oracle) cluster, set this parameter to **OTHER** or **EXPRESS** to connect the cluster as a self-managed database over a public IP address or Express Connect.
        # - For information about supported source and destination database combinations, see [Supported databases](https://help.aliyun.com/document_detail/131497.html).
        # - If the source instance is a self-managed database, you must complete the required preparations. For more information, see [Preparations overview](https://help.aliyun.com/document_detail/130607.html).
        # 
        # This parameter is required.
        self.source_endpoint_instance_type = source_endpoint_instance_type
        # The SID of the Oracle database.
        # > This parameter is available and required only when **SourceEndpointEngineName** is set to **Oracle** and the Oracle database is a non-RAC instance.
        self.source_endpoint_oracle_sid = source_endpoint_oracle_sid
        # The Alibaba Cloud account ID to which the source instance belongs.
        # > Specifying this parameter indicates you execute a cross-account data migration or synchronization. You must also specify the **SourceEndpointRole** parameter.
        self.source_endpoint_owner_id = source_endpoint_owner_id
        # The password of the source database account.
        self.source_endpoint_password = source_endpoint_password
        # The database service port of the source instance.
        # > This parameter is available and required only when the source instance is a self-managed database.
        self.source_endpoint_port = source_endpoint_port
        # The region of the source instance. For details, see [Supported regions](https://help.aliyun.com/document_detail/141033.html).
        # > If the source instance is an Alibaba Cloud database, this parameter is required.
        self.source_endpoint_region = source_endpoint_region
        # The name of the RAM role configured for the Alibaba Cloud account to which the source instance belongs.
        # > This parameter is required for cross-account data migration or synchronization. For information about the permissions and authorization method required for this role, see [Configure RAM authorization for cross-account data migration or synchronization](https://help.aliyun.com/document_detail/48468.html).
        self.source_endpoint_role = source_endpoint_role
        # The database account of the source database.
        # > - In most cases, you must specify the database account of the source database.
        # - The required permissions vary depending on the database being migrated or synchronized. For more information, see [Prepare database accounts for data migration](https://help.aliyun.com/document_detail/175878.html) and [Prepare database accounts for data synchronization](https://help.aliyun.com/document_detail/213152.html).
        self.source_endpoint_user_name = source_endpoint_user_name
        # The vSwitch instance ID for the data delivery link.
        self.source_endpoint_vswitch_id = source_endpoint_vswitch_id
        # The path of the CA certificate for SSL connection to the source database.
        # 
        # > This feature is not supported. Do not specify this parameter.
        self.src_ca_certificate_oss_url = src_ca_certificate_oss_url
        # The password of the CA certificate for SSL connection to the source database.
        # 
        # > This feature is not supported. Do not specify this parameter.
        self.src_ca_certificate_password = src_ca_certificate_password
        # The path of the client certificate for SSL connection to the source database.
        # 
        # > This feature is not supported. Do not specify this parameter.
        self.src_client_cert_oss_url = src_client_cert_oss_url
        # The path of the client certificate private key for SSL connection to the source database.
        # 
        # > This feature is not supported. Do not specify this parameter.
        self.src_client_key_oss_url = src_client_key_oss_url
        # The password of the client certificate private key for SSL connection to the source database.
        # 
        # > This feature is not supported. Do not specify this parameter.
        self.src_client_password = src_client_password
        # The primary vSwitch of the VPC NAT gateway on the source side.
        self.src_primary_vsw_id = src_primary_vsw_id
        # The secondary vSwitch of the VPC NAT gateway on the source side.
        self.src_secondary_vsw_id = src_secondary_vsw_id
        # Specifies whether to perform schema migration or initial schema synchronization. Valid values:
        # 
        # - **true**: Yes. This is the default value.
        # - **false**: No.
        # 
        # > If **JobType** is set to **CHECK**, this parameter can only be set to **false**.
        # 
        # This parameter is required.
        self.structure_initialization = structure_initialization
        # The synchronization direction. Valid values:
        # 
        # - **Forward**: forward.
        # - **Reverse**: reverse.
        # 
        # > - Default value: **Forward**.
        # - The value **Reverse** takes effect only when the synchronization topology of the synchronization task is two-way synchronization.
        self.synchronization_direction = synchronization_direction

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.checkpoint is not None:
            result['Checkpoint'] = self.checkpoint

        if self.data_check_configure is not None:
            result['DataCheckConfigure'] = self.data_check_configure

        if self.data_initialization is not None:
            result['DataInitialization'] = self.data_initialization

        if self.data_synchronization is not None:
            result['DataSynchronization'] = self.data_synchronization

        if self.db_list is not None:
            result['DbList'] = self.db_list

        if self.dedicated_cluster_id is not None:
            result['DedicatedClusterId'] = self.dedicated_cluster_id

        if self.delay_notice is not None:
            result['DelayNotice'] = self.delay_notice

        if self.delay_phone is not None:
            result['DelayPhone'] = self.delay_phone

        if self.delay_rule_time is not None:
            result['DelayRuleTime'] = self.delay_rule_time

        if self.dest_ca_certificate_oss_url is not None:
            result['DestCaCertificateOssUrl'] = self.dest_ca_certificate_oss_url

        if self.dest_ca_certificate_password is not None:
            result['DestCaCertificatePassword'] = self.dest_ca_certificate_password

        if self.dest_client_cert_oss_url is not None:
            result['DestClientCertOssUrl'] = self.dest_client_cert_oss_url

        if self.dest_client_key_oss_url is not None:
            result['DestClientKeyOssUrl'] = self.dest_client_key_oss_url

        if self.dest_client_password is not None:
            result['DestClientPassword'] = self.dest_client_password

        if self.dest_primary_vsw_id is not None:
            result['DestPrimaryVswId'] = self.dest_primary_vsw_id

        if self.dest_secondary_vsw_id is not None:
            result['DestSecondaryVswId'] = self.dest_secondary_vsw_id

        if self.destination_endpoint_data_base_name is not None:
            result['DestinationEndpointDataBaseName'] = self.destination_endpoint_data_base_name

        if self.destination_endpoint_engine_name is not None:
            result['DestinationEndpointEngineName'] = self.destination_endpoint_engine_name

        if self.destination_endpoint_ip is not None:
            result['DestinationEndpointIP'] = self.destination_endpoint_ip

        if self.destination_endpoint_instance_id is not None:
            result['DestinationEndpointInstanceID'] = self.destination_endpoint_instance_id

        if self.destination_endpoint_instance_type is not None:
            result['DestinationEndpointInstanceType'] = self.destination_endpoint_instance_type

        if self.destination_endpoint_oracle_sid is not None:
            result['DestinationEndpointOracleSID'] = self.destination_endpoint_oracle_sid

        if self.destination_endpoint_owner_id is not None:
            result['DestinationEndpointOwnerID'] = self.destination_endpoint_owner_id

        if self.destination_endpoint_password is not None:
            result['DestinationEndpointPassword'] = self.destination_endpoint_password

        if self.destination_endpoint_port is not None:
            result['DestinationEndpointPort'] = self.destination_endpoint_port

        if self.destination_endpoint_region is not None:
            result['DestinationEndpointRegion'] = self.destination_endpoint_region

        if self.destination_endpoint_role is not None:
            result['DestinationEndpointRole'] = self.destination_endpoint_role

        if self.destination_endpoint_user_name is not None:
            result['DestinationEndpointUserName'] = self.destination_endpoint_user_name

        if self.disaster_recovery_job is not None:
            result['DisasterRecoveryJob'] = self.disaster_recovery_job

        if self.dts_bis_label is not None:
            result['DtsBisLabel'] = self.dts_bis_label

        if self.dts_instance_id is not None:
            result['DtsInstanceId'] = self.dts_instance_id

        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id

        if self.dts_job_name is not None:
            result['DtsJobName'] = self.dts_job_name

        if self.error_notice is not None:
            result['ErrorNotice'] = self.error_notice

        if self.error_phone is not None:
            result['ErrorPhone'] = self.error_phone

        if self.file_oss_url_object is not None:
            result['FileOssUrl'] = self.file_oss_url_object

        if self.job_type is not None:
            result['JobType'] = self.job_type

        if self.max_du is not None:
            result['MaxDu'] = self.max_du

        if self.min_du is not None:
            result['MinDu'] = self.min_du

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.reserve is not None:
            result['Reserve'] = self.reserve

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.source_endpoint_database_name is not None:
            result['SourceEndpointDatabaseName'] = self.source_endpoint_database_name

        if self.source_endpoint_engine_name is not None:
            result['SourceEndpointEngineName'] = self.source_endpoint_engine_name

        if self.source_endpoint_ip is not None:
            result['SourceEndpointIP'] = self.source_endpoint_ip

        if self.source_endpoint_instance_id is not None:
            result['SourceEndpointInstanceID'] = self.source_endpoint_instance_id

        if self.source_endpoint_instance_type is not None:
            result['SourceEndpointInstanceType'] = self.source_endpoint_instance_type

        if self.source_endpoint_oracle_sid is not None:
            result['SourceEndpointOracleSID'] = self.source_endpoint_oracle_sid

        if self.source_endpoint_owner_id is not None:
            result['SourceEndpointOwnerID'] = self.source_endpoint_owner_id

        if self.source_endpoint_password is not None:
            result['SourceEndpointPassword'] = self.source_endpoint_password

        if self.source_endpoint_port is not None:
            result['SourceEndpointPort'] = self.source_endpoint_port

        if self.source_endpoint_region is not None:
            result['SourceEndpointRegion'] = self.source_endpoint_region

        if self.source_endpoint_role is not None:
            result['SourceEndpointRole'] = self.source_endpoint_role

        if self.source_endpoint_user_name is not None:
            result['SourceEndpointUserName'] = self.source_endpoint_user_name

        if self.source_endpoint_vswitch_id is not None:
            result['SourceEndpointVSwitchID'] = self.source_endpoint_vswitch_id

        if self.src_ca_certificate_oss_url is not None:
            result['SrcCaCertificateOssUrl'] = self.src_ca_certificate_oss_url

        if self.src_ca_certificate_password is not None:
            result['SrcCaCertificatePassword'] = self.src_ca_certificate_password

        if self.src_client_cert_oss_url is not None:
            result['SrcClientCertOssUrl'] = self.src_client_cert_oss_url

        if self.src_client_key_oss_url is not None:
            result['SrcClientKeyOssUrl'] = self.src_client_key_oss_url

        if self.src_client_password is not None:
            result['SrcClientPassword'] = self.src_client_password

        if self.src_primary_vsw_id is not None:
            result['SrcPrimaryVswId'] = self.src_primary_vsw_id

        if self.src_secondary_vsw_id is not None:
            result['SrcSecondaryVswId'] = self.src_secondary_vsw_id

        if self.structure_initialization is not None:
            result['StructureInitialization'] = self.structure_initialization

        if self.synchronization_direction is not None:
            result['SynchronizationDirection'] = self.synchronization_direction

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Checkpoint') is not None:
            self.checkpoint = m.get('Checkpoint')

        if m.get('DataCheckConfigure') is not None:
            self.data_check_configure = m.get('DataCheckConfigure')

        if m.get('DataInitialization') is not None:
            self.data_initialization = m.get('DataInitialization')

        if m.get('DataSynchronization') is not None:
            self.data_synchronization = m.get('DataSynchronization')

        if m.get('DbList') is not None:
            self.db_list = m.get('DbList')

        if m.get('DedicatedClusterId') is not None:
            self.dedicated_cluster_id = m.get('DedicatedClusterId')

        if m.get('DelayNotice') is not None:
            self.delay_notice = m.get('DelayNotice')

        if m.get('DelayPhone') is not None:
            self.delay_phone = m.get('DelayPhone')

        if m.get('DelayRuleTime') is not None:
            self.delay_rule_time = m.get('DelayRuleTime')

        if m.get('DestCaCertificateOssUrl') is not None:
            self.dest_ca_certificate_oss_url = m.get('DestCaCertificateOssUrl')

        if m.get('DestCaCertificatePassword') is not None:
            self.dest_ca_certificate_password = m.get('DestCaCertificatePassword')

        if m.get('DestClientCertOssUrl') is not None:
            self.dest_client_cert_oss_url = m.get('DestClientCertOssUrl')

        if m.get('DestClientKeyOssUrl') is not None:
            self.dest_client_key_oss_url = m.get('DestClientKeyOssUrl')

        if m.get('DestClientPassword') is not None:
            self.dest_client_password = m.get('DestClientPassword')

        if m.get('DestPrimaryVswId') is not None:
            self.dest_primary_vsw_id = m.get('DestPrimaryVswId')

        if m.get('DestSecondaryVswId') is not None:
            self.dest_secondary_vsw_id = m.get('DestSecondaryVswId')

        if m.get('DestinationEndpointDataBaseName') is not None:
            self.destination_endpoint_data_base_name = m.get('DestinationEndpointDataBaseName')

        if m.get('DestinationEndpointEngineName') is not None:
            self.destination_endpoint_engine_name = m.get('DestinationEndpointEngineName')

        if m.get('DestinationEndpointIP') is not None:
            self.destination_endpoint_ip = m.get('DestinationEndpointIP')

        if m.get('DestinationEndpointInstanceID') is not None:
            self.destination_endpoint_instance_id = m.get('DestinationEndpointInstanceID')

        if m.get('DestinationEndpointInstanceType') is not None:
            self.destination_endpoint_instance_type = m.get('DestinationEndpointInstanceType')

        if m.get('DestinationEndpointOracleSID') is not None:
            self.destination_endpoint_oracle_sid = m.get('DestinationEndpointOracleSID')

        if m.get('DestinationEndpointOwnerID') is not None:
            self.destination_endpoint_owner_id = m.get('DestinationEndpointOwnerID')

        if m.get('DestinationEndpointPassword') is not None:
            self.destination_endpoint_password = m.get('DestinationEndpointPassword')

        if m.get('DestinationEndpointPort') is not None:
            self.destination_endpoint_port = m.get('DestinationEndpointPort')

        if m.get('DestinationEndpointRegion') is not None:
            self.destination_endpoint_region = m.get('DestinationEndpointRegion')

        if m.get('DestinationEndpointRole') is not None:
            self.destination_endpoint_role = m.get('DestinationEndpointRole')

        if m.get('DestinationEndpointUserName') is not None:
            self.destination_endpoint_user_name = m.get('DestinationEndpointUserName')

        if m.get('DisasterRecoveryJob') is not None:
            self.disaster_recovery_job = m.get('DisasterRecoveryJob')

        if m.get('DtsBisLabel') is not None:
            self.dts_bis_label = m.get('DtsBisLabel')

        if m.get('DtsInstanceId') is not None:
            self.dts_instance_id = m.get('DtsInstanceId')

        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')

        if m.get('DtsJobName') is not None:
            self.dts_job_name = m.get('DtsJobName')

        if m.get('ErrorNotice') is not None:
            self.error_notice = m.get('ErrorNotice')

        if m.get('ErrorPhone') is not None:
            self.error_phone = m.get('ErrorPhone')

        if m.get('FileOssUrl') is not None:
            self.file_oss_url_object = m.get('FileOssUrl')

        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')

        if m.get('MaxDu') is not None:
            self.max_du = m.get('MaxDu')

        if m.get('MinDu') is not None:
            self.min_du = m.get('MinDu')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Reserve') is not None:
            self.reserve = m.get('Reserve')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SourceEndpointDatabaseName') is not None:
            self.source_endpoint_database_name = m.get('SourceEndpointDatabaseName')

        if m.get('SourceEndpointEngineName') is not None:
            self.source_endpoint_engine_name = m.get('SourceEndpointEngineName')

        if m.get('SourceEndpointIP') is not None:
            self.source_endpoint_ip = m.get('SourceEndpointIP')

        if m.get('SourceEndpointInstanceID') is not None:
            self.source_endpoint_instance_id = m.get('SourceEndpointInstanceID')

        if m.get('SourceEndpointInstanceType') is not None:
            self.source_endpoint_instance_type = m.get('SourceEndpointInstanceType')

        if m.get('SourceEndpointOracleSID') is not None:
            self.source_endpoint_oracle_sid = m.get('SourceEndpointOracleSID')

        if m.get('SourceEndpointOwnerID') is not None:
            self.source_endpoint_owner_id = m.get('SourceEndpointOwnerID')

        if m.get('SourceEndpointPassword') is not None:
            self.source_endpoint_password = m.get('SourceEndpointPassword')

        if m.get('SourceEndpointPort') is not None:
            self.source_endpoint_port = m.get('SourceEndpointPort')

        if m.get('SourceEndpointRegion') is not None:
            self.source_endpoint_region = m.get('SourceEndpointRegion')

        if m.get('SourceEndpointRole') is not None:
            self.source_endpoint_role = m.get('SourceEndpointRole')

        if m.get('SourceEndpointUserName') is not None:
            self.source_endpoint_user_name = m.get('SourceEndpointUserName')

        if m.get('SourceEndpointVSwitchID') is not None:
            self.source_endpoint_vswitch_id = m.get('SourceEndpointVSwitchID')

        if m.get('SrcCaCertificateOssUrl') is not None:
            self.src_ca_certificate_oss_url = m.get('SrcCaCertificateOssUrl')

        if m.get('SrcCaCertificatePassword') is not None:
            self.src_ca_certificate_password = m.get('SrcCaCertificatePassword')

        if m.get('SrcClientCertOssUrl') is not None:
            self.src_client_cert_oss_url = m.get('SrcClientCertOssUrl')

        if m.get('SrcClientKeyOssUrl') is not None:
            self.src_client_key_oss_url = m.get('SrcClientKeyOssUrl')

        if m.get('SrcClientPassword') is not None:
            self.src_client_password = m.get('SrcClientPassword')

        if m.get('SrcPrimaryVswId') is not None:
            self.src_primary_vsw_id = m.get('SrcPrimaryVswId')

        if m.get('SrcSecondaryVswId') is not None:
            self.src_secondary_vsw_id = m.get('SrcSecondaryVswId')

        if m.get('StructureInitialization') is not None:
            self.structure_initialization = m.get('StructureInitialization')

        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')

        return self

