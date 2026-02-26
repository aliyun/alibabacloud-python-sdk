# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class HeadPose(DaraModel):
    def __init__(
        self,
        pitch: float = None,
        roll: float = None,
        yaw: float = None,
    ):
        # The angel of elevation or depression of the head. Unit: degree. Valid values: -180 to 180. A recommended range for reliable results is from -30 to 30.
        self.pitch = pitch
        # The angle of the tilt to the side. Unit: degree. Valid values: -180 to 180. A recommended range for reliable results is from -45 to 45.
        self.roll = roll
        # The angle of leftward or rightward rotation of the head. Unit: degree. Valid values: -180 to 180. A recommended range for reliable results is from -80 to 80.
        self.yaw = yaw

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.pitch is not None:
            result['Pitch'] = self.pitch

        if self.roll is not None:
            result['Roll'] = self.roll

        if self.yaw is not None:
            result['Yaw'] = self.yaw

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Pitch') is not None:
            self.pitch = m.get('Pitch')

        if m.get('Roll') is not None:
            self.roll = m.get('Roll')

        if m.get('Yaw') is not None:
            self.yaw = m.get('Yaw')

        return self

