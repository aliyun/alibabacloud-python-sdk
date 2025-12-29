# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSecretParameterVersionsRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        name: str = None,
        next_token: str = None,
        region_id: str = None,
        share_type: str = None,
        with_decryption: bool = None,
    ):
        # The number of entries per page. Valid values: 10 to 100. Default value: 50.
        self.max_results = max_results
        # The name of the encryption parameter.
        # 
        # This parameter is required.
        self.name = name
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The ID of the region.
        self.region_id = region_id
        # The share type of the encryption parameter.
        self.share_type = share_type
        # Specifies whether to decrypt the parameter value. The decrypted parameter value is returned only if this parameter is set to true. Otherwise, null is returned.
        self.with_decryption = with_decryption

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.name is not None:
            result['Name'] = self.name

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.share_type is not None:
            result['ShareType'] = self.share_type

        if self.with_decryption is not None:
            result['WithDecryption'] = self.with_decryption

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')

        if m.get('WithDecryption') is not None:
            self.with_decryption = m.get('WithDecryption')

        return self

