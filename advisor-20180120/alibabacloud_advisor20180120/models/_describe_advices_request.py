# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAdvicesRequest(DaraModel):
    def __init__(
        self,
        advice_id: int = None,
        check_id: str = None,
        check_plan_id: int = None,
        exclude_advice_id: int = None,
        language: str = None,
        product: str = None,
        resource_id: str = None,
    ):
        self.advice_id = advice_id
        self.check_id = check_id
        self.check_plan_id = check_plan_id
        self.exclude_advice_id = exclude_advice_id
        self.language = language
        self.product = product
        self.resource_id = resource_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.advice_id is not None:
            result['AdviceId'] = self.advice_id

        if self.check_id is not None:
            result['CheckId'] = self.check_id

        if self.check_plan_id is not None:
            result['CheckPlanId'] = self.check_plan_id

        if self.exclude_advice_id is not None:
            result['ExcludeAdviceId'] = self.exclude_advice_id

        if self.language is not None:
            result['Language'] = self.language

        if self.product is not None:
            result['Product'] = self.product

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdviceId') is not None:
            self.advice_id = m.get('AdviceId')

        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')

        if m.get('CheckPlanId') is not None:
            self.check_plan_id = m.get('CheckPlanId')

        if m.get('ExcludeAdviceId') is not None:
            self.exclude_advice_id = m.get('ExcludeAdviceId')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('Product') is not None:
            self.product = m.get('Product')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        return self

