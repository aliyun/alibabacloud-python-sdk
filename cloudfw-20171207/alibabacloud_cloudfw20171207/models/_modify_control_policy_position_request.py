# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyControlPolicyPositionRequest(DaraModel):
    def __init__(
        self,
        direction: str = None,
        lang: str = None,
        new_order: str = None,
        old_order: str = None,
        source_ip: str = None,
    ):
        # The traffic direction of the IPv4 access control policy for the Internet firewall. Valid values:
        # 
        # - in: inbound traffic.
        # 
        # - out: outbound traffic.
        # 
        # This parameter is required.
        self.direction = direction
        # The language of the response message. Valid values:
        # 
        # - zh (default): Chinese.
        # 
        # - en: English.
        self.lang = lang
        # The new priority for the IPv4 access control policy of the Internet firewall. The priority is a number. A smaller number indicates a higher priority. The value 1 indicates the highest priority.
        # 
        # > The new priority value cannot be outside the range of existing priorities for IPv4 policies. Otherwise, the API call fails. Before you call this operation, call [DescribePolicyPriorUsed](https://help.aliyun.com/document_detail/138862.html) to query the priority range of IPv4 policies for a specific traffic direction.
        # 
        # This parameter is required.
        self.new_order = new_order
        # The current priority of the IPv4 access control policy that you want to modify.
        # 
        # This parameter is required.
        self.old_order = old_order
        # The source IP address of the visitor.
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.direction is not None:
            result['Direction'] = self.direction

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.new_order is not None:
            result['NewOrder'] = self.new_order

        if self.old_order is not None:
            result['OldOrder'] = self.old_order

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('NewOrder') is not None:
            self.new_order = m.get('NewOrder')

        if m.get('OldOrder') is not None:
            self.old_order = m.get('OldOrder')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        return self

