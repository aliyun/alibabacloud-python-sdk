# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class ListTrafficMirrorSessionsResponseBody(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        total_count: str = None,
        traffic_mirror_sessions: List[main_models.ListTrafficMirrorSessionsResponseBodyTrafficMirrorSessions] = None,
    ):
        # The token that is used for the next query. Valid values:
        # 
        # *   If no value is returned for **NextToken**, no next queries are sent.
        # *   If a value of **NextToken** is returned, the value is the token that is used for the subsequent query.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count
        # The details about the traffic mirror session.
        self.traffic_mirror_sessions = traffic_mirror_sessions

    def validate(self):
        if self.traffic_mirror_sessions:
            for v1 in self.traffic_mirror_sessions:
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

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['TrafficMirrorSessions'] = []
        if self.traffic_mirror_sessions is not None:
            for k1 in self.traffic_mirror_sessions:
                result['TrafficMirrorSessions'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.traffic_mirror_sessions = []
        if m.get('TrafficMirrorSessions') is not None:
            for k1 in m.get('TrafficMirrorSessions'):
                temp_model = main_models.ListTrafficMirrorSessionsResponseBodyTrafficMirrorSessions()
                self.traffic_mirror_sessions.append(temp_model.from_map(k1))

        return self

class ListTrafficMirrorSessionsResponseBodyTrafficMirrorSessions(DaraModel):
    def __init__(
        self,
        creation_time: str = None,
        enabled: bool = None,
        packet_length: int = None,
        priority: int = None,
        resource_group_id: str = None,
        tags: List[main_models.ListTrafficMirrorSessionsResponseBodyTrafficMirrorSessionsTags] = None,
        traffic_mirror_filter_id: str = None,
        traffic_mirror_session_business_status: str = None,
        traffic_mirror_session_description: str = None,
        traffic_mirror_session_id: str = None,
        traffic_mirror_session_name: str = None,
        traffic_mirror_session_status: str = None,
        traffic_mirror_source_ids: List[str] = None,
        traffic_mirror_target_id: str = None,
        traffic_mirror_target_type: str = None,
        virtual_network_id: int = None,
    ):
        # The time when the session is created.
        self.creation_time = creation_time
        # Indicates whether the traffic mirror session was enabled.
        # 
        # *   **false** 
        # *   **true**
        self.enabled = enabled
        # The maximum transmission unit.
        self.packet_length = packet_length
        # The priority of the traffic mirror session.
        # 
        # A smaller value indicates a higher priority.
        self.priority = priority
        # The ID of the resource group to which the traffic mirror session belongs.
        self.resource_group_id = resource_group_id
        # The tag list.
        self.tags = tags
        # The ID of the filter.
        self.traffic_mirror_filter_id = traffic_mirror_filter_id
        # The status of the traffic mirror session.
        # 
        # *   **Normal**
        # *   **FinancialLocked**
        self.traffic_mirror_session_business_status = traffic_mirror_session_business_status
        # The description of the traffic mirror session.
        self.traffic_mirror_session_description = traffic_mirror_session_description
        # The ID of the traffic mirror session.
        self.traffic_mirror_session_id = traffic_mirror_session_id
        # The name of the traffic mirror session.
        self.traffic_mirror_session_name = traffic_mirror_session_name
        # The status of the traffic mirror session. Valid values:
        # 
        # *   **Creating**
        # *   **Created**
        # *   **Modifying**
        # *   **Deleting**
        self.traffic_mirror_session_status = traffic_mirror_session_status
        # The ID of the traffic mirror source.
        self.traffic_mirror_source_ids = traffic_mirror_source_ids
        # The ID of the traffic mirror destination.
        self.traffic_mirror_target_id = traffic_mirror_target_id
        # The type of the traffic mirror destination. Valid values:
        # 
        # *   **NetworkInterface**: an elastic network interface (ENI)
        # *   **SLB**: an internal-facing Server Load Balancer (SLB) instance
        self.traffic_mirror_target_type = traffic_mirror_target_type
        # You can specify VNIs to distinguish different mirrored traffic.
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
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.packet_length is not None:
            result['PacketLength'] = self.packet_length

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.traffic_mirror_filter_id is not None:
            result['TrafficMirrorFilterId'] = self.traffic_mirror_filter_id

        if self.traffic_mirror_session_business_status is not None:
            result['TrafficMirrorSessionBusinessStatus'] = self.traffic_mirror_session_business_status

        if self.traffic_mirror_session_description is not None:
            result['TrafficMirrorSessionDescription'] = self.traffic_mirror_session_description

        if self.traffic_mirror_session_id is not None:
            result['TrafficMirrorSessionId'] = self.traffic_mirror_session_id

        if self.traffic_mirror_session_name is not None:
            result['TrafficMirrorSessionName'] = self.traffic_mirror_session_name

        if self.traffic_mirror_session_status is not None:
            result['TrafficMirrorSessionStatus'] = self.traffic_mirror_session_status

        if self.traffic_mirror_source_ids is not None:
            result['TrafficMirrorSourceIds'] = self.traffic_mirror_source_ids

        if self.traffic_mirror_target_id is not None:
            result['TrafficMirrorTargetId'] = self.traffic_mirror_target_id

        if self.traffic_mirror_target_type is not None:
            result['TrafficMirrorTargetType'] = self.traffic_mirror_target_type

        if self.virtual_network_id is not None:
            result['VirtualNetworkId'] = self.virtual_network_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('PacketLength') is not None:
            self.packet_length = m.get('PacketLength')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListTrafficMirrorSessionsResponseBodyTrafficMirrorSessionsTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TrafficMirrorFilterId') is not None:
            self.traffic_mirror_filter_id = m.get('TrafficMirrorFilterId')

        if m.get('TrafficMirrorSessionBusinessStatus') is not None:
            self.traffic_mirror_session_business_status = m.get('TrafficMirrorSessionBusinessStatus')

        if m.get('TrafficMirrorSessionDescription') is not None:
            self.traffic_mirror_session_description = m.get('TrafficMirrorSessionDescription')

        if m.get('TrafficMirrorSessionId') is not None:
            self.traffic_mirror_session_id = m.get('TrafficMirrorSessionId')

        if m.get('TrafficMirrorSessionName') is not None:
            self.traffic_mirror_session_name = m.get('TrafficMirrorSessionName')

        if m.get('TrafficMirrorSessionStatus') is not None:
            self.traffic_mirror_session_status = m.get('TrafficMirrorSessionStatus')

        if m.get('TrafficMirrorSourceIds') is not None:
            self.traffic_mirror_source_ids = m.get('TrafficMirrorSourceIds')

        if m.get('TrafficMirrorTargetId') is not None:
            self.traffic_mirror_target_id = m.get('TrafficMirrorTargetId')

        if m.get('TrafficMirrorTargetType') is not None:
            self.traffic_mirror_target_type = m.get('TrafficMirrorTargetType')

        if m.get('VirtualNetworkId') is not None:
            self.virtual_network_id = m.get('VirtualNetworkId')

        return self

class ListTrafficMirrorSessionsResponseBodyTrafficMirrorSessionsTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
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

