# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyInstanceAntiBruteForceRuleRequest(DaraModel):
    def __init__(
        self,
        new_rule_id: int = None,
        resource_owner_id: int = None,
        source_ip: str = None,
        uuid: str = None,
    ):
        # The ID of the defense rule.
        # 
        # This parameter is required.
        self.new_rule_id = new_rule_id
        self.resource_owner_id = resource_owner_id
        # The source IP address of the request.
        self.source_ip = source_ip
        # The UUID of the server for which you want to modify the defense rule. You can call the [DescribeCloudCenterInstances](https://help.aliyun.com/document_detail/141932.html) operation to query the UUIDs of servers.
        # 
        # This parameter is required.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.new_rule_id is not None:
            result['NewRuleId'] = self.new_rule_id

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewRuleId') is not None:
            self.new_rule_id = m.get('NewRuleId')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

