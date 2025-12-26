# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAlgorithmResponseBody(DaraModel):
    def __init__(
        self,
        algorithm_description: str = None,
        algorithm_id: str = None,
        algorithm_name: str = None,
        algorithm_provider: str = None,
        display_name: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        request_id: str = None,
        tenant_id: str = None,
        user_id: str = None,
        workspace_id: str = None,
    ):
        self.algorithm_description = algorithm_description
        self.algorithm_id = algorithm_id
        self.algorithm_name = algorithm_name
        self.algorithm_provider = algorithm_provider
        self.display_name = display_name
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.request_id = request_id
        self.tenant_id = tenant_id
        self.user_id = user_id
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.algorithm_description is not None:
            result['AlgorithmDescription'] = self.algorithm_description

        if self.algorithm_id is not None:
            result['AlgorithmId'] = self.algorithm_id

        if self.algorithm_name is not None:
            result['AlgorithmName'] = self.algorithm_name

        if self.algorithm_provider is not None:
            result['AlgorithmProvider'] = self.algorithm_provider

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgorithmDescription') is not None:
            self.algorithm_description = m.get('AlgorithmDescription')

        if m.get('AlgorithmId') is not None:
            self.algorithm_id = m.get('AlgorithmId')

        if m.get('AlgorithmName') is not None:
            self.algorithm_name = m.get('AlgorithmName')

        if m.get('AlgorithmProvider') is not None:
            self.algorithm_provider = m.get('AlgorithmProvider')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

