# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class GetBatchMediaProducingJobResponseBody(DaraModel):
    def __init__(
        self,
        editing_batch_job: main_models.GetBatchMediaProducingJobResponseBodyEditingBatchJob = None,
        request_id: str = None,
    ):
        # The information about the quick video production job.
        self.editing_batch_job = editing_batch_job
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.editing_batch_job:
            self.editing_batch_job.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.editing_batch_job is not None:
            result['EditingBatchJob'] = self.editing_batch_job.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EditingBatchJob') is not None:
            temp_model = main_models.GetBatchMediaProducingJobResponseBodyEditingBatchJob()
            self.editing_batch_job = temp_model.from_map(m.get('EditingBatchJob'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetBatchMediaProducingJobResponseBodyEditingBatchJob(DaraModel):
    def __init__(
        self,
        complete_time: str = None,
        create_time: str = None,
        editing_config: str = None,
        extend: str = None,
        extend_input: str = None,
        extend_output: str = None,
        input_config: str = None,
        job_id: str = None,
        job_type: str = None,
        modified_time: str = None,
        output_config: str = None,
        status: str = None,
        sub_job_list: List[main_models.GetBatchMediaProducingJobResponseBodyEditingBatchJobSubJobList] = None,
        user_data: str = None,
    ):
        # The time when the job was complete.
        # 
        # The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.complete_time = complete_time
        # The time when the job was created. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.create_time = create_time
        # The editing configurations. For more information, see [EditingConfig](~~2692547#1be9bba03b7qu~~).
        self.editing_config = editing_config
        # The extended information. This parameter contains the following fields:
        # 
        # ErrorCode: the error code of the main job.
        # 
        # ErrorMessage: the error message of the main job.
        self.extend = extend
        self.extend_input = extend_input
        self.extend_output = extend_output
        # The input configurations. For more information, see [InputConfig](~~2692547#2faed1559549n~~).
        self.input_config = input_config
        # The job ID.
        self.job_id = job_id
        self.job_type = job_type
        # The time when the job was last modified.
        # 
        # The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.modified_time = modified_time
        # The output configurations. For more information, see [OutputConfig](~~2692547#447b928fcbuoa~~).
        self.output_config = output_config
        # The job state. Valid values:
        # 
        # Init: The job is initialized.
        # 
        # Processing: The job is in progress.
        # 
        # Finished: The job is complete.
        self.status = status
        # The quick video production subjobs.
        self.sub_job_list = sub_job_list
        # The user-defined data, including the business and callback configurations. For more information, see [UserData](https://help.aliyun.com/document_detail/357745.html).
        self.user_data = user_data

    def validate(self):
        if self.sub_job_list:
            for v1 in self.sub_job_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.complete_time is not None:
            result['CompleteTime'] = self.complete_time

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.editing_config is not None:
            result['EditingConfig'] = self.editing_config

        if self.extend is not None:
            result['Extend'] = self.extend

        if self.extend_input is not None:
            result['ExtendInput'] = self.extend_input

        if self.extend_output is not None:
            result['ExtendOutput'] = self.extend_output

        if self.input_config is not None:
            result['InputConfig'] = self.input_config

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.job_type is not None:
            result['JobType'] = self.job_type

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.output_config is not None:
            result['OutputConfig'] = self.output_config

        if self.status is not None:
            result['Status'] = self.status

        result['SubJobList'] = []
        if self.sub_job_list is not None:
            for k1 in self.sub_job_list:
                result['SubJobList'].append(k1.to_map() if k1 else None)

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompleteTime') is not None:
            self.complete_time = m.get('CompleteTime')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('EditingConfig') is not None:
            self.editing_config = m.get('EditingConfig')

        if m.get('Extend') is not None:
            self.extend = m.get('Extend')

        if m.get('ExtendInput') is not None:
            self.extend_input = m.get('ExtendInput')

        if m.get('ExtendOutput') is not None:
            self.extend_output = m.get('ExtendOutput')

        if m.get('InputConfig') is not None:
            self.input_config = m.get('InputConfig')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('OutputConfig') is not None:
            self.output_config = m.get('OutputConfig')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.sub_job_list = []
        if m.get('SubJobList') is not None:
            for k1 in m.get('SubJobList'):
                temp_model = main_models.GetBatchMediaProducingJobResponseBodyEditingBatchJobSubJobList()
                self.sub_job_list.append(temp_model.from_map(k1))

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

class GetBatchMediaProducingJobResponseBodyEditingBatchJobSubJobList(DaraModel):
    def __init__(
        self,
        duration: float = None,
        error_code: str = None,
        error_message: str = None,
        job_id: str = None,
        media_id: str = None,
        media_url: str = None,
        project_id: str = None,
        status: str = None,
    ):
        self.duration = duration
        # The error code that is returned if the subjob failed. This parameter is not returned if the subjob is successful.
        self.error_code = error_code
        # The error message that is returned if the subjob failed. This parameter is not returned if the subjob is successful.
        self.error_message = error_message
        # The subjob ID.
        self.job_id = job_id
        # The ID of the output media asset.
        self.media_id = media_id
        # The URL of the output file.
        self.media_url = media_url
        # The ID of the online editing project.
        self.project_id = project_id
        # The subjob state. Valid values:
        # 
        # Init: The subjob is initialized.
        # 
        # Processing: The subjob is in progress.
        # 
        # Success: The subjob is successful.
        # 
        # Failed: The subjob failed.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration is not None:
            result['Duration'] = self.duration

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.media_url is not None:
            result['MediaURL'] = self.media_url

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('MediaURL') is not None:
            self.media_url = m.get('MediaURL')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

