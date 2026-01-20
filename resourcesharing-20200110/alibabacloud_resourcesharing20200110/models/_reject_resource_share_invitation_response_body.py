# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_resourcesharing20200110 import models as main_models
from darabonba.model import DaraModel

class RejectResourceShareInvitationResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        resource_share_invitation: main_models.RejectResourceShareInvitationResponseBodyResourceShareInvitation = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The information of the resource sharing invitation.
        self.resource_share_invitation = resource_share_invitation

    def validate(self):
        if self.resource_share_invitation:
            self.resource_share_invitation.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_share_invitation is not None:
            result['ResourceShareInvitation'] = self.resource_share_invitation.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceShareInvitation') is not None:
            temp_model = main_models.RejectResourceShareInvitationResponseBodyResourceShareInvitation()
            self.resource_share_invitation = temp_model.from_map(m.get('ResourceShareInvitation'))

        return self

class RejectResourceShareInvitationResponseBodyResourceShareInvitation(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        receiver_account_id: str = None,
        resource_share_id: str = None,
        resource_share_invitation_id: str = None,
        resource_share_name: str = None,
        sender_account_id: str = None,
        status: str = None,
    ):
        # The time when the invitation was created. The time is displayed in UTC.
        # 
        # This parameter is required.
        self.create_time = create_time
        # The Alibaba Cloud account ID of the invitee.
        # 
        # This parameter is required.
        self.receiver_account_id = receiver_account_id
        # The ID of the resource share.
        # 
        # This parameter is required.
        self.resource_share_id = resource_share_id
        # The ID of the invitation.
        # 
        # This parameter is required.
        self.resource_share_invitation_id = resource_share_invitation_id
        # The name of the resource share.
        # 
        # This parameter is required.
        self.resource_share_name = resource_share_name
        # The Alibaba Cloud account ID of the inviter.
        # 
        # This parameter is required.
        self.sender_account_id = sender_account_id
        # The status of the invitation. Valid values:
        # 
        # *   Pending: The invitation is waiting for confirmation.
        # *   Accepted: The invitation is accepted.
        # *   Cancelled: The invitation is canceled.
        # *   Rejected: The invitation is rejected.
        # *   Expired: The invitation has expired.
        # 
        # This parameter is required.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.receiver_account_id is not None:
            result['ReceiverAccountId'] = self.receiver_account_id

        if self.resource_share_id is not None:
            result['ResourceShareId'] = self.resource_share_id

        if self.resource_share_invitation_id is not None:
            result['ResourceShareInvitationId'] = self.resource_share_invitation_id

        if self.resource_share_name is not None:
            result['ResourceShareName'] = self.resource_share_name

        if self.sender_account_id is not None:
            result['SenderAccountId'] = self.sender_account_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ReceiverAccountId') is not None:
            self.receiver_account_id = m.get('ReceiverAccountId')

        if m.get('ResourceShareId') is not None:
            self.resource_share_id = m.get('ResourceShareId')

        if m.get('ResourceShareInvitationId') is not None:
            self.resource_share_invitation_id = m.get('ResourceShareInvitationId')

        if m.get('ResourceShareName') is not None:
            self.resource_share_name = m.get('ResourceShareName')

        if m.get('SenderAccountId') is not None:
            self.sender_account_id = m.get('SenderAccountId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

