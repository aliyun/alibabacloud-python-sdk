# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class RunCommandRequest(DaraModel):
    def __init__(
        self,
        command_content: str = None,
        command_role: str = None,
        content_encoding: str = None,
        desktop_id: List[str] = None,
        end_user_id: str = None,
        region_id: str = None,
        timeout: int = None,
        type: str = None,
    ):
        # The plaintext or Base64-encoded content of the script.  
        # The Base64-encoded script content cannot exceed 16 KB.
        # 
        # > If the script content is Base64-encoded, set the ContentEncoding parameter to Base64.
        # 
        # This parameter is required.
        self.command_content = command_content
        # The role used when the command is executed on the cloud computer.
        self.command_role = command_role
        # The encoding method of the script content.
        # 
        # > If the specified value is not within the valid values, the value is treated as `PlainText`.
        self.content_encoding = content_encoding
        # The list of cloud computer IDs. Valid values of N: 1 to 50.  
        # If multiple cloud computers are specified, the API call succeeds as long as the script is successfully executed on at least one cloud computer. If the script fails to execute on all specified cloud computers, reset this parameter.
        # 
        # This parameter is required.
        self.desktop_id = desktop_id
        # The ID of the end user. If this parameter is specified, the command is executed with the permissions of the end user.
        # 
        # > The user must have a session record on the cloud computer (the user has logged on and connected to the cloud computer after it was started, and the session was not preempted by another user). This parameter is not supported for Linux cloud computers.
        self.end_user_id = end_user_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The timeout period for executing the script. Unit: seconds. Default value: 300.  
        # A timeout may occur when the script cannot run because of process issues, missing modules, or a missing Cloud Assistant client. After a timeout, the script process is forcefully terminated.
        self.timeout = timeout
        # The language type of the O&M script.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.command_content is not None:
            result['CommandContent'] = self.command_content

        if self.command_role is not None:
            result['CommandRole'] = self.command_role

        if self.content_encoding is not None:
            result['ContentEncoding'] = self.content_encoding

        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommandContent') is not None:
            self.command_content = m.get('CommandContent')

        if m.get('CommandRole') is not None:
            self.command_role = m.get('CommandRole')

        if m.get('ContentEncoding') is not None:
            self.content_encoding = m.get('ContentEncoding')

        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

