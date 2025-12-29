# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from darabonba.model import DaraModel

class ModifyPolicyInstanceRequest(DaraModel):
    def __init__(
        self,
        action: str = None,
        instance_name: str = None,
        namespaces: List[str] = None,
        parameters: Dict[str, Any] = None,
    ):
        # The action of the policy. Valid values:
        # 
        # *   `deny`: Deployments that match the policy are denied.
        # *   `warn`: Alerts are generated for deployments that match the policy.
        self.action = action
        # The ID of the policy instance.
        self.instance_name = instance_name
        # The namespaces to which the policy is applied. The policy is applied to all namespaces if this parameter is left empty.
        self.namespaces = namespaces
        # The parameters of the policy instance. For more information, see [Predefined security policies of ACK](https://help.aliyun.com/document_detail/359819.html).
        self.parameters = parameters

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['action'] = self.action

        if self.instance_name is not None:
            result['instance_name'] = self.instance_name

        if self.namespaces is not None:
            result['namespaces'] = self.namespaces

        if self.parameters is not None:
            result['parameters'] = self.parameters

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')

        if m.get('instance_name') is not None:
            self.instance_name = m.get('instance_name')

        if m.get('namespaces') is not None:
            self.namespaces = m.get('namespaces')

        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')

        return self

