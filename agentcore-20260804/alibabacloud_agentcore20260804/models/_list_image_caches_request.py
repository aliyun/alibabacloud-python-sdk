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
        # The ID of the source ACR Enterprise instance. The match must be exact. An empty string (a string with no characters) is invalid.
        self.acr_instance_id = acr_instance_id
        # The image digest.
        self.digest = digest
        # Performs a case-insensitive literal substring search on the full source image reference in the format of registry/repository:tag. The repository already includes the namespace. If the value is empty after trimming leading and trailing whitespace, it is treated as not provided. Percent signs, underscores, and backslashes are treated as literal characters.
        self.image_ref_contains = image_ref_contains
        # The maximum number of results to return. Default value: 20. If you explicitly specify this parameter, the value must be an integer from 1 to 100. Otherwise, an InvalidMaxResults error is returned. When you paginate, this value must remain the same as the previous page.
        self.max_results = max_results
        # The source namespace. The match is case-sensitive and must be exact. An empty string is invalid.
        self.namespace = namespace
        # The pagination token. Omit this parameter for the first request. For subsequent requests, pass the nextToken value returned in the previous response as is. When you paginate, you must keep the filter conditions and maxResults unchanged. If you change any of these parameters, you must query the first page again.
        self.next_token = next_token
        # The region ID. The region ID must be passed as a query parameter and must match the selected region endpoint and the workspace region.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The domain name of the source registry. The match is case-insensitive and must be exact. Do not include the protocol, path, or tag. Public network and VPC domain names are not considered equal. An empty string is invalid.
        self.registry = registry
        # The repository name under the namespace. The match is case-sensitive and must be exact. Do not include the namespace. If you specify this parameter, you must also specify the namespace. An empty string is invalid.
        self.repository = repository
        # The cache status used to filter the results. To query all caches, omit this parameter.
        self.status = status
        # The source image tag. The match is case-sensitive and must be exact. The latest tag is not inferred. An empty string is invalid.
        self.tag = tag
        # The workspace ID.
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

