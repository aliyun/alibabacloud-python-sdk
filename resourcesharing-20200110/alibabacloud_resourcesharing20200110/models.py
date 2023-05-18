# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class AcceptResourceShareInvitationRequest(TeaModel):
    def __init__(
        self,
        resource_share_invitation_id: str = None,
    ):
        # The ID of the invitation.
        self.resource_share_invitation_id = resource_share_invitation_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_share_invitation_id is not None:
            result['ResourceShareInvitationId'] = self.resource_share_invitation_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceShareInvitationId') is not None:
            self.resource_share_invitation_id = m.get('ResourceShareInvitationId')
        return self


class AcceptResourceShareInvitationResponseBodyResourceShareInvitation(TeaModel):
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
        self.create_time = create_time
        self.receiver_account_id = receiver_account_id
        # The Alibaba Cloud account ID of the invitee.
        self.resource_share_id = resource_share_id
        # The Alibaba Cloud account ID of the inviter.
        self.resource_share_invitation_id = resource_share_invitation_id
        # The time when the invitation was created. The time is displayed in UTC.
        self.resource_share_name = resource_share_name
        # The status of the invitation. Valid values:
        # 
        # *   Pending: The invitation is waiting for confirmation.
        # *   Accepted: The invitation is accepted.
        # *   Cancelled: The invitation is canceled.
        # *   Rejected: The invitation is rejected.
        # *   Expired: The invitation has expired.
        self.sender_account_id = sender_account_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class AcceptResourceShareInvitationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_share_invitation: AcceptResourceShareInvitationResponseBodyResourceShareInvitation = None,
    ):
        # The ID of the resource share.
        self.request_id = request_id
        # The name of the resource share.
        self.resource_share_invitation = resource_share_invitation

    def validate(self):
        if self.resource_share_invitation:
            self.resource_share_invitation.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = AcceptResourceShareInvitationResponseBodyResourceShareInvitation()
            self.resource_share_invitation = temp_model.from_map(m['ResourceShareInvitation'])
        return self


class AcceptResourceShareInvitationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AcceptResourceShareInvitationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AcceptResourceShareInvitationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssociateResourceShareRequestResources(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
    ):
        # The name of a permission. If you do not configure this parameter, the system automatically associates the default permission for the specified resource type with the resource share. For more information, see [Permission library](~~465474~~).
        self.resource_id = resource_id
        # The ID of a principal.
        # 
        # *   If the value of `AllowExternalTargets` for the resource share is `false` in the response of the ListResourceShares operation, the resource share supports only resource sharing within a resource directory. In this case, you can set this parameter to the ID of the resource directory, ID of a folder in the resource directory, or ID of a member in the resource directory.
        # *   If the value of `AllowExternalTargets` for the resource share is `true` in the response of the ListResourceShares operation, the resource share supports both resource sharing within a resource directory and resource sharing outside a resource directory. In this case, you can set this parameter to the ID of an independent Alibaba Cloud account, ID of the resource directory, ID of a folder in the resource directory, or ID of a member in the resource directory.
        # 
        # For more information, see [Resource sharing modes](~~160622~~), [View the ID of a resource directory](~~111217~~), [View the ID of a folder](~~111223~~), or [View the ID of a member](~~111624~~).
        # 
        # Valid values of N: 1 to 5. This indicates that a maximum of five principals can be specified at a time.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class AssociateResourceShareRequest(TeaModel):
    def __init__(
        self,
        permission_names: List[str] = None,
        resource_share_id: str = None,
        resources: List[AssociateResourceShareRequestResources] = None,
        targets: List[str] = None,
    ):
        self.permission_names = permission_names
        # The ID of a shared resource.
        # 
        # Valid values of N: 1 to 5. This indicates that a maximum of five shared resources can be specified at a time.
        # 
        # >  Resources.N.ResourceId and Resources.N.ResourceType must be used in pairs.
        self.resource_share_id = resource_share_id
        self.resources = resources
        self.targets = targets

    def validate(self):
        if self.resources:
            for k in self.resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.permission_names is not None:
            result['PermissionNames'] = self.permission_names
        if self.resource_share_id is not None:
            result['ResourceShareId'] = self.resource_share_id
        result['Resources'] = []
        if self.resources is not None:
            for k in self.resources:
                result['Resources'].append(k.to_map() if k else None)
        if self.targets is not None:
            result['Targets'] = self.targets
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PermissionNames') is not None:
            self.permission_names = m.get('PermissionNames')
        if m.get('ResourceShareId') is not None:
            self.resource_share_id = m.get('ResourceShareId')
        self.resources = []
        if m.get('Resources') is not None:
            for k in m.get('Resources'):
                temp_model = AssociateResourceShareRequestResources()
                self.resources.append(temp_model.from_map(k))
        if m.get('Targets') is not None:
            self.targets = m.get('Targets')
        return self


