# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cbn20170912 import models as main_models
from darabonba.model import DaraModel

class CreateCenInterRegionTrafficQosPolicyRequest(DaraModel):
    def __init__(
        self,
        bandwidth_guarantee_mode: str = None,
        client_token: str = None,
        console_dry_run: bool = None,
        dry_run: bool = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        traffic_qos_policy_description: str = None,
        traffic_qos_policy_name: str = None,
        traffic_qos_queues: List[main_models.CreateCenInterRegionTrafficQosPolicyRequestTrafficQosQueues] = None,
        transit_router_attachment_id: str = None,
        transit_router_id: str = None,
    ):
        # The bandwidth guarantee mode. You can specify an absolute bandwidth value or a bandwidth percentage. Valid values:
        # 
        # - **byBandwidth**: configures the QoS queue based on an absolute bandwidth value.
        # 
        # - **byBandwidthPercent** (default): configures the QoS queue based on a bandwidth percentage.
        self.bandwidth_guarantee_mode = bandwidth_guarantee_mode
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that the value is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # Specifies whether to only precheck the request. Valid values:
        # 
        # - **true**: prechecks the request without creating the inter-region traffic QoS policy. The system checks whether required parameters are specified, the request format, and service limits. If the request fails the precheck, the corresponding error is returned. If the request passes the precheck, the `DryRunOperation` error code is returned.
        # - **false** (default): sends the request. If the request passes the precheck, the inter-region traffic QoS policy is created.
        self.console_dry_run = console_dry_run
        # Specifies whether to only precheck the request. Valid values:
        # - **true**: prechecks the request without creating the traffic QoS policy. The system checks whether required parameters are specified, the request format, and service limits. If the request fails the precheck, the corresponding error is returned. If the request passes the precheck, the `DryRunOperation` error code is returned.
        # - **false** (default): sends the request. If the request passes the precheck, the traffic QoS policy is created.
        self.dry_run = dry_run
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The description of the traffic QoS policy.
        # 
        # The description must be 1 to 256 characters in length, and can be left empty. It cannot start with http:// or https://.
        self.traffic_qos_policy_description = traffic_qos_policy_description
        # The name of the traffic QoS policy.
        # 
        # The name must be 1 to 128 characters in length, and can be left empty. It cannot start with http:// or https://.
        self.traffic_qos_policy_name = traffic_qos_policy_name
        # The information about the queues in the traffic QoS policy.
        # 
        # You can create up to three queues. To create more queues, call the CreateCenInterRegionTrafficQosQueue operation.
        self.traffic_qos_queues = traffic_qos_queues
        # The ID of the inter-region connection.
        # 
        # This parameter is required.
        self.transit_router_attachment_id = transit_router_attachment_id
        # The transit router instance ID, which is used for forward and routing.
        # 
        # This parameter is required.
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

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.console_dry_run is not None:
            result['ConsoleDryRun'] = self.console_dry_run

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.traffic_qos_policy_description is not None:
            result['TrafficQosPolicyDescription'] = self.traffic_qos_policy_description

        if self.traffic_qos_policy_name is not None:
            result['TrafficQosPolicyName'] = self.traffic_qos_policy_name

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

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ConsoleDryRun') is not None:
            self.console_dry_run = m.get('ConsoleDryRun')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('TrafficQosPolicyDescription') is not None:
            self.traffic_qos_policy_description = m.get('TrafficQosPolicyDescription')

        if m.get('TrafficQosPolicyName') is not None:
            self.traffic_qos_policy_name = m.get('TrafficQosPolicyName')

        self.traffic_qos_queues = []
        if m.get('TrafficQosQueues') is not None:
            for k1 in m.get('TrafficQosQueues'):
                temp_model = main_models.CreateCenInterRegionTrafficQosPolicyRequestTrafficQosQueues()
                self.traffic_qos_queues.append(temp_model.from_map(k1))

        if m.get('TransitRouterAttachmentId') is not None:
            self.transit_router_attachment_id = m.get('TransitRouterAttachmentId')

        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')

        return self

class CreateCenInterRegionTrafficQosPolicyRequestTrafficQosQueues(DaraModel):
    def __init__(
        self,
        bandwidth: str = None,
        dscps: List[int] = None,
        qos_queue_description: str = None,
        qos_queue_name: str = None,
        remain_bandwidth_percent: str = None,
    ):
        # The absolute value of the inter-region bandwidth that the queue can use. Unit: Mbit/s.
        # 
        # You can create up to 10 queues in a traffic QoS policy and specify the inter-region bandwidth that each queue can use.
        # 
        # For example, if you enter 1, packets that match the queue can use up to 1 Mbit/s of the inter-region bandwidth.
        # 
        # > The sum of the absolute values of the inter-region bandwidth allocated to all queues in a traffic QoS policy cannot exceed the total inter-region bandwidth.
        self.bandwidth = bandwidth
        # The DSCP values that match the queue.
        # 
        # You can create up to three queues in a traffic QoS policy. Each queue can match up to 60 DSCP values. Separate multiple DSCP values with commas (,).
        self.dscps = dscps
        # The description of the queue.
        # 
        # You can create up to 10 queues in a traffic QoS policy and add a description to each queue.
        # 
        # The description must be 1 to 256 characters in length, and can be left empty. It cannot start with http:// or https://.
        self.qos_queue_description = qos_queue_description
        # The name of the queue.
        # 
        # You can create up to three queues in a traffic QoS policy and specify a name for each queue.
        # 
        # The name must be 1 to 128 characters in length, and can be left empty. It cannot start with http:// or https://.
        self.qos_queue_name = qos_queue_name
        # The percentage of the inter-region bandwidth that the queue can use.
        # 
        # You can create up to 10 queues in a traffic QoS policy and specify the percentage of the inter-region bandwidth that each queue can use.
        # 
        # For example, if you enter **1**, packets that match the queue can use up to 1% of the inter-region bandwidth.
        # 
        # > The sum of the inter-region bandwidth percentages of all queues in a traffic QoS policy cannot exceed 100%.
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

        if self.qos_queue_description is not None:
            result['QosQueueDescription'] = self.qos_queue_description

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

        if m.get('QosQueueDescription') is not None:
            self.qos_queue_description = m.get('QosQueueDescription')

        if m.get('QosQueueName') is not None:
            self.qos_queue_name = m.get('QosQueueName')

        if m.get('RemainBandwidthPercent') is not None:
            self.remain_bandwidth_percent = m.get('RemainBandwidthPercent')

        return self

