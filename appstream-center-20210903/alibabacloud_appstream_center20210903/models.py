# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class GetConnectionTicketRequest(TeaModel):
    def __init__(
        self,
        access_type: str = None,
        app_id: str = None,
        app_instance_group_id: str = None,
        app_instance_id: str = None,
        app_policy_id: str = None,
        app_version: str = None,
        auto_connect_in_queue: bool = None,
        biz_region_id: str = None,
        client_id: str = None,
        client_ip: str = None,
        client_os: str = None,
        client_type: str = None,
        client_version: str = None,
        connection_properties: str = None,
        end_user_id: str = None,
        environment_config: str = None,
        login_region_id: str = None,
        login_token: str = None,
        param: str = None,
        product_type: str = None,
        resource_id: str = None,
        session_id: str = None,
        task_id: str = None,
        tenant_id: str = None,
        uuid: str = None,
    ):
        self.access_type = access_type
        self.app_id = app_id
        self.app_instance_group_id = app_instance_group_id
        self.app_instance_id = app_instance_id
        self.app_policy_id = app_policy_id
        self.app_version = app_version
        self.auto_connect_in_queue = auto_connect_in_queue
        self.biz_region_id = biz_region_id
        self.client_id = client_id
        self.client_ip = client_ip
        self.client_os = client_os
        self.client_type = client_type
        self.client_version = client_version
        self.connection_properties = connection_properties
        self.end_user_id = end_user_id
        self.environment_config = environment_config
        self.login_region_id = login_region_id
        self.login_token = login_token
        self.param = param
        # This parameter is required.
        self.product_type = product_type
        self.resource_id = resource_id
        self.session_id = session_id
        self.task_id = task_id
        self.tenant_id = tenant_id
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_type is not None:
            result['AccessType'] = self.access_type
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id
        if self.app_policy_id is not None:
            result['AppPolicyId'] = self.app_policy_id
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.auto_connect_in_queue is not None:
            result['AutoConnectInQueue'] = self.auto_connect_in_queue
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.client_os is not None:
            result['ClientOS'] = self.client_os
        if self.client_type is not None:
            result['ClientType'] = self.client_type
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        if self.connection_properties is not None:
            result['ConnectionProperties'] = self.connection_properties
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.environment_config is not None:
            result['EnvironmentConfig'] = self.environment_config
        if self.login_region_id is not None:
            result['LoginRegionId'] = self.login_region_id
        if self.login_token is not None:
            result['LoginToken'] = self.login_token
        if self.param is not None:
            result['Param'] = self.param
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessType') is not None:
            self.access_type = m.get('AccessType')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')
        if m.get('AppPolicyId') is not None:
            self.app_policy_id = m.get('AppPolicyId')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('AutoConnectInQueue') is not None:
            self.auto_connect_in_queue = m.get('AutoConnectInQueue')
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('ClientOS') is not None:
            self.client_os = m.get('ClientOS')
        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        if m.get('ConnectionProperties') is not None:
            self.connection_properties = m.get('ConnectionProperties')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('EnvironmentConfig') is not None:
            self.environment_config = m.get('EnvironmentConfig')
        if m.get('LoginRegionId') is not None:
            self.login_region_id = m.get('LoginRegionId')
        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')
        if m.get('Param') is not None:
            self.param = m.get('Param')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class GetConnectionTicketResponseBodyBindQueueInfo(TeaModel):
    def __init__(
        self,
        queue_status: str = None,
        rank: int = None,
        ready_timeout: int = None,
        remaining_time: int = None,
        request_key: str = None,
        target_id: str = None,
        wait_time: int = None,
    ):
        self.queue_status = queue_status
        self.rank = rank
        self.ready_timeout = ready_timeout
        self.remaining_time = remaining_time
        self.request_key = request_key
        self.target_id = target_id
        self.wait_time = wait_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.queue_status is not None:
            result['QueueStatus'] = self.queue_status
        if self.rank is not None:
            result['Rank'] = self.rank
        if self.ready_timeout is not None:
            result['ReadyTimeout'] = self.ready_timeout
        if self.remaining_time is not None:
            result['RemainingTime'] = self.remaining_time
        if self.request_key is not None:
            result['RequestKey'] = self.request_key
        if self.target_id is not None:
            result['TargetId'] = self.target_id
        if self.wait_time is not None:
            result['WaitTime'] = self.wait_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QueueStatus') is not None:
            self.queue_status = m.get('QueueStatus')
        if m.get('Rank') is not None:
            self.rank = m.get('Rank')
        if m.get('ReadyTimeout') is not None:
            self.ready_timeout = m.get('ReadyTimeout')
        if m.get('RemainingTime') is not None:
            self.remaining_time = m.get('RemainingTime')
        if m.get('RequestKey') is not None:
            self.request_key = m.get('RequestKey')
        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')
        if m.get('WaitTime') is not None:
            self.wait_time = m.get('WaitTime')
        return self


