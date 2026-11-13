# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from darabonba.model import DaraModel

class RunCommandRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        command_content: str = None,
        command_id: str = None,
        content_encoding: str = None,
        description: str = None,
        enable_parameter: bool = None,
        frequency: str = None,
        launcher: str = None,
        name: str = None,
        node_id_list: List[str] = None,
        parameters: Dict[str, Any] = None,
        repeat_mode: str = None,
        termination_mode: str = None,
        timeout: int = None,
        username: str = None,
        working_dir: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The client token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see How to ensure idempotence.
        self.client_token = client_token
        # The content of the command. Specify either this parameter or CommandId. The command content can be plaintext or Base64-encoded. Take note of the following items:
        # 
        # - Specify EnableParameter=true to enable the custom parameter feature in the command content.
        # - Define custom parameters by enclosing them in braces ({{}}). Spaces and line breaks before and after the parameter names inside {{}} are ignored.
        # - You can specify a maximum of 20 custom parameters.
        # - A custom parameter name can contain only letters, digits, hyphens (-), and underscores (_). Parameter names are not case-sensitive.
        # - A custom parameter name cannot exceed 64 bytes in length.
        self.command_content = command_content
        # The command ID.
        self.command_id = command_id
        # The encoding method of the script content. Valid values:
        # 
        # - PlainText: The content is not encoded and is transmitted in plaintext.
        # - Base64: The content is Base64-encoded.
        # 
        # Default value: PlainText. If an invalid value is specified, the value is processed as PlainText.
        self.content_encoding = content_encoding
        # The description of the command.
        self.description = description
        # Specifies whether the command contains custom parameters.
        # 
        # Default value: false.
        self.enable_parameter = enable_parameter
        # The scheduled execution time of the command. Three scheduled execution methods are supported: execution at fixed time intervals (based on rate expressions), one-time execution at a specified time, and clock-based scheduled execution (based on cron expressions).
        # 
        # - Execution at fixed time intervals: Based on rate expressions, the command is executed at the specified time interval. The time interval can be specified in seconds (s), minutes (m), hours (h), or days (d). This method is suitable for scenarios where tasks are executed at fixed time intervals. The format is rate(<interval value><interval unit>). For example, to execute the command every 5 minutes, use rate(5m). Limits on execution at fixed time intervals: 
        #     - The specified time interval must not exceed 7 days, must not be less than 60 seconds, and must be greater than the timeout period of the scheduled task. 
        #     - The execution interval is based only on the fixed frequency and is independent of the actual time required to execute the task. For example, if the command is executed every 5 minutes and the task takes 2 minutes to complete, the next execution starts 3 minutes after the task is completed. 
        #     - The task is not executed immediately upon creation. For example, if the command is executed every 5 minutes, it is not executed immediately when the task is created. Instead, the first execution starts 5 minutes after the task is created.
        #  
        # - One-time execution at a specified time: The command is executed once at the specified time in the specified time zone. The format is at(yyyy-MM-dd HH:mm:ss <time zone>). If no time zone is specified, the UTC time zone is used by default. The time zone can be specified in the following three formats: 
        #     - Full name of the time zone: such as Asia/Shanghai and America/Los_Angeles. 
        #     - Offset of the time zone relative to Greenwich Mean Time (GMT): such as GMT+8:00 and GMT-7:00. When the GMT format is used, leading zeros are not supported for the hour. 
        #     - Time zone abbreviation: Only UTC is supported.
        # If you want to execute the command once at 13:15:30 on June 6, 2022 in the Asia/Shanghai time zone, use at(2022-06-06 13:15:30 Asia/Shanghai). If you want to execute the command once at 13:15:30 on June 6, 2022 in the GMT-7:00 time zone, use at(2022-06-06 13:15:30 GMT-7:00).
        # 
        # - Clock-based scheduled execution (based on cron expressions): Based on cron expressions, the command is executed according to the scheduled task. The format is <seconds> <minutes> <hours> <day of month> <month> <day of week> <year (optional)> <time zone>, which is <cron expression> <time zone>. The scheduled task execution time is calculated and executed based on the cron expression in the specified time zone. If no time zone is specified, the internal system time zone of the instance where the scheduled task is executed is used by default. For more information about cron expressions, see Cron expressions. The time zone can be specified in the following three formats: 
        #     - Full name of the time zone: such as Asia/Shanghai and America/Los_Angeles. 
        #     - Offset of the time zone relative to GMT: such as GMT+8:00 and GMT-7:00. When the GMT format is used, leading zeros are not supported for the hour. 
        #     - Time zone abbreviation: Only UTC is supported.
        # 
        #     For example, to execute the command once at 10:15 every day in 2022 in the Asia/Shanghai time zone, use 0 15 10 ? * * 2022 Asia/Shanghai. To execute the command every half hour from 10:00 to 11:30 every day in 2022 in the GMT+8:00 time zone, use 0 0/30 10-11 * * ? 2022 GMT+8:00. To execute the command every 5 minutes from 14:00 to 14:55 every day in October every two years starting from 2022 in the UTC time zone, use 0 0/5 14 * 10 ? 2022/2 UTC.
        self.frequency = frequency
        # The launcher for script execution. The size cannot exceed 1 KB.
        self.launcher = launcher
        # The name of the command.
        self.name = name
        # The list of nodes.
        self.node_id_list = node_id_list
        # The key-value pairs of custom parameters that are passed when the command is executed, if the command contains custom parameters. For example, if the command content is `echo {{name}}`, you can pass the key-value pair `{"name":"Jack"}` by using the Parameters parameter. The custom parameter automatically replaces the variable value `name`, resulting in a new command. The actual command executed is `echo Jack`.
        # 
        # The number of custom parameters ranges from 0 to 10. Take note of the following items:
        # 
        # - The key cannot be an empty string and can contain a maximum of 64 characters.
        # - The value can be an empty string.
        # - After the custom parameters and the original command content are Base64-encoded, if the command is saved, the size of the Base64-encoded command content cannot exceed 18 KB. If the command is not saved, the size of the Base64-encoded command content cannot exceed 24 KB. You can use KeepCommand to specify whether to retain the command.
        # - The set of custom parameter names specified must be a subset of the parameter set defined when the command is created. For parameters that are not passed, you can use an empty string instead.
        # 
        # Default value: empty. An empty value indicates that this parameter is not specified and the custom parameter feature is disabled.
        self.parameters = parameters
        # The execution mode of the command. Valid values:
        # 
        # - Once: Executes the command immediately.
        # - Period: Executes the command on a schedule. If this parameter is set to Period, you must also specify the Frequency parameter.
        # - NextRebootOnly: Automatically executes the command the next time the instance starts.
        # - EveryReboot: Automatically executes the command every time the instance starts.
        # 
        # Default values:
        # - If the Frequency parameter is not specified, the default value is Once.
        # - If the Frequency parameter is specified, the value is processed as Period regardless of whether this parameter is set.
        self.repeat_mode = repeat_mode
        # The mode used when a task is stopped, either manually or due to an execution timeout. Valid values:
        # 
        # - Process: Stops the current script process.
        # - ProcessTree: Stops the current process tree, which includes the script process and all child processes created by it.
        self.termination_mode = termination_mode
        # The timeout period for command execution, in seconds. If the command cannot be executed due to process issues, missing modules, or a missing Cloud Assistant Agent, a timeout occurs. After a timeout, the command process is forcibly terminated. Default value: 60.
        self.timeout = timeout
        # The name of the user that executes the command on the instance. The name cannot exceed 255 characters in length.
        # For Linux instances, the command is executed by the root user by default.
        self.username = username
        # The custom execution path of the command. Default paths:
        # 
        # Linux instances: The default execution path is the home directory of the root user.
        self.working_dir = working_dir

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

        if self.command_id is not None:
            result['CommandId'] = self.command_id

        if self.content_encoding is not None:
            result['ContentEncoding'] = self.content_encoding

        if self.description is not None:
            result['Description'] = self.description

        if self.enable_parameter is not None:
            result['EnableParameter'] = self.enable_parameter

        if self.frequency is not None:
            result['Frequency'] = self.frequency

        if self.launcher is not None:
            result['Launcher'] = self.launcher

        if self.name is not None:
            result['Name'] = self.name

        if self.node_id_list is not None:
            result['NodeIdList'] = self.node_id_list

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        if self.repeat_mode is not None:
            result['RepeatMode'] = self.repeat_mode

        if self.termination_mode is not None:
            result['TerminationMode'] = self.termination_mode

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        if self.username is not None:
            result['Username'] = self.username

        if self.working_dir is not None:
            result['WorkingDir'] = self.working_dir

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('CommandContent') is not None:
            self.command_content = m.get('CommandContent')

        if m.get('CommandId') is not None:
            self.command_id = m.get('CommandId')

        if m.get('ContentEncoding') is not None:
            self.content_encoding = m.get('ContentEncoding')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnableParameter') is not None:
            self.enable_parameter = m.get('EnableParameter')

        if m.get('Frequency') is not None:
            self.frequency = m.get('Frequency')

        if m.get('Launcher') is not None:
            self.launcher = m.get('Launcher')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NodeIdList') is not None:
            self.node_id_list = m.get('NodeIdList')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        if m.get('RepeatMode') is not None:
            self.repeat_mode = m.get('RepeatMode')

        if m.get('TerminationMode') is not None:
            self.termination_mode = m.get('TerminationMode')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        if m.get('WorkingDir') is not None:
            self.working_dir = m.get('WorkingDir')

        return self

