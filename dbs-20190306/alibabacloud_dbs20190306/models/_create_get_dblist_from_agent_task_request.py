# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateGetDBListFromAgentTaskRequest(DaraModel):
    def __init__(
        self,
        backup_gateway_id: int = None,
        client_token: str = None,
        database_type: str = None,
        owner_id: str = None,
        source_endpoint_ip: str = None,
        source_endpoint_port: int = None,
        source_endpoint_region: str = None,
    ):
        # The ID of the backup gateway. You can call the [DescribeBackupPlanList](https://help.aliyun.com/document_detail/2869825.html) operation to query the ID.
        # 
        # > This parameter is required.
        self.backup_gateway_id = backup_gateway_id
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The type of the database. Valid values:
        # 
        # - **MySQL**
        # 
        # - **MSSQL**
        # 
        # - **Oracle**
        # 
        # - **MariaDB**
        # 
        # - **PostgreSQL**
        # 
        # - **DRDS**
        # 
        # - **MongoDB**
        # 
        # - **Redis**
        self.database_type = database_type
        self.owner_id = owner_id
        # The URL that is used to access the database.
        self.source_endpoint_ip = source_endpoint_ip
        # The port that is used to connect to the database.
        self.source_endpoint_port = source_endpoint_port
        # The region in which the backup gateway resides.
        self.source_endpoint_region = source_endpoint_region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_gateway_id is not None:
            result['BackupGatewayId'] = self.backup_gateway_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.database_type is not None:
            result['DatabaseType'] = self.database_type

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.source_endpoint_ip is not None:
            result['SourceEndpointIP'] = self.source_endpoint_ip

        if self.source_endpoint_port is not None:
            result['SourceEndpointPort'] = self.source_endpoint_port

        if self.source_endpoint_region is not None:
            result['SourceEndpointRegion'] = self.source_endpoint_region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupGatewayId') is not None:
            self.backup_gateway_id = m.get('BackupGatewayId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DatabaseType') is not None:
            self.database_type = m.get('DatabaseType')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('SourceEndpointIP') is not None:
            self.source_endpoint_ip = m.get('SourceEndpointIP')

        if m.get('SourceEndpointPort') is not None:
            self.source_endpoint_port = m.get('SourceEndpointPort')

        if m.get('SourceEndpointRegion') is not None:
            self.source_endpoint_region = m.get('SourceEndpointRegion')

        return self

