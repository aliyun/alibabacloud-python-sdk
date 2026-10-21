# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListImageCachesRequest(DaraModel):
    def __init__(
        self,
        acr_instance_id: str = None,
        digest: str = None,
        image_ref_contains: str = None,
        max_results: int = None,
        namespace: str = None,
        next_token: str = None,
        region_id: str = None,
        registry: str = None,
        repository: str = None,
        status: str = None,
        tag: str = None,
        workspace_id: str = None,
    ):
        # The ID of the source ACR Enterprise instance. The match must be exact. Empty character strings are invalid.
        self.acr_instance_id = acr_instance_id
        # The complete image digest in the sha256: format followed by a 64-character lowercase hexadecimal string. The format is verified by the console. The match must be exact, and prefixes are not supported.
        self.digest = digest
        # Performs a case-insensitive literal substring search on the complete source image reference in the registry/repository:tag format, where the repository already includes the namespace. If the value is empty after trimming leading and trailing whitespace, it is treated as not provided. Percent signs, underscores, and backslashes are treated as literal characters.
        self.image_ref_contains = image_ref_contains
        # The maximum number of results to return. If this parameter is not provided or is set to 0, the default value is 20. If the value exceeds 100, it is treated as 100. Negative values return an InvalidMaxResults error. The value can be adjusted for subsequent pages.
        self.max_results = max_results
        # The source namespace. The match is case-sensitive and must be exact. Empty strings are invalid.
        self.namespace = namespace
        # Omit this parameter for the first request. For subsequent requests, pass the nextToken value from the previous response exactly as returned. If the filter conditions change, you must query the first page again.
        self.next_token = next_token
        # The product entry region, which is determined by the selected region endpoint.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The domain name of the source repository. The match is case-insensitive and must be exact. Do not include the protocol, path, or tag. Public network and VPC domain names are not considered equal. Empty strings are invalid.
        self.registry = registry
        # The name of the repository under the namespace. The match is case-sensitive and must be exact. Do not include the namespace. If this parameter is provided, the namespace parameter must also be provided. Empty strings are invalid.
        self.repository = repository
        # Filters the results by a single cache status. Omit this parameter to query all statuses.
        self.status = status
        # The tag of the source image. The match is case-sensitive and must be exact. The latest tag is not inferred. Empty strings are invalid.
        self.tag = tag
        # The current routed workspace. The server verifies the account, region, and resource ownership. This parameter cannot be omitted or used to access other workspaces.
        # 
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acr_instance_id is not None:
            result['acrInstanceId'] = self.acr_instance_id

        if self.digest is not None:
            result['digest'] = self.digest

        if self.image_ref_contains is not None:
            result['imageRefContains'] = self.image_ref_contains

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.namespace is not None:
            result['namespace'] = self.namespace

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.registry is not None:
            result['registry'] = self.registry

        if self.repository is not None:
            result['repository'] = self.repository

        if self.status is not None:
            result['status'] = self.status

        if self.tag is not None:
            result['tag'] = self.tag

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('acrInstanceId') is not None:
            self.acr_instance_id = m.get('acrInstanceId')

        if m.get('digest') is not None:
            self.digest = m.get('digest')

        if m.get('imageRefContains') is not None:
            self.image_ref_contains = m.get('imageRefContains')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('registry') is not None:
            self.registry = m.get('registry')

        if m.get('repository') is not None:
            self.repository = m.get('repository')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('tag') is not None:
            self.tag = m.get('tag')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

