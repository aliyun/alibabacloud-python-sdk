# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateWorkspaceDocResponseBody(DaraModel):
    def __init__(
        self,
        dentry_uuid: str = None,
        doc_key: str = None,
        node_id: str = None,
        request_id: str = None,
        url: str = None,
        vendor_request_id: str = None,
        vendor_type: str = None,
        workspace_id: str = None,
    ):
        self.dentry_uuid = dentry_uuid
        self.doc_key = doc_key
        self.node_id = node_id
        # requestId
        self.request_id = request_id
        self.url = url
        self.vendor_request_id = vendor_request_id
        self.vendor_type = vendor_type
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dentry_uuid is not None:
            result['dentryUuid'] = self.dentry_uuid

        if self.doc_key is not None:
            result['docKey'] = self.doc_key

        if self.node_id is not None:
            result['nodeId'] = self.node_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.url is not None:
            result['url'] = self.url

        if self.vendor_request_id is not None:
            result['vendorRequestId'] = self.vendor_request_id

        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dentryUuid') is not None:
            self.dentry_uuid = m.get('dentryUuid')

        if m.get('docKey') is not None:
            self.doc_key = m.get('docKey')

        if m.get('nodeId') is not None:
            self.node_id = m.get('nodeId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('url') is not None:
            self.url = m.get('url')

        if m.get('vendorRequestId') is not None:
            self.vendor_request_id = m.get('vendorRequestId')

        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

