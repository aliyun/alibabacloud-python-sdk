# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeRiskEventStatisticResponseBody(DaraModel):
    def __init__(
        self,
        attack_app_cnt: int = None,
        attack_cnt: int = None,
        attack_ip_cnt: int = None,
        drop_cnt: int = None,
        request_id: str = None,
    ):
        self.attack_app_cnt = attack_app_cnt
        self.attack_cnt = attack_cnt
        self.attack_ip_cnt = attack_ip_cnt
        self.drop_cnt = drop_cnt
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attack_app_cnt is not None:
            result['AttackAppCnt'] = self.attack_app_cnt

        if self.attack_cnt is not None:
            result['AttackCnt'] = self.attack_cnt

        if self.attack_ip_cnt is not None:
            result['AttackIpCnt'] = self.attack_ip_cnt

        if self.drop_cnt is not None:
            result['DropCnt'] = self.drop_cnt

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttackAppCnt') is not None:
            self.attack_app_cnt = m.get('AttackAppCnt')

        if m.get('AttackCnt') is not None:
            self.attack_cnt = m.get('AttackCnt')

        if m.get('AttackIpCnt') is not None:
            self.attack_ip_cnt = m.get('AttackIpCnt')

        if m.get('DropCnt') is not None:
            self.drop_cnt = m.get('DropCnt')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

