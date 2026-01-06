# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeDiagnosisDimensionsResponseBody(DaraModel):
    def __init__(
        self,
        client_ips: List[str] = None,
        databases: List[str] = None,
        request_id: str = None,
        resource_groups: List[str] = None,
        user_names: List[str] = None,
    ):
        # The queried source IP addresses.
        self.client_ips = client_ips
        # The queried database names.
        self.databases = databases
        # The request ID.
        self.request_id = request_id
        # The queried resource group names.
        self.resource_groups = resource_groups
        # The queried usernames.
        self.user_names = user_names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_ips is not None:
            result['ClientIps'] = self.client_ips

        if self.databases is not None:
            result['Databases'] = self.databases

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_groups is not None:
            result['ResourceGroups'] = self.resource_groups

        if self.user_names is not None:
            result['UserNames'] = self.user_names

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientIps') is not None:
            self.client_ips = m.get('ClientIps')

        if m.get('Databases') is not None:
            self.databases = m.get('Databases')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroups') is not None:
            self.resource_groups = m.get('ResourceGroups')

        if m.get('UserNames') is not None:
            self.user_names = m.get('UserNames')

        return self

