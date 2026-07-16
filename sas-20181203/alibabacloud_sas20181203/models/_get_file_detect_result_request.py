# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetFileDetectResultRequest(DaraModel):
    def __init__(
        self,
        hash_key_list: List[str] = None,
        source_ip: str = None,
        type: int = None,
    ):
        # An array of up to 100 unique file identifiers.
        # 
        # This parameter is required.
        self.hash_key_list = hash_key_list
        # The source IP address of the request.
        self.source_ip = source_ip
        # The type of file to detect. Valid values:
        # 
        # - **0**: malicious file detection
        # 
        # - **6**: Skill compressed package detection
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hash_key_list is not None:
            result['HashKeyList'] = self.hash_key_list

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HashKeyList') is not None:
            self.hash_key_list = m.get('HashKeyList')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

