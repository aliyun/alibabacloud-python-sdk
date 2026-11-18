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
        # The ID of the animated image template.
        # 
        # This parameter is required.
        self.dynamic_image_template_id = dynamic_image_template_id
        # The override parameters in JSON string format. For more information, see [OverrideParams](https://help.aliyun.com/document_detail/98618.html). You can override the parameters in the animated image template configuration. For more information, see [DynamicImageTemplateConfig](https://help.aliyun.com/document_detail/52839.html).
        self.override_params = override_params
        # The video ID. You can obtain the video ID by using one of the following methods:
        # 
        # - For videos uploaded through the console, log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com) and choose **Media Assets** > **Audio/Video** to view the video ID.
        # - When you call the [Obtain the upload URL and credential for a video](https://help.aliyun.com/document_detail/55407.html) operation to obtain the upload URL and credential, the video ID is the value of the VideoId response parameter.
        # - After a video is uploaded, you can call the [Search for media information](https://help.aliyun.com/document_detail/86044.html) operation to query the video ID. The video ID is the value of the VideoId response parameter.
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

