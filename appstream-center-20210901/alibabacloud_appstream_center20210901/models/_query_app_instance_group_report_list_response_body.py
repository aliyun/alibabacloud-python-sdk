# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class QueryAppInstanceGroupReportListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        index_data: List[main_models.QueryAppInstanceGroupReportListResponseBodyIndexData] = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
    ):
        # The business status code. A value of `200` indicates that the request is processed. Other values indicate that the processing failed.
        self.code = code
        # The list of app instance group report data.
        self.index_data = index_data
        # The description of the request processing result. If the request is successful, `success` is usually returned.
        self.message = message
        # The page number corresponding to the current response.
        self.page_number = page_number
        # The number of entries per page used in the current response.
        self.page_size = page_size
        # The unique identifier of the current request, which can be used to troubleshoot request issues.
        self.request_id = request_id

    def validate(self):
        if self.index_data:
            for v1 in self.index_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['IndexData'] = []
        if self.index_data is not None:
            for k1 in self.index_data:
                result['IndexData'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.index_data = []
        if m.get('IndexData') is not None:
            for k1 in m.get('IndexData'):
                temp_model = main_models.QueryAppInstanceGroupReportListResponseBodyIndexData()
                self.index_data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class QueryAppInstanceGroupReportListResponseBodyIndexData(DaraModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        app_instance_group_name: str = None,
        status: str = None,
    ):
        # The ID of the app instance group.
        self.app_instance_group_id = app_instance_group_id
        # The name of the app instance group.
        self.app_instance_group_name = app_instance_group_name
        # The current status of the app instance group.
        # 
        # Valid values:
        # 
        # - `DEPLOYING`: Deploying.
        # - `DEPLOYED`: Deployed but not published.
        # - `PUBLISHED`: Published and available to provide services based on the current configurations.
        # - `STOPPING`: Stopping.
        # - `STOPPED`: Stopped.
        # - `MAINTAINING`: Maintaining.
        # - `FAILED`: Deployment or running failed.
        # - `MAINTAIN_FAILED`: Maintenance failed.
        # - `DELETING`: Deleting.
        # - `DELETED`: Deleted.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id

        if self.app_instance_group_name is not None:
            result['AppInstanceGroupName'] = self.app_instance_group_name

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')

        if m.get('AppInstanceGroupName') is not None:
            self.app_instance_group_name = m.get('AppInstanceGroupName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

