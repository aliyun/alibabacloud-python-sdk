# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EnterpriseRoleQueryAccountForRoleGrantByPageRequest(DaraModel):
    def __init__(
        self,
        biz_role_code: str = None,
        encrypt_ticket: str = None,
        max_results: int = None,
        next_token: str = None,
        org_id: str = None,
        oriented_ec_id: str = None,
        oriented_le_id: str = None,
        oriented_nb_id: str = None,
        page_no: int = None,
        page_size: int = None,
        query: str = None,
        show_complete_info: bool = None,
    ):
        self.biz_role_code = biz_role_code
        self.encrypt_ticket = encrypt_ticket
        self.max_results = max_results
        self.next_token = next_token
        self.org_id = org_id
        self.oriented_ec_id = oriented_ec_id
        self.oriented_le_id = oriented_le_id
        self.oriented_nb_id = oriented_nb_id
        self.page_no = page_no
        self.page_size = page_size
        self.query = query
        self.show_complete_info = show_complete_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_role_code is not None:
            result['BizRoleCode'] = self.biz_role_code

        if self.encrypt_ticket is not None:
            result['EncryptTicket'] = self.encrypt_ticket

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.org_id is not None:
            result['OrgId'] = self.org_id

        if self.oriented_ec_id is not None:
            result['OrientedEcId'] = self.oriented_ec_id

        if self.oriented_le_id is not None:
            result['OrientedLeId'] = self.oriented_le_id

        if self.oriented_nb_id is not None:
            result['OrientedNbId'] = self.oriented_nb_id

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.query is not None:
            result['Query'] = self.query

        if self.show_complete_info is not None:
            result['ShowCompleteInfo'] = self.show_complete_info

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizRoleCode') is not None:
            self.biz_role_code = m.get('BizRoleCode')

        if m.get('EncryptTicket') is not None:
            self.encrypt_ticket = m.get('EncryptTicket')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')

        if m.get('OrientedEcId') is not None:
            self.oriented_ec_id = m.get('OrientedEcId')

        if m.get('OrientedLeId') is not None:
            self.oriented_le_id = m.get('OrientedLeId')

        if m.get('OrientedNbId') is not None:
            self.oriented_nb_id = m.get('OrientedNbId')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        if m.get('ShowCompleteInfo') is not None:
            self.show_complete_info = m.get('ShowCompleteInfo')

        return self

