# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModifyObjectGroupOperationRequest(DaraModel):
    def __init__(
        self,
        comment: str = None,
        direction: str = None,
        lang: str = None,
        object_list: List[str] = None,
        object_operation: str = None,
        object_type: str = None,
        source_ip: str = None,
    ):
        # The remarks for the operation.
        self.comment = comment
        # The traffic direction that is controlled by the access control policy.
        # 
        # Valid values:
        # 
        # - **in**: Inbound traffic.
        # 
        # - **out**: Outbound traffic.
        # 
        # This parameter is required.
        self.direction = direction
        # The language of the response. Valid values:
        # 
        # - **zh** (default): Chinese
        # 
        # - **en**: English
        self.lang = lang
        # The list of objects.
        # 
        # This parameter is required.
        self.object_list = object_list
        # The operation to perform. Valid values:
        # 
        # - **subscribe**: Follows the object.
        # 
        # - **unsubscribe**: Unfollows the object.
        # 
        # - **ignore**: Adds the object to the whitelist.
        # 
        # - **cancelIgnore**: Removes the object from the whitelist.
        # 
        # This parameter is required.
        self.object_operation = object_operation
        # The type of object to add to the whitelist or follow.
        # 
        # Valid values:
        # 
        # - **assetsIp**: Asset IP address.
        # 
        # - **destinationIp**: Destination IP address.
        # 
        # - **destinationPort**: Destination port.
        # 
        # - **destinationDomain**: Destination domain name.
        # 
        # This parameter is required.
        self.object_type = object_type
        # The source IP address of the visitor.
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.direction is not None:
            result['Direction'] = self.direction

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.object_list is not None:
            result['ObjectList'] = self.object_list

        if self.object_operation is not None:
            result['ObjectOperation'] = self.object_operation

        if self.object_type is not None:
            result['ObjectType'] = self.object_type

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('ObjectList') is not None:
            self.object_list = m.get('ObjectList')

        if m.get('ObjectOperation') is not None:
            self.object_operation = m.get('ObjectOperation')

        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        return self

