# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListProjectsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        page_result: main_models.ListProjectsResponseBodyPageResult = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.page_result = page_result
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.page_result:
            self.page_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.page_result is not None:
            result['PageResult'] = self.page_result.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageResult') is not None:
            temp_model = main_models.ListProjectsResponseBodyPageResult()
            self.page_result = temp_model.from_map(m.get('PageResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListProjectsResponseBodyPageResult(DaraModel):
    def __init__(
        self,
        project_list: List[main_models.ListProjectsResponseBodyPageResultProjectList] = None,
        total_count: int = None,
    ):
        self.project_list = project_list
        self.total_count = total_count

    def validate(self):
        if self.project_list:
            for v1 in self.project_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ProjectList'] = []
        if self.project_list is not None:
            for k1 in self.project_list:
                result['ProjectList'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.project_list = []
        if m.get('ProjectList') is not None:
            for k1 in m.get('ProjectList'):
                temp_model = main_models.ListProjectsResponseBodyPageResultProjectList()
                self.project_list.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListProjectsResponseBodyPageResultProjectList(DaraModel):
    def __init__(
        self,
        biz_unit_id: int = None,
        data_source_id: int = None,
        data_source_name: str = None,
        description: str = None,
        display_name: str = None,
        env: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        mode: str = None,
        name: str = None,
        owner: str = None,
        owner_name: str = None,
        realtime_data_source_id: int = None,
        realtime_data_source_name: str = None,
        type: str = None,
    ):
        self.biz_unit_id = biz_unit_id
        self.data_source_id = data_source_id
        self.data_source_name = data_source_name
        self.description = description
        self.display_name = display_name
        self.env = env
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.mode = mode
        self.name = name
        self.owner = owner
        self.owner_name = owner_name
        self.realtime_data_source_id = realtime_data_source_id
        self.realtime_data_source_name = realtime_data_source_name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_unit_id is not None:
            result['BizUnitId'] = self.biz_unit_id

        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id

        if self.data_source_name is not None:
            result['DataSourceName'] = self.data_source_name

        if self.description is not None:
            result['Description'] = self.description

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.env is not None:
            result['Env'] = self.env

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.name is not None:
            result['Name'] = self.name

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name

        if self.realtime_data_source_id is not None:
            result['RealtimeDataSourceId'] = self.realtime_data_source_id

        if self.realtime_data_source_name is not None:
            result['RealtimeDataSourceName'] = self.realtime_data_source_name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizUnitId') is not None:
            self.biz_unit_id = m.get('BizUnitId')

        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')

        if m.get('DataSourceName') is not None:
            self.data_source_name = m.get('DataSourceName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Env') is not None:
            self.env = m.get('Env')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')

        if m.get('RealtimeDataSourceId') is not None:
            self.realtime_data_source_id = m.get('RealtimeDataSourceId')

        if m.get('RealtimeDataSourceName') is not None:
            self.realtime_data_source_name = m.get('RealtimeDataSourceName')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