class AssociateResourceShareResponseBodyResourceShareAssociations(TeaModel):
    def __init__(
        self,
        association_status: str = None,
        association_status_message: str = None,
        association_type: str = None,
        create_time: str = None,
        entity_id: str = None,
        entity_type: str = None,
        resource_share_id: str = None,
        resource_share_name: str = None,
        update_time: str = None,
    ):
        self.association_status = association_status
        # The association status. Valid values:
        # 
        # *   Associating: The entity is being associated.
        # *   Associated: The entity is associated.
        # *   Failed: The entity fails to be associated.
        # *   Disassociating: The entity is being disassociated.
        # *   Disassociated: The entity is disassociated.
        # 
        # >  The system deletes the records of entities in the `Failed` or `Disassociated` state within 48 hours to 96 hours.
        self.association_status_message = association_status_message
        self.association_type = association_type
        # The ID of the resource share.
        self.create_time = create_time
        # The time when the association of the entity was created. The value of this parameter depends on the value of the AssociationType parameter:
        # 
        # *   If the value of `AssociationType` is `Resource`, the value of this parameter is the time when the shared resource was associated with the resource share.
        # *   If the value of `AssociationType` is `Target`, the value of this parameter is the time when the principal was associated with the resource share.
        self.entity_id = entity_id
        # The cause of the association failure.
        self.entity_type = entity_type
        # The association type. Valid values:
        # 
        # *   Resource
        # *   Target
        self.resource_share_id = resource_share_id
        # The type of the entity. The value of this parameter depends on the value of the AssociationType parameter:
        # 
        # *   If the value of AssociationType is Resource, the value of this parameter is the type of the shared resource. For more information about the types of resources that can be shared, see [Services that work with Resource Sharing](~~450526~~).
        # *   If the value of AssociationType is Target, the value of this parameter is `Account`.
        self.resource_share_name = resource_share_name
        # The name of the resource share.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.association_status is not None:
            result['AssociationStatus'] = self.association_status
        if self.association_status_message is not None:
            result['AssociationStatusMessage'] = self.association_status_message
        if self.association_type is not None:
            result['AssociationType'] = self.association_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.resource_share_id is not None:
            result['ResourceShareId'] = self.resource_share_id
        if self.resource_share_name is not None:
            result['ResourceShareName'] = self.resource_share_name
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssociationStatus') is not None:
            self.association_status = m.get('AssociationStatus')
        if m.get('AssociationStatusMessage') is not None:
            self.association_status_message = m.get('AssociationStatusMessage')
        if m.get('AssociationType') is not None:
            self.association_type = m.get('AssociationType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('ResourceShareId') is not None:
            self.resource_share_id = m.get('ResourceShareId')
        if m.get('ResourceShareName') is not None:
            self.resource_share_name = m.get('ResourceShareName')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class AssociateResourceShareResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_share_associations: List[AssociateResourceShareResponseBodyResourceShareAssociations] = None,
    ):
        # The time when the association of the entity was updated. The value of this parameter depends on the value of the AssociationType parameter:
        # 
        # *   If the value of `AssociationType` is `Resource`, the value of this parameter is the time when the association of the shared resource was updated.
        # *   If the value of `AssociationType` is `Target`, the value of this parameter is the time when the association of the principal was updated.
        self.request_id = request_id
        # The ID of the entity. The value of this parameter depends on the value of the AssociationType parameter:
        # 
        # *   If the value of `AssociationType` is `Resource`, the value of this parameter is the ID of the shared resource.
        # *   If the value of `AssociationType` is `Target`, the value of this parameter is the ID of the principal.
        self.resource_share_associations = resource_share_associations

    def validate(self):
        if self.resource_share_associations:
            for k in self.resource_share_associations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ResourceShareAssociations'] = []
        if self.resource_share_associations is not None:
            for k in self.resource_share_associations:
                result['ResourceShareAssociations'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.resource_share_associations = []
        if m.get('ResourceShareAssociations') is not None:
            for k in m.get('ResourceShareAssociations'):
                temp_model = AssociateResourceShareResponseBodyResourceShareAssociations()
                self.resource_share_associations.append(temp_model.from_map(k))
        return self


class AssociateResourceShareResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AssociateResourceShareResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AssociateResourceShareResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssociateResourceSharePermissionRequest(TeaModel):
    def __init__(
        self,
        permission_name: str = None,
        replace: bool = None,
        resource_share_id: str = None,
    ):
        self.permission_name = permission_name
        self.replace = replace
        self.resource_share_id = resource_share_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.permission_name is not None:
            result['PermissionName'] = self.permission_name
        if self.replace is not None:
            result['Replace'] = self.replace
        if self.resource_share_id is not None:
            result['ResourceShareId'] = self.resource_share_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PermissionName') is not None:
            self.permission_name = m.get('PermissionName')
        if m.get('Replace') is not None:
            self.replace = m.get('Replace')
        if m.get('ResourceShareId') is not None:
            self.resource_share_id = m.get('ResourceShareId')
        return self


class AssociateResourceSharePermissionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AssociateResourceSharePermissionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AssociateResourceSharePermissionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AssociateResourceSharePermissionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateResourceShareRequestResources(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
    ):
        # The name of a permission. If you do not configure this parameter, the system automatically associates the default permission for the specified resource type with the resource share. For more information, see [Permission library](~~465474~~).
        self.resource_id = resource_id
        # The ID of a principal. Valid values:
        # 
        # *   If you set `AllowExternalTargets` to `false`, set this parameter to the ID of a resource directory, ID of a folder in a resource directory, or ID of a member in a resource directory.
        # *   If you set `AllowExternalTargets` to `true`, set this parameter to the ID of an independent Alibaba Cloud account, ID of a resource directory, ID of a folder in a resource directory, or ID of a member in a resource directory.
        # 
        # For more information, see [Resource sharing modes](~~160622~~), [View the ID of a resource directory](~~111217~~), [View the ID of a folder](~~111223~~), or [View the ID of a member](~~111624~~).
        # 
        # Valid values of N: 1 to 5. This indicates that a maximum of five principals can be specified at a time.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class CreateResourceShareRequest(TeaModel):
    def __init__(
        self,
        allow_external_targets: bool = None,
        permission_names: List[str] = None,
        resource_share_name: str = None,
        resources: List[CreateResourceShareRequestResources] = None,
        targets: List[str] = None,
    ):
        # The information of the resource share.
        self.allow_external_targets = allow_external_targets
        self.permission_names = permission_names
        # The ID of a shared resource.
        # 
        # Valid values of N: 1 to 5. This indicates that a maximum of five shared resources can be specified at a time.
        # 
        # >  `Resources.N.ResourceId` and `Resources.N.ResourceType` must be used in pairs.
        self.resource_share_name = resource_share_name
        self.resources = resources
        self.targets = targets

    def validate(self):
        if self.resources:
            for k in self.resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_external_targets is not None:
            result['AllowExternalTargets'] = self.allow_external_targets
        if self.permission_names is not None:
            result['PermissionNames'] = self.permission_names
        if self.resource_share_name is not None:
            result['ResourceShareName'] = self.resource_share_name
        result['Resources'] = []
        if self.resources is not None:
            for k in self.resources:
                result['Resources'].append(k.to_map() if k else None)
        if self.targets is not None:
            result['Targets'] = self.targets
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowExternalTargets') is not None:
            self.allow_external_targets = m.get('AllowExternalTargets')
        if m.get('PermissionNames') is not None:
            self.permission_names = m.get('PermissionNames')
        if m.get('ResourceShareName') is not None:
            self.resource_share_name = m.get('ResourceShareName')
        self.resources = []
        if m.get('Resources') is not None:
            for k in m.get('Resources'):
                temp_model = CreateResourceShareRequestResources()
                self.resources.append(temp_model.from_map(k))
        if m.get('Targets') is not None:
            self.targets = m.get('Targets')
        return self


class CreateResourceShareResponseBodyResourceShare(TeaModel):
    def __init__(
        self,
        allow_external_targets: bool = None,
        create_time: str = None,
        resource_share_id: str = None,
        resource_share_name: str = None,
        resource_share_owner: str = None,
        resource_share_status: str = None,
        update_time: str = None,
    ):
        self.allow_external_targets = allow_external_targets
        # The status of the resource share. Valid values:
        # 
        # *   Active: The resource share is enabled.
        # *   Pending: The resource share is associated with one or more resource sharing invitations that are waiting for confirmation.
        # *   Deleting: The resource share is being deleted.
        # *   Deleted: The resource share is deleted.
        # 
        # >  The system deletes the records of resource shares in the Deleted state within 48 hours to 96 hours after you delete the resource shares.
        self.create_time = create_time
        # Indicates whether resources in the resource share can be shared with accounts outside the resource directory. Valid values:
        # 
        # *   false: Resources in the resource share can be shared only with accounts in the resource directory.
        # *   true: Resources in the resource share can be shared with both accounts in the resource directory and accounts outside the resource directory.
        self.resource_share_id = resource_share_id
        # The time when the resource share was created.
        self.resource_share_name = resource_share_name
        # The ID of the resource share.
        self.resource_share_owner = resource_share_owner
        self.resource_share_status = resource_share_status
        # The owner of the resource share.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_external_targets is not None:
            result['AllowExternalTargets'] = self.allow_external_targets
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.resource_share_id is not None:
            result['ResourceShareId'] = self.resource_share_id
        if self.resource_share_name is not None:
            result['ResourceShareName'] = self.resource_share_name
        if self.resource_share_owner is not None:
            result['ResourceShareOwner'] = self.resource_share_owner
        if self.resource_share_status is not None:
            result['ResourceShareStatus'] = self.resource_share_status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowExternalTargets') is not None:
            self.allow_external_targets = m.get('AllowExternalTargets')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ResourceShareId') is not None:
            self.resource_share_id = m.get('ResourceShareId')
        if m.get('ResourceShareName') is not None:
            self.resource_share_name = m.get('ResourceShareName')
        if m.get('ResourceShareOwner') is not None:
            self.resource_share_owner = m.get('ResourceShareOwner')
        if m.get('ResourceShareStatus') is not None:
            self.resource_share_status = m.get('ResourceShareStatus')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class CreateResourceShareResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_share: CreateResourceShareResponseBodyResourceShare = None,
    ):
        # The time when the resource share was updated.
        self.request_id = request_id
        # The name of the resource share.
        self.resource_share = resource_share

    def validate(self):
        if self.resource_share:
            self.resource_share.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_share is not None:
            result['ResourceShare'] = self.resource_share.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceShare') is not None:
            temp_model = CreateResourceShareResponseBodyResourceShare()
            self.resource_share = temp_model.from_map(m['ResourceShare'])
        return self


class CreateResourceShareResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateResourceShareResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateResourceShareResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteResourceShareRequest(TeaModel):
    def __init__(
        self,
        resource_share_id: str = None,
    ):
        self.resource_share_id = resource_share_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_share_id is not None:
            result['ResourceShareId'] = self.resource_share_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceShareId') is not None:
            self.resource_share_id = m.get('ResourceShareId')
        return self


class DeleteResourceShareResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteResourceShareResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteResourceShareResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteResourceShareResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
    ):
        # The supported natural language. Valid values:
        # 
        # *   zh-CN: Chinese
        # *   en-US: English
        self.accept_language = accept_language

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(
        self,
        local_name: str = None,
        region_endpoint: str = None,
        region_id: str = None,
    ):
        # The name of the region.
        self.local_name = local_name
        # The endpoint of the Resource Sharing service in the region.
        self.region_endpoint = region_endpoint
        # The ID of the region.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_endpoint is not None:
            result['RegionEndpoint'] = self.region_endpoint
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionEndpoint') is not None:
            self.region_endpoint = m.get('RegionEndpoint')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        regions: List[DescribeRegionsResponseBodyRegions] = None,
        request_id: str = None,
    ):
        # The information of the regions.
        self.regions = regions
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.regions:
            for k in self.regions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = DescribeRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeRegionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisassociateResourceShareRequestResources(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
    ):
        # The owner of the resource share. Valid values:
        # 
        # *   Self: The resource share belongs to the current account. This is the default value. If you are the management account or a member of a resource directory and you want to remove resources or principals from a resource share, set this parameter to Self.
        # *   OtherAccounts: The resource share belongs to another account. If you are not the management account or a member of a resource directory and you want to exit a resource share, set this parameter to OtherAccounts.
        self.resource_id = resource_id
        # The ID of a principal.
        # 
        # Valid values of N: 1 to 5. This indicates that a maximum of five principals can be specified at a time.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class DisassociateResourceShareRequest(TeaModel):
    def __init__(
        self,
        resource_owner: str = None,
        resource_share_id: str = None,
        resources: List[DisassociateResourceShareRequestResources] = None,
        targets: List[str] = None,
    ):
        # The information of the entities that are associated with the resource share.
        self.resource_owner = resource_owner
        # The ID of a shared resource.
        # 
        # Valid values of N: 1 to 5. This indicates that a maximum of five shared resources can be specified at a time.
        # 
        # >  Resources.N.ResourceId and Resources.N.ResourceType must be used in pairs.
        self.resource_share_id = resource_share_id
        self.resources = resources
        self.targets = targets

    def validate(self):
        if self.resources:
            for k in self.resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_owner is not None:
            result['ResourceOwner'] = self.resource_owner
        if self.resource_share_id is not None:
            result['ResourceShareId'] = self.resource_share_id
        result['Resources'] = []
        if self.resources is not None:
            for k in self.resources:
                result['Resources'].append(k.to_map() if k else None)
        if self.targets is not None:
            result['Targets'] = self.targets
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceOwner') is not None:
            self.resource_owner = m.get('ResourceOwner')
        if m.get('ResourceShareId') is not None:
            self.resource_share_id = m.get('ResourceShareId')
        self.resources = []
        if m.get('Resources') is not None:
            for k in m.get('Resources'):
                temp_model = DisassociateResourceShareRequestResources()
                self.resources.append(temp_model.from_map(k))
        if m.get('Targets') is not None:
            self.targets = m.get('Targets')
        return self


