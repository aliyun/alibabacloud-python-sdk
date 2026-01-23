# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cr20181201 import models as main_models
from darabonba.model import DaraModel

class UpdateStorageDomainRoutingRuleRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        routes: List[main_models.RouteItem] = None,
        rule_id: str = None,
    ):
        # The instance ID
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The route list
        # 
        # This parameter is required.
        self.routes = routes
        # The rule ID.
        # 
        # This parameter is required.
        self.rule_id = rule_id

    def validate(self):
        if self.routes:
            for v1 in self.routes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        result['Routes'] = []
        if self.routes is not None:
            for k1 in self.routes:
                result['Routes'].append(k1.to_map() if k1 else None)

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        self.routes = []
        if m.get('Routes') is not None:
            for k1 in m.get('Routes'):
                temp_model = main_models.RouteItem()
                self.routes.append(temp_model.from_map(k1))

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        return self

