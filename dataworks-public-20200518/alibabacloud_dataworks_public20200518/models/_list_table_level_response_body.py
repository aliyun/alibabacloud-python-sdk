# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class ListTableLevelResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
        table_level_info: main_models.ListTableLevelResponseBodyTableLevelInfo = None,
    ):
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success
        # The information about the table levels.
        self.table_level_info = table_level_info

    def validate(self):
        if self.table_level_info:
            self.table_level_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.table_level_info is not None:
            result['TableLevelInfo'] = self.table_level_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TableLevelInfo') is not None:
            temp_model = main_models.ListTableLevelResponseBodyTableLevelInfo()
            self.table_level_info = temp_model.from_map(m.get('TableLevelInfo'))

        return self

class ListTableLevelResponseBodyTableLevelInfo(DaraModel):
    def __init__(
        self,
        level_list: List[main_models.ListTableLevelResponseBodyTableLevelInfoLevelList] = None,
        total_count: int = None,
    ):
        # The list of table levels.
        self.level_list = level_list
        # The total number of table levels returned.
        self.total_count = total_count

    def validate(self):
        if self.level_list:
            for v1 in self.level_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LevelList'] = []
        if self.level_list is not None:
            for k1 in self.level_list:
                result['LevelList'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.level_list = []
        if m.get('LevelList') is not None:
            for k1 in m.get('LevelList'):
                temp_model = main_models.ListTableLevelResponseBodyTableLevelInfoLevelList()
                self.level_list.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListTableLevelResponseBodyTableLevelInfoLevelList(DaraModel):
    def __init__(
        self,
        description: str = None,
        level_id: int = None,
        level_type: int = None,
        name: str = None,
        project_id: int = None,
    ):
        # The description of the table level.
        self.description = description
        # The table level ID.
        self.level_id = level_id
        # The table level type. Valid values: 1 and 2. The value 1 indicates the logical level. The value 2 indicates the physical level.
        self.level_type = level_type
        # The name of the table level.
        self.name = name
        # The ID of the DataWorks workspace.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.level_id is not None:
            result['LevelId'] = self.level_id

        if self.level_type is not None:
            result['LevelType'] = self.level_type

        if self.name is not None:
            result['Name'] = self.name

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('LevelId') is not None:
            self.level_id = m.get('LevelId')

        if m.get('LevelType') is not None:
            self.level_type = m.get('LevelType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

