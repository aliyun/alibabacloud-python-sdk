# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class RevokeConsumerModelCardGrantsRequest(DaraModel):
    def __init__(
        self,
        model_card_ids: List[str] = None,
        model_group_ids: List[str] = None,
        principal_id: str = None,
        principal_type: str = None,
    ):
        # The IDs of the model cards for which entitlements are revoked in this API. Revoking non-existent entitlements is a valid no-op.
        self.model_card_ids = model_card_ids
        # The IDs of the actual model groups for which entitlements are revoked in this API. If you revoke only group entitlements, modelCardIds can be empty, and the group or principal is not required to exist. At least one of the two target types must be specified. This operation does not delete consumers, keys, or quotas.
        self.model_group_ids = model_group_ids
        # The immutable ID of the principal for which entitlements are revoked. This is not the name.
        # 
        # This parameter is required.
        self.principal_id = principal_id
        # The type of the principal for which entitlements are revoked. Valid values:
        # - Consumer
        # - ConsumerGroup
        # 
        # This parameter is required.
        self.principal_type = principal_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model_card_ids is not None:
            result['modelCardIds'] = self.model_card_ids

        if self.model_group_ids is not None:
            result['modelGroupIds'] = self.model_group_ids

        if self.principal_id is not None:
            result['principalId'] = self.principal_id

        if self.principal_type is not None:
            result['principalType'] = self.principal_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('modelCardIds') is not None:
            self.model_card_ids = m.get('modelCardIds')

        if m.get('modelGroupIds') is not None:
            self.model_group_ids = m.get('modelGroupIds')

        if m.get('principalId') is not None:
            self.principal_id = m.get('principalId')

        if m.get('principalType') is not None:
            self.principal_type = m.get('principalType')

        return self

