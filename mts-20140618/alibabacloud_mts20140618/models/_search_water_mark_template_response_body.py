# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mts20140618 import models as main_models
from darabonba.model import DaraModel

class SearchWaterMarkTemplateResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        water_mark_template_list: main_models.SearchWaterMarkTemplateResponseBodyWaterMarkTemplateList = None,
    ):
        # The width of the watermark image in the output video. The value can be an integer or a decimal.
        # 
        # *   **Integer**: the width of the watermark image. This indicates the absolute position. Unit: pixel.
        # *   **Decimal**: the ratio of the width of the watermark image to the width of the output video. The ratio varies based on the size of the video. Four decimal places are supported, such as 0.9999. More decimal places are discarded.
        self.page_number = page_number
        # The values of the Height, Width, Dx, and Dy parameters relative to the reference edges. If the values of the Height, Width, Dx, and Dy parameters are decimals between 0 and 1, the values are calculated by referring to the following edges in sequence:
        # 
        # *   **Width**: the width edge.
        # *   **Height**: the height edge.
        # *   **Long**: the long edge.
        # *   **Short**: the short edge.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The type of the watermark. Valid values:
        # 
        # *   Image: an image watermark.
        # *   Text: a text watermark.
        # 
        # >  Only watermarks of the **Image** types are supported.
        self.total_count = total_count
        self.water_mark_template_list = water_mark_template_list

    def validate(self):
        if self.water_mark_template_list:
            self.water_mark_template_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.water_mark_template_list is not None:
            result['WaterMarkTemplateList'] = self.water_mark_template_list.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('WaterMarkTemplateList') is not None:
            temp_model = main_models.SearchWaterMarkTemplateResponseBodyWaterMarkTemplateList()
            self.water_mark_template_list = temp_model.from_map(m.get('WaterMarkTemplateList'))

        return self

class SearchWaterMarkTemplateResponseBodyWaterMarkTemplateList(DaraModel):
    def __init__(
        self,
        water_mark_template: List[main_models.SearchWaterMarkTemplateResponseBodyWaterMarkTemplateListWaterMarkTemplate] = None,
    ):
        self.water_mark_template = water_mark_template

    def validate(self):
        if self.water_mark_template:
            for v1 in self.water_mark_template:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['WaterMarkTemplate'] = []
        if self.water_mark_template is not None:
            for k1 in self.water_mark_template:
                result['WaterMarkTemplate'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.water_mark_template = []
        if m.get('WaterMarkTemplate') is not None:
            for k1 in m.get('WaterMarkTemplate'):
                temp_model = main_models.SearchWaterMarkTemplateResponseBodyWaterMarkTemplateListWaterMarkTemplate()
                self.water_mark_template.append(temp_model.from_map(k1))

        return self

class SearchWaterMarkTemplateResponseBodyWaterMarkTemplateListWaterMarkTemplate(DaraModel):
    def __init__(
        self,
        dx: str = None,
        dy: str = None,
        height: str = None,
        id: str = None,
        name: str = None,
        ratio_refer: main_models.SearchWaterMarkTemplateResponseBodyWaterMarkTemplateListWaterMarkTemplateRatioRefer = None,
        refer_pos: str = None,
        state: str = None,
        timeline: main_models.SearchWaterMarkTemplateResponseBodyWaterMarkTemplateListWaterMarkTemplateTimeline = None,
        type: str = None,
        width: str = None,
    ):
        self.dx = dx
        self.dy = dy
        self.height = height
        self.id = id
        self.name = name
        self.ratio_refer = ratio_refer
        self.refer_pos = refer_pos
        self.state = state
        self.timeline = timeline
        self.type = type
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
            temp_model = main_models.SearchWaterMarkTemplateResponseBodyWaterMarkTemplateListWaterMarkTemplateRatioRefer()
            self.ratio_refer = temp_model.from_map(m.get('RatioRefer'))

        if m.get('ReferPos') is not None:
            self.refer_pos = m.get('ReferPos')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('Timeline') is not None:
            temp_model = main_models.SearchWaterMarkTemplateResponseBodyWaterMarkTemplateListWaterMarkTemplateTimeline()
            self.timeline = temp_model.from_map(m.get('Timeline'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

class SearchWaterMarkTemplateResponseBodyWaterMarkTemplateListWaterMarkTemplateTimeline(DaraModel):
    def __init__(
        self,
        duration: str = None,
        start: str = None,
    ):
        self.duration = duration
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

class SearchWaterMarkTemplateResponseBodyWaterMarkTemplateListWaterMarkTemplateRatioRefer(DaraModel):
    def __init__(
        self,
        dx: str = None,
        dy: str = None,
        height: str = None,
        width: str = None,
    ):
        self.dx = dx
        self.dy = dy
        self.height = height
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