class DisassociateResourceShareResponseBodyResourceShareAssociations(TeaModel):
    def __init__(
        self,
        association_status: str = None,
        association_status_message: str = None,
        association_type: str = None,
        create_time: str = None,
        entity_id: str = None,
        entity_type: str = None,
        resource_share_id: str = None,
        resource_share_name: str = None,
        update_time: str = None,
    ):
        self.association_status = association_status
        # The association status. Valid values:
        # 
        # *   Associating: The entity is being associated.
        # *   Associated: The entity is associated.
        # *   Failed: The entity fails to be associated.
        # *   Disassociating: The entity is being disassociated.
        # *   Disassociated: The entity is disassociated.
        # 
        # >  The system deletes the records of entities in the `Failed` or `Disassociated` state within 48 hours to 96 hours.
        self.association_status_message = association_status_message
        self.association_type = association_type
        # The ID of the resource share.
        self.create_time = create_time
        # The time when the disassociation of the entity was performed. The value of this parameter depends on the value of the AssociationType parameter:
        # 
        # *   If the value of `AssociationType` is `Resource`, the value of this parameter is the time when the resource was disassociated from the resource share.
        # *   If the value of `AssociationType` is `Target`, the value of this parameter is the time when the principal was disassociated from the resource share.
        self.entity_id = entity_id
        # The cause of the disassociation failure.
        self.entity_type = entity_type
        # The association type. Valid values:
        # 
        # *   Resource
        # *   Target
        self.resource_share_id = resource_share_id
        # The type of the entity. The value of this parameter depends on the value of the AssociationType parameter:
        # 
        # *   If the value of AssociationType is Resource, the value of this parameter is the type of the resource. For more information about the types of resources that can be shared, see [Services that work with Resource Sharing](~~450526~~).
        # *   If the value of AssociationType is Target, the value of this parameter is Account.
        self.resource_share_name = resource_share_name
        # The name of the resource share.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.association_status is not None:
            result['AssociationStatus'] = self.association_status
        if self.association_status_message is not None:
            result['AssociationStatusMessage'] = self.association_status_message
        if self.association_type is not None:
            result['AssociationType'] = self.association_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.resource_share_id is not None:
            result['ResourceShareId'] = self.resource_share_id
        if self.resource_share_name is not None:
            result['ResourceShareName'] = self.resource_share_name
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssociationStatus') is not None:
            self.association_status = m.get('AssociationStatus')
        if m.get('AssociationStatusMessage') is not None:
            self.association_status_message = m.get('AssociationStatusMessage')
        if m.get('AssociationType') is not None:
            self.association_type = m.get('AssociationType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('ResourceShareId') is not None:
            self.resource_share_id = m.get('ResourceShareId')
        if m.get('ResourceShareName') is not None:
            self.resource_share_name = m.get('ResourceShareName')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class DisassociateResourceShareResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_share_associations: List[DisassociateResourceShareResponseBodyResourceShareAssociations] = None,
    ):
        # The time when the disassociation of the entity was updated. The value of this parameter depends on the value of the AssociationType parameter:
        # 
        # *   If the value of `AssociationType` is `Resource`, the value of this parameter is the time when the disassociation of the resource was updated.
        # *   If the value of `AssociationType` is `Target`, the value of this parameter is the time when the disassociation of the principal was updated.
        self.request_id = request_id
        # The ID of the entity. The value of this parameter depends on the value of the AssociationType parameter:
        # 
        # *   If the value of `AssociationType` is `Resource`, the value of this parameter is the ID of the resource.
        # *   If the value of `AssociationType` is `Target`, the value of this parameter is the ID of the resource directory, folder, or member.
        self.resource_share_associations = resource_share_associations

    def validate(self):
        if self.resource_share_associations:
            for k in self.resource_share_associations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ResourceShareAssociations'] = []
        if self.resource_share_associations is not None:
            for k in self.resource_share_associations:
                result['ResourceShareAssociations'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.resource_share_associations = []
        if m.get('ResourceShareAssociations') is not None:
            for k in m.get('ResourceShareAssociations'):
                temp_model = DisassociateResourceShareResponseBodyResourceShareAssociations()
                self.resource_share_associations.append(temp_model.from_map(k))
        return self


class DisassociateResourceShareResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DisassociateResourceShareResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DisassociateResourceShareResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisassociateResourceSharePermissionRequest(TeaModel):
    def __init__(
        self,
        permission_name: str = None,
        resource_share_id: str = None,
    ):
        # The ID of the request.
        self.permission_name = permission_name
        # The name of the permission. For more information, see [Permission library](~~465474~~).
        self.resource_share_id = resource_share_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.permission_name is not None:
            result['PermissionName'] = self.permission_name
        if self.resource_share_id is not None:
            result['ResourceShareId'] = self.resource_share_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PermissionName') is not None:
            self.permission_name = m.get('PermissionName')
        if m.get('ResourceShareId') is not None:
            self.resource_share_id = m.get('ResourceShareId')
        return self


class DisassociateResourceSharePermissionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DisassociateResourceSharePermissionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DisassociateResourceSharePermissionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DisassociateResourceSharePermissionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableSharingWithResourceDirectoryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EnableSharingWithResourceDirectoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnableSharingWithResourceDirectoryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = EnableSharingWithResourceDirectoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPermissionRequest(TeaModel):
    def __init__(
        self,
        permission_name: str = None,
        permission_version: str = None,
    ):
        # The name of the permission.
        self.permission_name = permission_name
        # The version of the permission.
        self.permission_version = permission_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.permission_name is not None:
            result['PermissionName'] = self.permission_name
        if self.permission_version is not None:
            result['PermissionVersion'] = self.permission_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PermissionName') is not None:
            self.permission_name = m.get('PermissionName')
        if m.get('PermissionVersion') is not None:
            self.permission_version = m.get('PermissionVersion')
        return self


class GetPermissionResponseBodyPermission(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        default_permission: bool = None,
        default_version: bool = None,
        permission: str = None,
        permission_name: str = None,
        permission_version: str = None,
        resource_type: str = None,
        update_time: str = None,
    ):
        self.create_time = create_time
        self.default_permission = default_permission
        self.default_version = default_version
        # The update time.
        self.permission = permission
        # Indicates whether the version is the default version. Valid values:
        # 
        # *   false: The version is not the default version.
        # *   true: The version is the default version.
        self.permission_name = permission_name
        # The creation time.
        self.permission_version = permission_version
        # Indicates whether the permission is the default permission. Valid values:
        # 
        # *   false: The permission is not the default permission.
        # *   true: The permission is the default permission.
        self.resource_type = resource_type
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.default_permission is not None:
            result['DefaultPermission'] = self.default_permission
        if self.default_version is not None:
            result['DefaultVersion'] = self.default_version
        if self.permission is not None:
            result['Permission'] = self.permission
        if self.permission_name is not None:
            result['PermissionName'] = self.permission_name
        if self.permission_version is not None:
            result['PermissionVersion'] = self.permission_version
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DefaultPermission') is not None:
            self.default_permission = m.get('DefaultPermission')
        if m.get('DefaultVersion') is not None:
            self.default_version = m.get('DefaultVersion')
        if m.get('Permission') is not None:
            self.permission = m.get('Permission')
        if m.get('PermissionName') is not None:
            self.permission_name = m.get('PermissionName')
        if m.get('PermissionVersion') is not None:
            self.permission_version = m.get('PermissionVersion')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class GetPermissionResponseBody(TeaModel):
    def __init__(
        self,
        permission: GetPermissionResponseBodyPermission = None,
        request_id: str = None,
    ):
        # The type of the shared resources.
        # 
        # For more information about the types of resources that can be shared, see [Services that work with Resource Sharing](~~450526~~).
        self.permission = permission
        # The document of the policy related to the permission.
        self.request_id = request_id

    def validate(self):
        if self.permission:
            self.permission.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.permission is not None:
            result['Permission'] = self.permission.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Permission') is not None:
            temp_model = GetPermissionResponseBodyPermission()
            self.permission = temp_model.from_map(m['Permission'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPermissionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPermissionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetPermissionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPermissionVersionsRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        permission_name: str = None,
    ):
        # The information about the permission.
        self.max_results = max_results
        # The name of the permission.
        self.next_token = next_token
        # The ID of the request.
        self.permission_name = permission_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.permission_name is not None:
            result['PermissionName'] = self.permission_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PermissionName') is not None:
            self.permission_name = m.get('PermissionName')
        return self


class ListPermissionVersionsResponseBodyPermissions(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        default_permission: bool = None,
        default_version: bool = None,
        permission_name: str = None,
        permission_version: str = None,
        resource_type: str = None,
        update_time: str = None,
    ):
        self.create_time = create_time
        self.default_permission = default_permission
        # Indicates whether the permission is the default permission. Valid values:
        # 
        # *   false: The permission is not the default permission.
        # *   true: The permission is the default permission.
        self.default_version = default_version
        # The update time.
        self.permission_name = permission_name
        # The type of the shared resources.
        # 
        # For more information about the types of resources that can be shared, see [Services that work with Resource Sharing](~~450526~~).
        self.permission_version = permission_version
        self.resource_type = resource_type
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.default_permission is not None:
            result['DefaultPermission'] = self.default_permission
        if self.default_version is not None:
            result['DefaultVersion'] = self.default_version
        if self.permission_name is not None:
            result['PermissionName'] = self.permission_name
        if self.permission_version is not None:
            result['PermissionVersion'] = self.permission_version
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DefaultPermission') is not None:
            self.default_permission = m.get('DefaultPermission')
        if m.get('DefaultVersion') is not None:
            self.default_version = m.get('DefaultVersion')
        if m.get('PermissionName') is not None:
            self.permission_name = m.get('PermissionName')
        if m.get('PermissionVersion') is not None:
            self.permission_version = m.get('PermissionVersion')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListPermissionVersionsResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        permissions: List[ListPermissionVersionsResponseBodyPermissions] = None,
        request_id: str = None,
    ):
        # The version of the permission.
        self.next_token = next_token
        # The creation time.
        self.permissions = permissions
        # Indicates whether the version is the default version. Valid values:
        # 
        # *   false: The version is not the default version.
        # *   true: The version is the default version.
        self.request_id = request_id

    def validate(self):
        if self.permissions:
            for k in self.permissions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['Permissions'] = []
        if self.permissions is not None:
            for k in self.permissions:
                result['Permissions'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.permissions = []
        if m.get('Permissions') is not None:
            for k in m.get('Permissions'):
                temp_model = ListPermissionVersionsResponseBodyPermissions()
                self.permissions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListPermissionVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPermissionVersionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListPermissionVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPermissionsRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        resource_type: str = None,
    ):
        # The information about the permission.
        self.max_results = max_results
        # The name of the permission.
        self.next_token = next_token
        # The ID of the request.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ListPermissionsResponseBodyPermissions(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        default_permission: bool = None,
        default_version: bool = None,
        permission_name: str = None,
        permission_version: str = None,
        resource_type: str = None,
        update_time: str = None,
    ):
        self.create_time = create_time
        self.default_permission = default_permission
        # Indicates whether the permission is the default permission. Valid values:
        # 
        # *   false: The permission is not the default permission.
        # *   true: The permission is the default permission.
        self.default_version = default_version
        # The update time.
        self.permission_name = permission_name
        # The type of the shared resources.
        # 
        # For more information about the types of resources that can be shared, see [Services that work with Resource Sharing](~~450526~~).
        self.permission_version = permission_version
        self.resource_type = resource_type
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.default_permission is not None:
            result['DefaultPermission'] = self.default_permission
        if self.default_version is not None:
            result['DefaultVersion'] = self.default_version
        if self.permission_name is not None:
            result['PermissionName'] = self.permission_name
        if self.permission_version is not None:
            result['PermissionVersion'] = self.permission_version
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DefaultPermission') is not None:
            self.default_permission = m.get('DefaultPermission')
        if m.get('DefaultVersion') is not None:
            self.default_version = m.get('DefaultVersion')
        if m.get('PermissionName') is not None:
            self.permission_name = m.get('PermissionName')
        if m.get('PermissionVersion') is not None:
            self.permission_version = m.get('PermissionVersion')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListPermissionsResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        permissions: List[ListPermissionsResponseBodyPermissions] = None,
        request_id: str = None,
    ):
        # The version of the permission.
        self.next_token = next_token
        # The creation time.
        self.permissions = permissions
        # Indicates whether the version is the default version. Valid values:
        # 
        # *   false: The version is not the default version.
        # *   true: The version is the default version.
        self.request_id = request_id

    def validate(self):
        if self.permissions:
            for k in self.permissions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['Permissions'] = []
        if self.permissions is not None:
            for k in self.permissions:
                result['Permissions'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.permissions = []
        if m.get('Permissions') is not None:
            for k in m.get('Permissions'):
                temp_model = ListPermissionsResponseBodyPermissions()
                self.permissions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListPermissionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPermissionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListPermissionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourceShareAssociationsRequest(TeaModel):
    def __init__(
        self,
        association_status: str = None,
        association_type: str = None,
        max_results: int = None,
        next_token: str = None,
        resource_id: str = None,
        resource_share_ids: List[str] = None,
        target: str = None,
    ):
        # The association status. Valid values:
        # 
        # *   Associating: The entity is being associated.
        # *   Associated: The entity is associated.
        # *   Failed: The entity fails to be associated.
        # *   Disassociating: The entity is being disassociated.
        # *   Disassociated: The entity is disassociated.
        # 
        # >  The system deletes the records of entities in the `Failed` or `Disassociated` state within 48 hours to 96 hours.
        self.association_status = association_status
        # The association type. Valid values:
        # 
        # *   Resource
        # *   Target
        self.association_type = association_type
        # The maximum number of entries to return for a single request.
        # 
        # Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results
        # The `token` that is used to initiate the next request. If the response of the current request is truncated, you can use the token to initiate another request and obtain the remaining records.
        self.next_token = next_token
        # The ID of the resource.
        # 
        # >  This parameter is unavailable if you set the `AssociationType` parameter to `Target`.
        self.resource_id = resource_id
        self.resource_share_ids = resource_share_ids
        # The ID of the principal.
        # 
        # >  This parameter is unavailable if you set the `AssociationType` parameter to `Resource`.
        self.target = target

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.association_status is not None:
            result['AssociationStatus'] = self.association_status
        if self.association_type is not None:
            result['AssociationType'] = self.association_type
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_share_ids is not None:
            result['ResourceShareIds'] = self.resource_share_ids
        if self.target is not None:
            result['Target'] = self.target
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssociationStatus') is not None:
            self.association_status = m.get('AssociationStatus')
        if m.get('AssociationType') is not None:
            self.association_type = m.get('AssociationType')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceShareIds') is not None:
            self.resource_share_ids = m.get('ResourceShareIds')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        return self


class ListResourceShareAssociationsResponseBodyResourceShareAssociations(TeaModel):
    def __init__(
        self,
        association_status: str = None,
        association_status_message: str = None,
        association_type: str = None,
        create_time: str = None,
        entity_id: str = None,
        entity_type: str = None,
        external: bool = None,
        resource_share_id: str = None,
        resource_share_name: str = None,
        update_time: str = None,
    ):
        # The association status. Valid values:
        # 
        # *   Associating: The entity is being associated.
        # *   Associated: The entity is associated.
        # *   Failed: The entity fails to be associated.
        # *   Disassociating: The entity is being disassociated.
        # *   Disassociated: The entity is disassociated.
        # 
        # >  The system deletes the records of entities in the `Failed` or `Disassociated` state within 48 hours to 96 hours.
        self.association_status = association_status
        # The cause of the association failure.
        self.association_status_message = association_status_message
        # The association type. Valid values:
        # 
        # *   Resource
        # *   Target
        self.association_type = association_type
        # The time when the association of the entity was created. The value of this parameter depends on the value of the AssociationType parameter:
        # 
        # *   If the value of `AssociationType` is `Resource`, the value of this parameter is the time when the shared resource was associated with or disassociated from the resource share.
        # *   If the value of `AssociationType` is `Target`, the value of this parameter is the time when the principal was associated with or disassociated from the resource share.
        self.create_time = create_time
        # The ID of the entity. The value of this parameter depends on the value of the AssociationType parameter:
        # 
        # *   If the value of `AssociationType` is `Resource`, the value of this parameter is the ID of the shared resource.
        # *   If the value of `AssociationType` is `Target`, the value of this parameter is the ID of the principal.
        self.entity_id = entity_id
        # The type of the entity. The value of this parameter depends on the value of the AssociationType parameter:
        # 
        # *   If the value of AssociationType is Resource, the value of this parameter is the type of the resource. For more information about the types of resources that can be shared, see [Services that work with Resource Sharing](~~450526~~).
        # *   If the value of AssociationType is Target, the value of this parameter is `Account`.
        self.entity_type = entity_type
        # Indicates whether the principal is outside the resource directory. Valid values:
        # 
        # *   true: The principal is outside the resource directory.
        # *   false: The principal is in the resource directory.
        self.external = external
        # The ID of the resource share.
        self.resource_share_id = resource_share_id
        # The name of the resource share.
        self.resource_share_name = resource_share_name
        # The time when the association of the entity was updated. The value of this parameter depends on the value of the AssociationType parameter:
        # 
        # *   If the value of `AssociationType` is `Resource`, the value of this parameter is the time when the association of the shared resource was updated.
        # *   If the value of `AssociationType` is `Target`, the value of this parameter is the time when the association of the principal was updated.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.association_status is not None:
            result['AssociationStatus'] = self.association_status
        if self.association_status_message is not None:
            result['AssociationStatusMessage'] = self.association_status_message
        if self.association_type is not None:
            result['AssociationType'] = self.association_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.external is not None:
            result['External'] = self.external
        if self.resource_share_id is not None:
            result['ResourceShareId'] = self.resource_share_id
        if self.resource_share_name is not None:
            result['ResourceShareName'] = self.resource_share_name
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssociationStatus') is not None:
            self.association_status = m.get('AssociationStatus')
        if m.get('AssociationStatusMessage') is not None:
            self.association_status_message = m.get('AssociationStatusMessage')
        if m.get('AssociationType') is not None:
            self.association_type = m.get('AssociationType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('External') is not None:
            self.external = m.get('External')
        if m.get('ResourceShareId') is not None:
            self.resource_share_id = m.get('ResourceShareId')
        if m.get('ResourceShareName') is not None:
            self.resource_share_name = m.get('ResourceShareName')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListResourceShareAssociationsResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        resource_share_associations: List[ListResourceShareAssociationsResponseBodyResourceShareAssociations] = None,
    ):
        # The `token` that is used to initiate the next request. If the response of the current request is truncated, you can use the token to initiate another request and obtain the remaining records.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The information of the entities.
        self.resource_share_associations = resource_share_associations

    def validate(self):
        if self.resource_share_associations:
            for k in self.resource_share_associations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ResourceShareAssociations'] = []
        if self.resource_share_associations is not None:
            for k in self.resource_share_associations:
                result['ResourceShareAssociations'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.resource_share_associations = []
        if m.get('ResourceShareAssociations') is not None:
            for k in m.get('ResourceShareAssociations'):
                temp_model = ListResourceShareAssociationsResponseBodyResourceShareAssociations()
                self.resource_share_associations.append(temp_model.from_map(k))
        return self


class ListResourceShareAssociationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListResourceShareAssociationsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListResourceShareAssociationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourceShareInvitationsRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        resource_share_ids: List[str] = None,
        resource_share_invitation_ids: List[str] = None,
    ):
        # The IDs of the resource sharing invitations.
        self.max_results = max_results
        # The `token` that is used to initiate the next request. If the response of the current request is truncated, you can use the token to initiate another request and obtain the remaining records.
        self.next_token = next_token
        self.resource_share_ids = resource_share_ids
        self.resource_share_invitation_ids = resource_share_invitation_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_share_ids is not None:
            result['ResourceShareIds'] = self.resource_share_ids
        if self.resource_share_invitation_ids is not None:
            result['ResourceShareInvitationIds'] = self.resource_share_invitation_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceShareIds') is not None:
            self.resource_share_ids = m.get('ResourceShareIds')
        if m.get('ResourceShareInvitationIds') is not None:
            self.resource_share_invitation_ids = m.get('ResourceShareInvitationIds')
        return self


class ListResourceShareInvitationsResponseBodyResourceShareInvitations(TeaModel):
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
        # The Alibaba Cloud account ID of the inviter.
        self.create_time = create_time
        self.receiver_account_id = receiver_account_id
        # The Alibaba Cloud account ID of the invitee.
        self.resource_share_id = resource_share_id
        self.resource_share_invitation_id = resource_share_invitation_id
        # The ID of the invitation.
        self.resource_share_name = resource_share_name
        self.sender_account_id = sender_account_id
        # The name of the resource share.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListResourceShareInvitationsResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        resource_share_invitations: List[ListResourceShareInvitationsResponseBodyResourceShareInvitations] = None,
    ):
        # The status of the invitation. Valid values:
        # 
        # *   Pending: The invitation is waiting for confirmation.
        # *   Accepted: The invitation is accepted.
        # *   Cancelled: The invitation is canceled.
        # *   Rejected: The invitation is rejected.
        # *   Expired: The invitation has expired.
        self.next_token = next_token
        # The time when the invitation was created. The time is displayed in UTC.
        self.request_id = request_id
        # The ID of the resource share.
        self.resource_share_invitations = resource_share_invitations

    def validate(self):
        if self.resource_share_invitations:
            for k in self.resource_share_invitations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ResourceShareInvitations'] = []
        if self.resource_share_invitations is not None:
            for k in self.resource_share_invitations:
                result['ResourceShareInvitations'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.resource_share_invitations = []
        if m.get('ResourceShareInvitations') is not None:
            for k in m.get('ResourceShareInvitations'):
                temp_model = ListResourceShareInvitationsResponseBodyResourceShareInvitations()
                self.resource_share_invitations.append(temp_model.from_map(k))
        return self


class ListResourceShareInvitationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListResourceShareInvitationsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListResourceShareInvitationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourceSharePermissionsRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        resource_owner: str = None,
        resource_share_id: str = None,
    ):
        # The ID of the request.
        self.max_results = max_results
        # The information about the permissions.
        self.next_token = next_token
        # The name of the permission.
        self.resource_owner = resource_owner
        # The `token` that is used to initiate the next request. If the response of the current request is truncated, you can use the token to initiate another request and obtain the remaining records.
        self.resource_share_id = resource_share_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_owner is not None:
            result['ResourceOwner'] = self.resource_owner
        if self.resource_share_id is not None:
            result['ResourceShareId'] = self.resource_share_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceOwner') is not None:
            self.resource_owner = m.get('ResourceOwner')
        if m.get('ResourceShareId') is not None:
            self.resource_share_id = m.get('ResourceShareId')
        return self


