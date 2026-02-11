# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ConfigAppRequest(DaraModel):
    def __init__(
        self,
        app_ids: str = None,
        enable: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.app_ids = app_ids
        self.enable = enable
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_ids is not None:
            result['AppIds'] = self.app_ids

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppIds') is not None:
            self.app_ids = m.get('AppIds')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

