# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitSymbolicRequest(DaraModel):
    def __init__(
        self,
        app_key: int = None,
        app_version: str = None,
        build_id: str = None,
        file_name: str = None,
        file_path: str = None,
        file_type: str = None,
        os: str = None,
        uuid: str = None,
    ):
        # appKey
        # 
        # This parameter is required.
        self.app_key = app_key
        self.app_version = app_version
        self.build_id = build_id
        # This parameter is required.
        self.file_name = file_name
        # This parameter is required.
        self.file_path = file_path
        # This parameter is required.
        self.file_type = file_type
        # This parameter is required.
        self.os = os
        # uuid
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_key is not None:
            result['AppKey'] = self.app_key

        if self.app_version is not None:
            result['AppVersion'] = self.app_version

        if self.build_id is not None:
            result['BuildId'] = self.build_id

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.file_path is not None:
            result['FilePath'] = self.file_path

        if self.file_type is not None:
            result['FileType'] = self.file_type

        if self.os is not None:
            result['Os'] = self.os

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')

        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')

        if m.get('BuildId') is not None:
            self.build_id = m.get('BuildId')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')

        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')

        if m.get('Os') is not None:
            self.os = m.get('Os')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

