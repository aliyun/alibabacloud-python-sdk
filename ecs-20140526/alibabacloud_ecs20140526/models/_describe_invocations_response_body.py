# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeInvocationsResponseBody(DaraModel):
    def __init__(
        self,
        invocations: main_models.DescribeInvocationsResponseBodyInvocations = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The ID of instance N. When you specify this parameter, the system queries all the execution records of all the commands that run on the instance.
        self.invocations = invocations
        # The overall execution status of the command task. The value of this parameter depends on the execution states of the command task on all involved instances. Valid values:
        # 
        # *   Running:
        # 
        #     *   Scheduled task: Before you stop the scheduled execution of the command, the overall execution state is always Running.
        #     *   One-time task: If the command is being run on instances, the overall execution state is Running.
        # 
        # *   Finished:
        # 
        #     *   Scheduled task: The overall execution state can never be Finished.
        #     *   One-time task: The execution is complete on all instances, or the execution is stopped on some instances and is complete on the other instances.
        # 
        # *   Success: If the execution state on at least one instance is Success and the execution state on the other instances is Stopped or Success, the overall execution state is Success.
        # 
        #     *   One-time task: The execution is complete, and the exit code is 0.
        #     *   Scheduled task: The last execution is complete, the exit code is 0, and the specified period ends.
        # 
        # *   Failed:
        # 
        #     *   Scheduled task: The overall execution state can never be Failed.
        #     *   One-time task: The execution failed on all instances.
        # 
        # *   Stopped: The task is stopped.
        # 
        # *   Stopping: The task is being stopped.
        # 
        # *   PartialFailed: The task fails on some instances. If you specify both this parameter and `InstanceId`, this parameter does not take effect.
        # 
        # *   Pending: The command is being verified or sent. If the execution state on at least one instance is Pending, the overall execution state is Pending.
        # 
        # *   Scheduled: The command that is set to run on a schedule is sent and waiting to be run. If the execution state on at least one instance is Scheduled, the overall execution state is Scheduled.
        self.next_token = next_token
        # The command type. Valid values:
        # 
        # *   RunBatScript: batch command, applicable to Windows instances.
        # *   RunPowerShellScript: PowerShell command, applicable to Windows instances.
        # *   RunShellScript: shell command, applicable to Linux instances.
        self.page_number = page_number
        # The command ID. You can call the [DescribeCommands](https://help.aliyun.com/document_detail/64843.html) operation to query all available command IDs.
        self.page_size = page_size
        # The command name. If you specify both this parameter and `InstanceId`, this parameter does not take effect.
        self.request_id = request_id
        # Specifies whether the command is to be automatically run. Valid values:
        # 
        # *   true: The command is run by calling the `RunCommand` or `InvokeCommand` operation with `RepeatMode` set to `Period`, `NextRebootOnly`, or `EveryReboot`.
        # 
        # *   false: The command meets one of the following requirements:
        # 
        #     *   The command is run by calling the `RunCommand` or `InvokeCommand` operation with `RepeatMode` set to `Once`.
        #     *   The command task is canceled, stopped, or completed.
        # 
        # Default value: false.
        self.total_count = total_count

    def validate(self):
        if self.invocations:
            self.invocations.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.invocations is not None:
            result['Invocations'] = self.invocations.to_map()

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
        if m.get('Invocations') is not None:
            temp_model = main_models.DescribeInvocationsResponseBodyInvocations()
            self.invocations = temp_model.from_map(m.get('Invocations'))

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

class DescribeInvocationsResponseBodyInvocations(DaraModel):
    def __init__(
        self,
        invocation: List[main_models.DescribeInvocationsResponseBodyInvocationsInvocation] = None,
    ):
        self.invocation = invocation

    def validate(self):
        if self.invocation:
            for v1 in self.invocation:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Invocation'] = []
        if self.invocation is not None:
            for k1 in self.invocation:
                result['Invocation'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.invocation = []
        if m.get('Invocation') is not None:
            for k1 in m.get('Invocation'):
                temp_model = main_models.DescribeInvocationsResponseBodyInvocationsInvocation()
                self.invocation.append(temp_model.from_map(k1))

        return self

class DescribeInvocationsResponseBodyInvocationsInvocation(DaraModel):
    def __init__(
        self,
        command_content: str = None,
        command_description: str = None,
        command_id: str = None,
        command_name: str = None,
        command_type: str = None,
        container_id: str = None,
        container_name: str = None,
        creation_time: str = None,
        frequency: str = None,
        invocation_status: str = None,
        invoke_id: str = None,
        invoke_instances: main_models.DescribeInvocationsResponseBodyInvocationsInvocationInvokeInstances = None,
        invoke_status: str = None,
        launcher: str = None,
        oss_output_delivery: str = None,
        parameters: str = None,
        repeat_mode: str = None,
        tags: main_models.DescribeInvocationsResponseBodyInvocationsInvocationTags = None,
        termination_mode: str = None,
        timed: bool = None,
        timeout: int = None,
        username: str = None,
        working_dir: str = None,
    ):
        # The size of the Output text that was truncated and discarded because the Output value exceeded 24 KB in size.
        self.command_content = command_content
        # The pagination token that is used in the next request to retrieve a new page of results. You must specify the token that is obtained from the previous query as the value of NextToken.
        self.command_description = command_description
        # The time when the command process ended.
        self.command_id = command_id
        # The command output.
        # 
        # *   If ContentEncoding is set to PlainText in the request, the original command output is returned.
        # *   If ContentEncoding is set to Base64 in the request, the Base64-encoded command output is returned.
        self.command_name = command_name
        # The execution status of the command on a single instance.
        # 
        # >  We recommend that you ignore this parameter and check the value of `InvocationStatus` in the response to obtain the execution status.
        self.command_type = command_type
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
        self.container_id = container_id
        # The time when the command started to be run on the instance.
        self.container_name = container_name
        # The number of times that the command was run on the instance.
        # 
        # *   If the command is set to run only once, the value is 0 or 1.
        # *   If the command is set to run on a schedule, the value is the number of times that the command has been run on the instance.
        self.creation_time = creation_time
        # The command execution Output delivers the object URI to OSS. This field is an empty string when the delivery fails or is in progress.
        self.frequency = frequency
        # >  This parameter will be removed in the future. We recommend that you use NextToken and MaxResults for a paged query.
        self.invocation_status = invocation_status
        # The time when the command task was created.
        self.invoke_id = invoke_id
        # The tags that are added to the command.
        self.invoke_instances = invoke_instances
        # Indicates whether the command is to be automatically run.
        self.invoke_status = invoke_status
        # The output delivery status of the command execution. Valid values:
        # 
        # *   InProgress: The delivery is in progress.
        # *   Finished: The delivery is complete.
        # *   Failed: The delivery failed.
        self.launcher = launcher
        # Specifies whether to return the command outputs in the response.
        # 
        # *   true: The command outputs are returned. When this parameter is set to true, you must specify `InvokeId`, `InstanceId`, or both.
        # *   false: The command outputs are not returned.
        # 
        # Default value: false
        self.oss_output_delivery = oss_output_delivery
        # >  This parameter will be removed in the future. We recommend that you use NextToken and MaxResults for a paged query.
        self.parameters = parameters
        # The instance ID.
        self.repeat_mode = repeat_mode
        # The error code for the failure to send or run the command. Valid values:
        # 
        # *   If this parameter is empty, the command is run normally.
        # *   InstanceNotExists: The specified instance did not exist or was released.
        # *   InstanceReleased: The instance is released during command execution.
        # *   InstanceNotRunning: The instance was not running when the command started to be run.
        # *   CommandNotApplicable: The command was inapplicable to the specified instance.
        # *   AccountNotExists: The username specified to run the command did not exist.
        # *   DirectoryNotExists: The specified directory did not exist.
        # *   BadCronExpression: The specified cron expression for the execution schedule was invalid.
        # *   ClientNotRunning: Cloud Assistant Agent was not running.
        # *   ClientNotResponse: Cloud Assistant Agent does not respond.
        # *   ClientIsUpgrading: Cloud Assistant Agent is being upgraded.
        # *   ClientNeedUpgrade: Cloud Assistant Agent needed to be upgraded.
        # *   DeliveryTimeout: The request to send the command timed out.
        # *   ExecutionTimeout: The execution timed out.
        # *   ExecutionException: An exception occurred while the command was being executed.
        # *   ExecutionInterrupted: The command task was interrupted.
        # *   ExitCodeNonzero: The execution was complete, but the exit code was not 0.
        # *   SecurityGroupRuleDenied: Access to Cloud Assistant was denied by security group rules.
        # *   TaskConcurrencyLimit: The number of concurrent tasks exceeds the maximum limit.
        self.tags = tags
        # The time when the execution status was updated.
        self.termination_mode = termination_mode
        # The maximum number of entries per page.
        # 
        # Valid values: 1 to 50.
        # 
        # Default value: 10.
        self.timed = timed
        # The execution mode of the command. If you specify both this parameter and `InstanceId`, this parameter does not take effect. Valid values:
        # 
        # *   Once: The command is immediately run.
        # *   Period: The command is run on a schedule.
        # *   NextRebootOnly: The command is run the next time the instances start.
        # *   EveryReboot: The command is run every time the instances start.
        # 
        # This parameter is empty by default, which indicates that commands run in all modes are queried.
        self.timeout = timeout
        # The exit code of the execution. Valid values:
        # 
        # *   For Linux instances, the value is the exit code of the shell process.
        # *   For Windows instances, the value is the exit code of the batch or PowerShell process.
        self.username = username
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
        #     *   Scheduled task: The last execution was complete, but the exit code was not 0. The specified period is about to end.
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
        self.working_dir = working_dir

    def validate(self):
        if self.invoke_instances:
            self.invoke_instances.validate()
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.command_content is not None:
            result['CommandContent'] = self.command_content

        if self.command_description is not None:
            result['CommandDescription'] = self.command_description

        if self.command_id is not None:
            result['CommandId'] = self.command_id

        if self.command_name is not None:
            result['CommandName'] = self.command_name

        if self.command_type is not None:
            result['CommandType'] = self.command_type

        if self.container_id is not None:
            result['ContainerId'] = self.container_id

        if self.container_name is not None:
            result['ContainerName'] = self.container_name

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.frequency is not None:
            result['Frequency'] = self.frequency

        if self.invocation_status is not None:
            result['InvocationStatus'] = self.invocation_status

        if self.invoke_id is not None:
            result['InvokeId'] = self.invoke_id

        if self.invoke_instances is not None:
            result['InvokeInstances'] = self.invoke_instances.to_map()

        if self.invoke_status is not None:
            result['InvokeStatus'] = self.invoke_status

        if self.launcher is not None:
            result['Launcher'] = self.launcher

        if self.oss_output_delivery is not None:
            result['OssOutputDelivery'] = self.oss_output_delivery

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        if self.repeat_mode is not None:
            result['RepeatMode'] = self.repeat_mode

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.termination_mode is not None:
            result['TerminationMode'] = self.termination_mode

        if self.timed is not None:
            result['Timed'] = self.timed

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        if self.username is not None:
            result['Username'] = self.username

        if self.working_dir is not None:
            result['WorkingDir'] = self.working_dir

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommandContent') is not None:
            self.command_content = m.get('CommandContent')

        if m.get('CommandDescription') is not None:
            self.command_description = m.get('CommandDescription')

        if m.get('CommandId') is not None:
            self.command_id = m.get('CommandId')

        if m.get('CommandName') is not None:
            self.command_name = m.get('CommandName')

        if m.get('CommandType') is not None:
            self.command_type = m.get('CommandType')

        if m.get('ContainerId') is not None:
            self.container_id = m.get('ContainerId')

        if m.get('ContainerName') is not None:
            self.container_name = m.get('ContainerName')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Frequency') is not None:
            self.frequency = m.get('Frequency')

        if m.get('InvocationStatus') is not None:
            self.invocation_status = m.get('InvocationStatus')

        if m.get('InvokeId') is not None:
            self.invoke_id = m.get('InvokeId')

        if m.get('InvokeInstances') is not None:
            temp_model = main_models.DescribeInvocationsResponseBodyInvocationsInvocationInvokeInstances()
            self.invoke_instances = temp_model.from_map(m.get('InvokeInstances'))

        if m.get('InvokeStatus') is not None:
            self.invoke_status = m.get('InvokeStatus')

        if m.get('Launcher') is not None:
            self.launcher = m.get('Launcher')

        if m.get('OssOutputDelivery') is not None:
            self.oss_output_delivery = m.get('OssOutputDelivery')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        if m.get('RepeatMode') is not None:
            self.repeat_mode = m.get('RepeatMode')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeInvocationsResponseBodyInvocationsInvocationTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('TerminationMode') is not None:
            self.termination_mode = m.get('TerminationMode')

        if m.get('Timed') is not None:
            self.timed = m.get('Timed')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        if m.get('WorkingDir') is not None:
            self.working_dir = m.get('WorkingDir')

        return self

class DescribeInvocationsResponseBodyInvocationsInvocationTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeInvocationsResponseBodyInvocationsInvocationTagsTag] = None,
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
                temp_model = main_models.DescribeInvocationsResponseBodyInvocationsInvocationTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeInvocationsResponseBodyInvocationsInvocationTagsTag(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The command content.
        # 
        # *   If ContentEncoding is set to PlainText in the request, the original command content is returned.
        # *   If ContentEncoding is set to Base64 in the request, the Base64-encoded command content is returned.
        self.tag_key = tag_key
        # The execution path of the command.
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

class DescribeInvocationsResponseBodyInvocationsInvocationInvokeInstances(DaraModel):
    def __init__(
        self,
        invoke_instance: List[main_models.DescribeInvocationsResponseBodyInvocationsInvocationInvokeInstancesInvokeInstance] = None,
    ):
        self.invoke_instance = invoke_instance

    def validate(self):
        if self.invoke_instance:
            for v1 in self.invoke_instance:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InvokeInstance'] = []
        if self.invoke_instance is not None:
            for k1 in self.invoke_instance:
                result['InvokeInstance'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.invoke_instance = []
        if m.get('InvokeInstance') is not None:
            for k1 in m.get('InvokeInstance'):
                temp_model = main_models.DescribeInvocationsResponseBodyInvocationsInvocationInvokeInstancesInvokeInstance()
                self.invoke_instance.append(temp_model.from_map(k1))

        return self

class DescribeInvocationsResponseBodyInvocationsInvocationInvokeInstancesInvokeInstance(DaraModel):
    def __init__(
        self,
        creation_time: str = None,
        dropped: int = None,
        error_code: str = None,
        error_info: str = None,
        exit_code: int = None,
        finish_time: str = None,
        instance_id: str = None,
        instance_invoke_status: str = None,
        invocation_status: str = None,
        oss_output_error_code: str = None,
        oss_output_error_info: str = None,
        oss_output_status: str = None,
        oss_output_uri: str = None,
        output: str = None,
        repeats: int = None,
        start_time: str = None,
        stop_time: str = None,
        timed: bool = None,
        update_time: str = None,
    ):
        # The command description.
        self.creation_time = creation_time
        # The value of tag N of the command. You can specify up to 20 tag values for the command. The tag value can be an empty string. It can be up to 128 characters in length and cannot contain `http://` or `https://`.
        self.dropped = dropped
        # The instances on which the command was run.
        self.error_code = error_code
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.error_info = error_info
        # The total number of the commands.
        self.exit_code = exit_code
        # The custom parameters in the command.
        self.finish_time = finish_time
        # The number of entries returned on each page.
        self.instance_id = instance_id
        # The page number of the returned page.
        self.instance_invoke_status = instance_invoke_status
        # The key of tag N of the command. You can specify up to 20 tag keys for the command. The tag key cannot be an empty string.
        # 
        # If a single tag is specified to query resources, up to 1,000 resources that have this tag added can be displayed in the response. If multiple tags are specified to query resources, up to 1,000 resources that have all these tags added can be displayed in the response. To query more than 1,000 resources that have specified tags added, call the [ListTagResources](https://help.aliyun.com/document_detail/110425.html) operation.
        # 
        # The tag key can be up to 64 characters in length and cannot contain `http://` or `https://`. The tag key cannot start with `acs:` or `aliyun`.
        self.invocation_status = invocation_status
        self.oss_output_error_code = oss_output_error_code
        self.oss_output_error_info = oss_output_error_info
        # The overall execution status of the command task. The value of this parameter depends on the execution status of the command task on all the involved instances. Valid values:
        # 
        # *   Pending: The command is being verified or sent. When the execution state on at least one instance is Pending, the overall execution state is Pending.
        # 
        # *   Scheduled: The command that is set to run on a schedule was sent and waiting to be run. When the execution state on at least one instance is Scheduled, the overall execution state is Scheduled.
        # 
        # *   Running: The command is being run on the instances. When the execution state on at least one instance is Running, the overall execution state is Running.
        # 
        # *   Success: When the execution state on at least one instance is Success and the execution state on the other instances is Stopped or Success, the overall execution state is Success.
        # 
        #     *   One-time task: The execution was complete, and the exit code was 0.
        #     *   Scheduled task: The last execution was complete, the exit code was 0, and the specified period ended.
        # 
        # *   Failed: When the execution state on all instances is Stopped or Failed, the overall execution state is Failed. When the execution state on an instance is one of the following values, Failed is returned as the overall execution state:
        # 
        #     *   Invalid: The command is invalid.
        #     *   Aborted: The command failed to be sent.
        #     *   Failed: The execution was complete, but the exit code was not 0.
        #     *   Timeout: The execution timed out.
        #     *   Error: An error occurred while the command was being run.
        # 
        # *   Stopping: The command task is being stopped. When the execution state on at least one instance is Stopping, the overall execution state is Stopping.
        # 
        # *   Stopped: The task was stopped. When the execution state on all instances is Stopped, the overall execution state is Stopped. When the execution state on an instance is one of the following values, Stopped is returned as the overall execution state:
        # 
        #     *   Cancelled: The task was canceled.
        #     *   Terminated: The task was terminated.
        # 
        # *   PartialFailed: The execution was complete on some instances and failed on other instances. When the execution state is Success on some instances and is Failed or Stopped on the other instances, the overall execution state is PartialFailed.
        # 
        # >  `InvokeStatus` in the response functions similarly to this parameter. We recommend that you check the value of this parameter.
        self.oss_output_status = oss_output_status
        # Command to execute the Output OSS delivery configuration.
        self.oss_output_uri = oss_output_uri
        # Indicates whether the command is to be automatically run.
        self.output = output
        # The time when the command task was created.
        self.repeats = repeats
        # Details about the command executions.
        self.start_time = start_time
        # The execution states of the command.
        self.stop_time = stop_time
        # The request ID.
        self.timed = timed
        # The maximum timeout period for the command execution. Unit: seconds.
        # 
        # When a command cannot be run, the command execution times out. When a command execution times out, Cloud Assistant Agent forcefully terminates the command process by canceling the process ID (PID) of the command.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.dropped is not None:
            result['Dropped'] = self.dropped

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_info is not None:
            result['ErrorInfo'] = self.error_info

        if self.exit_code is not None:
            result['ExitCode'] = self.exit_code

        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_invoke_status is not None:
            result['InstanceInvokeStatus'] = self.instance_invoke_status

        if self.invocation_status is not None:
            result['InvocationStatus'] = self.invocation_status

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

        if self.timed is not None:
            result['Timed'] = self.timed

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Dropped') is not None:
            self.dropped = m.get('Dropped')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorInfo') is not None:
            self.error_info = m.get('ErrorInfo')

        if m.get('ExitCode') is not None:
            self.exit_code = m.get('ExitCode')

        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceInvokeStatus') is not None:
            self.instance_invoke_status = m.get('InstanceInvokeStatus')

        if m.get('InvocationStatus') is not None:
            self.invocation_status = m.get('InvocationStatus')

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

        if m.get('Timed') is not None:
            self.timed = m.get('Timed')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

