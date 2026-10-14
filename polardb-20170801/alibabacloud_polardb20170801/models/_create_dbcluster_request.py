# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class CreateDBClusterRequest(DaraModel):
    def __init__(
        self,
        agentic_db_cluster_description: str = None,
        agentic_db_cluster_id: str = None,
        agentic_db_type: str = None,
        allow_shut_down: str = None,
        architecture: str = None,
        auto_renew: bool = None,
        auto_use_coupon: bool = None,
        backup_retention_policy_on_cluster_deletion: str = None,
        bursting_enabled: str = None,
        client_token: str = None,
        clone_data_point: str = None,
        cloud_provider: str = None,
        cluster_network_type: str = None,
        creation_category: str = None,
        creation_option: str = None,
        dbcluster_description: str = None,
        dbminor_version: str = None,
        dbnode_class: str = None,
        dbnode_num: int = None,
        dbtype: str = None,
        dbversion: str = None,
        default_time_zone: str = None,
        ens_region_id: str = None,
        gdnid: str = None,
        hot_standby_cluster: str = None,
        loose_polar_log_bin: str = None,
        loose_xengine: str = None,
        loose_xengine_use_memory_pct: str = None,
        lower_case_table_names: str = None,
        owner_account: str = None,
        owner_id: int = None,
        parameter_group_id: str = None,
        pay_type: str = None,
        period: str = None,
        promotion_code: str = None,
        provisioned_iops: int = None,
        proxy_class: str = None,
        proxy_type: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scale_max: str = None,
        scale_min: str = None,
        scale_ro_num_max: str = None,
        scale_ro_num_min: str = None,
        security_iplist: str = None,
        serverless_type: str = None,
        source_resource_id: str = None,
        source_uid: int = None,
        standby_az: str = None,
        storage_auto_scale: str = None,
        storage_encryption: bool = None,
        storage_encryption_key: str = None,
        storage_pay_type: str = None,
        storage_space: int = None,
        storage_type: str = None,
        storage_upper_bound: int = None,
        strict_consistency: str = None,
        tdestatus: bool = None,
        tag: List[main_models.CreateDBClusterRequestTag] = None,
        target_minor_version: str = None,
        used_time: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        # The Agentic cluster description.
        self.agentic_db_cluster_description = agentic_db_cluster_description
        # The Agentic cluster ID.
        self.agentic_db_cluster_id = agentic_db_cluster_id
        # The Agentic database engine type. Valid values:
        # 
        # * dedicated
        self.agentic_db_type = agentic_db_type
        # Specifies whether to enable No-activity Suspension. Valid values:
        # 
        # - **true**: enables No-activity Suspension.
        # 
        # - **false**: disables No-activity Suspension (default).
        # > Only serverless clusters support this parameter.
        self.allow_shut_down = allow_shut_down
        # The CPU architecture. Valid values:
        # - X86
        # - ARM
        self.architecture = architecture
        # Specifies whether to enable auto-renewal. Valid values:
        # 
        # - **true**: enables auto-renewal.
        # - **false**: disables auto-renewal.
        # 
        # Default value: **false**.
        # 
        # > This parameter takes effect only when **PayType** is set to **Prepaid**.
        self.auto_renew = auto_renew
        # Specifies whether to automatically use coupons. Valid values:
        # * true (default): Uses coupons.
        # * false: Does not use coupons.
        self.auto_use_coupon = auto_use_coupon
        # The data retention policy applied when the cluster is deleted. Valid values:
        # * **ALL**: long-term retention (LTR) of all backups.
        # * **LATEST**: long-term retention (LTR) of the last backup (an automatic backup is performed before deletion).
        # * **NONE**: does not retain backups upon cluster deletion.
        # 
        # When a cluster is created, the default value is **NONE**, which means backups are not retained upon cluster deletion.
        # >* This parameter takes effect only when **DBType** is set to **MySQL**.
        # >* Serverless clusters do not support this parameter.
        self.backup_retention_policy_on_cluster_deletion = backup_retention_policy_on_cluster_deletion
        # Specifies whether to enable I/O performance burst for ESSD AutoPL cloud disks. Valid values:
        # 
        # - **true**: enables I/O performance burst.
        # - **false**: does not enable I/O performance burst (default).
        # 
        # > This parameter is supported only when StorageType is set to ESSDAUTOPL.
        self.bursting_enabled = bursting_enabled
        # The client token that is used to ensure the idempotence of the request. The token is generated by the client and must be unique among different requests. The token is case-sensitive and cannot exceed 64 ASCII characters in length.
        self.client_token = client_token
        # The point in time at which data is cloned. Valid values: 
        # 
        # -  **LATEST**: the latest point in time.
        # - **BackupID**: a historical backup set ID. Set this parameter to the specific backup set ID.
        # - **Timestamp**: a historical point in time. Specify the time in the `YYYY-MM-DDThh:mm:ssZ` format (UTC).
        # 
        #  Default value: **LATEST**.
        # 
        # > If **CreationOption** is set to **CloneFromRDS**, this parameter can only be set to **LATEST**.
        self.clone_data_point = clone_data_point
        # The cloud service provider to which the instance belongs.
        self.cloud_provider = cloud_provider
        # The network type of the cluster. Only virtual private clouds (VPCs) are supported. Set the value to **VPC**.
        self.cluster_network_type = cluster_network_type
        # The edition of the cluster. Valid values:
        # * **Normal**: Cluster Edition (default).
        # * **Basic**: Single Node Edition.
        # * **ArchiveNormal**: PolarDB X-Engine Edition.
        # * **NormalMultimaster**: Multi-master Cluster Edition.
        # * **SENormal**: Standard Edition.
        # 
        # > * **MySQL** **5.6**, **5.7**, **8.0**, **PostgreSQL** **14**, and **Oracle syntax-compatible 2.0** support **Basic**.
        # > * **MySQL** **8.0** supports **ArchiveNormal** and **NormalMultimaster**.
        # > * **MySQL** **5.6**, **5.7**, **8.0**, and **PostgreSQL** **14** support **SENormal**.
        # 
        # For more information about editions, see [Product editions](https://help.aliyun.com/document_detail/183258.html).
        self.creation_category = creation_category
        # The method used to create the cluster. Valid values: 
        # 
        # * **Normal**: creates a new PolarDB cluster. For more information about console operations, see the following topics:
        # 
        #     * [Create a PolarDB for MySQL database cluster](https://help.aliyun.com/document_detail/58769.html)
        #     * [Create a PolarDB for PostgreSQL database cluster](https://help.aliyun.com/document_detail/118063.html)
        #     * [Create a PolarDB for PostgreSQL (Compatible with Oracle) database cluster](https://help.aliyun.com/document_detail/118182.html)
        # 
        # * **CloneFromPolarDB**: clones data from an existing PolarDB cluster to a new PolarDB cluster. For more information about console operations, see the following topics:
        # 
        #     * [Clone a PolarDB for MySQL cluster](https://help.aliyun.com/document_detail/87966.html)
        #     * [Clone a PolarDB for PostgreSQL cluster](https://help.aliyun.com/document_detail/118108.html)
        #     * [Clone a PolarDB for PostgreSQL (Compatible with Oracle) cluster](https://help.aliyun.com/document_detail/118221.html)
        # 
        # * **RecoverFromRecyclebin**: restores data from a released PolarDB cluster to a new PolarDB cluster. For more information about console operations, see the following topics:
        # 
        #     * [Restore a released PolarDB for MySQL cluster](https://help.aliyun.com/document_detail/164880.html)
        #     * [Restore a released PolarDB for PostgreSQL cluster](https://help.aliyun.com/document_detail/432844.html)
        #     * [Restore a released PolarDB for PostgreSQL (Compatible with Oracle) cluster](https://help.aliyun.com/document_detail/424632.html)
        # 
        # * **CloneFromRDS**: clones data from an existing ApsaraDB RDS instance to a new PolarDB cluster. For more information about console operations, see [Clone an ApsaraDB RDS for MySQL instance to a PolarDB for MySQL cluster](https://help.aliyun.com/document_detail/121812.html).
        # 
        # * **MigrationFromRDS**: migrates data from an existing ApsaraDB RDS instance to a new PolarDB cluster. The created PolarDB cluster is in read-only pattern and has Binlog enabled by default. For more information about console operations, see [Upgrade an ApsaraDB RDS for MySQL instance to a PolarDB for MySQL cluster](https://help.aliyun.com/document_detail/121582.html).
        # 
        # * **CreateGdnStandby**: creates a secondary cluster. For more information about console operations, see [Add a secondary cluster](https://help.aliyun.com/document_detail/160381.html).
        # 
        # * **UpgradeFromPolarDB**: performs instance migration and upgrade from PolarDB. For more information about console operations, see [Major engine version upgrade](https://help.aliyun.com/document_detail/459712.html).
        # 
        # Default value: **Normal**.
        # 
        # > When **DBType** is set to **MySQL** and **DBVersion** is set to **8.0**, you can set this parameter to **CreateGdnStandby**.
        self.creation_option = creation_option
        # The name of the cluster. The name must meet the following requirements:
        # * It cannot start with `http://` or `https://`.
        # * It must be 2 to 256 characters in length.
        self.dbcluster_description = dbcluster_description
        # The minor version of the database engine. Valid values:
        # 
        # - **8.0.2**
        # 
        # - **8.0.1**
        # 
        # > This parameter takes effect only when **DBType** is set to **MySQL** and **DBVersion** is set to **8.0**.
        self.dbminor_version = dbminor_version
        # The node specification. For more information, see the following topics:
        # 
        # - PolarDB for MySQL: [Compute node specifications](https://help.aliyun.com/document_detail/102542.html).
        # - PolarDB for PostgreSQL (Compatible with Oracle): [Compute node specifications](https://help.aliyun.com/document_detail/207921.html).
        # - PolarDB for PostgreSQL: [Compute node specifications](https://help.aliyun.com/document_detail/209380.html).
        # 
        # >  - To create a serverless cluster for PolarDB for MySQL Cluster Edition, set this parameter to **polar.mysql.sl.small**.
        # > - To create a serverless cluster for PolarDB for MySQL Standard Edition, set this parameter to **polar.mysql.sl.small.c**.
        # > - To create a serverless cluster for PolarDB for PostgreSQL Cluster Edition, set this parameter to **polar.pg.sl.small**.
        # > - To create a serverless cluster for PolarDB for PostgreSQL Standard Edition, set this parameter to **polar.pg.sl.small.c**.
        # > - To create a serverless cluster for PolarDB for PostgreSQL (Compatible with Oracle), set this parameter to **polar.o.sl.small**.
        self.dbnode_class = dbnode_class
        # The number of nodes for Standard Edition and Enterprise Edition. Valid values:
        # - Standard Edition: 1 to 8 (supports 1 read/write node and 7 read-only nodes).
        # - Enterprise Edition: 1 to 16 (supports 1 read/write node and 15 read-only nodes).
        # > - Enterprise Edition has 2 nodes by default, and Standard Edition has 1 node by default.
        # > - Only PolarDB for MySQL supports this parameter.
        # > - Changing the number of nodes for Multi-master Cluster Edition clusters is not supported.
        self.dbnode_num = dbnode_num
        # The type of the database engine. Valid values: 
        # 
        # - **MySQL**
        # - **PostgreSQL**
        # - **Oracle**
        # 
        # This parameter is required.
        self.dbtype = dbtype
        # The database DPI engine version number.
        # * Valid values for MySQL version number: 
        #     * **5.6**
        #     * **5.7**
        #     * **8.0**
        # * Valid values for PostgreSQL version number:
        #     * **11**
        #     * **14**
        #     * **15**
        #     <props="china">
        #       
        #       > To create a serverless cluster for PolarDB for PostgreSQL, only version 14 is supported. 
        #     
        #     
        # * Valid values for Oracle version number:
        #     * **11**
        #     * **14**
        # 
        # This parameter is required.
        self.dbversion = dbversion
        # The default time zone of the cluster (UTC). The value can be any time frame within the range of **-12:00 to +13:00**, such as **00:00**. Default value: **SYSTEM**, which indicates that the default time zone is the same as the time zone of the region.
        # > This parameter takes effect only when **DBType** is set to **MySQL**.
        self.default_time_zone = default_time_zone
        # The ID of the Edge Node Service (ENS) node. This parameter is required when you create an ENS database.
        self.ens_region_id = ens_region_id
        # The ID of the Global Database Network (GDN).
        # 
        # > This parameter is required when **CreationOption** is set to **CreateGdnStandby**.
        self.gdnid = gdnid
        # Specifies whether to enable the hot standby cluster. Valid values:
        # 
        # - **ON** (default): enables the hot standby storage cluster.
        # - **OFF**: disables the hot standby cluster.
        # - **STANDBY**: enables the hot standby cluster.
        # - **EQUAL**: enables both the hot standby storage cluster and the hot standby compute cluster.
        # - **3AZ**: enables multi-zone strong data consistency.
        # > **STANDBY** takes effect only for PolarDB for PostgreSQL.
        self.hot_standby_cluster = hot_standby_cluster
        # Specifies whether to enable the Binlog feature. Valid values:
        # 
        # - **ON**: enables the Binlog feature for the cluster.
        # - **OFF**: disables the Binlog feature for the cluster.
        # > This parameter takes effect only when **DBType** is set to **MySQL**.
        self.loose_polar_log_bin = loose_polar_log_bin
        # Specifies whether to enable the X-Engine storage engine. Valid values:
        # 
        # - **ON**: enables the X-Engine storage engine for the cluster.
        # - **OFF**: disables the X-Engine storage engine for the cluster.
        # > This parameter takes effect only when **CreationOption** is not set to **CreateGdnStandby**, **DBType** is set to **MySQL**, and **DBVersion** is set to **8.0**. The memory specification of the node with X-Engine enabled must be 8 GB or more.
        self.loose_xengine = loose_xengine
        # The percentage of memory allocated to the X-Engine storage engine. Valid values: integers from 10 to 90.
        # > This parameter takes effect only when **LooseXEngine** is set to **ON**.
        self.loose_xengine_use_memory_pct = loose_xengine_use_memory_pct
        # Specifies whether table names are case-sensitive. Valid values:
        # * **1**: Table names are case-insensitive.
        # * **0**: Table names are case-sensitive.
        # 
        # Default value: **1**.
        # > This parameter takes effect only when **DBType** is set to **MySQL**.
        self.lower_case_table_names = lower_case_table_names
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the parameter template.
        # 
        # > You can call the [DescribeParameterGroups](https://help.aliyun.com/document_detail/207178.html) operation to query the list of parameter templates in the target region, including parameter template IDs.
        self.parameter_group_id = parameter_group_id
        # The billing method. Valid values: 
        # 
        # - **Postpaid**: pay-as-you-go.
        # - **Prepaid**: subscription.
        # 
        # This parameter is required.
        self.pay_type = pay_type
        # This is a required parameter to pass when **PayType** is set to **Prepaid**. Specifies the subscription type of the subscription cluster. 
        # 
        # - **Year**: annual subscription.
        # - **Month**: monthly subscription.
        self.period = period
        # The coupon code. If you do not specify this parameter, the default coupon is used.
        self.promotion_code = promotion_code
        # <p id="p_wyg_t4a_glm" props="china" icmsditafragmentmagic=1>The provisioned read/write IOPS for ESSD AutoPL cloud disks. Valid values: 0 to min{50,000, 1000 × capacity - baseline performance}.</p>
        # <p id="p_6de_jxy_k2g" props="china" icmsditafragmentmagic=1>Baseline performance = min{1,800 + 50 × capacity, 50000}.</p>
        # <note id="note_7kj_j0o_rgs" props="china" icmsditafragmentmagic=1>This parameter is supported only when StorageType is set to ESSDAUTOPL.</note>
        self.provisioned_iops = provisioned_iops
        # The specification of the database proxy for Standard Edition. Valid values:
        # 
        # - **polar.maxscale.g2.medium.c**: 2 cores.
        # - **polar.maxscale.g2.large.c**: 4 cores.
        # - **polar.maxscale.g2.xlarge.c**: 8 cores.
        # - **polar.maxscale.g2.2xlarge.c**: 16 cores.
        # - **polar.maxscale.g2.3xlarge.c**: 24 cores.
        # - **polar.maxscale.g2.4xlarge.c**: 32 cores.
        # - **polar.maxscale.g2.8xlarge.c**: 64 cores.
        self.proxy_class = proxy_class
        # The type of the database proxy. Valid values:
        # - **EXCLUSIVE**: Dedicated Enterprise Edition.
        # - **GENERAL**: Standard Enterprise Edition.
        # > The proxy type must match the type that corresponds to the node specifications of the cluster:
        # > - If the node specifications are General-purpose, set the proxy type to Standard Enterprise Edition.
        # > - If the node specifications are Dedicated, set the proxy type to Dedicated Enterprise Edition.
        self.proxy_type = proxy_type
        # The region ID.
        # 
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/98041.html) operation to query available regions.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The maximum scaling limit for a single node. Valid values: 1 PCU to 32 PCU.
        # > Only serverless clusters support this parameter.
        self.scale_max = scale_max
        # The minimum scaling limit for a single node. Valid values: 1 PCU to 31 PCU.
        # 
        # > Only serverless clusters support this parameter.
        self.scale_min = scale_min
        # The maximum number of read-only nodes for scaling. Valid values: 0 to 15.
        # > Only serverless clusters support this parameter.
        self.scale_ro_num_max = scale_ro_num_max
        # The minimum number of read-only nodes for scaling. Valid values: 0 to 15.
        # > Only serverless clusters support this parameter.
        self.scale_ro_num_min = scale_ro_num_min
        # The IP whitelist of the PolarDB cluster.
        # > You can configure multiple IP addresses in the whitelist. Separate multiple IP addresses with commas (,).
        self.security_iplist = security_iplist
        # The serverless type. Set the value to **AgileServerless** (agile).
        # > Only serverless clusters support this parameter.
        self.serverless_type = serverless_type
        # Instance ID of the source ApsaraDB RDS instance or the source PolarDB cluster. This parameter is required only when **CreationOption** is set to **MigrationFromRDS**, **CloneFromRDS**, **CloneFromPolarDB**, or **RecoverFromRecyclebin**.
        # * If **CreationOption** is set to **MigrationFromRDS** or **CloneFromRDS**, set this parameter to instance ID of the source ApsaraDB RDS instance. The source ApsaraDB RDS instance must run ApsaraDB RDS for MySQL 5.6, 5.7, or 8.0 High-availability Edition.
        # 
        # * If **CreationOption** is set to **CloneFromPolarDB**, set this parameter to instance ID of the source PolarDB cluster. The cloned cluster and the source cluster use the same DBType by default. For example, if the source cluster runs MySQL 8.0, set **DBType** to **MySQL** and **DBVersion** to **8.0** for the cloned cluster.
        # * If **CreationOption** is set to **RecoverFromRecyclebin**, set this parameter to instance ID of the released source PolarDB cluster. The restored cluster and the source cluster must use the same DBType. For example, if the source cluster runs MySQL 8.0, set **DBType** to **MySQL** and **DBVersion** to **8.0** for the restored cluster.
        self.source_resource_id = source_resource_id
        # The UID of the account that owns the source backup set in a cross-account backup restoration scenario.
        self.source_uid = source_uid
        # The zone of the hot standby cluster.
        # 
        # > This parameter takes effect only when the hot standby cluster or multi-zone strong data consistency is enabled.
        self.standby_az = standby_az
        # Specifies whether to enable automatic storage scaling for Standard Edition clusters. Valid values:
        # 
        # - Enable: enables automatic storage scaling.
        # - Disable: disables automatic storage scaling.
        self.storage_auto_scale = storage_auto_scale
        # Specifies whether to enable cloud disk encryption. Valid values:
        # 
        # - **true**: Enabled.
        # - **false**: Disabled (default).
        # > This parameter takes effect only when **DBType** is set to **MySQL**.
        # 
        # > This parameter takes effect only when **StorageType** is set to a Standard Edition storage type.
        self.storage_encryption = storage_encryption
        # The ID of a custom encryption key for cloud disk encryption in the same region as the instance. If you specify this parameter, cloud disk encryption is automatically enabled and cannot be disabled. To use the default service key for cloud disk encryption, leave this parameter empty.
        # 
        # You can view the key ID in the Key Management Service (KMS) console or create a new key.
        # 
        # > This parameter takes effect only when **DBType** is set to **MySQL**.
        # 
        # > This parameter takes effect only when **StorageType** is set to a Standard Edition storage type.
        self.storage_encryption_key = storage_encryption_key
        # The billing method for storage. Valid values:
        # 
        # - Postpaid: pay-by-capacity (pay-as-you-go).
        # - Prepaid: pay-by-space (subscription).
        self.storage_pay_type = storage_pay_type
        # The storage space for subscription (pay-by-space) billing. Unit: GB.
        # > - Valid values for PolarDB for MySQL Enterprise Edition: 10 to 50000.
        # > - Valid values for PolarDB for MySQL Standard Edition: 20 to 64000.
        # > - When the storage type of Standard Edition is ESSDAUTOPL, valid values are 40 to 64000 with a minimum step of 10, meaning only values such as 40, 50, 60, and so on are accepted.
        self.storage_space = storage_space
        # Valid values for Enterprise Edition storage type:
        # - **PSL5**
        # - **PSL4**
        # 
        # Valid values for Standard Edition storage type:
        # - **ESSDPL0**
        # - **ESSDPL1**
        # - **ESSDPL2**
        # - **ESSDPL3**
        # - **ESSDAUTOPL**
        self.storage_type = storage_type
        # The upper limit for automatic storage scaling of Standard Edition clusters. Unit: GB.
        # 
        # > The maximum value is 32000.
        self.storage_upper_bound = storage_upper_bound
        # Specifies whether multi-zone strong data consistency is enabled for the cluster. Valid values:
        # 
        # - **ON**: Multi-zone strong data consistency is enabled. This value applies to the Standard Edition three-zone deployment scenario.
        # 
        # - **OFF**: Multi-zone strong data consistency is not enabled.
        self.strict_consistency = strict_consistency
        # Specifies whether to enable Transparent Data Encryption (TDE). Valid values:
        # 
        # - **true**: enables TDE.
        # - **false**: disables TDE (default).
        # 
        # > * This parameter takes effect only when **DBType** is set to **PostgreSQL** or **Oracle**.
        # > * You can call the [ModifyDBClusterTDE](https://help.aliyun.com/document_detail/167982.html) operation to enable TDE for a PolarDB for MySQL cluster.
        # > * After TDE is enabled, it cannot be disabled.
        self.tdestatus = tdestatus
        # The list of tags.
        self.tag = tag
        # The target minor engine version.
        self.target_minor_version = target_minor_version
        # This parameter is required when **PayType** is set to **Prepaid**.
        # - If **Period** is set to **Month**, **UsedTime** is an integer that ranges from `[1-9]`.
        # - If **Period** is set to **Year**, **UsedTime** is an integer that ranges from `[1-3]`.
        self.used_time = used_time
        # The VPC ID.
        self.vpcid = vpcid
        # The vSwitch ID.
        # 
        # > If you specify VPCId, you must also specify VSwitchId.
        self.v_switch_id = v_switch_id
        # The zone ID.
        # 
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/98041.html) operation to query available zones.
        self.zone_id = zone_id

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agentic_db_cluster_description is not None:
            result['AgenticDbClusterDescription'] = self.agentic_db_cluster_description

        if self.agentic_db_cluster_id is not None:
            result['AgenticDbClusterId'] = self.agentic_db_cluster_id

        if self.agentic_db_type is not None:
            result['AgenticDbType'] = self.agentic_db_type

        if self.allow_shut_down is not None:
            result['AllowShutDown'] = self.allow_shut_down

        if self.architecture is not None:
            result['Architecture'] = self.architecture

        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.auto_use_coupon is not None:
            result['AutoUseCoupon'] = self.auto_use_coupon

        if self.backup_retention_policy_on_cluster_deletion is not None:
            result['BackupRetentionPolicyOnClusterDeletion'] = self.backup_retention_policy_on_cluster_deletion

        if self.bursting_enabled is not None:
            result['BurstingEnabled'] = self.bursting_enabled

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.clone_data_point is not None:
            result['CloneDataPoint'] = self.clone_data_point

        if self.cloud_provider is not None:
            result['CloudProvider'] = self.cloud_provider

        if self.cluster_network_type is not None:
            result['ClusterNetworkType'] = self.cluster_network_type

        if self.creation_category is not None:
            result['CreationCategory'] = self.creation_category

        if self.creation_option is not None:
            result['CreationOption'] = self.creation_option

        if self.dbcluster_description is not None:
            result['DBClusterDescription'] = self.dbcluster_description

        if self.dbminor_version is not None:
            result['DBMinorVersion'] = self.dbminor_version

        if self.dbnode_class is not None:
            result['DBNodeClass'] = self.dbnode_class

        if self.dbnode_num is not None:
            result['DBNodeNum'] = self.dbnode_num

        if self.dbtype is not None:
            result['DBType'] = self.dbtype

        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion

        if self.default_time_zone is not None:
            result['DefaultTimeZone'] = self.default_time_zone

        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.gdnid is not None:
            result['GDNId'] = self.gdnid

        if self.hot_standby_cluster is not None:
            result['HotStandbyCluster'] = self.hot_standby_cluster

        if self.loose_polar_log_bin is not None:
            result['LoosePolarLogBin'] = self.loose_polar_log_bin

        if self.loose_xengine is not None:
            result['LooseXEngine'] = self.loose_xengine

        if self.loose_xengine_use_memory_pct is not None:
            result['LooseXEngineUseMemoryPct'] = self.loose_xengine_use_memory_pct

        if self.lower_case_table_names is not None:
            result['LowerCaseTableNames'] = self.lower_case_table_names

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.parameter_group_id is not None:
            result['ParameterGroupId'] = self.parameter_group_id

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.period is not None:
            result['Period'] = self.period

        if self.promotion_code is not None:
            result['PromotionCode'] = self.promotion_code

        if self.provisioned_iops is not None:
            result['ProvisionedIops'] = self.provisioned_iops

        if self.proxy_class is not None:
            result['ProxyClass'] = self.proxy_class

        if self.proxy_type is not None:
            result['ProxyType'] = self.proxy_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.scale_max is not None:
            result['ScaleMax'] = self.scale_max

        if self.scale_min is not None:
            result['ScaleMin'] = self.scale_min

        if self.scale_ro_num_max is not None:
            result['ScaleRoNumMax'] = self.scale_ro_num_max

        if self.scale_ro_num_min is not None:
            result['ScaleRoNumMin'] = self.scale_ro_num_min

        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist

        if self.serverless_type is not None:
            result['ServerlessType'] = self.serverless_type

        if self.source_resource_id is not None:
            result['SourceResourceId'] = self.source_resource_id

        if self.source_uid is not None:
            result['SourceUid'] = self.source_uid

        if self.standby_az is not None:
            result['StandbyAZ'] = self.standby_az

        if self.storage_auto_scale is not None:
            result['StorageAutoScale'] = self.storage_auto_scale

        if self.storage_encryption is not None:
            result['StorageEncryption'] = self.storage_encryption

        if self.storage_encryption_key is not None:
            result['StorageEncryptionKey'] = self.storage_encryption_key

        if self.storage_pay_type is not None:
            result['StoragePayType'] = self.storage_pay_type

        if self.storage_space is not None:
            result['StorageSpace'] = self.storage_space

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        if self.storage_upper_bound is not None:
            result['StorageUpperBound'] = self.storage_upper_bound

        if self.strict_consistency is not None:
            result['StrictConsistency'] = self.strict_consistency

        if self.tdestatus is not None:
            result['TDEStatus'] = self.tdestatus

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.target_minor_version is not None:
            result['TargetMinorVersion'] = self.target_minor_version

        if self.used_time is not None:
            result['UsedTime'] = self.used_time

        if self.vpcid is not None:
            result['VPCId'] = self.vpcid

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgenticDbClusterDescription') is not None:
            self.agentic_db_cluster_description = m.get('AgenticDbClusterDescription')

        if m.get('AgenticDbClusterId') is not None:
            self.agentic_db_cluster_id = m.get('AgenticDbClusterId')

        if m.get('AgenticDbType') is not None:
            self.agentic_db_type = m.get('AgenticDbType')

        if m.get('AllowShutDown') is not None:
            self.allow_shut_down = m.get('AllowShutDown')

        if m.get('Architecture') is not None:
            self.architecture = m.get('Architecture')

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('AutoUseCoupon') is not None:
            self.auto_use_coupon = m.get('AutoUseCoupon')

        if m.get('BackupRetentionPolicyOnClusterDeletion') is not None:
            self.backup_retention_policy_on_cluster_deletion = m.get('BackupRetentionPolicyOnClusterDeletion')

        if m.get('BurstingEnabled') is not None:
            self.bursting_enabled = m.get('BurstingEnabled')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('CloneDataPoint') is not None:
            self.clone_data_point = m.get('CloneDataPoint')

        if m.get('CloudProvider') is not None:
            self.cloud_provider = m.get('CloudProvider')

        if m.get('ClusterNetworkType') is not None:
            self.cluster_network_type = m.get('ClusterNetworkType')

        if m.get('CreationCategory') is not None:
            self.creation_category = m.get('CreationCategory')

        if m.get('CreationOption') is not None:
            self.creation_option = m.get('CreationOption')

        if m.get('DBClusterDescription') is not None:
            self.dbcluster_description = m.get('DBClusterDescription')

        if m.get('DBMinorVersion') is not None:
            self.dbminor_version = m.get('DBMinorVersion')

        if m.get('DBNodeClass') is not None:
            self.dbnode_class = m.get('DBNodeClass')

        if m.get('DBNodeNum') is not None:
            self.dbnode_num = m.get('DBNodeNum')

        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')

        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')

        if m.get('DefaultTimeZone') is not None:
            self.default_time_zone = m.get('DefaultTimeZone')

        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('GDNId') is not None:
            self.gdnid = m.get('GDNId')

        if m.get('HotStandbyCluster') is not None:
            self.hot_standby_cluster = m.get('HotStandbyCluster')

        if m.get('LoosePolarLogBin') is not None:
            self.loose_polar_log_bin = m.get('LoosePolarLogBin')

        if m.get('LooseXEngine') is not None:
            self.loose_xengine = m.get('LooseXEngine')

        if m.get('LooseXEngineUseMemoryPct') is not None:
            self.loose_xengine_use_memory_pct = m.get('LooseXEngineUseMemoryPct')

        if m.get('LowerCaseTableNames') is not None:
            self.lower_case_table_names = m.get('LowerCaseTableNames')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ParameterGroupId') is not None:
            self.parameter_group_id = m.get('ParameterGroupId')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PromotionCode') is not None:
            self.promotion_code = m.get('PromotionCode')

        if m.get('ProvisionedIops') is not None:
            self.provisioned_iops = m.get('ProvisionedIops')

        if m.get('ProxyClass') is not None:
            self.proxy_class = m.get('ProxyClass')

        if m.get('ProxyType') is not None:
            self.proxy_type = m.get('ProxyType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ScaleMax') is not None:
            self.scale_max = m.get('ScaleMax')

        if m.get('ScaleMin') is not None:
            self.scale_min = m.get('ScaleMin')

        if m.get('ScaleRoNumMax') is not None:
            self.scale_ro_num_max = m.get('ScaleRoNumMax')

        if m.get('ScaleRoNumMin') is not None:
            self.scale_ro_num_min = m.get('ScaleRoNumMin')

        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')

        if m.get('ServerlessType') is not None:
            self.serverless_type = m.get('ServerlessType')

        if m.get('SourceResourceId') is not None:
            self.source_resource_id = m.get('SourceResourceId')

        if m.get('SourceUid') is not None:
            self.source_uid = m.get('SourceUid')

        if m.get('StandbyAZ') is not None:
            self.standby_az = m.get('StandbyAZ')

        if m.get('StorageAutoScale') is not None:
            self.storage_auto_scale = m.get('StorageAutoScale')

        if m.get('StorageEncryption') is not None:
            self.storage_encryption = m.get('StorageEncryption')

        if m.get('StorageEncryptionKey') is not None:
            self.storage_encryption_key = m.get('StorageEncryptionKey')

        if m.get('StoragePayType') is not None:
            self.storage_pay_type = m.get('StoragePayType')

        if m.get('StorageSpace') is not None:
            self.storage_space = m.get('StorageSpace')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        if m.get('StorageUpperBound') is not None:
            self.storage_upper_bound = m.get('StorageUpperBound')

        if m.get('StrictConsistency') is not None:
            self.strict_consistency = m.get('StrictConsistency')

        if m.get('TDEStatus') is not None:
            self.tdestatus = m.get('TDEStatus')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateDBClusterRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('TargetMinorVersion') is not None:
            self.target_minor_version = m.get('TargetMinorVersion')

        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')

        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class CreateDBClusterRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. To add multiple tags to the target cluster at a time, click **Add** to add tag keys.
        # 
        # > You can add up to 20 tag pairs at a time. `Tag.N.Key` corresponds to `Tag.N.Value`.
        self.key = key
        # The tag value. To add multiple tags to the target cluster at a time, click **Add** to add tag values.
        # 
        # > You can add up to 20 tag pairs at a time. `Tag.N.Value` corresponds to `Tag.N.Key`.
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

