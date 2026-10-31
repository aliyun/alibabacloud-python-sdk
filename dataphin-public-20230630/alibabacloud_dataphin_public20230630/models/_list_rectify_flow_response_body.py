# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListRectifyFlowResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        page_result: main_models.ListRectifyFlowResponseBodyPageResult = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The backend response code.
        self.code = code
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The backend exception details.
        self.message = message
        # The pagination result.
        self.page_result = page_result
        # Id of the request
        self.request_id = request_id
        # Indicates whether the request is successful.
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
            temp_model = main_models.ListRectifyFlowResponseBodyPageResult()
            self.page_result = temp_model.from_map(m.get('PageResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListRectifyFlowResponseBodyPageResult(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListRectifyFlowResponseBodyPageResultData] = None,
        total_count: int = None,
    ):
        # The processes on the current page.
        self.data = data
        # The total number of processes.
        self.total_count = total_count

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListRectifyFlowResponseBodyPageResultData()
                self.data.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListRectifyFlowResponseBodyPageResultData(DaraModel):
    def __init__(
        self,
        finish_time: int = None,
        problem_count: int = None,
        rectify_id: int = None,
        rectify_name: str = None,
        rectify_priority: str = None,
        rectify_user: str = None,
        rectify_user_name: str = None,
        start_time: int = None,
        status: str = None,
        submit_user: str = None,
        submit_user_name: str = None,
        verify_user: str = None,
        verify_user_name: str = None,
    ):
        # The completion time. The value is a UNIX timestamp in milliseconds. If the process is not completed, this parameter is empty.
        self.finish_time = finish_time
        # The total number of issues in the current process.
        self.problem_count = problem_count
        # The process ID.
        self.rectify_id = rectify_id
        # The process name.
        self.rectify_name = rectify_name
        # The priority.
        self.rectify_priority = rectify_priority
        # The rectifier ID.
        self.rectify_user = rectify_user
        # The rectifier name.
        self.rectify_user_name = rectify_user_name
        # The start time. The value is a UNIX timestamp in milliseconds.
        self.start_time = start_time
        # The process status.
        self.status = status
        # The initiator ID.
        self.submit_user = submit_user
        # The initiator name.
        self.submit_user_name = submit_user_name
        # The verifier ID.
        self.verify_user = verify_user
        # The verifier name.
        self.verify_user_name = verify_user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time

        if self.problem_count is not None:
            result['ProblemCount'] = self.problem_count

        if self.rectify_id is not None:
            result['RectifyId'] = self.rectify_id

        if self.rectify_name is not None:
            result['RectifyName'] = self.rectify_name

        if self.rectify_priority is not None:
            result['RectifyPriority'] = self.rectify_priority

        if self.rectify_user is not None:
            result['RectifyUser'] = self.rectify_user

        if self.rectify_user_name is not None:
            result['RectifyUserName'] = self.rectify_user_name

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.submit_user is not None:
            result['SubmitUser'] = self.submit_user

        if self.submit_user_name is not None:
            result['SubmitUserName'] = self.submit_user_name

        if self.verify_user is not None:
            result['VerifyUser'] = self.verify_user

        if self.verify_user_name is not None:
            result['VerifyUserName'] = self.verify_user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')

        if m.get('ProblemCount') is not None:
            self.problem_count = m.get('ProblemCount')

        if m.get('RectifyId') is not None:
            self.rectify_id = m.get('RectifyId')

        if m.get('RectifyName') is not None:
            self.rectify_name = m.get('RectifyName')

        if m.get('RectifyPriority') is not None:
            self.rectify_priority = m.get('RectifyPriority')

        if m.get('RectifyUser') is not None:
            self.rectify_user = m.get('RectifyUser')

        if m.get('RectifyUserName') is not None:
            self.rectify_user_name = m.get('RectifyUserName')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubmitUser') is not None:
            self.submit_user = m.get('SubmitUser')

        if m.get('SubmitUserName') is not None:
            self.submit_user_name = m.get('SubmitUserName')

        if m.get('VerifyUser') is not None:
            self.verify_user = m.get('VerifyUser')

        if m.get('VerifyUserName') is not None:
            self.verify_user_name = m.get('VerifyUserName')

        return self

