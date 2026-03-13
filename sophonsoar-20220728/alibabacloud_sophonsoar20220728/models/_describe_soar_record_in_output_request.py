# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSoarRecordInOutputRequest(DaraModel):
    def __init__(
        self,
        action_uuid: str = None,
        lang: str = None,
    ):
        # The UUID of the component action.
        # 
        # >  You can call the [DescribeSoarTaskAndActions](~~DescribeSoarTaskAndActions~~) operation to query the UUIDs of component actions.
        # 
        # This parameter is required.
        self.action_uuid = action_uuid
        # The language of the content within the request and the response. Valid values:
        # 
        # *   **zh** (default): Chinese
        # *   **en**: English
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_uuid is not None:
            result['ActionUuid'] = self.action_uuid

        if self.lang is not None:
            result['Lang'] = self.lang

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionUuid') is not None:
            self.action_uuid = m.get('ActionUuid')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        return self

