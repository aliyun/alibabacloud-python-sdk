# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListApiDestinationsRequest(DaraModel):
    def __init__(
        self,
        api_destination_name_prefix: str = None,
        connection_name: str = None,
        max_results: int = None,
        next_token: str = None,
    ):
        # The prefix of the API destination name.
        self.api_destination_name_prefix = api_destination_name_prefix
        # The connection name.
        self.connection_name = connection_name
        # The maximum number of entries to be returned in a call. You can use this parameter and NextToken to implement paging.
        # 
        # *   Default value: 10.
        self.max_results = max_results
        # If you set Limit and excess return values exist, this parameter is returned.
        # 
        # *   Default value: 0.
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_destination_name_prefix is not None:
            result['ApiDestinationNamePrefix'] = self.api_destination_name_prefix

        if self.connection_name is not None:
            result['ConnectionName'] = self.connection_name

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiDestinationNamePrefix') is not None:
            self.api_destination_name_prefix = m.get('ApiDestinationNamePrefix')

        if m.get('ConnectionName') is not None:
            self.connection_name = m.get('ConnectionName')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        return self

