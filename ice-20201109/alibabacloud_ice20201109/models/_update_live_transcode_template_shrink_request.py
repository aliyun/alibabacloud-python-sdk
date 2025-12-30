# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateLiveTranscodeTemplateShrinkRequest(DaraModel):
    def __init__(
        self,
        name: str = None,
        template_config_shrink: str = None,
        template_id: str = None,
    ):
        # The template name.
        self.name = name
        # The configuration of the template.
        self.template_config_shrink = template_config_shrink
        # The template ID. To obtain the template ID, log on to the [Intelligent Media Services (IMS) console](https://ims.console.aliyun.com/summary), choose Real-time Media Processing > Template Management, and then click the Transcoding tab. Alternatively, find the ID from the response parameters of the [CreateLiveTranscodeTemplate](https://help.aliyun.com/document_detail/449217.html) operation.
        # 
        # This parameter is required.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.template_config_shrink is not None:
            result['TemplateConfig'] = self.template_config_shrink

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('TemplateConfig') is not None:
            self.template_config_shrink = m.get('TemplateConfig')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

