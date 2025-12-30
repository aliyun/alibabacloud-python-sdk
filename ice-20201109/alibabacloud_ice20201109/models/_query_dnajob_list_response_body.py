# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class QueryDNAJobListResponseBody(DaraModel):
    def __init__(
        self,
        job_list: List[main_models.QueryDNAJobListResponseBodyJobList] = None,
        request_id: str = None,
    ):
        # The queried media fingerprint analysis jobs.
        self.job_list = job_list
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.job_list:
            for v1 in self.job_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['JobList'] = []
        if self.job_list is not None:
            for k1 in self.job_list:
                result['JobList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.job_list = []
        if m.get('JobList') is not None:
            for k1 in m.get('JobList'):
                temp_model = main_models.QueryDNAJobListResponseBodyJobList()
                self.job_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class QueryDNAJobListResponseBodyJobList(DaraModel):
    def __init__(
        self,
        code: str = None,
        config: str = None,
        creation_time: str = None,
        dbid: str = None,
        dnaresult: str = None,
        finish_time: str = None,
        id: str = None,
        input: main_models.QueryDNAJobListResponseBodyJobListInput = None,
        message: str = None,
        primary_key: str = None,
        status: str = None,
        user_data: str = None,
    ):
        # The response code.
        self.code = code
        # The configurations of the media fingerprint analysis job.
        self.config = config
        # The time when the job was created.
        self.creation_time = creation_time
        # The ID of the media fingerprint library.
        self.dbid = dbid
        # The URL of the media fingerprint analysis result.
        self.dnaresult = dnaresult
        # The time when the job was complete.
        self.finish_time = finish_time
        # The job ID.
        self.id = id
        # The details of the input file.
        self.input = input
        # The returned message.
        self.message = message
        # The primary key of the video. You must make sure that each primary key is unique.
        self.primary_key = primary_key
        # The job state. Valid values:
        # 
        # *   **Queuing**: The job is waiting in the queue.
        # *   **Analysing**: The job is in progress.
        # *   **Success**: The job is successful.
        # *   **Fail**: The job failed.
        self.status = status
        # The user-defined data.
        self.user_data = user_data

    def validate(self):
        if self.input:
            self.input.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.config is not None:
            result['Config'] = self.config

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.dbid is not None:
            result['DBId'] = self.dbid

        if self.dnaresult is not None:
            result['DNAResult'] = self.dnaresult

        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time

        if self.id is not None:
            result['Id'] = self.id

        if self.input is not None:
            result['Input'] = self.input.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.primary_key is not None:
            result['PrimaryKey'] = self.primary_key

        if self.status is not None:
            result['Status'] = self.status

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('DBId') is not None:
            self.dbid = m.get('DBId')

        if m.get('DNAResult') is not None:
            self.dnaresult = m.get('DNAResult')

        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Input') is not None:
            temp_model = main_models.QueryDNAJobListResponseBodyJobListInput()
            self.input = temp_model.from_map(m.get('Input'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PrimaryKey') is not None:
            self.primary_key = m.get('PrimaryKey')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

class QueryDNAJobListResponseBodyJobListInput(DaraModel):
    def __init__(
        self,
        media: str = None,
        type: str = None,
    ):
        # The input file. The file can be an OSS object or a media asset. The path of an OSS object can be in one of the following formats:
        # 
        # 1\\. oss://bucket/object
        # 
        # 2\\. http(s)://bucket.oss-[regionId].aliyuncs.com/object
        # 
        # In the preceding paths, bucket indicates an OSS bucket that resides in the same region as the current project, and object indicates the path of the object in the bucket.
        self.media = media
        # The type of the input file. Valid values:
        # 
        # 1.  OSS: Object Storage Service (OSS) object.
        # 2.  Media: media asset.
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

