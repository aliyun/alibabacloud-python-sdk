# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class CreateApsSlsADBJobRequest(DaraModel):
    def __init__(
        self,
        across_role: str = None,
        across_uid: str = None,
        advanced_config: str = None,
        columns: List[main_models.CreateApsSlsADBJobRequestColumns] = None,
        dbcluster_id: str = None,
        datasource_id: int = None,
        db_name: str = None,
        dirty_data_handle_mode: str = None,
        dirty_data_process_pattern: str = None,
        exactly_once: str = None,
        full_compute_unit: str = None,
        hudi_advanced_config: str = None,
        incremental_compute_unit: str = None,
        lakehouse_id: int = None,
        max_offsets_per_trigger: int = None,
        oss_location: str = None,
        output_format: str = None,
        partition_specs: List[Dict[str, Any]] = None,
        password: str = None,
        primary_key_definition: str = None,
        project: str = None,
        region_id: str = None,
        resource_group: str = None,
        source_region_id: str = None,
        starting_offsets: str = None,
        store: str = None,
        table_name: str = None,
        target_generate_rule: str = None,
        target_type: str = None,
        unix_timestamp_convert: main_models.CreateApsSlsADBJobRequestUnixTimestampConvert = None,
        user_name: str = None,
        workload_name: str = None,
    ):
        # The name of the cross-account role.
        self.across_role = across_role
        # The cross-account UID.
        self.across_uid = across_uid
        # The advanced configurations.
        self.advanced_config = advanced_config
        # The information about columns.
        # 
        # This parameter is required.
        self.columns = columns
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The data source ID.
        self.datasource_id = datasource_id
        # The name of the database.
        # 
        # This parameter is required.
        self.db_name = db_name
        # The dirty data processing mode.
        # 
        # This parameter is required.
        self.dirty_data_handle_mode = dirty_data_handle_mode
        # The dirty data processing mode.
        self.dirty_data_process_pattern = dirty_data_process_pattern
        # Specifies whether to enable the consistency check.
        self.exactly_once = exactly_once
        # The number of full AnalyticDB compute units (ACUs).
        self.full_compute_unit = full_compute_unit
        # The advanced configurations of Hudi.
        self.hudi_advanced_config = hudi_advanced_config
        # The number of increment ACUs.
        self.incremental_compute_unit = incremental_compute_unit
        # The lakehouse ID.
        self.lakehouse_id = lakehouse_id
        # The latest offset.
        self.max_offsets_per_trigger = max_offsets_per_trigger
        # The Object Storage Service (OSS) URL.
        self.oss_location = oss_location
        # The format of the output file.
        self.output_format = output_format
        # The information about partition.
        self.partition_specs = partition_specs
        # The password of the database account.
        # 
        # This parameter is required.
        self.password = password
        # The definition of the primary key.
        self.primary_key_definition = primary_key_definition
        # The name of the SLS project.
        self.project = project
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The name of the resource group.
        self.resource_group = resource_group
        # The region ID of the source cluster.
        self.source_region_id = source_region_id
        # The start offset.
        # 
        # This parameter is required.
        self.starting_offsets = starting_offsets
        # The SLS Logstore.
        self.store = store
        # The name of the table.
        # 
        # This parameter is required.
        self.table_name = table_name
        # The rules for generating the destination database.
        self.target_generate_rule = target_generate_rule
        # The destination type.
        self.target_type = target_type
        # The timestamp conversion.
        self.unix_timestamp_convert = unix_timestamp_convert
        # The name of the database account.
        # 
        # This parameter is required.
        self.user_name = user_name
        # The name of the workload.
        # 
        # This parameter is required.
        self.workload_name = workload_name

    def validate(self):
        if self.columns:
            for v1 in self.columns:
                 if v1:
                    v1.validate()
        if self.unix_timestamp_convert:
            self.unix_timestamp_convert.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.across_role is not None:
            result['AcrossRole'] = self.across_role

        if self.across_uid is not None:
            result['AcrossUid'] = self.across_uid

        if self.advanced_config is not None:
            result['AdvancedConfig'] = self.advanced_config

        result['Columns'] = []
        if self.columns is not None:
            for k1 in self.columns:
                result['Columns'].append(k1.to_map() if k1 else None)

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.datasource_id is not None:
            result['DatasourceId'] = self.datasource_id

        if self.db_name is not None:
            result['DbName'] = self.db_name

        if self.dirty_data_handle_mode is not None:
            result['DirtyDataHandleMode'] = self.dirty_data_handle_mode

        if self.dirty_data_process_pattern is not None:
            result['DirtyDataProcessPattern'] = self.dirty_data_process_pattern

        if self.exactly_once is not None:
            result['ExactlyOnce'] = self.exactly_once

        if self.full_compute_unit is not None:
            result['FullComputeUnit'] = self.full_compute_unit

        if self.hudi_advanced_config is not None:
            result['HudiAdvancedConfig'] = self.hudi_advanced_config

        if self.incremental_compute_unit is not None:
            result['IncrementalComputeUnit'] = self.incremental_compute_unit

        if self.lakehouse_id is not None:
            result['LakehouseId'] = self.lakehouse_id

        if self.max_offsets_per_trigger is not None:
            result['MaxOffsetsPerTrigger'] = self.max_offsets_per_trigger

        if self.oss_location is not None:
            result['OssLocation'] = self.oss_location

        if self.output_format is not None:
            result['OutputFormat'] = self.output_format

        if self.partition_specs is not None:
            result['PartitionSpecs'] = self.partition_specs

        if self.password is not None:
            result['Password'] = self.password

        if self.primary_key_definition is not None:
            result['PrimaryKeyDefinition'] = self.primary_key_definition

        if self.project is not None:
            result['Project'] = self.project

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group is not None:
            result['ResourceGroup'] = self.resource_group

        if self.source_region_id is not None:
            result['SourceRegionId'] = self.source_region_id

        if self.starting_offsets is not None:
            result['StartingOffsets'] = self.starting_offsets

        if self.store is not None:
            result['Store'] = self.store

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.target_generate_rule is not None:
            result['TargetGenerateRule'] = self.target_generate_rule

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        if self.unix_timestamp_convert is not None:
            result['UnixTimestampConvert'] = self.unix_timestamp_convert.to_map()

        if self.user_name is not None:
            result['UserName'] = self.user_name

        if self.workload_name is not None:
            result['WorkloadName'] = self.workload_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcrossRole') is not None:
            self.across_role = m.get('AcrossRole')

        if m.get('AcrossUid') is not None:
            self.across_uid = m.get('AcrossUid')

        if m.get('AdvancedConfig') is not None:
            self.advanced_config = m.get('AdvancedConfig')

        self.columns = []
        if m.get('Columns') is not None:
            for k1 in m.get('Columns'):
                temp_model = main_models.CreateApsSlsADBJobRequestColumns()
                self.columns.append(temp_model.from_map(k1))

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DatasourceId') is not None:
            self.datasource_id = m.get('DatasourceId')

        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')

        if m.get('DirtyDataHandleMode') is not None:
            self.dirty_data_handle_mode = m.get('DirtyDataHandleMode')

        if m.get('DirtyDataProcessPattern') is not None:
            self.dirty_data_process_pattern = m.get('DirtyDataProcessPattern')

        if m.get('ExactlyOnce') is not None:
            self.exactly_once = m.get('ExactlyOnce')

        if m.get('FullComputeUnit') is not None:
            self.full_compute_unit = m.get('FullComputeUnit')

        if m.get('HudiAdvancedConfig') is not None:
            self.hudi_advanced_config = m.get('HudiAdvancedConfig')

        if m.get('IncrementalComputeUnit') is not None:
            self.incremental_compute_unit = m.get('IncrementalComputeUnit')

        if m.get('LakehouseId') is not None:
            self.lakehouse_id = m.get('LakehouseId')

        if m.get('MaxOffsetsPerTrigger') is not None:
            self.max_offsets_per_trigger = m.get('MaxOffsetsPerTrigger')

        if m.get('OssLocation') is not None:
            self.oss_location = m.get('OssLocation')

        if m.get('OutputFormat') is not None:
            self.output_format = m.get('OutputFormat')

        if m.get('PartitionSpecs') is not None:
            self.partition_specs = m.get('PartitionSpecs')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('PrimaryKeyDefinition') is not None:
            self.primary_key_definition = m.get('PrimaryKeyDefinition')

        if m.get('Project') is not None:
            self.project = m.get('Project')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroup') is not None:
            self.resource_group = m.get('ResourceGroup')

        if m.get('SourceRegionId') is not None:
            self.source_region_id = m.get('SourceRegionId')

        if m.get('StartingOffsets') is not None:
            self.starting_offsets = m.get('StartingOffsets')

        if m.get('Store') is not None:
            self.store = m.get('Store')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('TargetGenerateRule') is not None:
            self.target_generate_rule = m.get('TargetGenerateRule')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        if m.get('UnixTimestampConvert') is not None:
            temp_model = main_models.CreateApsSlsADBJobRequestUnixTimestampConvert()
            self.unix_timestamp_convert = temp_model.from_map(m.get('UnixTimestampConvert'))

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        if m.get('WorkloadName') is not None:
            self.workload_name = m.get('WorkloadName')

        return self

