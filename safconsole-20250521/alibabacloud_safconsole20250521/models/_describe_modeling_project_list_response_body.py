# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_safconsole20250521 import models as main_models
from darabonba.model import DaraModel

class DescribeModelingProjectListResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        current_page: int = None,
        page_size: int = None,
        request_id: str = None,
        result_object: List[main_models.DescribeModelingProjectListResponseBodyResultObject] = None,
        success: bool = None,
        total_item: int = None,
        total_page: int = None,
    ):
        # Status code. A return value of 200 indicates success.
        self.code = code
        # Current page.
        self.current_page = current_page
        # Pagination parameter: number of items per page, with a default value of 10.
        self.page_size = page_size
        # Request ID.
        self.request_id = request_id
        # Returned result.
        self.result_object = result_object
        # Indicates whether the call was successful.
        # 
        # - **true**: Call succeeded.
        # - **false**: Call failed.
        self.success = success
        # Total number of records.
        self.total_item = total_item
        # Total number of pages.
        self.total_page = total_page

    def validate(self):
        if self.result_object:
            for v1 in self.result_object:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ResultObject'] = []
        if self.result_object is not None:
            for k1 in self.result_object:
                result['ResultObject'].append(k1.to_map() if k1 else None)

        if self.success is not None:
            result['Success'] = self.success

        if self.total_item is not None:
            result['TotalItem'] = self.total_item

        if self.total_page is not None:
            result['TotalPage'] = self.total_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result_object = []
        if m.get('ResultObject') is not None:
            for k1 in m.get('ResultObject'):
                temp_model = main_models.DescribeModelingProjectListResponseBodyResultObject()
                self.result_object.append(temp_model.from_map(k1))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalItem') is not None:
            self.total_item = m.get('TotalItem')

        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')

        return self

class DescribeModelingProjectListResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        env_status: str = None,
        login_account: str = None,
        modeling_status: str = None,
        project_id: str = None,
        project_name: str = None,
        start_time: int = None,
    ):
        # End time of the secure modeling project.
        self.end_time = end_time
        # Secure environment status.
        self.env_status = env_status
        # Login account.
        self.login_account = login_account
        # Modeling project status.
        self.modeling_status = modeling_status
        # Project ID.
        self.project_id = project_id
        # Project name.
        self.project_name = project_name
        # Start time of the secure modeling project.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.env_status is not None:
            result['EnvStatus'] = self.env_status

        if self.login_account is not None:
            result['LoginAccount'] = self.login_account

        if self.modeling_status is not None:
            result['ModelingStatus'] = self.modeling_status

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EnvStatus') is not None:
            self.env_status = m.get('EnvStatus')

        if m.get('LoginAccount') is not None:
            self.login_account = m.get('LoginAccount')

        if m.get('ModelingStatus') is not None:
            self.modeling_status = m.get('ModelingStatus')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

