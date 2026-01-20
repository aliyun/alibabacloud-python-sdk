# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetOrganizationalUnitIdByExternalIdRequest(DaraModel):
    def __init__(
        self,
        organizational_unit_external_id: str = None,
        organizational_unit_source_id: str = None,
        organizational_unit_source_type: str = None,
    ):
        # The external ID of the organizational unit. The external ID can be used to map external data to the data of the organizational unit in Employee Identity and Access Management (EIAM) of Identity as a Service (IDaaS). By default, the external ID is the organizational unit ID.
        # 
        # Note: For organizational units with the same source type and source ID, each organizational unit has a unique external ID.
        # 
        # This parameter is required.
        self.organizational_unit_external_id = organizational_unit_external_id
        # The source ID of the organizational unit.
        # 
        # If the organizational unit was created in IDaaS, its source ID is the ID of the IDaaS instance. If the organizational unit was imported, its source ID is the enterprise ID in the source. For example, if the organizational unit was imported from DingTalk, its source ID is the corpId value of the enterprise in DingTalk.
        # 
        # This parameter is required.
        self.organizational_unit_source_id = organizational_unit_source_id
        # The source type of the organizational unit. Valid values:
        # 
        # *   build_in: The organizational unit was created in IDaaS.
        # *   ding_talk: The organizational unit was imported from DingTalk.
        # *   ad: The organizational unit was imported from Microsoft Active Directory (AD).
        # *   ldap: The organizational unit was imported from a Lightweight Directory Access Protocol (LDAP) service.
        # 
        # This parameter is required.
        self.organizational_unit_source_type = organizational_unit_source_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.organizational_unit_external_id is not None:
            result['organizationalUnitExternalId'] = self.organizational_unit_external_id

        if self.organizational_unit_source_id is not None:
            result['organizationalUnitSourceId'] = self.organizational_unit_source_id

        if self.organizational_unit_source_type is not None:
            result['organizationalUnitSourceType'] = self.organizational_unit_source_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('organizationalUnitExternalId') is not None:
            self.organizational_unit_external_id = m.get('organizationalUnitExternalId')

        if m.get('organizationalUnitSourceId') is not None:
            self.organizational_unit_source_id = m.get('organizationalUnitSourceId')

        if m.get('organizationalUnitSourceType') is not None:
            self.organizational_unit_source_type = m.get('organizationalUnitSourceType')

        return self

