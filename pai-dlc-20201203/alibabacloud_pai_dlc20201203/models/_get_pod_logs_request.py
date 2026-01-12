# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetPodLogsRequest(DaraModel):
    def __init__(
        self,
        download_to_file: bool = None,
        end_time: str = None,
        max_lines: int = None,
        pod_uid: str = None,
        start_time: str = None,
    ):
        # Specifies whether to download the log file. Default value: false. Valid values:
        # 
        # *   false
        # *   true
        self.download_to_file = download_to_file
        # The end time of the query. Default value: current time.
        self.end_time = end_time
        # The maximum number of log entries. Default value: 2000.
        self.max_lines = max_lines
        # The node UID. For more information about how to obtain a node UID, see [GetJob](https://help.aliyun.com/document_detail/459677.html).
        self.pod_uid = pod_uid
        # The start time of the query. Default value: 7 days ago.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.download_to_file is not None:
            result['DownloadToFile'] = self.download_to_file

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.max_lines is not None:
            result['MaxLines'] = self.max_lines

        if self.pod_uid is not None:
            result['PodUid'] = self.pod_uid

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownloadToFile') is not None:
            self.download_to_file = m.get('DownloadToFile')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('MaxLines') is not None:
            self.max_lines = m.get('MaxLines')

        if m.get('PodUid') is not None:
            self.pod_uid = m.get('PodUid')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

