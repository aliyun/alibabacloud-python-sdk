# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitDynamicImageJobRequest(DaraModel):
    def __init__(
        self,
        dynamic_image_template_id: str = None,
        override_params: str = None,
        video_id: str = None,
    ):
        # The ID of the frame animation template.
        # 
        # This parameter is required.
        self.dynamic_image_template_id = dynamic_image_template_id
        # The override parameter. Specify the value in the JSON format. For more information, see [Parameters for media processing](https://help.aliyun.com/document_detail/98618.html). You can use this parameter to override configurations in the animated image template. For more information, see the "DynamicImageTemplateConfig: the configurations of an animated sticker template" section of the [Basic data types](https://help.aliyun.com/document_detail/52839.html) topic.
        self.override_params = override_params
        # The ID of the video. You can use one of the following methods to obtain the ID:
        # 
        # *   Log on to the [ApsaraVideo VOD](https://vod.console.aliyun.com) console. In the left-side navigation pane, choose **Media Files** > **Audio/Video**. On the Video and Audio page, view the ID of the media file. This method is applicable to files that are uploaded by using the ApsaraVideo VOD console.
        # *   Obtain the value of VideoId from the response to the [CreateUploadVideo](https://help.aliyun.com/document_detail/55407.html) operation that you call to upload media files.
        # *   Obtain the value of VideoId from the response to the [SearchMedia](https://help.aliyun.com/document_detail/86044.html) operation after you upload media files.
        # 
        # This parameter is required.
        self.video_id = video_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dynamic_image_template_id is not None:
            result['DynamicImageTemplateId'] = self.dynamic_image_template_id

        if self.override_params is not None:
            result['OverrideParams'] = self.override_params

        if self.video_id is not None:
            result['VideoId'] = self.video_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DynamicImageTemplateId') is not None:
            self.dynamic_image_template_id = m.get('DynamicImageTemplateId')

        if m.get('OverrideParams') is not None:
            self.override_params = m.get('OverrideParams')

        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')

        return self

