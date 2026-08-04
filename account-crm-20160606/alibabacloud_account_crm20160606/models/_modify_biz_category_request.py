# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyBizCategoryRequest(DaraModel):
    def __init__(
        self,
        param_list: str = None,
        user_id: int = None,
    ):
        # This parameter is required.
        self.param_list = param_list
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.param_list is not None:
            result['ParamList'] = self.param_list

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParamList') is not None:
            self.param_list = m.get('ParamList')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

