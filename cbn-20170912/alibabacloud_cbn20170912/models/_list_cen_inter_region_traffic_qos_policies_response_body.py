# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cbn20170912 import models as main_models
from darabonba.model import DaraModel

class ListCenInterRegionTrafficQosPoliciesResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
        traffic_qos_policies: List[main_models.ListCenInterRegionTrafficQosPoliciesResponseBodyTrafficQosPolicies] = None,
    ):
        # The number of entries per page for a paged query.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results.
        # 
        # - If **NextToken** is empty, no next query exists.
        # - If **NextToken** is returned, the value indicates the token for the next query.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count
        # The list of traffic scheduling policies.
        self.traffic_qos_policies = traffic_qos_policies

    def validate(self):
        if self.traffic_qos_policies:
            for v1 in self.traffic_qos_policies:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['TrafficQosPolicies'] = []
        if self.traffic_qos_policies is not None:
            for k1 in self.traffic_qos_policies:
                result['TrafficQosPolicies'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.traffic_qos_policies = []
        if m.get('TrafficQosPolicies') is not None:
            for k1 in m.get('TrafficQosPolicies'):
                temp_model = main_models.ListCenInterRegionTrafficQosPoliciesResponseBodyTrafficQosPolicies()
                self.traffic_qos_policies.append(temp_model.from_map(k1))

        return self

class ListCenInterRegionTrafficQosPoliciesResponseBodyTrafficQosPolicies(DaraModel):
    def __init__(
        self,
        bandwidth_guarantee_mode: str = None,
        traffic_qos_policy_description: str = None,
        traffic_qos_policy_id: str = None,
        traffic_qos_policy_name: str = None,
        traffic_qos_policy_status: str = None,
        traffic_qos_queues: List[main_models.ListCenInterRegionTrafficQosPoliciesResponseBodyTrafficQosPoliciesTrafficQosQueues] = None,
        transit_router_attachment_id: str = None,
        transit_router_id: str = None,
    ):
        # The bandwidth guarantee type. Valid values:
        # - **byBandwidth**: configures QoS queues by absolute bandwidth value.
        # - **byBandwidthPercent**: configures QoS queues by bandwidth percentage.
        self.bandwidth_guarantee_mode = bandwidth_guarantee_mode
        # The description of the traffic scheduling policy.
        self.traffic_qos_policy_description = traffic_qos_policy_description
        # The ID of the traffic scheduling policy.
        self.traffic_qos_policy_id = traffic_qos_policy_id
        # The name of the traffic scheduling policy.
        self.traffic_qos_policy_name = traffic_qos_policy_name
        # The status of the traffic scheduling policy.
        # 
        # - **Creating**: being created.
        # - **Active**: active.
        # - **Modifying**: being modified.
        # - **Deleting**: being deleted.
        self.traffic_qos_policy_status = traffic_qos_policy_status
        # The list of queues.
        self.traffic_qos_queues = traffic_qos_queues
        # The ID of the network instance connection.
        self.transit_router_attachment_id = transit_router_attachment_id
        # The transit router instance ID.
        self.transit_router_id = transit_router_id

    def validate(self):
        if self.traffic_qos_queues:
            for v1 in self.traffic_qos_queues:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth_guarantee_mode is not None:
            result['BandwidthGuaranteeMode'] = self.bandwidth_guarantee_mode

        if self.traffic_qos_policy_description is not None:
            result['TrafficQosPolicyDescription'] = self.traffic_qos_policy_description

        if self.traffic_qos_policy_id is not None:
            result['TrafficQosPolicyId'] = self.traffic_qos_policy_id

        if self.traffic_qos_policy_name is not None:
            result['TrafficQosPolicyName'] = self.traffic_qos_policy_name

        if self.traffic_qos_policy_status is not None:
            result['TrafficQosPolicyStatus'] = self.traffic_qos_policy_status

        result['TrafficQosQueues'] = []
        if self.traffic_qos_queues is not None:
            for k1 in self.traffic_qos_queues:
                result['TrafficQosQueues'].append(k1.to_map() if k1 else None)

        if self.transit_router_attachment_id is not None:
            result['TransitRouterAttachmentId'] = self.transit_router_attachment_id

        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandwidthGuaranteeMode') is not None:
            self.bandwidth_guarantee_mode = m.get('BandwidthGuaranteeMode')

        if m.get('TrafficQosPolicyDescription') is not None:
            self.traffic_qos_policy_description = m.get('TrafficQosPolicyDescription')

        if m.get('TrafficQosPolicyId') is not None:
            self.traffic_qos_policy_id = m.get('TrafficQosPolicyId')

        if m.get('TrafficQosPolicyName') is not None:
            self.traffic_qos_policy_name = m.get('TrafficQosPolicyName')

        if m.get('TrafficQosPolicyStatus') is not None:
            self.traffic_qos_policy_status = m.get('TrafficQosPolicyStatus')

        self.traffic_qos_queues = []
        if m.get('TrafficQosQueues') is not None:
            for k1 in m.get('TrafficQosQueues'):
                temp_model = main_models.ListCenInterRegionTrafficQosPoliciesResponseBodyTrafficQosPoliciesTrafficQosQueues()
                self.traffic_qos_queues.append(temp_model.from_map(k1))

        if m.get('TransitRouterAttachmentId') is not None:
            self.transit_router_attachment_id = m.get('TransitRouterAttachmentId')

        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')

        return self

class ListCenInterRegionTrafficQosPoliciesResponseBodyTrafficQosPoliciesTrafficQosQueues(DaraModel):
    def __init__(
        self,
        bandwidth: str = None,
        dscps: List[int] = None,
        effective_bandwidth: str = None,
        qos_queue_description: str = None,
        qos_queue_id: str = None,
        qos_queue_name: str = None,
        remain_bandwidth_percent: int = None,
    ):
        # The inter-region bandwidth allocated to the current queue when the bandwidth guarantee type is set to the absolute value mode.
        self.bandwidth = bandwidth
        # The DSCP values of the traffic packets to be matched by the current queue.
        self.dscps = dscps
        # The actual effective bandwidth of the current queue.
        self.effective_bandwidth = effective_bandwidth
        # The description of the queue.
        self.qos_queue_description = qos_queue_description
        # The ID of the queue.
        self.qos_queue_id = qos_queue_id
        # The name of the queue.
        self.qos_queue_name = qos_queue_name
        # The percentage of inter-region bandwidth occupied by the current queue when the bandwidth guarantee type is set to the percentage mode.
        self.remain_bandwidth_percent = remain_bandwidth_percent

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.dscps is not None:
            result['Dscps'] = self.dscps

        if self.effective_bandwidth is not None:
            result['EffectiveBandwidth'] = self.effective_bandwidth

        if self.qos_queue_description is not None:
            result['QosQueueDescription'] = self.qos_queue_description

        if self.qos_queue_id is not None:
            result['QosQueueId'] = self.qos_queue_id

        if self.qos_queue_name is not None:
            result['QosQueueName'] = self.qos_queue_name

        if self.remain_bandwidth_percent is not None:
            result['RemainBandwidthPercent'] = self.remain_bandwidth_percent

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('Dscps') is not None:
            self.dscps = m.get('Dscps')

        if m.get('EffectiveBandwidth') is not None:
            self.effective_bandwidth = m.get('EffectiveBandwidth')

        if m.get('QosQueueDescription') is not None:
            self.qos_queue_description = m.get('QosQueueDescription')

        if m.get('QosQueueId') is not None:
            self.qos_queue_id = m.get('QosQueueId')

        if m.get('QosQueueName') is not None:
            self.qos_queue_name = m.get('QosQueueName')

        if m.get('RemainBandwidthPercent') is not None:
            self.remain_bandwidth_percent = m.get('RemainBandwidthPercent')

        return self

