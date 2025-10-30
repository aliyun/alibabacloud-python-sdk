# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class CreateDBInstanceRequest(DaraModel):
    def __init__(
        self,
        ainode_spec_infos: List[main_models.CreateDBInstanceRequestAINodeSpecInfos] = None,
        backup_id: str = None,
        cache_storage_size: str = None,
        client_token: str = None,
        create_sample_data: bool = None,
        dbinstance_category: str = None,
        dbinstance_class: str = None,
        dbinstance_description: str = None,
        dbinstance_group_count: str = None,
        dbinstance_mode: str = None,
        deploy_mode: str = None,
        enable_ssl: bool = None,
        encryption_key: str = None,
        encryption_type: str = None,
        engine: str = None,
        engine_version: str = None,
        idle_time: int = None,
        instance_network_type: str = None,
        instance_spec: str = None,
        master_aispec: str = None,
        master_cu: int = None,
        master_node_num: str = None,
        owner_id: int = None,
        pay_type: str = None,
        period: str = None,
        private_ip_address: str = None,
        prod_type: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        security_iplist: str = None,
        seg_disk_performance_level: str = None,
        seg_node_num: str = None,
        seg_storage_type: str = None,
        serverless_mode: str = None,
        serverless_resource: int = None,
        src_db_instance_name: str = None,
        standby_vswitch_id: str = None,
        standby_zone_id: str = None,
        storage_size: int = None,
        storage_type: str = None,
        tag: List[main_models.CreateDBInstanceRequestTag] = None,
        used_time: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
        vector_configuration_status: str = None,
        zone_id: str = None,
    ):
        self.ainode_spec_infos = ainode_spec_infos
        # Backup set ID.
        # 
        # > You can call the [DescribeDataBackups](https://help.aliyun.com/document_detail/210093.html) interface to view the backup set IDs of all backup sets under the target instance.
        self.backup_id = backup_id
        self.cache_storage_size = cache_storage_size
        # Idempotence check. For more information, see [How to Ensure Idempotence](https://help.aliyun.com/document_detail/327176.html).
        self.client_token = client_token
        # Whether to load sample datasets after the instance is created. The values are as follows:
        # 
        # - **true**: Load sample datasets.
        # - **false**: Do not load sample datasets.
        # 
        # > If this parameter is not specified, it defaults to not loading sample datasets.
        self.create_sample_data = create_sample_data
        # Instance series. The value description is as follows:
        # 
        # - **HighAvailability**: High availability version.
        # - **Basic**: Basic version.
        # 
        # > This parameter is required when creating an instance in the storage elastic mode.
        self.dbinstance_category = dbinstance_category
        # Instance type. For more details, see the supplementary description of the DBInstanceClass parameter.
        # 
        # > This parameter is required when creating a reserved storage mode instance.
        self.dbinstance_class = dbinstance_class
        # Instance description.
        self.dbinstance_description = dbinstance_description
        # Number of compute groups. The values are: 2, 4, 8, 12, 16, 24, 32, 64, 96, 128.
        # 
        # > This parameter is required when creating a reserved storage mode instance.
        self.dbinstance_group_count = dbinstance_group_count
        # Instance resource type. The value description is as follows:
        # 
        # - **StorageElastic**: Storage elastic mode.
        # - **Serverless**: Serverless mode.
        # - **Classic**: Storage reserved mode.
        # 
        # > This parameter is required.
        # 
        # This parameter is required.
        self.dbinstance_mode = dbinstance_mode
        # Deployment mode. The values are as follows:
        # - multiple: Multi-zone deployment.
        # - single: Single-zone deployment.
        # 
        # > 
        # > - If this parameter is not specified, the default value is single-zone deployment.
        # > - Currently, only single-zone deployment is supported.
        self.deploy_mode = deploy_mode
        # Specifies whether to enable SSL encryption. Valid values:
        # 
        # *   **true**
        # *   **false** (default)
        self.enable_ssl = enable_ssl
        # Key ID.
        # 
        # > If the value of the **EncryptionType** parameter is **CloudDisk**, you need to specify the encryption key ID within the same region through this parameter; otherwise, it should be empty.
        self.encryption_key = encryption_key
        # Encryption type. The value description is as follows:
        # 
        # - **NULL**: No encryption (default).
        # - **CloudDisk**: Enable cloud disk encryption and specify the key through the **EncryptionKey** parameter.
        # 
        # > Once cloud disk encryption is enabled, it cannot be disabled.
        self.encryption_type = encryption_type
        # Database engine, with the value **gpdb**.
        # 
        # This parameter is required.
        self.engine = engine
        # Engine version. The values are as follows:
        # - **6.0**: Version 6.0.
        # - **7.0**: Version 7.0.
        # 
        # This parameter is required.
        self.engine_version = engine_version
        # The idle release wait time. When the duration without business traffic reaches the specified time, the instance will enter the idle state. The unit is seconds, with a minimum value of 60, and the default value is 600.
        # 
        # > This parameter is required only for Serverless auto-scheduling mode instances.
        self.idle_time = idle_time
        # Instance network type, with the value **VPC**.
        # 
        # > - Only VPC networks are supported in public cloud.
        # > - If not specified, it defaults to VPC type.
        self.instance_network_type = instance_network_type
        # Compute node specifications.
        # 
        # For high-availability versions of the elastic storage mode, the values are as follows:
        # - **2C16G**
        # - **4C32G**
        # - **16C128G**
        # 
        # For basic versions of the elastic storage mode, the values are as follows:
        # - **2C8G**
        # - **4C16G**
        # - **8C32G**
        # - **16C64G**
        # 
        # For Serverless mode, the values are as follows:
        # - **4C16G**
        # - **8C32G**
        # 
        # > This parameter is required when creating an elastic storage mode instance or a Serverless mode instance.
        self.instance_spec = instance_spec
        # This parameter must be specified if you want to change coordinator nodes to AI coordinator nodes.
        # 
        # >-  You cannot specify the MasterAISpec and MasterCU parameters at the same time.
        # >- You can change coordinator nodes to AI coordinator nodes only in specific regions and zones.
        # >- Only AnalyticDB for PostgreSQL V7.0 instances of Basic Edition support AI coordinator nodes.
        # >- You can view the valid values of this parameter on the configuration change page of coordinator nodes.
        self.master_aispec = master_aispec
        # Master resources, with the following values: 
        # - 2 CU 
        # - 4 CU 
        # - 8 CU 
        # - 16 CU 
        # - 32 CU 
        # > Master resources above 8 CU will incur charges.
        self.master_cu = master_cu
        # This parameter is deprecated and should not be passed.
        self.master_node_num = master_node_num
        self.owner_id = owner_id
        # The billing method of the instance. Valid values:
        # 
        # *   **Postpaid**: pay-as-you-go.
        # *   **Prepaid**: subscription.
        # 
        # > 
        # 
        # *   If you do not specify this parameter, Postpaid is used.
        # 
        # *   You can obtain more cost savings if you create a subscription instance for one year or longer. We recommend that you select the billing method that best suits your needs.
        self.pay_type = pay_type
        # Unit of the duration for which resources are purchased. The values are as follows:
        # - **Month**: Month
        # - **Year**: Year
        # 
        # > This parameter is required when creating a subscription-billed instance.
        self.period = period
        # This parameter is deprecated and should not be passed.
        self.private_ip_address = private_ip_address
        # Product type. The values are as follows:
        # - **standard**: Standard Edition.
        # - **cost-effective**: Cost-Effective Edition.
        # 
        # > If this parameter is not specified, the default value is Standard Edition.
        self.prod_type = prod_type
        # Region ID.
        # 
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/86912.html) interface to view available region IDs.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the enterprise resource group where the instance is located.
        self.resource_group_id = resource_group_id
        # The IP address whitelist of the instance.
        # 
        # A value of 127.0.0.1 denies access from any external IP address. You can call the [ModifySecurityIps](https://help.aliyun.com/document_detail/86928.html) operation to modify the IP address whitelist after you create an instance.
        self.security_iplist = security_iplist
        # The performance level of ESSDs. Valid values:
        # 
        # *   **pl0**
        # *   **pl1**
        # *   **pl2**
        # 
        # > 
        # 
        # *   This parameter takes effect only when SegStorageType is set to cloud_essd.
        # 
        # *   If you do not specify this parameter, pl1 is used.
        self.seg_disk_performance_level = seg_disk_performance_level
        # The number of compute nodes. The value description is as follows:
        # 
        # - For the high-availability version of the storage elastic mode, the value range is 4 to 512, and the value must be a multiple of 4.
        # - For the basic version of the storage elastic mode, the value range is 2 to 512, and the value must be a multiple of 2.
        # - For the Serverless mode, the value range is 2 to 512, and the value must be a multiple of 2.
        # 
        # > This parameter is required when creating instances in the storage elastic mode or Serverless mode.
        self.seg_node_num = seg_node_num
        # Disk storage type, currently only ESSD cloud disks are supported, with the value **cloud_essd**.
        # 
        # > This parameter is required when creating an elastic storage mode instance.
        self.seg_storage_type = seg_storage_type
        # The mode of the Serverless instance. The values are as follows:
        # 
        # - **Manual**: Manual scheduling (default).
        # - **Auto**: Auto scheduling.
        # 
        # > This parameter is required only for Serverless mode instances.
        self.serverless_mode = serverless_mode
        # The threshold for computing resources. The value range is 8 to 32, with a step of 8, and the unit is ACU. The default value is 32.
        # 
        # > This parameter is required only for Serverless auto-scheduling mode instances.
        self.serverless_resource = serverless_resource
        # ID of the source instance to be cloned.
        # 
        # > You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) interface to view details of all AnalyticDB for PostgreSQL instances in the target region, including the instance ID.
        self.src_db_instance_name = src_db_instance_name
        # VSwitch ID of the standby zone.
        # 
        # > 
        # > - This parameter is required for multi-zone deployment.
        # > - The VSwitch ID of the standby zone must be in the same zone as the StandbyZoneId.
        self.standby_vswitch_id = standby_vswitch_id
        # ID of the standby zone.
        # 
        # > 
        # > - This parameter is required for multi-zone deployment.
        # > - You can call the [DescribeRegions](https://help.aliyun.com/document_detail/86912.html) interface to view available zone IDs.
        # > - The ID of the standby zone must be different from the ID of the primary zone.
        self.standby_zone_id = standby_zone_id
        # The size of the storage space, in GB, with a value range of <props="china">50~8000<props="intl">50~6000.
        # 
        # > This parameter is required when creating an instance in the storage elastic mode.
        self.storage_size = storage_size
        # This parameter is deprecated and should not be passed.
        self.storage_type = storage_type
        # The Nth tag. The value of N ranges from 1 to 20.
        self.tag = tag
        # Duration for which resources are purchased. The values are as follows:
        # - When **Period** is **Month**, the value ranges from 1 to 9.
        # - When **Period** is **Year**, the value ranges from 1 to 3.
        # 
        # > This parameter is required when creating a subscription-billed instance.
        self.used_time = used_time
        # VPC ID.
        # 
        # > - **VPCId** is required.
        # > - The region of the **VPC** must be consistent with **RegionId**.
        self.vpcid = vpcid
        # vSwitch ID.
        # 
        # > - **vSwitchId** is required.
        # > - The availability zone of the **vSwitch** must be consistent with **ZoneId**.
        self.v_switch_id = v_switch_id
        # Whether to enable vector engine optimization. The value description is as follows:
        # - **enabled**: Enable vector engine optimization.
        # - **disabled** (default): Do not enable vector engine optimization.
        # 
        # > - For mainstream analysis scenarios, data warehouse scenarios, and real-time data warehouse scenarios, it is recommended to **not enable** vector engine optimization.
        # > - For users using the vector analysis engine for AIGC, vector retrieval, and other scenarios, it is recommended to **enable** vector engine optimization.
        self.vector_configuration_status = vector_configuration_status
        # Zone ID.
        # 
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/86912.html) interface to view available zone IDs.
        # 
        # This parameter is required.
        self.zone_id = zone_id

    def validate(self):
        if self.ainode_spec_infos:
            for v1 in self.ainode_spec_infos:
                 if v1:
                    v1.validate()
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AINodeSpecInfos'] = []
        if self.ainode_spec_infos is not None:
            for k1 in self.ainode_spec_infos:
                result['AINodeSpecInfos'].append(k1.to_map() if k1 else None)

        if self.backup_id is not None:
            result['BackupId'] = self.backup_id

        if self.cache_storage_size is not None:
            result['CacheStorageSize'] = self.cache_storage_size

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.create_sample_data is not None:
            result['CreateSampleData'] = self.create_sample_data

        if self.dbinstance_category is not None:
            result['DBInstanceCategory'] = self.dbinstance_category

        if self.dbinstance_class is not None:
            result['DBInstanceClass'] = self.dbinstance_class

        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description

        if self.dbinstance_group_count is not None:
            result['DBInstanceGroupCount'] = self.dbinstance_group_count

        if self.dbinstance_mode is not None:
            result['DBInstanceMode'] = self.dbinstance_mode

        if self.deploy_mode is not None:
            result['DeployMode'] = self.deploy_mode

        if self.enable_ssl is not None:
            result['EnableSSL'] = self.enable_ssl

        if self.encryption_key is not None:
            result['EncryptionKey'] = self.encryption_key

        if self.encryption_type is not None:
            result['EncryptionType'] = self.encryption_type

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.idle_time is not None:
            result['IdleTime'] = self.idle_time

        if self.instance_network_type is not None:
            result['InstanceNetworkType'] = self.instance_network_type

        if self.instance_spec is not None:
            result['InstanceSpec'] = self.instance_spec

        if self.master_aispec is not None:
            result['MasterAISpec'] = self.master_aispec

        if self.master_cu is not None:
            result['MasterCU'] = self.master_cu

        if self.master_node_num is not None:
            result['MasterNodeNum'] = self.master_node_num

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.period is not None:
            result['Period'] = self.period

        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address

        if self.prod_type is not None:
            result['ProdType'] = self.prod_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist

        if self.seg_disk_performance_level is not None:
            result['SegDiskPerformanceLevel'] = self.seg_disk_performance_level

        if self.seg_node_num is not None:
            result['SegNodeNum'] = self.seg_node_num

        if self.seg_storage_type is not None:
            result['SegStorageType'] = self.seg_storage_type

        if self.serverless_mode is not None:
            result['ServerlessMode'] = self.serverless_mode

        if self.serverless_resource is not None:
            result['ServerlessResource'] = self.serverless_resource

        if self.src_db_instance_name is not None:
            result['SrcDbInstanceName'] = self.src_db_instance_name

        if self.standby_vswitch_id is not None:
            result['StandbyVSwitchId'] = self.standby_vswitch_id

        if self.standby_zone_id is not None:
            result['StandbyZoneId'] = self.standby_zone_id

        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.used_time is not None:
            result['UsedTime'] = self.used_time

        if self.vpcid is not None:
            result['VPCId'] = self.vpcid

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vector_configuration_status is not None:
            result['VectorConfigurationStatus'] = self.vector_configuration_status

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ainode_spec_infos = []
        if m.get('AINodeSpecInfos') is not None:
            for k1 in m.get('AINodeSpecInfos'):
                temp_model = main_models.CreateDBInstanceRequestAINodeSpecInfos()
                self.ainode_spec_infos.append(temp_model.from_map(k1))

        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')

        if m.get('CacheStorageSize') is not None:
            self.cache_storage_size = m.get('CacheStorageSize')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('CreateSampleData') is not None:
            self.create_sample_data = m.get('CreateSampleData')

        if m.get('DBInstanceCategory') is not None:
            self.dbinstance_category = m.get('DBInstanceCategory')

        if m.get('DBInstanceClass') is not None:
            self.dbinstance_class = m.get('DBInstanceClass')

        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')

        if m.get('DBInstanceGroupCount') is not None:
            self.dbinstance_group_count = m.get('DBInstanceGroupCount')

        if m.get('DBInstanceMode') is not None:
            self.dbinstance_mode = m.get('DBInstanceMode')

        if m.get('DeployMode') is not None:
            self.deploy_mode = m.get('DeployMode')

        if m.get('EnableSSL') is not None:
            self.enable_ssl = m.get('EnableSSL')

        if m.get('EncryptionKey') is not None:
            self.encryption_key = m.get('EncryptionKey')

        if m.get('EncryptionType') is not None:
            self.encryption_type = m.get('EncryptionType')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('IdleTime') is not None:
            self.idle_time = m.get('IdleTime')

        if m.get('InstanceNetworkType') is not None:
            self.instance_network_type = m.get('InstanceNetworkType')

        if m.get('InstanceSpec') is not None:
            self.instance_spec = m.get('InstanceSpec')

        if m.get('MasterAISpec') is not None:
            self.master_aispec = m.get('MasterAISpec')

        if m.get('MasterCU') is not None:
            self.master_cu = m.get('MasterCU')

        if m.get('MasterNodeNum') is not None:
            self.master_node_num = m.get('MasterNodeNum')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')

        if m.get('ProdType') is not None:
            self.prod_type = m.get('ProdType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')

        if m.get('SegDiskPerformanceLevel') is not None:
            self.seg_disk_performance_level = m.get('SegDiskPerformanceLevel')

        if m.get('SegNodeNum') is not None:
            self.seg_node_num = m.get('SegNodeNum')

        if m.get('SegStorageType') is not None:
            self.seg_storage_type = m.get('SegStorageType')

        if m.get('ServerlessMode') is not None:
            self.serverless_mode = m.get('ServerlessMode')

        if m.get('ServerlessResource') is not None:
            self.serverless_resource = m.get('ServerlessResource')

        if m.get('SrcDbInstanceName') is not None:
            self.src_db_instance_name = m.get('SrcDbInstanceName')

        if m.get('StandbyVSwitchId') is not None:
            self.standby_vswitch_id = m.get('StandbyVSwitchId')

        if m.get('StandbyZoneId') is not None:
            self.standby_zone_id = m.get('StandbyZoneId')

        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateDBInstanceRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')

        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VectorConfigurationStatus') is not None:
            self.vector_configuration_status = m.get('VectorConfigurationStatus')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class CreateDBInstanceRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # Tag key. The restrictions are as follows:
        # 
        # - It cannot be an empty string.
        # - It supports up to 128 characters.
        # - It cannot start with `aliyun` or `acs:`, and it cannot contain `http://` or `https://`.
        self.key = key
        # Tag value. The restrictions are as follows:
        # 
        # - It can be an empty string.
        # - It supports up to 128 characters.
        # - It cannot start with `acs:`, and it cannot contain `http://` or `https://`.
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

class CreateDBInstanceRequestAINodeSpecInfos(DaraModel):
    def __init__(
        self,
        ainode_num: str = None,
        ainode_spec: str = None,
    ):
        self.ainode_num = ainode_num
        self.ainode_spec = ainode_spec

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ainode_num is not None:
            result['AINodeNum'] = self.ainode_num

        if self.ainode_spec is not None:
            result['AINodeSpec'] = self.ainode_spec

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AINodeNum') is not None:
            self.ainode_num = m.get('AINodeNum')

        if m.get('AINodeSpec') is not None:
            self.ainode_spec = m.get('AINodeSpec')

        return self

