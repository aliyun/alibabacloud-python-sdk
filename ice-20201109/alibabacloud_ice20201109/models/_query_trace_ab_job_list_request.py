# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryTraceAbJobListRequest(DaraModel):
    def __init__(
        self,
        create_time_end: int = None,
        create_time_start: int = None,
        job_id: str = None,
        page_number: int = None,
        page_size: int = None,
        trace_media_id: str = None,
    ):
        # The end of the creation time range for the query, in UNIX timestamp format.
        self.create_time_end = create_time_end
        # The start of the creation time range for the query, in UNIX timestamp format.
        self.create_time_start = create_time_start
        # The job ID. You can obtain the value of this parameter from the response of the SubmitTraceAbJob operation.
        self.job_id = job_id
        # The page number.
        self.page_number = page_number
        # The number of entries to return on each page.
        self.page_size = page_size
        # The media ID for the trace watermark. You can obtain this from the response of the SubmitTraceAbJob operation.
        self.trace_media_id = trace_media_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time_end is not None:
            result['CreateTimeEnd'] = self.create_time_end

        if self.create_time_start is not None:
            result['CreateTimeStart'] = self.create_time_start

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.trace_media_id is not None:
            result['TraceMediaId'] = self.trace_media_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTimeEnd') is not None:
            self.create_time_end = m.get('CreateTimeEnd')

        if m.get('CreateTimeStart') is not None:
            self.create_time_start = m.get('CreateTimeStart')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TraceMediaId') is not None:
            self.trace_media_id = m.get('TraceMediaId')

        return self

