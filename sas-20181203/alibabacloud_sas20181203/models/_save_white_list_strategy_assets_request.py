# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SaveWhiteListStrategyAssetsRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        operations: str = None,
        relation_type: int = None,
        source_ip: str = None,
        strategy_id: int = None,
    ):
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese.
        # *   **en**: English.
        self.lang = lang
        # The operation that you want to perform. This parameter is in the JSON format. The value is case-sensitive. The value contains the following fields:
        # 
        # *   **status**: the operation. Valid values:
        # 
        #     *   **0**: the delete operation.
        #     *   **1**: the add operation.
        # 
        # *   **target**: the UUID of the server.
        # 
        # >  You can call the [DescribeCloudCenterInstances](~~DescribeCloudCenterInstances~~) operation to obtain the value of **target** from the response parameter Uuid.
        # 
        # This parameter is required.
        self.operations = operations
        # The type of the policy. Valid values:
        # 
        # *   **1**: learning policy.
        # *   **2**: application policy.
        # 
        # This parameter is required.
        self.relation_type = relation_type
        # The source IP address of the request. You do not need to specify this parameter. It is automatically obtained by the system.
        self.source_ip = source_ip
        # The ID of the policy.
        # 
        # >  You can call the [DescribeWhiteListStrategyList](~~DescribeWhiteListStrategyList~~) operation to query the ID.
        # 
        # This parameter is required.
        self.strategy_id = strategy_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.operations is not None:
            result['Operations'] = self.operations

        if self.relation_type is not None:
            result['RelationType'] = self.relation_type

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.strategy_id is not None:
            result['StrategyId'] = self.strategy_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Operations') is not None:
            self.operations = m.get('Operations')

        if m.get('RelationType') is not None:
            self.relation_type = m.get('RelationType')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('StrategyId') is not None:
            self.strategy_id = m.get('StrategyId')

        return self

