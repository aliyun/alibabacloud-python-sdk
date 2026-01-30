# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeInvocationResultsResponseBody(DaraModel):
    def __init__(
        self,
        invocation: main_models.DescribeInvocationResultsResponseBodyInvocation = None,
        request_id: str = None,
    ):
        # The execution status of the command task. Valid values:
        # 
        # *   Running:
        # 
        #     *   Scheduled task: Before you stop the scheduled execution of the command, the execution state is always Running.
        #     *   One-time task: If the command is being run on instances, the execution state is Running.
        # 
        # *   Finished:
        # 
        #     *   Scheduled task: The execution state can never be Finished.
        #     *   One-time task: The execution is complete on all instances, or the execution is stopped on some instances and is complete on the other instances.
        # 
        # *   Success:
        # 
        #     *   One-time task: The execution is complete, and the exit code is 0.
        #     *   Scheduled task: The last execution is complete, the exit code is 0, and the specified period ends.
        # 
        # *   Failed:
        # 
        #     *   Scheduled task: The execution state can never be Failed.
        #     *   One-time task: The execution fails on all instances.
        # 
        # *   PartialFailed:
        # 
        #     *   Scheduled task: The execution state can never be PartialFailed.
        #     *   One-time task: The execution fails on some instances.
        # 
        # *   Stopped: The task is stopped.
        # 
        # *   Stopping: The task is being stopped.
        self.invocation = invocation
        # The ID of the command.
        self.request_id = request_id

    def validate(self):
        if self.invocation:
            self.invocation.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.invocation is not None:
            result['Invocation'] = self.invocation.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Invocation') is not None:
            temp_model = main_models.DescribeInvocationResultsResponseBodyInvocation()
            self.invocation = temp_model.from_map(m.get('Invocation'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeInvocationResultsResponseBodyInvocation(DaraModel):
    def __init__(
        self,
        invocation_results: main_models.DescribeInvocationResultsResponseBodyInvocationInvocationResults = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The maximum number of entries per page.
        # 
        # Valid values: 1 to 50.
        # 
        # Default value: 10.
        self.invocation_results = invocation_results
        # >  This parameter will be removed in the future. We recommend that you use NextToken and MaxResults for a paged query.
        self.next_token = next_token
        # The encoding mode of the `CommandContent` and `Output` values in the response. Valid values:
        # 
        # *   PlainText: returns the original command content and command output.
        # *   Base64: returns the Base64-encoded command content and command output.
        # 
        # Default value: Base64.
        self.page_number = page_number
        # Specifies whether to return the results of historical scheduled executions. Valid values:
        # 
        # *   true: returns the results of historical scheduled executions. If you set this parameter to true, you must set InvokeId to the ID of a task that is run on a schedule (RepeatMode set to Period) or on each system startup (RepeatMode set to EveryReboot).
        # *   false: does not return the results of historical scheduled executions.
        # 
        # Default value: false.
        self.page_size = page_size
        # >  This parameter will be removed in the future. We recommend that you use NextToken and MaxResults for a paged query.
        self.total_count = total_count

    def validate(self):
        if self.invocation_results:
            self.invocation_results.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.invocation_results is not None:
            result['InvocationResults'] = self.invocation_results.to_map()

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InvocationResults') is not None:
            temp_model = main_models.DescribeInvocationResultsResponseBodyInvocationInvocationResults()
            self.invocation_results = temp_model.from_map(m.get('InvocationResults'))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeInvocationResultsResponseBodyInvocationInvocationResults(DaraModel):
    def __init__(
        self,
        invocation_result: List[main_models.DescribeInvocationResultsResponseBodyInvocationInvocationResultsInvocationResult] = None,
    ):
        self.invocation_result = invocation_result

    def validate(self):
        if self.invocation_result:
            for v1 in self.invocation_result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InvocationResult'] = []
        if self.invocation_result is not None:
            for k1 in self.invocation_result:
                result['InvocationResult'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.invocation_result = []
        if m.get('InvocationResult') is not None:
            for k1 in m.get('InvocationResult'):
                temp_model = main_models.DescribeInvocationResultsResponseBodyInvocationInvocationResultsInvocationResult()
                self.invocation_result.append(temp_model.from_map(k1))

        return self

class DescribeInvocationResultsResponseBodyInvocationInvocationResultsInvocationResult(DaraModel):
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
        launcher: str = None,
        oss_output_delivery: str = None,
        oss_output_error_code: str = None,
        oss_output_error_info: str = None,
        oss_output_status: str = None,
        oss_output_uri: str = None,
        output: str = None,
        repeats: int = None,
        start_time: str = None,
        stop_time: str = None,
        tags: main_models.DescribeInvocationResultsResponseBodyInvocationInvocationResultsInvocationResultTags = None,
        termination_mode: str = None,
        username: str = None,
    ):
        # The error message returned when the command failed to be sent or run. Valid values:
        # 
        # *   If this parameter is empty, the command was run as expected.
        # *   The security group rules denied access to the aliyun service.
        # *   The specified instance does not exist.
        # *   The specified instance was released during task execution.
        # *   The specified instance was not running during task execution.
        # *   The OS type of the instance does not support the specified command type.
        # *   The specified account does not exist.
        # *   The specified directory does not exist.
        # *   The cron expression is invalid.
        # *   The aliyun service is not running on the instance.
        # *   The aliyun service in the instance does not response.
        # *   The aliyun service in the instance is upgrading during task execution.
        # *   The aliyun service in the instance need to be upgraded to at least version to support the feature. indicates the earliest version that supports the feature. indicates the name of the feature.
        # *   The command delivery has been timeout.
        # *   The command execution has been timeout.
        # *   The command execution got an exception.
        # *   The command execution exit code is not zero.
        # *   The specified instance was released during task execution.
        self.command_id = command_id
        # Command to execute the Output OSS delivery configuration.
        self.container_id = container_id
        # The execution status on a single instance. Valid values:
        # 
        # *   Pending: The command is being verified or sent.
        # 
        # *   Invalid: The specified command type or parameter is invalid.
        # 
        # *   Aborted: The command failed to be sent to the instance. To send a command to an instance, make sure that the instance is in the Running state and the command can be sent to the instance within 1 minute.
        # 
        # *   Running: The command is being run on the instance.
        # 
        # *   Success:
        # 
        #     *   One-time task: The execution was complete, and the exit code was 0.
        #     *   Scheduled task: The last execution was complete, the exit code was 0, and the specified period ended.
        # 
        # *   Failed:
        # 
        #     *   One-time task: The execution was complete, but the exit code was not 0.
        #     *   Scheduled task: The last execution was complete, but the exit code was not 0. The specified period was about to end.
        # 
        # *   Error: The execution cannot proceed due to an exception.
        # 
        # *   Timeout: The execution timed out.
        # 
        # *   Cancelled: The execution was canceled before it started.
        # 
        # *   Stopping: The command task is being stopped.
        # 
        # *   Terminated: The execution was terminated before completion.
        # 
        # *   Scheduled:
        # 
        #     *   One-time task: The execution state can never be Scheduled.
        #     *   Scheduled task: The command is waiting to be run.
        self.container_name = container_name
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of NextToken.
        self.dropped = dropped
        # The time when the command started to be run on the instance.
        self.error_code = error_code
        # The ID of the request.
        self.error_info = error_info
        # The key of tag N of the command task. Valid values of N: 1 to 20. The tag key cannot be an empty string.
        # 
        # If a single tag is specified to query resources, up to 1,000 resources that have this tag added can be displayed in the response. If multiple tags are specified to query resources, up to 1,000 resources that have all these tags added can be displayed in the response. To query more than 1,000 resources that have specified tags added, call the [ListTagResources](https://help.aliyun.com/document_detail/110425.html) operation.
        # 
        # The tag key can be up to 64 characters in length and cannot start with `acs:` or `aliyun`. It cannot contain `http://` or `https://`.
        self.exit_code = exit_code
        # The total number of the commands.
        self.finished_time = finished_time
        # The value of tag N of the command task. Valid values of N: 1 to 20. The tag value can be an empty string.
        # 
        # The tag value can be up to 128 characters in length and cannot contain `http://` or `https://`.
        self.instance_id = instance_id
        # The tag of the command task.
        self.invocation_status = invocation_status
        # The number of times that the command was run on the instance.
        # 
        # *   If the command is set to run only once, the value is 0 or 1.
        # *   If the command is set to run on a schedule, the value is the number of times that the command has been run on the instance.
        self.invoke_id = invoke_id
        # The page number.
        self.invoke_record_status = invoke_record_status
        # The exit code of the command task.
        # 
        # *   For Linux instances, the value is the exit code of the shell command.
        # *   For Windows instances, the value is the exit code of the batch or PowerShell command.
        self.launcher = launcher
        # The tags of the command task.
        self.oss_output_delivery = oss_output_delivery
        self.oss_output_error_code = oss_output_error_code
        self.oss_output_error_info = oss_output_error_info
        # The execution results.
        self.oss_output_status = oss_output_status
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.oss_output_uri = oss_output_uri
        # The instance ID.
        self.output = output
        # The number of entries per page.
        self.repeats = repeats
        # Details about the execution results.
        self.start_time = start_time
        # root
        self.stop_time = stop_time
        # The time when the command task was completed. If the command task times out, the end time is equal to the start time of the command task specified by `StartTime` plus the timeout period specified by `Timeout`.
        self.tags = tags
        # The execution status of the command. Valid values:
        # 
        # *   Running:
        # 
        #     *   Scheduled task: Before you stop the scheduled execution of the command, the execution state is always Running.
        #     *   One-time task: If the command is being run on instances, the execution state is Running.
        # 
        # *   Finished:
        # 
        #     *   Scheduled task: The execution state can never be Finished.
        #     *   One-time task: The execution was complete on all instances, or the execution was stopped on some instances and was complete on the other instances.
        # 
        # *   Failed:
        # 
        #     *   Scheduled task: The execution state can never be Failed.
        #     *   One-time task: The execution failed on all instances.
        # 
        # *   PartialFailed:
        # 
        #     *   Scheduled task: The execution state can never be PartialFailed.
        #     *   One-time task: The execution failed on some instances.
        # 
        # *   Stopped: The task was stopped.
        # 
        # *   Stopping: The task is being stopped.
        self.termination_mode = termination_mode
        # The size of the Output text that was truncated and discarded because the `Output` value exceeded 24 KB in size.
        self.username = username

    def validate(self):
        if self.tags:
            self.tags.validate()

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

        if self.launcher is not None:
            result['Launcher'] = self.launcher

        if self.oss_output_delivery is not None:
            result['OssOutputDelivery'] = self.oss_output_delivery

        if self.oss_output_error_code is not None:
            result['OssOutputErrorCode'] = self.oss_output_error_code

        if self.oss_output_error_info is not None:
            result['OssOutputErrorInfo'] = self.oss_output_error_info

        if self.oss_output_status is not None:
            result['OssOutputStatus'] = self.oss_output_status

        if self.oss_output_uri is not None:
            result['OssOutputUri'] = self.oss_output_uri

        if self.output is not None:
            result['Output'] = self.output

        if self.repeats is not None:
            result['Repeats'] = self.repeats

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.stop_time is not None:
            result['StopTime'] = self.stop_time

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.termination_mode is not None:
            result['TerminationMode'] = self.termination_mode

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

        if m.get('Launcher') is not None:
            self.launcher = m.get('Launcher')

        if m.get('OssOutputDelivery') is not None:
            self.oss_output_delivery = m.get('OssOutputDelivery')

        if m.get('OssOutputErrorCode') is not None:
            self.oss_output_error_code = m.get('OssOutputErrorCode')

        if m.get('OssOutputErrorInfo') is not None:
            self.oss_output_error_info = m.get('OssOutputErrorInfo')

        if m.get('OssOutputStatus') is not None:
            self.oss_output_status = m.get('OssOutputStatus')

        if m.get('OssOutputUri') is not None:
            self.oss_output_uri = m.get('OssOutputUri')

        if m.get('Output') is not None:
            self.output = m.get('Output')

        if m.get('Repeats') is not None:
            self.repeats = m.get('Repeats')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StopTime') is not None:
            self.stop_time = m.get('StopTime')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeInvocationResultsResponseBodyInvocationInvocationResultsInvocationResultTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('TerminationMode') is not None:
            self.termination_mode = m.get('TerminationMode')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        return self

class DescribeInvocationResultsResponseBodyInvocationInvocationResultsInvocationResultTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeInvocationResultsResponseBodyInvocationInvocationResultsInvocationResultTagsTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeInvocationResultsResponseBodyInvocationInvocationResultsInvocationResultTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeInvocationResultsResponseBodyInvocationInvocationResultsInvocationResultTagsTag(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The output delivery status of the command execution. Valid values:
        # 
        # *   InProgress: The delivery is in progress.
        # *   Finished: The delivery is complete.
        # *   Failed: The delivery failed.
        self.tag_key = tag_key
        # The username used to run the command on the instance.
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

