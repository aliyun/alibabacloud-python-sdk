# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteAppInstancesRequest(DaraModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        app_instance_ids: List[str] = None,
        product_type: str = None,
    ):
        # The delivery group ID. You can call [ListAppInstanceGroup](https://help.aliyun.com/document_detail/428506.html) to obtain this parameter.
        # 
        # This parameter is required.
        self.app_instance_group_id = app_instance_group_id
        # The list of application instance IDs.
        # 
        # This parameter is required.
        self.app_instance_ids = app_instance_ids
        # The product type.
        # 
        # This parameter is required.
        self.product_type = product_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id

        if self.app_instance_ids is not None:
            result['AppInstanceIds'] = self.app_instance_ids

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')

        if m.get('AppInstanceIds') is not None:
            self.app_instance_ids = m.get('AppInstanceIds')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        return self

