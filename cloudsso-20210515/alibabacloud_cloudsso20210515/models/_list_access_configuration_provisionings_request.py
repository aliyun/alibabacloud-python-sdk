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
        # The access configuration ID used as a filter condition for the query.
        self.access_configuration_id = access_configuration_id
        # The directory ID.
        self.directory_id = directory_id
        # The maximum number of entries to return on each page.
        # 
        # Valid values: 1 to 20.
        # 
        # Default value: 10.
        self.max_results = max_results
        # The token used to return the next page of query results. You do not need to specify NextToken when you call this operation for the first time.
        # 
        # When you call this operation for the first time, if the total number of returned entries exceeds the value of MaxResults, the returned results are truncated. Only the number of entries specified by MaxResults is returned, the IsTruncated parameter is set to true, and a NextToken is returned. You can use the returned NextToken to call this operation again to query the truncated entries while keeping other request parameters unchanged. You can repeat this process until IsTruncated is set to false, which indicates that all entries are returned.
        self.next_token = next_token
        # The Alibaba Cloud account ID of the provisioning target.
        self.origin_target_id = origin_target_id
        # The provisioning status used as a filter condition for the query. Valid values:
        # 
        # - Provisioned: The provisioning succeeded.
        # - ReprovisionRequired: Reprovisioning is required.
        # - DeprovisionFailed: The provisioning failed.
        self.provisioning_status = provisioning_status
        # The target ID used as a filter condition for the query.
        # 
        # > You must specify both TargetId and TargetType for them to take effect as filter conditions.
        self.target_id = target_id
        # The target type used as a filter condition for the query.
        # 
        # Valid values:
        # - RD-Account: The target is an account in a resource directory.
        # 
        # > You must specify both TargetId and TargetType for them to take effect as filter conditions.
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

