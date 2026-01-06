# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class ListApsLifecycleStrategyResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        items: List[main_models.ListApsLifecycleStrategyResponseBodyItems] = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The HTTP status code or the error code.
        self.code = code
        # The response code. The status code 200 indicates that the request was successful.
        self.http_status_code = http_status_code
        # The queried lifecycle management policies.
        self.items = items
        # The returned message. Valid values:
        # 
        # *   If the request was successful, a success message is returned.****
        # *   If the request failed, an error message is returned.
        self.message = message
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.success = success
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.ListApsLifecycleStrategyResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListApsLifecycleStrategyResponseBodyItems(DaraModel):
    def __init__(
        self,
        aps_job_id: str = None,
        created_time: str = None,
        dbcluster_id: str = None,
        modified_time: str = None,
        operation_tables: List[main_models.ListApsLifecycleStrategyResponseBodyItemsOperationTables] = None,
        status: str = None,
        strategy_databases: int = None,
        strategy_desc: str = None,
        strategy_name: str = None,
        strategy_tables: int = None,
        strategy_type: str = None,
        strategy_value: str = None,
    ):
        # The job ID.
        self.aps_job_id = aps_job_id
        # The time when the policy was created.
        self.created_time = created_time
        # The cluster ID.
        self.dbcluster_id = dbcluster_id
        # The time when the policy was modified.
        self.modified_time = modified_time
        # The operation tables.
        self.operation_tables = operation_tables
        # The status of the lifecycle management policy. Valid values:
        # 
        # 1.  on: enables the current policy.
        # 2.  off: disables the current policy.
        self.status = status
        # The number of databases that are managed during the lifecycle management.
        self.strategy_databases = strategy_databases
        # The description of the lifecycle management policy.
        self.strategy_desc = strategy_desc
        # The name of the lifecycle management policy.
        self.strategy_name = strategy_name
        # The number of tables that are managed during the lifecycle management.
        self.strategy_tables = strategy_tables
        # The type of the lifecycle management policy.
        self.strategy_type = strategy_type
        # The value of the lifecycle management policy.
        self.strategy_value = strategy_value

    def validate(self):
        if self.operation_tables:
            for v1 in self.operation_tables:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aps_job_id is not None:
            result['ApsJobId'] = self.aps_job_id

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        result['OperationTables'] = []
        if self.operation_tables is not None:
            for k1 in self.operation_tables:
                result['OperationTables'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['Status'] = self.status

        if self.strategy_databases is not None:
            result['StrategyDatabases'] = self.strategy_databases

        if self.strategy_desc is not None:
            result['StrategyDesc'] = self.strategy_desc

        if self.strategy_name is not None:
            result['StrategyName'] = self.strategy_name

        if self.strategy_tables is not None:
            result['StrategyTables'] = self.strategy_tables

        if self.strategy_type is not None:
            result['StrategyType'] = self.strategy_type

        if self.strategy_value is not None:
            result['StrategyValue'] = self.strategy_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApsJobId') is not None:
            self.aps_job_id = m.get('ApsJobId')

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        self.operation_tables = []
        if m.get('OperationTables') is not None:
            for k1 in m.get('OperationTables'):
                temp_model = main_models.ListApsLifecycleStrategyResponseBodyItemsOperationTables()
                self.operation_tables.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StrategyDatabases') is not None:
            self.strategy_databases = m.get('StrategyDatabases')

        if m.get('StrategyDesc') is not None:
            self.strategy_desc = m.get('StrategyDesc')

        if m.get('StrategyName') is not None:
            self.strategy_name = m.get('StrategyName')

        if m.get('StrategyTables') is not None:
            self.strategy_tables = m.get('StrategyTables')

        if m.get('StrategyType') is not None:
            self.strategy_type = m.get('StrategyType')

        if m.get('StrategyValue') is not None:
            self.strategy_value = m.get('StrategyValue')

        return self

class ListApsLifecycleStrategyResponseBodyItemsOperationTables(DaraModel):
    def __init__(
        self,
        database_name: str = None,
        process_all: str = None,
        table_names: List[str] = None,
    ):
        # The name of the database.
        self.database_name = database_name
        # Indicates whether all tables in the database are selected.
        self.process_all = process_all
        # The names of the tables.
        self.table_names = table_names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name

        if self.process_all is not None:
            result['ProcessAll'] = self.process_all

        if self.table_names is not None:
            result['TableNames'] = self.table_names

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')

        if m.get('ProcessAll') is not None:
            self.process_all = m.get('ProcessAll')

        if m.get('TableNames') is not None:
            self.table_names = m.get('TableNames')

        return self

