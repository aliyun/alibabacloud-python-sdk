# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class TableModel(DaraModel):
    def __init__(
        self,
        archive_type: str = None,
        block_size: int = None,
        bucket: int = None,
        bucket_count: int = None,
        cols: List[main_models.FieldSchemaModel] = None,
        comment: str = None,
        compression: str = None,
        create_time: str = None,
        created_by_source: str = None,
        created_by_user: str = None,
        current_version: int = None,
        db_name: str = None,
        dict_encode: bool = None,
        distribute_columns: List[main_models.FieldSchemaModel] = None,
        distribute_type: str = None,
        enable_dfs: bool = None,
        hot_partition_count: int = None,
        indexes: List[main_models.CstoreIndexModel] = None,
        is_all_index: bool = None,
        is_fulltext_dict: bool = None,
        max_column_id: int = None,
        parameters: Dict[str, str] = None,
        partition_column: str = None,
        partition_count: int = None,
        partition_keys: List[main_models.FieldSchemaModel] = None,
        partition_type: str = None,
        physical_database_name: str = None,
        physical_table_name: str = None,
        previous_version: int = None,
        raw_table_name: str = None,
        route_columns: List[main_models.FieldSchemaModel] = None,
        route_effective_column: main_models.FieldSchemaModel = None,
        route_type: str = None,
        rt_engine_type: str = None,
        rt_index_all: bool = None,
        rt_mode_type: str = None,
        sd: main_models.StorageDescriptorModel = None,
        storage_policy: str = None,
        subpartition_column: str = None,
        subpartition_count: int = None,
        subpartition_type: str = None,
        table_engine_name: str = None,
        table_name: str = None,
        table_type: str = None,
        tbl_id: int = None,
        temporary: bool = None,
        update_time: str = None,
        view_expanded_text: str = None,
        view_original_text: str = None,
        view_security_mode: str = None,
    ):
        self.archive_type = archive_type
        self.block_size = block_size
        self.bucket = bucket
        self.bucket_count = bucket_count
        self.cols = cols
        self.comment = comment
        self.compression = compression
        self.create_time = create_time
        self.created_by_source = created_by_source
        self.created_by_user = created_by_user
        self.current_version = current_version
        self.db_name = db_name
        self.dict_encode = dict_encode
        self.distribute_columns = distribute_columns
        self.distribute_type = distribute_type
        self.enable_dfs = enable_dfs
        self.hot_partition_count = hot_partition_count
        self.indexes = indexes
        self.is_all_index = is_all_index
        self.is_fulltext_dict = is_fulltext_dict
        self.max_column_id = max_column_id
        self.parameters = parameters
        self.partition_column = partition_column
        self.partition_count = partition_count
        self.partition_keys = partition_keys
        self.partition_type = partition_type
        self.physical_database_name = physical_database_name
        self.physical_table_name = physical_table_name
        self.previous_version = previous_version
        self.raw_table_name = raw_table_name
        self.route_columns = route_columns
        self.route_effective_column = route_effective_column
        self.route_type = route_type
        self.rt_engine_type = rt_engine_type
        self.rt_index_all = rt_index_all
        self.rt_mode_type = rt_mode_type
        self.sd = sd
        self.storage_policy = storage_policy
        self.subpartition_column = subpartition_column
        self.subpartition_count = subpartition_count
        self.subpartition_type = subpartition_type
        self.table_engine_name = table_engine_name
        self.table_name = table_name
        self.table_type = table_type
        self.tbl_id = tbl_id
        self.temporary = temporary
        self.update_time = update_time
        self.view_expanded_text = view_expanded_text
        self.view_original_text = view_original_text
        self.view_security_mode = view_security_mode

    def validate(self):
        if self.cols:
            for v1 in self.cols:
                 if v1:
                    v1.validate()
        if self.distribute_columns:
            for v1 in self.distribute_columns:
                 if v1:
                    v1.validate()
        if self.indexes:
            for v1 in self.indexes:
                 if v1:
                    v1.validate()
        if self.partition_keys:
            for v1 in self.partition_keys:
                 if v1:
                    v1.validate()
        if self.route_columns:
            for v1 in self.route_columns:
                 if v1:
                    v1.validate()
        if self.route_effective_column:
            self.route_effective_column.validate()
        if self.sd:
            self.sd.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.archive_type is not None:
            result['ArchiveType'] = self.archive_type

        if self.block_size is not None:
            result['BlockSize'] = self.block_size

        if self.bucket is not None:
            result['Bucket'] = self.bucket

        if self.bucket_count is not None:
            result['BucketCount'] = self.bucket_count

        result['Cols'] = []
        if self.cols is not None:
            for k1 in self.cols:
                result['Cols'].append(k1.to_map() if k1 else None)

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.compression is not None:
            result['Compression'] = self.compression

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.created_by_source is not None:
            result['CreatedBySource'] = self.created_by_source

        if self.created_by_user is not None:
            result['CreatedByUser'] = self.created_by_user

        if self.current_version is not None:
            result['CurrentVersion'] = self.current_version

        if self.db_name is not None:
            result['DbName'] = self.db_name

        if self.dict_encode is not None:
            result['DictEncode'] = self.dict_encode

        result['DistributeColumns'] = []
        if self.distribute_columns is not None:
            for k1 in self.distribute_columns:
                result['DistributeColumns'].append(k1.to_map() if k1 else None)

        if self.distribute_type is not None:
            result['DistributeType'] = self.distribute_type

        if self.enable_dfs is not None:
            result['EnableDfs'] = self.enable_dfs

        if self.hot_partition_count is not None:
            result['HotPartitionCount'] = self.hot_partition_count

        result['Indexes'] = []
        if self.indexes is not None:
            for k1 in self.indexes:
                result['Indexes'].append(k1.to_map() if k1 else None)

        if self.is_all_index is not None:
            result['IsAllIndex'] = self.is_all_index

        if self.is_fulltext_dict is not None:
            result['IsFulltextDict'] = self.is_fulltext_dict

        if self.max_column_id is not None:
            result['MaxColumnId'] = self.max_column_id

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        if self.partition_column is not None:
            result['PartitionColumn'] = self.partition_column

        if self.partition_count is not None:
            result['PartitionCount'] = self.partition_count

        result['PartitionKeys'] = []
        if self.partition_keys is not None:
            for k1 in self.partition_keys:
                result['PartitionKeys'].append(k1.to_map() if k1 else None)

        if self.partition_type is not None:
            result['PartitionType'] = self.partition_type

        if self.physical_database_name is not None:
            result['PhysicalDatabaseName'] = self.physical_database_name

        if self.physical_table_name is not None:
            result['PhysicalTableName'] = self.physical_table_name

        if self.previous_version is not None:
            result['PreviousVersion'] = self.previous_version

        if self.raw_table_name is not None:
            result['RawTableName'] = self.raw_table_name

        result['RouteColumns'] = []
        if self.route_columns is not None:
            for k1 in self.route_columns:
                result['RouteColumns'].append(k1.to_map() if k1 else None)

        if self.route_effective_column is not None:
            result['RouteEffectiveColumn'] = self.route_effective_column.to_map()

        if self.route_type is not None:
            result['RouteType'] = self.route_type

        if self.rt_engine_type is not None:
            result['RtEngineType'] = self.rt_engine_type

        if self.rt_index_all is not None:
            result['RtIndexAll'] = self.rt_index_all

        if self.rt_mode_type is not None:
            result['RtModeType'] = self.rt_mode_type

        if self.sd is not None:
            result['Sd'] = self.sd.to_map()

        if self.storage_policy is not None:
            result['StoragePolicy'] = self.storage_policy

        if self.subpartition_column is not None:
            result['SubpartitionColumn'] = self.subpartition_column

        if self.subpartition_count is not None:
            result['SubpartitionCount'] = self.subpartition_count

        if self.subpartition_type is not None:
            result['SubpartitionType'] = self.subpartition_type

        if self.table_engine_name is not None:
            result['TableEngineName'] = self.table_engine_name

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.table_type is not None:
            result['TableType'] = self.table_type

        if self.tbl_id is not None:
            result['TblId'] = self.tbl_id

        if self.temporary is not None:
            result['Temporary'] = self.temporary

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.view_expanded_text is not None:
            result['ViewExpandedText'] = self.view_expanded_text

        if self.view_original_text is not None:
            result['ViewOriginalText'] = self.view_original_text

        if self.view_security_mode is not None:
            result['ViewSecurityMode'] = self.view_security_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArchiveType') is not None:
            self.archive_type = m.get('ArchiveType')

        if m.get('BlockSize') is not None:
            self.block_size = m.get('BlockSize')

        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')

        if m.get('BucketCount') is not None:
            self.bucket_count = m.get('BucketCount')

        self.cols = []
        if m.get('Cols') is not None:
            for k1 in m.get('Cols'):
                temp_model = main_models.FieldSchemaModel()
                self.cols.append(temp_model.from_map(k1))

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('Compression') is not None:
            self.compression = m.get('Compression')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreatedBySource') is not None:
            self.created_by_source = m.get('CreatedBySource')

        if m.get('CreatedByUser') is not None:
            self.created_by_user = m.get('CreatedByUser')

        if m.get('CurrentVersion') is not None:
            self.current_version = m.get('CurrentVersion')

        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')

        if m.get('DictEncode') is not None:
            self.dict_encode = m.get('DictEncode')

        self.distribute_columns = []
        if m.get('DistributeColumns') is not None:
            for k1 in m.get('DistributeColumns'):
                temp_model = main_models.FieldSchemaModel()
                self.distribute_columns.append(temp_model.from_map(k1))

        if m.get('DistributeType') is not None:
            self.distribute_type = m.get('DistributeType')

        if m.get('EnableDfs') is not None:
            self.enable_dfs = m.get('EnableDfs')

        if m.get('HotPartitionCount') is not None:
            self.hot_partition_count = m.get('HotPartitionCount')

        self.indexes = []
        if m.get('Indexes') is not None:
            for k1 in m.get('Indexes'):
                temp_model = main_models.CstoreIndexModel()
                self.indexes.append(temp_model.from_map(k1))

        if m.get('IsAllIndex') is not None:
            self.is_all_index = m.get('IsAllIndex')

        if m.get('IsFulltextDict') is not None:
            self.is_fulltext_dict = m.get('IsFulltextDict')

        if m.get('MaxColumnId') is not None:
            self.max_column_id = m.get('MaxColumnId')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        if m.get('PartitionColumn') is not None:
            self.partition_column = m.get('PartitionColumn')

        if m.get('PartitionCount') is not None:
            self.partition_count = m.get('PartitionCount')

        self.partition_keys = []
        if m.get('PartitionKeys') is not None:
            for k1 in m.get('PartitionKeys'):
                temp_model = main_models.FieldSchemaModel()
                self.partition_keys.append(temp_model.from_map(k1))

        if m.get('PartitionType') is not None:
            self.partition_type = m.get('PartitionType')

        if m.get('PhysicalDatabaseName') is not None:
            self.physical_database_name = m.get('PhysicalDatabaseName')

        if m.get('PhysicalTableName') is not None:
            self.physical_table_name = m.get('PhysicalTableName')

        if m.get('PreviousVersion') is not None:
            self.previous_version = m.get('PreviousVersion')

        if m.get('RawTableName') is not None:
            self.raw_table_name = m.get('RawTableName')

        self.route_columns = []
        if m.get('RouteColumns') is not None:
            for k1 in m.get('RouteColumns'):
                temp_model = main_models.FieldSchemaModel()
                self.route_columns.append(temp_model.from_map(k1))

        if m.get('RouteEffectiveColumn') is not None:
            temp_model = main_models.FieldSchemaModel()
            self.route_effective_column = temp_model.from_map(m.get('RouteEffectiveColumn'))

        if m.get('RouteType') is not None:
            self.route_type = m.get('RouteType')

        if m.get('RtEngineType') is not None:
            self.rt_engine_type = m.get('RtEngineType')

        if m.get('RtIndexAll') is not None:
            self.rt_index_all = m.get('RtIndexAll')

        if m.get('RtModeType') is not None:
            self.rt_mode_type = m.get('RtModeType')

        if m.get('Sd') is not None:
            temp_model = main_models.StorageDescriptorModel()
            self.sd = temp_model.from_map(m.get('Sd'))

        if m.get('StoragePolicy') is not None:
            self.storage_policy = m.get('StoragePolicy')

        if m.get('SubpartitionColumn') is not None:
            self.subpartition_column = m.get('SubpartitionColumn')

        if m.get('SubpartitionCount') is not None:
            self.subpartition_count = m.get('SubpartitionCount')

        if m.get('SubpartitionType') is not None:
            self.subpartition_type = m.get('SubpartitionType')

        if m.get('TableEngineName') is not None:
            self.table_engine_name = m.get('TableEngineName')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('TableType') is not None:
            self.table_type = m.get('TableType')

        if m.get('TblId') is not None:
            self.tbl_id = m.get('TblId')

        if m.get('Temporary') is not None:
            self.temporary = m.get('Temporary')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('ViewExpandedText') is not None:
            self.view_expanded_text = m.get('ViewExpandedText')

        if m.get('ViewOriginalText') is not None:
            self.view_original_text = m.get('ViewOriginalText')

        if m.get('ViewSecurityMode') is not None:
            self.view_security_mode = m.get('ViewSecurityMode')

        return self

