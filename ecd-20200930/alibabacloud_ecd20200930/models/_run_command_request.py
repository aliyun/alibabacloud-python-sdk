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
        # The script content in plaintext or Base64-encoded format.<br>
        # The Base64-encoded script content cannot exceed 16 KB.<br>
        # 
        # > If the script content is Base64-encoded, you must set the `ContentEncoding` parameter to `Base64`.
        # 
        # This parameter is required.
        self.command_content = command_content
        self.command_role = command_role
        # The encoding mode of the script content.
        # 
        # > If you specify a value that is not a valid enumeration member, the system defaults to `PlainText`.
        self.content_encoding = content_encoding
        # The IDs of the cloud computers on which to run the script. You can specify up to 50 IDs.<br>
        # The API call is considered successful if the script runs on at least one of the specified cloud computers. The call fails only if the script fails on all of them.<br>
        # 
        # This parameter is required.
        self.desktop_id = desktop_id
        # If you specify this parameter, the command runs with the permissions of the specified end user.
        # 
        # > This user must have a session history on the cloud computer. This means the user must have logged in after the cloud computer started and their session was not taken over by another user. This parameter is not supported for Linux cloud computers.
        self.end_user_id = end_user_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The script execution timeout, in seconds. Default value: 300.<br>
        # A command times out if the script cannot be run due to issues such as process conflicts, missing modules, or an unavailable Cloud Assistant client. When a command times out, the system forcibly terminates the script process.<br>
        self.timeout = timeout
        # The type of the script.
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

