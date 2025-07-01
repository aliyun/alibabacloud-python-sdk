# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class AddClientToBlackListRequest(TeaModel):
    def __init__(
        self,
        client_ip: str = None,
        client_token: str = None,
        file_system_id: str = None,
        region_id: str = None,
    ):
        # The IP address of the client to add.
        # 
        # This parameter is required.
        self.client_ip = client_ip
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        # 
        # For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        # 
        # This parameter is required.
        self.client_token = client_token
        # The ID of the file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The ID of the region where the file system resides.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_ip is not None:
            result['ClientIP'] = self.client_ip
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientIP') is not None:
            self.client_ip = m.get('ClientIP')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AddClientToBlackListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddClientToBlackListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddClientToBlackListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AddClientToBlackListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ApplyAutoSnapshotPolicyRequest(TeaModel):
    def __init__(
        self,
        auto_snapshot_policy_id: str = None,
        file_system_ids: str = None,
    ):
        # The ID of the automatic snapshot policy.
        # 
        # This parameter is required.
        self.auto_snapshot_policy_id = auto_snapshot_policy_id
        # The IDs of advanced Extreme NAS file systems.
        # 
        # You can specify a maximum of 100 file system IDs at a time. If you want to apply an automatic snapshot policy to multiple file systems, separate the file system IDs with commas (,).
        # 
        # This parameter is required.
        self.file_system_ids = file_system_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_snapshot_policy_id is not None:
            result['AutoSnapshotPolicyId'] = self.auto_snapshot_policy_id
        if self.file_system_ids is not None:
            result['FileSystemIds'] = self.file_system_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoSnapshotPolicyId') is not None:
            self.auto_snapshot_policy_id = m.get('AutoSnapshotPolicyId')
        if m.get('FileSystemIds') is not None:
            self.file_system_ids = m.get('FileSystemIds')
        return self


class ApplyAutoSnapshotPolicyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ApplyAutoSnapshotPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ApplyAutoSnapshotPolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ApplyAutoSnapshotPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ApplyDataFlowAutoRefreshRequestAutoRefreshs(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.refresh_path is not None:
            result['RefreshPath'] = self.refresh_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RefreshPath') is not None:
            self.refresh_path = m.get('RefreshPath')
        return self


class ApplyDataFlowAutoRefreshRequest(TeaModel):
    def __init__(
        self,
        auto_refresh_interval: int = None,
        auto_refresh_policy: str = None,
        auto_refreshs: List[ApplyDataFlowAutoRefreshRequestAutoRefreshs] = None,
        client_token: str = None,
        data_flow_id: str = None,
        dry_run: bool = None,
        file_system_id: str = None,
    ):
        # The automatic update interval. CPFS checks whether data is updated in the directory at the interval specified by this parameter. If data is updated, CPFS starts an automatic update task. Unit: minutes.
        # 
        # Valid values: 5 to 526600. Default value: 10.
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
        # The dataflow ID.
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
            for k in self.auto_refreshs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_refresh_interval is not None:
            result['AutoRefreshInterval'] = self.auto_refresh_interval
        if self.auto_refresh_policy is not None:
            result['AutoRefreshPolicy'] = self.auto_refresh_policy
        result['AutoRefreshs'] = []
        if self.auto_refreshs is not None:
            for k in self.auto_refreshs:
                result['AutoRefreshs'].append(k.to_map() if k else None)
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
            for k in m.get('AutoRefreshs'):
                temp_model = ApplyDataFlowAutoRefreshRequestAutoRefreshs()
                self.auto_refreshs.append(temp_model.from_map(k))
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DataFlowId') is not None:
            self.data_flow_id = m.get('DataFlowId')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        return self


class ApplyDataFlowAutoRefreshResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ApplyDataFlowAutoRefreshResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ApplyDataFlowAutoRefreshResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ApplyDataFlowAutoRefreshResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelAutoSnapshotPolicyRequest(TeaModel):
    def __init__(
        self,
        file_system_ids: str = None,
    ):
        # The IDs of file systems.
        # 
        # You can specify a maximum of 100 file system IDs. If you want to remove automatic snapshot policies from multiple file systems, separate the file system IDs with commas (,).
        # 
        # This parameter is required.
        self.file_system_ids = file_system_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_ids is not None:
            result['FileSystemIds'] = self.file_system_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemIds') is not None:
            self.file_system_ids = m.get('FileSystemIds')
        return self


class CancelAutoSnapshotPolicyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        # 
        # Every response returns a unique request ID regardless of whether the request is successful.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CancelAutoSnapshotPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelAutoSnapshotPolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CancelAutoSnapshotPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelDataFlowAutoRefreshRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        data_flow_id: str = None,
        dry_run: bool = None,
        file_system_id: str = None,
        refresh_path: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.
        # 
        # The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How do I ensure the idempotence?](https://help.aliyun.com/document_detail/25693.html)
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The value of RequestId may be different for each API request.
        self.client_token = client_token
        # The dataflow ID.
        # 
        # This parameter is required.
        self.data_flow_id = data_flow_id
        # Specifies whether to perform a dry run.
        # 
        # During the dry run, the system checks whether the request parameters are valid and whether the requested resources are available. During the dry run, no file system is created and no fee is incurred.
        # 
        # Valid values:
        # 
        # *   true: performs a dry run. The system checks the request format, service limits, prerequisites, and whether the required parameters are specified. If the request fails the dry run, an error message is returned. If the request passes the dry run, the HTTP status code 200 is returned. No value is returned for the DataFlowld parameter.
        # *   false (default): performs a dry run and sends the request. If the request passes the dry run, a file system is created.
        self.dry_run = dry_run
        # The ID of the file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The directory for which you want to cancel AutoRefresh configurations.
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.data_flow_id is not None:
            result['DataFlowId'] = self.data_flow_id
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.refresh_path is not None:
            result['RefreshPath'] = self.refresh_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DataFlowId') is not None:
            self.data_flow_id = m.get('DataFlowId')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('RefreshPath') is not None:
            self.refresh_path = m.get('RefreshPath')
        return self


class CancelDataFlowAutoRefreshResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CancelDataFlowAutoRefreshResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelDataFlowAutoRefreshResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CancelDataFlowAutoRefreshResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelDataFlowSubTaskRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        data_flow_id: str = None,
        data_flow_sub_task_id: str = None,
        data_flow_task_id: str = None,
        dry_run: bool = None,
        file_system_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.
        # 
        # The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How do I ensure the idempotence?](https://help.aliyun.com/document_detail/25693.html)
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token
        # The ID of the data flow.
        # 
        # This parameter is required.
        self.data_flow_id = data_flow_id
        # The ID of the data streaming task.
        # 
        # This parameter is required.
        self.data_flow_sub_task_id = data_flow_sub_task_id
        # The ID of the data flow task.
        # 
        # This parameter is required.
        self.data_flow_task_id = data_flow_task_id
        # Specifies whether to perform a dry run.
        # 
        # During the dry run, the system checks whether the request parameters are valid and whether the requested resources are available. During the dry run, no data streaming task is created and no fee is incurred.
        # 
        # Valid values:
        # 
        # *   true: performs a dry run. The system checks the required parameters, request syntax, service limits, and available File Storage NAS (NAS) resources. If the request fails the dry run, an error message is returned. If the request passes the dry run, the HTTP status code 200 is returned.
        # *   false (default): performs a dry run and sends the request. If the request passes the dry run, a data streaming task is created.
        self.dry_run = dry_run
        # The ID of the file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.data_flow_id is not None:
            result['DataFlowId'] = self.data_flow_id
        if self.data_flow_sub_task_id is not None:
            result['DataFlowSubTaskId'] = self.data_flow_sub_task_id
        if self.data_flow_task_id is not None:
            result['DataFlowTaskId'] = self.data_flow_task_id
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DataFlowId') is not None:
            self.data_flow_id = m.get('DataFlowId')
        if m.get('DataFlowSubTaskId') is not None:
            self.data_flow_sub_task_id = m.get('DataFlowSubTaskId')
        if m.get('DataFlowTaskId') is not None:
            self.data_flow_task_id = m.get('DataFlowTaskId')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        return self


class CancelDataFlowSubTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CancelDataFlowSubTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelDataFlowSubTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CancelDataFlowSubTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelDataFlowTaskRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        data_flow_id: str = None,
        dry_run: bool = None,
        file_system_id: str = None,
        task_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.
        # 
        # The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How do I ensure the idempotence?](https://help.aliyun.com/document_detail/25693.html)
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token
        # The dataflow ID.
        # 
        # This parameter is required.
        self.data_flow_id = data_flow_id
        # Specifies whether to perform only a dry run, without performing the actual request.
        # 
        # During the dry run, the system checks whether the request parameters are valid and whether the requested resources are available. The dry run does not cancel the specified dataflow task or incur fees.
        # 
        # Valid values:
        # 
        # *   true: performs only a dry run. The system checks the required parameters, request syntax, service limits, and available NAS resources. If the request fails the dry run, an error message is returned. If the request passes the dry run, the HTTP status code 200 is returned.
        # *   false (default): performs a dry run and sends the request. If the request passes the dry run, the specified dataflow task is canceled.
        self.dry_run = dry_run
        # The ID of the file system.
        # 
        # *   The IDs of CPFS file systems must start with `cpfs-`. Example: cpfs-125487\\*\\*\\*\\*.
        # *   The IDs of CPFS for LINGJUN file systems must start with `bmcpfs-`. Example: bmcpfs-0015\\*\\*\\*\\*.
        # 
        # >  CPFS is not supported on the international site.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The ID of the dataflow task.
        # 
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.data_flow_id is not None:
            result['DataFlowId'] = self.data_flow_id
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DataFlowId') is not None:
            self.data_flow_id = m.get('DataFlowId')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CancelDataFlowTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CancelDataFlowTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelDataFlowTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CancelDataFlowTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelDirQuotaRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        path: str = None,
        user_id: str = None,
        user_type: str = None,
    ):
        # The ID of the file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The absolute path of a directory.
        # 
        # This parameter is required.
        self.path = path
        # The UID or GID of a user for whom you want to cancel the directory quota.
        # 
        # This parameter is required and valid only if the UserType parameter is set to Uid or Gid.
        # 
        # Examples:
        # 
        # *   If you want to cancel a quota for a user whose UID is 500, set the UserType parameter to Uid and set the UserId parameter to 500.
        # *   If you want to cancel a quota for a group whose GID is 100, set the UserType parameter to Gid and set the UserId parameter to 100.
        self.user_id = user_id
        # The type of the user.
        # 
        # Valid values:
        # 
        # *   Uid: user ID
        # *   Gid: user group ID
        # *   AllUsers: all users
        # 
        # This parameter is required.
        self.user_type = user_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.path is not None:
            result['Path'] = self.path
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class CancelDirQuotaResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CancelDirQuotaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelDirQuotaResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CancelDirQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelFilesetQuotaRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        file_system_id: str = None,
        fset_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.
        # 
        # The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How do I ensure the idempotence?](https://help.aliyun.com/document_detail/25693.html)
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform a dry run.
        # 
        # During the dry run, the system checks whether the request parameters are valid and whether the requested resources are available. During the dry run, no fileset quota is canceled and no fee is incurred.
        # 
        # Valid values:
        # 
        # *   true: performs a dry run. The system checks the required parameters, request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the HTTP status code 200 is returned. No value is returned for the DataFlowld parameter.
        # *   false (default): performs a dry run and sends the request. If the request passes the dry run, the fileset quota is canceled.
        self.dry_run = dry_run
        # The ID of the CPFS for LINGJUN file system. The IDs of CPFS for LINGJUN file systems must start with `bmcpfs-`. Example: bmcpfs-290w65p03ok64ya\\*\\*\\*\\*.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The fileset ID.
        # 
        # This parameter is required.
        self.fset_id = fset_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.fset_id is not None:
            result['FsetId'] = self.fset_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('FsetId') is not None:
            self.fset_id = m.get('FsetId')
        return self


class CancelFilesetQuotaResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CancelFilesetQuotaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelFilesetQuotaResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CancelFilesetQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelLifecycleRetrieveJobRequest(TeaModel):
    def __init__(
        self,
        job_id: str = None,
    ):
        # The ID of the data retrieval task.
        # 
        # This parameter is required.
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class CancelLifecycleRetrieveJobResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CancelLifecycleRetrieveJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelLifecycleRetrieveJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CancelLifecycleRetrieveJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelRecycleBinJobRequest(TeaModel):
    def __init__(
        self,
        job_id: str = None,
    ):
        # The job ID.
        # 
        # This parameter is required.
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class CancelRecycleBinJobResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CancelRecycleBinJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelRecycleBinJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CancelRecycleBinJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangeResourceGroupRequest(TeaModel):
    def __init__(
        self,
        new_resource_group_id: str = None,
        region_id: str = None,
        resource_id: str = None,
        resource_type: str = None,
    ):
        # The ID of the new resource group.
        # 
        # You can log on to the [Resource Management console](https://resourcemanager.console.aliyun.com/resource-groups?) to view resource group IDs.
        # 
        # This parameter is required.
        self.new_resource_group_id = new_resource_group_id
        # The region ID of the zone.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/2412111.html) operation to query the latest region list.
        self.region_id = region_id
        # The resource ID.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The resource type.
        # 
        # Set the value to filesystem.
        # 
        # This parameter is required.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.new_resource_group_id is not None:
            result['NewResourceGroupId'] = self.new_resource_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewResourceGroupId') is not None:
            self.new_resource_group_id = m.get('NewResourceGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ChangeResourceGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ChangeResourceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ChangeResourceGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ChangeResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAccessGroupRequest(TeaModel):
    def __init__(
        self,
        access_group_name: str = None,
        access_group_type: str = None,
        description: str = None,
        file_system_type: str = None,
    ):
        # The name of the permission group.
        # 
        # Limits:
        # 
        # *   The name must be 3 to 64 characters in length.
        # *   The name must start with a letter and can contain letters, digits, underscores (_), and hyphens (-).
        # *   The name must be different from the name of the default permission group.
        # 
        # The default permission group for virtual private clouds (VPCs) is named DEFAULT_VPC_GROUP_NAME.
        # 
        # This parameter is required.
        self.access_group_name = access_group_name
        # The network type of the permission group. Valid value: **Vpc**.
        # 
        # This parameter is required.
        self.access_group_type = access_group_type
        # The description of the permission group.
        # 
        # Limits:
        # 
        # *   By default, the description of a permission group is the same as the name of the permission group. The description must be 2 to 128 characters in length.
        # *   The name must start with a letter and cannot start with `http://` or `https://`.
        # *   The description can contain digits, colons (:), underscores (_), and hyphens (-).
        self.description = description
        # The type of the file system.
        # 
        # Valid values:
        # 
        # *   standard (default): General-purpose NAS file system
        # *   extreme: Extreme NAS file system
        self.file_system_type = file_system_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group_name is not None:
            result['AccessGroupName'] = self.access_group_name
        if self.access_group_type is not None:
            result['AccessGroupType'] = self.access_group_type
        if self.description is not None:
            result['Description'] = self.description
        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessGroupName') is not None:
            self.access_group_name = m.get('AccessGroupName')
        if m.get('AccessGroupType') is not None:
            self.access_group_type = m.get('AccessGroupType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')
        return self


class CreateAccessGroupResponseBody(TeaModel):
    def __init__(
        self,
        access_group_name: str = None,
        request_id: str = None,
    ):
        # The name of the permission group.
        self.access_group_name = access_group_name
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group_name is not None:
            result['AccessGroupName'] = self.access_group_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessGroupName') is not None:
            self.access_group_name = m.get('AccessGroupName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAccessGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAccessGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateAccessGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAccessPointRequest(TeaModel):
    def __init__(
        self,
        access_group: str = None,
        access_point_name: str = None,
        enabled_ram: bool = None,
        file_system_id: str = None,
        owner_group_id: int = None,
        owner_user_id: int = None,
        permission: str = None,
        posix_group_id: int = None,
        posix_secondary_group_ids: str = None,
        posix_user_id: int = None,
        root_directory: str = None,
        vpc_id: str = None,
        vsw_id: str = None,
    ):
        # The name of the permission group.
        # 
        # This parameter is required for a General-purpose File Storage NAS (NAS) file system.
        # 
        # The default permission group for virtual private clouds (VPCs) is named DEFAULT_VPC_GROUP_NAME.
        # 
        # This parameter is required.
        self.access_group = access_group
        # The name of the access point.
        self.access_point_name = access_point_name
        # Specifies whether to enable the RAM policy. Valid values:
        # 
        # *   true: The RAM policy is enabled.
        # *   false (default): The RAM policy is disabled.
        # 
        # >  After the RAM policy is enabled for access points, no RAM user is allowed to use access points to mount and access data by default. To use access points to mount and access data as a RAM user, you must grant the related access permissions to the RAM user. If the RAM policy is disabled, access points can be anonymously mounted. For more information about how to configure permissions on access points, see [Configure a policy for the access point](https://help.aliyun.com/document_detail/2545998.html).
        self.enabled_ram = enabled_ram
        # The ID of the file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The ID of the owner group.
        # 
        # This parameter is required if the RootDirectory directory does not exist.
        self.owner_group_id = owner_group_id
        # The owner ID.
        # 
        # This parameter is required if the RootDirectory directory does not exist.
        self.owner_user_id = owner_user_id
        # The Portable Operating System Interface for UNIX (POSIX) permission. Default value: 0777.
        # 
        # This field takes effect only if you specify the OwnerUserId and OwnerGroupId parameters.
        self.permission = permission
        # The ID of the POSIX user group.
        self.posix_group_id = posix_group_id
        # The secondary user group. Separate multiple user group IDs with commas (,).
        self.posix_secondary_group_ids = posix_secondary_group_ids
        # The ID of the POSIX user.
        self.posix_user_id = posix_user_id
        # The root directory of the access point. The default value is /. If the directory does not exist, you must also specify the OwnerUserId and OwnerGroupId parameters.
        self.root_directory = root_directory
        # The VPC ID.
        # 
        # This parameter is required.
        self.vpc_id = vpc_id
        # The vSwitch ID.
        # 
        # This parameter is required.
        self.vsw_id = vsw_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group is not None:
            result['AccessGroup'] = self.access_group
        if self.access_point_name is not None:
            result['AccessPointName'] = self.access_point_name
        if self.enabled_ram is not None:
            result['EnabledRam'] = self.enabled_ram
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.owner_group_id is not None:
            result['OwnerGroupId'] = self.owner_group_id
        if self.owner_user_id is not None:
            result['OwnerUserId'] = self.owner_user_id
        if self.permission is not None:
            result['Permission'] = self.permission
        if self.posix_group_id is not None:
            result['PosixGroupId'] = self.posix_group_id
        if self.posix_secondary_group_ids is not None:
            result['PosixSecondaryGroupIds'] = self.posix_secondary_group_ids
        if self.posix_user_id is not None:
            result['PosixUserId'] = self.posix_user_id
        if self.root_directory is not None:
            result['RootDirectory'] = self.root_directory
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vsw_id is not None:
            result['VswId'] = self.vsw_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessGroup') is not None:
            self.access_group = m.get('AccessGroup')
        if m.get('AccessPointName') is not None:
            self.access_point_name = m.get('AccessPointName')
        if m.get('EnabledRam') is not None:
            self.enabled_ram = m.get('EnabledRam')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('OwnerGroupId') is not None:
            self.owner_group_id = m.get('OwnerGroupId')
        if m.get('OwnerUserId') is not None:
            self.owner_user_id = m.get('OwnerUserId')
        if m.get('Permission') is not None:
            self.permission = m.get('Permission')
        if m.get('PosixGroupId') is not None:
            self.posix_group_id = m.get('PosixGroupId')
        if m.get('PosixSecondaryGroupIds') is not None:
            self.posix_secondary_group_ids = m.get('PosixSecondaryGroupIds')
        if m.get('PosixUserId') is not None:
            self.posix_user_id = m.get('PosixUserId')
        if m.get('RootDirectory') is not None:
            self.root_directory = m.get('RootDirectory')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswId') is not None:
            self.vsw_id = m.get('VswId')
        return self


class CreateAccessPointResponseBodyAccessPoint(TeaModel):
    def __init__(
        self,
        access_point_domain: str = None,
        access_point_id: str = None,
    ):
        # The domain name of the access point.
        self.access_point_domain = access_point_domain
        # The ID of the access point.
        self.access_point_id = access_point_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_point_domain is not None:
            result['AccessPointDomain'] = self.access_point_domain
        if self.access_point_id is not None:
            result['AccessPointId'] = self.access_point_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessPointDomain') is not None:
            self.access_point_domain = m.get('AccessPointDomain')
        if m.get('AccessPointId') is not None:
            self.access_point_id = m.get('AccessPointId')
        return self


class CreateAccessPointResponseBody(TeaModel):
    def __init__(
        self,
        access_point: CreateAccessPointResponseBodyAccessPoint = None,
        request_id: str = None,
    ):
        # The access point.
        self.access_point = access_point
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.access_point:
            self.access_point.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_point is not None:
            result['AccessPoint'] = self.access_point.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessPoint') is not None:
            temp_model = CreateAccessPointResponseBodyAccessPoint()
            self.access_point = temp_model.from_map(m['AccessPoint'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAccessPointResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAccessPointResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateAccessPointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAccessRuleRequest(TeaModel):
    def __init__(
        self,
        access_group_name: str = None,
        file_system_type: str = None,
        ipv_6source_cidr_ip: str = None,
        priority: int = None,
        rwaccess_type: str = None,
        source_cidr_ip: str = None,
        user_access_type: str = None,
    ):
        # The name of the permission group.
        # 
        # This parameter is required.
        self.access_group_name = access_group_name
        # The type of the file system.
        # 
        # Valid values:
        # 
        # *   standard (default): General-purpose NAS file system
        # *   extreme: Extreme NAS file system
        self.file_system_type = file_system_type
        # The IPv6 address or CIDR block of the authorized object.
        # 
        # You must set this parameter to an IPv6 address or CIDR block.
        # 
        # > *   Only Extreme NAS file systems that reside in the Chinese mainland support IPv6. If you specify this parameter, you must enable IPv6 for the file system.
        # >*   Only permission groups that reside in virtual private clouds (VPCs) support IPv6.
        # >*   You cannot specify an IPv4 address and an IPv6 address at the same time.
        self.ipv_6source_cidr_ip = ipv_6source_cidr_ip
        # The priority of the rule.
        # 
        # The rule with the highest priority takes effect if multiple rules are attached to the authorized object.
        # 
        # Valid values: 1 to 100. The value 1 indicates the highest priority.
        self.priority = priority
        # The access permissions of the authorized object on the file system.
        # 
        # Valid values:
        # 
        # *   RDWR (default): the read and write permissions
        # *   RDONLY: the read-only permissions
        self.rwaccess_type = rwaccess_type
        # The IP address or CIDR block of the authorized object.
        # 
        # You must set this parameter to an IP address or CIDR block.
        # 
        # > If the permission group resides in the classic network, you must set this parameter to an IP address.
        self.source_cidr_ip = source_cidr_ip
        # The access permissions for different types of users in the authorized object.
        # 
        # Valid values:
        # 
        # *   no_squash (default): grants root users the permissions to access the file system.
        # *   root_squash: grants root users the least permissions as the nobody user.
        # *   all_squash: grants all users the least permissions as the nobody user.
        # 
        # The nobody user has the least permissions in Linux and can access only the public content of the file system. This ensures the security of the file system.
        self.user_access_type = user_access_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group_name is not None:
            result['AccessGroupName'] = self.access_group_name
        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type
        if self.ipv_6source_cidr_ip is not None:
            result['Ipv6SourceCidrIp'] = self.ipv_6source_cidr_ip
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.rwaccess_type is not None:
            result['RWAccessType'] = self.rwaccess_type
        if self.source_cidr_ip is not None:
            result['SourceCidrIp'] = self.source_cidr_ip
        if self.user_access_type is not None:
            result['UserAccessType'] = self.user_access_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessGroupName') is not None:
            self.access_group_name = m.get('AccessGroupName')
        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')
        if m.get('Ipv6SourceCidrIp') is not None:
            self.ipv_6source_cidr_ip = m.get('Ipv6SourceCidrIp')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('RWAccessType') is not None:
            self.rwaccess_type = m.get('RWAccessType')
        if m.get('SourceCidrIp') is not None:
            self.source_cidr_ip = m.get('SourceCidrIp')
        if m.get('UserAccessType') is not None:
            self.user_access_type = m.get('UserAccessType')
        return self


class CreateAccessRuleResponseBody(TeaModel):
    def __init__(
        self,
        access_rule_id: str = None,
        request_id: str = None,
    ):
        # The rule ID.
        self.access_rule_id = access_rule_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_rule_id is not None:
            result['AccessRuleId'] = self.access_rule_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessRuleId') is not None:
            self.access_rule_id = m.get('AccessRuleId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAccessRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAccessRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateAccessRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAutoSnapshotPolicyRequest(TeaModel):
    def __init__(
        self,
        auto_snapshot_policy_name: str = None,
        file_system_type: str = None,
        repeat_weekdays: str = None,
        retention_days: int = None,
        time_points: str = None,
    ):
        # The name of the automatic snapshot policy.
        # 
        # Limits:
        # 
        # *   The name must be 2 to 128 characters in length.
        # *   The name must start with a letter.
        # *   The name can contain digits, colons (:), underscores (_), and hyphens (-). It cannot start with `http://` or `https://`.
        # *   This parameter is empty by default.
        self.auto_snapshot_policy_name = auto_snapshot_policy_name
        # The type of the file system.
        # 
        # Valid value: extreme, which indicates Extreme NAS file systems.
        # 
        # This parameter is required.
        self.file_system_type = file_system_type
        # The days of a week on which to create automatic snapshots.
        # 
        # Cycle: week.
        # 
        # Valid values: 1 to 7. The values from 1 to 7 indicate the seven days in a week from Monday to Sunday.
        # 
        # If you want to create multiple auto snapshots within a week, you can specify multiple days from Monday to Sunday and separate the days with commas (,). You can specify a maximum of seven days.
        # 
        # This parameter is required.
        self.repeat_weekdays = repeat_weekdays
        # The retention period of auto snapshots.
        # 
        # Unit: days.
        # 
        # Valid values:
        # 
        # *   \\-1 (default). Auto snapshots are permanently retained. After the number of auto snapshots exceeds the upper limit, the earliest auto snapshot is automatically deleted.
        # *   1 to 65536: Auto snapshots are retained for the specified days. After the retention period of auto snapshots expires, the auto snapshots are automatically deleted.
        self.retention_days = retention_days
        # The points in time at which auto snapshots were created.
        # 
        # Unit: hours.
        # 
        # Valid values: 0 to 23. The values from 0 to 23 indicate a total of 24 hours from 00:00 to 23:00. For example, the value 1 indicates 01:00.
        # 
        # If you want to create multiple auto snapshots within a day, you can specify multiple points in time and separate the points in time with commas (,). You can specify a maximum of 24 points in time.
        # 
        # This parameter is required.
        self.time_points = time_points

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_snapshot_policy_name is not None:
            result['AutoSnapshotPolicyName'] = self.auto_snapshot_policy_name
        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type
        if self.repeat_weekdays is not None:
            result['RepeatWeekdays'] = self.repeat_weekdays
        if self.retention_days is not None:
            result['RetentionDays'] = self.retention_days
        if self.time_points is not None:
            result['TimePoints'] = self.time_points
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoSnapshotPolicyName') is not None:
            self.auto_snapshot_policy_name = m.get('AutoSnapshotPolicyName')
        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')
        if m.get('RepeatWeekdays') is not None:
            self.repeat_weekdays = m.get('RepeatWeekdays')
        if m.get('RetentionDays') is not None:
            self.retention_days = m.get('RetentionDays')
        if m.get('TimePoints') is not None:
            self.time_points = m.get('TimePoints')
        return self


class CreateAutoSnapshotPolicyResponseBody(TeaModel):
    def __init__(
        self,
        auto_snapshot_policy_id: str = None,
        request_id: str = None,
    ):
        # The ID of the automatic snapshot policy.
        self.auto_snapshot_policy_id = auto_snapshot_policy_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_snapshot_policy_id is not None:
            result['AutoSnapshotPolicyId'] = self.auto_snapshot_policy_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoSnapshotPolicyId') is not None:
            self.auto_snapshot_policy_id = m.get('AutoSnapshotPolicyId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAutoSnapshotPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAutoSnapshotPolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateAutoSnapshotPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDataFlowRequestAutoRefreshs(TeaModel):
    def __init__(
        self,
        refresh_path: str = None,
    ):
        # The automatic update directory. CPFS registers the data update event in the source storage, and automatically checks whether the source data in the directory is updated and imports the updated data.
        # 
        # This parameter is empty by default. Updated data in the source storage is not automatically imported into the CPFS file system. You must import the updated data by running a manual task.
        # 
        # Limits:
        # 
        # *   The directory must be 2 to 1,024 characters in length.
        # *   The directory must be encoded in UTF-8.
        # *   The directory must start and end with a forward slash (/).
        # *   The directory must be an existing directory in the CPFS file system and must be in a fileset where the data flow is enabled.
        self.refresh_path = refresh_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.refresh_path is not None:
            result['RefreshPath'] = self.refresh_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RefreshPath') is not None:
            self.refresh_path = m.get('RefreshPath')
        return self


class CreateDataFlowRequest(TeaModel):
    def __init__(
        self,
        auto_refresh_interval: int = None,
        auto_refresh_policy: str = None,
        auto_refreshs: List[CreateDataFlowRequestAutoRefreshs] = None,
        client_token: str = None,
        description: str = None,
        dry_run: bool = None,
        file_system_id: str = None,
        file_system_path: str = None,
        fset_id: str = None,
        source_security_type: str = None,
        source_storage: str = None,
        source_storage_path: str = None,
        throughput: int = None,
    ):
        # The automatic update interval. CPFS checks whether data is updated in the directory at the interval specified by this parameter. If data is updated, CPFS starts an automatic update task. Unit: minutes.
        # 
        # Valid values: 10 to 525600. Default value: 10.
        # 
        # >  This parameter takes effect only for CPFS file systems.
        self.auto_refresh_interval = auto_refresh_interval
        # The automatic update policy. The updated data in the source storage is imported into the CPFS file system based on the policy.
        # 
        # *   None (default): Updated data in the source storage is not automatically imported into the CPFS file system. You can run a data flow task to import the updated data from the source storage.
        # *   ImportChanged: Updated data in the source storage is automatically imported into the CPFS file system.
        # 
        # >  This parameter takes effect only for CPFS file systems.
        self.auto_refresh_policy = auto_refresh_policy
        # The automatic update configurations.
        # 
        # >  This parameter takes effect only for CPFS file systems.
        self.auto_refreshs = auto_refreshs
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.
        # 
        # The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How do I ensure the idempotence?](https://help.aliyun.com/document_detail/25693.html)
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The value of RequestId may be different for each API request.
        self.client_token = client_token
        # The description of the dataflow.
        # 
        # Limits:
        # 
        # *   The description must be 2 to 128 characters in length.
        # *   The description must start with a letter but cannot start with `http://` or `https://`.
        # *   The description can contain letters, digits, colons (:), underscores (_), and hyphens (-).
        self.description = description
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
        # *   The IDs of CPFS file systems must start with `cpfs-`. Example: cpfs-125487\\*\\*\\*\\*.
        # *   The IDs of CPFS for LINGJUN file systems must start with `bmcpfs-`. Example: bmcpfs-0015\\*\\*\\*\\*.
        # 
        # >  CPFS is not supported on the international site.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The directory in the CPFS for LINGJUN file system. Limits:
        # 
        # *   The directory must start and end with a forward slash (/).
        # *   The directory must be an existing directory in the CPFS for LINGJUN file system.
        # *   The directory must be 1 to 1023 characters in length.
        # *   The directory must be encoded in UTF-8.
        # 
        # >  This parameter is required for CPFS for LINGJUN file systems.
        self.file_system_path = file_system_path
        # The fileset ID.
        # 
        # >  This parameter is required for CPFS file systems.
        self.fset_id = fset_id
        # The type of security mechanism for the source storage. This parameter must be specified if the source storage is accessed with a security mechanism. Valid values:
        # 
        # *   None (default): The source storage can be accessed without a security mechanism.
        # *   SSL: The source storage must be accessed with an SSL certificate.
        self.source_security_type = source_security_type
        # The access path of the source storage. Format: `<storage type>://[<account id>:]<path>`.
        # 
        # Parameters:
        # 
        # *   storage type: Only OSS is supported.
        # 
        # *   account id (optional): the UID of the account of the source storage. This parameter is required when you use OSS buckets across accounts.
        # 
        # *   path: the name of the OSS bucket. Limits:
        # 
        #     *   The name can contain only lowercase letters, digits, and hyphens (-). The name must start and end with a lowercase letter or digit.
        #     *   The name can be up to 128 characters in length.
        #     *   The name must be encoded in UTF-8.
        # 
        # > *   The OSS bucket must be an existing bucket in the region.
        # > *   Only CPFS for LINGJUN V2.6.0 and later support the account id parameter.
        # 
        # This parameter is required.
        self.source_storage = source_storage
        # The access path in the bucket of the source storage. Limits:
        # 
        # *   The path must start and end with a forward slash (/).
        # *   The path is case-sensitive.
        # *   The path must be 1 to 1023 characters in length.
        # *   The path must be encoded in UTF-8.
        # 
        # >  This parameter is required for CPFS for LINGJUN file systems.
        self.source_storage_path = source_storage_path
        # The maximum data flow throughput. Unit: MB/s. Valid values:
        # 
        # *   600
        # *   1200
        # *   1500
        # 
        # >  The data flow throughput must be less than the I/O throughput of the file system. This parameter is required for CPFS file systems.
        self.throughput = throughput

    def validate(self):
        if self.auto_refreshs:
            for k in self.auto_refreshs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_refresh_interval is not None:
            result['AutoRefreshInterval'] = self.auto_refresh_interval
        if self.auto_refresh_policy is not None:
            result['AutoRefreshPolicy'] = self.auto_refresh_policy
        result['AutoRefreshs'] = []
        if self.auto_refreshs is not None:
            for k in self.auto_refreshs:
                result['AutoRefreshs'].append(k.to_map() if k else None)
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.file_system_path is not None:
            result['FileSystemPath'] = self.file_system_path
        if self.fset_id is not None:
            result['FsetId'] = self.fset_id
        if self.source_security_type is not None:
            result['SourceSecurityType'] = self.source_security_type
        if self.source_storage is not None:
            result['SourceStorage'] = self.source_storage
        if self.source_storage_path is not None:
            result['SourceStoragePath'] = self.source_storage_path
        if self.throughput is not None:
            result['Throughput'] = self.throughput
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRefreshInterval') is not None:
            self.auto_refresh_interval = m.get('AutoRefreshInterval')
        if m.get('AutoRefreshPolicy') is not None:
            self.auto_refresh_policy = m.get('AutoRefreshPolicy')
        self.auto_refreshs = []
        if m.get('AutoRefreshs') is not None:
            for k in m.get('AutoRefreshs'):
                temp_model = CreateDataFlowRequestAutoRefreshs()
                self.auto_refreshs.append(temp_model.from_map(k))
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('FileSystemPath') is not None:
            self.file_system_path = m.get('FileSystemPath')
        if m.get('FsetId') is not None:
            self.fset_id = m.get('FsetId')
        if m.get('SourceSecurityType') is not None:
            self.source_security_type = m.get('SourceSecurityType')
        if m.get('SourceStorage') is not None:
            self.source_storage = m.get('SourceStorage')
        if m.get('SourceStoragePath') is not None:
            self.source_storage_path = m.get('SourceStoragePath')
        if m.get('Throughput') is not None:
            self.throughput = m.get('Throughput')
        return self


class CreateDataFlowResponseBody(TeaModel):
    def __init__(
        self,
        data_flow_id: str = None,
        request_id: str = None,
    ):
        # The dataflow ID.
        self.data_flow_id = data_flow_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_flow_id is not None:
            result['DataFlowId'] = self.data_flow_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataFlowId') is not None:
            self.data_flow_id = m.get('DataFlowId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDataFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDataFlowResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateDataFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDataFlowSubTaskRequestCondition(TeaModel):
    def __init__(
        self,
        modify_time: int = None,
        size: int = None,
    ):
        # The modification time. The value must be a UNIX timestamp. Unit: ns.
        self.modify_time = modify_time
        # The file size. Unit: bytes.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class CreateDataFlowSubTaskRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        condition: CreateDataFlowSubTaskRequestCondition = None,
        data_flow_id: str = None,
        data_flow_task_id: str = None,
        dry_run: bool = None,
        dst_file_path: str = None,
        file_system_id: str = None,
        src_file_path: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.
        # 
        # The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How do I ensure the idempotence?](https://help.aliyun.com/document_detail/25693.html)
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token
        # The check conditions. The check must be passed after the following conditions are specified.
        self.condition = condition
        # The ID of the data flow.
        # 
        # This parameter is required.
        self.data_flow_id = data_flow_id
        # The ID of the data flow task.
        # 
        # >  Only the IDs of data streaming tasks are supported.
        # 
        # This parameter is required.
        self.data_flow_task_id = data_flow_task_id
        # Specifies whether to perform a dry run.
        # 
        # During the dry run, the system checks whether the request parameters are valid and whether the requested resources are available. During the dry run, no data streaming subtask is created and no fee is incurred.
        # 
        # Valid values:
        # 
        # *   true: performs a dry run. The system checks the required parameters, request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the HTTP status code 200 is returned. No value is returned for the DataFlowSubTaskId parameter.
        # *   false (default): performs a dry run and sends the request. If the request passes the dry run, a data streaming subtask is created.
        self.dry_run = dry_run
        # The path of the destination file. Limits:
        # 
        # *   The path must be 1 to 1,023 characters in length.
        # *   The path must be encoded in UTF-8.
        # *   The path must start with a forward slash (/).
        # *   The path must end with the file name.
        # 
        # This parameter is required.
        self.dst_file_path = dst_file_path
        # The ID of the file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The path of the source file. Limits:
        # 
        # *   The path must be 1 to 1,023 characters in length.
        # *   The path must be encoded in UTF-8.
        # *   The path must start with a forward slash (/).
        # *   The path must end with the file name.
        # 
        # This parameter is required.
        self.src_file_path = src_file_path

    def validate(self):
        if self.condition:
            self.condition.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.condition is not None:
            result['Condition'] = self.condition.to_map()
        if self.data_flow_id is not None:
            result['DataFlowId'] = self.data_flow_id
        if self.data_flow_task_id is not None:
            result['DataFlowTaskId'] = self.data_flow_task_id
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.dst_file_path is not None:
            result['DstFilePath'] = self.dst_file_path
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.src_file_path is not None:
            result['SrcFilePath'] = self.src_file_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Condition') is not None:
            temp_model = CreateDataFlowSubTaskRequestCondition()
            self.condition = temp_model.from_map(m['Condition'])
        if m.get('DataFlowId') is not None:
            self.data_flow_id = m.get('DataFlowId')
        if m.get('DataFlowTaskId') is not None:
            self.data_flow_task_id = m.get('DataFlowTaskId')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('DstFilePath') is not None:
            self.dst_file_path = m.get('DstFilePath')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('SrcFilePath') is not None:
            self.src_file_path = m.get('SrcFilePath')
        return self


class CreateDataFlowSubTaskResponseBody(TeaModel):
    def __init__(
        self,
        data_flow_sub_task_id: str = None,
        request_id: str = None,
    ):
        # The ID of the data streaming task.
        self.data_flow_sub_task_id = data_flow_sub_task_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_flow_sub_task_id is not None:
            result['DataFlowSubTaskId'] = self.data_flow_sub_task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataFlowSubTaskId') is not None:
            self.data_flow_sub_task_id = m.get('DataFlowSubTaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDataFlowSubTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDataFlowSubTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateDataFlowSubTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDataFlowTaskRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        conflict_policy: str = None,
        create_dir_if_not_exist: bool = None,
        data_flow_id: str = None,
        data_type: str = None,
        directory: str = None,
        dry_run: bool = None,
        dst_directory: str = None,
        entry_list: str = None,
        file_system_id: str = None,
        includes: str = None,
        src_task_id: str = None,
        task_action: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.
        # 
        # The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How do I ensure the idempotence?](https://help.aliyun.com/document_detail/25693.html)
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The value of RequestId may be different for each API request.
        self.client_token = client_token
        # The conflict policy for files with the same name. Valid values:
        # 
        # *   SKIP_THE_FILE: skips files with the same name.
        # *   KEEP_LATEST: compares the update time and keeps the latest version.
        # *   OVERWRITE_EXISTING: forcibly overwrites the existing file.
        # 
        # >  This parameter is required for CPFS for LINGJUN file systems.
        self.conflict_policy = conflict_policy
        # Specifies whether to automatically create a directory if no directory exists. Valid values:
        # 
        # *   true: automatically creates a directory.
        # *   false (default): does not automatically create a directory.
        # 
        # > - This parameter is required if the TaskAction parameter is set to Import.
        # > - Only CPFS for LINGJUN V2.6.0 and later support this parameter.
        self.create_dir_if_not_exist = create_dir_if_not_exist
        # The dataflow ID.
        # 
        # This parameter is required.
        self.data_flow_id = data_flow_id
        # The type of data on which operations are performed by the dataflow task.
        # 
        # Valid values:
        # 
        # *   Metadata: the metadata of a file, including the timestamp, ownership, and permission information of the file. If you select Metadata, only the metadata of the file is imported. You can only query the file. When you access the file data, the file is loaded from the source storage as required.
        # *   Data: the data blocks of a file.
        # *   MetaAndData: the metadata and data blocks of the file.
        self.data_type = data_type
        # The source directory of the data.
        # 
        # Limits:
        # 
        # *   The directory must be 1 to 1,023 characters in length.
        # *   The directory must be encoded in UTF-8.
        # *   The directory must start and end with a forward slash (/).
        # *   Only one directory can be listed at a time.
        # *   If the TaskAction parameter is set to Export, the directory must be a relative path within the FileSystemPath.
        # *   If the TaskAction parameter is set to Import, the directory must be a relative path within the SourceStoragePath.
        # *   If the TaskAction parameter is set to StreamExport, the directory must be a relative path within the FileSystemPath.
        # *   If the TaskAction parameter is set to StreamImport, the directory must be a relative path within the SourceStoragePath.
        # 
        # >  Only CPFS for LINGJUN V2.6.0 and later support StreamImport and StreamExport.
        self.directory = directory
        # Specifies whether to perform a dry run.
        # 
        # During the dry run, the system checks whether the request parameters are valid and whether the requested resources are available. During the dry run, no data flow task is created and no fee is incurred.
        # 
        # Valid values:
        # 
        # *   true: performs a dry run. The system checks the required parameters, request syntax, service limits, and available File Storage NAS (NAS) resources. If the request fails the dry run, an error message is returned. If the request passes the dry run, the HTTP status code 200 is returned. No value is returned for the TaskId parameter.
        # *   false (default): performs a dry run and sends the request. If the request passes the dry run, a data flow task is created.
        self.dry_run = dry_run
        # The directory mapped to the data flow task. Limits:
        # 
        # *   The directory must start and end with a forward slash (/). The directory cannot be /../.
        # *   The directory must be 1 to 1,023 characters in length.
        # *   The directory must be encoded in UTF-8.
        # *   Only one directory can be listed at a time.
        # *   If the TaskAction parameter is set to Export, the directory must be a relative path within the SourceStoragePath.
        # *   If the TaskAction parameter is set to Import, the directory must be a relative path within the FileSystemPath.
        # *   If the TaskAction parameter is set to StreamExport, the directory must be a relative path within the SourceStoragePath.
        # *   If the TaskAction parameter is set to StreamImport, the directory must be a relative path within the FileSystemPath.
        # 
        # >  Only CPFS for LINGJUN V2.6.0 and later support StreamImport and StreamExport.
        self.dst_directory = dst_directory
        # The list of files that are executed by the data flow task.
        # 
        # Limits:
        # 
        # *   The list must be encoded in UTF-8.
        # *   The total length of the file list cannot exceed 64 KB.
        # *   The file list is in JSON format.
        # *   The path of a single file must be 1 to 1,023 characters in length and must start with a forward slash (/).
        # *   If the TaskAction parameter is set to Import, each element in the list represents an OSS object name.
        # *   If the TaskAction parameter is set to Export, each element in the list represents a CPFS file path.
        self.entry_list = entry_list
        # The ID of the file system.
        # 
        # *   The IDs of CPFS file systems must start with `cpfs-`. Example: cpfs-125487\\*\\*\\*\\*.
        # *   The IDs of CPFS for LINGJUN file systems must start with `bmcpfs-`. Example: bmcpfs-0015\\*\\*\\*\\*.
        # 
        # >  CPFS is not supported on the international site.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        self.includes = includes
        # If you specify SrcTaskId, the configurations of the TaskAction, DataType, and EntryList parameters are copied from the desired dataflow task. You do not need to specify them.
        self.src_task_id = src_task_id
        # The type of the data flow task.
        # 
        # Valid values:
        # 
        # *   Import: imports data stored in the source storage to a CPFS file system.
        # *   Export: exports specified data from a CPFS file system to the source storage.
        # *   StreamImport: batch imports the specified data from the source storage to a CPFS file system.
        # *   StreamExport: batch exports specified data from a CPFS file system to the source storage.
        # 
        # >  Only CPFS for LINGJUN V2.6.0 and later support StreamImport and StreamExport.
        self.task_action = task_action

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.conflict_policy is not None:
            result['ConflictPolicy'] = self.conflict_policy
        if self.create_dir_if_not_exist is not None:
            result['CreateDirIfNotExist'] = self.create_dir_if_not_exist
        if self.data_flow_id is not None:
            result['DataFlowId'] = self.data_flow_id
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.directory is not None:
            result['Directory'] = self.directory
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.dst_directory is not None:
            result['DstDirectory'] = self.dst_directory
        if self.entry_list is not None:
            result['EntryList'] = self.entry_list
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.includes is not None:
            result['Includes'] = self.includes
        if self.src_task_id is not None:
            result['SrcTaskId'] = self.src_task_id
        if self.task_action is not None:
            result['TaskAction'] = self.task_action
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ConflictPolicy') is not None:
            self.conflict_policy = m.get('ConflictPolicy')
        if m.get('CreateDirIfNotExist') is not None:
            self.create_dir_if_not_exist = m.get('CreateDirIfNotExist')
        if m.get('DataFlowId') is not None:
            self.data_flow_id = m.get('DataFlowId')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('Directory') is not None:
            self.directory = m.get('Directory')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('DstDirectory') is not None:
            self.dst_directory = m.get('DstDirectory')
        if m.get('EntryList') is not None:
            self.entry_list = m.get('EntryList')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('Includes') is not None:
            self.includes = m.get('Includes')
        if m.get('SrcTaskId') is not None:
            self.src_task_id = m.get('SrcTaskId')
        if m.get('TaskAction') is not None:
            self.task_action = m.get('TaskAction')
        return self


class CreateDataFlowTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The ID of the dataflow task.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateDataFlowTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDataFlowTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateDataFlowTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDirRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        owner_group_id: int = None,
        owner_user_id: int = None,
        permission: str = None,
        recursion: bool = None,
        root_directory: str = None,
    ):
        # The ID of the file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The ID of the owner group for the directory. Valid values: 0 to 4294967295.
        # 
        # This parameter is required.
        self.owner_group_id = owner_group_id
        # The owner ID for the directory. Valid values: 0 to 4294967295.
        # 
        # This parameter is required.
        self.owner_user_id = owner_user_id
        # The Portable Operating System Interface (POSIX) permissions applied to the root directory. The value is a valid octal number, such as 0755.
        # 
        # This parameter is required.
        self.permission = permission
        # Specifies whether to create a multi-level directory. Valid values:
        # 
        # *   true (default): If no multi-level directory exists, directories are created level by level.
        # *   false: Only the last level of directory is created. An error message is returned because the parent directory does not exist.
        self.recursion = recursion
        # The directory name.
        # 
        # *   The directory must start with a forward slash (/).
        # *   The directory can contain digits and letters.
        # *   The directory can contain underscores (_), hyphens (-), and periods (.).
        # *   The directory cannot contain symbolic links, such as the current directory (.), the upper-level directory (..), and other symbolic links.
        # 
        # > *   If the root directory does not exist, configure the information for directory creation. The system then automatically creates the specified root directory based on your settings.
        # > *  If the root directory exists, you do not need to configure the information for directory creation. The configurations for directory creation are ignored even if you configure the information.
        # 
        # This parameter is required.
        self.root_directory = root_directory

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.owner_group_id is not None:
            result['OwnerGroupId'] = self.owner_group_id
        if self.owner_user_id is not None:
            result['OwnerUserId'] = self.owner_user_id
        if self.permission is not None:
            result['Permission'] = self.permission
        if self.recursion is not None:
            result['Recursion'] = self.recursion
        if self.root_directory is not None:
            result['RootDirectory'] = self.root_directory
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('OwnerGroupId') is not None:
            self.owner_group_id = m.get('OwnerGroupId')
        if m.get('OwnerUserId') is not None:
            self.owner_user_id = m.get('OwnerUserId')
        if m.get('Permission') is not None:
            self.permission = m.get('Permission')
        if m.get('Recursion') is not None:
            self.recursion = m.get('Recursion')
        if m.get('RootDirectory') is not None:
            self.root_directory = m.get('RootDirectory')
        return self


class CreateDirResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDirResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDirResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateDirResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFileRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        owner: str = None,
        owner_access_inheritable: bool = None,
        path: str = None,
        type: str = None,
    ):
        # The ID of the file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The ID of the portable account. The ID must be a 16-digit string. The string can contain digits and lowercase letters.
        self.owner = owner
        # Specifies whether to share the directory. Valid values:
        # 
        # *   false (default): does not share the directory.
        # *   true: shares the directory.
        # 
        # > *   This parameter takes effect only if the Type parameter is set to Directory and the Owner parameter is not empty.
        # > *   The permissions on a directory can be inherited by the owner. The owner has read and write permissions on the subdirectories and subfiles created in the directory, even if they are created by others.
        self.owner_access_inheritable = owner_access_inheritable
        # The absolute path of the directory or file. The path must start and end with a forward slash (/) and must be 2 to 1024 characters in length.
        # 
        # This parameter is required.
        self.path = path
        # The type of the object. Valid values:
        # 
        # *   File
        # *   Directory
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.owner_access_inheritable is not None:
            result['OwnerAccessInheritable'] = self.owner_access_inheritable
        if self.path is not None:
            result['Path'] = self.path
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('OwnerAccessInheritable') is not None:
            self.owner_access_inheritable = m.get('OwnerAccessInheritable')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateFileResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateFileResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFileSystemRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        # 
        # Limits:
        # 
        # *   The tag key cannot be null or an empty string.
        # *   The tag key can be up to 128 characters in length.
        # *   The tag key cannot start with `aliyun` or `acs:`.
        # *   The tag key cannot contain `http://` or `https://`.
        self.key = key
        # The tag value.
        # 
        # Limits:
        # 
        # *   The tag value cannot be null or an empty string.
        # *   The tag value can be up to 128 characters in length.
        # *   The tag value cannot contain `http://` or `https://`.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateFileSystemRequest(TeaModel):
    def __init__(
        self,
        bandwidth: int = None,
        capacity: int = None,
        charge_type: str = None,
        client_token: str = None,
        description: str = None,
        dry_run: bool = None,
        duration: int = None,
        encrypt_type: int = None,
        file_system_type: str = None,
        kms_key_id: str = None,
        protocol_type: str = None,
        resource_group_id: str = None,
        snapshot_id: str = None,
        storage_type: str = None,
        tag: List[CreateFileSystemRequestTag] = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # The maximum throughput of the file system.
        # 
        # Unit: MB/s.
        # 
        # Specify a value based on the specifications on the buy page.
        self.bandwidth = bandwidth
        # The capacity of the file system. Unit: GiB.
        # 
        # This parameter is valid and required if the FileSystemType parameter is set to extreme.
        # 
        # Specify a value based on the specifications on the following buy page:
        # 
        # [Extreme NAS file system (Pay-as-you-go)](https://common-buy-intl.alibabacloud.com/?commodityCode=nas_extpost_public_intl#/buy)
        self.capacity = capacity
        # The billing method.
        # 
        # Valid values:
        # 
        # *   PayAsYouGo (default): pay-as-you-go
        # *   Subscription: subscription
        self.charge_type = charge_type
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How do I ensure the idempotence?](https://help.aliyun.com/document_detail/25693.html)
        # 
        # > If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token
        # The description of the file system.
        # 
        # Limits:
        # 
        # *   The description must be 2 to 128 characters in length.
        # *   The description must start with a letter and cannot start with `http://` or `https://`.
        # *   The description can contain letters, digits, colons (:), underscores (_), and hyphens (-).
        self.description = description
        # Specifies whether to perform a dry run.
        # 
        # During the dry run, the system checks whether the request parameters are valid and whether the requested resources are available. During the dry run, no file system is created and no fee is incurred.
        # 
        # Valid values:
        # 
        # *   true: performs a dry run. The system checks the required parameters, request syntax, limits, and available NAS resources. If the request fails the dry run, an error message is returned. If the request passes the precheck, the HTTP status code 200 is returned. No value is returned for the FileSystemId parameter.
        # *   false (default): performs a dry run and sends the request. If the request passes the dry run, a file system is created.
        self.dry_run = dry_run
        # The subscription duration.
        # 
        # This parameter is valid and required only if the ChargeType parameter is set to Subscription. Unit: months.
        # 
        # If you do not renew a subscription file system when the file system expires, the file system is automatically released.
        self.duration = duration
        # Specifies whether to encrypt data in the file system.
        # 
        # You can use the keys that are managed by Key Management Service (KMS) to encrypt data in a file system. When you read and write the encrypted data, the data is automatically decrypted.
        # 
        # Valid values:
        # 
        # *   0 (default): The data in the file system is not encrypted.
        # *   1: A NAS-managed key is used to encrypt the data in the file system. This value is valid only if the FileSystemType parameter is set to standard or extreme.
        # *   2: A KMS-managed key is used to encrypt the data in the file system. This value is valid only if the FileSystemType parameter is set to standard or extreme.
        # 
        # >  *   Extreme NAS file systems: All regions except China East 1 Finance support KMS-managed keys.
        # > *   General-purpose NAS file systems: All regions support KMS-managed keys.
        self.encrypt_type = encrypt_type
        # The type of the file system.
        # 
        # Valid values:
        # 
        # *   standard (default): General-purpose NAS file system
        # *   extreme: Extreme NAS file system
        # *   cpfs: Cloud Parallel File Storage (CPFS) file system
        # 
        # > CPFS file systems are available only on the China site (aliyun.com).
        self.file_system_type = file_system_type
        # The ID of the KMS key.
        # 
        # This parameter is required only if the EncryptType parameter is set to 2.
        self.kms_key_id = kms_key_id
        # The protocol type.
        # 
        # *   If the FileSystemType parameter is set to standard, you can set the ProtocolType parameter to NFS or SMB.
        # *   If the FileSystemType parameter is set to extreme, you can set the ProtocolType parameter to NFS.
        # 
        # This parameter is required.
        self.protocol_type = protocol_type
        # The resource group ID.
        # 
        # You can log on to the [Resource Management console](https://resourcemanager.console.aliyun.com/resource-groups?) to view resource group IDs.
        self.resource_group_id = resource_group_id
        # The snapshot ID.
        # 
        # This parameter is available only for advanced Extreme NAS file systems.
        # 
        # >  You can create a file system from a snapshot. In this case, the version of the file system is the same as that of the source file system. For example, the source file system of the snapshot uses version 1. To create a file system of version 2, you can create File System A from the snapshot and create File System B of version 2. You can then copy the data and migrate your business from File System A to File System B.
        self.snapshot_id = snapshot_id
        # The storage class.
        # 
        # *   If the FileSystemType parameter is set to standard, you can set the StorageType parameter to Performance, Capacity, or Premium.
        # *   If the FileSystemType parameter is set to extreme, you can set the StorageType parameter to standard or advance.
        # 
        # This parameter is required.
        self.storage_type = storage_type
        # An array of tags.
        # 
        # You can specify up to 20 tags. If you specify multiple tags, each tag key must be unique.
        self.tag = tag
        # The vSwitch ID.
        # 
        # This parameter is reserved and does not take effect. You do not need to configure this parameter.
        self.v_switch_id = v_switch_id
        # The ID of the virtual private cloud (VPC).
        # 
        # This parameter is reserved and does not take effect. You do not need to configure this parameter.
        self.vpc_id = vpc_id
        # The zone ID.
        # 
        # Each region has multiple isolated locations known as zones. Each zone has its own independent power supply and networks.
        # 
        # This parameter is not required if the FileSystemType parameter is set to standard. By default, a random zone is selected based on the protocol type and storage type.
        # 
        # This parameter is required if the FileSystemType parameter is set to extreme.
        # 
        # > *   An Elastic Compute Service (ECS) instance and a NAS file system that reside in different zones of the same region can access each other.
        # >*   We recommend that you select the zone where the ECS instance resides. This prevents cross-zone latency between the file system and the ECS instance.
        self.zone_id = zone_id

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.encrypt_type is not None:
            result['EncryptType'] = self.encrypt_type
        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type
        if self.kms_key_id is not None:
            result['KmsKeyId'] = self.kms_key_id
        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('EncryptType') is not None:
            self.encrypt_type = m.get('EncryptType')
        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')
        if m.get('KmsKeyId') is not None:
            self.kms_key_id = m.get('KmsKeyId')
        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateFileSystemRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateFileSystemResponseBody(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        request_id: str = None,
    ):
        # The ID of the file system that is created.
        self.file_system_id = file_system_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateFileSystemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateFileSystemResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateFileSystemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFilesetRequestQuota(TeaModel):
    def __init__(
        self,
        file_count_limit: int = None,
        size_limit: int = None,
    ):
        # The number of files of the quota. Valid values:
        # 
        # *   Minimum value: 100000.
        # *   Maximum value: 10000000000.
        self.file_count_limit = file_count_limit
        # The total capacity of the quota. Unit: bytes.
        # 
        # Valid values:
        # 
        # *   Minimum value: 10737418240 (10 GiB).
        # *   Maximum value: 1073741824000 (1024000 GiB).
        # *   Step size: 1073741824 (1 GiB).
        self.size_limit = size_limit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_count_limit is not None:
            result['FileCountLimit'] = self.file_count_limit
        if self.size_limit is not None:
            result['SizeLimit'] = self.size_limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileCountLimit') is not None:
            self.file_count_limit = m.get('FileCountLimit')
        if m.get('SizeLimit') is not None:
            self.size_limit = m.get('SizeLimit')
        return self


class CreateFilesetRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        deletion_protection: bool = None,
        description: str = None,
        dry_run: bool = None,
        file_system_id: str = None,
        file_system_path: str = None,
        quota: CreateFilesetRequestQuota = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.
        # 
        # The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How do I ensure the idempotence?](https://help.aliyun.com/document_detail/25693.html)
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token
        # Specifies whether to enable deletion protection to allow you to release the fileset by using the console or by calling the [DeleteFileset](https://help.aliyun.com/document_detail/2838077.html) operation.
        # 
        # *   true: enables release protection.
        # *   false (default): disables release protection.
        # 
        # >  This parameter can protect filesets only against manual releases, but not against automatic releases.
        self.deletion_protection = deletion_protection
        # The description of the fileset.
        # 
        # *   The description must be 2 to 128 characters in length.
        # *   The description must start with a letter but cannot start with http:// or https://.
        # *   The description can contain letters, digits, colons (:), underscores (_), and hyphens (-).
        self.description = description
        # Specifies whether to perform a dry run.
        # 
        # During the dry run, the system checks whether the request parameters are valid and whether the requested resources are available. During the dry run, no fileset is created and no fee is incurred.
        # 
        # Valid values:
        # 
        # *   true: performs a dry run. The system checks the required parameters, request syntax, service limits, and available Apsara File Storage NAS (NAS) resources. If the request fails the dry run, an error message is returned. If the request passes the dry run, the HTTP status code 200 is returned. No value is returned for the FsetId parameter.
        # *   false (default): performs a dry run and sends the request. If the request passes the dry run, a fileset is created.
        self.dry_run = dry_run
        # The ID of the file system.
        # 
        # *   The IDs of CPFS file systems must start with `cpfs-`. Example: cpfs-099394bd928c\\*\\*\\*\\*.
        # *   The IDs of CPFS for LINGJUN file systems must start with `bmcpfs-`. Example: bmcpfs-290w65p03ok64ya\\*\\*\\*\\*.
        # 
        # >  CPFS is not supported on the international site.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The absolute path of the fileset.
        # 
        # *   The path must be 2 to 1024 characters in length.
        # *   The path must start and end with a forward slash (/).
        # *   The fileset path must be a new path and cannot be an existing path. Fileset paths cannot be renamed and cannot be symbolic links.
        # *   The maximum depth supported by a fileset path is eight levels. The depth of the root directory / is 0 levels. For example, the fileset path /test/aaa/ccc/ has three levels.
        # *   If the fileset path is a multi-level path, the parent directory must be an existing directory.
        # *   Nested filesets are not supported. If a fileset is specified as a parent directory, its subdirectory cannot be a fileset. A fileset path supports only one quota.
        # 
        # This parameter is required.
        self.file_system_path = file_system_path
        # The quota information.
        # 
        # >  Only CPFS for LINGJUN V2.7.0 and later support this parameter.
        self.quota = quota

    def validate(self):
        if self.quota:
            self.quota.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.deletion_protection is not None:
            result['DeletionProtection'] = self.deletion_protection
        if self.description is not None:
            result['Description'] = self.description
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.file_system_path is not None:
            result['FileSystemPath'] = self.file_system_path
        if self.quota is not None:
            result['Quota'] = self.quota.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DeletionProtection') is not None:
            self.deletion_protection = m.get('DeletionProtection')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('FileSystemPath') is not None:
            self.file_system_path = m.get('FileSystemPath')
        if m.get('Quota') is not None:
            temp_model = CreateFilesetRequestQuota()
            self.quota = temp_model.from_map(m['Quota'])
        return self


class CreateFilesetResponseBody(TeaModel):
    def __init__(
        self,
        fset_id: str = None,
        request_id: str = None,
    ):
        # The fileset ID.
        self.fset_id = fset_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fset_id is not None:
            result['FsetId'] = self.fset_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FsetId') is not None:
            self.fset_id = m.get('FsetId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateFilesetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateFilesetResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateFilesetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLDAPConfigRequest(TeaModel):
    def __init__(
        self,
        bind_dn: str = None,
        file_system_id: str = None,
        search_base: str = None,
        uri: str = None,
    ):
        # An LDAP entry.
        self.bind_dn = bind_dn
        # The ID of the file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # An LDAP search base.
        # 
        # This parameter is required.
        self.search_base = search_base
        # An LDAP URI.
        # 
        # This parameter is required.
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bind_dn is not None:
            result['BindDN'] = self.bind_dn
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.search_base is not None:
            result['SearchBase'] = self.search_base
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindDN') is not None:
            self.bind_dn = m.get('BindDN')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('SearchBase') is not None:
            self.search_base = m.get('SearchBase')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class CreateLDAPConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateLDAPConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateLDAPConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateLDAPConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLifecyclePolicyRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        lifecycle_policy_name: str = None,
        lifecycle_rule_name: str = None,
        path: str = None,
        paths: List[str] = None,
        storage_type: str = None,
    ):
        # The ID of the file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The name of the lifecycle policy. The name must be 3 to 64 characters in length and can contain letters, digits, underscores (_), and hyphens (-). The name must start with a letter.
        # 
        # This parameter is required.
        self.lifecycle_policy_name = lifecycle_policy_name
        # The management rule that is associated with the lifecycle policy.
        # 
        # Valid values:
        # 
        # *   DEFAULT_ATIME_14: Files that are not accessed in the last 14 days are dumped to the IA storage medium.
        # *   DEFAULT_ATIME_30: Files that are not accessed in the last 30 days are dumped to the IA storage medium.
        # *   DEFAULT_ATIME_60: Files that are not accessed in the last 60 days are dumped to the IA storage medium.
        # *   DEFAULT_ATIME_90: Files that are not accessed in the last 90 days are dumped to the IA storage medium.
        self.lifecycle_rule_name = lifecycle_rule_name
        # The absolute path of the directory that is associated with the lifecycle policy.
        # 
        # If you specify this parameter, you can associate the lifecycle policy with only one directory. The path must start with a forward slash (/) and must be a path that exists in the mount target.
        # 
        # > We recommend that you specify the Paths.N parameter so that you can associate the lifecycle policy with multiple directories.
        self.path = path
        # The absolute paths of the directories that are associated with the lifecycle policy.
        # 
        # If you specify this parameter, you can associate the lifecycle policy with multiple directories. Each path must start with a forward slash (/) and must be a path that exists in the mount target. Valid values of N: 1 to 10.
        self.paths = paths
        # The storage type of the data that is dumped to the IA storage medium.
        # 
        # Default value: InfrequentAccess (IA).
        # 
        # This parameter is required.
        self.storage_type = storage_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.lifecycle_policy_name is not None:
            result['LifecyclePolicyName'] = self.lifecycle_policy_name
        if self.lifecycle_rule_name is not None:
            result['LifecycleRuleName'] = self.lifecycle_rule_name
        if self.path is not None:
            result['Path'] = self.path
        if self.paths is not None:
            result['Paths'] = self.paths
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('LifecyclePolicyName') is not None:
            self.lifecycle_policy_name = m.get('LifecyclePolicyName')
        if m.get('LifecycleRuleName') is not None:
            self.lifecycle_rule_name = m.get('LifecycleRuleName')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Paths') is not None:
            self.paths = m.get('Paths')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        return self


class CreateLifecyclePolicyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateLifecyclePolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateLifecyclePolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateLifecyclePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLifecycleRetrieveJobRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        paths: List[str] = None,
        storage_type: str = None,
    ):
        # The ID of the file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The directories or files that you want to retrieve. You can specify a maximum of 10 paths.
        # 
        # This parameter is required.
        self.paths = paths
        # The storage class.
        # 
        # *   InfrequentAccess (default): the Infrequent Access (IA) storage class.
        # *   Archive: the Archive storage class.
        self.storage_type = storage_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.paths is not None:
            result['Paths'] = self.paths
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('Paths') is not None:
            self.paths = m.get('Paths')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        return self


class CreateLifecycleRetrieveJobResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
    ):
        # The ID of the data retrieval task.
        self.job_id = job_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateLifecycleRetrieveJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateLifecycleRetrieveJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateLifecycleRetrieveJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLogAnalysisRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        region_id: str = None,
    ):
        # The ID of the file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateLogAnalysisResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateLogAnalysisResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateLogAnalysisResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateLogAnalysisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMountTargetRequest(TeaModel):
    def __init__(
        self,
        access_group_name: str = None,
        dry_run: bool = None,
        enable_ipv_6: bool = None,
        file_system_id: str = None,
        network_type: str = None,
        security_group_id: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # The name of the permission group.
        # 
        # This parameter is required if you create a mount target for a General-purpose NAS file system or an Extreme NAS file system.
        # 
        # The default permission group for virtual private clouds (VPCs) is named DEFAULT_VPC_GROUP_NAME.
        self.access_group_name = access_group_name
        # Specifies whether to perform a dry run to check for existing mount targets. This parameter is valid only for CPFS file systems.
        # 
        # If you set this parameter to true, the system checks whether the request parameters are valid and whether the requested resources are available. In this case, no mount target is created and no fee is incurred.
        # 
        # *   true: performs a dry run but does not create a mount target. In the dry run, the system checks the request format, service limits, available CPFS resources, and whether the required parameters are specified. If the request fails the dry run, an error message is returned. If the request passes the dry run, the HTTP status code `200` is returned. No value is returned for the `MountTargetDomain` parameter.
        # *   false (default): sends the request. If the request passes the dry run, a mount target is created.
        self.dry_run = dry_run
        # Specifies whether to create an IPv6 domain name for the mount target.
        # 
        # Valid values:
        # 
        # *   true: An IPv6 domain name is created for the mount target.
        # *   false (default): No IPv6 domain name is created for the mount target.
        # 
        # > Only Extreme NAS file systems that reside in the Chinese mainland support IPv6. If you want to create an IPv6 domain name for the mount target, you must enable IPv6 for the file system.
        self.enable_ipv_6 = enable_ipv_6
        # The ID of the file system.
        # 
        # *   Sample ID of a General-purpose NAS file system: 31a8e4\\*\\*\\*\\*.
        # *   The IDs of Extreme NAS file systems must start with `extreme-`, for example, extreme-0015\\*\\*\\*\\*.
        # *   The IDs of Cloud Parallel File Storage (CPFS) file systems must start with `cpfs-`, for example, cpfs-125487\\*\\*\\*\\*.
        # 
        # > CPFS file systems are available only on the China site (aliyun.com).
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The network type of the mount target. Valid value: **Vpc**.
        # 
        # This parameter is required.
        self.network_type = network_type
        # The ID of the security group.
        self.security_group_id = security_group_id
        # The ID of the vSwitch.
        # 
        # This parameter is valid and required if the mount target resides in a VPC. Example: If you set the NetworkType parameter to VPC, you must specify the VSwitchId parameter.
        self.v_switch_id = v_switch_id
        # The ID of the VPC.
        # 
        # This parameter is valid and required if the mount target resides in a VPC. Example: If you set the NetworkType parameter to VPC, you must specify the VpcId parameter.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group_name is not None:
            result['AccessGroupName'] = self.access_group_name
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.enable_ipv_6 is not None:
            result['EnableIpv6'] = self.enable_ipv_6
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessGroupName') is not None:
            self.access_group_name = m.get('AccessGroupName')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EnableIpv6') is not None:
            self.enable_ipv_6 = m.get('EnableIpv6')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class CreateMountTargetResponseBodyMountTargetExtra(TeaModel):
    def __init__(
        self,
        dual_stack_mount_target_domain: str = None,
    ):
        # The dual-stack (IPv4 and IPv6) domain name of the mount target.
        self.dual_stack_mount_target_domain = dual_stack_mount_target_domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dual_stack_mount_target_domain is not None:
            result['DualStackMountTargetDomain'] = self.dual_stack_mount_target_domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DualStackMountTargetDomain') is not None:
            self.dual_stack_mount_target_domain = m.get('DualStackMountTargetDomain')
        return self


class CreateMountTargetResponseBody(TeaModel):
    def __init__(
        self,
        mount_target_domain: str = None,
        mount_target_extra: CreateMountTargetResponseBodyMountTargetExtra = None,
        request_id: str = None,
    ):
        # The IPv4 domain name of the mount target.
        self.mount_target_domain = mount_target_domain
        # The information about the mount target.
        self.mount_target_extra = mount_target_extra
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.mount_target_extra:
            self.mount_target_extra.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mount_target_domain is not None:
            result['MountTargetDomain'] = self.mount_target_domain
        if self.mount_target_extra is not None:
            result['MountTargetExtra'] = self.mount_target_extra.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MountTargetDomain') is not None:
            self.mount_target_domain = m.get('MountTargetDomain')
        if m.get('MountTargetExtra') is not None:
            temp_model = CreateMountTargetResponseBodyMountTargetExtra()
            self.mount_target_extra = temp_model.from_map(m['MountTargetExtra'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateMountTargetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateMountTargetResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateMountTargetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProtocolMountTargetRequest(TeaModel):
    def __init__(
        self,
        access_group_name: str = None,
        client_token: str = None,
        description: str = None,
        dry_run: bool = None,
        file_system_id: str = None,
        fset_id: str = None,
        path: str = None,
        protocol_service_id: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # The name of the permission group.
        # 
        # Default value: DEFAULT_VPC_GROUP_NAME.
        self.access_group_name = access_group_name
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.
        # 
        # The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How do I ensure the idempotence?](https://help.aliyun.com/document_detail/25693.html)
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token
        # The description of the export directory for the protocol service. The **name of the export directory** appears in the console.
        # 
        # Limits:
        # 
        # *   The description must be 2 to 128 characters in length.
        # *   The description must start with a letter but cannot start with `http://` or `https://`.
        # *   The description can contain letters, digits, colons (:), underscores (_), and hyphens (-).
        self.description = description
        # Specifies whether to perform a dry run. The dry run checks parameter validity and prerequisites. The dry run does not create an export directory or incur fees.
        # 
        # Valid values:
        # 
        # *   true: performs a dry run. The system checks the request format, service limits, prerequisites, and whether the required parameters are specified. If the request fails the dry run, an error message is returned. If the request passes the dry run, the HTTP status code 200 is returned. No value is returned for the ExportId parameter.
        # *   false (default): performs a dry run and sends the request. If the request passes the dry run, an export directory is created.
        self.dry_run = dry_run
        # The ID of the file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The ID of the fileset that you want to export.
        # 
        # Limits:
        # 
        # *   The fileset already exists.
        # *   You can create only one export directory for a fileset.
        # *   You can specify either a fileset or a path.
        self.fset_id = fset_id
        # The path of the CPFS directory that you want to export.
        # 
        # Limits:
        # 
        # *   The directory already exists in the CPFS file system.
        # *   You can create only one export directory for a directory.
        # *   You can specify either a fileset or a path.
        # 
        # Format:
        # 
        # *   The path must be 1 to 1,024 characters in length.
        # *   The path must be encoded in UTF-8.
        # *   The path must start and end with a forward slash (/). The root directory is `/`.
        self.path = path
        # The ID of the protocol service.
        # 
        # This parameter is required.
        self.protocol_service_id = protocol_service_id
        # The vSwitch ID of the export directory for the protocol service.
        # 
        # This parameter is required.
        self.v_switch_id = v_switch_id
        # The VPC ID of the export directory for the protocol service.
        # 
        # This parameter is required.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group_name is not None:
            result['AccessGroupName'] = self.access_group_name
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.fset_id is not None:
            result['FsetId'] = self.fset_id
        if self.path is not None:
            result['Path'] = self.path
        if self.protocol_service_id is not None:
            result['ProtocolServiceId'] = self.protocol_service_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessGroupName') is not None:
            self.access_group_name = m.get('AccessGroupName')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('FsetId') is not None:
            self.fset_id = m.get('FsetId')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('ProtocolServiceId') is not None:
            self.protocol_service_id = m.get('ProtocolServiceId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class CreateProtocolMountTargetResponseBody(TeaModel):
    def __init__(
        self,
        export_id: str = None,
        request_id: str = None,
    ):
        # The ID of the export directory for the protocol service.
        self.export_id = export_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.export_id is not None:
            result['ExportId'] = self.export_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExportId') is not None:
            self.export_id = m.get('ExportId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateProtocolMountTargetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateProtocolMountTargetResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateProtocolMountTargetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProtocolServiceRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        dry_run: bool = None,
        file_system_id: str = None,
        protocol_spec: str = None,
        protocol_type: str = None,
        throughput: int = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.
        # 
        # The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How do I ensure the idempotence?](https://help.aliyun.com/document_detail/25693.html)
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token
        # The description of the protocol service. The name of the protocol service appears in the console.
        # 
        # Limits:
        # 
        # *   The description must be 2 to 128 characters in length.
        # *   The description must start with a letter and cannot start with `http://` or `https://`.
        # *   The description can contain letters, digits, colons (:), underscores (_), and hyphens (-).
        self.description = description
        # Specifies whether to perform a dry run.
        # 
        # The dry run checks parameter validity and prerequisites. The dry run does not create a protocol service or incur fees.
        # 
        # Valid values:
        # 
        # *   true: performs only a dry run and does not create the protocol service. The system checks the request format, service limits, prerequisites, and whether the required parameters are specified. If the request fails the dry run, an error message is returned. If the request passes the dry run, the HTTP status code 200 is returned. No value is returned for the ProtocolServiceId parameter.
        # *   false (default): performs a dry run and sends the request. If the request passes the dry run, a protocol service is created.
        self.dry_run = dry_run
        # The ID of the file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The specification of the protocol service.
        # 
        # Set the value to General (default).
        # 
        # Valid values:
        # 
        # *   CL2
        # *   General
        # *   CL1
        # 
        # This parameter is required.
        self.protocol_spec = protocol_spec
        # The protocol type of the protocol service.
        # 
        # Valid value: NFS (default). Only NFSv3 is supported.
        # 
        # This parameter is required.
        self.protocol_type = protocol_type
        # The throughput of the protocol service.
        # 
        # Unit: MB/s.
        self.throughput = throughput
        # The vSwitch ID of the protocol service.
        # 
        # This parameter is required.
        self.v_switch_id = v_switch_id
        # The virtual private cloud (VPC) ID of the protocol service. The VPC ID of the protocol service must be the same as the VPC ID of the file system.
        # 
        # This parameter is required.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.protocol_spec is not None:
            result['ProtocolSpec'] = self.protocol_spec
        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type
        if self.throughput is not None:
            result['Throughput'] = self.throughput
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('ProtocolSpec') is not None:
            self.protocol_spec = m.get('ProtocolSpec')
        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')
        if m.get('Throughput') is not None:
            self.throughput = m.get('Throughput')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class CreateProtocolServiceResponseBody(TeaModel):
    def __init__(
        self,
        protocol_service_id: str = None,
        request_id: str = None,
    ):
        # The ID of the protocol service.
        self.protocol_service_id = protocol_service_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.protocol_service_id is not None:
            result['ProtocolServiceId'] = self.protocol_service_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProtocolServiceId') is not None:
            self.protocol_service_id = m.get('ProtocolServiceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateProtocolServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateProtocolServiceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateProtocolServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRecycleBinDeleteJobRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        file_id: str = None,
        file_system_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How do I ensure the idempotence?](https://help.aliyun.com/document_detail/25693.html)
        # 
        # > If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token
        # The ID of the file or directory that you want to permanently delete.
        # 
        # You can call the [ListRecycledDirectoriesAndFiles](https://help.aliyun.com/document_detail/264193.html) operation to query the value of the FileId parameter.
        # 
        # This parameter is required.
        self.file_id = file_id
        # The ID of the file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        return self


class CreateRecycleBinDeleteJobResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
    ):
        # The job ID.
        self.job_id = job_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateRecycleBinDeleteJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateRecycleBinDeleteJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateRecycleBinDeleteJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRecycleBinRestoreJobRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        file_id: str = None,
        file_system_id: str = None,
        target_file_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        # 
        # > If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token
        # The ID of the file or directory that you want to restore.
        # 
        # You can call the [ListRecycleBinJobs](https://help.aliyun.com/document_detail/264192.html) operation to query the value of the FileId parameter.
        # 
        # This parameter is required.
        self.file_id = file_id
        # The ID of the file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The ID of the directory to which the file is restored.
        # 
        # This parameter is required.
        self.target_file_id = target_file_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.target_file_id is not None:
            result['TargetFileId'] = self.target_file_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('TargetFileId') is not None:
            self.target_file_id = m.get('TargetFileId')
        return self


class CreateRecycleBinRestoreJobResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
    ):
        # The job ID.
        self.job_id = job_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateRecycleBinRestoreJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateRecycleBinRestoreJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateRecycleBinRestoreJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSnapshotRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        file_system_id: str = None,
        retention_days: int = None,
        snapshot_name: str = None,
    ):
        # The description of the snapshot.
        # 
        # Limits:
        # 
        # *   The description must be 2 to 256 characters in length.
        # *   The description cannot start with `http://` or `https://`.
        # *   This parameter is empty by default.
        self.description = description
        # The ID of the advanced Extreme NAS file system. The value must start with `extreme-`, for example, `extreme-01dd****`.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The retention period of the snapshot.
        # 
        # Unit: days.
        # 
        # Valid values:
        # 
        # *   \\-1 (default). Auto snapshots are permanently retained. After the number of auto snapshots exceeds the upper limit, the earliest auto snapshot is automatically deleted.
        # *   1 to 65536: Auto snapshots are retained for the specified days. After the retention period of auto snapshots expires, the auto snapshots are automatically deleted.
        self.retention_days = retention_days
        # The snapshot name.
        # 
        # Limits:
        # 
        # *   The name must be 2 to 128 characters in length. The name must start with a letter and cannot start with `http://` or `https://`.
        # *   The name can contain letters, digits, colons (:), underscores (_), and hyphens (-).
        # *   The name cannot start with auto because snapshots whose names start with auto are recognized as auto snapshots.
        self.snapshot_name = snapshot_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.retention_days is not None:
            result['RetentionDays'] = self.retention_days
        if self.snapshot_name is not None:
            result['SnapshotName'] = self.snapshot_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('RetentionDays') is not None:
            self.retention_days = m.get('RetentionDays')
        if m.get('SnapshotName') is not None:
            self.snapshot_name = m.get('SnapshotName')
        return self


class CreateSnapshotResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        snapshot_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The snapshot ID.
        self.snapshot_id = snapshot_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        return self


class CreateSnapshotResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateSnapshotResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateSnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAccessGroupRequest(TeaModel):
    def __init__(
        self,
        access_group_name: str = None,
        file_system_type: str = None,
    ):
        # The name of the permission group to be deleted.
        # 
        # This parameter is required.
        self.access_group_name = access_group_name
        # The type of the file system.
        # 
        # Valid values:
        # 
        # *   standard (default): General-purpose NAS file system
        # *   extreme: Extreme NAS file system
        self.file_system_type = file_system_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group_name is not None:
            result['AccessGroupName'] = self.access_group_name
        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessGroupName') is not None:
            self.access_group_name = m.get('AccessGroupName')
        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')
        return self


class DeleteAccessGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAccessGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAccessGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteAccessGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAccessPointRequest(TeaModel):
    def __init__(
        self,
        access_point_id: str = None,
        file_system_id: str = None,
    ):
        # The ID of the access point.
        # 
        # This parameter is required.
        self.access_point_id = access_point_id
        # The ID of the file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_point_id is not None:
            result['AccessPointId'] = self.access_point_id
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessPointId') is not None:
            self.access_point_id = m.get('AccessPointId')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        return self


class DeleteAccessPointResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAccessPointResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAccessPointResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteAccessPointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAccessRuleRequest(TeaModel):
    def __init__(
        self,
        access_group_name: str = None,
        access_rule_id: str = None,
        file_system_type: str = None,
    ):
        # The name of the permission group.
        # 
        # This parameter is required.
        self.access_group_name = access_group_name
        # The rule ID.
        # 
        # This parameter is required.
        self.access_rule_id = access_rule_id
        # The type of the file system.
        # 
        # Valid values:
        # 
        # *   standard (default): General-purpose NAS file system
        # *   extreme: Extreme NAS file system
        self.file_system_type = file_system_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group_name is not None:
            result['AccessGroupName'] = self.access_group_name
        if self.access_rule_id is not None:
            result['AccessRuleId'] = self.access_rule_id
        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessGroupName') is not None:
            self.access_group_name = m.get('AccessGroupName')
        if m.get('AccessRuleId') is not None:
            self.access_rule_id = m.get('AccessRuleId')
        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')
        return self


class DeleteAccessRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAccessRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAccessRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteAccessRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAutoSnapshotPolicyRequest(TeaModel):
    def __init__(
        self,
        auto_snapshot_policy_id: str = None,
    ):
        # The ID of the automatic snapshot policy.
        # 
        # You can call the [DescribeAutoSnapshotPolicies](https://help.aliyun.com/document_detail/126583.html) operation to view available automatic snapshot policies.
        # 
        # This parameter is required.
        self.auto_snapshot_policy_id = auto_snapshot_policy_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_snapshot_policy_id is not None:
            result['AutoSnapshotPolicyId'] = self.auto_snapshot_policy_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoSnapshotPolicyId') is not None:
            self.auto_snapshot_policy_id = m.get('AutoSnapshotPolicyId')
        return self


class DeleteAutoSnapshotPolicyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        # 
        # Every response returns a unique request ID regardless of whether the request is successful.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAutoSnapshotPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAutoSnapshotPolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteAutoSnapshotPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDataFlowRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        data_flow_id: str = None,
        dry_run: bool = None,
        file_system_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.
        # 
        # The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How do I ensure the idempotence?](https://help.aliyun.com/document_detail/25693.html)
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The value of RequestId may be different for each API request.
        self.client_token = client_token
        # The dataflow ID.
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
        # *   The IDs of CPFS file systems must start with `cpfs-`. Example: cpfs-125487\\*\\*\\*\\*.
        # *   The IDs of CPFS for LINGJUN file systems must start with `bmcpfs-`. Example: bmcpfs-0015\\*\\*\\*\\*.
        # 
        # >  CPFS is not supported on the international site.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DataFlowId') is not None:
            self.data_flow_id = m.get('DataFlowId')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        return self


class DeleteDataFlowResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteDataFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDataFlowResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteDataFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFileSystemRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
    ):
        # The ID of the file system that you want to delete.
        # 
        # *   Sample ID of a General-purpose NAS file system: 31a8e4\\*\\*\\*\\*.
        # *   The IDs of Extreme NAS file systems must start with `extreme-`, for example, extreme-0015\\*\\*\\*\\*.
        # *   The IDs of Cloud Parallel File Storage (CPFS) file systems must start with `cpfs-`, for example, cpfs-00cb6fa094ca\\*\\*\\*\\*.
        # 
        # > CPFS file systems are available only on the China site (aliyun.com).
        # 
        # This parameter is required.
        self.file_system_id = file_system_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        return self


class DeleteFileSystemResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteFileSystemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteFileSystemResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteFileSystemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFilesetRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        file_system_id: str = None,
        fset_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.
        # 
        # The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How do I ensure the idempotence?](https://help.aliyun.com/document_detail/25693.html)
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform a dry run.
        # 
        # During the dry run, the system checks whether the request parameters are valid and whether the requested resources are available. During the dry run, no fileset is deleted.
        # 
        # Valid values:
        # 
        # *   true: performs only a dry run. The system checks the required parameters, request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the HTTP status code 200 is returned.
        # *   false (default): performs a dry run and sends the request. If the request passes the dry run, the fileset is deleted.
        self.dry_run = dry_run
        # The ID of the file system.
        # 
        # *   The IDs of CPFS file systems must start with `cpfs-`. Example: cpfs-099394bd928c\\*\\*\\*\\*.
        # *   The IDs of CPFS for LINGJUN file systems must start with `bmcpfs-`. Example: bmcpfs-290w65p03ok64ya\\*\\*\\*\\*.
        # 
        # >  CPFS is not supported on the international site.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The fileset ID.
        # 
        # This parameter is required.
        self.fset_id = fset_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.fset_id is not None:
            result['FsetId'] = self.fset_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('FsetId') is not None:
            self.fset_id = m.get('FsetId')
        return self


class DeleteFilesetResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteFilesetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteFilesetResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteFilesetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteLDAPConfigRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
    ):
        # The ID of the file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        return self


class DeleteLDAPConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteLDAPConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteLDAPConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteLDAPConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteLifecyclePolicyRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        lifecycle_policy_name: str = None,
    ):
        # The ID of the file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The name of the lifecycle policy.
        # 
        # This parameter is required.
        self.lifecycle_policy_name = lifecycle_policy_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.lifecycle_policy_name is not None:
            result['LifecyclePolicyName'] = self.lifecycle_policy_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('LifecyclePolicyName') is not None:
            self.lifecycle_policy_name = m.get('LifecyclePolicyName')
        return self


class DeleteLifecyclePolicyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteLifecyclePolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteLifecyclePolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteLifecyclePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteLogAnalysisRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        region_id: str = None,
    ):
        # The ID of the file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteLogAnalysisResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteLogAnalysisResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteLogAnalysisResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteLogAnalysisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteMountTargetRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        mount_target_domain: str = None,
    ):
        # The ID of the file system.
        # 
        # *   Sample ID of a General-purpose NAS file system: 31a8e4\\*\\*\\*\\*.
        # *   The IDs of Extreme NAS file systems must start with `extreme-`, for example, extreme-0015\\*\\*\\*\\*.
        # *   The IDs of Cloud Parallel File Storage (CPFS) file systems must start with `cpfs-`, for example, cpfs-125487\\*\\*\\*\\*.
        # 
        # > CPFS file systems are available only on the China site (aliyun.com).
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The domain name of the mount target.
        # 
        # This parameter is required.
        self.mount_target_domain = mount_target_domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.mount_target_domain is not None:
            result['MountTargetDomain'] = self.mount_target_domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('MountTargetDomain') is not None:
            self.mount_target_domain = m.get('MountTargetDomain')
        return self


class DeleteMountTargetResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteMountTargetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteMountTargetResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteMountTargetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteProtocolMountTargetRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        export_id: str = None,
        file_system_id: str = None,
        protocol_service_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.
        # 
        # The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How do I ensure the idempotence?](https://help.aliyun.com/document_detail/25693.html)
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform only a dry run, without performing the actual request. The dry run checks parameter validity and prerequisites. The dry run does not delete the specified export directory or incur fees.
        # 
        # Valid values:
        # 
        # *   true: performs only a dry run. The system checks the required parameters, request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the HTTP status code 200 is returned.
        # *   false (default): performs a dry run and sends the request. If the request passes the dry run, the specified export directory is deleted.
        self.dry_run = dry_run
        # The ID of the export directory.
        # 
        # This parameter is required.
        self.export_id = export_id
        # The ID of the file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The ID of the protocol service.
        # 
        # This parameter is required.
        self.protocol_service_id = protocol_service_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.export_id is not None:
            result['ExportId'] = self.export_id
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.protocol_service_id is not None:
            result['ProtocolServiceId'] = self.protocol_service_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('ExportId') is not None:
            self.export_id = m.get('ExportId')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('ProtocolServiceId') is not None:
            self.protocol_service_id = m.get('ProtocolServiceId')
        return self


class DeleteProtocolMountTargetResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteProtocolMountTargetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteProtocolMountTargetResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteProtocolMountTargetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteProtocolServiceRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        file_system_id: str = None,
        protocol_service_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.
        # 
        # The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How do I ensure the idempotence?](https://help.aliyun.com/document_detail/25693.html)
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform only a dry run, without performing the actual request. The dry run checks parameter validity and prerequisites. The dry run does not delete the specified protocol service.
        # 
        # Valid values:
        # 
        # *   true: performs only a dry run. The system checks the required parameters, request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the HTTP status code 200 is returned.
        # *   false (default): performs a dry run and sends the request. If the request passes the dry run, the specified protocol service is deleted.
        self.dry_run = dry_run
        # The ID of the file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The ID of the protocol service.
        # 
        # This parameter is required.
        self.protocol_service_id = protocol_service_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.protocol_service_id is not None:
            result['ProtocolServiceId'] = self.protocol_service_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('ProtocolServiceId') is not None:
            self.protocol_service_id = m.get('ProtocolServiceId')
        return self


class DeleteProtocolServiceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteProtocolServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteProtocolServiceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteProtocolServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSnapshotRequest(TeaModel):
    def __init__(
        self,
        snapshot_id: str = None,
    ):
        # The snapshot ID.
        # 
        # This parameter is required.
        self.snapshot_id = snapshot_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        return self


class DeleteSnapshotResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        # 
        # Every response returns a unique request ID regardless of whether the request is successful.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteSnapshotResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteSnapshotResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteSnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAccessGroupsRequest(TeaModel):
    def __init__(
        self,
        access_group_name: str = None,
        file_system_type: str = None,
        page_number: int = None,
        page_size: int = None,
        use_utcdate_time: bool = None,
    ):
        # The name of the permission group.
        # 
        # Limits:
        # 
        # *   The name must be 3 to 64 characters in length.
        # *   The name must start with a letter and can contain letters, digits, underscores (_), and hyphens (-).
        self.access_group_name = access_group_name
        # The type of the file system.
        # 
        # Valid values:
        # 
        # *   standard (default): General-purpose NAS file system
        # *   extreme: Extreme NAS file system
        # *   cpfs: Cloud Parallel File Storage (CPFS) file system
        # 
        # > CPFS file systems are available only on the China site (aliyun.com).
        self.file_system_type = file_system_type
        # The page number.
        # 
        # Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 10.
        self.page_size = page_size
        # Specifies whether to display the creation time of the permission group in UTC.
        # 
        # Valid values:
        # 
        # *   true (default): The time is displayed in UTC.
        # *   false: The time is not displayed in UTC.
        self.use_utcdate_time = use_utcdate_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group_name is not None:
            result['AccessGroupName'] = self.access_group_name
        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.use_utcdate_time is not None:
            result['UseUTCDateTime'] = self.use_utcdate_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessGroupName') is not None:
            self.access_group_name = m.get('AccessGroupName')
        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('UseUTCDateTime') is not None:
            self.use_utcdate_time = m.get('UseUTCDateTime')
        return self


class DescribeAccessGroupsResponseBodyAccessGroupsAccessGroup(TeaModel):
    def __init__(
        self,
        access_group_name: str = None,
        access_group_type: str = None,
        create_time: str = None,
        description: str = None,
        file_system_type: str = None,
        mount_target_count: int = None,
        region_id: str = None,
        rule_count: int = None,
    ):
        # The name of the permission group.
        self.access_group_name = access_group_name
        # The network type of the permission group. Valid value: **Vpc**.
        self.access_group_type = access_group_type
        # The time when the permission group was created.
        self.create_time = create_time
        # The description of the permission group.
        self.description = description
        # The type of the file system.
        # 
        # Valid values:
        # 
        # *   standard: General-purpose File Storage NAS (NAS) file system
        # *   extreme: Extreme NAS file system
        # *   cpfs: Cloud Parallel File Storage (CPFS) file system
        # 
        # >  CPFS file systems are available only on the China site (aliyun.com).
        self.file_system_type = file_system_type
        # The number of mount targets to which the permission group is attached.
        self.mount_target_count = mount_target_count
        # The region ID.
        self.region_id = region_id
        # The total number of rules in the permission group.
        self.rule_count = rule_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group_name is not None:
            result['AccessGroupName'] = self.access_group_name
        if self.access_group_type is not None:
            result['AccessGroupType'] = self.access_group_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type
        if self.mount_target_count is not None:
            result['MountTargetCount'] = self.mount_target_count
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.rule_count is not None:
            result['RuleCount'] = self.rule_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessGroupName') is not None:
            self.access_group_name = m.get('AccessGroupName')
        if m.get('AccessGroupType') is not None:
            self.access_group_type = m.get('AccessGroupType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')
        if m.get('MountTargetCount') is not None:
            self.mount_target_count = m.get('MountTargetCount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RuleCount') is not None:
            self.rule_count = m.get('RuleCount')
        return self


class DescribeAccessGroupsResponseBodyAccessGroups(TeaModel):
    def __init__(
        self,
        access_group: List[DescribeAccessGroupsResponseBodyAccessGroupsAccessGroup] = None,
    ):
        self.access_group = access_group

    def validate(self):
        if self.access_group:
            for k in self.access_group:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AccessGroup'] = []
        if self.access_group is not None:
            for k in self.access_group:
                result['AccessGroup'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.access_group = []
        if m.get('AccessGroup') is not None:
            for k in m.get('AccessGroup'):
                temp_model = DescribeAccessGroupsResponseBodyAccessGroupsAccessGroup()
                self.access_group.append(temp_model.from_map(k))
        return self


class DescribeAccessGroupsResponseBody(TeaModel):
    def __init__(
        self,
        access_groups: DescribeAccessGroupsResponseBodyAccessGroups = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The queried permission groups.
        self.access_groups = access_groups
        # The page number.
        self.page_number = page_number
        # The number of permission groups returned per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of permission groups.
        self.total_count = total_count

    def validate(self):
        if self.access_groups:
            self.access_groups.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_groups is not None:
            result['AccessGroups'] = self.access_groups.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessGroups') is not None:
            temp_model = DescribeAccessGroupsResponseBodyAccessGroups()
            self.access_groups = temp_model.from_map(m['AccessGroups'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAccessGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAccessGroupsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAccessGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAccessPointRequest(TeaModel):
    def __init__(
        self,
        access_point_id: str = None,
        file_system_id: str = None,
    ):
        # The ID of the access point.
        # 
        # This parameter is required.
        self.access_point_id = access_point_id
        # The ID of the file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_point_id is not None:
            result['AccessPointId'] = self.access_point_id
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessPointId') is not None:
            self.access_point_id = m.get('AccessPointId')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        return self


class DescribeAccessPointResponseBodyAccessPointPosixUser(TeaModel):
    def __init__(
        self,
        posix_group_id: int = None,
        posix_secondary_group_ids: List[int] = None,
        posix_user_id: int = None,
    ):
        # The ID of the POSIX user group.
        self.posix_group_id = posix_group_id
        # The IDs of the secondary user groups.
        self.posix_secondary_group_ids = posix_secondary_group_ids
        # The ID of the POSIX user.
        self.posix_user_id = posix_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.posix_group_id is not None:
            result['PosixGroupId'] = self.posix_group_id
        if self.posix_secondary_group_ids is not None:
            result['PosixSecondaryGroupIds'] = self.posix_secondary_group_ids
        if self.posix_user_id is not None:
            result['PosixUserId'] = self.posix_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PosixGroupId') is not None:
            self.posix_group_id = m.get('PosixGroupId')
        if m.get('PosixSecondaryGroupIds') is not None:
            self.posix_secondary_group_ids = m.get('PosixSecondaryGroupIds')
        if m.get('PosixUserId') is not None:
            self.posix_user_id = m.get('PosixUserId')
        return self


class DescribeAccessPointResponseBodyAccessPointRootPathPermission(TeaModel):
    def __init__(
        self,
        owner_group_id: int = None,
        owner_user_id: int = None,
        permission: str = None,
    ):
        # The ID of the owner group.
        self.owner_group_id = owner_group_id
        # The owner ID.
        self.owner_user_id = owner_user_id
        # The POSIX permission.
        self.permission = permission

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_group_id is not None:
            result['OwnerGroupId'] = self.owner_group_id
        if self.owner_user_id is not None:
            result['OwnerUserId'] = self.owner_user_id
        if self.permission is not None:
            result['Permission'] = self.permission
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerGroupId') is not None:
            self.owner_group_id = m.get('OwnerGroupId')
        if m.get('OwnerUserId') is not None:
            self.owner_user_id = m.get('OwnerUserId')
        if m.get('Permission') is not None:
            self.permission = m.get('Permission')
        return self


class DescribeAccessPointResponseBodyAccessPoint(TeaModel):
    def __init__(
        self,
        arn: str = None,
        access_group: str = None,
        access_point_id: str = None,
        access_point_name: str = None,
        create_time: str = None,
        domain_name: str = None,
        enabled_ram: bool = None,
        file_system_id: str = None,
        modify_time: str = None,
        posix_user: DescribeAccessPointResponseBodyAccessPointPosixUser = None,
        region_id: str = None,
        root_path: str = None,
        root_path_permission: DescribeAccessPointResponseBodyAccessPointRootPathPermission = None,
        root_path_status: str = None,
        status: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the access point.
        self.arn = arn
        # The name of the permission group.
        self.access_group = access_group
        # The ID of the access point.
        self.access_point_id = access_point_id
        # The name of the access point.
        self.access_point_name = access_point_name
        # The time when the access point was created.
        self.create_time = create_time
        # The domain name of the access point.
        self.domain_name = domain_name
        # Indicates whether the RAM policy is enabled.
        self.enabled_ram = enabled_ram
        # The ID of the file system.
        self.file_system_id = file_system_id
        # The time when the access point was modified.
        self.modify_time = modify_time
        # The POSIX user.
        self.posix_user = posix_user
        # The region ID.
        self.region_id = region_id
        # The root directory.
        self.root_path = root_path
        # The permissions to create the root directory.
        self.root_path_permission = root_path_permission
        # The status of the root directory.
        # 
        # Valid values:
        # 
        # *   0: The rootpath status is unknown.
        # *   1: The rootpath does not exist and may be deleted.
        # *   2: The rootpath is normal.
        self.root_path_status = root_path_status
        # The status of the access point.
        # 
        # Valid values:
        # 
        # *   Active: The access point is available.
        # *   Inactive: The access point is unavailable.
        # *   Pending: The access point is being created.
        # *   Deleting: The access point is being deleted.
        self.status = status
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The ID of the virtual private cloud (VPC).
        # 
        # You must select the VPC of the Elastic Compute Service (ECS) instance on which you want to mount the file system.
        self.vpc_id = vpc_id

    def validate(self):
        if self.posix_user:
            self.posix_user.validate()
        if self.root_path_permission:
            self.root_path_permission.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['ARN'] = self.arn
        if self.access_group is not None:
            result['AccessGroup'] = self.access_group
        if self.access_point_id is not None:
            result['AccessPointId'] = self.access_point_id
        if self.access_point_name is not None:
            result['AccessPointName'] = self.access_point_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.enabled_ram is not None:
            result['EnabledRam'] = self.enabled_ram
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.posix_user is not None:
            result['PosixUser'] = self.posix_user.to_map()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.root_path is not None:
            result['RootPath'] = self.root_path
        if self.root_path_permission is not None:
            result['RootPathPermission'] = self.root_path_permission.to_map()
        if self.root_path_status is not None:
            result['RootPathStatus'] = self.root_path_status
        if self.status is not None:
            result['Status'] = self.status
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ARN') is not None:
            self.arn = m.get('ARN')
        if m.get('AccessGroup') is not None:
            self.access_group = m.get('AccessGroup')
        if m.get('AccessPointId') is not None:
            self.access_point_id = m.get('AccessPointId')
        if m.get('AccessPointName') is not None:
            self.access_point_name = m.get('AccessPointName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EnabledRam') is not None:
            self.enabled_ram = m.get('EnabledRam')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('PosixUser') is not None:
            temp_model = DescribeAccessPointResponseBodyAccessPointPosixUser()
            self.posix_user = temp_model.from_map(m['PosixUser'])
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RootPath') is not None:
            self.root_path = m.get('RootPath')
        if m.get('RootPathPermission') is not None:
            temp_model = DescribeAccessPointResponseBodyAccessPointRootPathPermission()
            self.root_path_permission = temp_model.from_map(m['RootPathPermission'])
        if m.get('RootPathStatus') is not None:
            self.root_path_status = m.get('RootPathStatus')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DescribeAccessPointResponseBody(TeaModel):
    def __init__(
        self,
        access_point: DescribeAccessPointResponseBodyAccessPoint = None,
        request_id: str = None,
    ):
        # The information about the access point.
        self.access_point = access_point
        # The request ID.
        # 
        # This parameter is required.
        self.request_id = request_id

    def validate(self):
        if self.access_point:
            self.access_point.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_point is not None:
            result['AccessPoint'] = self.access_point.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessPoint') is not None:
            temp_model = DescribeAccessPointResponseBodyAccessPoint()
            self.access_point = temp_model.from_map(m['AccessPoint'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAccessPointResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAccessPointResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAccessPointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAccessPointsRequest(TeaModel):
    def __init__(
        self,
        access_group: str = None,
        file_system_id: str = None,
        max_results: int = None,
        next_token: str = None,
    ):
        # The name of the permission group.
        # 
        # This parameter is required for a General-purpose File Storage NAS (NAS) file system.
        # 
        # The default permission group for virtual private clouds (VPCs) is named DEFAULT_VPC_GROUP_NAME.
        self.access_group = access_group
        # The ID of the file system.
        self.file_system_id = file_system_id
        # The number of results for each query.
        # 
        # Valid values: 10 to 100. Default value: 10.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group is not None:
            result['AccessGroup'] = self.access_group
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessGroup') is not None:
            self.access_group = m.get('AccessGroup')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class DescribeAccessPointsResponseBodyAccessPointsPosixUser(TeaModel):
    def __init__(
        self,
        posix_group_id: int = None,
        posix_secondary_group_ids: List[int] = None,
        posix_user_id: int = None,
    ):
        # The ID of the POSIX user group.
        self.posix_group_id = posix_group_id
        # The IDs of the secondary user groups.
        self.posix_secondary_group_ids = posix_secondary_group_ids
        # The ID of the POSIX user.
        self.posix_user_id = posix_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.posix_group_id is not None:
            result['PosixGroupId'] = self.posix_group_id
        if self.posix_secondary_group_ids is not None:
            result['PosixSecondaryGroupIds'] = self.posix_secondary_group_ids
        if self.posix_user_id is not None:
            result['PosixUserId'] = self.posix_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PosixGroupId') is not None:
            self.posix_group_id = m.get('PosixGroupId')
        if m.get('PosixSecondaryGroupIds') is not None:
            self.posix_secondary_group_ids = m.get('PosixSecondaryGroupIds')
        if m.get('PosixUserId') is not None:
            self.posix_user_id = m.get('PosixUserId')
        return self


class DescribeAccessPointsResponseBodyAccessPointsRootPathPermission(TeaModel):
    def __init__(
        self,
        owner_group_id: int = None,
        owner_user_id: int = None,
        permission: str = None,
    ):
        # The ID of the owner group.
        self.owner_group_id = owner_group_id
        # The owner ID.
        self.owner_user_id = owner_user_id
        # The POSIX permission.
        self.permission = permission

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_group_id is not None:
            result['OwnerGroupId'] = self.owner_group_id
        if self.owner_user_id is not None:
            result['OwnerUserId'] = self.owner_user_id
        if self.permission is not None:
            result['Permission'] = self.permission
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerGroupId') is not None:
            self.owner_group_id = m.get('OwnerGroupId')
        if m.get('OwnerUserId') is not None:
            self.owner_user_id = m.get('OwnerUserId')
        if m.get('Permission') is not None:
            self.permission = m.get('Permission')
        return self


class DescribeAccessPointsResponseBodyAccessPoints(TeaModel):
    def __init__(
        self,
        arn: str = None,
        access_group: str = None,
        access_point_id: str = None,
        access_point_name: str = None,
        create_time: str = None,
        domain_name: str = None,
        enabled_ram: bool = None,
        file_system_id: str = None,
        modify_time: str = None,
        posix_user: DescribeAccessPointsResponseBodyAccessPointsPosixUser = None,
        root_path: str = None,
        root_path_permission: DescribeAccessPointsResponseBodyAccessPointsRootPathPermission = None,
        root_path_status: str = None,
        status: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the access point.
        self.arn = arn
        # The name of the permission group.
        self.access_group = access_group
        # The ID of the access point.
        self.access_point_id = access_point_id
        # The name of the access point.
        self.access_point_name = access_point_name
        # The time when the access point was created.
        self.create_time = create_time
        # The domain name of the access point.
        self.domain_name = domain_name
        # Indicates whether the Resource Access Management (RAM) policy is enabled.
        self.enabled_ram = enabled_ram
        # The ID of the file system.
        self.file_system_id = file_system_id
        # The time when the access point was modified.
        self.modify_time = modify_time
        # The Portable Operating System Interface for UNIX (POSIX) user.
        self.posix_user = posix_user
        # The root directory.
        self.root_path = root_path
        # The permissions on the root directory.
        self.root_path_permission = root_path_permission
        # The status of the root directory.
        # 
        # Valid values:
        # 
        # *   0: The rootpath status is unknown.
        # *   1: The rootpath does not exist and may be deleted.
        # *   2: The rootpath is normal.
        self.root_path_status = root_path_status
        # The status of the access point.
        # 
        # Valid values:
        # 
        # *   Active: The access point is available.
        # *   Inactive: The access point is unavailable.
        # *   Pending: The access point is being created.
        # *   Deleting: The access point is being deleted.
        # 
        # >  You can mount a file system only if the access point is in the Active state.
        self.status = status
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The VPC ID.
        self.vpc_id = vpc_id

    def validate(self):
        if self.posix_user:
            self.posix_user.validate()
        if self.root_path_permission:
            self.root_path_permission.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['ARN'] = self.arn
        if self.access_group is not None:
            result['AccessGroup'] = self.access_group
        if self.access_point_id is not None:
            result['AccessPointId'] = self.access_point_id
        if self.access_point_name is not None:
            result['AccessPointName'] = self.access_point_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.enabled_ram is not None:
            result['EnabledRam'] = self.enabled_ram
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.posix_user is not None:
            result['PosixUser'] = self.posix_user.to_map()
        if self.root_path is not None:
            result['RootPath'] = self.root_path
        if self.root_path_permission is not None:
            result['RootPathPermission'] = self.root_path_permission.to_map()
        if self.root_path_status is not None:
            result['RootPathStatus'] = self.root_path_status
        if self.status is not None:
            result['Status'] = self.status
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ARN') is not None:
            self.arn = m.get('ARN')
        if m.get('AccessGroup') is not None:
            self.access_group = m.get('AccessGroup')
        if m.get('AccessPointId') is not None:
            self.access_point_id = m.get('AccessPointId')
        if m.get('AccessPointName') is not None:
            self.access_point_name = m.get('AccessPointName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EnabledRam') is not None:
            self.enabled_ram = m.get('EnabledRam')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('PosixUser') is not None:
            temp_model = DescribeAccessPointsResponseBodyAccessPointsPosixUser()
            self.posix_user = temp_model.from_map(m['PosixUser'])
        if m.get('RootPath') is not None:
            self.root_path = m.get('RootPath')
        if m.get('RootPathPermission') is not None:
            temp_model = DescribeAccessPointsResponseBodyAccessPointsRootPathPermission()
            self.root_path_permission = temp_model.from_map(m['RootPathPermission'])
        if m.get('RootPathStatus') is not None:
            self.root_path_status = m.get('RootPathStatus')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DescribeAccessPointsResponseBody(TeaModel):
    def __init__(
        self,
        access_points: List[DescribeAccessPointsResponseBodyAccessPoints] = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The information about the access point.
        self.access_points = access_points
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token
        # The request ID.
        # 
        # This parameter is required.
        self.request_id = request_id
        # The total number of access points.
        self.total_count = total_count

    def validate(self):
        if self.access_points:
            for k in self.access_points:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AccessPoints'] = []
        if self.access_points is not None:
            for k in self.access_points:
                result['AccessPoints'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.access_points = []
        if m.get('AccessPoints') is not None:
            for k in m.get('AccessPoints'):
                temp_model = DescribeAccessPointsResponseBodyAccessPoints()
                self.access_points.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAccessPointsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAccessPointsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAccessPointsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAccessRulesRequest(TeaModel):
    def __init__(
        self,
        access_group_name: str = None,
        access_rule_id: str = None,
        file_system_type: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The name of the permission group.
        # 
        # This parameter is required.
        self.access_group_name = access_group_name
        # The rule ID.
        self.access_rule_id = access_rule_id
        # The type of the file system.
        # 
        # Valid values:
        # 
        # *   standard (default): General-purpose NAS file system
        # *   extreme: Extreme NAS file system
        self.file_system_type = file_system_type
        # The page number.
        # 
        # Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 10.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group_name is not None:
            result['AccessGroupName'] = self.access_group_name
        if self.access_rule_id is not None:
            result['AccessRuleId'] = self.access_rule_id
        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessGroupName') is not None:
            self.access_group_name = m.get('AccessGroupName')
        if m.get('AccessRuleId') is not None:
            self.access_rule_id = m.get('AccessRuleId')
        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeAccessRulesResponseBodyAccessRulesAccessRule(TeaModel):
    def __init__(
        self,
        access_group_name: str = None,
        access_rule_id: str = None,
        file_system_type: str = None,
        ipv_6source_cidr_ip: str = None,
        priority: int = None,
        rwaccess: str = None,
        region_id: str = None,
        source_cidr_ip: str = None,
        user_access: str = None,
    ):
        # The name of the permission group.
        self.access_group_name = access_group_name
        # The ID of the rule.
        self.access_rule_id = access_rule_id
        # The type of the file system.
        # 
        # Valid values:
        # 
        # *   standard: General-purpose File Storage NAS (NAS) file system
        # *   extreme: Extreme NAS file system
        self.file_system_type = file_system_type
        # The IPv6 address or CIDR block of the authorized object.
        self.ipv_6source_cidr_ip = ipv_6source_cidr_ip
        # The priority of the rule.
        # 
        # If multiple rules are attached to the authorized object, the rule with the highest priority takes effect.
        # 
        # Valid values: 1 to 100. The value 1 indicates the highest priority.
        self.priority = priority
        # The access permissions of the authorized object on the file system.
        # 
        # Valid values:
        # 
        # *   RDWR (default): the read and write permissions
        # *   RDONLY: the read-only permissions
        self.rwaccess = rwaccess
        # The region ID.
        self.region_id = region_id
        # The IP address or CIDR block of the authorized object.
        self.source_cidr_ip = source_cidr_ip
        # The access permissions for different types of users in the authorized object.
        # 
        # Valid values:
        # 
        # *   no_squash: allows access from root users to the file system.
        # *   root_squash: grants root users the least permissions as the nobody user.
        # *   all_squash: grants all users the least permissions as the nobody user.
        # 
        # The nobody user has the least permissions in Linux and can access only the public content of the file system. This ensures the security of the file system.
        self.user_access = user_access

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group_name is not None:
            result['AccessGroupName'] = self.access_group_name
        if self.access_rule_id is not None:
            result['AccessRuleId'] = self.access_rule_id
        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type
        if self.ipv_6source_cidr_ip is not None:
            result['Ipv6SourceCidrIp'] = self.ipv_6source_cidr_ip
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.rwaccess is not None:
            result['RWAccess'] = self.rwaccess
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.source_cidr_ip is not None:
            result['SourceCidrIp'] = self.source_cidr_ip
        if self.user_access is not None:
            result['UserAccess'] = self.user_access
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessGroupName') is not None:
            self.access_group_name = m.get('AccessGroupName')
        if m.get('AccessRuleId') is not None:
            self.access_rule_id = m.get('AccessRuleId')
        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')
        if m.get('Ipv6SourceCidrIp') is not None:
            self.ipv_6source_cidr_ip = m.get('Ipv6SourceCidrIp')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('RWAccess') is not None:
            self.rwaccess = m.get('RWAccess')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SourceCidrIp') is not None:
            self.source_cidr_ip = m.get('SourceCidrIp')
        if m.get('UserAccess') is not None:
            self.user_access = m.get('UserAccess')
        return self


class DescribeAccessRulesResponseBodyAccessRules(TeaModel):
    def __init__(
        self,
        access_rule: List[DescribeAccessRulesResponseBodyAccessRulesAccessRule] = None,
    ):
        self.access_rule = access_rule

    def validate(self):
        if self.access_rule:
            for k in self.access_rule:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AccessRule'] = []
        if self.access_rule is not None:
            for k in self.access_rule:
                result['AccessRule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.access_rule = []
        if m.get('AccessRule') is not None:
            for k in m.get('AccessRule'):
                temp_model = DescribeAccessRulesResponseBodyAccessRulesAccessRule()
                self.access_rule.append(temp_model.from_map(k))
        return self


class DescribeAccessRulesResponseBody(TeaModel):
    def __init__(
        self,
        access_rules: DescribeAccessRulesResponseBodyAccessRules = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The rules in the permission group.
        self.access_rules = access_rules
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of rules.
        self.total_count = total_count

    def validate(self):
        if self.access_rules:
            self.access_rules.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_rules is not None:
            result['AccessRules'] = self.access_rules.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessRules') is not None:
            temp_model = DescribeAccessRulesResponseBodyAccessRules()
            self.access_rules = temp_model.from_map(m['AccessRules'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAccessRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAccessRulesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAccessRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAutoSnapshotPoliciesRequest(TeaModel):
    def __init__(
        self,
        auto_snapshot_policy_id: str = None,
        file_system_type: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The ID of the automatic snapshot policy.
        self.auto_snapshot_policy_id = auto_snapshot_policy_id
        # The type of the file system.
        # 
        # Valid value: extreme, which indicates Extreme File Storage NAS (NAS) file systems.
        self.file_system_type = file_system_type
        # The page number.
        # 
        # Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 10.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_snapshot_policy_id is not None:
            result['AutoSnapshotPolicyId'] = self.auto_snapshot_policy_id
        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoSnapshotPolicyId') is not None:
            self.auto_snapshot_policy_id = m.get('AutoSnapshotPolicyId')
        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeAutoSnapshotPoliciesResponseBodyAutoSnapshotPoliciesAutoSnapshotPolicy(TeaModel):
    def __init__(
        self,
        auto_snapshot_policy_id: str = None,
        auto_snapshot_policy_name: str = None,
        create_time: str = None,
        file_system_nums: int = None,
        file_system_type: str = None,
        region_id: str = None,
        repeat_weekdays: str = None,
        retention_days: int = None,
        status: str = None,
        time_points: str = None,
    ):
        # The ID of the automatic snapshot policy.
        self.auto_snapshot_policy_id = auto_snapshot_policy_id
        # The name of the automatic snapshot policy.
        self.auto_snapshot_policy_name = auto_snapshot_policy_name
        # The time when the automatic snapshot policy was created.
        # 
        # The time follows the [ISO8601](https://www.iso.org/iso-8601-date-and-time-format.html) standard in the `yyyy-MM-ddTHH:mm:ssZ` format. The time is displayed in UTC.
        self.create_time = create_time
        # The number of file systems to which the automatic snapshot policy applies.
        self.file_system_nums = file_system_nums
        # The type of the file system.
        self.file_system_type = file_system_type
        # The region ID of the automatic snapshot policy.
        self.region_id = region_id
        # The days of a week on which auto snapshots are created.
        # 
        # Auto snapshots are created on a weekly basis.
        # 
        # Valid values: 1 to 7. The values from 1 to 7 indicate 7 days in a week from Monday to Sunday.
        self.repeat_weekdays = repeat_weekdays
        # The retention period of auto snapshots.
        # 
        # Unit: days.
        # 
        # Valid values:
        # 
        # *   \\-1: Auto snapshots are permanently retained. After the number of auto snapshots exceeds the upper limit, the earliest auto snapshot is automatically deleted.
        # *   1 to 65536: Auto snapshots are retained for the specified days. After the retention period of auto snapshots expires, the auto snapshots are automatically deleted.
        self.retention_days = retention_days
        # The status of the automatic snapshot policy.
        # 
        # Valid values:
        # 
        # *   Creating: The automatic snapshot policy is being created.
        # *   Available: The automatic snapshot policy is available.
        self.status = status
        # The points in time at which auto snapshots are created.
        # 
        # Unit: hours.
        # 
        # Valid values: `0 to 23`. The values from 0 to 23 indicate a total of 24 hours from `00:00 to 23:00`. For example, 1 indicates 01:00. A maximum of 24 points in time can be returned. Multiple points in time are separated with commas (,).
        self.time_points = time_points

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_snapshot_policy_id is not None:
            result['AutoSnapshotPolicyId'] = self.auto_snapshot_policy_id
        if self.auto_snapshot_policy_name is not None:
            result['AutoSnapshotPolicyName'] = self.auto_snapshot_policy_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.file_system_nums is not None:
            result['FileSystemNums'] = self.file_system_nums
        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.repeat_weekdays is not None:
            result['RepeatWeekdays'] = self.repeat_weekdays
        if self.retention_days is not None:
            result['RetentionDays'] = self.retention_days
        if self.status is not None:
            result['Status'] = self.status
        if self.time_points is not None:
            result['TimePoints'] = self.time_points
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoSnapshotPolicyId') is not None:
            self.auto_snapshot_policy_id = m.get('AutoSnapshotPolicyId')
        if m.get('AutoSnapshotPolicyName') is not None:
            self.auto_snapshot_policy_name = m.get('AutoSnapshotPolicyName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('FileSystemNums') is not None:
            self.file_system_nums = m.get('FileSystemNums')
        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RepeatWeekdays') is not None:
            self.repeat_weekdays = m.get('RepeatWeekdays')
        if m.get('RetentionDays') is not None:
            self.retention_days = m.get('RetentionDays')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TimePoints') is not None:
            self.time_points = m.get('TimePoints')
        return self


class DescribeAutoSnapshotPoliciesResponseBodyAutoSnapshotPolicies(TeaModel):
    def __init__(
        self,
        auto_snapshot_policy: List[DescribeAutoSnapshotPoliciesResponseBodyAutoSnapshotPoliciesAutoSnapshotPolicy] = None,
    ):
        self.auto_snapshot_policy = auto_snapshot_policy

    def validate(self):
        if self.auto_snapshot_policy:
            for k in self.auto_snapshot_policy:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AutoSnapshotPolicy'] = []
        if self.auto_snapshot_policy is not None:
            for k in self.auto_snapshot_policy:
                result['AutoSnapshotPolicy'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.auto_snapshot_policy = []
        if m.get('AutoSnapshotPolicy') is not None:
            for k in m.get('AutoSnapshotPolicy'):
                temp_model = DescribeAutoSnapshotPoliciesResponseBodyAutoSnapshotPoliciesAutoSnapshotPolicy()
                self.auto_snapshot_policy.append(temp_model.from_map(k))
        return self


class DescribeAutoSnapshotPoliciesResponseBody(TeaModel):
    def __init__(
        self,
        auto_snapshot_policies: DescribeAutoSnapshotPoliciesResponseBodyAutoSnapshotPolicies = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The queried automatic snapshot policies.
        self.auto_snapshot_policies = auto_snapshot_policies
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of automatic snapshot policies.
        self.total_count = total_count

    def validate(self):
        if self.auto_snapshot_policies:
            self.auto_snapshot_policies.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_snapshot_policies is not None:
            result['AutoSnapshotPolicies'] = self.auto_snapshot_policies.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoSnapshotPolicies') is not None:
            temp_model = DescribeAutoSnapshotPoliciesResponseBodyAutoSnapshotPolicies()
            self.auto_snapshot_policies = temp_model.from_map(m['AutoSnapshotPolicies'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAutoSnapshotPoliciesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAutoSnapshotPoliciesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAutoSnapshotPoliciesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAutoSnapshotTasksRequest(TeaModel):
    def __init__(
        self,
        auto_snapshot_policy_ids: str = None,
        file_system_ids: str = None,
        file_system_type: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The IDs of automatic snapshot policies.
        # 
        # You can specify a maximum of 100 policy IDs. If you want to query the tasks of multiple automatic snapshot policies, you must separate the policy IDs with commas (,).
        self.auto_snapshot_policy_ids = auto_snapshot_policy_ids
        # The ID of the file system.
        # 
        # You can specify a maximum of 100 file system IDs. If you want to query the snapshots of multiple file systems, you must separate the file system IDs with commas (,).
        self.file_system_ids = file_system_ids
        # The type of the file system.
        # 
        # Valid value: extreme, which indicates Extreme NAS file systems.
        # 
        # This parameter is required.
        self.file_system_type = file_system_type
        # The number of entries per page.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 10.
        self.page_number = page_number
        # The page number.
        # 
        # Pages start from page 1. Default value: 1.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_snapshot_policy_ids is not None:
            result['AutoSnapshotPolicyIds'] = self.auto_snapshot_policy_ids
        if self.file_system_ids is not None:
            result['FileSystemIds'] = self.file_system_ids
        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoSnapshotPolicyIds') is not None:
            self.auto_snapshot_policy_ids = m.get('AutoSnapshotPolicyIds')
        if m.get('FileSystemIds') is not None:
            self.file_system_ids = m.get('FileSystemIds')
        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeAutoSnapshotTasksResponseBodyAutoSnapshotTasksAutoSnapshotTask(TeaModel):
    def __init__(
        self,
        auto_snapshot_policy_id: str = None,
        source_file_system_id: str = None,
    ):
        # The ID of the automatic snapshot policy.
        self.auto_snapshot_policy_id = auto_snapshot_policy_id
        # The ID of the file system.
        self.source_file_system_id = source_file_system_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_snapshot_policy_id is not None:
            result['AutoSnapshotPolicyId'] = self.auto_snapshot_policy_id
        if self.source_file_system_id is not None:
            result['SourceFileSystemId'] = self.source_file_system_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoSnapshotPolicyId') is not None:
            self.auto_snapshot_policy_id = m.get('AutoSnapshotPolicyId')
        if m.get('SourceFileSystemId') is not None:
            self.source_file_system_id = m.get('SourceFileSystemId')
        return self


class DescribeAutoSnapshotTasksResponseBodyAutoSnapshotTasks(TeaModel):
    def __init__(
        self,
        auto_snapshot_task: List[DescribeAutoSnapshotTasksResponseBodyAutoSnapshotTasksAutoSnapshotTask] = None,
    ):
        self.auto_snapshot_task = auto_snapshot_task

    def validate(self):
        if self.auto_snapshot_task:
            for k in self.auto_snapshot_task:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AutoSnapshotTask'] = []
        if self.auto_snapshot_task is not None:
            for k in self.auto_snapshot_task:
                result['AutoSnapshotTask'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.auto_snapshot_task = []
        if m.get('AutoSnapshotTask') is not None:
            for k in m.get('AutoSnapshotTask'):
                temp_model = DescribeAutoSnapshotTasksResponseBodyAutoSnapshotTasksAutoSnapshotTask()
                self.auto_snapshot_task.append(temp_model.from_map(k))
        return self


class DescribeAutoSnapshotTasksResponseBody(TeaModel):
    def __init__(
        self,
        auto_snapshot_tasks: DescribeAutoSnapshotTasksResponseBodyAutoSnapshotTasks = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The queried automatic snapshot tasks.
        self.auto_snapshot_tasks = auto_snapshot_tasks
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of automatic snapshot tasks.
        self.total_count = total_count

    def validate(self):
        if self.auto_snapshot_tasks:
            self.auto_snapshot_tasks.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_snapshot_tasks is not None:
            result['AutoSnapshotTasks'] = self.auto_snapshot_tasks.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoSnapshotTasks') is not None:
            temp_model = DescribeAutoSnapshotTasksResponseBodyAutoSnapshotTasks()
            self.auto_snapshot_tasks = temp_model.from_map(m['AutoSnapshotTasks'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAutoSnapshotTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAutoSnapshotTasksResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAutoSnapshotTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBlackListClientsRequest(TeaModel):
    def __init__(
        self,
        client_ip: str = None,
        file_system_id: str = None,
        region_id: str = None,
    ):
        # The IP address of the client.
        self.client_ip = client_ip
        # The ID of the file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The ID of the region where the file system resides.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_ip is not None:
            result['ClientIP'] = self.client_ip
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientIP') is not None:
            self.client_ip = m.get('ClientIP')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeBlackListClientsResponseBody(TeaModel):
    def __init__(
        self,
        clients: str = None,
        request_id: str = None,
    ):
        # The IDs of clients and the status of each client. The parameter value is a JSON string, for example, `{"client1": "EVICTING","client2":"EVICTED"}`.
        # 
        # Available client statuses include:
        # 
        # *   EVICTING: The client is being evicted.
        # *   EVICTED: The client is evicted.
        # *   ACCEPTING: The write access to the file system is being granted to the client.
        # *   ACCEPTABLE: The write access to the file system is granted to the client.
        self.clients = clients
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.clients is not None:
            result['Clients'] = self.clients
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Clients') is not None:
            self.clients = m.get('Clients')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeBlackListClientsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeBlackListClientsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeBlackListClientsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDataFlowSubTasksRequestFilters(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The filter name.
        # 
        # Valid values:
        # 
        # *   DataFlowIds: filters data flow subtasks by data flow ID.
        # *   DataFlowTaskIds: filters data flow subtasks by data flow task ID.
        # *   DataFlowSubTaskIds: filters data flow subtasks by data streaming task ID.
        # *   Status: filters data flow subtasks by status.
        # *   SrcFilePath: filters data flow subtasks by source file path.
        # *   DstFilePath: filters data flow subtasks by destination file path.
        self.key = key
        # The filter value. This parameter does not support wildcards.
        # 
        # *   If Key is set to DataFlowIds, set Value to a data flow ID or a part of the data flow ID. You can specify a data flow ID or a group of data flow IDs. You can specify a maximum of 10 data flow IDs. Example: `df-194433a5be31****` or `df-194433a5be31****,df-244433a5be31****`.
        # *   If Key is set to DataFlowTaskIds, set Value to a data flow task ID or a part of the data flow task ID. You can specify a data flow task ID or a group of data flow task IDs. You can specify a maximum of 10 data flow task IDs. Example:  `task-38aa8e890f45****` or `task-38aa8e890f45****,task-27aa8e890f45****`.
        # *   If Key is set to DataFlowSubTaskIds, set Value to a data streaming task ID or a part of the data streaming task ID. You can specify a data streaming task ID or a group of data streaming task IDs. You can specify a maximum of 10 data streaming task IDs. Example: ` subTaskId-370kyfmyknxcyzw****  `or `subTaskId-370kyfmyknxcyzw****,subTaskId-280kyfmyknxcyzw****`.
        # *   If Key is set to Status, set Value to the status of the data flow task. The status can be EXPIRED, CREATED, RUNNING, COMPLETE, CANCELING, FAILED, or CANCELED. Combined query is supported.
        # *   If Key is set to SrcFilePath, set Value to the path of the source file. The path can be up to 1,023 characters in length.
        # *   If Key is set to DstFilePath, set Value to the path of the destination file. The path can be up to 1,023 characters in length.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDataFlowSubTasksRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        filters: List[DescribeDataFlowSubTasksRequestFilters] = None,
        max_results: int = None,
        next_token: str = None,
    ):
        # The ID of the file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The filter that is used to query data streaming tasks.
        self.filters = filters
        # The number of results for each query.
        # 
        # *   Valid values: 20 to 100.
        # *   Default value: 20.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token

    def validate(self):
        if self.filters:
            for k in self.filters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        result['Filters'] = []
        if self.filters is not None:
            for k in self.filters:
                result['Filters'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        self.filters = []
        if m.get('Filters') is not None:
            for k in m.get('Filters'):
                temp_model = DescribeDataFlowSubTasksRequestFilters()
                self.filters.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class DescribeDataFlowSubTasksResponseBodyDataFlowSubTaskDataFlowSubTaskFileDetail(TeaModel):
    def __init__(
        self,
        checksum: str = None,
        modify_time: int = None,
        size: int = None,
    ):
        # The checksum. Format example: crc64:123456.
        self.checksum = checksum
        # The time when the file was modified. The value is a UNIX timestamp. Unit: ns.
        self.modify_time = modify_time
        # The file size. Unit: bytes.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.checksum is not None:
            result['Checksum'] = self.checksum
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Checksum') is not None:
            self.checksum = m.get('Checksum')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class DescribeDataFlowSubTasksResponseBodyDataFlowSubTaskDataFlowSubTaskProgressStats(TeaModel):
    def __init__(
        self,
        actual_bytes: int = None,
        average_speed: int = None,
        bytes_done: int = None,
        bytes_total: int = None,
    ):
        # The actual amount of data for which the data flow task is complete. Unit: bytes.
        self.actual_bytes = actual_bytes
        # The average flow velocity. Unit: bytes/s.
        self.average_speed = average_speed
        # The amount of data (including skipped data) for which the data flow task is complete. Unit: bytes.
        self.bytes_done = bytes_done
        # The amount of data scanned on the source. Unit: bytes.
        self.bytes_total = bytes_total

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actual_bytes is not None:
            result['ActualBytes'] = self.actual_bytes
        if self.average_speed is not None:
            result['AverageSpeed'] = self.average_speed
        if self.bytes_done is not None:
            result['BytesDone'] = self.bytes_done
        if self.bytes_total is not None:
            result['BytesTotal'] = self.bytes_total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActualBytes') is not None:
            self.actual_bytes = m.get('ActualBytes')
        if m.get('AverageSpeed') is not None:
            self.average_speed = m.get('AverageSpeed')
        if m.get('BytesDone') is not None:
            self.bytes_done = m.get('BytesDone')
        if m.get('BytesTotal') is not None:
            self.bytes_total = m.get('BytesTotal')
        return self


class DescribeDataFlowSubTasksResponseBodyDataFlowSubTaskDataFlowSubTask(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        data_flow_id: str = None,
        data_flow_sub_task_id: str = None,
        data_flow_task_id: str = None,
        dst_file_path: str = None,
        end_time: str = None,
        error_msg: str = None,
        file_detail: DescribeDataFlowSubTasksResponseBodyDataFlowSubTaskDataFlowSubTaskFileDetail = None,
        file_system_id: str = None,
        progress: int = None,
        progress_stats: DescribeDataFlowSubTasksResponseBodyDataFlowSubTaskDataFlowSubTaskProgressStats = None,
        src_file_path: str = None,
        start_time: str = None,
        status: str = None,
    ):
        # The time when the data streaming task was created.
        self.create_time = create_time
        # The ID of the data flow.
        self.data_flow_id = data_flow_id
        # The ID of the data streaming task.
        self.data_flow_sub_task_id = data_flow_sub_task_id
        # The ID of the data flow task.
        self.data_flow_task_id = data_flow_task_id
        # The path of the destination file. Limits:
        # 
        # *   The path must be 1 to 1,023 characters in length.
        # *   The path must be encoded in UTF-8.
        # *   The path must start with a forward slash (/).
        # *   The path must end with the file name.
        self.dst_file_path = dst_file_path
        # The time when the data streaming task ended.
        self.end_time = end_time
        # The error message returned when the task failed.
        self.error_msg = error_msg
        # The file information.
        self.file_detail = file_detail
        # The ID of the file system.
        self.file_system_id = file_system_id
        # The progress of the data streaming task. Valid values: 0 to 10000.
        self.progress = progress
        # The progress information about data streaming tasks.
        self.progress_stats = progress_stats
        # The path of the source file. Limits:
        # 
        # *   The path must be 1 to 1,023 characters in length.
        # *   The path must be encoded in UTF-8.
        # *   The path must start with a forward slash (/).
        # *   The path must end with the file name.
        self.src_file_path = src_file_path
        # The time when the data streaming task started.
        self.start_time = start_time
        # The status of the data streaming task. Valid values:
        # 
        # *   EXPIRED: The task is terminated.
        # *   CREATED: The task is created.
        # *   RUNNING: The task is running.
        # *   COMPLETE: The task is complete.
        # *   CANCELING: The task is being canceled.
        # *   FAILED: The task failed to be executed.
        # *   CANCELED: The task is canceled.
        self.status = status

    def validate(self):
        if self.file_detail:
            self.file_detail.validate()
        if self.progress_stats:
            self.progress_stats.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.data_flow_id is not None:
            result['DataFlowId'] = self.data_flow_id
        if self.data_flow_sub_task_id is not None:
            result['DataFlowSubTaskId'] = self.data_flow_sub_task_id
        if self.data_flow_task_id is not None:
            result['DataFlowTaskId'] = self.data_flow_task_id
        if self.dst_file_path is not None:
            result['DstFilePath'] = self.dst_file_path
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.file_detail is not None:
            result['FileDetail'] = self.file_detail.to_map()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.progress_stats is not None:
            result['ProgressStats'] = self.progress_stats.to_map()
        if self.src_file_path is not None:
            result['SrcFilePath'] = self.src_file_path
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DataFlowId') is not None:
            self.data_flow_id = m.get('DataFlowId')
        if m.get('DataFlowSubTaskId') is not None:
            self.data_flow_sub_task_id = m.get('DataFlowSubTaskId')
        if m.get('DataFlowTaskId') is not None:
            self.data_flow_task_id = m.get('DataFlowTaskId')
        if m.get('DstFilePath') is not None:
            self.dst_file_path = m.get('DstFilePath')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('FileDetail') is not None:
            temp_model = DescribeDataFlowSubTasksResponseBodyDataFlowSubTaskDataFlowSubTaskFileDetail()
            self.file_detail = temp_model.from_map(m['FileDetail'])
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('ProgressStats') is not None:
            temp_model = DescribeDataFlowSubTasksResponseBodyDataFlowSubTaskDataFlowSubTaskProgressStats()
            self.progress_stats = temp_model.from_map(m['ProgressStats'])
        if m.get('SrcFilePath') is not None:
            self.src_file_path = m.get('SrcFilePath')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeDataFlowSubTasksResponseBodyDataFlowSubTask(TeaModel):
    def __init__(
        self,
        data_flow_sub_task: List[DescribeDataFlowSubTasksResponseBodyDataFlowSubTaskDataFlowSubTask] = None,
    ):
        self.data_flow_sub_task = data_flow_sub_task

    def validate(self):
        if self.data_flow_sub_task:
            for k in self.data_flow_sub_task:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataFlowSubTask'] = []
        if self.data_flow_sub_task is not None:
            for k in self.data_flow_sub_task:
                result['DataFlowSubTask'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_flow_sub_task = []
        if m.get('DataFlowSubTask') is not None:
            for k in m.get('DataFlowSubTask'):
                temp_model = DescribeDataFlowSubTasksResponseBodyDataFlowSubTaskDataFlowSubTask()
                self.data_flow_sub_task.append(temp_model.from_map(k))
        return self


class DescribeDataFlowSubTasksResponseBody(TeaModel):
    def __init__(
        self,
        data_flow_sub_task: DescribeDataFlowSubTasksResponseBodyDataFlowSubTask = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The details about data streaming tasks.
        self.data_flow_sub_task = data_flow_sub_task
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data_flow_sub_task:
            self.data_flow_sub_task.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_flow_sub_task is not None:
            result['DataFlowSubTask'] = self.data_flow_sub_task.to_map()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataFlowSubTask') is not None:
            temp_model = DescribeDataFlowSubTasksResponseBodyDataFlowSubTask()
            self.data_flow_sub_task = temp_model.from_map(m['DataFlowSubTask'])
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDataFlowSubTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDataFlowSubTasksResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDataFlowSubTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDataFlowTasksRequestFilters(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The filter name.
        # 
        # Valid values:
        # 
        # *   DataFlowIds: filters data flow tasks by data flow ID.
        # *   TaskIds: filters data flow tasks by task ID.
        # *   Originator: filters data flow tasks by task initiator.
        # *   TaskActions: filters data flow tasks by task type.
        # *   DataTypes: filters data flow tasks by data type.
        # *   Status: filters data flow tasks by data flow status.
        # *   CreateTimeBegin: filters data flow tasks that are created after a specified time.
        # *   CreateTimeEnd: filters data flow tasks that are created before a specified time.
        # *   StartTimeBegin: filters data flow tasks that are started after a specified time.
        # *   StartTimeEnd: filters data flow tasks that are started before a specified time.
        # *   EndTimeBegin: filters data flow tasks that are stopped after a specified time.
        # *   EndTimeEnd: filters data flow tasks that are stopped before a specified time.
        self.key = key
        # The filter value. This parameter does not support wildcards.
        # 
        # *   If Key is set to DataFlowIds, set Value to a data flow ID or a part of the data flow ID. You can specify a data flow ID or a group of data flow IDs. You can specify a maximum of 10 data flow IDs. Example: `df-194433a5be31****` or `df-194433a512a2****,df-234533a5be31****`.
        # *   If Key is set to TaskId, set Value to a data flow task ID or a part of the data flow task ID. You can specify a data flow task ID or a group of data flow task IDs. You can specify a maximum of 10 data flow task IDs. Example: `task-38aa8e890f45****` or `task-38aa8e890f45****,task-29ae8e890f45****`.
        # *   If Key is set to TaskActions, set Value to the type of data flow task. The task type can be **Import**, **Export**, **Evict**, **Inventory**, **StreamImport**, or **StreamExport**. Combined query is supported. CPFS for LINGJUN supports only the Import, Export, StreamImport, and StreamExport tasks. Only CPFS for LINGJUN V2.6.0 and later support the StreamImport and StreamExport tasks.
        # *   If Key is set to DataTypes, set Value to the data type of the data flow task. The data type can be MetaAndData, Metadata, or Data. Combined query is supported.
        # *   If Key is set to Originator, set Value to the initiator of the data flow task. The initiator can be User or System.
        # *   If Key is set to Status, set Value to the status of the data flow task. The status can be Pending, Executing, Failed, Completed, Canceling, or Canceled. Combined query is supported.
        # *   If Key is set to CreateTimeBegin, set Value to the beginning of the time range to create the data flow task. Time format: `yyyy-MM-ddThh:mmZ`.
        # *   If Key is set to CreateTimeEnd, set Value to the end of the time range to create the data flow task. Time format: `yyyy-MM-ddThh:mmZ`.
        # *   If Key is set to StartTimeBegin, set Value to the beginning of the time range to start the data flow task. Time format: `yyyy-MM-ddThh:mmZ`.
        # *   If Key is set to StartTimeEnd, set Value to the end of the time range to start the data flow task. Time format: `yyyy-MM-ddThh:mmZ`.
        # *   If Key is set to EndTimeBegin, set Value to the beginning of the time range to stop the data flow task. Time format: `yyyy-MM-ddThh:mmZ`.
        # *   If Key is set to EndTimeEnd, set Value to the end of the time range to stop the data flow task. Time format: `yyyy-MM-ddThh:mmZ`.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDataFlowTasksRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        filters: List[DescribeDataFlowTasksRequestFilters] = None,
        max_results: int = None,
        next_token: str = None,
    ):
        # The ID of the file system.
        # 
        # *   The IDs of CPFS file systems must start with `cpfs-`. Example: cpfs-099394bd928c\\*\\*\\*\\*.
        # *   The IDs of CPFS for LINGJUN file systems must start with `bmcpfs-`. Example: bmcpfs-290w65p03ok64ya\\*\\*\\*\\*.
        # 
        # >  CPFS is not supported on the international site.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The details about filters.
        self.filters = filters
        # The number of results for each query.
        # 
        # Valid values: 10 to 100.
        # 
        # Default value: 20.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token

    def validate(self):
        if self.filters:
            for k in self.filters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        result['Filters'] = []
        if self.filters is not None:
            for k in self.filters:
                result['Filters'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        self.filters = []
        if m.get('Filters') is not None:
            for k in m.get('Filters'):
                temp_model = DescribeDataFlowTasksRequestFilters()
                self.filters.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class DescribeDataFlowTasksResponseBodyTaskInfoTaskProgressStats(TeaModel):
    def __init__(
        self,
        actual_bytes: int = None,
        actual_files: int = None,
        average_speed: int = None,
        bytes_done: int = None,
        bytes_total: int = None,
        files_done: int = None,
        files_total: int = None,
        remain_time: int = None,
    ):
        # The actual amount of data for which the data flow task is complete. Unit: bytes.
        self.actual_bytes = actual_bytes
        # The actual number of files for which the data flow task is complete.
        self.actual_files = actual_files
        # The average flow velocity. Unit: bytes/s.
        self.average_speed = average_speed
        # The amount of data (including skipped data) for which the data flow task is complete. Unit: bytes.
        self.bytes_done = bytes_done
        # The amount of data scanned on the source. Unit: bytes.
        self.bytes_total = bytes_total
        # The number of files (including skipped files) for which the data flow task is complete.
        self.files_done = files_done
        # The number of files scanned on the source.
        self.files_total = files_total
        # The estimated remaining execution time. Unit: seconds.
        self.remain_time = remain_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actual_bytes is not None:
            result['ActualBytes'] = self.actual_bytes
        if self.actual_files is not None:
            result['ActualFiles'] = self.actual_files
        if self.average_speed is not None:
            result['AverageSpeed'] = self.average_speed
        if self.bytes_done is not None:
            result['BytesDone'] = self.bytes_done
        if self.bytes_total is not None:
            result['BytesTotal'] = self.bytes_total
        if self.files_done is not None:
            result['FilesDone'] = self.files_done
        if self.files_total is not None:
            result['FilesTotal'] = self.files_total
        if self.remain_time is not None:
            result['RemainTime'] = self.remain_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActualBytes') is not None:
            self.actual_bytes = m.get('ActualBytes')
        if m.get('ActualFiles') is not None:
            self.actual_files = m.get('ActualFiles')
        if m.get('AverageSpeed') is not None:
            self.average_speed = m.get('AverageSpeed')
        if m.get('BytesDone') is not None:
            self.bytes_done = m.get('BytesDone')
        if m.get('BytesTotal') is not None:
            self.bytes_total = m.get('BytesTotal')
        if m.get('FilesDone') is not None:
            self.files_done = m.get('FilesDone')
        if m.get('FilesTotal') is not None:
            self.files_total = m.get('FilesTotal')
        if m.get('RemainTime') is not None:
            self.remain_time = m.get('RemainTime')
        return self


class DescribeDataFlowTasksResponseBodyTaskInfoTaskReportsReport(TeaModel):
    def __init__(
        self,
        name: str = None,
        path: str = None,
    ):
        # The name of the report.
        # 
        # *   CPFS:
        # 
        #     TotalFilesReport: task reports.
        # 
        # *   CPFS for LINGJUN:
        # 
        #     *   FailedFilesReport: failed file reports.
        #     *   SkippedFilesReport: skipped file reports.
        #     *   SuccessFilesReport: successful file reports.
        self.name = name
        # The report URL.
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class DescribeDataFlowTasksResponseBodyTaskInfoTaskReports(TeaModel):
    def __init__(
        self,
        report: List[DescribeDataFlowTasksResponseBodyTaskInfoTaskReportsReport] = None,
    ):
        self.report = report

    def validate(self):
        if self.report:
            for k in self.report:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Report'] = []
        if self.report is not None:
            for k in self.report:
                result['Report'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.report = []
        if m.get('Report') is not None:
            for k in m.get('Report'):
                temp_model = DescribeDataFlowTasksResponseBodyTaskInfoTaskReportsReport()
                self.report.append(temp_model.from_map(k))
        return self


class DescribeDataFlowTasksResponseBodyTaskInfoTask(TeaModel):
    def __init__(
        self,
        conflict_policy: str = None,
        create_time: str = None,
        data_flow_id: str = None,
        data_type: str = None,
        directory: str = None,
        dst_directory: str = None,
        end_time: str = None,
        error_msg: str = None,
        file_system_path: str = None,
        filesystem_id: str = None,
        fs_path: str = None,
        includes: str = None,
        originator: str = None,
        progress: int = None,
        progress_stats: DescribeDataFlowTasksResponseBodyTaskInfoTaskProgressStats = None,
        report_path: str = None,
        reports: DescribeDataFlowTasksResponseBodyTaskInfoTaskReports = None,
        source_storage: str = None,
        start_time: str = None,
        status: str = None,
        task_action: str = None,
        task_id: str = None,
    ):
        # The conflict policy for files with the same name. Valid values:
        # 
        # *   SKIP_THE_FILE: skips files with the same name.
        # *   KEEP_LATEST: compares the update time and keeps the latest version.
        # *   OVERWRITE_EXISTING: forcibly overwrites the existing file.
        self.conflict_policy = conflict_policy
        # The time when the task was created.
        self.create_time = create_time
        # The ID of the data flow.
        self.data_flow_id = data_flow_id
        # The type of data on which operations are performed by the data flow task. Valid values:
        # 
        # *   Metadata: the metadata of a file, including the timestamp, ownership, and permission information of the file. If you select Metadata, only the metadata of the file is imported. You can only query the file. When you access the file data, the file is loaded from the source storage as required.
        # *   Data: the data blocks of the file.
        # *   MetaAndData: the metadata and data blocks of the file.
        # 
        # >  CPFS for LINGJUN supports only the MetaAndData type.
        self.data_type = data_type
        # The directory in which the data flow task is executed.
        self.directory = directory
        # The directory mapped to the data flow task.
        self.dst_directory = dst_directory
        # The time when the task ended.
        self.end_time = end_time
        # The cause of the task exception.
        # 
        # >  If this parameter is not returned or the return value is empty, no error occurs.
        self.error_msg = error_msg
        # The directory of the fileset in the CPFS file system.
        # 
        # Limits:
        # 
        # *   The directory must be 2 to 1024 characters in length.
        # *   The directory must be encoded in UTF-8.
        # *   The directory must start and end with a forward slash (/).
        # *   The directory must be a fileset directory in the CPFS file system.
        # 
        # >  Only CPFS supports this parameter.
        self.file_system_path = file_system_path
        # The ID of the file system.
        self.filesystem_id = filesystem_id
        # The path of the smart directory.
        self.fs_path = fs_path
        self.includes = includes
        # The initiator of the data flow task. Valid values:
        # 
        # *   User: The task is initiated by a user.
        # *   System: The task is automatically initiated by CPFS based on the automatic update interval.
        # 
        # >  Only CPFS supports this parameter.
        self.originator = originator
        # The progress of the data flow task. The number of operations that have been performed by the data flow task.
        self.progress = progress
        # The progress of the data flow task.
        self.progress_stats = progress_stats
        # The save path of data flow task reports in the CPFS file system.
        # 
        # *   The task reports for a CPFS file system are generated in the `.dataflow_report` directory of the CPFS file system.
        # *   CPFS for LINGJUN returns an OSS download link for you to download the task reports.
        self.report_path = report_path
        # The reports.
        # 
        # >  Streaming tasks do not support reports.
        self.reports = reports
        # The access path of the source storage. Format: `<storage type>://[<account id>:]<path>`.
        # 
        # Parameters:
        # 
        # *   storage type: Only Object Storage Service (OSS) is supported.
        # 
        # *   account id: the UID of the account of the source storage.
        # 
        # *   path: the name of the OSS bucket. Limits:
        # 
        #     *   The name can contain only lowercase letters, digits, and hyphens (-). The name must start and end with a lowercase letter or digit.
        #     *   The name can be up to 128 characters in length.
        #     *   The name must be encoded in UTF-8.
        # 
        # > 
        # 
        # *   The OSS bucket must be an existing bucket in the region.
        # 
        # *   Only CPFS for LINGJUN V2.6.0 and later support the account id parameter.
        self.source_storage = source_storage
        # The time when the task started.
        self.start_time = start_time
        # The status of the data flow task. Valid values:
        # 
        # *   Pending: The data flow task has been created and has not started.
        # *   Executing: The data flow task is being executed.
        # *   Failed: The data flow task failed to be executed. You can view the cause of the failure in the data flow task report.
        # *   Completed: The data flow task is completed. You can check that all the files have been correctly transferred in the data flow task report.
        # *   Canceled: The data flow task is canceled and is not completed.
        # *   Canceling: The data flow task is being canceled.
        self.status = status
        # The type of the data flow task. Valid values:
        # 
        # *   Import: imports data stored in the source storage to a CPFS file system.
        # *   Export: exports specified data from a CPFS file system to the source storage.
        # *   StreamImport: imports the specified data from the source storage to a CPFS file system in streaming mode.
        # *   StreamExport: exports specified data from a CPFS file system to the source storage in streaming mode.
        # *   Evict: releases the data blocks of a file in a CPFS file system. After the eviction, only the metadata of the file is retained in the CPFS file system. You can still query the file. However, the data blocks of the file are cleared and do not occupy the storage space in the CPFS file system. When you access the file data, the file is loaded from the source storage as required.
        # *   Inventory: obtains the inventory list managed by a data flow from the CPFS file system, providing the cache status of inventories in the data flow.
        # 
        # >  Only CPFS for LINGJUN V2.6.0 and later support StreamImport and StreamExport.
        self.task_action = task_action
        # The ID of the data flow task.
        self.task_id = task_id

    def validate(self):
        if self.progress_stats:
            self.progress_stats.validate()
        if self.reports:
            self.reports.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conflict_policy is not None:
            result['ConflictPolicy'] = self.conflict_policy
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.data_flow_id is not None:
            result['DataFlowId'] = self.data_flow_id
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.directory is not None:
            result['Directory'] = self.directory
        if self.dst_directory is not None:
            result['DstDirectory'] = self.dst_directory
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.file_system_path is not None:
            result['FileSystemPath'] = self.file_system_path
        if self.filesystem_id is not None:
            result['FilesystemId'] = self.filesystem_id
        if self.fs_path is not None:
            result['FsPath'] = self.fs_path
        if self.includes is not None:
            result['Includes'] = self.includes
        if self.originator is not None:
            result['Originator'] = self.originator
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.progress_stats is not None:
            result['ProgressStats'] = self.progress_stats.to_map()
        if self.report_path is not None:
            result['ReportPath'] = self.report_path
        if self.reports is not None:
            result['Reports'] = self.reports.to_map()
        if self.source_storage is not None:
            result['SourceStorage'] = self.source_storage
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.task_action is not None:
            result['TaskAction'] = self.task_action
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConflictPolicy') is not None:
            self.conflict_policy = m.get('ConflictPolicy')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DataFlowId') is not None:
            self.data_flow_id = m.get('DataFlowId')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('Directory') is not None:
            self.directory = m.get('Directory')
        if m.get('DstDirectory') is not None:
            self.dst_directory = m.get('DstDirectory')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('FileSystemPath') is not None:
            self.file_system_path = m.get('FileSystemPath')
        if m.get('FilesystemId') is not None:
            self.filesystem_id = m.get('FilesystemId')
        if m.get('FsPath') is not None:
            self.fs_path = m.get('FsPath')
        if m.get('Includes') is not None:
            self.includes = m.get('Includes')
        if m.get('Originator') is not None:
            self.originator = m.get('Originator')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('ProgressStats') is not None:
            temp_model = DescribeDataFlowTasksResponseBodyTaskInfoTaskProgressStats()
            self.progress_stats = temp_model.from_map(m['ProgressStats'])
        if m.get('ReportPath') is not None:
            self.report_path = m.get('ReportPath')
        if m.get('Reports') is not None:
            temp_model = DescribeDataFlowTasksResponseBodyTaskInfoTaskReports()
            self.reports = temp_model.from_map(m['Reports'])
        if m.get('SourceStorage') is not None:
            self.source_storage = m.get('SourceStorage')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskAction') is not None:
            self.task_action = m.get('TaskAction')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeDataFlowTasksResponseBodyTaskInfo(TeaModel):
    def __init__(
        self,
        task: List[DescribeDataFlowTasksResponseBodyTaskInfoTask] = None,
    ):
        self.task = task

    def validate(self):
        if self.task:
            for k in self.task:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Task'] = []
        if self.task is not None:
            for k in self.task:
                result['Task'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.task = []
        if m.get('Task') is not None:
            for k in m.get('Task'):
                temp_model = DescribeDataFlowTasksResponseBodyTaskInfoTask()
                self.task.append(temp_model.from_map(k))
        return self


class DescribeDataFlowTasksResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        task_info: DescribeDataFlowTasksResponseBodyTaskInfo = None,
    ):
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The information about data flow tasks.
        self.task_info = task_info

    def validate(self):
        if self.task_info:
            self.task_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_info is not None:
            result['TaskInfo'] = self.task_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskInfo') is not None:
            temp_model = DescribeDataFlowTasksResponseBodyTaskInfo()
            self.task_info = temp_model.from_map(m['TaskInfo'])
        return self


class DescribeDataFlowTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDataFlowTasksResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDataFlowTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDataFlowsRequestFilters(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The filter name. Valid values:
        # 
        # *   DataFlowIds: filters data flows by data flow ID.
        # *   FsetIds: filters data flows by fileset ID.
        # *   FileSystemPath: filters data flows based on the path of a fileset in a CPFS file system.
        # *   SourceStorage: filters data flows based on the access path of the source storage.
        # *   ThroughputList: filters data flows based on data flow throughput.
        # *   Description: filters data flows based on the fileset description.
        # *   Status: filters data flows based on data flow status.
        self.key = key
        # The filter value. This parameter does not support wildcards.
        # 
        # *   If Key is set to DataFlowIds, set Value to a data flow ID or a part of the data flow ID. You can specify a data flow ID or a group of data flow IDs. You can specify a maximum of 10 data flow IDs. Example: `df-194433a5be31****` or `df-194433a5be31****,df-184433a5be31****`.
        # *   If Key is set to FsetIds, set Value to a fileset ID or a part of the fileset ID. You can specify a fileset ID or a group of fileset IDs. You can specify a maximum of 10 fileset IDs. Example: `fset-1902718ea0ae****` or `fset-1902718ea0ae****,fset-1242718ea0ae****`.
        # *   If Key is set to FileSystemPath, set Value to the path or a part of the path of a fileset in a CPFS file system. The value of the parameter must be 1 to 1,024 characters in length.
        # *   If Key is set to SourceStorage, set Value to the access path or a part of the access path of the source storage. The path can be up to 1,024 characters in length.
        # *   If Key is set to ThroughputList, set Value to the data flow throughput. Combined query is supported.
        # *   If Key is set to Description, set Value to a data flow description or a part of the data flow description.
        # *   If Key is set to Status, set Value to the data flow status.
        # *   If Key is set to SourceStoragePath, set Value to the access path or a part of the access path of the source storage. The path can be up to 1,024 characters in length.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDataFlowsRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        filters: List[DescribeDataFlowsRequestFilters] = None,
        max_results: int = None,
        next_token: str = None,
    ):
        # The ID of the file system.
        # 
        # *   The IDs of CPFS file systems must start with `cpfs-`. Example: cpfs-125487\\*\\*\\*\\*.
        # *   The IDs of CPFS for LINGJUN file systems must start with `bmcpfs-`. Example: bmcpfs-0015\\*\\*\\*\\*.
        # 
        # >  CPFS file systems are available only on the China site (aliyun.com).
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The filter that is used to query data flows.
        self.filters = filters
        # The number of results for each query.
        # 
        # Valid values: 10 to 100. Default value: 20.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token

    def validate(self):
        if self.filters:
            for k in self.filters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        result['Filters'] = []
        if self.filters is not None:
            for k in self.filters:
                result['Filters'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        self.filters = []
        if m.get('Filters') is not None:
            for k in m.get('Filters'):
                temp_model = DescribeDataFlowsRequestFilters()
                self.filters.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class DescribeDataFlowsResponseBodyDataFlowInfoDataFlowAutoRefreshAutoRefresh(TeaModel):
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
        self.refresh_path = refresh_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.refresh_path is not None:
            result['RefreshPath'] = self.refresh_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RefreshPath') is not None:
            self.refresh_path = m.get('RefreshPath')
        return self


class DescribeDataFlowsResponseBodyDataFlowInfoDataFlowAutoRefresh(TeaModel):
    def __init__(
        self,
        auto_refresh: List[DescribeDataFlowsResponseBodyDataFlowInfoDataFlowAutoRefreshAutoRefresh] = None,
    ):
        self.auto_refresh = auto_refresh

    def validate(self):
        if self.auto_refresh:
            for k in self.auto_refresh:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AutoRefresh'] = []
        if self.auto_refresh is not None:
            for k in self.auto_refresh:
                result['AutoRefresh'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.auto_refresh = []
        if m.get('AutoRefresh') is not None:
            for k in m.get('AutoRefresh'):
                temp_model = DescribeDataFlowsResponseBodyDataFlowInfoDataFlowAutoRefreshAutoRefresh()
                self.auto_refresh.append(temp_model.from_map(k))
        return self


class DescribeDataFlowsResponseBodyDataFlowInfoDataFlow(TeaModel):
    def __init__(
        self,
        auto_refresh: DescribeDataFlowsResponseBodyDataFlowInfoDataFlowAutoRefresh = None,
        auto_refresh_interval: int = None,
        auto_refresh_policy: str = None,
        create_time: str = None,
        data_flow_id: str = None,
        description: str = None,
        error_message: str = None,
        file_system_id: str = None,
        file_system_path: str = None,
        fset_description: str = None,
        fset_id: str = None,
        source_security_type: str = None,
        source_storage: str = None,
        source_storage_path: str = None,
        status: str = None,
        throughput: int = None,
        update_time: str = None,
    ):
        # The details about automatic update policies.
        # 
        # >  Only CPFS supports this parameter.
        self.auto_refresh = auto_refresh
        # The automatic update interval. CPFS checks whether data is updated in the directory at the interval specified by this parameter. If data is updated, CPFS starts an automatic update task. Unit: minutes.
        # 
        # Valid values: 5 to 526600. Default value: 10.
        # 
        # >  Only CPFS supports this parameter.
        self.auto_refresh_interval = auto_refresh_interval
        # The automatic update policy. The updated data in the source storage is imported into the CPFS file system based on the policy. Valid values:
        # 
        # *   None: Updated data in the source storage is not automatically imported into the CPFS file system. You can run a data flow task to import the updated data from the source storage.
        # *   ImportChanged: Updated data in the source storage is automatically imported into the CPFS file system.
        # 
        # >  Only CPFS supports this parameter.
        self.auto_refresh_policy = auto_refresh_policy
        # The time when the fileset was created.
        # 
        # The time follows the ISO 8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format.
        self.create_time = create_time
        # The dataflow ID.
        self.data_flow_id = data_flow_id
        # The description of the dataflow.
        # 
        # Limits:
        # 
        # *   The description must be 2 to 128 characters in length.
        # *   The description must start with a letter but cannot start with `http://` or `https://`.
        # *   The description can contain letters, digits, colons (:), underscores (_), and hyphens (-).
        self.description = description
        # The error message returned. Valid values:
        # 
        # *   None (default): The dataflow status is normal.
        # *   SourceStorageUnreachable: The access path of the source storage is not found.
        # *   ThroughputTooLow: The dataflow throughput is low.
        self.error_message = error_message
        # The ID of the file system.
        self.file_system_id = file_system_id
        # The directory of the fileset in the CPFS file system.
        # 
        # Limits:
        # 
        # *   The directory must be 2 to 1,024 characters in length.
        # *   The directory must be encoded in UTF-8.
        # *   The directory must start and end with a forward slash (/).
        # *   The directory must be a fileset directory in the CPFS file system.
        # 
        # >  Only CPFS supports this parameter.
        self.file_system_path = file_system_path
        # The description of the automatic update.
        # 
        # >  Only CPFS supports this parameter.
        self.fset_description = fset_description
        # The fileset ID.
        self.fset_id = fset_id
        # The type of security mechanism for the source storage. This parameter must be specified if the source storage is accessed with a security mechanism. Valid values:
        # 
        # *   None (default): The source storage can be accessed without a security mechanism.
        # *   SSL: The source storage must be accessed with an SSL certificate.
        self.source_security_type = source_security_type
        # The access path of the source storage. Format: `<storage type>://<path>`.
        # 
        # Parameters:
        # 
        # *   storage type: Only Object Storage Service (OSS) is supported.
        # 
        # *   path: the name of the OSS bucket.
        # 
        #     *   The name can contain only lowercase letters, digits, and hyphens (-). The name must start and end with a lowercase letter or digit.
        #     *   The name must be 8 to 128 characters in length.
        #     *   The name must be encoded in UTF-8.
        #     *   The name cannot start with http:// or https://.
        # 
        # >  The OSS bucket must be an existing bucket in the region.
        self.source_storage = source_storage
        # The access path in the bucket of the source storage.
        # 
        # >  Only CPFS for LINGJUN supports this parameter.
        self.source_storage_path = source_storage_path
        # The dataflow status. Valid values:
        # 
        # *   Starting: The dataflow is being created or enabled.
        # *   Running: The dataflow has been created and is running properly.
        # *   Updating: The dataflow is being modified. For example, the dataflow throughput is increased and the automatic update interval is modified.
        # *   Deleting: The dataflow is being deleted.
        # *   Stopping: The dataflow is being disabled.
        # *   Stopped: The dataflow has been disabled.
        # *   Misconfigured: The dataflow configuration is abnormal. For example, the source storage is inaccessible, and the automatic update cannot be completed due to low dataflow throughput.
        self.status = status
        # The maximum dataflow throughput. Unit: MB/s. Valid values:
        # 
        # *   600
        # *   1,200
        # *   1,500
        # 
        # >  The dataflow throughput must be less than the I/O throughput of the file system.
        self.throughput = throughput
        # The time when the fileset was last updated.
        # 
        # The time follows the ISO 8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format.
        self.update_time = update_time

    def validate(self):
        if self.auto_refresh:
            self.auto_refresh.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_refresh is not None:
            result['AutoRefresh'] = self.auto_refresh.to_map()
        if self.auto_refresh_interval is not None:
            result['AutoRefreshInterval'] = self.auto_refresh_interval
        if self.auto_refresh_policy is not None:
            result['AutoRefreshPolicy'] = self.auto_refresh_policy
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.data_flow_id is not None:
            result['DataFlowId'] = self.data_flow_id
        if self.description is not None:
            result['Description'] = self.description
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.file_system_path is not None:
            result['FileSystemPath'] = self.file_system_path
        if self.fset_description is not None:
            result['FsetDescription'] = self.fset_description
        if self.fset_id is not None:
            result['FsetId'] = self.fset_id
        if self.source_security_type is not None:
            result['SourceSecurityType'] = self.source_security_type
        if self.source_storage is not None:
            result['SourceStorage'] = self.source_storage
        if self.source_storage_path is not None:
            result['SourceStoragePath'] = self.source_storage_path
        if self.status is not None:
            result['Status'] = self.status
        if self.throughput is not None:
            result['Throughput'] = self.throughput
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRefresh') is not None:
            temp_model = DescribeDataFlowsResponseBodyDataFlowInfoDataFlowAutoRefresh()
            self.auto_refresh = temp_model.from_map(m['AutoRefresh'])
        if m.get('AutoRefreshInterval') is not None:
            self.auto_refresh_interval = m.get('AutoRefreshInterval')
        if m.get('AutoRefreshPolicy') is not None:
            self.auto_refresh_policy = m.get('AutoRefreshPolicy')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DataFlowId') is not None:
            self.data_flow_id = m.get('DataFlowId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('FileSystemPath') is not None:
            self.file_system_path = m.get('FileSystemPath')
        if m.get('FsetDescription') is not None:
            self.fset_description = m.get('FsetDescription')
        if m.get('FsetId') is not None:
            self.fset_id = m.get('FsetId')
        if m.get('SourceSecurityType') is not None:
            self.source_security_type = m.get('SourceSecurityType')
        if m.get('SourceStorage') is not None:
            self.source_storage = m.get('SourceStorage')
        if m.get('SourceStoragePath') is not None:
            self.source_storage_path = m.get('SourceStoragePath')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Throughput') is not None:
            self.throughput = m.get('Throughput')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class DescribeDataFlowsResponseBodyDataFlowInfo(TeaModel):
    def __init__(
        self,
        data_flow: List[DescribeDataFlowsResponseBodyDataFlowInfoDataFlow] = None,
    ):
        self.data_flow = data_flow

    def validate(self):
        if self.data_flow:
            for k in self.data_flow:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataFlow'] = []
        if self.data_flow is not None:
            for k in self.data_flow:
                result['DataFlow'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_flow = []
        if m.get('DataFlow') is not None:
            for k in m.get('DataFlow'):
                temp_model = DescribeDataFlowsResponseBodyDataFlowInfoDataFlow()
                self.data_flow.append(temp_model.from_map(k))
        return self


class DescribeDataFlowsResponseBody(TeaModel):
    def __init__(
        self,
        data_flow_info: DescribeDataFlowsResponseBodyDataFlowInfo = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The details about data flows.
        self.data_flow_info = data_flow_info
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data_flow_info:
            self.data_flow_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_flow_info is not None:
            result['DataFlowInfo'] = self.data_flow_info.to_map()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataFlowInfo') is not None:
            temp_model = DescribeDataFlowsResponseBodyDataFlowInfo()
            self.data_flow_info = temp_model.from_map(m['DataFlowInfo'])
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDataFlowsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDataFlowsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDataFlowsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDirQuotasRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        page_number: int = None,
        page_size: int = None,
        path: str = None,
    ):
        # The ID of the file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The page number.
        # 
        # Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 10.
        # 
        # Valid values: 1 to 100.
        self.page_size = page_size
        # The absolute path of a directory.
        # 
        # If you do not specify this parameter, all directories for which quotas are created are returned.
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class DescribeDirQuotasResponseBodyDirQuotaInfosUserQuotaInfos(TeaModel):
    def __init__(
        self,
        file_count_limit: int = None,
        file_count_real: int = None,
        quota_type: str = None,
        size_limit: int = None,
        size_real: int = None,
        size_real_in_byte: int = None,
        user_id: str = None,
        user_type: str = None,
    ):
        # The maximum number of files that a user can create in the directory.
        self.file_count_limit = file_count_limit
        # The total number of files that a user has created in the directory.
        self.file_count_real = file_count_real
        # The type of the quota. Valid values: Accounting and Enforcement.
        self.quota_type = quota_type
        # The maximum size of files that a user can create in the directory. Unit: GiB.
        self.size_limit = size_limit
        # The total size of files that a user has created in the directory. Unit: GiB.
        self.size_real = size_real
        # The total size of files that a user has created in the directory. Unit: bytes.
        self.size_real_in_byte = size_real_in_byte
        # The ID of the user that you specify to create a quota for the directory. The value depends on the value of the UserType parameter. Valid values: Uid and Gid.
        self.user_id = user_id
        # The type of user. Valid values: Uid, Gid, and AllUsers.
        # 
        # *   If Uid or Gid is returned, a value is returned for UserId.
        # *   If AllUsers is returned, UserId is empty.
        self.user_type = user_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_count_limit is not None:
            result['FileCountLimit'] = self.file_count_limit
        if self.file_count_real is not None:
            result['FileCountReal'] = self.file_count_real
        if self.quota_type is not None:
            result['QuotaType'] = self.quota_type
        if self.size_limit is not None:
            result['SizeLimit'] = self.size_limit
        if self.size_real is not None:
            result['SizeReal'] = self.size_real
        if self.size_real_in_byte is not None:
            result['SizeRealInByte'] = self.size_real_in_byte
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileCountLimit') is not None:
            self.file_count_limit = m.get('FileCountLimit')
        if m.get('FileCountReal') is not None:
            self.file_count_real = m.get('FileCountReal')
        if m.get('QuotaType') is not None:
            self.quota_type = m.get('QuotaType')
        if m.get('SizeLimit') is not None:
            self.size_limit = m.get('SizeLimit')
        if m.get('SizeReal') is not None:
            self.size_real = m.get('SizeReal')
        if m.get('SizeRealInByte') is not None:
            self.size_real_in_byte = m.get('SizeRealInByte')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class DescribeDirQuotasResponseBodyDirQuotaInfos(TeaModel):
    def __init__(
        self,
        dir_inode: str = None,
        path: str = None,
        status: str = None,
        user_quota_infos: List[DescribeDirQuotasResponseBodyDirQuotaInfosUserQuotaInfos] = None,
    ):
        # The inode number of the directory.
        self.dir_inode = dir_inode
        # The absolute path of a directory.
        self.path = path
        # The status of the quota created for the directory. Valid values: Initializing and Normal. The Initializing state indicates that the quota is being created. The Normal state indicates that the quota is created.
        self.status = status
        # The information about quotas for all users.
        self.user_quota_infos = user_quota_infos

    def validate(self):
        if self.user_quota_infos:
            for k in self.user_quota_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dir_inode is not None:
            result['DirInode'] = self.dir_inode
        if self.path is not None:
            result['Path'] = self.path
        if self.status is not None:
            result['Status'] = self.status
        result['UserQuotaInfos'] = []
        if self.user_quota_infos is not None:
            for k in self.user_quota_infos:
                result['UserQuotaInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirInode') is not None:
            self.dir_inode = m.get('DirInode')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.user_quota_infos = []
        if m.get('UserQuotaInfos') is not None:
            for k in m.get('UserQuotaInfos'):
                temp_model = DescribeDirQuotasResponseBodyDirQuotaInfosUserQuotaInfos()
                self.user_quota_infos.append(temp_model.from_map(k))
        return self


class DescribeDirQuotasResponseBody(TeaModel):
    def __init__(
        self,
        dir_quota_infos: List[DescribeDirQuotasResponseBodyDirQuotaInfos] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The queried directory quotas.
        self.dir_quota_infos = dir_quota_infos
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of directories.
        self.total_count = total_count

    def validate(self):
        if self.dir_quota_infos:
            for k in self.dir_quota_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DirQuotaInfos'] = []
        if self.dir_quota_infos is not None:
            for k in self.dir_quota_infos:
                result['DirQuotaInfos'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dir_quota_infos = []
        if m.get('DirQuotaInfos') is not None:
            for k in m.get('DirQuotaInfos'):
                temp_model = DescribeDirQuotasResponseBodyDirQuotaInfos()
                self.dir_quota_infos.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDirQuotasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDirQuotasResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDirQuotasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFileSystemStatisticsRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
    ):
        # The page number.
        # 
        # Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 10.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeFileSystemStatisticsResponseBodyFileSystemStatisticsFileSystemStatistic(TeaModel):
    def __init__(
        self,
        expired_count: int = None,
        expiring_count: int = None,
        file_system_type: str = None,
        metered_size: int = None,
        total_count: int = None,
    ):
        # The number of expired file systems.
        self.expired_count = expired_count
        # The number of expiring file systems.
        # 
        # File systems whose expiration time is less than or equal to seven days away from the current time are counted.
        self.expiring_count = expiring_count
        # The type of the file system.
        self.file_system_type = file_system_type
        # The storage usage of the file system.
        # 
        # The value of this parameter is the maximum storage usage of the file system over the last hour.
        # 
        # Unit: bytes.
        self.metered_size = metered_size
        # The number of file systems of the current type.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expired_count is not None:
            result['ExpiredCount'] = self.expired_count
        if self.expiring_count is not None:
            result['ExpiringCount'] = self.expiring_count
        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type
        if self.metered_size is not None:
            result['MeteredSize'] = self.metered_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpiredCount') is not None:
            self.expired_count = m.get('ExpiredCount')
        if m.get('ExpiringCount') is not None:
            self.expiring_count = m.get('ExpiringCount')
        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')
        if m.get('MeteredSize') is not None:
            self.metered_size = m.get('MeteredSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeFileSystemStatisticsResponseBodyFileSystemStatistics(TeaModel):
    def __init__(
        self,
        file_system_statistic: List[DescribeFileSystemStatisticsResponseBodyFileSystemStatisticsFileSystemStatistic] = None,
    ):
        self.file_system_statistic = file_system_statistic

    def validate(self):
        if self.file_system_statistic:
            for k in self.file_system_statistic:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FileSystemStatistic'] = []
        if self.file_system_statistic is not None:
            for k in self.file_system_statistic:
                result['FileSystemStatistic'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.file_system_statistic = []
        if m.get('FileSystemStatistic') is not None:
            for k in m.get('FileSystemStatistic'):
                temp_model = DescribeFileSystemStatisticsResponseBodyFileSystemStatisticsFileSystemStatistic()
                self.file_system_statistic.append(temp_model.from_map(k))
        return self


class DescribeFileSystemStatisticsResponseBodyFileSystemsFileSystemPackagesPackage(TeaModel):
    def __init__(
        self,
        expired_time: str = None,
        package_id: str = None,
        size: int = None,
        start_time: str = None,
    ):
        # The end time of the validity period for the storage plan.
        self.expired_time = expired_time
        # The ID of the storage plan.
        self.package_id = package_id
        # The capacity of the storage plan.
        self.size = size
        # The start time of the validity period for the storage plan.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.package_id is not None:
            result['PackageId'] = self.package_id
        if self.size is not None:
            result['Size'] = self.size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('PackageId') is not None:
            self.package_id = m.get('PackageId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeFileSystemStatisticsResponseBodyFileSystemsFileSystemPackages(TeaModel):
    def __init__(
        self,
        package: List[DescribeFileSystemStatisticsResponseBodyFileSystemsFileSystemPackagesPackage] = None,
    ):
        self.package = package

    def validate(self):
        if self.package:
            for k in self.package:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Package'] = []
        if self.package is not None:
            for k in self.package:
                result['Package'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.package = []
        if m.get('Package') is not None:
            for k in m.get('Package'):
                temp_model = DescribeFileSystemStatisticsResponseBodyFileSystemsFileSystemPackagesPackage()
                self.package.append(temp_model.from_map(k))
        return self


class DescribeFileSystemStatisticsResponseBodyFileSystemsFileSystem(TeaModel):
    def __init__(
        self,
        capacity: int = None,
        charge_type: str = None,
        create_time: str = None,
        description: str = None,
        expired_time: str = None,
        file_system_id: str = None,
        file_system_type: str = None,
        metered_iasize: int = None,
        metered_size: int = None,
        packages: DescribeFileSystemStatisticsResponseBodyFileSystemsFileSystemPackages = None,
        protocol_type: str = None,
        region_id: str = None,
        status: str = None,
        storage_type: str = None,
        zone_id: str = None,
    ):
        # The capacity of the file system.
        # 
        # Unit: GiB.
        self.capacity = capacity
        # The billing method.
        # 
        # Valid values:
        # 
        # *   Subscription: The subscription billing method is used.
        # *   PayAsYouGo: The pay-as-you-go billing method is used.
        # *   Package: A storage plan is attached to the file system.
        self.charge_type = charge_type
        # The time when the NAS file system was created.
        self.create_time = create_time
        # The description of the file system.
        self.description = description
        # The time when the file system expires.
        self.expired_time = expired_time
        # The ID of the file system.
        self.file_system_id = file_system_id
        # The type of the file system.
        # 
        # Valid values:
        # 
        # *   standard: General-purpose NAS file system
        # *   extreme: Extreme NAS file system
        # *   cpfs: CPFS file system
        self.file_system_type = file_system_type
        # The storage usage of the Infrequent Access (IA) storage medium.
        # 
        # Unit: bytes.
        self.metered_iasize = metered_iasize
        # The storage usage of the file system.
        # 
        # The value of this parameter is the maximum storage usage of the file system over the last hour. Unit: bytes.
        self.metered_size = metered_size
        # The information about storage plans.
        self.packages = packages
        # The protocol type of the file system.
        # 
        # Valid values:
        # 
        # *   NFS: Network File System (NFS)
        # *   SMB: Server Message Block (SMB)
        # *   cpfs: the protocol type supported by the CPFS file system
        self.protocol_type = protocol_type
        # The region ID.
        self.region_id = region_id
        # The status of the file system.
        # 
        # This parameter is returned for Extreme NAS file systems and Cloud Parallel File Storage (CPFS) file systems. Valid values:
        # 
        # *   Pending: The file system is being created or modified.
        # *   Running: The file system is available. Before you create a mount target for the file system, make sure that the file system is in the Running state.
        # *   Stopped: The file system is unavailable.
        # *   Extending: The file system is being scaled out.
        # *   Stopping: The file system is being disabled.
        # *   Deleting: The file system is being deleted.
        self.status = status
        # The storage type.
        # 
        # Valid values:
        # 
        # *   Valid values for General-purpose NAS file systems: Capacity and Performance.
        # *   Valid values for Extreme NAS file systems: standard and advance.
        # *   Valid values for CPFS file systems: advance_100 (100 MB/s/TiB baseline) and advance_200 (200 MB/s/TiB baseline).
        self.storage_type = storage_type
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        if self.packages:
            self.packages.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type
        if self.metered_iasize is not None:
            result['MeteredIASize'] = self.metered_iasize
        if self.metered_size is not None:
            result['MeteredSize'] = self.metered_size
        if self.packages is not None:
            result['Packages'] = self.packages.to_map()
        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')
        if m.get('MeteredIASize') is not None:
            self.metered_iasize = m.get('MeteredIASize')
        if m.get('MeteredSize') is not None:
            self.metered_size = m.get('MeteredSize')
        if m.get('Packages') is not None:
            temp_model = DescribeFileSystemStatisticsResponseBodyFileSystemsFileSystemPackages()
            self.packages = temp_model.from_map(m['Packages'])
        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeFileSystemStatisticsResponseBodyFileSystems(TeaModel):
    def __init__(
        self,
        file_system: List[DescribeFileSystemStatisticsResponseBodyFileSystemsFileSystem] = None,
    ):
        self.file_system = file_system

    def validate(self):
        if self.file_system:
            for k in self.file_system:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FileSystem'] = []
        if self.file_system is not None:
            for k in self.file_system:
                result['FileSystem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.file_system = []
        if m.get('FileSystem') is not None:
            for k in m.get('FileSystem'):
                temp_model = DescribeFileSystemStatisticsResponseBodyFileSystemsFileSystem()
                self.file_system.append(temp_model.from_map(k))
        return self


class DescribeFileSystemStatisticsResponseBody(TeaModel):
    def __init__(
        self,
        file_system_statistics: DescribeFileSystemStatisticsResponseBodyFileSystemStatistics = None,
        file_systems: DescribeFileSystemStatisticsResponseBodyFileSystems = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The statistics of file systems.
        self.file_system_statistics = file_system_statistics
        # The queried file systems.
        self.file_systems = file_systems
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of file system entries.
        self.total_count = total_count

    def validate(self):
        if self.file_system_statistics:
            self.file_system_statistics.validate()
        if self.file_systems:
            self.file_systems.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_statistics is not None:
            result['FileSystemStatistics'] = self.file_system_statistics.to_map()
        if self.file_systems is not None:
            result['FileSystems'] = self.file_systems.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemStatistics') is not None:
            temp_model = DescribeFileSystemStatisticsResponseBodyFileSystemStatistics()
            self.file_system_statistics = temp_model.from_map(m['FileSystemStatistics'])
        if m.get('FileSystems') is not None:
            temp_model = DescribeFileSystemStatisticsResponseBodyFileSystems()
            self.file_systems = temp_model.from_map(m['FileSystems'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeFileSystemStatisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeFileSystemStatisticsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeFileSystemStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFileSystemsRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N to add to the resource.
        # 
        # Limits:
        # - Valid values of N: 1 to 20.
        # - The tag key must be 1 to 128 characters in length.
        # - The tag key cannot start with aliyun or acs:.
        # - The tag key cannot contain http:// or https://.
        self.key = key
        # The value of tag N to add to the resource.
        # 
        # Limits:
        # - Valid values of N: 1 to 20.
        # - The tag value must be 1 to 128 characters in length.
        # - The tag value cannot start with aliyun or acs:.
        # - The tag value cannot contain http:// or https://.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeFileSystemsRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        file_system_type: str = None,
        page_number: int = None,
        page_size: int = None,
        resource_group_id: str = None,
        tag: List[DescribeFileSystemsRequestTag] = None,
        vpc_id: str = None,
    ):
        # The ID of the file system.
        # 
        # - Sample ID of a General-purpose NAS file system: 31a8e4****.
        # - The IDs of Extreme NAS file systems must start with extreme-, for example, extreme-0015****.
        # - The IDs of Cloud Parallel File Storage (CPFS) file systems must start with cpfs-, for example, cpfs-125487****.
        # > CPFS file systems are available only on the China site (aliyun.com).
        self.file_system_id = file_system_id
        # The type of the file system.
        # 
        # Valid values:
        # - all (default): all types
        # - standard: General-purpose NAS file system
        # - extreme: Extreme NAS file system
        # - cpfs: CPFS file system
        # > CPFS file systems are available only on the China site (aliyun.com).
        self.file_system_type = file_system_type
        # The page number.
        # 
        # Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 10.
        self.page_size = page_size
        # The resource group ID.
        # 
        # You can log on to the [Resource Management console](https://resourcemanager.console.aliyun.com/resource-groups?) to view resource group IDs.
        self.resource_group_id = resource_group_id
        # The details about the tags.
        self.tag = tag
        # The ID of the virtual private cloud (VPC).
        # 
        # If you want to mount the file system on an Elastic Compute Service (ECS) instance, the file system and the ECS instance must reside in the same VPC.
        self.vpc_id = vpc_id

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeFileSystemsRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DescribeFileSystemsResponseBodyFileSystemsFileSystemLdap(TeaModel):
    def __init__(
        self,
        bind_dn: str = None,
        search_base: str = None,
        uri: str = None,
    ):
        # An LDAP entry.
        self.bind_dn = bind_dn
        # An LDAP search base.
        self.search_base = search_base
        # An LDAP URI.
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bind_dn is not None:
            result['BindDN'] = self.bind_dn
        if self.search_base is not None:
            result['SearchBase'] = self.search_base
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindDN') is not None:
            self.bind_dn = m.get('BindDN')
        if m.get('SearchBase') is not None:
            self.search_base = m.get('SearchBase')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargetsMountTargetClientMasterNodesClientMasterNode(TeaModel):
    def __init__(
        self,
        default_passwd: str = None,
        ecs_id: str = None,
        ecs_ip: str = None,
    ):
        # The default logon password of the ECS instance on the client management node.
        self.default_passwd = default_passwd
        # The ID of the ECS instance on the client management node.
        self.ecs_id = ecs_id
        # The IP address of the ECS instance on the client management node.
        self.ecs_ip = ecs_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_passwd is not None:
            result['DefaultPasswd'] = self.default_passwd
        if self.ecs_id is not None:
            result['EcsId'] = self.ecs_id
        if self.ecs_ip is not None:
            result['EcsIp'] = self.ecs_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultPasswd') is not None:
            self.default_passwd = m.get('DefaultPasswd')
        if m.get('EcsId') is not None:
            self.ecs_id = m.get('EcsId')
        if m.get('EcsIp') is not None:
            self.ecs_ip = m.get('EcsIp')
        return self


class DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargetsMountTargetClientMasterNodes(TeaModel):
    def __init__(
        self,
        client_master_node: List[DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargetsMountTargetClientMasterNodesClientMasterNode] = None,
    ):
        self.client_master_node = client_master_node

    def validate(self):
        if self.client_master_node:
            for k in self.client_master_node:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ClientMasterNode'] = []
        if self.client_master_node is not None:
            for k in self.client_master_node:
                result['ClientMasterNode'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.client_master_node = []
        if m.get('ClientMasterNode') is not None:
            for k in m.get('ClientMasterNode'):
                temp_model = DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargetsMountTargetClientMasterNodesClientMasterNode()
                self.client_master_node.append(temp_model.from_map(k))
        return self


class DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargetsMountTargetTagsTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargetsMountTargetTags(TeaModel):
    def __init__(
        self,
        tag: List[DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargetsMountTargetTagsTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargetsMountTargetTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargetsMountTarget(TeaModel):
    def __init__(
        self,
        access_group_name: str = None,
        client_master_nodes: DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargetsMountTargetClientMasterNodes = None,
        dual_stack_mount_target_domain: str = None,
        mount_target_domain: str = None,
        network_type: str = None,
        status: str = None,
        tags: DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargetsMountTargetTags = None,
        vpc_id: str = None,
        vsw_id: str = None,
    ):
        # The name of the permission group that is attached to the mount target.
        self.access_group_name = access_group_name
        # The information about client management nodes.
        # 
        # This parameter is available only for CPFS file systems.
        self.client_master_nodes = client_master_nodes
        # The dual-stack (IPv4 and IPv6) domain name of the mount target.
        # > Only Extreme NAS file systems that reside in the Chinese mainland support IPv6.
        self.dual_stack_mount_target_domain = dual_stack_mount_target_domain
        # The domain name of the mount target.
        self.mount_target_domain = mount_target_domain
        # The network type. Valid value: vpc.
        self.network_type = network_type
        # The status of the mount target.
        # 
        # Valid values:
        # 
        # *   Active: The mount target is available.
        # *   Inactive: The mount target is unavailable.
        # *   Pending: The mount target is being processed.
        # *   Deleting: The mount target is being deleted.
        # *   Hibernating: The mount target is being hibernated.
        # *   Hibernated: The mount target is hibernated.
        self.status = status
        # The tags that are attached to the mount target.
        self.tags = tags
        # The ID of the VPC.
        self.vpc_id = vpc_id
        # The ID of the vSwitch.
        self.vsw_id = vsw_id

    def validate(self):
        if self.client_master_nodes:
            self.client_master_nodes.validate()
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group_name is not None:
            result['AccessGroupName'] = self.access_group_name
        if self.client_master_nodes is not None:
            result['ClientMasterNodes'] = self.client_master_nodes.to_map()
        if self.dual_stack_mount_target_domain is not None:
            result['DualStackMountTargetDomain'] = self.dual_stack_mount_target_domain
        if self.mount_target_domain is not None:
            result['MountTargetDomain'] = self.mount_target_domain
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.status is not None:
            result['Status'] = self.status
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vsw_id is not None:
            result['VswId'] = self.vsw_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessGroupName') is not None:
            self.access_group_name = m.get('AccessGroupName')
        if m.get('ClientMasterNodes') is not None:
            temp_model = DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargetsMountTargetClientMasterNodes()
            self.client_master_nodes = temp_model.from_map(m['ClientMasterNodes'])
        if m.get('DualStackMountTargetDomain') is not None:
            self.dual_stack_mount_target_domain = m.get('DualStackMountTargetDomain')
        if m.get('MountTargetDomain') is not None:
            self.mount_target_domain = m.get('MountTargetDomain')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tags') is not None:
            temp_model = DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargetsMountTargetTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswId') is not None:
            self.vsw_id = m.get('VswId')
        return self


class DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargets(TeaModel):
    def __init__(
        self,
        mount_target: List[DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargetsMountTarget] = None,
    ):
        self.mount_target = mount_target

    def validate(self):
        if self.mount_target:
            for k in self.mount_target:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MountTarget'] = []
        if self.mount_target is not None:
            for k in self.mount_target:
                result['MountTarget'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.mount_target = []
        if m.get('MountTarget') is not None:
            for k in m.get('MountTarget'):
                temp_model = DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargetsMountTarget()
                self.mount_target.append(temp_model.from_map(k))
        return self


class DescribeFileSystemsResponseBodyFileSystemsFileSystemOptions(TeaModel):
    def __init__(
        self,
        enable_oplock: bool = None,
    ):
        # Specifies whether to enable the oplock feature. Valid values:
        # 
        # *   true: enables the feature.
        # *   false: disables the feature.
        # 
        # >  Only Server Message Block (SMB) file systems support this feature.
        self.enable_oplock = enable_oplock

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_oplock is not None:
            result['EnableOplock'] = self.enable_oplock
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableOplock') is not None:
            self.enable_oplock = m.get('EnableOplock')
        return self


class DescribeFileSystemsResponseBodyFileSystemsFileSystemPackagesPackage(TeaModel):
    def __init__(
        self,
        expired_time: str = None,
        package_id: str = None,
        package_type: str = None,
        size: int = None,
        start_time: str = None,
    ):
        # The end time of the validity period for the storage plan.
        self.expired_time = expired_time
        # The ID of the storage plan.
        self.package_id = package_id
        # The type of the storage plan.
        # 
        # Valid values:
        # - ssd: the storage plan for Performance NAS file systems.
        # - hybrid: the storage plan for Capacity NAS file systems.
        self.package_type = package_type
        # The capacity of the storage plan. Unit: bytes.
        self.size = size
        # The start time of the validity period for the storage plan.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.package_id is not None:
            result['PackageId'] = self.package_id
        if self.package_type is not None:
            result['PackageType'] = self.package_type
        if self.size is not None:
            result['Size'] = self.size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('PackageId') is not None:
            self.package_id = m.get('PackageId')
        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeFileSystemsResponseBodyFileSystemsFileSystemPackages(TeaModel):
    def __init__(
        self,
        package: List[DescribeFileSystemsResponseBodyFileSystemsFileSystemPackagesPackage] = None,
    ):
        self.package = package

    def validate(self):
        if self.package:
            for k in self.package:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Package'] = []
        if self.package is not None:
            for k in self.package:
                result['Package'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.package = []
        if m.get('Package') is not None:
            for k in m.get('Package'):
                temp_model = DescribeFileSystemsResponseBodyFileSystemsFileSystemPackagesPackage()
                self.package.append(temp_model.from_map(k))
        return self


class DescribeFileSystemsResponseBodyFileSystemsFileSystemSupportedFeatures(TeaModel):
    def __init__(
        self,
        supported_feature: List[str] = None,
    ):
        self.supported_feature = supported_feature

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.supported_feature is not None:
            result['SupportedFeature'] = self.supported_feature
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SupportedFeature') is not None:
            self.supported_feature = m.get('SupportedFeature')
        return self


class DescribeFileSystemsResponseBodyFileSystemsFileSystemTagsTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeFileSystemsResponseBodyFileSystemsFileSystemTags(TeaModel):
    def __init__(
        self,
        tag: List[DescribeFileSystemsResponseBodyFileSystemsFileSystemTagsTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeFileSystemsResponseBodyFileSystemsFileSystemTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeFileSystemsResponseBodyFileSystemsFileSystemVswIds(TeaModel):
    def __init__(
        self,
        vsw_id: List[str] = None,
    ):
        self.vsw_id = vsw_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vsw_id is not None:
            result['VswId'] = self.vsw_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VswId') is not None:
            self.vsw_id = m.get('VswId')
        return self


class DescribeFileSystemsResponseBodyFileSystemsFileSystem(TeaModel):
    def __init__(
        self,
        access_point_count: str = None,
        auto_snapshot_policy_id: str = None,
        bandwidth: int = None,
        capacity: int = None,
        charge_type: str = None,
        create_time: str = None,
        description: str = None,
        encrypt_type: int = None,
        expired_time: str = None,
        file_system_id: str = None,
        file_system_type: str = None,
        kmskey_id: str = None,
        ldap: DescribeFileSystemsResponseBodyFileSystemsFileSystemLdap = None,
        metered_archive_size: int = None,
        metered_iasize: int = None,
        metered_size: int = None,
        mount_targets: DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargets = None,
        options: DescribeFileSystemsResponseBodyFileSystemsFileSystemOptions = None,
        packages: DescribeFileSystemsResponseBodyFileSystemsFileSystemPackages = None,
        protocol_type: str = None,
        quorum_vsw_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        status: str = None,
        storage_type: str = None,
        supported_features: DescribeFileSystemsResponseBodyFileSystemsFileSystemSupportedFeatures = None,
        tags: DescribeFileSystemsResponseBodyFileSystemsFileSystemTags = None,
        version: str = None,
        vpc_id: str = None,
        vsc_target: str = None,
        vsw_ids: DescribeFileSystemsResponseBodyFileSystemsFileSystemVswIds = None,
        zone_id: str = None,
    ):
        # Number of access points.
        self.access_point_count = access_point_count
        # The ID of the automatic snapshot policy.
        self.auto_snapshot_policy_id = auto_snapshot_policy_id
        # The bandwidth of the file system.
        # 
        # Unit: MB/s. This parameter is unavailable for General-purpose NAS file systems.
        self.bandwidth = bandwidth
        # The capacity of the file system.
        # 
        # Unit: GiB.
        self.capacity = capacity
        # The billing method.
        # 
        # Valid values:
        # - Subscription: The subscription billing method is used.
        # - PayAsYouGo: The pay-as-you-go billing method is used.
        # - Package: A storage plan is attached to the file system.
        self.charge_type = charge_type
        # The time when the file system was created.
        self.create_time = create_time
        # The description of the file system.
        self.description = description
        # The encryption type.
        # 
        # Valid values:
        # 
        # *   0: The data in the file system is not encrypted.
        # *   1: A NAS-managed key is used to encrypt the data in the file system.
        # *   2: A KMS-managed key is used to encrypt the data in the file system.
        self.encrypt_type = encrypt_type
        # The time when the file system expires.
        self.expired_time = expired_time
        # The ID of the file system.
        self.file_system_id = file_system_id
        # The type of the file system.
        # 
        # Valid values:
        # - standard: General-purpose NAS file system
        # - extreme: Extreme NAS file system
        # - cpfs: CPFS file system
        # > CPFS file systems are available only on the China site (aliyun.com).
        self.file_system_type = file_system_type
        # The ID of the key that is managed by Key Management Service (KMS).
        self.kmskey_id = kmskey_id
        # The Lightweight Directory Access Protocol (LDAP) configurations.
        # 
        # This parameter is available only for CPFS file systems.
        self.ldap = ldap
        # Archive storage usage.
        # 
        # Unit: Byte.
        self.metered_archive_size = metered_archive_size
        # The storage usage of the Infrequent Access (IA) storage medium.
        # 
        # Unit: bytes.
        self.metered_iasize = metered_iasize
        # The storage usage of the file system.
        # 
        # The value of this parameter is the maximum storage usage of the file system over the last hour. Unit: bytes.
        self.metered_size = metered_size
        # The information about mount targets.
        self.mount_targets = mount_targets
        # The options.
        self.options = options
        # The information about storage plans.
        self.packages = packages
        # The protocol type of the file system.
        # 
        # Valid values:
        # 
        # *   NFS: Network File System (NFS)
        # *   SMB: Server Message Block (SMB)
        # *   cpfs: the protocol type supported by the CPFS file system
        # 
        # > CPFS file systems are available only on the China site (aliyun.com).
        self.protocol_type = protocol_type
        # The ID of the vSwitch.
        self.quorum_vsw_id = quorum_vsw_id
        # The region ID.
        self.region_id = region_id
        # The resource group ID.
        # 
        # You can log on to the [Resource Management console](https://resourcemanager.console.aliyun.com/resource-groups?) to view resource group IDs.
        self.resource_group_id = resource_group_id
        # The status of the file system. Valid values:
        # - Pending: The file system is being created or modified.
        # - Running: The file system is available. Before you create a mount target for the file system, make sure that the file system is in the Running state.
        # - Stopped: The file system is unavailable.
        # - Extending: The file system is being scaled up.
        # - Stopping: The file system is being stopped.
        # - Deleting: The file system is being deleted.
        self.status = status
        # The storage type.
        # 
        # Valid values:
        # - Valid values for General-purpose NAS file systems: Capacity,Premium and Performance.
        # - Valid values for Extreme NAS file systems: standard and advance.
        # - Valid values for CPFS file systems: advance_100 (100 MB/s/TiB baseline) and advance_200 (200 MB/s/TiB baseline).
        #  > CPFS file systems are available only on the China site (aliyun.com).
        self.storage_type = storage_type
        # The features that are supported by the file system.
        self.supported_features = supported_features
        # The tags that are attached to the file system.
        self.tags = tags
        # The version number of the file system.
        # 
        # This parameter is available only for Extreme NAS file systems and CPFS file systems.
        self.version = version
        # The ID of the virtual private cloud (VPC).
        self.vpc_id = vpc_id
        self.vsc_target = vsc_target
        # A collection of vSwitch IDs.
        self.vsw_ids = vsw_ids
        # The ID of the zone where the file system resides.
        self.zone_id = zone_id

    def validate(self):
        if self.ldap:
            self.ldap.validate()
        if self.mount_targets:
            self.mount_targets.validate()
        if self.options:
            self.options.validate()
        if self.packages:
            self.packages.validate()
        if self.supported_features:
            self.supported_features.validate()
        if self.tags:
            self.tags.validate()
        if self.vsw_ids:
            self.vsw_ids.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_point_count is not None:
            result['AccessPointCount'] = self.access_point_count
        if self.auto_snapshot_policy_id is not None:
            result['AutoSnapshotPolicyId'] = self.auto_snapshot_policy_id
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.encrypt_type is not None:
            result['EncryptType'] = self.encrypt_type
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type
        if self.kmskey_id is not None:
            result['KMSKeyId'] = self.kmskey_id
        if self.ldap is not None:
            result['Ldap'] = self.ldap.to_map()
        if self.metered_archive_size is not None:
            result['MeteredArchiveSize'] = self.metered_archive_size
        if self.metered_iasize is not None:
            result['MeteredIASize'] = self.metered_iasize
        if self.metered_size is not None:
            result['MeteredSize'] = self.metered_size
        if self.mount_targets is not None:
            result['MountTargets'] = self.mount_targets.to_map()
        if self.options is not None:
            result['Options'] = self.options.to_map()
        if self.packages is not None:
            result['Packages'] = self.packages.to_map()
        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type
        if self.quorum_vsw_id is not None:
            result['QuorumVswId'] = self.quorum_vsw_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.status is not None:
            result['Status'] = self.status
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.supported_features is not None:
            result['SupportedFeatures'] = self.supported_features.to_map()
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.version is not None:
            result['Version'] = self.version
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vsc_target is not None:
            result['VscTarget'] = self.vsc_target
        if self.vsw_ids is not None:
            result['VswIds'] = self.vsw_ids.to_map()
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessPointCount') is not None:
            self.access_point_count = m.get('AccessPointCount')
        if m.get('AutoSnapshotPolicyId') is not None:
            self.auto_snapshot_policy_id = m.get('AutoSnapshotPolicyId')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EncryptType') is not None:
            self.encrypt_type = m.get('EncryptType')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')
        if m.get('KMSKeyId') is not None:
            self.kmskey_id = m.get('KMSKeyId')
        if m.get('Ldap') is not None:
            temp_model = DescribeFileSystemsResponseBodyFileSystemsFileSystemLdap()
            self.ldap = temp_model.from_map(m['Ldap'])
        if m.get('MeteredArchiveSize') is not None:
            self.metered_archive_size = m.get('MeteredArchiveSize')
        if m.get('MeteredIASize') is not None:
            self.metered_iasize = m.get('MeteredIASize')
        if m.get('MeteredSize') is not None:
            self.metered_size = m.get('MeteredSize')
        if m.get('MountTargets') is not None:
            temp_model = DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargets()
            self.mount_targets = temp_model.from_map(m['MountTargets'])
        if m.get('Options') is not None:
            temp_model = DescribeFileSystemsResponseBodyFileSystemsFileSystemOptions()
            self.options = temp_model.from_map(m['Options'])
        if m.get('Packages') is not None:
            temp_model = DescribeFileSystemsResponseBodyFileSystemsFileSystemPackages()
            self.packages = temp_model.from_map(m['Packages'])
        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')
        if m.get('QuorumVswId') is not None:
            self.quorum_vsw_id = m.get('QuorumVswId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('SupportedFeatures') is not None:
            temp_model = DescribeFileSystemsResponseBodyFileSystemsFileSystemSupportedFeatures()
            self.supported_features = temp_model.from_map(m['SupportedFeatures'])
        if m.get('Tags') is not None:
            temp_model = DescribeFileSystemsResponseBodyFileSystemsFileSystemTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VscTarget') is not None:
            self.vsc_target = m.get('VscTarget')
        if m.get('VswIds') is not None:
            temp_model = DescribeFileSystemsResponseBodyFileSystemsFileSystemVswIds()
            self.vsw_ids = temp_model.from_map(m['VswIds'])
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeFileSystemsResponseBodyFileSystems(TeaModel):
    def __init__(
        self,
        file_system: List[DescribeFileSystemsResponseBodyFileSystemsFileSystem] = None,
    ):
        self.file_system = file_system

    def validate(self):
        if self.file_system:
            for k in self.file_system:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FileSystem'] = []
        if self.file_system is not None:
            for k in self.file_system:
                result['FileSystem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.file_system = []
        if m.get('FileSystem') is not None:
            for k in m.get('FileSystem'):
                temp_model = DescribeFileSystemsResponseBodyFileSystemsFileSystem()
                self.file_system.append(temp_model.from_map(k))
        return self


class DescribeFileSystemsResponseBody(TeaModel):
    def __init__(
        self,
        file_systems: DescribeFileSystemsResponseBodyFileSystems = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The queried file systems.
        self.file_systems = file_systems
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of file systems.
        self.total_count = total_count

    def validate(self):
        if self.file_systems:
            self.file_systems.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_systems is not None:
            result['FileSystems'] = self.file_systems.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystems') is not None:
            temp_model = DescribeFileSystemsResponseBodyFileSystems()
            self.file_systems = temp_model.from_map(m['FileSystems'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeFileSystemsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeFileSystemsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeFileSystemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFilesetsRequestFilters(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The filter name. Valid values:
        # 
        # *   FsetIds: filters filesets by fileset ID.
        # *   FileSystemPath: filters filesets based on the path of a fileset in a CPFS file system.
        # *   Description: filters filesets based on the fileset description.
        # *   QuotaExists: filters filesets based on whether quotas exist.
        # 
        # >  Only CPFS for LINGJUN V2.7.0 and later support the QuotaExists parameter.
        self.key = key
        # The filter value. This parameter does not support wildcards.
        # 
        # *   If Key is set to FsetIds, set Value to a fileset ID or a part of the fileset ID. You can specify a fileset ID or a group of fileset IDs. You can specify a maximum of 10 fileset IDs. Example: `fset-1902718ea0ae****` or `fset-1902718ea0ae****,fset-3212718ea0ae****`.
        # *   If Key is set to FileSystemPath, set Value to the path or a part of the path of a fileset in a CPFS file system. The value must be 2 to 1024 characters in length. The value must be encoded in UTF-8.
        # *   If Key is set to Description, set Value to a fileset description or a part of the fileset description.
        # *   If Key is set to QuotaExists, set Value to true or false. If you do not specify the parameter, all filesets are returned.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeFilesetsRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        filters: List[DescribeFilesetsRequestFilters] = None,
        max_results: int = None,
        next_token: str = None,
        order_by_field: str = None,
        sort_order: str = None,
    ):
        # The ID of the file system.
        # 
        # *   The IDs of CPFS file systems must start with `cpfs-`. Example: cpfs-099394bd928c\\*\\*\\*\\*.
        # *   The IDs of CPFS for LINGJUN file systems must start with `bmcpfs-`. Example: bmcpfs-290w65p03ok64ya\\*\\*\\*\\*.
        # 
        # >  CPFS is not supported on the international site.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The filter that is used to query filesets.
        self.filters = filters
        # The number of results for each query.
        # 
        # Valid values: 10 to 100. Default value: 20.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token
        # The condition by which the results are sorted. Valid values:
        # 
        # *   FileCountLimit: the file quantity quota
        # *   SizeLimit: the capacity quota
        # *   FileCountUsage: the usage of the file quantity quota
        # *   SpaceUsage: the capacity usage
        self.order_by_field = order_by_field
        # The order in which you want to sort the results. Valid values:
        # 
        # *   asc (default): ascending order
        # *   desc: descending order
        # 
        # >  This parameter takes effect only if you specify the OrderByField parameter.
        self.sort_order = sort_order

    def validate(self):
        if self.filters:
            for k in self.filters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        result['Filters'] = []
        if self.filters is not None:
            for k in self.filters:
                result['Filters'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order_by_field is not None:
            result['OrderByField'] = self.order_by_field
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        self.filters = []
        if m.get('Filters') is not None:
            for k in m.get('Filters'):
                temp_model = DescribeFilesetsRequestFilters()
                self.filters.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OrderByField') is not None:
            self.order_by_field = m.get('OrderByField')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        return self


class DescribeFilesetsResponseBodyEntriesEntrieQuota(TeaModel):
    def __init__(
        self,
        file_count_limit: int = None,
        size_limit: int = None,
    ):
        # The file quantity quota. Valid values:
        # 
        # *   Minimum value: 10000.
        # *   Maximum value: 10000000000.
        self.file_count_limit = file_count_limit
        # The capacity quota. Unit: bytes.
        # 
        # *   Minimum value: 10737418240 (10 GiB).
        # *   Step size: 1073741824 (1 GiB).
        self.size_limit = size_limit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_count_limit is not None:
            result['FileCountLimit'] = self.file_count_limit
        if self.size_limit is not None:
            result['SizeLimit'] = self.size_limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileCountLimit') is not None:
            self.file_count_limit = m.get('FileCountLimit')
        if m.get('SizeLimit') is not None:
            self.size_limit = m.get('SizeLimit')
        return self


class DescribeFilesetsResponseBodyEntriesEntrie(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        deletion_protection: bool = None,
        description: str = None,
        file_count_usage: int = None,
        file_system_id: str = None,
        file_system_path: str = None,
        fset_id: str = None,
        quota: DescribeFilesetsResponseBodyEntriesEntrieQuota = None,
        space_usage: int = None,
        status: str = None,
        update_time: str = None,
    ):
        # The time when the fileset was created.
        # 
        # The time follows the ISO 8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format.
        self.create_time = create_time
        # Specifies whether to enable deletion protection to allow you to release the fileset by using the console or by calling the [DeleteFileset](https://help.aliyun.com/document_detail/2838077.html) operation. Valid values:
        # 
        # *   true
        # *   false
        # 
        # >  This parameter can protect filesets only against manual releases, but not against automatic releases.
        self.deletion_protection = deletion_protection
        # The fileset description.
        self.description = description
        # The usage of the file quantity.
        # 
        # >  Only CPFS for LINGJUN V2.7.0 and later support this parameter.
        self.file_count_usage = file_count_usage
        # The ID of the file system.
        # 
        # *   The IDs of CPFS file systems must start with `cpfs-`. Example: cpfs-099394bd928c\\*\\*\\*\\*.
        # *   The IDs of CPFS for LINGJUN file systems must start with `bmcpfs-`. Example: bmcpfs-290w65p03ok64ya\\*\\*\\*\\*.
        # 
        # >  CPFS is not supported on the international site.
        self.file_system_id = file_system_id
        # The fileset path.
        self.file_system_path = file_system_path
        # The fileset ID.
        self.fset_id = fset_id
        # The quota information.
        # 
        # >  Only CPFS for Lingjun V2.7.0 and later support this parameter.
        self.quota = quota
        # The capacity usage. Unit: bytes.
        # 
        # >  Only CPFS for LINGJUN V2.7.0 and later support this parameter.
        self.space_usage = space_usage
        # The fileset status. Valid values:
        # 
        # *   CREATING: The fileset is being created.
        # *   CREATED: The fileset has been created and is running properly.
        # *   RELEASING: The fileset is being released.
        # *   RELEASED: The fileset has been deleted.
        self.status = status
        # The time when the fileset was last updated.
        # 
        # The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format.
        self.update_time = update_time

    def validate(self):
        if self.quota:
            self.quota.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deletion_protection is not None:
            result['DeletionProtection'] = self.deletion_protection
        if self.description is not None:
            result['Description'] = self.description
        if self.file_count_usage is not None:
            result['FileCountUsage'] = self.file_count_usage
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.file_system_path is not None:
            result['FileSystemPath'] = self.file_system_path
        if self.fset_id is not None:
            result['FsetId'] = self.fset_id
        if self.quota is not None:
            result['Quota'] = self.quota.to_map()
        if self.space_usage is not None:
            result['SpaceUsage'] = self.space_usage
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DeletionProtection') is not None:
            self.deletion_protection = m.get('DeletionProtection')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FileCountUsage') is not None:
            self.file_count_usage = m.get('FileCountUsage')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('FileSystemPath') is not None:
            self.file_system_path = m.get('FileSystemPath')
        if m.get('FsetId') is not None:
            self.fset_id = m.get('FsetId')
        if m.get('Quota') is not None:
            temp_model = DescribeFilesetsResponseBodyEntriesEntrieQuota()
            self.quota = temp_model.from_map(m['Quota'])
        if m.get('SpaceUsage') is not None:
            self.space_usage = m.get('SpaceUsage')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class DescribeFilesetsResponseBodyEntries(TeaModel):
    def __init__(
        self,
        entrie: List[DescribeFilesetsResponseBodyEntriesEntrie] = None,
    ):
        self.entrie = entrie

    def validate(self):
        if self.entrie:
            for k in self.entrie:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Entrie'] = []
        if self.entrie is not None:
            for k in self.entrie:
                result['Entrie'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.entrie = []
        if m.get('Entrie') is not None:
            for k in m.get('Entrie'):
                temp_model = DescribeFilesetsResponseBodyEntriesEntrie()
                self.entrie.append(temp_model.from_map(k))
        return self


class DescribeFilesetsResponseBody(TeaModel):
    def __init__(
        self,
        entries: DescribeFilesetsResponseBodyEntries = None,
        file_system_id: str = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The fileset information.
        self.entries = entries
        # The ID of the file system.
        # 
        # *   The IDs of CPFS file systems must start with `cpfs-`. Example: cpfs-099394bd928c\\*\\*\\*\\*.
        # *   The IDs of CPFS for LINGJUN file systems must start with `bmcpfs-`. Example: bmcpfs-290w65p03ok64ya\\*\\*\\*\\*.
        # 
        # >  CPFS is not supported on the international site.
        self.file_system_id = file_system_id
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.entries:
            self.entries.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entries is not None:
            result['Entries'] = self.entries.to_map()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Entries') is not None:
            temp_model = DescribeFilesetsResponseBodyEntries()
            self.entries = temp_model.from_map(m['Entries'])
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeFilesetsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeFilesetsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeFilesetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLifecyclePoliciesRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        lifecycle_policy_name: str = None,
        page_number: int = None,
        page_size: int = None,
        storage_type: str = None,
    ):
        # The ID of the file system.
        self.file_system_id = file_system_id
        # The name of the lifecycle policy. The name must meet the following conventions:
        # 
        # The name must be 3 to 64 characters in length and must start with a letter. It can contain letters, digits, underscores (_), and hyphens (-).
        self.lifecycle_policy_name = lifecycle_policy_name
        # The page number.
        # 
        # Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 10.
        self.page_size = page_size
        # The storage class.
        # 
        # *   InfrequentAccess: the Infrequent Access (IA) storage class.
        # *   Archive: the Archive storage class.
        # 
        # >  If the StorageType parameter is not specified, data retrieval tasks of all types are returned.
        self.storage_type = storage_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.lifecycle_policy_name is not None:
            result['LifecyclePolicyName'] = self.lifecycle_policy_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('LifecyclePolicyName') is not None:
            self.lifecycle_policy_name = m.get('LifecyclePolicyName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        return self


class DescribeLifecyclePoliciesResponseBodyLifecyclePolicies(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        file_system_id: str = None,
        lifecycle_policy_name: str = None,
        lifecycle_rule_name: str = None,
        path: str = None,
        paths: List[str] = None,
        storage_type: str = None,
    ):
        # The time when the lifecycle policy was created.
        # 
        # The time follows the ISO 8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format.
        self.create_time = create_time
        # The ID of the file system.
        self.file_system_id = file_system_id
        # The name of the lifecycle policy.
        self.lifecycle_policy_name = lifecycle_policy_name
        # The management rule that is associated with the lifecycle policy.
        # 
        # Valid values:
        # 
        # *   DEFAULT_ATIME_14: Files that are not accessed in the last 14 days are dumped to the IA storage medium.
        # *   DEFAULT_ATIME_30: Files that are not accessed in the last 30 days are dumped to the IA storage medium.
        # *   DEFAULT_ATIME_60: Files that are not accessed in the last 60 days are dumped to the IA storage medium.
        # *   DEFAULT_ATIME_90: Files that are not accessed in the last 90 days are dumped to the IA storage medium.
        self.lifecycle_rule_name = lifecycle_rule_name
        # The absolute path of a directory with which the lifecycle policy is associated.
        self.path = path
        # The absolute paths to multiple directories associated with the lifecycle policy.
        self.paths = paths
        # The storage type of the data that is dumped to the IA storage medium.
        # 
        # Default value: InfrequentAccess (IA).
        self.storage_type = storage_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.lifecycle_policy_name is not None:
            result['LifecyclePolicyName'] = self.lifecycle_policy_name
        if self.lifecycle_rule_name is not None:
            result['LifecycleRuleName'] = self.lifecycle_rule_name
        if self.path is not None:
            result['Path'] = self.path
        if self.paths is not None:
            result['Paths'] = self.paths
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('LifecyclePolicyName') is not None:
            self.lifecycle_policy_name = m.get('LifecyclePolicyName')
        if m.get('LifecycleRuleName') is not None:
            self.lifecycle_rule_name = m.get('LifecycleRuleName')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Paths') is not None:
            self.paths = m.get('Paths')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        return self


class DescribeLifecyclePoliciesResponseBody(TeaModel):
    def __init__(
        self,
        lifecycle_policies: List[DescribeLifecyclePoliciesResponseBodyLifecyclePolicies] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The queried lifecycle policies.
        self.lifecycle_policies = lifecycle_policies
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of lifecycle policies.
        self.total_count = total_count

    def validate(self):
        if self.lifecycle_policies:
            for k in self.lifecycle_policies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LifecyclePolicies'] = []
        if self.lifecycle_policies is not None:
            for k in self.lifecycle_policies:
                result['LifecyclePolicies'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.lifecycle_policies = []
        if m.get('LifecyclePolicies') is not None:
            for k in m.get('LifecyclePolicies'):
                temp_model = DescribeLifecyclePoliciesResponseBodyLifecyclePolicies()
                self.lifecycle_policies.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeLifecyclePoliciesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeLifecyclePoliciesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeLifecyclePoliciesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLogAnalysisRequest(TeaModel):
    def __init__(
        self,
        file_system_type: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
    ):
        # The type of the file system.
        # 
        # Valid values:
        # 
        # *   standard: General-purpose NAS file system
        # *   extreme: Extreme NAS file system
        # *   all (default): all types
        self.file_system_type = file_system_type
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 100. Default value: 10.
        self.page_size = page_size
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeLogAnalysisResponseBodyAnalysesAnalysisMetaValue(TeaModel):
    def __init__(
        self,
        logstore: str = None,
        project: str = None,
        region: str = None,
        role_arn: str = None,
    ):
        # The name of the dedicated Logstore that is used to store NAS operation logs.
        self.logstore = logstore
        # The name of the project where the dedicated Logstore resides.
        self.project = project
        # The region where the dedicated Logstore resides.
        self.region = region
        # The role that is used by NAS to access Simple Log Service.
        self.role_arn = role_arn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logstore is not None:
            result['Logstore'] = self.logstore
        if self.project is not None:
            result['Project'] = self.project
        if self.region is not None:
            result['Region'] = self.region
        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Logstore') is not None:
            self.logstore = m.get('Logstore')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')
        return self


class DescribeLogAnalysisResponseBodyAnalysesAnalysis(TeaModel):
    def __init__(
        self,
        meta_key: str = None,
        meta_value: DescribeLogAnalysisResponseBodyAnalysesAnalysisMetaValue = None,
    ):
        # The ID of the file system.
        self.meta_key = meta_key
        # The log dump information of the file system.
        self.meta_value = meta_value

    def validate(self):
        if self.meta_value:
            self.meta_value.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.meta_key is not None:
            result['MetaKey'] = self.meta_key
        if self.meta_value is not None:
            result['MetaValue'] = self.meta_value.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MetaKey') is not None:
            self.meta_key = m.get('MetaKey')
        if m.get('MetaValue') is not None:
            temp_model = DescribeLogAnalysisResponseBodyAnalysesAnalysisMetaValue()
            self.meta_value = temp_model.from_map(m['MetaValue'])
        return self


class DescribeLogAnalysisResponseBodyAnalyses(TeaModel):
    def __init__(
        self,
        analysis: List[DescribeLogAnalysisResponseBodyAnalysesAnalysis] = None,
    ):
        self.analysis = analysis

    def validate(self):
        if self.analysis:
            for k in self.analysis:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Analysis'] = []
        if self.analysis is not None:
            for k in self.analysis:
                result['Analysis'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.analysis = []
        if m.get('Analysis') is not None:
            for k in m.get('Analysis'):
                temp_model = DescribeLogAnalysisResponseBodyAnalysesAnalysis()
                self.analysis.append(temp_model.from_map(k))
        return self


class DescribeLogAnalysisResponseBody(TeaModel):
    def __init__(
        self,
        analyses: DescribeLogAnalysisResponseBodyAnalyses = None,
        code: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The collection of log dump information.
        self.analyses = analyses
        # The HTTP status code.
        self.code = code
        # The page number.
        self.page_number = page_number
        # The number of log dump entries returned per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of log dump entries in the region.
        self.total_count = total_count

    def validate(self):
        if self.analyses:
            self.analyses.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.analyses is not None:
            result['Analyses'] = self.analyses.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Analyses') is not None:
            temp_model = DescribeLogAnalysisResponseBodyAnalyses()
            self.analyses = temp_model.from_map(m['Analyses'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeLogAnalysisResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeLogAnalysisResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeLogAnalysisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMountTargetsRequest(TeaModel):
    def __init__(
        self,
        dual_stack_mount_target_domain: str = None,
        file_system_id: str = None,
        mount_target_domain: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The dual-stack (IPv4 and IPv6) domain name of the mount target.
        # 
        # > Only Extreme NAS file systems that reside in the Chinese mainland support IPv6.
        self.dual_stack_mount_target_domain = dual_stack_mount_target_domain
        # The ID of the file system.
        # 
        # *   Sample ID of a General-purpose NAS file system: 31a8e4\\*\\*\\*\\*.
        # *   The IDs of Extreme NAS file systems must start with `extreme-`, for example, extreme-0015\\*\\*\\*\\*.
        # *   The IDs of Cloud Parallel File Storage (CPFS) file systems must start with `cpfs-`, for example, cpfs-125487\\*\\*\\*\\*.
        # 
        # > CPFS file systems are available only on the China site (aliyun.com).
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The domain name of the mount target.
        self.mount_target_domain = mount_target_domain
        # The page number.
        # 
        # Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 10.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dual_stack_mount_target_domain is not None:
            result['DualStackMountTargetDomain'] = self.dual_stack_mount_target_domain
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.mount_target_domain is not None:
            result['MountTargetDomain'] = self.mount_target_domain
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DualStackMountTargetDomain') is not None:
            self.dual_stack_mount_target_domain = m.get('DualStackMountTargetDomain')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('MountTargetDomain') is not None:
            self.mount_target_domain = m.get('MountTargetDomain')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeMountTargetsResponseBodyMountTargetsMountTargetClientMasterNodesClientMasterNode(TeaModel):
    def __init__(
        self,
        default_passwd: str = None,
        ecs_id: str = None,
        ecs_ip: str = None,
    ):
        # The default logon password of the ECS instance.
        self.default_passwd = default_passwd
        # The ID of the ECS instance on the client management node.
        self.ecs_id = ecs_id
        # The IP address of the ECS instance on the client management node.
        self.ecs_ip = ecs_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_passwd is not None:
            result['DefaultPasswd'] = self.default_passwd
        if self.ecs_id is not None:
            result['EcsId'] = self.ecs_id
        if self.ecs_ip is not None:
            result['EcsIp'] = self.ecs_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultPasswd') is not None:
            self.default_passwd = m.get('DefaultPasswd')
        if m.get('EcsId') is not None:
            self.ecs_id = m.get('EcsId')
        if m.get('EcsIp') is not None:
            self.ecs_ip = m.get('EcsIp')
        return self


class DescribeMountTargetsResponseBodyMountTargetsMountTargetClientMasterNodes(TeaModel):
    def __init__(
        self,
        client_master_node: List[DescribeMountTargetsResponseBodyMountTargetsMountTargetClientMasterNodesClientMasterNode] = None,
    ):
        self.client_master_node = client_master_node

    def validate(self):
        if self.client_master_node:
            for k in self.client_master_node:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ClientMasterNode'] = []
        if self.client_master_node is not None:
            for k in self.client_master_node:
                result['ClientMasterNode'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.client_master_node = []
        if m.get('ClientMasterNode') is not None:
            for k in m.get('ClientMasterNode'):
                temp_model = DescribeMountTargetsResponseBodyMountTargetsMountTargetClientMasterNodesClientMasterNode()
                self.client_master_node.append(temp_model.from_map(k))
        return self


class DescribeMountTargetsResponseBodyMountTargetsMountTargetTagsTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. Limits:
        # 
        # *   The tag key cannot be null or an empty string.
        # *   The tag key can be up to 128 characters in length.
        # *   The key value cannot start with aliyun or acs:.
        # *   The key value cannot contain http:// or https://.
        self.key = key
        # The tag value.
        # 
        # Limits:
        # 
        # *   The tag value can be up to 128 characters in length.
        # *   The tag value cannot contain http:// or https://.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeMountTargetsResponseBodyMountTargetsMountTargetTags(TeaModel):
    def __init__(
        self,
        tag: List[DescribeMountTargetsResponseBodyMountTargetsMountTargetTagsTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeMountTargetsResponseBodyMountTargetsMountTargetTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeMountTargetsResponseBodyMountTargetsMountTarget(TeaModel):
    def __init__(
        self,
        access_group: str = None,
        client_master_nodes: DescribeMountTargetsResponseBodyMountTargetsMountTargetClientMasterNodes = None,
        dual_stack_mount_target_domain: str = None,
        ipversion: str = None,
        mount_target_domain: str = None,
        network_type: str = None,
        status: str = None,
        tags: DescribeMountTargetsResponseBodyMountTargetsMountTargetTags = None,
        vpc_id: str = None,
        vsw_id: str = None,
    ):
        # The name of the permission group that is attached to the mount target.
        self.access_group = access_group
        # The information about client management nodes.
        self.client_master_nodes = client_master_nodes
        # The dual-stack (IPv4 and IPv6) domain name of the mount target.
        self.dual_stack_mount_target_domain = dual_stack_mount_target_domain
        # The type of the mount target.
        # 
        # *   IPv4: an IPv4 mount target
        # *   DualStack: a dual-stack mount target
        self.ipversion = ipversion
        # The IPv4 domain name of the mount target.
        self.mount_target_domain = mount_target_domain
        # The network type. Valid value: **Vpc**.
        self.network_type = network_type
        # The status of the mount target.
        # 
        # Valid values:
        # 
        # *   Active: The mount target is available.
        # *   Inactive: The mount target is unavailable.
        # *   Pending: The mount target is being created or modified.
        # *   Deleting: The mount target is being deleted.
        # *   Hibernating: The mount target is being hibernated.
        # *   Hibernated: The mount target is hibernated.
        # 
        # > You can mount a file system only when the mount target of the file system is in the Active state.
        self.status = status
        # An array of tags. The array may contain up to 20 tags. If the array contains multiple tags, each tag key is unique.
        self.tags = tags
        # The ID of the virtual private cloud (VPC).
        self.vpc_id = vpc_id
        # The ID of the vSwitch.
        self.vsw_id = vsw_id

    def validate(self):
        if self.client_master_nodes:
            self.client_master_nodes.validate()
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group is not None:
            result['AccessGroup'] = self.access_group
        if self.client_master_nodes is not None:
            result['ClientMasterNodes'] = self.client_master_nodes.to_map()
        if self.dual_stack_mount_target_domain is not None:
            result['DualStackMountTargetDomain'] = self.dual_stack_mount_target_domain
        if self.ipversion is not None:
            result['IPVersion'] = self.ipversion
        if self.mount_target_domain is not None:
            result['MountTargetDomain'] = self.mount_target_domain
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.status is not None:
            result['Status'] = self.status
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vsw_id is not None:
            result['VswId'] = self.vsw_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessGroup') is not None:
            self.access_group = m.get('AccessGroup')
        if m.get('ClientMasterNodes') is not None:
            temp_model = DescribeMountTargetsResponseBodyMountTargetsMountTargetClientMasterNodes()
            self.client_master_nodes = temp_model.from_map(m['ClientMasterNodes'])
        if m.get('DualStackMountTargetDomain') is not None:
            self.dual_stack_mount_target_domain = m.get('DualStackMountTargetDomain')
        if m.get('IPVersion') is not None:
            self.ipversion = m.get('IPVersion')
        if m.get('MountTargetDomain') is not None:
            self.mount_target_domain = m.get('MountTargetDomain')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tags') is not None:
            temp_model = DescribeMountTargetsResponseBodyMountTargetsMountTargetTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswId') is not None:
            self.vsw_id = m.get('VswId')
        return self


class DescribeMountTargetsResponseBodyMountTargets(TeaModel):
    def __init__(
        self,
        mount_target: List[DescribeMountTargetsResponseBodyMountTargetsMountTarget] = None,
    ):
        self.mount_target = mount_target

    def validate(self):
        if self.mount_target:
            for k in self.mount_target:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MountTarget'] = []
        if self.mount_target is not None:
            for k in self.mount_target:
                result['MountTarget'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.mount_target = []
        if m.get('MountTarget') is not None:
            for k in m.get('MountTarget'):
                temp_model = DescribeMountTargetsResponseBodyMountTargetsMountTarget()
                self.mount_target.append(temp_model.from_map(k))
        return self


class DescribeMountTargetsResponseBody(TeaModel):
    def __init__(
        self,
        mount_targets: DescribeMountTargetsResponseBodyMountTargets = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The queried mount targets.
        self.mount_targets = mount_targets
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of mount targets.
        self.total_count = total_count

    def validate(self):
        if self.mount_targets:
            self.mount_targets.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mount_targets is not None:
            result['MountTargets'] = self.mount_targets.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MountTargets') is not None:
            temp_model = DescribeMountTargetsResponseBodyMountTargets()
            self.mount_targets = temp_model.from_map(m['MountTargets'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeMountTargetsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeMountTargetsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeMountTargetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMountedClientsRequest(TeaModel):
    def __init__(
        self,
        client_ip: str = None,
        file_system_id: str = None,
        mount_target_domain: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
    ):
        # The IP address of the client.
        # 
        # *   If you specify an IP address, the operation checks whether the client list includes this IP address. If the client list includes the IP address, the operation returns the IP address. If the client list does not include the IP address, the operation returns an empty list.
        # *   If you do not specify an IP address, the operation returns the IP addresses of all clients that have accessed the specified NAS file system within the last minute.
        self.client_ip = client_ip
        # The ID of the file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The domain name of the mount target.
        # 
        # This parameter is required.
        self.mount_target_domain = mount_target_domain
        # The page number.
        # 
        # Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of IP addresses to return on each page.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 10.
        self.page_size = page_size
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_ip is not None:
            result['ClientIP'] = self.client_ip
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.mount_target_domain is not None:
            result['MountTargetDomain'] = self.mount_target_domain
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientIP') is not None:
            self.client_ip = m.get('ClientIP')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('MountTargetDomain') is not None:
            self.mount_target_domain = m.get('MountTargetDomain')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeMountedClientsResponseBodyClientsClient(TeaModel):
    def __init__(
        self,
        client_ip: str = None,
    ):
        # The IP address of the client.
        self.client_ip = client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_ip is not None:
            result['ClientIP'] = self.client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientIP') is not None:
            self.client_ip = m.get('ClientIP')
        return self


class DescribeMountedClientsResponseBodyClients(TeaModel):
    def __init__(
        self,
        client: List[DescribeMountedClientsResponseBodyClientsClient] = None,
    ):
        self.client = client

    def validate(self):
        if self.client:
            for k in self.client:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Client'] = []
        if self.client is not None:
            for k in self.client:
                result['Client'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.client = []
        if m.get('Client') is not None:
            for k in m.get('Client'):
                temp_model = DescribeMountedClientsResponseBodyClientsClient()
                self.client.append(temp_model.from_map(k))
        return self


class DescribeMountedClientsResponseBody(TeaModel):
    def __init__(
        self,
        clients: DescribeMountedClientsResponseBodyClients = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The queried clients.
        self.clients = clients
        # The page number.
        self.page_number = page_number
        # The number of IP addresses returned per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of IP addresses.
        self.total_count = total_count

    def validate(self):
        if self.clients:
            self.clients.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.clients is not None:
            result['Clients'] = self.clients.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Clients') is not None:
            temp_model = DescribeMountedClientsResponseBodyClients()
            self.clients = temp_model.from_map(m['Clients'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeMountedClientsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeMountedClientsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeMountedClientsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNfsAclRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
    ):
        # The ID of the file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        return self


class DescribeNfsAclResponseBodyAcl(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
    ):
        # Indicates whether the NFS ACL feature is enabled.
        # 
        # *   true: The NFS ACL feature is enabled.
        # *   false: The NFS ACL feature is disabled.
        self.enabled = enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        return self


class DescribeNfsAclResponseBody(TeaModel):
    def __init__(
        self,
        acl: DescribeNfsAclResponseBodyAcl = None,
        request_id: str = None,
    ):
        # The information about the ACL feature.
        self.acl = acl
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.acl:
            self.acl.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl is not None:
            result['Acl'] = self.acl.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Acl') is not None:
            temp_model = DescribeNfsAclResponseBodyAcl()
            self.acl = temp_model.from_map(m['Acl'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeNfsAclResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeNfsAclResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeNfsAclResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeProtocolMountTargetRequestFilters(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The filter name.
        # 
        # *   ProtocolServiceIds: filters export directories by protocol service ID.
        # *   ExportIds: filters export directories by export directory ID.
        # *   VpcIds: filters export directories by virtual private cloud (VPC) ID.
        # *   VSwitchIds: filters export directories by vSwitch ID.
        # *   FsetIds: filters export directories by fileset ID.
        # *   Paths: filters export directories based on the path of the file system corresponding to the mount target.
        # *   AccessGroupNames: filters export directories by permission group name.
        self.key = key
        # The filter value. This parameter does not support wildcards.
        # 
        # *   If Key is set to ProtocolServiceIds, set Value to a protocol service ID. You can specify a maximum of 10 protocol service IDs. Example: `ptc-12345678` or `ptc-12345678,ptc-12345679`.
        # *   If Key is set to ExportIds, set Value to an export directory ID. You can specify a maximum of 10 export directory IDs. Example: `exp-12345678` or `exp-12345678,exp-12345679`.
        # *   If Key is set to VpcIds, set Value to a VPC ID of the protocol service. You can specify a maximum of 10 VPC IDs. Example: `vpc-12345678` or `vpc-12345678,vpc-12345679`.
        # *   If Key is set to FsetIds, set Value to a fileset ID. You can specify a maximum of 10 fileset IDs. Example: `fset-12345678` or `fset-12345678,fset-12345679`.
        # *   If Key is set to Paths, set Value to a path of the file system corresponding to the mount target. You can specify a maximum of 10 paths. Example: `/cpfs/mnt_1/` or `/cpfs/mnt_1/,/cpfs/mnt_2/`.
        # *   If Key is set to AccessGroupNames, set Value to a permission group name for the protocol service. You can specify a maximum of 10 permission group names. Example: `ag-12345678` or `ag-12345678,ag-12345679`.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeProtocolMountTargetRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        file_system_id: str = None,
        filters: List[DescribeProtocolMountTargetRequestFilters] = None,
        max_results: int = None,
        next_token: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.
        # 
        # The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How do I ensure the idempotence?](https://help.aliyun.com/document_detail/25693.html)
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token
        # The ID of the file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The filter that is used to query the export directories of the protocol service.
        self.filters = filters
        # The number of results for each query.
        # 
        # *   Value values: 10 to 100.
        # *   Default value: 20.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token

    def validate(self):
        if self.filters:
            for k in self.filters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        result['Filters'] = []
        if self.filters is not None:
            for k in self.filters:
                result['Filters'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        self.filters = []
        if m.get('Filters') is not None:
            for k in m.get('Filters'):
                temp_model = DescribeProtocolMountTargetRequestFilters()
                self.filters.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class DescribeProtocolMountTargetResponseBodyProtocolMountTargets(TeaModel):
    def __init__(
        self,
        access_group_name: str = None,
        create_time: str = None,
        description: str = None,
        export_id: str = None,
        fset_id: str = None,
        path: str = None,
        protocol_mount_target_domain: str = None,
        protocol_service_id: str = None,
        protocol_type: str = None,
        status: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # The permission group that is associated with the export directory of the protocol service.
        self.access_group_name = access_group_name
        # The time when the export directory of the protocol service was created.
        self.create_time = create_time
        # The description of the export directory for the protocol service.
        self.description = description
        # The ID of the export directory for the protocol service.
        self.export_id = export_id
        # The fileset ID of the export directory for the protocol service.
        self.fset_id = fset_id
        # The export directory of the protocol service.
        self.path = path
        # The domain name of the export directory for the protocol service.
        self.protocol_mount_target_domain = protocol_mount_target_domain
        # The ID of the protocol service.
        self.protocol_service_id = protocol_service_id
        # The protocol type supported by the protocol service.
        self.protocol_type = protocol_type
        # The status of the mount target.
        self.status = status
        # The vSwitch ID of the export directory for the protocol service.
        self.v_switch_id = v_switch_id
        # The VPC ID of the export directory for the protocol service.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group_name is not None:
            result['AccessGroupName'] = self.access_group_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.export_id is not None:
            result['ExportId'] = self.export_id
        if self.fset_id is not None:
            result['FsetId'] = self.fset_id
        if self.path is not None:
            result['Path'] = self.path
        if self.protocol_mount_target_domain is not None:
            result['ProtocolMountTargetDomain'] = self.protocol_mount_target_domain
        if self.protocol_service_id is not None:
            result['ProtocolServiceId'] = self.protocol_service_id
        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type
        if self.status is not None:
            result['Status'] = self.status
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessGroupName') is not None:
            self.access_group_name = m.get('AccessGroupName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExportId') is not None:
            self.export_id = m.get('ExportId')
        if m.get('FsetId') is not None:
            self.fset_id = m.get('FsetId')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('ProtocolMountTargetDomain') is not None:
            self.protocol_mount_target_domain = m.get('ProtocolMountTargetDomain')
        if m.get('ProtocolServiceId') is not None:
            self.protocol_service_id = m.get('ProtocolServiceId')
        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DescribeProtocolMountTargetResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        protocol_mount_targets: List[DescribeProtocolMountTargetResponseBodyProtocolMountTargets] = None,
        request_id: str = None,
    ):
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The export directories of the protocol service.
        self.protocol_mount_targets = protocol_mount_targets
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.protocol_mount_targets:
            for k in self.protocol_mount_targets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['ProtocolMountTargets'] = []
        if self.protocol_mount_targets is not None:
            for k in self.protocol_mount_targets:
                result['ProtocolMountTargets'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.protocol_mount_targets = []
        if m.get('ProtocolMountTargets') is not None:
            for k in m.get('ProtocolMountTargets'):
                temp_model = DescribeProtocolMountTargetResponseBodyProtocolMountTargets()
                self.protocol_mount_targets.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeProtocolMountTargetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeProtocolMountTargetResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeProtocolMountTargetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeProtocolServiceRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        file_system_id: str = None,
        max_results: int = None,
        next_token: str = None,
        protocol_service_ids: str = None,
        status: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How do I ensure the idempotence?](https://help.aliyun.com/document_detail/25693.html)
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token
        # The description or a part of the description of the protocol service.
        # 
        # Limits:
        # 
        # *   The description must be 2 to 128 characters in length.
        # *   The description must start with a letter and cannot start with `http://` or `https://`.
        # *   The description can contain letters, digits, colons (:), underscores (_), and hyphens (-).
        self.description = description
        # The ID of the file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The number of results for each query.
        # 
        # *   Maximum value: 100.
        # *   Minimum value: 10.
        # *   Default value: 20.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token
        # The ID of the protocol service.
        # 
        # *   Format: CSV.
        # *   Limit: You can specify a maximum of 10 protocol service IDs.
        self.protocol_service_ids = protocol_service_ids
        # The status of the protocol service.
        # 
        # Format: CSV.
        # 
        # Valid values:
        # 
        # *   Creating: The protocol service is being created.
        # *   Starting: The protocol service is being started.
        # *   Running: The protocol service is running.
        # *   Updating: The protocol service is being updated.
        # *   Deleting: The protocol service is being deleted.
        # *   Stopping: The protocol service is being stopped.
        # *   Stopped: The protocol service is stopped.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.protocol_service_ids is not None:
            result['ProtocolServiceIds'] = self.protocol_service_ids
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ProtocolServiceIds') is not None:
            self.protocol_service_ids = m.get('ProtocolServiceIds')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeProtocolServiceResponseBodyProtocolServices(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        file_system_id: str = None,
        instance_base_throughput: int = None,
        instance_burst_throughput: int = None,
        instance_ram: int = None,
        modify_time: str = None,
        mount_target_count: int = None,
        protocol_service_id: str = None,
        protocol_spec: str = None,
        protocol_throughput: int = None,
        protocol_type: str = None,
        status: str = None,
    ):
        # The time when the protocol service was created. The time is displayed in UTC.
        self.create_time = create_time
        # The description of the protocol service.
        # 
        # Limits:
        # 
        # *   The description must be 2 to 128 characters in length.
        # *   The description must start with a letter and cannot start with `http://` or `https://`.
        # *   The description can contain letters, digits, colons (:), underscores (_), and hyphens (-).
        self.description = description
        # The ID of the file system.
        self.file_system_id = file_system_id
        # The base throughput of the protocol service. Unit: MB/s.
        self.instance_base_throughput = instance_base_throughput
        # The burst throughput of the protocol service. Unit: MB/s.
        self.instance_burst_throughput = instance_burst_throughput
        # The memory cache size of the protocol service. Unit: GiB.
        self.instance_ram = instance_ram
        # The time when the protocol service was modified. The time is displayed in UTC.
        self.modify_time = modify_time
        # The total number of CPFS directories and filesets exported in the protocol service.
        self.mount_target_count = mount_target_count
        # The ID of the protocol service.
        self.protocol_service_id = protocol_service_id
        # The specification of the protocol service.
        # 
        # *   Valid value: General.
        # *   Default value: General.
        self.protocol_spec = protocol_spec
        # The throughput of the protocol service. Unit: MB/s.
        self.protocol_throughput = protocol_throughput
        # The protocol type supported by the protocol service.
        # 
        # Valid values:
        # 
        # *   NFS: The protocol service supports access over the Network File System (NFS) protocol.
        self.protocol_type = protocol_type
        # The status of the protocol service.
        # 
        # Valid values:
        # 
        # *   Creating: The protocol service is being created.
        # *   Starting: The protocol service is being started.
        # *   Running: The protocol service is running.
        # *   Updating: The protocol service is being updated.
        # *   Deleting: The protocol service is being deleted.
        # *   Stopping: The protocol service is being stopped.
        # *   Stopped: The protocol service is stopped.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.instance_base_throughput is not None:
            result['InstanceBaseThroughput'] = self.instance_base_throughput
        if self.instance_burst_throughput is not None:
            result['InstanceBurstThroughput'] = self.instance_burst_throughput
        if self.instance_ram is not None:
            result['InstanceRAM'] = self.instance_ram
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.mount_target_count is not None:
            result['MountTargetCount'] = self.mount_target_count
        if self.protocol_service_id is not None:
            result['ProtocolServiceId'] = self.protocol_service_id
        if self.protocol_spec is not None:
            result['ProtocolSpec'] = self.protocol_spec
        if self.protocol_throughput is not None:
            result['ProtocolThroughput'] = self.protocol_throughput
        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('InstanceBaseThroughput') is not None:
            self.instance_base_throughput = m.get('InstanceBaseThroughput')
        if m.get('InstanceBurstThroughput') is not None:
            self.instance_burst_throughput = m.get('InstanceBurstThroughput')
        if m.get('InstanceRAM') is not None:
            self.instance_ram = m.get('InstanceRAM')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('MountTargetCount') is not None:
            self.mount_target_count = m.get('MountTargetCount')
        if m.get('ProtocolServiceId') is not None:
            self.protocol_service_id = m.get('ProtocolServiceId')
        if m.get('ProtocolSpec') is not None:
            self.protocol_spec = m.get('ProtocolSpec')
        if m.get('ProtocolThroughput') is not None:
            self.protocol_throughput = m.get('ProtocolThroughput')
        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeProtocolServiceResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        protocol_services: List[DescribeProtocolServiceResponseBodyProtocolServices] = None,
        request_id: str = None,
    ):
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The information about protocol services.
        self.protocol_services = protocol_services
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.protocol_services:
            for k in self.protocol_services:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['ProtocolServices'] = []
        if self.protocol_services is not None:
            for k in self.protocol_services:
                result['ProtocolServices'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.protocol_services = []
        if m.get('ProtocolServices') is not None:
            for k in m.get('ProtocolServices'):
                temp_model = DescribeProtocolServiceResponseBodyProtocolServices()
                self.protocol_services.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeProtocolServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeProtocolServiceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeProtocolServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(
        self,
        file_system_type: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The type of the file system.
        # 
        # Valid values:
        # 
        # *   all: all types of file systems
        # *   standard (default): General-purpose NAS file system
        # *   extreme: Extreme NAS file system
        # *   cpfs: Cloud Parallel File Storage (CPFS) file system
        # 
        # > CPFS file systems are available only on the China site (aliyun.com).
        self.file_system_type = file_system_type
        # The page number.
        # 
        # Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 10.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeRegionsResponseBodyRegionsRegion(TeaModel):
    def __init__(
        self,
        local_name: str = None,
        region_endpoint: str = None,
        region_id: str = None,
    ):
        # The region name.
        self.local_name = local_name
        # The endpoint for the region.
        self.region_endpoint = region_endpoint
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_endpoint is not None:
            result['RegionEndpoint'] = self.region_endpoint
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionEndpoint') is not None:
            self.region_endpoint = m.get('RegionEndpoint')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(
        self,
        region: List[DescribeRegionsResponseBodyRegionsRegion] = None,
    ):
        self.region = region

    def validate(self):
        if self.region:
            for k in self.region:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Region'] = []
        if self.region is not None:
            for k in self.region:
                result['Region'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.region = []
        if m.get('Region') is not None:
            for k in m.get('Region'):
                temp_model = DescribeRegionsResponseBodyRegionsRegion()
                self.region.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        regions: DescribeRegionsResponseBodyRegions = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The queried regions.
        self.regions = regions
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.regions:
            self.regions.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.regions is not None:
            result['Regions'] = self.regions.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Regions') is not None:
            temp_model = DescribeRegionsResponseBodyRegions()
            self.regions = temp_model.from_map(m['Regions'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeRegionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSmbAclRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
    ):
        # The ID of the file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        return self


class DescribeSmbAclResponseBodyAcl(TeaModel):
    def __init__(
        self,
        enable_anonymous_access: bool = None,
        enabled: bool = None,
        encrypt_data: bool = None,
        home_dir_path: str = None,
        reject_unencrypted_access: bool = None,
        super_admin_sid: str = None,
    ):
        # Indicates whether the file system allows anonymous access. Valid values:
        # 
        # *   true: The file system allows anonymous access.
        # *   false: The file system does not allow anonymous access.
        self.enable_anonymous_access = enable_anonymous_access
        # Indicates whether the ACL feature is enabled. Valid values:
        # 
        # *   true: The ACL feature is enabled.
        # *   false: The ACL feature is disabled.
        self.enabled = enabled
        # Indicates whether encryption in transit is enabled. Valid values:
        # 
        # *   true: Encryption in transit is enabled.
        # *   false: Encryption in transit is disabled.
        self.encrypt_data = encrypt_data
        # The home directory of each user.
        self.home_dir_path = home_dir_path
        # Indicates whether the file system denies access from non-encrypted clients. Valid values:
        # 
        # *   true: The file system denies access from non-encrypted clients.
        # *   false: The file system allows access from non-encrypted clients.
        self.reject_unencrypted_access = reject_unencrypted_access
        # The ID of a super admin.
        self.super_admin_sid = super_admin_sid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_anonymous_access is not None:
            result['EnableAnonymousAccess'] = self.enable_anonymous_access
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.encrypt_data is not None:
            result['EncryptData'] = self.encrypt_data
        if self.home_dir_path is not None:
            result['HomeDirPath'] = self.home_dir_path
        if self.reject_unencrypted_access is not None:
            result['RejectUnencryptedAccess'] = self.reject_unencrypted_access
        if self.super_admin_sid is not None:
            result['SuperAdminSid'] = self.super_admin_sid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableAnonymousAccess') is not None:
            self.enable_anonymous_access = m.get('EnableAnonymousAccess')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('EncryptData') is not None:
            self.encrypt_data = m.get('EncryptData')
        if m.get('HomeDirPath') is not None:
            self.home_dir_path = m.get('HomeDirPath')
        if m.get('RejectUnencryptedAccess') is not None:
            self.reject_unencrypted_access = m.get('RejectUnencryptedAccess')
        if m.get('SuperAdminSid') is not None:
            self.super_admin_sid = m.get('SuperAdminSid')
        return self


class DescribeSmbAclResponseBody(TeaModel):
    def __init__(
        self,
        acl: DescribeSmbAclResponseBodyAcl = None,
        request_id: str = None,
    ):
        # The information about the ACL feature.
        self.acl = acl
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.acl:
            self.acl.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl is not None:
            result['Acl'] = self.acl.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Acl') is not None:
            temp_model = DescribeSmbAclResponseBodyAcl()
            self.acl = temp_model.from_map(m['Acl'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeSmbAclResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSmbAclResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeSmbAclResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSnapshotsRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        file_system_type: str = None,
        page_number: int = None,
        page_size: int = None,
        snapshot_ids: str = None,
        snapshot_name: str = None,
        snapshot_type: str = None,
        status: str = None,
    ):
        # The ID of the file system.
        self.file_system_id = file_system_id
        # The type of the file system.
        # 
        # Valid value: extreme, which indicates Extreme File Storage NAS (NAS) file systems.
        self.file_system_type = file_system_type
        # The page number.
        # 
        # Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 10.
        self.page_size = page_size
        # The snapshot IDs.
        # 
        # You can specify a maximum of 100 snapshot IDs. You must separate snapshot IDs with commas (,).
        self.snapshot_ids = snapshot_ids
        # The snapshot name.
        self.snapshot_name = snapshot_name
        # The type of the snapshot.
        # 
        # Valid values:
        # 
        # *   auto: auto snapshot
        # *   user: manual snapshot
        # *   all (default): all snapshot types
        self.snapshot_type = snapshot_type
        # The status of the snapshot.
        # 
        # Valid values:
        # 
        # *   progressing: The snapshot is being created.
        # *   accomplished: The snapshot is created.
        # *   failed: The snapshot fails to be created.
        # *   all (default): all snapshot states.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.snapshot_ids is not None:
            result['SnapshotIds'] = self.snapshot_ids
        if self.snapshot_name is not None:
            result['SnapshotName'] = self.snapshot_name
        if self.snapshot_type is not None:
            result['SnapshotType'] = self.snapshot_type
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SnapshotIds') is not None:
            self.snapshot_ids = m.get('SnapshotIds')
        if m.get('SnapshotName') is not None:
            self.snapshot_name = m.get('SnapshotName')
        if m.get('SnapshotType') is not None:
            self.snapshot_type = m.get('SnapshotType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeSnapshotsResponseBodySnapshotsSnapshot(TeaModel):
    def __init__(
        self,
        completed_time: str = None,
        create_time: str = None,
        description: str = None,
        encrypt_type: int = None,
        file_system_type: str = None,
        progress: str = None,
        remain_time: int = None,
        retention_days: int = None,
        snapshot_id: str = None,
        snapshot_name: str = None,
        snapshot_type: str = None,
        source_file_system_id: str = None,
        source_file_system_size: int = None,
        source_file_system_version: str = None,
        status: str = None,
    ):
        # The time when snapshot creation was complete.
        # 
        # The time follows the [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) standard in UTC. The time is displayed in the `yyyy-MM-ddThh:mmZ` format.
        # 
        # >  This parameter is valid only when the snapshot is created. During snapshot creation, the value of this parameter is the same as that of CreateTime.
        self.completed_time = completed_time
        # The time when the snapshot was created.
        # 
        # The time follows the [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) standard in UTC. The time is displayed in the `yyyy-MM-ddThh:mmZ` format.
        self.create_time = create_time
        # The description of the snapshot.
        self.description = description
        # Indicates whether the snapshot is encrypted.
        # 
        # Valid values:
        # 
        # *   0: The snapshot is not encrypted.
        # *   1: The snapshot is encrypted.
        self.encrypt_type = encrypt_type
        # The type of the file system.
        self.file_system_type = file_system_type
        # The progress of the snapshot creation. The value of this parameter is expressed as a percentage.
        self.progress = progress
        # The remaining time that is required to create the snapshot.
        # 
        # Unit: seconds.
        self.remain_time = remain_time
        # The retention period of the auto snapshot.
        # 
        # Unit: days.
        # 
        # Valid values:
        # 
        # *   \\-1: Auto snapshots are permanently retained. After the number of auto snapshots exceeds the upper limit, the earliest auto snapshot is automatically deleted.
        # *   1 to 65536: Auto snapshots are retained for the specified days. After the retention period of auto snapshots expires, the auto snapshots are automatically deleted.
        self.retention_days = retention_days
        # The snapshot ID.
        self.snapshot_id = snapshot_id
        # The snapshot name.
        # 
        # If you specify a name to create a snapshot, the name of the snapshot is returned. Otherwise, no value is returned for this parameter.
        self.snapshot_name = snapshot_name
        # The snapshot type. Valid values:
        # 
        # *   auto: automatically created snapshots
        # *   user: manually created snapshots
        self.snapshot_type = snapshot_type
        # The ID of the source file system.
        # 
        # This parameter is retained even if the source file system of the snapshot is deleted.
        self.source_file_system_id = source_file_system_id
        # The capacity of the source file system.
        # 
        # Unit: GiB.
        self.source_file_system_size = source_file_system_size
        # The version of the source file system.
        self.source_file_system_version = source_file_system_version
        # The status of the snapshot.
        # 
        # Valid values:
        # 
        # *   progressing: The snapshot is being created.
        # *   accomplished: The snapshot is created.
        # *   failed: The snapshot fails to be created.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.completed_time is not None:
            result['CompletedTime'] = self.completed_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.encrypt_type is not None:
            result['EncryptType'] = self.encrypt_type
        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.remain_time is not None:
            result['RemainTime'] = self.remain_time
        if self.retention_days is not None:
            result['RetentionDays'] = self.retention_days
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        if self.snapshot_name is not None:
            result['SnapshotName'] = self.snapshot_name
        if self.snapshot_type is not None:
            result['SnapshotType'] = self.snapshot_type
        if self.source_file_system_id is not None:
            result['SourceFileSystemId'] = self.source_file_system_id
        if self.source_file_system_size is not None:
            result['SourceFileSystemSize'] = self.source_file_system_size
        if self.source_file_system_version is not None:
            result['SourceFileSystemVersion'] = self.source_file_system_version
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompletedTime') is not None:
            self.completed_time = m.get('CompletedTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EncryptType') is not None:
            self.encrypt_type = m.get('EncryptType')
        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('RemainTime') is not None:
            self.remain_time = m.get('RemainTime')
        if m.get('RetentionDays') is not None:
            self.retention_days = m.get('RetentionDays')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        if m.get('SnapshotName') is not None:
            self.snapshot_name = m.get('SnapshotName')
        if m.get('SnapshotType') is not None:
            self.snapshot_type = m.get('SnapshotType')
        if m.get('SourceFileSystemId') is not None:
            self.source_file_system_id = m.get('SourceFileSystemId')
        if m.get('SourceFileSystemSize') is not None:
            self.source_file_system_size = m.get('SourceFileSystemSize')
        if m.get('SourceFileSystemVersion') is not None:
            self.source_file_system_version = m.get('SourceFileSystemVersion')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeSnapshotsResponseBodySnapshots(TeaModel):
    def __init__(
        self,
        snapshot: List[DescribeSnapshotsResponseBodySnapshotsSnapshot] = None,
    ):
        self.snapshot = snapshot

    def validate(self):
        if self.snapshot:
            for k in self.snapshot:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Snapshot'] = []
        if self.snapshot is not None:
            for k in self.snapshot:
                result['Snapshot'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.snapshot = []
        if m.get('Snapshot') is not None:
            for k in m.get('Snapshot'):
                temp_model = DescribeSnapshotsResponseBodySnapshotsSnapshot()
                self.snapshot.append(temp_model.from_map(k))
        return self


class DescribeSnapshotsResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        snapshots: DescribeSnapshotsResponseBodySnapshots = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The details about snapshots.
        self.snapshots = snapshots
        # The total number of snapshots returned.
        self.total_count = total_count

    def validate(self):
        if self.snapshots:
            self.snapshots.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.snapshots is not None:
            result['Snapshots'] = self.snapshots.to_map()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Snapshots') is not None:
            temp_model = DescribeSnapshotsResponseBodySnapshots()
            self.snapshots = temp_model.from_map(m['Snapshots'])
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeSnapshotsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSnapshotsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeSnapshotsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeStoragePackagesRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        use_utcdate_time: bool = None,
    ):
        # The number of the page to return.
        # 
        # Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of storage plans to return on each page.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 10.
        self.page_size = page_size
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Specifies whether the time to return is in UTC.
        # 
        # Valid values:
        # 
        # *   true (default): returns UTC time.
        # *   false: returns UNIX timestamp.
        self.use_utcdate_time = use_utcdate_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.use_utcdate_time is not None:
            result['UseUTCDateTime'] = self.use_utcdate_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UseUTCDateTime') is not None:
            self.use_utcdate_time = m.get('UseUTCDateTime')
        return self


class DescribeStoragePackagesResponseBodyPackagesPackage(TeaModel):
    def __init__(
        self,
        expired_time: str = None,
        file_system_id: str = None,
        package_id: str = None,
        size: int = None,
        start_time: str = None,
        status: str = None,
        storage_type: str = None,
    ):
        # The end time of the validity period for the storage plan.
        self.expired_time = expired_time
        # The ID of the file system that is bound to the storage plan.
        self.file_system_id = file_system_id
        # The ID of the storage plan.
        self.package_id = package_id
        # The capacity of the storage plan.
        # 
        # Unit: bytes.
        self.size = size
        # The start time of the validity period for the storage plan.
        self.start_time = start_time
        # The status of the storage plan.
        # 
        # Valid values:
        # 
        # *   free: The storage plan is not bound to a file system. You can bind the storage plan to a file system of the same storage type.
        # *   bound: The storage plan is bound to a file system.
        self.status = status
        # The type of the storage plan.
        # 
        # Valid values:
        # 
        # *   Performance
        # *   Capacity
        self.storage_type = storage_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.package_id is not None:
            result['PackageId'] = self.package_id
        if self.size is not None:
            result['Size'] = self.size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('PackageId') is not None:
            self.package_id = m.get('PackageId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        return self


class DescribeStoragePackagesResponseBodyPackages(TeaModel):
    def __init__(
        self,
        package: List[DescribeStoragePackagesResponseBodyPackagesPackage] = None,
    ):
        self.package = package

    def validate(self):
        if self.package:
            for k in self.package:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Package'] = []
        if self.package is not None:
            for k in self.package:
                result['Package'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.package = []
        if m.get('Package') is not None:
            for k in m.get('Package'):
                temp_model = DescribeStoragePackagesResponseBodyPackagesPackage()
                self.package.append(temp_model.from_map(k))
        return self


class DescribeStoragePackagesResponseBody(TeaModel):
    def __init__(
        self,
        packages: DescribeStoragePackagesResponseBodyPackages = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of storage plans.
        self.packages = packages
        # The page number of the returned page.
        self.page_number = page_number
        # The number of storage plans returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The number of storage plans.
        self.total_count = total_count

    def validate(self):
        if self.packages:
            self.packages.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.packages is not None:
            result['Packages'] = self.packages.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Packages') is not None:
            temp_model = DescribeStoragePackagesResponseBodyPackages()
            self.packages = temp_model.from_map(m['Packages'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeStoragePackagesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeStoragePackagesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeStoragePackagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeZonesRequest(TeaModel):
    def __init__(
        self,
        file_system_type: str = None,
        region_id: str = None,
    ):
        # The type of the file system.
        # 
        # Valid values:
        # 
        # *   standard (default): General-purpose NAS file system
        # *   extreme: Extreme NAS file system
        # *   cpfs: Cloud Parallel File Storage (CPFS) file system
        # 
        # > CPFS file systems are available only on the China site (aliyun.com).
        self.file_system_type = file_system_type
        # The ID of the region where you want to query zones.
        # 
        # You can call the DescribeRegions operation to query the latest region list.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeZonesResponseBodyZonesZoneCapacity(TeaModel):
    def __init__(
        self,
        protocol: List[str] = None,
    ):
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        return self


class DescribeZonesResponseBodyZonesZoneInstanceTypesInstanceType(TeaModel):
    def __init__(
        self,
        protocol_type: str = None,
        storage_type: str = None,
    ):
        # The protocol type.
        # 
        # *   If the FileSystemType parameter is set to standard, the protocol type is nfs or smb.
        # *   If the FileSystemType parameter is set to extreme, the protocol type is nfs.
        # *   If the FileSystemType parameter is set to cpfs, the protocol type is cpfs.
        # 
        # > CPFS file systems are available only on the China site (aliyun.com).
        self.protocol_type = protocol_type
        # The storage type.
        # 
        # *   If the FileSystemType parameter is set to standard, the storage type is Performance or Capacity.
        # *   If the FileSystemType parameter is set to extreme, the storage type is standard or advance.
        # *   If the FileSystemType parameter is set to cpfs, the storage type is advance_100 (100 MB/s/TiB baseline) or advance_200 (200 MB/s/TiB baseline).
        # 
        # > CPFS file systems are available only on the China site (aliyun.com).
        self.storage_type = storage_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        return self


class DescribeZonesResponseBodyZonesZoneInstanceTypes(TeaModel):
    def __init__(
        self,
        instance_type: List[DescribeZonesResponseBodyZonesZoneInstanceTypesInstanceType] = None,
    ):
        self.instance_type = instance_type

    def validate(self):
        if self.instance_type:
            for k in self.instance_type:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InstanceType'] = []
        if self.instance_type is not None:
            for k in self.instance_type:
                result['InstanceType'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_type = []
        if m.get('InstanceType') is not None:
            for k in m.get('InstanceType'):
                temp_model = DescribeZonesResponseBodyZonesZoneInstanceTypesInstanceType()
                self.instance_type.append(temp_model.from_map(k))
        return self


class DescribeZonesResponseBodyZonesZonePerformance(TeaModel):
    def __init__(
        self,
        protocol: List[str] = None,
    ):
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        return self


class DescribeZonesResponseBodyZonesZone(TeaModel):
    def __init__(
        self,
        capacity: DescribeZonesResponseBodyZonesZoneCapacity = None,
        instance_types: DescribeZonesResponseBodyZonesZoneInstanceTypes = None,
        performance: DescribeZonesResponseBodyZonesZonePerformance = None,
        zone_id: str = None,
    ):
        # This parameter is reserved. You can ignore this parameter.
        self.capacity = capacity
        # The details about file system types.
        self.instance_types = instance_types
        # This parameter is reserved. You can ignore this parameter.
        self.performance = performance
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        if self.capacity:
            self.capacity.validate()
        if self.instance_types:
            self.instance_types.validate()
        if self.performance:
            self.performance.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capacity is not None:
            result['Capacity'] = self.capacity.to_map()
        if self.instance_types is not None:
            result['InstanceTypes'] = self.instance_types.to_map()
        if self.performance is not None:
            result['Performance'] = self.performance.to_map()
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Capacity') is not None:
            temp_model = DescribeZonesResponseBodyZonesZoneCapacity()
            self.capacity = temp_model.from_map(m['Capacity'])
        if m.get('InstanceTypes') is not None:
            temp_model = DescribeZonesResponseBodyZonesZoneInstanceTypes()
            self.instance_types = temp_model.from_map(m['InstanceTypes'])
        if m.get('Performance') is not None:
            temp_model = DescribeZonesResponseBodyZonesZonePerformance()
            self.performance = temp_model.from_map(m['Performance'])
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeZonesResponseBodyZones(TeaModel):
    def __init__(
        self,
        zone: List[DescribeZonesResponseBodyZonesZone] = None,
    ):
        self.zone = zone

    def validate(self):
        if self.zone:
            for k in self.zone:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Zone'] = []
        if self.zone is not None:
            for k in self.zone:
                result['Zone'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.zone = []
        if m.get('Zone') is not None:
            for k in m.get('Zone'):
                temp_model = DescribeZonesResponseBodyZonesZone()
                self.zone.append(temp_model.from_map(k))
        return self


class DescribeZonesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        zones: DescribeZonesResponseBodyZones = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The queried zones.
        self.zones = zones

    def validate(self):
        if self.zones:
            self.zones.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.zones is not None:
            result['Zones'] = self.zones.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Zones') is not None:
            temp_model = DescribeZonesResponseBodyZones()
            self.zones = temp_model.from_map(m['Zones'])
        return self


class DescribeZonesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeZonesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeZonesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableAndCleanRecycleBinRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
    ):
        # The ID of the file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        return self


class DisableAndCleanRecycleBinResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DisableAndCleanRecycleBinResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DisableAndCleanRecycleBinResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DisableAndCleanRecycleBinResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableNfsAclRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
    ):
        # The ID of the file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        return self


class DisableNfsAclResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DisableNfsAclResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DisableNfsAclResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DisableNfsAclResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableSmbAclRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
    ):
        # The ID of the file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        return self


class DisableSmbAclResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DisableSmbAclResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DisableSmbAclResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DisableSmbAclResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableNfsAclRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
    ):
        # The ID of the file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        return self


class EnableNfsAclResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EnableNfsAclResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnableNfsAclResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = EnableNfsAclResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableRecycleBinRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        reserved_days: int = None,
    ):
        # The ID of the file system for which you want to enable the recycle bin feature.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The retention period of the files in the recycle bin. Unit: days.
        # 
        # Valid values: 1 to 180.
        # 
        # Default value: 3.
        self.reserved_days = reserved_days

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.reserved_days is not None:
            result['ReservedDays'] = self.reserved_days
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('ReservedDays') is not None:
            self.reserved_days = m.get('ReservedDays')
        return self


class EnableRecycleBinResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EnableRecycleBinResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnableRecycleBinResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = EnableRecycleBinResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableSmbAclRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        keytab: str = None,
        keytab_md_5: str = None,
    ):
        # The ID of the file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The string that is generated after the system encodes the keytab file by using Base64.
        self.keytab = keytab
        # The string that is generated after the system encodes the keytab file by using MD5.
        self.keytab_md_5 = keytab_md_5

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.keytab is not None:
            result['Keytab'] = self.keytab
        if self.keytab_md_5 is not None:
            result['KeytabMd5'] = self.keytab_md_5
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('Keytab') is not None:
            self.keytab = m.get('Keytab')
        if m.get('KeytabMd5') is not None:
            self.keytab_md_5 = m.get('KeytabMd5')
        return self


class EnableSmbAclResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EnableSmbAclResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnableSmbAclResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = EnableSmbAclResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDirectoryOrFilePropertiesRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        path: str = None,
    ):
        # The ID of the file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The absolute path of the directory.
        # 
        # The path must start with a forward slash (/) and must be a path that exists in the mount target.
        # 
        # This parameter is required.
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class GetDirectoryOrFilePropertiesResponseBodyEntry(TeaModel):
    def __init__(
        self,
        atime: str = None,
        ctime: str = None,
        has_archive_file: bool = None,
        has_infrequent_access_file: bool = None,
        inode: str = None,
        mtime: str = None,
        name: str = None,
        retrieve_time: str = None,
        size: int = None,
        storage_type: str = None,
        type: str = None,
    ):
        # The time when the file was queried.
        # 
        # The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format.
        # 
        # This parameter is returned only if the value of the Type parameter is File.
        self.atime = atime
        # The time when the metadata was modified.
        # 
        # The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format.
        # 
        # This parameter is returned only if the value of the Type parameter is File.
        self.ctime = ctime
        # Indicates whether the directory contains files stored in the Archive storage class.
        # 
        # This parameter is returned only if the Type parameter is set to Directory.
        # 
        # Valid values:
        # 
        # *   true: The directory contains files stored in the Archive storage class.
        # *   false: The directory does not contain files stored in the Archive storage class.
        self.has_archive_file = has_archive_file
        # Indicates whether the directory contains files stored in the IA storage medium.
        # 
        # This parameter is returned only if the value of the Type parameter is Directory.
        # 
        # Valid values:
        # 
        # *   true: The directory contains files stored in the IA storage medium.
        # *   false: The directory does not contain files stored in the IA storage medium.
        self.has_infrequent_access_file = has_infrequent_access_file
        # The file or directory inode.
        self.inode = inode
        # The time when the file was modified.
        # 
        # The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format.
        # 
        # This parameter is returned only if the value of the Type parameter is File.
        self.mtime = mtime
        # The name of the file or directory.
        self.name = name
        # The time when the last data retrieval task was run.
        # 
        # The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format.
        # 
        # This parameter is returned only if the value of the Type parameter is File.
        self.retrieve_time = retrieve_time
        # The size of the file.
        # 
        # Unit: bytes.
        # 
        # This parameter is returned only if the value of the Type parameter is File.
        self.size = size
        # The storage class of the file.
        # 
        # This parameter is returned only if the value of the Type parameter is File.
        # 
        # Valid values:
        # 
        # *   standard: General-purpose NAS file system
        # *   InfrequentAccess: the IA storage class.
        self.storage_type = storage_type
        # The type of the query result.
        # 
        # Valid values:
        # 
        # *   File
        # *   Directory
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.atime is not None:
            result['ATime'] = self.atime
        if self.ctime is not None:
            result['CTime'] = self.ctime
        if self.has_archive_file is not None:
            result['HasArchiveFile'] = self.has_archive_file
        if self.has_infrequent_access_file is not None:
            result['HasInfrequentAccessFile'] = self.has_infrequent_access_file
        if self.inode is not None:
            result['Inode'] = self.inode
        if self.mtime is not None:
            result['MTime'] = self.mtime
        if self.name is not None:
            result['Name'] = self.name
        if self.retrieve_time is not None:
            result['RetrieveTime'] = self.retrieve_time
        if self.size is not None:
            result['Size'] = self.size
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ATime') is not None:
            self.atime = m.get('ATime')
        if m.get('CTime') is not None:
            self.ctime = m.get('CTime')
        if m.get('HasArchiveFile') is not None:
            self.has_archive_file = m.get('HasArchiveFile')
        if m.get('HasInfrequentAccessFile') is not None:
            self.has_infrequent_access_file = m.get('HasInfrequentAccessFile')
        if m.get('Inode') is not None:
            self.inode = m.get('Inode')
        if m.get('MTime') is not None:
            self.mtime = m.get('MTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RetrieveTime') is not None:
            self.retrieve_time = m.get('RetrieveTime')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetDirectoryOrFilePropertiesResponseBody(TeaModel):
    def __init__(
        self,
        entry: GetDirectoryOrFilePropertiesResponseBodyEntry = None,
        request_id: str = None,
    ):
        # The details about the file or directory.
        self.entry = entry
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.entry:
            self.entry.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entry is not None:
            result['Entry'] = self.entry.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Entry') is not None:
            temp_model = GetDirectoryOrFilePropertiesResponseBodyEntry()
            self.entry = temp_model.from_map(m['Entry'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDirectoryOrFilePropertiesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDirectoryOrFilePropertiesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetDirectoryOrFilePropertiesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRecycleBinAttributeRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
    ):
        # The ID of the file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        return self


class GetRecycleBinAttributeResponseBodyRecycleBinAttribute(TeaModel):
    def __init__(
        self,
        archive_size: int = None,
        enable_time: str = None,
        reserved_days: int = None,
        secondary_size: int = None,
        size: int = None,
        status: str = None,
    ):
        # The size of the archived data that is dumped to the recycle bin. Unit: bytes.
        self.archive_size = archive_size
        # The time at which the recycle bin was enabled.
        self.enable_time = enable_time
        # The retention period of the files in the recycle bin. Unit: days.
        # 
        # If the recycle bin is disabled, 0 is returned for this parameter.
        self.reserved_days = reserved_days
        # The size of the Infrequent Access (IA) data that is dumped to the recycle bin. Unit: bytes.
        self.secondary_size = secondary_size
        # The size of the files that are dumped to the recycle bin. Unit: bytes.
        self.size = size
        # The status of the recycle bin.
        # 
        # Valid values:
        # 
        # *   Enable: The recycle bin is enabled.
        # *   Disable: The recycle bin is disabled.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.archive_size is not None:
            result['ArchiveSize'] = self.archive_size
        if self.enable_time is not None:
            result['EnableTime'] = self.enable_time
        if self.reserved_days is not None:
            result['ReservedDays'] = self.reserved_days
        if self.secondary_size is not None:
            result['SecondarySize'] = self.secondary_size
        if self.size is not None:
            result['Size'] = self.size
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArchiveSize') is not None:
            self.archive_size = m.get('ArchiveSize')
        if m.get('EnableTime') is not None:
            self.enable_time = m.get('EnableTime')
        if m.get('ReservedDays') is not None:
            self.reserved_days = m.get('ReservedDays')
        if m.get('SecondarySize') is not None:
            self.secondary_size = m.get('SecondarySize')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetRecycleBinAttributeResponseBody(TeaModel):
    def __init__(
        self,
        recycle_bin_attribute: GetRecycleBinAttributeResponseBodyRecycleBinAttribute = None,
        request_id: str = None,
    ):
        # The description of the recycle bin.
        self.recycle_bin_attribute = recycle_bin_attribute
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.recycle_bin_attribute:
            self.recycle_bin_attribute.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.recycle_bin_attribute is not None:
            result['RecycleBinAttribute'] = self.recycle_bin_attribute.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecycleBinAttribute') is not None:
            temp_model = GetRecycleBinAttributeResponseBodyRecycleBinAttribute()
            self.recycle_bin_attribute = temp_model.from_map(m['RecycleBinAttribute'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetRecycleBinAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRecycleBinAttributeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetRecycleBinAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDirectoriesAndFilesRequest(TeaModel):
    def __init__(
        self,
        directory_only: bool = None,
        file_system_id: str = None,
        max_results: int = None,
        next_token: str = None,
        path: str = None,
        storage_type: str = None,
    ):
        # Specifies whether to query only directories.
        # 
        # Valid values:
        # 
        # *   false (default): queries both directories and files.
        # *   true: queries only directories.
        # 
        # >  If you set the StorageType parameter to All, you must set the DirectoryOnly parameter to true.
        self.directory_only = directory_only
        # The ID of the file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The maximum number of directories or files to include in the results of each query.
        # 
        # Valid values: 10 to 128.
        # 
        # Default value: 100.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token
        # The absolute path of the directory.
        # 
        # The path must start with a forward slash (/) and must be a path that exists in the mount target.
        # 
        # This parameter is required.
        self.path = path
        # The storage class.
        # 
        # *   InfrequentAccess: the Infrequent Access (IA) storage class.
        # *   Archive: the Archive storage class.
        # *   All: all stored data.
        # 
        # >  If you set the StorageType parameter to All, you must set the DirectoryOnly parameter to true.
        # 
        # This parameter is required.
        self.storage_type = storage_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_only is not None:
            result['DirectoryOnly'] = self.directory_only
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.path is not None:
            result['Path'] = self.path
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryOnly') is not None:
            self.directory_only = m.get('DirectoryOnly')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        return self


class ListDirectoriesAndFilesResponseBodyEntries(TeaModel):
    def __init__(
        self,
        atime: str = None,
        ctime: str = None,
        file_id: str = None,
        has_archive_file: str = None,
        has_infrequent_access_file: bool = None,
        inode: str = None,
        mtime: str = None,
        name: str = None,
        owner: str = None,
        retrieve_time: str = None,
        size: int = None,
        storage_type: str = None,
        type: str = None,
    ):
        # The time when the file was queried.
        # 
        # The time follows the ISO 8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format.
        # 
        # This parameter is returned and valid only if the value of the Type parameter is File.
        self.atime = atime
        # The time when the raw data was modified.
        # 
        # The time follows the ISO 8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format.
        # 
        # This parameter is returned and valid only if the value of the Type parameter is File.
        self.ctime = ctime
        # The ID of the directory or file.
        self.file_id = file_id
        # Indicates whether the directory contains files stored in the Archive storage class.
        # 
        # This parameter is returned and valid only if the value of the Type parameter is Directory.
        # 
        # Valid values:
        # 
        # *   true: The directory contains files stored in the Archive storage class.
        # *   false: The directory does not contain files stored in the Archive storage class.
        self.has_archive_file = has_archive_file
        # Indicates whether the directory contains files stored in the IA storage class.
        # 
        # This parameter is returned and valid only if the value of the Type parameter is Directory.
        # 
        # Valid values:
        # 
        # *   true: The directory contains files stored in the IA storage class.
        # *   false: The directory does not contain files stored in the IA storage class.
        self.has_infrequent_access_file = has_infrequent_access_file
        # The file or directory inode.
        self.inode = inode
        # The time when the file was modified.
        # 
        # The time follows the ISO 8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format.
        # 
        # This parameter is returned and valid only if the value of the Type parameter is File.
        self.mtime = mtime
        # The name of the file or directory.
        self.name = name
        # The ID of the portable account. This parameter is returned and valid only if the value of the ProtocolType parameter is SMB and RAM-based access control is enabled.
        self.owner = owner
        # The time when the last data retrieval task was run.
        # 
        # The time follows the ISO 8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format.
        # 
        # This parameter is returned and valid only if the value of the Type parameter is File.
        self.retrieve_time = retrieve_time
        # The size of the file.
        # 
        # Unit: bytes.
        # 
        # This parameter is returned and valid only if the value of the Type parameter is File.
        self.size = size
        # The storage class.
        # 
        # This parameter is returned and valid only if the value of the Type parameter is File.
        # 
        # Valid values:
        # 
        # *   InfrequentAccess: the IA storage class.
        # *   Archive: the Archive storage class.
        self.storage_type = storage_type
        # The type of the query result.
        # 
        # Valid values:
        # 
        # *   File
        # *   Directory
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.atime is not None:
            result['Atime'] = self.atime
        if self.ctime is not None:
            result['Ctime'] = self.ctime
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.has_archive_file is not None:
            result['HasArchiveFile'] = self.has_archive_file
        if self.has_infrequent_access_file is not None:
            result['HasInfrequentAccessFile'] = self.has_infrequent_access_file
        if self.inode is not None:
            result['Inode'] = self.inode
        if self.mtime is not None:
            result['Mtime'] = self.mtime
        if self.name is not None:
            result['Name'] = self.name
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.retrieve_time is not None:
            result['RetrieveTime'] = self.retrieve_time
        if self.size is not None:
            result['Size'] = self.size
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Atime') is not None:
            self.atime = m.get('Atime')
        if m.get('Ctime') is not None:
            self.ctime = m.get('Ctime')
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('HasArchiveFile') is not None:
            self.has_archive_file = m.get('HasArchiveFile')
        if m.get('HasInfrequentAccessFile') is not None:
            self.has_infrequent_access_file = m.get('HasInfrequentAccessFile')
        if m.get('Inode') is not None:
            self.inode = m.get('Inode')
        if m.get('Mtime') is not None:
            self.mtime = m.get('Mtime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('RetrieveTime') is not None:
            self.retrieve_time = m.get('RetrieveTime')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListDirectoriesAndFilesResponseBody(TeaModel):
    def __init__(
        self,
        entries: List[ListDirectoriesAndFilesResponseBodyEntries] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The details about the files or directories.
        self.entries = entries
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.entries:
            for k in self.entries:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Entries'] = []
        if self.entries is not None:
            for k in self.entries:
                result['Entries'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.entries = []
        if m.get('Entries') is not None:
            for k in m.get('Entries'):
                temp_model = ListDirectoriesAndFilesResponseBodyEntries()
                self.entries.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListDirectoriesAndFilesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDirectoriesAndFilesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDirectoriesAndFilesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLifecycleRetrieveJobsRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        page_number: int = None,
        page_size: int = None,
        status: str = None,
        storage_type: str = None,
    ):
        # The ID of the file system.
        self.file_system_id = file_system_id
        # The number of the page to return.
        # 
        # Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 10.
        self.page_size = page_size
        # The status of the data retrieval task. Valid values:
        # 
        # *   active: The task is running.
        # *   canceled: The task is canceled.
        # *   completed: The task is completed.
        # *   failed: The task has failed.
        self.status = status
        # The storage class.
        # 
        # *   InfrequentAccess: the Infrequent Access (IA) storage class.
        # *   Archive: the Archive storage class.
        # 
        # >  If the StorageType parameter is not specified, data retrieval tasks of all types are returned.
        self.storage_type = storage_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        return self


class ListLifecycleRetrieveJobsResponseBodyLifecycleRetrieveJobs(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        discovered_file_count: int = None,
        file_system_id: str = None,
        job_id: str = None,
        paths: List[str] = None,
        retrieved_file_count: int = None,
        status: str = None,
        storage_type: str = None,
        update_time: str = None,
    ):
        # The time when the task was created.
        # 
        # The time follows the ISO 8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format.
        self.create_time = create_time
        # The total number of files that are read in the data retrieval task.
        self.discovered_file_count = discovered_file_count
        # The ID of the file system.
        self.file_system_id = file_system_id
        # The ID of the data retrieval task.
        self.job_id = job_id
        # The execution path of the data retrieval task.
        self.paths = paths
        # The total number of files that are retrieved.
        self.retrieved_file_count = retrieved_file_count
        # The status of the data retrieval task. Valid values:
        # 
        # *   active: The task is running.
        # *   canceled: The task is canceled.
        # *   completed: The task is completed.
        # *   failed: The task has failed.
        self.status = status
        # The storage class.
        # 
        # *   InfrequentAccess: the IA storage class.
        # *   Archive: the Archive storage class.
        self.storage_type = storage_type
        # The time when the task was updated.
        # 
        # The time follows the ISO 8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.discovered_file_count is not None:
            result['DiscoveredFileCount'] = self.discovered_file_count
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.paths is not None:
            result['Paths'] = self.paths
        if self.retrieved_file_count is not None:
            result['RetrievedFileCount'] = self.retrieved_file_count
        if self.status is not None:
            result['Status'] = self.status
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DiscoveredFileCount') is not None:
            self.discovered_file_count = m.get('DiscoveredFileCount')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Paths') is not None:
            self.paths = m.get('Paths')
        if m.get('RetrievedFileCount') is not None:
            self.retrieved_file_count = m.get('RetrievedFileCount')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListLifecycleRetrieveJobsResponseBody(TeaModel):
    def __init__(
        self,
        lifecycle_retrieve_jobs: List[ListLifecycleRetrieveJobsResponseBodyLifecycleRetrieveJobs] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The details about the data retrieval tasks.
        self.lifecycle_retrieve_jobs = lifecycle_retrieve_jobs
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of data retrieval tasks.
        self.total_count = total_count

    def validate(self):
        if self.lifecycle_retrieve_jobs:
            for k in self.lifecycle_retrieve_jobs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LifecycleRetrieveJobs'] = []
        if self.lifecycle_retrieve_jobs is not None:
            for k in self.lifecycle_retrieve_jobs:
                result['LifecycleRetrieveJobs'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.lifecycle_retrieve_jobs = []
        if m.get('LifecycleRetrieveJobs') is not None:
            for k in m.get('LifecycleRetrieveJobs'):
                temp_model = ListLifecycleRetrieveJobsResponseBodyLifecycleRetrieveJobs()
                self.lifecycle_retrieve_jobs.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListLifecycleRetrieveJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListLifecycleRetrieveJobsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListLifecycleRetrieveJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRecentlyRecycledDirectoriesRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        max_results: int = None,
        next_token: str = None,
    ):
        # The ID of the file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The number of directories to return for each query.
        # 
        # Valid values: 10 to 1000.
        # 
        # Default value: 100.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request.
        # 
        # If not all directories are returned in a query, the return value of the NextToken parameter is not empty. In this case, you can specify a valid value for the NextToken parameter to continue the query.
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListRecentlyRecycledDirectoriesResponseBodyEntries(TeaModel):
    def __init__(
        self,
        file_id: str = None,
        last_delete_time: str = None,
        name: str = None,
        path: str = None,
    ):
        # The ID of the directory.
        self.file_id = file_id
        # The time when the directory was last deleted.
        self.last_delete_time = last_delete_time
        # The name of the directory.
        self.name = name
        # The absolute path to the directory.
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.last_delete_time is not None:
            result['LastDeleteTime'] = self.last_delete_time
        if self.name is not None:
            result['Name'] = self.name
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('LastDeleteTime') is not None:
            self.last_delete_time = m.get('LastDeleteTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class ListRecentlyRecycledDirectoriesResponseBody(TeaModel):
    def __init__(
        self,
        entries: List[ListRecentlyRecycledDirectoriesResponseBodyEntries] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The information about the directories that are recently deleted.
        self.entries = entries
        # A pagination token.
        # 
        # If not all directories are returned in a query, the return value of the NextToken parameter is not empty. In this case, you can specify a valid value for the NextToken parameter to continue the query.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.entries:
            for k in self.entries:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Entries'] = []
        if self.entries is not None:
            for k in self.entries:
                result['Entries'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.entries = []
        if m.get('Entries') is not None:
            for k in m.get('Entries'):
                temp_model = ListRecentlyRecycledDirectoriesResponseBodyEntries()
                self.entries.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListRecentlyRecycledDirectoriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRecentlyRecycledDirectoriesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListRecentlyRecycledDirectoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRecycleBinJobsRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        job_id: str = None,
        page_number: int = None,
        page_size: int = None,
        status: str = None,
    ):
        # The ID of the file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The job ID.
        self.job_id = job_id
        # The page number.
        # 
        # Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 10.
        self.page_size = page_size
        # The job status. Valid values:
        # 
        # *   Running: The job is running.
        # *   Defragmenting: The job is defragmenting data.
        # *   PartialSuccess: The job is partially completed.
        # *   Success: The job is completed.
        # *   Fail: The job failed.
        # *   Cancelled: The job is canceled.
        # *   all (default)
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListRecycleBinJobsResponseBodyJobs(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        error_code: str = None,
        error_message: str = None,
        file_id: str = None,
        file_name: str = None,
        id: str = None,
        progress: str = None,
        status: str = None,
        type: str = None,
    ):
        # The time when the job was created.
        self.create_time = create_time
        # The error code returned.
        # 
        # A valid value is returned only if you set the Status parameter to Fail or PartialSuccess.
        self.error_code = error_code
        # The error message.
        # 
        # A valid value is returned only if you set the Status parameter to Fail or PartialSuccess.
        self.error_message = error_message
        # The ID of the file or directory in the job.
        self.file_id = file_id
        # The name of the file or directory that is associated with the job.
        self.file_name = file_name
        # The job ID.
        self.id = id
        # The progress of the job.
        # 
        # Valid values: 1 to 100.
        self.progress = progress
        # The status of the job. Valid values:
        # 
        # *   Running: The job is running.
        # *   Defragmenting: The job is defragmenting data.
        # *   PartialSuccess: The job is partially completed.
        # *   Success: The job is completed.
        # *   Fail: The job failed.
        # *   Cancelled: The job is canceled.
        self.status = status
        # The type of the job. Valid values:
        # 
        # *   Restore: a file restoration job
        # *   Delete: a file deletion job
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.id is not None:
            result['Id'] = self.id
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListRecycleBinJobsResponseBody(TeaModel):
    def __init__(
        self,
        jobs: List[ListRecycleBinJobsResponseBodyJobs] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The information about the jobs of the recycle bin.
        self.jobs = jobs
        # The page number.
        self.page_number = page_number
        # The number of jobs returned per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of jobs.
        self.total_count = total_count

    def validate(self):
        if self.jobs:
            for k in self.jobs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Jobs'] = []
        if self.jobs is not None:
            for k in self.jobs:
                result['Jobs'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.jobs = []
        if m.get('Jobs') is not None:
            for k in m.get('Jobs'):
                temp_model = ListRecycleBinJobsResponseBodyJobs()
                self.jobs.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListRecycleBinJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRecycleBinJobsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListRecycleBinJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRecycledDirectoriesAndFilesRequest(TeaModel):
    def __init__(
        self,
        file_id: str = None,
        file_system_id: str = None,
        max_results: int = None,
        next_token: str = None,
    ):
        # The ID of the directory that you want to query.
        # 
        # You can call the [ListRecentlyRecycledDirectories ](https://help.aliyun.com/document_detail/2412173.html)operation to query the file ID.
        # 
        # This parameter is required.
        self.file_id = file_id
        # The ID of the file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The number of files or directories to return for each query.
        # 
        # Valid values: 10 to 1000.
        # 
        # Default value: 100.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request.
        # 
        # If all the files and directories are incompletely returned in a query, the return value of the NextToken parameter is not empty. In this case, you can specify a valid value for the NextToken parameter to continue the query.
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListRecycledDirectoriesAndFilesResponseBodyEntries(TeaModel):
    def __init__(
        self,
        atime: str = None,
        ctime: str = None,
        delete_time: str = None,
        file_id: str = None,
        inode: str = None,
        mtime: str = None,
        name: str = None,
        size: int = None,
        type: str = None,
    ):
        # The time when the file or directory was last accessed.
        self.atime = atime
        # The time when the metadata was last modified.
        self.ctime = ctime
        # The time when the file or directory was deleted.
        self.delete_time = delete_time
        # The IDs of the files or directories.
        self.file_id = file_id
        # The inode of the file or directory.
        self.inode = inode
        # The time when the file or directory was last modified.
        self.mtime = mtime
        # The name of the file or directory before it was deleted.
        self.name = name
        # The size of the file. Unit: bytes.
        # 
        # The value 0 is returned for this parameter if Directory is returned for the Type parameter.
        self.size = size
        # The type of the returned object. Valid values:
        # 
        # *   File
        # *   Directory
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.atime is not None:
            result['ATime'] = self.atime
        if self.ctime is not None:
            result['CTime'] = self.ctime
        if self.delete_time is not None:
            result['DeleteTime'] = self.delete_time
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.inode is not None:
            result['Inode'] = self.inode
        if self.mtime is not None:
            result['MTime'] = self.mtime
        if self.name is not None:
            result['Name'] = self.name
        if self.size is not None:
            result['Size'] = self.size
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ATime') is not None:
            self.atime = m.get('ATime')
        if m.get('CTime') is not None:
            self.ctime = m.get('CTime')
        if m.get('DeleteTime') is not None:
            self.delete_time = m.get('DeleteTime')
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('Inode') is not None:
            self.inode = m.get('Inode')
        if m.get('MTime') is not None:
            self.mtime = m.get('MTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListRecycledDirectoriesAndFilesResponseBody(TeaModel):
    def __init__(
        self,
        entries: List[ListRecycledDirectoriesAndFilesResponseBodyEntries] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The information about files or directories in the recycle bin.
        self.entries = entries
        # A pagination token.
        # 
        # If all the files and directories are incompletely returned in a query, the return value of the NextToken parameter is not empty. In this case, you can specify a valid value for the NextToken parameter to continue the query.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.entries:
            for k in self.entries:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Entries'] = []
        if self.entries is not None:
            for k in self.entries:
                result['Entries'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.entries = []
        if m.get('Entries') is not None:
            for k in m.get('Entries'):
                temp_model = ListRecycledDirectoriesAndFilesResponseBodyEntries()
                self.entries.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListRecycledDirectoriesAndFilesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRecycledDirectoriesAndFilesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListRecycledDirectoriesAndFilesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        # 
        # Limits:
        # 
        # *   The tag key cannot be left empty.
        # *   Valid values of N: 1 to 20.
        # *   The tag key must be 1 to 128 characters in length.
        # *   The tag key cannot start with `aliyun` or `acs:`.
        # *   The tag key cannot contain `http://` or `https://`.
        self.key = key
        # The tag value.
        # 
        # Limits:
        # 
        # *   Valid values of N: 1 to 20.
        # *   The tag value must be 1 to 128 characters in length.
        # *   The tag value cannot start with `aliyun` or `acs:`.
        # *   The tag value cannot contain `http://` or `https://`.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListTagResourcesRequest(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag: List[ListTagResourcesRequestTag] = None,
    ):
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The resource IDs.
        self.resource_id = resource_id
        # The resource type. Set the value to filesystem.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The details about the tags.
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBodyTagResourcesTagResource(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The resource ID.
        self.resource_id = resource_id
        # The resource type.
        self.resource_type = resource_type
        # The tag key.
        self.tag_key = tag_key
        # The tag value.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(
        self,
        tag_resource: List[ListTagResourcesResponseBodyTagResourcesTagResource] = None,
    ):
        self.tag_resource = tag_resource

    def validate(self):
        if self.tag_resource:
            for k in self.tag_resource:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TagResource'] = []
        if self.tag_resource is not None:
            for k in self.tag_resource:
                result['TagResource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag_resource = []
        if m.get('TagResource') is not None:
            for k in m.get('TagResource'):
                temp_model = ListTagResourcesResponseBodyTagResourcesTagResource()
                self.tag_resource.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        tag_resources: ListTagResourcesResponseBodyTagResources = None,
    ):
        # A pagination token. It can be used in the next request to retrieve a new page of results. If the value of this parameter is null, no queries are performed after the current query.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The list of resources.
        self.tag_resources = tag_resources

    def validate(self):
        if self.tag_resources:
            self.tag_resources.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tag_resources is not None:
            result['TagResources'] = self.tag_resources.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TagResources') is not None:
            temp_model = ListTagResourcesResponseBodyTagResources()
            self.tag_resources = temp_model.from_map(m['TagResources'])
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAccessGroupRequest(TeaModel):
    def __init__(
        self,
        access_group_name: str = None,
        description: str = None,
        file_system_type: str = None,
    ):
        # The name of the permission group.
        # 
        # Limits:
        # 
        # *   The name must be 3 to 64 characters in length.
        # *   The name must start with a letter and can contain letters, digits, underscores (_), and hyphens (-).
        # 
        # This parameter is required.
        self.access_group_name = access_group_name
        # The description of the permission group.
        # 
        # Limits:
        # 
        # *   By default, the description of the permission group is the same as the name of the permission group. The description must be 2 to 128 characters in length.
        # *   The description must start with a letter and cannot start with `http://` or `https://`.
        # *   The description can contain digits, colons (:), underscores (_), and hyphens (-).
        self.description = description
        # The type of the file system.
        # 
        # Valid values:
        # 
        # *   standard (default): General-purpose NAS file system
        # *   extreme: Extreme NAS file system
        self.file_system_type = file_system_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group_name is not None:
            result['AccessGroupName'] = self.access_group_name
        if self.description is not None:
            result['Description'] = self.description
        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessGroupName') is not None:
            self.access_group_name = m.get('AccessGroupName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')
        return self


class ModifyAccessGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyAccessGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyAccessGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyAccessGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAccessPointRequest(TeaModel):
    def __init__(
        self,
        access_group: str = None,
        access_point_id: str = None,
        access_point_name: str = None,
        enabled_ram: bool = None,
        file_system_id: str = None,
    ):
        # The name of the permission group.
        # 
        # This parameter is required for a General-purpose File Storage NAS (NAS) file system.
        # 
        # The default permission group for virtual private clouds (VPCs) is named DEFAULT_VPC_GROUP_NAME.
        self.access_group = access_group
        # The ID of the access point.
        # 
        # This parameter is required.
        self.access_point_id = access_point_id
        # The name of the access point.
        self.access_point_name = access_point_name
        # Specifies whether to enable the Resource Access Management (RAM) policy. Valid values:
        # 
        # *   true: The RAM policy is enabled.
        # *   false (default): The RAM policy is disabled.
        # 
        # >  After the RAM policy is enabled for access points, no RAM user is allowed to use access points to mount and access data by default. To use access points to mount and access data as a RAM user, you must grant the related access permissions to the RAM user. If the RAM policy is disabled, access points can be anonymously mounted.
        self.enabled_ram = enabled_ram
        # The ID of the file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group is not None:
            result['AccessGroup'] = self.access_group
        if self.access_point_id is not None:
            result['AccessPointId'] = self.access_point_id
        if self.access_point_name is not None:
            result['AccessPointName'] = self.access_point_name
        if self.enabled_ram is not None:
            result['EnabledRam'] = self.enabled_ram
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessGroup') is not None:
            self.access_group = m.get('AccessGroup')
        if m.get('AccessPointId') is not None:
            self.access_point_id = m.get('AccessPointId')
        if m.get('AccessPointName') is not None:
            self.access_point_name = m.get('AccessPointName')
        if m.get('EnabledRam') is not None:
            self.enabled_ram = m.get('EnabledRam')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        return self


class ModifyAccessPointResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        # 
        # This parameter is required.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyAccessPointResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyAccessPointResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyAccessPointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAccessRuleRequest(TeaModel):
    def __init__(
        self,
        access_group_name: str = None,
        access_rule_id: str = None,
        file_system_type: str = None,
        ipv_6source_cidr_ip: str = None,
        priority: int = None,
        rwaccess_type: str = None,
        source_cidr_ip: str = None,
        user_access_type: str = None,
    ):
        # The name of the permission group.
        # 
        # This parameter is required.
        self.access_group_name = access_group_name
        # The rule ID.
        # 
        # This parameter is required.
        self.access_rule_id = access_rule_id
        # The type of the file system.
        # 
        # Valid values:
        # 
        # *   standard (default): General-purpose NAS file system
        # *   extreme: Extreme NAS file system
        self.file_system_type = file_system_type
        # The IPv6 address or CIDR block of the authorized object.
        # 
        # You must set this parameter to an IPv6 IP address or CIDR block.
        # 
        # > *   Only Extreme NAS file systems that reside in the China (Hohhot) region support IPv6.
        # >*   Only permission groups that reside in virtual private clouds (VPCs) support IPv6.
        # >*   This parameter is unavailable if you specify the SourceCidrIp parameter.
        self.ipv_6source_cidr_ip = ipv_6source_cidr_ip
        # The priority of the rule.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 1, which indicates the highest priority.
        self.priority = priority
        # The access permissions of the authorized object on the file system.
        # 
        # Valid values:
        # 
        # *   RDWR (default): the read and write permissions
        # *   RDONLY: the read-only permissions
        self.rwaccess_type = rwaccess_type
        # The IP address or CIDR block of the authorized object.
        # 
        # You must set this parameter to an IP address or CIDR block.
        self.source_cidr_ip = source_cidr_ip
        # The access permissions for different types of users in the authorized object.
        # 
        # Valid values:
        # 
        # *   no_squash: allows access from root users to the file system.
        # *   root_squash: grants root users the least permissions as the nobody user.
        # *   all_squash: grants all users the least permissions as the nobody user.
        # 
        # The nobody user has the least permissions in Linux and can access only the public content of the file system. This ensures the security of the file system.
        self.user_access_type = user_access_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group_name is not None:
            result['AccessGroupName'] = self.access_group_name
        if self.access_rule_id is not None:
            result['AccessRuleId'] = self.access_rule_id
        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type
        if self.ipv_6source_cidr_ip is not None:
            result['Ipv6SourceCidrIp'] = self.ipv_6source_cidr_ip
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.rwaccess_type is not None:
            result['RWAccessType'] = self.rwaccess_type
        if self.source_cidr_ip is not None:
            result['SourceCidrIp'] = self.source_cidr_ip
        if self.user_access_type is not None:
            result['UserAccessType'] = self.user_access_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessGroupName') is not None:
            self.access_group_name = m.get('AccessGroupName')
        if m.get('AccessRuleId') is not None:
            self.access_rule_id = m.get('AccessRuleId')
        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')
        if m.get('Ipv6SourceCidrIp') is not None:
            self.ipv_6source_cidr_ip = m.get('Ipv6SourceCidrIp')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('RWAccessType') is not None:
            self.rwaccess_type = m.get('RWAccessType')
        if m.get('SourceCidrIp') is not None:
            self.source_cidr_ip = m.get('SourceCidrIp')
        if m.get('UserAccessType') is not None:
            self.user_access_type = m.get('UserAccessType')
        return self


class ModifyAccessRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyAccessRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyAccessRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyAccessRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAutoSnapshotPolicyRequest(TeaModel):
    def __init__(
        self,
        auto_snapshot_policy_id: str = None,
        auto_snapshot_policy_name: str = None,
        repeat_weekdays: str = None,
        retention_days: int = None,
        time_points: str = None,
    ):
        # The ID of the automatic snapshot policy.
        # 
        # You can call the DescribeAutoSnapshotPolicies operation to view available automatic snapshot policies.
        # 
        # This parameter is required.
        self.auto_snapshot_policy_id = auto_snapshot_policy_id
        # The name of the automatic snapshot policy. If you do not specify this parameter, the policy name is not changed.
        # 
        # Limits:
        # 
        # *   The name must be 2 to 128 characters in length.
        # *   The name must start with a letter.
        # *   The name can contain digits, letters, colons (:), underscores (_), and hyphens (-). It cannot start with `http://` or `https://`.
        self.auto_snapshot_policy_name = auto_snapshot_policy_name
        # The days of a week on which auto snapshots are created.
        # 
        # Cycle: week.
        # 
        # Valid values: 1 to 7. The value 1 indicates Monday. If you want to create multiple auto snapshots within a week, you can specify multiple days from Monday to Sunday and separate the days with commas (,). You can specify a maximum of seven days.
        self.repeat_weekdays = repeat_weekdays
        # The retention period of auto snapshots.
        # 
        # Unit: days.
        # 
        # Valid values:
        # 
        # *   \\-1 (default): Auto snapshots are permanently retained. After the number of auto snapshots exceeds the upper limit, the earliest auto snapshot is automatically deleted.
        # *   1 to 65536: Auto snapshots are retained for the specified number of days. After the retention period of auto snapshots expires, the auto snapshots are automatically deleted.
        self.retention_days = retention_days
        # The points in time at which auto snapshots are created.
        # 
        # Unit: hours.
        # 
        # Valid values: 0 to 23. The values from 0 to 23 indicate a total of 24 hours from 00:00 to 23:00. For example, the value 1 indicates 01:00. If you want to create multiple auto snapshots within a day, you can specify multiple points in time and separate the points in time with commas (,). You can specify a maximum of 24 points in time.
        self.time_points = time_points

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_snapshot_policy_id is not None:
            result['AutoSnapshotPolicyId'] = self.auto_snapshot_policy_id
        if self.auto_snapshot_policy_name is not None:
            result['AutoSnapshotPolicyName'] = self.auto_snapshot_policy_name
        if self.repeat_weekdays is not None:
            result['RepeatWeekdays'] = self.repeat_weekdays
        if self.retention_days is not None:
            result['RetentionDays'] = self.retention_days
        if self.time_points is not None:
            result['TimePoints'] = self.time_points
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoSnapshotPolicyId') is not None:
            self.auto_snapshot_policy_id = m.get('AutoSnapshotPolicyId')
        if m.get('AutoSnapshotPolicyName') is not None:
            self.auto_snapshot_policy_name = m.get('AutoSnapshotPolicyName')
        if m.get('RepeatWeekdays') is not None:
            self.repeat_weekdays = m.get('RepeatWeekdays')
        if m.get('RetentionDays') is not None:
            self.retention_days = m.get('RetentionDays')
        if m.get('TimePoints') is not None:
            self.time_points = m.get('TimePoints')
        return self


class ModifyAutoSnapshotPolicyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        # 
        # Every response returns a unique request ID regardless of whether the request is successful.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyAutoSnapshotPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyAutoSnapshotPolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyAutoSnapshotPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDataFlowRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        data_flow_id: str = None,
        description: str = None,
        dry_run: bool = None,
        file_system_id: str = None,
        throughput: int = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.
        # 
        # The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How do I ensure the idempotence?](https://help.aliyun.com/document_detail/25693.html)
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The value of RequestId may be different for each API request.
        self.client_token = client_token
        # The dataflow ID.
        # 
        # This parameter is required.
        self.data_flow_id = data_flow_id
        # The description of the dataflow.
        # 
        # Limits:
        # 
        # *   The description must be 2 to 128 characters in length.
        # *   The description must start with a letter but cannot start with http:// or https://.
        # *   The description can contain letters, digits, colons (:), underscores (_), and hyphens (-).
        self.description = description
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
        # *   The IDs of CPFS file systems must start with `cpfs-`. Example: cpfs-125487\\*\\*\\*\\*.
        # *   The IDs of CPFS for LINGJUN file systems must start with `bmcpfs-`. Example: bmcpfs-0015\\*\\*\\*\\*.
        # 
        # >  CPFS is not supported on the international site.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The maximum data flow throughput. Unit: MB/s. Valid values:
        # 
        # *   600
        # *   1200
        # *   1500
        # 
        # >  The data flow throughput must be less than the I/O throughput of the file system. This parameter is required for CPFS file systems.
        self.throughput = throughput

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.data_flow_id is not None:
            result['DataFlowId'] = self.data_flow_id
        if self.description is not None:
            result['Description'] = self.description
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.throughput is not None:
            result['Throughput'] = self.throughput
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DataFlowId') is not None:
            self.data_flow_id = m.get('DataFlowId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('Throughput') is not None:
            self.throughput = m.get('Throughput')
        return self


class ModifyDataFlowResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyDataFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyDataFlowResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyDataFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDataFlowAutoRefreshRequest(TeaModel):
    def __init__(
        self,
        auto_refresh_interval: int = None,
        auto_refresh_policy: str = None,
        client_token: str = None,
        data_flow_id: str = None,
        dry_run: bool = None,
        file_system_id: str = None,
    ):
        # The automatic update interval. CPFS checks whether data is updated in the directory at the interval. If data is updated, CPFS runs an AutoRefresh task. Unit: minutes.
        # 
        # Valid values: 5 to 526600. Default value: 10.
        self.auto_refresh_interval = auto_refresh_interval
        # The automatic update policy. CPFS imports data updates in the Object Storage Service (OSS) bucket to the CPFS file system based on this policy. Valid values:
        # 
        # *   None: CPFS does not automatically import data updates in the OSS bucket to the CPFS file system. You can import the data updates by using a dataflow task.
        # *   ImportChanged: CPFS automatically imports data updates in the OSS bucket to the CPFS file system.
        self.auto_refresh_policy = auto_refresh_policy
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.
        # 
        # The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How do I ensure the idempotence?](https://help.aliyun.com/document_detail/25693.html)
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The value of RequestId may be different for each API request.
        self.client_token = client_token
        # The dataflow ID.
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
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_refresh_interval is not None:
            result['AutoRefreshInterval'] = self.auto_refresh_interval
        if self.auto_refresh_policy is not None:
            result['AutoRefreshPolicy'] = self.auto_refresh_policy
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
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DataFlowId') is not None:
            self.data_flow_id = m.get('DataFlowId')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        return self


class ModifyDataFlowAutoRefreshResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyDataFlowAutoRefreshResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyDataFlowAutoRefreshResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyDataFlowAutoRefreshResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyFileSystemRequestOptions(TeaModel):
    def __init__(
        self,
        enable_oplock: bool = None,
    ):
        # Specifies whether to enable the oplock feature. Valid values:
        # 
        # *   true: enables the feature.
        # *   false: disables the feature.
        # 
        # >  Only Server Message Block (SMB) file systems support this feature.
        self.enable_oplock = enable_oplock

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_oplock is not None:
            result['EnableOplock'] = self.enable_oplock
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableOplock') is not None:
            self.enable_oplock = m.get('EnableOplock')
        return self


class ModifyFileSystemRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        file_system_id: str = None,
        options: ModifyFileSystemRequestOptions = None,
    ):
        # The description of the file system.
        # 
        # Limits:
        # 
        # *   The description must be 2 to 128 characters in length.
        # *   It must start with a letter but cannot start with `http://` or `https://`.
        # *   The description can contain letters, digits, colons (:), underscores (_), and hyphens (-).
        self.description = description
        # The ID of the file system.
        # 
        # *   Sample ID of a General-purpose NAS file system: `31a8e4****`.
        # *   The IDs of Extreme NAS file systems must start with `extreme-`. Example: `extreme-0015****`.
        # *   The IDs of Cloud Paralleled File System (CPFS) file systems must start with `cpfs-`. Example: `cpfs-125487****`.
        # >CPFS file systems are available only on the China site (aliyun.com).
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The options.
        self.options = options

    def validate(self):
        if self.options:
            self.options.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.options is not None:
            result['Options'] = self.options.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('Options') is not None:
            temp_model = ModifyFileSystemRequestOptions()
            self.options = temp_model.from_map(m['Options'])
        return self


class ModifyFileSystemShrinkRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        file_system_id: str = None,
        options_shrink: str = None,
    ):
        # The description of the file system.
        # 
        # Limits:
        # 
        # *   The description must be 2 to 128 characters in length.
        # *   It must start with a letter but cannot start with `http://` or `https://`.
        # *   The description can contain letters, digits, colons (:), underscores (_), and hyphens (-).
        self.description = description
        # The ID of the file system.
        # 
        # *   Sample ID of a General-purpose NAS file system: `31a8e4****`.
        # *   The IDs of Extreme NAS file systems must start with `extreme-`. Example: `extreme-0015****`.
        # *   The IDs of Cloud Paralleled File System (CPFS) file systems must start with `cpfs-`. Example: `cpfs-125487****`.
        # >CPFS file systems are available only on the China site (aliyun.com).
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The options.
        self.options_shrink = options_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.options_shrink is not None:
            result['Options'] = self.options_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('Options') is not None:
            self.options_shrink = m.get('Options')
        return self


class ModifyFileSystemResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyFileSystemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyFileSystemResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyFileSystemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyFilesetRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        deletion_protection: bool = None,
        description: str = None,
        dry_run: bool = None,
        file_system_id: str = None,
        fset_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.
        # 
        # The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How do I ensure the idempotence?](https://help.aliyun.com/document_detail/25693.html)
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token
        # Specifies whether to enable deletion protection to allow you to release the fileset by using the console or by calling the [DeleteFileset](https://help.aliyun.com/document_detail/2838077.html) operation.
        # 
        # *   true: enables release protection.
        # *   false: disables release protection.
        # 
        # >  This parameter can protect filesets only against manual releases, but not against automatic releases.
        self.deletion_protection = deletion_protection
        # The fileset description.
        self.description = description
        # Specifies whether to perform only a dry run, without performing the actual request.
        # 
        # During the dry run, the system checks whether the request parameters are valid and whether the requested resources are available. During the dry run, no fileset is modified and no fees incurred.
        # 
        # Valid values:
        # 
        # *   true: performs only a dry run. The system checks the required parameters, request syntax, service limits, and Apsara File Storage NAS (NAS) inventory data. If the request fails the dry run, an error message is returned. If the request passes the dry run, the HTTP status code 200 is returned.
        # *   false (default): performs a dry run and sends the request. If the request passes the dry run, the specified fileset is modified.
        self.dry_run = dry_run
        # The ID of the file system.
        # 
        # *   The IDs of CPFS file systems must start with `cpfs-`. Example: cpfs-099394bd928c\\*\\*\\*\\*.
        # *   The IDs of CPFS for LINGJUN file systems must start with `bmcpfs-`. Example: bmcpfs-290w65p03ok64ya\\*\\*\\*\\*.
        # 
        # >  CPFS is not supported on the international site.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The fileset ID.
        # 
        # This parameter is required.
        self.fset_id = fset_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.deletion_protection is not None:
            result['DeletionProtection'] = self.deletion_protection
        if self.description is not None:
            result['Description'] = self.description
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.fset_id is not None:
            result['FsetId'] = self.fset_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DeletionProtection') is not None:
            self.deletion_protection = m.get('DeletionProtection')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('FsetId') is not None:
            self.fset_id = m.get('FsetId')
        return self


class ModifyFilesetResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyFilesetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyFilesetResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyFilesetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyLDAPConfigRequest(TeaModel):
    def __init__(
        self,
        bind_dn: str = None,
        file_system_id: str = None,
        search_base: str = None,
        uri: str = None,
    ):
        # The LDAP entry.
        self.bind_dn = bind_dn
        # The ID of the file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The LDAP search base.
        # 
        # This parameter is required.
        self.search_base = search_base
        # The LDAP service address.
        # 
        # This parameter is required.
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bind_dn is not None:
            result['BindDN'] = self.bind_dn
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.search_base is not None:
            result['SearchBase'] = self.search_base
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindDN') is not None:
            self.bind_dn = m.get('BindDN')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('SearchBase') is not None:
            self.search_base = m.get('SearchBase')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class ModifyLDAPConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyLDAPConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyLDAPConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyLDAPConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyLifecyclePolicyRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        lifecycle_policy_name: str = None,
        lifecycle_rule_name: str = None,
        path: str = None,
        storage_type: str = None,
    ):
        # The ID of the file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The name of the lifecycle policy.
        # 
        # The name must be 3 to 64 characters in length and can contain letters, digits, underscores (_), and hyphens (-). The name must start with a letter.
        # 
        # This parameter is required.
        self.lifecycle_policy_name = lifecycle_policy_name
        # The management rule that is associated with the lifecycle policy.
        # 
        # Valid values:
        # 
        # *   DEFAULT_ATIME_14: Files that are not accessed in the last 14 days are dumped to the IA storage medium.
        # *   DEFAULT_ATIME_30: Files that are not accessed in the last 30 days are dumped to the IA storage medium.
        # *   DEFAULT_ATIME_60: Files that are not accessed in the last 60 days are dumped to the IA storage medium.
        # *   DEFAULT_ATIME_90: Files that are not accessed in the last 90 days are dumped to the IA storage medium.
        self.lifecycle_rule_name = lifecycle_rule_name
        # The absolute path of a directory with which the lifecycle policy is associated.
        # 
        # The path must start with a forward slash (/) and must be a path that exists in the mount target.
        self.path = path
        # The storage type of the data that is dumped to the IA storage medium.
        # 
        # Default value: InfrequentAccess (IA).
        self.storage_type = storage_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.lifecycle_policy_name is not None:
            result['LifecyclePolicyName'] = self.lifecycle_policy_name
        if self.lifecycle_rule_name is not None:
            result['LifecycleRuleName'] = self.lifecycle_rule_name
        if self.path is not None:
            result['Path'] = self.path
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('LifecyclePolicyName') is not None:
            self.lifecycle_policy_name = m.get('LifecyclePolicyName')
        if m.get('LifecycleRuleName') is not None:
            self.lifecycle_rule_name = m.get('LifecycleRuleName')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        return self


class ModifyLifecyclePolicyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyLifecyclePolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyLifecyclePolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyLifecyclePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyMountTargetRequest(TeaModel):
    def __init__(
        self,
        access_group_name: str = None,
        dual_stack_mount_target_domain: str = None,
        file_system_id: str = None,
        mount_target_domain: str = None,
        status: str = None,
    ):
        # The name of the permission group that is attached to the mount target.
        self.access_group_name = access_group_name
        # The dual-stack (IPv4 and IPv6) domain name of the mount target.
        # 
        # >  Only Extreme NAS file systems that reside in the Chinese mainland support IPv6.
        self.dual_stack_mount_target_domain = dual_stack_mount_target_domain
        # The ID of the file system.
        # 
        # *   Sample ID of a General-purpose NAS file system: `31a8e4****`.
        # *   The IDs of Extreme NAS file systems must start with `extreme-`, for example, `extreme-0015****`.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The IPv4 domain name of the mount target.
        self.mount_target_domain = mount_target_domain
        # The status of the mount target.
        # 
        # Valid values:
        # 
        # *   Active: The mount target is available.
        # *   Inactive: The mount target is unavailable.
        # 
        # >  Only General-purpose File Storage NAS (NAS) file systems support changing the mount target status.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group_name is not None:
            result['AccessGroupName'] = self.access_group_name
        if self.dual_stack_mount_target_domain is not None:
            result['DualStackMountTargetDomain'] = self.dual_stack_mount_target_domain
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.mount_target_domain is not None:
            result['MountTargetDomain'] = self.mount_target_domain
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessGroupName') is not None:
            self.access_group_name = m.get('AccessGroupName')
        if m.get('DualStackMountTargetDomain') is not None:
            self.dual_stack_mount_target_domain = m.get('DualStackMountTargetDomain')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('MountTargetDomain') is not None:
            self.mount_target_domain = m.get('MountTargetDomain')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ModifyMountTargetResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyMountTargetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyMountTargetResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyMountTargetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyProtocolMountTargetRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        dry_run: bool = None,
        export_id: str = None,
        file_system_id: str = None,
        protocol_service_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.
        # 
        # The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How do I ensure the idempotence?](https://help.aliyun.com/document_detail/25693.html)
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token
        # The description of the export directory for the protocol service.
        # 
        # Limits:
        # 
        # *   The description must be 2 to 128 characters in length.
        # *   The description must start with a letter but cannot start with `http://` or `https://`.
        # *   The description can contain letters, digits, colons (:), underscores (_), and hyphens (-).
        self.description = description
        # Specifies whether to perform only a dry run, without performing the actual request. The dry run checks parameter validity and prerequisites. The dry run does not modify the specified export directory or incur fees.
        # 
        # Valid values:
        # 
        # *   true: performs only a dry run. The system checks the required parameters, request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the HTTP status code 200 is returned.
        # *   false (default): performs a dry run and sends the request.
        self.dry_run = dry_run
        # The ID of the export directory for the protocol service.
        # 
        # This parameter is required.
        self.export_id = export_id
        # The ID of the file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The ID of the protocol service.
        # 
        # This parameter is required.
        self.protocol_service_id = protocol_service_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.export_id is not None:
            result['ExportId'] = self.export_id
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.protocol_service_id is not None:
            result['ProtocolServiceId'] = self.protocol_service_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('ExportId') is not None:
            self.export_id = m.get('ExportId')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('ProtocolServiceId') is not None:
            self.protocol_service_id = m.get('ProtocolServiceId')
        return self


class ModifyProtocolMountTargetResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyProtocolMountTargetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyProtocolMountTargetResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyProtocolMountTargetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyProtocolServiceRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        dry_run: bool = None,
        file_system_id: str = None,
        protocol_service_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.
        # 
        # The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How do I ensure the idempotence?](https://help.aliyun.com/document_detail/25693.html)
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token
        # The description of the protocol service.
        # 
        # Limits:
        # 
        # *   The description must be 2 to 128 characters in length.
        # *   The description must start with a letter and cannot start with `http://` or `https://`.
        # *   The description can contain letters, digits, colons (:), underscores (_), and hyphens (-).
        self.description = description
        # Specifies whether to perform only a dry run, without performing the actual request. The dry run checks parameter validity and prerequisites. The dry run does not modify a file system or incur fees.
        # 
        # Valid values:
        # 
        # *   true: performs only a dry run and does not modify the protocol service. The system checks the request format, service limits, prerequisites, and whether the required parameters are specified. If the request fails the dry run, an error message is returned. If the request passes the dry run, a 200 HTTP status code is returned.
        # *   false (default): performs a dry run and performs the actual request. If the request passes the dry run, the service protocol is modified.
        self.dry_run = dry_run
        # The ID of the file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The ID of the protocol service.
        # 
        # This parameter is required.
        self.protocol_service_id = protocol_service_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.protocol_service_id is not None:
            result['ProtocolServiceId'] = self.protocol_service_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('ProtocolServiceId') is not None:
            self.protocol_service_id = m.get('ProtocolServiceId')
        return self


class ModifyProtocolServiceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyProtocolServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyProtocolServiceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyProtocolServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySmbAclRequest(TeaModel):
    def __init__(
        self,
        enable_anonymous_access: bool = None,
        encrypt_data: bool = None,
        file_system_id: str = None,
        home_dir_path: str = None,
        keytab: str = None,
        keytab_md_5: str = None,
        reject_unencrypted_access: bool = None,
        super_admin_sid: str = None,
    ):
        # Specifies whether to allow anonymous access. Valid values:
        # 
        # *   true: The file system allows anonymous access.
        # *   false (default): The file system denies anonymous access.
        self.enable_anonymous_access = enable_anonymous_access
        # Specifies whether to enable encryption in transit. Valid values:
        # 
        # *   true: enables encryption in transit.
        # *   false (default): disables encryption in transit.
        self.encrypt_data = encrypt_data
        # The ID of the file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The home directory of each user. Each user-specific home directory must meet the following requirements:
        # 
        # *   Each segment starts with a forward slash (/) or a backward slash (\\\\).
        # *   Each segment does not contain the following special characters: `<>":|?*`.
        # *   Each segment is 0 to 255 characters in length.
        # *   The total length is 0 to 32,767 characters.
        # 
        # For example, if you create a user named A and the home directory is `/home`, the file system automatically creates a directory named `/home/A` when User A logs on to the file system. If the `/home/A` directory already exists, the file system does not create the directory.
        # 
        # > User A must have the permissions to create folders in the \\home directory. Otherwise, the file system cannot create the `/home/A` directory when User A logs on to the file system.
        self.home_dir_path = home_dir_path
        # The string that is generated after the system encodes the keytab file by using Base64.
        self.keytab = keytab
        # The string that is generated after the system encodes the keytab file by using MD5.
        self.keytab_md_5 = keytab_md_5
        # Specifies whether to deny access from non-encrypted clients. Valid values:
        # 
        # *   true: The file system denies access from non-encrypted clients.
        # *   false (default): The file system allows access from non-encrypted clients.
        self.reject_unencrypted_access = reject_unencrypted_access
        # The ID of a super admin. The ID must meet the following requirements:
        # 
        # *   The ID starts with `S` and does not contain letters except S.
        # *   The ID contains at least three hyphens (-) as delimiters.
        # 
        # Examples: `S-1-5-22` and `S-1-5-22-23`.
        self.super_admin_sid = super_admin_sid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_anonymous_access is not None:
            result['EnableAnonymousAccess'] = self.enable_anonymous_access
        if self.encrypt_data is not None:
            result['EncryptData'] = self.encrypt_data
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.home_dir_path is not None:
            result['HomeDirPath'] = self.home_dir_path
        if self.keytab is not None:
            result['Keytab'] = self.keytab
        if self.keytab_md_5 is not None:
            result['KeytabMd5'] = self.keytab_md_5
        if self.reject_unencrypted_access is not None:
            result['RejectUnencryptedAccess'] = self.reject_unencrypted_access
        if self.super_admin_sid is not None:
            result['SuperAdminSid'] = self.super_admin_sid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableAnonymousAccess') is not None:
            self.enable_anonymous_access = m.get('EnableAnonymousAccess')
        if m.get('EncryptData') is not None:
            self.encrypt_data = m.get('EncryptData')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('HomeDirPath') is not None:
            self.home_dir_path = m.get('HomeDirPath')
        if m.get('Keytab') is not None:
            self.keytab = m.get('Keytab')
        if m.get('KeytabMd5') is not None:
            self.keytab_md_5 = m.get('KeytabMd5')
        if m.get('RejectUnencryptedAccess') is not None:
            self.reject_unencrypted_access = m.get('RejectUnencryptedAccess')
        if m.get('SuperAdminSid') is not None:
            self.super_admin_sid = m.get('SuperAdminSid')
        return self


class ModifySmbAclResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifySmbAclResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifySmbAclResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifySmbAclResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenNASServiceResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        order_id: str = None,
        request_id: str = None,
    ):
        # The details about the failed permission verification.
        self.access_denied_detail = access_denied_detail
        # The order ID.
        self.order_id = order_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OpenNASServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OpenNASServiceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OpenNASServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveClientFromBlackListRequest(TeaModel):
    def __init__(
        self,
        client_ip: str = None,
        client_token: str = None,
        file_system_id: str = None,
        region_id: str = None,
    ):
        # The IP address of a client to remove from the blacklist.
        # 
        # This parameter is required.
        self.client_ip = client_ip
        # This parameter ensures the idempotency of each request. A ClientToken is generated for each client. Make sure that each ClientToken is unique between different requests. The parameter can be a maximum of 64 characters in length and contain only ASCII characters.
        # 
        # For more information, see [How to ensure idempotence](https://www.alibabacloud.com/help/doc-detail/25693.htm).
        # 
        # This parameter is required.
        self.client_token = client_token
        # The ID of the file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The ID of the region where the file system resides.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_ip is not None:
            result['ClientIP'] = self.client_ip
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientIP') is not None:
            self.client_ip = m.get('ClientIP')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class RemoveClientFromBlackListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RemoveClientFromBlackListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveClientFromBlackListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RemoveClientFromBlackListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetFileSystemRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        snapshot_id: str = None,
    ):
        # The ID of the advanced Extreme NAS file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The snapshot ID.
        # 
        # This parameter is required.
        self.snapshot_id = snapshot_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        return self


class ResetFileSystemResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ResetFileSystemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ResetFileSystemResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ResetFileSystemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RetryLifecycleRetrieveJobRequest(TeaModel):
    def __init__(
        self,
        job_id: str = None,
    ):
        # The ID of the data retrieval task.
        # 
        # This parameter is required.
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class RetryLifecycleRetrieveJobResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RetryLifecycleRetrieveJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RetryLifecycleRetrieveJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RetryLifecycleRetrieveJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDirQuotaRequest(TeaModel):
    def __init__(
        self,
        file_count_limit: int = None,
        file_system_id: str = None,
        path: str = None,
        quota_type: str = None,
        size_limit: int = None,
        user_id: str = None,
        user_type: str = None,
    ):
        # The number of files that a user can create in the directory.
        # 
        # This number includes the number of files, subdirectories, and special files.
        # 
        # If you set the QuotaType parameter to Enforcement, you must specify at least one of the SizeLimit and FileCountLimit parameters.
        self.file_count_limit = file_count_limit
        # The ID of the file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The absolute path of the directory in the file system.
        # 
        # > *   You can set quotas only for the directories that have been created in a NAS file system. The path of the directory that you specify for a quota is the absolute path of the directory in the NAS file system, but not the local path of the compute node, such as an Elastic Compute Service (ECS) instance or a container.
        # > *   Directories whose names contain Chinese characters are not supported.
        # 
        # This parameter is required.
        self.path = path
        # The type of the quota.
        # 
        # Valid values:
        # 
        # *   Accounting: a statistical quota. If you set this parameter to Accounting, NAS calculates only the storage usage of the directory.
        # *   Enforcement: a restricted quota. If you set this parameter to Enforcement and the storage usage exceeds the quota, you can no longer create files or subdirectories for the directory, or write data to the directory.
        # 
        # This parameter is required.
        self.quota_type = quota_type
        # The size of files that a user can create in the directory.
        # 
        # Unit: GiB.
        # 
        # If you set the QuotaType parameter to Enforcement, you must specify at least one of the SizeLimit and FileCountLimit parameters.
        self.size_limit = size_limit
        # The UID or GID of the user for whom you want to set a directory quota.
        # 
        # This parameter is required and valid only if the UserType parameter is set to Uid or Gid.
        # 
        # Examples:
        # 
        # *   If you want to set a directory quota for a user whose UID is 500, set the UserType parameter to Uid and set the UserId parameter to 500.
        # *   If you want to set a directory quota for a user group whose GID is 100, set the UserType parameter to Gid and set the UserId parameter to 100.
        self.user_id = user_id
        # The type of the user.
        # 
        # Valid values:
        # 
        # *   Uid: user ID
        # *   Gid: user group ID
        # *   AllUsers: all users
        # 
        # This parameter is required.
        self.user_type = user_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_count_limit is not None:
            result['FileCountLimit'] = self.file_count_limit
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.path is not None:
            result['Path'] = self.path
        if self.quota_type is not None:
            result['QuotaType'] = self.quota_type
        if self.size_limit is not None:
            result['SizeLimit'] = self.size_limit
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileCountLimit') is not None:
            self.file_count_limit = m.get('FileCountLimit')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('QuotaType') is not None:
            self.quota_type = m.get('QuotaType')
        if m.get('SizeLimit') is not None:
            self.size_limit = m.get('SizeLimit')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class SetDirQuotaResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SetDirQuotaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetDirQuotaResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SetDirQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetFilesetQuotaRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        file_count_limit: int = None,
        file_system_id: str = None,
        fset_id: str = None,
        size_limit: int = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.
        # 
        # The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How do I ensure the idempotence?](https://help.aliyun.com/document_detail/25693.html)
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform a dry run. The dry run checks parameter validity and prerequisites. The dry run does not delete the specified quota or incur fees.
        # 
        # Valid values:
        # 
        # *   true: performs only a dry run. The system checks the required parameters, request syntax, and service limits. If the request fails the dry run, an error code is returned. If the request passes the dry run, the HTTP status code 200 is returned.
        # *   false (default): performs a dry run and sends the request. If the request passes the dry run, the quota is deleted.
        self.dry_run = dry_run
        # The limit of the file quantity of the quota. Valid values:
        # 
        # *   Minimum value: 10000.
        # *   Maximum value: 10000000000.
        self.file_count_limit = file_count_limit
        # The ID of the CPFS for LINGJUN file system. The IDs of CPFS for LINGJUN file systems must start with `bmcpfs-`. Example: bmcpfs-290w65p03ok64ya\\*\\*\\*\\*.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The fileset ID.
        # 
        # This parameter is required.
        self.fset_id = fset_id
        # The total capacity of the quota. Unit: bytes.
        # 
        # Valid values:
        # 
        # *   Minimum value: 10737418240 (10 GiB).
        # *   Step size: 1073741824 (1 GiB).
        self.size_limit = size_limit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.file_count_limit is not None:
            result['FileCountLimit'] = self.file_count_limit
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.fset_id is not None:
            result['FsetId'] = self.fset_id
        if self.size_limit is not None:
            result['SizeLimit'] = self.size_limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('FileCountLimit') is not None:
            self.file_count_limit = m.get('FileCountLimit')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('FsetId') is not None:
            self.fset_id = m.get('FsetId')
        if m.get('SizeLimit') is not None:
            self.size_limit = m.get('SizeLimit')
        return self


class SetFilesetQuotaResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetFilesetQuotaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetFilesetQuotaResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SetFilesetQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartDataFlowRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        data_flow_id: str = None,
        dry_run: bool = None,
        file_system_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.
        # 
        # The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How do I ensure the idempotence?](https://help.aliyun.com/document_detail/25693.html)
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token
        # The dataflow ID.
        # 
        # This parameter is required.
        self.data_flow_id = data_flow_id
        # Specifies whether to perform only a dry run, without performing the actual request.
        # 
        # During the dry run, the system checks whether the request parameters are valid and whether the requested resources are available. The dry run does not enable the specified dataflow or incur fees.
        # 
        # Valid values:
        # 
        # *   true: performs only a dry run. The system checks the required parameters, request syntax, service limits, and available NAS resources. If the request fails the dry run, an error message is returned. If the request passes the dry run, the HTTP status code 200 is returned.
        # *   false (default): performs a dry run and sends the request. If the request passes the dry run, the specified dataflow is enabled.
        self.dry_run = dry_run
        # The ID of the file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DataFlowId') is not None:
            self.data_flow_id = m.get('DataFlowId')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        return self


class StartDataFlowResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StartDataFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartDataFlowResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StartDataFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopDataFlowRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        data_flow_id: str = None,
        dry_run: bool = None,
        file_system_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.
        # 
        # The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How do I ensure the idempotence?](https://help.aliyun.com/document_detail/25693.html)
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The value of RequestId may be different for each API request.
        self.client_token = client_token
        # The dataflow ID.
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
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DataFlowId') is not None:
            self.data_flow_id = m.get('DataFlowId')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        return self


class StopDataFlowResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopDataFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopDataFlowResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StopDataFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N to add to the resource.
        # 
        # Limits:
        # 
        # *   The tag key cannot be left empty.
        # *   Valid values of N: 1 to 20.
        # *   The tag key must be 1 to 128 characters in length.
        # *   The tag key cannot start with `aliyun` or `acs:`.
        # *   The tag key cannot contain `http://` or `https://`.
        # 
        # This parameter is required.
        self.key = key
        # The value of tag N to add to the resource.
        # 
        # Limits:
        # 
        # *   Valid values of N: 1 to 20.
        # *   The tag value must be 1 to 128 characters in length.
        # *   The tag value cannot start with `aliyun` or `acs:`.
        # *   The tag value cannot contain `http://` or `https://`.
        # 
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class TagResourcesRequest(TeaModel):
    def __init__(
        self,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag: List[TagResourcesRequestTag] = None,
    ):
        # The resource IDs. Valid values of N: 1 to 50.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The resource type. Set the value to filesystem.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The details about the tags.
        # 
        # This parameter is required.
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class TagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(
        self,
        all: bool = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag_key: List[str] = None,
    ):
        # Specifies whether to remove all tags from the file system.
        # 
        # This parameter is valid only if the TagKey.N parameter is not specified.
        # 
        # Valid values:
        # 
        # *   true: All tags are removed from the file system. If the file system does not have tags, a success message is returned.
        # *   false (default): No tags are removed from the file system and a success message is returned.
        self.all = all
        # The resource IDs. Valid values of N: 1 to 50.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The resource type.
        # 
        # Set the value to filesystem.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The tag keys of the resources. Valid values of N: 1 to 20.
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class UntagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UntagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UntagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UntagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRecycleBinAttributeRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        reserved_days: int = None,
    ):
        # The ID of the file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The retention period of the files in the recycle bin. Unit: days.
        # 
        # Valid values: 1 to 180.
        # 
        # Default value: 3.
        # 
        # This parameter is required.
        self.reserved_days = reserved_days

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.reserved_days is not None:
            result['ReservedDays'] = self.reserved_days
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('ReservedDays') is not None:
            self.reserved_days = m.get('ReservedDays')
        return self


class UpdateRecycleBinAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateRecycleBinAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateRecycleBinAttributeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateRecycleBinAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeFileSystemRequest(TeaModel):
    def __init__(
        self,
        capacity: int = None,
        client_token: str = None,
        dry_run: bool = None,
        file_system_id: str = None,
    ):
        # The desired capacity of the file system.
        # 
        # The desired capacity of the file system must be greater than the original capacity of the file system. Unit: GiB.
        # 
        # This parameter is required.
        self.capacity = capacity
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.
        # 
        # The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How do I ensure the idempotence?](https://help.aliyun.com/document_detail/25693.html)
        # 
        # > If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token
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
        # *   The IDs of Extreme NAS file systems must start with `extreme-`, for example, extreme-0015\\*\\*\\*\\*.
        # *   The IDs of CPFS file systems must start with `cpfs-`, for example, cpfs-125487\\*\\*\\*\\*.
        # 
        # > CPFS file systems are available only on the China site (aliyun.com).
        # 
        # This parameter is required.
        self.file_system_id = file_system_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        return self


class UpgradeFileSystemResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpgradeFileSystemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpgradeFileSystemResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpgradeFileSystemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


