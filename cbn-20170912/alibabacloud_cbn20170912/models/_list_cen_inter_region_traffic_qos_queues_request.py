# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cbn20170912 import models as main_models
from darabonba.model import DaraModel

class ListCenInterRegionTrafficQosQueuesRequest(DaraModel):
    def __init__(
        self,
        effective_bandwidth_filter: main_models.ListCenInterRegionTrafficQosQueuesRequestEffectiveBandwidthFilter = None,
        max_results: int = None,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        traffic_qos_policy_id: str = None,
        traffic_qos_queue_description: str = None,
        traffic_qos_queue_id: str = None,
        traffic_qos_queue_name: str = None,
        transit_router_attachment_id: str = None,
        transit_router_id: str = None,
    ):
        # The filter works based on the actual bandwidth. Enter a positive integer. Unit: Mbit/s.
        self.effective_bandwidth_filter = effective_bandwidth_filter
        # The number of entries to return on each page. Valid values: **1** to **100**. Default value: **20**.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results.
        # 
        # *   If **NextToken** is empty, no next page exists.
        # *   If a value of **NextToken** is returned, the value indicates the token that is used for the next query.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the QoS policy.
        self.traffic_qos_policy_id = traffic_qos_policy_id
        # The description of the QoS queue.
        # 
        # This parameter is optional. If you enter a description, it must be 1 to 256 characters in length and cannot start with http:// or https://.
        self.traffic_qos_queue_description = traffic_qos_queue_description
        # The ID of the queue.
        self.traffic_qos_queue_id = traffic_qos_queue_id
        # The name of the QoS queue.
        # 
        # The name must be 1 to 128 characters in length, and cannot start with http:// or https://.
        self.traffic_qos_queue_name = traffic_qos_queue_name
        # The ID of the inter-region connection.
        self.transit_router_attachment_id = transit_router_attachment_id
        # The ID of the transit router.
        self.transit_router_id = transit_router_id

    def validate(self):
        if self.effective_bandwidth_filter:
            self.effective_bandwidth_filter.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.effective_bandwidth_filter is not None:
            result['EffectiveBandwidthFilter'] = self.effective_bandwidth_filter.to_map()

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

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
        if m.get('EffectiveBandwidthFilter') is not None:
            temp_model = main_models.ListCenInterRegionTrafficQosQueuesRequestEffectiveBandwidthFilter()
            self.effective_bandwidth_filter = temp_model.from_map(m.get('EffectiveBandwidthFilter'))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

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

class ListCenInterRegionTrafficQosQueuesRequestEffectiveBandwidthFilter(DaraModel):
    def __init__(
        self,
        gte: int = None,
        lte: int = None,
    ):
        # The actual bandwidth is equal to or larger than the specified value.
        self.gte = gte
        # The actual bandwidth is equal to or smaller than the specified value.
        self.lte = lte

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gte is not None:
            result['Gte'] = self.gte

        if self.lte is not None:
            result['Lte'] = self.lte

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Gte') is not None:
            self.gte = m.get('Gte')

        if m.get('Lte') is not None:
            self.lte = m.get('Lte')

        return self

