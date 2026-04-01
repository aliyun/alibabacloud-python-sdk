# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ValidateImportTaskRequest(DaraModel):
    def __init__(
        self,
        db_instance_id: str = None,
        estimated_size: int = None,
        host: str = None,
        owner_id: int = None,
        password: str = None,
        port: int = None,
        region_id: str = None,
        source_instance_id: str = None,
        source_platform: str = None,
        stream_port: int = None,
        user: str = None,
        xtrabackup_path: str = None,
    ):
        # This parameter is required.
        self.db_instance_id = db_instance_id
        self.estimated_size = estimated_size
        # This parameter is required.
        self.host = host
        self.owner_id = owner_id
        # This parameter is required.
        self.password = password
        # This parameter is required.
        self.port = port
        # This parameter is required.
        self.region_id = region_id
        self.source_instance_id = source_instance_id
        self.source_platform = source_platform
        # This parameter is required.
        self.stream_port = stream_port
        # This parameter is required.
        self.user = user
        self.xtrabackup_path = xtrabackup_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_instance_id is not None:
            result['DbInstanceId'] = self.db_instance_id

        if self.estimated_size is not None:
            result['EstimatedSize'] = self.estimated_size

        if self.host is not None:
            result['Host'] = self.host

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.password is not None:
            result['Password'] = self.password

        if self.port is not None:
            result['Port'] = self.port

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.source_instance_id is not None:
            result['SourceInstanceId'] = self.source_instance_id

        if self.source_platform is not None:
            result['SourcePlatform'] = self.source_platform

        if self.stream_port is not None:
            result['StreamPort'] = self.stream_port

        if self.user is not None:
            result['User'] = self.user

        if self.xtrabackup_path is not None:
            result['XtrabackupPath'] = self.xtrabackup_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbInstanceId') is not None:
            self.db_instance_id = m.get('DbInstanceId')

        if m.get('EstimatedSize') is not None:
            self.estimated_size = m.get('EstimatedSize')

        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SourceInstanceId') is not None:
            self.source_instance_id = m.get('SourceInstanceId')

        if m.get('SourcePlatform') is not None:
            self.source_platform = m.get('SourcePlatform')

        if m.get('StreamPort') is not None:
            self.stream_port = m.get('StreamPort')

        if m.get('User') is not None:
            self.user = m.get('User')

        if m.get('XtrabackupPath') is not None:
            self.xtrabackup_path = m.get('XtrabackupPath')

        return self

