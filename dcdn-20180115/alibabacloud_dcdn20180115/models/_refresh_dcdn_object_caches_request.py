# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RefreshDcdnObjectCachesRequest(DaraModel):
    def __init__(
        self,
        force: bool = None,
        object_path: str = None,
        object_type: str = None,
        owner_id: int = None,
        security_token: str = None,
    ):
        # Specifies whether to refresh resources in a directory if the resources are different from the resources in the same directory in the origin server. Default value: false.
        # 
        # *   **true**: refresh all resources in the directory.
        # *   **false**: refresh the changed resources in the directory.
        self.force = force
        # The path of the objects that you want to refresh. Separate multiple URLs with line feed characters (\\n) or a pair of carriage return and line feed characters (\\r\\n).
        # 
        # This parameter is required.
        self.object_path = object_path
        # The refresh type. Valid values:
        # 
        # *   **File** (default): refreshes resources based on URLs.
        # *   **Directory**: refreshes resources based on directories.
        # *   **Regex**: refreshes content based on regular expressions.
        # *   **IgnoreParams**: removes the question mark (`?`) and parameters after `?` in a request URL and refreshes content. After you call this operation with the request URL submitted, the system compares the submitted URL with the URL of the cached resource without specific parameters. If the URLs match, the DCDN POPs refresh the cached resource.
        # 
        # >*   For more information about features of URL refresh and directory refresh, see [Refresh and prefetch resources](https://help.aliyun.com/document_detail/64936.html).
        # >*   If you set ObjectType to Directory, the resources in the directory that you want to refresh are marked as expired. You cannot delete the directory. If clients request resources after the resources on POPs are marked as expired, DCDN checks whether the resources on your origin server are updated with a later version. If a later version exists, DCDN retrieves the resources of the later version and returns the resources to the clients. Otherwise, DCDN retrieves the 304 status code from the origin server.
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

