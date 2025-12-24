# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLiveStreamWatermarksResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        total: int = None,
        watermark_list: main_models.DescribeLiveStreamWatermarksResponseBodyWatermarkList = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The total number of watermark templates that meet the specified conditions.
        self.total = total
        # Details of the watermark templates.
        self.watermark_list = watermark_list

    def validate(self):
        if self.watermark_list:
            self.watermark_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total is not None:
            result['Total'] = self.total

        if self.watermark_list is not None:
            result['WatermarkList'] = self.watermark_list.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        if m.get('WatermarkList') is not None:
            temp_model = main_models.DescribeLiveStreamWatermarksResponseBodyWatermarkList()
            self.watermark_list = temp_model.from_map(m.get('WatermarkList'))

        return self

class DescribeLiveStreamWatermarksResponseBodyWatermarkList(DaraModel):
    def __init__(
        self,
        watermark: List[main_models.DescribeLiveStreamWatermarksResponseBodyWatermarkListWatermark] = None,
    ):
        self.watermark = watermark

    def validate(self):
        if self.watermark:
            for v1 in self.watermark:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Watermark'] = []
        if self.watermark is not None:
            for k1 in self.watermark:
                result['Watermark'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.watermark = []
        if m.get('Watermark') is not None:
            for k1 in m.get('Watermark'):
                temp_model = main_models.DescribeLiveStreamWatermarksResponseBodyWatermarkListWatermark()
                self.watermark.append(temp_model.from_map(k1))

        return self

class DescribeLiveStreamWatermarksResponseBodyWatermarkListWatermark(DaraModel):
    def __init__(
        self,
        description: str = None,
        height: int = None,
        name: str = None,
        offset_corner: str = None,
        picture_url: str = None,
        ref_height: int = None,
        ref_width: int = None,
        rule_count: int = None,
        template_id: str = None,
        transparency: int = None,
        type: int = None,
        xoffset: float = None,
        yoffset: float = None,
    ):
        # The description of the watermark.
        self.description = description
        # The height of the watermark. Unit: pixels.
        self.height = height
        # The name of the watermark.
        self.name = name
        # The position of the watermark.
        # 
        # *   TopLeft: the upper-left corner.
        # *   TopRight: the upper-right corner.
        # *   BottomLeft: the lower-left corner.
        # *   BottomRight: the lower-right corner.
        self.offset_corner = offset_corner
        # The URL of the watermark image.
        self.picture_url = picture_url
        # The height of the background video. Unit: pixels.
        self.ref_height = ref_height
        # The width of the background video. Unit: pixels.
        self.ref_width = ref_width
        # The number of watermark rules configured for the domain name.
        self.rule_count = rule_count
        # The ID of the watermark template.
        self.template_id = template_id
        # The transparency of the watermark. A smaller value indicates a more transparent watermark. Valid values: 0 to 255.
        self.transparency = transparency
        # The watermark type.
        # 
        # *   0: image. Only image watermarks are supported.
        # *   1: text.
        self.type = type
        # The offset of the watermark along the x-axis. Unit: pixels.
        # 
        # >  The value of the RefWidth parameter is used as the reference. If the OffsetCorner parameter is set to TopLeft, the value of the XOffset parameter indicates the x-axis offset of the upper-left corner of the watermark relative to that of the background video. The directions from the coordinate axes to the center of the background video are positive. In other words, the x-axis is positive toward the right.
        self.xoffset = xoffset
        # The offset of the watermark along the y-axis. Unit: pixels.
        # 
        # >  The value of the RefHeight parameter is used as the reference. If the OffsetCorner parameter is set to TopLeft, the value of the YOffset parameter indicates the y-axis offset of the upper-left corner of the watermark relative to that of the background video. The directions from the coordinate axes to the center of the background video are positive. In other words, the y-axis is positive downward.
        self.yoffset = yoffset

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.height is not None:
            result['Height'] = self.height

        if self.name is not None:
            result['Name'] = self.name

        if self.offset_corner is not None:
            result['OffsetCorner'] = self.offset_corner

        if self.picture_url is not None:
            result['PictureUrl'] = self.picture_url

        if self.ref_height is not None:
            result['RefHeight'] = self.ref_height

        if self.ref_width is not None:
            result['RefWidth'] = self.ref_width

        if self.rule_count is not None:
            result['RuleCount'] = self.rule_count

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.transparency is not None:
            result['Transparency'] = self.transparency

        if self.type is not None:
            result['Type'] = self.type

        if self.xoffset is not None:
            result['XOffset'] = self.xoffset

        if self.yoffset is not None:
            result['YOffset'] = self.yoffset

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OffsetCorner') is not None:
            self.offset_corner = m.get('OffsetCorner')

        if m.get('PictureUrl') is not None:
            self.picture_url = m.get('PictureUrl')

        if m.get('RefHeight') is not None:
            self.ref_height = m.get('RefHeight')

        if m.get('RefWidth') is not None:
            self.ref_width = m.get('RefWidth')

        if m.get('RuleCount') is not None:
            self.rule_count = m.get('RuleCount')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('Transparency') is not None:
            self.transparency = m.get('Transparency')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('XOffset') is not None:
            self.xoffset = m.get('XOffset')

        if m.get('YOffset') is not None:
            self.yoffset = m.get('YOffset')

        return self

