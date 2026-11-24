# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteCostRuleResponseBody(DaraModel):
    def __init__(
        self,
        affected_model_api_ids: List[str] = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The list of model API IDs affected by the deletion.
        self.affected_model_api_ids = affected_model_api_ids
        # The request ID.
        self.request_id = request_id
        # Indicates whether the deletion was successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.affected_model_api_ids is not None:
            result['AffectedModelApiIds'] = self.affected_model_api_ids

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AffectedModelApiIds') is not None:
            self.affected_model_api_ids = m.get('AffectedModelApiIds')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

