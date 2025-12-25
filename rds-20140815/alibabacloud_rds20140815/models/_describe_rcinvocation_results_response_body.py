# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeRCInvocationResultsResponseBody(DaraModel):
    def __init__(
        self,
        invocation_results: List[main_models.DescribeRCInvocationResultsResponseBodyInvocationResults] = None,
        next_token: str = None,
        page_number: str = None,
        page_size: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.invocation_results = invocation_results
        # This parameter is required.
        self.next_token = next_token
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.invocation_results:
            for v1 in self.invocation_results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InvocationResults'] = []
        if self.invocation_results is not None:
            for k1 in self.invocation_results:
                result['InvocationResults'].append(k1.to_map() if k1 else None)

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
        self.invocation_results = []
        if m.get('InvocationResults') is not None:
            for k1 in m.get('InvocationResults'):
                temp_model = main_models.DescribeRCInvocationResultsResponseBodyInvocationResults()
                self.invocation_results.append(temp_model.from_map(k1))

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

class DescribeRCInvocationResultsResponseBodyInvocationResults(DaraModel):
    def __init__(
        self,
        command_id: str = None,
        container_id: str = None,
        container_name: str = None,
        dropped: int = None,
        error_code: str = None,
        error_info: str = None,
        exit_code: int = None,
        finished_time: str = None,
        instance_id: str = None,
        invocation_status: str = None,
        invoke_id: str = None,
        invoke_record_status: str = None,
        output: str = None,
        repeats: str = None,
        start_time: str = None,
        stop_time: str = None,
        tags: List[main_models.DescribeRCInvocationResultsResponseBodyInvocationResultsTags] = None,
        username: str = None,
    ):
        self.command_id = command_id
        self.container_id = container_id
        self.container_name = container_name
        self.dropped = dropped
        self.error_code = error_code
        self.error_info = error_info
        self.exit_code = exit_code
        self.finished_time = finished_time
        self.instance_id = instance_id
        self.invocation_status = invocation_status
        self.invoke_id = invoke_id
        self.invoke_record_status = invoke_record_status
        self.output = output
        self.repeats = repeats
        self.start_time = start_time
        self.stop_time = stop_time
        self.tags = tags
        self.username = username

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.command_id is not None:
            result['CommandId'] = self.command_id

        if self.container_id is not None:
            result['ContainerId'] = self.container_id

        if self.container_name is not None:
            result['ContainerName'] = self.container_name

        if self.dropped is not None:
            result['Dropped'] = self.dropped

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_info is not None:
            result['ErrorInfo'] = self.error_info

        if self.exit_code is not None:
            result['ExitCode'] = self.exit_code

        if self.finished_time is not None:
            result['FinishedTime'] = self.finished_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.invocation_status is not None:
            result['InvocationStatus'] = self.invocation_status

        if self.invoke_id is not None:
            result['InvokeId'] = self.invoke_id

        if self.invoke_record_status is not None:
            result['InvokeRecordStatus'] = self.invoke_record_status

        if self.output is not None:
            result['Output'] = self.output

        if self.repeats is not None:
            result['Repeats'] = self.repeats

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.stop_time is not None:
            result['StopTime'] = self.stop_time

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.username is not None:
            result['Username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommandId') is not None:
            self.command_id = m.get('CommandId')

        if m.get('ContainerId') is not None:
            self.container_id = m.get('ContainerId')

        if m.get('ContainerName') is not None:
            self.container_name = m.get('ContainerName')

        if m.get('Dropped') is not None:
            self.dropped = m.get('Dropped')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorInfo') is not None:
            self.error_info = m.get('ErrorInfo')

        if m.get('ExitCode') is not None:
            self.exit_code = m.get('ExitCode')

        if m.get('FinishedTime') is not None:
            self.finished_time = m.get('FinishedTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InvocationStatus') is not None:
            self.invocation_status = m.get('InvocationStatus')

        if m.get('InvokeId') is not None:
            self.invoke_id = m.get('InvokeId')

        if m.get('InvokeRecordStatus') is not None:
            self.invoke_record_status = m.get('InvokeRecordStatus')

        if m.get('Output') is not None:
            self.output = m.get('Output')

        if m.get('Repeats') is not None:
            self.repeats = m.get('Repeats')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StopTime') is not None:
            self.stop_time = m.get('StopTime')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeRCInvocationResultsResponseBodyInvocationResultsTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('Username') is not None:
            self.username = m.get('Username')

        return self

class DescribeRCInvocationResultsResponseBodyInvocationResultsTags(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

