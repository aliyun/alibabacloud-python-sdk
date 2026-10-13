# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class CreateDBInstanceRequest(DaraModel):
    def __init__(
        self,
        amount: int = None,
        auto_create_proxy: bool = None,
        auto_pay: bool = None,
        auto_renew: str = None,
        auto_use_coupon: bool = None,
        babelfish_config: str = None,
        bpe_enabled: str = None,
        bursting_enabled: bool = None,
        business_info: str = None,
        category: str = None,
        client_token: str = None,
        cold_data_enabled: bool = None,
        connection_mode: str = None,
        connection_string: str = None,
        create_strategy: str = None,
        custom_extra_info: str = None,
        dbinstance_class: str = None,
        dbinstance_description: str = None,
        dbinstance_net_type: str = None,
        dbinstance_storage: int = None,
        dbinstance_storage_type: str = None,
        dbis_ignore_case: str = None,
        dbparam_group_id: str = None,
        dbtime_zone: str = None,
        dedicated_host_group_id: str = None,
        deletion_protection: bool = None,
        dry_run: bool = None,
        encryption_key: str = None,
        engine: str = None,
        engine_version: str = None,
        external_replication: bool = None,
        instance_network_type: str = None,
        io_acceleration_enabled: str = None,
        optimized_writes: str = None,
        pay_type: str = None,
        period: str = None,
        port: str = None,
        private_ip_address: str = None,
        promotion_code: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_id: int = None,
        role_arn: str = None,
        security_iplist: str = None,
        serverless_config: main_models.CreateDBInstanceRequestServerlessConfig = None,
        storage_auto_scale: str = None,
        storage_threshold: int = None,
        storage_upper_bound: int = None,
        system_dbcharset: str = None,
        tag: List[main_models.CreateDBInstanceRequestTag] = None,
        target_dedicated_host_id_for_log: str = None,
        target_dedicated_host_id_for_master: str = None,
        target_dedicated_host_id_for_slave: str = None,
        target_minor_version: str = None,
        used_time: str = None,
        user_backup_id: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
        whitelist_template_list: str = None,
        zone_id: str = None,
        zone_id_slave_1: str = None,
        zone_id_slave_2: str = None,
    ):
        # The number of ApsaraDB RDS for MySQL instances to create. This parameter is applicable only when you create multiple ApsaraDB RDS for MySQL instances at a time.
        # 
        # Valid values: **1** to **20**. Default value: **1**.
        # 
        # > - When you create multiple ApsaraDB RDS for MySQL instances, you can use the **Tag.Key** and **Tag.Value** parameters to add tags to the instances in the same batch. This facilitates instance management by tag after creation.
        # > - After multiple instances are created, the API operation returns only the **TaskId**, **RequestId**, and **Message** parameters. Other detail parameters are not returned. To query the details of a specific instance, call the DescribeDBInstanceAttribute operation.
        # > - If **Engine** is not set to **MySQL** and the value of this parameter is greater than **1**, the API operation fails and returns the error code `InvalidParam.Engine`.
        self.amount = amount
        # Specifies whether to automatically create a proxy. Valid values:
        # 
        # - **true**: enables automatic creation. By default, a general-purpose proxy is created.
        # - **false**: disables automatic creation.
        self.auto_create_proxy = auto_create_proxy
        # Specifies whether to enable automatic payment. Valid values:
        # 
        # - **true**: enables automatic payment. Make sure that your account balance is sufficient.
        # - **false**: generates an order without deducting fees.
        # 
        # > The default value is true. If your payment method has an insufficient balance, you can set AutoPay to false. In this case, an unpaid order is generated, and you can log on to the ApsaraDB RDS console to complete the payment.
        # >
        self.auto_pay = auto_pay
        # Specifies whether to enable auto-renewal for the instance. This parameter is valid only when you create a subscription instance. Valid values:
        # - **true**
        # - **false**
        # 
        # > - If you purchase the instance on a monthly basis, the auto-renewal epoch is one month.
        # > - If you purchase the instance on a yearly basis, the auto-renewal epoch is one year.
        self.auto_renew = auto_renew
        # Specifies whether to use a voucher. Valid values:
        # * **true**: uses a voucher.
        # * **false**: does not use a voucher. This is the default value.
        # 
        # > If you use a voucher and later need to downgrade the instance configuration, the amount deducted by the voucher will not be refunded.
        self.auto_use_coupon = auto_use_coupon
        # The configuration information for Babelfish for ApsaraDB RDS for PostgreSQL.
        # 
        # Configuration format: {"babelfishEnabled":"true","migrationMode":"xxxxxxx","masterUsername":"xxxxxxx","masterUserPassword":"xxxxxxxx"}
        # 
        # Parameter description:
        # - **babelfishEnabled**: specifies whether to enable Babelfish. Set the value to **true** to enable Babelfish. By default, Babelfish is disabled.
        # - **migrationMode**: the database mode. Set the value to **single-db** for the single-database mode or **multi-db** for the multi-database mode.
        # - **masterUsername**: the initial administrator account. The username must be 1 to 63 characters in length and can contain lowercase letters, digits, and underscores (_). It must start with a letter and end with a letter or digit. It cannot start with pg.
        # - **masterUserPassword**: the password of the administrator account. The password must be 8 to 32 characters in length and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. Special characters include `! @ # $ % ^ & * () _ + - =`.
        # 
        # > This parameter is applicable only to ApsaraDB RDS for PostgreSQL instances. For more information about Babelfish for ApsaraDB RDS for PostgreSQL, see [Babelfish overview](https://help.aliyun.com/document_detail/428613.html).
        self.babelfish_config = babelfish_config
        self.bpe_enabled = bpe_enabled
        # Specifies whether to enable the I/O performance burst feature for Premium ESSD cloud disks. Valid values:
        # * **true**: enables the feature.
        # * **false**: disables the feature.
        # > For more information about the I/O performance burst feature for Premium ESSD cloud disks, see [What is a Premium ESSD cloud disk?](https://help.aliyun.com/document_detail/2340501.html).
        self.bursting_enabled = bursting_enabled
        # The extended business parameters.
        self.business_info = business_info
        # The instance edition. Valid values:
        # * Regular instances
        #     * **Basic**: Basic Edition.
        #     * **HighAvailability**: high-availability series.
        #     * **cluster**: Cluster Edition for MySQL or PostgreSQL.
        #     * **AlwaysOn**: Cluster Edition for SQL Server.
        #     * **Finance**: RDS Enterprise Edition.
        #     > This parameter is required when you create a SQL Server Enterprise Edition Cluster<props="china">, Basic Edition Standard, or Basic Edition Enterprise instance. For example, when you create a Basic Edition 2022 Enterprise Edition Cluster (2022_ent) instance, you must set this parameter to Basic.
        # * Serverless instances
        #     * **serverless_basic**: Serverless Basic Edition. This value is applicable only to MySQL and PostgreSQL.
        #     * **serverless_standard**: Serverless high-availability series. This value is applicable only to MySQL and PostgreSQL.
        #     * **serverless_ha**: Serverless high-availability series for SQL Server.
        # 
        #     > This parameter is required when PayType is set to Serverless.
        self.category = category
        # The client token that is used to ensure the idempotence of the request and prevent duplicate submissions. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # Specifies whether to enable the [data archiving](https://help.aliyun.com/document_detail/2701832.html) feature for Premium ESSD cloud disks. Valid values:
        # 
        # - **true**: enables the feature.
        # - **false**: disables the feature.
        self.cold_data_enabled = cold_data_enabled
        # The access mode of the instance. Valid values:
        # * **Standard**: standard access mode.
        # * **Safe**: database proxy mode.
        # 
        # The default value is allocated by the RDS system.
        # > SQL Server 2012, 2016, and 2017 instances support only the standard access mode.
        self.connection_mode = connection_mode
        # The internal endpoint of the database.
        # 
        # Endpoint format: `xxx.mysql.rds.aliyuncs.com`, where `xxx` is the prefix of the instance ID, such as rm-uf6wjk5***.
        self.connection_string = connection_string
        # The strategy for creating multiple instances at a time. This parameter takes effect only when **Amount** is greater than 1. Valid values:
        # * **Atomicity**: atomicity. All instances in the same batch are created successfully, or none of them are created if one fails. This is the default value.
        # * **Partial**: non-atomicity. The creation of an instance is not affected by other instances in the same batch.
        self.create_strategy = create_strategy
        self.custom_extra_info = custom_extra_info
        # The instance type. You can specify a standard or Yitian instance type. For more information, see [Primary ApsaraDB RDS instance types](https://help.aliyun.com/document_detail/26312.html).
        # 
        # To create a Serverless instance, specify one of the following values:
        # 
        # - MySQL Basic Edition: **mysql.n2.serverless.1c**
        # - MySQL high-availability series: **mysql.n2.serverless.2c**
        # - SQL Server: **mssql.mem2.serverless.s2**
        # - PostgreSQL Basic Edition: **pg.n2.serverless.1c**
        # - PostgreSQL high-availability series: **pg.n2.serverless.2c**
        # 
        # This parameter is required.
        self.dbinstance_class = dbinstance_class
        # The name of the instance. The name must be 2 to 255 characters in length. It must start with a letter and can contain digits, letters, and hyphens (-).
        # > The name cannot start with http:// or https://.
        self.dbinstance_description = dbinstance_description
        # The network connectivity type of the instance. Set the value to **Intranet**, which indicates an internal network connection.
        # 
        # This parameter is required.
        self.dbinstance_net_type = dbinstance_net_type
        # Instance storage capacity of the instance. Unit: GB. Instance storage capacity increases in increments of 5 GB. For more information about the valid values, see [Primary ApsaraDB RDS instance types](https://help.aliyun.com/document_detail/26312.html).
        # 
        # This parameter is required.
        self.dbinstance_storage = dbinstance_storage
        # The storage type of the instance. Valid values:
        # * **local_ssd**: high-performance local SSD (recommended).
        # * **general_essd**: Premium ESSD cloud disk (recommended).
        # * **cloud_essd**: PL1 ESSD.
        # * **cloud_essd2**: PL2 ESSD.
        # * **cloud_essd3**: PL3 ESSD.
        # * **cloud_ssd**: standard SSD (not recommended, discontinued in some regions).
        # 
        # The default value of this parameter is automatically determined based on the instance type specified by **DBInstanceClass**:
        # * If the instance type is a high-performance local SSD type, the default value is **local_ssd**.
        # * If the instance type is a cloud disk type, the default value is **cloud_essd**.
        # 
        # > Serverless instances support only PL1 ESSDs and Premium ESSD cloud disks.
        self.dbinstance_storage_type = dbinstance_storage_type
        # Specifies whether table names are case-sensitive. Valid values:
        # * **true**: Table names are not case-sensitive. This is the default value.
        # * **false**: Table names are case-sensitive.
        self.dbis_ignore_case = dbis_ignore_case
        # The ID of the parameter template. You can call the DescribeParameterGroups operation to query the parameter template ID.
        # > This parameter is supported only by MySQL and PostgreSQL. If you do not specify this parameter, the default parameter template is used. You can also create a custom parameter template and specify it here.
        self.dbparam_group_id = dbparam_group_id
        # The time zone of the instance. This parameter takes effect only when **Engine** is set to **MySQL** or **PostgreSQL**.
        # 
        # - If **Engine** is set to **MySQL**:
        #     - This parameter specifies the UTC time zone. Valid values: **-12:59** to **+13:00**.
        #     - For an instance with Premium Local SSDs, you can specify a named time zone, such as Asia/Hong_Kong. For more information about named time zones, see [Named time zones](https://help.aliyun.com/document_detail/297356.html).
        # - If **Engine** is set to **PostgreSQL**:
        #     - This parameter specifies a named time zone. UTC time zones are not supported. For more information about named time zones, see [Named time zones](https://help.aliyun.com/document_detail/297356.html).
        #     - This parameter can be configured only for ApsaraDB RDS for PostgreSQL instances with cloud disks.
        # 
        # > - You can set the time zone when you purchase a primary instance. Read-only instances do not support parameter settings for the time zone and inherit the time zone of the primary instance.
        # > - If you do not specify this parameter, the system selects the default time zone based on the region where the instance is created.
        self.dbtime_zone = dbtime_zone
        # The ID of the dedicated cluster host group.
        # 
        # This parameter is required when you create an instance in a dedicated cluster.
        # 
        # - You can call the DescribeDedicatedHostGroups operation to query the host group information.
        # - If you have not created a host group, you can call the CreateDedicatedHostGroup operation to create one.
        self.dedicated_host_group_id = dedicated_host_group_id
        # Specifies whether to enable release protection for the instance. This feature is supported only for pay-as-you-go instances. Valid values:
        # * **true**: enables release protection.
        # * **false**: disables release protection. This is the default value.
        self.deletion_protection = deletion_protection
        # Specifies whether to perform a precheck before creating the instance. Valid values:
        # * **true**: performs a precheck but does not create the instance. The system checks the request parameters, request format, service limits, and inventory.
        # * **false**: sends a normal request and creates the instance after the request passes the precheck. This is the default value.
        self.dry_run = dry_run
        # The ID of the key used for cloud disk encryption in the same region. If you specify this parameter, cloud disk encryption is enabled and cannot be disabled. You must also specify **RoleARN**.
        # 
        # You can view the key ID or create a new key in the Key Management Service (KMS) console. For more information, see [Create a key](https://help.aliyun.com/document_detail/181610.html).
        # 
        # > - For ApsaraDB RDS for MySQL, ApsaraDB RDS for PostgreSQL, and ApsaraDB RDS for SQL Server, you do not need to specify this parameter. You only need to specify **RoleARN** to use the service key to create an instance with cloud disk encryption enabled.
        # > - If RAM authorization requires RAM users to enable cloud disk encryption when creating instances, the instances cannot be created if cloud disk encryption is not enabled. Configure the following RAM policy for the RAM user:
        # `{"Version":"1","Statement":[{"Effect":"Deny","Action":"rds:CreateDBInstance","Resource":"*","Condition":{"StringEquals":{"rds:DiskEncryptionRequired":"false"}}}]}`
        # >Warning: This configuration also affects the CreateOrder operation for creating instances in the console.
        self.encryption_key = encryption_key
        # The database engine. Valid values:
        # * **MySQL**
        # * **SQLServer**
        # * **PostgreSQL**
        # * **MariaDB**
        # 
        # This parameter is required.
        self.engine = engine
        # The database engine version. Valid values:
        # * Regular instances
        #     * MySQL: **5.5**, **5.6**, **5.7**, and **8.0**
        #     * SQL Server: **08r2_ent_ha** (cloud disk edition, discontinued), **2008r2** (high-performance local SSD, discontinued), **2012** (Enterprise Edition Standalone), **2012_ent_ha**, **2012_std_ha**, **2012_web**, **2014_ent_ha**, **2014_std_ha**, **2016_ent_ha**, **2016_std_ha**, **2016_web**, **2017_ent**, **2017_std_ha**, **2017_web**, **2019_ent**, **2019_std_ha**, **2019_web**, **2022_ent**, **2022_std_ha**, **2022_web**, **2025_ent**, and **2025_std**
        #     * PostgreSQL: **10.0**, **11.0**, **12.0**, **13.0**, **14.0**, **15.0**, **16.0**, **17.0**, and **18.0**
        #     * MariaDB: **10.3** and **10.6**
        # * Serverless instances
        #     * MySQL: **5.7** and **8.0**
        #     * SQL Server: **2016_std_sl**, **2017_std_sl**, and **2019_std_sl**
        #     * PostgreSQL: **14.0**, **15.0**, **16.0**, **17.0**, and **18.0**
        # 
        # > - MariaDB does not support Serverless instances.
        # > - For SQL Server instances, `_ent` indicates the Enterprise Edition Cluster, `_ent_ha` indicates the Enterprise Edition, `_std_ha` indicates the Standard Edition, and `_web` indicates the Web Edition.
        # > - SQL Server 2014 instances are not available on the international site.
        # > - Babelfish for ApsaraDB RDS for PostgreSQL instances support only major version 15.0.
        # 
        # This parameter is required.
        self.engine_version = engine_version
        # Specifies whether to enable [native replication for ApsaraDB RDS for MySQL](https://help.aliyun.com/document_detail/2856526.html). Valid values:
        # - **ON**: enables native replication.
        # - **OFF**: disables native replication.
        self.external_replication = external_replication
        # The network type of the instance. Valid values:
        # 
        # * **VPC**: Virtual Private Cloud (VPC).
        # * **Classic**: classic network.
        # 
        # > * ApsaraDB RDS for MySQL cloud disk instances support only VPCs. You must set this parameter to **VPC**.
        # > * ApsaraDB RDS for PostgreSQL and ApsaraDB RDS for MariaDB instances support only VPCs. You must set this parameter to **VPC**.
        # > * ApsaraDB RDS for SQL Server Basic Edition and Web Edition instances support both the classic network and VPCs. Other instances support only VPCs. You must set this parameter to **VPC**.
        self.instance_network_type = instance_network_type
        # Specifies whether to enable the [Buffer Pool Extension (BPE)](https://help.aliyun.com/document_detail/2527067.html) feature for Premium ESSD cloud disks. Valid values:
        # 
        #  - **1**: enables the feature.
        #  - **0**: disables the feature.
        self.io_acceleration_enabled = io_acceleration_enabled
        # Specifies whether to enable the [16KB atomic write](https://help.aliyun.com/document_detail/2858761.html) feature. Valid values:
        # 
        # - **optimized**: enables the feature.
        # - **none**: disables the feature. This is the default value.
        self.optimized_writes = optimized_writes
        # The billing method of the instance. Valid values:
        # - **Postpaid**: pay-as-you-go.
        # - **Prepaid**: subscription.
        # - **Serverless**: Serverless billing method. MariaDB instances are not supported. For more information, see [Overview of ApsaraDB RDS for MySQL Serverless instances](https://help.aliyun.com/document_detail/411291.html), [Overview of ApsaraDB RDS for SQL Server Serverless instances](https://help.aliyun.com/document_detail/604344.html), and [Overview of ApsaraDB RDS for PostgreSQL Serverless instances](https://help.aliyun.com/document_detail/607742.html).
        # > The system automatically generates an order and completes the payment. You do not need to manually confirm the payment.
        # 
        # This parameter is required.
        self.pay_type = pay_type
        # The subscription period unit. Valid values:
        # * **Year**: year.
        # * **Month**: month.
        # 
        # > This parameter is required when **PayType** is set to **Prepaid**.
        self.period = period
        # The port used to initialize the instance upon creation. Valid values:
        # - MySQL: 1000 to 65534
        # - PostgreSQL, SQL Server, and MariaDB: 1000 to 5999
        self.port = port
        # The internal IP address of the instance. The IP address must be within the address range of the specified vSwitch. By default, the system automatically allocates an IP address based on **VPCId** and **VSwitchId**.
        self.private_ip_address = private_ip_address
        # The coupon code.
        self.promotion_code = promotion_code
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/610399.html) operation to query the region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        self.resource_owner_id = resource_owner_id
        # The global resource descriptor (ARN) used for the authorization of the ApsaraDB RDS service account by the primary account to access KMS. You can call the CheckCloudResourceAuthorized operation to query the descriptor.
        # >Notice: You must specify **RoleARN** when you enable cloud disk encryption.
        self.role_arn = role_arn
        # The [IP address whitelist](https://help.aliyun.com/document_detail/43185.html) of the instance. Separate multiple IP addresses or CIDR blocks with commas (,). Each IP address or CIDR block must be unique. You can add up to 1,000 IP addresses or CIDR blocks to the whitelist of a single instance. The following formats are supported:
        # * IP addresses, such as 10.10.XX.XX.
        # * CIDR blocks, such as 10.10.XX.XX/24. In this example, 24 indicates that the prefix of the CIDR block is 24 bits long. The prefix length ranges from 1 to 32 bits.
        # 
        # This parameter is required.
        self.security_iplist = security_iplist
        # The settings for the Serverless instance. This parameter is required when you create a Serverless instance.
        # > MariaDB does not support Serverless instances.
        self.serverless_config = serverless_config
        # Specifies whether to enable automatic storage expansion. This parameter is supported only by MySQL and PostgreSQL. Valid values:
        # * **Enable**: enables automatic storage expansion.
        # * **Disable**: disables automatic storage expansion. This is the default value.
        # 
        # > You can also call the ModifyDasInstanceConfig operation to adjust this setting after the instance is created. For more information, see [Configure automatic storage expansion](https://help.aliyun.com/document_detail/173826.html).
        self.storage_auto_scale = storage_auto_scale
        # The threshold that triggers automatic storage expansion. Unit: %. Valid values:
        # * **10**
        # * **20**
        # * **30**
        # * **40**
        # * **50**
        # 
        # > This parameter is required when **StorageAutoScale** is set to **Enable**.
        self.storage_threshold = storage_threshold
        # The maximum storage capacity after automatic storage expansion. Automatic storage expansion does not increase the total storage capacity of the instance beyond this value. Unit: GB.
        # 
        # > - The value must be greater than or equal to 0.
        # > - This parameter is required when **StorageAutoScale** is set to **Enable**.
        self.storage_upper_bound = storage_upper_bound
        # **[Deprecated]** This parameter is deprecated and does not need to be configured.
        self.system_dbcharset = system_dbcharset
        # The list of tags.
        self.tag = tag
        # The ID of the host for the logger node in the dedicated cluster.
        # 
        # This parameter is required when you create an RDS Enterprise Edition instance in a dedicated cluster. If you do not specify this parameter, the system automatically allocates a host by default.
        # 
        # - You can call the DescribeDedicatedHosts operation to query the host information in the dedicated cluster.
        # - If you do not have a host, you can call the CreateDedicatedHost operation to add one.
        self.target_dedicated_host_id_for_log = target_dedicated_host_id_for_log
        # The ID of the host on which the primary instance is created in the dedicated cluster.
        # 
        # This parameter is required when you create an instance in a dedicated cluster. If you do not specify this parameter, the system automatically assigns a host.
        # 
        # - You can call the DescribeDedicatedHosts operation to query the host information in the host group.
        # - If you do not have a host, you can call the CreateDedicatedHost operation to add one.
        self.target_dedicated_host_id_for_master = target_dedicated_host_id_for_master
        # The ID of the host on which the secondary instance is created in the dedicated cluster.
        # 
        # This parameter is required when you create a high-availability series or RDS Enterprise Edition instance in a dedicated cluster. If you do not specify this parameter, the system automatically allocates a host by default.
        # 
        # - You can call the DescribeDedicatedHosts operation to query the host information in the dedicated cluster.
        # - If you do not have a host, you can call the CreateDedicatedHost operation to add one.
        self.target_dedicated_host_id_for_slave = target_dedicated_host_id_for_slave
        # The minor engine version of the RDS instance to be created. This parameter is required only when you create a MySQL or PostgreSQL instance.
        # Format:
        # * MySQL: `<Instance version>_<Numeric version number>`. Examples: `rds_20200229`, `xcluster_20200229`, and `xcluster80_20200229`. Description:
        #     * rds: high-availability series or Basic Edition.
        #     * xcluster: MySQL 5.7 RDS Enterprise Edition.
        #     * xcluster80: MySQL 8.0 RDS Enterprise Edition.
        # 
        #     > You can call the DescribeDBMiniEngineVersions operation to query the numeric version number. For more information about the differences between versions, see [AliSQL release notes](https://help.aliyun.com/document_detail/96060.html).
        # * PostgreSQL: `rds_postgres_<Major version>00_<Minor engine version number>`. Example: `rds_postgres_1400_20220830`. Description:
        #     * 1400: PostgreSQL major version 14.
        #     * 20220830: AliPG minor engine version. You can call the DescribeDBMiniEngineVersions operation to query the minor engine version. For more information about the differences between versions, see [PostgreSQL release notes](https://help.aliyun.com/document_detail/126002.html).
        # 
        #     > If Babelfish is enabled in **BabelfishConfig**, the minor engine version format for ApsaraDB RDS for PostgreSQL is: `rds_postgres_<Major version>00_<AliPG minor engine version>_babelfish`.
        self.target_minor_version = target_minor_version
        # The subscription duration. Valid values:
        # * If **Period** is set to **Year**, the valid values of **UsedTime** are **1** to **5**.
        # * If **Period** is set to **Month**, the valid values of **UsedTime** are **1** to **11**.
        # 
        # > This parameter is required when **PayType** is set to **Prepaid**.
        self.used_time = used_time
        # The ID of the user backup. You can call the ListUserBackupFiles operation to query the backup ID. If you specify this parameter, the instance is created based on the user backup.
        # 
        # To specify this parameter, the following limits apply:
        # - **PayType** must be set to **Postpaid**.
        # - **Engine** must be set to **MySQL**.
        # - **EngineVersion** must be set to **5.7**.
        # - **Category** must be set to **Basic**.
        self.user_backup_id = user_backup_id
        # The ID of the VPC.
        # > This parameter takes effect only when the network type **InstanceNetworkType** is set to **VPC**.
        self.vpcid = vpcid
        # The ID of the vSwitch.
        # 
        # - **Zone mapping**: The zone of the vSwitch must match the zone of the primary node (**ZoneId**) and the zone of the secondary node (**ZoneIdSlave1**). If you specify two vSwitch IDs, their order must match the order of **ZoneId** and **ZoneIdSlave1**.
        # - **Network type limit**: **InstanceNetworkType** must be set to **VPC**.
        # - **Multiple vSwitches**: If you specify **ZoneIdSlave1** and the value is not **Auto**, you must specify two vSwitch IDs and separate them with a comma (,).
        # - **Character limit**: **VSwitchId** cannot contain special characters such as spaces, exclamation marks (!), number signs (#), currency symbols (¥), ampersands (&), and percent signs (%).
        self.v_switch_id = v_switch_id
        # The list of whitelists.
        # To configure multiple IP addresses, separate them with commas (,). Do not add spaces before or after the commas. Example: `192.168.0.1,172.16.213.9`.
        self.whitelist_template_list = whitelist_template_list
        # The zone ID of the primary node.
        # 
        # - If you specify a VPC and a vSwitch, you must specify the zone ID of the vSwitch. Otherwise, the instance cannot be created.
        # - For a high-availability series instance, you must also specify **ZoneIdSlave1** to determine whether the instance uses a single-zone deployment or multi-zone deployment.
        # - For an RDS Enterprise Edition instance, you must also specify **ZoneIdSlave1** and **ZoneIdSlave2** to determine whether the instance uses a single-zone deployment or multi-zone deployment.
        # - For an ApsaraDB RDS Cluster Edition instance, you must also specify **ZoneIdSlave1** for a two-node instance, and both **ZoneIdSlave1** and **ZoneIdSlave2** for a three-node instance.
        self.zone_id = zone_id
        # The zone ID of the secondary node.
        # 
        # - If you set this parameter to **Auto**, the instance uses a multi-zone deployment and the system automatically selects a zone for the secondary node.
        # - If you set this parameter to the same value as **ZoneId**, the instance uses a single-zone deployment.
        # - If you set this parameter to a value different from **ZoneId**, the instance uses a multi-zone deployment.
        self.zone_id_slave_1 = zone_id_slave_1
        # The zone ID of the second secondary node. ApsaraDB RDS for MySQL Cluster Edition instances support the creation of one or two secondary nodes when you create an instance. You can use this parameter to specify the zone of the second secondary node.
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

        if self.auto_use_coupon is not None:
            result['AutoUseCoupon'] = self.auto_use_coupon

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

        if self.cold_data_enabled is not None:
            result['ColdDataEnabled'] = self.cold_data_enabled

        if self.connection_mode is not None:
            result['ConnectionMode'] = self.connection_mode

        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string

        if self.create_strategy is not None:
            result['CreateStrategy'] = self.create_strategy

        if self.custom_extra_info is not None:
            result['CustomExtraInfo'] = self.custom_extra_info

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

        if self.external_replication is not None:
            result['ExternalReplication'] = self.external_replication

        if self.instance_network_type is not None:
            result['InstanceNetworkType'] = self.instance_network_type

        if self.io_acceleration_enabled is not None:
            result['IoAccelerationEnabled'] = self.io_acceleration_enabled

        if self.optimized_writes is not None:
            result['OptimizedWrites'] = self.optimized_writes

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.period is not None:
            result['Period'] = self.period

        if self.port is not None:
            result['Port'] = self.port

        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address

        if self.promotion_code is not None:
            result['PromotionCode'] = self.promotion_code

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.role_arn is not None:
            result['RoleARN'] = self.role_arn

        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist

        if self.serverless_config is not None:
            result['ServerlessConfig'] = self.serverless_config.to_map()

        if self.storage_auto_scale is not None:
            result['StorageAutoScale'] = self.storage_auto_scale

        if self.storage_threshold is not None:
            result['StorageThreshold'] = self.storage_threshold

        if self.storage_upper_bound is not None:
            result['StorageUpperBound'] = self.storage_upper_bound

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

        if self.vpcid is not None:
            result['VPCId'] = self.vpcid

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

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

        if m.get('AutoUseCoupon') is not None:
            self.auto_use_coupon = m.get('AutoUseCoupon')

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

        if m.get('ColdDataEnabled') is not None:
            self.cold_data_enabled = m.get('ColdDataEnabled')

        if m.get('ConnectionMode') is not None:
            self.connection_mode = m.get('ConnectionMode')

        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')

        if m.get('CreateStrategy') is not None:
            self.create_strategy = m.get('CreateStrategy')

        if m.get('CustomExtraInfo') is not None:
            self.custom_extra_info = m.get('CustomExtraInfo')

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

        if m.get('ExternalReplication') is not None:
            self.external_replication = m.get('ExternalReplication')

        if m.get('InstanceNetworkType') is not None:
            self.instance_network_type = m.get('InstanceNetworkType')

        if m.get('IoAccelerationEnabled') is not None:
            self.io_acceleration_enabled = m.get('IoAccelerationEnabled')

        if m.get('OptimizedWrites') is not None:
            self.optimized_writes = m.get('OptimizedWrites')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')

        if m.get('PromotionCode') is not None:
            self.promotion_code = m.get('PromotionCode')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('RoleARN') is not None:
            self.role_arn = m.get('RoleARN')

        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')

        if m.get('ServerlessConfig') is not None:
            temp_model = main_models.CreateDBInstanceRequestServerlessConfig()
            self.serverless_config = temp_model.from_map(m.get('ServerlessConfig'))

        if m.get('StorageAutoScale') is not None:
            self.storage_auto_scale = m.get('StorageAutoScale')

        if m.get('StorageThreshold') is not None:
            self.storage_threshold = m.get('StorageThreshold')

        if m.get('StorageUpperBound') is not None:
            self.storage_upper_bound = m.get('StorageUpperBound')

        if m.get('SystemDBCharset') is not None:
            self.system_dbcharset = m.get('SystemDBCharset')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateDBInstanceRequestTag()
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

        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('WhitelistTemplateList') is not None:
            self.whitelist_template_list = m.get('WhitelistTemplateList')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        if m.get('ZoneIdSlave1') is not None:
            self.zone_id_slave_1 = m.get('ZoneIdSlave1')

        if m.get('ZoneIdSlave2') is not None:
            self.zone_id_slave_2 = m.get('ZoneIdSlave2')

        return self

class CreateDBInstanceRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. Specify this parameter to add a tag to the instance.
        # 
        # * If the specified tag key already exists, the tag key is directly added to the instance. You can call the ListTagResources operation to query existing tags.
        # * If the specified tag key does not exist, the system creates the tag key and adds it to the instance.
        # * Empty strings are not allowed.
        # * This parameter must be used together with **Tag.Value**.
        self.key = key
        # The tag value that corresponds to the tag key. Specify this parameter to add a tag to the instance.
        # 
        # * If the specified tag value exists for the corresponding tag key, the tag value is directly added to the instance. You can call the ListTagResources operation to query existing tags.
        # * If the specified tag value does not exist for the corresponding tag key, the system creates the tag value and adds it to the instance.
        # * This parameter must be used together with **Tag.Key**.
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

class CreateDBInstanceRequestServerlessConfig(DaraModel):
    def __init__(
        self,
        auto_pause: bool = None,
        max_capacity: float = None,
        min_capacity: float = None,
        switch_force: bool = None,
    ):
        # Specifies whether to enable the smart pause and resume feature for the Serverless instance. Valid values:
        # * **true**: enables the feature.
        # * **false**: disables the feature. This is the default value.
        # 
        # > This parameter is required only for MySQL and PostgreSQL Serverless instances. If no connections are established within 10 minutes, the instance enters the paused state and automatically resumes when a new connection is established.
        self.auto_pause = auto_pause
        # The maximum number of RDS capacity units (RCUs) for automatic scaling. Valid values:
        # 
        # - MySQL: **1** to **32**
        # - SQL Server: **2** to **16**
        # - PostgreSQL: **1** to **14**
        # 
        # > The value of this parameter must be greater than or equal to the value of **MinCapacity**. Only **integers** are supported.
        self.max_capacity = max_capacity
        # The minimum number of RCUs for automatic scaling. Valid values:
        # 
        # - MySQL: **0.5** to **32**
        # - SQL Server: **2** to **16** (integers only)
        # - PostgreSQL: **0.5** to **14**
        # 
        # > The value of this parameter must be less than or equal to the value of **MaxCapacity**.
        self.min_capacity = min_capacity
        # Specifies whether to enable forced elastic scaling for the Serverless instance. Valid values:
        # * **true**: enables forced elastic scaling.
        # * **false**: disables forced elastic scaling. This is the default value.
        # 
        # > * This parameter is required only for MySQL and PostgreSQL Serverless instances. If you enable this parameter, the instance will be unavailable for 30 to 120 seconds during forced scaling. Use this parameter with caution based on your business requirements.
        # > * Elastic scaling of RCUs usually takes effect immediately. However, in some special cases (such as during the execution of a large transaction), scaling cannot be completed immediately. In this case, you can enable this parameter to force scaling.
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

