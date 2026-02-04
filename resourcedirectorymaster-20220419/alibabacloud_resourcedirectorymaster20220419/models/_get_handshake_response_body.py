# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_resourcedirectorymaster20220419 import models as main_models
from darabonba.model import DaraModel

class GetHandshakeResponseBody(DaraModel):
    def __init__(
        self,
        handshake: main_models.GetHandshakeResponseBodyHandshake = None,
        request_id: str = None,
    ):
        # The information of the invitation.
        self.handshake = handshake
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.handshake:
            self.handshake.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.handshake is not None:
            result['Handshake'] = self.handshake.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Handshake') is not None:
            temp_model = main_models.GetHandshakeResponseBodyHandshake()
            self.handshake = temp_model.from_map(m.get('Handshake'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetHandshakeResponseBodyHandshake(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        expire_time: str = None,
        handshake_id: str = None,
        invited_account_real_name: str = None,
        master_account_id: str = None,
        master_account_name: str = None,
        master_account_real_name: str = None,
        modify_time: str = None,
        note: str = None,
        resource_directory_id: str = None,
        status: str = None,
        target_entity: str = None,
        target_type: str = None,
    ):
        # The time when the invitation was created. The time is displayed in UTC.
        self.create_time = create_time
        # The time when the invitation expires. The time is displayed in UTC.
        self.expire_time = expire_time
        # The ID of the invitation.
        self.handshake_id = handshake_id
        # The real-name verification information of the invitee.
        # 
        # > This parameter is available only when an invitee calls this operation.
        self.invited_account_real_name = invited_account_real_name
        # The ID of the management account of the resource directory.
        self.master_account_id = master_account_id
        # The name of the management account of the resource directory.
        self.master_account_name = master_account_name
        # The real-name verification information of the management account of the resource directory.
        # 
        # > This parameter is available only when an invitee calls this operation.
        self.master_account_real_name = master_account_real_name
        # The time when the invitation was modified. The time is displayed in UTC.
        self.modify_time = modify_time
        # The description of the invitation.
        self.note = note
        # The ID of the resource directory.
        self.resource_directory_id = resource_directory_id
        # The status of the invitation. Valid values:
        # 
        # *   Pending: The invitation is waiting for confirmation.
        # *   Accepted: The invitation is accepted.
        # *   Cancelled: The invitation is canceled.
        # *   Declined: The invitation is rejected.
        # *   Expired: The invitation expires.
        self.status = status
        # The ID or logon email address of the invited account.
        self.target_entity = target_entity
        # The type of the invited account. Valid values:
        # 
        # *   Account: indicates the ID of the account.
        # *   Email: indicates the logon email address of the account.
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.handshake_id is not None:
            result['HandshakeId'] = self.handshake_id

        if self.invited_account_real_name is not None:
            result['InvitedAccountRealName'] = self.invited_account_real_name

        if self.master_account_id is not None:
            result['MasterAccountId'] = self.master_account_id

        if self.master_account_name is not None:
            result['MasterAccountName'] = self.master_account_name

        if self.master_account_real_name is not None:
            result['MasterAccountRealName'] = self.master_account_real_name

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.note is not None:
            result['Note'] = self.note

        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id

        if self.status is not None:
            result['Status'] = self.status

        if self.target_entity is not None:
            result['TargetEntity'] = self.target_entity

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('HandshakeId') is not None:
            self.handshake_id = m.get('HandshakeId')

        if m.get('InvitedAccountRealName') is not None:
            self.invited_account_real_name = m.get('InvitedAccountRealName')

        if m.get('MasterAccountId') is not None:
            self.master_account_id = m.get('MasterAccountId')

        if m.get('MasterAccountName') is not None:
            self.master_account_name = m.get('MasterAccountName')

        if m.get('MasterAccountRealName') is not None:
            self.master_account_real_name = m.get('MasterAccountRealName')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Note') is not None:
            self.note = m.get('Note')

        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TargetEntity') is not None:
            self.target_entity = m.get('TargetEntity')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        return self

