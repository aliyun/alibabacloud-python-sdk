# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateDataSourceRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        connection_info: str = None,
        credential: str = None,
        data_source_id: str = None,
        data_source_name: str = None,
        exclude: str = None,
        include: str = None,
        index_level: str = None,
        options: str = None,
        path: List[str] = None,
        schedule: str = None,
        speed_limit: str = None,
    ):
        # The ID of the client group used to access the data source.
        self.cluster_id = cluster_id
        # The connection information for the data source. Examples:
        # 
        # - On-premises NAS data source:
        #   {
        #   "dataServerAddresses": [
        #   {
        #   "host": "123.123.123.123",
        #   "port": "8080"
        #   }
        #   ],
        #   "sharePath": "/share",
        #   "mountOptions": "vers=3",
        #   "fileSystemType": "nfs"
        #   }
        # 
        # - Intelligent Computing CPFS data source:
        #   {"vpcMountTarget":"cpfs-010wn\\*\\*\\*wy-vpc-ta\\*\\*\\*8.cn-shanghai.cpfs.aliyuncs.com","sharePath":"/"}
        # 
        # - Other large-scale file system data sources:
        #   {"path":"/mnt"}
        self.connection_info = connection_info
        # The access credentials for the data source. This parameter is used for on-premises NAS data sources that use the SMB protocol, and for OSS and S3 protocol-compatible data sources. Examples:
        # 
        # - On-premises NAS data source (SMB protocol):
        #   {
        #   "mountUsername": "\\*\\*\\*\\*\\*",
        #   "mountPassword": "\\*\\*\\*\\*\\*"
        #   }
        # 
        # - OSS protocol-compatible data source/S3 protocol-compatible data source:
        #   {
        #   "accessKeyId": "\\*\\*\\*\\*\\*",
        #   "accessKeySecret": "\\*\\*\\*\\*\\*"
        #   }
        self.credential = credential
        # The ID of the data source.
        # 
        # This parameter is required.
        self.data_source_id = data_source_id
        # The name of the data source.
        self.data_source_name = data_source_name
        # A filter to specify which files to exclude. This parameter applies only to the archive feature.
        self.exclude = exclude
        # A filter to specify which files to include. This parameter applies only to the archive feature.
        self.include = include
        # The index level for data source analysis. This parameter applies only to the archive feature.
        # 
        # - OFF: No index is created.
        # 
        # - META: A metadata index is created.
        # 
        # - ALL: A full-text index is created. (Deprecated)
        self.index_level = index_level
        # The options for data source analysis. This parameter applies only to the archive feature.
        self.options = options
        # A list of paths for data source analysis. This parameter applies only to the archive feature.
        self.path = path
        # The schedule for data source analysis. This parameter applies only to the archive feature. The format is `I|{startTime}|{interval}`. This specifies a task that starts at `{startTime}` and repeats at the specified `{interval}`. `startTime` is a Unix time value in seconds. `interval` is an ISO 8601 time interval. For example, `PT1H` indicates a one-hour interval, and `P1D` indicates a one-day interval.
        self.schedule = schedule
        # The rate limiting configuration for data source analysis. This parameter applies only to the archive feature.
        self.speed_limit = speed_limit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.connection_info is not None:
            result['ConnectionInfo'] = self.connection_info

        if self.credential is not None:
            result['Credential'] = self.credential

        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id

        if self.data_source_name is not None:
            result['DataSourceName'] = self.data_source_name

        if self.exclude is not None:
            result['Exclude'] = self.exclude

        if self.include is not None:
            result['Include'] = self.include

        if self.index_level is not None:
            result['IndexLevel'] = self.index_level

        if self.options is not None:
            result['Options'] = self.options

        if self.path is not None:
            result['Path'] = self.path

        if self.schedule is not None:
            result['Schedule'] = self.schedule

        if self.speed_limit is not None:
            result['SpeedLimit'] = self.speed_limit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ConnectionInfo') is not None:
            self.connection_info = m.get('ConnectionInfo')

        if m.get('Credential') is not None:
            self.credential = m.get('Credential')

        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')

        if m.get('DataSourceName') is not None:
            self.data_source_name = m.get('DataSourceName')

        if m.get('Exclude') is not None:
            self.exclude = m.get('Exclude')

        if m.get('Include') is not None:
            self.include = m.get('Include')

        if m.get('IndexLevel') is not None:
            self.index_level = m.get('IndexLevel')

        if m.get('Options') is not None:
            self.options = m.get('Options')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')

        if m.get('SpeedLimit') is not None:
            self.speed_limit = m.get('SpeedLimit')

        return self

