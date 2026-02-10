# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeCustomizedStrategyTargetsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        startegy_targets: List[main_models.DescribeCustomizedStrategyTargetsResponseBodyStartegyTargets] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The information about the servers to which custom policies are applied.
        self.startegy_targets = startegy_targets

    def validate(self):
        if self.startegy_targets:
            for v1 in self.startegy_targets:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['StartegyTargets'] = []
        if self.startegy_targets is not None:
            for k1 in self.startegy_targets:
                result['StartegyTargets'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.startegy_targets = []
        if m.get('StartegyTargets') is not None:
            for k1 in m.get('StartegyTargets'):
                temp_model = main_models.DescribeCustomizedStrategyTargetsResponseBodyStartegyTargets()
                self.startegy_targets.append(temp_model.from_map(k1))

        return self

class DescribeCustomizedStrategyTargetsResponseBodyStartegyTargets(DaraModel):
    def __init__(
        self,
        group_id: int = None,
        strategy_id: int = None,
        strategy_name: str = None,
        uuid: str = None,
    ):
        # The ID of the server group.
        # 
        # >  You can call the [DescribeAllGroups](~~DescribeAllGroups~~) operation to query the IDs of server groups.
        self.group_id = group_id
        # The ID of the baseline check policy.
        self.strategy_id = strategy_id
        # The name of the baseline check policy.
        self.strategy_name = strategy_name
        # The UUID of the server.
        # 
        # >  You can call the [DescribeCloudCenterInstances](~~DescribeCloudCenterInstances~~) operation to query the UUIDs of servers.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.strategy_id is not None:
            result['StrategyId'] = self.strategy_id

        if self.strategy_name is not None:
            result['StrategyName'] = self.strategy_name

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('StrategyId') is not None:
            self.strategy_id = m.get('StrategyId')

        if m.get('StrategyName') is not None:
            self.strategy_name = m.get('StrategyName')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