class ListResourceSharePermissionsResponseBodyPermissions(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        default_permission: bool = None,
        default_version: bool = None,
        permission_name: str = None,
        permission_version: str = None,
        resource_type: str = None,
        update_time: str = None,
    ):
        self.create_time = create_time
        self.default_permission = default_permission
        # Indicates whether the permission is the default permission. Valid values:
        # 
        # *   false: The permission is not the default permission.
        # *   true: The permission is the default permission.
        self.default_version = default_version
        # The update time.
        self.permission_name = permission_name
        # The type of the shared resources.
        # 
        # For more information about the types of resources that can be shared, see [Services that work with Resource Sharing](~~450526~~).
        self.permission_version = permission_version
        self.resource_type = resource_type
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.default_permission is not None:
            result['DefaultPermission'] = self.default_permission
        if self.default_version is not None:
            result['DefaultVersion'] = self.default_version
        if self.permission_name is not None:
            result['PermissionName'] = self.permission_name
        if self.permission_version is not None:
            result['PermissionVersion'] = self.permission_version
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DefaultPermission') is not None:
            self.default_permission = m.get('DefaultPermission')
        if m.get('DefaultVersion') is not None:
            self.default_version = m.get('DefaultVersion')
        if m.get('PermissionName') is not None:
            self.permission_name = m.get('PermissionName')
        if m.get('PermissionVersion') is not None:
            self.permission_version = m.get('PermissionVersion')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListResourceSharePermissionsResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        permissions: List[ListResourceSharePermissionsResponseBodyPermissions] = None,
        request_id: str = None,
    ):
        # The version of the permission.
        self.next_token = next_token
        # The creation time.
        self.permissions = permissions
        # Indicates whether the version is the default version. Valid values:
        # 
        # *   false: The version is not the default version.
        # *   true: The version is the default version.
        self.request_id = request_id

    def validate(self):
        if self.permissions:
            for k in self.permissions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['Permissions'] = []
        if self.permissions is not None:
            for k in self.permissions:
                result['Permissions'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.permissions = []
        if m.get('Permissions') is not None:
            for k in m.get('Permissions'):
                temp_model = ListResourceSharePermissionsResponseBodyPermissions()
                self.permissions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListResourceSharePermissionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListResourceSharePermissionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListResourceSharePermissionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourceSharesRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        permission_name: str = None,
        resource_owner: str = None,
        resource_share_ids: List[str] = None,
        resource_share_name: str = None,
        resource_share_status: str = None,
    ):
        # The ID of a resource share.
        self.max_results = max_results
        # The name of the permission. For more information, see [Permission library](~~465474~~).
        self.next_token = next_token
        # The ID of the request.
        self.permission_name = permission_name
        # The status of the resource share. Valid values:
        # 
        # *   Active: The resource share is enabled.
        # *   Pending: The resource share is associated with one or more resource sharing invitations that are waiting for confirmation.
        # *   Deleting: The resource share is being deleted.
        # *   Deleted: The resource share is deleted.
        # 
        # >  The system deletes the records of resource shares in the Deleted state within 48 hours to 96 hours after you delete the resource shares.
        self.resource_owner = resource_owner
        self.resource_share_ids = resource_share_ids
        # The maximum number of entries to return for a single request.
        # 
        # Valid values: 1 to 100. Default value: 20.
        self.resource_share_name = resource_share_name
        # The `token` that is used to initiate the next request. If the response of the current request is truncated, you can use the token to initiate another request and obtain the remaining records.
        self.resource_share_status = resource_share_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.permission_name is not None:
            result['PermissionName'] = self.permission_name
        if self.resource_owner is not None:
            result['ResourceOwner'] = self.resource_owner
        if self.resource_share_ids is not None:
            result['ResourceShareIds'] = self.resource_share_ids
        if self.resource_share_name is not None:
            result['ResourceShareName'] = self.resource_share_name
        if self.resource_share_status is not None:
            result['ResourceShareStatus'] = self.resource_share_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PermissionName') is not None:
            self.permission_name = m.get('PermissionName')
        if m.get('ResourceOwner') is not None:
            self.resource_owner = m.get('ResourceOwner')
        if m.get('ResourceShareIds') is not None:
            self.resource_share_ids = m.get('ResourceShareIds')
        if m.get('ResourceShareName') is not None:
            self.resource_share_name = m.get('ResourceShareName')
        if m.get('ResourceShareStatus') is not None:
            self.resource_share_status = m.get('ResourceShareStatus')
        return self


