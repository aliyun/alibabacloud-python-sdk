# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_rocketmq20220801 import models as main_models
from darabonba.model import DaraModel

class ListMigrationsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListMigrationsResponseBodyData = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.dynamic_code is not None:
            result['dynamicCode'] = self.dynamic_code

        if self.dynamic_message is not None:
            result['dynamicMessage'] = self.dynamic_message

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.ListMigrationsResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('dynamicCode') is not None:
            self.dynamic_code = m.get('dynamicCode')

        if m.get('dynamicMessage') is not None:
            self.dynamic_message = m.get('dynamicMessage')

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class ListMigrationsResponseBodyData(DaraModel):
    def __init__(
        self,
        list: List[main_models.ListMigrationsResponseBodyDataList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.list = list
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['list'] = []
        if self.list is not None:
            for k1 in self.list:
                result['list'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k1 in m.get('list'):
                temp_model = main_models.ListMigrationsResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListMigrationsResponseBodyDataList(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        current_stage: main_models.ListMigrationsResponseBodyDataListCurrentStage = None,
        migration_id: int = None,
        migration_name: str = None,
        migration_source: main_models.ListMigrationsResponseBodyDataListMigrationSource = None,
        migration_status: str = None,
        migration_target: main_models.ListMigrationsResponseBodyDataListMigrationTarget = None,
        migration_type: str = None,
        update_time: str = None,
        user_id: str = None,
    ):
        self.create_time = create_time
        self.current_stage = current_stage
        self.migration_id = migration_id
        self.migration_name = migration_name
        self.migration_source = migration_source
        self.migration_status = migration_status
        self.migration_target = migration_target
        self.migration_type = migration_type
        self.update_time = update_time
        self.user_id = user_id

    def validate(self):
        if self.current_stage:
            self.current_stage.validate()
        if self.migration_source:
            self.migration_source.validate()
        if self.migration_target:
            self.migration_target.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.current_stage is not None:
            result['currentStage'] = self.current_stage.to_map()

        if self.migration_id is not None:
            result['migrationId'] = self.migration_id

        if self.migration_name is not None:
            result['migrationName'] = self.migration_name

        if self.migration_source is not None:
            result['migrationSource'] = self.migration_source.to_map()

        if self.migration_status is not None:
            result['migrationStatus'] = self.migration_status

        if self.migration_target is not None:
            result['migrationTarget'] = self.migration_target.to_map()

        if self.migration_type is not None:
            result['migrationType'] = self.migration_type

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('currentStage') is not None:
            temp_model = main_models.ListMigrationsResponseBodyDataListCurrentStage()
            self.current_stage = temp_model.from_map(m.get('currentStage'))

        if m.get('migrationId') is not None:
            self.migration_id = m.get('migrationId')

        if m.get('migrationName') is not None:
            self.migration_name = m.get('migrationName')

        if m.get('migrationSource') is not None:
            temp_model = main_models.ListMigrationsResponseBodyDataListMigrationSource()
            self.migration_source = temp_model.from_map(m.get('migrationSource'))

        if m.get('migrationStatus') is not None:
            self.migration_status = m.get('migrationStatus')

        if m.get('migrationTarget') is not None:
            temp_model = main_models.ListMigrationsResponseBodyDataListMigrationTarget()
            self.migration_target = temp_model.from_map(m.get('migrationTarget'))

        if m.get('migrationType') is not None:
            self.migration_type = m.get('migrationType')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

class ListMigrationsResponseBodyDataListMigrationTarget(DaraModel):
    def __init__(
        self,
        target_data: Any = None,
        target_type: str = None,
    ):
        self.target_data = target_data
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.target_data is not None:
            result['targetData'] = self.target_data

        if self.target_type is not None:
            result['targetType'] = self.target_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('targetData') is not None:
            self.target_data = m.get('targetData')

        if m.get('targetType') is not None:
            self.target_type = m.get('targetType')

        return self

class ListMigrationsResponseBodyDataListMigrationSource(DaraModel):
    def __init__(
        self,
        source_data: Any = None,
        source_type: str = None,
    ):
        self.source_data = source_data
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.source_data is not None:
            result['sourceData'] = self.source_data

        if self.source_type is not None:
            result['sourceType'] = self.source_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sourceData') is not None:
            self.source_data = m.get('sourceData')

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        return self

class ListMigrationsResponseBodyDataListCurrentStage(DaraModel):
    def __init__(
        self,
        stage_data: Any = None,
        stage_status: str = None,
        stage_type: str = None,
    ):
        self.stage_data = stage_data
        self.stage_status = stage_status
        self.stage_type = stage_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.stage_data is not None:
            result['stageData'] = self.stage_data

        if self.stage_status is not None:
            result['stageStatus'] = self.stage_status

        if self.stage_type is not None:
            result['stageType'] = self.stage_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('stageData') is not None:
            self.stage_data = m.get('stageData')

        if m.get('stageStatus') is not None:
            self.stage_status = m.get('stageStatus')

        if m.get('stageType') is not None:
            self.stage_type = m.get('stageType')

        return self

