# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from darabonba.model import DaraModel

class ModifyInvocationAttributeRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        command_content: str = None,
        content_encoding: str = None,
        enable_parameter: bool = None,
        frequency: str = None,
        instance_id: List[str] = None,
        invoke_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        parameters: Dict[str, Any] = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that the value is unique among different requests. The **ClientToken** value can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The modified command content. The command content can be plaintext or Base64-encoded. Take note of the following items:
        # 
        # - The size of the Base64-encoded command content cannot exceed 24 KB.
        # - If the command content is Base64-encoded, you must set `ContentEncoding` to `Base64`.
        # - You can set `EnableParameter` to `true` to enable the custom parameter feature in the command content:
        #     - Define custom parameters by enclosing them in `{{}}`. Spaces and line breaks before and after the parameter names within `{{}}` are ignored.
        #     - You can define up to 20 custom parameters.
        #     - A custom parameter name can contain letters, digits, hyphens (-), and underscores (_). The `acs::` prefix is not supported for specifying non-built-in environment variables. Other characters are not supported. Parameter names are not case-sensitive.
        #     - A single custom parameter name cannot exceed 64 bytes in length.
        # 
        # - You can specify built-in environment variables as custom parameters. When the command is executed, you do not need to manually assign values to these parameters. Cloud Assistant automatically replaces them with the corresponding values in the environment. The following built-in environment variables are supported:
        #     - `{{ACS::RegionId}}`: the region ID.
        #     - `{{ACS::AccountId}}`: the UID of the Alibaba Cloud account.
        #     - `{{ACS::InstanceId}}`: the instance ID. If the command is sent to multiple instances and you want to specify `{{ACS::InstanceId}}` as a built-in environment variable, make sure that the Cloud Assistant Agent version is not earlier than the following versions:
        #         - Linux: 2.2.3.309
        #         - Windows: 2.1.3.309
        #     - `{{ACS::InstanceName}}`: the instance name. If the command is sent to multiple instances and you want to specify `{{ACS::InstanceName}}` as a built-in environment variable, make sure that the Cloud Assistant Agent version is not earlier than the following versions:
        #         - Linux: 2.2.3.344
        #         - Windows: 2.1.3.344
        #     - `{{ACS::InvokeId}}`: the command execution ID. If you want to specify `{{ACS::InvokeId}}` as a built-in environment variable, make sure that the Cloud Assistant Agent version is not earlier than the following versions:
        #         - Linux: 2.2.3.309
        #         - Windows: 2.1.3.309
        #     - `{{ACS::CommandId}}`: the command ID. If you call this operation to execute a command and want to specify `{{ACS::CommandId}}` as a built-in environment variable, make sure that the Cloud Assistant Agent version is not earlier than the following versions: 
        #         - Linux: 2.2.3.309
        #         - Windows: 2.1.3.309
        self.command_content = command_content
        # The encoding method of the command content specified by `CommandContent`. Valid values (case-insensitive):
        # 
        # - PlainText: no encoding. The command content is transmitted in plaintext.
        # - Base64: Base64 encoding.
        # 
        # Default value: PlainText. If an invalid value is specified, PlainText is used.
        self.content_encoding = content_encoding
        # Specifies whether the modified command contains custom parameters.
        # - If you enable custom parameters or modify the custom parameters specified by `Parameters`, set this parameter to `true`.
        # - If you do not modify the custom parameters specified by `Parameters`, leave this parameter empty or set it to `false`.
        self.enable_parameter = enable_parameter
        # The modified scheduled execution frequency. This parameter takes effect only when `RepeatMode` is set to `Period`. Three scheduled execution modes are supported: execution at a fixed time interval (based on a rate expression), one-time execution at a specified time, and clock-based scheduled execution (based on a cron expression).
        # 
        # - Execution at a fixed time interval: based on a rate expression, the command is executed at the specified time interval. The time interval can be specified in seconds (s), minutes (m), hours (h), or days (d). This mode is suitable for scenarios where tasks are executed at fixed time intervals. The format is `rate(<interval value><interval unit>)`. For example, to execute the command every 5 minutes, use `rate(5m)`. The following limits apply to execution at a fixed time interval:
        #     - The specified time interval must not exceed 7 days, must not be less than 60 seconds, and must be greater than the timeout period specified when the scheduled task was created.
        #     - The execution interval is based only on the fixed frequency and is independent of the actual time required to execute the task. For example, if the command is executed every 5 minutes and the task takes 2 minutes to complete, the next execution starts 3 minutes after the task is completed.
        #     - The next execution time is calculated based on the task creation time (refer to [CreationTime](https://help.aliyun.com/document_detail/64840.html) returned by `DescribeInvocations`, not the modification time) and the modified execution interval.
        # 
        # - One-time execution at a specified time: the command is executed once at the specified time zone and time point. The format is `at(yyyy-MM-dd HH:mm:ss <time zone>)`, which means `at(year-month-day hour:minute:second <time zone>)`. If no time zone is specified, the UTC time zone is used by default. The time zone supports the following three formats:
        #     - Time zone full name: such as `Asia/Shanghai` (China/Shanghai time) and `America/Los_Angeles` (US/Los Angeles time).
        #     - Time zone offset from Greenwich Mean Time: such as `GMT+8:00` (UTC+8) and `GMT-7:00` (UTC-7). When the GMT format is used, leading zeros are not supported for the hour.
        #     - Time zone abbreviation: only UTC (Coordinated Universal Time) is supported.
        # 
        #   For example, to execute the command once at 13:15:30 on June 6, 2022 in the China/Shanghai time zone, use `at(2022-06-06 13:15:30 Asia/Shanghai)`. To execute the command once at 13:15:30 on June 6, 2022 in the UTC-7 time zone, use `at(2022-06-06 13:15:30 GMT-7:00)`.
        # 
        # - Clock-based scheduled execution (based on a cron expression): based on a cron expression, the command is executed according to the scheduled task settings. The format is `<seconds> <minutes> <hours> <day of month> <month> <day of week> <year (optional)> <time zone>`, which means `<cron expression> <time zone>`. In the specified time zone, the execution time of the scheduled task is calculated based on the cron expression and executed. If no time zone is specified, the internal system time zone of the instance that executes the scheduled task is used by default. For more information about cron expressions, see [Cron expressions](https://help.aliyun.com/document_detail/64769.html). The time zone supports the following three formats:
        #     - Time zone full name: such as `Asia/Shanghai` (China/Shanghai time) and `America/Los_Angeles` (US/Los Angeles time).
        #     - Time zone offset from Greenwich Mean Time: such as `GMT+8:00` (UTC+8) and `GMT-7:00` (UTC-7). When the GMT format is used, leading zeros are not supported for the hour.
        #     - Time zone abbreviation: only UTC (Coordinated Universal Time) is supported.
        #   For example, to execute the command once at 10:15 every day in 2022 in the China/Shanghai time zone, use `0 15 10 ? * * 2022 Asia/Shanghai`. To execute the command every half hour from 10:00 to 11:30 every day in 2022 in the UTC+8 time zone, use `0 0/30 10-11 * * ? 2022 GMT+8:00`. To execute the command every 5 minutes from 14:00 to 14:55 every day in October every two years starting from 2022 in the UTC time zone, use `0 0/5 14 * 10 ? 2022/2 UTC`.
        # 
        #     > The minimum time interval must be greater than or equal to the timeout period specified when the scheduled task was created, and must not be less than 10 seconds.
        self.frequency = frequency
        # The ECS instance ID or managed instance ID to be added to the task.
        self.instance_id = instance_id
        # The execution ID of the command for the task to be modified.
        # 
        # This parameter is required.
        self.invoke_id = invoke_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The key-value pairs of the custom parameters passed when the command is executed. This parameter is valid when the command contains custom parameters.
        # 
        # You can specify 0 to 10 custom parameters. Take note of the following items:
        # 
        # - A key cannot be an empty string and can be up to 64 characters in length.
        # - A value can be an empty string.
        # - After the custom parameters and the original command content are Base64-encoded, the size of the Base64-encoded command content cannot exceed 24 KB.
        # - The set of custom parameter names must be a subset of the parameter set defined when the command was created. For parameters that are not passed, you can use empty strings.
        # 
        # Default value: empty. This indicates that the key-value pairs of custom parameters are not modified.
        self.parameters = parameters
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.command_content is not None:
            result['CommandContent'] = self.command_content

        if self.content_encoding is not None:
            result['ContentEncoding'] = self.content_encoding

        if self.enable_parameter is not None:
            result['EnableParameter'] = self.enable_parameter

        if self.frequency is not None:
            result['Frequency'] = self.frequency

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.invoke_id is not None:
            result['InvokeId'] = self.invoke_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('CommandContent') is not None:
            self.command_content = m.get('CommandContent')

        if m.get('ContentEncoding') is not None:
            self.content_encoding = m.get('ContentEncoding')

        if m.get('EnableParameter') is not None:
            self.enable_parameter = m.get('EnableParameter')

        if m.get('Frequency') is not None:
            self.frequency = m.get('Frequency')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InvokeId') is not None:
            self.invoke_id = m.get('InvokeId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

