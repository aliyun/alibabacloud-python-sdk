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
        # The direction of the traffic to which the IPv4 access control policy applies. Valid values:
        # 
        # *   in: inbound traffic
        # *   out: outbound traffic
        # 
        # This parameter is required.
        self.direction = direction
        # The language of the content within the response. Valid values:
        # 
        # *   zh: Chinese (default)
        # *   en: English
        self.lang = lang
        # The new priority of the IPv4 access control policy. You must specify a numeric value for this parameter. The value 1 indicates the highest priority. A larger value indicates a lower priority.
        # 
        # >  The new priority cannot exceed the priority range of the IPv4 access control policy. Otherwise, an error occurs when you call this operation. Before you call this operation, we recommend that you use the [DescribePolicyPriorUsed](https://help.aliyun.com/document_detail/138862.html) operation to query the priority range of the IPv4 access control policy in the specified direction.
        # 
        # This parameter is required.
        self.new_order = new_order
        # The original priority of the IPv4 access control policy.
        # 
        # This parameter is required.
        self.old_order = old_order
        # The source IP address of the request.
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

