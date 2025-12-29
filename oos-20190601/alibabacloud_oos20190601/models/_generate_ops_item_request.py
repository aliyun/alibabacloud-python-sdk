# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GenerateOpsItemRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        configuration_id: str = None,
        data: str = None,
        data_source: str = None,
        region_id: str = None,
    ):
        # The token that is used to ensure the idempotency.
        self.client_token = client_token
        # The configuration ID of the O\\&M item.
        self.configuration_id = configuration_id
        # The source system data.
        # 
        # This parameter is required.
        self.data = data
        # The data source system.
        self.data_source = data_source
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.configuration_id is not None:
            result['ConfigurationId'] = self.configuration_id

        if self.data is not None:
            result['Data'] = self.data

        if self.data_source is not None:
            result['DataSource'] = self.data_source

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ConfigurationId') is not None:
            self.configuration_id = m.get('ConfigurationId')

        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('DataSource') is not None:
            self.data_source = m.get('DataSource')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

