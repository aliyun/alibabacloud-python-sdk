# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RefreshErObjectCachesRequest(DaraModel):
    def __init__(
        self,
        force: bool = None,
        merge_domain_name: str = None,
        object_path: str = None,
        object_type: str = None,
        routine_id: str = None,
    ):
        # Specifies whether to refresh resources in a directory if the resources requested are different from the resources on the origin server. Default value: false.
        # 
        # *   **true**: refreshes all resources in the directory.
        # *   **false**: refreshes the changed resources in the directory.
        self.force = force
        # The domain names that are merged for refreshing. POPs that provide services for the domain names are refreshed.
        # 
        # >  Separate multiple domain names with commas (,).
        self.merge_domain_name = merge_domain_name
        # The URL that you want to refresh.
        # 
        # > *   Separate URLs with line feeds (\\n or \\r\\n). Each object path can be up to 1,024 characters in length.
        # >*   The URLs in a request must belong to the same domain name.
        # >*   You can refresh up to 1,000 URLs in each request.
        # 
        # This parameter is required.
        self.object_path = object_path
        # The refresh type. Valid values:
        # 
        # *   **File** (default): refreshes content based on URLs.
        # *   **Directory**: refreshes content based on directories.
        # *   **Regex**: refreshes content based on regular expressions.
        # *   **IgnoreParams**: removes the question mark (`?`) and parameters after the question mark (`?`) in a request URL and refreshes content. After you call this operation with the request URL submitted, the system compares the submitted URL with the URL of the cached resource without specific parameters. If the URLs match, the points of presence (POPs) refresh the cached resource.
        # 
        # >  If you refresh the files in one or more directories, the resources in the directory that you want to refresh are marked as expired. You cannot delete the directory. If clients request resources on POPs that are marked as expired, Dynamic Content Delivery Network (DCDN) checks whether the resources on your origin server are updated. If resources are updated, DCDN retrieves the latest version of the resources and returns the resources to the clients. Otherwise, the origin server returns the 304 status code.
        # 
        # This parameter is required.
        self.object_type = object_type
        # The ID of the routine, which is in the format of "Name.Subdomain" and is the unique identifier of a custom routine.
        self.routine_id = routine_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.force is not None:
            result['Force'] = self.force

        if self.merge_domain_name is not None:
            result['MergeDomainName'] = self.merge_domain_name

        if self.object_path is not None:
            result['ObjectPath'] = self.object_path

        if self.object_type is not None:
            result['ObjectType'] = self.object_type

        if self.routine_id is not None:
            result['RoutineId'] = self.routine_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Force') is not None:
            self.force = m.get('Force')

        if m.get('MergeDomainName') is not None:
            self.merge_domain_name = m.get('MergeDomainName')

        if m.get('ObjectPath') is not None:
            self.object_path = m.get('ObjectPath')

        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')

        if m.get('RoutineId') is not None:
            self.routine_id = m.get('RoutineId')

        return self

