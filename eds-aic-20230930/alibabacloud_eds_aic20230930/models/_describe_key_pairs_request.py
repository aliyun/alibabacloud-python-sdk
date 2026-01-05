# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeKeyPairsRequest(DaraModel):
    def __init__(
        self,
        key_pair_ids: List[str] = None,
        key_pair_name: str = None,
        max_results: int = None,
        next_token: str = None,
    ):
        # The IDs of the ADB key pairs.
        self.key_pair_ids = key_pair_ids
        # The name of the ADB key pair.
        self.key_pair_name = key_pair_name
        # The maximum number of entries per page. Valid values: 1 to 100. Default value: 10.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. If the parameter is left empty, the data is queried from the first entry.
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key_pair_ids is not None:
            result['KeyPairIds'] = self.key_pair_ids

        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyPairIds') is not None:
            self.key_pair_ids = m.get('KeyPairIds')

        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        return self

