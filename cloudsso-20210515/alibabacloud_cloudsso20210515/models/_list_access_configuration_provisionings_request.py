# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAccessConfigurationProvisioningsRequest(DaraModel):
    def __init__(
        self,
        access_configuration_id: str = None,
        directory_id: str = None,
        max_results: int = None,
        next_token: str = None,
        origin_target_id: str = None,
        provisioning_status: str = None,
        target_id: str = None,
        target_type: str = None,
    ):
        # The ID of the access configuration. The ID can be used to filter access permissions.
        self.access_configuration_id = access_configuration_id
        # The ID of the directory.
        self.directory_id = directory_id
        # The maximum number of entries per page.
        # 
        # Valid values: 1 to 20.
        # 
        # Default value: 10.
        self.max_results = max_results
        # The returned value of NextToken is a pagination token, which can be used in the next request to retrieve a new page of results. If this is your first time to call this operation, you do not need to specify the `NextToken` parameter.
        # 
        # When you call this operation for the first time, if the total number of entries to return exceeds the value of `MaxResults`, the entries are truncated. Only the entries that match the value of `MaxResults` are returned, and the excess entries are not returned. In this case, the value of the response parameter `IsTruncated` is `true`, and `NextToken` is returned. In the next call, you can use the value of `NextToken` and maintain the settings of the other request parameters to query the excess entries. You can repeat the call until the value of `IsTruncated` becomes `false`. This way, all entries are returned.
        self.next_token = next_token
        self.origin_target_id = origin_target_id
        # The status of the access configuration. The value can be used to filter accounts. Valid values:
        # 
        # - Provisioned: The access configuration is provisioned.
        # 
        # - ReprovisionRequired: The access configuration needs to be re-provisioned.
        # 
        # - DeprovisionFailed: The access configuration failed to be provisioned.
        self.provisioning_status = provisioning_status
        # The ID of the task object. The ID can be used to filter access permissions.
        # 
        # > You can use the type to filter access permissions only if you specify both `TargetId` and `TargetType`.
        self.target_id = target_id
        # The type of the task object. The type can be used to filter access permissions.
        # 
        # Set the value to RD-Account, which specifies the accounts in the resource directory.
        # 
        # > You can use the type to filter access permissions only if you specify both `TargetId` and `TargetType`.
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

        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.origin_target_id is not None:
            result['OriginTargetId'] = self.origin_target_id

        if self.provisioning_status is not None:
            result['ProvisioningStatus'] = self.provisioning_status

        if self.target_id is not None:
            result['TargetId'] = self.target_id

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessConfigurationId') is not None:
            self.access_configuration_id = m.get('AccessConfigurationId')

        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OriginTargetId') is not None:
            self.origin_target_id = m.get('OriginTargetId')

        if m.get('ProvisioningStatus') is not None:
            self.provisioning_status = m.get('ProvisioningStatus')

        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        return self

