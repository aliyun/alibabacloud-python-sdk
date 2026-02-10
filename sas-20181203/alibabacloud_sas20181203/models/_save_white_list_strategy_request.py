# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SaveWhiteListStrategyRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        source_ip: str = None,
        strategy_id: int = None,
        strategy_name: str = None,
        study_time: int = None,
    ):
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The source IP address of the request. You do not need to specify this parameter. It is automatically obtained by the system.
        self.source_ip = source_ip
        # The ID of the application whitelist policy.
        # 
        # >  You can call the [DescribeWhiteListStrategyList](~~DescribeWhiteListStrategyList~~) operation to query the ID.
        self.strategy_id = strategy_id
        # The name of the application whitelist policy.
        # 
        # This parameter is required.
        self.strategy_name = strategy_name
        # The duration of intelligent learning. Unit: hours.
        # 
        # This parameter is required.
        self.study_time = study_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.strategy_id is not None:
            result['StrategyId'] = self.strategy_id

        if self.strategy_name is not None:
            result['StrategyName'] = self.strategy_name

        if self.study_time is not None:
            result['StudyTime'] = self.study_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('StrategyId') is not None:
            self.strategy_id = m.get('StrategyId')

        if m.get('StrategyName') is not None:
            self.strategy_name = m.get('StrategyName')

        if m.get('StudyTime') is not None:
            self.study_time = m.get('StudyTime')

        return self

