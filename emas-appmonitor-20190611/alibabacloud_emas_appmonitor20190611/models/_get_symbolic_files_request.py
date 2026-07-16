# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetSymbolicFilesRequest(DaraModel):
    def __init__(
        self,
        app_key: int = None,
        app_version: str = None,
        build_id: str = None,
        end_time: int = None,
        export_status: str = None,
        file_name: str = None,
        file_type: str = None,
        os: str = None,
        page_index: int = None,
        page_size: int = None,
        start_time: int = None,
        uuid: str = None,
    ):
        # appKey
        # 
        # This parameter is required.
        self.app_key = app_key
        self.app_version = app_version
        self.build_id = build_id
        self.end_time = end_time
        self.export_status = export_status
        self.file_name = file_name
        # This parameter is required.
        self.file_type = file_type
        # This parameter is required.
        self.os = os
        # This parameter is required.
        self.page_index = page_index
        # This parameter is required.
        self.page_size = page_size
        self.start_time = start_time
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

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.export_status is not None:
            result['ExportStatus'] = self.export_status

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.file_type is not None:
            result['FileType'] = self.file_type

        if self.os is not None:
            result['Os'] = self.os

        if self.page_index is not None:
            result['PageIndex'] = self.page_index

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.start_time is not None:
            result['StartTime'] = self.start_time

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

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('ExportStatus') is not None:
            self.export_status = m.get('ExportStatus')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')

        if m.get('Os') is not None:
            self.os = m.get('Os')

        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

