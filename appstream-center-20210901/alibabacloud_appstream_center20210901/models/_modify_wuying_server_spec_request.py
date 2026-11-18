# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyWuyingServerSpecRequest(DaraModel):
    def __init__(
        self,
        after_status: str = None,
        product_type: str = None,
        promotion_id: str = None,
        server_instance_type: str = None,
        wuying_server_id: str = None,
    ):
        # The status after the specification change is complete.
        # 
        # - `stopped`: Shuts down the workstation after the specification change is complete.
        # 
        # This option applies to Enterprise Edition or container workstations that support this setting.
        self.after_status = after_status
        # The product type of the target workstation. It must match the actual type of the resource. For Enterprise Edition workstations, use `WuyingServer`. If this parameter is omitted, `WuyingServer` is used by default.
        self.product_type = product_type
        # The ID of the promotion. It is used to identify a promotional event or coupon.
        self.promotion_id = promotion_id
        # The ID of the target workstation specification. This parameter is required when you call the operation. Select a specification that is available in the region where the workstation is located and compatible with existing resources.
        # 
        # **Limits:** Conversion between CPU specifications and GPU specifications is not supported.
        self.server_instance_type = server_instance_type
        # The ID of the workstation whose specifications you want to change. This parameter is required.
        self.wuying_server_id = wuying_server_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.after_status is not None:
            result['AfterStatus'] = self.after_status

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id

        if self.server_instance_type is not None:
            result['ServerInstanceType'] = self.server_instance_type

        if self.wuying_server_id is not None:
            result['WuyingServerId'] = self.wuying_server_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AfterStatus') is not None:
            self.after_status = m.get('AfterStatus')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')

        if m.get('ServerInstanceType') is not None:
            self.server_instance_type = m.get('ServerInstanceType')

        if m.get('WuyingServerId') is not None:
            self.wuying_server_id = m.get('WuyingServerId')

        return self

