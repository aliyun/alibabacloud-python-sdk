# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mts20140618 import models as main_models
from darabonba.model import DaraModel

class ListFpShotImportJobResponseBody(DaraModel):
    def __init__(
        self,
        fp_shot_import_job_list: List[main_models.ListFpShotImportJobResponseBodyFpShotImportJobList] = None,
        non_exist_ids: List[str] = None,
        request_id: str = None,
    ):
        # The jobs of importing text files to a text fingerprint library.
        self.fp_shot_import_job_list = fp_shot_import_job_list
        # The job IDs that do not exist. This parameter is not returned if all specified job IDs exist.
        self.non_exist_ids = non_exist_ids
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.fp_shot_import_job_list:
            for v1 in self.fp_shot_import_job_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FpShotImportJobList'] = []
        if self.fp_shot_import_job_list is not None:
            for k1 in self.fp_shot_import_job_list:
                result['FpShotImportJobList'].append(k1.to_map() if k1 else None)

        if self.non_exist_ids is not None:
            result['NonExistIds'] = self.non_exist_ids

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.fp_shot_import_job_list = []
        if m.get('FpShotImportJobList') is not None:
            for k1 in m.get('FpShotImportJobList'):
                temp_model = main_models.ListFpShotImportJobResponseBodyFpShotImportJobList()
                self.fp_shot_import_job_list.append(temp_model.from_map(k1))

        if m.get('NonExistIds') is not None:
            self.non_exist_ids = m.get('NonExistIds')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListFpShotImportJobResponseBodyFpShotImportJobList(DaraModel):
    def __init__(
        self,
        code: str = None,
        create_time: str = None,
        finish_time: str = None,
        fp_dbid: str = None,
        fp_import_config: str = None,
        id: str = None,
        input: str = None,
        message: str = None,
        pipeline_id: str = None,
        process_message: str = None,
        status: str = None,
        user_data: str = None,
    ):
        # The error code returned when the job fails.
        self.code = code
        # The time when the job was created.
        self.create_time = create_time
        # The time when the job was completed.
        self.finish_time = finish_time
        # The ID of the text fingerprint library.
        self.fp_dbid = fp_dbid
        # The import configuration.
        self.fp_import_config = fp_import_config
        # The job ID.
        self.id = id
        # The input file.
        self.input = input
        # The error message returned when the job fails.
        self.message = message
        # The ID of the ApsaraVideo Media Processing (MPS) queue to which the job is submitted.
        self.pipeline_id = pipeline_id
        # The processing information of the job.
        self.process_message = process_message
        # The status of the job. Valid values:
        # 
        # *   Processing: The job is in progress.
        # *   Fail: The job fails.
        # *   Success: The job is successful.
        self.status = status
        # The user-defined data.
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

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time

        if self.fp_dbid is not None:
            result['FpDBId'] = self.fp_dbid

        if self.fp_import_config is not None:
            result['FpImportConfig'] = self.fp_import_config

        if self.id is not None:
            result['Id'] = self.id

        if self.input is not None:
            result['Input'] = self.input

        if self.message is not None:
            result['Message'] = self.message

        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id

        if self.process_message is not None:
            result['ProcessMessage'] = self.process_message

        if self.status is not None:
            result['Status'] = self.status

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')

        if m.get('FpDBId') is not None:
            self.fp_dbid = m.get('FpDBId')

        if m.get('FpImportConfig') is not None:
            self.fp_import_config = m.get('FpImportConfig')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Input') is not None:
            self.input = m.get('Input')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')

        if m.get('ProcessMessage') is not None:
            self.process_message = m.get('ProcessMessage')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

