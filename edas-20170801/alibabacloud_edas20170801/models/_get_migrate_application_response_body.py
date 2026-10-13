# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_edas20170801 import models as main_models
from darabonba.model import DaraModel

class GetMigrateApplicationResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.GetMigrateApplicationResponseBodyData = None,
        message: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        # The status code.
        self.code = code
        # The response data.
        self.data = data
        # The response message.
        self.message = message
        # Indicates whether the request was successful.
        self.success = success
        # The trace ID.
        self.trace_id = trace_id

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

        if self.message is not None:
            result['message'] = self.message

        if self.success is not None:
            result['success'] = self.success

        if self.trace_id is not None:
            result['traceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.GetMigrateApplicationResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class GetMigrateApplicationResponseBodyData(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        result: List[main_models.GetMigrateApplicationResponseBodyDataResult] = None,
        total_size: int = None,
    ):
        # The current page number.
        self.current_page = current_page
        # The number of entries per page.
        self.page_size = page_size
        # The list of results.
        self.result = result
        # The total number of entries.
        self.total_size = total_size

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['currentPage'] = self.current_page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        result['result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['result'].append(k1.to_map() if k1 else None)

        if self.total_size is not None:
            result['totalSize'] = self.total_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        self.result = []
        if m.get('result') is not None:
            for k1 in m.get('result'):
                temp_model = main_models.GetMigrateApplicationResponseBodyDataResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('totalSize') is not None:
            self.total_size = m.get('totalSize')

        return self

class GetMigrateApplicationResponseBodyDataResult(DaraModel):
    def __init__(
        self,
        app_detail_state: str = None,
        binary_cleaned: int = None,
        create_time: int = None,
        extra_info: main_models.GetMigrateApplicationResponseBodyDataResultExtraInfo = None,
        migration_id: str = None,
        migration_type: int = None,
        owner: str = None,
        region_id: str = None,
        state: str = None,
        state_percent: str = None,
        update_time: int = None,
    ):
        # The detailed status of the application.
        self.app_detail_state = app_detail_state
        # Indicates whether binary resources are cleaned up. Valid values: 0: not cleaned up. 1: cleaned up.
        self.binary_cleaned = binary_cleaned
        # The creation time.
        self.create_time = create_time
        # The additional information.
        self.extra_info = extra_info
        # The migration ID.
        self.migration_id = migration_id
        # The operation type of the migration task. Valid values: 1: import. 2: export. 3: clone.
        self.migration_type = migration_type
        # The executor.
        self.owner = owner
        # regionId
        self.region_id = region_id
        # The application migration status. Valid values: failed: Failed. finished: Succeeded.
        self.state = state
        # The task progress percentage, stored as a floating-point number. For example, if the API returns 0.33, the progress bar displays 33%.
        self.state_percent = state_percent
        # The update time.
        self.update_time = update_time

    def validate(self):
        if self.extra_info:
            self.extra_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_detail_state is not None:
            result['appDetailState'] = self.app_detail_state

        if self.binary_cleaned is not None:
            result['binaryCleaned'] = self.binary_cleaned

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.extra_info is not None:
            result['extraInfo'] = self.extra_info.to_map()

        if self.migration_id is not None:
            result['migrationId'] = self.migration_id

        if self.migration_type is not None:
            result['migrationType'] = self.migration_type

        if self.owner is not None:
            result['owner'] = self.owner

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.state is not None:
            result['state'] = self.state

        if self.state_percent is not None:
            result['statePercent'] = self.state_percent

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appDetailState') is not None:
            self.app_detail_state = m.get('appDetailState')

        if m.get('binaryCleaned') is not None:
            self.binary_cleaned = m.get('binaryCleaned')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('extraInfo') is not None:
            temp_model = main_models.GetMigrateApplicationResponseBodyDataResultExtraInfo()
            self.extra_info = temp_model.from_map(m.get('extraInfo'))

        if m.get('migrationId') is not None:
            self.migration_id = m.get('migrationId')

        if m.get('migrationType') is not None:
            self.migration_type = m.get('migrationType')

        if m.get('owner') is not None:
            self.owner = m.get('owner')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('state') is not None:
            self.state = m.get('state')

        if m.get('statePercent') is not None:
            self.state_percent = m.get('statePercent')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        return self

class GetMigrateApplicationResponseBodyDataResultExtraInfo(DaraModel):
    def __init__(
        self,
        app_json_file: str = None,
        error_msg: str = None,
    ):
        # appJsonFile
        self.app_json_file = app_json_file
        # The error message.
        self.error_msg = error_msg

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_json_file is not None:
            result['appJsonFile'] = self.app_json_file

        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appJsonFile') is not None:
            self.app_json_file = m.get('appJsonFile')

        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')

        return self

