# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateApsKafkaHudiJobShrinkRequest(DaraModel):
    def __init__(
        self,
        across_role: str = None,
        across_uid: str = None,
        advanced_config: str = None,
        columns_shrink: str = None,
        dbcluster_id: str = None,
        data_format_type: str = None,
        data_output_format: str = None,
        datasource_id: int = None,
        db_name: str = None,
        full_compute_unit: str = None,
        hudi_advanced_config: str = None,
        incremental_compute_unit: str = None,
        json_parse_level: int = None,
        kafka_cluster_id: str = None,
        kafka_topic: str = None,
        lakehouse_id: int = None,
        max_offsets_per_trigger: int = None,
        oss_location: str = None,
        output_format: str = None,
        partition_specs_shrink: str = None,
        primary_key_definition: str = None,
        region_id: str = None,
        resource_group: str = None,
        source_region_id: str = None,
        starting_offsets: str = None,
        table_name: str = None,
        target_generate_rule: str = None,
        target_type: str = None,
        workload_name: str = None,
    ):
        # The RAM role of a trusted entity that is an Alibaba Cloud account. For more information about how to create a RAM role, see Create a RAM role for a trusted Alibaba Cloud account.
        # The Alibaba Cloud account that owns the AnalyticDB for MySQL cluster must be added as a trusted account to the RAM role.
        self.across_role = across_role
        # The ID of the Alibaba Cloud account to which the source Kafka instance belongs.
        self.across_uid = across_uid
        # The advanced configuration.
        self.advanced_config = advanced_config
        # The column information.
        # 
        # This parameter is required.
        self.columns_shrink = columns_shrink
        # The cluster ID.
        # 
        # > Call the [DescribeDBClusters](https://help.aliyun.com/document_detail/129857.html) operation to view the cluster IDs of all AnalyticDB for MySQL Data Lakehouse Edition (V3.0) clusters in the destination region.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The Kafka message type. Valid values: json, general_canal_json, mongo_canal_json, dataworks_json, and shareplex_json.
        self.data_format_type = data_format_type
        # The valid values and their descriptions are as follows:
        # Single: The source is a single-line JSON record.
        # Multi: The source is a JSON array. A single JSON record is returned as the output.
        self.data_output_format = data_output_format
        # The data source ID.
        self.datasource_id = datasource_id
        # The user-defined name of the database.
        # 
        # This parameter is required.
        self.db_name = db_name
        # The configuration for full synchronization.
        self.full_compute_unit = full_compute_unit
        # The Hudi configuration for the destination.
        self.hudi_advanced_config = hudi_advanced_config
        # The configuration for incremental synchronization.
        # 
        # This parameter is required.
        self.incremental_compute_unit = incremental_compute_unit
        # The number of nested JSON layers to parse. Valid values:
        # 0: No parsing is performed.
        # 1: One layer is parsed.
        # 2: Two layers are parsed.
        # 3: Three layers are parsed.
        # 4: Four layers are parsed.
        # By default, one layer is parsed. For more information about the JSON parsing policy for nested data, see JSON parsing levels and schema field inference examples.
        self.json_parse_level = json_parse_level
        # The ID of the Kafka instance. Obtain the ID from the Kafka console.
        self.kafka_cluster_id = kafka_cluster_id
        # The ID of the Kafka topic. Obtain the ID from the Kafka console.
        self.kafka_topic = kafka_topic
        # The ID of the lakehouse.
        self.lakehouse_id = lakehouse_id
        # The number of entries to consume in a single batch.
        self.max_offsets_per_trigger = max_offsets_per_trigger
        # The destination lakehouse address. This must be a complete OSS path.
        self.oss_location = oss_location
        # The output data format.
        self.output_format = output_format
        # The partition information.
        self.partition_specs_shrink = partition_specs_shrink
        # The primary key settings. This parameter supports the UUID policy and the mapping policy. The policies are described as follows.
        # UUID policy: "Strategy": "uuid".
        # Mapping policy:
        # "Strategy": "mapping",
        # "Values":[
        # "f1",
        # "f2"
        # ],
        # "RecordVersionField","xxx"
        # \\`RecordVersionField\\` specifies the Hudi record version.
        self.primary_key_definition = primary_key_definition
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The name of the resource group.
        # 
        # This parameter is required.
        self.resource_group = resource_group
        # The region ID.
        self.source_region_id = source_region_id
        # The initial consumer offset for Kafka.
        # Valid values:
        # begin_cursor, end_cursor, and timestamp.
        # These values correspond to the earliest offset, the latest offset, and a specified time.
        # 
        # This parameter is required.
        self.starting_offsets = starting_offsets
        # The user-defined name of the table.
        # 
        # This parameter is required.
        self.table_name = table_name
        # The generation rule for the destination.
        self.target_generate_rule = target_generate_rule
        # The type of the destination.
        self.target_type = target_type
        # The name of the workload.
        # 
        # This parameter is required.
        self.workload_name = workload_name

    def validate(self):
        pass

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

        if self.columns_shrink is not None:
            result['Columns'] = self.columns_shrink

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.data_format_type is not None:
            result['DataFormatType'] = self.data_format_type

        if self.data_output_format is not None:
            result['DataOutputFormat'] = self.data_output_format

        if self.datasource_id is not None:
            result['DatasourceId'] = self.datasource_id

        if self.db_name is not None:
            result['DbName'] = self.db_name

        if self.full_compute_unit is not None:
            result['FullComputeUnit'] = self.full_compute_unit

        if self.hudi_advanced_config is not None:
            result['HudiAdvancedConfig'] = self.hudi_advanced_config

        if self.incremental_compute_unit is not None:
            result['IncrementalComputeUnit'] = self.incremental_compute_unit

        if self.json_parse_level is not None:
            result['JsonParseLevel'] = self.json_parse_level

        if self.kafka_cluster_id is not None:
            result['KafkaClusterId'] = self.kafka_cluster_id

        if self.kafka_topic is not None:
            result['KafkaTopic'] = self.kafka_topic

        if self.lakehouse_id is not None:
            result['LakehouseId'] = self.lakehouse_id

        if self.max_offsets_per_trigger is not None:
            result['MaxOffsetsPerTrigger'] = self.max_offsets_per_trigger

        if self.oss_location is not None:
            result['OssLocation'] = self.oss_location

        if self.output_format is not None:
            result['OutputFormat'] = self.output_format

        if self.partition_specs_shrink is not None:
            result['PartitionSpecs'] = self.partition_specs_shrink

        if self.primary_key_definition is not None:
            result['PrimaryKeyDefinition'] = self.primary_key_definition

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group is not None:
            result['ResourceGroup'] = self.resource_group

        if self.source_region_id is not None:
            result['SourceRegionId'] = self.source_region_id

        if self.starting_offsets is not None:
            result['StartingOffsets'] = self.starting_offsets

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.target_generate_rule is not None:
            result['TargetGenerateRule'] = self.target_generate_rule

        if self.target_type is not None:
            result['TargetType'] = self.target_type

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

        if m.get('Columns') is not None:
            self.columns_shrink = m.get('Columns')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DataFormatType') is not None:
            self.data_format_type = m.get('DataFormatType')

        if m.get('DataOutputFormat') is not None:
            self.data_output_format = m.get('DataOutputFormat')

        if m.get('DatasourceId') is not None:
            self.datasource_id = m.get('DatasourceId')

        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')

        if m.get('FullComputeUnit') is not None:
            self.full_compute_unit = m.get('FullComputeUnit')

        if m.get('HudiAdvancedConfig') is not None:
            self.hudi_advanced_config = m.get('HudiAdvancedConfig')

        if m.get('IncrementalComputeUnit') is not None:
            self.incremental_compute_unit = m.get('IncrementalComputeUnit')

        if m.get('JsonParseLevel') is not None:
            self.json_parse_level = m.get('JsonParseLevel')

        if m.get('KafkaClusterId') is not None:
            self.kafka_cluster_id = m.get('KafkaClusterId')

        if m.get('KafkaTopic') is not None:
            self.kafka_topic = m.get('KafkaTopic')

        if m.get('LakehouseId') is not None:
            self.lakehouse_id = m.get('LakehouseId')

        if m.get('MaxOffsetsPerTrigger') is not None:
            self.max_offsets_per_trigger = m.get('MaxOffsetsPerTrigger')

        if m.get('OssLocation') is not None:
            self.oss_location = m.get('OssLocation')

        if m.get('OutputFormat') is not None:
            self.output_format = m.get('OutputFormat')

        if m.get('PartitionSpecs') is not None:
            self.partition_specs_shrink = m.get('PartitionSpecs')

        if m.get('PrimaryKeyDefinition') is not None:
            self.primary_key_definition = m.get('PrimaryKeyDefinition')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroup') is not None:
            self.resource_group = m.get('ResourceGroup')

        if m.get('SourceRegionId') is not None:
            self.source_region_id = m.get('SourceRegionId')

        if m.get('StartingOffsets') is not None:
            self.starting_offsets = m.get('StartingOffsets')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('TargetGenerateRule') is not None:
            self.target_generate_rule = m.get('TargetGenerateRule')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        if m.get('WorkloadName') is not None:
            self.workload_name = m.get('WorkloadName')

        return self

