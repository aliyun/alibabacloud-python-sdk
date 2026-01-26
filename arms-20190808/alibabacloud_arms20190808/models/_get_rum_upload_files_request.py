# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetRumUploadFilesRequest(DaraModel):
    def __init__(
        self,
        app_type: str = None,
        file_name: str = None,
        next_token: str = None,
        page_size: int = None,
        pid: str = None,
        region_id: str = None,
        service_id: str = None,
        version_id: str = None,
        workspace: str = None,
    ):
        # The file type. Valid values: source-map: SourceMap files. mapping: symbol table files for Android. dsym: dSYM files for iOS.
        self.app_type = app_type
        self.file_name = file_name
        self.next_token = next_token
        self.page_size = page_size
        # The process ID (PID) of the application.
        self.pid = pid
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.service_id = service_id
        # The version number of the files. If you do not specify this parameter, all versions of the files are returned by default.
        self.version_id = version_id
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_type is not None:
            result['AppType'] = self.app_type

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.pid is not None:
            result['Pid'] = self.pid

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.version_id is not None:
            result['VersionId'] = self.version_id

        if self.workspace is not None:
            result['Workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Pid') is not None:
            self.pid = m.get('Pid')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')

        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')

        return self

