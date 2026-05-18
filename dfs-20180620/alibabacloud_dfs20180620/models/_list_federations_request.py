# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListFederationsRequest(DaraModel):
    def __init__(
        self,
        federation_id: str = None,
        file_system_id: str = None,
        input_region_id: str = None,
        max_results: int = None,
        next_token: str = None,
    ):
        self.federation_id = federation_id
        self.file_system_id = file_system_id
        # This parameter is required.
        self.input_region_id = input_region_id
        self.max_results = max_results
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.federation_id is not None:
            result['FederationId'] = self.federation_id

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FederationId') is not None:
            self.federation_id = m.get('FederationId')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        return self

