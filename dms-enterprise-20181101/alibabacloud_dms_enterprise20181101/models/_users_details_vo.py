# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UsersDetailsVO(DaraModel):
    def __init__(
        self,
        approval_signature_base_64: str = None,
        approval_sql_template: str = None,
        approval_status: str = None,
        creator: int = None,
        data_ready: int = None,
        id: int = None,
        mekid: int = None,
        path_prefix: str = None,
        result_party: int = None,
        uid: str = None,
        user_confirmed: int = None,
        user_name: str = None,
        user_public_key_pem: str = None,
    ):
        self.approval_signature_base_64 = approval_signature_base_64
        self.approval_sql_template = approval_sql_template
        self.approval_status = approval_status
        self.creator = creator
        self.data_ready = data_ready
        self.id = id
        self.mekid = mekid
        self.path_prefix = path_prefix
        self.result_party = result_party
        self.uid = uid
        self.user_confirmed = user_confirmed
        self.user_name = user_name
        self.user_public_key_pem = user_public_key_pem

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.approval_signature_base_64 is not None:
            result['ApprovalSignatureBase64'] = self.approval_signature_base_64

        if self.approval_sql_template is not None:
            result['ApprovalSqlTemplate'] = self.approval_sql_template

        if self.approval_status is not None:
            result['ApprovalStatus'] = self.approval_status

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.data_ready is not None:
            result['DataReady'] = self.data_ready

        if self.id is not None:
            result['Id'] = self.id

        if self.mekid is not None:
            result['Mekid'] = self.mekid

        if self.path_prefix is not None:
            result['PathPrefix'] = self.path_prefix

        if self.result_party is not None:
            result['ResultParty'] = self.result_party

        if self.uid is not None:
            result['Uid'] = self.uid

        if self.user_confirmed is not None:
            result['UserConfirmed'] = self.user_confirmed

        if self.user_name is not None:
            result['UserName'] = self.user_name

        if self.user_public_key_pem is not None:
            result['UserPublicKeyPem'] = self.user_public_key_pem

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApprovalSignatureBase64') is not None:
            self.approval_signature_base_64 = m.get('ApprovalSignatureBase64')

        if m.get('ApprovalSqlTemplate') is not None:
            self.approval_sql_template = m.get('ApprovalSqlTemplate')

        if m.get('ApprovalStatus') is not None:
            self.approval_status = m.get('ApprovalStatus')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('DataReady') is not None:
            self.data_ready = m.get('DataReady')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Mekid') is not None:
            self.mekid = m.get('Mekid')

        if m.get('PathPrefix') is not None:
            self.path_prefix = m.get('PathPrefix')

        if m.get('ResultParty') is not None:
            self.result_party = m.get('ResultParty')

        if m.get('Uid') is not None:
            self.uid = m.get('Uid')

        if m.get('UserConfirmed') is not None:
            self.user_confirmed = m.get('UserConfirmed')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        if m.get('UserPublicKeyPem') is not None:
            self.user_public_key_pem = m.get('UserPublicKeyPem')

        return self

