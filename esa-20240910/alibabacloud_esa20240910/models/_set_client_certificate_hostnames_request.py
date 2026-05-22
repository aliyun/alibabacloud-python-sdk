# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SetClientCertificateHostnamesRequest(DaraModel):
    def __init__(
        self,
        hostnames: List[str] = None,
        id: str = None,
        site_id: int = None,
    ):
        # The domain names to associate.
        # 
        # This parameter is required.
        self.hostnames = hostnames
        # The ID of the client CA certificate.
        self.id = id
        # The website ID.
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
        if self.hostnames is not None:
            result['Hostnames'] = self.hostnames

        if self.id is not None:
            result['Id'] = self.id

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Hostnames') is not None:
            self.hostnames = m.get('Hostnames')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        return self

