# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeInstanceStatusRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        product_type: int = None,
    ):
        # The ID of the Anti-DDoS Proxy instance to query.
        # 
        # >  You can call the [DescribeInstanceIds](https://help.aliyun.com/document_detail/157459.html) operation to query the IDs of all Anti-DDoS Proxy (Chinese Mainland) or Anti-DDoS Proxy (Outside Chinese Mainland) instances.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The type of the Anti-DDoS Proxy instance to query. Valid values:
        # 
        # *   **1**: an Anti-DDoS Proxy (Chinese Mainland) instance
        # *   **2**: an Anti-DDoS Proxy (Outside Chinese Mainland) instance
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
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        return self

