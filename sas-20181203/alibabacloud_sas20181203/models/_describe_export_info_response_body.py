# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeExportInfoResponseBody(DaraModel):
    def __init__(
        self,
        current_count: int = None,
        export_status: str = None,
        file_name: str = None,
        id: int = None,
        link: str = None,
        message: str = None,
        progress: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The number of exported entries.
        self.current_count = current_count
        # The status of the export task.
        # 
        # Valid values:
        # 
        # *   **init**: The task is being initialized.
        # *   **exporting**: The task is in progress.
        # *   **success**: The task is complete.
        self.export_status = export_status
        # The name of the exported Excel file.
        self.file_name = file_name
        # The ID of the export task.
        self.id = id
        # The URL at which you can download the exported Excel file.
        self.link = link
        # The message that shows the task result. The value is fixed as **success**, which indicates that the task is complete.
        self.message = message
        # The progress percentage of the export task.
        self.progress = progress
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The total number of entries in the exported Excel file.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_count is not None:
            result['CurrentCount'] = self.current_count

        if self.export_status is not None:
            result['ExportStatus'] = self.export_status

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.id is not None:
            result['Id'] = self.id

        if self.link is not None:
            result['Link'] = self.link

        if self.message is not None:
            result['Message'] = self.message

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentCount') is not None:
            self.current_count = m.get('CurrentCount')

        if m.get('ExportStatus') is not None:
            self.export_status = m.get('ExportStatus')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Link') is not None:
            self.link = m.get('Link')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

