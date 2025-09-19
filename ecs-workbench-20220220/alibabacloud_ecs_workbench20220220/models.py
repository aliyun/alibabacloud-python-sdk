# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class GetInstanceRecordConfigRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetInstanceRecordConfigResponseBodyRoot(TeaModel):
    def __init__(
        self,
        expiration_days: int = None,
        instance_id: str = None,
        parent_id: str = None,
        record_storage_target: str = None,
    ):
        self.expiration_days = expiration_days
        self.instance_id = instance_id
        self.parent_id = parent_id
        self.record_storage_target = record_storage_target

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expiration_days is not None:
            result['ExpirationDays'] = self.expiration_days
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.record_storage_target is not None:
            result['RecordStorageTarget'] = self.record_storage_target
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpirationDays') is not None:
            self.expiration_days = m.get('ExpirationDays')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('RecordStorageTarget') is not None:
            self.record_storage_target = m.get('RecordStorageTarget')
        return self


class GetInstanceRecordConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        root: GetInstanceRecordConfigResponseBodyRoot = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.root = root
        self.success = success

    def validate(self):
        if self.root:
            self.root.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.root is not None:
            result['Root'] = self.root.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Root') is not None:
            temp_model = GetInstanceRecordConfigResponseBodyRoot()
            self.root = temp_model.from_map(m['Root'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetInstanceRecordConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetInstanceRecordConfigResponseBody = None,
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
            temp_model = GetInstanceRecordConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstanceRecordsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
    ):
        self.instance_id = instance_id
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListInstanceRecordsResponseBodyRootRecordList(TeaModel):
    def __init__(
        self,
        account_id: int = None,
        expire_time: str = None,
        gmt_create: str = None,
        instance_id: str = None,
        instance_record_url: str = None,
        record_duration_millis: int = None,
        status: str = None,
        terminal_session_token: str = None,
    ):
        self.account_id = account_id
        self.expire_time = expire_time
        self.gmt_create = gmt_create
        self.instance_id = instance_id
        self.instance_record_url = instance_record_url
        self.record_duration_millis = record_duration_millis
        self.status = status
        self.terminal_session_token = terminal_session_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_record_url is not None:
            result['InstanceRecordUrl'] = self.instance_record_url
        if self.record_duration_millis is not None:
            result['RecordDurationMillis'] = self.record_duration_millis
        if self.status is not None:
            result['Status'] = self.status
        if self.terminal_session_token is not None:
            result['TerminalSessionToken'] = self.terminal_session_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceRecordUrl') is not None:
            self.instance_record_url = m.get('InstanceRecordUrl')
        if m.get('RecordDurationMillis') is not None:
            self.record_duration_millis = m.get('RecordDurationMillis')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TerminalSessionToken') is not None:
            self.terminal_session_token = m.get('TerminalSessionToken')
        return self


class ListInstanceRecordsResponseBodyRoot(TeaModel):
    def __init__(
        self,
        record_list: List[ListInstanceRecordsResponseBodyRootRecordList] = None,
        total_count: int = None,
    ):
        self.record_list = record_list
        self.total_count = total_count

    def validate(self):
        if self.record_list:
            for k in self.record_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RecordList'] = []
        if self.record_list is not None:
            for k in self.record_list:
                result['RecordList'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.record_list = []
        if m.get('RecordList') is not None:
            for k in m.get('RecordList'):
                temp_model = ListInstanceRecordsResponseBodyRootRecordList()
                self.record_list.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListInstanceRecordsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        root: ListInstanceRecordsResponseBodyRoot = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.root = root
        self.success = success

    def validate(self):
        if self.root:
            self.root.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.root is not None:
            result['Root'] = self.root.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Root') is not None:
            temp_model = ListInstanceRecordsResponseBodyRoot()
            self.root = temp_model.from_map(m['Root'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListInstanceRecordsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListInstanceRecordsResponseBody = None,
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
            temp_model = ListInstanceRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTerminalCommandsRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        terminal_session_token: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        # This parameter is required.
        self.terminal_session_token = terminal_session_token

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
        if self.terminal_session_token is not None:
            result['TerminalSessionToken'] = self.terminal_session_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TerminalSessionToken') is not None:
            self.terminal_session_token = m.get('TerminalSessionToken')
        return self


class ListTerminalCommandsResponseBodyTerminalCommandList(TeaModel):
    def __init__(
        self,
        command_line: str = None,
        create_time: str = None,
        execute_path: str = None,
        login_user: str = None,
    ):
        self.command_line = command_line
        self.create_time = create_time
        self.execute_path = execute_path
        self.login_user = login_user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command_line is not None:
            result['CommandLine'] = self.command_line
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.execute_path is not None:
            result['ExecutePath'] = self.execute_path
        if self.login_user is not None:
            result['LoginUser'] = self.login_user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommandLine') is not None:
            self.command_line = m.get('CommandLine')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExecutePath') is not None:
            self.execute_path = m.get('ExecutePath')
        if m.get('LoginUser') is not None:
            self.login_user = m.get('LoginUser')
        return self


class ListTerminalCommandsResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        terminal_command_list: List[ListTerminalCommandsResponseBodyTerminalCommandList] = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.terminal_command_list = terminal_command_list
        self.total_count = total_count

    def validate(self):
        if self.terminal_command_list:
            for k in self.terminal_command_list:
                if k:
                    k.validate()

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
        result['TerminalCommandList'] = []
        if self.terminal_command_list is not None:
            for k in self.terminal_command_list:
                result['TerminalCommandList'].append(k.to_map() if k else None)
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
        self.terminal_command_list = []
        if m.get('TerminalCommandList') is not None:
            for k in m.get('TerminalCommandList'):
                temp_model = ListTerminalCommandsResponseBodyTerminalCommandList()
                self.terminal_command_list.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListTerminalCommandsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTerminalCommandsResponseBody = None,
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
            temp_model = ListTerminalCommandsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LoginInstanceRequestInstanceLoginInfoEncryptionOptions(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
        kmskey_id: str = None,
        mode: str = None,
    ):
        self.enabled = enabled
        self.kmskey_id = kmskey_id
        self.mode = mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.kmskey_id is not None:
            result['KMSKeyId'] = self.kmskey_id
        if self.mode is not None:
            result['Mode'] = self.mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('KMSKeyId') is not None:
            self.kmskey_id = m.get('KMSKeyId')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        return self


class LoginInstanceRequestInstanceLoginInfoOptionsContainerInfo(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_name: str = None,
        container_name: str = None,
        deployment: str = None,
        endpoint: str = None,
        headers: Dict[str, Any] = None,
        namespace: str = None,
        pod_name: str = None,
    ):
        self.cluster_id = cluster_id
        self.cluster_name = cluster_name
        self.container_name = container_name
        self.deployment = deployment
        self.endpoint = endpoint
        self.headers = headers
        self.namespace = namespace
        self.pod_name = pod_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.container_name is not None:
            result['ContainerName'] = self.container_name
        if self.deployment is not None:
            result['Deployment'] = self.deployment
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.headers is not None:
            result['Headers'] = self.headers
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.pod_name is not None:
            result['PodName'] = self.pod_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('ContainerName') is not None:
            self.container_name = m.get('ContainerName')
        if m.get('Deployment') is not None:
            self.deployment = m.get('Deployment')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('Headers') is not None:
            self.headers = m.get('Headers')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('PodName') is not None:
            self.pod_name = m.get('PodName')
        return self


class LoginInstanceRequestInstanceLoginInfoOptions(TeaModel):
    def __init__(
        self,
        audio_mute_seconds: int = None,
        container_info: LoginInstanceRequestInstanceLoginInfoOptionsContainerInfo = None,
        fixed_height: int = None,
        fixed_width: int = None,
        notification_event_types: str = None,
        notification_recipient_url: str = None,
        notification_retry_interval_seconds: int = None,
        notification_retry_limit: int = None,
        operation_disable_seconds: int = None,
        session_control: str = None,
        video_freeze_seconds: int = None,
    ):
        self.audio_mute_seconds = audio_mute_seconds
        self.container_info = container_info
        self.fixed_height = fixed_height
        self.fixed_width = fixed_width
        self.notification_event_types = notification_event_types
        self.notification_recipient_url = notification_recipient_url
        self.notification_retry_interval_seconds = notification_retry_interval_seconds
        self.notification_retry_limit = notification_retry_limit
        self.operation_disable_seconds = operation_disable_seconds
        self.session_control = session_control
        self.video_freeze_seconds = video_freeze_seconds

    def validate(self):
        if self.container_info:
            self.container_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audio_mute_seconds is not None:
            result['AudioMuteSeconds'] = self.audio_mute_seconds
        if self.container_info is not None:
            result['ContainerInfo'] = self.container_info.to_map()
        if self.fixed_height is not None:
            result['FixedHeight'] = self.fixed_height
        if self.fixed_width is not None:
            result['FixedWidth'] = self.fixed_width
        if self.notification_event_types is not None:
            result['NotificationEventTypes'] = self.notification_event_types
        if self.notification_recipient_url is not None:
            result['NotificationRecipientUrl'] = self.notification_recipient_url
        if self.notification_retry_interval_seconds is not None:
            result['NotificationRetryIntervalSeconds'] = self.notification_retry_interval_seconds
        if self.notification_retry_limit is not None:
            result['NotificationRetryLimit'] = self.notification_retry_limit
        if self.operation_disable_seconds is not None:
            result['OperationDisableSeconds'] = self.operation_disable_seconds
        if self.session_control is not None:
            result['SessionControl'] = self.session_control
        if self.video_freeze_seconds is not None:
            result['VideoFreezeSeconds'] = self.video_freeze_seconds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AudioMuteSeconds') is not None:
            self.audio_mute_seconds = m.get('AudioMuteSeconds')
        if m.get('ContainerInfo') is not None:
            temp_model = LoginInstanceRequestInstanceLoginInfoOptionsContainerInfo()
            self.container_info = temp_model.from_map(m['ContainerInfo'])
        if m.get('FixedHeight') is not None:
            self.fixed_height = m.get('FixedHeight')
        if m.get('FixedWidth') is not None:
            self.fixed_width = m.get('FixedWidth')
        if m.get('NotificationEventTypes') is not None:
            self.notification_event_types = m.get('NotificationEventTypes')
        if m.get('NotificationRecipientUrl') is not None:
            self.notification_recipient_url = m.get('NotificationRecipientUrl')
        if m.get('NotificationRetryIntervalSeconds') is not None:
            self.notification_retry_interval_seconds = m.get('NotificationRetryIntervalSeconds')
        if m.get('NotificationRetryLimit') is not None:
            self.notification_retry_limit = m.get('NotificationRetryLimit')
        if m.get('OperationDisableSeconds') is not None:
            self.operation_disable_seconds = m.get('OperationDisableSeconds')
        if m.get('SessionControl') is not None:
            self.session_control = m.get('SessionControl')
        if m.get('VideoFreezeSeconds') is not None:
            self.video_freeze_seconds = m.get('VideoFreezeSeconds')
        return self


class LoginInstanceRequestInstanceLoginInfo(TeaModel):
    def __init__(
        self,
        authentication_type: str = None,
        certificate: str = None,
        credential_token: str = None,
        docker_container_name: str = None,
        docker_exec: str = None,
        duration_seconds: int = None,
        encryption_options: LoginInstanceRequestInstanceLoginInfoEncryptionOptions = None,
        expire_time: str = None,
        host: str = None,
        instance_id: str = None,
        instance_type: str = None,
        login_by_instance_credential: bool = None,
        login_by_instance_shortcut: bool = None,
        network_access_mode: str = None,
        options: LoginInstanceRequestInstanceLoginInfoOptions = None,
        pass_phrase: str = None,
        password: str = None,
        port: int = None,
        protocol: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        shortcut_token: str = None,
        username: str = None,
        vpc_id: str = None,
    ):
        self.authentication_type = authentication_type
        self.certificate = certificate
        self.credential_token = credential_token
        self.docker_container_name = docker_container_name
        self.docker_exec = docker_exec
        self.duration_seconds = duration_seconds
        self.encryption_options = encryption_options
        self.expire_time = expire_time
        self.host = host
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.login_by_instance_credential = login_by_instance_credential
        self.login_by_instance_shortcut = login_by_instance_shortcut
        self.network_access_mode = network_access_mode
        self.options = options
        self.pass_phrase = pass_phrase
        self.password = password
        self.port = port
        self.protocol = protocol
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.shortcut_token = shortcut_token
        self.username = username
        self.vpc_id = vpc_id

    def validate(self):
        if self.encryption_options:
            self.encryption_options.validate()
        if self.options:
            self.options.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authentication_type is not None:
            result['AuthenticationType'] = self.authentication_type
        if self.certificate is not None:
            result['Certificate'] = self.certificate
        if self.credential_token is not None:
            result['CredentialToken'] = self.credential_token
        if self.docker_container_name is not None:
            result['DockerContainerName'] = self.docker_container_name
        if self.docker_exec is not None:
            result['DockerExec'] = self.docker_exec
        if self.duration_seconds is not None:
            result['DurationSeconds'] = self.duration_seconds
        if self.encryption_options is not None:
            result['EncryptionOptions'] = self.encryption_options.to_map()
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.host is not None:
            result['Host'] = self.host
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.login_by_instance_credential is not None:
            result['LoginByInstanceCredential'] = self.login_by_instance_credential
        if self.login_by_instance_shortcut is not None:
            result['LoginByInstanceShortcut'] = self.login_by_instance_shortcut
        if self.network_access_mode is not None:
            result['NetworkAccessMode'] = self.network_access_mode
        if self.options is not None:
            result['Options'] = self.options.to_map()
        if self.pass_phrase is not None:
            result['PassPhrase'] = self.pass_phrase
        if self.password is not None:
            result['Password'] = self.password
        if self.port is not None:
            result['Port'] = self.port
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.shortcut_token is not None:
            result['ShortcutToken'] = self.shortcut_token
        if self.username is not None:
            result['Username'] = self.username
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthenticationType') is not None:
            self.authentication_type = m.get('AuthenticationType')
        if m.get('Certificate') is not None:
            self.certificate = m.get('Certificate')
        if m.get('CredentialToken') is not None:
            self.credential_token = m.get('CredentialToken')
        if m.get('DockerContainerName') is not None:
            self.docker_container_name = m.get('DockerContainerName')
        if m.get('DockerExec') is not None:
            self.docker_exec = m.get('DockerExec')
        if m.get('DurationSeconds') is not None:
            self.duration_seconds = m.get('DurationSeconds')
        if m.get('EncryptionOptions') is not None:
            temp_model = LoginInstanceRequestInstanceLoginInfoEncryptionOptions()
            self.encryption_options = temp_model.from_map(m['EncryptionOptions'])
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('LoginByInstanceCredential') is not None:
            self.login_by_instance_credential = m.get('LoginByInstanceCredential')
        if m.get('LoginByInstanceShortcut') is not None:
            self.login_by_instance_shortcut = m.get('LoginByInstanceShortcut')
        if m.get('NetworkAccessMode') is not None:
            self.network_access_mode = m.get('NetworkAccessMode')
        if m.get('Options') is not None:
            temp_model = LoginInstanceRequestInstanceLoginInfoOptions()
            self.options = temp_model.from_map(m['Options'])
        if m.get('PassPhrase') is not None:
            self.pass_phrase = m.get('PassPhrase')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ShortcutToken') is not None:
            self.shortcut_token = m.get('ShortcutToken')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class LoginInstanceRequestPartnerInfo(TeaModel):
    def __init__(
        self,
        partner_id: str = None,
        partner_name: str = None,
    ):
        self.partner_id = partner_id
        self.partner_name = partner_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.partner_id is not None:
            result['PartnerId'] = self.partner_id
        if self.partner_name is not None:
            result['PartnerName'] = self.partner_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PartnerId') is not None:
            self.partner_id = m.get('PartnerId')
        if m.get('PartnerName') is not None:
            self.partner_name = m.get('PartnerName')
        return self


class LoginInstanceRequestUserAccountOptions(TeaModel):
    def __init__(
        self,
        login_limit: int = None,
    ):
        self.login_limit = login_limit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.login_limit is not None:
            result['LoginLimit'] = self.login_limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoginLimit') is not None:
            self.login_limit = m.get('LoginLimit')
        return self


class LoginInstanceRequestUserAccount(TeaModel):
    def __init__(
        self,
        account_id: int = None,
        account_platform: str = None,
        account_structure: str = None,
        duration_seconds: int = None,
        emp_id: str = None,
        expire_time: str = None,
        login_name: str = None,
        options: LoginInstanceRequestUserAccountOptions = None,
        parent_id: int = None,
    ):
        self.account_id = account_id
        self.account_platform = account_platform
        self.account_structure = account_structure
        self.duration_seconds = duration_seconds
        self.emp_id = emp_id
        self.expire_time = expire_time
        self.login_name = login_name
        self.options = options
        self.parent_id = parent_id

    def validate(self):
        if self.options:
            self.options.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.account_platform is not None:
            result['AccountPlatform'] = self.account_platform
        if self.account_structure is not None:
            result['AccountStructure'] = self.account_structure
        if self.duration_seconds is not None:
            result['DurationSeconds'] = self.duration_seconds
        if self.emp_id is not None:
            result['EmpId'] = self.emp_id
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.login_name is not None:
            result['LoginName'] = self.login_name
        if self.options is not None:
            result['Options'] = self.options.to_map()
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AccountPlatform') is not None:
            self.account_platform = m.get('AccountPlatform')
        if m.get('AccountStructure') is not None:
            self.account_structure = m.get('AccountStructure')
        if m.get('DurationSeconds') is not None:
            self.duration_seconds = m.get('DurationSeconds')
        if m.get('EmpId') is not None:
            self.emp_id = m.get('EmpId')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('LoginName') is not None:
            self.login_name = m.get('LoginName')
        if m.get('Options') is not None:
            temp_model = LoginInstanceRequestUserAccountOptions()
            self.options = temp_model.from_map(m['Options'])
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        return self


class LoginInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_login_info: LoginInstanceRequestInstanceLoginInfo = None,
        partner_info: LoginInstanceRequestPartnerInfo = None,
        user_account: LoginInstanceRequestUserAccount = None,
    ):
        self.instance_login_info = instance_login_info
        self.partner_info = partner_info
        self.user_account = user_account

    def validate(self):
        if self.instance_login_info:
            self.instance_login_info.validate()
        if self.partner_info:
            self.partner_info.validate()
        if self.user_account:
            self.user_account.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_login_info is not None:
            result['InstanceLoginInfo'] = self.instance_login_info.to_map()
        if self.partner_info is not None:
            result['PartnerInfo'] = self.partner_info.to_map()
        if self.user_account is not None:
            result['UserAccount'] = self.user_account.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceLoginInfo') is not None:
            temp_model = LoginInstanceRequestInstanceLoginInfo()
            self.instance_login_info = temp_model.from_map(m['InstanceLoginInfo'])
        if m.get('PartnerInfo') is not None:
            temp_model = LoginInstanceRequestPartnerInfo()
            self.partner_info = temp_model.from_map(m['PartnerInfo'])
        if m.get('UserAccount') is not None:
            temp_model = LoginInstanceRequestUserAccount()
            self.user_account = temp_model.from_map(m['UserAccount'])
        return self


class LoginInstanceResponseBodyRootDisposableAccount(TeaModel):
    def __init__(
        self,
        login_form_action_url: str = None,
        login_url: str = None,
    ):
        self.login_form_action_url = login_form_action_url
        self.login_url = login_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.login_form_action_url is not None:
            result['LoginFormActionUrl'] = self.login_form_action_url
        if self.login_url is not None:
            result['LoginUrl'] = self.login_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoginFormActionUrl') is not None:
            self.login_form_action_url = m.get('LoginFormActionUrl')
        if m.get('LoginUrl') is not None:
            self.login_url = m.get('LoginUrl')
        return self


class LoginInstanceResponseBodyRootInstanceLoginInfoListInstanceLoginView(TeaModel):
    def __init__(
        self,
        default_view_url: str = None,
    ):
        self.default_view_url = default_view_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_view_url is not None:
            result['DefaultViewUrl'] = self.default_view_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultViewUrl') is not None:
            self.default_view_url = m.get('DefaultViewUrl')
        return self


class LoginInstanceResponseBodyRootInstanceLoginInfoList(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_login_token: str = None,
        instance_login_view: LoginInstanceResponseBodyRootInstanceLoginInfoListInstanceLoginView = None,
        login_success: bool = None,
    ):
        self.instance_id = instance_id
        self.instance_login_token = instance_login_token
        self.instance_login_view = instance_login_view
        self.login_success = login_success

    def validate(self):
        if self.instance_login_view:
            self.instance_login_view.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_login_token is not None:
            result['InstanceLoginToken'] = self.instance_login_token
        if self.instance_login_view is not None:
            result['InstanceLoginView'] = self.instance_login_view.to_map()
        if self.login_success is not None:
            result['LoginSuccess'] = self.login_success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceLoginToken') is not None:
            self.instance_login_token = m.get('InstanceLoginToken')
        if m.get('InstanceLoginView') is not None:
            temp_model = LoginInstanceResponseBodyRootInstanceLoginInfoListInstanceLoginView()
            self.instance_login_view = temp_model.from_map(m['InstanceLoginView'])
        if m.get('LoginSuccess') is not None:
            self.login_success = m.get('LoginSuccess')
        return self


class LoginInstanceResponseBodyRootSessionControl(TeaModel):
    def __init__(
        self,
        base_url: str = None,
    ):
        self.base_url = base_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_url is not None:
            result['BaseUrl'] = self.base_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseUrl') is not None:
            self.base_url = m.get('BaseUrl')
        return self


class LoginInstanceResponseBodyRoot(TeaModel):
    def __init__(
        self,
        disposable_account: LoginInstanceResponseBodyRootDisposableAccount = None,
        instance_login_info_list: List[LoginInstanceResponseBodyRootInstanceLoginInfoList] = None,
        session_control: LoginInstanceResponseBodyRootSessionControl = None,
    ):
        self.disposable_account = disposable_account
        self.instance_login_info_list = instance_login_info_list
        self.session_control = session_control

    def validate(self):
        if self.disposable_account:
            self.disposable_account.validate()
        if self.instance_login_info_list:
            for k in self.instance_login_info_list:
                if k:
                    k.validate()
        if self.session_control:
            self.session_control.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disposable_account is not None:
            result['DisposableAccount'] = self.disposable_account.to_map()
        result['InstanceLoginInfoList'] = []
        if self.instance_login_info_list is not None:
            for k in self.instance_login_info_list:
                result['InstanceLoginInfoList'].append(k.to_map() if k else None)
        if self.session_control is not None:
            result['SessionControl'] = self.session_control.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisposableAccount') is not None:
            temp_model = LoginInstanceResponseBodyRootDisposableAccount()
            self.disposable_account = temp_model.from_map(m['DisposableAccount'])
        self.instance_login_info_list = []
        if m.get('InstanceLoginInfoList') is not None:
            for k in m.get('InstanceLoginInfoList'):
                temp_model = LoginInstanceResponseBodyRootInstanceLoginInfoList()
                self.instance_login_info_list.append(temp_model.from_map(k))
        if m.get('SessionControl') is not None:
            temp_model = LoginInstanceResponseBodyRootSessionControl()
            self.session_control = temp_model.from_map(m['SessionControl'])
        return self


class LoginInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        root: LoginInstanceResponseBodyRoot = None,
        success: str = None,
    ):
        self.code = code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.root = root
        self.success = success

    def validate(self):
        if self.root:
            self.root.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.root is not None:
            result['Root'] = self.root.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Root') is not None:
            temp_model = LoginInstanceResponseBodyRoot()
            self.root = temp_model.from_map(m['Root'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class LoginInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: LoginInstanceResponseBody = None,
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
            temp_model = LoginInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetInstanceRecordConfigRequest(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
        expiration_days: int = None,
        instance_id: str = None,
        record_storage_target: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.enabled = enabled
        self.expiration_days = expiration_days
        # This parameter is required.
        self.instance_id = instance_id
        self.record_storage_target = record_storage_target
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.expiration_days is not None:
            result['ExpirationDays'] = self.expiration_days
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.record_storage_target is not None:
            result['RecordStorageTarget'] = self.record_storage_target
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('ExpirationDays') is not None:
            self.expiration_days = m.get('ExpirationDays')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RecordStorageTarget') is not None:
            self.record_storage_target = m.get('RecordStorageTarget')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class SetInstanceRecordConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        root: bool = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.root = root
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.root is not None:
            result['Root'] = self.root
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Root') is not None:
            self.root = m.get('Root')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SetInstanceRecordConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetInstanceRecordConfigResponseBody = None,
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
            temp_model = SetInstanceRecordConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ViewInstanceRecordsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
        terminal_session_token: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        self.region_id = region_id
        # This parameter is required.
        self.terminal_session_token = terminal_session_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.terminal_session_token is not None:
            result['TerminalSessionToken'] = self.terminal_session_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TerminalSessionToken') is not None:
            self.terminal_session_token = m.get('TerminalSessionToken')
        return self


class ViewInstanceRecordsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        root: bool = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.root = root
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.root is not None:
            result['Root'] = self.root
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Root') is not None:
            self.root = m.get('Root')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ViewInstanceRecordsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ViewInstanceRecordsResponseBody = None,
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
            temp_model = ViewInstanceRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


