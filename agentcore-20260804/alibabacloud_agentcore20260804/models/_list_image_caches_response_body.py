# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class ListImageCachesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        items: List[main_models.ListImageCachesResponseBodyItems] = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The business response code.
        # 
        # This parameter is required.
        self.code = code
        # The HTTP status code.
        # 
        # This parameter is required.
        self.http_status_code = http_status_code
        # The records on the current page. An empty array is returned if no matching items are found.
        # 
        # This parameter is required.
        self.items = items
        # The actual page size used for this request. This is not the number of items on the current page.
        # 
        # This parameter is required.
        self.max_results = max_results
        # The response message.
        # 
        # This parameter is required.
        self.message = message
        # The opaque cursor for the next page. An empty string indicates that no more pages are available.
        # 
        # This parameter is required.
        self.next_token = next_token
        # The request ID used for troubleshooting.
        # 
        # This parameter is required.
        self.request_id = request_id
        # Indicates whether the request was successful. A value of true does not indicate that the cache creation is complete.
        # 
        # This parameter is required.
        self.success = success
        # The total number of records that match the current filter conditions. Do not use this value to determine whether all pages have been returned.
        # 
        # This parameter is required.
        self.total_count = total_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.message is not None:
            result['message'] = self.message

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.ListImageCachesResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListImageCachesResponseBodyItems(DaraModel):
    def __init__(
        self,
        acr_instance_id: str = None,
        agent_count: int = None,
        cache_size_bytes: int = None,
        can_delete: bool = None,
        created_at: str = None,
        delete_block_reason: str = None,
        digest: str = None,
        error: main_models.ListImageCachesResponseBodyItemsError = None,
        image_id: str = None,
        registry: str = None,
        repository: str = None,
        status: str = None,
        tag: str = None,
        workspace_id: str = None,
    ):
        # The ID of the source ACR Enterprise instance.
        # 
        # This parameter is required.
        self.acr_instance_id = acr_instance_id
        # The deduplicated number of agents in the current workspace that have useImageCache set to true and are associated with this logical resource. The value is greater than or equal to 0. This matches the set filtered by imageCacheId in ListAllAgents. Disabled agents are not counted, and this value is independent of the number of occupied instances.
        # 
        # This parameter is required.
        self.agent_count = agent_count
        # The actual cache size in bytes. The value is greater than or equal to 0 if known, or null if unknown. The compressed size of the source image cannot be used as a substitute.
        # 
        # This parameter is required.
        self.cache_size_bytes = cache_size_bytes
        # Indicates whether the resource can be deleted. The value is true if no configuration references with the switch enabled exist in the current workspace, no valid instances are occupying the resource, and the resource is not being deleted. If the reference status is unknown, the query fails instead of defaulting to true.
        # 
        # This parameter is required.
        self.can_delete = can_delete
        # The creation time of the logical resource in the current workspace, in RFC 3339 format with the time zone. Content updates for the latest tag do not refresh this time.
        # 
        # This parameter is required.
        self.created_at = created_at
        # The reason why deletion is blocked. The value is null if canDelete is true. Otherwise, the value is returned based on the priority of DELETING, AGENT_ENABLED, and INSTANCES_RELEASING. Old instances may still occupy the resource even if the agent count is 0.
        # 
        # This parameter is required.
        self.delete_block_reason = delete_block_reason
        # The digest in the sha256: format followed by a 64-character lowercase hexadecimal string. It only describes the currently registered content and does not indicate whether old instances have been switched.
        # 
        # This parameter is required.
        self.digest = digest
        # The cache failure details. It is a non-null object when the status is FAILED, and null for other statuses. It only describes the current content and the current creation attempt.
        # 
        # This parameter is required.
        self.error = error
        # The logical resource ID that can be managed in the current workspace. This is not the shared physical cache ID.
        # 
        # This parameter is required.
        self.image_id = image_id
        # The domain name of the source image. It does not include the protocol, path, or credentials.
        # 
        # This parameter is required.
        self.registry = registry
        # The path of the source image repository in the namespace/repository format. The namespace is included.
        # 
        # This parameter is required.
        self.repository = repository
        # The status of the image cache. Valid values: PENDING (creating), READY (available), FAILED (abnormal), and DELETING (deleting in the current workspace).
        # 
        # This parameter is required.
        self.status = status
        # The tag of the source image. It is case-sensitive. Regular tags cannot be registered with different digests, except for the exact lowercase \\"latest\\".
        # 
        # This parameter is required.
        self.tag = tag
        # The workspace ID. It must be consistent with the requested workspace. Resources with the same content from other workspaces must not be returned.
        # 
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        if self.error:
            self.error.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acr_instance_id is not None:
            result['acrInstanceId'] = self.acr_instance_id

        if self.agent_count is not None:
            result['agentCount'] = self.agent_count

        if self.cache_size_bytes is not None:
            result['cacheSizeBytes'] = self.cache_size_bytes

        if self.can_delete is not None:
            result['canDelete'] = self.can_delete

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.delete_block_reason is not None:
            result['deleteBlockReason'] = self.delete_block_reason

        if self.digest is not None:
            result['digest'] = self.digest

        if self.error is not None:
            result['error'] = self.error.to_map()

        if self.image_id is not None:
            result['imageId'] = self.image_id

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

        if m.get('agentCount') is not None:
            self.agent_count = m.get('agentCount')

        if m.get('cacheSizeBytes') is not None:
            self.cache_size_bytes = m.get('cacheSizeBytes')

        if m.get('canDelete') is not None:
            self.can_delete = m.get('canDelete')

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('deleteBlockReason') is not None:
            self.delete_block_reason = m.get('deleteBlockReason')

        if m.get('digest') is not None:
            self.digest = m.get('digest')

        if m.get('error') is not None:
            temp_model = main_models.ListImageCachesResponseBodyItemsError()
            self.error = temp_model.from_map(m.get('error'))

        if m.get('imageId') is not None:
            self.image_id = m.get('imageId')

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

class ListImageCachesResponseBodyItemsError(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        # The secure and non-empty error code for the current creation attempt.
        # 
        # This parameter is required.
        self.code = code
        # The secure and non-empty description of the failure. It does not contain credentials, internal addresses, or stack traces.
        # 
        # This parameter is required.
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        return self

