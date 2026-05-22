# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateUrlObservationRequest(DaraModel):
    def __init__(
        self,
        sdk_type: str = None,
        site_id: int = None,
        url: str = None,
    ):
        # SDK integration. Supported
        # 
        # *   **automatic**
        # *   **manual**
        # 
        # This parameter is required.
        self.sdk_type = sdk_type
        # The website ID, which can be obtained by calling the [ListSites](~~ListSites~~) operation.
        # 
        # This parameter is required.
        self.site_id = site_id
        # The URL of the web page to monitor.
        # 
        # This parameter is required.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.sdk_type is not None:
            result['SdkType'] = self.sdk_type

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SdkType') is not None:
            self.sdk_type = m.get('SdkType')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

