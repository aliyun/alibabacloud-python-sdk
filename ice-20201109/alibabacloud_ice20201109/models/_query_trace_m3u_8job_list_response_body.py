# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class QueryTraceM3u8JobListResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.QueryTraceM3u8JobListResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        status_code: int = None,
    ):
        # The data returned.
        self.data = data
        # The message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # The status code.
        self.status_code = status_code

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status_code is not None:
            result['StatusCode'] = self.status_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.QueryTraceM3u8JobListResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')

        return self

class QueryTraceM3u8JobListResponseBodyData(DaraModel):
    def __init__(
        self,
        gmt_create: int = None,
        gmt_modified: int = None,
        job_id: str = None,
        output: main_models.QueryTraceM3u8JobListResponseBodyDataOutput = None,
        status: str = None,
        trace: str = None,
        trace_media_id: str = None,
        user_data: str = None,
        user_id: int = None,
    ):
        # The creation time of the job.
        self.gmt_create = gmt_create
        # The last modification time of the job.
        self.gmt_modified = gmt_modified
        # The job ID.
        self.job_id = job_id
        # The output video.
        self.output = output
        # The current status of the job.
        self.status = status
        # The watermark information.
        self.trace = trace
        # The media ID for the trace watermark.
        self.trace_media_id = trace_media_id
        # The user-defined data.
        self.user_data = user_data
        # The ID of the user who initiated the job.
        self.user_id = user_id

    def validate(self):
        if self.output:
            self.output.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.output is not None:
            result['Output'] = self.output.to_map()

        if self.status is not None:
            result['Status'] = self.status

        if self.trace is not None:
            result['Trace'] = self.trace

        if self.trace_media_id is not None:
            result['TraceMediaId'] = self.trace_media_id

        if self.user_data is not None:
            result['UserData'] = self.user_data

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('Output') is not None:
            temp_model = main_models.QueryTraceM3u8JobListResponseBodyDataOutput()
            self.output = temp_model.from_map(m.get('Output'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Trace') is not None:
            self.trace = m.get('Trace')

        if m.get('TraceMediaId') is not None:
            self.trace_media_id = m.get('TraceMediaId')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class QueryTraceM3u8JobListResponseBodyDataOutput(DaraModel):
    def __init__(
        self,
        media: str = None,
        type: str = None,
    ):
        # The specific output information.
        self.media = media
        # The type of the output file. Valid values:
        # 
        # *   OSS: an OSS object.
        # *   Media: a media asset.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.media is not None:
            result['Media'] = self.media

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Media') is not None:
            self.media = m.get('Media')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

