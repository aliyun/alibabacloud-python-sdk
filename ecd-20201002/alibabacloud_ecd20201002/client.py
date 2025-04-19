# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ecd20201002 import models as ecd_20201002_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(
        self, 
        config: open_api_models.Config,
    ):
        super().__init__(config)
        self._signature_algorithm = 'v2'
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def approve_fota_update_with_options(
        self,
        request: ecd_20201002_models.ApproveFotaUpdateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20201002_models.ApproveFotaUpdateResponse:
        """
        @summary 允许桌面FOTA升级
        
        @param request: ApproveFotaUpdateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ApproveFotaUpdateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_version):
            query['AppVersion'] = request.app_version
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.login_token):
            query['LoginToken'] = request.login_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.target_status):
            query['TargetStatus'] = request.target_status
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApproveFotaUpdate',
            version='2020-10-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20201002_models.ApproveFotaUpdateResponse(),
            self.call_api(params, req, runtime)
        )

    async def approve_fota_update_with_options_async(
        self,
        request: ecd_20201002_models.ApproveFotaUpdateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20201002_models.ApproveFotaUpdateResponse:
        """
        @summary 允许桌面FOTA升级
        
        @param request: ApproveFotaUpdateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ApproveFotaUpdateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_version):
            query['AppVersion'] = request.app_version
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.login_token):
            query['LoginToken'] = request.login_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.target_status):
            query['TargetStatus'] = request.target_status
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApproveFotaUpdate',
            version='2020-10-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20201002_models.ApproveFotaUpdateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def approve_fota_update(
        self,
        request: ecd_20201002_models.ApproveFotaUpdateRequest,
    ) -> ecd_20201002_models.ApproveFotaUpdateResponse:
        """
        @summary 允许桌面FOTA升级
        
        @param request: ApproveFotaUpdateRequest
        @return: ApproveFotaUpdateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.approve_fota_update_with_options(request, runtime)

    async def approve_fota_update_async(
        self,
        request: ecd_20201002_models.ApproveFotaUpdateRequest,
    ) -> ecd_20201002_models.ApproveFotaUpdateResponse:
        """
        @summary 允许桌面FOTA升级
        
        @param request: ApproveFotaUpdateRequest
        @return: ApproveFotaUpdateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.approve_fota_update_with_options_async(request, runtime)

    def change_password_with_options(
        self,
        request: ecd_20201002_models.ChangePasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20201002_models.ChangePasswordResponse:
        """
        @summary Changes the password of a user account.
        
        @param request: ChangePasswordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangePasswordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.login_token):
            query['LoginToken'] = request.login_token
        if not UtilClient.is_unset(request.new_password):
            query['NewPassword'] = request.new_password
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.old_password):
            query['OldPassword'] = request.old_password
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangePassword',
            version='2020-10-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20201002_models.ChangePasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_password_with_options_async(
        self,
        request: ecd_20201002_models.ChangePasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20201002_models.ChangePasswordResponse:
        """
        @summary Changes the password of a user account.
        
        @param request: ChangePasswordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangePasswordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.login_token):
            query['LoginToken'] = request.login_token
        if not UtilClient.is_unset(request.new_password):
            query['NewPassword'] = request.new_password
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.old_password):
            query['OldPassword'] = request.old_password
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangePassword',
            version='2020-10-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20201002_models.ChangePasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_password(
        self,
        request: ecd_20201002_models.ChangePasswordRequest,
    ) -> ecd_20201002_models.ChangePasswordResponse:
        """
        @summary Changes the password of a user account.
        
        @param request: ChangePasswordRequest
        @return: ChangePasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.change_password_with_options(request, runtime)

    async def change_password_async(
        self,
        request: ecd_20201002_models.ChangePasswordRequest,
    ) -> ecd_20201002_models.ChangePasswordResponse:
        """
        @summary Changes the password of a user account.
        
        @param request: ChangePasswordRequest
        @return: ChangePasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.change_password_with_options_async(request, runtime)

    def delete_finger_print_template_with_options(
        self,
        request: ecd_20201002_models.DeleteFingerPrintTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20201002_models.DeleteFingerPrintTemplateResponse:
        """
        @param request: DeleteFingerPrintTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFingerPrintTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.index):
            query['Index'] = request.index
        if not UtilClient.is_unset(request.login_token):
            query['LoginToken'] = request.login_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFingerPrintTemplate',
            version='2020-10-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20201002_models.DeleteFingerPrintTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_finger_print_template_with_options_async(
        self,
        request: ecd_20201002_models.DeleteFingerPrintTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20201002_models.DeleteFingerPrintTemplateResponse:
        """
        @param request: DeleteFingerPrintTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFingerPrintTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.index):
            query['Index'] = request.index
        if not UtilClient.is_unset(request.login_token):
            query['LoginToken'] = request.login_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFingerPrintTemplate',
            version='2020-10-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20201002_models.DeleteFingerPrintTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_finger_print_template(
        self,
        request: ecd_20201002_models.DeleteFingerPrintTemplateRequest,
    ) -> ecd_20201002_models.DeleteFingerPrintTemplateResponse:
        """
        @param request: DeleteFingerPrintTemplateRequest
        @return: DeleteFingerPrintTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_finger_print_template_with_options(request, runtime)

    async def delete_finger_print_template_async(
        self,
        request: ecd_20201002_models.DeleteFingerPrintTemplateRequest,
    ) -> ecd_20201002_models.DeleteFingerPrintTemplateResponse:
        """
        @param request: DeleteFingerPrintTemplateRequest
        @return: DeleteFingerPrintTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_finger_print_template_with_options_async(request, runtime)

    def describe_directories_with_options(
        self,
        request: ecd_20201002_models.DescribeDirectoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20201002_models.DescribeDirectoriesResponse:
        """
        @summary Queries directory details.
        
        @param request: DescribeDirectoriesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDirectoriesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDirectories',
            version='2020-10-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20201002_models.DescribeDirectoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_directories_with_options_async(
        self,
        request: ecd_20201002_models.DescribeDirectoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20201002_models.DescribeDirectoriesResponse:
        """
        @summary Queries directory details.
        
        @param request: DescribeDirectoriesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDirectoriesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDirectories',
            version='2020-10-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20201002_models.DescribeDirectoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_directories(
        self,
        request: ecd_20201002_models.DescribeDirectoriesRequest,
    ) -> ecd_20201002_models.DescribeDirectoriesResponse:
        """
        @summary Queries directory details.
        
        @param request: DescribeDirectoriesRequest
        @return: DescribeDirectoriesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_directories_with_options(request, runtime)

    async def describe_directories_async(
        self,
        request: ecd_20201002_models.DescribeDirectoriesRequest,
    ) -> ecd_20201002_models.DescribeDirectoriesResponse:
        """
        @summary Queries directory details.
        
        @param request: DescribeDirectoriesRequest
        @return: DescribeDirectoriesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_directories_with_options_async(request, runtime)

    def describe_finger_print_templates_with_options(
        self,
        request: ecd_20201002_models.DescribeFingerPrintTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20201002_models.DescribeFingerPrintTemplatesResponse:
        """
        @summary Queries fingerprint templates.
        
        @param request: DescribeFingerPrintTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeFingerPrintTemplatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.login_token):
            query['LoginToken'] = request.login_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFingerPrintTemplates',
            version='2020-10-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20201002_models.DescribeFingerPrintTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_finger_print_templates_with_options_async(
        self,
        request: ecd_20201002_models.DescribeFingerPrintTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20201002_models.DescribeFingerPrintTemplatesResponse:
        """
        @summary Queries fingerprint templates.
        
        @param request: DescribeFingerPrintTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeFingerPrintTemplatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.login_token):
            query['LoginToken'] = request.login_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFingerPrintTemplates',
            version='2020-10-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20201002_models.DescribeFingerPrintTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_finger_print_templates(
        self,
        request: ecd_20201002_models.DescribeFingerPrintTemplatesRequest,
    ) -> ecd_20201002_models.DescribeFingerPrintTemplatesResponse:
        """
        @summary Queries fingerprint templates.
        
        @param request: DescribeFingerPrintTemplatesRequest
        @return: DescribeFingerPrintTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_finger_print_templates_with_options(request, runtime)

    async def describe_finger_print_templates_async(
        self,
        request: ecd_20201002_models.DescribeFingerPrintTemplatesRequest,
    ) -> ecd_20201002_models.DescribeFingerPrintTemplatesResponse:
        """
        @summary Queries fingerprint templates.
        
        @param request: DescribeFingerPrintTemplatesRequest
        @return: DescribeFingerPrintTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_finger_print_templates_with_options_async(request, runtime)

    def describe_global_desktops_with_options(
        self,
        request: ecd_20201002_models.DescribeGlobalDesktopsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20201002_models.DescribeGlobalDesktopsResponse:
        """
        @param request: DescribeGlobalDesktopsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGlobalDesktopsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.desktop_access_type):
            query['DesktopAccessType'] = request.desktop_access_type
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.desktop_name):
            query['DesktopName'] = request.desktop_name
        if not UtilClient.is_unset(request.desktop_status):
            query['DesktopStatus'] = request.desktop_status
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.login_region_id):
            query['LoginRegionId'] = request.login_region_id
        if not UtilClient.is_unset(request.login_token):
            query['LoginToken'] = request.login_token
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.query_fota_update):
            query['QueryFotaUpdate'] = request.query_fota_update
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.search_region_id):
            query['SearchRegionId'] = request.search_region_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.sort_type):
            query['SortType'] = request.sort_type
        if not UtilClient.is_unset(request.without_latency):
            query['WithoutLatency'] = request.without_latency
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGlobalDesktops',
            version='2020-10-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20201002_models.DescribeGlobalDesktopsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_global_desktops_with_options_async(
        self,
        request: ecd_20201002_models.DescribeGlobalDesktopsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20201002_models.DescribeGlobalDesktopsResponse:
        """
        @param request: DescribeGlobalDesktopsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGlobalDesktopsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.desktop_access_type):
            query['DesktopAccessType'] = request.desktop_access_type
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.desktop_name):
            query['DesktopName'] = request.desktop_name
        if not UtilClient.is_unset(request.desktop_status):
            query['DesktopStatus'] = request.desktop_status
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.login_region_id):
            query['LoginRegionId'] = request.login_region_id
        if not UtilClient.is_unset(request.login_token):
            query['LoginToken'] = request.login_token
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.query_fota_update):
            query['QueryFotaUpdate'] = request.query_fota_update
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.search_region_id):
            query['SearchRegionId'] = request.search_region_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.sort_type):
            query['SortType'] = request.sort_type
        if not UtilClient.is_unset(request.without_latency):
            query['WithoutLatency'] = request.without_latency
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGlobalDesktops',
            version='2020-10-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20201002_models.DescribeGlobalDesktopsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_global_desktops(
        self,
        request: ecd_20201002_models.DescribeGlobalDesktopsRequest,
    ) -> ecd_20201002_models.DescribeGlobalDesktopsResponse:
        """
        @param request: DescribeGlobalDesktopsRequest
        @return: DescribeGlobalDesktopsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_global_desktops_with_options(request, runtime)

    async def describe_global_desktops_async(
        self,
        request: ecd_20201002_models.DescribeGlobalDesktopsRequest,
    ) -> ecd_20201002_models.DescribeGlobalDesktopsResponse:
        """
        @param request: DescribeGlobalDesktopsRequest
        @return: DescribeGlobalDesktopsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_global_desktops_with_options_async(request, runtime)

    def describe_office_sites_with_options(
        self,
        request: ecd_20201002_models.DescribeOfficeSitesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20201002_models.DescribeOfficeSitesResponse:
        """
        @param request: DescribeOfficeSitesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeOfficeSitesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOfficeSites',
            version='2020-10-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20201002_models.DescribeOfficeSitesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_office_sites_with_options_async(
        self,
        request: ecd_20201002_models.DescribeOfficeSitesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20201002_models.DescribeOfficeSitesResponse:
        """
        @param request: DescribeOfficeSitesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeOfficeSitesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOfficeSites',
            version='2020-10-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20201002_models.DescribeOfficeSitesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_office_sites(
        self,
        request: ecd_20201002_models.DescribeOfficeSitesRequest,
    ) -> ecd_20201002_models.DescribeOfficeSitesResponse:
        """
        @param request: DescribeOfficeSitesRequest
        @return: DescribeOfficeSitesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_office_sites_with_options(request, runtime)

    async def describe_office_sites_async(
        self,
        request: ecd_20201002_models.DescribeOfficeSitesRequest,
    ) -> ecd_20201002_models.DescribeOfficeSitesResponse:
        """
        @param request: DescribeOfficeSitesRequest
        @return: DescribeOfficeSitesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_office_sites_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: ecd_20201002_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20201002_models.DescribeRegionsResponse:
        """
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2020-10-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20201002_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: ecd_20201002_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20201002_models.DescribeRegionsResponse:
        """
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2020-10-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20201002_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: ecd_20201002_models.DescribeRegionsRequest,
    ) -> ecd_20201002_models.DescribeRegionsResponse:
        """
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: ecd_20201002_models.DescribeRegionsRequest,
    ) -> ecd_20201002_models.DescribeRegionsResponse:
        """
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_snapshots_with_options(
        self,
        request: ecd_20201002_models.DescribeSnapshotsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20201002_models.DescribeSnapshotsResponse:
        """
        @summary 列举快照
        
        @param request: DescribeSnapshotsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSnapshotsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.login_token):
            query['LoginToken'] = request.login_token
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSnapshots',
            version='2020-10-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20201002_models.DescribeSnapshotsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_snapshots_with_options_async(
        self,
        request: ecd_20201002_models.DescribeSnapshotsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20201002_models.DescribeSnapshotsResponse:
        """
        @summary 列举快照
        
        @param request: DescribeSnapshotsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSnapshotsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.login_token):
            query['LoginToken'] = request.login_token
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSnapshots',
            version='2020-10-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20201002_models.DescribeSnapshotsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_snapshots(
        self,
        request: ecd_20201002_models.DescribeSnapshotsRequest,
    ) -> ecd_20201002_models.DescribeSnapshotsResponse:
        """
        @summary 列举快照
        
        @param request: DescribeSnapshotsRequest
        @return: DescribeSnapshotsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_snapshots_with_options(request, runtime)

    async def describe_snapshots_async(
        self,
        request: ecd_20201002_models.DescribeSnapshotsRequest,
    ) -> ecd_20201002_models.DescribeSnapshotsResponse:
        """
        @summary 列举快照
        
        @param request: DescribeSnapshotsRequest
        @return: DescribeSnapshotsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_snapshots_with_options_async(request, runtime)

    def describe_user_resources_with_options(
        self,
        request: ecd_20201002_models.DescribeUserResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20201002_models.DescribeUserResourcesResponse:
        """
        @summary 查询用户资源列表
        
        @param request: DescribeUserResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUserResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_type):
            query['AccessType'] = request.access_type
        if not UtilClient.is_unset(request.auto_refresh):
            query['AutoRefresh'] = request.auto_refresh
        if not UtilClient.is_unset(request.category_id):
            query['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.category_type):
            query['CategoryType'] = request.category_type
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.client_type):
            query['ClientType'] = request.client_type
        if not UtilClient.is_unset(request.client_version):
            query['ClientVersion'] = request.client_version
        if not UtilClient.is_unset(request.dual_center_forward):
            query['DualCenterForward'] = request.dual_center_forward
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.login_region_id):
            query['LoginRegionId'] = request.login_region_id
        if not UtilClient.is_unset(request.login_token):
            query['LoginToken'] = request.login_token
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.office_site_ids):
            query['OfficeSiteIds'] = request.office_site_ids
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.product_types):
            query['ProductTypes'] = request.product_types
        if not UtilClient.is_unset(request.protocol_type):
            query['ProtocolType'] = request.protocol_type
        if not UtilClient.is_unset(request.query_fota_update):
            query['QueryFotaUpdate'] = request.query_fota_update
        if not UtilClient.is_unset(request.refresh_fota_update):
            query['RefreshFotaUpdate'] = request.refresh_fota_update
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not UtilClient.is_unset(request.resource_types):
            query['ResourceTypes'] = request.resource_types
        if not UtilClient.is_unset(request.scene):
            query['Scene'] = request.scene
        if not UtilClient.is_unset(request.search_region_id):
            query['SearchRegionId'] = request.search_region_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.sort_type):
            query['SortType'] = request.sort_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserResources',
            version='2020-10-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20201002_models.DescribeUserResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_resources_with_options_async(
        self,
        request: ecd_20201002_models.DescribeUserResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20201002_models.DescribeUserResourcesResponse:
        """
        @summary 查询用户资源列表
        
        @param request: DescribeUserResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUserResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_type):
            query['AccessType'] = request.access_type
        if not UtilClient.is_unset(request.auto_refresh):
            query['AutoRefresh'] = request.auto_refresh
        if not UtilClient.is_unset(request.category_id):
            query['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.category_type):
            query['CategoryType'] = request.category_type
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.client_type):
            query['ClientType'] = request.client_type
        if not UtilClient.is_unset(request.client_version):
            query['ClientVersion'] = request.client_version
        if not UtilClient.is_unset(request.dual_center_forward):
            query['DualCenterForward'] = request.dual_center_forward
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.login_region_id):
            query['LoginRegionId'] = request.login_region_id
        if not UtilClient.is_unset(request.login_token):
            query['LoginToken'] = request.login_token
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.office_site_ids):
            query['OfficeSiteIds'] = request.office_site_ids
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.product_types):
            query['ProductTypes'] = request.product_types
        if not UtilClient.is_unset(request.protocol_type):
            query['ProtocolType'] = request.protocol_type
        if not UtilClient.is_unset(request.query_fota_update):
            query['QueryFotaUpdate'] = request.query_fota_update
        if not UtilClient.is_unset(request.refresh_fota_update):
            query['RefreshFotaUpdate'] = request.refresh_fota_update
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not UtilClient.is_unset(request.resource_types):
            query['ResourceTypes'] = request.resource_types
        if not UtilClient.is_unset(request.scene):
            query['Scene'] = request.scene
        if not UtilClient.is_unset(request.search_region_id):
            query['SearchRegionId'] = request.search_region_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.sort_type):
            query['SortType'] = request.sort_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserResources',
            version='2020-10-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20201002_models.DescribeUserResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_resources(
        self,
        request: ecd_20201002_models.DescribeUserResourcesRequest,
    ) -> ecd_20201002_models.DescribeUserResourcesResponse:
        """
        @summary 查询用户资源列表
        
        @param request: DescribeUserResourcesRequest
        @return: DescribeUserResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_user_resources_with_options(request, runtime)

    async def describe_user_resources_async(
        self,
        request: ecd_20201002_models.DescribeUserResourcesRequest,
    ) -> ecd_20201002_models.DescribeUserResourcesResponse:
        """
        @summary 查询用户资源列表
        
        @param request: DescribeUserResourcesRequest
        @return: DescribeUserResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_resources_with_options_async(request, runtime)

    def encrypt_password_with_options(
        self,
        request: ecd_20201002_models.EncryptPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20201002_models.EncryptPasswordResponse:
        """
        @summary Encrypts a password.
        
        @param request: EncryptPasswordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EncryptPasswordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.login_token):
            query['LoginToken'] = request.login_token
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EncryptPassword',
            version='2020-10-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20201002_models.EncryptPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def encrypt_password_with_options_async(
        self,
        request: ecd_20201002_models.EncryptPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20201002_models.EncryptPasswordResponse:
        """
        @summary Encrypts a password.
        
        @param request: EncryptPasswordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EncryptPasswordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.login_token):
            query['LoginToken'] = request.login_token
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EncryptPassword',
            version='2020-10-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20201002_models.EncryptPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def encrypt_password(
        self,
        request: ecd_20201002_models.EncryptPasswordRequest,
    ) -> ecd_20201002_models.EncryptPasswordResponse:
        """
        @summary Encrypts a password.
        
        @param request: EncryptPasswordRequest
        @return: EncryptPasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.encrypt_password_with_options(request, runtime)

    async def encrypt_password_async(
        self,
        request: ecd_20201002_models.EncryptPasswordRequest,
    ) -> ecd_20201002_models.EncryptPasswordResponse:
        """
        @summary Encrypts a password.
        
        @param request: EncryptPasswordRequest
        @return: EncryptPasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.encrypt_password_with_options_async(request, runtime)

    def get_cloud_drive_service_mount_token_with_options(
        self,
        request: ecd_20201002_models.GetCloudDriveServiceMountTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20201002_models.GetCloudDriveServiceMountTokenResponse:
        """
        @summary 获取无影云盘的免密token
        
        @param request: GetCloudDriveServiceMountTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCloudDriveServiceMountTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.login_token):
            query['LoginToken'] = request.login_token
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCloudDriveServiceMountToken',
            version='2020-10-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20201002_models.GetCloudDriveServiceMountTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_cloud_drive_service_mount_token_with_options_async(
        self,
        request: ecd_20201002_models.GetCloudDriveServiceMountTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20201002_models.GetCloudDriveServiceMountTokenResponse:
        """
        @summary 获取无影云盘的免密token
        
        @param request: GetCloudDriveServiceMountTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCloudDriveServiceMountTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.login_token):
            query['LoginToken'] = request.login_token
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCloudDriveServiceMountToken',
            version='2020-10-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20201002_models.GetCloudDriveServiceMountTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_cloud_drive_service_mount_token(
        self,
        request: ecd_20201002_models.GetCloudDriveServiceMountTokenRequest,
    ) -> ecd_20201002_models.GetCloudDriveServiceMountTokenResponse:
        """
        @summary 获取无影云盘的免密token
        
        @param request: GetCloudDriveServiceMountTokenRequest
        @return: GetCloudDriveServiceMountTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_cloud_drive_service_mount_token_with_options(request, runtime)

    async def get_cloud_drive_service_mount_token_async(
        self,
        request: ecd_20201002_models.GetCloudDriveServiceMountTokenRequest,
    ) -> ecd_20201002_models.GetCloudDriveServiceMountTokenResponse:
        """
        @summary 获取无影云盘的免密token
        
        @param request: GetCloudDriveServiceMountTokenRequest
        @return: GetCloudDriveServiceMountTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_cloud_drive_service_mount_token_with_options_async(request, runtime)

    def get_connection_ticket_with_options(
        self,
        request: ecd_20201002_models.GetConnectionTicketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20201002_models.GetConnectionTicketResponse:
        """
        @param request: GetConnectionTicketRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetConnectionTicketResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.client_os):
            query['ClientOS'] = request.client_os
        if not UtilClient.is_unset(request.client_type):
            query['ClientType'] = request.client_type
        if not UtilClient.is_unset(request.client_version):
            query['ClientVersion'] = request.client_version
        if not UtilClient.is_unset(request.command_content):
            query['CommandContent'] = request.command_content
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.login_token):
            query['LoginToken'] = request.login_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetConnectionTicket',
            version='2020-10-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20201002_models.GetConnectionTicketResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_connection_ticket_with_options_async(
        self,
        request: ecd_20201002_models.GetConnectionTicketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20201002_models.GetConnectionTicketResponse:
        """
        @param request: GetConnectionTicketRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetConnectionTicketResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.client_os):
            query['ClientOS'] = request.client_os
        if not UtilClient.is_unset(request.client_type):
            query['ClientType'] = request.client_type
        if not UtilClient.is_unset(request.client_version):
            query['ClientVersion'] = request.client_version
        if not UtilClient.is_unset(request.command_content):
            query['CommandContent'] = request.command_content
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.login_token):
            query['LoginToken'] = request.login_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetConnectionTicket',
            version='2020-10-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20201002_models.GetConnectionTicketResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_connection_ticket(
        self,
        request: ecd_20201002_models.GetConnectionTicketRequest,
    ) -> ecd_20201002_models.GetConnectionTicketResponse:
        """
        @param request: GetConnectionTicketRequest
        @return: GetConnectionTicketResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_connection_ticket_with_options(request, runtime)

    async def get_connection_ticket_async(
        self,
        request: ecd_20201002_models.GetConnectionTicketRequest,
    ) -> ecd_20201002_models.GetConnectionTicketResponse:
        """
        @param request: GetConnectionTicketRequest
        @return: GetConnectionTicketResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_connection_ticket_with_options_async(request, runtime)

    def get_login_token_with_options(
        self,
        request: ecd_20201002_models.GetLoginTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20201002_models.GetLoginTokenResponse:
        """
        @summary Obtains logon credentials.
        
        @param request: GetLoginTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLoginTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authentication_code):
            query['AuthenticationCode'] = request.authentication_code
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.client_os):
            query['ClientOS'] = request.client_os
        if not UtilClient.is_unset(request.client_type):
            query['ClientType'] = request.client_type
        if not UtilClient.is_unset(request.client_version):
            query['ClientVersion'] = request.client_version
        if not UtilClient.is_unset(request.current_stage):
            query['CurrentStage'] = request.current_stage
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.keep_alive):
            query['KeepAlive'] = request.keep_alive
        if not UtilClient.is_unset(request.keep_alive_token):
            query['KeepAliveToken'] = request.keep_alive_token
        if not UtilClient.is_unset(request.new_password):
            query['NewPassword'] = request.new_password
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.old_password):
            query['OldPassword'] = request.old_password
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.token_code):
            query['TokenCode'] = request.token_code
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLoginToken',
            version='2020-10-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20201002_models.GetLoginTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_login_token_with_options_async(
        self,
        request: ecd_20201002_models.GetLoginTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20201002_models.GetLoginTokenResponse:
        """
        @summary Obtains logon credentials.
        
        @param request: GetLoginTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLoginTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authentication_code):
            query['AuthenticationCode'] = request.authentication_code
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.client_os):
            query['ClientOS'] = request.client_os
        if not UtilClient.is_unset(request.client_type):
            query['ClientType'] = request.client_type
        if not UtilClient.is_unset(request.client_version):
            query['ClientVersion'] = request.client_version
        if not UtilClient.is_unset(request.current_stage):
            query['CurrentStage'] = request.current_stage
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.keep_alive):
            query['KeepAlive'] = request.keep_alive
        if not UtilClient.is_unset(request.keep_alive_token):
            query['KeepAliveToken'] = request.keep_alive_token
        if not UtilClient.is_unset(request.new_password):
            query['NewPassword'] = request.new_password
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.old_password):
            query['OldPassword'] = request.old_password
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.token_code):
            query['TokenCode'] = request.token_code
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLoginToken',
            version='2020-10-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20201002_models.GetLoginTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_login_token(
        self,
        request: ecd_20201002_models.GetLoginTokenRequest,
    ) -> ecd_20201002_models.GetLoginTokenResponse:
        """
        @summary Obtains logon credentials.
        
        @param request: GetLoginTokenRequest
        @return: GetLoginTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_login_token_with_options(request, runtime)

    async def get_login_token_async(
        self,
        request: ecd_20201002_models.GetLoginTokenRequest,
    ) -> ecd_20201002_models.GetLoginTokenResponse:
        """
        @summary Obtains logon credentials.
        
        @param request: GetLoginTokenRequest
        @return: GetLoginTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_login_token_with_options_async(request, runtime)

    def is_keep_alive_with_options(
        self,
        request: ecd_20201002_models.IsKeepAliveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20201002_models.IsKeepAliveResponse:
        """
        @summary 是否保持登录判断接口
        
        @param request: IsKeepAliveRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: IsKeepAliveResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='IsKeepAlive',
            version='2020-10-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20201002_models.IsKeepAliveResponse(),
            self.call_api(params, req, runtime)
        )

    async def is_keep_alive_with_options_async(
        self,
        request: ecd_20201002_models.IsKeepAliveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20201002_models.IsKeepAliveResponse:
        """
        @summary 是否保持登录判断接口
        
        @param request: IsKeepAliveRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: IsKeepAliveResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='IsKeepAlive',
            version='2020-10-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20201002_models.IsKeepAliveResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def is_keep_alive(
        self,
        request: ecd_20201002_models.IsKeepAliveRequest,
    ) -> ecd_20201002_models.IsKeepAliveResponse:
        """
        @summary 是否保持登录判断接口
        
        @param request: IsKeepAliveRequest
        @return: IsKeepAliveResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.is_keep_alive_with_options(request, runtime)

    async def is_keep_alive_async(
        self,
        request: ecd_20201002_models.IsKeepAliveRequest,
    ) -> ecd_20201002_models.IsKeepAliveResponse:
        """
        @summary 是否保持登录判断接口
        
        @param request: IsKeepAliveRequest
        @return: IsKeepAliveResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.is_keep_alive_with_options_async(request, runtime)

    def query_eds_agent_report_config_with_options(
        self,
        request: ecd_20201002_models.QueryEdsAgentReportConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20201002_models.QueryEdsAgentReportConfigResponse:
        """
        @summary 查询Agent需要上报的配置信息
        
        @param request: QueryEdsAgentReportConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryEdsAgentReportConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.ecs_instance_id):
            query['EcsInstanceId'] = request.ecs_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryEdsAgentReportConfig',
            version='2020-10-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20201002_models.QueryEdsAgentReportConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_eds_agent_report_config_with_options_async(
        self,
        request: ecd_20201002_models.QueryEdsAgentReportConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20201002_models.QueryEdsAgentReportConfigResponse:
        """
        @summary 查询Agent需要上报的配置信息
        
        @param request: QueryEdsAgentReportConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryEdsAgentReportConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.ecs_instance_id):
            query['EcsInstanceId'] = request.ecs_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryEdsAgentReportConfig',
            version='2020-10-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20201002_models.QueryEdsAgentReportConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_eds_agent_report_config(
        self,
        request: ecd_20201002_models.QueryEdsAgentReportConfigRequest,
    ) -> ecd_20201002_models.QueryEdsAgentReportConfigResponse:
        """
        @summary 查询Agent需要上报的配置信息
        
        @param request: QueryEdsAgentReportConfigRequest
        @return: QueryEdsAgentReportConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_eds_agent_report_config_with_options(request, runtime)

    async def query_eds_agent_report_config_async(
        self,
        request: ecd_20201002_models.QueryEdsAgentReportConfigRequest,
    ) -> ecd_20201002_models.QueryEdsAgentReportConfigResponse:
        """
        @summary 查询Agent需要上报的配置信息
        
        @param request: QueryEdsAgentReportConfigRequest
        @return: QueryEdsAgentReportConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_eds_agent_report_config_with_options_async(request, runtime)

    def reboot_desktops_with_options(
        self,
        request: ecd_20201002_models.RebootDesktopsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20201002_models.RebootDesktopsResponse:
        """
        @summary Restart cloud computers.
        
        @param request: RebootDesktopsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RebootDesktopsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.client_os):
            query['ClientOS'] = request.client_os
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.client_version):
            query['ClientVersion'] = request.client_version
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.login_token):
            query['LoginToken'] = request.login_token
        if not UtilClient.is_unset(request.os_update):
            query['OsUpdate'] = request.os_update
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.session_token):
            query['SessionToken'] = request.session_token
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RebootDesktops',
            version='2020-10-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20201002_models.RebootDesktopsResponse(),
            self.call_api(params, req, runtime)
        )

    async def reboot_desktops_with_options_async(
        self,
        request: ecd_20201002_models.RebootDesktopsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20201002_models.RebootDesktopsResponse:
        """
        @summary Restart cloud computers.
        
        @param request: RebootDesktopsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RebootDesktopsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.client_os):
            query['ClientOS'] = request.client_os
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.client_version):
            query['ClientVersion'] = request.client_version
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.login_token):
            query['LoginToken'] = request.login_token
        if not UtilClient.is_unset(request.os_update):
            query['OsUpdate'] = request.os_update
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.session_token):
            query['SessionToken'] = request.session_token
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RebootDesktops',
            version='2020-10-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20201002_models.RebootDesktopsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reboot_desktops(
        self,
        request: ecd_20201002_models.RebootDesktopsRequest,
    ) -> ecd_20201002_models.RebootDesktopsResponse:
        """
        @summary Restart cloud computers.
        
        @param request: RebootDesktopsRequest
        @return: RebootDesktopsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reboot_desktops_with_options(request, runtime)

    async def reboot_desktops_async(
        self,
        request: ecd_20201002_models.RebootDesktopsRequest,
    ) -> ecd_20201002_models.RebootDesktopsResponse:
        """
        @summary Restart cloud computers.
        
        @param request: RebootDesktopsRequest
        @return: RebootDesktopsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.reboot_desktops_with_options_async(request, runtime)

    def refresh_login_token_with_options(
        self,
        request: ecd_20201002_models.RefreshLoginTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20201002_models.RefreshLoginTokenResponse:
        """
        @param request: RefreshLoginTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RefreshLoginTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.login_token):
            query['LoginToken'] = request.login_token
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefreshLoginToken',
            version='2020-10-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20201002_models.RefreshLoginTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def refresh_login_token_with_options_async(
        self,
        request: ecd_20201002_models.RefreshLoginTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20201002_models.RefreshLoginTokenResponse:
        """
        @param request: RefreshLoginTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RefreshLoginTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.login_token):
            query['LoginToken'] = request.login_token
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefreshLoginToken',
            version='2020-10-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20201002_models.RefreshLoginTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refresh_login_token(
        self,
        request: ecd_20201002_models.RefreshLoginTokenRequest,
    ) -> ecd_20201002_models.RefreshLoginTokenResponse:
        """
        @param request: RefreshLoginTokenRequest
        @return: RefreshLoginTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.refresh_login_token_with_options(request, runtime)

    async def refresh_login_token_async(
        self,
        request: ecd_20201002_models.RefreshLoginTokenRequest,
    ) -> ecd_20201002_models.RefreshLoginTokenResponse:
        """
        @param request: RefreshLoginTokenRequest
        @return: RefreshLoginTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.refresh_login_token_with_options_async(request, runtime)

    def report_eds_agent_info_with_options(
        self,
        request: ecd_20201002_models.ReportEdsAgentInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20201002_models.ReportEdsAgentInfoResponse:
        """
        @summary 上报edsAgent的信息
        
        @param request: ReportEdsAgentInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReportEdsAgentInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.ecs_instance_id):
            query['EcsInstanceId'] = request.ecs_instance_id
        if not UtilClient.is_unset(request.eds_agent_info):
            query['EdsAgentInfo'] = request.eds_agent_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReportEdsAgentInfo',
            version='2020-10-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20201002_models.ReportEdsAgentInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def report_eds_agent_info_with_options_async(
        self,
        request: ecd_20201002_models.ReportEdsAgentInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20201002_models.ReportEdsAgentInfoResponse:
        """
        @summary 上报edsAgent的信息
        
        @param request: ReportEdsAgentInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReportEdsAgentInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.ecs_instance_id):
            query['EcsInstanceId'] = request.ecs_instance_id
        if not UtilClient.is_unset(request.eds_agent_info):
            query['EdsAgentInfo'] = request.eds_agent_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReportEdsAgentInfo',
            version='2020-10-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20201002_models.ReportEdsAgentInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def report_eds_agent_info(
        self,
        request: ecd_20201002_models.ReportEdsAgentInfoRequest,
    ) -> ecd_20201002_models.ReportEdsAgentInfoResponse:
        """
        @summary 上报edsAgent的信息
        
        @param request: ReportEdsAgentInfoRequest
        @return: ReportEdsAgentInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.report_eds_agent_info_with_options(request, runtime)

    async def report_eds_agent_info_async(
        self,
        request: ecd_20201002_models.ReportEdsAgentInfoRequest,
    ) -> ecd_20201002_models.ReportEdsAgentInfoResponse:
        """
        @summary 上报edsAgent的信息
        
        @param request: ReportEdsAgentInfoRequest
        @return: ReportEdsAgentInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.report_eds_agent_info_with_options_async(request, runtime)

    def report_session_status_with_options(
        self,
        request: ecd_20201002_models.ReportSessionStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20201002_models.ReportSessionStatusResponse:
        """
        @param request: ReportSessionStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReportSessionStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.session_change_time):
            query['SessionChangeTime'] = request.session_change_time
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.session_status):
            query['SessionStatus'] = request.session_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReportSessionStatus',
            version='2020-10-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20201002_models.ReportSessionStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def report_session_status_with_options_async(
        self,
        request: ecd_20201002_models.ReportSessionStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20201002_models.ReportSessionStatusResponse:
        """
        @param request: ReportSessionStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReportSessionStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.session_change_time):
            query['SessionChangeTime'] = request.session_change_time
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.session_status):
            query['SessionStatus'] = request.session_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReportSessionStatus',
            version='2020-10-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20201002_models.ReportSessionStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def report_session_status(
        self,
        request: ecd_20201002_models.ReportSessionStatusRequest,
    ) -> ecd_20201002_models.ReportSessionStatusResponse:
        """
        @param request: ReportSessionStatusRequest
        @return: ReportSessionStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.report_session_status_with_options(request, runtime)

    async def report_session_status_async(
        self,
        request: ecd_20201002_models.ReportSessionStatusRequest,
    ) -> ecd_20201002_models.ReportSessionStatusResponse:
        """
        @param request: ReportSessionStatusRequest
        @return: ReportSessionStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.report_session_status_with_options_async(request, runtime)

    def reset_password_with_options(
        self,
        request: ecd_20201002_models.ResetPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20201002_models.ResetPasswordResponse:
        """
        @summary Resets a password.
        
        @param request: ResetPasswordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetPasswordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.phone):
            query['phone'] = request.phone
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetPassword',
            version='2020-10-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20201002_models.ResetPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_password_with_options_async(
        self,
        request: ecd_20201002_models.ResetPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20201002_models.ResetPasswordResponse:
        """
        @summary Resets a password.
        
        @param request: ResetPasswordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetPasswordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.phone):
            query['phone'] = request.phone
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetPassword',
            version='2020-10-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20201002_models.ResetPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_password(
        self,
        request: ecd_20201002_models.ResetPasswordRequest,
    ) -> ecd_20201002_models.ResetPasswordResponse:
        """
        @summary Resets a password.
        
        @param request: ResetPasswordRequest
        @return: ResetPasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reset_password_with_options(request, runtime)

    async def reset_password_async(
        self,
        request: ecd_20201002_models.ResetPasswordRequest,
    ) -> ecd_20201002_models.ResetPasswordResponse:
        """
        @summary Resets a password.
        
        @param request: ResetPasswordRequest
        @return: ResetPasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.reset_password_with_options_async(request, runtime)

    def reset_snapshot_with_options(
        self,
        request: ecd_20201002_models.ResetSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20201002_models.ResetSnapshotResponse:
        """
        @summary Restores the data of a disk from a snapshot.
        
        @param request: ResetSnapshotRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetSnapshotResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.login_token):
            query['LoginToken'] = request.login_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        if not UtilClient.is_unset(request.stop_desktop):
            query['StopDesktop'] = request.stop_desktop
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetSnapshot',
            version='2020-10-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20201002_models.ResetSnapshotResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_snapshot_with_options_async(
        self,
        request: ecd_20201002_models.ResetSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20201002_models.ResetSnapshotResponse:
        """
        @summary Restores the data of a disk from a snapshot.
        
        @param request: ResetSnapshotRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetSnapshotResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.login_token):
            query['LoginToken'] = request.login_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        if not UtilClient.is_unset(request.stop_desktop):
            query['StopDesktop'] = request.stop_desktop
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetSnapshot',
            version='2020-10-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20201002_models.ResetSnapshotResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_snapshot(
        self,
        request: ecd_20201002_models.ResetSnapshotRequest,
    ) -> ecd_20201002_models.ResetSnapshotResponse:
        """
        @summary Restores the data of a disk from a snapshot.
        
        @param request: ResetSnapshotRequest
        @return: ResetSnapshotResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reset_snapshot_with_options(request, runtime)

    async def reset_snapshot_async(
        self,
        request: ecd_20201002_models.ResetSnapshotRequest,
    ) -> ecd_20201002_models.ResetSnapshotResponse:
        """
        @summary Restores the data of a disk from a snapshot.
        
        @param request: ResetSnapshotRequest
        @return: ResetSnapshotResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.reset_snapshot_with_options_async(request, runtime)

    def send_token_code_with_options(
        self,
        request: ecd_20201002_models.SendTokenCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20201002_models.SendTokenCodeResponse:
        """
        @summary Sends a logon verification code.
        
        @param request: SendTokenCodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendTokenCodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.client_os):
            query['ClientOS'] = request.client_os
        if not UtilClient.is_unset(request.client_version):
            query['ClientVersion'] = request.client_version
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.login_token):
            query['LoginToken'] = request.login_token
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.token_code):
            query['TokenCode'] = request.token_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendTokenCode',
            version='2020-10-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20201002_models.SendTokenCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_token_code_with_options_async(
        self,
        request: ecd_20201002_models.SendTokenCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20201002_models.SendTokenCodeResponse:
        """
        @summary Sends a logon verification code.
        
        @param request: SendTokenCodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendTokenCodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.client_os):
            query['ClientOS'] = request.client_os
        if not UtilClient.is_unset(request.client_version):
            query['ClientVersion'] = request.client_version
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.login_token):
            query['LoginToken'] = request.login_token
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.token_code):
            query['TokenCode'] = request.token_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendTokenCode',
            version='2020-10-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20201002_models.SendTokenCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_token_code(
        self,
        request: ecd_20201002_models.SendTokenCodeRequest,
    ) -> ecd_20201002_models.SendTokenCodeResponse:
        """
        @summary Sends a logon verification code.
        
        @param request: SendTokenCodeRequest
        @return: SendTokenCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.send_token_code_with_options(request, runtime)

    async def send_token_code_async(
        self,
        request: ecd_20201002_models.SendTokenCodeRequest,
    ) -> ecd_20201002_models.SendTokenCodeResponse:
        """
        @summary Sends a logon verification code.
        
        @param request: SendTokenCodeRequest
        @return: SendTokenCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.send_token_code_with_options_async(request, runtime)

    def set_finger_print_template_with_options(
        self,
        request: ecd_20201002_models.SetFingerPrintTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20201002_models.SetFingerPrintTemplateResponse:
        """
        @param request: SetFingerPrintTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetFingerPrintTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.encrypted_finger_print_template):
            query['EncryptedFingerPrintTemplate'] = request.encrypted_finger_print_template
        if not UtilClient.is_unset(request.encrypted_key):
            query['EncryptedKey'] = request.encrypted_key
        if not UtilClient.is_unset(request.finger_print_template):
            query['FingerPrintTemplate'] = request.finger_print_template
        if not UtilClient.is_unset(request.login_token):
            query['LoginToken'] = request.login_token
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetFingerPrintTemplate',
            version='2020-10-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20201002_models.SetFingerPrintTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_finger_print_template_with_options_async(
        self,
        request: ecd_20201002_models.SetFingerPrintTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20201002_models.SetFingerPrintTemplateResponse:
        """
        @param request: SetFingerPrintTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetFingerPrintTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.encrypted_finger_print_template):
            query['EncryptedFingerPrintTemplate'] = request.encrypted_finger_print_template
        if not UtilClient.is_unset(request.encrypted_key):
            query['EncryptedKey'] = request.encrypted_key
        if not UtilClient.is_unset(request.finger_print_template):
            query['FingerPrintTemplate'] = request.finger_print_template
        if not UtilClient.is_unset(request.login_token):
            query['LoginToken'] = request.login_token
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetFingerPrintTemplate',
            version='2020-10-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20201002_models.SetFingerPrintTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_finger_print_template(
        self,
        request: ecd_20201002_models.SetFingerPrintTemplateRequest,
    ) -> ecd_20201002_models.SetFingerPrintTemplateResponse:
        """
        @param request: SetFingerPrintTemplateRequest
        @return: SetFingerPrintTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_finger_print_template_with_options(request, runtime)

    async def set_finger_print_template_async(
        self,
        request: ecd_20201002_models.SetFingerPrintTemplateRequest,
    ) -> ecd_20201002_models.SetFingerPrintTemplateResponse:
        """
        @param request: SetFingerPrintTemplateRequest
        @return: SetFingerPrintTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_finger_print_template_with_options_async(request, runtime)

    def set_finger_print_template_description_with_options(
        self,
        request: ecd_20201002_models.SetFingerPrintTemplateDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20201002_models.SetFingerPrintTemplateDescriptionResponse:
        """
        @param request: SetFingerPrintTemplateDescriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetFingerPrintTemplateDescriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.index):
            query['Index'] = request.index
        if not UtilClient.is_unset(request.login_token):
            query['LoginToken'] = request.login_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetFingerPrintTemplateDescription',
            version='2020-10-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20201002_models.SetFingerPrintTemplateDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_finger_print_template_description_with_options_async(
        self,
        request: ecd_20201002_models.SetFingerPrintTemplateDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20201002_models.SetFingerPrintTemplateDescriptionResponse:
        """
        @param request: SetFingerPrintTemplateDescriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetFingerPrintTemplateDescriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.index):
            query['Index'] = request.index
        if not UtilClient.is_unset(request.login_token):
            query['LoginToken'] = request.login_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetFingerPrintTemplateDescription',
            version='2020-10-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20201002_models.SetFingerPrintTemplateDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_finger_print_template_description(
        self,
        request: ecd_20201002_models.SetFingerPrintTemplateDescriptionRequest,
    ) -> ecd_20201002_models.SetFingerPrintTemplateDescriptionResponse:
        """
        @param request: SetFingerPrintTemplateDescriptionRequest
        @return: SetFingerPrintTemplateDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_finger_print_template_description_with_options(request, runtime)

    async def set_finger_print_template_description_async(
        self,
        request: ecd_20201002_models.SetFingerPrintTemplateDescriptionRequest,
    ) -> ecd_20201002_models.SetFingerPrintTemplateDescriptionResponse:
        """
        @param request: SetFingerPrintTemplateDescriptionRequest
        @return: SetFingerPrintTemplateDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_finger_print_template_description_with_options_async(request, runtime)

    def start_desktops_with_options(
        self,
        request: ecd_20201002_models.StartDesktopsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20201002_models.StartDesktopsResponse:
        """
        @summary Start cloud computers.
        
        @description The cloud computers that you want to start must be in the Stopped state. After you call this operation, the cloud computers enter the Running state.
        
        @param request: StartDesktopsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartDesktopsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.client_os):
            query['ClientOS'] = request.client_os
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.client_version):
            query['ClientVersion'] = request.client_version
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.login_token):
            query['LoginToken'] = request.login_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartDesktops',
            version='2020-10-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20201002_models.StartDesktopsResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_desktops_with_options_async(
        self,
        request: ecd_20201002_models.StartDesktopsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20201002_models.StartDesktopsResponse:
        """
        @summary Start cloud computers.
        
        @description The cloud computers that you want to start must be in the Stopped state. After you call this operation, the cloud computers enter the Running state.
        
        @param request: StartDesktopsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartDesktopsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.client_os):
            query['ClientOS'] = request.client_os
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.client_version):
            query['ClientVersion'] = request.client_version
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.login_token):
            query['LoginToken'] = request.login_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartDesktops',
            version='2020-10-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20201002_models.StartDesktopsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_desktops(
        self,
        request: ecd_20201002_models.StartDesktopsRequest,
    ) -> ecd_20201002_models.StartDesktopsResponse:
        """
        @summary Start cloud computers.
        
        @description The cloud computers that you want to start must be in the Stopped state. After you call this operation, the cloud computers enter the Running state.
        
        @param request: StartDesktopsRequest
        @return: StartDesktopsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_desktops_with_options(request, runtime)

    async def start_desktops_async(
        self,
        request: ecd_20201002_models.StartDesktopsRequest,
    ) -> ecd_20201002_models.StartDesktopsResponse:
        """
        @summary Start cloud computers.
        
        @description The cloud computers that you want to start must be in the Stopped state. After you call this operation, the cloud computers enter the Running state.
        
        @param request: StartDesktopsRequest
        @return: StartDesktopsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_desktops_with_options_async(request, runtime)

    def start_record_content_with_options(
        self,
        request: ecd_20201002_models.StartRecordContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20201002_models.StartRecordContentResponse:
        """
        @param request: StartRecordContentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartRecordContentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.client_os):
            query['ClientOS'] = request.client_os
        if not UtilClient.is_unset(request.client_version):
            query['ClientVersion'] = request.client_version
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.file_path):
            query['FilePath'] = request.file_path
        if not UtilClient.is_unset(request.login_token):
            query['LoginToken'] = request.login_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartRecordContent',
            version='2020-10-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20201002_models.StartRecordContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_record_content_with_options_async(
        self,
        request: ecd_20201002_models.StartRecordContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20201002_models.StartRecordContentResponse:
        """
        @param request: StartRecordContentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartRecordContentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.client_os):
            query['ClientOS'] = request.client_os
        if not UtilClient.is_unset(request.client_version):
            query['ClientVersion'] = request.client_version
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.file_path):
            query['FilePath'] = request.file_path
        if not UtilClient.is_unset(request.login_token):
            query['LoginToken'] = request.login_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartRecordContent',
            version='2020-10-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20201002_models.StartRecordContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_record_content(
        self,
        request: ecd_20201002_models.StartRecordContentRequest,
    ) -> ecd_20201002_models.StartRecordContentResponse:
        """
        @param request: StartRecordContentRequest
        @return: StartRecordContentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_record_content_with_options(request, runtime)

    async def start_record_content_async(
        self,
        request: ecd_20201002_models.StartRecordContentRequest,
    ) -> ecd_20201002_models.StartRecordContentResponse:
        """
        @param request: StartRecordContentRequest
        @return: StartRecordContentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_record_content_with_options_async(request, runtime)

    def stop_desktops_with_options(
        self,
        request: ecd_20201002_models.StopDesktopsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20201002_models.StopDesktopsResponse:
        """
        @summary Stops cloud computers.
        
        @description The cloud computers that you want to stop must be in the Running state. After you call this operation, the cloud computers enter the Stopped state.
        
        @param request: StopDesktopsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopDesktopsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.client_os):
            query['ClientOS'] = request.client_os
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.client_version):
            query['ClientVersion'] = request.client_version
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.login_token):
            query['LoginToken'] = request.login_token
        if not UtilClient.is_unset(request.os_update):
            query['OsUpdate'] = request.os_update
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.session_token):
            query['SessionToken'] = request.session_token
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopDesktops',
            version='2020-10-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20201002_models.StopDesktopsResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_desktops_with_options_async(
        self,
        request: ecd_20201002_models.StopDesktopsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20201002_models.StopDesktopsResponse:
        """
        @summary Stops cloud computers.
        
        @description The cloud computers that you want to stop must be in the Running state. After you call this operation, the cloud computers enter the Stopped state.
        
        @param request: StopDesktopsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopDesktopsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.client_os):
            query['ClientOS'] = request.client_os
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.client_version):
            query['ClientVersion'] = request.client_version
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.login_token):
            query['LoginToken'] = request.login_token
        if not UtilClient.is_unset(request.os_update):
            query['OsUpdate'] = request.os_update
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.session_token):
            query['SessionToken'] = request.session_token
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopDesktops',
            version='2020-10-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20201002_models.StopDesktopsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_desktops(
        self,
        request: ecd_20201002_models.StopDesktopsRequest,
    ) -> ecd_20201002_models.StopDesktopsResponse:
        """
        @summary Stops cloud computers.
        
        @description The cloud computers that you want to stop must be in the Running state. After you call this operation, the cloud computers enter the Stopped state.
        
        @param request: StopDesktopsRequest
        @return: StopDesktopsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_desktops_with_options(request, runtime)

    async def stop_desktops_async(
        self,
        request: ecd_20201002_models.StopDesktopsRequest,
    ) -> ecd_20201002_models.StopDesktopsResponse:
        """
        @summary Stops cloud computers.
        
        @description The cloud computers that you want to stop must be in the Running state. After you call this operation, the cloud computers enter the Stopped state.
        
        @param request: StopDesktopsRequest
        @return: StopDesktopsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_desktops_with_options_async(request, runtime)

    def stop_record_content_with_options(
        self,
        request: ecd_20201002_models.StopRecordContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20201002_models.StopRecordContentResponse:
        """
        @param request: StopRecordContentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopRecordContentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.client_os):
            query['ClientOS'] = request.client_os
        if not UtilClient.is_unset(request.client_version):
            query['ClientVersion'] = request.client_version
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.login_token):
            query['LoginToken'] = request.login_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopRecordContent',
            version='2020-10-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20201002_models.StopRecordContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_record_content_with_options_async(
        self,
        request: ecd_20201002_models.StopRecordContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20201002_models.StopRecordContentResponse:
        """
        @param request: StopRecordContentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopRecordContentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.client_os):
            query['ClientOS'] = request.client_os
        if not UtilClient.is_unset(request.client_version):
            query['ClientVersion'] = request.client_version
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.login_token):
            query['LoginToken'] = request.login_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopRecordContent',
            version='2020-10-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20201002_models.StopRecordContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_record_content(
        self,
        request: ecd_20201002_models.StopRecordContentRequest,
    ) -> ecd_20201002_models.StopRecordContentResponse:
        """
        @param request: StopRecordContentRequest
        @return: StopRecordContentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_record_content_with_options(request, runtime)

    async def stop_record_content_async(
        self,
        request: ecd_20201002_models.StopRecordContentRequest,
    ) -> ecd_20201002_models.StopRecordContentResponse:
        """
        @param request: StopRecordContentRequest
        @return: StopRecordContentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_record_content_with_options_async(request, runtime)

    def unbind_user_desktop_with_options(
        self,
        request: ecd_20201002_models.UnbindUserDesktopRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20201002_models.UnbindUserDesktopResponse:
        """
        @summary Unbinds end users from cloud computers.
        
        @param request: UnbindUserDesktopRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnbindUserDesktopResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.client_type):
            query['ClientType'] = request.client_type
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        if not UtilClient.is_unset(request.login_token):
            query['LoginToken'] = request.login_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.user_desktop_id):
            query['UserDesktopId'] = request.user_desktop_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindUserDesktop',
            version='2020-10-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20201002_models.UnbindUserDesktopResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_user_desktop_with_options_async(
        self,
        request: ecd_20201002_models.UnbindUserDesktopRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20201002_models.UnbindUserDesktopResponse:
        """
        @summary Unbinds end users from cloud computers.
        
        @param request: UnbindUserDesktopRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnbindUserDesktopResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.client_type):
            query['ClientType'] = request.client_type
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        if not UtilClient.is_unset(request.login_token):
            query['LoginToken'] = request.login_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.user_desktop_id):
            query['UserDesktopId'] = request.user_desktop_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindUserDesktop',
            version='2020-10-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20201002_models.UnbindUserDesktopResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_user_desktop(
        self,
        request: ecd_20201002_models.UnbindUserDesktopRequest,
    ) -> ecd_20201002_models.UnbindUserDesktopResponse:
        """
        @summary Unbinds end users from cloud computers.
        
        @param request: UnbindUserDesktopRequest
        @return: UnbindUserDesktopResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.unbind_user_desktop_with_options(request, runtime)

    async def unbind_user_desktop_async(
        self,
        request: ecd_20201002_models.UnbindUserDesktopRequest,
    ) -> ecd_20201002_models.UnbindUserDesktopResponse:
        """
        @summary Unbinds end users from cloud computers.
        
        @param request: UnbindUserDesktopRequest
        @return: UnbindUserDesktopResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.unbind_user_desktop_with_options_async(request, runtime)

    def verify_credential_with_options(
        self,
        request: ecd_20201002_models.VerifyCredentialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20201002_models.VerifyCredentialResponse:
        """
        @param request: VerifyCredentialRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: VerifyCredentialResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.credential):
            query['Credential'] = request.credential
        if not UtilClient.is_unset(request.credential_type):
            query['CredentialType'] = request.credential_type
        if not UtilClient.is_unset(request.encrypted_key):
            query['EncryptedKey'] = request.encrypted_key
        if not UtilClient.is_unset(request.login_token):
            query['LoginToken'] = request.login_token
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyCredential',
            version='2020-10-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20201002_models.VerifyCredentialResponse(),
            self.call_api(params, req, runtime)
        )

    async def verify_credential_with_options_async(
        self,
        request: ecd_20201002_models.VerifyCredentialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20201002_models.VerifyCredentialResponse:
        """
        @param request: VerifyCredentialRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: VerifyCredentialResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.credential):
            query['Credential'] = request.credential
        if not UtilClient.is_unset(request.credential_type):
            query['CredentialType'] = request.credential_type
        if not UtilClient.is_unset(request.encrypted_key):
            query['EncryptedKey'] = request.encrypted_key
        if not UtilClient.is_unset(request.login_token):
            query['LoginToken'] = request.login_token
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyCredential',
            version='2020-10-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20201002_models.VerifyCredentialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def verify_credential(
        self,
        request: ecd_20201002_models.VerifyCredentialRequest,
    ) -> ecd_20201002_models.VerifyCredentialResponse:
        """
        @param request: VerifyCredentialRequest
        @return: VerifyCredentialResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.verify_credential_with_options(request, runtime)

    async def verify_credential_async(
        self,
        request: ecd_20201002_models.VerifyCredentialRequest,
    ) -> ecd_20201002_models.VerifyCredentialResponse:
        """
        @param request: VerifyCredentialRequest
        @return: VerifyCredentialResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.verify_credential_with_options_async(request, runtime)
