# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListBusinessResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListBusinessResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Details of workflows.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The request ID. Used for troubleshooting when an error occurs.
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
            temp_model = main_models.ListBusinessResponseBodyData()
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

class ListBusinessResponseBodyData(DaraModel):
    def __init__(
        self,
        business: List[main_models.ListBusinessResponseBodyDataBusiness] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # Information about the workflow list.
        self.business = business
        # The current page number.
        self.page_number = page_number
        # The number of records on the current page.
        self.page_size = page_size
        # The total number of records that meet the query conditions.
        self.total_count = total_count

    def validate(self):
        if self.business:
            for v1 in self.business:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Business'] = []
        if self.business is not None:
            for k1 in self.business:
                result['Business'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.business = []
        if m.get('Business') is not None:
            for k1 in m.get('Business'):
                temp_model = main_models.ListBusinessResponseBodyDataBusiness()
                self.business.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListBusinessResponseBodyDataBusiness(DaraModel):
    def __init__(
        self,
        business_id: int = None,
        business_name: str = None,
        description: str = None,
        owner: str = None,
        project_id: int = None,
        use_type: str = None,
    ):
        # The workflow ID.
        self.business_id = business_id
        # The name of the workflow.
        self.business_name = business_name
        # The description of the workflow.
        self.description = description
        # The owner of the workflow.
        self.owner = owner
        # The ID of the workspace to which the workflow belongs.
        self.project_id = project_id
        # The module to which the workflow belongs. Valid values: NORMAL (Data Studio) and MANUAL_BIZ (Manually Triggered Workflow).
        self.use_type = use_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_id is not None:
            result['BusinessId'] = self.business_id

        if self.business_name is not None:
            result['BusinessName'] = self.business_name

        if self.description is not None:
            result['Description'] = self.description

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.use_type is not None:
            result['UseType'] = self.use_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessId') is not None:
            self.business_id = m.get('BusinessId')

        if m.get('BusinessName') is not None:
            self.business_name = m.get('BusinessName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('UseType') is not None:
            self.use_type = m.get('UseType')

        return self

