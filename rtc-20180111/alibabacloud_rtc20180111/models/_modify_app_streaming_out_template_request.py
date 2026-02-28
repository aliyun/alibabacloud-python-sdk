# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rtc20180111 import models as main_models
from darabonba.model import DaraModel

class ModifyAppStreamingOutTemplateRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        streaming_out_template: main_models.ModifyAppStreamingOutTemplateRequestStreamingOutTemplate = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.streaming_out_template = streaming_out_template

    def validate(self):
        if self.streaming_out_template:
            self.streaming_out_template.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.streaming_out_template is not None:
            result['StreamingOutTemplate'] = self.streaming_out_template.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('StreamingOutTemplate') is not None:
            temp_model = main_models.ModifyAppStreamingOutTemplateRequestStreamingOutTemplate()
            self.streaming_out_template = temp_model.from_map(m.get('StreamingOutTemplate'))

        return self

class ModifyAppStreamingOutTemplateRequestStreamingOutTemplate(DaraModel):
    def __init__(
        self,
        layout_ids: List[str] = None,
        media_encode: int = None,
        name: str = None,
        template_id: str = None,
    ):
        # This parameter is required.
        self.layout_ids = layout_ids
        # This parameter is required.
        self.media_encode = media_encode
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.layout_ids is not None:
            result['LayoutIds'] = self.layout_ids

        if self.media_encode is not None:
            result['MediaEncode'] = self.media_encode

        if self.name is not None:
            result['Name'] = self.name

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LayoutIds') is not None:
            self.layout_ids = m.get('LayoutIds')

        if m.get('MediaEncode') is not None:
            self.media_encode = m.get('MediaEncode')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

