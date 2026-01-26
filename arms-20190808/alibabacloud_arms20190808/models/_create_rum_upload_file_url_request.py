# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateRumUploadFileUrlRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        content_type: str = None,
        file_name: str = None,
        pid: str = None,
        region_id: str = None,
        service_id: str = None,
        sourcemap_type: str = None,
        uuid: str = None,
        version_id: str = None,
        workspace: str = None,
    ):
        # The application name.
        self.app_name = app_name
        # The type of the file. You can set this parameter to "application/zip", "text/plain", or an empty string.
        self.content_type = content_type
        # The file name.
        # 
        # This parameter is required.
        self.file_name = file_name
        # The process ID (PID) of the application.
        self.pid = pid
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.service_id = service_id
        # The file type. Valid values: source-map: SourceMap files. mapping: symbol table files for Android. dsym: dSYM files for iOS.
        self.sourcemap_type = sourcemap_type
        # The file ID.
        self.uuid = uuid
        # The version number of the file.
        self.version_id = version_id
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.content_type is not None:
            result['ContentType'] = self.content_type

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.pid is not None:
            result['Pid'] = self.pid

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.sourcemap_type is not None:
            result['SourcemapType'] = self.sourcemap_type

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        if self.version_id is not None:
            result['VersionId'] = self.version_id

        if self.workspace is not None:
            result['Workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('Pid') is not None:
            self.pid = m.get('Pid')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('SourcemapType') is not None:
            self.sourcemap_type = m.get('SourcemapType')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')

        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')

        return self

