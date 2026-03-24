# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RefreshObjectCachesRequest(DaraModel):
    def __init__(
        self,
        force: bool = None,
        object_path: str = None,
        object_type: str = None,
        owner_id: int = None,
        security_token: str = None,
    ):
        # When the comparison between the source content and the source site resources is consistent, should the resources within the corresponding range be forcibly refreshed. The default is false.
        # 
        # *   **true**: purges all resources in the range that corresponds to the type of the purge task. If you set this parameter to true, when the requested resource matches the resource in the range that corresponds to the type of the purge task, the POP retrieves the resource from the origin server, returns the resource to the client, and caches the resource.
        # *   **false**: purges the changed resources in the range that corresponds to the type of the purge task. If you set this parameter to false, when the requested resource matches the resource in the range that corresponds to the type of the purge task, the POP obtains the Last-Modified parameter of the resource from the origin server. If the obtained value of the Last-Modified parameter is the same as that of the cached resource, the cached resource is returned. Otherwise, the POP retrieves the resource from the origin server, returns the resource to the client, and caches the resource.
        # 
        # >  This parameter takes effect only when the ObjectType parameter is not set to File.
        self.force = force
        # *   If you submit multiple URLs or directories at a time, separate them with line breaks (\\n) or (\\r\\n).
        # *   The total number of domain names contained all URLs in a submitted task cannot exceed 10.
        # 
        # This parameter is required.
        self.object_path = object_path
        # The type of the object that you want to refresh. Valid values:
        # 
        # *   **File** (default): refreshes one or more files.
        # *   **Directory**: refreshes the files in one or more directories.
        # *   **Regex**: refreshes content based on regular expressions.
        # *   **ExQuery**: omits parameters after the question mark in the URL and refreshes content.
        # 
        # If you set the ObjectType parameter to File or Directory, you can view [Refresh and prefetch resources](https://help.aliyun.com/document_detail/27140.html) to obtain more information. If you set the ObjectType parameter to Regex, you can view [Configure URL refresh rules that contain regular expressions](https://help.aliyun.com/document_detail/146195.html) to obtain more information.
        # 
        # If you set the ObjectType parameter to Directory, the resources in the directory that you want to refresh are marked as expired. You cannot delete the directory. If clients request resources on POPs that are marked as expired, Alibaba Cloud CDN checks whether the resources on your origin server are updated. If resources are updated, Alibaba Cloud CDN retrieves the latest version of the resources and returns the resources to the clients. Otherwise, the origin server returns the 304 status code.
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

