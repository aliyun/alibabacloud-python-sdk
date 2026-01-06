# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class InviteUsersRequest(DaraModel):
    def __init__(
        self,
        invitee_list: List[main_models.InviteUsersRequestInviteeList] = None,
        tenant_context: main_models.InviteUsersRequestTenantContext = None,
        conference_id: str = None,
        phone_invitee_list: List[main_models.InviteUsersRequestPhoneInviteeList] = None,
    ):
        self.invitee_list = invitee_list
        self.tenant_context = tenant_context
        # This parameter is required.
        self.conference_id = conference_id
        self.phone_invitee_list = phone_invitee_list

    def validate(self):
        if self.invitee_list:
            for v1 in self.invitee_list:
                 if v1:
                    v1.validate()
        if self.tenant_context:
            self.tenant_context.validate()
        if self.phone_invitee_list:
            for v1 in self.phone_invitee_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InviteeList'] = []
        if self.invitee_list is not None:
            for k1 in self.invitee_list:
                result['InviteeList'].append(k1.to_map() if k1 else None)

        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()

        if self.conference_id is not None:
            result['conferenceId'] = self.conference_id

        result['phoneInviteeList'] = []
        if self.phone_invitee_list is not None:
            for k1 in self.phone_invitee_list:
                result['phoneInviteeList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.invitee_list = []
        if m.get('InviteeList') is not None:
            for k1 in m.get('InviteeList'):
                temp_model = main_models.InviteUsersRequestInviteeList()
                self.invitee_list.append(temp_model.from_map(k1))

        if m.get('TenantContext') is not None:
            temp_model = main_models.InviteUsersRequestTenantContext()
            self.tenant_context = temp_model.from_map(m.get('TenantContext'))

        if m.get('conferenceId') is not None:
            self.conference_id = m.get('conferenceId')

        self.phone_invitee_list = []
        if m.get('phoneInviteeList') is not None:
            for k1 in m.get('phoneInviteeList'):
                temp_model = main_models.InviteUsersRequestPhoneInviteeList()
                self.phone_invitee_list.append(temp_model.from_map(k1))

        return self

class InviteUsersRequestPhoneInviteeList(DaraModel):
    def __init__(
        self,
        invite_client: bool = None,
        nick: str = None,
        phone_number: str = None,
        status_code: str = None,
    ):
        self.invite_client = invite_client
        self.nick = nick
        self.phone_number = phone_number
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.invite_client is not None:
            result['InviteClient'] = self.invite_client

        if self.nick is not None:
            result['Nick'] = self.nick

        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number

        if self.status_code is not None:
            result['StatusCode'] = self.status_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InviteClient') is not None:
            self.invite_client = m.get('InviteClient')

        if m.get('Nick') is not None:
            self.nick = m.get('Nick')

        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')

        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')

        return self

class InviteUsersRequestTenantContext(DaraModel):
    def __init__(
        self,
        tenant_id: str = None,
    ):
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

class InviteUsersRequestInviteeList(DaraModel):
    def __init__(
        self,
        nick: str = None,
        user_id: str = None,
    ):
        # This parameter is required.
        self.nick = nick
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.nick is not None:
            result['Nick'] = self.nick

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Nick') is not None:
            self.nick = m.get('Nick')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

