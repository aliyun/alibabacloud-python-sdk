# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class LabelBuildRequest(DaraModel):
    def __init__(
        self,
        mode: str = None,
        model_style: str = None,
        optimize_wall_width: str = None,
        plan_style: str = None,
        scene_id: str = None,
        wall_height: int = None,
    ):
        self.mode = mode
        self.model_style = model_style
        self.optimize_wall_width = optimize_wall_width
        self.plan_style = plan_style
        # This parameter is required.
        self.scene_id = scene_id
        self.wall_height = wall_height

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mode is not None:
            result['Mode'] = self.mode

        if self.model_style is not None:
            result['ModelStyle'] = self.model_style

        if self.optimize_wall_width is not None:
            result['OptimizeWallWidth'] = self.optimize_wall_width

        if self.plan_style is not None:
            result['PlanStyle'] = self.plan_style

        if self.scene_id is not None:
            result['SceneId'] = self.scene_id

        if self.wall_height is not None:
            result['WallHeight'] = self.wall_height

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('ModelStyle') is not None:
            self.model_style = m.get('ModelStyle')

        if m.get('OptimizeWallWidth') is not None:
            self.optimize_wall_width = m.get('OptimizeWallWidth')

        if m.get('PlanStyle') is not None:
            self.plan_style = m.get('PlanStyle')

        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')

        if m.get('WallHeight') is not None:
            self.wall_height = m.get('WallHeight')

        return self

