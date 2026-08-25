# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class AddDataSourceRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        connection_info: str = None,
        credential: str = None,
        data_source_name: str = None,
        data_source_type: str = None,
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
        # - Local NAS data source:
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
        # - CPFS AI-Computing Edition data source:
        #   {"vpcMountTarget":"cpfs-010wn\\*\\*\\*wy-vpc-ta\\*\\*\\*8.cn-shanghai.cpfs.aliyuncs.com","sharePath":"/"}
        # 
        # - Other large-scale file system data source:
        #   {"path":"/mnt"}
        self.connection_info = connection_info
        # The access credential for the data source. This parameter is required for local NAS (SMB) data sources and for OSS- or S3-compatible data sources. Examples:
        # 
        # - Local NAS data source (SMB protocol):
        #   {
        #   "mountUsername": "\\*\\*\\*\\*\\*",
        #   "mountPassword": "\\*\\*\\*\\*\\*"
        #   }
        # 
        # - OSS-compatible or S3-compatible data source:
        #   {
        #   "accessKeyId": "\\*\\*\\*\\*\\*",
        #   "accessKeySecret": "\\*\\*\\*\\*\\*"
        #   }
        self.credential = credential
        # The name of the data source.
        # 
        # This parameter is required.
        self.data_source_name = data_source_name
        # The type of the data source.
        # 
        # This parameter is required.
        self.data_source_type = data_source_type
        # A filter that specifies the files to exclude. This parameter applies only to data source analysis with the archive feature.
        self.exclude = exclude
        # A filter that specifies the files to include. This parameter applies only to data source analysis with the archive feature.
        self.include = include
        # The index level. This parameter applies only to data source analysis with the archive feature.
        # 
        # - `OFF`: No index is created.
        # 
        # - `META`: A metadata index is created.
        # 
        # - `ALL`: A full-text index is created. (Deprecated)
        self.index_level = index_level
        # The options for data source analysis. This parameter applies only to data source analysis with the archive feature.
        self.options = options
        # A list of paths for data source analysis. This parameter applies only to data source analysis with the archive feature.
        self.path = path
        # The execution schedule. This parameter applies only to data source analysis with the archive feature. The format `I|{startTime}|{interval}` specifies a task that runs at a defined interval starting from `{startTime}`. `{interval}` is an ISO 8601 duration. For example, `PT1H` specifies a one-hour interval, and `P1D` specifies a one-day interval.
        self.schedule = schedule
        # The rate limiting settings. This parameter applies only to data source analysis with the archive feature.
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

        if self.data_source_name is not None:
            result['DataSourceName'] = self.data_source_name

        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type

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

        if m.get('DataSourceName') is not None:
            self.data_source_name = m.get('DataSourceName')

        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')

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

