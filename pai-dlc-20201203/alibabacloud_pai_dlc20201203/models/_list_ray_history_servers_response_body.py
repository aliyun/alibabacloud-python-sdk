# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pai_dlc20201203 import models as main_models
from darabonba.model import DaraModel

class ListRayHistoryServersResponseBody(DaraModel):
    def __init__(
        self,
        ray_history_servers: List[main_models.ListRayHistoryServersResponseBodyRayHistoryServers] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of RayHistoryServer entries.
        self.ray_history_servers = ray_history_servers
        # The request ID, which is used for diagnostics and troubleshooting.
        self.request_id = request_id
        # The total number of entries that match the filter conditions.
        self.total_count = total_count

    def validate(self):
        if self.ray_history_servers:
            for v1 in self.ray_history_servers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RayHistoryServers'] = []
        if self.ray_history_servers is not None:
            for k1 in self.ray_history_servers:
                result['RayHistoryServers'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ray_history_servers = []
        if m.get('RayHistoryServers') is not None:
            for k1 in m.get('RayHistoryServers'):
                temp_model = main_models.ListRayHistoryServersResponseBodyRayHistoryServers()
                self.ray_history_servers.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListRayHistoryServersResponseBodyRayHistoryServers(DaraModel):
    def __init__(
        self,
        accessibility: str = None,
        display_name: str = None,
        ecs_spec: str = None,
        gmt_create_time: str = None,
        gmt_finish_time: str = None,
        gmt_modify_time: str = None,
        max_runtime_minutes: int = None,
        ray_history_server_id: str = None,
        ray_history_server_url: str = None,
        reason_code: str = None,
        reason_message: str = None,
        resource_id: str = None,
        resource_name: str = None,
        status: str = None,
        storage_path: str = None,
        tenant_id: str = None,
        user_id: str = None,
        username: str = None,
        workspace_id: str = None,
    ):
        # The visibility of the job. Valid values:
        # - PUBLIC: visible to all users in the workspace.
        # - PRIVATE (default): visible only to you and administrators in the workspace.
        self.accessibility = accessibility
        # The display name of the job.
        self.display_name = display_name
        # The hardware specifications of the public resource group. Visit [PAI-DLC billing](https://help.aliyun.com/document_detail/171758.html) for a detailed list of specifications.>Notice: Prices vary depending on the specifications..
        self.ecs_spec = ecs_spec
        # The time when the job was created, in UTC.
        self.gmt_create_time = gmt_create_time
        # The time when the job ended, in UTC.
        self.gmt_finish_time = gmt_finish_time
        # The time when the job was last modified, in UTC.
        self.gmt_modify_time = gmt_modify_time
        # The maximum runtime in minutes.
        self.max_runtime_minutes = max_runtime_minutes
        # The ID of the created RayHistoryServer.
        self.ray_history_server_id = ray_history_server_id
        # Ray Dashboard URL。
        self.ray_history_server_url = ray_history_server_url
        # The status detail code.
        self.reason_code = reason_code
        # The status details.
        self.reason_message = reason_message
        # The resource group ID. For information about how to query the ID of a dedicated resource group, see [Manage resource quotas](https://help.aliyun.com/document_detail/2651299.html).
        self.resource_id = resource_id
        # The name of the resource on which the job runs.
        self.resource_name = resource_name
        # The RayHistoryServer status. Valid values:
        # - Creating: being created.
        # - Running: running.
        # - Stopped: stopped.
        # - Succeeded: succeeded.
        # - Failed: failed.
        self.status = status
        # The storage path of Ray logs.
        self.storage_path = storage_path
        # The tenant ID.
        self.tenant_id = tenant_id
        # The user ID.
        self.user_id = user_id
        # The username.
        self.username = username
        # The workspace ID. <props="china">For information about how to obtain the workspace ID, see [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html)..
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.ecs_spec is not None:
            result['EcsSpec'] = self.ecs_spec

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_finish_time is not None:
            result['GmtFinishTime'] = self.gmt_finish_time

        if self.gmt_modify_time is not None:
            result['GmtModifyTime'] = self.gmt_modify_time

        if self.max_runtime_minutes is not None:
            result['MaxRuntimeMinutes'] = self.max_runtime_minutes

        if self.ray_history_server_id is not None:
            result['RayHistoryServerId'] = self.ray_history_server_id

        if self.ray_history_server_url is not None:
            result['RayHistoryServerUrl'] = self.ray_history_server_url

        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code

        if self.reason_message is not None:
            result['ReasonMessage'] = self.reason_message

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name

        if self.status is not None:
            result['Status'] = self.status

        if self.storage_path is not None:
            result['StoragePath'] = self.storage_path

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.username is not None:
            result['Username'] = self.username

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('EcsSpec') is not None:
            self.ecs_spec = m.get('EcsSpec')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtFinishTime') is not None:
            self.gmt_finish_time = m.get('GmtFinishTime')

        if m.get('GmtModifyTime') is not None:
            self.gmt_modify_time = m.get('GmtModifyTime')

        if m.get('MaxRuntimeMinutes') is not None:
            self.max_runtime_minutes = m.get('MaxRuntimeMinutes')

        if m.get('RayHistoryServerId') is not None:
            self.ray_history_server_id = m.get('RayHistoryServerId')

        if m.get('RayHistoryServerUrl') is not None:
            self.ray_history_server_url = m.get('RayHistoryServerUrl')

        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')

        if m.get('ReasonMessage') is not None:
            self.reason_message = m.get('ReasonMessage')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StoragePath') is not None:
            self.storage_path = m.get('StoragePath')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