class CreateApsSlsADBJobRequestUnixTimestampConvert(DaraModel):
    def __init__(
        self,
        convert: str = None,
        format: str = None,
        transform: bool = None,
    ):
        # Specifies whether to enable the conversion of timestamps.
        self.convert = convert
        # The format of the timestamp.
        self.format = format
        # Specifies whether to enable the timestamp conversion.
        self.transform = transform

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.convert is not None:
            result['Convert'] = self.convert

        if self.format is not None:
            result['Format'] = self.format

        if self.transform is not None:
            result['Transform'] = self.transform

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Convert') is not None:
            self.convert = m.get('Convert')

        if m.get('Format') is not None:
            self.format = m.get('Format')

        if m.get('Transform') is not None:
            self.transform = m.get('Transform')

        return self

class CreateApsSlsADBJobRequestColumns(DaraModel):
    def __init__(
        self,
        map_name: str = None,
        map_type: str = None,
        name: str = None,
        type: str = None,
    ):
        # The name of the mapping.
        self.map_name = map_name
        # The type of the mapping.
        self.map_type = map_type
        # The name of the column.
        self.name = name
        # The data type of the column.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.map_name is not None:
            result['MapName'] = self.map_name

        if self.map_type is not None:
            result['MapType'] = self.map_type

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MapName') is not None:
            self.map_name = m.get('MapName')

        if m.get('MapType') is not None:
            self.map_type = m.get('MapType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

