# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreatePipelineRequest(DaraModel):
    def __init__(
        self,
        name: str = None,
        priority: int = None,
        speed: str = None,
    ):
        # The name of the MPS queue.
        # 
        # This parameter is required.
        self.name = name
        # The priority. Default value: 6. Valid values: 1 to 10. A greater value specifies a higher priority.
        self.priority = priority
        # The type of the MPS queue. Valid values:
        # 
        # 1.  Standard: standard MPS queue.
        # 2.  Boost: MPS queue with transcoding speed boosted.
        # 3.  NarrowBandHDV2: MPS queue that supports Narrowband HD 2.0.
        # 
        # This parameter is required.
        self.speed = speed

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.speed is not None:
            result['Speed'] = self.speed

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('Speed') is not None:
            self.speed = m.get('Speed')

        return self

