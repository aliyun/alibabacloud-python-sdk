# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UploadRequest(DaraModel):
    def __init__(
        self,
        edition: str = None,
        file: str = None,
        file_name: str = None,
        pid: str = None,
        region_id: str = None,
        version: str = None,
    ):
        # The version of the SourceMap file.
        self.edition = edition
        # The string of the SourceMap file.
        self.file = file
        # The name of the SourceMap file.
        # 
        # This parameter is required.
        self.file_name = file_name
        # The application ID.
        # 
        # Log on to the **ARMS console**. In the left-side navigation pane, choose **Browser Monitoring** > **Browser Monitoring**. On the Browser Monitoring page, click the name of an application. The URL in the address bar contains the process ID (PID) of the application. The PID is indicated in the pid=xxx format. The PID is usually percent encoded as xxx%40xxx. You must modify this value to remove the percent encoding. For example, if the PID in the URL is eb4zdose6v%409781be0f44d\\*\\*\\*\\*, you must replace %40 with @ to obtain eb4zdose6v@9781be0f44d\\*\\*\\*\\*.
        # 
        # This parameter is required.
        self.pid = pid
        # The ID of the region to which the SourceMap file is uploaded.
        # 
        # This parameter is required.
        self.region_id = region_id
        # We recommend that you do not specify this parameter.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.edition is not None:
            result['Edition'] = self.edition

        if self.file is not None:
            result['File'] = self.file

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.pid is not None:
            result['Pid'] = self.pid

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Edition') is not None:
            self.edition = m.get('Edition')

        if m.get('File') is not None:
            self.file = m.get('File')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('Pid') is not None:
            self.pid = m.get('Pid')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

