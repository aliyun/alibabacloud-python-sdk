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
        # The ID of the access configuration.
        self.access_configuration_id = access_configuration_id
        # Specifies whether to de-provision the access configuration when you remove the access permissions from the CloudSSO identity. The access configuration is used to assign the access permissions, and the identity is the only one that uses the access configuration and is associated with the account. Valid values:
        # 
        # - DeprovisionForLastAccessAssignmentOnAccount: de-provisions the access configuration.
        # 
        # - None: does not de-provision the access configuration. This is the default value.
        self.deprovision_strategy = deprovision_strategy
        # The ID of the directory.
        self.directory_id = directory_id
        self.origin_target_id = origin_target_id
        # The ID of the CloudSSO identity.
        # 
        # - If you set `PrincipalType` to `User`, set `PrincipalId` to the ID of the CloudSSO user.
        # 
        # - If you set `PrincipalType` to `Group`, set `PrincipalId` to the ID of the CloudSSO group.
        self.principal_id = principal_id
        # The type of the CloudSSO identity. Valid values:
        # 
        # - User
        # 
        # - Group
        self.principal_type = principal_type
        # The ID of the task object.
        self.target_id = target_id
        # The type of the task object. Set the value to RD-Account, which specifies the accounts in the resource directory.
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

