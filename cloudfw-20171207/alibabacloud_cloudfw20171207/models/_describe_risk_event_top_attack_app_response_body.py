# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeRiskEventTopAttackAppResponseBody(DaraModel):
    def __init__(
        self,
        attack_apps: List[main_models.DescribeRiskEventTopAttackAppResponseBodyAttackApps] = None,
        request_id: str = None,
    ):
        self.attack_apps = attack_apps
        self.request_id = request_id

    def validate(self):
        if self.attack_apps:
            for v1 in self.attack_apps:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AttackApps'] = []
        if self.attack_apps is not None:
            for k1 in self.attack_apps:
                result['AttackApps'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attack_apps = []
        if m.get('AttackApps') is not None:
            for k1 in m.get('AttackApps'):
                temp_model = main_models.DescribeRiskEventTopAttackAppResponseBodyAttackApps()
                self.attack_apps.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeRiskEventTopAttackAppResponseBodyAttackApps(DaraModel):
    def __init__(
        self,
        app: str = None,
        attack_cnt: int = None,
        drop_cnt: int = None,
    ):
        self.app = app
        self.attack_cnt = attack_cnt
        self.drop_cnt = drop_cnt

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app is not None:
            result['App'] = self.app

        if self.attack_cnt is not None:
            result['AttackCnt'] = self.attack_cnt

        if self.drop_cnt is not None:
            result['DropCnt'] = self.drop_cnt

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('App') is not None:
            self.app = m.get('App')

        if m.get('AttackCnt') is not None:
            self.attack_cnt = m.get('AttackCnt')

        if m.get('DropCnt') is not None:
            self.drop_cnt = m.get('DropCnt')

        return self

