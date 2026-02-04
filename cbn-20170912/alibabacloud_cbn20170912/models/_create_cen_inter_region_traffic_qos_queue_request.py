# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateCenInterRegionTrafficQosQueueRequest(DaraModel):
    def __init__(
        self,
        bandwidth: int = None,
        client_token: str = None,
        dry_run: bool = None,
        dscps: List[int] = None,
        owner_account: str = None,
        owner_id: int = None,
        qos_queue_description: str = None,
        qos_queue_name: str = None,
        remain_bandwidth_percent: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        traffic_qos_policy_id: str = None,
    ):
        # The maximum absolute bandwidth value that can be allocated to the queue. Unit: Mbit/s.
        # 
        # - The value specifies an absolute bandwidth. For example, a value of 20 specifies that the queue can consume at most 20 Mbit/s of bandwidth.
        # - The sum of the bandwidth values specified for all queues that belong to the same inter-region connection cannot exceed the maximum bandwidth of the inter-region connection.
        self.bandwidth = bandwidth
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform a dry run. Valid values:
        # 
        # - **true**: performs a dry run. The system checks the required parameters, the request format, and the service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # - **false** (default): performs a dry run and sends the request.
        self.dry_run = dry_run
        # The differentiated services code point (DSCP) value that matches the current queue.
        # 
        # You can specify at most 20 DSCP values for a queue in each call. Separate DSCP values with commas (,).
        # 
        # This parameter is required.
        self.dscps = dscps
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The description of the queue.
        # 
        # This parameter is optional. If you enter a description, it must be 1 to 256 characters in length and cannot start with http:// or https://.
        self.qos_queue_description = qos_queue_description
        # The name of the queue.
        # 
        # The name can be empty or 1 to 128 characters in length, and cannot start with http:// or https://.
        self.qos_queue_name = qos_queue_name
        # The maximum percentage of inter-region bandwidth that can be allocated to the queue.
        # 
        # - Unit: percentage. For example, a value of 20 specifies that the queue can consume at most 20% of inter-region bandwidth.
        # - The sum of the percentage values specified for all queues that belong to the same inter-region connection cannot exceed 100%.
        self.remain_bandwidth_percent = remain_bandwidth_percent
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the QoS policy.
        # 
        # This parameter is required.
        self.traffic_qos_policy_id = traffic_qos_policy_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.dscps is not None:
            result['Dscps'] = self.dscps

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.qos_queue_description is not None:
            result['QosQueueDescription'] = self.qos_queue_description

        if self.qos_queue_name is not None:
            result['QosQueueName'] = self.qos_queue_name

        if self.remain_bandwidth_percent is not None:
            result['RemainBandwidthPercent'] = self.remain_bandwidth_percent

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.traffic_qos_policy_id is not None:
            result['TrafficQosPolicyId'] = self.traffic_qos_policy_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('Dscps') is not None:
            self.dscps = m.get('Dscps')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('QosQueueDescription') is not None:
            self.qos_queue_description = m.get('QosQueueDescription')

        if m.get('QosQueueName') is not None:
            self.qos_queue_name = m.get('QosQueueName')

        if m.get('RemainBandwidthPercent') is not None:
            self.remain_bandwidth_percent = m.get('RemainBandwidthPercent')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('TrafficQosPolicyId') is not None:
            self.traffic_qos_policy_id = m.get('TrafficQosPolicyId')

        return self

