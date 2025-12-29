# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteStateConfigurationsRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        region_id: str = None,
        state_configuration_ids: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        # The region ID.
        self.region_id = region_id
        # The IDs of desired-state configurations.
        # 
        # This parameter is required.
        self.state_configuration_ids = state_configuration_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.state_configuration_ids is not None:
            result['StateConfigurationIds'] = self.state_configuration_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StateConfigurationIds') is not None:
            self.state_configuration_ids = m.get('StateConfigurationIds')

        return self