class ListResourceSharesResponseBodyResourceShares(TeaModel):
    def __init__(
        self,
        allow_external_targets: bool = None,
        create_time: str = None,
        resource_share_id: str = None,
        resource_share_name: str = None,
        resource_share_owner: str = None,
        resource_share_status: str = None,
        update_time: str = None,
    ):
        self.allow_external_targets = allow_external_targets
        # The status of the resource share. Valid values:
        # 
        # *   Active: The resource share is enabled.
        # *   Pending: The resource share is associated with one or more resource sharing invitations that are waiting for confirmation.
        # *   Deleting: The resource share is being deleted.
        # *   Deleted: The resource share is deleted.
        # 
        # >  The system deletes the records of resource shares in the Deleted state within 48 hours to 96 hours after you delete the resource shares.
        self.create_time = create_time
        # Indicates whether resources in the resource share can be shared with accounts outside the resource directory. Valid values:
        # 
        # *   false: Resources in the resource share can be shared only with accounts in the resource directory.
        # *   true: Resources in the resource share can be shared with both accounts in the resource directory and accounts outside the resource directory.
        self.resource_share_id = resource_share_id
        # The time when the resource share was created.
        self.resource_share_name = resource_share_name
        # The ID of the resource share.
        self.resource_share_owner = resource_share_owner
        self.resource_share_status = resource_share_status
        # The owner of the resource share.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_external_targets is not None:
            result['AllowExternalTargets'] = self.allow_external_targets
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.resource_share_id is not None:
            result['ResourceShareId'] = self.resource_share_id
        if self.resource_share_name is not None:
            result['ResourceShareName'] = self.resource_share_name
        if self.resource_share_owner is not None:
            result['ResourceShareOwner'] = self.resource_share_owner
        if self.resource_share_status is not None:
            result['ResourceShareStatus'] = self.resource_share_status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowExternalTargets') is not None:
            self.allow_external_targets = m.get('AllowExternalTargets')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ResourceShareId') is not None:
            self.resource_share_id = m.get('ResourceShareId')
        if m.get('ResourceShareName') is not None:
            self.resource_share_name = m.get('ResourceShareName')
        if m.get('ResourceShareOwner') is not None:
            self.resource_share_owner = m.get('ResourceShareOwner')
        if m.get('ResourceShareStatus') is not None:
            self.resource_share_status = m.get('ResourceShareStatus')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListResourceSharesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        resource_shares: List[ListResourceSharesResponseBodyResourceShares] = None,
    ):
        # The information of the resource shares.
        self.next_token = next_token
        # The time when the resource share was updated.
        self.request_id = request_id
        # The name of the resource share.
        self.resource_shares = resource_shares

    def validate(self):
        if self.resource_shares:
            for k in self.resource_shares:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ResourceShares'] = []
        if self.resource_shares is not None:
            for k in self.resource_shares:
                result['ResourceShares'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.resource_shares = []
        if m.get('ResourceShares') is not None:
            for k in m.get('ResourceShares'):
                temp_model = ListResourceSharesResponseBodyResourceShares()
                self.resource_shares.append(temp_model.from_map(k))
        return self


class ListResourceSharesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListResourceSharesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListResourceSharesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSharedResourcesRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        resource_ids: List[str] = None,
        resource_owner: str = None,
        resource_share_ids: List[str] = None,
        resource_type: str = None,
        target: str = None,
    ):
        # The maximum number of entries to return for a single request.
        # 
        # Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results
        # The `token` that is used to initiate the next request. If the response of the current request is truncated, you can use the token to initiate another request and obtain the remaining records.
        self.next_token = next_token
        self.resource_ids = resource_ids
        # The owner of the resource shares. Valid values:
        # 
        # *   Self: your account. If you set the value to Self, the resources you share with other accounts are queried.
        # *   OtherAccounts: another account. If you set the value to OtherAccounts, the resources other accounts share with you are queried.
        self.resource_owner = resource_owner
        self.resource_share_ids = resource_share_ids
        # The type of the shared resources.
        # 
        # For more information about the types of resources that can be shared, see [Services that work with Resource Sharing](~~450526~~).
        self.resource_type = resource_type
        # The ID of the principal or resource owner.
        # 
        # *   If the value of `ResourceOwner` is `Self`, set this parameter to the ID of a principal.
        # *   If the value of `ResourceOwner` is `OtherAccounts`, set this parameter to the ID of a resource owner.
        self.target = target

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids
        if self.resource_owner is not None:
            result['ResourceOwner'] = self.resource_owner
        if self.resource_share_ids is not None:
            result['ResourceShareIds'] = self.resource_share_ids
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.target is not None:
            result['Target'] = self.target
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')
        if m.get('ResourceOwner') is not None:
            self.resource_owner = m.get('ResourceOwner')
        if m.get('ResourceShareIds') is not None:
            self.resource_share_ids = m.get('ResourceShareIds')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        return self


