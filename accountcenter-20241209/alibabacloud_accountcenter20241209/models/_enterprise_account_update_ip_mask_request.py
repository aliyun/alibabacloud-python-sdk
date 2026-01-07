# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EnterpriseAccountUpdateIpMaskRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        ip_masks_json: str = None,
        oriented_ec_id: str = None,
        oriented_le_id: str = None,
        oriented_nb_id: str = None,
        pk: str = None,
        request_id: str = None,
        status: str = None,
    ):
        self.app_name = app_name
        # This parameter is required.
        self.ip_masks_json = ip_masks_json
        self.oriented_ec_id = oriented_ec_id
        self.oriented_le_id = oriented_le_id
        self.oriented_nb_id = oriented_nb_id
        # This parameter is required.
        self.pk = pk
        # This parameter is required.
        self.request_id = request_id
        # This parameter is required.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.ip_masks_json is not None:
            result['IpMasksJson'] = self.ip_masks_json

        if self.oriented_ec_id is not None:
            result['OrientedEcId'] = self.oriented_ec_id

        if self.oriented_le_id is not None:
            result['OrientedLeId'] = self.oriented_le_id

        if self.oriented_nb_id is not None:
            result['OrientedNbId'] = self.oriented_nb_id

        if self.pk is not None:
            result['Pk'] = self.pk

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('IpMasksJson') is not None:
            self.ip_masks_json = m.get('IpMasksJson')

        if m.get('OrientedEcId') is not None:
            self.oriented_ec_id = m.get('OrientedEcId')

        if m.get('OrientedLeId') is not None:
            self.oriented_le_id = m.get('OrientedLeId')

        if m.get('OrientedNbId') is not None:
            self.oriented_nb_id = m.get('OrientedNbId')

        if m.get('Pk') is not None:
            self.pk = m.get('Pk')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

