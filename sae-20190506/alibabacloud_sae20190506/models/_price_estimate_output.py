# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class PriceEstimateOutput(DaraModel):
    def __init__(
        self,
        apps: List[main_models.PriceEstimateOutputApps] = None,
        items: List[main_models.PriceEstimateOutputItems] = None,
        post_pay_items: List[main_models.PriceEstimateOutputPostPayItems] = None,
        post_pay_total_price: float = None,
        total_price: float = None,
    ):
        self.apps = apps
        self.items = items
        self.post_pay_items = post_pay_items
        self.post_pay_total_price = post_pay_total_price
        self.total_price = total_price

    def validate(self):
        if self.apps:
            for v1 in self.apps:
                 if v1:
                    v1.validate()
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()
        if self.post_pay_items:
            for v1 in self.post_pay_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Apps'] = []
        if self.apps is not None:
            for k1 in self.apps:
                result['Apps'].append(k1.to_map() if k1 else None)

        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        result['PostPayItems'] = []
        if self.post_pay_items is not None:
            for k1 in self.post_pay_items:
                result['PostPayItems'].append(k1.to_map() if k1 else None)

        if self.post_pay_total_price is not None:
            result['PostPayTotalPrice'] = self.post_pay_total_price

        if self.total_price is not None:
            result['TotalPrice'] = self.total_price

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.apps = []
        if m.get('Apps') is not None:
            for k1 in m.get('Apps'):
                temp_model = main_models.PriceEstimateOutputApps()
                self.apps.append(temp_model.from_map(k1))

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.PriceEstimateOutputItems()
                self.items.append(temp_model.from_map(k1))

        self.post_pay_items = []
        if m.get('PostPayItems') is not None:
            for k1 in m.get('PostPayItems'):
                temp_model = main_models.PriceEstimateOutputPostPayItems()
                self.post_pay_items.append(temp_model.from_map(k1))

        if m.get('PostPayTotalPrice') is not None:
            self.post_pay_total_price = m.get('PostPayTotalPrice')

        if m.get('TotalPrice') is not None:
            self.total_price = m.get('TotalPrice')

        return self

class PriceEstimateOutputPostPayItems(DaraModel):
    def __init__(
        self,
        amount: float = None,
        count: int = None,
        id: str = None,
        price: float = None,
        steps: List[main_models.PriceEstimateOutputPostPayItemsSteps] = None,
        type: str = None,
        unit: str = None,
    ):
        self.amount = amount
        self.count = count
        self.id = id
        self.price = price
        self.steps = steps
        self.type = type
        self.unit = unit

    def validate(self):
        if self.steps:
            for v1 in self.steps:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['Amount'] = self.amount

        if self.count is not None:
            result['Count'] = self.count

        if self.id is not None:
            result['Id'] = self.id

        if self.price is not None:
            result['Price'] = self.price

        result['Steps'] = []
        if self.steps is not None:
            for k1 in self.steps:
                result['Steps'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['Type'] = self.type

        if self.unit is not None:
            result['Unit'] = self.unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Price') is not None:
            self.price = m.get('Price')

        self.steps = []
        if m.get('Steps') is not None:
            for k1 in m.get('Steps'):
                temp_model = main_models.PriceEstimateOutputPostPayItemsSteps()
                self.steps.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        return self

class PriceEstimateOutputPostPayItemsSteps(DaraModel):
    def __init__(
        self,
        begin: int = None,
        end: int = None,
        price: float = None,
        region_ids: List[str] = None,
        unit: str = None,
    ):
        self.begin = begin
        self.end = end
        self.price = price
        self.region_ids = region_ids
        self.unit = unit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin is not None:
            result['Begin'] = self.begin

        if self.end is not None:
            result['End'] = self.end

        if self.price is not None:
            result['Price'] = self.price

        if self.region_ids is not None:
            result['RegionIds'] = self.region_ids

        if self.unit is not None:
            result['Unit'] = self.unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')

        if m.get('End') is not None:
            self.end = m.get('End')

        if m.get('Price') is not None:
            self.price = m.get('Price')

        if m.get('RegionIds') is not None:
            self.region_ids = m.get('RegionIds')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        return self

class PriceEstimateOutputItems(DaraModel):
    def __init__(
        self,
        amount: float = None,
        count: int = None,
        id: str = None,
        price: float = None,
        steps: List[main_models.PriceEstimateOutputItemsSteps] = None,
        type: str = None,
        unit: str = None,
    ):
        self.amount = amount
        self.count = count
        self.id = id
        self.price = price
        self.steps = steps
        self.type = type
        self.unit = unit

    def validate(self):
        if self.steps:
            for v1 in self.steps:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['Amount'] = self.amount

        if self.count is not None:
            result['Count'] = self.count

        if self.id is not None:
            result['Id'] = self.id

        if self.price is not None:
            result['Price'] = self.price

        result['Steps'] = []
        if self.steps is not None:
            for k1 in self.steps:
                result['Steps'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['Type'] = self.type

        if self.unit is not None:
            result['Unit'] = self.unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Price') is not None:
            self.price = m.get('Price')

        self.steps = []
        if m.get('Steps') is not None:
            for k1 in m.get('Steps'):
                temp_model = main_models.PriceEstimateOutputItemsSteps()
                self.steps.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        return self

class PriceEstimateOutputItemsSteps(DaraModel):
    def __init__(
        self,
        begin: int = None,
        end: int = None,
        price: float = None,
        region_ids: List[str] = None,
        unit: str = None,
    ):
        self.begin = begin
        self.end = end
        self.price = price
        self.region_ids = region_ids
        self.unit = unit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin is not None:
            result['Begin'] = self.begin

        if self.end is not None:
            result['End'] = self.end

        if self.price is not None:
            result['Price'] = self.price

        if self.region_ids is not None:
            result['RegionIds'] = self.region_ids

        if self.unit is not None:
            result['Unit'] = self.unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')

        if m.get('End') is not None:
            self.end = m.get('End')

        if m.get('Price') is not None:
            self.price = m.get('Price')

        if m.get('RegionIds') is not None:
            self.region_ids = m.get('RegionIds')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        return self

class PriceEstimateOutputApps(DaraModel):
    def __init__(
        self,
        feature: main_models.PriceEstimateFeature = None,
        id: int = None,
        usages: List[main_models.PriceEstimateOutputAppsUsages] = None,
    ):
        self.feature = feature
        self.id = id
        self.usages = usages

    def validate(self):
        if self.feature:
            self.feature.validate()
        if self.usages:
            for v1 in self.usages:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.feature is not None:
            result['Feature'] = self.feature.to_map()

        if self.id is not None:
            result['Id'] = self.id

        result['Usages'] = []
        if self.usages is not None:
            for k1 in self.usages:
                result['Usages'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Feature') is not None:
            temp_model = main_models.PriceEstimateFeature()
            self.feature = temp_model.from_map(m.get('Feature'))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        self.usages = []
        if m.get('Usages') is not None:
            for k1 in m.get('Usages'):
                temp_model = main_models.PriceEstimateOutputAppsUsages()
                self.usages.append(temp_model.from_map(k1))

        return self

class PriceEstimateOutputAppsUsages(DaraModel):
    def __init__(
        self,
        amount: float = None,
        id: str = None,
        unit: str = None,
    ):
        self.amount = amount
        self.id = id
        self.unit = unit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['Amount'] = self.amount

        if self.id is not None:
            result['Id'] = self.id

        if self.unit is not None:
            result['Unit'] = self.unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        return self

