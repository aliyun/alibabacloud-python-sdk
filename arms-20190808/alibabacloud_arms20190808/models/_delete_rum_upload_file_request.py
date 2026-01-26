# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteRumUploadFileRequest(DaraModel):
    def __init__(
        self,
        batch_items: str = None,
        file_name: str = None,
        pid: str = None,
        region_id: str = None,
        service_id: str = None,
        uuid: str = None,
        version_id: str = None,
        workspace: str = None,
    ):
        # Information of files to be deleted in JSON array format. If a single file needs to be deleted, this field should be left empty. If multiple files need to be deleted, just fill in this field.
        self.batch_items = batch_items
        # The file name, with the extension.
        self.file_name = file_name
        # The application ID.
        self.pid = pid
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.service_id = service_id
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
        if self.batch_items is not None:
            result['BatchItems'] = self.batch_items

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.pid is not None:
            result['Pid'] = self.pid

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        if self.version_id is not None:
            result['VersionId'] = self.version_id

        if self.workspace is not None:
            result['Workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchItems') is not None:
            self.batch_items = m.get('BatchItems')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('Pid') is not None:
            self.pid = m.get('Pid')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')

        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')

        return self

