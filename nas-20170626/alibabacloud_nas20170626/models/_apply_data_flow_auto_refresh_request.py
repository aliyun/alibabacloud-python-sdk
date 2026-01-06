# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nas20170626 import models as main_models
from darabonba.model import DaraModel

class ApplyDataFlowAutoRefreshRequest(DaraModel):
    def __init__(
        self,
        auto_refresh_interval: int = None,
        auto_refresh_policy: str = None,
        auto_refreshs: List[main_models.ApplyDataFlowAutoRefreshRequestAutoRefreshs] = None,
        client_token: str = None,
        data_flow_id: str = None,
        dry_run: bool = None,
        file_system_id: str = None,
    ):
        # The automatic update interval. CPFS checks whether data is updated in the directory at the interval specified by this parameter. If data is updated, CPFS starts an automatic update task. Unit: minute.
        # 
        # Valid values: 10 to 525600. Default value: 10.
        self.auto_refresh_interval = auto_refresh_interval
        # The automatic update policy. The updated data in the source storage is imported into the CPFS file system based on the policy. Valid values:
        # 
        # *   None (default): Updated data in the source storage is not automatically imported into the CPFS file system. You can run a dataflow task to import the updated data from the source storage.
        # *   ImportChanged: Updated data in the source storage is automatically imported into the CPFS file system.
        self.auto_refresh_policy = auto_refresh_policy
        # The automatic update configurations.
        # 
        # This parameter is required.
        self.auto_refreshs = auto_refreshs
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.
        # 
        # The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How do I ensure the idempotence?](https://help.aliyun.com/document_detail/25693.html)
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The value of RequestId may be different for each API request.
        self.client_token = client_token
        # The ID of the dataflow.
        # 
        # This parameter is required.
        self.data_flow_id = data_flow_id
        # Specifies whether to perform a dry run.
        # 
        # During the dry run, the system checks whether the request parameters are valid and whether the requested resources are available. During the dry run, no file system is created and no fee is incurred.
        # 
        # Valid values:
        # 
        # *   true: performs a dry run. The system checks the required parameters, request syntax, limits, and available NAS resources. If the request fails the dry run, an error message is returned. If the request passes the dry run, the HTTP status code 200 is returned. No value is returned for the FileSystemId parameter.
        # *   false (default): performs a dry run and sends the request. If the request passes the dry run, a file system is created.
        self.dry_run = dry_run
        # The ID of the file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id

    def validate(self):
        if self.auto_refreshs:
            for v1 in self.auto_refreshs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_refresh_interval is not None:
            result['AutoRefreshInterval'] = self.auto_refresh_interval

        if self.auto_refresh_policy is not None:
            result['AutoRefreshPolicy'] = self.auto_refresh_policy

        result['AutoRefreshs'] = []
        if self.auto_refreshs is not None:
            for k1 in self.auto_refreshs:
                result['AutoRefreshs'].append(k1.to_map() if k1 else None)

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.data_flow_id is not None:
            result['DataFlowId'] = self.data_flow_id

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRefreshInterval') is not None:
            self.auto_refresh_interval = m.get('AutoRefreshInterval')

        if m.get('AutoRefreshPolicy') is not None:
            self.auto_refresh_policy = m.get('AutoRefreshPolicy')

        self.auto_refreshs = []
        if m.get('AutoRefreshs') is not None:
            for k1 in m.get('AutoRefreshs'):
                temp_model = main_models.ApplyDataFlowAutoRefreshRequestAutoRefreshs()
                self.auto_refreshs.append(temp_model.from_map(k1))

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DataFlowId') is not None:
            self.data_flow_id = m.get('DataFlowId')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        return self



class ApplyDataFlowAutoRefreshRequestAutoRefreshs(DaraModel):
    def __init__(
        self,
        refresh_path: str = None,
    ):
        # The automatic update directory. CPFS automatically checks whether the source data only in the directory is updated and imports the updated data.
        # 
        # Limits:
        # 
        # *   The directory must be 2 to 1,024 characters in length.
        # *   The directory must be encoded in UTF-8.
        # *   The directory must start and end with a forward slash (/).
        # 
        # >  The directory must be an existing directory in the CPFS file system and must be in a fileset where the dataflow is enabled.
        # 
        # This parameter is required.
        self.refresh_path = refresh_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.refresh_path is not None:
            result['RefreshPath'] = self.refresh_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RefreshPath') is not None:
            self.refresh_path = m.get('RefreshPath')

        return self

