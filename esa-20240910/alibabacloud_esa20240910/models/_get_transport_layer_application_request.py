# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTransportLayerApplicationRequest(DaraModel):
    def __init__(
        self,
        application_id: int = None,
        site_id: int = None,
    ):
        # Number of forwarding rules contained in the transport layer acceleration application.
        # 
        # This parameter is required.
        self.application_id = application_id
        # Transport layer application ID.
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
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        return self

