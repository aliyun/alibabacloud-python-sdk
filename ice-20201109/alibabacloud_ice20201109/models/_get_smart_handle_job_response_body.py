# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class GetSmartHandleJobResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        job_id: str = None,
        job_result: main_models.GetSmartHandleJobResponseBodyJobResult = None,
        output: str = None,
        request_id: str = None,
        smart_job_info: main_models.GetSmartHandleJobResponseBodySmartJobInfo = None,
        state: str = None,
        user_data: str = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        # The job ID.
        self.job_id = job_id
        # The job results.
        self.job_result = job_result
        # The job results.
        self.output = output
        # The request ID.
        self.request_id = request_id
        # The information about the intelligent job.
        self.smart_job_info = smart_job_info
        # The job state.
        # 
        # Valid values:
        # 
        # *   Finished
        # *   Failed
        # *   Executing
        # *   Created
        self.state = state
        # The user-defined data in the JSON format.
        self.user_data = user_data

    def validate(self):
        if self.job_result:
            self.job_result.validate()
        if self.smart_job_info:
            self.smart_job_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.job_result is not None:
            result['JobResult'] = self.job_result.to_map()

        if self.output is not None:
            result['Output'] = self.output

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.smart_job_info is not None:
            result['SmartJobInfo'] = self.smart_job_info.to_map()

        if self.state is not None:
            result['State'] = self.state

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('JobResult') is not None:
            temp_model = main_models.GetSmartHandleJobResponseBodyJobResult()
            self.job_result = temp_model.from_map(m.get('JobResult'))

        if m.get('Output') is not None:
            self.output = m.get('Output')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SmartJobInfo') is not None:
            temp_model = main_models.GetSmartHandleJobResponseBodySmartJobInfo()
            self.smart_job_info = temp_model.from_map(m.get('SmartJobInfo'))

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

class GetSmartHandleJobResponseBodySmartJobInfo(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        input_config: main_models.GetSmartHandleJobResponseBodySmartJobInfoInputConfig = None,
        job_type: str = None,
        modified_time: str = None,
        output_config: main_models.GetSmartHandleJobResponseBodySmartJobInfoOutputConfig = None,
        title: str = None,
        user_id: str = None,
    ):
        # The time when the job was created.
        self.create_time = create_time
        # The job description.
        self.description = description
        # The input configurations.
        self.input_config = input_config
        # The job type.
        self.job_type = job_type
        # The time when the job was last modified.
        self.modified_time = modified_time
        # The output configurations.
        self.output_config = output_config
        # The job title.
        self.title = title
        # The user ID.
        self.user_id = user_id

    def validate(self):
        if self.input_config:
            self.input_config.validate()
        if self.output_config:
            self.output_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.input_config is not None:
            result['InputConfig'] = self.input_config.to_map()

        if self.job_type is not None:
            result['JobType'] = self.job_type

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.output_config is not None:
            result['OutputConfig'] = self.output_config.to_map()

        if self.title is not None:
            result['Title'] = self.title

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InputConfig') is not None:
            temp_model = main_models.GetSmartHandleJobResponseBodySmartJobInfoInputConfig()
            self.input_config = temp_model.from_map(m.get('InputConfig'))

        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('OutputConfig') is not None:
            temp_model = main_models.GetSmartHandleJobResponseBodySmartJobInfoOutputConfig()
            self.output_config = temp_model.from_map(m.get('OutputConfig'))

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class GetSmartHandleJobResponseBodySmartJobInfoOutputConfig(DaraModel):
    def __init__(
        self,
        bucket: str = None,
        object: str = None,
    ):
        # The OSS bucket.
        self.bucket = bucket
        # The OSS object.
        self.object = object

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket is not None:
            result['Bucket'] = self.bucket

        if self.object is not None:
            result['Object'] = self.object

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')

        if m.get('Object') is not None:
            self.object = m.get('Object')

        return self

class GetSmartHandleJobResponseBodySmartJobInfoInputConfig(DaraModel):
    def __init__(
        self,
        input_file: str = None,
    ):
        # The OSS URL or the ID of the material in the media asset library.
        self.input_file = input_file

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input_file is not None:
            result['InputFile'] = self.input_file

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputFile') is not None:
            self.input_file = m.get('InputFile')

        return self

class GetSmartHandleJobResponseBodyJobResult(DaraModel):
    def __init__(
        self,
        ai_result: str = None,
        media_id: str = None,
        media_url: str = None,
        usage: str = None,
    ):
        # The AI analysis result.
        self.ai_result = ai_result
        # The ID of the media asset.
        self.media_id = media_id
        self.media_url = media_url
        # The token usage. This parameter is returned only for keyword-based text generation jobs.
        self.usage = usage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ai_result is not None:
            result['AiResult'] = self.ai_result

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.media_url is not None:
            result['MediaUrl'] = self.media_url

        if self.usage is not None:
            result['Usage'] = self.usage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AiResult') is not None:
            self.ai_result = m.get('AiResult')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('MediaUrl') is not None:
            self.media_url = m.get('MediaUrl')

        if m.get('Usage') is not None:
            self.usage = m.get('Usage')

        return self

