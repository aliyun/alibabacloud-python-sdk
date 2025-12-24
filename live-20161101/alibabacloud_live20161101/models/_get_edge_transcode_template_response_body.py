# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class GetEdgeTranscodeTemplateResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        template: main_models.GetEdgeTranscodeTemplateResponseBodyTemplate = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The details of the edge transcoding template.
        self.template = template

    def validate(self):
        if self.template:
            self.template.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.template is not None:
            result['Template'] = self.template.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Template') is not None:
            temp_model = main_models.GetEdgeTranscodeTemplateResponseBodyTemplate()
            self.template = temp_model.from_map(m.get('Template'))

        return self

class GetEdgeTranscodeTemplateResponseBodyTemplate(DaraModel):
    def __init__(
        self,
        bitrate: str = None,
        codec: str = None,
        create_time: str = None,
        fps: str = None,
        gop: str = None,
        name: str = None,
        resolution: str = None,
        template_id: str = None,
        type: str = None,
    ):
        # The bitrate. If a numeric value is returned, a fixed bitrate is configured for the output stream. If ws is returned, the output stream maintains the same bitrate as the input stream.
        self.bitrate = bitrate
        # The video encoding format. Valid values:
        # 
        # *   H.264
        # *   H.265
        self.codec = codec
        # The time when the template was created.
        self.create_time = create_time
        # The frame rate. If a numeric value is returned, a fixed frame rate is configured for the output stream. If ws is returned, the output stream maintains the same frame rate as the input stream.
        self.fps = fps
        # The group of pictures (GOP) size. The GOP size can be defined by the number of frames or the time interval between I-frames. If ws is returned, the output stream maintains the same GOP size as the input stream.
        self.gop = gop
        # The template name.
        self.name = name
        # The resolution. If width and height values are returned, a fixed resolution is configured for the output stream. If ws is returned, the output stream maintains the same resolution as the input stream.
        # 
        # >  If the width value is -1, the width of the output stream is adapted to the height. If the height value is -2, the height of the output stream is adapted to the width.
        self.resolution = resolution
        # The template ID.
        self.template_id = template_id
        # The type of edge transcoding.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate

        if self.codec is not None:
            result['Codec'] = self.codec

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.fps is not None:
            result['Fps'] = self.fps

        if self.gop is not None:
            result['Gop'] = self.gop

        if self.name is not None:
            result['Name'] = self.name

        if self.resolution is not None:
            result['Resolution'] = self.resolution

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')

        if m.get('Codec') is not None:
            self.codec = m.get('Codec')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Fps') is not None:
            self.fps = m.get('Fps')

        if m.get('Gop') is not None:
            self.gop = m.get('Gop')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Resolution') is not None:
            self.resolution = m.get('Resolution')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

