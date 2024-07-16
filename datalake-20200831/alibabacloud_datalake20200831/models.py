# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class DatalakeFile(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        file_group_id: str = None,
        file_name: str = None,
        file_size: int = None,
        is_log_file: bool = None,
        partition_id: str = None,
        table_id: str = None,
        timestamp: str = None,
        update_time: int = None,
    ):
        self.create_time = create_time
        self.file_group_id = file_group_id
        self.file_name = file_name
        self.file_size = file_size
        self.is_log_file = is_log_file
        self.partition_id = partition_id
        self.table_id = table_id
        self.timestamp = timestamp
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.file_group_id is not None:
            result['FileGroupId'] = self.file_group_id
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.is_log_file is not None:
            result['IsLogFile'] = self.is_log_file
        if self.partition_id is not None:
            result['PartitionId'] = self.partition_id
        if self.table_id is not None:
            result['TableId'] = self.table_id
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('FileGroupId') is not None:
            self.file_group_id = m.get('FileGroupId')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('IsLogFile') is not None:
            self.is_log_file = m.get('IsLogFile')
        if m.get('PartitionId') is not None:
            self.partition_id = m.get('PartitionId')
        if m.get('TableId') is not None:
            self.table_id = m.get('TableId')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class DatalakeInstant(TeaModel):
    def __init__(
        self,
        action: str = None,
        create_time: int = None,
        duration: int = None,
        state: str = None,
        table_id: str = None,
        timestamp: str = None,
        update_time: int = None,
    ):
        self.action = action
        self.create_time = create_time
        self.duration = duration
        self.state = state
        self.table_id = table_id
        self.timestamp = timestamp
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.state is not None:
            result['State'] = self.state
        if self.table_id is not None:
            result['TableId'] = self.table_id
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('TableId') is not None:
            self.table_id = m.get('TableId')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class DatalakePartition(TeaModel):
    def __init__(
        self,
        end_timestamp: str = None,
        partition_id: str = None,
        partition_location: str = None,
        partition_name: str = None,
        start_timestamp: str = None,
        table_id: str = None,
    ):
        self.end_timestamp = end_timestamp
        self.partition_id = partition_id
        self.partition_location = partition_location
        self.partition_name = partition_name
        self.start_timestamp = start_timestamp
        self.table_id = table_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_timestamp is not None:
            result['EndTimestamp'] = self.end_timestamp
        if self.partition_id is not None:
            result['PartitionId'] = self.partition_id
        if self.partition_location is not None:
            result['PartitionLocation'] = self.partition_location
        if self.partition_name is not None:
            result['PartitionName'] = self.partition_name
        if self.start_timestamp is not None:
            result['StartTimestamp'] = self.start_timestamp
        if self.table_id is not None:
            result['TableId'] = self.table_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')
        if m.get('PartitionId') is not None:
            self.partition_id = m.get('PartitionId')
        if m.get('PartitionLocation') is not None:
            self.partition_location = m.get('PartitionLocation')
        if m.get('PartitionName') is not None:
            self.partition_name = m.get('PartitionName')
        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')
        if m.get('TableId') is not None:
            self.table_id = m.get('TableId')
        return self


class DatalakeSimpleFile(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        file_size: int = None,
        partition_name: str = None,
    ):
        self.file_name = file_name
        self.file_size = file_size
        self.partition_name = partition_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.partition_name is not None:
            result['PartitionName'] = self.partition_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('PartitionName') is not None:
            self.partition_name = m.get('PartitionName')
        return self


class DatalakeTable(TeaModel):
    def __init__(
        self,
        catalog_id: str = None,
        create_time: int = None,
        database_name: str = None,
        is_partitioned_table: int = None,
        location: str = None,
        table_format: str = None,
        table_id: str = None,
        table_name: str = None,
        table_properties: str = None,
        table_version: str = None,
        uid: str = None,
        update_time: int = None,
    ):
        self.catalog_id = catalog_id
        self.create_time = create_time
        self.database_name = database_name
        self.is_partitioned_table = is_partitioned_table
        self.location = location
        self.table_format = table_format
        self.table_id = table_id
        self.table_name = table_name
        self.table_properties = table_properties
        self.table_version = table_version
        self.uid = uid
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.is_partitioned_table is not None:
            result['IsPartitionedTable'] = self.is_partitioned_table
        if self.location is not None:
            result['Location'] = self.location
        if self.table_format is not None:
            result['TableFormat'] = self.table_format
        if self.table_id is not None:
            result['TableId'] = self.table_id
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.table_properties is not None:
            result['TableProperties'] = self.table_properties
        if self.table_version is not None:
            result['TableVersion'] = self.table_version
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('IsPartitionedTable') is not None:
            self.is_partitioned_table = m.get('IsPartitionedTable')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('TableFormat') is not None:
            self.table_format = m.get('TableFormat')
        if m.get('TableId') is not None:
            self.table_id = m.get('TableId')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('TableProperties') is not None:
            self.table_properties = m.get('TableProperties')
        if m.get('TableVersion') is not None:
            self.table_version = m.get('TableVersion')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class Instant(TeaModel):
    def __init__(
        self,
        action: str = None,
        instant_action: str = None,
        state: str = None,
        timestamp: str = None,
    ):
        self.action = action
        self.instant_action = instant_action
        self.state = state
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.instant_action is not None:
            result['InstantAction'] = self.instant_action
        if self.state is not None:
            result['State'] = self.state
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('InstantAction') is not None:
            self.instant_action = m.get('InstantAction')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class InstantMetadata(TeaModel):
    def __init__(
        self,
        metadata: str = None,
    ):
        self.metadata = metadata

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        return self


class InstantWithMetadata(TeaModel):
    def __init__(
        self,
        instant: Instant = None,
        instant_metadata: InstantMetadata = None,
    ):
        self.instant = instant
        self.instant_metadata = instant_metadata

    def validate(self):
        if self.instant:
            self.instant.validate()
        if self.instant_metadata:
            self.instant_metadata.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instant is not None:
            result['Instant'] = self.instant.to_map()
        if self.instant_metadata is not None:
            result['InstantMetadata'] = self.instant_metadata.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Instant') is not None:
            temp_model = Instant()
            self.instant = temp_model.from_map(m['Instant'])
        if m.get('InstantMetadata') is not None:
            temp_model = InstantMetadata()
            self.instant_metadata = temp_model.from_map(m['InstantMetadata'])
        return self


