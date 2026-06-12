# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class LaunchServiceRequest(DaraModel):
    def __init__(
        self,
        categories: List[str] = None,
        client_token: str = None,
        recommend: bool = None,
        region_id: str = None,
        service_id: str = None,
        service_version: str = None,
    ):
        # The service categories.
        self.categories = categories
        # A client token used to ensure the idempotence of the request. Generate a unique value from your client for each request. The ClientToken parameter supports only ASCII characters.
        self.client_token = client_token
        # Specifies whether to recommend the service when publishing it to the Service Catalog.
        self.recommend = recommend
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The service ID.
        # 
        # This parameter is required.
        self.service_id = service_id
        # The service version.
        # 
        # This parameter is required.
        self.service_version = service_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.categories is not None:
            result['Categories'] = self.categories

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.recommend is not None:
            result['Recommend'] = self.recommend

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Recommend') is not None:
            self.recommend = m.get('Recommend')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')

        return self

