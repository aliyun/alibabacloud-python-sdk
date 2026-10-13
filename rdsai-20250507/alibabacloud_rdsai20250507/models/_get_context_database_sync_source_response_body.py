# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rdsai20250507 import models as main_models
from darabonba.model import DaraModel

class GetContextDatabaseSyncSourceResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetContextDatabaseSyncSourceResponseBodyData = None,
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
        # The message.
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
            temp_model = main_models.GetContextDatabaseSyncSourceResponseBodyData()
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

class GetContextDatabaseSyncSourceResponseBodyData(DaraModel):
    def __init__(
        self,
        confirmed_at: str = None,
        connection_id: str = None,
        id: str = None,
        name: str = None,
        selected_node_keys: List[str] = None,
        selection_policy: str = None,
        source_config: str = None,
    ):
        # The confirmation time.
        self.confirmed_at = confirmed_at
        # The connection ID, which is a system-generated UUID.
        self.connection_id = connection_id
        # The data source ID, which is a system-generated UUID.
        self.id = id
        # The name.
        self.name = name
        # The list of selected node keys.
        self.selected_node_keys = selected_node_keys
        # The selection policy.
        self.selection_policy = selection_policy
        # The datasource config, which varies by plug-in.
        self.source_config = source_config

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.confirmed_at is not None:
            result['ConfirmedAt'] = self.confirmed_at

        if self.connection_id is not None:
            result['ConnectionId'] = self.connection_id

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.selected_node_keys is not None:
            result['SelectedNodeKeys'] = self.selected_node_keys

        if self.selection_policy is not None:
            result['SelectionPolicy'] = self.selection_policy

        if self.source_config is not None:
            result['SourceConfig'] = self.source_config

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfirmedAt') is not None:
            self.confirmed_at = m.get('ConfirmedAt')

        if m.get('ConnectionId') is not None:
            self.connection_id = m.get('ConnectionId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SelectedNodeKeys') is not None:
            self.selected_node_keys = m.get('SelectedNodeKeys')

        if m.get('SelectionPolicy') is not None:
            self.selection_policy = m.get('SelectionPolicy')

        if m.get('SourceConfig') is not None:
            self.source_config = m.get('SourceConfig')

        return self

