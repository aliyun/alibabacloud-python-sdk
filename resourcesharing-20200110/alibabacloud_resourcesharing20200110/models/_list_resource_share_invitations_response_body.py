# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_resourcesharing20200110 import models as main_models
from darabonba.model import DaraModel

class ListResourceShareInvitationsResponseBody(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        resource_share_invitations: List[main_models.ListResourceShareInvitationsResponseBodyResourceShareInvitations] = None,
    ):
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of `NextToken`.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The information about the resource sharing invitations.
        self.resource_share_invitations = resource_share_invitations

    def validate(self):
        if self.resource_share_invitations:
            for v1 in self.resource_share_invitations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ResourceShareInvitations'] = []
        if self.resource_share_invitations is not None:
            for k1 in self.resource_share_invitations:
                result['ResourceShareInvitations'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.resource_share_invitations = []
        if m.get('ResourceShareInvitations') is not None:
            for k1 in m.get('ResourceShareInvitations'):
                temp_model = main_models.ListResourceShareInvitationsResponseBodyResourceShareInvitations()
                self.resource_share_invitations.append(temp_model.from_map(k1))

        return self

class ListResourceShareInvitationsResponseBodyResourceShareInvitations(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        invitation_failed_details: List[main_models.ListResourceShareInvitationsResponseBodyResourceShareInvitationsInvitationFailedDetails] = None,
        receiver_account_id: str = None,
        resource_share_id: str = None,
        resource_share_invitation_id: str = None,
        resource_share_name: str = None,
        sender_account_id: str = None,
        status: str = None,
    ):
        # The time when the invitation was created. The time is displayed in UTC.
        self.create_time = create_time
        # The information about the failure.
        self.invitation_failed_details = invitation_failed_details
        # The Alibaba Cloud account ID of the invitee.
        self.receiver_account_id = receiver_account_id
        # The ID of the resource share.
        self.resource_share_id = resource_share_id
        # The ID of the invitation.
        self.resource_share_invitation_id = resource_share_invitation_id
        # The name of the resource share.
        self.resource_share_name = resource_share_name
        # The Alibaba Cloud account ID of the inviter.
        self.sender_account_id = sender_account_id
        # The status of the invitation. Valid values:
        # 
        # *   Pending
        # *   Accepted
        # *   Cancelled
        # *   Rejected
        # *   Expired
        # *   AcceptFailed
        self.status = status

    def validate(self):
        if self.invitation_failed_details:
            for v1 in self.invitation_failed_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        result['InvitationFailedDetails'] = []
        if self.invitation_failed_details is not None:
            for k1 in self.invitation_failed_details:
                result['InvitationFailedDetails'].append(k1.to_map() if k1 else None)

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

        self.invitation_failed_details = []
        if m.get('InvitationFailedDetails') is not None:
            for k1 in m.get('InvitationFailedDetails'):
                temp_model = main_models.ListResourceShareInvitationsResponseBodyResourceShareInvitationsInvitationFailedDetails()
                self.invitation_failed_details.append(temp_model.from_map(k1))

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

class ListResourceShareInvitationsResponseBodyResourceShareInvitationsInvitationFailedDetails(DaraModel):
    def __init__(
        self,
        associate_type: str = None,
        failure_description: str = None,
        failure_reason: str = None,
        operation_type: str = None,
        resource_arn: str = None,
        resource_id: str = None,
        resource_type: str = None,
        status: str = None,
        status_message: str = None,
    ):
        # This parameter is deprecated. The OperationType parameter is used instead.
        self.associate_type = associate_type
        # The failure description.
        self.failure_description = failure_description
        # The failure cause. Valid values:
        # 
        # *   Unavailable: The resource cannot be shared.
        # *   LimitExceeded: The number of shared resources within the Alibaba Cloud account exceeds the upper limit.
        # *   ZonalResourceInaccessible: The resource is unavailable in this region.
        # *   InternalError: An internal error occurred during the check.
        # *   UnsupportedOperation: You cannot perform this operation.
        self.failure_reason = failure_reason
        # The operation type. Valid values:
        # 
        # *   Associate
        # *   Disassociate
        self.operation_type = operation_type
        self.resource_arn = resource_arn
        # The ID of the shared resource.
        self.resource_id = resource_id
        # The type of the shared resource.
        # 
        # For more information about the types of resources that can be shared, see [Services that work with Resource Sharing](https://help.aliyun.com/document_detail/450526.html).
        self.resource_type = resource_type
        # This parameter is deprecated. The FailureReason parameter is used instead.
        self.status = status
        # This parameter is deprecated. The FailureDescription parameter is used instead.
        self.status_message = status_message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.associate_type is not None:
            result['AssociateType'] = self.associate_type

        if self.failure_description is not None:
            result['FailureDescription'] = self.failure_description

        if self.failure_reason is not None:
            result['FailureReason'] = self.failure_reason

        if self.operation_type is not None:
            result['OperationType'] = self.operation_type

        if self.resource_arn is not None:
            result['ResourceArn'] = self.resource_arn

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.status is not None:
            result['Status'] = self.status

        if self.status_message is not None:
            result['StatusMessage'] = self.status_message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssociateType') is not None:
            self.associate_type = m.get('AssociateType')

        if m.get('FailureDescription') is not None:
            self.failure_description = m.get('FailureDescription')

        if m.get('FailureReason') is not None:
            self.failure_reason = m.get('FailureReason')

        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')

        if m.get('ResourceArn') is not None:
            self.resource_arn = m.get('ResourceArn')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusMessage') is not None:
            self.status_message = m.get('StatusMessage')

        return self

