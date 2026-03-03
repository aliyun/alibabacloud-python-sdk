# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_websitebuild20250429 import models as main_models
from darabonba.model import DaraModel

class AllocateSupabaseForAdminResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        allow_retry: bool = None,
        app_name: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_args: List[Any] = None,
        module: main_models.AllocateSupabaseForAdminResponseBodyModule = None,
        request_id: str = None,
        root_error_code: str = None,
        root_error_msg: str = None,
        synchro: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.allow_retry = allow_retry
        self.app_name = app_name
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_args = error_args
        self.module = module
        # Id of the request
        self.request_id = request_id
        self.root_error_code = root_error_code
        self.root_error_msg = root_error_msg
        self.synchro = synchro

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.allow_retry is not None:
            result['AllowRetry'] = self.allow_retry

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code

        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message

        if self.error_args is not None:
            result['ErrorArgs'] = self.error_args

        if self.module is not None:
            result['Module'] = self.module.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.root_error_code is not None:
            result['RootErrorCode'] = self.root_error_code

        if self.root_error_msg is not None:
            result['RootErrorMsg'] = self.root_error_msg

        if self.synchro is not None:
            result['Synchro'] = self.synchro

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('AllowRetry') is not None:
            self.allow_retry = m.get('AllowRetry')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')

        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')

        if m.get('ErrorArgs') is not None:
            self.error_args = m.get('ErrorArgs')

        if m.get('Module') is not None:
            temp_model = main_models.AllocateSupabaseForAdminResponseBodyModule()
            self.module = temp_model.from_map(m.get('Module'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RootErrorCode') is not None:
            self.root_error_code = m.get('RootErrorCode')

        if m.get('RootErrorMsg') is not None:
            self.root_error_msg = m.get('RootErrorMsg')

        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')

        return self

class AllocateSupabaseForAdminResponseBodyModule(DaraModel):
    def __init__(
        self,
        anon_key: str = None,
        biz_id: str = None,
        db_instance_create_time: str = None,
        db_instance_id: str = None,
        db_public_url: str = None,
        db_type: str = None,
        extra: str = None,
        instance_create_finished_time: str = None,
        instance_create_status: str = None,
        is_deleted: int = None,
        rds_database_password: str = None,
        service_key: str = None,
        status: int = None,
        supabase_dashboard_password: str = None,
        supabase_dashboard_user_name: str = None,
        supabase_instance_create_time: str = None,
        supabase_instance_id: str = None,
        supabase_kong_url: str = None,
        supabase_private_ip: str = None,
        supabase_public_ip: str = None,
        supabase_public_url: str = None,
        tenant_id: str = None,
        user_id: str = None,
    ):
        self.anon_key = anon_key
        self.biz_id = biz_id
        self.db_instance_create_time = db_instance_create_time
        self.db_instance_id = db_instance_id
        self.db_public_url = db_public_url
        self.db_type = db_type
        self.extra = extra
        self.instance_create_finished_time = instance_create_finished_time
        self.instance_create_status = instance_create_status
        self.is_deleted = is_deleted
        self.rds_database_password = rds_database_password
        self.service_key = service_key
        self.status = status
        self.supabase_dashboard_password = supabase_dashboard_password
        self.supabase_dashboard_user_name = supabase_dashboard_user_name
        self.supabase_instance_create_time = supabase_instance_create_time
        self.supabase_instance_id = supabase_instance_id
        # Supabase Kong URL
        self.supabase_kong_url = supabase_kong_url
        self.supabase_private_ip = supabase_private_ip
        self.supabase_public_ip = supabase_public_ip
        self.supabase_public_url = supabase_public_url
        self.tenant_id = tenant_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.anon_key is not None:
            result['AnonKey'] = self.anon_key

        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.db_instance_create_time is not None:
            result['DbInstanceCreateTime'] = self.db_instance_create_time

        if self.db_instance_id is not None:
            result['DbInstanceId'] = self.db_instance_id

        if self.db_public_url is not None:
            result['DbPublicUrl'] = self.db_public_url

        if self.db_type is not None:
            result['DbType'] = self.db_type

        if self.extra is not None:
            result['Extra'] = self.extra

        if self.instance_create_finished_time is not None:
            result['InstanceCreateFinishedTime'] = self.instance_create_finished_time

        if self.instance_create_status is not None:
            result['InstanceCreateStatus'] = self.instance_create_status

        if self.is_deleted is not None:
            result['IsDeleted'] = self.is_deleted

        if self.rds_database_password is not None:
            result['RdsDatabasePassword'] = self.rds_database_password

        if self.service_key is not None:
            result['ServiceKey'] = self.service_key

        if self.status is not None:
            result['Status'] = self.status

        if self.supabase_dashboard_password is not None:
            result['SupabaseDashboardPassword'] = self.supabase_dashboard_password

        if self.supabase_dashboard_user_name is not None:
            result['SupabaseDashboardUserName'] = self.supabase_dashboard_user_name

        if self.supabase_instance_create_time is not None:
            result['SupabaseInstanceCreateTime'] = self.supabase_instance_create_time

        if self.supabase_instance_id is not None:
            result['SupabaseInstanceId'] = self.supabase_instance_id

        if self.supabase_kong_url is not None:
            result['SupabaseKongUrl'] = self.supabase_kong_url

        if self.supabase_private_ip is not None:
            result['SupabasePrivateIp'] = self.supabase_private_ip

        if self.supabase_public_ip is not None:
            result['SupabasePublicIp'] = self.supabase_public_ip

        if self.supabase_public_url is not None:
            result['SupabasePublicUrl'] = self.supabase_public_url

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnonKey') is not None:
            self.anon_key = m.get('AnonKey')

        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('DbInstanceCreateTime') is not None:
            self.db_instance_create_time = m.get('DbInstanceCreateTime')

        if m.get('DbInstanceId') is not None:
            self.db_instance_id = m.get('DbInstanceId')

        if m.get('DbPublicUrl') is not None:
            self.db_public_url = m.get('DbPublicUrl')

        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')

        if m.get('Extra') is not None:
            self.extra = m.get('Extra')

        if m.get('InstanceCreateFinishedTime') is not None:
            self.instance_create_finished_time = m.get('InstanceCreateFinishedTime')

        if m.get('InstanceCreateStatus') is not None:
            self.instance_create_status = m.get('InstanceCreateStatus')

        if m.get('IsDeleted') is not None:
            self.is_deleted = m.get('IsDeleted')

        if m.get('RdsDatabasePassword') is not None:
            self.rds_database_password = m.get('RdsDatabasePassword')

        if m.get('ServiceKey') is not None:
            self.service_key = m.get('ServiceKey')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SupabaseDashboardPassword') is not None:
            self.supabase_dashboard_password = m.get('SupabaseDashboardPassword')

        if m.get('SupabaseDashboardUserName') is not None:
            self.supabase_dashboard_user_name = m.get('SupabaseDashboardUserName')

        if m.get('SupabaseInstanceCreateTime') is not None:
            self.supabase_instance_create_time = m.get('SupabaseInstanceCreateTime')

        if m.get('SupabaseInstanceId') is not None:
            self.supabase_instance_id = m.get('SupabaseInstanceId')

        if m.get('SupabaseKongUrl') is not None:
            self.supabase_kong_url = m.get('SupabaseKongUrl')

        if m.get('SupabasePrivateIp') is not None:
            self.supabase_private_ip = m.get('SupabasePrivateIp')

        if m.get('SupabasePublicIp') is not None:
            self.supabase_public_ip = m.get('SupabasePublicIp')

        if m.get('SupabasePublicUrl') is not None:
            self.supabase_public_url = m.get('SupabasePublicUrl')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