class GetConnectionTicketResponseBodyPolicy(TeaModel):
    def __init__(
        self,
        resolution_adaptive: str = None,
        resolution_height: int = None,
        resolution_width: int = None,
    ):
        self.resolution_adaptive = resolution_adaptive
        self.resolution_height = resolution_height
        self.resolution_width = resolution_width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resolution_adaptive is not None:
            result['ResolutionAdaptive'] = self.resolution_adaptive
        if self.resolution_height is not None:
            result['ResolutionHeight'] = self.resolution_height
        if self.resolution_width is not None:
            result['ResolutionWidth'] = self.resolution_width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResolutionAdaptive') is not None:
            self.resolution_adaptive = m.get('ResolutionAdaptive')
        if m.get('ResolutionHeight') is not None:
            self.resolution_height = m.get('ResolutionHeight')
        if m.get('ResolutionWidth') is not None:
            self.resolution_width = m.get('ResolutionWidth')
        return self


class GetConnectionTicketResponseBody(TeaModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        app_instance_id: str = None,
        app_instance_persistent_id: str = None,
        avatar_id: str = None,
        bind_queue_info: GetConnectionTicketResponseBodyBindQueueInfo = None,
        code: str = None,
        login_token: str = None,
        message: str = None,
        next_poll_interval_ms: int = None,
        os_type: str = None,
        policy: GetConnectionTicketResponseBodyPolicy = None,
        region_id: str = None,
        request_id: str = None,
        retry_times: int = None,
        task_id: str = None,
        task_status: str = None,
        tenant_id: int = None,
        ticket: str = None,
    ):
        self.app_instance_group_id = app_instance_group_id
        self.app_instance_id = app_instance_id
        self.app_instance_persistent_id = app_instance_persistent_id
        self.avatar_id = avatar_id
        self.bind_queue_info = bind_queue_info
        self.code = code
        self.login_token = login_token
        self.message = message
        self.next_poll_interval_ms = next_poll_interval_ms
        self.os_type = os_type
        self.policy = policy
        self.region_id = region_id
        # Id of the request
        self.request_id = request_id
        self.retry_times = retry_times
        self.task_id = task_id
        self.task_status = task_status
        self.tenant_id = tenant_id
        self.ticket = ticket

    def validate(self):
        if self.bind_queue_info:
            self.bind_queue_info.validate()
        if self.policy:
            self.policy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id
        if self.app_instance_persistent_id is not None:
            result['AppInstancePersistentId'] = self.app_instance_persistent_id
        if self.avatar_id is not None:
            result['AvatarId'] = self.avatar_id
        if self.bind_queue_info is not None:
            result['BindQueueInfo'] = self.bind_queue_info.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.login_token is not None:
            result['LoginToken'] = self.login_token
        if self.message is not None:
            result['Message'] = self.message
        if self.next_poll_interval_ms is not None:
            result['NextPollIntervalMs'] = self.next_poll_interval_ms
        if self.os_type is not None:
            result['OsType'] = self.os_type
        if self.policy is not None:
            result['Policy'] = self.policy.to_map()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.retry_times is not None:
            result['RetryTimes'] = self.retry_times
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.ticket is not None:
            result['Ticket'] = self.ticket
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')
        if m.get('AppInstancePersistentId') is not None:
            self.app_instance_persistent_id = m.get('AppInstancePersistentId')
        if m.get('AvatarId') is not None:
            self.avatar_id = m.get('AvatarId')
        if m.get('BindQueueInfo') is not None:
            temp_model = GetConnectionTicketResponseBodyBindQueueInfo()
            self.bind_queue_info = temp_model.from_map(m['BindQueueInfo'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextPollIntervalMs') is not None:
            self.next_poll_interval_ms = m.get('NextPollIntervalMs')
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('Policy') is not None:
            temp_model = GetConnectionTicketResponseBodyPolicy()
            self.policy = temp_model.from_map(m['Policy'])
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RetryTimes') is not None:
            self.retry_times = m.get('RetryTimes')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Ticket') is not None:
            self.ticket = m.get('Ticket')
        return self


class GetConnectionTicketResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetConnectionTicketResponseBody = None,
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
            temp_model = GetConnectionTicketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPublishedAppInfoRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        biz_region_id: str = None,
        category_id: int = None,
        category_type: int = None,
        client_id: str = None,
        client_ip: str = None,
        client_os: str = None,
        client_version: str = None,
        end_user_id: str = None,
        login_region_id: str = None,
        login_token: str = None,
        order_param: str = None,
        product_type: str = None,
        session_id: str = None,
        sort_type: str = None,
    ):
        self.app_name = app_name
        self.biz_region_id = biz_region_id
        self.category_id = category_id
        self.category_type = category_type
        self.client_id = client_id
        self.client_ip = client_ip
        self.client_os = client_os
        self.client_version = client_version
        self.end_user_id = end_user_id
        self.login_region_id = login_region_id
        self.login_token = login_token
        self.order_param = order_param
        self.product_type = product_type
        self.session_id = session_id
        self.sort_type = sort_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.category_type is not None:
            result['CategoryType'] = self.category_type
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.client_os is not None:
            result['ClientOS'] = self.client_os
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.login_region_id is not None:
            result['LoginRegionId'] = self.login_region_id
        if self.login_token is not None:
            result['LoginToken'] = self.login_token
        if self.order_param is not None:
            result['OrderParam'] = self.order_param
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.sort_type is not None:
            result['SortType'] = self.sort_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CategoryType') is not None:
            self.category_type = m.get('CategoryType')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('ClientOS') is not None:
            self.client_os = m.get('ClientOS')
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('LoginRegionId') is not None:
            self.login_region_id = m.get('LoginRegionId')
        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')
        if m.get('OrderParam') is not None:
            self.order_param = m.get('OrderParam')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('SortType') is not None:
            self.sort_type = m.get('SortType')
        return self


class ListPublishedAppInfoResponseBodyAppModels(TeaModel):
    def __init__(
        self,
        app_center_image_id: str = None,
        app_id: str = None,
        app_name: str = None,
        app_theme_color: str = None,
        app_version: str = None,
        app_version_name: str = None,
        auth_time: str = None,
        category_id: int = None,
        category_type: int = None,
        icon_url: str = None,
        is_auth: bool = None,
        used_in_session: bool = None,
    ):
        self.app_center_image_id = app_center_image_id
        self.app_id = app_id
        self.app_name = app_name
        self.app_theme_color = app_theme_color
        self.app_version = app_version
        self.app_version_name = app_version_name
        self.auth_time = auth_time
        self.category_id = category_id
        self.category_type = category_type
        self.icon_url = icon_url
        self.is_auth = is_auth
        self.used_in_session = used_in_session

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_center_image_id is not None:
            result['AppCenterImageId'] = self.app_center_image_id
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_theme_color is not None:
            result['AppThemeColor'] = self.app_theme_color
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.app_version_name is not None:
            result['AppVersionName'] = self.app_version_name
        if self.auth_time is not None:
            result['AuthTime'] = self.auth_time
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.category_type is not None:
            result['CategoryType'] = self.category_type
        if self.icon_url is not None:
            result['IconUrl'] = self.icon_url
        if self.is_auth is not None:
            result['IsAuth'] = self.is_auth
        if self.used_in_session is not None:
            result['UsedInSession'] = self.used_in_session
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCenterImageId') is not None:
            self.app_center_image_id = m.get('AppCenterImageId')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppThemeColor') is not None:
            self.app_theme_color = m.get('AppThemeColor')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('AppVersionName') is not None:
            self.app_version_name = m.get('AppVersionName')
        if m.get('AuthTime') is not None:
            self.auth_time = m.get('AuthTime')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CategoryType') is not None:
            self.category_type = m.get('CategoryType')
        if m.get('IconUrl') is not None:
            self.icon_url = m.get('IconUrl')
        if m.get('IsAuth') is not None:
            self.is_auth = m.get('IsAuth')
        if m.get('UsedInSession') is not None:
            self.used_in_session = m.get('UsedInSession')
        return self


class ListPublishedAppInfoResponseBody(TeaModel):
    def __init__(
        self,
        app_models: List[ListPublishedAppInfoResponseBodyAppModels] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # appModels
        self.app_models = app_models
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.app_models:
            for k in self.app_models:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AppModels'] = []
        if self.app_models is not None:
            for k in self.app_models:
                result['AppModels'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.app_models = []
        if m.get('AppModels') is not None:
            for k in m.get('AppModels'):
                temp_model = ListPublishedAppInfoResponseBodyAppModels()
                self.app_models.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListPublishedAppInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPublishedAppInfoResponseBody = None,
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
            temp_model = ListPublishedAppInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRunningAppsRequest(TeaModel):
    def __init__(
        self,
        biz_region_id: str = None,
        client_id: str = None,
        client_ip: str = None,
        client_os: str = None,
        client_version: str = None,
        end_user_id: str = None,
        login_region_id: str = None,
        login_token: str = None,
        product_type: str = None,
        session_id: str = None,
        tenant_id: str = None,
        uuid: str = None,
    ):
        self.biz_region_id = biz_region_id
        self.client_id = client_id
        self.client_ip = client_ip
        self.client_os = client_os
        self.client_version = client_version
        self.end_user_id = end_user_id
        self.login_region_id = login_region_id
        self.login_token = login_token
        self.product_type = product_type
        self.session_id = session_id
        self.tenant_id = tenant_id
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.client_os is not None:
            result['ClientOS'] = self.client_os
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.login_region_id is not None:
            result['LoginRegionId'] = self.login_region_id
        if self.login_token is not None:
            result['LoginToken'] = self.login_token
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('ClientOS') is not None:
            self.client_os = m.get('ClientOS')
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('LoginRegionId') is not None:
            self.login_region_id = m.get('LoginRegionId')
        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class ListRunningAppsResponseBodyRunningCloudApps(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_instance_group_id: str = None,
        app_instance_id: str = None,
        app_name: str = None,
        app_version: str = None,
        app_version_name: str = None,
        duration: int = None,
        icon_url: str = None,
        os_type: str = None,
        region_id: str = None,
        start_time: str = None,
    ):
        self.app_id = app_id
        self.app_instance_group_id = app_instance_group_id
        self.app_instance_id = app_instance_id
        self.app_name = app_name
        self.app_version = app_version
        self.app_version_name = app_version_name
        self.duration = duration
        self.icon_url = icon_url
        self.os_type = os_type
        self.region_id = region_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.app_version_name is not None:
            result['AppVersionName'] = self.app_version_name
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.icon_url is not None:
            result['IconUrl'] = self.icon_url
        if self.os_type is not None:
            result['OsType'] = self.os_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('AppVersionName') is not None:
            self.app_version_name = m.get('AppVersionName')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('IconUrl') is not None:
            self.icon_url = m.get('IconUrl')
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ListRunningAppsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        running_cloud_apps: List[ListRunningAppsResponseBodyRunningCloudApps] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.running_cloud_apps = running_cloud_apps

    def validate(self):
        if self.running_cloud_apps:
            for k in self.running_cloud_apps:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['RunningCloudApps'] = []
        if self.running_cloud_apps is not None:
            for k in self.running_cloud_apps:
                result['RunningCloudApps'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.running_cloud_apps = []
        if m.get('RunningCloudApps') is not None:
            for k in m.get('RunningCloudApps'):
                temp_model = ListRunningAppsResponseBodyRunningCloudApps()
                self.running_cloud_apps.append(temp_model.from_map(k))
        return self


class ListRunningAppsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRunningAppsResponseBody = None,
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
            temp_model = ListRunningAppsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetAppResourcesRequest(TeaModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        biz_region_id: str = None,
        client_id: str = None,
        client_ip: str = None,
        client_os: str = None,
        client_version: str = None,
        end_user_id: str = None,
        login_region_id: str = None,
        login_token: str = None,
        product_type: str = None,
        resource_ids: List[str] = None,
        session_id: str = None,
        uuid: str = None,
    ):
        # This parameter is required.
        self.app_instance_group_id = app_instance_group_id
        self.biz_region_id = biz_region_id
        # This parameter is required.
        self.client_id = client_id
        self.client_ip = client_ip
        self.client_os = client_os
        self.client_version = client_version
        self.end_user_id = end_user_id
        self.login_region_id = login_region_id
        # This parameter is required.
        self.login_token = login_token
        # This parameter is required.
        self.product_type = product_type
        # This parameter is required.
        self.resource_ids = resource_ids
        # This parameter is required.
        self.session_id = session_id
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.client_os is not None:
            result['ClientOS'] = self.client_os
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.login_region_id is not None:
            result['LoginRegionId'] = self.login_region_id
        if self.login_token is not None:
            result['LoginToken'] = self.login_token
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('ClientOS') is not None:
            self.client_os = m.get('ClientOS')
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('LoginRegionId') is not None:
            self.login_region_id = m.get('LoginRegionId')
        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class ResetAppResourcesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
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
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ResetAppResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ResetAppResourcesResponseBody = None,
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
            temp_model = ResetAppResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestartAppResourcesRequest(TeaModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        biz_region_id: str = None,
        client_id: str = None,
        client_ip: str = None,
        client_os: str = None,
        client_version: str = None,
        end_user_id: str = None,
        login_region_id: str = None,
        login_token: str = None,
        product_type: str = None,
        resource_ids: List[str] = None,
        session_id: str = None,
        uuid: str = None,
    ):
        # This parameter is required.
        self.app_instance_group_id = app_instance_group_id
        self.biz_region_id = biz_region_id
        # This parameter is required.
        self.client_id = client_id
        self.client_ip = client_ip
        self.client_os = client_os
        self.client_version = client_version
        self.end_user_id = end_user_id
        self.login_region_id = login_region_id
        # This parameter is required.
        self.login_token = login_token
        # This parameter is required.
        self.product_type = product_type
        # This parameter is required.
        self.resource_ids = resource_ids
        # This parameter is required.
        self.session_id = session_id
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.client_os is not None:
            result['ClientOS'] = self.client_os
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.login_region_id is not None:
            result['LoginRegionId'] = self.login_region_id
        if self.login_token is not None:
            result['LoginToken'] = self.login_token
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('ClientOS') is not None:
            self.client_os = m.get('ClientOS')
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('LoginRegionId') is not None:
            self.login_region_id = m.get('LoginRegionId')
        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class RestartAppResourcesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
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
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RestartAppResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RestartAppResourcesResponseBody = None,
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
            temp_model = RestartAppResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartAppResourcesRequest(TeaModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        biz_region_id: str = None,
        client_id: str = None,
        client_ip: str = None,
        client_os: str = None,
        client_version: str = None,
        end_user_id: str = None,
        login_region_id: str = None,
        login_token: str = None,
        product_type: str = None,
        resource_ids: List[str] = None,
        session_id: str = None,
        uuid: str = None,
    ):
        # This parameter is required.
        self.app_instance_group_id = app_instance_group_id
        self.biz_region_id = biz_region_id
        # This parameter is required.
        self.client_id = client_id
        self.client_ip = client_ip
        self.client_os = client_os
        self.client_version = client_version
        self.end_user_id = end_user_id
        self.login_region_id = login_region_id
        # This parameter is required.
        self.login_token = login_token
        # This parameter is required.
        self.product_type = product_type
        # This parameter is required.
        self.resource_ids = resource_ids
        # This parameter is required.
        self.session_id = session_id
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.client_os is not None:
            result['ClientOS'] = self.client_os
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.login_region_id is not None:
            result['LoginRegionId'] = self.login_region_id
        if self.login_token is not None:
            result['LoginToken'] = self.login_token
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('ClientOS') is not None:
            self.client_os = m.get('ClientOS')
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('LoginRegionId') is not None:
            self.login_region_id = m.get('LoginRegionId')
        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class StartAppResourcesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
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
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StartAppResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartAppResourcesResponseBody = None,
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
            temp_model = StartAppResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopAppRequest(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        api_type: str = None,
        app_id: str = None,
        app_instance_group_id: str = None,
        app_instance_id: str = None,
        biz_region_id: str = None,
        client_channel: str = None,
        client_id: str = None,
        client_ip: str = None,
        client_os: str = None,
        client_version: str = None,
        end_user_id: str = None,
        force_stop: bool = None,
        idp_id: str = None,
        login_region_id: str = None,
        login_token: str = None,
        product_type: str = None,
        region_id: str = None,
        session_id: str = None,
        uuid: str = None,
        wy_id: str = None,
    ):
        self.ali_uid = ali_uid
        self.api_type = api_type
        self.app_id = app_id
        self.app_instance_group_id = app_instance_group_id
        self.app_instance_id = app_instance_id
        self.biz_region_id = biz_region_id
        self.client_channel = client_channel
        self.client_id = client_id
        self.client_ip = client_ip
        self.client_os = client_os
        self.client_version = client_version
        self.end_user_id = end_user_id
        self.force_stop = force_stop
        self.idp_id = idp_id
        self.login_region_id = login_region_id
        self.login_token = login_token
        self.product_type = product_type
        self.region_id = region_id
        self.session_id = session_id
        self.uuid = uuid
        self.wy_id = wy_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.api_type is not None:
            result['ApiType'] = self.api_type
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id
        if self.client_channel is not None:
            result['ClientChannel'] = self.client_channel
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.client_os is not None:
            result['ClientOS'] = self.client_os
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.force_stop is not None:
            result['ForceStop'] = self.force_stop
        if self.idp_id is not None:
            result['IdpId'] = self.idp_id
        if self.login_region_id is not None:
            result['LoginRegionId'] = self.login_region_id
        if self.login_token is not None:
            result['LoginToken'] = self.login_token
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.wy_id is not None:
            result['WyId'] = self.wy_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('ApiType') is not None:
            self.api_type = m.get('ApiType')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')
        if m.get('ClientChannel') is not None:
            self.client_channel = m.get('ClientChannel')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('ClientOS') is not None:
            self.client_os = m.get('ClientOS')
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('ForceStop') is not None:
            self.force_stop = m.get('ForceStop')
        if m.get('IdpId') is not None:
            self.idp_id = m.get('IdpId')
        if m.get('LoginRegionId') is not None:
            self.login_region_id = m.get('LoginRegionId')
        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('WyId') is not None:
            self.wy_id = m.get('WyId')
        return self


class StopAppResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
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


class StopAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopAppResponseBody = None,
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
            temp_model = StopAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopAppResourcesRequest(TeaModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        biz_region_id: str = None,
        client_id: str = None,
        client_ip: str = None,
        client_os: str = None,
        client_version: str = None,
        end_user_id: str = None,
        login_region_id: str = None,
        login_token: str = None,
        product_type: str = None,
        resource_ids: List[str] = None,
        session_id: str = None,
        uuid: str = None,
    ):
        # This parameter is required.
        self.app_instance_group_id = app_instance_group_id
        self.biz_region_id = biz_region_id
        # This parameter is required.
        self.client_id = client_id
        self.client_ip = client_ip
        self.client_os = client_os
        self.client_version = client_version
        self.end_user_id = end_user_id
        self.login_region_id = login_region_id
        # This parameter is required.
        self.login_token = login_token
        # This parameter is required.
        self.product_type = product_type
        # This parameter is required.
        self.resource_ids = resource_ids
        # This parameter is required.
        self.session_id = session_id
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.client_os is not None:
            result['ClientOS'] = self.client_os
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.login_region_id is not None:
            result['LoginRegionId'] = self.login_region_id
        if self.login_token is not None:
            result['LoginToken'] = self.login_token
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('ClientOS') is not None:
            self.client_os = m.get('ClientOS')
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('LoginRegionId') is not None:
            self.login_region_id = m.get('LoginRegionId')
        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class StopAppResourcesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
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
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StopAppResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopAppResourcesResponseBody = None,
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
            temp_model = StopAppResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnbindRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_instance_group_id: str = None,
        app_instance_id: str = None,
        client_id: str = None,
        client_ip: str = None,
        client_os: str = None,
        client_version: str = None,
        end_user_id: str = None,
        login_region_id: str = None,
        login_token: str = None,
        product_type: str = None,
        session_id: str = None,
        tenant_id: int = None,
    ):
        self.app_id = app_id
        # This parameter is required.
        self.app_instance_group_id = app_instance_group_id
        self.app_instance_id = app_instance_id
        self.client_id = client_id
        self.client_ip = client_ip
        self.client_os = client_os
        self.client_version = client_version
        self.end_user_id = end_user_id
        self.login_region_id = login_region_id
        # This parameter is required.
        self.login_token = login_token
        # This parameter is required.
        self.product_type = product_type
        # This parameter is required.
        self.session_id = session_id
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.client_os is not None:
            result['ClientOS'] = self.client_os
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.login_region_id is not None:
            result['LoginRegionId'] = self.login_region_id
        if self.login_token is not None:
            result['LoginToken'] = self.login_token
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('ClientOS') is not None:
            self.client_os = m.get('ClientOS')
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('LoginRegionId') is not None:
            self.login_region_id = m.get('LoginRegionId')
        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class UnbindResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
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


class UnbindResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UnbindResponseBody = None,
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
            temp_model = UnbindResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


