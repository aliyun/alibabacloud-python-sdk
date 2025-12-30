# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class GetDynamicImageJobResponseBody(DaraModel):
    def __init__(
        self,
        dynamic_image_job: main_models.GetDynamicImageJobResponseBodyDynamicImageJob = None,
        request_id: str = None,
    ):
        # The information about the snapshot job.
        self.dynamic_image_job = dynamic_image_job
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.dynamic_image_job:
            self.dynamic_image_job.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dynamic_image_job is not None:
            result['DynamicImageJob'] = self.dynamic_image_job.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DynamicImageJob') is not None:
            temp_model = main_models.GetDynamicImageJobResponseBodyDynamicImageJob()
            self.dynamic_image_job = temp_model.from_map(m.get('DynamicImageJob'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetDynamicImageJobResponseBodyDynamicImageJob(DaraModel):
    def __init__(
        self,
        code: str = None,
        create_time: str = None,
        finish_time: str = None,
        input: main_models.GetDynamicImageJobResponseBodyDynamicImageJobInput = None,
        job_id: str = None,
        message: str = None,
        modified_time: str = None,
        name: str = None,
        output: main_models.GetDynamicImageJobResponseBodyDynamicImageJobOutput = None,
        output_url: str = None,
        pipeline_id: str = None,
        status: str = None,
        submit_time: str = None,
        template_config: str = None,
        template_id: str = None,
        trigger_source: str = None,
        user_data: str = None,
    ):
        # Error codes
        self.code = code
        # The time when the job was created.
        self.create_time = create_time
        # The time when the job was complete.
        self.finish_time = finish_time
        # The input of the job.
        self.input = input
        # The job ID.
        self.job_id = job_id
        # The error message that is returned.
        self.message = message
        # The time when the job was last modified.
        self.modified_time = modified_time
        # The name of the job.
        self.name = name
        # The output of the job.
        self.output = output
        # The URL of the output animated image.
        self.output_url = output_url
        # The ID of the MPS queue to which the job was submitted.
        self.pipeline_id = pipeline_id
        # The state of the job.
        # 
        # Valid values:
        # 
        # *   Init: The job is submitted.
        # *   Success: The job is successful.
        # *   Fail: The job failed.
        self.status = status
        # The time when the job was submitted.
        self.submit_time = submit_time
        # The animation template configuration.
        self.template_config = template_config
        # The template ID.
        self.template_id = template_id
        # The request trigger source.
        # 
        # Valid values:
        # 
        # *   Console
        # *   Workflow
        # *   API
        self.trigger_source = trigger_source
        # The user-defined data.
        self.user_data = user_data

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
        if self.code is not None:
            result['Code'] = self.code

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time

        if self.input is not None:
            result['Input'] = self.input.to_map()

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.message is not None:
            result['Message'] = self.message

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.name is not None:
            result['Name'] = self.name

        if self.output is not None:
            result['Output'] = self.output.to_map()

        if self.output_url is not None:
            result['OutputUrl'] = self.output_url

        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id

        if self.status is not None:
            result['Status'] = self.status

        if self.submit_time is not None:
            result['SubmitTime'] = self.submit_time

        if self.template_config is not None:
            result['TemplateConfig'] = self.template_config

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.trigger_source is not None:
            result['TriggerSource'] = self.trigger_source

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

        if m.get('Input') is not None:
            temp_model = main_models.GetDynamicImageJobResponseBodyDynamicImageJobInput()
            self.input = temp_model.from_map(m.get('Input'))

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Output') is not None:
            temp_model = main_models.GetDynamicImageJobResponseBodyDynamicImageJobOutput()
            self.output = temp_model.from_map(m.get('Output'))

        if m.get('OutputUrl') is not None:
            self.output_url = m.get('OutputUrl')

        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')

        if m.get('TemplateConfig') is not None:
            self.template_config = m.get('TemplateConfig')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TriggerSource') is not None:
            self.trigger_source = m.get('TriggerSource')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

class GetDynamicImageJobResponseBodyDynamicImageJobOutput(DaraModel):
    def __init__(
        self,
        media: str = None,
        oss_file: main_models.GetDynamicImageJobResponseBodyDynamicImageJobOutputOssFile = None,
        type: str = None,
    ):
        # The input file. If Type is set to OSS, the URL of an OSS object is returned. If Type is set to Media, the ID of a media asset is returned. The URL of an OSS object can be in one of the following formats:
        # 
        # 1.  OSS://bucket/object
        # 2.  http(s)://bucket.oss-[RegionId].aliyuncs.com/object In the URL, bucket specifies an OSS bucket that resides in the same region as the job, and object specifies the object URL in OSS.
        self.media = media
        # The three key elements of OSS.
        self.oss_file = oss_file
        # The type of the input file. Valid values: OSS: an OSS object. Media: a media asset.
        self.type = type

    def validate(self):
        if self.oss_file:
            self.oss_file.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.media is not None:
            result['Media'] = self.media

        if self.oss_file is not None:
            result['OssFile'] = self.oss_file.to_map()

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Media') is not None:
            self.media = m.get('Media')

        if m.get('OssFile') is not None:
            temp_model = main_models.GetDynamicImageJobResponseBodyDynamicImageJobOutputOssFile()
            self.oss_file = temp_model.from_map(m.get('OssFile'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetDynamicImageJobResponseBodyDynamicImageJobOutputOssFile(DaraModel):
    def __init__(
        self,
        bucket: str = None,
        location: str = None,
        object: str = None,
    ):
        # The OSS bucket.
        self.bucket = bucket
        # The OSS location.
        self.location = location
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

        if self.location is not None:
            result['Location'] = self.location

        if self.object is not None:
            result['Object'] = self.object

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')

        if m.get('Location') is not None:
            self.location = m.get('Location')

        if m.get('Object') is not None:
            self.object = m.get('Object')

        return self

class GetDynamicImageJobResponseBodyDynamicImageJobInput(DaraModel):
    def __init__(
        self,
        media: str = None,
        oss_file: main_models.GetDynamicImageJobResponseBodyDynamicImageJobInputOssFile = None,
        type: str = None,
    ):
        # The input file. If Type is set to OSS, the URL of an OSS object is returned. If Type is set to Media, the ID of a media asset is returned. The URL of an OSS object can be in one of the following formats:
        # 
        # 1.  OSS://bucket/object
        # 2.  http(s)://bucket.oss-[RegionId].aliyuncs.com/object
        # 
        # In the URL, bucket specifies an OSS bucket that resides in the same region as the job, and object specifies the object URL in OSS.
        self.media = media
        # The three key elements of OSS.
        self.oss_file = oss_file
        # The type of the input file. Valid values:
        # 
        # 1.  OSS: an Object Storage Service (OSS) object.
        # 2.  Media: a media asset.
        self.type = type

    def validate(self):
        if self.oss_file:
            self.oss_file.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.media is not None:
            result['Media'] = self.media

        if self.oss_file is not None:
            result['OssFile'] = self.oss_file.to_map()

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Media') is not None:
            self.media = m.get('Media')

        if m.get('OssFile') is not None:
            temp_model = main_models.GetDynamicImageJobResponseBodyDynamicImageJobInputOssFile()
            self.oss_file = temp_model.from_map(m.get('OssFile'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetDynamicImageJobResponseBodyDynamicImageJobInputOssFile(DaraModel):
    def __init__(
        self,
        bucket: str = None,
        location: str = None,
        object: str = None,
    ):
        # The OSS bucket.
        self.bucket = bucket
        # The OSS location.
        self.location = location
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

        if self.location is not None:
            result['Location'] = self.location

        if self.object is not None:
            result['Object'] = self.object

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')

        if m.get('Location') is not None:
            self.location = m.get('Location')

        if m.get('Object') is not None:
            self.object = m.get('Object')

        return self

