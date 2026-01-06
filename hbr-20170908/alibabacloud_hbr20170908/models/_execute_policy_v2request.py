# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExecutePolicyV2Request(DaraModel):
    def __init__(
        self,
        data_source_id: str = None,
        policy_id: str = None,
        rule_id: str = None,
        source_type: str = None,
    ):
        # Data source ID.
        self.data_source_id = data_source_id
        # Policy ID.
        # 
        # This parameter is required.
        self.policy_id = policy_id
        # Rule ID, limited to executing rules of **RuleType** **BACKUP**.
        # 
        # This parameter is required.
        self.rule_id = rule_id
        # Data source type, with the value range as follows:
        # 
        # - **UDM_ECS**: Represents ECS full machine backup.
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        return self

