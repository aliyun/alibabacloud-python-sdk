# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rdsai20250507 import models as main_models
from darabonba.model import DaraModel

class ListContextDatabaseSyncSourceTreeNodesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ListContextDatabaseSyncSourceTreeNodesResponseBodyData] = None,
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
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

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

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListContextDatabaseSyncSourceTreeNodesResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListContextDatabaseSyncSourceTreeNodesResponseBodyData(DaraModel):
    def __init__(
        self,
        discovered_at: str = None,
        extension: str = None,
        has_children: bool = None,
        kind: str = None,
        node_key: str = None,
        parent_key: str = None,
        stale_at: str = None,
        title: str = None,
        unsupported_reason: str = None,
    ):
        # The discovery time.
        self.discovered_at = discovered_at
        # The file name extension.
        self.extension = extension
        # Indicates whether the node has child nodes.
        self.has_children = has_children
        # The type.
        self.kind = kind
        # The node identifier.
        self.node_key = node_key
        # The parent node identifier.
        self.parent_key = parent_key
        # The expiration time.
        self.stale_at = stale_at
        # The title.
        self.title = title
        # The reason why the operation is not supported.
        self.unsupported_reason = unsupported_reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.discovered_at is not None:
            result['DiscoveredAt'] = self.discovered_at

        if self.extension is not None:
            result['Extension'] = self.extension

        if self.has_children is not None:
            result['HasChildren'] = self.has_children

        if self.kind is not None:
            result['Kind'] = self.kind

        if self.node_key is not None:
            result['NodeKey'] = self.node_key

        if self.parent_key is not None:
            result['ParentKey'] = self.parent_key

        if self.stale_at is not None:
            result['StaleAt'] = self.stale_at

        if self.title is not None:
            result['Title'] = self.title

        if self.unsupported_reason is not None:
            result['UnsupportedReason'] = self.unsupported_reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiscoveredAt') is not None:
            self.discovered_at = m.get('DiscoveredAt')

        if m.get('Extension') is not None:
            self.extension = m.get('Extension')

        if m.get('HasChildren') is not None:
            self.has_children = m.get('HasChildren')

        if m.get('Kind') is not None:
            self.kind = m.get('Kind')

        if m.get('NodeKey') is not None:
            self.node_key = m.get('NodeKey')

        if m.get('ParentKey') is not None:
            self.parent_key = m.get('ParentKey')

        if m.get('StaleAt') is not None:
            self.stale_at = m.get('StaleAt')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('UnsupportedReason') is not None:
            self.unsupported_reason = m.get('UnsupportedReason')

        return self

