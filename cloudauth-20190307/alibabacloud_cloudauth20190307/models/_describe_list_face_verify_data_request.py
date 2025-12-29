# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeListFaceVerifyDataRequest(DaraModel):
    def __init__(
        self,
        gmt_end: int = None,
        gmt_start: int = None,
        name: str = None,
        scene_id: int = None,
    ):
        # End time of the query.
        self.gmt_end = gmt_end
        # Start time of the query.
        self.gmt_start = gmt_start
        # Product Code, currently deprecated.
        self.name = name
        # Scene ID.
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gmt_end is not None:
            result['GmtEnd'] = self.gmt_end

        if self.gmt_start is not None:
            result['GmtStart'] = self.gmt_start

        if self.name is not None:
            result['Name'] = self.name

        if self.scene_id is not None:
            result['SceneId'] = self.scene_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtEnd') is not None:
            self.gmt_end = m.get('GmtEnd')

        if m.get('GmtStart') is not None:
            self.gmt_start = m.get('GmtStart')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')

        return self

