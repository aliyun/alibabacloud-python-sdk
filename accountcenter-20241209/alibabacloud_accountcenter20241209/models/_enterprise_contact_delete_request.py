# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EnterpriseContactDeleteRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        contact_id: int = None,
        oriented_ec_id: str = None,
        oriented_le_id: str = None,
        oriented_nb_id: str = None,
    ):
        # The application name.
        self.app_name = app_name
        # The ID of the contact to delete. You can call EnterpriseQueryPageList to query contact information by paging.
        self.contact_id = contact_id
        # The entity ID of the cross-enterprise management object.
        self.oriented_ec_id = oriented_ec_id
        # The enterprise currently switched to.
        self.oriented_le_id = oriented_le_id
        # The marketplace ID of the cross-enterprise management object.
        self.oriented_nb_id = oriented_nb_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.contact_id is not None:
            result['ContactId'] = self.contact_id

        if self.oriented_ec_id is not None:
            result['OrientedEcId'] = self.oriented_ec_id

        if self.oriented_le_id is not None:
            result['OrientedLeId'] = self.oriented_le_id

        if self.oriented_nb_id is not None:
            result['OrientedNbId'] = self.oriented_nb_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')

        if m.get('OrientedEcId') is not None:
            self.oriented_ec_id = m.get('OrientedEcId')

        if m.get('OrientedLeId') is not None:
            self.oriented_le_id = m.get('OrientedLeId')

        if m.get('OrientedNbId') is not None:
            self.oriented_nb_id = m.get('OrientedNbId')

        return self

