# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeStrategyTargetResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        strategy_targets: List[main_models.DescribeStrategyTargetResponseBodyStrategyTargets] = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The information about the assets to which the baseline check policy is applied.
        self.strategy_targets = strategy_targets

    def validate(self):
        if self.strategy_targets:
            for v1 in self.strategy_targets:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['StrategyTargets'] = []
        if self.strategy_targets is not None:
            for k1 in self.strategy_targets:
                result['StrategyTargets'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.strategy_targets = []
        if m.get('StrategyTargets') is not None:
            for k1 in m.get('StrategyTargets'):
                temp_model = main_models.DescribeStrategyTargetResponseBodyStrategyTargets()
                self.strategy_targets.append(temp_model.from_map(k1))

        return self

class DescribeStrategyTargetResponseBodyStrategyTargets(DaraModel):
    def __init__(
        self,
        bind_uuid_count: int = None,
        flag: str = None,
        target: str = None,
        target_type: str = None,
    ):
        # The number of the assets that belong to the asset group.
        self.bind_uuid_count = bind_uuid_count
        # Indicates whether the baseline check policy is applied to the asset group. Valid values:
        # 
        # *   **add**: The baseline check policy is applied to the asset group.
        # *   **del**: the baseline check policy is not applied to the asset group.
        self.flag = flag
        # The ID of the asset group to which the assets belong or the UUID of the asset.
        self.target = target
        # The method that is used to add the assets to the baseline check policy. Valid values:
        # 
        # *   **groupId**: the ID of the asset group
        # *   **uuid**: the UUID of the asset
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bind_uuid_count is not None:
            result['BindUuidCount'] = self.bind_uuid_count

        if self.flag is not None:
            result['Flag'] = self.flag

        if self.target is not None:
            result['Target'] = self.target

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindUuidCount') is not None:
            self.bind_uuid_count = m.get('BindUuidCount')

        if m.get('Flag') is not None:
            self.flag = m.get('Flag')

        if m.get('Target') is not None:
            self.target = m.get('Target')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        return self

