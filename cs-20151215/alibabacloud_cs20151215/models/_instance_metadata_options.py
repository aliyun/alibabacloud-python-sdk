# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InstanceMetadataOptions(DaraModel):
    def __init__(
        self,
        http_tokens: str = None,
    ):
        # Configuration of the ECS instance metadata access mode. Valid values:  
        # 
        # * `optional`: Compatible with both NAT mode and hardened mode.  
        # * `required`: Enables hardened mode only (IMDSv2). After this mode is enabled, applications within edge zones cannot access ECS instance metadata through NAT mode.  
        # 
        # Default Value: `optional`.  
        # 
        # >Notice:   
        # 
        # * This parameter is currently available only to users on the whitelist. To use it, submit a ticket to request access.  
        # * This parameter is supported only in ACK managed clusters of version 1.28 or later.  
        # 
        #   
        # 
        # > For more information about instance metadata access modes, see [Instance Metadata Access Mode](https://help.aliyun.com/document_detail/108460.html).
        self.http_tokens = http_tokens

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.http_tokens is not None:
            result['http_tokens'] = self.http_tokens

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('http_tokens') is not None:
            self.http_tokens = m.get('http_tokens')

        return self

