# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetLakebaseTenantTokenResponseBody(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        request_id: str = None,
        status: str = None,
        subdir: str = None,
        tenant: str = None,
        token: str = None,
    ):
        # The associated PolarDB instance ID.
        self.dbcluster_id = dbcluster_id
        # Id of the request
        self.request_id = request_id
        # The status.
        self.status = status
        # The mount subdirectory.
        self.subdir = subdir
        # The tenant identifier.
        self.tenant = tenant
        # The tenant token.
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        if self.subdir is not None:
            result['Subdir'] = self.subdir

        if self.tenant is not None:
            result['Tenant'] = self.tenant

        if self.token is not None:
            result['Token'] = self.token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Subdir') is not None:
            self.subdir = m.get('Subdir')

        if m.get('Tenant') is not None:
            self.tenant = m.get('Tenant')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        return self

