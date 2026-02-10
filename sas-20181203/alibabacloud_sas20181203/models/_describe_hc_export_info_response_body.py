# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeHcExportInfoResponseBody(DaraModel):
    def __init__(
        self,
        current_count: int = None,
        file_name: str = None,
        gmt_create: int = None,
        id: int = None,
        link: str = None,
        progress: int = None,
        request_id: str = None,
        result_status: str = None,
        total_count: int = None,
    ):
        # The number of exported entries.
        self.current_count = current_count
        # The name of the exported file.
        self.file_name = file_name
        # The time when the export task was created.
        self.gmt_create = gmt_create
        # The ID of the export task.
        self.id = id
        # The download URL for the exported file.
        self.link = link
        # The progress percentage of the export task.
        self.progress = progress
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The status of the export task. Valid values:
        # 
        # *   **exporting**: The task is in progress.
        # *   **success**: The task is complete.
        self.result_status = result_status
        # The total number of exported entries.
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

        if self.result_status is not None:
            result['ResultStatus'] = self.result_status

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentCount') is not None:
            self.current_count = m.get('CurrentCount')

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

        if m.get('ResultStatus') is not None:
            self.result_status = m.get('ResultStatus')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

