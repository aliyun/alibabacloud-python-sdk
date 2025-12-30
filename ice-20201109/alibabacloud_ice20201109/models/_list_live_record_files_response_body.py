# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class ListLiveRecordFilesResponseBody(DaraModel):
    def __init__(
        self,
        files: List[main_models.ListLiveRecordFilesResponseBodyFiles] = None,
        page_no: int = None,
        page_size: str = None,
        request_id: str = None,
        sort_by: str = None,
        total_count: str = None,
    ):
        # The list of index files.
        self.files = files
        # The page number.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The sorting order of the index files by creation time.
        self.sort_by = sort_by
        # The total number of files that meet the specified conditions.
        self.total_count = total_count

    def validate(self):
        if self.files:
            for v1 in self.files:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Files'] = []
        if self.files is not None:
            for k1 in self.files:
                result['Files'].append(k1.to_map() if k1 else None)

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.files = []
        if m.get('Files') is not None:
            for k1 in m.get('Files'):
                temp_model = main_models.ListLiveRecordFilesResponseBodyFiles()
                self.files.append(temp_model.from_map(k1))

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListLiveRecordFilesResponseBodyFiles(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        duration: float = None,
        end_time: str = None,
        format: str = None,
        height: int = None,
        job_id: str = None,
        job_name: str = None,
        record_id: str = None,
        record_output: str = None,
        record_url: str = None,
        start_time: str = None,
        stream_url: str = None,
        width: int = None,
    ):
        # The time when the file was created in UTC.
        self.create_time = create_time
        # The recording length. Unit: seconds.
        self.duration = duration
        # The end of the time range to query. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.end_time = end_time
        # The format of the recording file.
        self.format = format
        # The height of the video.
        self.height = height
        # The ID of the recording job.
        self.job_id = job_id
        # The name of the recording job.
        self.job_name = job_name
        # The ID of the index file.
        self.record_id = record_id
        # The storage information about the recording file.
        self.record_output = record_output
        # The URL of the index file.
        self.record_url = record_url
        # The beginning of the time range to query. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.start_time = start_time
        # The name of the live stream.
        self.stream_url = stream_url
        # The width of the video.
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.format is not None:
            result['Format'] = self.format

        if self.height is not None:
            result['Height'] = self.height

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.job_name is not None:
            result['JobName'] = self.job_name

        if self.record_id is not None:
            result['RecordId'] = self.record_id

        if self.record_output is not None:
            result['RecordOutput'] = self.record_output

        if self.record_url is not None:
            result['RecordUrl'] = self.record_url

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.stream_url is not None:
            result['StreamUrl'] = self.stream_url

        if self.width is not None:
            result['Width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Format') is not None:
            self.format = m.get('Format')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')

        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')

        if m.get('RecordOutput') is not None:
            self.record_output = m.get('RecordOutput')

        if m.get('RecordUrl') is not None:
            self.record_url = m.get('RecordUrl')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StreamUrl') is not None:
            self.stream_url = m.get('StreamUrl')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

