# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dts20200101 import models as main_models
from darabonba.model import DaraModel

class CreateGadOrderRequest(DaraModel):
    def __init__(
        self,
        amount: int = None,
        auto_create_proxy: bool = None,
        auto_pay: bool = None,
        auto_renew: str = None,
        babelfish_config: str = None,
        bpe_enabled: str = None,
        bursting_enabled: bool = None,
        business_info: str = None,
        category: str = None,
        client_token: str = None,
        cluster_id: str = None,
        cold_data_enabled: bool = None,
        connection_mode: str = None,
        connection_string: str = None,
        create_strategy: str = None,
        dbinstance_class: str = None,
        dbinstance_description: str = None,
        dbinstance_net_type: str = None,
        dbinstance_storage: int = None,
        dbinstance_storage_type: str = None,
        dbis_ignore_case: str = None,
        dbparam_group_id: str = None,
        dbtime_zone: str = None,
        db_list: str = None,
        db_list_mode: int = None,
        dedicated_host_group_id: str = None,
        deletion_protection: bool = None,
        dry_run: bool = None,
        encryption_key: str = None,
        engine: str = None,
        engine_version: str = None,
        instance_network_type: str = None,
        io_acceleration_enabled: str = None,
        master_account_exist: bool = None,
        master_account_name: str = None,
        master_account_password: str = None,
        master_database_name: str = None,
        master_engine_arch_type: str = None,
        master_instance_id: str = None,
        master_region: str = None,
        master_shard_account_name: str = None,
        master_shard_account_password: str = None,
        need_create_slave: bool = None,
        owner_id: str = None,
        pay_type: str = None,
        period: str = None,
        port: str = None,
        private_ip_address: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        role_arn: str = None,
        security_iplist: str = None,
        serverless_config: main_models.CreateGadOrderRequestServerlessConfig = None,
        slave_account_exist: bool = None,
        slave_account_name: str = None,
        slave_account_password: str = None,
        slave_database_name: str = None,
        slave_engine_arch_type: str = None,
        slave_instance_id: str = None,
        slave_read_only: bool = None,
        slave_region: str = None,
        storage_auto_scale: str = None,
        storage_threshold: int = None,
        storage_upper_bound: int = None,
        sync_account_type: str = None,
        sync_architecture: str = None,
        sync_conflict: str = None,
        system_dbcharset: str = None,
        tag: List[main_models.CreateGadOrderRequestTag] = None,
        target_dedicated_host_id_for_log: str = None,
        target_dedicated_host_id_for_master: str = None,
        target_dedicated_host_id_for_slave: str = None,
        target_minor_version: str = None,
        used_time: str = None,
        user_backup_id: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        whitelist_template_list: str = None,
        zone_id: str = None,
        zone_id_slave_1: str = None,
        zone_id_slave_2: str = None,
    ):
        # The number of ApsaraDB RDS for MySQL instances to be created. This parameter is applicable only when you create multiple ApsaraDB RDS for MySQL instances at a time.
        # 
        # Valid values: 1 to 20. Default value: 1.
        self.amount = amount
        # Specifies whether to automatically create a proxy. Valid values:
        # 
        # - **true**: enables automatic creation. By default, a general-purpose proxy is created.
        # 
        # - **false**: disables automatic creation.
        self.auto_create_proxy = auto_create_proxy
        # Specifies whether to enable auto-renewal upon expiration. Valid values:
        # - **false**: no. This is the default value.
        # - **true**: yes.
        self.auto_pay = auto_pay
        # Specifies whether to enable auto-renewal. Valid values:
        # 
        # - true: enables auto-renewal.
        # - false: disables auto-renewal.
        # 
        # Default value: false.
        self.auto_renew = auto_renew
        # The configuration information of Babelfish for ApsaraDB RDS for PostgreSQL.
        # 
        # Configuration format: {"babelfishEnabled":"true","migrationMode":"xxxxxxx","masterUsername":"xxxxxxx","masterUserPassword":"xxxxxxxx"}
        # 
        # Parameter descriptions:
        # - **babelfishEnabled**: specifies whether to enable Babelfish. Set the value to **true** to enable Babelfish. By default, Babelfish is disabled if this parameter is not configured.
        # - **migrationMode**: the database mode. Set the value to **single-db** for the single-database mode or **multi-db** for the multi-database mode.
        # - **masterUsername**: the initial administrator account. The username must be 1 to 63 characters in length and can contain lowercase letters, digits, and underscores (_). It must start with a letter and end with a letter or digit. It cannot start with pg.
        # - **masterUserPassword**: the password of the administrator account. The password must be 8 to 32 characters in length and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. Special characters include `! @ # $ % ^ & * () _ + - =`.
        # 
        # > This parameter is applicable only to ApsaraDB RDS for PostgreSQL instances. For more information about Babelfish for ApsaraDB RDS for PostgreSQL, see [Babelfish overview](https://help.aliyun.com/document_detail/428613.html).
        self.babelfish_config = babelfish_config
        self.bpe_enabled = bpe_enabled
        # Specifies whether to enable the I/O performance burst feature for ESSD AutoPL cloud disks. Valid values:
        # 
        # - **true**: enables the feature.
        # - **false**: disables the feature. This is the default value.
        # 
        # > This parameter is supported only when StorageType is set to ESSDAUTOPL.
        self.bursting_enabled = bursting_enabled
        # The additional parameter that specifies business information.
        self.business_info = business_info
        # The instance edition. Valid values:
        # 
        # General instances:
        # Basic: Basic Edition.
        # HighAvailability: high-availability series.
        # cluster: Cluster Edition for MySQL or PostgreSQL.
        # AlwaysOn: Cluster Edition for SQL Server.
        # Finance: RDS Enterprise Edition.
        # Note: This parameter is required when you create an ApsaraDB RDS for SQL Server instance of the RDS Enterprise Edition, Basic Edition Standard, or Basic Edition Enterprise. For example, when you create a Basic Edition instance of the 2022 RDS Enterprise Edition (2022_ent), you must set this parameter to Basic.
        # Serverless instances:
        # serverless_basic: Serverless Basic Edition. This edition is active only for MySQL and PostgreSQL.
        # 
        # serverless_standard: Serverless high availability series. This edition is active only for MySQL and PostgreSQL.
        # 
        # serverless_ha: SQL Server Serverless high availability series.
        # 
        # Note: This parameter is required when PayType is set to Serverless.
        self.category = category
        # The client token that is used to ensure the idempotence of the request. The portal rewrites this parameter as a random UUID.
        self.client_token = client_token
        # The instance ID.
        self.cluster_id = cluster_id
        # Specifies whether to enable the [data archiving](https://help.aliyun.com/document_detail/2701832.html) feature for premium performance disks. Valid values:
        # 
        # - **true**: enables the feature.
        # - **false**: disables the feature.
        self.cold_data_enabled = cold_data_enabled
        # The access mode of the instance. Valid values:
        # * **Standard**: standard access mode.
        # * **Safe**: database proxy mode.
        # 
        # Default value: allocated by the RDS system.
        # > SQL Server 2012, 2016, and 2017 support only the standard access mode.
        self.connection_mode = connection_mode
        # The database connection address.
        self.connection_string = connection_string
        # The policy for creating multiple instances at a time. This parameter takes effect only when the **Amount** parameter is set to a value greater than 1. Valid values:
        # * **Atomicity** (default): atomicity. All instances in the same batch are created successfully, or if one instance fails to be created, all instances fail to be created.
        # * **Partial**: non-atomicity. The creation of an instance is not affected by other instances in the same batch.
        self.create_strategy = create_strategy
        # The instance type. Valid values:
        # - **selectdb.xlarge**: 4 cores, 32 GB.
        # - **selectdb.2xlarge**: 8 cores, 64 GB.
        # - **selectdb.4xlarge**: 16 cores, 128 GB.
        # - **selectdb.8xlarge**: 32 cores, 256 GB.
        # - **selectdb.16xlarge**: 64 cores, 512 GB.
        # - **selectdb.24xlarge**: 96 cores, 768 GB.
        # - **selectdb.32xlarge**: 128 cores, 1024 GB.
        self.dbinstance_class = dbinstance_class
        # The name of the instance. The name must be 2 to 255 characters in length. It must start with a letter or Chinese character and can contain letters, Chinese characters, digits, and hyphens (-).
        self.dbinstance_description = dbinstance_description
        # The network connection type of the instance. Set the value to Intranet, which indicates an internal network connection.
        self.dbinstance_net_type = dbinstance_net_type
        # Instance storage capacity of the instance. Instance storage capacity of a read-only instance must be greater than or equal to that of the primary instance. Valid values: See the **Storage Capacity** column in [Read-only instance types](https://help.aliyun.com/document_detail/145759.html). The value must be a multiple of 5. Unit: GB.
        self.dbinstance_storage = dbinstance_storage
        # The storage type of the instance. Valid values:
        # * **local_ssd**: premium local SSD.
        # * **cloud_ssd**: standard SSD.
        # * **cloud_essd**: PL1 ESSD.
        # * **cloud_essd2**: PL2 ESSD.
        # * **cloud_essd3**: PL3 ESSD.
        # * **general_essd**: premium performance disk.
        # 
        # 
        # > * If the primary ApsaraDB RDS for MySQL instance uses premium local SSDs, you can set this parameter only to **local_ssd**. If the primary instance uses cloud disks, you can set this parameter only to a cloud disk storage type.
        # > * ApsaraDB RDS for SQL Server supports only cloud disk storage types.
        self.dbinstance_storage_type = dbinstance_storage_type
        # Specifies whether table names are case-sensitive. Valid values:
        # * **true**: Table names are not case-sensitive. This is the default value.
        # * **false**: Table names are case-sensitive.
        self.dbis_ignore_case = dbis_ignore_case
        # The ID of the parameter template. You can call the DescribeParameterGroups operation to query the ID.
        # > This parameter is supported only for MySQL and PostgreSQL. If you do not specify this parameter, the default parameter template is used. You can also create a custom parameter template and use it here.
        self.dbparam_group_id = dbparam_group_id
        # The time zone of the instance. This parameter takes effect only when **Engine** is set to **MySQL** or **PostgreSQL**.
        # 
        # - When **Engine** is set to **MySQL**:
        #     - The parameter settings configure the UTC time zone. Valid values: **-12:59** to **+13:00**.
        #     - An instance with Premium Local SSDs can use a named time zone, such as Asia/Hong_Kong. For more information about named time zones, see [Named time zones](https://help.aliyun.com/document_detail/297356.html).
        # - When **Engine** is set to **PostgreSQL**:
        #     - The parameter settings configure a named time zone. UTC time zones are not supported. For more information about named time zones, see [Named time zones](https://help.aliyun.com/document_detail/297356.html).
        #     - This parameter can be configured only for PostgreSQL instances that use cloud disks.
        # 
        # > - You can make parameter settings for the time zone when you purchase a primary instance. Read-only instances do not support time zone Settings and inherit the time zone of the primary instance.
        # > - If you do not make parameter settings for this parameter, the system selects the default time zone based on the region where the instance is created.
        self.dbtime_zone = dbtime_zone
        # The objects to be migrated or synchronized, in JSON format. For more information, see [Description of migration, synchronization, or change tracking objects](https://help.aliyun.com/document_detail/209545.html).
        # 
        # - The DbList parameter supports up to 1 MB of data.
        # - If DbList contains filter conditions, the total length of DbList, including the filter conditions, cannot exceed 1 MB.
        # - For distributed tasks (such as migration or synchronization tasks with PolarDB-X 1.0 as the source), DbList is split based on physical table shards to generate multiple subtasks. The DbList of each subtask supports up to 1 MB of data.
        self.db_list = db_list
        # The DbList mode for SQL Server disaster recovery. Set this parameter to 0. Valid values are 0, 1, and 2, and the value must be consistent within the same group.
        self.db_list_mode = db_list_mode
        # The ID of the existing dedicated cluster.
        self.dedicated_host_group_id = dedicated_host_group_id
        # Specifies whether to enable deletion protection for the resource stack. Valid values:
        # - Enabled: enables deletion protection for the resource stack.
        # - Disabled (default): disables deletion protection for the resource stack. In this case, you can release the resource stack by using the console or calling the DeleteStack operation.
        # 
        # > The deletion protection settings for a nested resource stack are the same as those for the root resource stack.
        self.deletion_protection = deletion_protection
        # Specifies whether to perform only a precheck. Valid values:
        # 
        # - **true**: yes. After the precheck succeeds, no changes are made to the instance.
        # - **false** (default): no. After the precheck succeeds, the database instance of the DTS task is modified and the task is run.
        self.dry_run = dry_run
        # The ID of the encryption key. If encryption is disabled, this parameter is empty.
        # 
        # > After disk encryption is enabled for a cloud disk instance, it cannot be disabled.
        self.encryption_key = encryption_key
        # The database engine type.
        # 
        # This parameter is required.
        self.engine = engine
        # The database engine version of the instance. The valid values vary based on the database engine type.
        self.engine_version = engine_version
        # The network type of the instance. Set the value to **VPC**.
        # 
        # > - Only VPCs are supported in Alibaba Cloud.
        # > - If you do not specify this parameter, the default value VPC is used.
        self.instance_network_type = instance_network_type
        # Specifies whether to enable the Buffer Pool Extension (BPE) feature for premium performance disks. Valid values:
        # 
        #  - **1**: enables the feature.
        #  - **0**: disables the feature.
        # 
        # > For more information about the Buffer Pool Extension (BPE) feature, see [Buffer Pool Extension (BPE)](https://help.aliyun.com/document_detail/2527067.html).
        self.io_acceleration_enabled = io_acceleration_enabled
        # Specifies whether the primary instance account exists.
        self.master_account_exist = master_account_exist
        # The privileged account of the primary instance.
        self.master_account_name = master_account_name
        # The password of the primary instance account.
        self.master_account_password = master_account_password
        # This parameter is specific to MongoDB. The architecture type of the primary database. Valid values:
        # - 1: replica set.
        # - 2: sharded cluster.
        self.master_database_name = master_database_name
        # This parameter is specific to MongoDB. The architecture type of the primary database. Valid values:
        # - 1: replica set.
        # - 2: sharded cluster.
        self.master_engine_arch_type = master_engine_arch_type
        # The primary instance.
        self.master_instance_id = master_instance_id
        # The region where the primary instance resides.
        self.master_region = master_region
        # The shard account.
        self.master_shard_account_name = master_shard_account_name
        # The password of the shard account.
        self.master_shard_account_password = master_shard_account_password
        # Specifies whether to purchase a new secondary instance. If this parameter is set to false, an existing instance is used.
        self.need_create_slave = need_create_slave
        self.owner_id = owner_id
        # The billing method of the instance. Valid values:
        # - **PrePaid**: subscription.
        # - **PostPaid**: pay-as-you-go.
        # 
        # > This parameter is required.
        self.pay_type = pay_type
        # The billing method for subscription instances. Valid values:
        # 
        # - **Year**: yearly.
        # - **Month**: monthly.
        # 
        # > This parameter is valid and required only when the billing method is **PrePaid** (subscription).
        self.period = period
        # The database service port of the destination instance.
        self.port = port
        # Settings for the internal network IP address of the instance. The IP address must be within the IP address range of the specified vSwitch. By default, the system automatically allocates an IP address based on the VpcId and VSwitchId parameters.
        self.private_ip_address = private_ip_address
        # The region ID of the primary instance.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The global resource descriptor (ARN) for the authorization of the RDS cloud service account by the primary account to access KMS. You can call the CheckCloudResourceAuthorized operation to query the ARN.
        # >Notice: When you enable cloud disk encryption, you must specify **RoleARN**.</notice>
        self.role_arn = role_arn
        # The IP addresses that are added to the whitelist of the instance. Separate multiple IP addresses with commas (,). Note: If you set this parameter to 127.0.0.1, access from all IP addresses is denied. If you set this parameter to 192.168.0.0/24, access from all IP addresses in the 192.168.0.XX format is allowed.
        self.security_iplist = security_iplist
        # The settings of the Serverless instance. This parameter is required when you create a Serverless instance.
        self.serverless_config = serverless_config
        # Specifies whether the secondary instance account exists.
        self.slave_account_exist = slave_account_exist
        # The account with the same name on the secondary instance.
        self.slave_account_name = slave_account_name
        # The password of the secondary instance account.
        self.slave_account_password = slave_account_password
        # The name of the secondary database.
        self.slave_database_name = slave_database_name
        # This parameter is specific to MongoDB. The architecture type of the secondary database. Valid values:
        # - 1: replica set.
        # - 2: sharded cluster.
        self.slave_engine_arch_type = slave_engine_arch_type
        # The secondary instance.
        self.slave_instance_id = slave_instance_id
        # Specifies whether the secondary instance is read-only.
        self.slave_read_only = slave_read_only
        # The region where the secondary instance resides.
        self.slave_region = slave_region
        # Specifies whether to enable Automatic storage scaling for the Standard Edition cluster. Valid values:
        # 
        # - Enable: enables Automatic storage scaling.
        # - Disable: shutdown Automatic storage scaling.
        self.storage_auto_scale = storage_auto_scale
        # The threshold (in percentage) that triggers automatic storage expansion. Valid values:
        # * **10**
        # * **20**
        # * **30**
        # * **40**
        # * **50**
        # 
        # > This parameter is required when **StorageAutoScale** is set to **Enable**.
        self.storage_threshold = storage_threshold
        # The Settings for the upper limit of Automatic storage scaling for the Standard Edition cluster. Unit: GB.
        # 
        # > The maximum value is 32000.
        self.storage_upper_bound = storage_upper_bound
        # The synchronization account type.
        self.sync_account_type = sync_account_type
        # The synchronization topology. Valid values:
        # 
        # - **oneway**: one-way synchronization. This is the default value.
        # - **bidirectional**: two-way synchronization.
        self.sync_architecture = sync_architecture
        # The conflict resolution policy.
        self.sync_conflict = sync_conflict
        # **[Deprecated]** This parameter is deprecated and does not need to be configured.
        self.system_dbcharset = system_dbcharset
        # The tags of the data migration instance. This parameter is used as a filter. If this parameter is not empty, only the instance tasks that have the specified tags are returned.
        self.tag = tag
        # The ID of the host on which the logger instance is created in the dedicated cluster.
        # 
        # This parameter is required when you create an RDS Enterprise Edition instance in a dedicated cluster. If you do not specify this parameter, the system automatically allocates a host by default.
        # 
        # - You can invoke the DescribeDedicatedHosts operation to query the host information in the dedicated cluster.
        # - If no hosts are active, you can invoke the CreateDedicatedHost operation to create a host.
        self.target_dedicated_host_id_for_log = target_dedicated_host_id_for_log
        # The ID of the host on which the primary instance is created in the dedicated cluster.
        # 
        # This parameter is required when you create an instance in a dedicated cluster. If you do not specify this parameter, the system automatically assigns a host.
        # 
        # You can call the DescribeDedicatedHosts operation to query the host information in the dedicated cluster.
        # If no hosts are available, you can call the CreateDedicatedHost operation to create a host.
        self.target_dedicated_host_id_for_master = target_dedicated_host_id_for_master
        # The ID of the host on which the secondary instance is created in the dedicated cluster.
        # 
        # This parameter is required when you create a high availability series or RDS Enterprise Edition instance in a dedicated cluster. If you do not specify this parameter, the system automatically allocates a host by default.
        # 
        # - You can invoke the DescribeDedicatedHosts operation to query the host information in the dedicated cluster.
        # - If no hosts are active, you can invoke the CreateDedicatedHost operation to create a host.
        self.target_dedicated_host_id_for_slave = target_dedicated_host_id_for_slave
        # The minor engine version of the ApsaraDB RDS instance. This parameter is required only when you create a MySQL or PostgreSQL instance.
        self.target_minor_version = target_minor_version
        # The purchase duration for subscription instances.
        # - When **Period** is set to **Month**, valid values are 1, 2, 3, 4, 5, 6, 7, 8, and 9.
        # - When **Period** is set to **Year**, valid values are 1, 2, 3, and 5.
        # > - This parameter is valid and required only when **PayType** is set to **PrePaid**.
        # - For the billing method of subscription instances, you can specify it in the **Period** parameter.
        self.used_time = used_time
        # The ID of the user backup. You can call the ListUserBackupFiles operation to query the ID. If you specify this parameter, the instance is created based on the user backup.
        # 
        # If you specify this parameter, the following limits apply:
        # 
        # - The PayType parameter must be set to Postpaid.
        # - The Engine parameter must be set to MySQL.
        # - The EngineVersion parameter must be set to 5.7.
        # - The Category parameter must be set to Basic.
        self.user_backup_id = user_backup_id
        # The ID of the vSwitch in the VPC.
        self.v_switch_id = v_switch_id
        # The ID of the VPC.
        self.vpc_id = vpc_id
        # The whitelist. To configure multiple IP addresses, separate the IP addresses or CIDR blocks with commas (,) without spaces before or after the commas. Example: `192.168.0.1,172.16.213.9`.
        self.whitelist_template_list = whitelist_template_list
        # The zone ID of the primary node.
        self.zone_id = zone_id
        # The zone ID of the secondary node.
        # 
        # - If you set this parameter to **Auto**, it indicates a multi-zone deployment and the system automatically selects an active zone for the secondary node.
        # - If you set this parameter to the same value as **ZoneId**, it is a single-zone deployment.
        # - If you set this parameter to a value different from **ZoneId**, it is a multi-zone deployment.
        self.zone_id_slave_1 = zone_id_slave_1
        # The secondary zone 2.
        # > This parameter is active only for instances of the RDS Enterprise Edition.
        self.zone_id_slave_2 = zone_id_slave_2

    def validate(self):
        if self.serverless_config:
            self.serverless_config.validate()
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['Amount'] = self.amount

        if self.auto_create_proxy is not None:
            result['AutoCreateProxy'] = self.auto_create_proxy

        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.babelfish_config is not None:
            result['BabelfishConfig'] = self.babelfish_config

        if self.bpe_enabled is not None:
            result['BpeEnabled'] = self.bpe_enabled

        if self.bursting_enabled is not None:
            result['BurstingEnabled'] = self.bursting_enabled

        if self.business_info is not None:
            result['BusinessInfo'] = self.business_info

        if self.category is not None:
            result['Category'] = self.category

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cold_data_enabled is not None:
            result['ColdDataEnabled'] = self.cold_data_enabled

        if self.connection_mode is not None:
            result['ConnectionMode'] = self.connection_mode

        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string

        if self.create_strategy is not None:
            result['CreateStrategy'] = self.create_strategy

        if self.dbinstance_class is not None:
            result['DBInstanceClass'] = self.dbinstance_class

        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description

        if self.dbinstance_net_type is not None:
            result['DBInstanceNetType'] = self.dbinstance_net_type

        if self.dbinstance_storage is not None:
            result['DBInstanceStorage'] = self.dbinstance_storage

        if self.dbinstance_storage_type is not None:
            result['DBInstanceStorageType'] = self.dbinstance_storage_type

        if self.dbis_ignore_case is not None:
            result['DBIsIgnoreCase'] = self.dbis_ignore_case

        if self.dbparam_group_id is not None:
            result['DBParamGroupId'] = self.dbparam_group_id

        if self.dbtime_zone is not None:
            result['DBTimeZone'] = self.dbtime_zone

        if self.db_list is not None:
            result['DbList'] = self.db_list

        if self.db_list_mode is not None:
            result['DbListMode'] = self.db_list_mode

        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id

        if self.deletion_protection is not None:
            result['DeletionProtection'] = self.deletion_protection

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.encryption_key is not None:
            result['EncryptionKey'] = self.encryption_key

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.instance_network_type is not None:
            result['InstanceNetworkType'] = self.instance_network_type

        if self.io_acceleration_enabled is not None:
            result['IoAccelerationEnabled'] = self.io_acceleration_enabled

        if self.master_account_exist is not None:
            result['MasterAccountExist'] = self.master_account_exist

        if self.master_account_name is not None:
            result['MasterAccountName'] = self.master_account_name

        if self.master_account_password is not None:
            result['MasterAccountPassword'] = self.master_account_password

        if self.master_database_name is not None:
            result['MasterDatabaseName'] = self.master_database_name

        if self.master_engine_arch_type is not None:
            result['MasterEngineArchType'] = self.master_engine_arch_type

        if self.master_instance_id is not None:
            result['MasterInstanceId'] = self.master_instance_id

        if self.master_region is not None:
            result['MasterRegion'] = self.master_region

        if self.master_shard_account_name is not None:
            result['MasterShardAccountName'] = self.master_shard_account_name

        if self.master_shard_account_password is not None:
            result['MasterShardAccountPassword'] = self.master_shard_account_password

        if self.need_create_slave is not None:
            result['NeedCreateSlave'] = self.need_create_slave

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.period is not None:
            result['Period'] = self.period

        if self.port is not None:
            result['Port'] = self.port

        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.role_arn is not None:
            result['RoleARN'] = self.role_arn

        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist

        if self.serverless_config is not None:
            result['ServerlessConfig'] = self.serverless_config.to_map()

        if self.slave_account_exist is not None:
            result['SlaveAccountExist'] = self.slave_account_exist

        if self.slave_account_name is not None:
            result['SlaveAccountName'] = self.slave_account_name

        if self.slave_account_password is not None:
            result['SlaveAccountPassword'] = self.slave_account_password

        if self.slave_database_name is not None:
            result['SlaveDatabaseName'] = self.slave_database_name

        if self.slave_engine_arch_type is not None:
            result['SlaveEngineArchType'] = self.slave_engine_arch_type

        if self.slave_instance_id is not None:
            result['SlaveInstanceId'] = self.slave_instance_id

        if self.slave_read_only is not None:
            result['SlaveReadOnly'] = self.slave_read_only

        if self.slave_region is not None:
            result['SlaveRegion'] = self.slave_region

        if self.storage_auto_scale is not None:
            result['StorageAutoScale'] = self.storage_auto_scale

        if self.storage_threshold is not None:
            result['StorageThreshold'] = self.storage_threshold

        if self.storage_upper_bound is not None:
            result['StorageUpperBound'] = self.storage_upper_bound

        if self.sync_account_type is not None:
            result['SyncAccountType'] = self.sync_account_type

        if self.sync_architecture is not None:
            result['SyncArchitecture'] = self.sync_architecture

        if self.sync_conflict is not None:
            result['SyncConflict'] = self.sync_conflict

        if self.system_dbcharset is not None:
            result['SystemDBCharset'] = self.system_dbcharset

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.target_dedicated_host_id_for_log is not None:
            result['TargetDedicatedHostIdForLog'] = self.target_dedicated_host_id_for_log

        if self.target_dedicated_host_id_for_master is not None:
            result['TargetDedicatedHostIdForMaster'] = self.target_dedicated_host_id_for_master

        if self.target_dedicated_host_id_for_slave is not None:
            result['TargetDedicatedHostIdForSlave'] = self.target_dedicated_host_id_for_slave

        if self.target_minor_version is not None:
            result['TargetMinorVersion'] = self.target_minor_version

        if self.used_time is not None:
            result['UsedTime'] = self.used_time

        if self.user_backup_id is not None:
            result['UserBackupId'] = self.user_backup_id

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.whitelist_template_list is not None:
            result['WhitelistTemplateList'] = self.whitelist_template_list

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        if self.zone_id_slave_1 is not None:
            result['ZoneIdSlave1'] = self.zone_id_slave_1

        if self.zone_id_slave_2 is not None:
            result['ZoneIdSlave2'] = self.zone_id_slave_2

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('AutoCreateProxy') is not None:
            self.auto_create_proxy = m.get('AutoCreateProxy')

        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('BabelfishConfig') is not None:
            self.babelfish_config = m.get('BabelfishConfig')

        if m.get('BpeEnabled') is not None:
            self.bpe_enabled = m.get('BpeEnabled')

        if m.get('BurstingEnabled') is not None:
            self.bursting_enabled = m.get('BurstingEnabled')

        if m.get('BusinessInfo') is not None:
            self.business_info = m.get('BusinessInfo')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ColdDataEnabled') is not None:
            self.cold_data_enabled = m.get('ColdDataEnabled')

        if m.get('ConnectionMode') is not None:
            self.connection_mode = m.get('ConnectionMode')

        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')

        if m.get('CreateStrategy') is not None:
            self.create_strategy = m.get('CreateStrategy')

        if m.get('DBInstanceClass') is not None:
            self.dbinstance_class = m.get('DBInstanceClass')

        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')

        if m.get('DBInstanceNetType') is not None:
            self.dbinstance_net_type = m.get('DBInstanceNetType')

        if m.get('DBInstanceStorage') is not None:
            self.dbinstance_storage = m.get('DBInstanceStorage')

        if m.get('DBInstanceStorageType') is not None:
            self.dbinstance_storage_type = m.get('DBInstanceStorageType')

        if m.get('DBIsIgnoreCase') is not None:
            self.dbis_ignore_case = m.get('DBIsIgnoreCase')

        if m.get('DBParamGroupId') is not None:
            self.dbparam_group_id = m.get('DBParamGroupId')

        if m.get('DBTimeZone') is not None:
            self.dbtime_zone = m.get('DBTimeZone')

        if m.get('DbList') is not None:
            self.db_list = m.get('DbList')

        if m.get('DbListMode') is not None:
            self.db_list_mode = m.get('DbListMode')

        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')

        if m.get('DeletionProtection') is not None:
            self.deletion_protection = m.get('DeletionProtection')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('EncryptionKey') is not None:
            self.encryption_key = m.get('EncryptionKey')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('InstanceNetworkType') is not None:
            self.instance_network_type = m.get('InstanceNetworkType')

        if m.get('IoAccelerationEnabled') is not None:
            self.io_acceleration_enabled = m.get('IoAccelerationEnabled')

        if m.get('MasterAccountExist') is not None:
            self.master_account_exist = m.get('MasterAccountExist')

        if m.get('MasterAccountName') is not None:
            self.master_account_name = m.get('MasterAccountName')

        if m.get('MasterAccountPassword') is not None:
            self.master_account_password = m.get('MasterAccountPassword')

        if m.get('MasterDatabaseName') is not None:
            self.master_database_name = m.get('MasterDatabaseName')

        if m.get('MasterEngineArchType') is not None:
            self.master_engine_arch_type = m.get('MasterEngineArchType')

        if m.get('MasterInstanceId') is not None:
            self.master_instance_id = m.get('MasterInstanceId')

        if m.get('MasterRegion') is not None:
            self.master_region = m.get('MasterRegion')

        if m.get('MasterShardAccountName') is not None:
            self.master_shard_account_name = m.get('MasterShardAccountName')

        if m.get('MasterShardAccountPassword') is not None:
            self.master_shard_account_password = m.get('MasterShardAccountPassword')

        if m.get('NeedCreateSlave') is not None:
            self.need_create_slave = m.get('NeedCreateSlave')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('RoleARN') is not None:
            self.role_arn = m.get('RoleARN')

        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')

        if m.get('ServerlessConfig') is not None:
            temp_model = main_models.CreateGadOrderRequestServerlessConfig()
            self.serverless_config = temp_model.from_map(m.get('ServerlessConfig'))

        if m.get('SlaveAccountExist') is not None:
            self.slave_account_exist = m.get('SlaveAccountExist')

        if m.get('SlaveAccountName') is not None:
            self.slave_account_name = m.get('SlaveAccountName')

        if m.get('SlaveAccountPassword') is not None:
            self.slave_account_password = m.get('SlaveAccountPassword')

        if m.get('SlaveDatabaseName') is not None:
            self.slave_database_name = m.get('SlaveDatabaseName')

        if m.get('SlaveEngineArchType') is not None:
            self.slave_engine_arch_type = m.get('SlaveEngineArchType')

        if m.get('SlaveInstanceId') is not None:
            self.slave_instance_id = m.get('SlaveInstanceId')

        if m.get('SlaveReadOnly') is not None:
            self.slave_read_only = m.get('SlaveReadOnly')

        if m.get('SlaveRegion') is not None:
            self.slave_region = m.get('SlaveRegion')

        if m.get('StorageAutoScale') is not None:
            self.storage_auto_scale = m.get('StorageAutoScale')

        if m.get('StorageThreshold') is not None:
            self.storage_threshold = m.get('StorageThreshold')

        if m.get('StorageUpperBound') is not None:
            self.storage_upper_bound = m.get('StorageUpperBound')

        if m.get('SyncAccountType') is not None:
            self.sync_account_type = m.get('SyncAccountType')

        if m.get('SyncArchitecture') is not None:
            self.sync_architecture = m.get('SyncArchitecture')

        if m.get('SyncConflict') is not None:
            self.sync_conflict = m.get('SyncConflict')

        if m.get('SystemDBCharset') is not None:
            self.system_dbcharset = m.get('SystemDBCharset')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateGadOrderRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('TargetDedicatedHostIdForLog') is not None:
            self.target_dedicated_host_id_for_log = m.get('TargetDedicatedHostIdForLog')

        if m.get('TargetDedicatedHostIdForMaster') is not None:
            self.target_dedicated_host_id_for_master = m.get('TargetDedicatedHostIdForMaster')

        if m.get('TargetDedicatedHostIdForSlave') is not None:
            self.target_dedicated_host_id_for_slave = m.get('TargetDedicatedHostIdForSlave')

        if m.get('TargetMinorVersion') is not None:
            self.target_minor_version = m.get('TargetMinorVersion')

        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')

        if m.get('UserBackupId') is not None:
            self.user_backup_id = m.get('UserBackupId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('WhitelistTemplateList') is not None:
            self.whitelist_template_list = m.get('WhitelistTemplateList')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        if m.get('ZoneIdSlave1') is not None:
            self.zone_id_slave_1 = m.get('ZoneIdSlave1')

        if m.get('ZoneIdSlave2') is not None:
            self.zone_id_slave_2 = m.get('ZoneIdSlave2')

        return self

class CreateGadOrderRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. You can call the [ListTagResources](https://help.aliyun.com/document_detail/191187.html) operation to query the tag key.
        # 
        # > - N indicates the sequence number of the tag key. For example, Tag.1.Key indicates the key of the first tag, and Tag.2.Key indicates the key of the second tag. You can specify 1 to 20 tag keys at a time.
        # - This parameter cannot be set to an empty string.
        self.key = key
        # The tag value. You can call the [ListTagResources](https://help.aliyun.com/document_detail/191187.html) operation to query the tag value.
        # > - N indicates the sequence number of the tag value. For example, Tag.1.Value indicates the value of the first tag, and Tag.2.Value indicates the value of the second tag. You can specify 1 to 20 tag values at a time.
        # - This parameter can be set to an empty string.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateGadOrderRequestServerlessConfig(DaraModel):
    def __init__(
        self,
        auto_pause: bool = None,
        max_capacity: float = None,
        min_capacity: float = None,
        switch_force: bool = None,
    ):
        # Specifies whether to enable the smart pause and start feature for the Serverless instance. Valid values:
        # * **true**: enables the feature.
        # * **false**: disables the feature. This is the default value.
        # 
        # > This parameter is required only for MySQL and PostgreSQL Serverless instances. If no connections are established within 10 minutes, the instance enters the paused state. When a connection is established, the instance is automatically woken up.
        self.auto_pause = auto_pause
        # The maximum number of RDS capacity units (RCUs) for automatic scaling of the instance. Valid values:
        # 
        # - MySQL: **1 to 32**
        # - SQL Server: **2 to 16**
        # - PostgreSQL: **1 to 14**
        # 
        # > The value of this parameter must be greater than or equal to the value of **MinCapacity**. Only **integers** are supported.
        self.max_capacity = max_capacity
        # The minimum number of RCUs for automatic scaling of the instance. Valid values:
        # 
        # - MySQL: **0.5 to 32**
        # - SQL Server: **2 to 16** (only integers are supported)
        # - PostgreSQL: **0.5 to 14**
        # 
        # > The value of this parameter must be less than or equal to the value of **MaxCapacity**.
        self.min_capacity = min_capacity
        # Specifies whether to enable forced elastic scaling for the Serverless instance. Valid values:
        # * **true**: enables forced elastic scaling.
        # * **false**: disables forced elastic scaling. This is the default value.
        # 
        # > * This parameter is required only for MySQL and PostgreSQL Serverless instances. After this parameter is enabled, the instance will be unavailable for 30 to 120 seconds during forced scaling. Use this feature with caution based on your business requirements.
        # > * Elastic scaling of instance RCUs usually takes effect immediately. However, in some special cases (such as during the execution of large transactions), scaling cannot be completed immediately. In this case, you can enable this parameter to perform forced scaling.
        self.switch_force = switch_force

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_pause is not None:
            result['AutoPause'] = self.auto_pause

        if self.max_capacity is not None:
            result['MaxCapacity'] = self.max_capacity

        if self.min_capacity is not None:
            result['MinCapacity'] = self.min_capacity

        if self.switch_force is not None:
            result['SwitchForce'] = self.switch_force

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPause') is not None:
            self.auto_pause = m.get('AutoPause')

        if m.get('MaxCapacity') is not None:
            self.max_capacity = m.get('MaxCapacity')

        if m.get('MinCapacity') is not None:
            self.min_capacity = m.get('MinCapacity')

        if m.get('SwitchForce') is not None:
            self.switch_force = m.get('SwitchForce')

        return self

