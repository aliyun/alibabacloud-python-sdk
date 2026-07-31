# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class InvokeCommandShrinkRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        command_id: str = None,
        container_id: str = None,
        container_name: str = None,
        frequency: str = None,
        instance_id: List[str] = None,
        launcher: str = None,
        oss_output_delivery: str = None,
        owner_account: str = None,
        owner_id: int = None,
        parameters_shrink: str = None,
        region_id: str = None,
        repeat_mode: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        resource_tag: List[main_models.InvokeCommandShrinkRequestResourceTag] = None,
        tag: List[main_models.InvokeCommandShrinkRequestTag] = None,
        termination_mode: str = None,
        timed: bool = None,
        timeout: int = None,
        username: str = None,
        windows_password_name: str = None,
        working_dir: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but make sure that the token is unique among different requests. The ClientToken value can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The command ID. You can call [DescribeCommands](https://help.aliyun.com/document_detail/64843.html) to query all available command IDs. 
        # 
        # >You can run public commands by specifying the command name. For more information, see [View and run Cloud Assistant public commands](https://help.aliyun.com/document_detail/429635.html).
        # 
        # This parameter is required.
        self.command_id = command_id
        # The container ID. Only 64-bit hexadecimal strings are supported. Container IDs that are prefixed with `docker://`, `containerd://`, or `cri-o://` are supported to specify the container runtime.
        # 
        # Usage notes:
        # - If you specify this parameter, Cloud Assistant runs the script in the specified container of the instance.
        # - If you specify this parameter, the command can be run only on Linux instances that have Cloud Assistant Agent 2.2.3.344 or later installed.
        # 
        #     - To view the Cloud Assistant Agent version, see [Install Cloud Assistant Agent](https://help.aliyun.com/document_detail/64921.html).
        #     - To upgrade Cloud Assistant Agent, see [Upgrade or disable upgrades for Cloud Assistant Agent](https://help.aliyun.com/document_detail/134383.html).
        # 
        # - If you specify this parameter, the `Username` parameter specified in this operation and the `WorkingDir` parameter specified in [CreateCommand](https://help.aliyun.com/document_detail/64844.html) do not take effect. The command is run only by the default user in the default working directory of the container. For more information, see [Use Cloud Assistant to run commands in containers](https://help.aliyun.com/document_detail/456641.html).
        # - If you specify this parameter, only shell scripts can be run in Linux containers. You cannot use a format such as `#!/usr/bin/python` at the beginning of a script to specify an interpreter. For more information, see [Use Cloud Assistant to run commands in containers](https://help.aliyun.com/document_detail/456641.html).
        self.container_id = container_id
        # The container name.
        # 
        # Usage notes:
        # - If you specify this parameter, Cloud Assistant runs the script in the specified container of the instance.
        # - If you specify this parameter, the command can be run only on Linux instances that have Cloud Assistant Agent 2.2.3.344 or later installed.
        # 
        #     - To view the Cloud Assistant Agent version, see [Install Cloud Assistant Agent](https://help.aliyun.com/document_detail/64921.html).
        #     - To upgrade Cloud Assistant Agent, see [Upgrade or disable upgrades for Cloud Assistant Agent](https://help.aliyun.com/document_detail/134383.html).
        # - If you specify this parameter, the `Username` parameter specified in this operation and the `WorkingDir` parameter specified in [CreateCommand](https://help.aliyun.com/document_detail/64844.html) do not take effect. The command is run only by the default user in the default working directory of the container. For more information, see [Use Cloud Assistant to run commands in containers](https://help.aliyun.com/document_detail/456641.html).
        # - If you specify this parameter, only shell scripts can be run in Linux containers. You cannot use a format such as `#!/usr/bin/python` at the beginning of a script to specify an interpreter. For more information, see [Use Cloud Assistant to run commands in containers](https://help.aliyun.com/document_detail/456641.html).
        self.container_name = container_name
        # The schedule on which the command is run. Three types of scheduled execution are supported: fixed interval (Rate expression-based), one-time execution at a specified time, and clock-based scheduling (Cron expression-based).
        # 
        # - Fixed interval execution: Based on a Rate expression, the command is run at a set interval. The interval can be specified in seconds (s), minutes (m), hours (h), or days (d). This is suitable for scenarios that require execution at fixed intervals. Format: `rate(<interval value><interval unit>)`. For example, to run the command every 5 minutes, use `rate(5m)`. Fixed interval execution has the following limits:
        #     - The interval must not exceed 7 days or be less than 60 seconds, and must be greater than the timeout period of the scheduled task.
        #     - The interval is based on a fixed frequency and is unrelated to the actual execution time of the task. For example, if the command is set to run every 5 minutes and the task takes 2 minutes to complete, the next round starts 3 minutes after the task completes.
        #     - The task is not run immediately upon creation. For example, if the command is set to run every 5 minutes, it does not run immediately when the task is created. Instead, it starts running 5 minutes after the task is created.
        # 
        # - One-time execution at a specified time: The command is run once at the specified time zone and time. Format: `at(yyyy-MM-dd HH:mm:ss <time zone>)`. If no time zone is specified, UTC is used by default. The time zone can be specified in the following formats:
        #     - Full time zone name: For example, `Asia/Shanghai` or `America/Los_Angeles`.
        #     - GMT offset from Greenwich Mean Time: For example, `GMT+8:00` or `GMT-7:00`. When using the GMT format, leading zeros are not supported in the hour field.
        #     - Time zone abbreviation: Only UTC (Coordinated Universal Time) is supported.
        # 
        #   For example, to run the command once at 13:15:30 on June 6, 2022 in the Asia/Shanghai time zone, use: `at(2022-06-06 13:15:30 Asia/Shanghai)`. To run the command once at 13:15:30 on June 6, 2022 in GMT-7:00, use: `at(2022-06-06 13:15:30 GMT-7:00)`.
        # 
        # - Clock-based scheduling (Cron expression-based): Based on a Cron expression, the command is run according to the specified schedule. Format: `<seconds> <minutes> <hours> <day of month> <month> <day of week> <year (optional)> <time zone>`. The scheduled execution time is calculated based on the Cron expression in the specified time zone. If no time zone is specified, the system time zone of the instance running the scheduled task is used. For more information about Cron expressions, see [Cron expressions](https://help.aliyun.com/document_detail/64769.html). The time zone can be specified in the following formats:
        #     - Full time zone name: For example, `Asia/Shanghai` or `America/Los_Angeles`.
        #     - GMT offset from Greenwich Mean Time: For example, `GMT+8:00` or `GMT-7:00`. When using the GMT format, leading zeros are not supported in the hour field.
        #     - Time zone abbreviation: Only UTC (Coordinated Universal Time) is supported.
        #   For example, to run the command once a day at 10:15 in the Asia/Shanghai time zone in 2022, use `0 15 10 ? * * 2022 Asia/Shanghai`. To run the command every 30 minutes from 10:00 to 11:30 every day in GMT+8:00 in 2022, use `0 0/30 10-11 * * ? 2022 GMT+8:00`. To run the command every 5 minutes from 14:00 to 14:55 every day in October every two years starting from 2022 in UTC, use `0 0/5 14 * 10 ? 2022/2 UTC`.
        # 
        #     >The minimum interval must be greater than or equal to the timeout period of the scheduled task and no less than 10 seconds.
        self.frequency = frequency
        # The list of instances on which to run the command. You can specify up to 100 instance IDs. Valid values of N: 1 to 100.
        # 
        # You can also apply for a quota increase in Quota Center (quota name: Maximum number of instances supported for command execution).
        self.instance_id = instance_id
        # The bootstrap program for script execution. The value cannot exceed 1 KB in length.
        self.launcher = launcher
        # The OSS delivery configuration for command execution output.
        # 
        # - Format: oss://${BucketName}/${Prefix}, where ${BucketName} is the name of the destination OSS bucket and ${Prefix} is the directory prefix for delivery.
        self.oss_output_delivery = oss_output_delivery
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The key-value pairs of custom parameters to pass in when the custom parameter feature is enabled. The number of custom parameters ranges from 0 to 10.
        # 
        # - Map keys cannot be empty strings and can be up to 64 characters in length.
        # - Map values can be empty strings.
        # - After Base64 encoding, the total length of the custom parameters and the original command content cannot exceed 18 KB.
        # - The set of custom parameter names must be a subset of the parameter set defined when the command was created. For parameters that are not passed in, you can use empty strings as substitutes.
        # 
        # You can unset this parameter to disable custom parameters.
        self.parameters_shrink = parameters_shrink
        # The region ID. You can call [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The execution mode of the command. Valid values:
        # 
        # - Once: immediately runs the command.
        # - Period: runs the command on a schedule. If you set this parameter to `Period`, you must also specify the `Frequency` parameter.
        # - NextRebootOnly: automatically runs the command the next time the instance starts.
        # - EveryReboot: automatically runs the command every time the instance starts.
        # - DryRun: performs a dry run of the request without actually running the command. The dry run checks request parameters, instance execution environment, and Cloud Assistant Agent status.
        # 
        # Default value:
        # 
        # - If you do not specify the `Frequency` parameter, the default value is `Once`.
        # - If you specify the `Frequency` parameter, the command is run on a schedule regardless of whether you set this parameter. The value is treated as `Period`.
        # 
        # Usage notes:
        # 
        # - You can call [StopInvocation](https://help.aliyun.com/document_detail/64838.html) to stop a pending or scheduled command.
        # - If you set this parameter to `Period` or `EveryReboot`, you can call [DescribeInvocationResults](https://help.aliyun.com/document_detail/64845.html) and specify `IncludeHistory=true` to view the execution history of the scheduled command.
        self.repeat_mode = repeat_mode
        # The ID of the resource group for the command execution. When you specify this parameter:
        # 
        # - The ECS instance specified by InstanceId must belong to this resource group if the instance is not in the default resource group.
        # 
        # - You can filter command execution results by specifying this parameter (by calling [DescribeInvocations](https://help.aliyun.com/document_detail/64840.html) or [DescribeInvocationResults](https://help.aliyun.com/document_detail/64845.html)).
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The tags used to filter instances. You can run a command in batches on instances that have the same tag without specifying InstanceId.
        self.resource_tag = resource_tag
        # The tags.
        self.tag = tag
        # The mode in which the task is stopped (manually stopped or interrupted due to timeout). Valid values:
        # - Process: stops the current script process.
        # - ProcessTree: stops the current process tree (the script process and all child processes it created).
        self.termination_mode = termination_mode
        # >This parameter is deprecated and has no effect if specified.
        self.timed = timed
        # The timeout period for the command execution. Unit: seconds.
        # 
        # - The value must be at least 10 seconds.
        # 
        # - If the command cannot be run due to process issues, missing modules, or missing Cloud Assistant Agent, a timeout occurs. When a timeout occurs, the command process is forcefully terminated.
        # 
        # - If you do not specify this parameter, the timeout period specified when the command was created is used.
        # 
        # - This value applies only to the current command execution and does not change the timeout period of the command itself.
        self.timeout = timeout
        # The username used to run the command on the ECS instance. The username can be up to 255 characters in length.
        # 
        # - For Linux instances, the root user is used by default.
        # - For Windows instances, the System user is used by default.
        # 
        # You can also specify another existing user on the instance to run the command. Running Cloud Assistant commands as a regular user is more secure. For more information, see [Configure a regular user to run Cloud Assistant commands](https://help.aliyun.com/document_detail/203771.html).
        self.username = username
        # The name of the password for the user who executes the command on a Windows instance. The name can be up to 255 characters in length.
        # 
        # To execute a command as a non-default user (System) on a Windows instance, you must specify both `Username` and this parameter. To reduce the risk of password leaks, store the plaintext password in the parameter repository of operations management, and pass in only the password name here. For more information, see [Encryption parameters](https://help.aliyun.com/document_detail/186828.html) and [Configure a regular user to execute Cloud Assistant commands](https://help.aliyun.com/document_detail/203771.html).
        # 
        # > This parameter is not required when you use the root user on a Linux instance or the System user on a Windows instance to execute the command.
        self.windows_password_name = windows_password_name
        # The directory in which the command is run on the ECS instance. The value can be up to 200 characters in length.
        # - If you do not specify this parameter, the working directory specified when the command was created is used.
        # - This value applies only to the current command execution and does not change the working directory of the command itself.
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

        if self.command_id is not None:
            result['CommandId'] = self.command_id

        if self.container_id is not None:
            result['ContainerId'] = self.container_id

        if self.container_name is not None:
            result['ContainerName'] = self.container_name

        if self.frequency is not None:
            result['Frequency'] = self.frequency

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.launcher is not None:
            result['Launcher'] = self.launcher

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

        if m.get('CommandId') is not None:
            self.command_id = m.get('CommandId')

        if m.get('ContainerId') is not None:
            self.container_id = m.get('ContainerId')

        if m.get('ContainerName') is not None:
            self.container_name = m.get('ContainerName')

        if m.get('Frequency') is not None:
            self.frequency = m.get('Frequency')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Launcher') is not None:
            self.launcher = m.get('Launcher')

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
                temp_model = main_models.InvokeCommandShrinkRequestResourceTag()
                self.resource_tag.append(temp_model.from_map(k1))

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.InvokeCommandShrinkRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('TerminationMode') is not None:
            self.termination_mode = m.get('TerminationMode')

        if m.get('Timed') is not None:
            self.timed = m.get('Timed')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        if m.get('WindowsPasswordName') is not None:
            self.windows_password_name = m.get('WindowsPasswordName')

        if m.get('WorkingDir') is not None:
            self.working_dir = m.get('WorkingDir')

        return self

class InvokeCommandShrinkRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the command execution. Valid values of N: 1 to 20. The tag key cannot be an empty string once specified.
        # 
        # If you use a single tag to filter resources, the number of resources with this tag cannot exceed 1,000. If you use multiple tags to filter resources, the number of resources that are attached with all specified tags cannot exceed 1,000. If the number of resources exceeds 1,000, execute the [ListTagResources](https://help.aliyun.com/document_detail/110425.html) operation to query resources.
        # 
        # The tag key can be up to 64 characters in length and cannot start with `aliyun` or `acs:`, or contain `http://` or `https://`.
        self.key = key
        # The tag value of the command execution. Valid values of N: 1 to 20. The tag value can be an empty string.
        # 
        # The tag value can be up to 128 characters in length and cannot contain `http://` or `https://`.
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

class InvokeCommandShrinkRequestResourceTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key used to filter instances.
        # 
        # Usage notes:
        # 
        # - This parameter conflicts with the InstanceId parameter. You cannot specify both parameters at the same time.
        # 
        # - Valid values of N: 1 to 10. The tag key cannot be an empty string once specified.
        # 
        # - The number of instances with the specified tag cannot exceed the limit of InstanceId.N. If the number of instances exceeds the limit, control the number of instances by adding batch tags, such as batch: b1.
        # 
        # - The tag key can be up to 64 characters in length and cannot start with aliyun or acs:, or contain http:// or https://.
        self.key = key
        # The tag value used to filter instances.
        # 
        # Usage notes:
        # 
        # - Valid values of N: 1 to 10.
        # - The tag value can be an empty string.
        # - The tag value can be up to 128 characters in length and cannot contain http:// or https://.
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

