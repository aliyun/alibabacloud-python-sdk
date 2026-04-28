# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RefreshAdvisorCostCheckShrinkRequest(DaraModel):
    def __init__(
        self,
        assume_aliyun_id_list_shrink: str = None,
        check_ids_shrink: str = None,
        check_plan_id: int = None,
        product: str = None,
        refresh_resource: bool = None,
        resource_ids_shrink: str = None,
    ):
        self.assume_aliyun_id_list_shrink = assume_aliyun_id_list_shrink
        self.check_ids_shrink = check_ids_shrink
        self.check_plan_id = check_plan_id
        self.product = product
        self.refresh_resource = refresh_resource
        self.resource_ids_shrink = resource_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assume_aliyun_id_list_shrink is not None:
            result['AssumeAliyunIdList'] = self.assume_aliyun_id_list_shrink

        if self.check_ids_shrink is not None:
            result['CheckIds'] = self.check_ids_shrink

        if self.check_plan_id is not None:
            result['CheckPlanId'] = self.check_plan_id

        if self.product is not None:
            result['Product'] = self.product

        if self.refresh_resource is not None:
            result['RefreshResource'] = self.refresh_resource

        if self.resource_ids_shrink is not None:
            result['ResourceIds'] = self.resource_ids_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssumeAliyunIdList') is not None:
            self.assume_aliyun_id_list_shrink = m.get('AssumeAliyunIdList')

        if m.get('CheckIds') is not None:
            self.check_ids_shrink = m.get('CheckIds')

        if m.get('CheckPlanId') is not None:
            self.check_plan_id = m.get('CheckPlanId')

        if m.get('Product') is not None:
            self.product = m.get('Product')

        if m.get('RefreshResource') is not None:
            self.refresh_resource = m.get('RefreshResource')

        if m.get('ResourceIds') is not None:
            self.resource_ids_shrink = m.get('ResourceIds')

        return self

