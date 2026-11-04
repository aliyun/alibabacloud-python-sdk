# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_linkvisual20180120 import models as main_models
from darabonba.model import DaraModel

class QueryRecordPlansResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.QueryRecordPlansResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code returned if the call fails. For more information, see [Error codes](https://help.aliyun.com/document_detail/145071.html).
        self.code = code
        # The query information.
        self.data = data
        # The error message returned if the call fails.
        self.error_message = error_message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the call was successful. Valid values:
        # - **true**: The call was successful.
        # - **false**: The call failed.
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
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.QueryRecordPlansResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryRecordPlansResponseBodyData(DaraModel):
    def __init__(
        self,
        list: List[main_models.QueryRecordPlansResponseBodyDataList] = None,
        page: int = None,
        page_count: int = None,
        page_size: int = None,
        total: int = None,
    ):
        # The list of returned recording plan templates.
        self.list = list
        # The current page number.
        self.page = page
        # The total number of pages.
        self.page_count = page_count
        # The number of records returned on each page.
        self.page_size = page_size
        # The total number of recording plans returned.
        self.total = total

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
        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        if self.page is not None:
            result['Page'] = self.page

        if self.page_count is not None:
            result['PageCount'] = self.page_count

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.QueryRecordPlansResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class QueryRecordPlansResponseBodyDataList(DaraModel):
    def __init__(
        self,
        name: str = None,
        plan_id: str = None,
        template_id: str = None,
    ):
        # The name of the recording plan.
        self.name = name
        # The ID of the recording plan.
        self.plan_id = plan_id
        # The ID of the time template associated with the recording plan.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.plan_id is not None:
            result['PlanId'] = self.plan_id

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

