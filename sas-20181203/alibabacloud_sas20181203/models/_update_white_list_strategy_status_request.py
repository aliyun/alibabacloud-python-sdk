# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateWhiteListStrategyStatusRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        source_ip: str = None,
        status: int = None,
        strategy_ids: str = None,
    ):
        # The language type for the request and response messages. Default value: **zh**. Valid values:
        # 
        # - **zh**: Chinese
        # - **en**: English.
        self.lang = lang
        # The source IP address of the request. You do not need to specify this parameter. The system automatically obtains this value.
        self.source_ip = source_ip
        # The policy status. Valid values:
        # - **0**: Deleted.
        # - **1**: Learning.
        # - **2**: Paused.
        # - **3**: Learning complete.
        # - **4**: Active.
        # 
        # > - Only a policy in the **Learning** state can be changed to the **Paused** state.
        # > - Only a policy in the **Paused** state can be changed to the **Learning** state.
        # > - Only a policy in the **Learning complete** state can be changed to the **Active** state.
        # 
        # This parameter is required.
        self.status = status
        # The policy ID.
        # >Call the [DescribeWhiteListStrategyList](~~DescribeWhiteListStrategyList~~) operation to obtain this parameter.
        # 
        # This parameter is required.
        self.strategy_ids = strategy_ids

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

        if self.status is not None:
            result['Status'] = self.status

        if self.strategy_ids is not None:
            result['StrategyIds'] = self.strategy_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StrategyIds') is not None:
            self.strategy_ids = m.get('StrategyIds')

        return self

