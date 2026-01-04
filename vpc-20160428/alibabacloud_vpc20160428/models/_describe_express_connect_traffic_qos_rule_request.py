# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeExpressConnectTrafficQosRuleRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        qos_id: str = None,
        queue_id: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        rule_id_list: List[str] = None,
        rule_name_list: List[str] = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must make sure that it is unique among different requests. The client token can contain only ASCII characters.
        # 
        # >  If you do not set this parameter, the system uses **RequestId** as **ClientToken**. **RequestId** may be different for each API request.
        self.client_token = client_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the QoS policy.
        self.qos_id = qos_id
        # The ID of the QoS queue.
        self.queue_id = queue_id
        # The region ID of the QoS policy.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        # The list of QoS rule IDs.
        self.rule_id_list = rule_id_list
        # The list of QoS rule names.
        self.rule_name_list = rule_name_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.qos_id is not None:
            result['QosId'] = self.qos_id

        if self.queue_id is not None:
            result['QueueId'] = self.queue_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.rule_id_list is not None:
            result['RuleIdList'] = self.rule_id_list

        if self.rule_name_list is not None:
            result['RuleNameList'] = self.rule_name_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('QosId') is not None:
            self.qos_id = m.get('QosId')

        if m.get('QueueId') is not None:
            self.queue_id = m.get('QueueId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('RuleIdList') is not None:
            self.rule_id_list = m.get('RuleIdList')

        if m.get('RuleNameList') is not None:
            self.rule_name_list = m.get('RuleNameList')

        return self

