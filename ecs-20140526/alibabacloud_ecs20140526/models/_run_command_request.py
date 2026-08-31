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
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. **ClientToken** can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The command content. The command content can be plaintext or Base64-encoded. Note the following items:
        # 
        # - The command content cannot exceed 24 KB after Base64 encoding. You can use `KeepCommand` to specify whether to retain the command.
        # - If the command content is Base64-encoded, you must set `ContentEncoding=Base64`.
        # - When `EnableParameter=true` is specified, the custom parameter feature is enabled in the command content:
        #     - Define custom parameters by enclosing them in `{{}}`. Spaces and line breaks before and after the parameter name within `{{}}` are ignored.
        #     - The number of custom parameters cannot exceed 20.
        #     - Custom parameter names can contain a-zA-Z0-9-_ combinations. The acs:: prefix for specifying non-built-in environment parameters is not supported. Other characters are not supported. Parameter names are case-insensitive.
        #     - Each custom parameter name cannot exceed 64 bytes.
        # 
        # - You can specify built-in environment parameters as custom parameters. When running the command, you do not need to manually assign values to these parameters because Cloud Assistant automatically replaces them with the corresponding values. The following built-in environment parameters are supported:
        #     - `{{ACS::RegionId}}`: The region ID.
        #     - `{{ACS::AccountId}}`: The Alibaba Cloud account ID.
        #     - `{{ACS::InstanceId}}`: The instance ID. When a command is sent to multiple instances and you want to use `{{ACS::InstanceId}}` as a built-in environment parameter, ensure that the Cloud Assistant Agent version is no earlier than:
        #         - Linux: 2.2.3.309
        #         - Windows: 2.1.3.309
        #     - `{{ACS::InstanceName}}`: The instance name. When a command is sent to multiple instances and you want to use `{{ACS::InstanceName}}` as a built-in environment parameter, ensure that the Cloud Assistant Agent version is no earlier than:
        #         - Linux: 2.2.3.344
        #         - Windows: 2.1.3.344
        #     - `{{ACS::InvokeId}}`: The invocation ID. To use `{{ACS::InvokeId}}` as a built-in environment parameter, ensure that the Cloud Assistant Agent version is no earlier than:
        #         - Linux: 2.2.3.309
        #         - Windows: 2.1.3.309
        #     - `{{ACS::CommandId}}`: The command ID. When running a command by calling this operation and you want to use `{{ACS::CommandId}}` as a built-in environment parameter, ensure that the Cloud Assistant Agent version is no earlier than: 
        #         - Linux: 2.2.3.309
        #         - Windows: 2.1.3.309
        # 
        # This parameter is required.
        self.command_content = command_content
        # The container ID. Only 64-bit hexadecimal strings are supported. The `docker://`, `containerd://`, or `cri-o://` prefix can be used to explicitly specify the container runtime.
        # 
        # Precautions:
        # - If this parameter is specified, Cloud Assistant runs the script in the specified container on the instance.
        # - If this parameter is specified, the command can only be run on Linux instances with Cloud Assistant Agent version 2.2.3.344 or later.
        # - If this parameter is specified, the `Username` and `WorkingDir` parameters do not take effect. The command is run only as the default container user in the default working directory of the container. For more information, see [Use Cloud Assistant to run commands in containers](https://help.aliyun.com/document_detail/456641.html).
        # > Only Shell scripts are supported in Linux containers. Specifying an interpreter at the beginning of the script in the format of `#!/usr/bin/python` is not supported. For more information, see [Use Cloud Assistant to run commands in containers](https://help.aliyun.com/document_detail/456641.html).
        self.container_id = container_id
        # The container name.
        # 
        # Precautions:
        # - If this parameter is specified, Cloud Assistant runs the script in the specified container on the instance.
        # - If this parameter is specified, the command can only be run on Linux instances with Cloud Assistant Agent version 2.2.3.344 or later.
        # - If this parameter is specified, the `Username` and `WorkingDir` parameters do not take effect. The command is run only as the default container user in the default working directory of the container. For more information, see [Use Cloud Assistant to run commands in containers](https://help.aliyun.com/document_detail/456641.html).
        # > Only Shell scripts are supported in Linux containers. Specifying an interpreter at the beginning of the script in the format of `#!/usr/bin/python` is not supported. For more information, see [Use Cloud Assistant to run commands in containers](https://help.aliyun.com/document_detail/456641.html).
        self.container_name = container_name
        # The encoding method of the command content (`CommandContent`). Valid values (case-insensitive):
        # 
        # - PlainText: no encoding. The content is transmitted in plaintext.
        # - Base64: Base64 encoding.
        # 
        # Default value: PlainText. Invalid values are treated as PlainText.
        self.content_encoding = content_encoding
        # The command description. All character sets are supported. The description cannot exceed 512 characters in length.
        self.description = description
        # Specifies whether the command contains custom parameters.
        # 
        # Default value: false.
        self.enable_parameter = enable_parameter
        # The schedule for running the command. Three scheduling methods are supported: execution at fixed intervals (based on Rate expressions), one-time execution at a specified time, and clock-based scheduled execution (based on Cron expressions).
        # 
        # - Execution at fixed intervals: Based on Rate expressions, the command is run at the specified interval. The interval can be specified in seconds (s), minutes (m), hours (h), or days (d). This method is applicable to scenarios where tasks are run at fixed intervals. Format: `rate(<interval value><interval unit>)`. For example, to run a command every 5 minutes, use `rate(5m)`. The following limits apply to fixed-interval execution:
        #     - The interval must be no greater than 7 days and no less than 60 seconds, and must be greater than the timeout period of the scheduled task.
        #     - The interval is based on a fixed frequency and is not related to the actual execution time of the task. For example, if a command is set to run every 5 minutes and the task takes 2 minutes to complete, the next round starts 3 minutes after the task is completed.
        #     - The task is not run immediately upon creation. For example, if a command is set to run every 5 minutes, the command is not run immediately when the task is created. Instead, execution starts 5 minutes after the task is created.
        # 
        # - One-time execution at a specified time: The command is run once at the specified time zone and time point. Format: `at(yyyy-MM-dd HH:mm:ss <time zone>)`. If no time zone is specified, UTC is used by default. The time zone supports the following three formats:
        #     - Full time zone name: such as `Asia/Shanghai` (China/Shanghai time) or `America/Los_Angeles` (US/Los Angeles time).
        #     - Time zone offset from Greenwich Mean Time: such as `GMT+8:00` (East 8th time zone) or `GMT-7:00` (West 7th time zone). When using the GMT format, leading zeros are not supported in the hour field.
        #     - Time zone abbreviation: Only UTC (Coordinated Universal Time) is supported.
        # 
        #   For example, to run a command once at 13:15:30 on June 6, 2022 in China/Shanghai time, use: `at(2022-06-06 13:15:30 Asia/Shanghai)`. To run a command once at 13:15:30 on June 6, 2022 in the West 7th time zone, use: `at(2022-06-06 13:15:30 GMT-7:00)`.
        # 
        # - Clock-based scheduled execution (based on Cron expressions): Based on Cron expressions, the command is run according to the scheduled task settings. Format: `<seconds> <minutes> <hours> <day of month> <month> <day of week> <year (optional)> <time zone>`, i.e., `<Cron expression> <time zone>`. The scheduled task execution time is calculated based on the Cron expression in the specified time zone. If no time zone is specified, the system time zone of the instance running the scheduled task is used by default. For more information about Cron expressions, see [Cron expressions](https://help.aliyun.com/document_detail/64769.html). The time zone supports the following three formats:
        #     - Full time zone name: such as `Asia/Shanghai` (China/Shanghai time) or `America/Los_Angeles` (US/Los Angeles time).
        #     - Time zone offset from Greenwich Mean Time: such as `GMT+8:00` (East 8th time zone) or `GMT-7:00` (West 7th time zone). When using the GMT format, leading zeros are not supported in the hour field.
        #     - Time zone abbreviation: Only UTC (Coordinated Universal Time) is supported.
        #   For example, to run a command once every day at 10:15 AM in China/Shanghai time in 2022, use `0 15 10 ? * * 2022 Asia/Shanghai`. To run a command every 30 minutes from 10:00 AM to 11:30 AM every day in the East 8th time zone in 2022, use `0 0/30 10-11 * * ? 2022 GMT+8:00`. To run a command every 5 minutes from 2:00 PM to 2:55 PM every day in October every two years starting from 2022 in UTC, use `0 0/5 14 * 10 ? 2022/2 UTC`.
        # 
        #     > The minimum interval must be greater than or equal to the timeout period of the scheduled task and no less than 10 seconds.
        self.frequency = frequency
        # The instance ID array of ECS instances. Array length: 1 to 100.
        # 
        # If any of the specified instances does not meet the execution conditions, you must reselect the instances.
        # 
        # You can also request a quota increase in Quota Center (quota name: Maximum number of instances supported for command execute).
        self.instance_id = instance_id
        # Specifies whether to retain the command after execution. Valid values:
        # 
        # - true: retains the command. The command can be run again by calling InvokeCommand. This counts toward the Cloud Assistant command retention quota.
        # - false: does not retain the command. The command is automatically deleted after execution and does not count toward the Cloud Assistant command retention quota.
        # 
        # Default value: false.
        self.keep_command = keep_command
        # The bootstrap program for script execution. The value cannot exceed 1 KB in length.
        self.launcher = launcher
        # The command name. All character sets are supported. The name cannot exceed 128 characters in length.
        self.name = name
        # The OSS delivery configuration for command execution output.
        # 
        # - Format: oss://${BucketName}/${Prefix}, where ${BucketName} is the name of the destination OSS bucket and ${Prefix} is the directory prefix for delivery.
        self.oss_output_delivery = oss_output_delivery
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The key-value pairs of custom parameters to pass in when running a command that contains custom parameters. For example, if the command content is `echo {{name}}`, you can pass in the key-value pair `{"name":"Jack"}` through the Parameter parameter. The custom parameter automatically replaces the variable value `name`, and the actual command executed is `echo Jack`.
        # 
        # The number of custom parameters ranges from 0 to 10. Note the following items:
        # 
        # - Keys cannot be empty strings and can contain up to 64 characters.
        # - Values can be empty strings.
        # - After custom parameters and the original command content are Base64-encoded, the total size cannot exceed 24 KB. You can use `KeepCommand` to specify whether to retain the command.
        # - The set of custom parameter names must be a subset of the parameter set defined when the command was created. For parameters that are not passed in, you can use empty strings as substitutes.
        # 
        # Default value: empty, which disables custom parameters.
        self.parameters = parameters
        # The region ID. You can call [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The execution mode of the command. Valid values:
        # 
        # - Once: immediately runs the command.
        # - Period: runs the command on a schedule. When this parameter is set to `Period`, you must also specify the `Frequency` parameter.
        # - NextRebootOnly: automatically runs the command the next time the instance starts.
        # - EveryReboot: automatically runs the command every time the instance starts.
        # - DryRun: performs a dry run of the request without actually running the command. Checks include request parameters, instance execution environment, and Cloud Assistant Agent running status.
        # 
        # Default values:
        # - When the `Frequency` parameter is not specified, the default value is `Once`.
        # - When the `Frequency` parameter is specified, the command is processed as `Period` regardless of whether this parameter is set.
        # 
        # Precautions:
        # - You can call [StopInvocation](https://help.aliyun.com/document_detail/64838.html) to stop a pending or scheduled command.
        # - When this parameter is set to `Period` or `EveryReboot`, you can call [DescribeInvocationResults](https://help.aliyun.com/document_detail/64845.html) and specify `IncludeHistory=true` to view the execution history of the scheduled command.
        self.repeat_mode = repeat_mode
        # The resource group ID for the command execution. When this parameter is specified:
        # 
        # - If the ECS instance corresponding to InstanceId belongs to a non-default resource group, the ECS instance must belong to this resource group.
        # 
        # - You can filter the corresponding command execution results by specifying this parameter (by calling [DescribeInvocations](https://help.aliyun.com/document_detail/64840.html) or [DescribeInvocationResults](https://help.aliyun.com/document_detail/64845.html)).
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The tags used to filter instances. Array length: 0 to 20. You can run commands in batches on instances with the same tags without specifying InstanceId.
        self.resource_tag = resource_tag
        # The tag pairs. Array length: 0 to 20.
        self.tag = tag
        # The mode for stopping the task (manual stop or timeout interruption). Valid values:
        # - Process: stops the current script process.
        # - ProcessTree: stops the current process tree (the collection of the script process and all child processes it created).
        self.termination_mode = termination_mode
        # **[Deprecated]** This parameter is deprecated. Passing in this parameter has no effect.
        self.timed = timed
        # The timeout period for command execution. Unit: seconds.
        # 
        # A timeout occurs when a command cannot be run because of process issues, missing modules, or missing Cloud Assistant Agent. When a timeout occurs, the command process is forcefully terminated.
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
        # The username for running the command on the ECS instance. The value cannot exceed 255 characters in length.
        # 
        # - For Linux ECS instances, commands are run as the root user by default.
        # - For Windows ECS instances, commands are run as the System user by default.
        # 
        # You can also specify another existing user on the instance to run the command. Running Cloud Assistant commands as a regular user is more secure. For more information, see [Configure a regular user to run Cloud Assistant commands](https://help.aliyun.com/document_detail/203771.html).
        self.username = username
        # The name of the password for the user who executes the command on a Windows instance. The value cannot exceed 255 characters in length.
        # 
        # When you want to execute a command as a non-default user (System) on a Windows instance, you must specify both `Username` and this parameter. To reduce the risk of password leaks, store the plaintext password in the parameter repository of operations management, and pass in only the password name here. For more information, see [Encryption parameters](https://help.aliyun.com/document_detail/186828.html) and [Settings for a regular user to execute Cloud Assistant commands](https://help.aliyun.com/document_detail/203771.html).
        # 
        # > This parameter is not required when you execute commands as the root user on a Linux instance or the System user on a Windows instance.
        self.windows_password_name = windows_password_name
        # The working directory of the command on the ECS instance. The value cannot exceed 200 characters in length.
        # 
        # Default values:
        # 
        # - For Linux instances, the default directory is the home directory of the root user, which is `/root`.
        # - For Windows instances, the default directory is the directory where the Cloud Assistant Agent process is located, such as `C:\\Windows\\System32`.
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
        # The tag key of the command execute. If this value is specified, it cannot be an empty string.
        # 
        # When you use a single tag to filter resources, the resource count under that tag cannot exceed 1,000. When you use multiple tags to filter resources, the resource count of resources that are attached to all specified tags cannot exceed 1,000. If the resource count exceeds 1,000, use the [ListTagResources](https://help.aliyun.com/document_detail/110425.html) operation to query resources.
        # 
        # The key can be up to 64 characters in length and cannot start with `aliyun` or `acs:`, and cannot contain `http://` or `https://`.
        self.key = key
        # The tag value of the command execution. The value can be an empty string.
        # 
        # The value can be up to 128 characters in length and cannot contain `http://` or `https://`.
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
        # - This parameter conflicts with the InstanceId parameter. They cannot be specified at the same time.
        # 
        # - If this value is specified, it cannot be an empty string.
        # 
        # - The number of instances under the tag cannot exceed the quantity limit of InstanceId.N. If the number of instances exceeds the limit, control the number of instances by adding batch tags, such as batch: b1.
        # 
        # - The key can be up to 64 characters in length and cannot start with aliyun or acs:, and cannot contain http:// or https://.
        self.key = key
        # The tag value used to filter instances.
        # 
        # Precautions:
        # - The value can be an empty string.
        # - The value can be up to 128 characters in length and cannot contain http:// or https://.
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

