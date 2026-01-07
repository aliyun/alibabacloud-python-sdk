# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EnterpriseRoleUpdateBizRoleRequest(DaraModel):
    def __init__(
        self,
        biz_permission_code_list_json: str = None,
        biz_role_code: str = None,
        biz_role_desc: str = None,
        biz_role_name: str = None,
        encrypt_ticket: str = None,
        oriented_ec_id: str = None,
        oriented_le_id: str = None,
        oriented_nb_id: str = None,
    ):
        self.biz_permission_code_list_json = biz_permission_code_list_json
        self.biz_role_code = biz_role_code
        self.biz_role_desc = biz_role_desc
        self.biz_role_name = biz_role_name
        self.encrypt_ticket = encrypt_ticket
        self.oriented_ec_id = oriented_ec_id
        self.oriented_le_id = oriented_le_id
        self.oriented_nb_id = oriented_nb_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_permission_code_list_json is not None:
            result['BizPermissionCodeListJson'] = self.biz_permission_code_list_json

        if self.biz_role_code is not None:
            result['BizRoleCode'] = self.biz_role_code

        if self.biz_role_desc is not None:
            result['BizRoleDesc'] = self.biz_role_desc

        if self.biz_role_name is not None:
            result['BizRoleName'] = self.biz_role_name

        if self.encrypt_ticket is not None:
            result['EncryptTicket'] = self.encrypt_ticket

        if self.oriented_ec_id is not None:
            result['OrientedEcId'] = self.oriented_ec_id

        if self.oriented_le_id is not None:
            result['OrientedLeId'] = self.oriented_le_id

        if self.oriented_nb_id is not None:
            result['OrientedNbId'] = self.oriented_nb_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizPermissionCodeListJson') is not None:
            self.biz_permission_code_list_json = m.get('BizPermissionCodeListJson')

        if m.get('BizRoleCode') is not None:
            self.biz_role_code = m.get('BizRoleCode')

        if m.get('BizRoleDesc') is not None:
            self.biz_role_desc = m.get('BizRoleDesc')

        if m.get('BizRoleName') is not None:
            self.biz_role_name = m.get('BizRoleName')

        if m.get('EncryptTicket') is not None:
            self.encrypt_ticket = m.get('EncryptTicket')

        if m.get('OrientedEcId') is not None:
            self.oriented_ec_id = m.get('OrientedEcId')

        if m.get('OrientedLeId') is not None:
            self.oriented_le_id = m.get('OrientedLeId')

        if m.get('OrientedNbId') is not None:
            self.oriented_nb_id = m.get('OrientedNbId')

        return self

