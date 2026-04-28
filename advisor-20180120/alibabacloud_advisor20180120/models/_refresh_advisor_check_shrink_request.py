# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RefreshAdvisorCheckShrinkRequest(DaraModel):
    def __init__(
        self,
        assume_aliyun_id: int = None,
        check_id: str = None,
        check_plan_id: int = None,
        language: str = None,
        product: str = None,
        resource_dimension_list_shrink: str = None,
        resource_id: str = None,
        token: str = None,
    ):
        self.assume_aliyun_id = assume_aliyun_id
        self.check_id = check_id
        self.check_plan_id = check_plan_id
        self.language = language
        self.product = product
        self.resource_dimension_list_shrink = resource_dimension_list_shrink
        self.resource_id = resource_id
        self.token = token

    def validate(self):
        pass

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

        if self.resource_dimension_list_shrink is not None:
            result['ResourceDimensionList'] = self.resource_dimension_list_shrink

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

        if m.get('ResourceDimensionList') is not None:
            self.resource_dimension_list_shrink = m.get('ResourceDimensionList')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        return self

