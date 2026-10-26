# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDdrInstanceRequest(DaraModel):
    def __init__(
        self,
        backup_set_id: str = None,
        backup_set_region: str = None,
        client_token: str = None,
        connection_mode: str = None,
        dbinstance_class: str = None,
        dbinstance_description: str = None,
        dbinstance_net_type: str = None,
        dbinstance_storage: int = None,
        dbinstance_storage_type: str = None,
        encryption_key: str = None,
        engine: str = None,
        engine_version: str = None,
        instance_network_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        pay_type: str = None,
        period: str = None,
        private_ip_address: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        restore_time: str = None,
        restore_type: str = None,
        role_arn: str = None,
        security_iplist: str = None,
        source_dbinstance_name: str = None,
        source_region: str = None,
        system_dbcharset: str = None,
        used_time: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        # The ID of the backup set used for restoration. You can call the DescribeCrossRegionBackups operation to query backup set IDs.
        # > This parameter is required when **RestoreType** is set to **BackupSet**.
        self.backup_set_id = backup_set_id
        # The region where the backup set resides.
        self.backup_set_region = backup_set_region
        # The client token that is used to ensure the idempotence of the request and prevent duplicate submissions. You can use the client to generate the token, but you must ensure that the token is unique among different requests. The token can contain a maximum of 64 ASCII characters and cannot contain non-ASCII characters.
        self.client_token = client_token
        # The access mode of the destination instance. Valid values:
        # 
        # - **Standard** (default): standard access mode
        # - **Safe**: database proxy mode
        self.connection_mode = connection_mode
        # The instance type of the destination instance. For more information, see [Instance types](https://help.aliyun.com/document_detail/26312.html).
        self.dbinstance_class = dbinstance_class
        # The name of the destination instance. The name must be 2 to 256 characters in length. It must start with a letter or a Chinese character and can contain letters, Chinese characters, digits, underscores (_), and hyphens (-).
        # > The name cannot start with `http://` or `https://`.
        self.dbinstance_description = dbinstance_description
        # The network connection type of the destination instance. Valid values:
        # * **Internet**: public network connection
        # * **Intranet**: internal network connection
        # 
        # This parameter is required.
        self.dbinstance_net_type = dbinstance_net_type
        # The storage capacity of the destination instance. Valid values: **5 to 2000**. The increment is 5 GB. Unit: GB. For more information, see [Instance types](https://help.aliyun.com/document_detail/26312.html).
        self.dbinstance_storage = dbinstance_storage
        # The storage type of the destination instance. Valid values:
        # > We recommend that you keep the storage type consistent with that of the source instance.
        # <details>
        # <summary>ApsaraDB RDS for MySQL</summary>
        # 
        # - local_ssd: Premium Local SSD (default)
        # - cloud_essd: PL1 ESSD
        # - cloud_essd2: PL2 ESSD
        # - cloud_essd3: PL3 ESSD
        # - cloud_ssd: standard SSD (discontinued)
        # </details>
        # 
        # <details>
        # <summary>ApsaraDB RDS for SQL Server</summary>
        # 
        # - cloud_essd: PL1 ESSD
        # - cloud_essd2: PL2 ESSD
        # - cloud_essd3: PL3 ESSD
        # - local_ssd: Premium Local SSD (discontinued)
        # - cloud_ssd: standard SSD (discontinued)
        # 
        # </details>
        # 
        # <details>
        # <summary>ApsaraDB RDS for PostgreSQL</summary>
        # 
        # - cloud_essd: PL1 ESSD
        # - cloud_essd2: PL2 ESSD
        # - cloud_essd3: PL3 ESSD
        # - local_ssd: Premium Local SSD (discontinued)
        # - cloud_ssd: standard SSD (discontinued)
        # 
        # </details>
        self.dbinstance_storage_type = dbinstance_storage_type
        # The ID of the custom key used for cloud disk encryption of the **SQL Server instance**. If you specify this parameter, cloud disk encryption is enabled and cannot be disabled. You must also specify the **RoleARN** parameter.
        # You can view service key ID in service key Management Service (KMS) console or [create a key](https://help.aliyun.com/document_detail/181610.html).
        # 
        # > You can also choose not to specify this parameter and only specify the **RoleARN** parameter. This sets the cloud disk encryption type of the instance to the default service customer master key (CMK) managed by ApsaraDB RDS.
        self.encryption_key = encryption_key
        # The type of the destination database engine. Valid values:
        # * **MySQL**
        # * **SQLServer**
        # * **PostgreSQL**
        # 
        # This parameter is required.
        self.engine = engine
        # The version of the destination database engine. Valid values vary based on the **Engine** parameter:
        # - MySQL: **5.5/5.6/5.7/8.0**
        # - SQL Server: **2008r2 (Premium Local SSD, discontinued)/08r2_ent_ha (Cloud disk edition, discontinued)/2012/2012_ent_ha/2012_std_ha/2012_web/2014_std_ha/2016_ent_ha/2016_std_ha/2016_web/2017_std_ha/2017_ent/2019_std_ha/2019_ent**
        # - PostgreSQL: **10.0/11.0/12.0/13.0/14.0/15.0**
        # 
        # > For SQL Server instances, `_ent` indicates Enterprise Cluster Edition, `_ent_ha` indicates Enterprise Edition, `_std_ha` indicates Standard Edition, and `_web` indicates Web Edition.
        # 
        # This parameter is required.
        self.engine_version = engine_version
        # The network type of the destination instance. Valid values:
        # 
        # * **VPC**: VPC
        # * **Classic**: classic network (discontinued)
        # 
        # > If you select **VPC**, you must also specify the **VpcId** and **VSwitchId** parameters.
        self.instance_network_type = instance_network_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The billing method of the destination instance. Valid values:
        # * **Postpaid**: pay-as-you-go
        # * **Prepaid**: subscription
        # 
        # This parameter is required.
        self.pay_type = pay_type
        # Specifies the subscription period of the destination instance as yearly or monthly. Valid values:
        # * **Year**: yearly
        # * **Month**: monthly
        # 
        # > This parameter is required when the billing method is set to **Prepaid**.
        self.period = period
        # The internal IP address of the destination instance. The IP address must be within the CIDR block of the specified vSwitch. By default, the system automatically allocates an IP address based on the **VPCId** and **VSwitchId** parameters.
        self.private_ip_address = private_ip_address
        # The ID of the destination region. You can call the DescribeRegions operation to query region IDs.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The point in time to which you want to restore data. The time must be earlier than the current time. Specify the time in the <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z format. The time must be in UTC.
        # > This parameter is required when **RestoreType** is set to **BackupTime**.
        self.restore_time = restore_time
        # The restoration method. Valid values:
        # 
        # - **BackupSet**: restores data from a backup set to the new instance. You must also specify the **BackupSetId** parameter.
        # - **BackupTime**: restores data to a specific point in time within the log backup retention period. You must also specify the **RestoreTime**, **SourceRegion**, and **SourceDBInstanceName** parameters.
        # 
        # This parameter is required.
        self.restore_type = restore_type
        # The Alibaba Cloud Resource Name (ARN) used for the authorization of the Alibaba Cloud account to grant the ApsaraDB RDS service account access to KMS for the **SQL Server instance**. You can call the [CheckCloudResourceAuthorized](https://help.aliyun.com/document_detail/2628797.html) operation to query the ARN.
        self.role_arn = role_arn
        # The [IP address whitelist](https://help.aliyun.com/document_detail/43185.html) of the destination instance. Separate multiple IP addresses with commas (,). You can add up to 1,000 unique IP addresses. The following formats are supported:
        # * IP address format. Example: 10.23.12.24.
        # * CIDR block format. Example: 10.23.12.24/24 (Classless Inter-Domain Routing, where 24 indicates the length of the prefix in the IP address, and the prefix length ranges from 1 to 32).
        # 
        # This parameter is required.
        self.security_iplist = security_iplist
        # The ID of the source instance for point-in-time restoration.
        # > This parameter is required when **RestoreType** is set to **BackupTime**.
        self.source_dbinstance_name = source_dbinstance_name
        # The ID of the source region for point-in-time restoration.
        # > This parameter is required when **RestoreType** is set to **BackupTime**.
        self.source_region = source_region
        # The character set of the destination instance. Valid values:
        # * **utf8**
        # * **gbk**
        # * **latin1**
        # * **utf8mb4**
        self.system_dbcharset = system_dbcharset
        # The subscription duration. Valid values:
        # * If the **Period** parameter is set to **Year**, valid values are **1 to 3**.
        # * If the **Period** parameter is set to **Month**, valid values are **1 to 9**.
        # 
        # > This parameter is required when the billing method is set to **Prepaid**.
        self.used_time = used_time
        # The VPC ID of the destination instance.
        # 
        # > - This parameter is required when **InstanceNetworkType** is set to **VPC**.
        # > - After you specify this parameter, you must also specify the **ZoneId** parameter.
        self.vpcid = vpcid
        # The vSwitch ID of the destination instance. Separate multiple vSwitch IDs with commas (,).
        # 
        # > - This parameter is required when **InstanceNetworkType** is set to **VPC**.
        # > - After you specify this parameter, you must also specify the **ZoneId** parameter.
        self.v_switch_id = v_switch_id
        # The zone ID of the destination instance. Separate multiple zone IDs with colons (:).
        # 
        # > If you specify a VPC and a vSwitch, this parameter is required to match the zone of the vSwitch.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_set_id is not None:
            result['BackupSetId'] = self.backup_set_id

        if self.backup_set_region is not None:
            result['BackupSetRegion'] = self.backup_set_region

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.connection_mode is not None:
            result['ConnectionMode'] = self.connection_mode

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

        if self.encryption_key is not None:
            result['EncryptionKey'] = self.encryption_key

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.instance_network_type is not None:
            result['InstanceNetworkType'] = self.instance_network_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.period is not None:
            result['Period'] = self.period

        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.restore_time is not None:
            result['RestoreTime'] = self.restore_time

        if self.restore_type is not None:
            result['RestoreType'] = self.restore_type

        if self.role_arn is not None:
            result['RoleARN'] = self.role_arn

        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist

        if self.source_dbinstance_name is not None:
            result['SourceDBInstanceName'] = self.source_dbinstance_name

        if self.source_region is not None:
            result['SourceRegion'] = self.source_region

        if self.system_dbcharset is not None:
            result['SystemDBCharset'] = self.system_dbcharset

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
        if m.get('BackupSetId') is not None:
            self.backup_set_id = m.get('BackupSetId')

        if m.get('BackupSetRegion') is not None:
            self.backup_set_region = m.get('BackupSetRegion')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ConnectionMode') is not None:
            self.connection_mode = m.get('ConnectionMode')

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

        if m.get('EncryptionKey') is not None:
            self.encryption_key = m.get('EncryptionKey')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('InstanceNetworkType') is not None:
            self.instance_network_type = m.get('InstanceNetworkType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('RestoreTime') is not None:
            self.restore_time = m.get('RestoreTime')

        if m.get('RestoreType') is not None:
            self.restore_type = m.get('RestoreType')

        if m.get('RoleARN') is not None:
            self.role_arn = m.get('RoleARN')

        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')

        if m.get('SourceDBInstanceName') is not None:
            self.source_dbinstance_name = m.get('SourceDBInstanceName')

        if m.get('SourceRegion') is not None:
            self.source_region = m.get('SourceRegion')

        if m.get('SystemDBCharset') is not None:
            self.system_dbcharset = m.get('SystemDBCharset')

        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')

        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

