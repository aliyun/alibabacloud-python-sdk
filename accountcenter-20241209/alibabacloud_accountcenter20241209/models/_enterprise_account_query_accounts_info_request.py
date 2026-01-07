# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EnterpriseAccountQueryAccountsInfoRequest(DaraModel):
    def __init__(
        self,
        encrypt_ticket: str = None,
        max_results: int = None,
        next_token: str = None,
        oriented_ec_id: str = None,
        oriented_le_id: str = None,
        oriented_nb_id: str = None,
        pks_json: str = None,
        request_id: str = None,
        show_complete_info: bool = None,
    ):
        self.encrypt_ticket = encrypt_ticket
        self.max_results = max_results
        self.next_token = next_token
        self.oriented_ec_id = oriented_ec_id
        self.oriented_le_id = oriented_le_id
        self.oriented_nb_id = oriented_nb_id
        # This parameter is required.
        self.pks_json = pks_json
        # This parameter is required.
        self.request_id = request_id
        self.show_complete_info = show_complete_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.encrypt_ticket is not None:
            result['EncryptTicket'] = self.encrypt_ticket

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.oriented_ec_id is not None:
            result['OrientedEcId'] = self.oriented_ec_id

        if self.oriented_le_id is not None:
            result['OrientedLeId'] = self.oriented_le_id

        if self.oriented_nb_id is not None:
            result['OrientedNbId'] = self.oriented_nb_id

        if self.pks_json is not None:
            result['PksJson'] = self.pks_json

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.show_complete_info is not None:
            result['ShowCompleteInfo'] = self.show_complete_info

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncryptTicket') is not None:
            self.encrypt_ticket = m.get('EncryptTicket')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OrientedEcId') is not None:
            self.oriented_ec_id = m.get('OrientedEcId')

        if m.get('OrientedLeId') is not None:
            self.oriented_le_id = m.get('OrientedLeId')

        if m.get('OrientedNbId') is not None:
            self.oriented_nb_id = m.get('OrientedNbId')

        if m.get('PksJson') is not None:
            self.pks_json = m.get('PksJson')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ShowCompleteInfo') is not None:
            self.show_complete_info = m.get('ShowCompleteInfo')

        return self

