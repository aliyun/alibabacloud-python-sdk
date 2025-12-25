# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescibeImportsFromDatabaseResponseBody(DaraModel):
    def __init__(
        self,
        items: main_models.DescibeImportsFromDatabaseResponseBodyItems = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        total_record_count: int = None,
    ):
        # The migration tasks.
        self.items = items
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_record_count = page_record_count
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_record_count = total_record_count

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.items is not None:
            result['Items'] = self.items.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Items') is not None:
            temp_model = main_models.DescibeImportsFromDatabaseResponseBodyItems()
            self.items = temp_model.from_map(m.get('Items'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescibeImportsFromDatabaseResponseBodyItems(DaraModel):
    def __init__(
        self,
        import_result_from_db: List[main_models.DescibeImportsFromDatabaseResponseBodyItemsImportResultFromDB] = None,
    ):
        self.import_result_from_db = import_result_from_db

    def validate(self):
        if self.import_result_from_db:
            for v1 in self.import_result_from_db:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ImportResultFromDB'] = []
        if self.import_result_from_db is not None:
            for k1 in self.import_result_from_db:
                result['ImportResultFromDB'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.import_result_from_db = []
        if m.get('ImportResultFromDB') is not None:
            for k1 in m.get('ImportResultFromDB'):
                temp_model = main_models.DescibeImportsFromDatabaseResponseBodyItemsImportResultFromDB()
                self.import_result_from_db.append(temp_model.from_map(k1))

        return self

class DescibeImportsFromDatabaseResponseBodyItemsImportResultFromDB(DaraModel):
    def __init__(
        self,
        import_data_status: str = None,
        import_data_status_description: str = None,
        import_data_type: str = None,
        import_id: int = None,
        incremental_importing_time: str = None,
    ):
        # The status of the migration task. Valid values:
        # 
        # *   **NotStart**: The migration task has not started.
        # *   **FullExporting**: The migration task is exporting full data.
        # *   **FullImporting**: The migration task is importing full data.
        # *   **Success**: The migration task is successful.
        # *   **Failed**: The migration task failed.
        # *   **Canceled**: The migration task is canceled.
        # *   **Canceling**: The migration task is being canceled.
        # *   **IncrementalWaiting**: The migration task is waiting to synchronize incremental data.
        # *   **IncrementalImporting**: The migration task is synchronizing incremental data.
        # *   **StopSyncing**: The migration task stops synchronizing data.
        self.import_data_status = import_data_status
        # The description of the migration task.
        self.import_data_status_description = import_data_status_description
        # The type of the migration task. Valid values:
        # 
        # *   **Full**: full migration
        # *   **Incremental:**: incremental migration
        self.import_data_type = import_data_type
        # The ID of the migration task.
        self.import_id = import_id
        # The time when the migration task synchronized incremental data. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.incremental_importing_time = incremental_importing_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.import_data_status is not None:
            result['ImportDataStatus'] = self.import_data_status

        if self.import_data_status_description is not None:
            result['ImportDataStatusDescription'] = self.import_data_status_description

        if self.import_data_type is not None:
            result['ImportDataType'] = self.import_data_type

        if self.import_id is not None:
            result['ImportId'] = self.import_id

        if self.incremental_importing_time is not None:
            result['IncrementalImportingTime'] = self.incremental_importing_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImportDataStatus') is not None:
            self.import_data_status = m.get('ImportDataStatus')

        if m.get('ImportDataStatusDescription') is not None:
            self.import_data_status_description = m.get('ImportDataStatusDescription')

        if m.get('ImportDataType') is not None:
            self.import_data_type = m.get('ImportDataType')

        if m.get('ImportId') is not None:
            self.import_id = m.get('ImportId')

        if m.get('IncrementalImportingTime') is not None:
            self.incremental_importing_time = m.get('IncrementalImportingTime')

        return self

