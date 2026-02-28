# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rtc20180111 import models as main_models
from darabonba.model import DaraModel

class CreateAppViewTemplateRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        template: main_models.CreateAppViewTemplateRequestTemplate = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.template = template

    def validate(self):
        if self.template:
            self.template.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.template is not None:
            result['Template'] = self.template.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Template') is not None:
            temp_model = main_models.CreateAppViewTemplateRequestTemplate()
            self.template = temp_model.from_map(m.get('Template'))

        return self

class CreateAppViewTemplateRequestTemplate(DaraModel):
    def __init__(
        self,
        layout_ids: List[str] = None,
        media_encode: int = None,
        name: str = None,
    ):
        # This parameter is required.
        self.layout_ids = layout_ids
        # This parameter is required.
        self.media_encode = media_encode
        # This parameter is required.
        self.name = name

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LayoutIds') is not None:
            self.layout_ids = m.get('LayoutIds')

        if m.get('MediaEncode') is not None:
            self.media_encode = m.get('MediaEncode')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

