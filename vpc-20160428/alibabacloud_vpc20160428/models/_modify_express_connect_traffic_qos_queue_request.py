# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyExpressConnectTrafficQosQueueRequest(DaraModel):
    def __init__(
        self,
        bandwidth_percent: str = None,
        client_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        qos_id: str = None,
        queue_description: str = None,
        queue_id: str = None,
        queue_name: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
    ):
        # The percentage of bandwidth allocated to the QoS queue.
        # 
        # *   If QueueType is set to **Medium**, this parameter is required. Valid values: 1 to 100.
        # *   If QueueType is set to **Default**, a value of - is returned.
        self.bandwidth_percent = bandwidth_percent
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must ensure that the value is unique among all requests. The client token can contain only ASCII characters.
        # 
        # >  If you do not set this parameter, the system uses **RequestId** as **ClientToken**. **RequestId** might be different for each API request.
        self.client_token = client_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the QoS policy.
        # 
        # This parameter is required.
        self.qos_id = qos_id
        # The description of the QoS queue.
        # 
        # The description must be 0 to 256 characters in length and cannot start with `http://` or `https://`.
        self.queue_description = queue_description
        # The ID of the QoS queue.
        # 
        # This parameter is required.
        self.queue_id = queue_id
        # The name of the QoS queue.
        # 
        # The name must be 0 to 128 characters in length and cannot start with `http://` or `https://`.
        self.queue_name = queue_name
        # The region ID of the QoS policy.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth_percent is not None:
            result['BandwidthPercent'] = self.bandwidth_percent

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.qos_id is not None:
            result['QosId'] = self.qos_id

        if self.queue_description is not None:
            result['QueueDescription'] = self.queue_description

        if self.queue_id is not None:
            result['QueueId'] = self.queue_id

        if self.queue_name is not None:
            result['QueueName'] = self.queue_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandwidthPercent') is not None:
            self.bandwidth_percent = m.get('BandwidthPercent')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('QosId') is not None:
            self.qos_id = m.get('QosId')

        if m.get('QueueDescription') is not None:
            self.queue_description = m.get('QueueDescription')

        if m.get('QueueId') is not None:
            self.queue_id = m.get('QueueId')

        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        return self

