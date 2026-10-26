# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class RunCommandRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        command_content: str = None,
        container_id: str = None,
        container_name: str = None,
        content_encoding: str = None,
        description: str = None,
        enable_parameter: bool = None,
        frequency: str = None,
        instance_id: List[str] = None,
        keep_command: bool = None,
        launcher: str = None,
        name: str = None,
        oss_output_delivery: str = None,
        owner_account: str = None,
        owner_id: int = None,
        parameters: Dict[str, Any] = None,
        region_id: str = None,
        repeat_mode: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        resource_tag: List[main_models.RunCommandRequestResourceTag] = None,
        tag: List[main_models.RunCommandRequestTag] = None,
        termination_mode: str = None,
        timed: bool = None,
        timeout: int = None,
        type: str = None,
        username: str = None,
        windows_password_name: str = None,
        working_dir: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The **ClientToken** value can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The command content. The command content can be plaintext or Base64-encoded. Take note of the following items:
        # 
        # - The size of the Base64-encoded command content cannot exceed 24 KB. You can use the `KeepCommand` parameter to specify whether to retain the command.
        # - If the command content is Base64-encoded, you must set `ContentEncoding` to Base64.
        # - If you set `EnableParameter` to true, you can use custom parameters in the command content:
        #     - Use `{{}}` to enclose custom parameters. Spaces and line breaks before and after the parameter names within `{{}}` are ignored.
        #     - You can define up to 20 custom parameters.
        #     - A custom parameter name can contain letters, digits, hyphens (-), and underscores (_). The `acs::` prefix cannot be used to specify non-built-in environment variables. Other characters are not supported. Parameter names are not case-sensitive.
        #     - A single custom parameter name cannot exceed 64 bytes in length.
        # 
        # - You can specify built-in environment variables as custom parameters. When the command is run, you do not need to manually assign values to the parameters. Cloud Assistant automatically replaces them with the corresponding values in the environment. The following built-in environment variables are supported:
        #     - `{{ACS::RegionId}}`: the region ID.
        #     - `{{ACS::AccountId}}`: the UID of the Alibaba Cloud account.
        #     - `{{ACS::InstanceId}}`: the instance ID. If the command is delivered to multiple instances and you want to specify `{{ACS::InstanceId}}` as a built-in environment variable, make sure that the Cloud Assistant Agent is of the following versions or later:
        #         - Linux: 2.2.3.309
        #         - Windows: 2.1.3.309
        #     - `{{ACS::InstanceName}}`: the instance name. If the command is delivered to multiple instances and you want to specify `{{ACS::InstanceName}}` as a built-in environment variable, make sure that the Cloud Assistant Agent is of the following versions or later:
        #         - Linux: 2.2.3.344
        #         - Windows: 2.1.3.344
        #     - `{{ACS::InvokeId}}`: the invocation ID. If you want to specify `{{ACS::InvokeId}}` as a built-in environment variable, make sure that the Cloud Assistant Agent is of the following versions or later:
        #         - Linux: 2.2.3.309
        #         - Windows: 2.1.3.309
        #     - `{{ACS::CommandId}}`: the command ID. If you call this operation to run a command and want to specify `{{ACS::CommandId}}` as a built-in environment variable, make sure that the Cloud Assistant Agent is of the following versions or later: 
        #         - Linux: 2.2.3.309
        #         - Windows: 2.1.3.309
        # 
        # This parameter is required.
        self.command_content = command_content
        # The container ID. Only 64-bit hexadecimal strings are supported. The `docker://`, `containerd://`, or `cri-o://` prefix is allowed to explicitly specify the container runtime.
        # 
        # Precautions:
        # - If you specify this parameter, Cloud Assistant runs the script in the specified container on the instance.
        # - If you specify this parameter, it is only supported on Linux instances where the Cloud Assistant Agent version is 2.2.3.344 or later.
        # - If you specify this parameter, the specified `Username` and `WorkingDir` parameters do not take effect. The command can only be run by the default user of the container in the default working directory of the container. For more information, see [Use Cloud Assistant to run commands in containers](https://help.aliyun.com/document_detail/456641.html).
        # > Only Shell scripts can be run in Linux containers. You cannot use a command similar to `#!/usr/bin/python` at the beginning of the script to specify the interpreter for the script content. For more information, see [Use Cloud Assistant to run commands in containers](https://help.aliyun.com/document_detail/456641.html).
        self.container_id = container_id
        # The container name.
        # 
        # Precautions:
        # - If you specify this parameter, Cloud Assistant runs the script in the specified container on the instance.
        # - If you specify this parameter, it is only supported on Linux instances where the Cloud Assistant Agent version is 2.2.3.344 or later.
        # - If you specify this parameter, the specified `Username` and `WorkingDir` parameters do not take effect. The command can only be run by the default user of the container in the default working directory of the container. For more information, see [Use Cloud Assistant to run commands in containers](https://help.aliyun.com/document_detail/456641.html).
        # > Only Shell scripts can be run in Linux containers. You cannot use a command similar to `#!/usr/bin/python` at the beginning of the script to specify the interpreter for the script content. For more information, see [Use Cloud Assistant to run commands in containers](https://help.aliyun.com/document_detail/456641.html).
        self.container_name = container_name
        # The encoding mode of the command content (`CommandContent`). Valid values (case-insensitive):
        # 
        # - PlainText: no encoding. The command content is transmitted in plaintext.
        # - Base64: Base64 encoding.
        # 
        # Default value: PlainText. If you enter an invalid value, it is processed as PlainText.
        self.content_encoding = content_encoding
        # The command description. It supports all character sets and can be up to 512 characters in length.
        self.description = description
        # Specifies whether the command contains custom parameters.
        # 
        # Default value: false.
        self.enable_parameter = enable_parameter
        # The execution time of the scheduled command. Three scheduled execution modes are supported: execution at fixed time intervals (based on rate expressions), one-time execution at a specified time, and clock-based scheduled execution (based on cron expressions).
        # 
        # - Execution at fixed time intervals: runs the command at the specified time interval based on a rate expression. The time interval can be specified in seconds (s), minutes (m), hours (h), or days (d). This mode is suitable for scenarios where tasks are run at fixed time intervals. The format is `rate(<interval value><interval unit>)`. For example, to run the command every 5 minutes, the format is `rate(5m)`. The following limits apply to execution at fixed time intervals:
        #     - The specified time interval must not exceed 7 days, must not be less than 60 seconds, and must be greater than the timeout period of the scheduled task.
        #     - The execution interval is based only on the fixed frequency and is independent of the actual time required to run the task. For example, if you set the command to run every 5 minutes and the task takes 2 minutes to complete, the next execution starts 3 minutes after the task is completed.
        #     - The task is not run immediately when it is created. For example, if you set the command to run every 5 minutes, the command is not run immediately when the task is created. Instead, it starts to run 5 minutes after the task is created.
        # 
        # - One-time execution at a specified time: runs the command once at the specified time zone and execution time. The format is `at(yyyy-MM-dd HH:mm:ss <time zone>)`, which is `at(year-month-day hour:minute:second <time zone>)`. If you do not specify a time zone, the UTC time zone is used by default. The time zone supports the following three formats:
        #     - Time zone full name: such as `Asia/Shanghai` (China/Shanghai time) and `America/Los_Angeles` (US/Los Angeles time).
        #     - Time zone offset from Greenwich Mean Time: such as `GMT+8:00` (East 8th time zone) and `GMT-7:00` (West 7th time zone). When you use the GMT format, leading zeros are not supported for the hour digit.
        #     - Time zone abbreviation: only UTC (Coordinated Universal Time) is supported.
        # 
        #   For example, to run the command once at 13:15:30 on June 6, 2022 in the China/Shanghai time zone, the format is `at(2022-06-06 13:15:30 Asia/Shanghai)`. To run the command once at 13:15:30 on June 6, 2022 in the West 7th time zone, the format is `at(2022-06-06 13:15:30 GMT-7:00)`.
        # 
        # - Clock-based scheduled execution (based on cron expressions): runs the command based on a cron expression. The format is `<seconds> <minutes> <hours> <day of month> <month> <day of week> <year (optional)> <time zone>`, which is `<cron expression> <time zone>`. In the specified time zone, the scheduled task execution time is calculated based on the cron expression and the task is run. If you do not specify a time zone, the internal system time zone of the instance that runs the scheduled task is used by default. For more information about cron expressions, see [Cron expressions](https://help.aliyun.com/document_detail/64769.html). The time zone supports the following three formats:
        #     - Time zone full name: such as `Asia/Shanghai` (China/Shanghai time) and `America/Los_Angeles` (US/Los Angeles time).
        #     - Time zone offset from Greenwich Mean Time: such as `GMT+8:00` (East 8th time zone) and `GMT-7:00` (West 7th time zone). When you use the GMT format, leading zeros are not supported for the hour digit.
        #     - Time zone abbreviation: only UTC (Coordinated Universal Time) is supported.
        #   For example, to run the command once at 10:15 every day in 2022 in the China/Shanghai time zone, the format is `0 15 10 ? * * 2022 Asia/Shanghai`. To run the command every half hour from 10:00 to 11:30 every day in 2022 in the East 8th time zone, the format is `0 0/30 10-11 * * ? 2022 GMT+8:00`. To run the command every 5 minutes from 14:00 to 14:55 every day in October every two years starting from 2022 in the UTC time zone, the format is `0 0/5 14 * 10 ? 2022/2 UTC`.
        # 
        #     > The minimum time interval must be greater than or equal to the timeout period of the scheduled task and must not be less than 10 seconds.
        self.frequency = frequency
        # The array of ECS instance IDs. Array length: 1 to 100.
        # 
        # If you specify multiple instances and one of the instances does not meet the execution conditions, you must reselect the instances.
        # 
        # You can also apply for a quota increase in Quota Center. The quota name is the maximum number of instances that support command execution.
        self.instance_id = instance_id
        # Specifies whether to retain the command after it is run. Valid values:
        # 
        # - true: retains the command. You can call the InvokeCommand operation to run the command again. This consumes the quota for retained Cloud Assistant commands.
        # - false: does not retain the command. The command is automatically deleted after it is run and does not consume the quota for retained Cloud Assistant commands.
        # 
        # Default value: false.
        self.keep_command = keep_command
        # The bootstrap program for script execution. It cannot exceed 1 KB in length.
        self.launcher = launcher
        # The command name. It supports all character sets and can be up to 128 characters in length.
        self.name = name
        # The OSS delivery configuration for the command execution output.
        # 
        # - Format: oss://${BucketName}/${Prefix}. ${BucketName} is the name of the OSS bucket to which the output is delivered, and ${Prefix} is the directory prefix to which the output is delivered.
        self.oss_output_delivery = oss_output_delivery
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The key-value pairs of custom parameters that are passed in when the command is run, if the command contains custom parameters. For example, if the command content is `echo {{name}}`, you can pass in the key-value pair `{"name":"Jack"}` by using the `Parameter` parameter. The custom parameter automatically replaces the variable value `name`, and a new command is generated. The actual command that is run is `echo Jack`.
        # 
        # The number of custom parameters ranges from 0 to 10. Take note of the following items:
        # 
        # - The key cannot be an empty string and can be up to 64 characters in length.
        # - The value can be an empty string.
        # - After the custom parameters and the original command content are Base64-encoded, the size of the Base64-encoded command content cannot exceed 24 KB. You can use the `KeepCommand` parameter to specify whether to retain the command.
        # - The set of custom parameter names must be a subset of the parameter set defined when the command is created. For parameters that are not passed in, you can use empty strings instead.
        # 
        # The default value is empty, which indicates that this parameter is not set and the custom parameter feature is disabled.
        self.parameters = parameters
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The execution mode of the command. Valid values:
        # 
        # - Once: runs the command immediately.
        # - Period: runs the command on a schedule. If you set this parameter to `Period`, you must also specify the `Frequency` parameter.
        # - NextRebootOnly: automatically runs the command the next time the instance starts.
        # - EveryReboot: automatically runs the command every time the instance starts.
        # - DryRun: prechecks the request only. The command is not actually run. The check items include the request parameters, instance execution environment, and Cloud Assistant Agent running status.
        # 
        # Default values:
        # - If you do not specify the `Frequency` parameter, the default value is `Once`.
        # - If you specify the `Frequency` parameter, the value is processed as `Period` regardless of whether this parameter is set.
        # 
        # Precautions:
        # - You can call the [StopInvocation](https://help.aliyun.com/document_detail/64838.html) operation to stop a pending command or a scheduled command.
        # - If you set this parameter to `Period` or `EveryReboot`, you can call the [DescribeInvocationResults](https://help.aliyun.com/document_detail/64845.html) operation and set `IncludeHistory` to true to view the historical records of the scheduled command execution.
        self.repeat_mode = repeat_mode
        # The ID of the resource group to which the command execution belongs. When you specify this parameter:
        # 
        # - If the ECS instance specified by InstanceId belongs to a non-default resource group, the ECS instance must belong to this resource group.
        # 
        # - You can specify this parameter to filter the corresponding command execution results by calling the [DescribeInvocations](https://help.aliyun.com/document_detail/64840.html) or [DescribeInvocationResults](https://help.aliyun.com/document_detail/64845.html) operation.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The array of tags used to filter instances. Array length: 0 to 20. You can run the command on multiple instances that have the same tags without specifying InstanceId.
        self.resource_tag = resource_tag
        # The array of tags. Array length: 0 to 20.
        self.tag = tag
        # The mode used when the task is stopped (manually stopped or interrupted due to execution timeout). Valid values:
        # - Process: stops the current script process.
        # - ProcessTree: stops the current process tree (the set of the script process and all child processes created by it).
        self.termination_mode = termination_mode
        # > **[Deprecated]** This parameter is deprecated and does not take effect.
        self.timed = timed
        # The timeout period for running the command. Unit: seconds.
        # 
        # If the command cannot be run because of process issues, missing modules, or a missing Cloud Assistant Agent, a timeout occurs. After a timeout, the command process is forcefully terminated.
        # 
        # Default value: 60.
        self.timeout = timeout
        # The command type. Valid values:
        # 
        # - RunBatScript: Bat commands for Windows instances.
        # - RunPowerShellScript: PowerShell commands for Windows instances.
        # - RunShellScript: Shell commands for Linux instances.
        # 
        # This parameter is required.
        self.type = type
        # The username that is used to run the command on the ECS instance. It can be up to 255 characters in length.
        # 
        # - For Linux ECS instances, the command is run by the root user by default.
        # - For Windows ECS instances, the command is run by the System user by default.
        # 
        # You can also specify another existing user on the instance to run the command. Running Cloud Assistant commands as a regular user is more secure. For more information, see [Configure a regular user to run Cloud Assistant commands](https://help.aliyun.com/document_detail/203771.html).
        self.username = username
        # The password name of the user that is used to execute the command on the Windows instance. It can be up to 255 characters in length.
        # 
        # If you want to execute the command as a non-default user (System) on a Windows instance, you must specify both `Username` and this parameter. To reduce the risk of password leakage, you must host the plaintext password in the parameter repository of CloudOps Orchestration Service and pass in only the password name here. For more information, see [Encrypt parameters](https://help.aliyun.com/document_detail/186828.html) and [Settings for regular users to execute Cloud Assistant commands](https://help.aliyun.com/document_detail/203771.html).
        # 
        # > You do not need to pass in this parameter when you execute the command as the root user on a Linux instance or the System user on a Windows instance.
        self.windows_password_name = windows_password_name
        # The running directory of the command on the ECS instance. It can be up to 200 characters in length.
        # 
        # Default values:
        # 
        # - For Linux instances, the default running directory is the home directory of the root user, which is `/root`.
        # - For Windows instances, the default running directory is the directory where the Cloud Assistant Agent process resides, such as `C:\\Windows\\System32`.
        self.working_dir = working_dir

    def validate(self):
        if self.resource_tag:
            for v1 in self.resource_tag:
                 if v1:
                    v1.validate()
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.command_content is not None:
            result['CommandContent'] = self.command_content

        if self.container_id is not None:
            result['ContainerId'] = self.container_id

        if self.container_name is not None:
            result['ContainerName'] = self.container_name

        if self.content_encoding is not None:
            result['ContentEncoding'] = self.content_encoding

        if self.description is not None:
            result['Description'] = self.description

        if self.enable_parameter is not None:
            result['EnableParameter'] = self.enable_parameter

        if self.frequency is not None:
            result['Frequency'] = self.frequency

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.keep_command is not None:
            result['KeepCommand'] = self.keep_command

        if self.launcher is not None:
            result['Launcher'] = self.launcher

        if self.name is not None:
            result['Name'] = self.name

        if self.oss_output_delivery is not None:
            result['OssOutputDelivery'] = self.oss_output_delivery

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.repeat_mode is not None:
            result['RepeatMode'] = self.repeat_mode

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        result['ResourceTag'] = []
        if self.resource_tag is not None:
            for k1 in self.resource_tag:
                result['ResourceTag'].append(k1.to_map() if k1 else None)

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.termination_mode is not None:
            result['TerminationMode'] = self.termination_mode

        if self.timed is not None:
            result['Timed'] = self.timed

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        if self.type is not None:
            result['Type'] = self.type

        if self.username is not None:
            result['Username'] = self.username

        if self.windows_password_name is not None:
            result['WindowsPasswordName'] = self.windows_password_name

        if self.working_dir is not None:
            result['WorkingDir'] = self.working_dir

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('CommandContent') is not None:
            self.command_content = m.get('CommandContent')

        if m.get('ContainerId') is not None:
            self.container_id = m.get('ContainerId')

        if m.get('ContainerName') is not None:
            self.container_name = m.get('ContainerName')

        if m.get('ContentEncoding') is not None:
            self.content_encoding = m.get('ContentEncoding')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnableParameter') is not None:
            self.enable_parameter = m.get('EnableParameter')

        if m.get('Frequency') is not None:
            self.frequency = m.get('Frequency')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('KeepCommand') is not None:
            self.keep_command = m.get('KeepCommand')

        if m.get('Launcher') is not None:
            self.launcher = m.get('Launcher')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OssOutputDelivery') is not None:
            self.oss_output_delivery = m.get('OssOutputDelivery')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RepeatMode') is not None:
            self.repeat_mode = m.get('RepeatMode')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        self.resource_tag = []
        if m.get('ResourceTag') is not None:
            for k1 in m.get('ResourceTag'):
                temp_model = main_models.RunCommandRequestResourceTag()
                self.resource_tag.append(temp_model.from_map(k1))

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.RunCommandRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('TerminationMode') is not None:
            self.termination_mode = m.get('TerminationMode')

        if m.get('Timed') is not None:
            self.timed = m.get('Timed')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        if m.get('WindowsPasswordName') is not None:
            self.windows_password_name = m.get('WindowsPasswordName')

        if m.get('WorkingDir') is not None:
            self.working_dir = m.get('WorkingDir')

        return self

class RunCommandRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the command to execute. It cannot be an empty string once specified.
        # 
        # If you use a single tag to filter resources, the resource count under the tag cannot exceed 1,000. If you use multiple tags to filter resources, the resource count of resources that are attached to all the specified tags cannot exceed 1,000. If the resource count exceeds 1,000, you must use the [ListTagResources](https://help.aliyun.com/document_detail/110425.html) operation to query the resources.
        # 
        # It can be up to 64 characters in length and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
        self.key = key
        # The tag value of the command execution. It can be an empty string.
        # 
        # It can be up to 128 characters in length and cannot contain `http://` or `https://`.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class RunCommandRequestResourceTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key used to filter instances.
        # 
        # Precautions:
        # 
        # - This parameter conflicts with the InstanceId parameter and they cannot be specified at the same time.
        # 
        # - It cannot be an empty string once specified.
        # 
        # - The number of instances under the tag cannot exceed the limit on the number of InstanceId.N parameters. If the number of instances exceeds the limit, we recommend that you control the number of instances by adding batch tags, such as batch: b1.
        # 
        # - It can be up to 64 characters in length and cannot start with aliyun or acs:. It cannot contain http:// or https://.
        self.key = key
        # The tag value used to filter instances.
        # 
        # Precautions:
        # - It can be an empty string.
        # - It can be up to 128 characters in length and cannot contain http:// or https://.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

