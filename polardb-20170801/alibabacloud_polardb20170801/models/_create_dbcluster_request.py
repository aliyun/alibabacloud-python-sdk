# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class CreateDBClusterRequest(DaraModel):
    def __init__(
        self,
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
        # Specifies whether to enable pause on inactivity. Valid values:
        # 
        # - **true**: enables pause on inactivity.
        # 
        # - **false** (default): disables pause on inactivity.
        # 
        # > This parameter is supported only for serverless clusters.
        self.allow_shut_down = allow_shut_down
        # The CPU architecture. Valid values:
        # 
        # - X86
        # 
        # - ARM
        self.architecture = architecture
        # Specifies whether to enable auto-renewal. Valid values:
        # 
        # - **true**: enables auto-renewal.
        # 
        # - **false**: disables auto-renewal.
        # 
        # Default value: **false**.
        # 
        # > This parameter takes effect only when **PayType** is set to **Prepaid**.
        self.auto_renew = auto_renew
        # Specifies whether to automatically use a coupon. Valid values:
        # 
        # - true (default): Automatically uses a coupon.
        # 
        # - false: does not use a coupon.
        self.auto_use_coupon = auto_use_coupon
        # The backup retention policy to apply when the cluster is deleted. Valid values:
        # 
        # - **ALL**: retains all backup sets.
        # 
        # - **LATEST**: retains only the last backup set. An automatic backup is performed before the cluster is deleted.
        # 
        # - **NONE**: does not retain backup sets.
        # 
        # Default value: **NONE**.
        # 
        # > - This parameter is valid only if **DBType** is set to **MySQL**.
        # >
        # > - Serverless clusters do not support this parameter.
        self.backup_retention_policy_on_cluster_deletion = backup_retention_policy_on_cluster_deletion
        # Specifies whether to enable the performance burst feature for the ESSD AutoPL cloud disk. Valid values:
        # 
        # - **true**: enables the performance burst feature.
        # 
        # - **false** (default): disables the performance burst feature.
        # 
        # > This parameter is supported only when **StorageType** is set to ESSDAUTOPL.
        self.bursting_enabled = bursting_enabled
        # A client-generated token that ensures the idempotence of the request. This token must be unique across all requests and is case-sensitive. It can contain up to 64 ASCII characters.
        self.client_token = client_token
        # The point in time for the clone. Valid values:
        # 
        # - **LATEST**: The latest point in time.
        # 
        # - **BackupID**: The ID of a historical backup set.
        # 
        # - **Timestamp**: A specific point in time in the `YYYY-MM-DDThh:mm:ssZ` format. The time must be in UTC.
        # 
        # Default value: **LATEST**.
        # 
        # > If you set **CreationOption** to **CloneFromRDS**, you can set this parameter only to **LATEST**.
        self.clone_data_point = clone_data_point
        # The cloud service provider of the instance.
        self.cloud_provider = cloud_provider
        # The network type of the cluster. Only **VPC** is supported.
        self.cluster_network_type = cluster_network_type
        # The edition of the cluster. Valid values:
        # 
        # - **Normal**: Cluster Edition (default)
        # 
        # - **Basic**: Single-node Edition
        # 
        # - **ArchiveNormal**: X-Engine Edition
        # 
        # - **NormalMultimaster**: Multi-master Cluster Edition
        # 
        # - **SENormal**: Standard Edition
        # 
        # > * The **Basic** edition is supported for PolarDB for MySQL **5.6**, **5.7**, and **8.0**; PolarDB for PostgreSQL **14**; and PolarDB for PostgreSQL (compatible with Oracle) **2.0**.
        # >
        # > * The **ArchiveNormal** and **NormalMultimaster** editions are supported for PolarDB for MySQL **8.0**.
        # >
        # > * The **SENormal** edition is supported for PolarDB for MySQL **5.6**, **5.7**, and **8.0** and PolarDB for PostgreSQL **14**.
        # 
        # For more information about product editions, see [Editions](https://help.aliyun.com/document_detail/183258.html).
        self.creation_category = creation_category
        # The method to create the cluster. Valid values:
        # 
        # - **Normal**: Creates a new PolarDB cluster. For more information, see the following topics:
        # 
        #   - [Create a PolarDB for MySQL cluster](https://help.aliyun.com/document_detail/58769.html)
        # 
        #   - [Create a PolarDB for PostgreSQL cluster](https://help.aliyun.com/document_detail/118063.html)
        # 
        #   - [Create a PolarDB for PostgreSQL (compatible with Oracle) cluster](https://help.aliyun.com/document_detail/118182.html)
        # 
        # - **CloneFromPolarDB**: Clones data from an existing PolarDB cluster. For more information, see the following topics:
        # 
        #   - [Clone a PolarDB for MySQL cluster](https://help.aliyun.com/document_detail/87966.html)
        # 
        #   - [Clone a PolarDB for PostgreSQL cluster](https://help.aliyun.com/document_detail/118108.html)
        # 
        #   - [Clone a PolarDB for PostgreSQL (compatible with Oracle) cluster](https://help.aliyun.com/document_detail/118221.html)
        # 
        # - **RecoverFromRecyclebin**: Restores a PolarDB cluster from the recycle bin. For more information, see the following topics:
        # 
        #   - [Restore a released PolarDB for MySQL cluster](https://help.aliyun.com/document_detail/164880.html)
        # 
        #   - [Restore a released PolarDB for PostgreSQL cluster](https://help.aliyun.com/document_detail/432844.html)
        # 
        #   - [Restore a released PolarDB for PostgreSQL (compatible with Oracle) cluster](https://help.aliyun.com/document_detail/424632.html)
        # 
        # - **CloneFromRDS**: Clones data from an existing ApsaraDB RDS instance to a new PolarDB cluster. For more information, see [One-click cloning from ApsaraDB RDS for MySQL to PolarDB for MySQL](https://help.aliyun.com/document_detail/121812.html).
        # 
        # - **MigrationFromRDS**: Migrates data from an existing ApsaraDB RDS instance. The created PolarDB cluster is in read-only mode and has binary logging enabled by default. For more information, see [One-click upgrade from ApsaraDB RDS for MySQL to PolarDB for MySQL](https://help.aliyun.com/document_detail/121582.html).
        # 
        # - **CreateGdnStandby**: Creates a secondary cluster in a Global Database Network (GDN). For more information, see [Add a secondary cluster](https://help.aliyun.com/document_detail/160381.html).
        # 
        # - **UpgradeFromPolarDB**: Upgrades the major version of a PolarDB cluster. For more information, see [Perform a major version upgrade](https://help.aliyun.com/document_detail/459712.html).
        # 
        # Default value: **Normal**.
        # 
        # > If **DBType** is set to **MySQL** and **DBVersion** is set to **8.0**, you can set this parameter to **CreateGdnStandby**.
        self.creation_option = creation_option
        # The description of the cluster. The description must meet the following requirements:
        # 
        # - It cannot start with `http://` or `https://`.
        # 
        # - It must be 2 to 256 characters in length.
        self.dbcluster_description = dbcluster_description
        # The minor version of the database engine. Valid values:
        # 
        # - **8.0.2**
        # 
        # - **8.0.1**
        # 
        # > This parameter is valid only if **DBType** is set to **MySQL** and **DBVersion** is set to **8.0**.
        self.dbminor_version = dbminor_version
        # The node specification. For more information, see the following topics:
        # 
        # - PolarDB for MySQL: [Compute node specifications](https://help.aliyun.com/document_detail/102542.html)
        # 
        # - PolarDB for PostgreSQL (compatible with Oracle): [Compute node specifications](https://help.aliyun.com/document_detail/207921.html)
        # 
        # - PolarDB for PostgreSQL: [Compute node specifications](https://help.aliyun.com/document_detail/209380.html)
        # 
        # > * To create a PolarDB for MySQL Cluster Edition serverless cluster, set this parameter to **polar.mysql.sl.small**.
        # >
        # > * To create a PolarDB for MySQL Standard Edition serverless cluster, set this parameter to **polar.mysql.sl.small.c**.
        # >
        # > * To create a PolarDB for PostgreSQL Cluster Edition serverless cluster, set this parameter to **polar.pg.sl.small**.
        # >
        # > * To create a PolarDB for PostgreSQL Standard Edition serverless cluster, set this parameter to **polar.pg.sl.small.c**.
        # >
        # > * To create a PolarDB for PostgreSQL (compatible with Oracle) serverless cluster, set this parameter to **polar.o.sl.small**.
        self.dbnode_class = dbnode_class
        # The number of nodes for a Standard Edition or Enterprise Edition cluster. Valid values:
        # 
        # - Standard Edition: 1 to 8. A cluster of this edition includes one read/write node and up to seven read-only nodes.
        # 
        # - Enterprise Edition: 1 to 16. A cluster of this edition includes one read/write node and up to 15 read-only nodes.
        # 
        # > * By default, an Enterprise Edition cluster has two nodes and a Standard Edition cluster has one node.
        # >
        # > * This parameter is supported only for PolarDB for MySQL.
        # >
        # > * You cannot change the number of nodes in a Multi-master Cluster Edition cluster.
        self.dbnode_num = dbnode_num
        # The database engine. Valid values:
        # 
        # - **MySQL**
        # 
        # - **PostgreSQL**
        # 
        # - **Oracle**
        # 
        # This parameter is required.
        self.dbtype = dbtype
        # The version of the database engine.
        # 
        # - Valid values for MySQL:
        # 
        #   - **5.6**
        # 
        #   - **5.7**
        # 
        #   - **8.0**
        # 
        # - Valid values for PostgreSQL:
        # 
        #   - **11**
        # 
        #   - **14**
        # 
        #   - **15**<props="china">
        # 
        # > If you create a serverless cluster for PolarDB for PostgreSQL, you must set this parameter to `14`.
        # 
        # \\* Valid values for Oracle:
        # \\* **11**
        # \\* **14**
        # 
        # This parameter is required.
        self.dbversion = dbversion
        # Cluster time zone (UTC). The value can be any full-hour offset from **-12:00 to +13:00**, such as **00:00**. The default value is **SYSTEM**, which uses the region\\"s time zone.
        # 
        # > This parameter takes effect only when **DBType** is **MySQL**.
        self.default_time_zone = default_time_zone
        # The ID of the Edge Node Service (ENS) node. This parameter is required if you want to create an ENS database instance.
        self.ens_region_id = ens_region_id
        # The ID of the Global Database Network (GDN).
        # 
        # > This parameter is required if **CreationOption** is set to **CreateGdnStandby**.
        self.gdnid = gdnid
        # Specifies whether to enable the hot standby cluster feature. Valid values:
        # 
        # - **ON** (default): enables a hot standby storage cluster.
        # 
        # - **OFF**: disables the hot standby cluster feature.
        # 
        # - **STANDBY**: enables a hot standby cluster.
        # 
        # - **EQUAL**: enables hot standby for both storage and computing resources.
        # 
        # - **3AZ**: enables multi-AZ strong consistency.
        # 
        # > The value **STANDBY** is valid only for PolarDB for PostgreSQL.
        self.hot_standby_cluster = hot_standby_cluster
        # Specifies whether to enable binary logging. Valid values:
        # 
        # - **ON**: enables binary logging.
        # 
        # - **OFF**: disables binary logging.
        # 
        # > This parameter is valid only if **DBType** is set to **MySQL**.
        self.loose_polar_log_bin = loose_polar_log_bin
        # Specifies whether to enable the X-Engine storage engine. Valid values:
        # 
        # - **ON**: enables the X-Engine storage engine.
        # 
        # - **OFF**: disables the X-Engine storage engine.
        # 
        # > This parameter is valid only if the **CreationOption** parameter is not set to **CreateGdnStandby**, **DBType** is set to **MySQL**, and **DBVersion** is set to **8.0**. To enable the X-Engine storage engine, the node must have at least 8 GB of memory.
        self.loose_xengine = loose_xengine
        # The percentage of memory allocated to the X-Engine storage engine. Valid values: integers from 10 to 90.
        # 
        # > This parameter is valid only if **LooseXEngine** is set to **ON**.
        self.loose_xengine_use_memory_pct = loose_xengine_use_memory_pct
        # The time zone of the cluster. The value must be a UTC offset in the `±HH:mm` format. Valid values: from **-12:00** to **+13:00** on the hour. For example, **00:00**. The default value **SYSTEM** indicates that the cluster uses the time zone of its region.
        # 
        # - **1**: Case-insensitive
        # 
        # - **0**: Case-sensitive
        # 
        # The default value is **1**.
        # 
        # > This parameter is valid only if **DBType** is set to **MySQL**.
        self.lower_case_table_names = lower_case_table_names
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the parameter template.
        # 
        # > You can call the [DescribeParameterGroups](https://help.aliyun.com/document_detail/207178.html) operation to query the parameter templates in a specific region, including the IDs of the parameter templates.
        self.parameter_group_id = parameter_group_id
        # The billing method. Valid values:
        # 
        # - **Postpaid**: pay-as-you-go.
        # 
        # - **Prepaid**: subscription.
        # 
        # This parameter is required.
        self.pay_type = pay_type
        # The unit of the subscription duration. This parameter is required if you set the **PayType** parameter to **Prepaid**. Valid values:
        # 
        # - **Year**: The subscription duration is measured in years.
        # 
        # - **Month**: The subscription duration is measured in months.
        self.period = period
        # The promotion code. If you do not specify this parameter, the default coupon is used.
        self.promotion_code = promotion_code
        # <props="china">
        # 
        # The provisioned read/write IOPS of the ESSD AutoPL cloud disk. Valid values: 0 to min{50,000, 1,000 × Capacity - Baseline IOPS}.
        # 
        # 
        # 
        # <props="china">
        # 
        # Baseline IOPS = min{1,800 + 50 × Capacity, 50,000}.
        # 
        # 
        # 
        # <props="china">
        # 
        # > This parameter is supported only when **StorageType** is set to ESSDAUTOPL.
        self.provisioned_iops = provisioned_iops
        # The specification of the database proxy for a Standard Edition cluster. Valid values:
        # 
        # - **polar.maxscale.g2.medium.c**: 2 cores
        # 
        # - **polar.maxscale.g2.large.c**: 4 cores
        # 
        # - **polar.maxscale.g2.xlarge.c**: 8 cores
        # 
        # - **polar.maxscale.g2.2xlarge.c**: 16 cores
        # 
        # - **polar.maxscale.g2.3xlarge.c**: 24 cores
        # 
        # - **polar.maxscale.g2.4xlarge.c**: 32 cores
        # 
        # - **polar.maxscale.g2.8xlarge.c**: 64 cores
        self.proxy_class = proxy_class
        # The type of the database proxy. Valid values:
        # 
        # - **EXCLUSIVE**: Enterprise Dedicated
        # 
        # - **GENERAL**: Enterprise General-purpose
        # 
        # > The proxy type must be consistent with the type that corresponds to the node specification of the cluster:
        # >
        # > - If the node specification is general-purpose, the proxy type must be Enterprise General-purpose.
        # >
        # > - If the node specification is dedicated, the proxy type must be Enterprise Dedicated.
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
        # The maximum number of PCUs for a single-node serverless cluster to scale up to. Valid values: 1 to 32.
        # 
        # > This parameter is supported only for serverless clusters.
        self.scale_max = scale_max
        # The minimum number of PolarDB compute units (PCUs) for a single-node serverless cluster to scale down to. Valid values: 1 to 31.
        # 
        # > This parameter is supported only for serverless clusters.
        self.scale_min = scale_min
        # The maximum number of read-only nodes that the serverless cluster scales up to. Valid values: 0 to 15.
        # 
        # > This parameter is supported only for serverless clusters.
        self.scale_ro_num_max = scale_ro_num_max
        # The minimum number of read-only nodes that the serverless cluster scales down to. Valid values: 0 to 15.
        # 
        # > This parameter is supported only for serverless clusters.
        self.scale_ro_num_min = scale_ro_num_min
        # The IP whitelist of the PolarDB cluster.
        # 
        # > You can specify multiple IP addresses in the IP whitelist. Separate the IP addresses with commas (,).
        self.security_iplist = security_iplist
        # The type of the serverless cluster. Set the value to **AgileServerless**.
        # 
        # > This parameter is supported only for serverless clusters.
        self.serverless_type = serverless_type
        # The ID of the source ApsaraDB RDS instance or source PolarDB cluster. This parameter is required only if **CreationOption** is set to **MigrationFromRDS**, **CloneFromRDS**, **CloneFromPolarDB**, or **RecoverFromRecyclebin**.
        # 
        # - If **CreationOption** is set to **MigrationFromRDS** or **CloneFromRDS**, specify the ID of the source ApsaraDB RDS instance. The source ApsaraDB RDS instance must be ApsaraDB RDS for MySQL 5.6, 5.7, or 8.0 High-availability Edition.
        # 
        # - If **CreationOption** is set to **CloneFromPolarDB**, specify the ID of the source PolarDB cluster. The new cluster must use the same database engine as the source cluster. For example, if the source cluster runs MySQL 8.0, you must set **DBType** to **MySQL** and **DBVersion** to **8.0** for the new cluster.
        # 
        # - If **CreationOption** is set to **RecoverFromRecyclebin**, specify the ID of the released source PolarDB cluster. The restored cluster must use the same database engine as the source cluster. For example, if the source cluster runs MySQL 8.0, you must set **DBType** to **MySQL** and **DBVersion** to **8.0** for the restored cluster.
        self.source_resource_id = source_resource_id
        # The UID of the source backup set owner in cross-account backup and restoration scenarios.
        self.source_uid = source_uid
        # The zone for the hot standby cluster.
        # 
        # > This parameter is valid only when the hot standby cluster feature or multi-AZ strong consistency is enabled.
        self.standby_az = standby_az
        # Specifies whether to enable automatic storage scaling for a Standard Edition cluster. Valid values:
        # 
        # - Enable: enables automatic storage scaling.
        # 
        # - Disable: disables automatic storage scaling.
        self.storage_auto_scale = storage_auto_scale
        # Specifies whether to enable cloud disk encryption. Valid values:
        # 
        # - **true**: enables cloud disk encryption.
        # 
        # - **false** (default): disables cloud disk encryption.
        # 
        # > This parameter is valid only if **DBType** is set to **MySQL**.
        # 
        # > This parameter is valid only if **StorageType** is set to a Standard Edition storage type.
        self.storage_encryption = storage_encryption
        # The ID of a custom key from Key Management Service (KMS) for cloud disk encryption. The key must be in the same region as the cluster. If you specify this parameter, cloud disk encryption is automatically enabled and cannot be disabled. If this parameter is empty, the default service key is used.
        # 
        # You can view the key ID or create a new key in the Key Management Service (KMS) console.
        # 
        # > This parameter is valid only if **DBType** is set to **MySQL**.
        # 
        # > This parameter is valid only if **StorageType** is set to a Standard Edition storage type.
        self.storage_encryption_key = storage_encryption_key
        # The billing method for storage. Valid values:
        # 
        # - Postpaid: pay-by-capacity (a pay-as-you-go method).
        # 
        # - Prepaid: pay-by-space (a subscription method).
        self.storage_pay_type = storage_pay_type
        # The storage space for a pay-by-space (subscription) cluster. Unit: GB.
        # 
        # > - Valid values for a PolarDB for MySQL Enterprise Edition cluster: 10 to 50000.
        # >
        # > - Valid values for a PolarDB for MySQL Standard Edition cluster: 20 to 64000.
        # >
        # > - If the storage type of a Standard Edition cluster is ESSD AutoPL, the storage space must be a multiple of 10 between 40 and 64000.
        self.storage_space = storage_space
        # Valid values for Enterprise Edition:
        # 
        # - **PSL5**
        # 
        # - **PSL4**
        # 
        # Valid values for Standard Edition:
        # 
        # - **ESSDPL0**
        # 
        # - **ESSDPL1**
        # 
        # - **ESSDPL2**
        # 
        # - **ESSDPL3**
        # 
        # - **ESSDAUTOPL**
        self.storage_type = storage_type
        # The maximum storage capacity for a Standard Edition cluster when automatic storage scaling is enabled. Unit: GB.
        # 
        # > The maximum value is 32000.
        self.storage_upper_bound = storage_upper_bound
        # Specifies whether to enable multi-AZ strong consistency for the cluster. Valid values:
        # 
        # - **ON**: enables multi-AZ strong consistency. This feature is applicable to Standard Edition clusters that are deployed across three zones.
        # 
        # - **OFF**: disables multi-AZ strong consistency.
        self.strict_consistency = strict_consistency
        # Specifies whether to enable transparent data encryption (TDE). Valid values:
        # 
        # - **true**: enables TDE.
        # 
        # - **false** (default): disables TDE.
        # 
        # > * This parameter is valid only when **DBType** is set to **PostgreSQL** or **Oracle**.
        # >
        # > * You can call the [ModifyDBClusterTDE](https://help.aliyun.com/document_detail/167982.html) operation to enable TDE for a PolarDB for MySQL cluster.
        # >
        # > * TDE cannot be disabled after it is enabled.
        self.tdestatus = tdestatus
        # The tags to add to the cluster.
        self.tag = tag
        # The target minor engine version.
        self.target_minor_version = target_minor_version
        # The subscription duration. This parameter is required if you set the **PayType** parameter to **Prepaid**.
        # 
        # - If **Period** is set to **Month**, **UsedTime** must be an integer from `[1-9]`.
        # 
        # - If **Period** is set to **Year**, **UsedTime** must be an integer from `[1-3]`.
        self.used_time = used_time
        # The ID of the VPC.
        self.vpcid = vpcid
        # The ID of the VSwitch.
        # 
        # > If you specify the VPCId parameter, you must also specify this parameter.
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
        # The key of the tag.
        # 
        # > You can add up to 20 tags at a time. The Nth tag is a key-value pair, where `Tag.N.Key` is the key and `Tag.N.Value` is the value.
        self.key = key
        # The value of the tag.
        # 
        # > You can add up to 20 tags at a time. The Nth tag is a key-value pair, where `Tag.N.Key` is the key and `Tag.N.Value` is the value.
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

