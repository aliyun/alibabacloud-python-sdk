# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class RunCommandShrinkRequest(DaraModel):
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
        parameters_shrink: str = None,
        region_id: str = None,
        repeat_mode: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        resource_tag: List[main_models.RunCommandShrinkRequestResourceTag] = None,
        tag: List[main_models.RunCommandShrinkRequestTag] = None,
        termination_mode: str = None,
        timed: bool = None,
        timeout: int = None,
        type: str = None,
        username: str = None,
        windows_password_name: str = None,
        working_dir: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but make sure that the token is unique among different requests. **ClientToken** supports only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The command content. The command content can be plaintext or Base64-encoded. Note the following:
        # 
        # - The size of the command content after Base64 encoding cannot exceed 24 KB. You can use `KeepCommand` to specify whether to retain the command.
        # - If the command content is Base64-encoded, set `ContentEncoding=Base64`.
        # - Set `EnableParameter=true` to enable custom parameters in the command content:
        #     - Custom parameters are defined by enclosing them in `{{}}`. Spaces and line breaks before and after the parameter name within `{{}}` are ignored.
        #     - A maximum of 20 custom parameters are supported.
        #     - Custom parameter names can contain only a-z, A-Z, 0-9, hyphens (-), and underscores (_). The acs:: prefix for specifying non-built-in environment parameters is not supported. Other characters are not supported. Parameter names are case-insensitive.
        #     - Each custom parameter name cannot exceed 64 bytes.
        # 
        # - You can specify built-in environment parameters as custom parameters. When the command is run, Cloud Assistant automatically replaces the parameters with the corresponding values in the environment without manual assignment. The following built-in environment parameters are supported:
        #     - `{{ACS::RegionId}}`: The region ID.
        #     - `{{ACS::AccountId}}`: The UID of the Alibaba Cloud account.
        #     - `{{ACS::InstanceId}}`: The instance ID. When the command is sent to multiple instances and you want to use `{{ACS::InstanceId}}` as a built-in environment parameter, make sure that the Cloud Assistant Agent version is not earlier than the following:
        #         - Linux: 2.2.3.309
        #         - Windows: 2.1.3.309
        #     - `{{ACS::InstanceName}}`: The instance name. When the command is sent to multiple instances and you want to use `{{ACS::InstanceName}}` as a built-in environment parameter, make sure that the Cloud Assistant Agent version is not earlier than the following:
        #         - Linux: 2.2.3.344
        #         - Windows: 2.1.3.344
        #     - `{{ACS::InvokeId}}`: The command execution ID. To use `{{ACS::InvokeId}}` as a built-in environment parameter, make sure that the Cloud Assistant Agent version is not earlier than the following:
        #         - Linux: 2.2.3.309
        #         - Windows: 2.1.3.309
        #     - `{{ACS::CommandId}}`: The command ID. When you call this operation to run a command and want to use `{{ACS::CommandId}}` as a built-in environment parameter, make sure that the Cloud Assistant Agent version is not earlier than the following:
        #         - Linux: 2.2.3.309
        #         - Windows: 2.1.3.309
        # 
        # This parameter is required.
        self.command_content = command_content
        # The container ID. Only 64-bit hexadecimal strings are supported. The `docker://`, `containerd://`, or `cri-o://` prefix can be added to specify the container runtime.
        # 
        # Precautions:
        # - If this parameter is specified, Cloud Assistant runs the script in the specified container of the instance.
        # - If this parameter is specified, the script can run only on Linux instances whose Cloud Assistant Agent version is 2.2.3.344 or later.
        # - If this parameter is specified, the specified `Username` and `WorkingDir` parameters do not take effect. Commands can be run only by using the default user of the container in the default working directory of the container. For more information, see [Use Cloud Assistant to run commands in containers](https://help.aliyun.com/document_detail/456641.html).
        # > In Linux containers, only shell scripts are supported. You cannot use a command such as `#!/usr/bin/python` at the beginning of a script to specify the interpreter. For more information, see [Use Cloud Assistant to run commands in containers](https://help.aliyun.com/document_detail/456641.html).
        self.container_id = container_id
        # The container name.
        # 
        # Precautions:
        # - If this parameter is specified, Cloud Assistant runs the script in the specified container of the instance.
        # - If this parameter is specified, the script can run only on Linux instances whose Cloud Assistant Agent version is 2.2.3.344 or later.
        # - If this parameter is specified, the Username and WorkingDir parameters do not take effect. Commands can be run only by using the default user in the default working directory of the container. For more information, see [Use Cloud Assistant to run commands in containers](https://help.aliyun.com/document_detail/456641.html).
        # > In Linux containers, only shell scripts can be run. You cannot specify an interpreter for the script content by adding a command such as `#!/usr/bin/python` to the beginning of the script. For more information, see [Use Cloud Assistant to run commands in containers](https://help.aliyun.com/document_detail/456641.html).
        self.container_name = container_name
        # The encoding mode of the command content (`CommandContent`). Valid values (case-insensitive):
        self.content_encoding = content_encoding
        # The command description. The description supports all character sets and can be up to 512 characters in length.
        self.description = description
        # Specifies whether the command contains custom parameters.
        self.enable_parameter = enable_parameter
        # The execution time for scheduled command execution. Three scheduling methods are supported: fixed interval execution (based on Rate expressions), one-time execution at a specified time, and clock-based scheduled execution (based on Cron expressions).
        # 
        # - Fixed interval execution: Based on Rate expressions, commands are executed at the specified time interval. The time interval can be specified in seconds (s), minutes (m), hours (h), or days (d). This method is suitable for scenarios that require task execution at fixed intervals. The format is `rate(<interval value><interval unit>)`. For example, to execute a command every 5 minutes, use `rate(5m)`. The following limits apply to fixed interval execution:
        #     - The specified interval cannot exceed 7 days or be less than 60 seconds, and must be greater than the timeout period of the scheduled task.
        #     - The execution interval is based on a fixed frequency and is independent of the actual execution time of the task. For example, if a command is set to execute every 5 minutes and the task takes 2 minutes to complete, the next execution starts 3 minutes after the task is completed.
        #     - The task is not executed immediately upon creation. For example, if a command is set to execute every 5 minutes, the command is not executed immediately when the task is created. Instead, execution starts 5 minutes after the task is created.
        # 
        # - One-time execution at a specified time: The command is executed once at the specified time and time zone. The format is `at(yyyy-MM-dd HH:mm:ss <time zone>)`. If no time zone is specified, the default is UTC. The following three time zone formats are supported:
        #     - Full time zone name: For example, `Asia/Shanghai` (China/Shanghai time) or `America/Los_Angeles` (US/Los Angeles time).
        #     - GMT offset from Greenwich Mean Time: For example, `GMT+8:00` (UTC+8) or `GMT-7:00` (UTC-7). When using the GMT format, leading zeros are not supported for the hour value.
        #     - Time zone abbreviation: Only UTC (Coordinated Universal Time) is supported.
        # 
        #   For example, to execute a command once at 13:15:30 on June 6, 2022 in China/Shanghai time, use `at(2022-06-06 13:15:30 Asia/Shanghai)`. To execute a command once at 13:15:30 on June 6, 2022 in UTC-7, use `at(2022-06-06 13:15:30 GMT-7:00)`.
        # 
        # - Clock-based scheduled execution (based on Cron expressions): Based on Cron expressions, commands are executed according to the scheduled task settings. The format is `<seconds> <minutes> <hours> <day of month> <month> <day of week> <year (optional)> <time zone>`, which is `<Cron expression> <time zone>`. The scheduled task execution time is calculated based on the Cron expression in the specified time zone. If no time zone is specified, the default is the internal system time zone of the instance that runs the scheduled task. For more information about Cron expressions, see [Cron expressions](https://help.aliyun.com/document_detail/64769.html). The following three time zone formats are supported:
        #     - Full time zone name: For example, `Asia/Shanghai` (China/Shanghai time) or `America/Los_Angeles` (US/Los Angeles time).
        #     - GMT offset from Greenwich Mean Time: For example, `GMT+8:00` (UTC+8) or `GMT-7:00` (UTC-7). When using the GMT format, leading zeros are not supported for the hour value.
        #     - Time zone abbreviation: Only UTC (Coordinated Universal Time) is supported.
        # 
        #   For example, to execute a command once at 10:15 every day in 2022 in China/Shanghai time, use `0 15 10 ? * * 2022 Asia/Shanghai`. To execute a command every 30 minutes from 10:00 to 11:30 every day in 2022 in UTC+8, use `0 0/30 10-11 * * ? 2022 GMT+8:00`. To execute a command every 5 minutes from 14:00 to 14:55 every day in October every two years starting from 2022 in UTC, use `0 0/5 14 * 10 ? 2022/2 UTC`.
        # 
        #     >The minimum time interval must be greater than or equal to the timeout period of the scheduled task and no less than 10 seconds.
        self.frequency = frequency
        # The ECS instance ID array. Array length: 1 to 100.
        self.instance_id = instance_id
        # Specifies whether to retain the command after it is run. Valid values:
        # 
        # - true: The command is retained. You can run it again by calling InvokeCommand. The command counts against the Cloud Assistant command quota.
        # - false: The command is not retained. It is automatically deleted after execution and does not count against the Cloud Assistant command quota.
        # 
        # Default value: false.
        self.keep_command = keep_command
        # The bootstrap program for script execution. The value can be up to 1 KB in length.
        self.launcher = launcher
        # The command name. The name supports all character sets and can be up to 128 characters in length.
        self.name = name
        # The OSS delivery configuration for command execution output.
        # 
        # - Format: oss://${BucketName}/${Prefix}, where ${BucketName} is the name of the destination OSS bucket and ${Prefix} is the directory prefix of the destination.
        self.oss_output_delivery = oss_output_delivery
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The key-value pairs of custom parameters to pass in when the command contains custom parameters. For example, if the command content is `echo {{name}}`, you can use the `Parameter` parameter to pass in the key-value pair `{"name":"Jack"}`. The custom parameter automatically replaces the variable value `name`, and the command that is actually run is `echo Jack`.
        self.parameters_shrink = parameters_shrink
        # The region ID. You can call [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The execution mode of the command. Valid values:
        # 
        # - Once: immediately executes the command.
        # - Period: executes the command on a schedule. If you set this parameter to `Period`, you must also specify the `Frequency` parameter.
        # - NextRebootOnly: automatically executes the command the next time the instance starts.
        # - EveryReboot: automatically executes the command every time the instance starts.
        # - DryRun: performs only a dry run of the request without actually executing the command. The dry run checks items such as request parameters, instance execution environment, and Cloud Assistant Agent status.
        # 
        # Default value:
        # - If the `Frequency` parameter is not specified, the default value is `Once`.
        # - If the `Frequency` parameter is specified, the command is executed as `Period` regardless of whether this parameter is set.
        # 
        # Precautions:
        # - You can call [StopInvocation](https://help.aliyun.com/document_detail/64838.html) to stop a pending or scheduled command.
        # - If this parameter is set to `Period` or `EveryReboot`, you can call [DescribeInvocationResults](https://help.aliyun.com/document_detail/64845.html) and specify `IncludeHistory=true` to view the historical records of scheduled command executions.
        self.repeat_mode = repeat_mode
        # The ID of the resource group for the command execution. When you specify this parameter:
        # 
        # - If the ECS instance specified by InstanceId belongs to a non-default resource group, the ECS instance must belong to this resource group.
        # 
        # - You can filter command execution results by specifying this parameter when you call [DescribeInvocations](https://help.aliyun.com/document_detail/64840.html) or [DescribeInvocationResults](https://help.aliyun.com/document_detail/64845.html).
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The tags that are used to filter instances. Array length: 0 to 20. You can run commands on instances that have the same tags in batches without specifying InstanceId.
        self.resource_tag = resource_tag
        # The tags. Array length: 0 to 20.
        self.tag = tag
        # The mode in which the task is stopped (manually stopped or interrupted due to timeout). Valid values:
        self.termination_mode = termination_mode
        # > This parameter is deprecated and has no effect if specified.
        self.timed = timed
        # The timeout period for the command execution. Unit: seconds.
        # 
        # A timeout occurs when the command cannot run due to process issues, missing modules, or missing Cloud Assistant Agent. After a timeout, the command process is forcefully terminated.
        # 
        # Default value: 60.
        self.timeout = timeout
        # The type of the command. Valid values:
        # 
        # - RunBatScript: Bat command for Windows instances.
        # - RunPowerShellScript: PowerShell command for Windows instances.
        # - RunShellScript: Shell command for Linux instances.
        # 
        # This parameter is required.
        self.type = type
        # The username that is used to run the command on the ECS instance. The username can be up to 255 characters in length.
        # 
        # - For Linux ECS instances, the command is run by the root user by default.
        # - For Windows ECS instances, the command is run by the System user by default.
        # 
        # You can also specify another existing user of the instance to run the command. Running Cloud Assistant commands as a regular user is more secure. For more information, see [Run Cloud Assistant commands as a regular user](https://help.aliyun.com/document_detail/203771.html).
        self.username = username
        # The name of the password for the user who runs the command on a Windows instance. The value can be up to 255 characters in length.
        self.windows_password_name = windows_password_name
        # The working directory of the command on the ECS instance. Maximum length: 200 characters.
        # 
        # Default value:
        # 
        # - For Linux instances, the default directory is the home directory of the root user, which is `/root`.
        # - For Windows instances, the default directory is the directory where the Cloud Assistant Agent process resides, such as `C:\\Windows\\System32`.
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

        if self.parameters_shrink is not None:
            result['Parameters'] = self.parameters_shrink

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
            self.parameters_shrink = m.get('Parameters')

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
                temp_model = main_models.RunCommandShrinkRequestResourceTag()
                self.resource_tag.append(temp_model.from_map(k1))

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.RunCommandShrinkRequestTag()
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

class RunCommandShrinkRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the command execution. If this value is specified, it cannot be an empty string.
        self.key = key
        # The tag value of the command execution. The value can be an empty string.
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

class RunCommandShrinkRequestResourceTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key that is used to filter instances.
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

