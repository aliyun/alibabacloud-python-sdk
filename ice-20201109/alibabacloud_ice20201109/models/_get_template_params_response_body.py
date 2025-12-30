# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class GetTemplateParamsResponseBody(DaraModel):
    def __init__(
        self,
        param_list: List[main_models.GetTemplateParamsResponseBodyParamList] = None,
        request_id: str = None,
        template_id: str = None,
    ):
        # The queried parameters.
        self.param_list = param_list
        # The request ID.
        self.request_id = request_id
        # The template ID.
        self.template_id = template_id

    def validate(self):
        if self.param_list:
            for v1 in self.param_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ParamList'] = []
        if self.param_list is not None:
            for k1 in self.param_list:
                result['ParamList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.param_list = []
        if m.get('ParamList') is not None:
            for k1 in m.get('ParamList'):
                temp_model = main_models.GetTemplateParamsResponseBodyParamList()
                self.param_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

class GetTemplateParamsResponseBodyParamList(DaraModel):
    def __init__(
        self,
        content: str = None,
        cover_url: str = None,
        height: int = None,
        key: str = None,
        media_url: str = None,
        timeline_in: float = None,
        timeline_out: float = None,
        type: str = None,
        width: int = None,
        x: int = None,
        y: int = None,
    ):
        # The original subtitle content.
        self.content = content
        # The thumbnail URL of the original material.
        self.cover_url = cover_url
        self.height = height
        # The parameter name.
        self.key = key
        # The URL of the original material.
        self.media_url = media_url
        self.timeline_in = timeline_in
        self.timeline_out = timeline_out
        # The material type.
        # 
        # Valid values:
        # 
        # *   Video
        # *   Text
        # *   Image
        self.type = type
        self.width = width
        self.x = x
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url

        if self.height is not None:
            result['Height'] = self.height

        if self.key is not None:
            result['Key'] = self.key

        if self.media_url is not None:
            result['MediaUrl'] = self.media_url

        if self.timeline_in is not None:
            result['TimelineIn'] = self.timeline_in

        if self.timeline_out is not None:
            result['TimelineOut'] = self.timeline_out

        if self.type is not None:
            result['Type'] = self.type

        if self.width is not None:
            result['Width'] = self.width

        if self.x is not None:
            result['X'] = self.x

        if self.y is not None:
            result['Y'] = self.y

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('MediaUrl') is not None:
            self.media_url = m.get('MediaUrl')

        if m.get('TimelineIn') is not None:
            self.timeline_in = m.get('TimelineIn')

        if m.get('TimelineOut') is not None:
            self.timeline_out = m.get('TimelineOut')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        if m.get('X') is not None:
            self.x = m.get('X')

        if m.get('Y') is not None:
            self.y = m.get('Y')

        return self

