# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDifyInstanceRequest(DaraModel):
    def __init__(
        self,
        adbpg_instance_mode: str = None,
        backup_vswitch_id: str = None,
        client_token: str = None,
        data_region: str = None,
        database_option: str = None,
        db_engine_type: str = None,
        db_engine_version: str = None,
        db_instance_account: str = None,
        db_instance_category: str = None,
        db_instance_class: str = None,
        db_instance_password: str = None,
        db_resource_id: int = None,
        db_storage_size: str = None,
        db_storage_type: str = None,
        dry_run: bool = None,
        edition: str = None,
        enable_extra_endpoint: bool = None,
        gpu_node_spec: str = None,
        kv_store_account: str = None,
        kv_store_engine_version: str = None,
        kv_store_instance_class: str = None,
        kv_store_node_type: str = None,
        kv_store_option: str = None,
        kv_store_password: str = None,
        kv_store_resource_id: int = None,
        kv_store_type: str = None,
        major_version: str = None,
        model_id: str = None,
        model_option: str = None,
        nat_gateway_option: str = None,
        only_intranet: bool = None,
        oss_path: str = None,
        oss_resource_id: int = None,
        pay_period: int = None,
        pay_period_type: str = None,
        pay_type: str = None,
        replicas: int = None,
        resource_quota: str = None,
        security_group_id: str = None,
        seg_disk_performance_level: str = None,
        seg_node_num: int = None,
        storage_type: str = None,
        v_switch_id: str = None,
        vectordb_account: str = None,
        vectordb_category: str = None,
        vectordb_engine_version: str = None,
        vectordb_instance_spec: str = None,
        vectordb_option: str = None,
        vectordb_password: str = None,
        vectordb_resource_id: int = None,
        vectordb_storage_size: str = None,
        vectordb_storage_type: str = None,
        vectordb_type: str = None,
        vpc_id: str = None,
        workspace_description: str = None,
        workspace_id: str = None,
        workspace_name: str = None,
        workspace_option: str = None,
        zone_id: str = None,
    ):
        self.adbpg_instance_mode = adbpg_instance_mode
        self.backup_vswitch_id = backup_vswitch_id
        self.client_token = client_token
        # This parameter is required.
        self.data_region = data_region
        self.database_option = database_option
        self.db_engine_type = db_engine_type
        self.db_engine_version = db_engine_version
        self.db_instance_account = db_instance_account
        self.db_instance_category = db_instance_category
        self.db_instance_class = db_instance_class
        self.db_instance_password = db_instance_password
        self.db_resource_id = db_resource_id
        self.db_storage_size = db_storage_size
        self.db_storage_type = db_storage_type
        self.dry_run = dry_run
        self.edition = edition
        self.enable_extra_endpoint = enable_extra_endpoint
        self.gpu_node_spec = gpu_node_spec
        self.kv_store_account = kv_store_account
        self.kv_store_engine_version = kv_store_engine_version
        self.kv_store_instance_class = kv_store_instance_class
        self.kv_store_node_type = kv_store_node_type
        self.kv_store_option = kv_store_option
        self.kv_store_password = kv_store_password
        self.kv_store_resource_id = kv_store_resource_id
        self.kv_store_type = kv_store_type
        self.major_version = major_version
        self.model_id = model_id
        self.model_option = model_option
        self.nat_gateway_option = nat_gateway_option
        self.only_intranet = only_intranet
        self.oss_path = oss_path
        self.oss_resource_id = oss_resource_id
        self.pay_period = pay_period
        self.pay_period_type = pay_period_type
        self.pay_type = pay_type
        self.replicas = replicas
        # This parameter is required.
        self.resource_quota = resource_quota
        # This parameter is required.
        self.security_group_id = security_group_id
        self.seg_disk_performance_level = seg_disk_performance_level
        self.seg_node_num = seg_node_num
        self.storage_type = storage_type
        # This parameter is required.
        self.v_switch_id = v_switch_id
        self.vectordb_account = vectordb_account
        self.vectordb_category = vectordb_category
        self.vectordb_engine_version = vectordb_engine_version
        self.vectordb_instance_spec = vectordb_instance_spec
        self.vectordb_option = vectordb_option
        self.vectordb_password = vectordb_password
        self.vectordb_resource_id = vectordb_resource_id
        self.vectordb_storage_size = vectordb_storage_size
        self.vectordb_storage_type = vectordb_storage_type
        self.vectordb_type = vectordb_type
        # This parameter is required.
        self.vpc_id = vpc_id
        self.workspace_description = workspace_description
        self.workspace_id = workspace_id
        self.workspace_name = workspace_name
        self.workspace_option = workspace_option
        # This parameter is required.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.adbpg_instance_mode is not None:
            result['AdbpgInstanceMode'] = self.adbpg_instance_mode

        if self.backup_vswitch_id is not None:
            result['BackupVSwitchId'] = self.backup_vswitch_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.data_region is not None:
            result['DataRegion'] = self.data_region

        if self.database_option is not None:
            result['DatabaseOption'] = self.database_option

        if self.db_engine_type is not None:
            result['DbEngineType'] = self.db_engine_type

        if self.db_engine_version is not None:
            result['DbEngineVersion'] = self.db_engine_version

        if self.db_instance_account is not None:
            result['DbInstanceAccount'] = self.db_instance_account

        if self.db_instance_category is not None:
            result['DbInstanceCategory'] = self.db_instance_category

        if self.db_instance_class is not None:
            result['DbInstanceClass'] = self.db_instance_class

        if self.db_instance_password is not None:
            result['DbInstancePassword'] = self.db_instance_password

        if self.db_resource_id is not None:
            result['DbResourceId'] = self.db_resource_id

        if self.db_storage_size is not None:
            result['DbStorageSize'] = self.db_storage_size

        if self.db_storage_type is not None:
            result['DbStorageType'] = self.db_storage_type

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.edition is not None:
            result['Edition'] = self.edition

        if self.enable_extra_endpoint is not None:
            result['EnableExtraEndpoint'] = self.enable_extra_endpoint

        if self.gpu_node_spec is not None:
            result['GpuNodeSpec'] = self.gpu_node_spec

        if self.kv_store_account is not None:
            result['KvStoreAccount'] = self.kv_store_account

        if self.kv_store_engine_version is not None:
            result['KvStoreEngineVersion'] = self.kv_store_engine_version

        if self.kv_store_instance_class is not None:
            result['KvStoreInstanceClass'] = self.kv_store_instance_class

        if self.kv_store_node_type is not None:
            result['KvStoreNodeType'] = self.kv_store_node_type

        if self.kv_store_option is not None:
            result['KvStoreOption'] = self.kv_store_option

        if self.kv_store_password is not None:
            result['KvStorePassword'] = self.kv_store_password

        if self.kv_store_resource_id is not None:
            result['KvStoreResourceId'] = self.kv_store_resource_id

        if self.kv_store_type is not None:
            result['KvStoreType'] = self.kv_store_type

        if self.major_version is not None:
            result['MajorVersion'] = self.major_version

        if self.model_id is not None:
            result['ModelId'] = self.model_id

        if self.model_option is not None:
            result['ModelOption'] = self.model_option

        if self.nat_gateway_option is not None:
            result['NatGatewayOption'] = self.nat_gateway_option

        if self.only_intranet is not None:
            result['OnlyIntranet'] = self.only_intranet

        if self.oss_path is not None:
            result['OssPath'] = self.oss_path

        if self.oss_resource_id is not None:
            result['OssResourceId'] = self.oss_resource_id

        if self.pay_period is not None:
            result['PayPeriod'] = self.pay_period

        if self.pay_period_type is not None:
            result['PayPeriodType'] = self.pay_period_type

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.replicas is not None:
            result['Replicas'] = self.replicas

        if self.resource_quota is not None:
            result['ResourceQuota'] = self.resource_quota

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.seg_disk_performance_level is not None:
            result['SegDiskPerformanceLevel'] = self.seg_disk_performance_level

        if self.seg_node_num is not None:
            result['SegNodeNum'] = self.seg_node_num

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vectordb_account is not None:
            result['VectordbAccount'] = self.vectordb_account

        if self.vectordb_category is not None:
            result['VectordbCategory'] = self.vectordb_category

        if self.vectordb_engine_version is not None:
            result['VectordbEngineVersion'] = self.vectordb_engine_version

        if self.vectordb_instance_spec is not None:
            result['VectordbInstanceSpec'] = self.vectordb_instance_spec

        if self.vectordb_option is not None:
            result['VectordbOption'] = self.vectordb_option

        if self.vectordb_password is not None:
            result['VectordbPassword'] = self.vectordb_password

        if self.vectordb_resource_id is not None:
            result['VectordbResourceId'] = self.vectordb_resource_id

        if self.vectordb_storage_size is not None:
            result['VectordbStorageSize'] = self.vectordb_storage_size

        if self.vectordb_storage_type is not None:
            result['VectordbStorageType'] = self.vectordb_storage_type

        if self.vectordb_type is not None:
            result['VectordbType'] = self.vectordb_type

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.workspace_description is not None:
            result['WorkspaceDescription'] = self.workspace_description

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name

        if self.workspace_option is not None:
            result['WorkspaceOption'] = self.workspace_option

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdbpgInstanceMode') is not None:
            self.adbpg_instance_mode = m.get('AdbpgInstanceMode')

        if m.get('BackupVSwitchId') is not None:
            self.backup_vswitch_id = m.get('BackupVSwitchId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DataRegion') is not None:
            self.data_region = m.get('DataRegion')

        if m.get('DatabaseOption') is not None:
            self.database_option = m.get('DatabaseOption')

        if m.get('DbEngineType') is not None:
            self.db_engine_type = m.get('DbEngineType')

        if m.get('DbEngineVersion') is not None:
            self.db_engine_version = m.get('DbEngineVersion')

        if m.get('DbInstanceAccount') is not None:
            self.db_instance_account = m.get('DbInstanceAccount')

        if m.get('DbInstanceCategory') is not None:
            self.db_instance_category = m.get('DbInstanceCategory')

        if m.get('DbInstanceClass') is not None:
            self.db_instance_class = m.get('DbInstanceClass')

        if m.get('DbInstancePassword') is not None:
            self.db_instance_password = m.get('DbInstancePassword')

        if m.get('DbResourceId') is not None:
            self.db_resource_id = m.get('DbResourceId')

        if m.get('DbStorageSize') is not None:
            self.db_storage_size = m.get('DbStorageSize')

        if m.get('DbStorageType') is not None:
            self.db_storage_type = m.get('DbStorageType')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('Edition') is not None:
            self.edition = m.get('Edition')

        if m.get('EnableExtraEndpoint') is not None:
            self.enable_extra_endpoint = m.get('EnableExtraEndpoint')

        if m.get('GpuNodeSpec') is not None:
            self.gpu_node_spec = m.get('GpuNodeSpec')

        if m.get('KvStoreAccount') is not None:
            self.kv_store_account = m.get('KvStoreAccount')

        if m.get('KvStoreEngineVersion') is not None:
            self.kv_store_engine_version = m.get('KvStoreEngineVersion')

        if m.get('KvStoreInstanceClass') is not None:
            self.kv_store_instance_class = m.get('KvStoreInstanceClass')

        if m.get('KvStoreNodeType') is not None:
            self.kv_store_node_type = m.get('KvStoreNodeType')

        if m.get('KvStoreOption') is not None:
            self.kv_store_option = m.get('KvStoreOption')

        if m.get('KvStorePassword') is not None:
            self.kv_store_password = m.get('KvStorePassword')

        if m.get('KvStoreResourceId') is not None:
            self.kv_store_resource_id = m.get('KvStoreResourceId')

        if m.get('KvStoreType') is not None:
            self.kv_store_type = m.get('KvStoreType')

        if m.get('MajorVersion') is not None:
            self.major_version = m.get('MajorVersion')

        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')

        if m.get('ModelOption') is not None:
            self.model_option = m.get('ModelOption')

        if m.get('NatGatewayOption') is not None:
            self.nat_gateway_option = m.get('NatGatewayOption')

        if m.get('OnlyIntranet') is not None:
            self.only_intranet = m.get('OnlyIntranet')

        if m.get('OssPath') is not None:
            self.oss_path = m.get('OssPath')

        if m.get('OssResourceId') is not None:
            self.oss_resource_id = m.get('OssResourceId')

        if m.get('PayPeriod') is not None:
            self.pay_period = m.get('PayPeriod')

        if m.get('PayPeriodType') is not None:
            self.pay_period_type = m.get('PayPeriodType')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('Replicas') is not None:
            self.replicas = m.get('Replicas')

        if m.get('ResourceQuota') is not None:
            self.resource_quota = m.get('ResourceQuota')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('SegDiskPerformanceLevel') is not None:
            self.seg_disk_performance_level = m.get('SegDiskPerformanceLevel')

        if m.get('SegNodeNum') is not None:
            self.seg_node_num = m.get('SegNodeNum')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VectordbAccount') is not None:
            self.vectordb_account = m.get('VectordbAccount')

        if m.get('VectordbCategory') is not None:
            self.vectordb_category = m.get('VectordbCategory')

        if m.get('VectordbEngineVersion') is not None:
            self.vectordb_engine_version = m.get('VectordbEngineVersion')

        if m.get('VectordbInstanceSpec') is not None:
            self.vectordb_instance_spec = m.get('VectordbInstanceSpec')

        if m.get('VectordbOption') is not None:
            self.vectordb_option = m.get('VectordbOption')

        if m.get('VectordbPassword') is not None:
            self.vectordb_password = m.get('VectordbPassword')

        if m.get('VectordbResourceId') is not None:
            self.vectordb_resource_id = m.get('VectordbResourceId')

        if m.get('VectordbStorageSize') is not None:
            self.vectordb_storage_size = m.get('VectordbStorageSize')

        if m.get('VectordbStorageType') is not None:
            self.vectordb_storage_type = m.get('VectordbStorageType')

        if m.get('VectordbType') is not None:
            self.vectordb_type = m.get('VectordbType')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('WorkspaceDescription') is not None:
            self.workspace_description = m.get('WorkspaceDescription')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')

        if m.get('WorkspaceOption') is not None:
            self.workspace_option = m.get('WorkspaceOption')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

