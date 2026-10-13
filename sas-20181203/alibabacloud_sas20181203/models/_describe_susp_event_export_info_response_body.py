# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSuspEventExportInfoResponseBody(DaraModel):
    def __init__(
        self,
        export_status: str = None,
        file_name: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        id: int = None,
        link: str = None,
        progress: int = None,
        properties: str = None,
        request_id: str = None,
        total_count: int = None,
        type: str = None,
    ):
        # The processing status of anomalous events. Valid values:
        # - **exporting**: Processing.
        # - **success**: Succeeded.
        # - **failed**: Failed.
        # - **pending**: Pending.
        self.export_status = export_status
        # The name of the exported file.
        self.file_name = file_name
        # The creation time.
        self.gmt_create = gmt_create
        # The modification time.
        self.gmt_modified = gmt_modified
        # The ID of the export task for anomalous events.
        self.id = id
        # The download URL of the exported Excel file.
        self.link = link
        # The export progress of anomalous events, in percentage.
        self.progress = progress
        # The export parameters for anomalous events.
        self.properties = properties
        # The ID of the request.
        self.request_id = request_id
        # The total number of anomalous events.
        self.total_count = total_count
        # The type of the export task. The value is fixed to suspiciousEvent.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.export_status is not None:
            result['ExportStatus'] = self.export_status

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.link is not None:
            result['Link'] = self.link

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.properties is not None:
            result['Properties'] = self.properties

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExportStatus') is not None:
            self.export_status = m.get('ExportStatus')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Link') is not None:
            self.link = m.get('Link')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('Properties') is not None:
            self.properties = m.get('Properties')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

