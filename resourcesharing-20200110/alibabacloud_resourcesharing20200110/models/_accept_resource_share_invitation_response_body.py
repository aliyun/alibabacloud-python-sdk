# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_resourcesharing20200110 import models as main_models
from darabonba.model import DaraModel

class AcceptResourceShareInvitationResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        resource_share_invitation: main_models.AcceptResourceShareInvitationResponseBodyResourceShareInvitation = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The information about the resource sharing invitation.
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
            temp_model = main_models.AcceptResourceShareInvitationResponseBodyResourceShareInvitation()
            self.resource_share_invitation = temp_model.from_map(m.get('ResourceShareInvitation'))

        return self

class AcceptResourceShareInvitationResponseBodyResourceShareInvitation(DaraModel):
    def __init__(
        self,
        accept_invitation_failed_details: List[main_models.AcceptResourceShareInvitationResponseBodyResourceShareInvitationAcceptInvitationFailedDetails] = None,
        create_time: str = None,
        receiver_account_id: str = None,
        resource_share_id: str = None,
        resource_share_invitation_id: str = None,
        resource_share_name: str = None,
        sender_account_id: str = None,
        status: str = None,
    ):
        # The information about the failure.
        self.accept_invitation_failed_details = accept_invitation_failed_details
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
        # The ID of the resource sharing invitation.
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
        # *   Pending
        # *   Accepted
        # *   Cancelled
        # *   Rejected
        # *   Expired
        # *   AcceptFailed
        # 
        # This parameter is required.
        self.status = status

    def validate(self):
        if self.accept_invitation_failed_details:
            for v1 in self.accept_invitation_failed_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AcceptInvitationFailedDetails'] = []
        if self.accept_invitation_failed_details is not None:
            for k1 in self.accept_invitation_failed_details:
                result['AcceptInvitationFailedDetails'].append(k1.to_map() if k1 else None)

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
        self.accept_invitation_failed_details = []
        if m.get('AcceptInvitationFailedDetails') is not None:
            for k1 in m.get('AcceptInvitationFailedDetails'):
                temp_model = main_models.AcceptResourceShareInvitationResponseBodyResourceShareInvitationAcceptInvitationFailedDetails()
                self.accept_invitation_failed_details.append(temp_model.from_map(k1))

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



class AcceptResourceShareInvitationResponseBodyResourceShareInvitationAcceptInvitationFailedDetails(DaraModel):
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
        self.failure_reason = failure_reason
        # The operation type. Valid values:
        # 
        # *   Associate
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

