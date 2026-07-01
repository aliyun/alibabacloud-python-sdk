# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitMediaCensorJobShrinkRequest(DaraModel):
    def __init__(
        self,
        barrages: str = None,
        cover_images: str = None,
        description: str = None,
        input_shrink: str = None,
        notify_url: str = None,
        output: str = None,
        schedule_config_shrink: str = None,
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
        self.input_shrink = input_shrink
        # The callback path. Both Message Service (MNS) and HTTP callbacks are supported.
        self.notify_url = notify_url
        # The output location for screenshots. The censor job generates screenshots and a result JSON file in the OSS location specified by this parameter.
        # 
        # - Example format: `oss://bucket/snapshot-{Count}.jpg`, where `bucket` is the name of an OSS bucket in the same region as the project, and `{Count}` is a placeholder for the screenshot sequence number.
        # 
        # - The detailed censor results are saved to a file named `{jobId}.output` in the same OSS folder as the value of `Output`. For information about the fields in the output file, see [Media censor result file fields](https://help.aliyun.com/document_detail/609211.html).
        self.output = output
        # The scheduling configuration.
        self.schedule_config_shrink = schedule_config_shrink
        # The template ID. If this parameter is left empty, the service uses the default template for the censor job.
        self.template_id = template_id
        # The video title. The maximum length is 64 bytes.
        # 
        # > If specified, this parameter overrides the title specified in the Media object.
        self.title = title
        # The user-defined data. The maximum length is 128 bytes.
        self.user_data = user_data

    def validate(self):
        pass

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

        if self.input_shrink is not None:
            result['Input'] = self.input_shrink

        if self.notify_url is not None:
            result['NotifyUrl'] = self.notify_url

        if self.output is not None:
            result['Output'] = self.output

        if self.schedule_config_shrink is not None:
            result['ScheduleConfig'] = self.schedule_config_shrink

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
            self.input_shrink = m.get('Input')

        if m.get('NotifyUrl') is not None:
            self.notify_url = m.get('NotifyUrl')

        if m.get('Output') is not None:
            self.output = m.get('Output')

        if m.get('ScheduleConfig') is not None:
            self.schedule_config_shrink = m.get('ScheduleConfig')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

