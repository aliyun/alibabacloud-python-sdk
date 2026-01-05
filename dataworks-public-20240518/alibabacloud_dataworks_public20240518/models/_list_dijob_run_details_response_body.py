# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListDIJobRunDetailsResponseBody(DaraModel):
    def __init__(
        self,
        paging_info: main_models.ListDIJobRunDetailsResponseBodyPagingInfo = None,
        request_id: str = None,
    ):
        # The pagination information.
        self.paging_info = paging_info
        # The request ID. You can use the ID to query logs and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.paging_info:
            self.paging_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.paging_info is not None:
            result['PagingInfo'] = self.paging_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PagingInfo') is not None:
            temp_model = main_models.ListDIJobRunDetailsResponseBodyPagingInfo()
            self.paging_info = temp_model.from_map(m.get('PagingInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListDIJobRunDetailsResponseBodyPagingInfo(DaraModel):
    def __init__(
        self,
        job_run_infos: List[main_models.ListDIJobRunDetailsResponseBodyPagingInfoJobRunInfos] = None,
        page_number: str = None,
        page_size: str = None,
        total_count: str = None,
    ):
        # The running information about the synchronization task.
        self.job_run_infos = job_run_infos
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.job_run_infos:
            for v1 in self.job_run_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['JobRunInfos'] = []
        if self.job_run_infos is not None:
            for k1 in self.job_run_infos:
                result['JobRunInfos'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.job_run_infos = []
        if m.get('JobRunInfos') is not None:
            for k1 in m.get('JobRunInfos'):
                temp_model = main_models.ListDIJobRunDetailsResponseBodyPagingInfoJobRunInfos()
                self.job_run_infos.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListDIJobRunDetailsResponseBodyPagingInfoJobRunInfos(DaraModel):
    def __init__(
        self,
        destination_database_name: str = None,
        destination_datasource_name: str = None,
        destination_schema_name: str = None,
        destination_table_name: str = None,
        full_migration_error_message: str = None,
        full_migration_status: str = None,
        offline_error_records: int = None,
        offline_total_bytes: int = None,
        offline_total_records: int = None,
        realtime_migration_error_message: str = None,
        realtime_migration_status: str = None,
        source_database_name: str = None,
        source_datasource_name: str = None,
        source_schema_name: str = None,
        source_table_name: str = None,
        structure_migration_error_message: str = None,
        structure_migration_status: str = None,
    ):
        # The name of the database in the destination.
        self.destination_database_name = destination_database_name
        # The name of the destination.
        self.destination_datasource_name = destination_datasource_name
        # The name of the schema of the destination.
        self.destination_schema_name = destination_schema_name
        # The name of the table in the destination.
        self.destination_table_name = destination_table_name
        # The error message that is returned if an error occurs during full batch synchronization. If no error occurs, no value is returned for this parameter.
        self.full_migration_error_message = full_migration_error_message
        # The status of full batch synchronization.
        self.full_migration_status = full_migration_status
        # The total number of errors that occur during full synchronization.
        self.offline_error_records = offline_error_records
        # The total number of bytes that are synchronized during full synchronization.
        self.offline_total_bytes = offline_total_bytes
        # The total number of data records that are synchronized during full synchronization.
        self.offline_total_records = offline_total_records
        # The error message that is returned if an error occurs during real-time synchronization. If no error occurs, no value is returned for this parameter.
        self.realtime_migration_error_message = realtime_migration_error_message
        # The status of real-time synchronization.
        self.realtime_migration_status = realtime_migration_status
        # The name of the database in the source.
        self.source_database_name = source_database_name
        # The name of the source.
        self.source_datasource_name = source_datasource_name
        # The name of the schema of the source.
        self.source_schema_name = source_schema_name
        # The name of the table in the source.
        self.source_table_name = source_table_name
        # The error message that is returned if an error occurs during schema synchronization. If no error occurs, no value is returned for this parameter.
        self.structure_migration_error_message = structure_migration_error_message
        # The synchronization status of the schema.
        self.structure_migration_status = structure_migration_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.destination_database_name is not None:
            result['DestinationDatabaseName'] = self.destination_database_name

        if self.destination_datasource_name is not None:
            result['DestinationDatasourceName'] = self.destination_datasource_name

        if self.destination_schema_name is not None:
            result['DestinationSchemaName'] = self.destination_schema_name

        if self.destination_table_name is not None:
            result['DestinationTableName'] = self.destination_table_name

        if self.full_migration_error_message is not None:
            result['FullMigrationErrorMessage'] = self.full_migration_error_message

        if self.full_migration_status is not None:
            result['FullMigrationStatus'] = self.full_migration_status

        if self.offline_error_records is not None:
            result['OfflineErrorRecords'] = self.offline_error_records

        if self.offline_total_bytes is not None:
            result['OfflineTotalBytes'] = self.offline_total_bytes

        if self.offline_total_records is not None:
            result['OfflineTotalRecords'] = self.offline_total_records

        if self.realtime_migration_error_message is not None:
            result['RealtimeMigrationErrorMessage'] = self.realtime_migration_error_message

        if self.realtime_migration_status is not None:
            result['RealtimeMigrationStatus'] = self.realtime_migration_status

        if self.source_database_name is not None:
            result['SourceDatabaseName'] = self.source_database_name

        if self.source_datasource_name is not None:
            result['SourceDatasourceName'] = self.source_datasource_name

        if self.source_schema_name is not None:
            result['SourceSchemaName'] = self.source_schema_name

        if self.source_table_name is not None:
            result['SourceTableName'] = self.source_table_name

        if self.structure_migration_error_message is not None:
            result['StructureMigrationErrorMessage'] = self.structure_migration_error_message

        if self.structure_migration_status is not None:
            result['StructureMigrationStatus'] = self.structure_migration_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationDatabaseName') is not None:
            self.destination_database_name = m.get('DestinationDatabaseName')

        if m.get('DestinationDatasourceName') is not None:
            self.destination_datasource_name = m.get('DestinationDatasourceName')

        if m.get('DestinationSchemaName') is not None:
            self.destination_schema_name = m.get('DestinationSchemaName')

        if m.get('DestinationTableName') is not None:
            self.destination_table_name = m.get('DestinationTableName')

        if m.get('FullMigrationErrorMessage') is not None:
            self.full_migration_error_message = m.get('FullMigrationErrorMessage')

        if m.get('FullMigrationStatus') is not None:
            self.full_migration_status = m.get('FullMigrationStatus')

        if m.get('OfflineErrorRecords') is not None:
            self.offline_error_records = m.get('OfflineErrorRecords')

        if m.get('OfflineTotalBytes') is not None:
            self.offline_total_bytes = m.get('OfflineTotalBytes')

        if m.get('OfflineTotalRecords') is not None:
            self.offline_total_records = m.get('OfflineTotalRecords')

        if m.get('RealtimeMigrationErrorMessage') is not None:
            self.realtime_migration_error_message = m.get('RealtimeMigrationErrorMessage')

        if m.get('RealtimeMigrationStatus') is not None:
            self.realtime_migration_status = m.get('RealtimeMigrationStatus')

        if m.get('SourceDatabaseName') is not None:
            self.source_database_name = m.get('SourceDatabaseName')

        if m.get('SourceDatasourceName') is not None:
            self.source_datasource_name = m.get('SourceDatasourceName')

        if m.get('SourceSchemaName') is not None:
            self.source_schema_name = m.get('SourceSchemaName')

        if m.get('SourceTableName') is not None:
            self.source_table_name = m.get('SourceTableName')

        if m.get('StructureMigrationErrorMessage') is not None:
            self.structure_migration_error_message = m.get('StructureMigrationErrorMessage')

        if m.get('StructureMigrationStatus') is not None:
            self.structure_migration_status = m.get('StructureMigrationStatus')

        return self

