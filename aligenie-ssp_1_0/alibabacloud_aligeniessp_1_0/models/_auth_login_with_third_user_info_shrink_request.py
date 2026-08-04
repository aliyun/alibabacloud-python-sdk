# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AuthLoginWithThirdUserInfoShrinkRequest(DaraModel):
    def __init__(
        self,
        ext_info_shrink: str = None,
        scene_code: str = None,
        third_user_identifier: str = None,
        third_user_type: str = None,
    ):
        # Extension information
        self.ext_info_shrink = ext_info_shrink
        # Scene code, which must be requested from Tmall Genie in advance
        # 
        # This parameter is required.
        self.scene_code = scene_code
        # Third-party User Identifier
        # 
        # This parameter is required.
        self.third_user_identifier = third_user_identifier
        # Third-party User Type
        # 
        # This parameter is required.
        self.third_user_type = third_user_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ext_info_shrink is not None:
            result['ExtInfo'] = self.ext_info_shrink

        if self.scene_code is not None:
            result['SceneCode'] = self.scene_code

        if self.third_user_identifier is not None:
            result['ThirdUserIdentifier'] = self.third_user_identifier

        if self.third_user_type is not None:
            result['ThirdUserType'] = self.third_user_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtInfo') is not None:
            self.ext_info_shrink = m.get('ExtInfo')

        if m.get('SceneCode') is not None:
            self.scene_code = m.get('SceneCode')

        if m.get('ThirdUserIdentifier') is not None:
            self.third_user_identifier = m.get('ThirdUserIdentifier')

        if m.get('ThirdUserType') is not None:
            self.third_user_type = m.get('ThirdUserType')

        return self

