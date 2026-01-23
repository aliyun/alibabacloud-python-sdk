# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cr20181201 import models as main_models
from darabonba.model import DaraModel

class GetStorageDomainRoutingRuleResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        create_time: int = None,
        modify_time: int = None,
        request_id: str = None,
        routes: List[main_models.RouteItem] = None,
        rule_id: str = None,
        success: bool = None,
    ):
        # The return value.
        self.code = code
        # The creation time.
        self.create_time = create_time
        # The modification time.
        self.modify_time = modify_time
        # The request ID.
        self.request_id = request_id
        # The routing list.
        self.routes = routes
        # The rule ID.
        self.rule_id = rule_id
        # Indicates whether the request is successful.
        self.success = success

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
        if self.code is not None:
            result['Code'] = self.code

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Routes'] = []
        if self.routes is not None:
            for k1 in self.routes:
                result['Routes'].append(k1.to_map() if k1 else None)

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.routes = []
        if m.get('Routes') is not None:
            for k1 in m.get('Routes'):
                temp_model = main_models.RouteItem()
                self.routes.append(temp_model.from_map(k1))

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

