# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class RefreshAdvisorCostCheckRequest(DaraModel):
    def __init__(
        self,
        assume_aliyun_id_list: List[int] = None,
        check_ids: List[str] = None,
        check_plan_id: int = None,
        product: str = None,
        refresh_resource: bool = None,
        resource_ids: List[str] = None,
    ):
        self.assume_aliyun_id_list = assume_aliyun_id_list
        self.check_ids = check_ids
        self.check_plan_id = check_plan_id
        self.product = product
        self.refresh_resource = refresh_resource
        self.resource_ids = resource_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assume_aliyun_id_list is not None:
            result['AssumeAliyunIdList'] = self.assume_aliyun_id_list

        if self.check_ids is not None:
            result['CheckIds'] = self.check_ids

        if self.check_plan_id is not None:
            result['CheckPlanId'] = self.check_plan_id

        if self.product is not None:
            result['Product'] = self.product

        if self.refresh_resource is not None:
            result['RefreshResource'] = self.refresh_resource

        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssumeAliyunIdList') is not None:
            self.assume_aliyun_id_list = m.get('AssumeAliyunIdList')

        if m.get('CheckIds') is not None:
            self.check_ids = m.get('CheckIds')

        if m.get('CheckPlanId') is not None:
            self.check_plan_id = m.get('CheckPlanId')

        if m.get('Product') is not None:
            self.product = m.get('Product')

        if m.get('RefreshResource') is not None:
            self.refresh_resource = m.get('RefreshResource')

        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')

        return self

