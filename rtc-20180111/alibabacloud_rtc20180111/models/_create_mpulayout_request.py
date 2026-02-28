# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rtc20180111 import models as main_models
from darabonba.model import DaraModel

class CreateMPULayoutRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        audio_mix_count: int = None,
        name: str = None,
        owner_id: int = None,
        panes: List[main_models.CreateMPULayoutRequestPanes] = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.audio_mix_count = audio_mix_count
        self.name = name
        self.owner_id = owner_id
        # This parameter is required.
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
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.audio_mix_count is not None:
            result['AudioMixCount'] = self.audio_mix_count

        if self.name is not None:
            result['Name'] = self.name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        result['Panes'] = []
        if self.panes is not None:
            for k1 in self.panes:
                result['Panes'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AudioMixCount') is not None:
            self.audio_mix_count = m.get('AudioMixCount')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        self.panes = []
        if m.get('Panes') is not None:
            for k1 in m.get('Panes'):
                temp_model = main_models.CreateMPULayoutRequestPanes()
                self.panes.append(temp_model.from_map(k1))

        return self

class CreateMPULayoutRequestPanes(DaraModel):
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

