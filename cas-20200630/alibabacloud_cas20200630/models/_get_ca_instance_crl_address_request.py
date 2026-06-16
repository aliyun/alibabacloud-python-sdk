# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetCaInstanceCrlAddressRequest(DaraModel):
    def __init__(
        self,
        ca_identifier: str = None,
        uuid: str = None,
    ):
        # The identifier of the CA certificate.
        self.ca_identifier = ca_identifier
        # The ID of the zone where the CAS instance resides.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ca_identifier is not None:
            result['CaIdentifier'] = self.ca_identifier

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CaIdentifier') is not None:
            self.ca_identifier = m.get('CaIdentifier')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

