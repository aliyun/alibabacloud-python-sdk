# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetExportTaskResponseBody(DaraModel):
    def __init__(
        self,
        export_status: str = None,
        export_type: str = None,
        file_name: str = None,
        gmt_create: str = None,
        id: int = None,
        link: str = None,
        progress: int = None,
        request_id: str = None,
    ):
        self.export_status = export_status
        self.export_type = export_type
        self.file_name = file_name
        self.gmt_create = gmt_create
        self.id = id
        self.link = link
        self.progress = progress
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.export_status is not None:
            result['ExportStatus'] = self.export_status

        if self.export_type is not None:
            result['ExportType'] = self.export_type

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.id is not None:
            result['Id'] = self.id

        if self.link is not None:
            result['Link'] = self.link

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExportStatus') is not None:
            self.export_status = m.get('ExportStatus')

        if m.get('ExportType') is not None:
            self.export_type = m.get('ExportType')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Link') is not None:
            self.link = m.get('Link')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

