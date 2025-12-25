# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryModifyInstancePriceShrinkRequest(DaraModel):
    def __init__(
        self,
        ha: bool = None,
        ha_resource_spec_shrink: str = None,
        ha_vswitch_ids_shrink: str = None,
        instance_id: str = None,
        promotion_code: str = None,
        region: str = None,
        resource_spec_shrink: str = None,
        use_promotion_code: bool = None,
    ):
        self.ha = ha
        self.ha_resource_spec_shrink = ha_resource_spec_shrink
        self.ha_vswitch_ids_shrink = ha_vswitch_ids_shrink
        # This parameter is required.
        self.instance_id = instance_id
        self.promotion_code = promotion_code
        # This parameter is required.
        self.region = region
        # This parameter is required.
        self.resource_spec_shrink = resource_spec_shrink
        self.use_promotion_code = use_promotion_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ha is not None:
            result['Ha'] = self.ha

        if self.ha_resource_spec_shrink is not None:
            result['HaResourceSpec'] = self.ha_resource_spec_shrink

        if self.ha_vswitch_ids_shrink is not None:
            result['HaVSwitchIds'] = self.ha_vswitch_ids_shrink

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.promotion_code is not None:
            result['PromotionCode'] = self.promotion_code

        if self.region is not None:
            result['Region'] = self.region

        if self.resource_spec_shrink is not None:
            result['ResourceSpec'] = self.resource_spec_shrink

        if self.use_promotion_code is not None:
            result['UsePromotionCode'] = self.use_promotion_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ha') is not None:
            self.ha = m.get('Ha')

        if m.get('HaResourceSpec') is not None:
            self.ha_resource_spec_shrink = m.get('HaResourceSpec')

        if m.get('HaVSwitchIds') is not None:
            self.ha_vswitch_ids_shrink = m.get('HaVSwitchIds')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PromotionCode') is not None:
            self.promotion_code = m.get('PromotionCode')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('ResourceSpec') is not None:
            self.resource_spec_shrink = m.get('ResourceSpec')

        if m.get('UsePromotionCode') is not None:
            self.use_promotion_code = m.get('UsePromotionCode')

        return self

