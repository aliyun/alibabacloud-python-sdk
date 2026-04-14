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

