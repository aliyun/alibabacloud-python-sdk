# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePolicyDetailsResponseBody(DaraModel):
    def __init__(
        self,
        action: str = None,
        category: str = None,
        description: str = None,
        is_deleted: int = None,
        name: str = None,
        no_config: int = None,
        severity: str = None,
        template: str = None,
    ):
        # The action of the policy. Valid values:
        # 
        # *   `enforce`: blocks deployments that match the policy.
        # *   `inform`: generates alerts for deployments that match the policy.
        self.action = action
        # The type of the policy.
        self.category = category
        # The description of the policy.
        self.description = description
        # Indicates whether the policy is deleted. Valid values:
        # 
        # *   0: The policy is not deleted.
        # *   1: The policy is deleted.
        self.is_deleted = is_deleted
        # The name of the policy.
        self.name = name
        # Indicates whether parameters are required. Valid values:
        # 
        # *   0: Parameters are required.
        # *   1: Parameters are optional.
        self.no_config = no_config
        # The severity level of the policy. Valid values:
        # 
        # *   `high`
        # *   `medium`
        # *   `low`
        self.severity = severity
        # The content of the policy.
        self.template = template

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['action'] = self.action

        if self.category is not None:
            result['category'] = self.category

        if self.description is not None:
            result['description'] = self.description

        if self.is_deleted is not None:
            result['is_deleted'] = self.is_deleted

        if self.name is not None:
            result['name'] = self.name

        if self.no_config is not None:
            result['no_config'] = self.no_config

        if self.severity is not None:
            result['severity'] = self.severity

        if self.template is not None:
            result['template'] = self.template

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')

        if m.get('category') is not None:
            self.category = m.get('category')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('is_deleted') is not None:
            self.is_deleted = m.get('is_deleted')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('no_config') is not None:
            self.no_config = m.get('no_config')

        if m.get('severity') is not None:
            self.severity = m.get('severity')

        if m.get('template') is not None:
            self.template = m.get('template')

        return self

