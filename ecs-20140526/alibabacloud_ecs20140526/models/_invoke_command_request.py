# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class InvokeCommandRequest(DaraModel):
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
        parameters: Dict[str, Any] = None,
        region_id: str = None,
        repeat_mode: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        resource_tag: List[main_models.InvokeCommandRequestResourceTag] = None,
        tag: List[main_models.InvokeCommandRequestTag] = None,
        termination_mode: str = None,
        timed: bool = None,
        timeout: int = None,
        username: str = None,
        windows_password_name: str = None,
        working_dir: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. For more information, see [Ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The command ID. You can call the [DescribeCommands](https://help.aliyun.com/document_detail/64843.html) operation to query all available command IDs. 
        # 
        # > For public commands, you can run them by command name. For more information, see [View and run Cloud Assistant public commands](https://help.aliyun.com/document_detail/429635.html).
        # 
        # This parameter is required.
        self.command_id = command_id
        # The container ID. Only 64-bit hexadecimal strings are supported. You can use the `docker://`, `containerd://`, or `cri-o://` prefix to specify the container runtime.
        # 
        # Precautions:
        # - If you specify this parameter, Cloud Assistant runs the script in the specified container on the instance.
        # - If you specify this parameter, the command can only be run on Linux instances where the Cloud Assistant Agent version is 2.2.3.344 or later.
        # 
        #     - For more information about how to view the Cloud Assistant Agent version, see [Install the Cloud Assistant Agent](https://help.aliyun.com/document_detail/64921.html).
        #     - For more information about how to upgrade the Cloud Assistant Agent version, see [Upgrade or disable the upgrade of the Cloud Assistant Agent](https://help.aliyun.com/document_detail/134383.html).
        # 
        # - If you specify this parameter, the `Username` parameter specified in this operation and the `WorkingDir` parameter specified in [CreateCommand](https://help.aliyun.com/document_detail/64844.html) do not take effect. The command can only be run by the default user of the container in the default working directory of the container. For more information, see [Use Cloud Assistant to run commands in containers](https://help.aliyun.com/document_detail/456641.html).
        # - If you specify this parameter, only shell scripts can be run in Linux containers. You cannot specify an interpreter for the script content by using a command such as `#!/usr/bin/python` at the beginning of the script. For more information, see [Use Cloud Assistant to run commands in containers](https://help.aliyun.com/document_detail/456641.html).
        self.container_id = container_id
        # The container name.
        # 
        # Precautions:
        # - If you specify this parameter, Cloud Assistant runs the script in the specified container on the instance.
        # - If you specify this parameter, the command can only be run on Linux instances where the Cloud Assistant Agent version is 2.2.3.344 or later.
        # 
        #     - For more information about how to view the Cloud Assistant Agent version, see [Install the Cloud Assistant Agent](https://help.aliyun.com/document_detail/64921.html).
        #     - For more information about how to upgrade the Cloud Assistant Agent version, see [Upgrade or disable the upgrade of the Cloud Assistant Agent](https://help.aliyun.com/document_detail/134383.html).
        # - If you specify this parameter, the `Username` parameter specified in this operation and the `WorkingDir` parameter specified in [CreateCommand](https://help.aliyun.com/document_detail/64844.html) do not take effect. The command can only be run by the default user of the container in the default working directory of the container. For more information, see [Use Cloud Assistant to run commands in containers](https://help.aliyun.com/document_detail/456641.html).
        # - If you specify this parameter, only shell scripts can be run in Linux containers. You cannot specify an interpreter for the script content by using a command such as `#!/usr/bin/python` at the beginning of the script. For more information, see [Use Cloud Assistant to run commands in containers](https://help.aliyun.com/document_detail/456641.html).
        self.container_name = container_name
        # The execution time of the scheduled command. Three scheduled execution modes are supported: execution at fixed intervals (based on rate expressions), one-time execution at a specified time, and clock-based scheduled execution (based on cron expressions).
        # 
        # - Execution at fixed intervals: runs the command at a specified interval based on a rate expression. The interval can be set in seconds (s), minutes (m), hours (h), or days (d). This mode is suitable for scenarios where tasks are run at fixed intervals. The format is `rate(<interval value><interval unit>)`. For example, to run the command every 5 minutes, use `rate(5m)`. The following limits apply to execution at fixed intervals:
        #     - The specified interval must not exceed 7 days or be less than 60 seconds, and must be greater than the timeout period of the scheduled task.
        #     - The execution interval is based only on the fixed frequency and is independent of the actual time required to run the task. For example, if you set the command to run every 5 minutes and the task takes 2 minutes to complete, the next execution starts 3 minutes after the task is completed.
        #     - The task is not run immediately upon creation. For example, if you set the command to run every 5 minutes, the command is not run immediately upon task creation, but starts 5 minutes after the task is created.
        # 
        # - One-time execution at a specified time: runs the command once at the specified time zone and time point. The format is `at(yyyy-MM-dd HH:mm:ss <time zone>)`. If you do not specify a time zone, the UTC time zone is used by default. The time zone supports the following three formats:
        #     - Time zone full name: for example, `Asia/Shanghai` (China/Shanghai time) and `America/Los_Angeles` (US/Los Angeles time).
        #     - Time zone offset from Greenwich Mean Time: for example, `GMT+8:00` (East 8th zone) and `GMT-7:00` (West 7th zone). When you use the GMT format, leading zeros are not supported for the hour.
        #     - Time zone abbreviation: only UTC (Coordinated Universal Time) is supported.
        # 
        #   For example, to run the command once at 13:15:30 on June 6, 2022 in the China/Shanghai time zone, use `at(2022-06-06 13:15:30 Asia/Shanghai)`. To run the command once at 13:15:30 on June 6, 2022 in the West 7th zone, use `at(2022-06-06 13:15:30 GMT-7:00)`.
        # 
        # - Clock-based scheduled execution (based on cron expressions): runs the command based on a cron expression. The format is `<seconds> <minutes> <hours> <day of month> <month> <day of week> <year (optional)> <time zone>`, which is `<cron expression> <time zone>`. The scheduled task execution time is calculated and executed based on the cron expression in the specified time zone. If you do not specify a time zone, the internal system time zone of the instance that runs the scheduled task is used by default. For more information about cron expressions, see [Cron expressions](https://help.aliyun.com/document_detail/64769.html). The time zone supports the following three formats:
        #     - Time zone full name: for example, `Asia/Shanghai` (China/Shanghai time) and `America/Los_Angeles` (US/Los Angeles time).
        #     - Time zone offset from Greenwich Mean Time: for example, `GMT+8:00` (East 8th zone) and `GMT-7:00` (West 7th zone). When you use the GMT format, leading zeros are not supported for the hour.
        #     - Time zone abbreviation: only UTC (Coordinated Universal Time) is supported.
        #   For example, to run the command once at 10:15 every day in 2022 in the China/Shanghai time zone, use `0 15 10 ? * * 2022 Asia/Shanghai`. To run the command every half hour from 10:00 to 11:30 every day in 2022 in the East 8th zone, use `0 0/30 10-11 * * ? 2022 GMT+8:00`. To run the command every 5 minutes from 14:00 to 14:55 every day in October every two years starting from 2022 in the UTC time zone, use `0 0/5 14 * 10 ? 2022/2 UTC`.
        # 
        #     > The minimum specified time interval must be greater than or equal to the timeout period of the scheduled task and not less than 10 seconds.
        self.frequency = frequency
        # The list of instance IDs on which the command is run. You can specify up to 100 instance IDs. Valid values of N: 1 to 100.
        # 
        # You can also apply for a quota increase in Quota Center. The quota name is the maximum number of instances supported for command execution.
        self.instance_id = instance_id
        # The bootstrap program for script execution. The length cannot exceed 1 KB.
        self.launcher = launcher
        # The OSS data shipping configuration for the command execution output.
        # 
        # - Format: `oss://${BucketName}/${Prefix}`. `${BucketName}` is the name of the OSS bucket to which the data is shipped, and `${Prefix}` is the directory prefix to which the data is shipped.
        self.oss_output_delivery = oss_output_delivery
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The key-value pairs of custom parameters passed when the command is run if the custom parameter feature is enabled. The number of custom parameters ranges from 0 to 10.
        # 
        # - The key in the map cannot be an empty string and can be up to 64 characters in length.
        # - The value in the map can be an empty string.
        # - The total length of the custom parameters and the original command content cannot exceed 24 KB after Base64 encoding.
        # - The set of custom parameter names must be a subset of the parameter set defined when the command was created. For parameters that are not passed, you can use an empty string instead.
        # 
        # You can leave this parameter unspecified to disable custom parameters.
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
        # - DryRun: only prechecks the request. The command is not actually run. The check items include the request parameters, instance execution environment, and Cloud Assistant Agent running status.
        # 
        # Default value:
        # 
        # - If you do not specify the `Frequency` parameter, the default value is `Once`.
        # - If you specify the `Frequency` parameter, the value is processed as `Period` regardless of whether this parameter is set.
        # 
        # Precautions:
        # 
        # - You can call the [StopInvocation](https://help.aliyun.com/document_detail/64838.html) operation to stop a pending or scheduled command.
        # - If you set this parameter to `Period` or `EveryReboot`, you can call the [DescribeInvocationResults](https://help.aliyun.com/document_detail/64845.html) operation and set `IncludeHistory` to `true` to view the historical records of the scheduled command execution.
        self.repeat_mode = repeat_mode
        # The ID of the resource group in which the command is run. When you specify this parameter:
        # 
        # - If the ECS instance specified by InstanceId belongs to a non-default resource group, the ECS instance must belong to this resource group.
        # 
        # - You can specify this parameter to filter the corresponding command execution results by calling the [DescribeInvocations](https://help.aliyun.com/document_detail/64840.html) or [DescribeInvocationResults](https://help.aliyun.com/document_detail/64845.html) operation.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The list of tags used to filter instances. You can run the command on instances with the same tag in batches without specifying InstanceId.
        self.resource_tag = resource_tag
        # The list of tags.
        self.tag = tag
        # The mode used when the task is stopped (manually stopped or interrupted due to execution timeout). Valid values:
        # - Process: stops the current script process.
        # - ProcessTree: stops the current process tree, which includes the script process and all its child processes.
        self.termination_mode = termination_mode
        # **[Deprecated]** This parameter is deprecated and does not take effect even if it is specified.
        self.timed = timed
        # The timeout period for running the command. Unit: seconds.
        # 
        # - The value cannot be less than 10.
        # 
        # - A timeout occurs when the command cannot be run due to process issues, missing modules, or a missing Cloud Assistant Agent. After a timeout, the command process is forcibly terminated.
        # 
        # - If you do not specify this parameter, the timeout period specified when the command was created is used.
        # 
        # - This value applies only to the current command execution and does not change the timeout period of the command itself.
        self.timeout = timeout
        # The name of the user that runs the command on the ECS instance. The name can be up to 255 characters in length.
        # 
        # - For ECS instances that run Linux, the command is run by the root user by default.
        # - For ECS instances that run Windows, the command is run by the System user by default.
        # 
        # You can also specify another existing user on the instance to run the command. Running Cloud Assistant commands as a regular user is more secure. For more information, see [Configure a regular user to run Cloud Assistant commands](https://help.aliyun.com/document_detail/203771.html).
        self.username = username
        # The name of the password for the user that executes the command on a Windows instance. The name can be up to 255 characters in length.
        # 
        # If you want to execute the command on a Windows instance as a non-default user (other than System), you must specify both `Username` and this parameter. To reduce the risk of password leakage, the plaintext password must be hosted in the parameter repository of System Operations Management. Here, you only pass the name of the password. For more information, see [Encrypt parameters](https://help.aliyun.com/document_detail/186828.html) and [Settings for regular users to execute Cloud Assistant commands](https://help.aliyun.com/document_detail/203771.html).
        # 
        # > You do not need to pass this parameter when you run the command as the root user on a Linux instance or the System user on a Windows instance.
        self.windows_password_name = windows_password_name
        # The directory in which the command is run on the ECS instance. The length cannot exceed 200 characters.
        # - If you do not specify this parameter, the running directory specified when the command was created is used.
        # - This value applies only to the current command execution and does not change the running directory of the command itself.
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
                temp_model = main_models.InvokeCommandRequestResourceTag()
                self.resource_tag.append(temp_model.from_map(k1))

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.InvokeCommandRequestTag()
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

class InvokeCommandRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key for the command to execute. Valid values of N: 1 to 20. The value cannot be an empty string.
        # 
        # If you use a single tag to filter resources, the resource count under the tag cannot exceed 1,000. If you use multiple tags to filter resources, the resource count of resources attached to all the specified tags cannot exceed 1,000. If the resource count exceeds 1,000, you must use the [ListTagResources](https://help.aliyun.com/document_detail/110425.html) operation to query the resources.
        # 
        # The value can be up to 64 characters in length and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
        self.key = key
        # The tag value of the command execution. Valid values of N: 1 to 20. The value can be an empty string.
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

class InvokeCommandRequestResourceTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key used to filter instances.
        # 
        # Precautions:
        # 
        # - This parameter conflicts with the InstanceId parameter and cannot be specified at the same time.
        # 
        # - Valid values of N: 1 to 10. The value cannot be an empty string.
        # 
        # - The number of instances under the tag cannot exceed the limit of InstanceId.N. If the number of instances exceeds the limit, control the number of instances by adding batch tags, such as batch: b1.
        # 
        # - The value can be up to 64 characters in length and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
        self.key = key
        # The tag value used to filter instances.
        # 
        # Precautions:
        # 
        # - Valid values of N: 1 to 10.
        # - The value can be an empty string.
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

