# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeCreditUsageInfoRequest(DaraModel):
    def __init__(
        self,
        biz_type: str = None,
        instance_ids: List[str] = None,
        scene_type: str = None,
        usage_type: str = None,
    ):
        # The business type.
        self.biz_type = biz_type
        # The JSON string of the instance ID list. This parameter can be omitted when `UsageType` is set to `User`. Set it to the credit package instance ID when `UsageType` is `CreditPackage`, and the agent ID when `UsageType` is `Agent`.
        self.instance_ids = instance_ids
        # The operator Scenarios type. Valid values:
        # - Not specified or NaturalMonthlyOwn: Natural monthly exclusive.
        # - JzYearlyShare: Jz annual shared.
        # - JzYearlyOwn: Jz annual exclusive.
        self.scene_type = scene_type
        # The usage type. Valid values:
        # - User: Returns the used amount, remaining amount, and consumption trend of the currently active credit packages for the user.
        # - CreditPackage: Requires a credit package ID. Returns the total amount and remaining amount of the specified credit package.
        # - Agent: Requires an agent ID. Returns the cumulative credit usage, cumulative allocated quota, and the percentage between the two.
        # - EndUser: Requires a Wuying ID. Returns the shared credit usage, pay-as-you-go credit usage, and total credit usage for the current period of the Wuying user.
        self.usage_type = usage_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.scene_type is not None:
            result['SceneType'] = self.scene_type

        if self.usage_type is not None:
            result['UsageType'] = self.usage_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('SceneType') is not None:
            self.scene_type = m.get('SceneType')

        if m.get('UsageType') is not None:
            self.usage_type = m.get('UsageType')

        return self

