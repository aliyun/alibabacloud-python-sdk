# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class LoginStateInfo(DaraModel):
    def __init__(
        self,
        scene_code: str = None,
        third_user_identifier: str = None,
        third_user_type: str = None,
        user_id: str = None,
    ):
        self.scene_code = scene_code
        self.third_user_identifier = third_user_identifier
        self.third_user_type = third_user_type
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.scene_code is not None:
            result['SceneCode'] = self.scene_code

        if self.third_user_identifier is not None:
            result['ThirdUserIdentifier'] = self.third_user_identifier

        if self.third_user_type is not None:
            result['ThirdUserType'] = self.third_user_type

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SceneCode') is not None:
            self.scene_code = m.get('SceneCode')

        if m.get('ThirdUserIdentifier') is not None:
            self.third_user_identifier = m.get('ThirdUserIdentifier')

        if m.get('ThirdUserType') is not None:
            self.third_user_type = m.get('ThirdUserType')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

