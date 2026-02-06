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
        # Specifies whether to purge resources in a directory if the resources requested are different from the resources on the origin server.
        # 
        # *   **true**: refreshes all resources in the directory. If you set this parameter to true, when the requested content matches the resource in the directory, the POP retrieves the resource from the origin server, returns the resource to the client, and caches the resource.
        # *   **false** (default): refreshes the changed resources in the directory. If you set this parameter to false, when the requested content matches the resource in the directory, the POP obtains the Last-Modified parameter of the resource from the origin server. If the value of the obtained Last-Modified parameter is the same as that of the cached resource, the cached resource is returned. Otherwise, the POP retrieves the resource from the origin server, returns the resource to the client, and caches the resource.
        self.force = force
        # The URL of the file to be prefetched. Separate multiple URLs with line breaks (\\n or \\r\\n).
        # 
        # This parameter is required.
        self.object_path = object_path
        # The type of the object that you want to refresh. Valid values:
        # 
        # *   **File** (default): refreshes one or more files.
        # *   **Directory**: refreshes the files in specified directories.
        # *   **Regex**: refreshes content based on regular expressions.
        # *   **IgnoreParams**: removes the question mark (?) and parameters after the question mark (?) in a request URL and refreshes content. After you call this operation with the request URL submitted, the system compares the submitted URL with the URL of the cached resource without specific parameters. If the URLs match, the POPs refresh the cached resource.
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

