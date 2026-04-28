# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class AppAccessStrategy(DaraModel):
    def __init__(
        self,
        effect: str = None,
        except_app_id_list: List[str] = None,
    ):
        # The global access policy of the application. Valid values:
        # 
        # *   allow: The domain allows access from all applications.
        # *   deny: The domain denies access from all apps. This is the default value.
        # 
        # Recommended settings:
        # 
        # 1.  Set effect to deny.
        # 2.  Specify except_app_id_list to allow specific applications to access the domain. Example: ["appid1", "appid2"].
        self.effect = effect
        # The IDs of applications excluded from the global access policy.
        # 
        # *   If you set effect to allow, which indicates that the domain allows access from all applications, the applications specified by this parameter value cannot access the domain.
        # *   If you set effect to deny, which indicates that the domain denies access from all applications, the applications specified by this parameter value can access the domain.
        self.except_app_id_list = except_app_id_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.effect is not None:
            result['effect'] = self.effect

        if self.except_app_id_list is not None:
            result['except_app_id_list'] = self.except_app_id_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('effect') is not None:
            self.effect = m.get('effect')

        if m.get('except_app_id_list') is not None:
            self.except_app_id_list = m.get('except_app_id_list')

        return self

