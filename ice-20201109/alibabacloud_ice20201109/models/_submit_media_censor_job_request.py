# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class SubmitMediaCensorJobRequest(DaraModel):
    def __init__(
        self,
        barrages: str = None,
        cover_images: str = None,
        description: str = None,
        input: main_models.SubmitMediaCensorJobRequestInput = None,
        notify_url: str = None,
        output: str = None,
        schedule_config: main_models.SubmitMediaCensorJobRequestScheduleConfig = None,
        template_id: str = None,
        title: str = None,
        user_data: str = None,
    ):
        # The video barrages (on-screen comments).
        # 
        # > If specified, it overrides the barrages specified in the Media object.
        self.barrages = barrages
        # The Object Storage Service (OSS) files for the cover images, specified as a JSON array. You can specify up to five cover images.
        # 
        # > If specified, this parameter overrides the cover image information in the **Media** object.
        self.cover_images = cover_images
        # The video description. The maximum length is 128 bytes.
        # 
        # > If specified, this parameter overrides the description specified in the Media object.
        self.description = description
        # The input file to censor.
        self.input = input
        # The callback path. Both Message Service (MNS) and HTTP callbacks are supported.
        self.notify_url = notify_url
        # The output location for screenshots. The censor job generates screenshots and a result JSON file in the OSS location specified by this parameter.
        # 
        # - Example format: `oss://bucket/snapshot-{Count}.jpg`, where `bucket` is the name of an OSS bucket in the same region as the project, and `{Count}` is a placeholder for the screenshot sequence number.
        # 
        # - The detailed censor results are saved to a file named `{jobId}.output` in the same OSS folder as the value of `Output`. For information about the fields in the output file, see [Media censor result file fields](https://help.aliyun.com/document_detail/609211.html).
        self.output = output
        # The scheduling configuration.
        self.schedule_config = schedule_config
        # The template ID. If this parameter is left empty, the service uses the default template for the censor job.
        self.template_id = template_id
        # The video title. The maximum length is 64 bytes.
        # 
        # > If specified, this parameter overrides the title specified in the Media object.
        self.title = title
        # The user-defined data. The maximum length is 128 bytes.
        self.user_data = user_data

    def validate(self):
        if self.input:
            self.input.validate()
        if self.schedule_config:
            self.schedule_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.barrages is not None:
            result['Barrages'] = self.barrages

        if self.cover_images is not None:
            result['CoverImages'] = self.cover_images

        if self.description is not None:
            result['Description'] = self.description

        if self.input is not None:
            result['Input'] = self.input.to_map()

        if self.notify_url is not None:
            result['NotifyUrl'] = self.notify_url

        if self.output is not None:
            result['Output'] = self.output

        if self.schedule_config is not None:
            result['ScheduleConfig'] = self.schedule_config.to_map()

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.title is not None:
            result['Title'] = self.title

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Barrages') is not None:
            self.barrages = m.get('Barrages')

        if m.get('CoverImages') is not None:
            self.cover_images = m.get('CoverImages')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Input') is not None:
            temp_model = main_models.SubmitMediaCensorJobRequestInput()
            self.input = temp_model.from_map(m.get('Input'))

        if m.get('NotifyUrl') is not None:
            self.notify_url = m.get('NotifyUrl')

        if m.get('Output') is not None:
            self.output = m.get('Output')

        if m.get('ScheduleConfig') is not None:
            temp_model = main_models.SubmitMediaCensorJobRequestScheduleConfig()
            self.schedule_config = temp_model.from_map(m.get('ScheduleConfig'))

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

class SubmitMediaCensorJobRequestScheduleConfig(DaraModel):
    def __init__(
        self,
        pipeline_id: str = None,
        priority: int = None,
    ):
        # The pipeline ID.
        self.pipeline_id = pipeline_id
        # The task priority. A higher value indicates a higher priority. Valid values range from 1 to 10.
        self.priority = priority

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id

        if self.priority is not None:
            result['Priority'] = self.priority

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        return self

class SubmitMediaCensorJobRequestInput(DaraModel):
    def __init__(
        self,
        media: str = None,
        type: str = None,
    ):
        # The identifier for the input file. You can specify either an OSS URL or a media ID.
        # Valid OSS URL formats:
        # 
        # 1\\. `oss://bucket/object`
        # 
        # 2\\. `http(s)://bucket.oss-[regionId].aliyuncs.com/object`
        # 
        # The `bucket` must be in the same region as the project, and `object` is the path to the file.
        self.media = media
        # The type of the input file. Valid values:
        # 
        # `OSS`: an OSS URL
        # 
        # `Media`: a media ID
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

