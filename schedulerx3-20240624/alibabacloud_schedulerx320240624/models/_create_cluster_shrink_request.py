# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_schedulerx320240624 import models as main_models
from darabonba.model import DaraModel

class CreateClusterShrinkRequest(DaraModel):
    def __init__(
        self,
        charge_type: str = None,
        cluster_name: str = None,
        cluster_spec: str = None,
        duration: int = None,
        engine_type: str = None,
        pricing_cycle: str = None,
        tag: List[main_models.CreateClusterShrinkRequestTag] = None,
        v_switches_shrink: str = None,
        vpc_id: str = None,
    ):
        self.charge_type = charge_type
        # This parameter is required.
        self.cluster_name = cluster_name
        # This parameter is required.
        self.cluster_spec = cluster_spec
        self.duration = duration
        # This parameter is required.
        self.engine_type = engine_type
        self.pricing_cycle = pricing_cycle
        self.tag = tag
        # This parameter is required.
        self.v_switches_shrink = v_switches_shrink
        # VPC id
        # 
        # This parameter is required.
        self.vpc_id = vpc_id

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.cluster_spec is not None:
            result['ClusterSpec'] = self.cluster_spec

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.engine_type is not None:
            result['EngineType'] = self.engine_type

        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.v_switches_shrink is not None:
            result['VSwitches'] = self.v_switches_shrink

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('ClusterSpec') is not None:
            self.cluster_spec = m.get('ClusterSpec')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')

        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateClusterShrinkRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('VSwitches') is not None:
            self.v_switches_shrink = m.get('VSwitches')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class CreateClusterShrinkRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

