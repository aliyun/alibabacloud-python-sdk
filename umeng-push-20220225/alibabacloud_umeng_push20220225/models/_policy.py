# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class Policy(DaraModel):
    def __init__(
        self,
        channel_strategy: Dict[str, str] = None,
        expire_time: str = None,
        outer_biz_no: str = None,
        speed: int = None,
        start_time: str = None,
    ):
        self.channel_strategy = channel_strategy
        self.expire_time = expire_time
        self.outer_biz_no = outer_biz_no
        self.speed = speed
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_strategy is not None:
            result['channelStrategy'] = self.channel_strategy

        if self.expire_time is not None:
            result['expireTime'] = self.expire_time

        if self.outer_biz_no is not None:
            result['outerBizNo'] = self.outer_biz_no

        if self.speed is not None:
            result['speed'] = self.speed

        if self.start_time is not None:
            result['startTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('channelStrategy') is not None:
            self.channel_strategy = m.get('channelStrategy')

        if m.get('expireTime') is not None:
            self.expire_time = m.get('expireTime')

        if m.get('outerBizNo') is not None:
            self.outer_biz_no = m.get('outerBizNo')

        if m.get('speed') is not None:
            self.speed = m.get('speed')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        return self

