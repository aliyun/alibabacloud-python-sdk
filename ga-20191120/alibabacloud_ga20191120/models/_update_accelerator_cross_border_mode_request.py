# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAcceleratorCrossBorderModeRequest(DaraModel):
    def __init__(
        self,
        accelerator_id: str = None,
        client_token: str = None,
        cross_border_mode: str = None,
        region_id: str = None,
    ):
        # The GA instance ID.
        # 
        # > The bandwidth metering method of the GA instance must be pay-by-data-transfer.
        # 
        # This parameter is required.
        self.accelerator_id = accelerator_id
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # The type of transmission network of the GA instance. Valid values:
        # 
        # *   **bgpPro**: BGP (Multi-ISP) Pro. BGP (Multi-ISP) Pro lines are used for cross-border acceleration. You do not need to complete real-name verification.
        # *   **private**: cross-border Express Connect circuit. Cross-border Express Connect circuits provide better acceleration performance but require real-name verification.
        # 
        # This parameter is required.
        self.cross_border_mode = cross_border_mode
        # The region ID of the GA instance. Set the value to **cn-hangzhou**.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.cross_border_mode is not None:
            result['CrossBorderMode'] = self.cross_border_mode

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('CrossBorderMode') is not None:
            self.cross_border_mode = m.get('CrossBorderMode')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

