# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModelRouterBatchBindModelGroupRequest(DaraModel):
    def __init__(
        self,
        allowed_model_group_config: str = None,
        client_id_list: List[int] = None,
    ):
        # The authorization configuration (JSON string). Internal key names use a fixed underscore style: {"model_ids":[...],"group_ids":["mg_xxx"]}
        # 
        # This parameter is required.
        self.allowed_model_group_config = allowed_model_group_config
        # The array of department IDs. You can specify 1 to 50 IDs. If more than 50, call this operation in batches.
        # 
        # This parameter is required.
        self.client_id_list = client_id_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allowed_model_group_config is not None:
            result['allowedModelGroupConfig'] = self.allowed_model_group_config

        if self.client_id_list is not None:
            result['clientIdList'] = self.client_id_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('allowedModelGroupConfig') is not None:
            self.allowed_model_group_config = m.get('allowedModelGroupConfig')

        if m.get('clientIdList') is not None:
            self.client_id_list = m.get('clientIdList')

        return self

