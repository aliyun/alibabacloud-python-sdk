# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListApplicationsForNetworkZoneRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        max_results: int = None,
        network_zone_id: str = None,
        next_token: str = None,
        previous_token: str = None,
    ):
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The number of entries to return on each page.
        self.max_results = max_results
        # The ID of the network domain associated with the application.
        # 
        # This parameter is required.
        self.network_zone_id = network_zone_id
        # The token used for the next query.
        self.next_token = next_token
        # The token used to query the previous page.
        self.previous_token = previous_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.network_zone_id is not None:
            result['NetworkZoneId'] = self.network_zone_id

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.previous_token is not None:
            result['PreviousToken'] = self.previous_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NetworkZoneId') is not None:
            self.network_zone_id = m.get('NetworkZoneId')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PreviousToken') is not None:
            self.previous_token = m.get('PreviousToken')

        return self

