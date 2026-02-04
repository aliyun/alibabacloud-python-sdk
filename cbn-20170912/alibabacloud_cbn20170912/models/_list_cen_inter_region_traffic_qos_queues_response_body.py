# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cbn20170912 import models as main_models
from darabonba.model import DaraModel

class ListCenInterRegionTrafficQosQueuesResponseBody(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        traffic_qos_queues: List[main_models.ListCenInterRegionTrafficQosQueuesResponseBodyTrafficQosQueues] = None,
    ):
        # A pagination token. It can be used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If **NextToken** is empty, no next page exists.
        # *   If a value of **NextToken** is returned, the value indicates the token that is used for the next query.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The information about the QoS queue.
        self.traffic_qos_queues = traffic_qos_queues

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
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['TrafficQosQueues'] = []
        if self.traffic_qos_queues is not None:
            for k1 in self.traffic_qos_queues:
                result['TrafficQosQueues'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.traffic_qos_queues = []
        if m.get('TrafficQosQueues') is not None:
            for k1 in m.get('TrafficQosQueues'):
                temp_model = main_models.ListCenInterRegionTrafficQosQueuesResponseBodyTrafficQosQueues()
                self.traffic_qos_queues.append(temp_model.from_map(k1))

        return self

class ListCenInterRegionTrafficQosQueuesResponseBodyTrafficQosQueues(DaraModel):
    def __init__(
        self,
        bandwidth: str = None,
        dscps: List[int] = None,
        effective_bandwidth: str = None,
        remain_bandwidth_percent: int = None,
        status: str = None,
        traffic_qos_policy_id: str = None,
        traffic_qos_queue_description: str = None,
        traffic_qos_queue_id: str = None,
        traffic_qos_queue_name: str = None,
        transit_router_attachment_id: str = None,
        transit_router_id: str = None,
    ):
        # The absolute bandwidth value that can be allocated to the current queue.
        # 
        # A value of **1** indicates that the QoS queue can consume at most 1 Mbit/s of inter-region bandwidth.
        self.bandwidth = bandwidth
        # The Differentiated Services Code Point (DSCP) value that matches the current QoS queue.
        self.dscps = dscps
        # The actual bandwidth of the current queue.
        self.effective_bandwidth = effective_bandwidth
        # The percentage of bandwidth that can be allocated to the current queue.
        # 
        # A value of **1** indicates that the QoS queue can consume at most 1% of the inter-region bandwidth.
        self.remain_bandwidth_percent = remain_bandwidth_percent
        # The status of the QoS queue. Valid values:
        # 
        # *   **Creating**
        # *   **Active**
        # *   **Deleting**
        self.status = status
        # The ID of the QoS policy.
        self.traffic_qos_policy_id = traffic_qos_policy_id
        # The description of the QoS queue.
        self.traffic_qos_queue_description = traffic_qos_queue_description
        # The ID of the QoS queue.
        self.traffic_qos_queue_id = traffic_qos_queue_id
        # The name of the QoS queue.
        self.traffic_qos_queue_name = traffic_qos_queue_name
        # The ID of the inter-region connection.
        self.transit_router_attachment_id = transit_router_attachment_id
        # The ID of the transit router.
        self.transit_router_id = transit_router_id

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

        if self.remain_bandwidth_percent is not None:
            result['RemainBandwidthPercent'] = self.remain_bandwidth_percent

        if self.status is not None:
            result['Status'] = self.status

        if self.traffic_qos_policy_id is not None:
            result['TrafficQosPolicyId'] = self.traffic_qos_policy_id

        if self.traffic_qos_queue_description is not None:
            result['TrafficQosQueueDescription'] = self.traffic_qos_queue_description

        if self.traffic_qos_queue_id is not None:
            result['TrafficQosQueueId'] = self.traffic_qos_queue_id

        if self.traffic_qos_queue_name is not None:
            result['TrafficQosQueueName'] = self.traffic_qos_queue_name

        if self.transit_router_attachment_id is not None:
            result['TransitRouterAttachmentId'] = self.transit_router_attachment_id

        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('Dscps') is not None:
            self.dscps = m.get('Dscps')

        if m.get('EffectiveBandwidth') is not None:
            self.effective_bandwidth = m.get('EffectiveBandwidth')

        if m.get('RemainBandwidthPercent') is not None:
            self.remain_bandwidth_percent = m.get('RemainBandwidthPercent')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TrafficQosPolicyId') is not None:
            self.traffic_qos_policy_id = m.get('TrafficQosPolicyId')

        if m.get('TrafficQosQueueDescription') is not None:
            self.traffic_qos_queue_description = m.get('TrafficQosQueueDescription')

        if m.get('TrafficQosQueueId') is not None:
            self.traffic_qos_queue_id = m.get('TrafficQosQueueId')

        if m.get('TrafficQosQueueName') is not None:
            self.traffic_qos_queue_name = m.get('TrafficQosQueueName')

        if m.get('TransitRouterAttachmentId') is not None:
            self.transit_router_attachment_id = m.get('TransitRouterAttachmentId')

        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')

        return self

