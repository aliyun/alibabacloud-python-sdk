# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_advisor20180120 import models as main_models
from darabonba.model import DaraModel

class RefreshAdvisorCheckRequest(DaraModel):
    def __init__(
        self,
        assume_aliyun_id: int = None,
        check_id: str = None,
        check_plan_id: int = None,
        language: str = None,
        product: str = None,
        resource_dimension_list: List[main_models.RefreshAdvisorCheckRequestResourceDimensionList] = None,
        resource_id: str = None,
        token: str = None,
    ):
        self.assume_aliyun_id = assume_aliyun_id
        self.check_id = check_id
        self.check_plan_id = check_plan_id
        self.language = language
        self.product = product
        self.resource_dimension_list = resource_dimension_list
        self.resource_id = resource_id
        self.token = token

    def validate(self):
        if self.resource_dimension_list:
            for v1 in self.resource_dimension_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assume_aliyun_id is not None:
            result['AssumeAliyunId'] = self.assume_aliyun_id

        if self.check_id is not None:
            result['CheckId'] = self.check_id

        if self.check_plan_id is not None:
            result['CheckPlanId'] = self.check_plan_id

        if self.language is not None:
            result['Language'] = self.language

        if self.product is not None:
            result['Product'] = self.product

        result['ResourceDimensionList'] = []
        if self.resource_dimension_list is not None:
            for k1 in self.resource_dimension_list:
                result['ResourceDimensionList'].append(k1.to_map() if k1 else None)

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.token is not None:
            result['Token'] = self.token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssumeAliyunId') is not None:
            self.assume_aliyun_id = m.get('AssumeAliyunId')

        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')

        if m.get('CheckPlanId') is not None:
            self.check_plan_id = m.get('CheckPlanId')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('Product') is not None:
            self.product = m.get('Product')

        self.resource_dimension_list = []
        if m.get('ResourceDimensionList') is not None:
            for k1 in m.get('ResourceDimensionList'):
                temp_model = main_models.RefreshAdvisorCheckRequestResourceDimensionList()
                self.resource_dimension_list.append(temp_model.from_map(k1))

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        return self

class RefreshAdvisorCheckRequestResourceDimensionList(DaraModel):
    def __init__(
        self,
        cost: bool = None,
        performance: bool = None,
        product: str = None,
        product_name: str = None,
        reliablility: bool = None,
        security: bool = None,
        service: bool = None,
    ):
        self.cost = cost
        self.performance = performance
        self.product = product
        self.product_name = product_name
        self.reliablility = reliablility
        self.security = security
        self.service = service

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cost is not None:
            result['Cost'] = self.cost

        if self.performance is not None:
            result['Performance'] = self.performance

        if self.product is not None:
            result['Product'] = self.product

        if self.product_name is not None:
            result['ProductName'] = self.product_name

        if self.reliablility is not None:
            result['Reliablility'] = self.reliablility

        if self.security is not None:
            result['Security'] = self.security

        if self.service is not None:
            result['Service'] = self.service

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cost') is not None:
            self.cost = m.get('Cost')

        if m.get('Performance') is not None:
            self.performance = m.get('Performance')

        if m.get('Product') is not None:
            self.product = m.get('Product')

        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')

        if m.get('Reliablility') is not None:
            self.reliablility = m.get('Reliablility')

        if m.get('Security') is not None:
            self.security = m.get('Security')

        if m.get('Service') is not None:
            self.service = m.get('Service')

        return self

