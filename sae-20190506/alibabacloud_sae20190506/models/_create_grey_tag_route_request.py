# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateGreyTagRouteRequest(DaraModel):
    def __init__(
        self,
        alb_rules: str = None,
        app_id: str = None,
        description: str = None,
        dubbo_rules: str = None,
        name: str = None,
        sc_rules: str = None,
    ):
        # The canary release rule of the application for which Application Load Balancer (ALB) gateway routing is configured.
        self.alb_rules = alb_rules
        # The application ID.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The description of the canary release rule. The name must be 1 to 64 characters in length.
        self.description = description
        # The canary release rule that you created for Dubbo applications. If your application uses the Dubbo framework, you must configure this parameter. You do not need to configure the **ScRules** parameter.
        self.dubbo_rules = dubbo_rules
        # The name of the canary release rule. The name must start with a lowercase letter and end with a digit or a lowercase letter. The name can contain only lowercase letters, Chinese characters, digits, and hyphens (-). The name must be 1 to 64 characters in length.
        # 
        # This parameter is required.
        self.name = name
        # The canary release rule that you created for Spring Cloud application. If your application uses the Spring Cloud framework, you must configure this parameter. You do not need to configure the **DubboRules** parameter.
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

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.description is not None:
            result['Description'] = self.description

        if self.dubbo_rules is not None:
            result['DubboRules'] = self.dubbo_rules

        if self.name is not None:
            result['Name'] = self.name

        if self.sc_rules is not None:
            result['ScRules'] = self.sc_rules

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlbRules') is not None:
            self.alb_rules = m.get('AlbRules')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DubboRules') is not None:
            self.dubbo_rules = m.get('DubboRules')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ScRules') is not None:
            self.sc_rules = m.get('ScRules')

        return self

