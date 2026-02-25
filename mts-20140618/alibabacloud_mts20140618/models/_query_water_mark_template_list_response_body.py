# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mts20140618 import models as main_models
from darabonba.model import DaraModel

class QueryWaterMarkTemplateListResponseBody(DaraModel):
    def __init__(
        self,
        non_exist_wids: main_models.QueryWaterMarkTemplateListResponseBodyNonExistWids = None,
        request_id: str = None,
        water_mark_template_list: main_models.QueryWaterMarkTemplateListResponseBodyWaterMarkTemplateList = None,
    ):
        self.non_exist_wids = non_exist_wids
        # The ID of the request.
        self.request_id = request_id
        self.water_mark_template_list = water_mark_template_list

    def validate(self):
        if self.non_exist_wids:
            self.non_exist_wids.validate()
        if self.water_mark_template_list:
            self.water_mark_template_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.non_exist_wids is not None:
            result['NonExistWids'] = self.non_exist_wids.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.water_mark_template_list is not None:
            result['WaterMarkTemplateList'] = self.water_mark_template_list.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NonExistWids') is not None:
            temp_model = main_models.QueryWaterMarkTemplateListResponseBodyNonExistWids()
            self.non_exist_wids = temp_model.from_map(m.get('NonExistWids'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('WaterMarkTemplateList') is not None:
            temp_model = main_models.QueryWaterMarkTemplateListResponseBodyWaterMarkTemplateList()
            self.water_mark_template_list = temp_model.from_map(m.get('WaterMarkTemplateList'))

        return self

class QueryWaterMarkTemplateListResponseBodyWaterMarkTemplateList(DaraModel):
    def __init__(
        self,
        water_mark_template: List[main_models.QueryWaterMarkTemplateListResponseBodyWaterMarkTemplateListWaterMarkTemplate] = None,
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
                temp_model = main_models.QueryWaterMarkTemplateListResponseBodyWaterMarkTemplateListWaterMarkTemplate()
                self.water_mark_template.append(temp_model.from_map(k1))

        return self

class QueryWaterMarkTemplateListResponseBodyWaterMarkTemplateListWaterMarkTemplate(DaraModel):
    def __init__(
        self,
        dx: str = None,
        dy: str = None,
        height: str = None,
        id: str = None,
        name: str = None,
        ratio_refer: main_models.QueryWaterMarkTemplateListResponseBodyWaterMarkTemplateListWaterMarkTemplateRatioRefer = None,
        refer_pos: str = None,
        state: str = None,
        timeline: main_models.QueryWaterMarkTemplateListResponseBodyWaterMarkTemplateListWaterMarkTemplateTimeline = None,
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
            temp_model = main_models.QueryWaterMarkTemplateListResponseBodyWaterMarkTemplateListWaterMarkTemplateRatioRefer()
            self.ratio_refer = temp_model.from_map(m.get('RatioRefer'))

        if m.get('ReferPos') is not None:
            self.refer_pos = m.get('ReferPos')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('Timeline') is not None:
            temp_model = main_models.QueryWaterMarkTemplateListResponseBodyWaterMarkTemplateListWaterMarkTemplateTimeline()
            self.timeline = temp_model.from_map(m.get('Timeline'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

class QueryWaterMarkTemplateListResponseBodyWaterMarkTemplateListWaterMarkTemplateTimeline(DaraModel):
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

class QueryWaterMarkTemplateListResponseBodyWaterMarkTemplateListWaterMarkTemplateRatioRefer(DaraModel):
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

class QueryWaterMarkTemplateListResponseBodyNonExistWids(DaraModel):
    def __init__(
        self,
        string: List[str] = None,
    ):
        self.string = string

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.string is not None:
            result['String'] = self.string

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('String') is not None:
            self.string = m.get('String')

        return self

