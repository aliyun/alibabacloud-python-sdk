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
        # The client token to ensure the idempotency of the request. Use your client to generate the token that is unique among requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see "How to ensure idempotence".
        self.client_token = client_token
        # The command content. Take note of the following:
        # 
        # *   When `EnableParameter` is set to true, you can use custom parameters in the command.
        # *   Define custom parameters in the {{}} format. Within `{{}}`, the spaces and line feeds before and after the parameter names are ignored.
        # *   You can specify up to 20 custom parameters.
        # *   A custom parameter name can contain only letters, digits, underscores (_), and hyphens (-). The name is not case-sensitive.
        # *   Each custom parameter name is up to 64 bytes in length.
        self.command_content = command_content
        # The ID of the command.
        self.command_id = command_id
        # The encoding mode of the command content. Valid values:
        # 
        # *   PlainText
        # *   Base64
        # 
        # Default value: PlainText. If the specified value of this parameter is invalid, PlainText is used by default.
        self.content_encoding = content_encoding
        # The command description.
        self.description = description
        # Specifies whether to use custom parameters in the command.
        # 
        # Default value: false.
        self.enable_parameter = enable_parameter
        # The schedule to run the command. Supported schedule types: at a fixed interval based on a rate expression, run only once at a specific time, or run at specific times based on a cron expression.
        # 
        # *   To run the command at a fixed interval, use a rate expression to specify the interval. The interval can be in seconds, minutes, hours, or days. This option is suitable for scenarios in which tasks need to be executed at a fixed interval. Format: rate(\\<Execution interval value> \\<Execution interval unit>). For example, rate(5m) means to run the command every 5 minutes. When you specify an interval, take note of the following limits:
        # 
        #     *   The interval can be anywhere from 60 seconds to 7 days, but must be longer than the timeout period of the scheduled task.
        #     *   The interval is the time between two consecutive executions, irrelevant of the time required to run the command. For example, assume that you set the interval to 5 minutes and that it takes 2 minutes to run the command each time. The system waits 3 minutes before running the command again.
        #     *   The command is not immediately executed after the task is created. For example, assume that you set the interval to 5 minutes. The task begins to be executed 5 minutes after it is created.
        # 
        # *   To run a command only once at a specific point in time, specify a point in time and a time zone. Format: at(yyyy-MM-dd HH:mm:ss \\<Time zone>). If you do not specify a time zone, the Coordinated Universal Time (UTC) time zone is used by default. The time zone name supports the following formats: Full name, such as Asia/Shanghai and America/Los_Angeles. The time offset from GMT. Examples: GMT+8:00 (UTC+8) and GMT-7:00 (UTC-7). If you use the GMT format, you cannot add leading zeros to the hour value. The time zone abbreviation. Only UTC is supported. For example, to configure a command to run only once at 13:15:30 on June 6, 2022 (Shanghai time), set the time to at(2022-06-06 13:15:30 Asia/Shanghai). To configure a command to run only once at 13:15:30 on June 6, 2022 (UTC-7), set the time to at(2022-06-06 13:15:30 GMT-7:00).
        # 
        # *   To run a command at designated points in time, use a cron expression to define the schedule. Format: \\<Cron expression> \\<Time zone>. Example: \\<Seconds> \\<Minutes> \\<Hours> \\<Day of the month> \\<Month> \\<Day of the week> \\<Year (optional)> \\<Time zone>. The system calculates the execution times of the command based on the specified cron expression and time zone and runs the command as scheduled. If you do not specify a time zone, the system time zone of the instance is used by default. For more information, see Cron expressions. The time zone name supports the following formats:
        # 
        #     *   Full name, such as Asia/Shanghai and America/Los_Angeles.
        #     *   The time offset from GMT. Examples: GMT+8:00 (UTC+8) and GMT-7:00 (UTC-7). If you use the GMT format, you cannot add leading zeros to the hour value.
        #     *   The time zone abbreviation. Only UTC is supported.
        # 
        #     For example, if you specify a command to run at 10:15:00 every day in 2022 in China/Shanghai time, set the time to 0 15 10 ? \\* \\* 2022 Asia/Shanghai. To configure a command to run every half an hour from 10:00:00 to 11:30:00 every day in 2022 (UTC+8), set the schedule to 0 0/30 10-11 \\* \\* ? 2022 GMT+8:00. To configure a command to run every 5 minutes from 14:00:00 to 14:55:00 every October every two years from 2022 in UTC, set the schedule to 0 0/5 14 \\* 10 ? 2022/2 UTC.
        self.frequency = frequency
        # The launcher for script execution. Cannot exceed 1 KB.
        self.launcher = launcher
        # The command name.
        self.name = name
        # The node list.
        self.node_id_list = node_id_list
        # The key-value pairs of custom parameters to pass in when the command includes custom parameters. For example, the command content is `echo {{name}}`. You can use `Parameters` to pass in the `{"name":"Jack"}` key-value pair. The `name` key of the custom parameter is automatically replaced by the paired Jack value to generate a new command. As a result, the `echo Jack` command is run.
        # 
        # You can specify 0 to 10 custom parameters. Take note of the following:
        # 
        # *   The key of a custom parameter can be up to 64 characters in length, and cannot be an empty string.
        # *   The value of a custom parameter can be an empty string.
        # *   If you want to retain a command, make sure that the command after Base64 encoding, including custom parameters and original command content, does not exceed 18 KB in size. If you do not want to retain the command, make sure that the command after Base64 encoding does not exceed 24 KB in size. You can set `KeepCommand` to specify whether to retain the command.
        # *   The specified custom parameter names must be included in the custom parameter names that you specify when you create the command. You can use empty strings to represent the parameters that are not passed in.
        # 
        # This parameter is left empty by default, which indicates that the custom parameter feature is disabled.
        self.parameters = parameters
        # The mode to run the command. Valid values:
        # 
        # *   Once: runs the command immediately.
        # *   Period: runs the command based on a schedule. When set to `Period`, `Frequency` is required.
        # *   NextRebootOnly: runs the command the next time the instances is started.
        # *   EveryReboot: runs the command every time the instance is started.
        # 
        # Default value:
        # 
        # *   If you do not specify `Frequency`, the default value is `Once`.
        # *   If you specify `Frequency`, RepeatMode is set to `Period` regardless of whether a value is already specified.
        self.repeat_mode = repeat_mode
        # Indicates how the command task is stopped when a command execution is manually stopped or times out. Valid values:
        # 
        # Process: The process of the command is stopped. ProcessTree: The process tree of the command is stopped. In this case, the process of the command and all subprocesses are stopped.
        self.termination_mode = termination_mode
        # The timeout period for the command. Unit: seconds. A timeout error occurs if the command cannot be run because the process slows down or because a specific module or Cloud Assistant Agent does not exist. When the specified timeout period ends, the command process is forcefully terminated. Default value: 60.
        self.timeout = timeout
        # The username that you use to run the command. The name can be up to 255 characters in length. For Linux instances, the root user is used by default.
        self.username = username
        # The working path of the command. You can specify a custom path. Default path:
        # 
        # Linux instances: By default, the path is in the /home directory of the root user.
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

