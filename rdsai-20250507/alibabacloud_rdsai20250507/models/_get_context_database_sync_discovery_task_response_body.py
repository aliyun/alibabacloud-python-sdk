# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_rdsai20250507 import models as main_models
from darabonba.model import DaraModel

class GetContextDatabaseSyncDiscoveryTaskResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetContextDatabaseSyncDiscoveryTaskResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code.
        self.code = code
        # The returned data.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The response message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
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
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetContextDatabaseSyncDiscoveryTaskResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetContextDatabaseSyncDiscoveryTaskResponseBodyData(DaraModel):
    def __init__(
        self,
        cancel_requested_at: str = None,
        connection_id: str = None,
        containers: int = None,
        created_at: str = None,
        error: str = None,
        plugin_ref: str = None,
        scanned: int = None,
        source_config: str = None,
        source_id: str = None,
        state: str = None,
        task_id: str = None,
        updated_at: str = None,
    ):
        # The time when the cancellation was requested.
        self.cancel_requested_at = cancel_requested_at
        # The connection ID, which is a system-generated UUID.
        self.connection_id = connection_id
        # The number of containers.
        self.containers = containers
        # The time when the task was created.
        self.created_at = created_at
        # The error message.
        self.error = error
        # The plug-in reference.
        self.plugin_ref = plugin_ref
        # The number of scanned items.
        self.scanned = scanned
        # The datasource config. The structure varies depending on the plug-in.
        self.source_config = source_config
        # The data source ID, which is a system-generated UUID.
        self.source_id = source_id
        # The discovery task status. Valid values: queued, running, succeeded, cancelled, and failed.
        self.state = state
        # The discovery task ID, which is a system-generated UUID.
        self.task_id = task_id
        # The time when the task was last updated.
        self.updated_at = updated_at

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cancel_requested_at is not None:
            result['CancelRequestedAt'] = self.cancel_requested_at

        if self.connection_id is not None:
            result['ConnectionId'] = self.connection_id

        if self.containers is not None:
            result['Containers'] = self.containers

        if self.created_at is not None:
            result['CreatedAt'] = self.created_at

        if self.error is not None:
            result['Error'] = self.error

        if self.plugin_ref is not None:
            result['PluginRef'] = self.plugin_ref

        if self.scanned is not None:
            result['Scanned'] = self.scanned

        if self.source_config is not None:
            result['SourceConfig'] = self.source_config

        if self.source_id is not None:
            result['SourceId'] = self.source_id

        if self.state is not None:
            result['State'] = self.state

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CancelRequestedAt') is not None:
            self.cancel_requested_at = m.get('CancelRequestedAt')

        if m.get('ConnectionId') is not None:
            self.connection_id = m.get('ConnectionId')

        if m.get('Containers') is not None:
            self.containers = m.get('Containers')

        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')

        if m.get('Error') is not None:
            self.error = m.get('Error')

        if m.get('PluginRef') is not None:
            self.plugin_ref = m.get('PluginRef')

        if m.get('Scanned') is not None:
            self.scanned = m.get('Scanned')

        if m.get('SourceConfig') is not None:
            self.source_config = m.get('SourceConfig')

        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')

        return self

