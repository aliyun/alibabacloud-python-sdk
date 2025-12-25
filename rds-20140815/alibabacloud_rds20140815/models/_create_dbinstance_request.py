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
        # The number of ApsaraDB RDS for MySQL instances that you want to create. The parameter takes effect only when you create multiple ApsaraDB RDS for MySQL instances at a time by using a single request.
        # 
        # Valid values: **1** to **20**. Default value: **1**.
        # 
        # > *   If you want to create multiple ApsaraDB RDS for MySQL instances at a time by using a single request, you can add tags to all the instances by using the **Tag.Key** parameter and the **Tag.Value** parameter. After the instances are created, you can manage the instances based on the tags.
        # > *   After you submit a request to create multiple ApsaraDB RDS for MySQL instances, this operation returns **TaskId**, **RequestId**, and **Message**. You can call the DescribeDBInstanceAttribute operation to query the information about an instance.
        # > *   If the value of the **Engine** parameter is not **MySQL** and the value of the Amount parameter is greater than **1**, this operation fails and returns an error code `InvalidParam.Engine`.
        self.amount = amount
        # Specifies whether to automatically create a proxy. Valid values:
        # 
        # *   **true**: automatically creates a database proxy. By default, a general-purpose database proxy is created.
        # *   **false**: does not automatically create a database proxy.
        self.auto_create_proxy = auto_create_proxy
        # Specifies whether to enable automatic payment. Valid values:
        # 
        # *   **true**: enables the feature. Make sure that your account balance is sufficient when you enable automatic payment.
        # *   **false**: does not automatically complete the payment. An unpaid order is generated.
        # 
        # >  Default value: true. If your account balance is insufficient, you can set AutoPay to false to generate an unpaid order. Then, you can log on to the ApsaraDB RDS console to complete the payment.
        self.auto_pay = auto_pay
        # Specifies whether to enable auto-renewal for the instance. You must specify this parameter only if the instance uses the subscription billing method. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # > *   The auto-renewal cycle is one month for a monthly subscription.
        # > *   The auto-renewal cycle is one year for a yearly subscription.
        self.auto_renew = auto_renew
        # Specifies whether to use a coupon. Default value: false. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # >  If you downgrade the specifications of an instance after you use coupons, the used coupons cannot be refunded.
        self.auto_use_coupon = auto_use_coupon
        # The configuration of the Babelfish feature for the instance that runs PostgreSQL.
        # 
        # Format:{"babelfishEnabled":"true","migrationMode":"xxxxxxx","masterUsername":"xxxxxxx","masterUserPassword":"xxxxxxxx"}
        # 
        # The following list describes the fields in the format:
        # 
        # *   **babelfishEnabled**: specifies whether to enable Babelfish for the instance. If you set this field to **true**, you enable Babelfish for the instance. If you leave this parameter empty, Babelfish is disabled for the instance.
        # *   **migrationMode**: The migration mode of the instance. Valid values: **single-db** and **multi-db**.
        # *   **masterUsername**: The username of the administrator account. The username can contain lowercase letters, digits, and underscores (_). It must start with a letter and end with a letter or digit. It can be up to 63 characters in length and cannot start with pg.
        # *   **masterUserPassword**: The password of the administrator account. The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. It must be 8 to 32 characters in length. The password can contain any of the following characters: `! @ # $ % ^ & * ( ) _ + - =`.
        # 
        # > This parameter applies only to ApsaraDB RDS for PostgreSQL instances. For more information about Babelfish for ApsaraDB RDS for PostgreSQL, see [Introduction to Babelfish](https://help.aliyun.com/document_detail/428613.html).
        self.babelfish_config = babelfish_config
        # A deprecated parameter. You do not need to specify this parameter.
        self.bpe_enabled = bpe_enabled
        # Specifies whether to enable the I/O burst feature of Premium ESSDs. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # >  For more information about the I/O burst feature of general ESSDs, see [What are Premium ESSDs?](https://help.aliyun.com/document_detail/2340501.html)
        self.bursting_enabled = bursting_enabled
        # The additional business information about the instance.
        self.business_info = business_info
        # The RDS edition of the instance. Valid values:
        # 
        # *   Regular RDS instance
        # 
        #     *   **Basic**: RDS Basic Edition
        #     *   **HighAvailability**: RDS High-availability Edition
        #     *   **cluster**: RDS Cluster Edition for ApsaraDB RDS for MySQL or PostgreSQL
        #     *   **AlwaysOn**: RDS Cluster Edition for ApsaraDB RDS for SQL Server
        #     *   **Finance**: RDS Basic Edition for serverless instances
        # 
        # *   Serverless RDS instance
        # 
        #     *   **serverless_basic**: RDS Basic Edition for serverless instances. This edition is available only for instances that run MySQL and PostgreSQL.
        #     *   **serverless_standard**: RDS High-availability Edition for serverless instances. This edition is available only for instances that run MySQL and PostgreSQL.
        #     *   **serverless_ha**: RDS High-availability Edition for serverless instances. This edition is available only for instances that run SQL Server.
        # 
        # > This parameter is required if PayType is set to Serverless.
        self.category = category
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # Specifies whether to enable the data archiving feature of Premium ESSDs. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # >  For more information about the data archiving feature of Premium ESSDs, see [Use the data archiving feature](https://help.aliyun.com/document_detail/2701832.html).
        self.cold_data_enabled = cold_data_enabled
        # The connection mode of the instance. Valid values:
        # 
        # *   **Standard**: standard mode
        # *   **Safe**: database proxy mode
        # 
        # ApsaraDB RDS automatically assigns a connection mode to the instance.
        # 
        # > SQL Server 2012, SQL Server 2016, and SQL Server 2017 support only the standard mode.
        self.connection_mode = connection_mode
        # The internal endpoint that is used to connect to the instance.
        self.connection_string = connection_string
        # The policy based on which multiple instances are created. The parameter takes effect only when the value of the **Amount** parameter is greater than 1. Valid values:
        # 
        # *   **Atomicity** (default): atomicity. The instances are all created together. If one instance cannot be created, none of the instances are created.
        # *   **Partial**: non-atomicity. Each instance is independently created. The failure in creating an instance does not affect the creation of the other instances.
        self.create_strategy = create_strategy
        self.custom_extra_info = custom_extra_info
        # The instance type of the instance. You can specify an instance type of the standard or YiTian product type. For more information, see [Primary ApsaraDB RDS instance types](https://help.aliyun.com/document_detail/26312.html).
        # 
        # To create a serverless instance, set this parameter to one of the following values:
        # 
        # *   If you want to create a serverless instance that runs MySQL on RDS Basic Edition, set this parameter to **mysql.n2.serverless.1c**.
        # *   If you want to create a serverless instance that runs MySQL on RDS High-availability Edition, set this parameter to **mysql.n2.serverless.2c**.
        # *   If you want to create a serverless instance that runs SQL Server, set this parameter to **mssql.mem2.serverless.s2**.
        # *   If you want to create a serverless instance that runs PostgreSQL on RDS Basic Edition, set this parameter to **pg.n2.serverless.1c**.
        # *   If you want to create a serverless instance that runs PostgreSQL on RDS High-availability Edition, set this parameter to **pg.n2.serverless.2c**.
        # 
        # This parameter is required.
        self.dbinstance_class = dbinstance_class
        # The instance name. The value must be 2 to 255 characters in length The name can contain letters, digits, and hyphens (-) and must start with a letter.
        # 
        # >  The value cannot start with http:// or https://.
        self.dbinstance_description = dbinstance_description
        # The network connection type of the instance. The value of this parameter is fixed as **Intranet**, indicating an internal network connection.
        # 
        # This parameter is required.
        self.dbinstance_net_type = dbinstance_net_type
        # The storage capacity of the instance. Unit: GB. The storage capacity increases in increments of 5 GB. For more information, see [Primary ApsaraDB RDS instance types](https://help.aliyun.com/document_detail/26312.html).
        # 
        # This parameter is required.
        self.dbinstance_storage = dbinstance_storage
        # The storage type of the instance. Valid values:
        # 
        # *   **local_ssd**: Premium Local SSD (recommended)
        # *   **general_essd**: Premium Enterprise SSD (ESSD) (recommend)
        # *   **cloud_essd**: PL1 ESSD
        # *   **cloud_essd2**: PL2 ESSD
        # *   **cloud_essd3**: PL3 ESSD
        # *   **cloud_ssd**: standard SSD. This storage type is not recommended. Standard SSDs are no longer available for purchase in some Alibaba Cloud regions.
        # 
        # The default value of this parameter is determined by the instance type specified by the **DBInstanceClass** parameter.
        # 
        # *   If the instance type specifies the Premium Local SSD storage type, the default value of this parameter is **local_ssd**.
        # *   If the instance type specifies the cloud disk storage type, the default value of this parameter is **cloud_essd**.
        # 
        # >  Serverless instances support only PL1 ESSDs and Premium ESSDs.
        self.dbinstance_storage_type = dbinstance_storage_type
        # Specifies whether the table name is case-sensitive. Valid values:
        # 
        # *   **true**: Table names are not case-sensitive. This is the default value.
        # *   **false**: Table names are case-sensitive.
        self.dbis_ignore_case = dbis_ignore_case
        # The parameter template ID. You can call the DescribeParameterGroups operation to query the parameter template ID.
        # 
        # >  This parameter is available if you want to create an instance that runs MySQL or PostgreSQL. If you do not configure this parameter, the default parameter template is used. If you want to use a custom parameter template, you can customize a parameter template and set this parameter to the ID of the custom template.
        self.dbparam_group_id = dbparam_group_id
        # The time zone of the instance. This parameter takes effect only when you set **Engine** to **MySQL** or **PostgreSQL**.
        # 
        # *   **Engine** is set to **MySQL**:
        # 
        #     *   This time zone is in UTC. Valid values: \\*\\*-12:59\\*\\* to **+13:00**.
        #     *   If the instance uses Premium Local SSDs, you can specify the name of the time zone. For example, you can specify the Asia/Hong_Kong time zone. For more information, see [Time zones](https://help.aliyun.com/document_detail/297356.html).
        # 
        # *   **Engine** is set to **PostgreSQL**.
        # 
        #     *   This time zone is not in UTC. For more information, see [Time zones](https://help.aliyun.com/document_detail/297356.html).
        #     *   You can configure this parameter only when the RDS instance uses cloud disks.
        # 
        # > *   You can specify the time zone when you create a primary instance. You cannot specify the time zone when you create a read-only instance. Read-only instances inherit the time zone of their primary instance.
        # > *   If you do not specify this parameter, the system automatically assigns the default time zone of the region in which the instance resides.
        self.dbtime_zone = dbtime_zone
        # The ID of the dedicated cluster to which the instance belongs.
        # 
        # If you create the instance in a dedicated cluster, you must specify this parameter.
        # 
        # *   You can call the DescribeDedicatedHostGroups operation to query the information about the dedicated cluster.
        # *   If no dedicated clusters are created, you can call the CreateDedicatedHostGroup operation to create a dedicated cluster.
        self.dedicated_host_group_id = dedicated_host_group_id
        # Specifies whether to enable the release protection feature for the instance. This feature is available only for pay-as-you-go instances. Valid values:
        # 
        # *   **true**: enables the feature.
        # *   **false** (default): disables the feature.
        self.deletion_protection = deletion_protection
        # Specifies whether to perform a dry run. Default value: false. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, service limits, and insufficient inventory errors.
        # *   **false** (default): performs a dry run and sends the request. If the request passes the dry run, the instance is created.
        self.dry_run = dry_run
        # The ID of the key that is used for cloud disk encryption in the region in which the instance is deployed. If this parameter is specified, cloud disk encryption is enabled and you must also specify the **RoleARN** parameter. Cloud disk encryption cannot be disabled after it is enabled.
        # 
        # You can obtain the ID of the key in the Key Management Service (KMS) console or create a key. For more information, see [Create a key](https://help.aliyun.com/document_detail/181610.html).
        # 
        # > *   This parameter is not required when you create an instance that runs MySQL, PostgreSQL, or SQL Server. You need to only specify the **RoleARN** parameter to create an instance that has cloud disk encryption enabled by using the obtained key ID.
        # > *   You can configure RAM authorization to require a RAM user to enable cloud disk encryption when the RAM user is used to create an instance. If cloud disk encryption is disabled during the instance creation, the creation operation fails. To complete the configuration, you can attach the following policy to the RAM user: `{"Version":"1","Statement":[{"Effect":"Deny","Action":"rds:CreateDBInstance","Resource":"*","Condition":{"StringEquals":{"rds:DiskEncryptionRequired":"false"}}}]}`
        # 
        # 
        # >Warning: The configuration also affects the CreateOrder operation that is called to create instances in the console.
        self.encryption_key = encryption_key
        # The database engine of the instance. Valid values:
        # 
        # *   **MySQL**
        # *   **SQLServer**
        # *   **PostgreSQL**
        # *   **MariaDB**
        # 
        # This parameter is required.
        self.engine = engine
        # The database engine version of the instance.
        # 
        # *   Regular RDS instance
        # 
        #     *   Valid values when you set Engine to MySQL: **5.5**, **5.6**, **5.7**, and **8.0**
        #     *   Valid values when you set Engine to SQLServer: **08r2_ent_ha**(cloud disks, discontinued), **2008r2**(premium local disks, discontinued), **2012**(SQL Server EE Basic), **2012_ent_ha**, **2012_std_ha**, **2012_web**, **2014_ent_ha**, **2014_std_ha**, **2016_ent_ha**, **2016_std_ha**, **2016_web**, **2017_ent**, **2017_std_ha**, **2017_web**, **2019_ent**, **2019_std_ha**, **2019_web**, **2022_ent**, **2022_std_ha**, and **2022_web**
        #     *   Valid values when you set Engine to PostgreSQL: **10.0**, **11.0**, **12.0**, **13.0**, **14.0**, **15.0**, **16.0**, and **17.0**
        #     *   Valid values when you set Engine to MariaDB: **10.3** and **10.6**
        # 
        # *   Serverless RDS instance
        # 
        #     *   Valid values when you set Engine to MySQL: **5.7** and **8.0**
        #     *   Valid values when you set Engine to SQLServer: **2016_std_sl**, **2017_std_sl**, and **2019_std_sl**
        #     *   Valid values when you set Engine to PostgreSQL: **14.0**, **15.0**, **16.0**, and **17.0**
        # 
        # > 
        # 
        # *   ApsaraDB RDS for MariaDB does not support serverless instances.
        # 
        # *   RDS instances that run SQL Server: `_ent` specifies SQL Server EE (Always On), `_ent_ha` specifies SQL Server EE, `_std_ha` specifies SQL Server SE, and `_web` specifies SQL Server Web.
        # 
        # *   RDS instances that run SQL Server 2014 are not available for purchase on the international site (alibabacloud.com).
        # 
        # *   Babelfish is supported only for RDS instances that run PostgreSQL 15.
        # 
        # This parameter is required.
        self.engine_version = engine_version
        self.external_replication = external_replication
        # The network type of the instance. Valid values:
        # 
        # *   **VPC**: virtual private cloud (VPC)
        # *   **Classic**: classic network
        # 
        # > 
        # 
        # *   If the instance runs MySQL and uses cloud disks, you must set this parameter to **VPC**.
        # 
        # *   If the instance runs PostgreSQL or MariaDB, you must set this parameter to **VPC**.
        # 
        # *   If the instance runs SQL Server Basic or SQL Server Web, you can set this parameter to VPC or Classic. If the instance runs other database engines, you must set this parameter to **VPC**.
        self.instance_network_type = instance_network_type
        # Specifies whether to enable Buffer Pool Extension (BPE) of Premium ESSDs. Valid values:
        # 
        # *   **1**: enables BPE.
        # *   **0**: disables BPE.
        # 
        # >  For more information about Buffer Pool Extension(BPE) of Premium ESSDs, see [Buffer Pool Extension(BPE)](https://help.aliyun.com/document_detail/2527067.html).
        self.io_acceleration_enabled = io_acceleration_enabled
        # Specifies whether to enable the 16K atomic write feature. Valid values:
        # 
        # *   **optimized**: enables the 16K atomic write feature.
        # *   **none** (default): does not enable the 16K atomic write feature.
        # 
        # >  For more information, see [Use the 16K atomic write feature](https://help.aliyun.com/document_detail/2858761.html).
        self.optimized_writes = optimized_writes
        # The billing method of the instance. Valid values:
        # 
        # *   **Postpaid**: pay-as-you-go.
        # *   **Prepaid**: subscription.
        # *   **Serverless**: serverless. This value is not supported for instances that run MariaDB. For more information, see [Overview of serverless ApsaraDB RDS for MySQL instances](https://help.aliyun.com/document_detail/411291.html), [Overview of serverless ApsaraDB RDS for SQL Server instances](https://help.aliyun.com/document_detail/604344.html), and [Overview of serverless ApsaraDB RDS for PostgreSQL instances](https://help.aliyun.com/document_detail/607742.html).
        # 
        # > The system automatically generates a purchase order and completes the payment.
        # 
        # This parameter is required.
        self.pay_type = pay_type
        # The unit of the subscription duration. Valid values:
        # 
        # *   **Year**
        # *   **Month**
        # 
        # >  If you set the PayType parameter to **Prepaid**, you must specify this parameter.
        self.period = period
        # The port. You can initialize the port when you create the instance.
        # 
        # *   Valid values if the instance runs MySQL: 1000 to 65534
        # *   Valid values if the instance runs PostgreSQL, SQL Server, or MariaDB: 1000 to 5999
        self.port = port
        # The private IP address of the instance. The private IP address must be within the CIDR block that is supported by the specified vSwitch. ApsaraDB RDS automatically assigns a private IP address to the instance based on the values of the **VPCId** and **vSwitchId** parameters.
        self.private_ip_address = private_ip_address
        # The coupon code.
        self.promotion_code = promotion_code
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/610399.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        self.resource_owner_id = resource_owner_id
        # The Alibaba Cloud Resource Name (ARN) that is provided by your Alibaba Cloud account for Resource Access Management (RAM) users. RAM users can use the ARN to connect to ApsaraDB RDS to Key Management Service (KMS). You can call the CheckCloudResourceAuthorized operation to query the ARN.
        # 
        # >  When you enable the encryption, you must specify the RoleARN.
        self.role_arn = role_arn
        # The IP address whitelist of the instance. For more information, see [Configure an IP address whitelist](https://help.aliyun.com/document_detail/43185.html). Separate multiple IP addresses or CIDR blocks with commas (,). You can add up to 1,000 IP addresses or CIDR blocks to the whitelist. The entries in the IP address whitelist must be in one of the following formats:
        # 
        # *   IP addresses, such as 10.10.XX.XX.
        # *   CIDR blocks, such as 10.10.XX.XX/24. In this example, 24 indicates that the prefix of each IP address in the IP address whitelist is 24 bits in length. You can replace 24 with a value within the range of 1 to 32.
        # 
        # This parameter is required.
        self.security_iplist = security_iplist
        # The settings of the serverless instance. These parameters are required only when you create a serverless instance.
        # 
        # >  ApsaraDB RDS for MariaDB does not support serverless instances.
        self.serverless_config = serverless_config
        # Specifies whether to enable the automatic storage expansion feature for the instance. This feature is supported if the instance runs MySQL or PostgreSQL. Valid values:
        # 
        # *   **Enable**: enables the feature.
        # *   **Disable** (default): disables the feature.
        # 
        # >  After the instance is created, you can call the ModifyDasInstanceConfig operation to adjust the settings. For more information, see [Configure automatic storage expansion](https://help.aliyun.com/document_detail/173826.html).
        self.storage_auto_scale = storage_auto_scale
        # The threshold in percentage based on which automatic storage expansion is triggered.
        # 
        # *   **10**
        # *   **20**
        # *   **30**
        # *   **40**
        # *   **50**
        # 
        # >  If you set the **StorageAutoScale** parameter to **Enable**, you must specify this parameter.
        self.storage_threshold = storage_threshold
        # The maximum storage capacity that is allowed for automatic storage expansion. The storage capacity of the instance cannot exceed the maximum storage capacity. Unit: GB.
        # 
        # > *   Valid values: an integer greater than or equal to 0.
        # > *   If you set **StorageAutoScale** to **Enable**, you must specify this parameter.
        self.storage_upper_bound = storage_upper_bound
        # A deprecated parameter. You do not need to specify this parameter.
        self.system_dbcharset = system_dbcharset
        # The tags that are added to instances.
        self.tag = tag
        # The ID of the host to which the logger instance belongs in the specified dedicated cluster.
        # 
        # If you want to create an instance that runs RDS Enterprise Edition in a dedicated cluster, you must specify this parameter. If you do not specify this parameter, the system automatically assigns a host.
        # 
        # *   You can call the DescribeDedicatedHosts operation to query the host in the dedicated cluster.
        # *   If no hosts are created, you can call the CreateDedicatedHost operation to create a host.
        self.target_dedicated_host_id_for_log = target_dedicated_host_id_for_log
        # The ID of the host to which the instance belongs in the specified dedicated cluster.
        # 
        # If you create the instance in a dedicated cluster, you must specify this parameter. If you do not specify this parameter, the system automatically assigns a host.
        # 
        # *   You can call the DescribeDedicatedHosts operation to query the host in the dedicated cluster.
        # *   If no hosts are created, you can call the CreateDedicatedHost operation to create a host.
        self.target_dedicated_host_id_for_master = target_dedicated_host_id_for_master
        # The ID of the host to which the secondary instance belongs in the specified dedicated cluster.
        # 
        # If you want to create an instance that runs RDS High-availability Edition or RDS Enterprise Edition in a dedicated cluster, you must specify this parameter. If you do not specify this parameter, the system automatically assigns a host.
        # 
        # *   You can call the DescribeDedicatedHosts operation to query the host in the dedicated cluster.
        # *   If no hosts are created, you can call the CreateDedicatedHost operation to create a host.
        self.target_dedicated_host_id_for_slave = target_dedicated_host_id_for_slave
        # The minor engine version of the instance. This parameter is required only when you create an instance that runs MySQL or PostgreSQL. The value format varies based on the database engine of the instance.
        # 
        # *   If you create an instance that runs MySQL, the value is in the following format: `<RDS edition>_<Minor engine version>`. Examples: `rds_20200229`, `xcluster_20200229`, and `xcluster80_20200229`.
        # 
        #     *   rds: The instance runs RDS Basic Edition or RDS High-availability Edition.
        #     *   xcluster: The instance runs MySQL 5.7 on RDS Enterprise Edition.
        #     *   xcluster80: The instance runs MySQL 8.0 on RDS Enterprise Edition.
        # 
        #     > You can call the DescribeDBMiniEngineVersions operation to query the minor engine version. For more information about the differences between minor engine versions of AliSQL, see [Release notes](https://help.aliyun.com/document_detail/96060.html).
        # 
        # *   If you create an instance that runs PostgreSQL, the value is in the following format: `rds_postgres_<Major engine version>00_<Minor engine version>`. Example: `rds_postgres_1400_20220830`.
        # 
        #     *   1400: The major engine version is PostgreSQL 14.
        #     *   20220830: the AliPG version. You can call the DescribeDBMiniEngineVersions operation to query the AliPG version. For more information about minor engine versions, see [Release notes for AliPG](https://help.aliyun.com/document_detail/126002.html).
        # 
        #     > If you configure the **BabelfishConfig** parameter for your instance that runs PostgreSQL and set the babelfishEnabled field to true, the value of this parameter is in the following format: `rds_postgres_Major engine version00_AliPG version_babelfish`.
        self.target_minor_version = target_minor_version
        # The subscription duration of the instance. Valid values:
        # 
        # *   If you set the **Period** parameter to **Year**, the value of the **UsedTime** parameter ranges from **1 to 5**.
        # *   If you set the **Period** parameter to **Month**, the value of the **UsedTime** parameter ranges from **1 to 11**.
        # 
        # >  If you set the PayType parameter to **Prepaid**, you must also specify this parameter.
        self.used_time = used_time
        # The ID of the full backup file. You can call the ListUserBackupFiles operation to query the ID of the full backup file. If you want to create an instance by using the data of a backup file, you must specify this parameter.
        # 
        # This parameter is supported only when the following requirements are met:
        # 
        # *   The **PayType** parameter is set to **Postpaid**.
        # *   The **Engine** parameter is set to **MySQL**.
        # *   The **EngineVersion** parameter is set to **5.7**.
        # *   The **Category** parameter is set to **Basic**.
        self.user_backup_id = user_backup_id
        # The ID of the VPC to which the instance belongs.
        # 
        # > This parameter is available when you set the **InstanceNetworkType** parameter to **VPC**.
        self.vpcid = vpcid
        # The vSwitch ID.
        # 
        # *   **Relations with zones**: Specify the vSwitch ID based on the zones in which the vSwitch belongs to. If you specify two vSwitch IDs, make sure that the vSwitch IDs match the zone IDs specified by the ZoneId and ZoneIdSlave1 parameters.
        # *   **Limits on the network type**: Set **InstanceNetworkType** to **VPC**.
        # *   **Limits on multiple vSwitch IDs**: If you set **ZoneSlaveId1** to a value that is not **Auto**, you must specify the IDs of two vSwitches for this parameter and separate the IDs with a comma (,).
        # *   **Limits on characters**: The value cannot contain `spaces` or the following characters: `!` `#` `￥` `&` `%`
        self.v_switch_id = v_switch_id
        # The entries in the whitelist. If you enter multiple IP addresses or CIDR blocks, you must separate the IP addresses or CIDR blocks with commas (,). Do not add spaces preceding or following the commas. Example: `192.168.0.1,172.16.213.9`.
        self.whitelist_template_list = whitelist_template_list
        # The zone ID of the primary instance.
        # 
        # *   If you specify a virtual private cloud (VPC) and a vSwitch, you must specify the ID of the zone to which the specified vSwitch belongs. Otherwise, the instance cannot be created.
        # *   If the instance runs RDS High-availability Edition, you must specify the **ZoneIdSlave1** parameter. The ZoneIdSlave1 parameter specifies whether to use the single-zone deployment method or the multi-zone deployment method.
        # *   If the instance runs RDS Enterprise Edition, you must specify the **ZoneIdSlave1** and **ZoneIdSlave2** parameters. The ZoneIdSlave1 and ZoneIdSlave2 parameters specify whether to use the single-zone deployment method or the multi-zone deployment method.
        # *   If the instance runs MySQL on RDS Cluster Edition, you must specify the **ZoneIdSlave1** parameter for the RDS cluster that has two nodes and the **ZoneIdSlave1** and **ZoneIdSlave2** parameters for the RDS cluster that has three nodes.
        self.zone_id = zone_id
        # The zone ID of the secondary instance.
        # 
        # *   If you set this parameter to **Auto**, the multi-zone deployment method is used and the zone of the secondary instance is automatically configured.
        # *   If you set this parameter to the same value as the **ZoneId** parameter, the single-zone deployment method is used.
        # *   If you set this parameter to a value that is different from the value of the **ZoneId** parameter, the multiple-zone deployment method is used.
        self.zone_id_slave_1 = zone_id_slave_1
        # The zone ID of the other secondary node. When you create an ApsaraDB RDS for MySQL cluster, you can create one to two secondary nodes for the cluster. This parameter applies if you create a cluster that contains two secondary nodes.
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
        # The tag key. You can use this parameter to add tags to the instance.
        # 
        # *   If the specified tag key is an existing key, the system directly adds the tag key to the instance. You can call the ListTagResources to query the existing tag.
        # *   If the specified tag key does not exist, the system creates the tag key and adds the tag key to the instance.
        # *   The value cannot be an empty string.
        # *   This parameter must be used together with the **Tag.Value** parameter.
        self.key = key
        # The tag value. You can use this parameter to add tags to the instance.
        # 
        # *   If the specified tag value is found in the specified tag key, the system directly adds the tag value to the instance. You can call the ListTagResources to query the existing tag.
        # *   If the specified tag value is not found in the specified tag key, the system creates the tag value and adds the tag value to the instance.
        # *   This parameter must be used together with the **Tag.Key** parameter.
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
        # Specifies whether to enable the automatic startup and stop feature for the serverless instance. Valid values:
        # 
        # *   **true**: enables the feature.
        # *   **false** (default): disables the feature.
        # 
        # >  This parameter is required only for serverless instances that run MySQL and PostgreSQL. After the automatic start and stop feature is enabled, if no connections to the instance are established within 10 minutes, the instance is suspended. After a connection to the instance is established, the instance is resumed.
        self.auto_pause = auto_pause
        # The maximum number of RDS Capacity Units (RCUs). Valid values:
        # 
        # *   Serverless ApsaraDB RDS for MySQL instances: **1 to 32**
        # *   Serverless ApsaraDB RDS for SQL Server instances: **2 to 16**
        # *   Serverless ApsaraDB RDS for PostgreSQL instances: **1 to 14**
        # 
        # >  The value of this parameter must be greater than or equal to the value of the **MinCapacity** parameter and can be set only to an **integer**.
        self.max_capacity = max_capacity
        # The minimum number of RCUs. Valid values:
        # 
        # *   Serverless ApsaraDB RDS for MySQL instances: **0.5 to 32**.
        # *   Serverless ApsaraDB RDS for SQL Server instances: **2 to 16**. Only integers are supported.
        # *   Serverless ApsaraDB RDS for PostgreSQL instances: **0.5 to 14**
        # 
        # >  The value of this parameter must be less than or equal to the value of the **MaxCapacity** parameter.
        self.min_capacity = min_capacity
        # Specifies whether to enable the forced scaling feature for the serverless instance. Valid values:
        # 
        # *   **true**: enables the feature.
        # *   **false** (default): disables the feature.
        # 
        # > 
        # 
        # *   This parameter is required only for serverless instances that run MySQL and PostgreSQL. If you set this parameter to true, a service interruption that lasts approximately 30 to 120 seconds occurs during forced scaling. Process with caution.
        # 
        # *   The RCU scaling for a serverless instance immediately takes effect. In some cases, such as the execution of large transactions, the scaling does not immediately take effect. In this case, you can enable this feature to forcefully scale the RCUs of the instance.
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

