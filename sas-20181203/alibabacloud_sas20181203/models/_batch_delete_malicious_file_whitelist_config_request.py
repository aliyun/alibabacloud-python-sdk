# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class BatchDeleteMaliciousFileWhitelistConfigRequest(DaraModel):
    def __init__(
        self,
        config_id_list: List[int] = None,
    ):
        # The IDs of the whitelist rules. You can call the [ListMaliciousFileWhitelistConfigs](~~ListMaliciousFileWhitelistConfigs~~) operation to query the IDs of whitelist rules.
        self.config_id_list = config_id_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_id_list is not None:
            result['ConfigIdList'] = self.config_id_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigIdList') is not None:
            self.config_id_list = m.get('ConfigIdList')

        return self

