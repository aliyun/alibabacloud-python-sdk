# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateProcessDefinitionShrinkRequest(DaraModel):
    def __init__(
        self,
        approval_nodes_shrink: str = None,
        client_token: str = None,
        description: str = None,
        enabled: bool = None,
        name: str = None,
        notification_services_shrink: str = None,
        rule_conditions_shrink: str = None,
        sub_type: str = None,
        type: str = None,
    ):
        # This parameter is required.
        self.approval_nodes_shrink = approval_nodes_shrink
        self.client_token = client_token
        # This parameter is required.
        self.description = description
        self.enabled = enabled
        # This parameter is required.
        self.name = name
        self.notification_services_shrink = notification_services_shrink
        # This parameter is required.
        self.rule_conditions_shrink = rule_conditions_shrink
        self.sub_type = sub_type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.approval_nodes_shrink is not None:
            result['ApprovalNodes'] = self.approval_nodes_shrink

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.name is not None:
            result['Name'] = self.name

        if self.notification_services_shrink is not None:
            result['NotificationServices'] = self.notification_services_shrink

        if self.rule_conditions_shrink is not None:
            result['RuleConditions'] = self.rule_conditions_shrink

        if self.sub_type is not None:
            result['SubType'] = self.sub_type

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApprovalNodes') is not None:
            self.approval_nodes_shrink = m.get('ApprovalNodes')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NotificationServices') is not None:
            self.notification_services_shrink = m.get('NotificationServices')

        if m.get('RuleConditions') is not None:
            self.rule_conditions_shrink = m.get('RuleConditions')

        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

