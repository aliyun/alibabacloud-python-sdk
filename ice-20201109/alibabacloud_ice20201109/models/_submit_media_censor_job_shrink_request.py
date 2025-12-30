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
        # The live comments of the video.
        # 
        # >  If this parameter is specified, the system checks the live comments specified by this parameter instead of the live comments of the input file specified by Media.
        self.barrages = barrages
        # The Object Storage Service (OSS) objects that are used as the thumbnails. Specify the thumbnails in a JSON array. A maximum of five thumbnails are supported.
        # 
        # >  If this parameter is specified, the system checks the thumbnails specified by this parameter instead of the thumbnails of the input file specified by **Media**.
        self.cover_images = cover_images
        # The video description, which can be up to 128 bytes in length.
        # 
        # >  If this parameter is specified, the system checks the description specified by this parameter instead of the description of the input file specified by Media.
        self.description = description
        # The information about the file to be moderated.
        self.input_shrink = input_shrink
        # The callback URL. Simple Message Queue (SMQ, formerly MNS) and HTTP callbacks are supported.
        self.notify_url = notify_url
        # The output snapshots. The moderation job generates output snapshots and the result JSON file in the path corresponding to the input file.
        # 
        # *   File name format of output snapshots: oss://bucket/snapshot-{Count}.jpg. In the path, bucket indicates an OSS bucket that resides in the same region as the current project, and {Count} is the sequence number of the snapshot.
        # *   The detailed moderation results are stored in the {jobId}.output file in the same OSS folder as the output snapshots. For more information about the parameters in the output file, see [Output parameters of media moderation jobs](https://help.aliyun.com/document_detail/609211.html).
        self.output = output
        # The scheduling configurations.
        self.schedule_config_shrink = schedule_config_shrink
        # The template ID. If this parameter is not specified, the default template is used for moderation.
        self.template_id = template_id
        # The video title, which can be up to 64 bytes in length.
        # 
        # >  If this parameter is specified, the system checks the title specified by this parameter instead of the title of the input file specified by Media.
        self.title = title
        # The user-defined data, which can be up to 128 bytes in length.
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

