# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteLangfuseInstanceRequest(DaraModel):
    def __init__(
        self,
        confirm_delete_ai_gateway: bool = None,
        dbinstance_id: str = None,
        region_id: str = None,
    ):
        # The confirmation mark for deleting the AI gateway instance associated with the Langfuse instance.
        self.confirm_delete_ai_gateway = confirm_delete_ai_gateway
        # The Langfuse instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.confirm_delete_ai_gateway is not None:
            result['ConfirmDeleteAiGateway'] = self.confirm_delete_ai_gateway

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfirmDeleteAiGateway') is not None:
            self.confirm_delete_ai_gateway = m.get('ConfirmDeleteAiGateway')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

