# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RefreshVodObjectCachesRequest(DaraModel):
    def __init__(
        self,
        force: bool = None,
        object_path: str = None,
        object_type: str = None,
        owner_id: int = None,
        security_token: str = None,
    ):
        # Specifies whether to purge all resources in the corresponding directory when the back-to-origin content is inconsistent with the origin server resources. Default value: false.
        # 
        # - **true**: purges all resources in the corresponding directory. When "Purge All Resources" is selected, if the requested content matches a resource in the directory, the CDN node fetches the new resource from the origin server, returns it to the user, and re-caches the resource.
        # - **false**: purges only changed resources in the corresponding directory. When "Purge Changed Resources" is selected, if the requested content matches a resource in the directory, the CDN node retrieves the Last-Modified information of the resource from the origin server. If it matches the currently cached resource, the cached resource is returned directly. If it does not match, the CDN node fetches the new resource from the origin server, returns it to the user, and re-caches the resource.
        self.force = force
        # The URL of the file to prefetch. Separate multiple URLs with line breaks (
        #  or 
        # ).
        # 
        # This parameter is required.
        self.object_path = object_path
        # The type of purge. Valid values:
        # 
        # - **File** (default): file purge.
        # - **Directory**: directory purge.
        # - **Regex**: regular expression-based purge.
        # - **IgnoreParams**: parameter-stripped purge. Parameter stripping refers to removing the question mark (?) and all characters after it from the request URL. Parameter-stripped purge means that you submit a parameter-stripped URL through the API, and the submitted URL is matched against cached resource URLs after parameter stripping. If a cached resource URL matches the submitted URL after parameter stripping, the CDN node purges the cached resource.
        self.object_type = object_type
        self.owner_id = owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.force is not None:
            result['Force'] = self.force

        if self.object_path is not None:
            result['ObjectPath'] = self.object_path

        if self.object_type is not None:
            result['ObjectType'] = self.object_type

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Force') is not None:
            self.force = m.get('Force')

        if m.get('ObjectPath') is not None:
            self.object_path = m.get('ObjectPath')

        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

