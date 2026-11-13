# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateProcessDefinitionShrinkRequest(DaraModel):
    def __init__(
        self,
        approval_nodes_shrink: str = None,
        client_token: str = None,
        description: str = None,
        id: str = None,
        name: str = None,
        notification_services_shrink: str = None,
        rule_conditions_shrink: str = None,
    ):
        # The list of approval nodes. Note: System policies do not take effect.
        self.approval_nodes_shrink = approval_nodes_shrink
        # The idempotency token. Used to prevent duplicate operations caused by multiple calls.
        self.client_token = client_token
        # The description of the approval process definition.
        self.description = description
        # The ID of the approval process definition.
        # 
        # This parameter is required.
        self.id = id
        # The name of the approval process definition.
        self.name = name
        # The notification service declaration.
        self.notification_services_shrink = notification_services_shrink
        # The list of conditional rules. Note: System policies do not take effect.
        self.rule_conditions_shrink = rule_conditions_shrink

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

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.notification_services_shrink is not None:
            result['NotificationServices'] = self.notification_services_shrink

        if self.rule_conditions_shrink is not None:
            result['RuleConditions'] = self.rule_conditions_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApprovalNodes') is not None:
            self.approval_nodes_shrink = m.get('ApprovalNodes')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NotificationServices') is not None:
            self.notification_services_shrink = m.get('NotificationServices')

        if m.get('RuleConditions') is not None:
            self.rule_conditions_shrink = m.get('RuleConditions')

        return self

