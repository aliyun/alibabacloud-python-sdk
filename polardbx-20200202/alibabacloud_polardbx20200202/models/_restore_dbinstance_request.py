# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RestoreDBInstanceRequest(DaraModel):
    def __init__(
        self,
        auto_renew: bool = None,
        backup_set_id: str = None,
        backup_set_region: str = None,
        cnnode_count: str = None,
        client_token: str = None,
        clone_instance_name: str = None,
        cn_class: str = None,
        dbnode_class: str = None,
        dbnode_count: int = None,
        dnnode_count: str = None,
        dn_class: str = None,
        engine_version: str = None,
        gdn_role: str = None,
        network_type: str = None,
        pay_type: str = None,
        period: str = None,
        primary_zone: str = None,
        recovery_type_code: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        restore_time: str = None,
        secondary_zone: str = None,
        series: str = None,
        source_instance_region: str = None,
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
        # - true: Enabled.
        # - false: Disabled.
        self.auto_renew = auto_renew
        # The backup set ID.
        self.backup_set_id = backup_set_id
        # The region where the backup set resides.
        # 
        # This parameter is required.
        self.backup_set_region = backup_set_region
        # The number of compute nodes.
        self.cnnode_count = cnnode_count
        # The client token used to ensure the idempotence of the request. Use a different value for each request.
        self.client_token = client_token
        # The name of the source instance.
        # 
        # This parameter is required.
        self.clone_instance_name = clone_instance_name
        # The compute node specifications. Valid values:
        # 
        # - polarx.x4.medium.2e: 2 cores, 8 GB
        # - polarx.x4.large.2e: 4 cores, 16 GB
        # - polarx.x8.large.2e: 4 cores, 32 GB
        # - polarx.x4.xlarge.2e: 8 cores, 32 GB
        # - polarx.x8.xlarge.2e: 8 cores, 64 GB
        # - polarx.x4.2xlarge.2e: 16 cores, 64 GB
        # - polarx.x8.2xlarge.2e: 16 cores, 128 GB
        # - polarx.x4.4xlarge.2e: 32 cores, 128 GB
        # - polarx.x8.4xlarge.2e: 32 cores, 256 GB
        # - polarx.st.8xlarge.2e: 60 cores, 470 GB
        # - polarx.st.12xlarge.2e: 90 cores, 720 GB
        self.cn_class = cn_class
        # The node specifications. Valid values:
        # 
        # - polarx.x4.medium.2e: 2 cores, 8 GB
        # - polarx.x4.large.2e: 4 cores, 16 GB
        # - polarx.x8.large.2e: 4 cores, 32 GB
        # - polarx.x4.xlarge.2e: 8 cores, 32 GB
        # - polarx.x8.xlarge.2e: 8 cores, 64 GB
        # - polarx.x4.2xlarge.2e: 16 cores, 64 GB
        # - polarx.x8.2xlarge.2e: 16 cores, 128 GB
        # - polarx.x4.4xlarge.2e: 32 cores, 128 GB
        # - polarx.x8.4xlarge.2e: 32 cores, 256 GB
        # - polarx.st.8xlarge.2e: 60 cores, 470 GB
        # - polarx.st.12xlarge.2e: 90 cores, 720 GB
        self.dbnode_class = dbnode_class
        # The number of instance nodes. The minimum value is 2.
        self.dbnode_count = dbnode_count
        # The number of storage nodes.
        self.dnnode_count = dnnode_count
        # The storage node specifications. Valid values:
        # 
        # - mysql.n4.medium.25: 2 cores, 8 GB
        # - mysql.n4.large.25: 4 cores, 16 GB
        # - mysql.x8.large.25: 4 cores, 32 GB
        # - mysql.n4.xlarge.25: 8 cores, 32 GB
        # - mysql.x8.xlarge.25: 8 cores, 64 GB
        # - mysql.n4.2xlarge.25: 16 cores, 64 GB
        # - mysql.x8.2xlarge.25: 16 cores, 128 GB
        # - mysql.x4.4xlarge.25: 32 cores, 128 GB
        # - mysql.x8.4xlarge.25: 32 cores, 256 GB
        # - mysql.st.8xlarge.25: 60 cores, 470 GB
        # - mysql.st.12xlarge.25: 90 cores, 720 GB
        self.dn_class = dn_class
        # The MySQL DPI engine version. Valid values: 5.7 and 8.0.
        # 
        # This parameter is required.
        self.engine_version = engine_version
        # The GDN role.
        self.gdn_role = gdn_role
        # The network type. Only VPC is supported.
        self.network_type = network_type
        # The billing method of the instance.
        # 
        # - PREPAY: subscription
        # - POSTPAY: pay-as-you-go
        # 
        # This parameter is required.
        self.pay_type = pay_type
        # The billing cycle. Valid values for subscription: Year and Month. Default value for pay-as-you-go: Hour.
        self.period = period
        # The primary zone.
        self.primary_zone = primary_zone
        # The recovery type.
        # 
        # This parameter is required.
        self.recovery_type_code = recovery_type_code
        # The region where the instance resides.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group ID. This parameter can be left empty. This parameter is not supported.
        self.resource_group_id = resource_group_id
        # The point in time to which you want to restore the instance. Specify the time in the yyyy-MM-ddTHH:mm:ssZ format (UTC).
        self.restore_time = restore_time
        # The secondary zone.
        self.secondary_zone = secondary_zone
        # The instance series. Valid values:
        # 
        # - enterprise: Enterprise Edition.
        # - standard: Standard Edition.
        self.series = series
        # The region where the source instance resides.
        # 
        # This parameter is required.
        self.source_instance_region = source_instance_region
        # The storage type.
        self.storage_type = storage_type
        # The zone for Three-zone deployment.
        self.tertiary_zone = tertiary_zone
        # The topology type. Valid values:
        # 
        # - 3azones: three-zone deployment.
        # - 1azone: single-zone deployment.
        # 
        # This parameter is required.
        self.topology_type = topology_type
        # The subscription duration. Specify the number of months or years.
        # 
        # > If Period is set to Year, valid values of this parameter are 1, 2, and 3.
        self.used_time = used_time
        # VPC ID。
        self.vpcid = vpcid
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The zone of the instance.
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

        if self.backup_set_id is not None:
            result['BackupSetId'] = self.backup_set_id

        if self.backup_set_region is not None:
            result['BackupSetRegion'] = self.backup_set_region

        if self.cnnode_count is not None:
            result['CNNodeCount'] = self.cnnode_count

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.clone_instance_name is not None:
            result['CloneInstanceName'] = self.clone_instance_name

        if self.cn_class is not None:
            result['CnClass'] = self.cn_class

        if self.dbnode_class is not None:
            result['DBNodeClass'] = self.dbnode_class

        if self.dbnode_count is not None:
            result['DBNodeCount'] = self.dbnode_count

        if self.dnnode_count is not None:
            result['DNNodeCount'] = self.dnnode_count

        if self.dn_class is not None:
            result['DnClass'] = self.dn_class

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.gdn_role is not None:
            result['GdnRole'] = self.gdn_role

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.period is not None:
            result['Period'] = self.period

        if self.primary_zone is not None:
            result['PrimaryZone'] = self.primary_zone

        if self.recovery_type_code is not None:
            result['RecoveryTypeCode'] = self.recovery_type_code

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.restore_time is not None:
            result['RestoreTime'] = self.restore_time

        if self.secondary_zone is not None:
            result['SecondaryZone'] = self.secondary_zone

        if self.series is not None:
            result['Series'] = self.series

        if self.source_instance_region is not None:
            result['SourceInstanceRegion'] = self.source_instance_region

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

        if m.get('BackupSetId') is not None:
            self.backup_set_id = m.get('BackupSetId')

        if m.get('BackupSetRegion') is not None:
            self.backup_set_region = m.get('BackupSetRegion')

        if m.get('CNNodeCount') is not None:
            self.cnnode_count = m.get('CNNodeCount')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('CloneInstanceName') is not None:
            self.clone_instance_name = m.get('CloneInstanceName')

        if m.get('CnClass') is not None:
            self.cn_class = m.get('CnClass')

        if m.get('DBNodeClass') is not None:
            self.dbnode_class = m.get('DBNodeClass')

        if m.get('DBNodeCount') is not None:
            self.dbnode_count = m.get('DBNodeCount')

        if m.get('DNNodeCount') is not None:
            self.dnnode_count = m.get('DNNodeCount')

        if m.get('DnClass') is not None:
            self.dn_class = m.get('DnClass')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('GdnRole') is not None:
            self.gdn_role = m.get('GdnRole')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PrimaryZone') is not None:
            self.primary_zone = m.get('PrimaryZone')

        if m.get('RecoveryTypeCode') is not None:
            self.recovery_type_code = m.get('RecoveryTypeCode')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('RestoreTime') is not None:
            self.restore_time = m.get('RestoreTime')

        if m.get('SecondaryZone') is not None:
            self.secondary_zone = m.get('SecondaryZone')

        if m.get('Series') is not None:
            self.series = m.get('Series')

        if m.get('SourceInstanceRegion') is not None:
            self.source_instance_region = m.get('SourceInstanceRegion')

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

