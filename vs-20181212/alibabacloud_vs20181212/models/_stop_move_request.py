# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StopMoveRequest(DaraModel):
    def __init__(
        self,
        id: str = None,
        owner_id: int = None,
        pan: bool = None,
        tilt: bool = None,
        zoom: bool = None,
    ):
        # The device ID.
        # 
        # This parameter is required.
        self.id = id
        self.owner_id = owner_id
        # Specifies whether to stop panning. The default value is false.
        self.pan = pan
        # Specifies whether to stop tilting. The default value is false.
        self.tilt = tilt
        # Specifies whether to stop zooming. The default value is false.
        self.zoom = zoom

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.pan is not None:
            result['Pan'] = self.pan

        if self.tilt is not None:
            result['Tilt'] = self.tilt

        if self.zoom is not None:
            result['Zoom'] = self.zoom

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Pan') is not None:
            self.pan = m.get('Pan')

        if m.get('Tilt') is not None:
            self.tilt = m.get('Tilt')

        if m.get('Zoom') is not None:
            self.zoom = m.get('Zoom')

        return self

