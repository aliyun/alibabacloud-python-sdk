# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeletePolicyBindingShrinkRequest(DaraModel):
    def __init__(
        self,
        data_source_ids_shrink: str = None,
        policy_id: str = None,
        source_type: str = None,
    ):
        # The IDs of the data sources that you want to disassociate from the backup policy.
        self.data_source_ids_shrink = data_source_ids_shrink
        # The ID of the backup policy.
        # 
        # This parameter is required.
        self.policy_id = policy_id
        # The type of the data source. Valid values:
        # 
        # *   **UDM_ECS**: ECS instance backup
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_source_ids_shrink is not None:
            result['DataSourceIds'] = self.data_source_ids_shrink

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceIds') is not None:
            self.data_source_ids_shrink = m.get('DataSourceIds')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        return self

