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
        # The start offset of incremental data migration or incremental data synchronization. The value is a UNIX timestamp. Unit: seconds.
        self.checkpoint = checkpoint
        # The parameters for data verification, including the configurations for data verification and alerts. The value is a JSON string. For more information, see [DataCheckConfigure parameter description](https://help.aliyun.com/document_detail/459023.html).
        self.data_check_configure = data_check_configure
        # Specifies whether to perform full data migration or full data synchronization. Valid values:
        # 
        # *   **true** (default)
        # *   **false**
        # 
        # > If **JobType** is set to **CHECK**, set this parameter to **false**.
        # 
        # This parameter is required.
        self.data_initialization = data_initialization
        # Specifies whether to perform incremental data migration or incremental data synchronization. Valid values:
        # 
        # *   **false** (default)
        # *   **true**
        # 
        # > If **JobType** is set to **CHECK**, set this parameter to **false**.
        # 
        # This parameter is required.
        self.data_synchronization = data_synchronization
        # The objects that you want to migrate or synchronize. The value is a JSON string. For more information, see [Objects of DTS tasks](https://help.aliyun.com/document_detail/209545.html).
        self.db_list = db_list
        # The ID of the DTS dedicated cluster on which the task runs.
        # 
        # > If this parameter is specified, the task is scheduled to the specified DTS dedicated cluster.
        self.dedicated_cluster_id = dedicated_cluster_id
        # Specifies whether to monitor task latency. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.delay_notice = delay_notice
        # The mobile phone numbers to which latency-related alerts are sent. Separate multiple mobile phone numbers with commas (,).
        # 
        # > 
        # 
        # *   This parameter is available only for users of the China site (aliyun.com). Only mobile phone numbers in the Chinese mainland are supported. You can specify up to 10 mobile phone numbers.
        # *   Users of the international site (alibabacloud.com) cannot receive alerts by using mobile phone numbers, but can configure alert rules for DTS tasks in the CloudMonitor console. For more information, see [Configure alert rules for DTS tasks in the CloudMonitor console](https://help.aliyun.com/document_detail/175876.html).
        self.delay_phone = delay_phone
        # The threshold for latency alerts. Unit: seconds. The value must be an integer. You can set the threshold based on your business requirements. To prevent unstable latency caused by network and database overloads, we recommend that you set the threshold to more than 10 seconds.
        # 
        # > If **DelayNotice** is set to **true**, this parameter is required.
        self.delay_rule_time = delay_rule_time
        # The path of the CA certificate that is used if the connection to the destination database is encrypted by using SSL.
        # 
        # > This feature is not supported. Do not specify this parameter.
        self.dest_ca_certificate_oss_url = dest_ca_certificate_oss_url
        # The key of the CA certificate that is used if the connection to the destination database is encrypted by using SSL.
        # 
        # > This feature is not supported. Do not specify this parameter.
        self.dest_ca_certificate_password = dest_ca_certificate_password
        # The path to the client certificate that is used if the connection to the destination database is encrypted by using SSL.
        # 
        # > This feature is not supported. Do not specify this parameter.
        self.dest_client_cert_oss_url = dest_client_cert_oss_url
        # The path to the private key of the client certificate that is used if the connection to the destination database is encrypted by using SSL.
        # 
        # > This feature is not supported. Do not specify this parameter.
        self.dest_client_key_oss_url = dest_client_key_oss_url
        # The password of the private key of the client certificate that is used if the connection to the destination database is encrypted by using SSL.
        # 
        # > This feature is not supported. Do not specify this parameter.
        self.dest_client_password = dest_client_password
        # VPCNAT destination main VSW
        self.dest_primary_vsw_id = dest_primary_vsw_id
        # VPCNAT destination backup VSW
        self.dest_secondary_vsw_id = dest_secondary_vsw_id
        # The name of the database to which the objects are migrated or synchronized in the destination instance.
        # 
        # > 
        # 
        # *   This parameter is valid and required only if the destination database is a PolarDB for PostgreSQL (Compatible with Oracle) cluster, an AnalyticDB for PostgreSQL instance, a PostgreSQL database, a MaxCompute project, or a MongoDB database.
        # *   If the destination instance is a MaxCompute project, you must specify the MaxCompute project ID.
        self.destination_endpoint_data_base_name = destination_endpoint_data_base_name
        # The type of the destination database. Valid values:
        # 
        # *   **MYSQL**: ApsaraDB RDS for MySQL instance or self-managed MySQL database.
        # *   **MARIADB**: ApsaraDB RDS for MariaDB instance.
        # *   **PolarDB**: PolarDB for MySQL cluster.
        # *   **POLARDB_O**: PolarDB for PostgreSQL (Compatible with Oracle) cluster.
        # *   **POLARDBX10**: PolarDB-X 1.0 instance (formerly DRDS).
        # *   **POLARDBX20**: PolarDB-X 2.0 instance.
        # *   **ORACLE**: self-managed Oracle database.
        # *   **POSTGRESQL**: ApsaraDB RDS for PostgreSQL instance or self-managed PostgreSQL database.
        # *   **MSSQL**: ApsaraDB RDS for SQL Server instance or self-managed SQL Server database.
        # *   **ADS**: AnalyticDB for MySQL V2.0 cluster.
        # *   **ADB30**: AnalyticDB for MySQL V3.0 cluster.
        # *   **MONGODB**: ApsaraDB for MongoDB instance or self-managed MongoDB database.
        # *   **GREENPLUM**: AnalyticDB for PostgreSQL instance.
        # *   **KAFKA**: ApsaraMQ for Kafka instance or self-managed Kafka cluster.
        # *   **DATAHUB**: DataHub project.
        # *   **DB2**: self-managed Db2 for LUW database.
        # *   **AS400**: Db2 for i database.
        # *   **ODPS**: MaxCompute project.
        # *   **Tablestore**: Tablestore instance.
        # *   **ELK**: Elasticsearch cluster.
        # *   **REDIS**: ApsaraDB for Redis instance or self-managed Redis database.
        # 
        # > 
        # 
        # *   Default value: **MYSQL**.
        # *   If this parameter is set to **KAFKA**, **MONGODB**, or **PolarDB**, you must also specify the database information in Reserve. For more information, see [Reserve parameter](https://help.aliyun.com/document_detail/273111.html).
        self.destination_endpoint_engine_name = destination_endpoint_engine_name
        # The IP address of the destination instance.
        # 
        # > This parameter is valid and required only if **DestinationEndpointInstanceType** is set to **OTHER**, **EXPRESS**, **DG**, or **CEN**.
        self.destination_endpoint_ip = destination_endpoint_ip
        # The destination instance ID.
        # 
        # If the destination instance is an Alibaba Cloud database instance, you must specify the database instance ID. For example, if the destination instance is an ApsaraDB RDS for MySQL instance, you must specify the ID of the ApsaraDB RDS for MySQL instance.
        # 
        # If the destination instance is a self-managed database, the value of this parameter varies with the value of **DestinationEndpointInstanceType**.****
        # 
        # *   If DestinationEndpointInstanceType is set to **ECS**, you must specify the ECS instance ID.
        # *   If DestinationEndpointInstanceType is set to **DG**, you must specify the database gateway ID.
        # *   If DestinationEndpointInstanceType is set to **EXPRESS** or **CEN**, you must specify the ID of the VPC that is connected to the source instance.
        # 
        # > If DestinationEndpointInstanceType is set to **CEN**, you must also specify the ID of the CEN instance in Reserve. For more information, see [Reserve parameter](https://help.aliyun.com/document_detail/273111.html).
        self.destination_endpoint_instance_id = destination_endpoint_instance_id
        # The type of the destination instance. Valid values:
        # 
        # **Alibaba Cloud database instance**
        # 
        # *   **RDS**: ApsaraDB RDS for MySQL instance, ApsaraDB RDS for SQL Server instance, ApsaraDB RDS for PostgreSQL instance, or ApsaraDB RDS for MariaDB instance.
        # *   **PolarDB**: PolarDB for MySQL cluster.
        # *   **DISTRIBUTED_POLARDBX10**: PolarDB-X 1.0 instance (formerly DRDS).
        # *   **POLARDBX20**: PolarDB-X 2.0 instance.
        # *   **REDIS**: ApsaraDB for Redis instance.
        # *   **ADS**: AnalyticDB for MySQL V2.0 cluster or AnalyticDB for MySQL V3.0 cluster.
        # *   **MONGODB**: ApsaraDB for MongoDB instance.
        # *   **GREENPLUM**: AnalyticDB for PostgreSQL instance.
        # *   **DATAHUB**: DataHub project.
        # *   **ELK**: Elasticsearch cluster.
        # *   **Tablestore**: Tablestore instance.
        # *   **ODPS**: MaxCompute project.
        # 
        # **Self-managed database**
        # 
        # *   **OTHER**: self-managed database with a public IP address.
        # *   **ECS**: self-managed database hosted on an ECS instance.
        # *   **EXPRESS**: self-managed database connected over Express Connect.
        # *   **CEN**: self-managed database connected over Cloud Enterprise Network (CEN).
        # *   **DG**: self-managed database connected over Database Gateway.
        # 
        # > 
        # 
        # *   If the destination instance is a PolarDB for PostgreSQL (Compatible with Oracle) cluster, you must connect the cluster to DTS as a self-managed database by using a public IP address or Express Connect and set this parameter to **OTHER** or **EXPRESS**.
        # *   If the destination instance is an ApsaraMQ for Kafka instance, you must connect the instance to DTS as a self-managed database by using ECS or Express Connect and set this parameter to **ECS** or **EXPRESS**.
        # *   For more information, see [Supported source and destination databases](https://help.aliyun.com/document_detail/176064.html).
        # *   If the destination instance is a self-managed database, you must deploy the network environment for the database. For more information, see [Preparation overview](https://help.aliyun.com/document_detail/146958.html).
        # 
        # This parameter is required.
        self.destination_endpoint_instance_type = destination_endpoint_instance_type
        # The SID of the Oracle database.
        # 
        # > This parameter is valid and required only if **DestinationEndpointEngineName** is set to **ORACLE** and the **Oracle** database is deployed in a non-RAC architecture.
        self.destination_endpoint_oracle_sid = destination_endpoint_oracle_sid
        # The ID of the Alibaba Cloud account to which the destination ApsaraDB RDS for MySQL instance belongs.
        # 
        # > 
        # 
        # *   This parameter is available only if the destination instance is an ApsaraDB RDS for MySQL instance.
        # *   You can specify this parameter to migrate or synchronize data across different Alibaba Cloud accounts. In this case, you must specify **DestinationEndpointRole**.
        self.destination_endpoint_owner_id = destination_endpoint_owner_id
        # The password of the account that is used to log on to the destination database.
        # 
        # > If the destination database is a MaxCompute project, you must specify the AccessKey secret of your Alibaba Cloud account. For information about how to obtain an AccessKey pair, see [Create an AccessKey pair](https://help.aliyun.com/document_detail/116401.html).
        self.destination_endpoint_password = destination_endpoint_password
        # The port number of the destination instance.
        # 
        # > This parameter is valid and required only if the destination instance is a self-managed database.
        self.destination_endpoint_port = destination_endpoint_port
        # The ID of the region in which the destination instance resides. For more information, see [Supported regions](https://help.aliyun.com/document_detail/141033.html).
        # 
        # > If the destination instance is an Alibaba Cloud database instance, this parameter is required.
        self.destination_endpoint_region = destination_endpoint_region
        # The name of the RAM role configured for the Alibaba Cloud account to which the destination instance belongs.
        # 
        # > This parameter is required if you migrate or synchronize data across Alibaba Cloud accounts. For information about the permissions and authorization methods of the RAM role, see [Configure RAM authorization for cross-account DTS tasks](https://help.aliyun.com/document_detail/48468.html).
        self.destination_endpoint_role = destination_endpoint_role
        # The username of the account that is used to log on to the destination database.
        # 
        # > 
        # 
        # *   In most cases, this parameter is required.
        # *   The permissions that are required for the database account vary with the migration or synchronization scenario. For more information, see [Prepare the database accounts for data migration](https://help.aliyun.com/document_detail/175878.html) or [Prepare the database accounts for data synchronization](https://help.aliyun.com/document_detail/213152.html).
        # *   If the destination database is a MaxCompute project, you must specify the AccessKey ID of your Alibaba Cloud account. For information about how to obtain an AccessKey pair, see [Create an AccessKey pair](https://help.aliyun.com/document_detail/116401.html).
        self.destination_endpoint_user_name = destination_endpoint_user_name
        # Specifies whether the instance is a disaster recovery instance. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.disaster_recovery_job = disaster_recovery_job
        # The environment tag of the DTS instance. Valid values:
        # 
        # *   **normal******
        # *   **online******
        self.dts_bis_label = dts_bis_label
        # The ID of the data migration or synchronization instance.
        # 
        # > You can call the [DescribeDtsJobs](https://help.aliyun.com/document_detail/209702.html) operation to query the instance ID.
        self.dts_instance_id = dts_instance_id
        # The ID of the data migration or synchronization task.
        # 
        # > You can call the [DescribeDtsJobs](https://help.aliyun.com/document_detail/209702.html) operation to query the task ID.
        self.dts_job_id = dts_job_id
        # The name of the DTS instance.
        # 
        # This parameter is required.
        self.dts_job_name = dts_job_name
        # Specifies whether to monitor task status. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.error_notice = error_notice
        # The mobile phone numbers to which status-related alerts are sent. Separate multiple mobile phone numbers with commas (,).
        # 
        # > 
        # 
        # *   This parameter is available only for users of the China site (aliyun.com). Only mobile phone numbers in the Chinese mainland are supported. You can specify up to 10 mobile phone numbers.
        # *   Users of the international site (alibabacloud.com) cannot receive alerts by using mobile phone numbers, but can configure alert rules for DTS tasks in the CloudMonitor console. For more information, see [Configure alert rules for DTS tasks in the CloudMonitor console](https://help.aliyun.com/document_detail/175876.html).
        self.error_phone = error_phone
        # The URL of the Object Storage Service (OSS) bucket that stores the files related to the DTS task.
        self.file_oss_url_object = file_oss_url_object
        # The type of the task. Valid values:
        # 
        # *   **MIGRATION**: data migration task.
        # *   **SYNC**: data synchronization task.
        # *   **CHECK**: data verification task. You must separately purchase a data verification instance.
        # 
        # > If you set this parameter to **MIGRATION** or **SYNC**, you can also enable data verification in the data migration or synchronization task.
        # 
        # This parameter is required.
        self.job_type = job_type
        # The maximum number of DUs.
        # 
        # > This parameter is supported only for serverless instances.
        self.max_du = max_du
        # The minimum number of DTS Units (DUs).
        # 
        # > This parameter is supported only for serverless instances.
        self.min_du = min_du
        self.owner_id = owner_id
        # The ID of the region in which the DTS instance resides. For more information, see [Supported regions](https://help.aliyun.com/document_detail/141033.html).
        self.region_id = region_id
        # The reserved parameter of DTS. The value is a JSON string. You can specify this parameter to add more configurations of the source or destination instance to the DTS task. For example, you can specify the data storage format of the destination Kafka database and the CEN instance ID. For more information, see [Reserve parameter](https://help.aliyun.com/document_detail/273111.html).
        self.reserve = reserve
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The name of the database from which the objects are migrated or synchronized in the source instance.
        # 
        # > This parameter is valid and required only if the source instance is a PolarDB for PostgreSQL (Compatible with Oracle) cluster, a PostgreSQL database, or a MongoDB database.
        self.source_endpoint_database_name = source_endpoint_database_name
        # The database type of the source instance.
        # 
        # *   **MYSQL**: ApsaraDB RDS for MySQL instance or self-managed MySQL database.
        # *   **MARIADB**: ApsaraDB RDS for MariaDB instance.
        # *   **PolarDB**: PolarDB for MySQL cluster.
        # *   **POLARDB_O**: PolarDB for PostgreSQL (Compatible with Oracle) cluster.
        # *   **POLARDBX10**: PolarDB-X 1.0 instance (formerly DRDS).
        # *   **POLARDBX20**: PolarDB-X 2.0 instance.
        # *   **ORACLE**: self-managed Oracle database.
        # *   **POSTGRESQL**: ApsaraDB RDS for PostgreSQL instance or self-managed PostgreSQL database.
        # *   **MSSQL**: ApsaraDB RDS for SQL Server instance or self-managed SQL Server database.
        # *   **MONGODB**: ApsaraDB for MongoDB instance or self-managed MongoDB database.
        # *   **DB2**: self-managed Db2 for LUW database.
        # *   **AS400**: self-managed Db2 for i database.
        # *   **DMSPOLARDB**: DMS logical database.
        # *   **HBASE**: self-managed HBase database.
        # *   **TERADATA**: Teradata database.
        # *   **TiDB**: TiDB database.
        # *   **REDIS**: ApsaraDB for Redis instance or self-managed Redis database.
        # 
        # > 
        # 
        # *   Default value: **MYSQL**.
        # *   If this parameter is set to **MONGODB**, you must also specify the architecture type of the MongoDB database in Reserve. For more information, see [Reserve parameter](https://help.aliyun.com/document_detail/273111.html).
        self.source_endpoint_engine_name = source_endpoint_engine_name
        # The IP address of the source instance.
        # 
        # > This parameter is valid and required only if **SourceEndpointInstanceType** is set to **OTHER**, **EXPRESS**, **DG**, or **CEN**.
        self.source_endpoint_ip = source_endpoint_ip
        # The source instance ID.
        # 
        # If the source instance is an Alibaba Cloud database instance, you must specify the database instance ID. For example, if the source instance is an ApsaraDB RDS for MySQL instance, you must specify the ID of the ApsaraDB RDS for MySQL instance.
        # 
        # If the source instance is a self-managed database, the value of this parameter varies with the value of **SourceEndpointInstanceType**.****
        # 
        # *   If SourceEndpointInstanceType is set to **ECS**, you must specify the ECS instance ID.
        # *   If SourceEndpointInstanceType is set to **DG**, you must specify the database gateway ID.
        # *   If SourceEndpointInstanceType is set to **EXPRESS** or **CEN**, you must specify the ID of the virtual private cloud (VPC) that is connected to the source instance.
        # 
        # > If SourceEndpointInstanceType is set to **CEN**, you must also specify the ID of the CEN instance in Reserve. For more information, see [Reserve parameter](https://help.aliyun.com/document_detail/273111.html).
        self.source_endpoint_instance_id = source_endpoint_instance_id
        # The type of the source instance. Valid values:
        # 
        # **Alibaba Cloud database instance**
        # 
        # *   **RDS**: ApsaraDB RDS for MySQL instance, ApsaraDB RDS for SQL Server instance, ApsaraDB RDS for PostgreSQL instance, or ApsaraDB RDS for MariaDB instance
        # *   **PolarDB**: PolarDB for MySQL cluster.
        # *   **REDIS**: ApsaraDB for Redis instance.
        # *   **DISTRIBUTED_POLARDBX10**: PolarDB-X 1.0 instance (formerly DRDS).
        # *   **POLARDBX20**: PolarDB-X 2.0 instance.
        # *   **MONGODB**: ApsaraDB for MongoDB instance.
        # *   **DISTRIBUTED_DMSLOGICDB**: Data Management (DMS) logical database
        # 
        # **Self-managed database**
        # 
        # *   **OTHER**: self-managed database with a public IP address.
        # *   **ECS**: self-managed database hosted on an ECS instance.
        # *   **EXPRESS**: self-managed database connected over Express Connect.
        # *   **CEN**: self-managed database connected over Cloud Enterprise Network (CEN).
        # *   **DG**: self-managed database connected over Database Gateway.
        # 
        # > 
        # 
        # *   If the source instance is a PolarDB for PostgreSQL (Compatible with Oracle) cluster, you must connect the cluster to DTS as a self-managed database by using a public IP address or Express Connect and set this parameter to **OTHER** or **EXPRESS**.
        # *   For more information, see [Supported sources and targets](https://help.aliyun.com/document_detail/176064.html).
        # *   If the source instance is a self-managed database, you must deploy the network environment for the database. For more information, see [Preparation overview](https://help.aliyun.com/document_detail/146958.html).
        # 
        # This parameter is required.
        self.source_endpoint_instance_type = source_endpoint_instance_type
        # The SID of the Oracle database.
        # 
        # > This parameter is valid and required only if **SourceEndpointEngineName** is set to **ORACLE** and the **Oracle** database is deployed in a non-Real Application Cluster (RAC) architecture.
        self.source_endpoint_oracle_sid = source_endpoint_oracle_sid
        # The ID of the Alibaba Cloud account to which the source database belongs.
        # 
        # > You can specify this parameter to migrate or synchronize data across different Alibaba Cloud accounts. In this case, you must specify **SourceEndpointRole**.
        self.source_endpoint_owner_id = source_endpoint_owner_id
        # The password of the account that is used to log on to the source database.
        self.source_endpoint_password = source_endpoint_password
        # The port number of the source instance.
        # 
        # > This parameter is required only if the source instance is a self-managed database.
        self.source_endpoint_port = source_endpoint_port
        # The ID of the region in which the source instance resides. For more information, see [Supported regions](https://help.aliyun.com/document_detail/141033.html).
        # 
        # > If the source instance is an Alibaba Cloud database instance, this parameter is required.
        self.source_endpoint_region = source_endpoint_region
        # The name of the Resource Access Management (RAM) role configured for the Alibaba Cloud account to which the source instance belongs.
        # 
        # > This parameter is required if you migrate or synchronize data across different Alibaba Cloud accounts. For information about the permissions and authorization methods of the RAM role, see [Configure RAM authorization for cross-account DTS tasks](https://help.aliyun.com/document_detail/48468.html).
        self.source_endpoint_role = source_endpoint_role
        # The username of the account that is used to log on to the source database.
        # 
        # > 
        # 
        # *   In most cases, this parameter is required.
        # *   The permissions that are required for the database account vary with the migration or synchronization scenario. For more information, see [Prepare the database accounts for data migration](https://help.aliyun.com/document_detail/175878.html) or [Prepare the database accounts for data synchronization](https://help.aliyun.com/document_detail/213152.html).
        self.source_endpoint_user_name = source_endpoint_user_name
        # The ID of the vSwitch that is used for data shipping.
        self.source_endpoint_vswitch_id = source_endpoint_vswitch_id
        # The path of the certificate authority (CA) certificate that is used if the connection to the source database is encrypted by using SSL.
        # 
        # > This feature is not supported. Do not specify this parameter.
        self.src_ca_certificate_oss_url = src_ca_certificate_oss_url
        # The key of the CA certificate that is used if the connection to the source database is encrypted by using SSL.
        # 
        # > This feature is not supported. Do not specify this parameter.
        self.src_ca_certificate_password = src_ca_certificate_password
        # The path to the client certificate that is used if the connection to the source database is encrypted by using SSL.
        # 
        # > This feature is not supported. Do not specify this parameter.
        self.src_client_cert_oss_url = src_client_cert_oss_url
        # The path to the private key of the client certificate that is used if the connection to the source database is encrypted by using SSL.
        # 
        # > This feature is not supported. Do not specify this parameter.
        self.src_client_key_oss_url = src_client_key_oss_url
        # The password of the private key of the client certificate that is used if the connection to the source database is encrypted by using SSL.
        # 
        # > This feature is not supported. Do not specify this parameter.
        self.src_client_password = src_client_password
        # VPCNAT source end main VSW
        self.src_primary_vsw_id = src_primary_vsw_id
        # VPCNAT source backup VSW
        self.src_secondary_vsw_id = src_secondary_vsw_id
        # Specifies whether to perform schema migration or schema synchronization. Valid values:
        # 
        # *   **true** (default)
        # *   **false**
        # 
        # > If **JobType** is set to **CHECK**, set this parameter to **false**.
        # 
        # This parameter is required.
        self.structure_initialization = structure_initialization
        # The synchronization direction. Valid values:
        # 
        # *   **Forward**
        # *   **Reverse**
        # 
        # > 
        # 
        # *   The default value is **Forward**.
        # *   The value **Reverse** takes effect only if the topology of the data synchronization task is two-way synchronization.
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

