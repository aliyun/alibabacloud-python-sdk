# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class BatchQuerySessionByClientIdsRequest(DaraModel):
    def __init__(
        self,
        client_id_list: List[str] = None,
        instance_id: str = None,
    ):
        # The list of clients.
        # 
        # This parameter is required.
        self.client_id_list = client_id_list
        # The ID of the ApsaraMQ for MQTT instance. The ID must match the actual instance ID used by the client. You can obtain the ID on the **Instance Details** page in the [console](https://mqtt.console.aliyun.com).
        # 
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_id_list is not None:
            result['ClientIdList'] = self.client_id_list

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientIdList') is not None:
            self.client_id_list = m.get('ClientIdList')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

