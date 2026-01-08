# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeRiskEventTopAttackTypeResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        top_attack_type_list: List[main_models.DescribeRiskEventTopAttackTypeResponseBodyTopAttackTypeList] = None,
        total_attack_cnt: int = None,
        total_protect_cnt: int = None,
    ):
        self.request_id = request_id
        self.top_attack_type_list = top_attack_type_list
        self.total_attack_cnt = total_attack_cnt
        self.total_protect_cnt = total_protect_cnt

    def validate(self):
        if self.top_attack_type_list:
            for v1 in self.top_attack_type_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['TopAttackTypeList'] = []
        if self.top_attack_type_list is not None:
            for k1 in self.top_attack_type_list:
                result['TopAttackTypeList'].append(k1.to_map() if k1 else None)

        if self.total_attack_cnt is not None:
            result['TotalAttackCnt'] = self.total_attack_cnt

        if self.total_protect_cnt is not None:
            result['TotalProtectCnt'] = self.total_protect_cnt

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.top_attack_type_list = []
        if m.get('TopAttackTypeList') is not None:
            for k1 in m.get('TopAttackTypeList'):
                temp_model = main_models.DescribeRiskEventTopAttackTypeResponseBodyTopAttackTypeList()
                self.top_attack_type_list.append(temp_model.from_map(k1))

        if m.get('TotalAttackCnt') is not None:
            self.total_attack_cnt = m.get('TotalAttackCnt')

        if m.get('TotalProtectCnt') is not None:
            self.total_protect_cnt = m.get('TotalProtectCnt')

        return self

class DescribeRiskEventTopAttackTypeResponseBodyTopAttackTypeList(DaraModel):
    def __init__(
        self,
        attack_cnt: int = None,
        attack_type: int = None,
        protect_cnt: int = None,
    ):
        self.attack_cnt = attack_cnt
        self.attack_type = attack_type
        self.protect_cnt = protect_cnt

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attack_cnt is not None:
            result['AttackCnt'] = self.attack_cnt

        if self.attack_type is not None:
            result['AttackType'] = self.attack_type

        if self.protect_cnt is not None:
            result['ProtectCnt'] = self.protect_cnt

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttackCnt') is not None:
            self.attack_cnt = m.get('AttackCnt')

        if m.get('AttackType') is not None:
            self.attack_type = m.get('AttackType')

        if m.get('ProtectCnt') is not None:
            self.protect_cnt = m.get('ProtectCnt')

        return self

