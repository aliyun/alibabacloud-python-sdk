# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateImportTaskRequest(DaraModel):
    def __init__(
        self,
        db_instance_id: str = None,
        estimated_size: int = None,
        host: str = None,
        owner_id: int = None,
        password: str = None,
        port: int = None,
        region_id: str = None,
        source_instance_id: str = None,
        source_platform: str = None,
        stream_port: int = None,
        user: str = None,
        xtrabackup_path: str = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.db_instance_id = db_instance_id
        # Estimated data space, in GB
        self.estimated_size = estimated_size
        # The source MySQL host IP address. RDS will access this IP address to retrieve the backup.
        # 
        # This parameter is required.
        self.host = host
        self.owner_id = owner_id
        # The Password of the source MySQL Account, which must be Base64-encoded.
        # 
        # This parameter is required.
        self.password = password
        # Source MySQL port
        # 
        # This parameter is required.
        self.port = port
        # The Region ID. You can invoke [DescribeRegions](https://help.aliyun.com/document_detail/610399.html) to obtain it.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The source cloud instance ID.
        self.source_instance_id = source_instance_id
        # Source cloud instance type
        self.source_platform = source_platform
        # Stream port used for backup transmission
        # 
        # This parameter is required.
        self.stream_port = stream_port
        # Source MySQL account, which must have permissions to create backups and set up replication. Refer to the following SQL for granting permissions:  
        # ```  
        # -- MySQL 5.7  
        # mysql> CREATE USER \\"myadmin\\"@\\"%\\" IDENTIFIED BY \\"s3cret\\";  
        # mysql> GRANT RELOAD, LOCK TABLES, PROCESS, REPLICATION CLIENT, REPLICATION SLAVE ON *.* TO  
        #        \\"myadmin\\"@\\"%\\";  
        # mysql> FLUSH PRIVILEGES;  
        # -- MySQL 8.0  
        # mysql> CREATE USER \\"myadmin\\"@\\"%\\" IDENTIFIED BY \\"Test123!\\";  
        # mysql> GRANT BACKUP_ADMIN, PROCESS, RELOAD, LOCK TABLES, REPLICATION CLIENT, REPLICATION SLAVE ON *.* TO \\"myadmin\\"@\\"%\\";  
        # mysql> GRANT SELECT ON performance_schema.log_status TO \\"myadmin\\"@\\"%\\";  
        # mysql> GRANT SELECT ON performance_schema.keyring_component_status TO myadmin@\\"%\\";  
        # mysql> GRANT SELECT ON performance_schema.replication_group_members TO myadmin@\\"%\\";  
        # mysql> FLUSH PRIVILEGES;  
        # ```
        # 
        # This parameter is required.
        self.user = user
        # Installation path of xtrabackup on the source
        self.xtrabackup_path = xtrabackup_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_instance_id is not None:
            result['DbInstanceId'] = self.db_instance_id

        if self.estimated_size is not None:
            result['EstimatedSize'] = self.estimated_size

        if self.host is not None:
            result['Host'] = self.host

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.password is not None:
            result['Password'] = self.password

        if self.port is not None:
            result['Port'] = self.port

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.source_instance_id is not None:
            result['SourceInstanceId'] = self.source_instance_id

        if self.source_platform is not None:
            result['SourcePlatform'] = self.source_platform

        if self.stream_port is not None:
            result['StreamPort'] = self.stream_port

        if self.user is not None:
            result['User'] = self.user

        if self.xtrabackup_path is not None:
            result['XtrabackupPath'] = self.xtrabackup_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbInstanceId') is not None:
            self.db_instance_id = m.get('DbInstanceId')

        if m.get('EstimatedSize') is not None:
            self.estimated_size = m.get('EstimatedSize')

        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SourceInstanceId') is not None:
            self.source_instance_id = m.get('SourceInstanceId')

        if m.get('SourcePlatform') is not None:
            self.source_platform = m.get('SourcePlatform')

        if m.get('StreamPort') is not None:
            self.stream_port = m.get('StreamPort')

        if m.get('User') is not None:
            self.user = m.get('User')

        if m.get('XtrabackupPath') is not None:
            self.xtrabackup_path = m.get('XtrabackupPath')

        return self

