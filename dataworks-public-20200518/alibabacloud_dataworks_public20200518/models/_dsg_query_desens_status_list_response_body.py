# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class DsgQueryDesensStatusListResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DsgQueryDesensStatusListResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.http_status_code = http_status_code
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
            temp_model = main_models.DsgQueryDesensStatusListResponseBodyData()
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

class DsgQueryDesensStatusListResponseBodyData(DaraModel):
    def __init__(
        self,
        page_data: List[main_models.DsgQueryDesensStatusListResponseBodyDataPageData] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.page_data = page_data
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.page_data:
            for v1 in self.page_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PageData'] = []
        if self.page_data is not None:
            for k1 in self.page_data:
                result['PageData'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.page_data = []
        if m.get('PageData') is not None:
            for k1 in m.get('PageData'):
                temp_model = main_models.DsgQueryDesensStatusListResponseBodyDataPageData()
                self.page_data.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DsgQueryDesensStatusListResponseBodyDataPageData(DaraModel):
    def __init__(
        self,
        desens_status: int = None,
        handle_space: str = None,
        id: int = None,
        workspace_identifier: str = None,
        workspace_name: str = None,
    ):
        self.desens_status = desens_status
        self.handle_space = handle_space
        self.id = id
        self.workspace_identifier = workspace_identifier
        self.workspace_name = workspace_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desens_status is not None:
            result['DesensStatus'] = self.desens_status

        if self.handle_space is not None:
            result['HandleSpace'] = self.handle_space

        if self.id is not None:
            result['Id'] = self.id

        if self.workspace_identifier is not None:
            result['WorkspaceIdentifier'] = self.workspace_identifier

        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesensStatus') is not None:
            self.desens_status = m.get('DesensStatus')

        if m.get('HandleSpace') is not None:
            self.handle_space = m.get('HandleSpace')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('WorkspaceIdentifier') is not None:
            self.workspace_identifier = m.get('WorkspaceIdentifier')

        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')

        return self

