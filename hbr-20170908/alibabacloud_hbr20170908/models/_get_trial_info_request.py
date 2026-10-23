# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTrialInfoRequest(DaraModel):
    def __init__(
        self,
        bucket: str = None,
        create_time: int = None,
        file_system_id: str = None,
        source_type: str = None,
    ):
        # This parameter is required only when **SourceType** is set to **OSS**. The name of the OSS bucket.
        self.bucket = bucket
        # This parameter is required only when **SourceType** is set to **NAS**. The time when the file system was created. UNIX timestamp, in seconds.
        self.create_time = create_time
        # This parameter is required only when **SourceType** is set to **NAS**. The ID of the file system.
        self.file_system_id = file_system_id
        # The data source type. Only free trial information of OSS backup and NAS backup can be queried.
        # 
        # This parameter is required.
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket is not None:
            result['Bucket'] = self.bucket

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        return self

