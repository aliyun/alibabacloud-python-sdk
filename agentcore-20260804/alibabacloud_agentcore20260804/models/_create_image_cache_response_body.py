# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class CreateImageCacheResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.CreateImageCacheResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The business response code.
        # 
        # This parameter is required.
        self.code = code
        # The result of creating the image cache.
        # 
        # This parameter is required.
        self.data = data
        # The HTTP status code.
        # 
        # This parameter is required.
        self.http_status_code = http_status_code
        # The response message.
        # 
        # This parameter is required.
        self.message = message
        # The request ID, which is used for troubleshooting.
        # 
        # This parameter is required.
        self.request_id = request_id
        # Indicates whether the request is successful. This does not indicate that the cache creation is complete.
        # 
        # This parameter is required.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.CreateImageCacheResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class CreateImageCacheResponseBodyData(DaraModel):
    def __init__(
        self,
        acr_instance_id: str = None,
        agent_count: int = None,
        cache_size_bytes: int = None,
        can_delete: bool = None,
        created_at: str = None,
        delete_block_reason: str = None,
        digest: str = None,
        error: main_models.CreateImageCacheResponseBodyDataError = None,
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
        # The deduplicated number of agents that have useImageCache set to true and are associated with this logical resource in the current workspace. The value is greater than or equal to 0. This set is the same as the set filtered by imageCacheId in ListAllAgents. Agents with the feature disabled are not counted, and this value is independent of the number of occupied instances.
        # 
        # This parameter is required.
        self.agent_count = agent_count
        # The actual cache size in bytes. The known value is greater than or equal to 0. If the value is unknown, it is null. The compressed size of the source image cannot be used as a substitute.
        # 
        # This parameter is required.
        self.cache_size_bytes = cache_size_bytes
        # Indicates whether deletion is allowed. The value is true when there are no configuration references with the switch enabled, no valid instances occupying the resource, and the resource is not being deleted in the current workspace. If the reference status is unknown, the query should fail, and deletion cannot be allowed by default.
        # 
        # This parameter is required.
        self.can_delete = can_delete
        # The creation time of the logical resource in the current workspace, in RFC3339 format with time zone. The time is not refreshed when the content of the latest tag is updated.
        # 
        # This parameter is required.
        self.created_at = created_at
        # The reason why deletion is blocked. The value is null when canDelete is true. Otherwise, the value is returned based on the priority of DELETING, AGENT_ENABLED, and INSTANCES_RELEASING. Even if the number of agents is 0, old instances may still occupy the resource.
        # 
        # This parameter is required.
        self.delete_block_reason = delete_block_reason
        # The current content digest in the format of sha256: followed by a 64-character lowercase hexadecimal string. It only describes the currently registered content and does not prove that old instances have been switched.
        # 
        # This parameter is required.
        self.digest = digest
        # The reason for the cache failure. This is a non-null object when the status is FAILED, and null for other statuses. It only describes the current content and the current creation round.
        # 
        # This parameter is required.
        self.error = error
        # The logical resource ID manageable by the current workspace, which is not a shared physical cache ID.
        # 
        # This parameter is required.
        self.image_id = image_id
        # The domain name of the source image, excluding the protocol, path, and credentials.
        # 
        # This parameter is required.
        self.registry = registry
        # The path of the source image repository in the namespace/repository format, which already includes the namespace.
        # 
        # This parameter is required.
        self.repository = repository
        # The status of the image cache. Valid values: PENDING: creating, READY: available, FAILED: abnormal, DELETING: deleting in the current workspace.
        # 
        # This parameter is required.
        self.status = status
        # The tag of the source image. Case is preserved. Regular tags cannot be registered with different digests, with the exact lowercase latest tag being the only exception.
        # 
        # This parameter is required.
        self.tag = tag
        # The workspace ID, which is consistent with the requested workspace. Resources with the same content from other workspaces are not returned.
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
            temp_model = main_models.CreateImageCacheResponseBodyDataError()
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

class CreateImageCacheResponseBodyDataError(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        # The secure and non-null error code for the current creation failure.
        # 
        # This parameter is required.
        self.code = code
        # The secure and non-null display reason for the creation failure, excluding credentials, internal addresses, or stack traces.
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

