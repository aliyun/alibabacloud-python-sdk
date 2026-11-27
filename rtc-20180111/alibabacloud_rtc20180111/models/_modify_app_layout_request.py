# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rtc20180111 import models as main_models
from darabonba.model import DaraModel

class ModifyAppLayoutRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        client_token: str = None,
        layout: main_models.ModifyAppLayoutRequestLayout = None,
    ):
        # Application ID. Create and query through the console. Only a single ID is supported.
        # 
        # This parameter is required.
        self.app_id = app_id
        # Idempotent parameter.
        self.client_token = client_token
        # Layout.
        # 
        # This parameter is required.
        self.layout = layout

    def validate(self):
        if self.layout:
            self.layout.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.layout is not None:
            result['Layout'] = self.layout.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Layout') is not None:
            temp_model = main_models.ModifyAppLayoutRequestLayout()
            self.layout = temp_model.from_map(m.get('Layout'))

        return self

class ModifyAppLayoutRequestLayout(DaraModel):
    def __init__(
        self,
        layout_id: str = None,
        name: str = None,
        panes: List[main_models.ModifyAppLayoutRequestLayoutPanes] = None,
    ):
        # Layout ID.
        # 
        # This parameter is required.
        self.layout_id = layout_id
        # Layout name.
        # 
        # This parameter is required.
        self.name = name
        # List of panes.
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
        if self.layout_id is not None:
            result['LayoutId'] = self.layout_id

        if self.name is not None:
            result['Name'] = self.name

        result['Panes'] = []
        if self.panes is not None:
            for k1 in self.panes:
                result['Panes'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LayoutId') is not None:
            self.layout_id = m.get('LayoutId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.panes = []
        if m.get('Panes') is not None:
            for k1 in m.get('Panes'):
                temp_model = main_models.ModifyAppLayoutRequestLayoutPanes()
                self.panes.append(temp_model.from_map(k1))

        return self

class ModifyAppLayoutRequestLayoutPanes(DaraModel):
    def __init__(
        self,
        height: float = None,
        pane_id: int = None,
        width: float = None,
        x: float = None,
        y: float = None,
        zorder: int = None,
    ):
        # Pane height, normalized percentage. Height ranges from 0.0\<Height≤1.0.
        self.height = height
        # Pane ID, starting from 0.
        self.pane_id = pane_id
        # Pane width, normalized percentage. Width ranges from 0.0\<Width≤1.0.
        self.width = width
        # X coordinate, normalized percentage. The X coordinate ranges from 0.0 to 1.0.
        self.x = x
        # Y coordinate, normalized percentage. The Y coordinate ranges from 0.0 to 1.0.
        self.y = y
        # Stacking order. 0 is the bottom layer, 1 is above 0, and so on.
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

