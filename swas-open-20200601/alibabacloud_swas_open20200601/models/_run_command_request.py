# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class RunCommandRequest(DaraModel):
    def __init__(
        self,
        command_content: str = None,
        enable_parameter: bool = None,
        instance_id: str = None,
        name: str = None,
        parameters: Dict[str, Any] = None,
        region_id: str = None,
        timeout: int = None,
        type: str = None,
        windows_password_name: str = None,
        working_dir: str = None,
        working_user: str = None,
    ):
        # The command content. Note the following items:
        # 
        # - Set `EnableParameter=true` to enable the custom parameter feature in the command content:
        # - Define custom parameters by enclosing them in `{{}}`. Spaces and line breaks before and after the parameter name within `{{}}` are ignored.
        # - The number of custom parameters cannot exceed 20.
        # - Custom parameter names can contain only letters (a-z, A-Z), digits (0-9), hyphens (-), and underscores (_). Other characters are not supported. Parameter names are case-insensitive.
        # - A single custom parameter name cannot exceed 64 bytes.
        # 
        # This parameter is required.
        self.command_content = command_content
        # Specifies whether the command contains custom parameters.
        # 
        # Default value: false.
        self.enable_parameter = enable_parameter
        # The instance ID of the simple application server.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The name of the command execution.
        # 
        # This parameter is required.
        self.name = name
        # The key-value pairs of custom parameters to pass in when the command contains custom parameters. For example, if the command content is `echo {{name}}`, you can use the `Parameters` parameter to pass in the key-value pair `{"name":"Jack"}`. The custom parameter automatically replaces the variable value `name`, and the actual command that runs is `echo Jack`.
        # 
        # The number of custom parameters ranges from 0 to 20. Note the following items:
        # 
        # - Keys cannot be empty strings and can contain up to 64 characters.
        # - Values can be empty strings.
        # - The set of custom parameter names must be a subset of the parameter set defined when the command was created. For parameters that are not passed in, you can use empty strings as substitutes.
        # 
        # Default value: empty, which indicates that this parameter is unset to disable custom parameters.
        self.parameters = parameters
        # The region ID. You can call [ListRegions](https://help.aliyun.com/document_detail/189315.html) to query the latest region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The timeout period for the command to run on the server instance. Unit: seconds.
        # 
        # When a command execution task times out, Command Assistant forcefully terminates the task process. Valid values: 10 to 86400 (24 hours).
        # 
        # Default value: 60.
        self.timeout = timeout
        # The language type of the command. Valid values:
        # 
        # - RunBatScript: Bat commands for Windows instances.
        # - RunPowerShellScript: PowerShell commands for Windows instances.
        # - RunShellScript: Shell commands for Linux instances.
        # 
        # This parameter is required.
        self.type = type
        # The password name of the user that runs the command on a Windows instance.
        # 
        # If you want to run a command as a non-default user (System) on a Windows instance, you must specify both WorkingUser and this parameter. To reduce the risk of password leaks, store the plaintext password in the parameter repository of CloudOps Orchestration Service and pass in only the password name here.
        self.windows_password_name = windows_password_name
        # The custom execution path of the command. Default paths:
        # 
        # - Linux instances: The default execution path is the /root directory of the root user.
        # - Windows instances: The default execution path is the C:\\Windows\\system32 directory.
        self.working_dir = working_dir
        # The user that you want to use to run the command on the simple application server instance. We recommend that you use a regular user to run commands to reduce security risks.
        # Default values:
        # 
        # - root: On Linux instances, commands are run as the root user by default.
        # 
        # - system: On Windows instances, commands are run as the system user by default.
        self.working_user = working_user

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.command_content is not None:
            result['CommandContent'] = self.command_content

        if self.enable_parameter is not None:
            result['EnableParameter'] = self.enable_parameter

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.name is not None:
            result['Name'] = self.name

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        if self.type is not None:
            result['Type'] = self.type

        if self.windows_password_name is not None:
            result['WindowsPasswordName'] = self.windows_password_name

        if self.working_dir is not None:
            result['WorkingDir'] = self.working_dir

        if self.working_user is not None:
            result['WorkingUser'] = self.working_user

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommandContent') is not None:
            self.command_content = m.get('CommandContent')

        if m.get('EnableParameter') is not None:
            self.enable_parameter = m.get('EnableParameter')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('WindowsPasswordName') is not None:
            self.windows_password_name = m.get('WindowsPasswordName')

        if m.get('WorkingDir') is not None:
            self.working_dir = m.get('WorkingDir')

        if m.get('WorkingUser') is not None:
            self.working_user = m.get('WorkingUser')

        return self

