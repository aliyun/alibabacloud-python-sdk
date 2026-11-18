# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class ListCommandInvocationResultsResponseBody(DaraModel):
    def __init__(
        self,
        command_invocation_result_model: List[main_models.ListCommandInvocationResultsResponseBodyCommandInvocationResultModel] = None,
        max_results: int = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of command execution results. Each element corresponds to an execution record on a persistent session. If no records meet the conditions, an empty array is returned.
        self.command_invocation_result_model = command_invocation_result_model
        # This field is not returned in the current version. Use PageNumber, PageSize, and TotalCount for pagination.
        self.max_results = max_results
        # This field is not returned in the current version. Use PageNumber, PageSize, and TotalCount for pagination.
        self.next_token = next_token
        # The page number of the currently displayed query results. In the current version, this field always returns 0 and does not echo echo request parameter PageNumber. Refer to echo request parameter for the actual value.
        self.page_number = page_number
        # The number of query results per page. In the current version, this field always returns 0 and does not echo echo request parameter PageSize. Refer to echo request parameter for the actual value.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of query results. If no records meet the conditions, 0 is returned.
        self.total_count = total_count

    def validate(self):
        if self.command_invocation_result_model:
            for v1 in self.command_invocation_result_model:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CommandInvocationResultModel'] = []
        if self.command_invocation_result_model is not None:
            for k1 in self.command_invocation_result_model:
                result['CommandInvocationResultModel'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.command_invocation_result_model = []
        if m.get('CommandInvocationResultModel') is not None:
            for k1 in m.get('CommandInvocationResultModel'):
                temp_model = main_models.ListCommandInvocationResultsResponseBodyCommandInvocationResultModel()
                self.command_invocation_result_model.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListCommandInvocationResultsResponseBodyCommandInvocationResultModel(DaraModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        app_instance_id: str = None,
        app_instance_persistent_id: str = None,
        finish_time: str = None,
        invocation_id: str = None,
        invocation_status: str = None,
        output: str = None,
        start_time: str = None,
    ):
        # The ID of the delivery group to which the persistent session that executed the command belongs.
        self.app_instance_group_id = app_instance_group_id
        # The instance ID of the app that executed the command.
        self.app_instance_id = app_instance_id
        # The ID of the persistent session that executed the command.
        self.app_instance_persistent_id = app_instance_persistent_id
        # The time when the command execution finished. The time is in UTC and follows the RFC 3339 standard in the yyyy-MM-ddTHH:mm:ssZ format. It is an empty string if the command execution has not finished.
        self.finish_time = finish_time
        # The command execution ID, which is the same as the request parameter InvocationId.
        self.invocation_id = invocation_id
        # The execution status of the command on the persistent session, such as Pending (waiting to be executed), Running (executing), Success (executed successfully), and Timeout (execution timed out).
        self.invocation_status = invocation_status
        # The output content generated by the command execution, which is raw text. It is an empty string if the command has not finished or has no output.
        self.output = output
        # The time when the command started to execute. The time is in UTC and follows the RFC 3339 standard in the yyyy-MM-ddTHH:mm:ssZ format. It is an empty string if the command has not started to execute.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id

        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id

        if self.app_instance_persistent_id is not None:
            result['AppInstancePersistentId'] = self.app_instance_persistent_id

        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time

        if self.invocation_id is not None:
            result['InvocationId'] = self.invocation_id

        if self.invocation_status is not None:
            result['InvocationStatus'] = self.invocation_status

        if self.output is not None:
            result['Output'] = self.output

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')

        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')

        if m.get('AppInstancePersistentId') is not None:
            self.app_instance_persistent_id = m.get('AppInstancePersistentId')

        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')

        if m.get('InvocationId') is not None:
            self.invocation_id = m.get('InvocationId')

        if m.get('InvocationStatus') is not None:
            self.invocation_status = m.get('InvocationStatus')

        if m.get('Output') is not None:
            self.output = m.get('Output')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