class ListSharedResourcesResponseBodySharedResources(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        resource_id: str = None,
        resource_share_id: str = None,
        resource_status: str = None,
        resource_status_message: str = None,
        resource_type: str = None,
        update_time: str = None,
    ):
        # The time when the shared resource was associated with the resource share.
        self.create_time = create_time
        # The ID of the shared resource.
        self.resource_id = resource_id
        # The ID of the resource share.
        self.resource_share_id = resource_share_id
        # The status of the shared resource. This parameter is returned only when you query the resources that other accounts share with you.
        # 
        # Valid values:
        # 
        # *   Available: The resource is available.
        # *   ZonalResourceInaccessible: The resource is unavailable in the current zone.
        # *   LimitExceeded: The resource is unavailable because the maximum number of resources that other accounts can share with you exceeds the upper limit.
        # *   Unavailable: The resource is unavailable.
        self.resource_status = resource_status
        # The cause of the association failure.
        self.resource_status_message = resource_status_message
        # The type of the shared resource.
        # 
        # For more information about the types of resources that can be shared, see [Services that work with Resource Sharing](~~450526~~).
        self.resource_type = resource_type
        # The time when the association of the shared resource was updated.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_share_id is not None:
            result['ResourceShareId'] = self.resource_share_id
        if self.resource_status is not None:
            result['ResourceStatus'] = self.resource_status
        if self.resource_status_message is not None:
            result['ResourceStatusMessage'] = self.resource_status_message
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceShareId') is not None:
            self.resource_share_id = m.get('ResourceShareId')
        if m.get('ResourceStatus') is not None:
            self.resource_status = m.get('ResourceStatus')
        if m.get('ResourceStatusMessage') is not None:
            self.resource_status_message = m.get('ResourceStatusMessage')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListSharedResourcesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        shared_resources: List[ListSharedResourcesResponseBodySharedResources] = None,
    ):
        # The token that is used to initiate the next request. If the response of the current request is truncated, you can use the token to initiate another request and obtain the remaining records.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The information of the shared resources.
        self.shared_resources = shared_resources

    def validate(self):
        if self.shared_resources:
            for k in self.shared_resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SharedResources'] = []
        if self.shared_resources is not None:
            for k in self.shared_resources:
                result['SharedResources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.shared_resources = []
        if m.get('SharedResources') is not None:
            for k in m.get('SharedResources'):
                temp_model = ListSharedResourcesResponseBodySharedResources()
                self.shared_resources.append(temp_model.from_map(k))
        return self


class ListSharedResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSharedResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListSharedResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSharedTargetsRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        resource_id: str = None,
        resource_owner: str = None,
        resource_share_ids: List[str] = None,
        resource_type: str = None,
        targets: List[str] = None,
    ):
        # The maximum number of entries to return for a single request.
        # 
        # Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results
        # The `token` that is used to initiate the next request. If the response of the current request is truncated, you can use the token to initiate another request and obtain the remaining records.
        self.next_token = next_token
        # The ID of the shared resource.
        self.resource_id = resource_id
        # The owner of the resource share.
        # 
        # *   Self: your account. If you set the value to Self, the principals that are associated with your resource shares are queried.
        # *   OtherAccounts: another account. If you set the value to OtherAccounts, the resource shares with which your account is associated and the owners of the resource shares are queried.
        self.resource_owner = resource_owner
        self.resource_share_ids = resource_share_ids
        # The type of the shared resources.
        # 
        # For more information about the types of resources that can be shared, see [Services that work with Resource Sharing](~~450526~~).
        self.resource_type = resource_type
        self.targets = targets

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_owner is not None:
            result['ResourceOwner'] = self.resource_owner
        if self.resource_share_ids is not None:
            result['ResourceShareIds'] = self.resource_share_ids
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.targets is not None:
            result['Targets'] = self.targets
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceOwner') is not None:
            self.resource_owner = m.get('ResourceOwner')
        if m.get('ResourceShareIds') is not None:
            self.resource_share_ids = m.get('ResourceShareIds')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Targets') is not None:
            self.targets = m.get('Targets')
        return self


