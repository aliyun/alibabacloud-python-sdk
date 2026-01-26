# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateRumFileStatusRequest(DaraModel):
    def __init__(
        self,
        file_name: str = None,
        pid: str = None,
        region_id: str = None,
        size: str = None,
        status: str = None,
        uuid: str = None,
        version_id: str = None,
    ):
        # The file name.
        self.file_name = file_name
        # The application ID.
        self.pid = pid
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The size of the file. Unit: bytes.
        self.size = size
        # The status of the file. Valid values: SUCCESS and INIT.
        self.status = status
        # The unique ID of the file. If you do not set this parameter, the system automatically sets a UUID for you.
        self.uuid = uuid
        # The version number of the file.
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.pid is not None:
            result['Pid'] = self.pid

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.size is not None:
            result['Size'] = self.size

        if self.status is not None:
            result['Status'] = self.status

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        if self.version_id is not None:
            result['VersionId'] = self.version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('Pid') is not None:
            self.pid = m.get('Pid')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')

        return self

