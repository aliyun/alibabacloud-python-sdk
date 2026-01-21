# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class Subscription(DaraModel):
    def __init__(
        self,
        conditions: List[main_models.SubscriptionConditions] = None,
        create_time: str = None,
        description: str = None,
        enabled: bool = None,
        name: str = None,
        product: str = None,
        relation: str = None,
        strategy_uuid: str = None,
        update_time: str = None,
        uuid: str = None,
    ):
        self.conditions = conditions
        self.create_time = create_time
        self.description = description
        self.enabled = enabled
        # This parameter is required.
        self.name = name
        self.product = product
        self.relation = relation
        self.strategy_uuid = strategy_uuid
        self.update_time = update_time
        self.uuid = uuid

    def validate(self):
        if self.conditions:
            for v1 in self.conditions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Conditions'] = []
        if self.conditions is not None:
            for k1 in self.conditions:
                result['Conditions'].append(k1.to_map() if k1 else None)

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.name is not None:
            result['Name'] = self.name

        if self.product is not None:
            result['Product'] = self.product

        if self.relation is not None:
            result['Relation'] = self.relation

        if self.strategy_uuid is not None:
            result['StrategyUuid'] = self.strategy_uuid

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.conditions = []
        if m.get('Conditions') is not None:
            for k1 in m.get('Conditions'):
                temp_model = main_models.SubscriptionConditions()
                self.conditions.append(temp_model.from_map(k1))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Product') is not None:
            self.product = m.get('Product')

        if m.get('Relation') is not None:
            self.relation = m.get('Relation')

        if m.get('StrategyUuid') is not None:
            self.strategy_uuid = m.get('StrategyUuid')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

class SubscriptionConditions(DaraModel):
    def __init__(
        self,
        field: str = None,
        operator: str = None,
        value: str = None,
    ):
        self.field = field
        self.operator = operator
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.field is not None:
            result['Field'] = self.field

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Field') is not None:
            self.field = m.get('Field')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

