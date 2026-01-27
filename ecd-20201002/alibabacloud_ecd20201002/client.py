# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_ecd20201002 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
from darabonba.runtime import RuntimeOptions

"""
"""
class Client(OpenApiClient):

    def __init__(
        self,
        config: open_api_util_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('ecd', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(
        self,
        product_id: str,
        region_id: str,
        endpoint_rule: str,
        network: str,
        suffix: str,
        endpoint_map: Dict[str, str],
        endpoint: str,
    ) -> str:
        if not DaraCore.is_null(endpoint):
            return endpoint
        if not DaraCore.is_null(endpoint_map) and not DaraCore.is_null(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return Utils.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def approve_fota_update_with_options(
        self,
        request: main_models.ApproveFotaUpdateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ApproveFotaUpdateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_version):
            query['AppVersion'] = request.app_version
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not DaraCore.is_null(request.login_token):
            query['LoginToken'] = request.login_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        if not DaraCore.is_null(request.target_status):
            query['TargetStatus'] = request.target_status
        if not DaraCore.is_null(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ApproveFotaUpdate',
            version = '2020-10-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ApproveFotaUpdateResponse(),
            self.do_rpcrequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    async def approve_fota_update_with_options_async(
        self,
        request: main_models.ApproveFotaUpdateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ApproveFotaUpdateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_version):
            query['AppVersion'] = request.app_version
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not DaraCore.is_null(request.login_token):
            query['LoginToken'] = request.login_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        if not DaraCore.is_null(request.target_status):
            query['TargetStatus'] = request.target_status
        if not DaraCore.is_null(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ApproveFotaUpdate',
            version = '2020-10-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ApproveFotaUpdateResponse(),
            await self.do_rpcrequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    def approve_fota_update(
        self,
        request: main_models.ApproveFotaUpdateRequest,
    ) -> main_models.ApproveFotaUpdateResponse:
        runtime = RuntimeOptions()
        return self.approve_fota_update_with_options(request, runtime)

    async def approve_fota_update_async(
        self,
        request: main_models.ApproveFotaUpdateRequest,
    ) -> main_models.ApproveFotaUpdateResponse:
        runtime = RuntimeOptions()
        return await self.approve_fota_update_with_options_async(request, runtime)

    def change_password_with_options(
        self,
        request: main_models.ChangePasswordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangePasswordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not DaraCore.is_null(request.login_token):
            query['LoginToken'] = request.login_token
        if not DaraCore.is_null(request.new_password):
            query['NewPassword'] = request.new_password
        if not DaraCore.is_null(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not DaraCore.is_null(request.old_password):
            query['OldPassword'] = request.old_password
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangePassword',
            version = '2020-10-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangePasswordResponse(),
            self.do_rpcrequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    async def change_password_with_options_async(
        self,
        request: main_models.ChangePasswordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangePasswordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not DaraCore.is_null(request.login_token):
            query['LoginToken'] = request.login_token
        if not DaraCore.is_null(request.new_password):
            query['NewPassword'] = request.new_password
        if not DaraCore.is_null(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not DaraCore.is_null(request.old_password):
            query['OldPassword'] = request.old_password
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangePassword',
            version = '2020-10-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangePasswordResponse(),
            await self.do_rpcrequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    def change_password(
        self,
        request: main_models.ChangePasswordRequest,
    ) -> main_models.ChangePasswordResponse:
        runtime = RuntimeOptions()
        return self.change_password_with_options(request, runtime)

    async def change_password_async(
        self,
        request: main_models.ChangePasswordRequest,
    ) -> main_models.ChangePasswordResponse:
        runtime = RuntimeOptions()
        return await self.change_password_with_options_async(request, runtime)

    def delete_finger_print_template_with_options(
        self,
        request: main_models.DeleteFingerPrintTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFingerPrintTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.index):
            query['Index'] = request.index
        if not DaraCore.is_null(request.login_token):
            query['LoginToken'] = request.login_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFingerPrintTemplate',
            version = '2020-10-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFingerPrintTemplateResponse(),
            self.do_rpcrequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    async def delete_finger_print_template_with_options_async(
        self,
        request: main_models.DeleteFingerPrintTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFingerPrintTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.index):
            query['Index'] = request.index
        if not DaraCore.is_null(request.login_token):
            query['LoginToken'] = request.login_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFingerPrintTemplate',
            version = '2020-10-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFingerPrintTemplateResponse(),
            await self.do_rpcrequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    def delete_finger_print_template(
        self,
        request: main_models.DeleteFingerPrintTemplateRequest,
    ) -> main_models.DeleteFingerPrintTemplateResponse:
        runtime = RuntimeOptions()
        return self.delete_finger_print_template_with_options(request, runtime)

    async def delete_finger_print_template_async(
        self,
        request: main_models.DeleteFingerPrintTemplateRequest,
    ) -> main_models.DeleteFingerPrintTemplateResponse:
        runtime = RuntimeOptions()
        return await self.delete_finger_print_template_with_options_async(request, runtime)

    def describe_directories_with_options(
        self,
        request: main_models.DescribeDirectoriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDirectoriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDirectories',
            version = '2020-10-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDirectoriesResponse(),
            self.do_rpcrequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    async def describe_directories_with_options_async(
        self,
        request: main_models.DescribeDirectoriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDirectoriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDirectories',
            version = '2020-10-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDirectoriesResponse(),
            await self.do_rpcrequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    def describe_directories(
        self,
        request: main_models.DescribeDirectoriesRequest,
    ) -> main_models.DescribeDirectoriesResponse:
        runtime = RuntimeOptions()
        return self.describe_directories_with_options(request, runtime)

    async def describe_directories_async(
        self,
        request: main_models.DescribeDirectoriesRequest,
    ) -> main_models.DescribeDirectoriesResponse:
        runtime = RuntimeOptions()
        return await self.describe_directories_with_options_async(request, runtime)

    def describe_finger_print_templates_with_options(
        self,
        request: main_models.DescribeFingerPrintTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFingerPrintTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.login_token):
            query['LoginToken'] = request.login_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFingerPrintTemplates',
            version = '2020-10-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFingerPrintTemplatesResponse(),
            self.do_rpcrequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    async def describe_finger_print_templates_with_options_async(
        self,
        request: main_models.DescribeFingerPrintTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFingerPrintTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.login_token):
            query['LoginToken'] = request.login_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFingerPrintTemplates',
            version = '2020-10-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFingerPrintTemplatesResponse(),
            await self.do_rpcrequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    def describe_finger_print_templates(
        self,
        request: main_models.DescribeFingerPrintTemplatesRequest,
    ) -> main_models.DescribeFingerPrintTemplatesResponse:
        runtime = RuntimeOptions()
        return self.describe_finger_print_templates_with_options(request, runtime)

    async def describe_finger_print_templates_async(
        self,
        request: main_models.DescribeFingerPrintTemplatesRequest,
    ) -> main_models.DescribeFingerPrintTemplatesResponse:
        runtime = RuntimeOptions()
        return await self.describe_finger_print_templates_with_options_async(request, runtime)

    def describe_global_desktops_with_options(
        self,
        request: main_models.DescribeGlobalDesktopsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGlobalDesktopsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.desktop_access_type):
            query['DesktopAccessType'] = request.desktop_access_type
        if not DaraCore.is_null(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not DaraCore.is_null(request.desktop_name):
            query['DesktopName'] = request.desktop_name
        if not DaraCore.is_null(request.desktop_status):
            query['DesktopStatus'] = request.desktop_status
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.login_region_id):
            query['LoginRegionId'] = request.login_region_id
        if not DaraCore.is_null(request.login_token):
            query['LoginToken'] = request.login_token
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.query_fota_update):
            query['QueryFotaUpdate'] = request.query_fota_update
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.search_region_id):
            query['SearchRegionId'] = request.search_region_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        if not DaraCore.is_null(request.sort_type):
            query['SortType'] = request.sort_type
        if not DaraCore.is_null(request.without_latency):
            query['WithoutLatency'] = request.without_latency
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGlobalDesktops',
            version = '2020-10-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGlobalDesktopsResponse(),
            self.do_rpcrequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    async def describe_global_desktops_with_options_async(
        self,
        request: main_models.DescribeGlobalDesktopsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGlobalDesktopsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.desktop_access_type):
            query['DesktopAccessType'] = request.desktop_access_type
        if not DaraCore.is_null(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not DaraCore.is_null(request.desktop_name):
            query['DesktopName'] = request.desktop_name
        if not DaraCore.is_null(request.desktop_status):
            query['DesktopStatus'] = request.desktop_status
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.login_region_id):
            query['LoginRegionId'] = request.login_region_id
        if not DaraCore.is_null(request.login_token):
            query['LoginToken'] = request.login_token
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.query_fota_update):
            query['QueryFotaUpdate'] = request.query_fota_update
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.search_region_id):
            query['SearchRegionId'] = request.search_region_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        if not DaraCore.is_null(request.sort_type):
            query['SortType'] = request.sort_type
        if not DaraCore.is_null(request.without_latency):
            query['WithoutLatency'] = request.without_latency
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGlobalDesktops',
            version = '2020-10-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGlobalDesktopsResponse(),
            await self.do_rpcrequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    def describe_global_desktops(
        self,
        request: main_models.DescribeGlobalDesktopsRequest,
    ) -> main_models.DescribeGlobalDesktopsResponse:
        runtime = RuntimeOptions()
        return self.describe_global_desktops_with_options(request, runtime)

    async def describe_global_desktops_async(
        self,
        request: main_models.DescribeGlobalDesktopsRequest,
    ) -> main_models.DescribeGlobalDesktopsResponse:
        runtime = RuntimeOptions()
        return await self.describe_global_desktops_with_options_async(request, runtime)

    def describe_office_sites_with_options(
        self,
        request: main_models.DescribeOfficeSitesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOfficeSitesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOfficeSites',
            version = '2020-10-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOfficeSitesResponse(),
            self.do_rpcrequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    async def describe_office_sites_with_options_async(
        self,
        request: main_models.DescribeOfficeSitesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOfficeSitesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOfficeSites',
            version = '2020-10-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOfficeSitesResponse(),
            await self.do_rpcrequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    def describe_office_sites(
        self,
        request: main_models.DescribeOfficeSitesRequest,
    ) -> main_models.DescribeOfficeSitesResponse:
        runtime = RuntimeOptions()
        return self.describe_office_sites_with_options(request, runtime)

    async def describe_office_sites_async(
        self,
        request: main_models.DescribeOfficeSitesRequest,
    ) -> main_models.DescribeOfficeSitesResponse:
        runtime = RuntimeOptions()
        return await self.describe_office_sites_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: main_models.DescribeRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2020-10-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRegionsResponse(),
            self.do_rpcrequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: main_models.DescribeRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2020-10-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRegionsResponse(),
            await self.do_rpcrequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    def describe_regions(
        self,
        request: main_models.DescribeRegionsRequest,
    ) -> main_models.DescribeRegionsResponse:
        runtime = RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: main_models.DescribeRegionsRequest,
    ) -> main_models.DescribeRegionsResponse:
        runtime = RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_snapshots_with_options(
        self,
        request: main_models.DescribeSnapshotsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSnapshotsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not DaraCore.is_null(request.login_token):
            query['LoginToken'] = request.login_token
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        if not DaraCore.is_null(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSnapshots',
            version = '2020-10-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSnapshotsResponse(),
            self.do_rpcrequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    async def describe_snapshots_with_options_async(
        self,
        request: main_models.DescribeSnapshotsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSnapshotsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not DaraCore.is_null(request.login_token):
            query['LoginToken'] = request.login_token
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        if not DaraCore.is_null(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSnapshots',
            version = '2020-10-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSnapshotsResponse(),
            await self.do_rpcrequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    def describe_snapshots(
        self,
        request: main_models.DescribeSnapshotsRequest,
    ) -> main_models.DescribeSnapshotsResponse:
        runtime = RuntimeOptions()
        return self.describe_snapshots_with_options(request, runtime)

    async def describe_snapshots_async(
        self,
        request: main_models.DescribeSnapshotsRequest,
    ) -> main_models.DescribeSnapshotsResponse:
        runtime = RuntimeOptions()
        return await self.describe_snapshots_with_options_async(request, runtime)

    def describe_user_resources_with_options(
        self,
        request: main_models.DescribeUserResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_type):
            query['AccessType'] = request.access_type
        if not DaraCore.is_null(request.auto_refresh):
            query['AutoRefresh'] = request.auto_refresh
        if not DaraCore.is_null(request.category_id):
            query['CategoryId'] = request.category_id
        if not DaraCore.is_null(request.category_type):
            query['CategoryType'] = request.category_type
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.client_type):
            query['ClientType'] = request.client_type
        if not DaraCore.is_null(request.client_version):
            query['ClientVersion'] = request.client_version
        if not DaraCore.is_null(request.dual_center_forward):
            query['DualCenterForward'] = request.dual_center_forward
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.login_region_id):
            query['LoginRegionId'] = request.login_region_id
        if not DaraCore.is_null(request.login_token):
            query['LoginToken'] = request.login_token
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.office_site_ids):
            query['OfficeSiteIds'] = request.office_site_ids
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.product_types):
            query['ProductTypes'] = request.product_types
        if not DaraCore.is_null(request.protocol_type):
            query['ProtocolType'] = request.protocol_type
        if not DaraCore.is_null(request.query_desktop_duration_list):
            query['QueryDesktopDurationList'] = request.query_desktop_duration_list
        if not DaraCore.is_null(request.query_desktop_timers):
            query['QueryDesktopTimers'] = request.query_desktop_timers
        if not DaraCore.is_null(request.query_fota_update):
            query['QueryFotaUpdate'] = request.query_fota_update
        if not DaraCore.is_null(request.refresh_fota_update):
            query['RefreshFotaUpdate'] = request.refresh_fota_update
        if not DaraCore.is_null(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not DaraCore.is_null(request.resource_types):
            query['ResourceTypes'] = request.resource_types
        if not DaraCore.is_null(request.scene):
            query['Scene'] = request.scene
        if not DaraCore.is_null(request.search_region_id):
            query['SearchRegionId'] = request.search_region_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        if not DaraCore.is_null(request.sort_type):
            query['SortType'] = request.sort_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserResources',
            version = '2020-10-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserResourcesResponse(),
            self.do_rpcrequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    async def describe_user_resources_with_options_async(
        self,
        request: main_models.DescribeUserResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_type):
            query['AccessType'] = request.access_type
        if not DaraCore.is_null(request.auto_refresh):
            query['AutoRefresh'] = request.auto_refresh
        if not DaraCore.is_null(request.category_id):
            query['CategoryId'] = request.category_id
        if not DaraCore.is_null(request.category_type):
            query['CategoryType'] = request.category_type
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.client_type):
            query['ClientType'] = request.client_type
        if not DaraCore.is_null(request.client_version):
            query['ClientVersion'] = request.client_version
        if not DaraCore.is_null(request.dual_center_forward):
            query['DualCenterForward'] = request.dual_center_forward
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.login_region_id):
            query['LoginRegionId'] = request.login_region_id
        if not DaraCore.is_null(request.login_token):
            query['LoginToken'] = request.login_token
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.office_site_ids):
            query['OfficeSiteIds'] = request.office_site_ids
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.product_types):
            query['ProductTypes'] = request.product_types
        if not DaraCore.is_null(request.protocol_type):
            query['ProtocolType'] = request.protocol_type
        if not DaraCore.is_null(request.query_desktop_duration_list):
            query['QueryDesktopDurationList'] = request.query_desktop_duration_list
        if not DaraCore.is_null(request.query_desktop_timers):
            query['QueryDesktopTimers'] = request.query_desktop_timers
        if not DaraCore.is_null(request.query_fota_update):
            query['QueryFotaUpdate'] = request.query_fota_update
        if not DaraCore.is_null(request.refresh_fota_update):
            query['RefreshFotaUpdate'] = request.refresh_fota_update
        if not DaraCore.is_null(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not DaraCore.is_null(request.resource_types):
            query['ResourceTypes'] = request.resource_types
        if not DaraCore.is_null(request.scene):
            query['Scene'] = request.scene
        if not DaraCore.is_null(request.search_region_id):
            query['SearchRegionId'] = request.search_region_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        if not DaraCore.is_null(request.sort_type):
            query['SortType'] = request.sort_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserResources',
            version = '2020-10-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserResourcesResponse(),
            await self.do_rpcrequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    def describe_user_resources(
        self,
        request: main_models.DescribeUserResourcesRequest,
    ) -> main_models.DescribeUserResourcesResponse:
        runtime = RuntimeOptions()
        return self.describe_user_resources_with_options(request, runtime)

    async def describe_user_resources_async(
        self,
        request: main_models.DescribeUserResourcesRequest,
    ) -> main_models.DescribeUserResourcesResponse:
        runtime = RuntimeOptions()
        return await self.describe_user_resources_with_options_async(request, runtime)

    def encrypt_password_with_options(
        self,
        request: main_models.EncryptPasswordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EncryptPasswordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.login_token):
            query['LoginToken'] = request.login_token
        if not DaraCore.is_null(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EncryptPassword',
            version = '2020-10-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EncryptPasswordResponse(),
            self.do_rpcrequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    async def encrypt_password_with_options_async(
        self,
        request: main_models.EncryptPasswordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EncryptPasswordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.login_token):
            query['LoginToken'] = request.login_token
        if not DaraCore.is_null(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EncryptPassword',
            version = '2020-10-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EncryptPasswordResponse(),
            await self.do_rpcrequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    def encrypt_password(
        self,
        request: main_models.EncryptPasswordRequest,
    ) -> main_models.EncryptPasswordResponse:
        runtime = RuntimeOptions()
        return self.encrypt_password_with_options(request, runtime)

    async def encrypt_password_async(
        self,
        request: main_models.EncryptPasswordRequest,
    ) -> main_models.EncryptPasswordResponse:
        runtime = RuntimeOptions()
        return await self.encrypt_password_with_options_async(request, runtime)

    def get_cloud_drive_service_mount_token_with_options(
        self,
        request: main_models.GetCloudDriveServiceMountTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCloudDriveServiceMountTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.login_token):
            query['LoginToken'] = request.login_token
        if not DaraCore.is_null(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCloudDriveServiceMountToken',
            version = '2020-10-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCloudDriveServiceMountTokenResponse(),
            self.do_rpcrequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    async def get_cloud_drive_service_mount_token_with_options_async(
        self,
        request: main_models.GetCloudDriveServiceMountTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCloudDriveServiceMountTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.login_token):
            query['LoginToken'] = request.login_token
        if not DaraCore.is_null(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCloudDriveServiceMountToken',
            version = '2020-10-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCloudDriveServiceMountTokenResponse(),
            await self.do_rpcrequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    def get_cloud_drive_service_mount_token(
        self,
        request: main_models.GetCloudDriveServiceMountTokenRequest,
    ) -> main_models.GetCloudDriveServiceMountTokenResponse:
        runtime = RuntimeOptions()
        return self.get_cloud_drive_service_mount_token_with_options(request, runtime)

    async def get_cloud_drive_service_mount_token_async(
        self,
        request: main_models.GetCloudDriveServiceMountTokenRequest,
    ) -> main_models.GetCloudDriveServiceMountTokenResponse:
        runtime = RuntimeOptions()
        return await self.get_cloud_drive_service_mount_token_with_options_async(request, runtime)

    def get_connection_ticket_with_options(
        self,
        request: main_models.GetConnectionTicketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetConnectionTicketResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_type):
            query['AccessType'] = request.access_type
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.client_os):
            query['ClientOS'] = request.client_os
        if not DaraCore.is_null(request.client_type):
            query['ClientType'] = request.client_type
        if not DaraCore.is_null(request.client_version):
            query['ClientVersion'] = request.client_version
        if not DaraCore.is_null(request.command_content):
            query['CommandContent'] = request.command_content
        if not DaraCore.is_null(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not DaraCore.is_null(request.login_token):
            query['LoginToken'] = request.login_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.ticket_black_list):
            query['TicketBlackList'] = request.ticket_black_list
        if not DaraCore.is_null(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetConnectionTicket',
            version = '2020-10-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConnectionTicketResponse(),
            self.do_rpcrequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    async def get_connection_ticket_with_options_async(
        self,
        request: main_models.GetConnectionTicketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetConnectionTicketResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_type):
            query['AccessType'] = request.access_type
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.client_os):
            query['ClientOS'] = request.client_os
        if not DaraCore.is_null(request.client_type):
            query['ClientType'] = request.client_type
        if not DaraCore.is_null(request.client_version):
            query['ClientVersion'] = request.client_version
        if not DaraCore.is_null(request.command_content):
            query['CommandContent'] = request.command_content
        if not DaraCore.is_null(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not DaraCore.is_null(request.login_token):
            query['LoginToken'] = request.login_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.ticket_black_list):
            query['TicketBlackList'] = request.ticket_black_list
        if not DaraCore.is_null(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetConnectionTicket',
            version = '2020-10-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConnectionTicketResponse(),
            await self.do_rpcrequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    def get_connection_ticket(
        self,
        request: main_models.GetConnectionTicketRequest,
    ) -> main_models.GetConnectionTicketResponse:
        runtime = RuntimeOptions()
        return self.get_connection_ticket_with_options(request, runtime)

    async def get_connection_ticket_async(
        self,
        request: main_models.GetConnectionTicketRequest,
    ) -> main_models.GetConnectionTicketResponse:
        runtime = RuntimeOptions()
        return await self.get_connection_ticket_with_options_async(request, runtime)

    def get_login_token_with_options(
        self,
        tmp_req: main_models.GetLoginTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLoginTokenResponse:
        tmp_req.validate()
        request = main_models.GetLoginTokenShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.available_features):
            request.available_features_shrink = Utils.array_to_string_with_specified_style(tmp_req.available_features, 'AvailableFeatures', 'json')
        query = {}
        if not DaraCore.is_null(request.authentication_code):
            query['AuthenticationCode'] = request.authentication_code
        if not DaraCore.is_null(request.available_features_shrink):
            query['AvailableFeatures'] = request.available_features_shrink
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.client_name):
            query['ClientName'] = request.client_name
        if not DaraCore.is_null(request.client_os):
            query['ClientOS'] = request.client_os
        if not DaraCore.is_null(request.client_type):
            query['ClientType'] = request.client_type
        if not DaraCore.is_null(request.client_version):
            query['ClientVersion'] = request.client_version
        if not DaraCore.is_null(request.current_stage):
            query['CurrentStage'] = request.current_stage
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not DaraCore.is_null(request.keep_alive):
            query['KeepAlive'] = request.keep_alive
        if not DaraCore.is_null(request.keep_alive_token):
            query['KeepAliveToken'] = request.keep_alive_token
        if not DaraCore.is_null(request.new_password):
            query['NewPassword'] = request.new_password
        if not DaraCore.is_null(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not DaraCore.is_null(request.old_password):
            query['OldPassword'] = request.old_password
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        if not DaraCore.is_null(request.token_code):
            query['TokenCode'] = request.token_code
        if not DaraCore.is_null(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLoginToken',
            version = '2020-10-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLoginTokenResponse(),
            self.do_rpcrequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    async def get_login_token_with_options_async(
        self,
        tmp_req: main_models.GetLoginTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLoginTokenResponse:
        tmp_req.validate()
        request = main_models.GetLoginTokenShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.available_features):
            request.available_features_shrink = Utils.array_to_string_with_specified_style(tmp_req.available_features, 'AvailableFeatures', 'json')
        query = {}
        if not DaraCore.is_null(request.authentication_code):
            query['AuthenticationCode'] = request.authentication_code
        if not DaraCore.is_null(request.available_features_shrink):
            query['AvailableFeatures'] = request.available_features_shrink
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.client_name):
            query['ClientName'] = request.client_name
        if not DaraCore.is_null(request.client_os):
            query['ClientOS'] = request.client_os
        if not DaraCore.is_null(request.client_type):
            query['ClientType'] = request.client_type
        if not DaraCore.is_null(request.client_version):
            query['ClientVersion'] = request.client_version
        if not DaraCore.is_null(request.current_stage):
            query['CurrentStage'] = request.current_stage
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not DaraCore.is_null(request.keep_alive):
            query['KeepAlive'] = request.keep_alive
        if not DaraCore.is_null(request.keep_alive_token):
            query['KeepAliveToken'] = request.keep_alive_token
        if not DaraCore.is_null(request.new_password):
            query['NewPassword'] = request.new_password
        if not DaraCore.is_null(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not DaraCore.is_null(request.old_password):
            query['OldPassword'] = request.old_password
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        if not DaraCore.is_null(request.token_code):
            query['TokenCode'] = request.token_code
        if not DaraCore.is_null(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLoginToken',
            version = '2020-10-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLoginTokenResponse(),
            await self.do_rpcrequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    def get_login_token(
        self,
        request: main_models.GetLoginTokenRequest,
    ) -> main_models.GetLoginTokenResponse:
        runtime = RuntimeOptions()
        return self.get_login_token_with_options(request, runtime)

    async def get_login_token_async(
        self,
        request: main_models.GetLoginTokenRequest,
    ) -> main_models.GetLoginTokenResponse:
        runtime = RuntimeOptions()
        return await self.get_login_token_with_options_async(request, runtime)

    def is_keep_alive_with_options(
        self,
        request: main_models.IsKeepAliveRequest,
        runtime: RuntimeOptions,
    ) -> main_models.IsKeepAliveResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'IsKeepAlive',
            version = '2020-10-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.IsKeepAliveResponse(),
            self.do_rpcrequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    async def is_keep_alive_with_options_async(
        self,
        request: main_models.IsKeepAliveRequest,
        runtime: RuntimeOptions,
    ) -> main_models.IsKeepAliveResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'IsKeepAlive',
            version = '2020-10-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.IsKeepAliveResponse(),
            await self.do_rpcrequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    def is_keep_alive(
        self,
        request: main_models.IsKeepAliveRequest,
    ) -> main_models.IsKeepAliveResponse:
        runtime = RuntimeOptions()
        return self.is_keep_alive_with_options(request, runtime)

    async def is_keep_alive_async(
        self,
        request: main_models.IsKeepAliveRequest,
    ) -> main_models.IsKeepAliveResponse:
        runtime = RuntimeOptions()
        return await self.is_keep_alive_with_options_async(request, runtime)

    def query_eds_agent_report_config_with_options(
        self,
        request: main_models.QueryEdsAgentReportConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryEdsAgentReportConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not DaraCore.is_null(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not DaraCore.is_null(request.ecs_instance_id):
            query['EcsInstanceId'] = request.ecs_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryEdsAgentReportConfig',
            version = '2020-10-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryEdsAgentReportConfigResponse(),
            self.do_rpcrequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    async def query_eds_agent_report_config_with_options_async(
        self,
        request: main_models.QueryEdsAgentReportConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryEdsAgentReportConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not DaraCore.is_null(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not DaraCore.is_null(request.ecs_instance_id):
            query['EcsInstanceId'] = request.ecs_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryEdsAgentReportConfig',
            version = '2020-10-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryEdsAgentReportConfigResponse(),
            await self.do_rpcrequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    def query_eds_agent_report_config(
        self,
        request: main_models.QueryEdsAgentReportConfigRequest,
    ) -> main_models.QueryEdsAgentReportConfigResponse:
        runtime = RuntimeOptions()
        return self.query_eds_agent_report_config_with_options(request, runtime)

    async def query_eds_agent_report_config_async(
        self,
        request: main_models.QueryEdsAgentReportConfigRequest,
    ) -> main_models.QueryEdsAgentReportConfigResponse:
        runtime = RuntimeOptions()
        return await self.query_eds_agent_report_config_with_options_async(request, runtime)

    def reboot_desktops_with_options(
        self,
        request: main_models.RebootDesktopsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RebootDesktopsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.client_os):
            query['ClientOS'] = request.client_os
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.client_version):
            query['ClientVersion'] = request.client_version
        if not DaraCore.is_null(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not DaraCore.is_null(request.login_token):
            query['LoginToken'] = request.login_token
        if not DaraCore.is_null(request.os_update):
            query['OsUpdate'] = request.os_update
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        if not DaraCore.is_null(request.session_token):
            query['SessionToken'] = request.session_token
        if not DaraCore.is_null(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RebootDesktops',
            version = '2020-10-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RebootDesktopsResponse(),
            self.do_rpcrequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    async def reboot_desktops_with_options_async(
        self,
        request: main_models.RebootDesktopsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RebootDesktopsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.client_os):
            query['ClientOS'] = request.client_os
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.client_version):
            query['ClientVersion'] = request.client_version
        if not DaraCore.is_null(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not DaraCore.is_null(request.login_token):
            query['LoginToken'] = request.login_token
        if not DaraCore.is_null(request.os_update):
            query['OsUpdate'] = request.os_update
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        if not DaraCore.is_null(request.session_token):
            query['SessionToken'] = request.session_token
        if not DaraCore.is_null(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RebootDesktops',
            version = '2020-10-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RebootDesktopsResponse(),
            await self.do_rpcrequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    def reboot_desktops(
        self,
        request: main_models.RebootDesktopsRequest,
    ) -> main_models.RebootDesktopsResponse:
        runtime = RuntimeOptions()
        return self.reboot_desktops_with_options(request, runtime)

    async def reboot_desktops_async(
        self,
        request: main_models.RebootDesktopsRequest,
    ) -> main_models.RebootDesktopsResponse:
        runtime = RuntimeOptions()
        return await self.reboot_desktops_with_options_async(request, runtime)

    def refresh_login_token_with_options(
        self,
        request: main_models.RefreshLoginTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RefreshLoginTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not DaraCore.is_null(request.login_token):
            query['LoginToken'] = request.login_token
        if not DaraCore.is_null(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RefreshLoginToken',
            version = '2020-10-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RefreshLoginTokenResponse(),
            self.do_rpcrequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    async def refresh_login_token_with_options_async(
        self,
        request: main_models.RefreshLoginTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RefreshLoginTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not DaraCore.is_null(request.login_token):
            query['LoginToken'] = request.login_token
        if not DaraCore.is_null(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RefreshLoginToken',
            version = '2020-10-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RefreshLoginTokenResponse(),
            await self.do_rpcrequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    def refresh_login_token(
        self,
        request: main_models.RefreshLoginTokenRequest,
    ) -> main_models.RefreshLoginTokenResponse:
        runtime = RuntimeOptions()
        return self.refresh_login_token_with_options(request, runtime)

    async def refresh_login_token_async(
        self,
        request: main_models.RefreshLoginTokenRequest,
    ) -> main_models.RefreshLoginTokenResponse:
        runtime = RuntimeOptions()
        return await self.refresh_login_token_with_options_async(request, runtime)

    def report_eds_agent_info_with_options(
        self,
        request: main_models.ReportEdsAgentInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReportEdsAgentInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not DaraCore.is_null(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not DaraCore.is_null(request.ecs_instance_id):
            query['EcsInstanceId'] = request.ecs_instance_id
        if not DaraCore.is_null(request.eds_agent_info):
            query['EdsAgentInfo'] = request.eds_agent_info
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReportEdsAgentInfo',
            version = '2020-10-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReportEdsAgentInfoResponse(),
            self.do_rpcrequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    async def report_eds_agent_info_with_options_async(
        self,
        request: main_models.ReportEdsAgentInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReportEdsAgentInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not DaraCore.is_null(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not DaraCore.is_null(request.ecs_instance_id):
            query['EcsInstanceId'] = request.ecs_instance_id
        if not DaraCore.is_null(request.eds_agent_info):
            query['EdsAgentInfo'] = request.eds_agent_info
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReportEdsAgentInfo',
            version = '2020-10-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReportEdsAgentInfoResponse(),
            await self.do_rpcrequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    def report_eds_agent_info(
        self,
        request: main_models.ReportEdsAgentInfoRequest,
    ) -> main_models.ReportEdsAgentInfoResponse:
        runtime = RuntimeOptions()
        return self.report_eds_agent_info_with_options(request, runtime)

    async def report_eds_agent_info_async(
        self,
        request: main_models.ReportEdsAgentInfoRequest,
    ) -> main_models.ReportEdsAgentInfoResponse:
        runtime = RuntimeOptions()
        return await self.report_eds_agent_info_with_options_async(request, runtime)

    def report_session_status_with_options(
        self,
        request: main_models.ReportSessionStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReportSessionStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.session_change_time):
            query['SessionChangeTime'] = request.session_change_time
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        if not DaraCore.is_null(request.session_status):
            query['SessionStatus'] = request.session_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReportSessionStatus',
            version = '2020-10-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReportSessionStatusResponse(),
            self.do_rpcrequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    async def report_session_status_with_options_async(
        self,
        request: main_models.ReportSessionStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReportSessionStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.session_change_time):
            query['SessionChangeTime'] = request.session_change_time
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        if not DaraCore.is_null(request.session_status):
            query['SessionStatus'] = request.session_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReportSessionStatus',
            version = '2020-10-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReportSessionStatusResponse(),
            await self.do_rpcrequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    def report_session_status(
        self,
        request: main_models.ReportSessionStatusRequest,
    ) -> main_models.ReportSessionStatusResponse:
        runtime = RuntimeOptions()
        return self.report_session_status_with_options(request, runtime)

    async def report_session_status_async(
        self,
        request: main_models.ReportSessionStatusRequest,
    ) -> main_models.ReportSessionStatusResponse:
        runtime = RuntimeOptions()
        return await self.report_session_status_with_options_async(request, runtime)

    def reset_password_with_options(
        self,
        request: main_models.ResetPasswordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResetPasswordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not DaraCore.is_null(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.phone):
            query['phone'] = request.phone
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResetPassword',
            version = '2020-10-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetPasswordResponse(),
            self.do_rpcrequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    async def reset_password_with_options_async(
        self,
        request: main_models.ResetPasswordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResetPasswordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not DaraCore.is_null(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.phone):
            query['phone'] = request.phone
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResetPassword',
            version = '2020-10-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetPasswordResponse(),
            await self.do_rpcrequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    def reset_password(
        self,
        request: main_models.ResetPasswordRequest,
    ) -> main_models.ResetPasswordResponse:
        runtime = RuntimeOptions()
        return self.reset_password_with_options(request, runtime)

    async def reset_password_async(
        self,
        request: main_models.ResetPasswordRequest,
    ) -> main_models.ResetPasswordResponse:
        runtime = RuntimeOptions()
        return await self.reset_password_with_options_async(request, runtime)

    def reset_snapshot_with_options(
        self,
        request: main_models.ResetSnapshotRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResetSnapshotResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not DaraCore.is_null(request.login_token):
            query['LoginToken'] = request.login_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        if not DaraCore.is_null(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        if not DaraCore.is_null(request.stop_desktop):
            query['StopDesktop'] = request.stop_desktop
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResetSnapshot',
            version = '2020-10-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetSnapshotResponse(),
            self.do_rpcrequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    async def reset_snapshot_with_options_async(
        self,
        request: main_models.ResetSnapshotRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResetSnapshotResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not DaraCore.is_null(request.login_token):
            query['LoginToken'] = request.login_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        if not DaraCore.is_null(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        if not DaraCore.is_null(request.stop_desktop):
            query['StopDesktop'] = request.stop_desktop
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResetSnapshot',
            version = '2020-10-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetSnapshotResponse(),
            await self.do_rpcrequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    def reset_snapshot(
        self,
        request: main_models.ResetSnapshotRequest,
    ) -> main_models.ResetSnapshotResponse:
        runtime = RuntimeOptions()
        return self.reset_snapshot_with_options(request, runtime)

    async def reset_snapshot_async(
        self,
        request: main_models.ResetSnapshotRequest,
    ) -> main_models.ResetSnapshotResponse:
        runtime = RuntimeOptions()
        return await self.reset_snapshot_with_options_async(request, runtime)

    def send_token_code_with_options(
        self,
        request: main_models.SendTokenCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SendTokenCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.client_os):
            query['ClientOS'] = request.client_os
        if not DaraCore.is_null(request.client_version):
            query['ClientVersion'] = request.client_version
        if not DaraCore.is_null(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not DaraCore.is_null(request.login_token):
            query['LoginToken'] = request.login_token
        if not DaraCore.is_null(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        if not DaraCore.is_null(request.token_code):
            query['TokenCode'] = request.token_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SendTokenCode',
            version = '2020-10-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendTokenCodeResponse(),
            self.do_rpcrequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    async def send_token_code_with_options_async(
        self,
        request: main_models.SendTokenCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SendTokenCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.client_os):
            query['ClientOS'] = request.client_os
        if not DaraCore.is_null(request.client_version):
            query['ClientVersion'] = request.client_version
        if not DaraCore.is_null(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not DaraCore.is_null(request.login_token):
            query['LoginToken'] = request.login_token
        if not DaraCore.is_null(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        if not DaraCore.is_null(request.token_code):
            query['TokenCode'] = request.token_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SendTokenCode',
            version = '2020-10-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendTokenCodeResponse(),
            await self.do_rpcrequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    def send_token_code(
        self,
        request: main_models.SendTokenCodeRequest,
    ) -> main_models.SendTokenCodeResponse:
        runtime = RuntimeOptions()
        return self.send_token_code_with_options(request, runtime)

    async def send_token_code_async(
        self,
        request: main_models.SendTokenCodeRequest,
    ) -> main_models.SendTokenCodeResponse:
        runtime = RuntimeOptions()
        return await self.send_token_code_with_options_async(request, runtime)

    def set_finger_print_template_with_options(
        self,
        request: main_models.SetFingerPrintTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetFingerPrintTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.encrypted_finger_print_template):
            query['EncryptedFingerPrintTemplate'] = request.encrypted_finger_print_template
        if not DaraCore.is_null(request.encrypted_key):
            query['EncryptedKey'] = request.encrypted_key
        if not DaraCore.is_null(request.finger_print_template):
            query['FingerPrintTemplate'] = request.finger_print_template
        if not DaraCore.is_null(request.login_token):
            query['LoginToken'] = request.login_token
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetFingerPrintTemplate',
            version = '2020-10-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetFingerPrintTemplateResponse(),
            self.do_rpcrequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    async def set_finger_print_template_with_options_async(
        self,
        request: main_models.SetFingerPrintTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetFingerPrintTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.encrypted_finger_print_template):
            query['EncryptedFingerPrintTemplate'] = request.encrypted_finger_print_template
        if not DaraCore.is_null(request.encrypted_key):
            query['EncryptedKey'] = request.encrypted_key
        if not DaraCore.is_null(request.finger_print_template):
            query['FingerPrintTemplate'] = request.finger_print_template
        if not DaraCore.is_null(request.login_token):
            query['LoginToken'] = request.login_token
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetFingerPrintTemplate',
            version = '2020-10-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetFingerPrintTemplateResponse(),
            await self.do_rpcrequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    def set_finger_print_template(
        self,
        request: main_models.SetFingerPrintTemplateRequest,
    ) -> main_models.SetFingerPrintTemplateResponse:
        runtime = RuntimeOptions()
        return self.set_finger_print_template_with_options(request, runtime)

    async def set_finger_print_template_async(
        self,
        request: main_models.SetFingerPrintTemplateRequest,
    ) -> main_models.SetFingerPrintTemplateResponse:
        runtime = RuntimeOptions()
        return await self.set_finger_print_template_with_options_async(request, runtime)

    def set_finger_print_template_description_with_options(
        self,
        request: main_models.SetFingerPrintTemplateDescriptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetFingerPrintTemplateDescriptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.index):
            query['Index'] = request.index
        if not DaraCore.is_null(request.login_token):
            query['LoginToken'] = request.login_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetFingerPrintTemplateDescription',
            version = '2020-10-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetFingerPrintTemplateDescriptionResponse(),
            self.do_rpcrequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    async def set_finger_print_template_description_with_options_async(
        self,
        request: main_models.SetFingerPrintTemplateDescriptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetFingerPrintTemplateDescriptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.index):
            query['Index'] = request.index
        if not DaraCore.is_null(request.login_token):
            query['LoginToken'] = request.login_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetFingerPrintTemplateDescription',
            version = '2020-10-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetFingerPrintTemplateDescriptionResponse(),
            await self.do_rpcrequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    def set_finger_print_template_description(
        self,
        request: main_models.SetFingerPrintTemplateDescriptionRequest,
    ) -> main_models.SetFingerPrintTemplateDescriptionResponse:
        runtime = RuntimeOptions()
        return self.set_finger_print_template_description_with_options(request, runtime)

    async def set_finger_print_template_description_async(
        self,
        request: main_models.SetFingerPrintTemplateDescriptionRequest,
    ) -> main_models.SetFingerPrintTemplateDescriptionResponse:
        runtime = RuntimeOptions()
        return await self.set_finger_print_template_description_with_options_async(request, runtime)

    def start_desktops_with_options(
        self,
        request: main_models.StartDesktopsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartDesktopsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.client_os):
            query['ClientOS'] = request.client_os
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.client_version):
            query['ClientVersion'] = request.client_version
        if not DaraCore.is_null(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not DaraCore.is_null(request.login_token):
            query['LoginToken'] = request.login_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        if not DaraCore.is_null(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartDesktops',
            version = '2020-10-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartDesktopsResponse(),
            self.do_rpcrequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    async def start_desktops_with_options_async(
        self,
        request: main_models.StartDesktopsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartDesktopsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.client_os):
            query['ClientOS'] = request.client_os
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.client_version):
            query['ClientVersion'] = request.client_version
        if not DaraCore.is_null(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not DaraCore.is_null(request.login_token):
            query['LoginToken'] = request.login_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        if not DaraCore.is_null(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartDesktops',
            version = '2020-10-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartDesktopsResponse(),
            await self.do_rpcrequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    def start_desktops(
        self,
        request: main_models.StartDesktopsRequest,
    ) -> main_models.StartDesktopsResponse:
        runtime = RuntimeOptions()
        return self.start_desktops_with_options(request, runtime)

    async def start_desktops_async(
        self,
        request: main_models.StartDesktopsRequest,
    ) -> main_models.StartDesktopsResponse:
        runtime = RuntimeOptions()
        return await self.start_desktops_with_options_async(request, runtime)

    def start_record_content_with_options(
        self,
        request: main_models.StartRecordContentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartRecordContentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.client_os):
            query['ClientOS'] = request.client_os
        if not DaraCore.is_null(request.client_version):
            query['ClientVersion'] = request.client_version
        if not DaraCore.is_null(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not DaraCore.is_null(request.file_path):
            query['FilePath'] = request.file_path
        if not DaraCore.is_null(request.login_token):
            query['LoginToken'] = request.login_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartRecordContent',
            version = '2020-10-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartRecordContentResponse(),
            self.do_rpcrequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    async def start_record_content_with_options_async(
        self,
        request: main_models.StartRecordContentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartRecordContentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.client_os):
            query['ClientOS'] = request.client_os
        if not DaraCore.is_null(request.client_version):
            query['ClientVersion'] = request.client_version
        if not DaraCore.is_null(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not DaraCore.is_null(request.file_path):
            query['FilePath'] = request.file_path
        if not DaraCore.is_null(request.login_token):
            query['LoginToken'] = request.login_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartRecordContent',
            version = '2020-10-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartRecordContentResponse(),
            await self.do_rpcrequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    def start_record_content(
        self,
        request: main_models.StartRecordContentRequest,
    ) -> main_models.StartRecordContentResponse:
        runtime = RuntimeOptions()
        return self.start_record_content_with_options(request, runtime)

    async def start_record_content_async(
        self,
        request: main_models.StartRecordContentRequest,
    ) -> main_models.StartRecordContentResponse:
        runtime = RuntimeOptions()
        return await self.start_record_content_with_options_async(request, runtime)

    def stop_desktops_with_options(
        self,
        request: main_models.StopDesktopsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopDesktopsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.client_os):
            query['ClientOS'] = request.client_os
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.client_version):
            query['ClientVersion'] = request.client_version
        if not DaraCore.is_null(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not DaraCore.is_null(request.login_token):
            query['LoginToken'] = request.login_token
        if not DaraCore.is_null(request.os_update):
            query['OsUpdate'] = request.os_update
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        if not DaraCore.is_null(request.session_token):
            query['SessionToken'] = request.session_token
        if not DaraCore.is_null(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopDesktops',
            version = '2020-10-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopDesktopsResponse(),
            self.do_rpcrequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    async def stop_desktops_with_options_async(
        self,
        request: main_models.StopDesktopsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopDesktopsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.client_os):
            query['ClientOS'] = request.client_os
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.client_version):
            query['ClientVersion'] = request.client_version
        if not DaraCore.is_null(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not DaraCore.is_null(request.login_token):
            query['LoginToken'] = request.login_token
        if not DaraCore.is_null(request.os_update):
            query['OsUpdate'] = request.os_update
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        if not DaraCore.is_null(request.session_token):
            query['SessionToken'] = request.session_token
        if not DaraCore.is_null(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopDesktops',
            version = '2020-10-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopDesktopsResponse(),
            await self.do_rpcrequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    def stop_desktops(
        self,
        request: main_models.StopDesktopsRequest,
    ) -> main_models.StopDesktopsResponse:
        runtime = RuntimeOptions()
        return self.stop_desktops_with_options(request, runtime)

    async def stop_desktops_async(
        self,
        request: main_models.StopDesktopsRequest,
    ) -> main_models.StopDesktopsResponse:
        runtime = RuntimeOptions()
        return await self.stop_desktops_with_options_async(request, runtime)

    def stop_record_content_with_options(
        self,
        request: main_models.StopRecordContentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopRecordContentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.client_os):
            query['ClientOS'] = request.client_os
        if not DaraCore.is_null(request.client_version):
            query['ClientVersion'] = request.client_version
        if not DaraCore.is_null(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not DaraCore.is_null(request.login_token):
            query['LoginToken'] = request.login_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopRecordContent',
            version = '2020-10-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopRecordContentResponse(),
            self.do_rpcrequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    async def stop_record_content_with_options_async(
        self,
        request: main_models.StopRecordContentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopRecordContentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.client_os):
            query['ClientOS'] = request.client_os
        if not DaraCore.is_null(request.client_version):
            query['ClientVersion'] = request.client_version
        if not DaraCore.is_null(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not DaraCore.is_null(request.login_token):
            query['LoginToken'] = request.login_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopRecordContent',
            version = '2020-10-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopRecordContentResponse(),
            await self.do_rpcrequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    def stop_record_content(
        self,
        request: main_models.StopRecordContentRequest,
    ) -> main_models.StopRecordContentResponse:
        runtime = RuntimeOptions()
        return self.stop_record_content_with_options(request, runtime)

    async def stop_record_content_async(
        self,
        request: main_models.StopRecordContentRequest,
    ) -> main_models.StopRecordContentResponse:
        runtime = RuntimeOptions()
        return await self.stop_record_content_with_options_async(request, runtime)

    def unbind_user_desktop_with_options(
        self,
        request: main_models.UnbindUserDesktopRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnbindUserDesktopResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.client_type):
            query['ClientType'] = request.client_type
        if not DaraCore.is_null(request.force):
            query['Force'] = request.force
        if not DaraCore.is_null(request.login_token):
            query['LoginToken'] = request.login_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        if not DaraCore.is_null(request.user_desktop_id):
            query['UserDesktopId'] = request.user_desktop_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnbindUserDesktop',
            version = '2020-10-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindUserDesktopResponse(),
            self.do_rpcrequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    async def unbind_user_desktop_with_options_async(
        self,
        request: main_models.UnbindUserDesktopRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnbindUserDesktopResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.client_type):
            query['ClientType'] = request.client_type
        if not DaraCore.is_null(request.force):
            query['Force'] = request.force
        if not DaraCore.is_null(request.login_token):
            query['LoginToken'] = request.login_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        if not DaraCore.is_null(request.user_desktop_id):
            query['UserDesktopId'] = request.user_desktop_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnbindUserDesktop',
            version = '2020-10-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindUserDesktopResponse(),
            await self.do_rpcrequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    def unbind_user_desktop(
        self,
        request: main_models.UnbindUserDesktopRequest,
    ) -> main_models.UnbindUserDesktopResponse:
        runtime = RuntimeOptions()
        return self.unbind_user_desktop_with_options(request, runtime)

    async def unbind_user_desktop_async(
        self,
        request: main_models.UnbindUserDesktopRequest,
    ) -> main_models.UnbindUserDesktopResponse:
        runtime = RuntimeOptions()
        return await self.unbind_user_desktop_with_options_async(request, runtime)

    def verify_credential_with_options(
        self,
        request: main_models.VerifyCredentialRequest,
        runtime: RuntimeOptions,
    ) -> main_models.VerifyCredentialResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.credential):
            query['Credential'] = request.credential
        if not DaraCore.is_null(request.credential_type):
            query['CredentialType'] = request.credential_type
        if not DaraCore.is_null(request.encrypted_key):
            query['EncryptedKey'] = request.encrypted_key
        if not DaraCore.is_null(request.login_token):
            query['LoginToken'] = request.login_token
        if not DaraCore.is_null(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'VerifyCredential',
            version = '2020-10-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.VerifyCredentialResponse(),
            self.do_rpcrequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    async def verify_credential_with_options_async(
        self,
        request: main_models.VerifyCredentialRequest,
        runtime: RuntimeOptions,
    ) -> main_models.VerifyCredentialResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.credential):
            query['Credential'] = request.credential
        if not DaraCore.is_null(request.credential_type):
            query['CredentialType'] = request.credential_type
        if not DaraCore.is_null(request.encrypted_key):
            query['EncryptedKey'] = request.encrypted_key
        if not DaraCore.is_null(request.login_token):
            query['LoginToken'] = request.login_token
        if not DaraCore.is_null(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'VerifyCredential',
            version = '2020-10-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.VerifyCredentialResponse(),
            await self.do_rpcrequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    def verify_credential(
        self,
        request: main_models.VerifyCredentialRequest,
    ) -> main_models.VerifyCredentialResponse:
        runtime = RuntimeOptions()
        return self.verify_credential_with_options(request, runtime)

    async def verify_credential_async(
        self,
        request: main_models.VerifyCredentialRequest,
    ) -> main_models.VerifyCredentialResponse:
        runtime = RuntimeOptions()
        return await self.verify_credential_with_options_async(request, runtime)
