# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class ListTrafficMirrorSessionsRequest(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        max_results: int = None,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        priority: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tags: List[main_models.ListTrafficMirrorSessionsRequestTags] = None,
        traffic_mirror_filter_id: str = None,
        traffic_mirror_session_ids: List[str] = None,
        traffic_mirror_session_name: str = None,
        traffic_mirror_source_id: str = None,
        traffic_mirror_target_id: str = None,
        virtual_network_id: int = None,
    ):
        # Specifies whether the traffic mirror session is enabled. Valid values:
        # 
        # - **false** (default): The traffic mirror session is not enabled.
        # 
        # - **true**: The traffic mirror session is enabled.
        self.enabled = enabled
        # The maximum number of entries to return in this query. Valid values: **1** to **100**. Default value: **10**.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. Valid values:
        # - You do not need to specify this parameter for the first request or if no next query exists.
        # - If a next query exists, set the value to the NextToken value returned in the previous API call.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The priority of traffic mirror session. Valid values: **1** to **32766**.
        # 
        # A smaller value indicates a higher priority. The priority of traffic mirror session created by the same account in the same region must be unique.
        self.priority = priority
        # The region ID of the traffic mirror session. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the region ID. For information about the regions that support traffic mirroring, see [Traffic mirroring overview](https://help.aliyun.com/document_detail/207513.html).
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the traffic mirroring session belongs.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The tags.
        self.tags = tags
        # The instance ID of the traffic mirror filter.
        self.traffic_mirror_filter_id = traffic_mirror_filter_id
        # The instance IDs of traffic mirror sessions. The maximum value of **N** is **100**, which means you can query up to 100 traffic mirror sessions.
        self.traffic_mirror_session_ids = traffic_mirror_session_ids
        # The name of the traffic mirror session.
        # 
        # The name must be 1 to 128 characters in length and cannot start with `http://` or `https://`.
        self.traffic_mirror_session_name = traffic_mirror_session_name
        # The instance ID of the traffic mirror source. Currently, elastic network interfaces (ENIs) are supported as traffic mirror sources.
        self.traffic_mirror_source_id = traffic_mirror_source_id
        # The instance ID of the traffic mirror destination. Currently, elastic network interfaces (ENIs) and internal-facing SLB instances are supported as traffic mirror destinations. Elastic network interfaces are also referred to as network interface controllers (NICs).
        self.traffic_mirror_target_id = traffic_mirror_target_id
        # The Virtual Network Identifier (VNI) used to distinguish different mirrored data. Valid values: **0** to **16777215**. You can use the VNI to identify mirrored data from different sessions at the traffic mirror destination. You can specify a custom VNI value or let the system randomly assign one. To let the system randomly assign a value, do not specify this parameter.
        self.virtual_network_id = virtual_network_id

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.traffic_mirror_filter_id is not None:
            result['TrafficMirrorFilterId'] = self.traffic_mirror_filter_id

        if self.traffic_mirror_session_ids is not None:
            result['TrafficMirrorSessionIds'] = self.traffic_mirror_session_ids

        if self.traffic_mirror_session_name is not None:
            result['TrafficMirrorSessionName'] = self.traffic_mirror_session_name

        if self.traffic_mirror_source_id is not None:
            result['TrafficMirrorSourceId'] = self.traffic_mirror_source_id

        if self.traffic_mirror_target_id is not None:
            result['TrafficMirrorTargetId'] = self.traffic_mirror_target_id

        if self.virtual_network_id is not None:
            result['VirtualNetworkId'] = self.virtual_network_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListTrafficMirrorSessionsRequestTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TrafficMirrorFilterId') is not None:
            self.traffic_mirror_filter_id = m.get('TrafficMirrorFilterId')

        if m.get('TrafficMirrorSessionIds') is not None:
            self.traffic_mirror_session_ids = m.get('TrafficMirrorSessionIds')

        if m.get('TrafficMirrorSessionName') is not None:
            self.traffic_mirror_session_name = m.get('TrafficMirrorSessionName')

        if m.get('TrafficMirrorSourceId') is not None:
            self.traffic_mirror_source_id = m.get('TrafficMirrorSourceId')

        if m.get('TrafficMirrorTargetId') is not None:
            self.traffic_mirror_target_id = m.get('TrafficMirrorTargetId')

        if m.get('VirtualNetworkId') is not None:
            self.virtual_network_id = m.get('VirtualNetworkId')

        return self

class ListTrafficMirrorSessionsRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the resource. You can specify up to 20 tag keys. The tag key cannot be an empty string.
        # 
        # The tag key can be up to 128 characters in length and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
        self.key = key
        # The tag value of the resource. You can specify up to 20 tag values. The tag value can be an empty string.
        # 
        # The tag value can be up to 128 characters in length and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

