# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudcallcenter20200701 import models as main_models
from darabonba.model import DaraModel

class ListCasesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListCasesResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

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
            temp_model = main_models.ListCasesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListCasesResponseBodyData(DaraModel):
    def __init__(
        self,
        list: List[main_models.ListCasesResponseBodyDataList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.list = list
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

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

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.ListCasesResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListCasesResponseBodyDataList(DaraModel):
    def __init__(
        self,
        abandon_type: str = None,
        attempt_count: int = None,
        case_id: str = None,
        custom_variables: str = None,
        expand_info: str = None,
        failure_reason: str = None,
        phone_number: str = None,
        state: str = None,
    ):
        self.abandon_type = abandon_type
        self.attempt_count = attempt_count
        self.case_id = case_id
        self.custom_variables = custom_variables
        self.expand_info = expand_info
        self.failure_reason = failure_reason
        self.phone_number = phone_number
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.abandon_type is not None:
            result['AbandonType'] = self.abandon_type

        if self.attempt_count is not None:
            result['AttemptCount'] = self.attempt_count

        if self.case_id is not None:
            result['CaseId'] = self.case_id

        if self.custom_variables is not None:
            result['CustomVariables'] = self.custom_variables

        if self.expand_info is not None:
            result['ExpandInfo'] = self.expand_info

        if self.failure_reason is not None:
            result['FailureReason'] = self.failure_reason

        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AbandonType') is not None:
            self.abandon_type = m.get('AbandonType')

        if m.get('AttemptCount') is not None:
            self.attempt_count = m.get('AttemptCount')

        if m.get('CaseId') is not None:
            self.case_id = m.get('CaseId')

        if m.get('CustomVariables') is not None:
            self.custom_variables = m.get('CustomVariables')

        if m.get('ExpandInfo') is not None:
            self.expand_info = m.get('ExpandInfo')

        if m.get('FailureReason') is not None:
            self.failure_reason = m.get('FailureReason')

        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

