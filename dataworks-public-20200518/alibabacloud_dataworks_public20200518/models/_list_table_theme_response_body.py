# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class ListTableThemeResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListTableThemeResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The returned result.
        self.data = data
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

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.ListTableThemeResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

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

        return self

class ListTableThemeResponseBodyData(DaraModel):
    def __init__(
        self,
        theme_list: List[main_models.ListTableThemeResponseBodyDataThemeList] = None,
        total_count: int = None,
    ):
        # The list of table levels.
        self.theme_list = theme_list
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.theme_list:
            for v1 in self.theme_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ThemeList'] = []
        if self.theme_list is not None:
            for k1 in self.theme_list:
                result['ThemeList'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.theme_list = []
        if m.get('ThemeList') is not None:
            for k1 in m.get('ThemeList'):
                temp_model = main_models.ListTableThemeResponseBodyDataThemeList()
                self.theme_list.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListTableThemeResponseBodyDataThemeList(DaraModel):
    def __init__(
        self,
        create_time_stamp: int = None,
        creator: str = None,
        level: int = None,
        name: str = None,
        parent_id: int = None,
        project_id: int = None,
        theme_id: int = None,
    ):
        # The time when the table level was created.
        self.create_time_stamp = create_time_stamp
        # The creator of the table level.
        self.creator = creator
        # The level of the table folder. Valid values: 1 and 2. The value 1 indicates the first level. The value 2 indicates the second level.
        self.level = level
        # The name of the table level.
        self.name = name
        # The ancestor node ID.
        self.parent_id = parent_id
        # The DataWorks workspace ID.
        self.project_id = project_id
        # The table theme ID.
        self.theme_id = theme_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time_stamp is not None:
            result['CreateTimeStamp'] = self.create_time_stamp

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.level is not None:
            result['Level'] = self.level

        if self.name is not None:
            result['Name'] = self.name

        if self.parent_id is not None:
            result['ParentId'] = self.parent_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.theme_id is not None:
            result['ThemeId'] = self.theme_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTimeStamp') is not None:
            self.create_time_stamp = m.get('CreateTimeStamp')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ThemeId') is not None:
            self.theme_id = m.get('ThemeId')

        return self

