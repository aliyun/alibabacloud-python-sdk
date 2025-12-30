# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class QueryCopyrightJobListResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.QueryCopyrightJobListResponseBodyData] = None,
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
                temp_model = main_models.QueryCopyrightJobListResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')

        return self

class QueryCopyrightJobListResponseBodyData(DaraModel):
    def __init__(
        self,
        gmt_create: int = None,
        gmt_modified: int = None,
        input: main_models.QueryCopyrightJobListResponseBodyDataInput = None,
        job_id: str = None,
        level: int = None,
        message: str = None,
        output: main_models.QueryCopyrightJobListResponseBodyDataOutput = None,
        result: str = None,
        status: str = None,
        user_data: str = None,
        user_id: int = None,
    ):
        # The creation time of the job.
        self.gmt_create = gmt_create
        # The last modification time of the job.
        self.gmt_modified = gmt_modified
        # Information about the input video for watermarking.
        self.input = input
        # The job ID.
        self.job_id = job_id
        # The watermark level.
        self.level = level
        # The content of the embedded watermark.
        self.message = message
        # Information about the watermarked output video.
        self.output = output
        # The job result.
        self.result = result
        # The status of the job.
        self.status = status
        # The user-defined data.
        self.user_data = user_data
        # The ID of the user who initiated the job.
        self.user_id = user_id

    def validate(self):
        if self.input:
            self.input.validate()
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

        if self.input is not None:
            result['Input'] = self.input.to_map()

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.level is not None:
            result['Level'] = self.level

        if self.message is not None:
            result['Message'] = self.message

        if self.output is not None:
            result['Output'] = self.output.to_map()

        if self.result is not None:
            result['Result'] = self.result

        if self.status is not None:
            result['Status'] = self.status

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

        if m.get('Input') is not None:
            temp_model = main_models.QueryCopyrightJobListResponseBodyDataInput()
            self.input = temp_model.from_map(m.get('Input'))

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Output') is not None:
            temp_model = main_models.QueryCopyrightJobListResponseBodyDataOutput()
            self.output = temp_model.from_map(m.get('Output'))

        if m.get('Result') is not None:
            self.result = m.get('Result')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class QueryCopyrightJobListResponseBodyDataOutput(DaraModel):
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

class QueryCopyrightJobListResponseBodyDataInput(DaraModel):
    def __init__(
        self,
        media: str = None,
        type: str = None,
    ):
        # The specific input information.
        self.media = media
        # The type of the input file. Valid values:
        # 
        # 1.  OSS: an Object Storage Service (OSS) object.
        # 2.  Media: a media asset.
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

