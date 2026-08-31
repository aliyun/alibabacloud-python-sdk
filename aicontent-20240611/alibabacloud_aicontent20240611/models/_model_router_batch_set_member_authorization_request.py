# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModelRouterBatchSetMemberAuthorizationRequest(DaraModel):
    def __init__(
        self,
        allowed_model_group_config: str = None,
        user_id_list: List[int] = None,
    ):
        # The authorization configuration. This parameter is a required JSON string and uses overwrite mode. Format: {"model_ids":[...],"group_ids":["mg_xxx"]}. Internal key names use a fixed underscore style and are not converted to the camelCase convention of the API.
        self.allowed_model_group_config = allowed_model_group_config
        # The list of user IDs. This parameter is required. You can specify 1 to 50 user IDs. If more than 50 user IDs are required, call this operation in batches. All specified users must be direct members of the department.
        self.user_id_list = user_id_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allowed_model_group_config is not None:
            result['allowedModelGroupConfig'] = self.allowed_model_group_config

        if self.user_id_list is not None:
            result['userIdList'] = self.user_id_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('allowedModelGroupConfig') is not None:
            self.allowed_model_group_config = m.get('allowedModelGroupConfig')

        if m.get('userIdList') is not None:
            self.user_id_list = m.get('userIdList')

        return self

