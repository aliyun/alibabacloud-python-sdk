# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDBInstanceShrinkRequest(DaraModel):
    def __init__(
        self,
        auto_renew: bool = None,
        cnnode_count: int = None,
        client_token: str = None,
        cn_class: str = None,
        dbnode_class: str = None,
        dbnode_count: int = None,
        dnnode_count: int = None,
        description: str = None,
        dn_class: str = None,
        dn_storage_space: str = None,
        engine_version: str = None,
        extra_params_shrink: str = None,
        is_columnar_read_dbinstance: bool = None,
        is_read_dbinstance: bool = None,
        network_type: str = None,
        origin_minor_version: str = None,
        pay_type: str = None,
        period: str = None,
        primary_dbinstance_name: str = None,
        primary_zone: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        secondary_zone: str = None,
        series: str = None,
        storage_type: str = None,
        tertiary_zone: str = None,
        topology_type: str = None,
        used_time: int = None,
        vpcid: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        # Specifies whether to enable auto-renewal. Default value: true.
        # 
        # - **true**: Enable
        # - **false**: Disable
        self.auto_renew = auto_renew
        # The number of compute nodes.
        self.cnnode_count = cnnode_count
        # The idempotency token. Ensure that a unique value is used for each creation request.
        self.client_token = client_token
        # The compute node specification. Required for creating Enterprise Edition instances. Not required for Standard Edition.
        # 
        # Enterprise Edition local disk:
        # 
        # - **polarx.x4.medium.2e**:	2 Cores 8 GB (General Purpose)
        # - **polarx.x4.large.2e**:	4 Cores 16 GB (General Purpose)
        # - **polarx.x4.xlarge.2e**:	8 Cores 32 GB (General Purpose)
        # - **polarx.x4.2xlarge.2e**:	16 Cores 64 GB (General Purpose)
        # - **polarx.x8.large.2e**:	4 Cores 32 GB (Dedicated)
        # - **polarx.x2.large.2x**:	8 Cores 16 GB (Dedicated)
        # - **polarx.x4.xlarge.2x**:	8 Cores 32 GB (Dedicated)
        # - **polarx.x8.xlarge.2e**:	8 Cores 64 GB (Dedicated)
        # - **polarx.x8.2xlarge.2e**:	16 Cores 128 GB (Dedicated)
        # - **polarx.x4.4xlarge.2e**:	32 Cores 128 GB (Dedicated)
        # - **polarx.x8.4xlarge.2e**:	32 Cores 256 GB (Dedicated)
        # - **polarx.st.8xlarge.2e**:	60 Cores 470 GB (Dedicated)
        # - **polarx.st.12xlarge.2e**:	90 Cores 720 GB (Dedicated)
        # 
        # 
        # Enterprise Edition cloud disk:
        # - **polarx.x4.medium.c2e**:	2 Cores 8 GB (General Purpose)
        # - **polarx.x4.large.c2e**:	4 Cores 16 GB (General Purpose)
        # - **polarx.x4.xlarge.c2e**:	8 Cores 32 GB (General Purpose)
        # - **polarx.x4.2xlarge.c2e**:	16 Cores 64 GB (General Purpose)
        # - **polarx.x8.large.c2e**:	4 Cores 32 GB (Dedicated)
        # - **polarx.x2.large.c2x**:	8 Cores 16 GB (Dedicated)
        # - **polarx.x4.xlarge.c2x**:	8 Cores 32 GB (Dedicated)
        # - **polarx.x8.xlarge.c2e**:	8 Cores 64 GB (Dedicated)
        # - **polarx.x8.2xlarge.c2e**:	16 Cores 128 GB (Dedicated)
        # - **polarx.x4.4xlarge.c2e**:	32 Cores 128 GB (Dedicated)
        # - **polarx.x8.4xlarge.c2e**:	32 Cores 256 GB (Dedicated)
        # - **polarx.st.8xlarge.c2e**:	60 Cores 470 GB (Dedicated)
        # - **polarx.st.12xlarge.c2e**:	90 Cores 720 GB (Dedicated)
        self.cn_class = cn_class
        # Required for creating Standard Edition instances. Not required for Enterprise Edition.
        # 
        # Standard Edition local disk specifications:
        # - **mysql.n8.small.25**:	1 Core 8 GB (General Purpose)
        # - **mysql.n2.medium.25**:	2 Cores 4 GB (General Purpose)
        # - **mysql.n4.medium.25**:	2 Cores 8 GB (General Purpose)
        # - **mysql.n8.medium.25**:	2 Cores 16 GB (General Purpose)
        # - **mysql.n2.large.25**:	4 Cores 8 GB (General Purpose)
        # - **mysql.n4.large.25**:	4 Cores 16 GB (General Purpose)
        # - **mysql.n8.large.25**:	4 Cores 32 GB (General Purpose)
        # - **mysql.n2.xlarge.25**:	8 Cores 16 GB (General Purpose)
        # - **mysql.n4.xlarge.25**:	8 Cores 32 GB (General Purpose)
        # - **mysql.n8.xlarge.25**:	8 Cores 64 GB (General Purpose)
        # - **mysql.n2.2xlarge.25**:	16 Cores 32 GB (General Purpose)
        # - **mysql.n4.2xlarge.25**:	16 Cores 64 GB (General Purpose)
        # - **mysql.n8.2xlarge.25**:	16 Cores 128 GB (General Purpose)
        # - **mysql.x2.medium.25**:	2 Cores 4 GB (Dedicated)
        # - **mysql.x4.medium.25**:	2 Cores 8 GB (Dedicated)
        # - **mysql.x8.medium.25**:	2 Cores 16 GB (Dedicated)
        # - **mysql.x2.large.25**:	4 Cores 8 GB (Dedicated)
        # - **mysql.x4.large.25**:	4 Cores 16 GB (Dedicated)
        # - **mysql.x8.large.25**:	4 Cores 32 GB (Dedicated)
        # - **mysql.x2.xlarge.25**:	8 Cores 16 GB (Dedicated)
        # - **mysql.x4.xlarge.25**:	8 Cores 32 GB (Dedicated)
        # - **mysql.x8.xlarge.25**:	8 Cores 64 GB (Dedicated)
        # - **mysql.x2.2xlarge.25**:	16 Cores 32 GB (Dedicated)
        # - **mysql.x4.2xlarge.25**:	16 Cores 64 GB (Dedicated)
        # - **mysql.x8.2xlarge.25**:	16 Cores 128 GB (Dedicated)
        # - **mysql.x4.4xlarge.25**:	32 Cores 128 GB (Dedicated)
        # - **mysql.x8.4xlarge.25**:	32 Cores 256 GB (Dedicated)
        # - **mysql.x4.8xlarge.25**:	64 Cores 256 GB (Dedicated)
        # - **mysql.x8.8xlarge.25**:	64 Cores 512 GB (Dedicated)
        # - **mysql.st.12xlarge.25**:	90 Cores 720 GB (Dedicated)
        # 
        # Standard Edition cloud disk specifications:
        # - **polarx.mysql.n2.medium.c25**:	2 Cores 4 GB (General Purpose)
        # - **polarx.mysql.n4.medium.c25**:	2 Cores 8 GB (General Purpose)
        # - **polarx.mysql.n8.medium.c25**:	2 Cores 16 GB (General Purpose)
        # - **polarx.mysql.n2.large.c25**:	4 Cores 8 GB (General Purpose)
        # - **polarx.mysql.n4.large.c25**:	4 Cores 16 GB (General Purpose)
        # - **polarx.mysql.n8.large.c25**:	4 Cores 32 GB (General Purpose)
        # - **polarx.mysql.n2.xlarge.c25**:	8 Cores 16 GB (General Purpose)
        # - **polarx.mysql.n4.xlarge.c25**:	8 Cores 32 GB (General Purpose)
        # - **polarx.mysql.n8.xlarge.c25**:	8 Cores 64 GB (General Purpose)
        # - **polarx.mysql.x2.medium.c25**:	2 Cores 4 GB (Dedicated)
        # - **polarx.mysql.x4.medium.c25**:	2 Cores 8 GB (Dedicated)
        # - **polarx.mysql.x8.medium.c25**:	2 Cores 16 GB (Dedicated)
        # - **polarx.mysql.x2.large.c25**:	4 Cores 8 GB (Dedicated)
        # - **polarx.mysql.x4.large.c25**:	4 Cores 16 GB (Dedicated)
        # - **polarx.mysql.x8.large.c25**:	4 Cores 32 GB (Dedicated)
        # - **polarx.mysql.x2.xlarge.c25**:	8 Cores 16 GB (Dedicated)
        # - **polarx.mysql.x4.xlarge.c25**:	8 Cores 32 GB (Dedicated)
        # - **polarx.mysql.x8.xlarge.c25**:	8 Cores 64 GB (Dedicated)
        # - **polarx.mysql.x2.2xlarge.c25**:	16 Cores 32 GB (Dedicated)
        # - **polarx.mysql.x4.2xlarge.c25**:	16 Cores 64 GB (Dedicated)
        # - **polarx.mysql.x8.2xlarge.c25**:	16 Cores 128 GB (Dedicated)
        # - **polarx.mysql.x2.4xlarge.c25**:	32 Cores 64 GB (Dedicated)
        # - **polarx.mysql.x4.4xlarge.c25**:	32 Cores 128 GB (Dedicated)
        # - **polarx.mysql.x8.4xlarge.c25**:	32 Cores 256 GB (Dedicated)
        # - **polarx.mysql.x2.8xlarge.c25**:	64 Cores 128 GB (Dedicated)
        # - **polarx.mysql.x4.8xlarge.c25**:	64 Cores 256 GB (Dedicated)
        # - **polarx.mysql.x8.8xlarge.c25**:	64 Cores 512 GB (Dedicated)
        self.dbnode_class = dbnode_class
        # The number of instance nodes:
        # * Standard Edition: 1
        # * Enterprise Edition: >=2
        self.dbnode_count = dbnode_count
        # The number of storage nodes.
        self.dnnode_count = dnnode_count
        # The description of the database.
        self.description = description
        # The storage node specification. Required for creating Enterprise Edition instances. Not required for Standard Edition.
        # 
        # Enterprise Edition local disk:
        # 
        # - **mysql.n2.medium.25**:	2 Cores 4 GB (General Purpose)
        # - **mysql.n4.medium.25**:	2 Cores 8 GB (General Purpose)
        # - **mysql.n2.large.25**:	4 Cores 8 GB (General Purpose)
        # - **mysql.n4.large.25**:	4 Cores 16 GB (General Purpose)
        # - **mysql.n4.xlarge.25**:	8 Cores 32 GB (General Purpose)
        # - **mysql.n4.2xlarge.25**:	16 Cores 64 GB (General Purpose)
        # - **mysql.x4.large.25**:	4 Cores 16 GB (Dedicated)
        # - **mysql.x8.large.25**:	4 Cores 32 GB (Dedicated)
        # - **mysql.x2.xlarge.25**:	8 Cores 16 GB (Dedicated)
        # - **mysql.x8.xlarge.25**:	8 Cores 64 GB (Dedicated)
        # - **mysql.x8.2xlarge.25**:	16 Cores 128 GB (Dedicated)
        # - **mysql.x4.4xlarge.25**:	32 Cores 128 GB (Dedicated)
        # - **mysql.x8.4xlarge.25**:	32 Cores 256 GB (Dedicated)
        # - **mysql.st.8xlarge.25**:	60 Cores 470 GB (Dedicated)
        # - **mysql.st.12xlarge.25**:	90 Cores 720 GB (Dedicated)
        # - **mysql.x8.45xlarge.25**:	180 Cores 1440 GB (Dedicated)
        # - **mysql.x8.60xlarge.25**:	240 Cores 1920 GB (Dedicated)
        # 
        # 
        # Enterprise Edition cloud disk:
        # 
        # - **polarx.mysql.n2.medium.c25**:	2 Cores 4 GB (General Purpose)
        # - **polarx.mysql.n4.medium.c25**:	2 Cores 8 GB (General Purpose)
        # - **polarx.mysql.n2.large.c25**:	4 Cores 8 GB (General Purpose)
        # - **polarx.mysql.n4.large.c25**:	4 Cores 16 GB (General Purpose)
        # - **polarx.mysql.n4.xlarge.c25**:	8 Cores 32 GB (General Purpose)
        # - **polarx.mysql.n4.2xlarge.c25**:	16 Cores 64 GB (General Purpose)
        # - **polarx.mysql.x4.large.c25**:	4 Cores 16 GB (Dedicated)
        # - **polarx.mysql.x8.large.c25**:	4 Cores 32 GB (Dedicated)
        # - **polarx.mysql.x2.xlarge.c25**:	8 Cores 16 GB (Dedicated)
        # - **polarx.mysql.x8.xlarge.c25**:	8 Cores 64 GB (Dedicated)
        # - **polarx.mysql.x8.2xlarge.c25**:	16 Cores 128 GB (Dedicated)
        # - **polarx.mysql.x4.4xlarge.c25**:	32 Cores 128 GB (Dedicated)
        # - **polarx.mysql.x8.4xlarge.c25**:	32 Cores 256 GB (Dedicated)
        # - **polarx.mysql.st.8xlarge.c25**:	60 Cores 470 GB (Dedicated)
        # - **polarx.mysql.st.12xlarge.c25**: 90 Cores 720 GB (Dedicated)
        # - **polarx.mysql.x8.45xlarge.c25**: 180 Cores 1440 GB (Dedicated)
        # - **polarx.mysql.x8.60xlarge.c25**: 240 Cores 1920 GB (Dedicated)
        self.dn_class = dn_class
        # The disk space size of the storage node.
        self.dn_storage_space = dn_storage_space
        # The MySQL engine version. Valid values: 5.7 and 8.0.
        # 
        # This parameter is required.
        self.engine_version = engine_version
        # Additional parameters.
        self.extra_params_shrink = extra_params_shrink
        # Specifies whether the instance to be created is a columnar read-only instance.
        self.is_columnar_read_dbinstance = is_columnar_read_dbinstance
        # Specifies whether the instance is a read-only instance.
        # 
        # - **true**: Yes
        # - **false**: No
        self.is_read_dbinstance = is_read_dbinstance
        # The network type. Only VPC is supported.
        self.network_type = network_type
        # The minor version number. This parameter is generally not required.
        self.origin_minor_version = origin_minor_version
        # The billing method of the instance.
        # 
        # - **PREPAY**: Subscription
        # - **POSTPAY**: Pay-as-you-go
        # 
        # This parameter is required.
        self.pay_type = pay_type
        # The billing cycle. For subscription instances, valid values are Year and Month. For pay-as-you-go instances, the default value is Hour.
        self.period = period
        # The primary instance must be specified if the instance is a read-only instance.
        self.primary_dbinstance_name = primary_dbinstance_name
        # The primary availability zone.
        self.primary_zone = primary_zone
        # The region where the instance resides.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group ID. This parameter can be left empty. This feature is currently not supported.
        self.resource_group_id = resource_group_id
        # The secondary availability zone.
        self.secondary_zone = secondary_zone
        # Enterprise Edition: enterprise
        # Standard Edition: standard
        self.series = series
        # The storage type.
        # * Local disk: custom_local_ssd
        # * Cloud disk: cloud_auto
        self.storage_type = storage_type
        # The tertiary availability zone.
        self.tertiary_zone = tertiary_zone
        # The topology type:
        # 
        # - **3azones**: Three availability zones
        # - **1azone**: Single availability zone
        # 
        # This parameter is required.
        self.topology_type = topology_type
        # The subscription duration. You can specify the number of months or years for prepaid instances.
        # 
        # > When Period is set to Year, valid values for this parameter are 1, 2, and 3.
        self.used_time = used_time
        # The VPC ID.
        self.vpcid = vpcid
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The availability zone of the instance.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.cnnode_count is not None:
            result['CNNodeCount'] = self.cnnode_count

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.cn_class is not None:
            result['CnClass'] = self.cn_class

        if self.dbnode_class is not None:
            result['DBNodeClass'] = self.dbnode_class

        if self.dbnode_count is not None:
            result['DBNodeCount'] = self.dbnode_count

        if self.dnnode_count is not None:
            result['DNNodeCount'] = self.dnnode_count

        if self.description is not None:
            result['Description'] = self.description

        if self.dn_class is not None:
            result['DnClass'] = self.dn_class

        if self.dn_storage_space is not None:
            result['DnStorageSpace'] = self.dn_storage_space

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.extra_params_shrink is not None:
            result['ExtraParams'] = self.extra_params_shrink

        if self.is_columnar_read_dbinstance is not None:
            result['IsColumnarReadDBInstance'] = self.is_columnar_read_dbinstance

        if self.is_read_dbinstance is not None:
            result['IsReadDBInstance'] = self.is_read_dbinstance

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.origin_minor_version is not None:
            result['OriginMinorVersion'] = self.origin_minor_version

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.period is not None:
            result['Period'] = self.period

        if self.primary_dbinstance_name is not None:
            result['PrimaryDBInstanceName'] = self.primary_dbinstance_name

        if self.primary_zone is not None:
            result['PrimaryZone'] = self.primary_zone

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.secondary_zone is not None:
            result['SecondaryZone'] = self.secondary_zone

        if self.series is not None:
            result['Series'] = self.series

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        if self.tertiary_zone is not None:
            result['TertiaryZone'] = self.tertiary_zone

        if self.topology_type is not None:
            result['TopologyType'] = self.topology_type

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
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('CNNodeCount') is not None:
            self.cnnode_count = m.get('CNNodeCount')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('CnClass') is not None:
            self.cn_class = m.get('CnClass')

        if m.get('DBNodeClass') is not None:
            self.dbnode_class = m.get('DBNodeClass')

        if m.get('DBNodeCount') is not None:
            self.dbnode_count = m.get('DBNodeCount')

        if m.get('DNNodeCount') is not None:
            self.dnnode_count = m.get('DNNodeCount')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DnClass') is not None:
            self.dn_class = m.get('DnClass')

        if m.get('DnStorageSpace') is not None:
            self.dn_storage_space = m.get('DnStorageSpace')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('ExtraParams') is not None:
            self.extra_params_shrink = m.get('ExtraParams')

        if m.get('IsColumnarReadDBInstance') is not None:
            self.is_columnar_read_dbinstance = m.get('IsColumnarReadDBInstance')

        if m.get('IsReadDBInstance') is not None:
            self.is_read_dbinstance = m.get('IsReadDBInstance')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('OriginMinorVersion') is not None:
            self.origin_minor_version = m.get('OriginMinorVersion')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PrimaryDBInstanceName') is not None:
            self.primary_dbinstance_name = m.get('PrimaryDBInstanceName')

        if m.get('PrimaryZone') is not None:
            self.primary_zone = m.get('PrimaryZone')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SecondaryZone') is not None:
            self.secondary_zone = m.get('SecondaryZone')

        if m.get('Series') is not None:
            self.series = m.get('Series')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        if m.get('TertiaryZone') is not None:
            self.tertiary_zone = m.get('TertiaryZone')

        if m.get('TopologyType') is not None:
            self.topology_type = m.get('TopologyType')

        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')

        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

