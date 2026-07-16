# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateUrlObservationRequest(DaraModel):
    def __init__(
        self,
        config_id: int = None,
        sdk_type: str = None,
        site_id: int = None,
    ):
        # The configuration ID. You can call the [ListUrlObservations](~~ListUrlObservations~~) operation to obtain the configuration ID.
        # 
        # This parameter is required.
        self.config_id = config_id
        # The SDK integration method. Valid values:
        # 
        # - **automatic**: automatic integration.
        # - **manual**: manual integration.
        # 
        # This parameter is required.
        self.sdk_type = sdk_type
        # The site ID. You can call the [ListSites](~~ListSites~~) operation to obtain the site ID.
        # 
        # This parameter is required.
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        if self.sdk_type is not None:
            result['SdkType'] = self.sdk_type

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('SdkType') is not None:
            self.sdk_type = m.get('SdkType')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        return self

