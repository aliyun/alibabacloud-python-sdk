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
        # A client-generated token that is used to ensure the idempotence of the request. You must make sure that the token is unique among different requests. The `ClientToken` parameter can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The command content, which can be in plaintext or Base64-encoded. Note the following:
        # 
        # - The size of the Base64-encoded command content is limited to 18 KB if `KeepCommand` is `true`, or 24 KB if `KeepCommand` is `false`.
        # 
        # - If the command content is Base64-encoded, you must set `ContentEncoding` to `Base64`.
        # 
        # - Set `EnableParameter` to `true` to enable the custom parameter feature in the command content.
        # 
        #   - Define custom parameters by using the `{{}}` format. Spaces and line breaks before and after the parameter names within `{{}}` are ignored.
        # 
        #   - You can define up to 20 custom parameters.
        # 
        #   - A custom parameter name can contain only letters, digits, underscores (_), and hyphens (-). The name is case-insensitive and cannot start with `acs::`, which is reserved for built-in environment parameters.
        # 
        #   - A custom parameter name can be up to 64 bytes long.
        # 
        # - You can use built-in environment parameters, which Cloud Assistant automatically replaces with their corresponding values at runtime. The following built-in environment parameters are supported:
        # 
        #   - `{{ACS::RegionId}}`: the region ID.
        # 
        #   - `{{ACS::AccountId}}`: the UID of the Alibaba Cloud account.
        # 
        #   - `{{ACS::InstanceId}}`: the instance ID. To use this parameter on multiple instances, the required Cloud Assistant Agent version is 2.2.3.309 or later for Linux instances, or 2.1.3.309 or later for Windows instances.
        # 
        #     - Linux: 2.2.3.309
        # 
        #     - Windows: 2.1.3.309
        # 
        #   - `{{ACS::InstanceName}}`: the instance name. To use this parameter on multiple instances, the required Cloud Assistant Agent version is 2.2.3.344 or later for Linux instances, or 2.1.3.344 or later for Windows instances.
        # 
        #     - Linux: 2.2.3.344
        # 
        #     - Windows: 2.1.3.344
        # 
        #   - `{{ACS::InvokeId}}`: the invocation ID. To use this parameter, the required Cloud Assistant Agent version is 2.2.3.309 or later for Linux instances, or 2.1.3.309 or later for Windows instances.
        # 
        #     - Linux: 2.2.3.309
        # 
        #     - Windows: 2.1.3.309
        # 
        #   - `{{ACS::CommandId}}`: the command ID. To use this parameter, the required Cloud Assistant Agent version is 2.2.3.309 or later for Linux instances, or 2.1.3.309 or later for Windows instances.
        # 
        #     - Linux: 2.2.3.309
        # 
        #     - Windows: 2.1.3.309
        # 
        # This parameter is required.
        self.command_content = command_content
        # The ID of the container. The ID must be a 64-bit hexadecimal string. You can add the `docker://`, `containerd://`, or `cri-o://` prefix to explicitly specify the container runtime.
        # 
        # Notes:
        # 
        # - If you specify this parameter, Cloud Assistant runs the script in the specified container of the instance.
        # 
        # - This parameter is supported only on Linux instances with Cloud Assistant Agent version 2.2.3.344 or later.
        # 
        # - If you specify this parameter, the specified `Username` and `WorkingDir` parameters are ignored. The command is run only by the default user in the default working directory of the container. For more information, see [Run commands in a container by using Cloud Assistant](https://help.aliyun.com/document_detail/456641.html).
        # 
        # > In Linux containers, you can run only Shell scripts. You cannot use commands such as `#!/usr/bin/python` at the beginning of a script to specify an interpreter. For more information, see [Run commands in a container by using Cloud Assistant](https://help.aliyun.com/document_detail/456641.html).
        self.container_id = container_id
        # The name of the container.
        # 
        # Notes:
        # 
        # - If you specify this parameter, Cloud Assistant runs the script in the specified container of the instance.
        # 
        # - This parameter is supported only on Linux instances with Cloud Assistant Agent version 2.2.3.344 or later.
        # 
        # - If you specify this parameter, the specified `Username` and `WorkingDir` parameters are ignored. The command is run only by the default user in the default working directory of the container. For more information, see [Run commands in a container by using Cloud Assistant](https://help.aliyun.com/document_detail/456641.html).
        # 
        # > In Linux containers, you can run only Shell scripts. You cannot use commands such as `#!/usr/bin/python` at the beginning of a script to specify an interpreter. For more information, see [Run commands in a container by using Cloud Assistant](https://help.aliyun.com/document_detail/456641.html).
        self.container_name = container_name
        # The encoding mode of the command content (`CommandContent`). Valid values (case-insensitive):
        # 
        # - `PlainText`: The command content is not encoded and is transmitted in plaintext.
        # 
        # - `Base64`: The command content is Base64-encoded.
        # 
        # Default value: `PlainText`. If you specify an invalid value, the value is automatically set to `PlainText`.
        self.content_encoding = content_encoding
        # The description of the command. It can be up to 512 characters long and supports all character sets.
        self.description = description
        # Specifies whether to use custom parameters in the command.
        # 
        # Default value: false.
        self.enable_parameter = enable_parameter
        # The schedule for the command. You can specify a rate expression, an at expression for one-time execution, or a cron expression.
        # 
        # - **Fixed-interval execution**: Runs the command at fixed intervals defined by a rate expression. You can specify the interval in seconds (s), minutes (m), hours (h), or days (d). This method is suitable for tasks that must be run at fixed intervals. The format is `rate(<value><unit>)`. For example, to run a command every 5 minutes, use `rate(5m)`. The following limits apply to this method:
        # 
        #   - The interval must be in the range of 60 seconds to 7 days, and must be longer than the timeout of the scheduled task.
        # 
        #   - The interval is fixed and starts from the beginning of the previous execution, not from its completion.
        # 
        #   - The task does not immediately run after it is created. For example, if you set an interval of 5 minutes, the first run starts 5 minutes after the task is created.
        # 
        # - **One-time execution**: Run the command once at a specified time and in a specified time zone. The format is `at(yyyy-MM-dd HH:mm:ss <time_zone>)`. If you do not specify a time zone, UTC is used by default. The following time zone formats are supported:
        # 
        #   - Full time zone name, such as `Asia/Shanghai` or `America/Los_Angeles`.
        # 
        #   - Offset from GMT, such as `GMT+8:00` or `GMT-7:00`. When you use the GMT format, you cannot add a leading zero to the hour.
        # 
        #   - Time zone abbreviation. Only `UTC` is supported.
        # 
        #   Example 1: To run a task at 13:15:30 on June 6, 2022 in the `Asia/Shanghai` time zone, use `at(2022-06-06 13:15:30 Asia/Shanghai)`. Example 2: To run a task at 13:15:30 on June 6, 2022 in the `GMT-7:00` time zone, use `at(2022-06-06 13:15:30 GMT-7:00)`.
        # 
        # - **Scheduled execution based on a cron expression**: Runs the command on a schedule defined by a cron expression. The format is `<second> <minute> <hour> <day_of_month> <month> <day_of_week> <year (optional)> <time_zone>`, or `<cron_expression> <time_zone>`. The task is run based on the cron expression in the specified time zone. If you do not specify a time zone, the system time zone of the instance where the task is run is used by default. For more information about cron expressions, see [Cron expressions](https://help.aliyun.com/document_detail/64769.html). The following time zone formats are supported:
        # 
        #   - Full time zone name, such as `Asia/Shanghai` or `America/Los_Angeles`.
        # 
        #   - Offset from GMT, such as `GMT+8:00` or `GMT-7:00`. When you use the GMT format, you cannot add a leading zero to the hour.
        # 
        #   - Time zone abbreviation. Only `UTC` is supported.
        #     For example, to run a command at 10:15 every day in 2022 in the `Asia/Shanghai` time zone, use `0 15 10 ? * * 2022 Asia/Shanghai`. To run a command every 30 minutes from 10:00 to 11:30 every day in 2022 in the `GMT+8:00` time zone, use `0 0/30 10-11 * * ? 2022 GMT+8:00`. To run a command every 5 minutes from 14:00 to 14:55 every day in October of every two years starting from 2022 in `UTC`, use `0 0/5 14 * 10 ? 2022/2 UTC`.
        # 
        #   > The minimum interval must be greater than or equal to the timeout of the scheduled task, and cannot be less than 10 seconds.
        self.frequency = frequency
        # The IDs of the ECS instances on which to run the command. You can specify from 1 to 100 instance IDs.
        # 
        # If any specified instance does not meet the execution requirements, the entire operation fails.
        # 
        # You can apply for a quota increase in Quota Center. The quota is named Maximum number of instances supported per command execution.
        self.instance_id = instance_id
        # Specifies whether to save the command after it is run. Valid values:
        # 
        # - `true`: Saves the command. You can then re-run it by calling InvokeCommand. Saved commands count towards your Cloud Assistant command quota.
        # 
        # - `false`: Does not save the command. The command is deleted after execution and does not count towards your quota.
        # 
        # Default value: false.
        self.keep_command = keep_command
        # The launcher that is used to run the script. The value can be up to 1 KB in length.
        self.launcher = launcher
        # The name of the command. It can be up to 128 characters long and supports all character sets.
        self.name = name
        # The OSS delivery configuration for the command output.
        # 
        # - Format: oss\\://${BucketName}/${Prefix}, where ${BucketName} is the name of the destination OSS bucket and ${Prefix} is the destination prefix.
        self.oss_output_delivery = oss_output_delivery
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The key-value pairs for custom parameters. For example, if `CommandContent` is `echo {{name}}`, setting `Parameters` to `{"name":"Jack"}` results in the command `echo Jack` being run.
        # 
        # You can specify 0 to 10 key-value pairs. Note the following:
        # 
        # - The key cannot be an empty string and can be up to 64 characters in length.
        # 
        # - The value can be an empty string.
        # 
        # - After Base64 encoding, the total size of the custom parameters and the original command content is limited to 18 KB if `KeepCommand` is `true`, or 24 KB if `KeepCommand` is `false`.
        # 
        # - The set of custom parameter names that you specify must be a subset of the parameters defined in `CommandContent`. The value of an omitted parameter defaults to an empty string.
        # 
        # By default, this parameter is empty, which indicates that no custom parameters are used.
        self.parameters = parameters
        # The ID of the region. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to query the latest Alibaba Cloud regions.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The execution mode of the command. Valid values:
        # 
        # - `Once`: The command is immediately run.
        # 
        # - `Period`: Runs the command as a scheduled task. This mode requires the `Frequency` parameter.
        # 
        # - `NextRebootOnly`: The command is automatically run the next time the instance starts.
        # 
        # - `EveryReboot`: The command is automatically run every time the instance starts.
        # 
        # - `DryRun`: Performs a dry run to check parameters and the environment without actually running the command.
        # 
        # Default value:
        # 
        # - If the `Frequency` parameter is not specified, the default value is `Once`.
        # 
        # - If `Frequency` is specified, this parameter is automatically set to `Period`.
        # 
        # Notes:
        # 
        # - You can call the [StopInvocation](https://help.aliyun.com/document_detail/64838.html) operation to stop pending or scheduled commands.
        # 
        # - If you set this parameter to `Period` or `EveryReboot`, you can call the [DescribeInvocationResults](https://help.aliyun.com/document_detail/64845.html) operation and set `IncludeHistory=true` to query the historical execution records of the scheduled command.
        self.repeat_mode = repeat_mode
        # The ID of the resource group for the command execution. When you specify this parameter, the following rules apply:
        # 
        # - If an ECS instance specified by `InstanceId` is in a non-default resource group, it must belong to the resource group specified by this parameter.
        # 
        # - You can use this parameter to filter command execution results when you call the [DescribeInvocations](https://help.aliyun.com/document_detail/64840.html) or [DescribeInvocationResults](https://help.aliyun.com/document_detail/64845.html) operation.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Tags used to filter instances for command execution. This allows you to run the command on all instances with matching tags, as an alternative to specifying instance IDs. The array can contain 0 to 20 tags.
        self.resource_tag = resource_tag
        # An array of tag pairs. The array can contain 0 to 20 tags.
        self.tag = tag
        # The mode for stopping the task when it is manually stopped or times out. Valid values:
        # 
        # - `Process`: Stops the current script process.
        # 
        # - `ProcessTree`: Stops the current process tree. A process tree includes the current script process and all of its subprocesses.
        self.termination_mode = termination_mode
        # > This parameter is deprecated and no longer has any effect.
        self.timed = timed
        # The command execution timeout, in seconds.
        # 
        # A timeout forcibly terminates the command process if the command fails to run due to exceptions, such as a process conflict, a missing module, or a disabled Cloud Assistant Agent.
        # 
        # Default value: 60.
        self.timeout = timeout
        # The type of the command. Valid values:
        # 
        # - `RunBatScript`: Bat commands for Windows instances.
        # 
        # - `RunPowerShellScript`: PowerShell commands for Windows instances.
        # 
        # - `RunShellScript`: Shell commands for Linux instances.
        # 
        # This parameter is required.
        self.type = type
        # The name of the user that runs the command on the ECS instance. The name can be up to 255 characters in length.
        # 
        # - Default on Linux: `root`.
        # 
        # - Default on Windows: `System`.
        # 
        # You can specify another existing user on the instance to run the command. Running Cloud Assistant commands as a standard user is more secure. For more information, see [Run Cloud Assistant commands as a standard user](https://help.aliyun.com/document_detail/203771.html).
        self.username = username
        # The name of the password of the user that runs the command on a Windows instance. The name can be up to 255 characters in length.
        # 
        # To run a command as a non-default user on a Windows instance, you must specify both `Username` and `WindowsPasswordName`. To reduce the risk of password leaks, we recommend storing the password in OOS Parameter Store and providing the parameter name here. For more information, see [Encryption parameters](https://help.aliyun.com/document_detail/186828.html) and [Run Cloud Assistant commands as a standard user](https://help.aliyun.com/document_detail/203771.html).
        # 
        # > You do not need to specify this parameter when you run a command as the `root` user on a Linux instance or as the `System` user on a Windows instance.
        self.windows_password_name = windows_password_name
        # The working directory for the command on the instance. The path can be up to 200 characters long.
        # 
        # Default values:
        # 
        # - For Linux instances, the default is the home directory of the `root` user (`/root`).
        # 
        # - For Windows instances, the default is the directory of the Cloud Assistant Agent process, such as `C:\\Windows\\System32`.
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
        # The tag key for the command execution. The key cannot be an empty string.
        # 
        # The key can be up to 64 characters long and cannot start with `aliyun` or `acs:`. It also cannot contain `http://` or `https://`.
        # 
        # The value can be up to 64 characters long and cannot start with `aliyun` or `acs:` or contain `http://` or `https://`.
        self.key = key
        # The tag value for the command execution. The value can be an empty string.
        # 
        # The value can be up to 128 characters long and cannot contain `http://` or `https://`.
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
        # The tag key that is used to filter instances.
        # 
        # Notes:
        # 
        # - You cannot specify both this parameter and the InstanceId parameter.
        # 
        # - The tag key cannot be an empty string.
        # 
        # - The number of instances matching the specified tag cannot exceed the per-execution instance limit (100 by default). If the number of matching instances exceeds this limit, you can use additional tags, such as `batch:b1`, to refine the selection.
        # 
        # - The value can be up to 64 characters in length and cannot start with `aliyun` or `acs:`. It also cannot contain `http://` or `https://`.
        self.key = key
        # The tag value that is used to filter instances.
        # 
        # Notes:
        # 
        # - The value can be an empty string.
        # 
        # - The value can be up to 128 characters in length and cannot contain `http://` or `https://`.
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

