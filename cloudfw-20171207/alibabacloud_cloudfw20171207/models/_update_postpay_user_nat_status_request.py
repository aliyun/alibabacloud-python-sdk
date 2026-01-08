# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdatePostpayUserNatStatusRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        lang: str = None,
        operate: str = None,
    ):
        # The instance ID of Cloud Firewall.
        self.instance_id = instance_id
        # The language of the content within the response. Valid values:
        # 
        # *   **zh** (default)
        # *   **en**
        self.lang = lang
        # The operation type.
        # 
        # *   Set the value to open.
        self.operate = operate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.operate is not None:
            result['Operate'] = self.operate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Operate') is not None:
            self.operate = m.get('Operate')

        return self

