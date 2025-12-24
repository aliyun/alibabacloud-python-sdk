# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ApplyScalingGroupRequest(DaraModel):
    def __init__(
        self,
        content: str = None,
        format: str = None,
        region_id: str = None,
    ):
        # The content of the configuration file.
        # 
        # This parameter is required.
        self.content = content
        # Optional. The format of the configuration file. Default value: YAML. Set the value to YAML.
        self.format = format
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.format is not None:
            result['Format'] = self.format

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Format') is not None:
            self.format = m.get('Format')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

