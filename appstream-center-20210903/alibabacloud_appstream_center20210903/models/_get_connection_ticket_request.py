# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetConnectionTicketRequest(DaraModel):
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
        require_uuid_validation: bool = None,
        resource_id: str = None,
        session_id: str = None,
        task_id: str = None,
        tenant_id: str = None,
        uuid: str = None,
    ):
        # The access type. If this parameter is not passed, both types are displayed. Valid values: INTERNET (Internet) and VPC (Express Connect circuit).
        self.access_type = access_type
        # The application ID.
        # 
        # > Required for the first call, and optional for subsequent calls.
        self.app_id = app_id
        # The delivery group ID.
        # > 
        # > - When this parameter is passed, an application instance is assigned only from the specified and authorized delivery groups.
        # > - When the AppInstanceId parameter is passed, this parameter is required.
        self.app_instance_group_id = app_instance_group_id
        # The application instance ID.
        # 
        # > 
        # > - When this parameter is passed, the system only attempts to assign the specified application instance.
        # > - When this parameter is passed, the AppInstanceGroupId parameter must also be passed.
        self.app_instance_id = app_instance_id
        # The policy ID.
        self.app_policy_id = app_policy_id
        # The application version number.
        self.app_version = app_version
        # Specifies whether to automatically connect when the turn is reached.
        # 
        # > This parameter is not available.
        self.auto_connect_in_queue = auto_connect_in_queue
        # The region ID.
        # 
        # > When this parameter is passed, an application instance is assigned only from the delivery groups in the specified region.
        self.biz_region_id = biz_region_id
        # The client ID.
        self.client_id = client_id
        # The client IP address.
        self.client_ip = client_ip
        # The client operating system.
        self.client_os = client_os
        # The client type.
        self.client_type = client_type
        # The client version.
        self.client_version = client_version
        # The connection properties in JSON format.
        # The following parameters are supported:
        # 
        # - authMode: the authorization mode, which is determined based on the authorization mode of the delivery group. Valid values: App (application authorization), AppInstanceGroup (delivery group authorization), and Session (persistent session authorization).
        # - appInstanceGroupScheduleTags: the delivery group scheduling tags. Multiple tag key-value pairs are supported for filtering. Multiple tag pairs have an AND relationship. The key must have a value, and the value can be empty. Format example: [{"key":"Resolution","value":"720p"},{"key":"Name"}].
        # - appInstanceGroupIds: the list of specified delivery group IDs.
        # - appInstancePersistentId: the specified persistent session ID.
        # - avatarId: the user avatar ID. Default value: default. This parameter is used to support assigning multiple session instances to a single user.
        # 
        # > Used when connecting to a cloud phone. Pass the fixed value `{"authMode":"Session"}`.
        self.connection_properties = connection_properties
        # The username of the convenience account.
        self.end_user_id = end_user_id
        # The environment configuration.
        self.environment_config = environment_config
        # The logon region ID. When a user logs on to a workspace, this parameter specifies the ID of the region to which the workspace belongs.
        self.login_region_id = login_region_id
        # The logon token.
        # Obtained by calling the GetLoginToken or GetStsToken API operation.
        # The GetLoginToken and GetStsToken API operations belong to the client logon authentication APIs of the 2021-02-20 version of WUYING Cloud App (product code: appstream-center). These two API operations are not provided in the 2021-09-03 version. OpenAPI Explorer links: https://api.aliyun.com/api/appstream-center/2021-02-20/GetLoginToken and https://api.aliyun.com/api/appstream-center/2021-02-20/GetStsToken.
        # Note: This parameter is required. If it is not provided, the API returns InvalidParameter.loginToken(400).
        self.login_token = login_token
        # The application startup parameters.
        self.param = param
        # The product type.
        # 
        # This parameter is required.
        self.product_type = product_type
        # Specifies whether UUID validation is required.
        self.require_uuid_validation = require_uuid_validation
        # The resource ID.
        # 
        # > Used when connecting to a cloud phone. Pass the persistent session ID that corresponds to the cloud phone instance.
        # > When connecting to a cloud browser, pass the cloud browser ID.
        # > When connecting to a cloud application, pass the application ID for the application authorization scenario, the delivery group ID for the delivery group authorization scenario, or the persistent session ID for the persistent session authorization scenario.
        self.resource_id = resource_id
        # The logon session ID. Obtained by calling the GetLoginToken or GetStsToken API operation. This parameter is used together with LoginToken.
        # The GetLoginToken and GetStsToken API operations belong to the client logon authentication APIs of the 2021-02-20 version of WUYING Cloud App (product code: appstream-center). These two API operations are not provided in the 2021-09-03 version. OpenAPI Explorer links: https://api.aliyun.com/api/appstream-center/2021-02-20/GetLoginToken and https://api.aliyun.com/api/appstream-center/2021-02-20/GetStsToken.
        # Note: This parameter is required. If it is not provided, the API returns InvalidParameter.sessionId(400). This parameter must be used together with LoginToken.
        self.session_id = session_id
        # The node ID.
        # 
        # > Required when you invoke the API not for the first time. Use this parameter query to check the node status and connection credentials.
        self.task_id = task_id
        # The tenant ID, which is the Alibaba Cloud account UID.
        self.tenant_id = tenant_id
        # The unique identifier of the logon device.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        if self.require_uuid_validation is not None:
            result['RequireUuidValidation'] = self.require_uuid_validation

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

        if m.get('RequireUuidValidation') is not None:
            self.require_uuid_validation = m.get('RequireUuidValidation')

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

