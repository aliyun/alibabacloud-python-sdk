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
        # The content of the command. The command content can be plaintext or Base64-encoded.\\
        # The Base64-encoded command content cannot exceed 16 KB in size.
        # 
        # > If the command content is Base64-encoded, you must set the ContentEncoding parameter to Base64.
        # 
        # This parameter is required.
        self.command_content = command_content
        self.command_role = command_role
        # The encoding mode of the command content. Valid values:
        # 
        # *   PlainText: The command content is not encoded.
        # *   Base64: The command content is Base64-encoded.
        # 
        # Default value: PlainText. If the specified value of this parameter is invalid, PlainText is used by default.
        self.content_encoding = content_encoding
        # The ID of cloud desktop N. Valid values of N: 1 to 50.\\
        # If multiple cloud desktops are specified and the command execution succeeds on at least one of the cloud desktops, the operation is considered successful. If multiple cloud desktops are specified and the command execution fails on all the cloud desktops, verify the value of the parameter and try again.
        # 
        # This parameter is required.
        self.desktop_id = desktop_id
        # The ID of the end user. If you specify a value, you run the command as the end user that is granted specific permissions. Note: The end user has sessions on a cloud computer. That is, when the cloud computer is started, the end user logs on to an Alibaba Cloud Workspace client and connects to the cloud computer, and the cloud computer is not preempted by another end user during the connection. This parameter is not available for Linux cloud computers.
        self.end_user_id = end_user_id
        # The ID of the region.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The timeout period for the command to run. Unit: seconds. Default value: 60.\\
        # A timeout error occurs if the command cannot be run because the process slows down or because a specific module or the Cloud Assistant client does not exist. When a timeout error occurs, the command process is forcibly terminated.
        self.timeout = timeout
        # The language of the O\\&M command. Valid values:
        # 
        # *   RunBatScript
        # *   RunPowerShellScript
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

