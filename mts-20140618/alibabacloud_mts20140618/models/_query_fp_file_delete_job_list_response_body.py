# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mts20140618 import models as main_models
from darabonba.model import DaraModel

class QueryFpFileDeleteJobListResponseBody(DaraModel):
    def __init__(
        self,
        fp_file_delete_job_list: main_models.QueryFpFileDeleteJobListResponseBodyFpFileDeleteJobList = None,
        non_exist_ids: main_models.QueryFpFileDeleteJobListResponseBodyNonExistIds = None,
        request_id: str = None,
    ):
        self.fp_file_delete_job_list = fp_file_delete_job_list
        self.non_exist_ids = non_exist_ids
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.fp_file_delete_job_list:
            self.fp_file_delete_job_list.validate()
        if self.non_exist_ids:
            self.non_exist_ids.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fp_file_delete_job_list is not None:
            result['FpFileDeleteJobList'] = self.fp_file_delete_job_list.to_map()

        if self.non_exist_ids is not None:
            result['NonExistIds'] = self.non_exist_ids.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FpFileDeleteJobList') is not None:
            temp_model = main_models.QueryFpFileDeleteJobListResponseBodyFpFileDeleteJobList()
            self.fp_file_delete_job_list = temp_model.from_map(m.get('FpFileDeleteJobList'))

        if m.get('NonExistIds') is not None:
            temp_model = main_models.QueryFpFileDeleteJobListResponseBodyNonExistIds()
            self.non_exist_ids = temp_model.from_map(m.get('NonExistIds'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class QueryFpFileDeleteJobListResponseBodyNonExistIds(DaraModel):
    def __init__(
        self,
        string: List[str] = None,
    ):
        self.string = string

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.string is not None:
            result['String'] = self.string

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('String') is not None:
            self.string = m.get('String')

        return self

class QueryFpFileDeleteJobListResponseBodyFpFileDeleteJobList(DaraModel):
    def __init__(
        self,
        fp_file_delete_job: List[main_models.QueryFpFileDeleteJobListResponseBodyFpFileDeleteJobListFpFileDeleteJob] = None,
    ):
        self.fp_file_delete_job = fp_file_delete_job

    def validate(self):
        if self.fp_file_delete_job:
            for v1 in self.fp_file_delete_job:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FpFileDeleteJob'] = []
        if self.fp_file_delete_job is not None:
            for k1 in self.fp_file_delete_job:
                result['FpFileDeleteJob'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.fp_file_delete_job = []
        if m.get('FpFileDeleteJob') is not None:
            for k1 in m.get('FpFileDeleteJob'):
                temp_model = main_models.QueryFpFileDeleteJobListResponseBodyFpFileDeleteJobListFpFileDeleteJob()
                self.fp_file_delete_job.append(temp_model.from_map(k1))

        return self

class QueryFpFileDeleteJobListResponseBodyFpFileDeleteJobListFpFileDeleteJob(DaraModel):
    def __init__(
        self,
        code: str = None,
        creation_time: str = None,
        file_ids: str = None,
        finish_time: str = None,
        fp_dbid: str = None,
        id: str = None,
        message: str = None,
        pipeline_id: str = None,
        status: str = None,
        user_data: str = None,
    ):
        self.code = code
        self.creation_time = creation_time
        self.file_ids = file_ids
        self.finish_time = finish_time
        self.fp_dbid = fp_dbid
        self.id = id
        self.message = message
        self.pipeline_id = pipeline_id
        self.status = status
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.file_ids is not None:
            result['FileIds'] = self.file_ids

        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time

        if self.fp_dbid is not None:
            result['FpDBId'] = self.fp_dbid

        if self.id is not None:
            result['Id'] = self.id

        if self.message is not None:
            result['Message'] = self.message

        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id

        if self.status is not None:
            result['Status'] = self.status

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('FileIds') is not None:
            self.file_ids = m.get('FileIds')

        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')

        if m.get('FpDBId') is not None:
            self.fp_dbid = m.get('FpDBId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

