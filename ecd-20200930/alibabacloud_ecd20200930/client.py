# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ecd20200930 import models as ecd_20200930_models
from alibabacloud_tea_util import models as util_models


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(
        self, 
        config: open_api_models.Config,
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_user_to_desktop_group_with_options(
        self,
        request: ecd_20200930_models.AddUserToDesktopGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.AddUserToDesktopGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.AddUserToDesktopGroupResponse(),
            self.do_rpcrequest('AddUserToDesktopGroup', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_user_to_desktop_group_with_options_async(
        self,
        request: ecd_20200930_models.AddUserToDesktopGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.AddUserToDesktopGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.AddUserToDesktopGroupResponse(),
            await self.do_rpcrequest_async('AddUserToDesktopGroup', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_user_to_desktop_group(
        self,
        request: ecd_20200930_models.AddUserToDesktopGroupRequest,
    ) -> ecd_20200930_models.AddUserToDesktopGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_user_to_desktop_group_with_options(request, runtime)

    async def add_user_to_desktop_group_async(
        self,
        request: ecd_20200930_models.AddUserToDesktopGroupRequest,
    ) -> ecd_20200930_models.AddUserToDesktopGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_user_to_desktop_group_with_options_async(request, runtime)

    def add_user_to_security_center_white_list_with_options(
        self,
        request: ecd_20200930_models.AddUserToSecurityCenterWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.AddUserToSecurityCenterWhiteListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.AddUserToSecurityCenterWhiteListResponse(),
            self.do_rpcrequest('AddUserToSecurityCenterWhiteList', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_user_to_security_center_white_list_with_options_async(
        self,
        request: ecd_20200930_models.AddUserToSecurityCenterWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.AddUserToSecurityCenterWhiteListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.AddUserToSecurityCenterWhiteListResponse(),
            await self.do_rpcrequest_async('AddUserToSecurityCenterWhiteList', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_user_to_security_center_white_list(
        self,
        request: ecd_20200930_models.AddUserToSecurityCenterWhiteListRequest,
    ) -> ecd_20200930_models.AddUserToSecurityCenterWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_user_to_security_center_white_list_with_options(request, runtime)

    async def add_user_to_security_center_white_list_async(
        self,
        request: ecd_20200930_models.AddUserToSecurityCenterWhiteListRequest,
    ) -> ecd_20200930_models.AddUserToSecurityCenterWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_user_to_security_center_white_list_with_options_async(request, runtime)

    def attach_cen_with_options(
        self,
        request: ecd_20200930_models.AttachCenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.AttachCenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.AttachCenResponse(),
            self.do_rpcrequest('AttachCen', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def attach_cen_with_options_async(
        self,
        request: ecd_20200930_models.AttachCenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.AttachCenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.AttachCenResponse(),
            await self.do_rpcrequest_async('AttachCen', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def attach_cen(
        self,
        request: ecd_20200930_models.AttachCenRequest,
    ) -> ecd_20200930_models.AttachCenResponse:
        runtime = util_models.RuntimeOptions()
        return self.attach_cen_with_options(request, runtime)

    async def attach_cen_async(
        self,
        request: ecd_20200930_models.AttachCenRequest,
    ) -> ecd_20200930_models.AttachCenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.attach_cen_with_options_async(request, runtime)

    def check_user_in_security_center_white_list_with_options(
        self,
        request: ecd_20200930_models.CheckUserInSecurityCenterWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CheckUserInSecurityCenterWhiteListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.CheckUserInSecurityCenterWhiteListResponse(),
            self.do_rpcrequest('CheckUserInSecurityCenterWhiteList', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def check_user_in_security_center_white_list_with_options_async(
        self,
        request: ecd_20200930_models.CheckUserInSecurityCenterWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CheckUserInSecurityCenterWhiteListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.CheckUserInSecurityCenterWhiteListResponse(),
            await self.do_rpcrequest_async('CheckUserInSecurityCenterWhiteList', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_user_in_security_center_white_list(
        self,
        request: ecd_20200930_models.CheckUserInSecurityCenterWhiteListRequest,
    ) -> ecd_20200930_models.CheckUserInSecurityCenterWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_user_in_security_center_white_list_with_options(request, runtime)

    async def check_user_in_security_center_white_list_async(
        self,
        request: ecd_20200930_models.CheckUserInSecurityCenterWhiteListRequest,
    ) -> ecd_20200930_models.CheckUserInSecurityCenterWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_user_in_security_center_white_list_with_options_async(request, runtime)

    def clone_policy_group_with_options(
        self,
        request: ecd_20200930_models.ClonePolicyGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ClonePolicyGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ClonePolicyGroupResponse(),
            self.do_rpcrequest('ClonePolicyGroup', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def clone_policy_group_with_options_async(
        self,
        request: ecd_20200930_models.ClonePolicyGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ClonePolicyGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ClonePolicyGroupResponse(),
            await self.do_rpcrequest_async('ClonePolicyGroup', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def clone_policy_group(
        self,
        request: ecd_20200930_models.ClonePolicyGroupRequest,
    ) -> ecd_20200930_models.ClonePolicyGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.clone_policy_group_with_options(request, runtime)

    async def clone_policy_group_async(
        self,
        request: ecd_20200930_models.ClonePolicyGroupRequest,
    ) -> ecd_20200930_models.ClonePolicyGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.clone_policy_group_with_options_async(request, runtime)

    def create_adconnector_directory_with_options(
        self,
        request: ecd_20200930_models.CreateADConnectorDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CreateADConnectorDirectoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateADConnectorDirectoryResponse(),
            self.do_rpcrequest('CreateADConnectorDirectory', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_adconnector_directory_with_options_async(
        self,
        request: ecd_20200930_models.CreateADConnectorDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CreateADConnectorDirectoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateADConnectorDirectoryResponse(),
            await self.do_rpcrequest_async('CreateADConnectorDirectory', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_adconnector_directory(
        self,
        request: ecd_20200930_models.CreateADConnectorDirectoryRequest,
    ) -> ecd_20200930_models.CreateADConnectorDirectoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_adconnector_directory_with_options(request, runtime)

    async def create_adconnector_directory_async(
        self,
        request: ecd_20200930_models.CreateADConnectorDirectoryRequest,
    ) -> ecd_20200930_models.CreateADConnectorDirectoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_adconnector_directory_with_options_async(request, runtime)

    def create_adconnector_office_site_with_options(
        self,
        request: ecd_20200930_models.CreateADConnectorOfficeSiteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CreateADConnectorOfficeSiteResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateADConnectorOfficeSiteResponse(),
            self.do_rpcrequest('CreateADConnectorOfficeSite', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_adconnector_office_site_with_options_async(
        self,
        request: ecd_20200930_models.CreateADConnectorOfficeSiteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CreateADConnectorOfficeSiteResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateADConnectorOfficeSiteResponse(),
            await self.do_rpcrequest_async('CreateADConnectorOfficeSite', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_adconnector_office_site(
        self,
        request: ecd_20200930_models.CreateADConnectorOfficeSiteRequest,
    ) -> ecd_20200930_models.CreateADConnectorOfficeSiteResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_adconnector_office_site_with_options(request, runtime)

    async def create_adconnector_office_site_async(
        self,
        request: ecd_20200930_models.CreateADConnectorOfficeSiteRequest,
    ) -> ecd_20200930_models.CreateADConnectorOfficeSiteResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_adconnector_office_site_with_options_async(request, runtime)

    def create_bundle_with_options(
        self,
        request: ecd_20200930_models.CreateBundleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CreateBundleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateBundleResponse(),
            self.do_rpcrequest('CreateBundle', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_bundle_with_options_async(
        self,
        request: ecd_20200930_models.CreateBundleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CreateBundleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateBundleResponse(),
            await self.do_rpcrequest_async('CreateBundle', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_bundle(
        self,
        request: ecd_20200930_models.CreateBundleRequest,
    ) -> ecd_20200930_models.CreateBundleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_bundle_with_options(request, runtime)

    async def create_bundle_async(
        self,
        request: ecd_20200930_models.CreateBundleRequest,
    ) -> ecd_20200930_models.CreateBundleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_bundle_with_options_async(request, runtime)

    def create_desktop_group_with_options(
        self,
        request: ecd_20200930_models.CreateDesktopGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CreateDesktopGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateDesktopGroupResponse(),
            self.do_rpcrequest('CreateDesktopGroup', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_desktop_group_with_options_async(
        self,
        request: ecd_20200930_models.CreateDesktopGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CreateDesktopGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateDesktopGroupResponse(),
            await self.do_rpcrequest_async('CreateDesktopGroup', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_desktop_group(
        self,
        request: ecd_20200930_models.CreateDesktopGroupRequest,
    ) -> ecd_20200930_models.CreateDesktopGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_desktop_group_with_options(request, runtime)

    async def create_desktop_group_async(
        self,
        request: ecd_20200930_models.CreateDesktopGroupRequest,
    ) -> ecd_20200930_models.CreateDesktopGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_desktop_group_with_options_async(request, runtime)

    def create_desktops_with_options(
        self,
        request: ecd_20200930_models.CreateDesktopsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CreateDesktopsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateDesktopsResponse(),
            self.do_rpcrequest('CreateDesktops', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_desktops_with_options_async(
        self,
        request: ecd_20200930_models.CreateDesktopsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CreateDesktopsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateDesktopsResponse(),
            await self.do_rpcrequest_async('CreateDesktops', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_desktops(
        self,
        request: ecd_20200930_models.CreateDesktopsRequest,
    ) -> ecd_20200930_models.CreateDesktopsResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_desktops_with_options(request, runtime)

    async def create_desktops_async(
        self,
        request: ecd_20200930_models.CreateDesktopsRequest,
    ) -> ecd_20200930_models.CreateDesktopsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_desktops_with_options_async(request, runtime)

    def create_desktops_lite_with_options(
        self,
        request: ecd_20200930_models.CreateDesktopsLiteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CreateDesktopsLiteResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateDesktopsLiteResponse(),
            self.do_rpcrequest('CreateDesktopsLite', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_desktops_lite_with_options_async(
        self,
        request: ecd_20200930_models.CreateDesktopsLiteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CreateDesktopsLiteResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateDesktopsLiteResponse(),
            await self.do_rpcrequest_async('CreateDesktopsLite', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_desktops_lite(
        self,
        request: ecd_20200930_models.CreateDesktopsLiteRequest,
    ) -> ecd_20200930_models.CreateDesktopsLiteResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_desktops_lite_with_options(request, runtime)

    async def create_desktops_lite_async(
        self,
        request: ecd_20200930_models.CreateDesktopsLiteRequest,
    ) -> ecd_20200930_models.CreateDesktopsLiteResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_desktops_lite_with_options_async(request, runtime)

    def create_image_with_options(
        self,
        request: ecd_20200930_models.CreateImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CreateImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateImageResponse(),
            self.do_rpcrequest('CreateImage', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_image_with_options_async(
        self,
        request: ecd_20200930_models.CreateImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CreateImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateImageResponse(),
            await self.do_rpcrequest_async('CreateImage', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_image(
        self,
        request: ecd_20200930_models.CreateImageRequest,
    ) -> ecd_20200930_models.CreateImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_image_with_options(request, runtime)

    async def create_image_async(
        self,
        request: ecd_20200930_models.CreateImageRequest,
    ) -> ecd_20200930_models.CreateImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_image_with_options_async(request, runtime)

    def create_nasfile_system_with_options(
        self,
        request: ecd_20200930_models.CreateNASFileSystemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CreateNASFileSystemResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateNASFileSystemResponse(),
            self.do_rpcrequest('CreateNASFileSystem', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_nasfile_system_with_options_async(
        self,
        request: ecd_20200930_models.CreateNASFileSystemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CreateNASFileSystemResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateNASFileSystemResponse(),
            await self.do_rpcrequest_async('CreateNASFileSystem', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_nasfile_system(
        self,
        request: ecd_20200930_models.CreateNASFileSystemRequest,
    ) -> ecd_20200930_models.CreateNASFileSystemResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_nasfile_system_with_options(request, runtime)

    async def create_nasfile_system_async(
        self,
        request: ecd_20200930_models.CreateNASFileSystemRequest,
    ) -> ecd_20200930_models.CreateNASFileSystemResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_nasfile_system_with_options_async(request, runtime)

    def create_network_package_with_options(
        self,
        request: ecd_20200930_models.CreateNetworkPackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CreateNetworkPackageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateNetworkPackageResponse(),
            self.do_rpcrequest('CreateNetworkPackage', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_network_package_with_options_async(
        self,
        request: ecd_20200930_models.CreateNetworkPackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CreateNetworkPackageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateNetworkPackageResponse(),
            await self.do_rpcrequest_async('CreateNetworkPackage', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_network_package(
        self,
        request: ecd_20200930_models.CreateNetworkPackageRequest,
    ) -> ecd_20200930_models.CreateNetworkPackageResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_network_package_with_options(request, runtime)

    async def create_network_package_async(
        self,
        request: ecd_20200930_models.CreateNetworkPackageRequest,
    ) -> ecd_20200930_models.CreateNetworkPackageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_network_package_with_options_async(request, runtime)

    def create_policy_group_with_options(
        self,
        request: ecd_20200930_models.CreatePolicyGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CreatePolicyGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreatePolicyGroupResponse(),
            self.do_rpcrequest('CreatePolicyGroup', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_policy_group_with_options_async(
        self,
        request: ecd_20200930_models.CreatePolicyGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CreatePolicyGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreatePolicyGroupResponse(),
            await self.do_rpcrequest_async('CreatePolicyGroup', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_policy_group(
        self,
        request: ecd_20200930_models.CreatePolicyGroupRequest,
    ) -> ecd_20200930_models.CreatePolicyGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_policy_group_with_options(request, runtime)

    async def create_policy_group_async(
        self,
        request: ecd_20200930_models.CreatePolicyGroupRequest,
    ) -> ecd_20200930_models.CreatePolicyGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_policy_group_with_options_async(request, runtime)

    def create_ramdirectory_with_options(
        self,
        request: ecd_20200930_models.CreateRAMDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CreateRAMDirectoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateRAMDirectoryResponse(),
            self.do_rpcrequest('CreateRAMDirectory', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_ramdirectory_with_options_async(
        self,
        request: ecd_20200930_models.CreateRAMDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CreateRAMDirectoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateRAMDirectoryResponse(),
            await self.do_rpcrequest_async('CreateRAMDirectory', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_ramdirectory(
        self,
        request: ecd_20200930_models.CreateRAMDirectoryRequest,
    ) -> ecd_20200930_models.CreateRAMDirectoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_ramdirectory_with_options(request, runtime)

    async def create_ramdirectory_async(
        self,
        request: ecd_20200930_models.CreateRAMDirectoryRequest,
    ) -> ecd_20200930_models.CreateRAMDirectoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_ramdirectory_with_options_async(request, runtime)

    def create_scale_strategy_with_options(
        self,
        request: ecd_20200930_models.CreateScaleStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CreateScaleStrategyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateScaleStrategyResponse(),
            self.do_rpcrequest('CreateScaleStrategy', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_scale_strategy_with_options_async(
        self,
        request: ecd_20200930_models.CreateScaleStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CreateScaleStrategyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateScaleStrategyResponse(),
            await self.do_rpcrequest_async('CreateScaleStrategy', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_scale_strategy(
        self,
        request: ecd_20200930_models.CreateScaleStrategyRequest,
    ) -> ecd_20200930_models.CreateScaleStrategyResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_scale_strategy_with_options(request, runtime)

    async def create_scale_strategy_async(
        self,
        request: ecd_20200930_models.CreateScaleStrategyRequest,
    ) -> ecd_20200930_models.CreateScaleStrategyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_scale_strategy_with_options_async(request, runtime)

    def create_service_linked_role_with_options(
        self,
        request: ecd_20200930_models.CreateServiceLinkedRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CreateServiceLinkedRoleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateServiceLinkedRoleResponse(),
            self.do_rpcrequest('CreateServiceLinkedRole', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_service_linked_role_with_options_async(
        self,
        request: ecd_20200930_models.CreateServiceLinkedRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CreateServiceLinkedRoleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateServiceLinkedRoleResponse(),
            await self.do_rpcrequest_async('CreateServiceLinkedRole', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_service_linked_role(
        self,
        request: ecd_20200930_models.CreateServiceLinkedRoleRequest,
    ) -> ecd_20200930_models.CreateServiceLinkedRoleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_service_linked_role_with_options(request, runtime)

    async def create_service_linked_role_async(
        self,
        request: ecd_20200930_models.CreateServiceLinkedRoleRequest,
    ) -> ecd_20200930_models.CreateServiceLinkedRoleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_service_linked_role_with_options_async(request, runtime)

    def create_simple_office_site_with_options(
        self,
        request: ecd_20200930_models.CreateSimpleOfficeSiteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CreateSimpleOfficeSiteResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateSimpleOfficeSiteResponse(),
            self.do_rpcrequest('CreateSimpleOfficeSite', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_simple_office_site_with_options_async(
        self,
        request: ecd_20200930_models.CreateSimpleOfficeSiteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CreateSimpleOfficeSiteResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateSimpleOfficeSiteResponse(),
            await self.do_rpcrequest_async('CreateSimpleOfficeSite', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_simple_office_site(
        self,
        request: ecd_20200930_models.CreateSimpleOfficeSiteRequest,
    ) -> ecd_20200930_models.CreateSimpleOfficeSiteResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_simple_office_site_with_options(request, runtime)

    async def create_simple_office_site_async(
        self,
        request: ecd_20200930_models.CreateSimpleOfficeSiteRequest,
    ) -> ecd_20200930_models.CreateSimpleOfficeSiteResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_simple_office_site_with_options_async(request, runtime)

    def create_snapshot_with_options(
        self,
        request: ecd_20200930_models.CreateSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CreateSnapshotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateSnapshotResponse(),
            self.do_rpcrequest('CreateSnapshot', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_snapshot_with_options_async(
        self,
        request: ecd_20200930_models.CreateSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CreateSnapshotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateSnapshotResponse(),
            await self.do_rpcrequest_async('CreateSnapshot', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_snapshot(
        self,
        request: ecd_20200930_models.CreateSnapshotRequest,
    ) -> ecd_20200930_models.CreateSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_snapshot_with_options(request, runtime)

    async def create_snapshot_async(
        self,
        request: ecd_20200930_models.CreateSnapshotRequest,
    ) -> ecd_20200930_models.CreateSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_snapshot_with_options_async(request, runtime)

    def delete_bundles_with_options(
        self,
        request: ecd_20200930_models.DeleteBundlesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DeleteBundlesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DeleteBundlesResponse(),
            self.do_rpcrequest('DeleteBundles', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_bundles_with_options_async(
        self,
        request: ecd_20200930_models.DeleteBundlesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DeleteBundlesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DeleteBundlesResponse(),
            await self.do_rpcrequest_async('DeleteBundles', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_bundles(
        self,
        request: ecd_20200930_models.DeleteBundlesRequest,
    ) -> ecd_20200930_models.DeleteBundlesResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_bundles_with_options(request, runtime)

    async def delete_bundles_async(
        self,
        request: ecd_20200930_models.DeleteBundlesRequest,
    ) -> ecd_20200930_models.DeleteBundlesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_bundles_with_options_async(request, runtime)

    def delete_desktop_group_with_options(
        self,
        request: ecd_20200930_models.DeleteDesktopGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DeleteDesktopGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DeleteDesktopGroupResponse(),
            self.do_rpcrequest('DeleteDesktopGroup', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_desktop_group_with_options_async(
        self,
        request: ecd_20200930_models.DeleteDesktopGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DeleteDesktopGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DeleteDesktopGroupResponse(),
            await self.do_rpcrequest_async('DeleteDesktopGroup', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_desktop_group(
        self,
        request: ecd_20200930_models.DeleteDesktopGroupRequest,
    ) -> ecd_20200930_models.DeleteDesktopGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_desktop_group_with_options(request, runtime)

    async def delete_desktop_group_async(
        self,
        request: ecd_20200930_models.DeleteDesktopGroupRequest,
    ) -> ecd_20200930_models.DeleteDesktopGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_desktop_group_with_options_async(request, runtime)

    def delete_desktops_with_options(
        self,
        request: ecd_20200930_models.DeleteDesktopsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DeleteDesktopsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DeleteDesktopsResponse(),
            self.do_rpcrequest('DeleteDesktops', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_desktops_with_options_async(
        self,
        request: ecd_20200930_models.DeleteDesktopsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DeleteDesktopsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DeleteDesktopsResponse(),
            await self.do_rpcrequest_async('DeleteDesktops', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_desktops(
        self,
        request: ecd_20200930_models.DeleteDesktopsRequest,
    ) -> ecd_20200930_models.DeleteDesktopsResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_desktops_with_options(request, runtime)

    async def delete_desktops_async(
        self,
        request: ecd_20200930_models.DeleteDesktopsRequest,
    ) -> ecd_20200930_models.DeleteDesktopsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_desktops_with_options_async(request, runtime)

    def delete_directories_with_options(
        self,
        request: ecd_20200930_models.DeleteDirectoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DeleteDirectoriesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DeleteDirectoriesResponse(),
            self.do_rpcrequest('DeleteDirectories', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_directories_with_options_async(
        self,
        request: ecd_20200930_models.DeleteDirectoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DeleteDirectoriesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DeleteDirectoriesResponse(),
            await self.do_rpcrequest_async('DeleteDirectories', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_directories(
        self,
        request: ecd_20200930_models.DeleteDirectoriesRequest,
    ) -> ecd_20200930_models.DeleteDirectoriesResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_directories_with_options(request, runtime)

    async def delete_directories_async(
        self,
        request: ecd_20200930_models.DeleteDirectoriesRequest,
    ) -> ecd_20200930_models.DeleteDirectoriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_directories_with_options_async(request, runtime)

    def delete_images_with_options(
        self,
        request: ecd_20200930_models.DeleteImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DeleteImagesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DeleteImagesResponse(),
            self.do_rpcrequest('DeleteImages', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_images_with_options_async(
        self,
        request: ecd_20200930_models.DeleteImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DeleteImagesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DeleteImagesResponse(),
            await self.do_rpcrequest_async('DeleteImages', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_images(
        self,
        request: ecd_20200930_models.DeleteImagesRequest,
    ) -> ecd_20200930_models.DeleteImagesResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_images_with_options(request, runtime)

    async def delete_images_async(
        self,
        request: ecd_20200930_models.DeleteImagesRequest,
    ) -> ecd_20200930_models.DeleteImagesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_images_with_options_async(request, runtime)

    def delete_nasfile_systems_with_options(
        self,
        request: ecd_20200930_models.DeleteNASFileSystemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DeleteNASFileSystemsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DeleteNASFileSystemsResponse(),
            self.do_rpcrequest('DeleteNASFileSystems', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_nasfile_systems_with_options_async(
        self,
        request: ecd_20200930_models.DeleteNASFileSystemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DeleteNASFileSystemsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DeleteNASFileSystemsResponse(),
            await self.do_rpcrequest_async('DeleteNASFileSystems', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_nasfile_systems(
        self,
        request: ecd_20200930_models.DeleteNASFileSystemsRequest,
    ) -> ecd_20200930_models.DeleteNASFileSystemsResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_nasfile_systems_with_options(request, runtime)

    async def delete_nasfile_systems_async(
        self,
        request: ecd_20200930_models.DeleteNASFileSystemsRequest,
    ) -> ecd_20200930_models.DeleteNASFileSystemsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_nasfile_systems_with_options_async(request, runtime)

    def delete_network_packages_with_options(
        self,
        request: ecd_20200930_models.DeleteNetworkPackagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DeleteNetworkPackagesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DeleteNetworkPackagesResponse(),
            self.do_rpcrequest('DeleteNetworkPackages', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_network_packages_with_options_async(
        self,
        request: ecd_20200930_models.DeleteNetworkPackagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DeleteNetworkPackagesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DeleteNetworkPackagesResponse(),
            await self.do_rpcrequest_async('DeleteNetworkPackages', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_network_packages(
        self,
        request: ecd_20200930_models.DeleteNetworkPackagesRequest,
    ) -> ecd_20200930_models.DeleteNetworkPackagesResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_network_packages_with_options(request, runtime)

    async def delete_network_packages_async(
        self,
        request: ecd_20200930_models.DeleteNetworkPackagesRequest,
    ) -> ecd_20200930_models.DeleteNetworkPackagesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_network_packages_with_options_async(request, runtime)

    def delete_office_sites_with_options(
        self,
        request: ecd_20200930_models.DeleteOfficeSitesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DeleteOfficeSitesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DeleteOfficeSitesResponse(),
            self.do_rpcrequest('DeleteOfficeSites', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_office_sites_with_options_async(
        self,
        request: ecd_20200930_models.DeleteOfficeSitesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DeleteOfficeSitesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DeleteOfficeSitesResponse(),
            await self.do_rpcrequest_async('DeleteOfficeSites', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_office_sites(
        self,
        request: ecd_20200930_models.DeleteOfficeSitesRequest,
    ) -> ecd_20200930_models.DeleteOfficeSitesResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_office_sites_with_options(request, runtime)

    async def delete_office_sites_async(
        self,
        request: ecd_20200930_models.DeleteOfficeSitesRequest,
    ) -> ecd_20200930_models.DeleteOfficeSitesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_office_sites_with_options_async(request, runtime)

    def delete_policy_groups_with_options(
        self,
        request: ecd_20200930_models.DeletePolicyGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DeletePolicyGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DeletePolicyGroupsResponse(),
            self.do_rpcrequest('DeletePolicyGroups', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_policy_groups_with_options_async(
        self,
        request: ecd_20200930_models.DeletePolicyGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DeletePolicyGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DeletePolicyGroupsResponse(),
            await self.do_rpcrequest_async('DeletePolicyGroups', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_policy_groups(
        self,
        request: ecd_20200930_models.DeletePolicyGroupsRequest,
    ) -> ecd_20200930_models.DeletePolicyGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_policy_groups_with_options(request, runtime)

    async def delete_policy_groups_async(
        self,
        request: ecd_20200930_models.DeletePolicyGroupsRequest,
    ) -> ecd_20200930_models.DeletePolicyGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_policy_groups_with_options_async(request, runtime)

    def delete_scale_strategy_with_options(
        self,
        request: ecd_20200930_models.DeleteScaleStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DeleteScaleStrategyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DeleteScaleStrategyResponse(),
            self.do_rpcrequest('DeleteScaleStrategy', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_scale_strategy_with_options_async(
        self,
        request: ecd_20200930_models.DeleteScaleStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DeleteScaleStrategyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DeleteScaleStrategyResponse(),
            await self.do_rpcrequest_async('DeleteScaleStrategy', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_scale_strategy(
        self,
        request: ecd_20200930_models.DeleteScaleStrategyRequest,
    ) -> ecd_20200930_models.DeleteScaleStrategyResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_scale_strategy_with_options(request, runtime)

    async def delete_scale_strategy_async(
        self,
        request: ecd_20200930_models.DeleteScaleStrategyRequest,
    ) -> ecd_20200930_models.DeleteScaleStrategyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_scale_strategy_with_options_async(request, runtime)

    def delete_snapshot_with_options(
        self,
        request: ecd_20200930_models.DeleteSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DeleteSnapshotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DeleteSnapshotResponse(),
            self.do_rpcrequest('DeleteSnapshot', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_snapshot_with_options_async(
        self,
        request: ecd_20200930_models.DeleteSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DeleteSnapshotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DeleteSnapshotResponse(),
            await self.do_rpcrequest_async('DeleteSnapshot', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_snapshot(
        self,
        request: ecd_20200930_models.DeleteSnapshotRequest,
    ) -> ecd_20200930_models.DeleteSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_snapshot_with_options(request, runtime)

    async def delete_snapshot_async(
        self,
        request: ecd_20200930_models.DeleteSnapshotRequest,
    ) -> ecd_20200930_models.DeleteSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_snapshot_with_options_async(request, runtime)

    def delete_virtual_mfadevice_with_options(
        self,
        request: ecd_20200930_models.DeleteVirtualMFADeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DeleteVirtualMFADeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DeleteVirtualMFADeviceResponse(),
            self.do_rpcrequest('DeleteVirtualMFADevice', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_virtual_mfadevice_with_options_async(
        self,
        request: ecd_20200930_models.DeleteVirtualMFADeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DeleteVirtualMFADeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DeleteVirtualMFADeviceResponse(),
            await self.do_rpcrequest_async('DeleteVirtualMFADevice', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_virtual_mfadevice(
        self,
        request: ecd_20200930_models.DeleteVirtualMFADeviceRequest,
    ) -> ecd_20200930_models.DeleteVirtualMFADeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_virtual_mfadevice_with_options(request, runtime)

    async def delete_virtual_mfadevice_async(
        self,
        request: ecd_20200930_models.DeleteVirtualMFADeviceRequest,
    ) -> ecd_20200930_models.DeleteVirtualMFADeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_virtual_mfadevice_with_options_async(request, runtime)

    def describe_alarm_event_stack_info_with_options(
        self,
        request: ecd_20200930_models.DescribeAlarmEventStackInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeAlarmEventStackInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeAlarmEventStackInfoResponse(),
            self.do_rpcrequest('DescribeAlarmEventStackInfo', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_alarm_event_stack_info_with_options_async(
        self,
        request: ecd_20200930_models.DescribeAlarmEventStackInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeAlarmEventStackInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeAlarmEventStackInfoResponse(),
            await self.do_rpcrequest_async('DescribeAlarmEventStackInfo', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_alarm_event_stack_info(
        self,
        request: ecd_20200930_models.DescribeAlarmEventStackInfoRequest,
    ) -> ecd_20200930_models.DescribeAlarmEventStackInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_alarm_event_stack_info_with_options(request, runtime)

    async def describe_alarm_event_stack_info_async(
        self,
        request: ecd_20200930_models.DescribeAlarmEventStackInfoRequest,
    ) -> ecd_20200930_models.DescribeAlarmEventStackInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_alarm_event_stack_info_with_options_async(request, runtime)

    def describe_bundles_with_options(
        self,
        request: ecd_20200930_models.DescribeBundlesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeBundlesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeBundlesResponse(),
            self.do_rpcrequest('DescribeBundles', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_bundles_with_options_async(
        self,
        request: ecd_20200930_models.DescribeBundlesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeBundlesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeBundlesResponse(),
            await self.do_rpcrequest_async('DescribeBundles', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_bundles(
        self,
        request: ecd_20200930_models.DescribeBundlesRequest,
    ) -> ecd_20200930_models.DescribeBundlesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_bundles_with_options(request, runtime)

    async def describe_bundles_async(
        self,
        request: ecd_20200930_models.DescribeBundlesRequest,
    ) -> ecd_20200930_models.DescribeBundlesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_bundles_with_options_async(request, runtime)

    def describe_cens_with_options(
        self,
        request: ecd_20200930_models.DescribeCensRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeCensResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeCensResponse(),
            self.do_rpcrequest('DescribeCens', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cens_with_options_async(
        self,
        request: ecd_20200930_models.DescribeCensRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeCensResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeCensResponse(),
            await self.do_rpcrequest_async('DescribeCens', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cens(
        self,
        request: ecd_20200930_models.DescribeCensRequest,
    ) -> ecd_20200930_models.DescribeCensResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cens_with_options(request, runtime)

    async def describe_cens_async(
        self,
        request: ecd_20200930_models.DescribeCensRequest,
    ) -> ecd_20200930_models.DescribeCensResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cens_with_options_async(request, runtime)

    def describe_client_events_with_options(
        self,
        request: ecd_20200930_models.DescribeClientEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeClientEventsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeClientEventsResponse(),
            self.do_rpcrequest('DescribeClientEvents', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_client_events_with_options_async(
        self,
        request: ecd_20200930_models.DescribeClientEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeClientEventsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeClientEventsResponse(),
            await self.do_rpcrequest_async('DescribeClientEvents', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_client_events(
        self,
        request: ecd_20200930_models.DescribeClientEventsRequest,
    ) -> ecd_20200930_models.DescribeClientEventsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_client_events_with_options(request, runtime)

    async def describe_client_events_async(
        self,
        request: ecd_20200930_models.DescribeClientEventsRequest,
    ) -> ecd_20200930_models.DescribeClientEventsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_client_events_with_options_async(request, runtime)

    def describe_desktop_ids_by_vul_names_with_options(
        self,
        request: ecd_20200930_models.DescribeDesktopIdsByVulNamesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeDesktopIdsByVulNamesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeDesktopIdsByVulNamesResponse(),
            self.do_rpcrequest('DescribeDesktopIdsByVulNames', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_desktop_ids_by_vul_names_with_options_async(
        self,
        request: ecd_20200930_models.DescribeDesktopIdsByVulNamesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeDesktopIdsByVulNamesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeDesktopIdsByVulNamesResponse(),
            await self.do_rpcrequest_async('DescribeDesktopIdsByVulNames', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_desktop_ids_by_vul_names(
        self,
        request: ecd_20200930_models.DescribeDesktopIdsByVulNamesRequest,
    ) -> ecd_20200930_models.DescribeDesktopIdsByVulNamesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_desktop_ids_by_vul_names_with_options(request, runtime)

    async def describe_desktop_ids_by_vul_names_async(
        self,
        request: ecd_20200930_models.DescribeDesktopIdsByVulNamesRequest,
    ) -> ecd_20200930_models.DescribeDesktopIdsByVulNamesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_desktop_ids_by_vul_names_with_options_async(request, runtime)

    def describe_desktop_policys_with_options(
        self,
        request: ecd_20200930_models.DescribeDesktopPolicysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeDesktopPolicysResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeDesktopPolicysResponse(),
            self.do_rpcrequest('DescribeDesktopPolicys', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_desktop_policys_with_options_async(
        self,
        request: ecd_20200930_models.DescribeDesktopPolicysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeDesktopPolicysResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeDesktopPolicysResponse(),
            await self.do_rpcrequest_async('DescribeDesktopPolicys', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_desktop_policys(
        self,
        request: ecd_20200930_models.DescribeDesktopPolicysRequest,
    ) -> ecd_20200930_models.DescribeDesktopPolicysResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_desktop_policys_with_options(request, runtime)

    async def describe_desktop_policys_async(
        self,
        request: ecd_20200930_models.DescribeDesktopPolicysRequest,
    ) -> ecd_20200930_models.DescribeDesktopPolicysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_desktop_policys_with_options_async(request, runtime)

    def describe_desktops_with_options(
        self,
        request: ecd_20200930_models.DescribeDesktopsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeDesktopsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeDesktopsResponse(),
            self.do_rpcrequest('DescribeDesktops', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_desktops_with_options_async(
        self,
        request: ecd_20200930_models.DescribeDesktopsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeDesktopsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeDesktopsResponse(),
            await self.do_rpcrequest_async('DescribeDesktops', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_desktops(
        self,
        request: ecd_20200930_models.DescribeDesktopsRequest,
    ) -> ecd_20200930_models.DescribeDesktopsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_desktops_with_options(request, runtime)

    async def describe_desktops_async(
        self,
        request: ecd_20200930_models.DescribeDesktopsRequest,
    ) -> ecd_20200930_models.DescribeDesktopsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_desktops_with_options_async(request, runtime)

    def describe_desktops_in_group_with_options(
        self,
        request: ecd_20200930_models.DescribeDesktopsInGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeDesktopsInGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeDesktopsInGroupResponse(),
            self.do_rpcrequest('DescribeDesktopsInGroup', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_desktops_in_group_with_options_async(
        self,
        request: ecd_20200930_models.DescribeDesktopsInGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeDesktopsInGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeDesktopsInGroupResponse(),
            await self.do_rpcrequest_async('DescribeDesktopsInGroup', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_desktops_in_group(
        self,
        request: ecd_20200930_models.DescribeDesktopsInGroupRequest,
    ) -> ecd_20200930_models.DescribeDesktopsInGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_desktops_in_group_with_options(request, runtime)

    async def describe_desktops_in_group_async(
        self,
        request: ecd_20200930_models.DescribeDesktopsInGroupRequest,
    ) -> ecd_20200930_models.DescribeDesktopsInGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_desktops_in_group_with_options_async(request, runtime)

    def describe_desktop_types_with_options(
        self,
        request: ecd_20200930_models.DescribeDesktopTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeDesktopTypesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeDesktopTypesResponse(),
            self.do_rpcrequest('DescribeDesktopTypes', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_desktop_types_with_options_async(
        self,
        request: ecd_20200930_models.DescribeDesktopTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeDesktopTypesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeDesktopTypesResponse(),
            await self.do_rpcrequest_async('DescribeDesktopTypes', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_desktop_types(
        self,
        request: ecd_20200930_models.DescribeDesktopTypesRequest,
    ) -> ecd_20200930_models.DescribeDesktopTypesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_desktop_types_with_options(request, runtime)

    async def describe_desktop_types_async(
        self,
        request: ecd_20200930_models.DescribeDesktopTypesRequest,
    ) -> ecd_20200930_models.DescribeDesktopTypesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_desktop_types_with_options_async(request, runtime)

    def describe_directories_with_options(
        self,
        request: ecd_20200930_models.DescribeDirectoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeDirectoriesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeDirectoriesResponse(),
            self.do_rpcrequest('DescribeDirectories', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_directories_with_options_async(
        self,
        request: ecd_20200930_models.DescribeDirectoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeDirectoriesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeDirectoriesResponse(),
            await self.do_rpcrequest_async('DescribeDirectories', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_directories(
        self,
        request: ecd_20200930_models.DescribeDirectoriesRequest,
    ) -> ecd_20200930_models.DescribeDirectoriesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_directories_with_options(request, runtime)

    async def describe_directories_async(
        self,
        request: ecd_20200930_models.DescribeDirectoriesRequest,
    ) -> ecd_20200930_models.DescribeDirectoriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_directories_with_options_async(request, runtime)

    def describe_front_vul_patch_list_with_options(
        self,
        request: ecd_20200930_models.DescribeFrontVulPatchListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeFrontVulPatchListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeFrontVulPatchListResponse(),
            self.do_rpcrequest('DescribeFrontVulPatchList', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_front_vul_patch_list_with_options_async(
        self,
        request: ecd_20200930_models.DescribeFrontVulPatchListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeFrontVulPatchListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeFrontVulPatchListResponse(),
            await self.do_rpcrequest_async('DescribeFrontVulPatchList', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_front_vul_patch_list(
        self,
        request: ecd_20200930_models.DescribeFrontVulPatchListRequest,
    ) -> ecd_20200930_models.DescribeFrontVulPatchListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_front_vul_patch_list_with_options(request, runtime)

    async def describe_front_vul_patch_list_async(
        self,
        request: ecd_20200930_models.DescribeFrontVulPatchListRequest,
    ) -> ecd_20200930_models.DescribeFrontVulPatchListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_front_vul_patch_list_with_options_async(request, runtime)

    def describe_grouped_vul_with_options(
        self,
        request: ecd_20200930_models.DescribeGroupedVulRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeGroupedVulResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeGroupedVulResponse(),
            self.do_rpcrequest('DescribeGroupedVul', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_grouped_vul_with_options_async(
        self,
        request: ecd_20200930_models.DescribeGroupedVulRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeGroupedVulResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeGroupedVulResponse(),
            await self.do_rpcrequest_async('DescribeGroupedVul', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_grouped_vul(
        self,
        request: ecd_20200930_models.DescribeGroupedVulRequest,
    ) -> ecd_20200930_models.DescribeGroupedVulResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_grouped_vul_with_options(request, runtime)

    async def describe_grouped_vul_async(
        self,
        request: ecd_20200930_models.DescribeGroupedVulRequest,
    ) -> ecd_20200930_models.DescribeGroupedVulResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_grouped_vul_with_options_async(request, runtime)

    def describe_images_with_options(
        self,
        request: ecd_20200930_models.DescribeImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeImagesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeImagesResponse(),
            self.do_rpcrequest('DescribeImages', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_images_with_options_async(
        self,
        request: ecd_20200930_models.DescribeImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeImagesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeImagesResponse(),
            await self.do_rpcrequest_async('DescribeImages', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_images(
        self,
        request: ecd_20200930_models.DescribeImagesRequest,
    ) -> ecd_20200930_models.DescribeImagesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_images_with_options(request, runtime)

    async def describe_images_async(
        self,
        request: ecd_20200930_models.DescribeImagesRequest,
    ) -> ecd_20200930_models.DescribeImagesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_images_with_options_async(request, runtime)

    def describe_invocations_with_options(
        self,
        request: ecd_20200930_models.DescribeInvocationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeInvocationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeInvocationsResponse(),
            self.do_rpcrequest('DescribeInvocations', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_invocations_with_options_async(
        self,
        request: ecd_20200930_models.DescribeInvocationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeInvocationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeInvocationsResponse(),
            await self.do_rpcrequest_async('DescribeInvocations', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_invocations(
        self,
        request: ecd_20200930_models.DescribeInvocationsRequest,
    ) -> ecd_20200930_models.DescribeInvocationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_invocations_with_options(request, runtime)

    async def describe_invocations_async(
        self,
        request: ecd_20200930_models.DescribeInvocationsRequest,
    ) -> ecd_20200930_models.DescribeInvocationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_invocations_with_options_async(request, runtime)

    def describe_modification_price_with_options(
        self,
        request: ecd_20200930_models.DescribeModificationPriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeModificationPriceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeModificationPriceResponse(),
            self.do_rpcrequest('DescribeModificationPrice', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_modification_price_with_options_async(
        self,
        request: ecd_20200930_models.DescribeModificationPriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeModificationPriceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeModificationPriceResponse(),
            await self.do_rpcrequest_async('DescribeModificationPrice', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_modification_price(
        self,
        request: ecd_20200930_models.DescribeModificationPriceRequest,
    ) -> ecd_20200930_models.DescribeModificationPriceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_modification_price_with_options(request, runtime)

    async def describe_modification_price_async(
        self,
        request: ecd_20200930_models.DescribeModificationPriceRequest,
    ) -> ecd_20200930_models.DescribeModificationPriceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_modification_price_with_options_async(request, runtime)

    def describe_nasfile_systems_with_options(
        self,
        request: ecd_20200930_models.DescribeNASFileSystemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeNASFileSystemsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeNASFileSystemsResponse(),
            self.do_rpcrequest('DescribeNASFileSystems', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_nasfile_systems_with_options_async(
        self,
        request: ecd_20200930_models.DescribeNASFileSystemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeNASFileSystemsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeNASFileSystemsResponse(),
            await self.do_rpcrequest_async('DescribeNASFileSystems', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_nasfile_systems(
        self,
        request: ecd_20200930_models.DescribeNASFileSystemsRequest,
    ) -> ecd_20200930_models.DescribeNASFileSystemsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_nasfile_systems_with_options(request, runtime)

    async def describe_nasfile_systems_async(
        self,
        request: ecd_20200930_models.DescribeNASFileSystemsRequest,
    ) -> ecd_20200930_models.DescribeNASFileSystemsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_nasfile_systems_with_options_async(request, runtime)

    def describe_network_packages_with_options(
        self,
        request: ecd_20200930_models.DescribeNetworkPackagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeNetworkPackagesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeNetworkPackagesResponse(),
            self.do_rpcrequest('DescribeNetworkPackages', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_network_packages_with_options_async(
        self,
        request: ecd_20200930_models.DescribeNetworkPackagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeNetworkPackagesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeNetworkPackagesResponse(),
            await self.do_rpcrequest_async('DescribeNetworkPackages', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_network_packages(
        self,
        request: ecd_20200930_models.DescribeNetworkPackagesRequest,
    ) -> ecd_20200930_models.DescribeNetworkPackagesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_network_packages_with_options(request, runtime)

    async def describe_network_packages_async(
        self,
        request: ecd_20200930_models.DescribeNetworkPackagesRequest,
    ) -> ecd_20200930_models.DescribeNetworkPackagesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_network_packages_with_options_async(request, runtime)

    def describe_office_sites_with_options(
        self,
        request: ecd_20200930_models.DescribeOfficeSitesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeOfficeSitesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeOfficeSitesResponse(),
            self.do_rpcrequest('DescribeOfficeSites', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_office_sites_with_options_async(
        self,
        request: ecd_20200930_models.DescribeOfficeSitesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeOfficeSitesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeOfficeSitesResponse(),
            await self.do_rpcrequest_async('DescribeOfficeSites', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_office_sites(
        self,
        request: ecd_20200930_models.DescribeOfficeSitesRequest,
    ) -> ecd_20200930_models.DescribeOfficeSitesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_office_sites_with_options(request, runtime)

    async def describe_office_sites_async(
        self,
        request: ecd_20200930_models.DescribeOfficeSitesRequest,
    ) -> ecd_20200930_models.DescribeOfficeSitesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_office_sites_with_options_async(request, runtime)

    def describe_policy_groups_with_options(
        self,
        request: ecd_20200930_models.DescribePolicyGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribePolicyGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribePolicyGroupsResponse(),
            self.do_rpcrequest('DescribePolicyGroups', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_policy_groups_with_options_async(
        self,
        request: ecd_20200930_models.DescribePolicyGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribePolicyGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribePolicyGroupsResponse(),
            await self.do_rpcrequest_async('DescribePolicyGroups', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_policy_groups(
        self,
        request: ecd_20200930_models.DescribePolicyGroupsRequest,
    ) -> ecd_20200930_models.DescribePolicyGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_policy_groups_with_options(request, runtime)

    async def describe_policy_groups_async(
        self,
        request: ecd_20200930_models.DescribePolicyGroupsRequest,
    ) -> ecd_20200930_models.DescribePolicyGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_policy_groups_with_options_async(request, runtime)

    def describe_post_paid_desktop_bills_with_options(
        self,
        request: ecd_20200930_models.DescribePostPaidDesktopBillsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribePostPaidDesktopBillsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribePostPaidDesktopBillsResponse(),
            self.do_rpcrequest('DescribePostPaidDesktopBills', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_post_paid_desktop_bills_with_options_async(
        self,
        request: ecd_20200930_models.DescribePostPaidDesktopBillsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribePostPaidDesktopBillsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribePostPaidDesktopBillsResponse(),
            await self.do_rpcrequest_async('DescribePostPaidDesktopBills', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_post_paid_desktop_bills(
        self,
        request: ecd_20200930_models.DescribePostPaidDesktopBillsRequest,
    ) -> ecd_20200930_models.DescribePostPaidDesktopBillsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_post_paid_desktop_bills_with_options(request, runtime)

    async def describe_post_paid_desktop_bills_async(
        self,
        request: ecd_20200930_models.DescribePostPaidDesktopBillsRequest,
    ) -> ecd_20200930_models.DescribePostPaidDesktopBillsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_post_paid_desktop_bills_with_options_async(request, runtime)

    def describe_price_with_options(
        self,
        request: ecd_20200930_models.DescribePriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribePriceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribePriceResponse(),
            self.do_rpcrequest('DescribePrice', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_price_with_options_async(
        self,
        request: ecd_20200930_models.DescribePriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribePriceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribePriceResponse(),
            await self.do_rpcrequest_async('DescribePrice', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_price(
        self,
        request: ecd_20200930_models.DescribePriceRequest,
    ) -> ecd_20200930_models.DescribePriceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_price_with_options(request, runtime)

    async def describe_price_async(
        self,
        request: ecd_20200930_models.DescribePriceRequest,
    ) -> ecd_20200930_models.DescribePriceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_price_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: ecd_20200930_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeRegionsResponse(),
            self.do_rpcrequest('DescribeRegions', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: ecd_20200930_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeRegionsResponse(),
            await self.do_rpcrequest_async('DescribeRegions', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_regions(
        self,
        request: ecd_20200930_models.DescribeRegionsRequest,
    ) -> ecd_20200930_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: ecd_20200930_models.DescribeRegionsRequest,
    ) -> ecd_20200930_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_scale_strategys_with_options(
        self,
        request: ecd_20200930_models.DescribeScaleStrategysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeScaleStrategysResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeScaleStrategysResponse(),
            self.do_rpcrequest('DescribeScaleStrategys', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_scale_strategys_with_options_async(
        self,
        request: ecd_20200930_models.DescribeScaleStrategysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeScaleStrategysResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeScaleStrategysResponse(),
            await self.do_rpcrequest_async('DescribeScaleStrategys', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_scale_strategys(
        self,
        request: ecd_20200930_models.DescribeScaleStrategysRequest,
    ) -> ecd_20200930_models.DescribeScaleStrategysResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scale_strategys_with_options(request, runtime)

    async def describe_scale_strategys_async(
        self,
        request: ecd_20200930_models.DescribeScaleStrategysRequest,
    ) -> ecd_20200930_models.DescribeScaleStrategysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scale_strategys_with_options_async(request, runtime)

    def describe_scan_task_progress_with_options(
        self,
        request: ecd_20200930_models.DescribeScanTaskProgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeScanTaskProgressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeScanTaskProgressResponse(),
            self.do_rpcrequest('DescribeScanTaskProgress', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_scan_task_progress_with_options_async(
        self,
        request: ecd_20200930_models.DescribeScanTaskProgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeScanTaskProgressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeScanTaskProgressResponse(),
            await self.do_rpcrequest_async('DescribeScanTaskProgress', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_scan_task_progress(
        self,
        request: ecd_20200930_models.DescribeScanTaskProgressRequest,
    ) -> ecd_20200930_models.DescribeScanTaskProgressResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scan_task_progress_with_options(request, runtime)

    async def describe_scan_task_progress_async(
        self,
        request: ecd_20200930_models.DescribeScanTaskProgressRequest,
    ) -> ecd_20200930_models.DescribeScanTaskProgressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scan_task_progress_with_options_async(request, runtime)

    def describe_security_event_operations_with_options(
        self,
        request: ecd_20200930_models.DescribeSecurityEventOperationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeSecurityEventOperationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeSecurityEventOperationsResponse(),
            self.do_rpcrequest('DescribeSecurityEventOperations', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_security_event_operations_with_options_async(
        self,
        request: ecd_20200930_models.DescribeSecurityEventOperationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeSecurityEventOperationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeSecurityEventOperationsResponse(),
            await self.do_rpcrequest_async('DescribeSecurityEventOperations', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_security_event_operations(
        self,
        request: ecd_20200930_models.DescribeSecurityEventOperationsRequest,
    ) -> ecd_20200930_models.DescribeSecurityEventOperationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_security_event_operations_with_options(request, runtime)

    async def describe_security_event_operations_async(
        self,
        request: ecd_20200930_models.DescribeSecurityEventOperationsRequest,
    ) -> ecd_20200930_models.DescribeSecurityEventOperationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_security_event_operations_with_options_async(request, runtime)

    def describe_security_event_operation_status_with_options(
        self,
        request: ecd_20200930_models.DescribeSecurityEventOperationStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeSecurityEventOperationStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeSecurityEventOperationStatusResponse(),
            self.do_rpcrequest('DescribeSecurityEventOperationStatus', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_security_event_operation_status_with_options_async(
        self,
        request: ecd_20200930_models.DescribeSecurityEventOperationStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeSecurityEventOperationStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeSecurityEventOperationStatusResponse(),
            await self.do_rpcrequest_async('DescribeSecurityEventOperationStatus', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_security_event_operation_status(
        self,
        request: ecd_20200930_models.DescribeSecurityEventOperationStatusRequest,
    ) -> ecd_20200930_models.DescribeSecurityEventOperationStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_security_event_operation_status_with_options(request, runtime)

    async def describe_security_event_operation_status_async(
        self,
        request: ecd_20200930_models.DescribeSecurityEventOperationStatusRequest,
    ) -> ecd_20200930_models.DescribeSecurityEventOperationStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_security_event_operation_status_with_options_async(request, runtime)

    def describe_snapshots_with_options(
        self,
        request: ecd_20200930_models.DescribeSnapshotsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeSnapshotsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeSnapshotsResponse(),
            self.do_rpcrequest('DescribeSnapshots', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_snapshots_with_options_async(
        self,
        request: ecd_20200930_models.DescribeSnapshotsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeSnapshotsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeSnapshotsResponse(),
            await self.do_rpcrequest_async('DescribeSnapshots', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_snapshots(
        self,
        request: ecd_20200930_models.DescribeSnapshotsRequest,
    ) -> ecd_20200930_models.DescribeSnapshotsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_snapshots_with_options(request, runtime)

    async def describe_snapshots_async(
        self,
        request: ecd_20200930_models.DescribeSnapshotsRequest,
    ) -> ecd_20200930_models.DescribeSnapshotsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_snapshots_with_options_async(request, runtime)

    def describe_susp_event_overview_with_options(
        self,
        request: ecd_20200930_models.DescribeSuspEventOverviewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeSuspEventOverviewResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeSuspEventOverviewResponse(),
            self.do_rpcrequest('DescribeSuspEventOverview', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_susp_event_overview_with_options_async(
        self,
        request: ecd_20200930_models.DescribeSuspEventOverviewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeSuspEventOverviewResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeSuspEventOverviewResponse(),
            await self.do_rpcrequest_async('DescribeSuspEventOverview', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_susp_event_overview(
        self,
        request: ecd_20200930_models.DescribeSuspEventOverviewRequest,
    ) -> ecd_20200930_models.DescribeSuspEventOverviewResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_susp_event_overview_with_options(request, runtime)

    async def describe_susp_event_overview_async(
        self,
        request: ecd_20200930_models.DescribeSuspEventOverviewRequest,
    ) -> ecd_20200930_models.DescribeSuspEventOverviewResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_susp_event_overview_with_options_async(request, runtime)

    def describe_susp_event_quara_files_with_options(
        self,
        request: ecd_20200930_models.DescribeSuspEventQuaraFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeSuspEventQuaraFilesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeSuspEventQuaraFilesResponse(),
            self.do_rpcrequest('DescribeSuspEventQuaraFiles', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_susp_event_quara_files_with_options_async(
        self,
        request: ecd_20200930_models.DescribeSuspEventQuaraFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeSuspEventQuaraFilesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeSuspEventQuaraFilesResponse(),
            await self.do_rpcrequest_async('DescribeSuspEventQuaraFiles', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_susp_event_quara_files(
        self,
        request: ecd_20200930_models.DescribeSuspEventQuaraFilesRequest,
    ) -> ecd_20200930_models.DescribeSuspEventQuaraFilesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_susp_event_quara_files_with_options(request, runtime)

    async def describe_susp_event_quara_files_async(
        self,
        request: ecd_20200930_models.DescribeSuspEventQuaraFilesRequest,
    ) -> ecd_20200930_models.DescribeSuspEventQuaraFilesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_susp_event_quara_files_with_options_async(request, runtime)

    def describe_susp_events_with_options(
        self,
        request: ecd_20200930_models.DescribeSuspEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeSuspEventsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeSuspEventsResponse(),
            self.do_rpcrequest('DescribeSuspEvents', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_susp_events_with_options_async(
        self,
        request: ecd_20200930_models.DescribeSuspEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeSuspEventsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeSuspEventsResponse(),
            await self.do_rpcrequest_async('DescribeSuspEvents', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_susp_events(
        self,
        request: ecd_20200930_models.DescribeSuspEventsRequest,
    ) -> ecd_20200930_models.DescribeSuspEventsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_susp_events_with_options(request, runtime)

    async def describe_susp_events_async(
        self,
        request: ecd_20200930_models.DescribeSuspEventsRequest,
    ) -> ecd_20200930_models.DescribeSuspEventsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_susp_events_with_options_async(request, runtime)

    def describe_user_connection_records_with_options(
        self,
        request: ecd_20200930_models.DescribeUserConnectionRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeUserConnectionRecordsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeUserConnectionRecordsResponse(),
            self.do_rpcrequest('DescribeUserConnectionRecords', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_user_connection_records_with_options_async(
        self,
        request: ecd_20200930_models.DescribeUserConnectionRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeUserConnectionRecordsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeUserConnectionRecordsResponse(),
            await self.do_rpcrequest_async('DescribeUserConnectionRecords', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_user_connection_records(
        self,
        request: ecd_20200930_models.DescribeUserConnectionRecordsRequest,
    ) -> ecd_20200930_models.DescribeUserConnectionRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_user_connection_records_with_options(request, runtime)

    async def describe_user_connection_records_async(
        self,
        request: ecd_20200930_models.DescribeUserConnectionRecordsRequest,
    ) -> ecd_20200930_models.DescribeUserConnectionRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_connection_records_with_options_async(request, runtime)

    def describe_users_in_group_with_options(
        self,
        request: ecd_20200930_models.DescribeUsersInGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeUsersInGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeUsersInGroupResponse(),
            self.do_rpcrequest('DescribeUsersInGroup', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_users_in_group_with_options_async(
        self,
        request: ecd_20200930_models.DescribeUsersInGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeUsersInGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeUsersInGroupResponse(),
            await self.do_rpcrequest_async('DescribeUsersInGroup', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_users_in_group(
        self,
        request: ecd_20200930_models.DescribeUsersInGroupRequest,
    ) -> ecd_20200930_models.DescribeUsersInGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_users_in_group_with_options(request, runtime)

    async def describe_users_in_group_async(
        self,
        request: ecd_20200930_models.DescribeUsersInGroupRequest,
    ) -> ecd_20200930_models.DescribeUsersInGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_users_in_group_with_options_async(request, runtime)

    def describe_virtual_mfadevices_with_options(
        self,
        request: ecd_20200930_models.DescribeVirtualMFADevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeVirtualMFADevicesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeVirtualMFADevicesResponse(),
            self.do_rpcrequest('DescribeVirtualMFADevices', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_virtual_mfadevices_with_options_async(
        self,
        request: ecd_20200930_models.DescribeVirtualMFADevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeVirtualMFADevicesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeVirtualMFADevicesResponse(),
            await self.do_rpcrequest_async('DescribeVirtualMFADevices', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_virtual_mfadevices(
        self,
        request: ecd_20200930_models.DescribeVirtualMFADevicesRequest,
    ) -> ecd_20200930_models.DescribeVirtualMFADevicesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_virtual_mfadevices_with_options(request, runtime)

    async def describe_virtual_mfadevices_async(
        self,
        request: ecd_20200930_models.DescribeVirtualMFADevicesRequest,
    ) -> ecd_20200930_models.DescribeVirtualMFADevicesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_virtual_mfadevices_with_options_async(request, runtime)

    def describe_vul_details_with_options(
        self,
        request: ecd_20200930_models.DescribeVulDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeVulDetailsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeVulDetailsResponse(),
            self.do_rpcrequest('DescribeVulDetails', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_vul_details_with_options_async(
        self,
        request: ecd_20200930_models.DescribeVulDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeVulDetailsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeVulDetailsResponse(),
            await self.do_rpcrequest_async('DescribeVulDetails', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vul_details(
        self,
        request: ecd_20200930_models.DescribeVulDetailsRequest,
    ) -> ecd_20200930_models.DescribeVulDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vul_details_with_options(request, runtime)

    async def describe_vul_details_async(
        self,
        request: ecd_20200930_models.DescribeVulDetailsRequest,
    ) -> ecd_20200930_models.DescribeVulDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vul_details_with_options_async(request, runtime)

    def describe_vul_list_with_options(
        self,
        request: ecd_20200930_models.DescribeVulListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeVulListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeVulListResponse(),
            self.do_rpcrequest('DescribeVulList', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_vul_list_with_options_async(
        self,
        request: ecd_20200930_models.DescribeVulListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeVulListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeVulListResponse(),
            await self.do_rpcrequest_async('DescribeVulList', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vul_list(
        self,
        request: ecd_20200930_models.DescribeVulListRequest,
    ) -> ecd_20200930_models.DescribeVulListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vul_list_with_options(request, runtime)

    async def describe_vul_list_async(
        self,
        request: ecd_20200930_models.DescribeVulListRequest,
    ) -> ecd_20200930_models.DescribeVulListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vul_list_with_options_async(request, runtime)

    def describe_vul_overview_with_options(
        self,
        request: ecd_20200930_models.DescribeVulOverviewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeVulOverviewResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeVulOverviewResponse(),
            self.do_rpcrequest('DescribeVulOverview', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_vul_overview_with_options_async(
        self,
        request: ecd_20200930_models.DescribeVulOverviewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeVulOverviewResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeVulOverviewResponse(),
            await self.do_rpcrequest_async('DescribeVulOverview', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vul_overview(
        self,
        request: ecd_20200930_models.DescribeVulOverviewRequest,
    ) -> ecd_20200930_models.DescribeVulOverviewResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vul_overview_with_options(request, runtime)

    async def describe_vul_overview_async(
        self,
        request: ecd_20200930_models.DescribeVulOverviewRequest,
    ) -> ecd_20200930_models.DescribeVulOverviewResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vul_overview_with_options_async(request, runtime)

    def describe_zones_with_options(
        self,
        request: ecd_20200930_models.DescribeZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeZonesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeZonesResponse(),
            self.do_rpcrequest('DescribeZones', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_zones_with_options_async(
        self,
        request: ecd_20200930_models.DescribeZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeZonesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeZonesResponse(),
            await self.do_rpcrequest_async('DescribeZones', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_zones(
        self,
        request: ecd_20200930_models.DescribeZonesRequest,
    ) -> ecd_20200930_models.DescribeZonesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_zones_with_options(request, runtime)

    async def describe_zones_async(
        self,
        request: ecd_20200930_models.DescribeZonesRequest,
    ) -> ecd_20200930_models.DescribeZonesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_zones_with_options_async(request, runtime)

    def detach_cen_with_options(
        self,
        request: ecd_20200930_models.DetachCenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DetachCenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DetachCenResponse(),
            self.do_rpcrequest('DetachCen', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detach_cen_with_options_async(
        self,
        request: ecd_20200930_models.DetachCenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DetachCenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DetachCenResponse(),
            await self.do_rpcrequest_async('DetachCen', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detach_cen(
        self,
        request: ecd_20200930_models.DetachCenRequest,
    ) -> ecd_20200930_models.DetachCenResponse:
        runtime = util_models.RuntimeOptions()
        return self.detach_cen_with_options(request, runtime)

    async def detach_cen_async(
        self,
        request: ecd_20200930_models.DetachCenRequest,
    ) -> ecd_20200930_models.DetachCenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detach_cen_with_options_async(request, runtime)

    def do_check_resource_with_options(
        self,
        request: ecd_20200930_models.DoCheckResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DoCheckResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DoCheckResourceResponse(),
            self.do_rpcrequest('DoCheckResource', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def do_check_resource_with_options_async(
        self,
        request: ecd_20200930_models.DoCheckResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DoCheckResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DoCheckResourceResponse(),
            await self.do_rpcrequest_async('DoCheckResource', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def do_check_resource(
        self,
        request: ecd_20200930_models.DoCheckResourceRequest,
    ) -> ecd_20200930_models.DoCheckResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.do_check_resource_with_options(request, runtime)

    async def do_check_resource_async(
        self,
        request: ecd_20200930_models.DoCheckResourceRequest,
    ) -> ecd_20200930_models.DoCheckResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.do_check_resource_with_options_async(request, runtime)

    def do_logical_delete_resource_with_options(
        self,
        request: ecd_20200930_models.DoLogicalDeleteResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DoLogicalDeleteResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DoLogicalDeleteResourceResponse(),
            self.do_rpcrequest('DoLogicalDeleteResource', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def do_logical_delete_resource_with_options_async(
        self,
        request: ecd_20200930_models.DoLogicalDeleteResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DoLogicalDeleteResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DoLogicalDeleteResourceResponse(),
            await self.do_rpcrequest_async('DoLogicalDeleteResource', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def do_logical_delete_resource(
        self,
        request: ecd_20200930_models.DoLogicalDeleteResourceRequest,
    ) -> ecd_20200930_models.DoLogicalDeleteResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.do_logical_delete_resource_with_options(request, runtime)

    async def do_logical_delete_resource_async(
        self,
        request: ecd_20200930_models.DoLogicalDeleteResourceRequest,
    ) -> ecd_20200930_models.DoLogicalDeleteResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.do_logical_delete_resource_with_options_async(request, runtime)

    def do_physical_delete_resource_with_options(
        self,
        request: ecd_20200930_models.DoPhysicalDeleteResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DoPhysicalDeleteResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DoPhysicalDeleteResourceResponse(),
            self.do_rpcrequest('DoPhysicalDeleteResource', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def do_physical_delete_resource_with_options_async(
        self,
        request: ecd_20200930_models.DoPhysicalDeleteResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DoPhysicalDeleteResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DoPhysicalDeleteResourceResponse(),
            await self.do_rpcrequest_async('DoPhysicalDeleteResource', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def do_physical_delete_resource(
        self,
        request: ecd_20200930_models.DoPhysicalDeleteResourceRequest,
    ) -> ecd_20200930_models.DoPhysicalDeleteResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.do_physical_delete_resource_with_options(request, runtime)

    async def do_physical_delete_resource_async(
        self,
        request: ecd_20200930_models.DoPhysicalDeleteResourceRequest,
    ) -> ecd_20200930_models.DoPhysicalDeleteResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.do_physical_delete_resource_with_options_async(request, runtime)

    def get_connection_ticket_with_options(
        self,
        request: ecd_20200930_models.GetConnectionTicketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.GetConnectionTicketResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.GetConnectionTicketResponse(),
            self.do_rpcrequest('GetConnectionTicket', '2020-09-30', 'HTTP', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_connection_ticket_with_options_async(
        self,
        request: ecd_20200930_models.GetConnectionTicketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.GetConnectionTicketResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.GetConnectionTicketResponse(),
            await self.do_rpcrequest_async('GetConnectionTicket', '2020-09-30', 'HTTP', 'POST', 'AK', 'json', req, runtime)
        )

    def get_connection_ticket(
        self,
        request: ecd_20200930_models.GetConnectionTicketRequest,
    ) -> ecd_20200930_models.GetConnectionTicketResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_connection_ticket_with_options(request, runtime)

    async def get_connection_ticket_async(
        self,
        request: ecd_20200930_models.GetConnectionTicketRequest,
    ) -> ecd_20200930_models.GetConnectionTicketResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_connection_ticket_with_options_async(request, runtime)

    def get_desktop_group_detail_with_options(
        self,
        request: ecd_20200930_models.GetDesktopGroupDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.GetDesktopGroupDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.GetDesktopGroupDetailResponse(),
            self.do_rpcrequest('GetDesktopGroupDetail', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_desktop_group_detail_with_options_async(
        self,
        request: ecd_20200930_models.GetDesktopGroupDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.GetDesktopGroupDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.GetDesktopGroupDetailResponse(),
            await self.do_rpcrequest_async('GetDesktopGroupDetail', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_desktop_group_detail(
        self,
        request: ecd_20200930_models.GetDesktopGroupDetailRequest,
    ) -> ecd_20200930_models.GetDesktopGroupDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_desktop_group_detail_with_options(request, runtime)

    async def get_desktop_group_detail_async(
        self,
        request: ecd_20200930_models.GetDesktopGroupDetailRequest,
    ) -> ecd_20200930_models.GetDesktopGroupDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_desktop_group_detail_with_options_async(request, runtime)

    def get_desktop_users_with_options(
        self,
        request: ecd_20200930_models.GetDesktopUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.GetDesktopUsersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.GetDesktopUsersResponse(),
            self.do_rpcrequest('GetDesktopUsers', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_desktop_users_with_options_async(
        self,
        request: ecd_20200930_models.GetDesktopUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.GetDesktopUsersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.GetDesktopUsersResponse(),
            await self.do_rpcrequest_async('GetDesktopUsers', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_desktop_users(
        self,
        request: ecd_20200930_models.GetDesktopUsersRequest,
    ) -> ecd_20200930_models.GetDesktopUsersResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_desktop_users_with_options(request, runtime)

    async def get_desktop_users_async(
        self,
        request: ecd_20200930_models.GetDesktopUsersRequest,
    ) -> ecd_20200930_models.GetDesktopUsersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_desktop_users_with_options_async(request, runtime)

    def get_directory_sso_status_with_options(
        self,
        request: ecd_20200930_models.GetDirectorySsoStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.GetDirectorySsoStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.GetDirectorySsoStatusResponse(),
            self.do_rpcrequest('GetDirectorySsoStatus', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_directory_sso_status_with_options_async(
        self,
        request: ecd_20200930_models.GetDirectorySsoStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.GetDirectorySsoStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.GetDirectorySsoStatusResponse(),
            await self.do_rpcrequest_async('GetDirectorySsoStatus', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_directory_sso_status(
        self,
        request: ecd_20200930_models.GetDirectorySsoStatusRequest,
    ) -> ecd_20200930_models.GetDirectorySsoStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_directory_sso_status_with_options(request, runtime)

    async def get_directory_sso_status_async(
        self,
        request: ecd_20200930_models.GetDirectorySsoStatusRequest,
    ) -> ecd_20200930_models.GetDirectorySsoStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_directory_sso_status_with_options_async(request, runtime)

    def get_office_site_sso_status_with_options(
        self,
        request: ecd_20200930_models.GetOfficeSiteSsoStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.GetOfficeSiteSsoStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.GetOfficeSiteSsoStatusResponse(),
            self.do_rpcrequest('GetOfficeSiteSsoStatus', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_office_site_sso_status_with_options_async(
        self,
        request: ecd_20200930_models.GetOfficeSiteSsoStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.GetOfficeSiteSsoStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.GetOfficeSiteSsoStatusResponse(),
            await self.do_rpcrequest_async('GetOfficeSiteSsoStatus', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_office_site_sso_status(
        self,
        request: ecd_20200930_models.GetOfficeSiteSsoStatusRequest,
    ) -> ecd_20200930_models.GetOfficeSiteSsoStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_office_site_sso_status_with_options(request, runtime)

    async def get_office_site_sso_status_async(
        self,
        request: ecd_20200930_models.GetOfficeSiteSsoStatusRequest,
    ) -> ecd_20200930_models.GetOfficeSiteSsoStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_office_site_sso_status_with_options_async(request, runtime)

    def get_sp_metadata_with_options(
        self,
        request: ecd_20200930_models.GetSpMetadataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.GetSpMetadataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.GetSpMetadataResponse(),
            self.do_rpcrequest('GetSpMetadata', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_sp_metadata_with_options_async(
        self,
        request: ecd_20200930_models.GetSpMetadataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.GetSpMetadataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.GetSpMetadataResponse(),
            await self.do_rpcrequest_async('GetSpMetadata', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_sp_metadata(
        self,
        request: ecd_20200930_models.GetSpMetadataRequest,
    ) -> ecd_20200930_models.GetSpMetadataResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_sp_metadata_with_options(request, runtime)

    async def get_sp_metadata_async(
        self,
        request: ecd_20200930_models.GetSpMetadataRequest,
    ) -> ecd_20200930_models.GetSpMetadataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_sp_metadata_with_options_async(request, runtime)

    def handle_security_events_with_options(
        self,
        request: ecd_20200930_models.HandleSecurityEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.HandleSecurityEventsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.HandleSecurityEventsResponse(),
            self.do_rpcrequest('HandleSecurityEvents', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def handle_security_events_with_options_async(
        self,
        request: ecd_20200930_models.HandleSecurityEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.HandleSecurityEventsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.HandleSecurityEventsResponse(),
            await self.do_rpcrequest_async('HandleSecurityEvents', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def handle_security_events(
        self,
        request: ecd_20200930_models.HandleSecurityEventsRequest,
    ) -> ecd_20200930_models.HandleSecurityEventsResponse:
        runtime = util_models.RuntimeOptions()
        return self.handle_security_events_with_options(request, runtime)

    async def handle_security_events_async(
        self,
        request: ecd_20200930_models.HandleSecurityEventsRequest,
    ) -> ecd_20200930_models.HandleSecurityEventsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.handle_security_events_with_options_async(request, runtime)

    def list_directory_users_with_options(
        self,
        request: ecd_20200930_models.ListDirectoryUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ListDirectoryUsersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ListDirectoryUsersResponse(),
            self.do_rpcrequest('ListDirectoryUsers', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_directory_users_with_options_async(
        self,
        request: ecd_20200930_models.ListDirectoryUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ListDirectoryUsersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ListDirectoryUsersResponse(),
            await self.do_rpcrequest_async('ListDirectoryUsers', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_directory_users(
        self,
        request: ecd_20200930_models.ListDirectoryUsersRequest,
    ) -> ecd_20200930_models.ListDirectoryUsersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_directory_users_with_options(request, runtime)

    async def list_directory_users_async(
        self,
        request: ecd_20200930_models.ListDirectoryUsersRequest,
    ) -> ecd_20200930_models.ListDirectoryUsersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_directory_users_with_options_async(request, runtime)

    def list_office_site_overview_with_options(
        self,
        request: ecd_20200930_models.ListOfficeSiteOverviewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ListOfficeSiteOverviewResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ListOfficeSiteOverviewResponse(),
            self.do_rpcrequest('ListOfficeSiteOverview', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_office_site_overview_with_options_async(
        self,
        request: ecd_20200930_models.ListOfficeSiteOverviewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ListOfficeSiteOverviewResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ListOfficeSiteOverviewResponse(),
            await self.do_rpcrequest_async('ListOfficeSiteOverview', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_office_site_overview(
        self,
        request: ecd_20200930_models.ListOfficeSiteOverviewRequest,
    ) -> ecd_20200930_models.ListOfficeSiteOverviewResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_office_site_overview_with_options(request, runtime)

    async def list_office_site_overview_async(
        self,
        request: ecd_20200930_models.ListOfficeSiteOverviewRequest,
    ) -> ecd_20200930_models.ListOfficeSiteOverviewResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_office_site_overview_with_options_async(request, runtime)

    def list_office_site_users_with_options(
        self,
        request: ecd_20200930_models.ListOfficeSiteUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ListOfficeSiteUsersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ListOfficeSiteUsersResponse(),
            self.do_rpcrequest('ListOfficeSiteUsers', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_office_site_users_with_options_async(
        self,
        request: ecd_20200930_models.ListOfficeSiteUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ListOfficeSiteUsersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ListOfficeSiteUsersResponse(),
            await self.do_rpcrequest_async('ListOfficeSiteUsers', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_office_site_users(
        self,
        request: ecd_20200930_models.ListOfficeSiteUsersRequest,
    ) -> ecd_20200930_models.ListOfficeSiteUsersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_office_site_users_with_options(request, runtime)

    async def list_office_site_users_async(
        self,
        request: ecd_20200930_models.ListOfficeSiteUsersRequest,
    ) -> ecd_20200930_models.ListOfficeSiteUsersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_office_site_users_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: ecd_20200930_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ListTagResourcesResponse(),
            self.do_rpcrequest('ListTagResources', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: ecd_20200930_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ListTagResourcesResponse(),
            await self.do_rpcrequest_async('ListTagResources', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag_resources(
        self,
        request: ecd_20200930_models.ListTagResourcesRequest,
    ) -> ecd_20200930_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: ecd_20200930_models.ListTagResourcesRequest,
    ) -> ecd_20200930_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def lock_virtual_mfadevice_with_options(
        self,
        request: ecd_20200930_models.LockVirtualMFADeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.LockVirtualMFADeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.LockVirtualMFADeviceResponse(),
            self.do_rpcrequest('LockVirtualMFADevice', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def lock_virtual_mfadevice_with_options_async(
        self,
        request: ecd_20200930_models.LockVirtualMFADeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.LockVirtualMFADeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.LockVirtualMFADeviceResponse(),
            await self.do_rpcrequest_async('LockVirtualMFADevice', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def lock_virtual_mfadevice(
        self,
        request: ecd_20200930_models.LockVirtualMFADeviceRequest,
    ) -> ecd_20200930_models.LockVirtualMFADeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.lock_virtual_mfadevice_with_options(request, runtime)

    async def lock_virtual_mfadevice_async(
        self,
        request: ecd_20200930_models.LockVirtualMFADeviceRequest,
    ) -> ecd_20200930_models.LockVirtualMFADeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.lock_virtual_mfadevice_with_options_async(request, runtime)

    def modify_adconnector_directory_with_options(
        self,
        request: ecd_20200930_models.ModifyADConnectorDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyADConnectorDirectoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyADConnectorDirectoryResponse(),
            self.do_rpcrequest('ModifyADConnectorDirectory', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_adconnector_directory_with_options_async(
        self,
        request: ecd_20200930_models.ModifyADConnectorDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyADConnectorDirectoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyADConnectorDirectoryResponse(),
            await self.do_rpcrequest_async('ModifyADConnectorDirectory', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_adconnector_directory(
        self,
        request: ecd_20200930_models.ModifyADConnectorDirectoryRequest,
    ) -> ecd_20200930_models.ModifyADConnectorDirectoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_adconnector_directory_with_options(request, runtime)

    async def modify_adconnector_directory_async(
        self,
        request: ecd_20200930_models.ModifyADConnectorDirectoryRequest,
    ) -> ecd_20200930_models.ModifyADConnectorDirectoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_adconnector_directory_with_options_async(request, runtime)

    def modify_adconnector_office_site_with_options(
        self,
        request: ecd_20200930_models.ModifyADConnectorOfficeSiteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyADConnectorOfficeSiteResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyADConnectorOfficeSiteResponse(),
            self.do_rpcrequest('ModifyADConnectorOfficeSite', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_adconnector_office_site_with_options_async(
        self,
        request: ecd_20200930_models.ModifyADConnectorOfficeSiteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyADConnectorOfficeSiteResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyADConnectorOfficeSiteResponse(),
            await self.do_rpcrequest_async('ModifyADConnectorOfficeSite', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_adconnector_office_site(
        self,
        request: ecd_20200930_models.ModifyADConnectorOfficeSiteRequest,
    ) -> ecd_20200930_models.ModifyADConnectorOfficeSiteResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_adconnector_office_site_with_options(request, runtime)

    async def modify_adconnector_office_site_async(
        self,
        request: ecd_20200930_models.ModifyADConnectorOfficeSiteRequest,
    ) -> ecd_20200930_models.ModifyADConnectorOfficeSiteResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_adconnector_office_site_with_options_async(request, runtime)

    def modify_bundle_with_options(
        self,
        request: ecd_20200930_models.ModifyBundleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyBundleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyBundleResponse(),
            self.do_rpcrequest('ModifyBundle', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_bundle_with_options_async(
        self,
        request: ecd_20200930_models.ModifyBundleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyBundleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyBundleResponse(),
            await self.do_rpcrequest_async('ModifyBundle', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_bundle(
        self,
        request: ecd_20200930_models.ModifyBundleRequest,
    ) -> ecd_20200930_models.ModifyBundleResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_bundle_with_options(request, runtime)

    async def modify_bundle_async(
        self,
        request: ecd_20200930_models.ModifyBundleRequest,
    ) -> ecd_20200930_models.ModifyBundleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_bundle_with_options_async(request, runtime)

    def modify_desktop_group_with_options(
        self,
        request: ecd_20200930_models.ModifyDesktopGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyDesktopGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyDesktopGroupResponse(),
            self.do_rpcrequest('ModifyDesktopGroup', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_desktop_group_with_options_async(
        self,
        request: ecd_20200930_models.ModifyDesktopGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyDesktopGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyDesktopGroupResponse(),
            await self.do_rpcrequest_async('ModifyDesktopGroup', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_desktop_group(
        self,
        request: ecd_20200930_models.ModifyDesktopGroupRequest,
    ) -> ecd_20200930_models.ModifyDesktopGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_desktop_group_with_options(request, runtime)

    async def modify_desktop_group_async(
        self,
        request: ecd_20200930_models.ModifyDesktopGroupRequest,
    ) -> ecd_20200930_models.ModifyDesktopGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_desktop_group_with_options_async(request, runtime)

    def modify_desktop_name_with_options(
        self,
        request: ecd_20200930_models.ModifyDesktopNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyDesktopNameResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyDesktopNameResponse(),
            self.do_rpcrequest('ModifyDesktopName', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_desktop_name_with_options_async(
        self,
        request: ecd_20200930_models.ModifyDesktopNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyDesktopNameResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyDesktopNameResponse(),
            await self.do_rpcrequest_async('ModifyDesktopName', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_desktop_name(
        self,
        request: ecd_20200930_models.ModifyDesktopNameRequest,
    ) -> ecd_20200930_models.ModifyDesktopNameResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_desktop_name_with_options(request, runtime)

    async def modify_desktop_name_async(
        self,
        request: ecd_20200930_models.ModifyDesktopNameRequest,
    ) -> ecd_20200930_models.ModifyDesktopNameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_desktop_name_with_options_async(request, runtime)

    def modify_desktop_policys_with_options(
        self,
        request: ecd_20200930_models.ModifyDesktopPolicysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyDesktopPolicysResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyDesktopPolicysResponse(),
            self.do_rpcrequest('ModifyDesktopPolicys', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_desktop_policys_with_options_async(
        self,
        request: ecd_20200930_models.ModifyDesktopPolicysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyDesktopPolicysResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyDesktopPolicysResponse(),
            await self.do_rpcrequest_async('ModifyDesktopPolicys', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_desktop_policys(
        self,
        request: ecd_20200930_models.ModifyDesktopPolicysRequest,
    ) -> ecd_20200930_models.ModifyDesktopPolicysResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_desktop_policys_with_options(request, runtime)

    async def modify_desktop_policys_async(
        self,
        request: ecd_20200930_models.ModifyDesktopPolicysRequest,
    ) -> ecd_20200930_models.ModifyDesktopPolicysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_desktop_policys_with_options_async(request, runtime)

    def modify_desktop_spec_with_options(
        self,
        request: ecd_20200930_models.ModifyDesktopSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyDesktopSpecResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyDesktopSpecResponse(),
            self.do_rpcrequest('ModifyDesktopSpec', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_desktop_spec_with_options_async(
        self,
        request: ecd_20200930_models.ModifyDesktopSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyDesktopSpecResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyDesktopSpecResponse(),
            await self.do_rpcrequest_async('ModifyDesktopSpec', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_desktop_spec(
        self,
        request: ecd_20200930_models.ModifyDesktopSpecRequest,
    ) -> ecd_20200930_models.ModifyDesktopSpecResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_desktop_spec_with_options(request, runtime)

    async def modify_desktop_spec_async(
        self,
        request: ecd_20200930_models.ModifyDesktopSpecRequest,
    ) -> ecd_20200930_models.ModifyDesktopSpecResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_desktop_spec_with_options_async(request, runtime)

    def modify_desktops_policy_group_with_options(
        self,
        request: ecd_20200930_models.ModifyDesktopsPolicyGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyDesktopsPolicyGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyDesktopsPolicyGroupResponse(),
            self.do_rpcrequest('ModifyDesktopsPolicyGroup', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_desktops_policy_group_with_options_async(
        self,
        request: ecd_20200930_models.ModifyDesktopsPolicyGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyDesktopsPolicyGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyDesktopsPolicyGroupResponse(),
            await self.do_rpcrequest_async('ModifyDesktopsPolicyGroup', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_desktops_policy_group(
        self,
        request: ecd_20200930_models.ModifyDesktopsPolicyGroupRequest,
    ) -> ecd_20200930_models.ModifyDesktopsPolicyGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_desktops_policy_group_with_options(request, runtime)

    async def modify_desktops_policy_group_async(
        self,
        request: ecd_20200930_models.ModifyDesktopsPolicyGroupRequest,
    ) -> ecd_20200930_models.ModifyDesktopsPolicyGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_desktops_policy_group_with_options_async(request, runtime)

    def modify_entitlement_with_options(
        self,
        request: ecd_20200930_models.ModifyEntitlementRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyEntitlementResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyEntitlementResponse(),
            self.do_rpcrequest('ModifyEntitlement', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_entitlement_with_options_async(
        self,
        request: ecd_20200930_models.ModifyEntitlementRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyEntitlementResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyEntitlementResponse(),
            await self.do_rpcrequest_async('ModifyEntitlement', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_entitlement(
        self,
        request: ecd_20200930_models.ModifyEntitlementRequest,
    ) -> ecd_20200930_models.ModifyEntitlementResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_entitlement_with_options(request, runtime)

    async def modify_entitlement_async(
        self,
        request: ecd_20200930_models.ModifyEntitlementRequest,
    ) -> ecd_20200930_models.ModifyEntitlementResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_entitlement_with_options_async(request, runtime)

    def modify_image_attribute_with_options(
        self,
        request: ecd_20200930_models.ModifyImageAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyImageAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyImageAttributeResponse(),
            self.do_rpcrequest('ModifyImageAttribute', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_image_attribute_with_options_async(
        self,
        request: ecd_20200930_models.ModifyImageAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyImageAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyImageAttributeResponse(),
            await self.do_rpcrequest_async('ModifyImageAttribute', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_image_attribute(
        self,
        request: ecd_20200930_models.ModifyImageAttributeRequest,
    ) -> ecd_20200930_models.ModifyImageAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_image_attribute_with_options(request, runtime)

    async def modify_image_attribute_async(
        self,
        request: ecd_20200930_models.ModifyImageAttributeRequest,
    ) -> ecd_20200930_models.ModifyImageAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_image_attribute_with_options_async(request, runtime)

    def modify_nasdefault_mount_target_with_options(
        self,
        request: ecd_20200930_models.ModifyNASDefaultMountTargetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyNASDefaultMountTargetResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyNASDefaultMountTargetResponse(),
            self.do_rpcrequest('ModifyNASDefaultMountTarget', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_nasdefault_mount_target_with_options_async(
        self,
        request: ecd_20200930_models.ModifyNASDefaultMountTargetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyNASDefaultMountTargetResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyNASDefaultMountTargetResponse(),
            await self.do_rpcrequest_async('ModifyNASDefaultMountTarget', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_nasdefault_mount_target(
        self,
        request: ecd_20200930_models.ModifyNASDefaultMountTargetRequest,
    ) -> ecd_20200930_models.ModifyNASDefaultMountTargetResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_nasdefault_mount_target_with_options(request, runtime)

    async def modify_nasdefault_mount_target_async(
        self,
        request: ecd_20200930_models.ModifyNASDefaultMountTargetRequest,
    ) -> ecd_20200930_models.ModifyNASDefaultMountTargetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_nasdefault_mount_target_with_options_async(request, runtime)

    def modify_network_package_with_options(
        self,
        request: ecd_20200930_models.ModifyNetworkPackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyNetworkPackageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyNetworkPackageResponse(),
            self.do_rpcrequest('ModifyNetworkPackage', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_network_package_with_options_async(
        self,
        request: ecd_20200930_models.ModifyNetworkPackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyNetworkPackageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyNetworkPackageResponse(),
            await self.do_rpcrequest_async('ModifyNetworkPackage', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_network_package(
        self,
        request: ecd_20200930_models.ModifyNetworkPackageRequest,
    ) -> ecd_20200930_models.ModifyNetworkPackageResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_network_package_with_options(request, runtime)

    async def modify_network_package_async(
        self,
        request: ecd_20200930_models.ModifyNetworkPackageRequest,
    ) -> ecd_20200930_models.ModifyNetworkPackageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_network_package_with_options_async(request, runtime)

    def modify_network_package_enabled_with_options(
        self,
        request: ecd_20200930_models.ModifyNetworkPackageEnabledRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyNetworkPackageEnabledResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyNetworkPackageEnabledResponse(),
            self.do_rpcrequest('ModifyNetworkPackageEnabled', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_network_package_enabled_with_options_async(
        self,
        request: ecd_20200930_models.ModifyNetworkPackageEnabledRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyNetworkPackageEnabledResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyNetworkPackageEnabledResponse(),
            await self.do_rpcrequest_async('ModifyNetworkPackageEnabled', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_network_package_enabled(
        self,
        request: ecd_20200930_models.ModifyNetworkPackageEnabledRequest,
    ) -> ecd_20200930_models.ModifyNetworkPackageEnabledResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_network_package_enabled_with_options(request, runtime)

    async def modify_network_package_enabled_async(
        self,
        request: ecd_20200930_models.ModifyNetworkPackageEnabledRequest,
    ) -> ecd_20200930_models.ModifyNetworkPackageEnabledResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_network_package_enabled_with_options_async(request, runtime)

    def modify_office_site_attribute_with_options(
        self,
        request: ecd_20200930_models.ModifyOfficeSiteAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyOfficeSiteAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyOfficeSiteAttributeResponse(),
            self.do_rpcrequest('ModifyOfficeSiteAttribute', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_office_site_attribute_with_options_async(
        self,
        request: ecd_20200930_models.ModifyOfficeSiteAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyOfficeSiteAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyOfficeSiteAttributeResponse(),
            await self.do_rpcrequest_async('ModifyOfficeSiteAttribute', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_office_site_attribute(
        self,
        request: ecd_20200930_models.ModifyOfficeSiteAttributeRequest,
    ) -> ecd_20200930_models.ModifyOfficeSiteAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_office_site_attribute_with_options(request, runtime)

    async def modify_office_site_attribute_async(
        self,
        request: ecd_20200930_models.ModifyOfficeSiteAttributeRequest,
    ) -> ecd_20200930_models.ModifyOfficeSiteAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_office_site_attribute_with_options_async(request, runtime)

    def modify_office_site_cross_desktop_access_with_options(
        self,
        request: ecd_20200930_models.ModifyOfficeSiteCrossDesktopAccessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyOfficeSiteCrossDesktopAccessResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyOfficeSiteCrossDesktopAccessResponse(),
            self.do_rpcrequest('ModifyOfficeSiteCrossDesktopAccess', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_office_site_cross_desktop_access_with_options_async(
        self,
        request: ecd_20200930_models.ModifyOfficeSiteCrossDesktopAccessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyOfficeSiteCrossDesktopAccessResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyOfficeSiteCrossDesktopAccessResponse(),
            await self.do_rpcrequest_async('ModifyOfficeSiteCrossDesktopAccess', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_office_site_cross_desktop_access(
        self,
        request: ecd_20200930_models.ModifyOfficeSiteCrossDesktopAccessRequest,
    ) -> ecd_20200930_models.ModifyOfficeSiteCrossDesktopAccessResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_office_site_cross_desktop_access_with_options(request, runtime)

    async def modify_office_site_cross_desktop_access_async(
        self,
        request: ecd_20200930_models.ModifyOfficeSiteCrossDesktopAccessRequest,
    ) -> ecd_20200930_models.ModifyOfficeSiteCrossDesktopAccessResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_office_site_cross_desktop_access_with_options_async(request, runtime)

    def modify_office_site_mfa_enabled_with_options(
        self,
        request: ecd_20200930_models.ModifyOfficeSiteMfaEnabledRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyOfficeSiteMfaEnabledResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyOfficeSiteMfaEnabledResponse(),
            self.do_rpcrequest('ModifyOfficeSiteMfaEnabled', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_office_site_mfa_enabled_with_options_async(
        self,
        request: ecd_20200930_models.ModifyOfficeSiteMfaEnabledRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyOfficeSiteMfaEnabledResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyOfficeSiteMfaEnabledResponse(),
            await self.do_rpcrequest_async('ModifyOfficeSiteMfaEnabled', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_office_site_mfa_enabled(
        self,
        request: ecd_20200930_models.ModifyOfficeSiteMfaEnabledRequest,
    ) -> ecd_20200930_models.ModifyOfficeSiteMfaEnabledResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_office_site_mfa_enabled_with_options(request, runtime)

    async def modify_office_site_mfa_enabled_async(
        self,
        request: ecd_20200930_models.ModifyOfficeSiteMfaEnabledRequest,
    ) -> ecd_20200930_models.ModifyOfficeSiteMfaEnabledResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_office_site_mfa_enabled_with_options_async(request, runtime)

    def modify_operate_vul_with_options(
        self,
        request: ecd_20200930_models.ModifyOperateVulRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyOperateVulResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyOperateVulResponse(),
            self.do_rpcrequest('ModifyOperateVul', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_operate_vul_with_options_async(
        self,
        request: ecd_20200930_models.ModifyOperateVulRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyOperateVulResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyOperateVulResponse(),
            await self.do_rpcrequest_async('ModifyOperateVul', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_operate_vul(
        self,
        request: ecd_20200930_models.ModifyOperateVulRequest,
    ) -> ecd_20200930_models.ModifyOperateVulResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_operate_vul_with_options(request, runtime)

    async def modify_operate_vul_async(
        self,
        request: ecd_20200930_models.ModifyOperateVulRequest,
    ) -> ecd_20200930_models.ModifyOperateVulResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_operate_vul_with_options_async(request, runtime)

    def modify_policy_group_with_options(
        self,
        request: ecd_20200930_models.ModifyPolicyGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyPolicyGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyPolicyGroupResponse(),
            self.do_rpcrequest('ModifyPolicyGroup', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_policy_group_with_options_async(
        self,
        request: ecd_20200930_models.ModifyPolicyGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyPolicyGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyPolicyGroupResponse(),
            await self.do_rpcrequest_async('ModifyPolicyGroup', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_policy_group(
        self,
        request: ecd_20200930_models.ModifyPolicyGroupRequest,
    ) -> ecd_20200930_models.ModifyPolicyGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_policy_group_with_options(request, runtime)

    async def modify_policy_group_async(
        self,
        request: ecd_20200930_models.ModifyPolicyGroupRequest,
    ) -> ecd_20200930_models.ModifyPolicyGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_policy_group_with_options_async(request, runtime)

    def modify_scale_strategy_with_options(
        self,
        request: ecd_20200930_models.ModifyScaleStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyScaleStrategyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyScaleStrategyResponse(),
            self.do_rpcrequest('ModifyScaleStrategy', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_scale_strategy_with_options_async(
        self,
        request: ecd_20200930_models.ModifyScaleStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyScaleStrategyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyScaleStrategyResponse(),
            await self.do_rpcrequest_async('ModifyScaleStrategy', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_scale_strategy(
        self,
        request: ecd_20200930_models.ModifyScaleStrategyRequest,
    ) -> ecd_20200930_models.ModifyScaleStrategyResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_scale_strategy_with_options(request, runtime)

    async def modify_scale_strategy_async(
        self,
        request: ecd_20200930_models.ModifyScaleStrategyRequest,
    ) -> ecd_20200930_models.ModifyScaleStrategyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_scale_strategy_with_options_async(request, runtime)

    def modify_user_to_desktop_group_with_options(
        self,
        request: ecd_20200930_models.ModifyUserToDesktopGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyUserToDesktopGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyUserToDesktopGroupResponse(),
            self.do_rpcrequest('ModifyUserToDesktopGroup', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_user_to_desktop_group_with_options_async(
        self,
        request: ecd_20200930_models.ModifyUserToDesktopGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyUserToDesktopGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyUserToDesktopGroupResponse(),
            await self.do_rpcrequest_async('ModifyUserToDesktopGroup', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_user_to_desktop_group(
        self,
        request: ecd_20200930_models.ModifyUserToDesktopGroupRequest,
    ) -> ecd_20200930_models.ModifyUserToDesktopGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_user_to_desktop_group_with_options(request, runtime)

    async def modify_user_to_desktop_group_async(
        self,
        request: ecd_20200930_models.ModifyUserToDesktopGroupRequest,
    ) -> ecd_20200930_models.ModifyUserToDesktopGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_user_to_desktop_group_with_options_async(request, runtime)

    def operate_vuls_with_options(
        self,
        request: ecd_20200930_models.OperateVulsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.OperateVulsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.OperateVulsResponse(),
            self.do_rpcrequest('OperateVuls', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def operate_vuls_with_options_async(
        self,
        request: ecd_20200930_models.OperateVulsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.OperateVulsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.OperateVulsResponse(),
            await self.do_rpcrequest_async('OperateVuls', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def operate_vuls(
        self,
        request: ecd_20200930_models.OperateVulsRequest,
    ) -> ecd_20200930_models.OperateVulsResponse:
        runtime = util_models.RuntimeOptions()
        return self.operate_vuls_with_options(request, runtime)

    async def operate_vuls_async(
        self,
        request: ecd_20200930_models.OperateVulsRequest,
    ) -> ecd_20200930_models.OperateVulsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.operate_vuls_with_options_async(request, runtime)

    def pay_order_callback_with_options(
        self,
        request: ecd_20200930_models.PayOrderCallbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.PayOrderCallbackResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.PayOrderCallbackResponse(),
            self.do_rpcrequest('PayOrderCallback', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def pay_order_callback_with_options_async(
        self,
        request: ecd_20200930_models.PayOrderCallbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.PayOrderCallbackResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.PayOrderCallbackResponse(),
            await self.do_rpcrequest_async('PayOrderCallback', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def pay_order_callback(
        self,
        request: ecd_20200930_models.PayOrderCallbackRequest,
    ) -> ecd_20200930_models.PayOrderCallbackResponse:
        runtime = util_models.RuntimeOptions()
        return self.pay_order_callback_with_options(request, runtime)

    async def pay_order_callback_async(
        self,
        request: ecd_20200930_models.PayOrderCallbackRequest,
    ) -> ecd_20200930_models.PayOrderCallbackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.pay_order_callback_with_options_async(request, runtime)

    def reboot_desktops_with_options(
        self,
        request: ecd_20200930_models.RebootDesktopsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.RebootDesktopsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.RebootDesktopsResponse(),
            self.do_rpcrequest('RebootDesktops', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def reboot_desktops_with_options_async(
        self,
        request: ecd_20200930_models.RebootDesktopsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.RebootDesktopsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.RebootDesktopsResponse(),
            await self.do_rpcrequest_async('RebootDesktops', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def reboot_desktops(
        self,
        request: ecd_20200930_models.RebootDesktopsRequest,
    ) -> ecd_20200930_models.RebootDesktopsResponse:
        runtime = util_models.RuntimeOptions()
        return self.reboot_desktops_with_options(request, runtime)

    async def reboot_desktops_async(
        self,
        request: ecd_20200930_models.RebootDesktopsRequest,
    ) -> ecd_20200930_models.RebootDesktopsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reboot_desktops_with_options_async(request, runtime)

    def rebuild_desktops_with_options(
        self,
        request: ecd_20200930_models.RebuildDesktopsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.RebuildDesktopsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.RebuildDesktopsResponse(),
            self.do_rpcrequest('RebuildDesktops', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def rebuild_desktops_with_options_async(
        self,
        request: ecd_20200930_models.RebuildDesktopsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.RebuildDesktopsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.RebuildDesktopsResponse(),
            await self.do_rpcrequest_async('RebuildDesktops', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def rebuild_desktops(
        self,
        request: ecd_20200930_models.RebuildDesktopsRequest,
    ) -> ecd_20200930_models.RebuildDesktopsResponse:
        runtime = util_models.RuntimeOptions()
        return self.rebuild_desktops_with_options(request, runtime)

    async def rebuild_desktops_async(
        self,
        request: ecd_20200930_models.RebuildDesktopsRequest,
    ) -> ecd_20200930_models.RebuildDesktopsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.rebuild_desktops_with_options_async(request, runtime)

    def recreate_desktop_group_with_options(
        self,
        request: ecd_20200930_models.RecreateDesktopGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.RecreateDesktopGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.RecreateDesktopGroupResponse(),
            self.do_rpcrequest('RecreateDesktopGroup', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def recreate_desktop_group_with_options_async(
        self,
        request: ecd_20200930_models.RecreateDesktopGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.RecreateDesktopGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.RecreateDesktopGroupResponse(),
            await self.do_rpcrequest_async('RecreateDesktopGroup', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def recreate_desktop_group(
        self,
        request: ecd_20200930_models.RecreateDesktopGroupRequest,
    ) -> ecd_20200930_models.RecreateDesktopGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.recreate_desktop_group_with_options(request, runtime)

    async def recreate_desktop_group_async(
        self,
        request: ecd_20200930_models.RecreateDesktopGroupRequest,
    ) -> ecd_20200930_models.RecreateDesktopGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recreate_desktop_group_with_options_async(request, runtime)

    def remove_user_from_desktop_group_with_options(
        self,
        request: ecd_20200930_models.RemoveUserFromDesktopGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.RemoveUserFromDesktopGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.RemoveUserFromDesktopGroupResponse(),
            self.do_rpcrequest('RemoveUserFromDesktopGroup', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_user_from_desktop_group_with_options_async(
        self,
        request: ecd_20200930_models.RemoveUserFromDesktopGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.RemoveUserFromDesktopGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.RemoveUserFromDesktopGroupResponse(),
            await self.do_rpcrequest_async('RemoveUserFromDesktopGroup', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_user_from_desktop_group(
        self,
        request: ecd_20200930_models.RemoveUserFromDesktopGroupRequest,
    ) -> ecd_20200930_models.RemoveUserFromDesktopGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_user_from_desktop_group_with_options(request, runtime)

    async def remove_user_from_desktop_group_async(
        self,
        request: ecd_20200930_models.RemoveUserFromDesktopGroupRequest,
    ) -> ecd_20200930_models.RemoveUserFromDesktopGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_user_from_desktop_group_with_options_async(request, runtime)

    def renew_desktops_with_options(
        self,
        request: ecd_20200930_models.RenewDesktopsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.RenewDesktopsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.RenewDesktopsResponse(),
            self.do_rpcrequest('RenewDesktops', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def renew_desktops_with_options_async(
        self,
        request: ecd_20200930_models.RenewDesktopsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.RenewDesktopsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.RenewDesktopsResponse(),
            await self.do_rpcrequest_async('RenewDesktops', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def renew_desktops(
        self,
        request: ecd_20200930_models.RenewDesktopsRequest,
    ) -> ecd_20200930_models.RenewDesktopsResponse:
        runtime = util_models.RuntimeOptions()
        return self.renew_desktops_with_options(request, runtime)

    async def renew_desktops_async(
        self,
        request: ecd_20200930_models.RenewDesktopsRequest,
    ) -> ecd_20200930_models.RenewDesktopsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.renew_desktops_with_options_async(request, runtime)

    def reset_nasdefault_mount_target_with_options(
        self,
        request: ecd_20200930_models.ResetNASDefaultMountTargetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ResetNASDefaultMountTargetResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ResetNASDefaultMountTargetResponse(),
            self.do_rpcrequest('ResetNASDefaultMountTarget', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def reset_nasdefault_mount_target_with_options_async(
        self,
        request: ecd_20200930_models.ResetNASDefaultMountTargetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ResetNASDefaultMountTargetResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ResetNASDefaultMountTargetResponse(),
            await self.do_rpcrequest_async('ResetNASDefaultMountTarget', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def reset_nasdefault_mount_target(
        self,
        request: ecd_20200930_models.ResetNASDefaultMountTargetRequest,
    ) -> ecd_20200930_models.ResetNASDefaultMountTargetResponse:
        runtime = util_models.RuntimeOptions()
        return self.reset_nasdefault_mount_target_with_options(request, runtime)

    async def reset_nasdefault_mount_target_async(
        self,
        request: ecd_20200930_models.ResetNASDefaultMountTargetRequest,
    ) -> ecd_20200930_models.ResetNASDefaultMountTargetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_nasdefault_mount_target_with_options_async(request, runtime)

    def reset_snapshot_with_options(
        self,
        request: ecd_20200930_models.ResetSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ResetSnapshotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ResetSnapshotResponse(),
            self.do_rpcrequest('ResetSnapshot', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def reset_snapshot_with_options_async(
        self,
        request: ecd_20200930_models.ResetSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ResetSnapshotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ResetSnapshotResponse(),
            await self.do_rpcrequest_async('ResetSnapshot', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def reset_snapshot(
        self,
        request: ecd_20200930_models.ResetSnapshotRequest,
    ) -> ecd_20200930_models.ResetSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return self.reset_snapshot_with_options(request, runtime)

    async def reset_snapshot_async(
        self,
        request: ecd_20200930_models.ResetSnapshotRequest,
    ) -> ecd_20200930_models.ResetSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_snapshot_with_options_async(request, runtime)

    def rollback_susp_event_quara_file_with_options(
        self,
        request: ecd_20200930_models.RollbackSuspEventQuaraFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.RollbackSuspEventQuaraFileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.RollbackSuspEventQuaraFileResponse(),
            self.do_rpcrequest('RollbackSuspEventQuaraFile', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def rollback_susp_event_quara_file_with_options_async(
        self,
        request: ecd_20200930_models.RollbackSuspEventQuaraFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.RollbackSuspEventQuaraFileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.RollbackSuspEventQuaraFileResponse(),
            await self.do_rpcrequest_async('RollbackSuspEventQuaraFile', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def rollback_susp_event_quara_file(
        self,
        request: ecd_20200930_models.RollbackSuspEventQuaraFileRequest,
    ) -> ecd_20200930_models.RollbackSuspEventQuaraFileResponse:
        runtime = util_models.RuntimeOptions()
        return self.rollback_susp_event_quara_file_with_options(request, runtime)

    async def rollback_susp_event_quara_file_async(
        self,
        request: ecd_20200930_models.RollbackSuspEventQuaraFileRequest,
    ) -> ecd_20200930_models.RollbackSuspEventQuaraFileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.rollback_susp_event_quara_file_with_options_async(request, runtime)

    def run_command_with_options(
        self,
        request: ecd_20200930_models.RunCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.RunCommandResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.RunCommandResponse(),
            self.do_rpcrequest('RunCommand', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def run_command_with_options_async(
        self,
        request: ecd_20200930_models.RunCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.RunCommandResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.RunCommandResponse(),
            await self.do_rpcrequest_async('RunCommand', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def run_command(
        self,
        request: ecd_20200930_models.RunCommandRequest,
    ) -> ecd_20200930_models.RunCommandResponse:
        runtime = util_models.RuntimeOptions()
        return self.run_command_with_options(request, runtime)

    async def run_command_async(
        self,
        request: ecd_20200930_models.RunCommandRequest,
    ) -> ecd_20200930_models.RunCommandResponse:
        runtime = util_models.RuntimeOptions()
        return await self.run_command_with_options_async(request, runtime)

    def set_directory_sso_status_with_options(
        self,
        request: ecd_20200930_models.SetDirectorySsoStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.SetDirectorySsoStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.SetDirectorySsoStatusResponse(),
            self.do_rpcrequest('SetDirectorySsoStatus', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_directory_sso_status_with_options_async(
        self,
        request: ecd_20200930_models.SetDirectorySsoStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.SetDirectorySsoStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.SetDirectorySsoStatusResponse(),
            await self.do_rpcrequest_async('SetDirectorySsoStatus', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_directory_sso_status(
        self,
        request: ecd_20200930_models.SetDirectorySsoStatusRequest,
    ) -> ecd_20200930_models.SetDirectorySsoStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_directory_sso_status_with_options(request, runtime)

    async def set_directory_sso_status_async(
        self,
        request: ecd_20200930_models.SetDirectorySsoStatusRequest,
    ) -> ecd_20200930_models.SetDirectorySsoStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_directory_sso_status_with_options_async(request, runtime)

    def set_idp_metadata_with_options(
        self,
        request: ecd_20200930_models.SetIdpMetadataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.SetIdpMetadataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.SetIdpMetadataResponse(),
            self.do_rpcrequest('SetIdpMetadata', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_idp_metadata_with_options_async(
        self,
        request: ecd_20200930_models.SetIdpMetadataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.SetIdpMetadataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.SetIdpMetadataResponse(),
            await self.do_rpcrequest_async('SetIdpMetadata', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_idp_metadata(
        self,
        request: ecd_20200930_models.SetIdpMetadataRequest,
    ) -> ecd_20200930_models.SetIdpMetadataResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_idp_metadata_with_options(request, runtime)

    async def set_idp_metadata_async(
        self,
        request: ecd_20200930_models.SetIdpMetadataRequest,
    ) -> ecd_20200930_models.SetIdpMetadataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_idp_metadata_with_options_async(request, runtime)

    def set_office_site_sso_status_with_options(
        self,
        request: ecd_20200930_models.SetOfficeSiteSsoStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.SetOfficeSiteSsoStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.SetOfficeSiteSsoStatusResponse(),
            self.do_rpcrequest('SetOfficeSiteSsoStatus', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_office_site_sso_status_with_options_async(
        self,
        request: ecd_20200930_models.SetOfficeSiteSsoStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.SetOfficeSiteSsoStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.SetOfficeSiteSsoStatusResponse(),
            await self.do_rpcrequest_async('SetOfficeSiteSsoStatus', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_office_site_sso_status(
        self,
        request: ecd_20200930_models.SetOfficeSiteSsoStatusRequest,
    ) -> ecd_20200930_models.SetOfficeSiteSsoStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_office_site_sso_status_with_options(request, runtime)

    async def set_office_site_sso_status_async(
        self,
        request: ecd_20200930_models.SetOfficeSiteSsoStatusRequest,
    ) -> ecd_20200930_models.SetOfficeSiteSsoStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_office_site_sso_status_with_options_async(request, runtime)

    def start_desktops_with_options(
        self,
        request: ecd_20200930_models.StartDesktopsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.StartDesktopsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.StartDesktopsResponse(),
            self.do_rpcrequest('StartDesktops', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_desktops_with_options_async(
        self,
        request: ecd_20200930_models.StartDesktopsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.StartDesktopsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.StartDesktopsResponse(),
            await self.do_rpcrequest_async('StartDesktops', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_desktops(
        self,
        request: ecd_20200930_models.StartDesktopsRequest,
    ) -> ecd_20200930_models.StartDesktopsResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_desktops_with_options(request, runtime)

    async def start_desktops_async(
        self,
        request: ecd_20200930_models.StartDesktopsRequest,
    ) -> ecd_20200930_models.StartDesktopsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_desktops_with_options_async(request, runtime)

    def start_virus_scan_task_with_options(
        self,
        request: ecd_20200930_models.StartVirusScanTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.StartVirusScanTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.StartVirusScanTaskResponse(),
            self.do_rpcrequest('StartVirusScanTask', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_virus_scan_task_with_options_async(
        self,
        request: ecd_20200930_models.StartVirusScanTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.StartVirusScanTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.StartVirusScanTaskResponse(),
            await self.do_rpcrequest_async('StartVirusScanTask', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_virus_scan_task(
        self,
        request: ecd_20200930_models.StartVirusScanTaskRequest,
    ) -> ecd_20200930_models.StartVirusScanTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_virus_scan_task_with_options(request, runtime)

    async def start_virus_scan_task_async(
        self,
        request: ecd_20200930_models.StartVirusScanTaskRequest,
    ) -> ecd_20200930_models.StartVirusScanTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_virus_scan_task_with_options_async(request, runtime)

    def stop_desktops_with_options(
        self,
        request: ecd_20200930_models.StopDesktopsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.StopDesktopsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.StopDesktopsResponse(),
            self.do_rpcrequest('StopDesktops', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def stop_desktops_with_options_async(
        self,
        request: ecd_20200930_models.StopDesktopsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.StopDesktopsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.StopDesktopsResponse(),
            await self.do_rpcrequest_async('StopDesktops', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_desktops(
        self,
        request: ecd_20200930_models.StopDesktopsRequest,
    ) -> ecd_20200930_models.StopDesktopsResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_desktops_with_options(request, runtime)

    async def stop_desktops_async(
        self,
        request: ecd_20200930_models.StopDesktopsRequest,
    ) -> ecd_20200930_models.StopDesktopsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_desktops_with_options_async(request, runtime)

    def stop_invocation_with_options(
        self,
        request: ecd_20200930_models.StopInvocationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.StopInvocationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.StopInvocationResponse(),
            self.do_rpcrequest('StopInvocation', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def stop_invocation_with_options_async(
        self,
        request: ecd_20200930_models.StopInvocationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.StopInvocationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.StopInvocationResponse(),
            await self.do_rpcrequest_async('StopInvocation', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_invocation(
        self,
        request: ecd_20200930_models.StopInvocationRequest,
    ) -> ecd_20200930_models.StopInvocationResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_invocation_with_options(request, runtime)

    async def stop_invocation_async(
        self,
        request: ecd_20200930_models.StopInvocationRequest,
    ) -> ecd_20200930_models.StopInvocationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_invocation_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: ecd_20200930_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.TagResourcesResponse(),
            self.do_rpcrequest('TagResources', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: ecd_20200930_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.TagResourcesResponse(),
            await self.do_rpcrequest_async('TagResources', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def tag_resources(
        self,
        request: ecd_20200930_models.TagResourcesRequest,
    ) -> ecd_20200930_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: ecd_20200930_models.TagResourcesRequest,
    ) -> ecd_20200930_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def unlock_virtual_mfadevice_with_options(
        self,
        request: ecd_20200930_models.UnlockVirtualMFADeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.UnlockVirtualMFADeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.UnlockVirtualMFADeviceResponse(),
            self.do_rpcrequest('UnlockVirtualMFADevice', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def unlock_virtual_mfadevice_with_options_async(
        self,
        request: ecd_20200930_models.UnlockVirtualMFADeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.UnlockVirtualMFADeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.UnlockVirtualMFADeviceResponse(),
            await self.do_rpcrequest_async('UnlockVirtualMFADevice', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def unlock_virtual_mfadevice(
        self,
        request: ecd_20200930_models.UnlockVirtualMFADeviceRequest,
    ) -> ecd_20200930_models.UnlockVirtualMFADeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.unlock_virtual_mfadevice_with_options(request, runtime)

    async def unlock_virtual_mfadevice_async(
        self,
        request: ecd_20200930_models.UnlockVirtualMFADeviceRequest,
    ) -> ecd_20200930_models.UnlockVirtualMFADeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unlock_virtual_mfadevice_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: ecd_20200930_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.UntagResourcesResponse(),
            self.do_rpcrequest('UntagResources', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: ecd_20200930_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.UntagResourcesResponse(),
            await self.do_rpcrequest_async('UntagResources', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def untag_resources(
        self,
        request: ecd_20200930_models.UntagResourcesRequest,
    ) -> ecd_20200930_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: ecd_20200930_models.UntagResourcesRequest,
    ) -> ecd_20200930_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)