class ListSharedTargetsResponseBodySharedTargets(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        external: bool = None,
        resource_share_id: str = None,
        target_id: str = None,
        update_time: str = None,
    ):
        # The time when the principal was associated with the resource share.
        self.create_time = create_time
        # Indicates whether the principal is outside the resource directory. Valid values:
        # 
        # *   true: The principal is outside the resource directory.
        # *   false: The principal is in the resource directory.
        self.external = external
        # The ID of the resource share.
        self.resource_share_id = resource_share_id
        # The ID of the principal or resource owner.
        # 
        # *   If the value of `ResourceOwner` is `Self`, the value of this parameter is the ID of a principal.
        # *   If the value of `ResourceOwner` is `OtherAccounts`, the value of this parameter is the ID of a resource owner.
        self.target_id = target_id
        # The time when the association of the principal was updated.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.external is not None:
            result['External'] = self.external
        if self.resource_share_id is not None:
            result['ResourceShareId'] = self.resource_share_id
        if self.target_id is not None:
            result['TargetId'] = self.target_id
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('External') is not None:
            self.external = m.get('External')
        if m.get('ResourceShareId') is not None:
            self.resource_share_id = m.get('ResourceShareId')
        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListSharedTargetsResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        shared_targets: List[ListSharedTargetsResponseBodySharedTargets] = None,
    ):
        # The `token` that is used to initiate the next request. If the response of the current request is truncated, you can use the token to initiate another request and obtain the remaining records.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The information of the principals.
        self.shared_targets = shared_targets

    def validate(self):
        if self.shared_targets:
            for k in self.shared_targets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SharedTargets'] = []
        if self.shared_targets is not None:
            for k in self.shared_targets:
                result['SharedTargets'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.shared_targets = []
        if m.get('SharedTargets') is not None:
            for k in m.get('SharedTargets'):
                temp_model = ListSharedTargetsResponseBodySharedTargets()
                self.shared_targets.append(temp_model.from_map(k))
        return self


class ListSharedTargetsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSharedTargetsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListSharedTargetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RejectResourceShareInvitationRequest(TeaModel):
    def __init__(
        self,
        resource_share_invitation_id: str = None,
    ):
        # The ID of the invitation.
        self.resource_share_invitation_id = resource_share_invitation_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_share_invitation_id is not None:
            result['ResourceShareInvitationId'] = self.resource_share_invitation_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceShareInvitationId') is not None:
            self.resource_share_invitation_id = m.get('ResourceShareInvitationId')
        return self


class RejectResourceShareInvitationResponseBodyResourceShareInvitation(TeaModel):
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
        self.create_time = create_time
        self.receiver_account_id = receiver_account_id
        # The Alibaba Cloud account ID of the invitee.
        self.resource_share_id = resource_share_id
        # The Alibaba Cloud account ID of the inviter.
        self.resource_share_invitation_id = resource_share_invitation_id
        # The time when the invitation was created. The time is displayed in UTC.
        self.resource_share_name = resource_share_name
        # The status of the invitation. Valid values:
        # 
        # *   Pending: The invitation is waiting for confirmation.
        # *   Accepted: The invitation is accepted.
        # *   Cancelled: The invitation is canceled.
        # *   Rejected: The invitation is rejected.
        # *   Expired: The invitation has expired.
        self.sender_account_id = sender_account_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class RejectResourceShareInvitationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_share_invitation: RejectResourceShareInvitationResponseBodyResourceShareInvitation = None,
    ):
        # The ID of the resource share.
        self.request_id = request_id
        # The name of the resource share.
        self.resource_share_invitation = resource_share_invitation

    def validate(self):
        if self.resource_share_invitation:
            self.resource_share_invitation.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = RejectResourceShareInvitationResponseBodyResourceShareInvitation()
            self.resource_share_invitation = temp_model.from_map(m['ResourceShareInvitation'])
        return self


class RejectResourceShareInvitationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RejectResourceShareInvitationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RejectResourceShareInvitationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateResourceShareRequest(TeaModel):
    def __init__(
        self,
        allow_external_targets: bool = None,
        resource_share_id: str = None,
        resource_share_name: str = None,
    ):
        # The information of the resource share.
        self.allow_external_targets = allow_external_targets
        # Specifies whether resources in the resource share can be shared with accounts outside the resource directory. Valid values:
        # 
        # *   false: Resources in the resource share can be shared only with accounts in the resource directory.
        # *   true: Resources in the resource share can be shared with both accounts in the resource directory and accounts outside the resource directory.
        self.resource_share_id = resource_share_id
        # The ID of the request.
        self.resource_share_name = resource_share_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_external_targets is not None:
            result['AllowExternalTargets'] = self.allow_external_targets
        if self.resource_share_id is not None:
            result['ResourceShareId'] = self.resource_share_id
        if self.resource_share_name is not None:
            result['ResourceShareName'] = self.resource_share_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowExternalTargets') is not None:
            self.allow_external_targets = m.get('AllowExternalTargets')
        if m.get('ResourceShareId') is not None:
            self.resource_share_id = m.get('ResourceShareId')
        if m.get('ResourceShareName') is not None:
            self.resource_share_name = m.get('ResourceShareName')
        return self


class UpdateResourceShareResponseBodyResourceShare(TeaModel):
    def __init__(
        self,
        allow_external_targets: bool = None,
        create_time: str = None,
        resource_share_id: str = None,
        resource_share_name: str = None,
        resource_share_owner: str = None,
        resource_share_status: str = None,
        update_time: str = None,
    ):
        self.allow_external_targets = allow_external_targets
        # The status of the resource share. Valid values:
        # 
        # *   Active: The resource share is enabled.
        # *   Pending: The resource share is associated with one or more resource sharing invitations that are waiting for confirmation.
        # *   Deleting: The resource share is being deleted.
        # *   Deleted: The resource share is deleted.
        # 
        # >  The system deletes the records of resource shares in the Deleted state within 48 hours to 96 hours after you delete the resource shares.
        self.create_time = create_time
        # Indicates whether resources in the resource share can be shared with accounts outside the resource directory. Valid values:
        # 
        # *   false: Resources in the resource share can be shared only with accounts in the resource directory.
        # *   true: Resources in the resource share can be shared with both accounts in the resource directory and accounts outside the resource directory.
        self.resource_share_id = resource_share_id
        # The time when the resource share was created.
        self.resource_share_name = resource_share_name
        # The ID of the resource share.
        self.resource_share_owner = resource_share_owner
        self.resource_share_status = resource_share_status
        # The owner of the resource share.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_external_targets is not None:
            result['AllowExternalTargets'] = self.allow_external_targets
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.resource_share_id is not None:
            result['ResourceShareId'] = self.resource_share_id
        if self.resource_share_name is not None:
            result['ResourceShareName'] = self.resource_share_name
        if self.resource_share_owner is not None:
            result['ResourceShareOwner'] = self.resource_share_owner
        if self.resource_share_status is not None:
            result['ResourceShareStatus'] = self.resource_share_status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowExternalTargets') is not None:
            self.allow_external_targets = m.get('AllowExternalTargets')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ResourceShareId') is not None:
            self.resource_share_id = m.get('ResourceShareId')
        if m.get('ResourceShareName') is not None:
            self.resource_share_name = m.get('ResourceShareName')
        if m.get('ResourceShareOwner') is not None:
            self.resource_share_owner = m.get('ResourceShareOwner')
        if m.get('ResourceShareStatus') is not None:
            self.resource_share_status = m.get('ResourceShareStatus')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class UpdateResourceShareResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_share: UpdateResourceShareResponseBodyResourceShare = None,
    ):
        # The time when the resource share was updated.
        self.request_id = request_id
        # The name of the resource share.
        self.resource_share = resource_share

    def validate(self):
        if self.resource_share:
            self.resource_share.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_share is not None:
            result['ResourceShare'] = self.resource_share.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceShare') is not None:
            temp_model = UpdateResourceShareResponseBodyResourceShare()
            self.resource_share = temp_model.from_map(m['ResourceShare'])
        return self


class UpdateResourceShareResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateResourceShareResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateResourceShareResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


