# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rtc20180111 import models as main_models
from darabonba.model import DaraModel

class DescribeSystemLayoutListResponseBody(DaraModel):
    def __init__(
        self,
        layouts: main_models.DescribeSystemLayoutListResponseBodyLayouts = None,
        request_id: str = None,
        total_num: int = None,
        total_page: int = None,
    ):
        self.layouts = layouts
        self.request_id = request_id
        self.total_num = total_num
        self.total_page = total_page

    def validate(self):
        if self.layouts:
            self.layouts.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.layouts is not None:
            result['Layouts'] = self.layouts.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_num is not None:
            result['TotalNum'] = self.total_num

        if self.total_page is not None:
            result['TotalPage'] = self.total_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Layouts') is not None:
            temp_model = main_models.DescribeSystemLayoutListResponseBodyLayouts()
            self.layouts = temp_model.from_map(m.get('Layouts'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')

        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')

        return self

class DescribeSystemLayoutListResponseBodyLayouts(DaraModel):
    def __init__(
        self,
        layout: List[main_models.DescribeSystemLayoutListResponseBodyLayoutsLayout] = None,
    ):
        self.layout = layout

    def validate(self):
        if self.layout:
            for v1 in self.layout:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Layout'] = []
        if self.layout is not None:
            for k1 in self.layout:
                result['Layout'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.layout = []
        if m.get('Layout') is not None:
            for k1 in m.get('Layout'):
                temp_model = main_models.DescribeSystemLayoutListResponseBodyLayoutsLayout()
                self.layout.append(temp_model.from_map(k1))

        return self

class DescribeSystemLayoutListResponseBodyLayoutsLayout(DaraModel):
    def __init__(
        self,
        audio_mix_count: int = None,
        layout_id: int = None,
        name: str = None,
        panes: main_models.DescribeSystemLayoutListResponseBodyLayoutsLayoutPanes = None,
    ):
        self.audio_mix_count = audio_mix_count
        self.layout_id = layout_id
        self.name = name
        self.panes = panes

    def validate(self):
        if self.panes:
            self.panes.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audio_mix_count is not None:
            result['AudioMixCount'] = self.audio_mix_count

        if self.layout_id is not None:
            result['LayoutId'] = self.layout_id

        if self.name is not None:
            result['Name'] = self.name

        if self.panes is not None:
            result['Panes'] = self.panes.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AudioMixCount') is not None:
            self.audio_mix_count = m.get('AudioMixCount')

        if m.get('LayoutId') is not None:
            self.layout_id = m.get('LayoutId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Panes') is not None:
            temp_model = main_models.DescribeSystemLayoutListResponseBodyLayoutsLayoutPanes()
            self.panes = temp_model.from_map(m.get('Panes'))

        return self

class DescribeSystemLayoutListResponseBodyLayoutsLayoutPanes(DaraModel):
    def __init__(
        self,
        panes: List[main_models.DescribeSystemLayoutListResponseBodyLayoutsLayoutPanesPanes] = None,
    ):
        self.panes = panes

    def validate(self):
        if self.panes:
            for v1 in self.panes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Panes'] = []
        if self.panes is not None:
            for k1 in self.panes:
                result['Panes'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.panes = []
        if m.get('Panes') is not None:
            for k1 in m.get('Panes'):
                temp_model = main_models.DescribeSystemLayoutListResponseBodyLayoutsLayoutPanesPanes()
                self.panes.append(temp_model.from_map(k1))

        return self

class DescribeSystemLayoutListResponseBodyLayoutsLayoutPanesPanes(DaraModel):
    def __init__(
        self,
        height: float = None,
        major_pane: int = None,
        pane_id: int = None,
        width: float = None,
        x: float = None,
        y: float = None,
        zorder: int = None,
    ):
        self.height = height
        self.major_pane = major_pane
        self.pane_id = pane_id
        self.width = width
        self.x = x
        self.y = y
        self.zorder = zorder

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.height is not None:
            result['Height'] = self.height

        if self.major_pane is not None:
            result['MajorPane'] = self.major_pane

        if self.pane_id is not None:
            result['PaneId'] = self.pane_id

        if self.width is not None:
            result['Width'] = self.width

        if self.x is not None:
            result['X'] = self.x

        if self.y is not None:
            result['Y'] = self.y

        if self.zorder is not None:
            result['ZOrder'] = self.zorder

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('MajorPane') is not None:
            self.major_pane = m.get('MajorPane')

        if m.get('PaneId') is not None:
            self.pane_id = m.get('PaneId')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        if m.get('X') is not None:
            self.x = m.get('X')

        if m.get('Y') is not None:
            self.y = m.get('Y')

        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')

        return self

