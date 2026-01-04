# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ConfigLayer4RemarkRequest(DaraModel):
    def __init__(
        self,
        listeners: str = None,
    ):
        # The port forwarding rule that you want to manage.
        # 
        # This parameter is a string that consists of JSON arrays. Each element in a JSON array indicates a port forwarding rule. You can perform this operation only on one port forwarding rule at a time.
        # 
        # > You can call the [DescribeNetworkRules](https://help.aliyun.com/document_detail/157484.html) to query existing port forwarding rules.
        # 
        # Each port forwarding rule contains the following fields:
        # 
        # *   **InstanceId**: the ID of the instance. This field is required and must be of the STRING type.
        # *   **Protocol**: the forwarding protocol. This field is required and must be of the STRING type. Valid values: **tcp** and **udp**.
        # *   **FrontendPort**: the forwarding port. This field is required and must be of the INTEGER type.
        # *   **Remark**: the remarks of the port forwarding rule. This field is required and must be of the STRING type. The value can contain letters, digits, and some special characters, such as `, . + - * / _`. The value can be up to 200 characters in length.
        # 
        # This parameter is required.
        self.listeners = listeners

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.listeners is not None:
            result['Listeners'] = self.listeners

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Listeners') is not None:
            self.listeners = m.get('Listeners')

        return self

