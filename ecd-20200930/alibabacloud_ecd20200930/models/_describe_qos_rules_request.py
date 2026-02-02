# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeQosRulesRequest(DaraModel):
    def __init__(
        self,
        network_package_id: str = None,
        qos_rule_name: str = None,
    ):
        # This parameter is required.
        self.network_package_id = network_package_id
        self.qos_rule_name = qos_rule_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.network_package_id is not None:
            result['NetworkPackageId'] = self.network_package_id

        if self.qos_rule_name is not None:
            result['QosRuleName'] = self.qos_rule_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkPackageId') is not None:
            self.network_package_id = m.get('NetworkPackageId')

        if m.get('QosRuleName') is not None:
            self.qos_rule_name = m.get('QosRuleName')

        return self

