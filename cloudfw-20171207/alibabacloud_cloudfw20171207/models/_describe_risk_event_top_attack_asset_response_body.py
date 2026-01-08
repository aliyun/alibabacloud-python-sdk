# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeRiskEventTopAttackAssetResponseBody(DaraModel):
    def __init__(
        self,
        assets: List[main_models.DescribeRiskEventTopAttackAssetResponseBodyAssets] = None,
        request_id: str = None,
    ):
        self.assets = assets
        self.request_id = request_id

    def validate(self):
        if self.assets:
            for v1 in self.assets:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Assets'] = []
        if self.assets is not None:
            for k1 in self.assets:
                result['Assets'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.assets = []
        if m.get('Assets') is not None:
            for k1 in m.get('Assets'):
                temp_model = main_models.DescribeRiskEventTopAttackAssetResponseBodyAssets()
                self.assets.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeRiskEventTopAttackAssetResponseBodyAssets(DaraModel):
    def __init__(
        self,
        attack_cnt: int = None,
        drop_cnt: int = None,
        ip: str = None,
        region_no: str = None,
        resource_instance_id: str = None,
        resource_instance_name: str = None,
        resource_type: str = None,
    ):
        self.attack_cnt = attack_cnt
        self.drop_cnt = drop_cnt
        self.ip = ip
        self.region_no = region_no
        self.resource_instance_id = resource_instance_id
        self.resource_instance_name = resource_instance_name
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attack_cnt is not None:
            result['AttackCnt'] = self.attack_cnt

        if self.drop_cnt is not None:
            result['DropCnt'] = self.drop_cnt

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        if self.resource_instance_id is not None:
            result['ResourceInstanceId'] = self.resource_instance_id

        if self.resource_instance_name is not None:
            result['ResourceInstanceName'] = self.resource_instance_name

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttackCnt') is not None:
            self.attack_cnt = m.get('AttackCnt')

        if m.get('DropCnt') is not None:
            self.drop_cnt = m.get('DropCnt')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        if m.get('ResourceInstanceId') is not None:
            self.resource_instance_id = m.get('ResourceInstanceId')

        if m.get('ResourceInstanceName') is not None:
            self.resource_instance_name = m.get('ResourceInstanceName')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

