# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModifyInvocationAttributeShrinkRequest(DaraModel):
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
        parameters_shrink: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but make sure that the token is unique among different requests. The **ClientToken** value can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The modified command content. The command content can be plaintext or Base64-encoded. Note the following items:
        # 
        # - The size of the command content after Base64 encoding cannot exceed 24 KB.
        # - If your command content is Base64-encoded, you must set `ContentEncoding=Base64`.
        # - You can set `EnableParameter=true` to enable the custom parameter feature in the command content:
        #     - Custom parameters are defined by enclosing them in `{{}}`. Spaces and line breaks before and after the parameter name within `{{}}` are ignored.
        #     - The number of custom parameters cannot exceed 20.
        #     - Custom parameter names can contain a-z, A-Z, 0-9, hyphens (-), and underscores (_). The acs:: prefix for specifying non-built-in environment parameters is not supported. Other characters are not supported. Parameter names are case-insensitive.
        #     - A single custom parameter name cannot exceed 64 bytes.
        # 
        # - You can specify built-in environment parameters as custom parameters. When the command is executed, you do not need to manually assign values to the parameters. Cloud Assistant automatically replaces them with the corresponding values in the environment. The following built-in environment parameters are supported:
        #     - `{{ACS::RegionId}}`: The region ID.
        #     - `{{ACS::AccountId}}`: The UID of the Alibaba Cloud account.
        #     - `{{ACS::InstanceId}}`: The instance ID. When the command is sent to multiple instances, to specify `{{ACS::InstanceId}}` as a built-in environment parameter, ensure that the Cloud Assistant Agent version is not earlier than the following versions:
        #         - Linux: 2.2.3.309
        #         - Windows: 2.1.3.309
        #     - `{{ACS::InstanceName}}`: The instance name. When the command is sent to multiple instances, to specify `{{ACS::InstanceName}}` as a built-in environment parameter, ensure that the Cloud Assistant Agent version is not earlier than the following versions:
        #         - Linux: 2.2.3.344
        #         - Windows: 2.1.3.344
        #     - `{{ACS::InvokeId}}`: The command execution ID. To specify `{{ACS::InvokeId}}` as a built-in environment parameter, ensure that the Cloud Assistant Agent version is not earlier than the following versions:
        #         - Linux: 2.2.3.309
        #         - Windows: 2.1.3.309
        #     - `{{ACS::CommandId}}`: The command ID. When you call this operation to execute a command, to specify `{{ACS::CommandId}}` as a built-in environment parameter, ensure that the Cloud Assistant Agent version is not earlier than the following versions: 
        #         - Linux: 2.2.3.309
        #         - Windows: 2.1.3.309
        self.command_content = command_content
        # The encoding method of the command content (`CommandContent`). Valid values (case-insensitive):
        # 
        # - PlainText: no encoding. The content is transmitted in plaintext.
        # - Base64: Base64 encoding.
        # 
        # Default value: PlainText. If an invalid value is specified, it is treated as PlainText.
        self.content_encoding = content_encoding
        # Specifies whether the modified command contains custom parameters.
        # - When you enable custom parameters or modify the custom parameters `Parameters`, set this parameter to `true`.
        # - When you do not modify the custom parameters `Parameters`, do not set this parameter or set it to `false`.
        self.enable_parameter = enable_parameter
        # The modified scheduled execution frequency. This parameter takes effect only when `RepeatMode` is set to `Period`. Three types of scheduled execution are supported: fixed interval execution (based on Rate expressions), one-time execution at a specified time, and clock-based scheduled execution (based on Cron expressions).
        # 
        # - Fixed interval execution: Based on Rate expressions, the command is executed at the specified time interval. The time interval can be specified in seconds (s), minutes (m), hours (h), or days (d). This is applicable to scenarios where tasks are executed at fixed intervals. Format: `rate(<interval value><interval unit>)`. For example, to execute every 5 minutes, the format is `rate(5m)`. The following limits apply to fixed interval execution:
        #     - The specified interval cannot exceed 7 days or be less than 60 seconds, and must be greater than the timeout period specified when the scheduled task was created.
        #     - The execution interval is based only on the fixed frequency and is not related to the actual time required for task execution. For example, if the command is set to execute every 5 minutes and the task takes 2 minutes to complete, the next round of execution starts 3 minutes after the task is completed.
        #     - The next execution time is calculated based on the task creation time (see [CreationTime](https://help.aliyun.com/document_detail/64840.html) returned by `DescribeInvocations`, note that this is not the modification time) and the modified execution interval.
        # 
        # - One-time execution at a specified time: The command is executed once at the specified time zone and time point. Format: `at(yyyy-MM-dd HH:mm:ss <time zone>)`, which is `at(year-month-day hour:minute:second <time zone>)`. If no time zone is specified, the default is UTC. The time zone supports the following three formats:
        #     - Full time zone name: such as `Asia/Shanghai` (China/Shanghai time) or `America/Los_Angeles` (US/Los Angeles time).
        #     - Time zone offset from Greenwich Mean Time: such as `GMT+8:00` (East 8th time zone) or `GMT-7:00` (West 7th time zone). When using the GMT format, leading zeros are not supported in the hour field.
        #     - Time zone abbreviation: Only UTC (Coordinated Universal Time) is supported.
        # 
        #   For example, to execute once at 13:15:30 on June 6, 2022 in China/Shanghai time, the format is: `at(2022-06-06 13:15:30 Asia/Shanghai)`. To execute once at 13:15:30 on June 6, 2022 in the West 7th time zone, the format is: `at(2022-06-06 13:15:30 GMT-7:00)`.
        # 
        # - Clock-based scheduled execution (based on Cron expressions): Based on Cron expressions, the command is executed according to the scheduled task settings. Format: `<seconds> <minutes> <hours> <day of month> <month> <day of week> <year (optional)> <time zone>`, which is `<Cron expression> <time zone>`. The scheduled task execution time is calculated based on the Cron expression in the specified time zone. If no time zone is specified, the default is the internal system time zone of the instance running the scheduled task. For more information about Cron expressions, see [Cron expressions](https://help.aliyun.com/document_detail/64769.html). The time zone supports the following three formats:
        #     - Full time zone name: such as `Asia/Shanghai` (China/Shanghai time) or `America/Los_Angeles` (US/Los Angeles time).
        #     - Time zone offset from Greenwich Mean Time: such as `GMT+8:00` (East 8th time zone) or `GMT-7:00` (West 7th time zone). When using the GMT format, leading zeros are not supported in the hour field.
        #     - Time zone abbreviation: Only UTC (Coordinated Universal Time) is supported.
        #   For example, to execute a command once a day at 10:15 AM in China/Shanghai time in 2022, the format is `0 15 10 ? * * 2022 Asia/Shanghai`. To execute every half hour from 10:00 AM to 11:30 AM every day in the East 8th time zone in 2022, the format is `0 0/30 10-11 * * ? 2022 GMT+8:00`. To execute every 5 minutes from 2:00 PM to 2:55 PM every day in October every two years starting from 2022 in UTC, the format is `0 0/5 14 * 10 ? 2022/2 UTC`.
        # 
        #     >The minimum time interval must be greater than or equal to the timeout period specified when the scheduled task was created, and must not be less than 10 seconds.
        self.frequency = frequency
        # The instance ID of the ECS instance or managed instance to add to the task.
        self.instance_id = instance_id
        # The command execution ID of the task to modify.
        # 
        # This parameter is required.
        self.invoke_id = invoke_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The key-value pairs of custom parameters to modify when the command contains custom parameters.
        # 
        # The number of custom parameters ranges from 0 to 10. Note the following items:
        # 
        # - Keys cannot be empty strings and can contain up to 64 characters.
        # - Values can be empty strings.
        # - After the custom parameters and original command content are Base64-encoded, the total size of the command content cannot exceed 24 KB.
        # - The set of custom parameter names must be a subset of the parameter set defined when the command was created. For parameters that are not passed in, you can use empty strings as substitutes.
        # 
        # Default value: empty, which indicates that no custom parameter key-value pairs are modified.
        self.parameters_shrink = parameters_shrink
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

        if self.parameters_shrink is not None:
            result['Parameters'] = self.parameters_shrink

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
            self.parameters_shrink = m.get('Parameters')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

