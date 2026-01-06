# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryRobotUnsubscriptionRequest(DaraModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        robot_code: str = None,
        scene_code: str = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.robot_code = robot_code
        self.scene_code = scene_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.robot_code is not None:
            result['RobotCode'] = self.robot_code

        if self.scene_code is not None:
            result['SceneCode'] = self.scene_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RobotCode') is not None:
            self.robot_code = m.get('RobotCode')

        if m.get('SceneCode') is not None:
            self.scene_code = m.get('SceneCode')

        return self

