# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_mts20140618 import models as main_models
from darabonba.model import DaraModel

class AddWaterMarkTemplateResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        water_mark_template: main_models.AddWaterMarkTemplateResponseBodyWaterMarkTemplate = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The details of the watermark template.
        self.water_mark_template = water_mark_template

    def validate(self):
        if self.water_mark_template:
            self.water_mark_template.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.water_mark_template is not None:
            result['WaterMarkTemplate'] = self.water_mark_template.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('WaterMarkTemplate') is not None:
            temp_model = main_models.AddWaterMarkTemplateResponseBodyWaterMarkTemplate()
            self.water_mark_template = temp_model.from_map(m.get('WaterMarkTemplate'))

        return self

class AddWaterMarkTemplateResponseBodyWaterMarkTemplate(DaraModel):
    def __init__(
        self,
        dx: str = None,
        dy: str = None,
        height: str = None,
        id: str = None,
        name: str = None,
        ratio_refer: main_models.AddWaterMarkTemplateResponseBodyWaterMarkTemplateRatioRefer = None,
        refer_pos: str = None,
        state: str = None,
        timeline: main_models.AddWaterMarkTemplateResponseBodyWaterMarkTemplateTimeline = None,
        type: str = None,
        width: str = None,
    ):
        # The horizontal offset. Unit: pixel.
        self.dx = dx
        # The vertical offset. Unit: pixel.
        self.dy = dy
        # The height of the watermark image. Unit: pixel.
        self.height = height
        # The ID of the watermark template. We recommend that you keep this ID for subsequent operation calls.
        self.id = id
        # The name of the watermark template.
        self.name = name
        # The values of the Height, Width, Dx, and Dy parameters relative to the reference edges. If the values of the Height, Width, Dx, and Dy parameters are decimals between 0 and 1, the values are calculated by referring to the following edges in sequence:
        # 
        # *   **Width**: the width edge.
        # *   **Height**: the height edge.
        # *   **Long**: the long edge.
        # *   **Short**: the short edge.
        self.ratio_refer = ratio_refer
        # The position of the watermark. Valid values:
        # 
        # *   **TopRight**: the upper-right corner.
        # *   **TopLeft**: the upper-left corner.
        # *   **BottomRight**: the lower-right corner.
        # *   **BottomLeft**: the lower-left corner.
        self.refer_pos = refer_pos
        # The status of the watermark template.
        # 
        # *   **Normal**: The watermark template is normal.
        # *   **Deleted**: The watermark template is deleted.
        self.state = state
        # The timeline of the watermark.
        self.timeline = timeline
        # The type of the watermark. Valid values:
        # 
        # *   Image: an image watermark.
        # *   Text: a text watermark.
        self.type = type
        # The width of the watermark image. Unit: pixel.
        self.width = width

    def validate(self):
        if self.ratio_refer:
            self.ratio_refer.validate()
        if self.timeline:
            self.timeline.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dx is not None:
            result['Dx'] = self.dx

        if self.dy is not None:
            result['Dy'] = self.dy

        if self.height is not None:
            result['Height'] = self.height

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.ratio_refer is not None:
            result['RatioRefer'] = self.ratio_refer.to_map()

        if self.refer_pos is not None:
            result['ReferPos'] = self.refer_pos

        if self.state is not None:
            result['State'] = self.state

        if self.timeline is not None:
            result['Timeline'] = self.timeline.to_map()

        if self.type is not None:
            result['Type'] = self.type

        if self.width is not None:
            result['Width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dx') is not None:
            self.dx = m.get('Dx')

        if m.get('Dy') is not None:
            self.dy = m.get('Dy')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RatioRefer') is not None:
            temp_model = main_models.AddWaterMarkTemplateResponseBodyWaterMarkTemplateRatioRefer()
            self.ratio_refer = temp_model.from_map(m.get('RatioRefer'))

        if m.get('ReferPos') is not None:
            self.refer_pos = m.get('ReferPos')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('Timeline') is not None:
            temp_model = main_models.AddWaterMarkTemplateResponseBodyWaterMarkTemplateTimeline()
            self.timeline = temp_model.from_map(m.get('Timeline'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

class AddWaterMarkTemplateResponseBodyWaterMarkTemplateTimeline(DaraModel):
    def __init__(
        self,
        duration: str = None,
        start: str = None,
    ):
        # The display duration of the watermark. Default value: **ToEND**. The default value indicates that the watermark is displayed until the video ends.
        self.duration = duration
        # The beginning of the time range during which the watermark is displayed.
        # 
        # *   Unit: seconds.
        # *   Default value: **0**.
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration is not None:
            result['Duration'] = self.duration

        if self.start is not None:
            result['Start'] = self.start

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('Start') is not None:
            self.start = m.get('Start')

        return self

class AddWaterMarkTemplateResponseBodyWaterMarkTemplateRatioRefer(DaraModel):
    def __init__(
        self,
        dx: str = None,
        dy: str = None,
        height: str = None,
        width: str = None,
    ):
        # The horizontal offset of the watermark relative to the output video image. Default value: **0**. The default value indicates no offset. The value can be an integer or a decimal.
        # 
        # *   **Integer**: the vertical offset. This indicates the absolute position. Unit: pixel.
        # *   **Decimal**: the ratio of the horizontal offset to the width of the output video. The ratio varies based on the size of the video. Four decimal places are supported, such as 0.9999. More decimal places are discarded.
        self.dx = dx
        # The vertical offset of the watermark relative to the output video image. Default value: **0**. The default value indicates no offset. The value can be an integer or a decimal.
        # 
        # *   **Integer**: the vertical offset. This indicates the absolute position. Unit: pixel.
        # *   **Decimal**: the ratio of the vertical offset to the height of the output video. The ratio varies based on the size of the video. Four decimal places are supported, such as 0.9999. More decimal places are discarded.
        self.dy = dy
        # The height of the watermark image in the output video. The value can be an integer or a decimal.
        # 
        # *   **Integer**: the height of the watermark image. This indicates the absolute position. Unit: pixel.
        # *   **Decimal**: the ratio of the height of the watermark image to the height of the output video. The ratio varies based on the size of the video. Four decimal places are supported, such as 0.9999. More decimal places are discarded.
        self.height = height
        # The width of the watermark image in the output video. The value can be an integer or a decimal.
        # 
        # *   **Integer**: the width of the watermark image. This indicates the absolute position. Unit: pixel.
        # *   **Decimal**: the ratio of the width of the watermark image to the width of the output video. The ratio varies based on the size of the video. Four decimal places are supported, such as 0.9999. More decimal places are discarded.
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dx is not None:
            result['Dx'] = self.dx

        if self.dy is not None:
            result['Dy'] = self.dy

        if self.height is not None:
            result['Height'] = self.height

        if self.width is not None:
            result['Width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dx') is not None:
            self.dx = m.get('Dx')

        if m.get('Dy') is not None:
            self.dy = m.get('Dy')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

