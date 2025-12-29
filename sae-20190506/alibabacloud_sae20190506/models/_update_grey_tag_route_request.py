# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateGreyTagRouteRequest(DaraModel):
    def __init__(
        self,
        alb_rules: str = None,
        description: str = None,
        dubbo_rules: str = None,
        grey_tag_route_id: int = None,
        sc_rules: str = None,
    ):
        # The canary release rule of the application for which ALB gateway routing is configured.
        self.alb_rules = alb_rules
        # The description of the canary release rule.
        self.description = description
        # The canary release rule of the Dubbo application.
        self.dubbo_rules = dubbo_rules
        # The ID of the canary release rule.
        # 
        # This parameter is required.
        self.grey_tag_route_id = grey_tag_route_id
        # The canary release rule of the Spring Cloud application.
        self.sc_rules = sc_rules

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alb_rules is not None:
            result['AlbRules'] = self.alb_rules

        if self.description is not None:
            result['Description'] = self.description

        if self.dubbo_rules is not None:
            result['DubboRules'] = self.dubbo_rules

        if self.grey_tag_route_id is not None:
            result['GreyTagRouteId'] = self.grey_tag_route_id

        if self.sc_rules is not None:
            result['ScRules'] = self.sc_rules

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlbRules') is not None:
            self.alb_rules = m.get('AlbRules')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DubboRules') is not None:
            self.dubbo_rules = m.get('DubboRules')

        if m.get('GreyTagRouteId') is not None:
            self.grey_tag_route_id = m.get('GreyTagRouteId')

        if m.get('ScRules') is not None:
            self.sc_rules = m.get('ScRules')

        return self

