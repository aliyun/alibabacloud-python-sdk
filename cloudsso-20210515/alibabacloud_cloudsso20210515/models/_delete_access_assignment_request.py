# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteAccessAssignmentRequest(DaraModel):
    def __init__(
        self,
        access_configuration_id: str = None,
        deprovision_strategy: str = None,
        directory_id: str = None,
        origin_target_id: str = None,
        principal_id: str = None,
        principal_type: str = None,
        target_id: str = None,
        target_type: str = None,
    ):
        # The access configuration ID.
        self.access_configuration_id = access_configuration_id
        # Specifies whether to remove the deployment of the access configuration provisioning when you remove the last authorization that uses the access configuration on an account in a resource directory. Valid values:
        # 
        # - DeprovisionForLastAccessAssignmentOnAccount: removes the deployment of the access configuration provisioning.
        # - None: does not remove the deployment of the access configuration provisioning. Default value.
        self.deprovision_strategy = deprovision_strategy
        # The directory ID.
        self.directory_id = directory_id
        # The ID of the Alibaba Cloud account to which the authorization target belongs.
        self.origin_target_id = origin_target_id
        # The CloudSSO identity ID. Details:
        # 
        # - If PrincipalType is set to User, PrincipalId is the CloudSSO user ID.
        # - If PrincipalType is set to Group, PrincipalId is the CloudSSO group ID.
        self.principal_id = principal_id
        # The CloudSSO identity type. Valid values:
        # 
        # - User: user.
        # - Group: group.
        self.principal_type = principal_type
        # The ID of the task target.
        self.target_id = target_id
        # The type of the task target. Valid values:
        # - RD-Account: an account in a resource directory.
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_configuration_id is not None:
            result['AccessConfigurationId'] = self.access_configuration_id

        if self.deprovision_strategy is not None:
            result['DeprovisionStrategy'] = self.deprovision_strategy

        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.origin_target_id is not None:
            result['OriginTargetId'] = self.origin_target_id

        if self.principal_id is not None:
            result['PrincipalId'] = self.principal_id

        if self.principal_type is not None:
            result['PrincipalType'] = self.principal_type

        if self.target_id is not None:
            result['TargetId'] = self.target_id

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessConfigurationId') is not None:
            self.access_configuration_id = m.get('AccessConfigurationId')

        if m.get('DeprovisionStrategy') is not None:
            self.deprovision_strategy = m.get('DeprovisionStrategy')

        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('OriginTargetId') is not None:
            self.origin_target_id = m.get('OriginTargetId')

        if m.get('PrincipalId') is not None:
            self.principal_id = m.get('PrincipalId')

        if m.get('PrincipalType') is not None:
            self.principal_type = m.get('PrincipalType')

        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        return self

