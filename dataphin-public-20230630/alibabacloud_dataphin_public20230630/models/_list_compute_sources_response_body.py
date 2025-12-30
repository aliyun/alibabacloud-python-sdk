# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListComputeSourcesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        page_result: main_models.ListComputeSourcesResponseBodyPageResult = None,
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
            temp_model = main_models.ListComputeSourcesResponseBodyPageResult()
            self.page_result = temp_model.from_map(m.get('PageResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListComputeSourcesResponseBodyPageResult(DaraModel):
    def __init__(
        self,
        compute_source_list: List[main_models.ListComputeSourcesResponseBodyPageResultComputeSourceList] = None,
        total_count: int = None,
    ):
        self.compute_source_list = compute_source_list
        self.total_count = total_count

    def validate(self):
        if self.compute_source_list:
            for v1 in self.compute_source_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ComputeSourceList'] = []
        if self.compute_source_list is not None:
            for k1 in self.compute_source_list:
                result['ComputeSourceList'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.compute_source_list = []
        if m.get('ComputeSourceList') is not None:
            for k1 in m.get('ComputeSourceList'):
                temp_model = main_models.ListComputeSourcesResponseBodyPageResultComputeSourceList()
                self.compute_source_list.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListComputeSourcesResponseBodyPageResultComputeSourceList(DaraModel):
    def __init__(
        self,
        bind_project: bool = None,
        bind_project_id: int = None,
        bind_project_name: str = None,
        creator: str = None,
        creator_name: str = None,
        description: str = None,
        display_name: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        name: str = None,
        owner: str = None,
        owner_name: str = None,
        type: str = None,
    ):
        self.bind_project = bind_project
        self.bind_project_id = bind_project_id
        self.bind_project_name = bind_project_name
        self.creator = creator
        self.creator_name = creator_name
        self.description = description
        self.display_name = display_name
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.name = name
        self.owner = owner
        self.owner_name = owner_name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bind_project is not None:
            result['BindProject'] = self.bind_project

        if self.bind_project_id is not None:
            result['BindProjectId'] = self.bind_project_id

        if self.bind_project_name is not None:
            result['BindProjectName'] = self.bind_project_name

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.creator_name is not None:
            result['CreatorName'] = self.creator_name

        if self.description is not None:
            result['Description'] = self.description

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindProject') is not None:
            self.bind_project = m.get('BindProject')

        if m.get('BindProjectId') is not None:
            self.bind_project_id = m.get('BindProjectId')

        if m.get('BindProjectName') is not None:
            self.bind_project_name = m.get('BindProjectName')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('CreatorName') is not None:
            self.creator_name = m.get('CreatorName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

