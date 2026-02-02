# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeAppsRequest(DaraModel):
    def __init__(
        self,
        app_ids: List[str] = None,
        app_names: List[str] = None,
        client_token: str = None,
        owner: str = None,
        region_id: str = None,
    ):
        self.app_ids = app_ids
        self.app_names = app_names
        self.client_token = client_token
        self.owner = owner
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_ids is not None:
            result['AppIds'] = self.app_ids

        if self.app_names is not None:
            result['AppNames'] = self.app_names

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppIds') is not None:
            self.app_ids = m.get('AppIds')

        if m.get('AppNames') is not None:
            self.app_names = m.get('AppNames')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

