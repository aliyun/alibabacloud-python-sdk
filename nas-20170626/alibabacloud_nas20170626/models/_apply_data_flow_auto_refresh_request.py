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
        # The auto-refresh interval. CPFS checks the directory for data updates at this interval. If data updates exist, an auto-refresh task is started. Unit: minutes.
        # 
        # Valid values: 10 to 525600. Default value: 10.
        self.auto_refresh_interval = auto_refresh_interval
        # The auto-refresh policy. This policy determines how data updates from the source are imported to CPFS. Valid values:
        # 
        # - None: Data updates from the source are not automatically imported to CPFS. You can use a data flow task to import data updates from the source.
        # - ImportChanged: Data updates from the source are automatically imported to CPFS.
        self.auto_refresh_policy = auto_refresh_policy
        # The collection of auto-refresh configurations.
        # 
        # This parameter is required.
        self.auto_refreshs = auto_refreshs
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but make sure that the token is unique among different requests.
        # 
        # The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        # 
        # > If you do not specify this parameter, the system automatically uses the RequestId of the API request as the ClientToken. The RequestId may differ for each API request.
        self.client_token = client_token
        # The ID of the data flow.
        # 
        # This parameter is required.
        self.data_flow_id = data_flow_id
        # Specifies whether to perform a dry run for this request.
        # 
        # A dry run checks parameter validity and resource availability without actually creating an instance or incurring charges.
        # 
        # Valid values:
        # 
        # - true: Sends a dry run request without creating an instance. The check items include required parameters, request format, business limits, and NAS inventory. If the check fails, the corresponding error is returned. If the check succeeds, HTTP status code 200 is returned, but FileSystemId is empty.
        # - false (default): Sends a normal request. After the check succeeds, the instance is created.
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
        # The auto-refresh directory. CPFS automatically checks whether data in this directory on the source has been updated and imports the updated data.
        # 
        # Limits:
        # 
        # - The path must be 2 to 1,024 characters in length.
        # - The path must be encoded in UTF-8.
        # - The path must start and end with a forward slash (/).
        # 
        # > The directory must already exist in CPFS and must be in a fileset that has data flow enabled.
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

