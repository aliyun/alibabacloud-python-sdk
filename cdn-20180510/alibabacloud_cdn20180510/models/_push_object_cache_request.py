# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PushObjectCacheRequest(DaraModel):
    def __init__(
        self,
        area: str = None,
        consistency_hash: bool = None,
        l_2preload: bool = None,
        object_path: str = None,
        owner_id: int = None,
        query_hashkey: bool = None,
        security_token: str = None,
        with_header: str = None,
    ):
        # The acceleration region where content is to be prefetched. Valid values:
        # 
        # *   **domestic****: Chinese mainland**
        # *   **overseas****: regions outside the Chinese mainland**
        # 
        # If you do not set this parameter, content in the service location (specified by parameter Coverage) that you configured for the domain is prefetched. Content is prefetched based on the following rules:
        # 
        # *   If the acceleration region is set to **Chinese Mainland Only**, content in regions in the Chinese mainland is prefetched.
        # *   If the acceleration region is set to **Global**, content in all regions is prefetched.
        # *   If the acceleration region is set to **Global (Excluding the Chinese Mainland)**, content in regions outside the Chinese mainland is prefetched.
        self.area = area
        self.consistency_hash = consistency_hash
        # Specifies whether to prefetch content to L2 points of presence (POPs). Valid values:
        # 
        # *   **true**: prefetches content to L2 POPs.
        # *   **false**: prefetches content to regular POPs. Regular POPs can be L2 POPs or L3 POPs. Default value: **false**.
        self.l_2preload = l_2preload
        # The URLs based on which content is prefetched. Format: **accelerated domain name/files to be prefetched**.
        # 
        # > Separate URLs with line feeds (\\n or \\r\\n). Each object path can be up to 1,024 characters in length.
        # 
        # This parameter is required.
        self.object_path = object_path
        self.owner_id = owner_id
        # This parameter specifies whether to enable the hash key query mode when you run a prefetch task. Valid values:
        # 
        # *   false: The default mode, in which the submitted URL is used as the hash key for the prefetch.
        # *   true: In this mode, the actual hash key used for the prefetch is queried based on the configuration of the domain name.
        self.query_hashkey = query_hashkey
        self.security_token = security_token
        # The custom header for prefetch in the JSON format.
        self.with_header = with_header

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.area is not None:
            result['Area'] = self.area

        if self.consistency_hash is not None:
            result['ConsistencyHash'] = self.consistency_hash

        if self.l_2preload is not None:
            result['L2Preload'] = self.l_2preload

        if self.object_path is not None:
            result['ObjectPath'] = self.object_path

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.query_hashkey is not None:
            result['QueryHashkey'] = self.query_hashkey

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.with_header is not None:
            result['WithHeader'] = self.with_header

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Area') is not None:
            self.area = m.get('Area')

        if m.get('ConsistencyHash') is not None:
            self.consistency_hash = m.get('ConsistencyHash')

        if m.get('L2Preload') is not None:
            self.l_2preload = m.get('L2Preload')

        if m.get('ObjectPath') is not None:
            self.object_path = m.get('ObjectPath')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('QueryHashkey') is not None:
            self.query_hashkey = m.get('QueryHashkey')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('WithHeader') is not None:
            self.with_header = m.get('WithHeader')

        return self

