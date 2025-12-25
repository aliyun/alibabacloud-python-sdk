# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class BatchGetExpressionFieldsRequest(DaraModel):
    def __init__(
        self,
        expressions: List[main_models.BatchGetExpressionFieldsRequestExpressions] = None,
        instance_id: str = None,
        kind: str = None,
        phase: str = None,
        plan_name_en: str = None,
        site_id: int = None,
    ):
        # List of expressions.
        self.expressions = expressions
        self.instance_id = instance_id
        self.kind = kind
        # WAF Phase
        self.phase = phase
        self.plan_name_en = plan_name_en
        # Site ID
        self.site_id = site_id

    def validate(self):
        if self.expressions:
            for v1 in self.expressions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Expressions'] = []
        if self.expressions is not None:
            for k1 in self.expressions:
                result['Expressions'].append(k1.to_map() if k1 else None)

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.kind is not None:
            result['Kind'] = self.kind

        if self.phase is not None:
            result['Phase'] = self.phase

        if self.plan_name_en is not None:
            result['PlanNameEn'] = self.plan_name_en

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.expressions = []
        if m.get('Expressions') is not None:
            for k1 in m.get('Expressions'):
                temp_model = main_models.BatchGetExpressionFieldsRequestExpressions()
                self.expressions.append(temp_model.from_map(k1))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Kind') is not None:
            self.kind = m.get('Kind')

        if m.get('Phase') is not None:
            self.phase = m.get('Phase')

        if m.get('PlanNameEn') is not None:
            self.plan_name_en = m.get('PlanNameEn')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        return self

class BatchGetExpressionFieldsRequestExpressions(DaraModel):
    def __init__(
        self,
        expression: str = None,
        id: int = None,
    ):
        # Content of the expression.
        self.expression = expression
        # The sequence number of the expression.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expression is not None:
            result['Expression'] = self.expression

        if self.id is not None:
            result['Id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        return self

