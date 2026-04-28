# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class FileDownloadCallbackInfo(DaraModel):
    def __init__(
        self,
        bucket: str = None,
        domain_id: str = None,
        drive_id: str = None,
        file_id: str = None,
        object: str = None,
        user_id: str = None,
    ):
        # This parameter is required.
        self.bucket = bucket
        # This parameter is required.
        self.domain_id = domain_id
        # This parameter is required.
        self.drive_id = drive_id
        # This parameter is required.
        self.file_id = file_id
        # This parameter is required.
        self.object = object
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket is not None:
            result['bucket'] = self.bucket

        if self.domain_id is not None:
            result['domain_id'] = self.domain_id

        if self.drive_id is not None:
            result['drive_id'] = self.drive_id

        if self.file_id is not None:
            result['file_id'] = self.file_id

        if self.object is not None:
            result['object'] = self.object

        if self.user_id is not None:
            result['user_id'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bucket') is not None:
            self.bucket = m.get('bucket')

        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')

        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')

        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')

        if m.get('object') is not None:
            self.object = m.get('object')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        return self

