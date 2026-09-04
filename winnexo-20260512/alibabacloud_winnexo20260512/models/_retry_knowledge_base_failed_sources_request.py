# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RetryKnowledgeBaseFailedSourcesRequest(DaraModel):
    def __init__(
        self,
        directory_id: str = None,
        tenant_id: str = None,
    ):
        # The enterprise knowledge base directory ID (recursively includes failed resources in subdirectories).
        # 
        # This parameter is required.
        self.directory_id = directory_id
        # The tenant ID. This is a common parameter. In winnexo-cli, pass this value explicitly with --tenant-id.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.directory_id is not None:
            result['directoryId'] = self.directory_id

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('directoryId') is not None:
            self.directory_id = m.get('directoryId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

