# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_mpserverless20190615 import models as mpserverless_20190615_models
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
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('mpserverless', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def run_function_with_options(
        self,
        request: mpserverless_20190615_models.RunFunctionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.RunFunctionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.RunFunctionResponse(),
            self.do_rpcrequest('RunFunction', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def run_function_with_options_async(
        self,
        request: mpserverless_20190615_models.RunFunctionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.RunFunctionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.RunFunctionResponse(),
            await self.do_rpcrequest_async('RunFunction', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def run_function(
        self,
        request: mpserverless_20190615_models.RunFunctionRequest,
    ) -> mpserverless_20190615_models.RunFunctionResponse:
        runtime = util_models.RuntimeOptions()
        return self.run_function_with_options(request, runtime)

    async def run_function_async(
        self,
        request: mpserverless_20190615_models.RunFunctionRequest,
    ) -> mpserverless_20190615_models.RunFunctionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.run_function_with_options_async(request, runtime)

    def list_function_with_options(
        self,
        request: mpserverless_20190615_models.ListFunctionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.ListFunctionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.ListFunctionResponse(),
            self.do_rpcrequest('ListFunction', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_function_with_options_async(
        self,
        request: mpserverless_20190615_models.ListFunctionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.ListFunctionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.ListFunctionResponse(),
            await self.do_rpcrequest_async('ListFunction', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_function(
        self,
        request: mpserverless_20190615_models.ListFunctionRequest,
    ) -> mpserverless_20190615_models.ListFunctionResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_function_with_options(request, runtime)

    async def list_function_async(
        self,
        request: mpserverless_20190615_models.ListFunctionRequest,
    ) -> mpserverless_20190615_models.ListFunctionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_function_with_options_async(request, runtime)

    def get_web_hosting_certificate_detail_with_options(
        self,
        request: mpserverless_20190615_models.GetWebHostingCertificateDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.GetWebHostingCertificateDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.GetWebHostingCertificateDetailResponse(),
            self.do_rpcrequest('GetWebHostingCertificateDetail', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_web_hosting_certificate_detail_with_options_async(
        self,
        request: mpserverless_20190615_models.GetWebHostingCertificateDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.GetWebHostingCertificateDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.GetWebHostingCertificateDetailResponse(),
            await self.do_rpcrequest_async('GetWebHostingCertificateDetail', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_web_hosting_certificate_detail(
        self,
        request: mpserverless_20190615_models.GetWebHostingCertificateDetailRequest,
    ) -> mpserverless_20190615_models.GetWebHostingCertificateDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_web_hosting_certificate_detail_with_options(request, runtime)

    async def get_web_hosting_certificate_detail_async(
        self,
        request: mpserverless_20190615_models.GetWebHostingCertificateDetailRequest,
    ) -> mpserverless_20190615_models.GetWebHostingCertificateDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_web_hosting_certificate_detail_with_options_async(request, runtime)

    def update_space_with_options(
        self,
        request: mpserverless_20190615_models.UpdateSpaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.UpdateSpaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.UpdateSpaceResponse(),
            self.do_rpcrequest('UpdateSpace', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_space_with_options_async(
        self,
        request: mpserverless_20190615_models.UpdateSpaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.UpdateSpaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.UpdateSpaceResponse(),
            await self.do_rpcrequest_async('UpdateSpace', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_space(
        self,
        request: mpserverless_20190615_models.UpdateSpaceRequest,
    ) -> mpserverless_20190615_models.UpdateSpaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_space_with_options(request, runtime)

    async def update_space_async(
        self,
        request: mpserverless_20190615_models.UpdateSpaceRequest,
    ) -> mpserverless_20190615_models.UpdateSpaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_space_with_options_async(request, runtime)

    def save_web_hosting_custom_domain_config_with_options(
        self,
        request: mpserverless_20190615_models.SaveWebHostingCustomDomainConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.SaveWebHostingCustomDomainConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.SaveWebHostingCustomDomainConfigResponse(),
            self.do_rpcrequest('SaveWebHostingCustomDomainConfig', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def save_web_hosting_custom_domain_config_with_options_async(
        self,
        request: mpserverless_20190615_models.SaveWebHostingCustomDomainConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.SaveWebHostingCustomDomainConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.SaveWebHostingCustomDomainConfigResponse(),
            await self.do_rpcrequest_async('SaveWebHostingCustomDomainConfig', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def save_web_hosting_custom_domain_config(
        self,
        request: mpserverless_20190615_models.SaveWebHostingCustomDomainConfigRequest,
    ) -> mpserverless_20190615_models.SaveWebHostingCustomDomainConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.save_web_hosting_custom_domain_config_with_options(request, runtime)

    async def save_web_hosting_custom_domain_config_async(
        self,
        request: mpserverless_20190615_models.SaveWebHostingCustomDomainConfigRequest,
    ) -> mpserverless_20190615_models.SaveWebHostingCustomDomainConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_web_hosting_custom_domain_config_with_options_async(request, runtime)

    def list_function_spec_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.ListFunctionSpecResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            mpserverless_20190615_models.ListFunctionSpecResponse(),
            self.do_rpcrequest('ListFunctionSpec', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_function_spec_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.ListFunctionSpecResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            mpserverless_20190615_models.ListFunctionSpecResponse(),
            await self.do_rpcrequest_async('ListFunctionSpec', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_function_spec(self) -> mpserverless_20190615_models.ListFunctionSpecResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_function_spec_with_options(runtime)

    async def list_function_spec_async(self) -> mpserverless_20190615_models.ListFunctionSpecResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_function_spec_with_options_async(runtime)

    def delete_wechat_open_platform_config_with_options(
        self,
        request: mpserverless_20190615_models.DeleteWechatOpenPlatformConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.DeleteWechatOpenPlatformConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.DeleteWechatOpenPlatformConfigResponse(),
            self.do_rpcrequest('DeleteWechatOpenPlatformConfig', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_wechat_open_platform_config_with_options_async(
        self,
        request: mpserverless_20190615_models.DeleteWechatOpenPlatformConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.DeleteWechatOpenPlatformConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.DeleteWechatOpenPlatformConfigResponse(),
            await self.do_rpcrequest_async('DeleteWechatOpenPlatformConfig', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_wechat_open_platform_config(
        self,
        request: mpserverless_20190615_models.DeleteWechatOpenPlatformConfigRequest,
    ) -> mpserverless_20190615_models.DeleteWechatOpenPlatformConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_wechat_open_platform_config_with_options(request, runtime)

    async def delete_wechat_open_platform_config_async(
        self,
        request: mpserverless_20190615_models.DeleteWechatOpenPlatformConfigRequest,
    ) -> mpserverless_20190615_models.DeleteWechatOpenPlatformConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_wechat_open_platform_config_with_options_async(request, runtime)

    def create_space_with_options(
        self,
        request: mpserverless_20190615_models.CreateSpaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.CreateSpaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.CreateSpaceResponse(),
            self.do_rpcrequest('CreateSpace', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_space_with_options_async(
        self,
        request: mpserverless_20190615_models.CreateSpaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.CreateSpaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.CreateSpaceResponse(),
            await self.do_rpcrequest_async('CreateSpace', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_space(
        self,
        request: mpserverless_20190615_models.CreateSpaceRequest,
    ) -> mpserverless_20190615_models.CreateSpaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_space_with_options(request, runtime)

    async def create_space_async(
        self,
        request: mpserverless_20190615_models.CreateSpaceRequest,
    ) -> mpserverless_20190615_models.CreateSpaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_space_with_options_async(request, runtime)

    def open_product_with_options(
        self,
        request: mpserverless_20190615_models.OpenProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.OpenProductResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.OpenProductResponse(),
            self.do_rpcrequest('OpenProduct', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def open_product_with_options_async(
        self,
        request: mpserverless_20190615_models.OpenProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.OpenProductResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.OpenProductResponse(),
            await self.do_rpcrequest_async('OpenProduct', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def open_product(
        self,
        request: mpserverless_20190615_models.OpenProductRequest,
    ) -> mpserverless_20190615_models.OpenProductResponse:
        runtime = util_models.RuntimeOptions()
        return self.open_product_with_options(request, runtime)

    async def open_product_async(
        self,
        request: mpserverless_20190615_models.OpenProductRequest,
    ) -> mpserverless_20190615_models.OpenProductResponse:
        runtime = util_models.RuntimeOptions()
        return await self.open_product_with_options_async(request, runtime)

    def open_service_with_options(
        self,
        request: mpserverless_20190615_models.OpenServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.OpenServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.OpenServiceResponse(),
            self.do_rpcrequest('OpenService', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def open_service_with_options_async(
        self,
        request: mpserverless_20190615_models.OpenServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.OpenServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.OpenServiceResponse(),
            await self.do_rpcrequest_async('OpenService', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def open_service(
        self,
        request: mpserverless_20190615_models.OpenServiceRequest,
    ) -> mpserverless_20190615_models.OpenServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.open_service_with_options(request, runtime)

    async def open_service_async(
        self,
        request: mpserverless_20190615_models.OpenServiceRequest,
    ) -> mpserverless_20190615_models.OpenServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.open_service_with_options_async(request, runtime)

    def delete_space_with_options(
        self,
        request: mpserverless_20190615_models.DeleteSpaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.DeleteSpaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.DeleteSpaceResponse(),
            self.do_rpcrequest('DeleteSpace', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_space_with_options_async(
        self,
        request: mpserverless_20190615_models.DeleteSpaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.DeleteSpaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.DeleteSpaceResponse(),
            await self.do_rpcrequest_async('DeleteSpace', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_space(
        self,
        request: mpserverless_20190615_models.DeleteSpaceRequest,
    ) -> mpserverless_20190615_models.DeleteSpaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_space_with_options(request, runtime)

    async def delete_space_async(
        self,
        request: mpserverless_20190615_models.DeleteSpaceRequest,
    ) -> mpserverless_20190615_models.DeleteSpaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_space_with_options_async(request, runtime)

    def delete_ant_open_platform_config_with_options(
        self,
        request: mpserverless_20190615_models.DeleteAntOpenPlatformConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.DeleteAntOpenPlatformConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.DeleteAntOpenPlatformConfigResponse(),
            self.do_rpcrequest('DeleteAntOpenPlatformConfig', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_ant_open_platform_config_with_options_async(
        self,
        request: mpserverless_20190615_models.DeleteAntOpenPlatformConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.DeleteAntOpenPlatformConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.DeleteAntOpenPlatformConfigResponse(),
            await self.do_rpcrequest_async('DeleteAntOpenPlatformConfig', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_ant_open_platform_config(
        self,
        request: mpserverless_20190615_models.DeleteAntOpenPlatformConfigRequest,
    ) -> mpserverless_20190615_models.DeleteAntOpenPlatformConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_ant_open_platform_config_with_options(request, runtime)

    async def delete_ant_open_platform_config_async(
        self,
        request: mpserverless_20190615_models.DeleteAntOpenPlatformConfigRequest,
    ) -> mpserverless_20190615_models.DeleteAntOpenPlatformConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_ant_open_platform_config_with_options_async(request, runtime)

    def describe_fcopen_status_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.DescribeFCOpenStatusResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            mpserverless_20190615_models.DescribeFCOpenStatusResponse(),
            self.do_rpcrequest('DescribeFCOpenStatus', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_fcopen_status_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.DescribeFCOpenStatusResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            mpserverless_20190615_models.DescribeFCOpenStatusResponse(),
            await self.do_rpcrequest_async('DescribeFCOpenStatus', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_fcopen_status(self) -> mpserverless_20190615_models.DescribeFCOpenStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_fcopen_status_with_options(runtime)

    async def describe_fcopen_status_async(self) -> mpserverless_20190615_models.DescribeFCOpenStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_fcopen_status_with_options_async(runtime)

    def describe_file_upload_signed_url_with_options(
        self,
        request: mpserverless_20190615_models.DescribeFileUploadSignedUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.DescribeFileUploadSignedUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.DescribeFileUploadSignedUrlResponse(),
            self.do_rpcrequest('DescribeFileUploadSignedUrl', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_file_upload_signed_url_with_options_async(
        self,
        request: mpserverless_20190615_models.DescribeFileUploadSignedUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.DescribeFileUploadSignedUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.DescribeFileUploadSignedUrlResponse(),
            await self.do_rpcrequest_async('DescribeFileUploadSignedUrl', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_file_upload_signed_url(
        self,
        request: mpserverless_20190615_models.DescribeFileUploadSignedUrlRequest,
    ) -> mpserverless_20190615_models.DescribeFileUploadSignedUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_file_upload_signed_url_with_options(request, runtime)

    async def describe_file_upload_signed_url_async(
        self,
        request: mpserverless_20190615_models.DescribeFileUploadSignedUrlRequest,
    ) -> mpserverless_20190615_models.DescribeFileUploadSignedUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_file_upload_signed_url_with_options_async(request, runtime)

    def delete_file_with_options(
        self,
        request: mpserverless_20190615_models.DeleteFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.DeleteFileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.DeleteFileResponse(),
            self.do_rpcrequest('DeleteFile', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_file_with_options_async(
        self,
        request: mpserverless_20190615_models.DeleteFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.DeleteFileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.DeleteFileResponse(),
            await self.do_rpcrequest_async('DeleteFile', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_file(
        self,
        request: mpserverless_20190615_models.DeleteFileRequest,
    ) -> mpserverless_20190615_models.DeleteFileResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_file_with_options(request, runtime)

    async def delete_file_async(
        self,
        request: mpserverless_20190615_models.DeleteFileRequest,
    ) -> mpserverless_20190615_models.DeleteFileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_file_with_options_async(request, runtime)

    def query_dbimport_task_status_with_options(
        self,
        request: mpserverless_20190615_models.QueryDBImportTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.QueryDBImportTaskStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.QueryDBImportTaskStatusResponse(),
            self.do_rpcrequest('QueryDBImportTaskStatus', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_dbimport_task_status_with_options_async(
        self,
        request: mpserverless_20190615_models.QueryDBImportTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.QueryDBImportTaskStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.QueryDBImportTaskStatusResponse(),
            await self.do_rpcrequest_async('QueryDBImportTaskStatus', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_dbimport_task_status(
        self,
        request: mpserverless_20190615_models.QueryDBImportTaskStatusRequest,
    ) -> mpserverless_20190615_models.QueryDBImportTaskStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_dbimport_task_status_with_options(request, runtime)

    async def query_dbimport_task_status_async(
        self,
        request: mpserverless_20190615_models.QueryDBImportTaskStatusRequest,
    ) -> mpserverless_20190615_models.QueryDBImportTaskStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_dbimport_task_status_with_options_async(request, runtime)

    def register_file_with_options(
        self,
        request: mpserverless_20190615_models.RegisterFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.RegisterFileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.RegisterFileResponse(),
            self.do_rpcrequest('RegisterFile', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def register_file_with_options_async(
        self,
        request: mpserverless_20190615_models.RegisterFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.RegisterFileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.RegisterFileResponse(),
            await self.do_rpcrequest_async('RegisterFile', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def register_file(
        self,
        request: mpserverless_20190615_models.RegisterFileRequest,
    ) -> mpserverless_20190615_models.RegisterFileResponse:
        runtime = util_models.RuntimeOptions()
        return self.register_file_with_options(request, runtime)

    async def register_file_async(
        self,
        request: mpserverless_20190615_models.RegisterFileRequest,
    ) -> mpserverless_20190615_models.RegisterFileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.register_file_with_options_async(request, runtime)

    def save_ant_open_platform_config_with_options(
        self,
        request: mpserverless_20190615_models.SaveAntOpenPlatformConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.SaveAntOpenPlatformConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.SaveAntOpenPlatformConfigResponse(),
            self.do_rpcrequest('SaveAntOpenPlatformConfig', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def save_ant_open_platform_config_with_options_async(
        self,
        request: mpserverless_20190615_models.SaveAntOpenPlatformConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.SaveAntOpenPlatformConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.SaveAntOpenPlatformConfigResponse(),
            await self.do_rpcrequest_async('SaveAntOpenPlatformConfig', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def save_ant_open_platform_config(
        self,
        request: mpserverless_20190615_models.SaveAntOpenPlatformConfigRequest,
    ) -> mpserverless_20190615_models.SaveAntOpenPlatformConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.save_ant_open_platform_config_with_options(request, runtime)

    async def save_ant_open_platform_config_async(
        self,
        request: mpserverless_20190615_models.SaveAntOpenPlatformConfigRequest,
    ) -> mpserverless_20190615_models.SaveAntOpenPlatformConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_ant_open_platform_config_with_options_async(request, runtime)

    def describe_function_with_options(
        self,
        request: mpserverless_20190615_models.DescribeFunctionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.DescribeFunctionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.DescribeFunctionResponse(),
            self.do_rpcrequest('DescribeFunction', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_function_with_options_async(
        self,
        request: mpserverless_20190615_models.DescribeFunctionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.DescribeFunctionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.DescribeFunctionResponse(),
            await self.do_rpcrequest_async('DescribeFunction', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_function(
        self,
        request: mpserverless_20190615_models.DescribeFunctionRequest,
    ) -> mpserverless_20190615_models.DescribeFunctionResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_function_with_options(request, runtime)

    async def describe_function_async(
        self,
        request: mpserverless_20190615_models.DescribeFunctionRequest,
    ) -> mpserverless_20190615_models.DescribeFunctionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_function_with_options_async(request, runtime)

    def open_web_hosting_service_with_options(
        self,
        request: mpserverless_20190615_models.OpenWebHostingServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.OpenWebHostingServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.OpenWebHostingServiceResponse(),
            self.do_rpcrequest('OpenWebHostingService', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def open_web_hosting_service_with_options_async(
        self,
        request: mpserverless_20190615_models.OpenWebHostingServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.OpenWebHostingServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.OpenWebHostingServiceResponse(),
            await self.do_rpcrequest_async('OpenWebHostingService', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def open_web_hosting_service(
        self,
        request: mpserverless_20190615_models.OpenWebHostingServiceRequest,
    ) -> mpserverless_20190615_models.OpenWebHostingServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.open_web_hosting_service_with_options(request, runtime)

    async def open_web_hosting_service_async(
        self,
        request: mpserverless_20190615_models.OpenWebHostingServiceRequest,
    ) -> mpserverless_20190615_models.OpenWebHostingServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.open_web_hosting_service_with_options_async(request, runtime)

    def describe_sms_sign_with_options(
        self,
        request: mpserverless_20190615_models.DescribeSmsSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.DescribeSmsSignResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.DescribeSmsSignResponse(),
            self.do_rpcrequest('DescribeSmsSign', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_sms_sign_with_options_async(
        self,
        request: mpserverless_20190615_models.DescribeSmsSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.DescribeSmsSignResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.DescribeSmsSignResponse(),
            await self.do_rpcrequest_async('DescribeSmsSign', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sms_sign(
        self,
        request: mpserverless_20190615_models.DescribeSmsSignRequest,
    ) -> mpserverless_20190615_models.DescribeSmsSignResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sms_sign_with_options(request, runtime)

    async def describe_sms_sign_async(
        self,
        request: mpserverless_20190615_models.DescribeSmsSignRequest,
    ) -> mpserverless_20190615_models.DescribeSmsSignResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sms_sign_with_options_async(request, runtime)

    def list_available_certificates_with_options(
        self,
        request: mpserverless_20190615_models.ListAvailableCertificatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.ListAvailableCertificatesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.ListAvailableCertificatesResponse(),
            self.do_rpcrequest('ListAvailableCertificates', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_available_certificates_with_options_async(
        self,
        request: mpserverless_20190615_models.ListAvailableCertificatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.ListAvailableCertificatesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.ListAvailableCertificatesResponse(),
            await self.do_rpcrequest_async('ListAvailableCertificates', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_available_certificates(
        self,
        request: mpserverless_20190615_models.ListAvailableCertificatesRequest,
    ) -> mpserverless_20190615_models.ListAvailableCertificatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_available_certificates_with_options(request, runtime)

    async def list_available_certificates_async(
        self,
        request: mpserverless_20190615_models.ListAvailableCertificatesRequest,
    ) -> mpserverless_20190615_models.ListAvailableCertificatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_available_certificates_with_options_async(request, runtime)

    def list_open_platform_config_with_options(
        self,
        request: mpserverless_20190615_models.ListOpenPlatformConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.ListOpenPlatformConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.ListOpenPlatformConfigResponse(),
            self.do_rpcrequest('ListOpenPlatformConfig', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_open_platform_config_with_options_async(
        self,
        request: mpserverless_20190615_models.ListOpenPlatformConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.ListOpenPlatformConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.ListOpenPlatformConfigResponse(),
            await self.do_rpcrequest_async('ListOpenPlatformConfig', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_open_platform_config(
        self,
        request: mpserverless_20190615_models.ListOpenPlatformConfigRequest,
    ) -> mpserverless_20190615_models.ListOpenPlatformConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_open_platform_config_with_options(request, runtime)

    async def list_open_platform_config_async(
        self,
        request: mpserverless_20190615_models.ListOpenPlatformConfigRequest,
    ) -> mpserverless_20190615_models.ListOpenPlatformConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_open_platform_config_with_options_async(request, runtime)

    def modify_web_hosting_config_with_options(
        self,
        request: mpserverless_20190615_models.ModifyWebHostingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.ModifyWebHostingConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.ModifyWebHostingConfigResponse(),
            self.do_rpcrequest('ModifyWebHostingConfig', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_web_hosting_config_with_options_async(
        self,
        request: mpserverless_20190615_models.ModifyWebHostingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.ModifyWebHostingConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.ModifyWebHostingConfigResponse(),
            await self.do_rpcrequest_async('ModifyWebHostingConfig', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_web_hosting_config(
        self,
        request: mpserverless_20190615_models.ModifyWebHostingConfigRequest,
    ) -> mpserverless_20190615_models.ModifyWebHostingConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_web_hosting_config_with_options(request, runtime)

    async def modify_web_hosting_config_async(
        self,
        request: mpserverless_20190615_models.ModifyWebHostingConfigRequest,
    ) -> mpserverless_20190615_models.ModifyWebHostingConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_web_hosting_config_with_options_async(request, runtime)

    def delete_sms_sign_with_options(
        self,
        request: mpserverless_20190615_models.DeleteSmsSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.DeleteSmsSignResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.DeleteSmsSignResponse(),
            self.do_rpcrequest('DeleteSmsSign', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_sms_sign_with_options_async(
        self,
        request: mpserverless_20190615_models.DeleteSmsSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.DeleteSmsSignResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.DeleteSmsSignResponse(),
            await self.do_rpcrequest_async('DeleteSmsSign', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_sms_sign(
        self,
        request: mpserverless_20190615_models.DeleteSmsSignRequest,
    ) -> mpserverless_20190615_models.DeleteSmsSignResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_sms_sign_with_options(request, runtime)

    async def delete_sms_sign_async(
        self,
        request: mpserverless_20190615_models.DeleteSmsSignRequest,
    ) -> mpserverless_20190615_models.DeleteSmsSignResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_sms_sign_with_options_async(request, runtime)

    def describe_sms_open_status_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.DescribeSmsOpenStatusResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            mpserverless_20190615_models.DescribeSmsOpenStatusResponse(),
            self.do_rpcrequest('DescribeSmsOpenStatus', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_sms_open_status_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.DescribeSmsOpenStatusResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            mpserverless_20190615_models.DescribeSmsOpenStatusResponse(),
            await self.do_rpcrequest_async('DescribeSmsOpenStatus', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sms_open_status(self) -> mpserverless_20190615_models.DescribeSmsOpenStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sms_open_status_with_options(runtime)

    async def describe_sms_open_status_async(self) -> mpserverless_20190615_models.DescribeSmsOpenStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sms_open_status_with_options_async(runtime)

    def list_space_with_options(
        self,
        request: mpserverless_20190615_models.ListSpaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.ListSpaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.ListSpaceResponse(),
            self.do_rpcrequest('ListSpace', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_space_with_options_async(
        self,
        request: mpserverless_20190615_models.ListSpaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.ListSpaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.ListSpaceResponse(),
            await self.do_rpcrequest_async('ListSpace', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_space(
        self,
        request: mpserverless_20190615_models.ListSpaceRequest,
    ) -> mpserverless_20190615_models.ListSpaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_space_with_options(request, runtime)

    async def list_space_async(
        self,
        request: mpserverless_20190615_models.ListSpaceRequest,
    ) -> mpserverless_20190615_models.ListSpaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_space_with_options_async(request, runtime)

    def delete_dbcollection_with_options(
        self,
        request: mpserverless_20190615_models.DeleteDBCollectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.DeleteDBCollectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.DeleteDBCollectionResponse(),
            self.do_rpcrequest('DeleteDBCollection', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_dbcollection_with_options_async(
        self,
        request: mpserverless_20190615_models.DeleteDBCollectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.DeleteDBCollectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.DeleteDBCollectionResponse(),
            await self.do_rpcrequest_async('DeleteDBCollection', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_dbcollection(
        self,
        request: mpserverless_20190615_models.DeleteDBCollectionRequest,
    ) -> mpserverless_20190615_models.DeleteDBCollectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_dbcollection_with_options(request, runtime)

    async def delete_dbcollection_async(
        self,
        request: mpserverless_20190615_models.DeleteDBCollectionRequest,
    ) -> mpserverless_20190615_models.DeleteDBCollectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_dbcollection_with_options_async(request, runtime)

    def create_function_deployment_with_options(
        self,
        request: mpserverless_20190615_models.CreateFunctionDeploymentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.CreateFunctionDeploymentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.CreateFunctionDeploymentResponse(),
            self.do_rpcrequest('CreateFunctionDeployment', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_function_deployment_with_options_async(
        self,
        request: mpserverless_20190615_models.CreateFunctionDeploymentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.CreateFunctionDeploymentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.CreateFunctionDeploymentResponse(),
            await self.do_rpcrequest_async('CreateFunctionDeployment', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_function_deployment(
        self,
        request: mpserverless_20190615_models.CreateFunctionDeploymentRequest,
    ) -> mpserverless_20190615_models.CreateFunctionDeploymentResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_function_deployment_with_options(request, runtime)

    async def create_function_deployment_async(
        self,
        request: mpserverless_20190615_models.CreateFunctionDeploymentRequest,
    ) -> mpserverless_20190615_models.CreateFunctionDeploymentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_function_deployment_with_options_async(request, runtime)

    def get_web_hosting_upload_credential_with_options(
        self,
        request: mpserverless_20190615_models.GetWebHostingUploadCredentialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.GetWebHostingUploadCredentialResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.GetWebHostingUploadCredentialResponse(),
            self.do_rpcrequest('GetWebHostingUploadCredential', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_web_hosting_upload_credential_with_options_async(
        self,
        request: mpserverless_20190615_models.GetWebHostingUploadCredentialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.GetWebHostingUploadCredentialResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.GetWebHostingUploadCredentialResponse(),
            await self.do_rpcrequest_async('GetWebHostingUploadCredential', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_web_hosting_upload_credential(
        self,
        request: mpserverless_20190615_models.GetWebHostingUploadCredentialRequest,
    ) -> mpserverless_20190615_models.GetWebHostingUploadCredentialResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_web_hosting_upload_credential_with_options(request, runtime)

    async def get_web_hosting_upload_credential_async(
        self,
        request: mpserverless_20190615_models.GetWebHostingUploadCredentialRequest,
    ) -> mpserverless_20190615_models.GetWebHostingUploadCredentialResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_web_hosting_upload_credential_with_options_async(request, runtime)

    def list_function_deployment_with_options(
        self,
        request: mpserverless_20190615_models.ListFunctionDeploymentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.ListFunctionDeploymentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.ListFunctionDeploymentResponse(),
            self.do_rpcrequest('ListFunctionDeployment', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_function_deployment_with_options_async(
        self,
        request: mpserverless_20190615_models.ListFunctionDeploymentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.ListFunctionDeploymentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.ListFunctionDeploymentResponse(),
            await self.do_rpcrequest_async('ListFunctionDeployment', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_function_deployment(
        self,
        request: mpserverless_20190615_models.ListFunctionDeploymentRequest,
    ) -> mpserverless_20190615_models.ListFunctionDeploymentResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_function_deployment_with_options(request, runtime)

    async def list_function_deployment_async(
        self,
        request: mpserverless_20190615_models.ListFunctionDeploymentRequest,
    ) -> mpserverless_20190615_models.ListFunctionDeploymentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_function_deployment_with_options_async(request, runtime)

    def add_dingtalk_open_platform_config_with_options(
        self,
        request: mpserverless_20190615_models.AddDingtalkOpenPlatformConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.AddDingtalkOpenPlatformConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.AddDingtalkOpenPlatformConfigResponse(),
            self.do_rpcrequest('AddDingtalkOpenPlatformConfig', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_dingtalk_open_platform_config_with_options_async(
        self,
        request: mpserverless_20190615_models.AddDingtalkOpenPlatformConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.AddDingtalkOpenPlatformConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.AddDingtalkOpenPlatformConfigResponse(),
            await self.do_rpcrequest_async('AddDingtalkOpenPlatformConfig', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_dingtalk_open_platform_config(
        self,
        request: mpserverless_20190615_models.AddDingtalkOpenPlatformConfigRequest,
    ) -> mpserverless_20190615_models.AddDingtalkOpenPlatformConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_dingtalk_open_platform_config_with_options(request, runtime)

    async def add_dingtalk_open_platform_config_async(
        self,
        request: mpserverless_20190615_models.AddDingtalkOpenPlatformConfigRequest,
    ) -> mpserverless_20190615_models.AddDingtalkOpenPlatformConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_dingtalk_open_platform_config_with_options_async(request, runtime)

    def create_dbrestore_task_with_options(
        self,
        request: mpserverless_20190615_models.CreateDBRestoreTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.CreateDBRestoreTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.CreateDBRestoreTaskResponse(),
            self.do_rpcrequest('CreateDBRestoreTask', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_dbrestore_task_with_options_async(
        self,
        request: mpserverless_20190615_models.CreateDBRestoreTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.CreateDBRestoreTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.CreateDBRestoreTaskResponse(),
            await self.do_rpcrequest_async('CreateDBRestoreTask', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_dbrestore_task(
        self,
        request: mpserverless_20190615_models.CreateDBRestoreTaskRequest,
    ) -> mpserverless_20190615_models.CreateDBRestoreTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_dbrestore_task_with_options(request, runtime)

    async def create_dbrestore_task_async(
        self,
        request: mpserverless_20190615_models.CreateDBRestoreTaskRequest,
    ) -> mpserverless_20190615_models.CreateDBRestoreTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_dbrestore_task_with_options_async(request, runtime)

    def attach_web_hosting_certificate_with_options(
        self,
        request: mpserverless_20190615_models.AttachWebHostingCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.AttachWebHostingCertificateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.AttachWebHostingCertificateResponse(),
            self.do_rpcrequest('AttachWebHostingCertificate', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def attach_web_hosting_certificate_with_options_async(
        self,
        request: mpserverless_20190615_models.AttachWebHostingCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.AttachWebHostingCertificateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.AttachWebHostingCertificateResponse(),
            await self.do_rpcrequest_async('AttachWebHostingCertificate', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def attach_web_hosting_certificate(
        self,
        request: mpserverless_20190615_models.AttachWebHostingCertificateRequest,
    ) -> mpserverless_20190615_models.AttachWebHostingCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.attach_web_hosting_certificate_with_options(request, runtime)

    async def attach_web_hosting_certificate_async(
        self,
        request: mpserverless_20190615_models.AttachWebHostingCertificateRequest,
    ) -> mpserverless_20190615_models.AttachWebHostingCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.attach_web_hosting_certificate_with_options_async(request, runtime)

    def list_file_with_options(
        self,
        request: mpserverless_20190615_models.ListFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.ListFileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.ListFileResponse(),
            self.do_rpcrequest('ListFile', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_file_with_options_async(
        self,
        request: mpserverless_20190615_models.ListFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.ListFileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.ListFileResponse(),
            await self.do_rpcrequest_async('ListFile', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_file(
        self,
        request: mpserverless_20190615_models.ListFileRequest,
    ) -> mpserverless_20190615_models.ListFileResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_file_with_options(request, runtime)

    async def list_file_async(
        self,
        request: mpserverless_20190615_models.ListFileRequest,
    ) -> mpserverless_20190615_models.ListFileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_file_with_options_async(request, runtime)

    def query_dbrestore_task_status_with_options(
        self,
        request: mpserverless_20190615_models.QueryDBRestoreTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.QueryDBRestoreTaskStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.QueryDBRestoreTaskStatusResponse(),
            self.do_rpcrequest('QueryDBRestoreTaskStatus', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_dbrestore_task_status_with_options_async(
        self,
        request: mpserverless_20190615_models.QueryDBRestoreTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.QueryDBRestoreTaskStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.QueryDBRestoreTaskStatusResponse(),
            await self.do_rpcrequest_async('QueryDBRestoreTaskStatus', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_dbrestore_task_status(
        self,
        request: mpserverless_20190615_models.QueryDBRestoreTaskStatusRequest,
    ) -> mpserverless_20190615_models.QueryDBRestoreTaskStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_dbrestore_task_status_with_options(request, runtime)

    async def query_dbrestore_task_status_async(
        self,
        request: mpserverless_20190615_models.QueryDBRestoreTaskStatusRequest,
    ) -> mpserverless_20190615_models.QueryDBRestoreTaskStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_dbrestore_task_status_with_options_async(request, runtime)

    def verify_web_hosting_domain_owner_with_options(
        self,
        request: mpserverless_20190615_models.VerifyWebHostingDomainOwnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.VerifyWebHostingDomainOwnerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.VerifyWebHostingDomainOwnerResponse(),
            self.do_rpcrequest('VerifyWebHostingDomainOwner', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def verify_web_hosting_domain_owner_with_options_async(
        self,
        request: mpserverless_20190615_models.VerifyWebHostingDomainOwnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.VerifyWebHostingDomainOwnerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.VerifyWebHostingDomainOwnerResponse(),
            await self.do_rpcrequest_async('VerifyWebHostingDomainOwner', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def verify_web_hosting_domain_owner(
        self,
        request: mpserverless_20190615_models.VerifyWebHostingDomainOwnerRequest,
    ) -> mpserverless_20190615_models.VerifyWebHostingDomainOwnerResponse:
        runtime = util_models.RuntimeOptions()
        return self.verify_web_hosting_domain_owner_with_options(request, runtime)

    async def verify_web_hosting_domain_owner_async(
        self,
        request: mpserverless_20190615_models.VerifyWebHostingDomainOwnerRequest,
    ) -> mpserverless_20190615_models.VerifyWebHostingDomainOwnerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.verify_web_hosting_domain_owner_with_options_async(request, runtime)

    def delete_sms_template_with_options(
        self,
        request: mpserverless_20190615_models.DeleteSmsTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.DeleteSmsTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.DeleteSmsTemplateResponse(),
            self.do_rpcrequest('DeleteSmsTemplate', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_sms_template_with_options_async(
        self,
        request: mpserverless_20190615_models.DeleteSmsTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.DeleteSmsTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.DeleteSmsTemplateResponse(),
            await self.do_rpcrequest_async('DeleteSmsTemplate', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_sms_template(
        self,
        request: mpserverless_20190615_models.DeleteSmsTemplateRequest,
    ) -> mpserverless_20190615_models.DeleteSmsTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_sms_template_with_options(request, runtime)

    async def delete_sms_template_async(
        self,
        request: mpserverless_20190615_models.DeleteSmsTemplateRequest,
    ) -> mpserverless_20190615_models.DeleteSmsTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_sms_template_with_options_async(request, runtime)

    def query_dbexport_task_status_with_options(
        self,
        request: mpserverless_20190615_models.QueryDBExportTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.QueryDBExportTaskStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.QueryDBExportTaskStatusResponse(),
            self.do_rpcrequest('QueryDBExportTaskStatus', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_dbexport_task_status_with_options_async(
        self,
        request: mpserverless_20190615_models.QueryDBExportTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.QueryDBExportTaskStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.QueryDBExportTaskStatusResponse(),
            await self.do_rpcrequest_async('QueryDBExportTaskStatus', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_dbexport_task_status(
        self,
        request: mpserverless_20190615_models.QueryDBExportTaskStatusRequest,
    ) -> mpserverless_20190615_models.QueryDBExportTaskStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_dbexport_task_status_with_options(request, runtime)

    async def query_dbexport_task_status_async(
        self,
        request: mpserverless_20190615_models.QueryDBExportTaskStatusRequest,
    ) -> mpserverless_20190615_models.QueryDBExportTaskStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_dbexport_task_status_with_options_async(request, runtime)

    def create_dbimport_task_with_options(
        self,
        request: mpserverless_20190615_models.CreateDBImportTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.CreateDBImportTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.CreateDBImportTaskResponse(),
            self.do_rpcrequest('CreateDBImportTask', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_dbimport_task_with_options_async(
        self,
        request: mpserverless_20190615_models.CreateDBImportTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.CreateDBImportTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.CreateDBImportTaskResponse(),
            await self.do_rpcrequest_async('CreateDBImportTask', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_dbimport_task(
        self,
        request: mpserverless_20190615_models.CreateDBImportTaskRequest,
    ) -> mpserverless_20190615_models.CreateDBImportTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_dbimport_task_with_options(request, runtime)

    async def create_dbimport_task_async(
        self,
        request: mpserverless_20190615_models.CreateDBImportTaskRequest,
    ) -> mpserverless_20190615_models.CreateDBImportTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_dbimport_task_with_options_async(request, runtime)

    def check_sms_has_authorized_to_mpswith_options(
        self,
        request: mpserverless_20190615_models.CheckSmsHasAuthorizedToMPSRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.CheckSmsHasAuthorizedToMPSResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.CheckSmsHasAuthorizedToMPSResponse(),
            self.do_rpcrequest('CheckSmsHasAuthorizedToMPS', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def check_sms_has_authorized_to_mpswith_options_async(
        self,
        request: mpserverless_20190615_models.CheckSmsHasAuthorizedToMPSRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.CheckSmsHasAuthorizedToMPSResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.CheckSmsHasAuthorizedToMPSResponse(),
            await self.do_rpcrequest_async('CheckSmsHasAuthorizedToMPS', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_sms_has_authorized_to_mps(
        self,
        request: mpserverless_20190615_models.CheckSmsHasAuthorizedToMPSRequest,
    ) -> mpserverless_20190615_models.CheckSmsHasAuthorizedToMPSResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_sms_has_authorized_to_mpswith_options(request, runtime)

    async def check_sms_has_authorized_to_mps_async(
        self,
        request: mpserverless_20190615_models.CheckSmsHasAuthorizedToMPSRequest,
    ) -> mpserverless_20190615_models.CheckSmsHasAuthorizedToMPSResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_sms_has_authorized_to_mpswith_options_async(request, runtime)

    def describe_service_policy_with_options(
        self,
        request: mpserverless_20190615_models.DescribeServicePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.DescribeServicePolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.DescribeServicePolicyResponse(),
            self.do_rpcrequest('DescribeServicePolicy', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_service_policy_with_options_async(
        self,
        request: mpserverless_20190615_models.DescribeServicePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.DescribeServicePolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.DescribeServicePolicyResponse(),
            await self.do_rpcrequest_async('DescribeServicePolicy', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_service_policy(
        self,
        request: mpserverless_20190615_models.DescribeServicePolicyRequest,
    ) -> mpserverless_20190615_models.DescribeServicePolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_service_policy_with_options(request, runtime)

    async def describe_service_policy_async(
        self,
        request: mpserverless_20190615_models.DescribeServicePolicyRequest,
    ) -> mpserverless_20190615_models.DescribeServicePolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_service_policy_with_options_async(request, runtime)

    def list_sms_templates_with_options(
        self,
        request: mpserverless_20190615_models.ListSmsTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.ListSmsTemplatesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.ListSmsTemplatesResponse(),
            self.do_rpcrequest('ListSmsTemplates', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_sms_templates_with_options_async(
        self,
        request: mpserverless_20190615_models.ListSmsTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.ListSmsTemplatesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.ListSmsTemplatesResponse(),
            await self.do_rpcrequest_async('ListSmsTemplates', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_sms_templates(
        self,
        request: mpserverless_20190615_models.ListSmsTemplatesRequest,
    ) -> mpserverless_20190615_models.ListSmsTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_sms_templates_with_options(request, runtime)

    async def list_sms_templates_async(
        self,
        request: mpserverless_20190615_models.ListSmsTemplatesRequest,
    ) -> mpserverless_20190615_models.ListSmsTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_sms_templates_with_options_async(request, runtime)

    def query_dbbackup_collections_with_options(
        self,
        request: mpserverless_20190615_models.QueryDBBackupCollectionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.QueryDBBackupCollectionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.QueryDBBackupCollectionsResponse(),
            self.do_rpcrequest('QueryDBBackupCollections', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_dbbackup_collections_with_options_async(
        self,
        request: mpserverless_20190615_models.QueryDBBackupCollectionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.QueryDBBackupCollectionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.QueryDBBackupCollectionsResponse(),
            await self.do_rpcrequest_async('QueryDBBackupCollections', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_dbbackup_collections(
        self,
        request: mpserverless_20190615_models.QueryDBBackupCollectionsRequest,
    ) -> mpserverless_20190615_models.QueryDBBackupCollectionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_dbbackup_collections_with_options(request, runtime)

    async def query_dbbackup_collections_async(
        self,
        request: mpserverless_20190615_models.QueryDBBackupCollectionsRequest,
    ) -> mpserverless_20190615_models.QueryDBBackupCollectionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_dbbackup_collections_with_options_async(request, runtime)

    def query_service_status_with_options(
        self,
        request: mpserverless_20190615_models.QueryServiceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.QueryServiceStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.QueryServiceStatusResponse(),
            self.do_rpcrequest('QueryServiceStatus', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_service_status_with_options_async(
        self,
        request: mpserverless_20190615_models.QueryServiceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.QueryServiceStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.QueryServiceStatusResponse(),
            await self.do_rpcrequest_async('QueryServiceStatus', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_service_status(
        self,
        request: mpserverless_20190615_models.QueryServiceStatusRequest,
    ) -> mpserverless_20190615_models.QueryServiceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_service_status_with_options(request, runtime)

    async def query_service_status_async(
        self,
        request: mpserverless_20190615_models.QueryServiceStatusRequest,
    ) -> mpserverless_20190615_models.QueryServiceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_service_status_with_options_async(request, runtime)

    def describe_space_client_config_with_options(
        self,
        request: mpserverless_20190615_models.DescribeSpaceClientConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.DescribeSpaceClientConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.DescribeSpaceClientConfigResponse(),
            self.do_rpcrequest('DescribeSpaceClientConfig', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_space_client_config_with_options_async(
        self,
        request: mpserverless_20190615_models.DescribeSpaceClientConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.DescribeSpaceClientConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.DescribeSpaceClientConfigResponse(),
            await self.do_rpcrequest_async('DescribeSpaceClientConfig', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_space_client_config(
        self,
        request: mpserverless_20190615_models.DescribeSpaceClientConfigRequest,
    ) -> mpserverless_20190615_models.DescribeSpaceClientConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_space_client_config_with_options(request, runtime)

    async def describe_space_client_config_async(
        self,
        request: mpserverless_20190615_models.DescribeSpaceClientConfigRequest,
    ) -> mpserverless_20190615_models.DescribeSpaceClientConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_space_client_config_with_options_async(request, runtime)

    def save_builtin_function_template_with_options(
        self,
        request: mpserverless_20190615_models.SaveBuiltinFunctionTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.SaveBuiltinFunctionTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.SaveBuiltinFunctionTemplateResponse(),
            self.do_rpcrequest('SaveBuiltinFunctionTemplate', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def save_builtin_function_template_with_options_async(
        self,
        request: mpserverless_20190615_models.SaveBuiltinFunctionTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.SaveBuiltinFunctionTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.SaveBuiltinFunctionTemplateResponse(),
            await self.do_rpcrequest_async('SaveBuiltinFunctionTemplate', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def save_builtin_function_template(
        self,
        request: mpserverless_20190615_models.SaveBuiltinFunctionTemplateRequest,
    ) -> mpserverless_20190615_models.SaveBuiltinFunctionTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.save_builtin_function_template_with_options(request, runtime)

    async def save_builtin_function_template_async(
        self,
        request: mpserverless_20190615_models.SaveBuiltinFunctionTemplateRequest,
    ) -> mpserverless_20190615_models.SaveBuiltinFunctionTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_builtin_function_template_with_options_async(request, runtime)

    def describe_isvfile_upload_signed_url_with_options(
        self,
        request: mpserverless_20190615_models.DescribeISVFileUploadSignedUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.DescribeISVFileUploadSignedUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.DescribeISVFileUploadSignedUrlResponse(),
            self.do_rpcrequest('DescribeISVFileUploadSignedUrl', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_isvfile_upload_signed_url_with_options_async(
        self,
        request: mpserverless_20190615_models.DescribeISVFileUploadSignedUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.DescribeISVFileUploadSignedUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.DescribeISVFileUploadSignedUrlResponse(),
            await self.do_rpcrequest_async('DescribeISVFileUploadSignedUrl', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_isvfile_upload_signed_url(
        self,
        request: mpserverless_20190615_models.DescribeISVFileUploadSignedUrlRequest,
    ) -> mpserverless_20190615_models.DescribeISVFileUploadSignedUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_isvfile_upload_signed_url_with_options(request, runtime)

    async def describe_isvfile_upload_signed_url_async(
        self,
        request: mpserverless_20190615_models.DescribeISVFileUploadSignedUrlRequest,
    ) -> mpserverless_20190615_models.DescribeISVFileUploadSignedUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_isvfile_upload_signed_url_with_options_async(request, runtime)

    def create_builtin_function_template_with_options(
        self,
        request: mpserverless_20190615_models.CreateBuiltinFunctionTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.CreateBuiltinFunctionTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.CreateBuiltinFunctionTemplateResponse(),
            self.do_rpcrequest('CreateBuiltinFunctionTemplate', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_builtin_function_template_with_options_async(
        self,
        request: mpserverless_20190615_models.CreateBuiltinFunctionTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.CreateBuiltinFunctionTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.CreateBuiltinFunctionTemplateResponse(),
            await self.do_rpcrequest_async('CreateBuiltinFunctionTemplate', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_builtin_function_template(
        self,
        request: mpserverless_20190615_models.CreateBuiltinFunctionTemplateRequest,
    ) -> mpserverless_20190615_models.CreateBuiltinFunctionTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_builtin_function_template_with_options(request, runtime)

    async def create_builtin_function_template_async(
        self,
        request: mpserverless_20190615_models.CreateBuiltinFunctionTemplateRequest,
    ) -> mpserverless_20190615_models.CreateBuiltinFunctionTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_builtin_function_template_with_options_async(request, runtime)

    def get_web_hosting_status_with_options(
        self,
        request: mpserverless_20190615_models.GetWebHostingStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.GetWebHostingStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.GetWebHostingStatusResponse(),
            self.do_rpcrequest('GetWebHostingStatus', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_web_hosting_status_with_options_async(
        self,
        request: mpserverless_20190615_models.GetWebHostingStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.GetWebHostingStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.GetWebHostingStatusResponse(),
            await self.do_rpcrequest_async('GetWebHostingStatus', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_web_hosting_status(
        self,
        request: mpserverless_20190615_models.GetWebHostingStatusRequest,
    ) -> mpserverless_20190615_models.GetWebHostingStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_web_hosting_status_with_options(request, runtime)

    async def get_web_hosting_status_async(
        self,
        request: mpserverless_20190615_models.GetWebHostingStatusRequest,
    ) -> mpserverless_20190615_models.GetWebHostingStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_web_hosting_status_with_options_async(request, runtime)

    def list_function_log_with_options(
        self,
        request: mpserverless_20190615_models.ListFunctionLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.ListFunctionLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.ListFunctionLogResponse(),
            self.do_rpcrequest('ListFunctionLog', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_function_log_with_options_async(
        self,
        request: mpserverless_20190615_models.ListFunctionLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.ListFunctionLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.ListFunctionLogResponse(),
            await self.do_rpcrequest_async('ListFunctionLog', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_function_log(
        self,
        request: mpserverless_20190615_models.ListFunctionLogRequest,
    ) -> mpserverless_20190615_models.ListFunctionLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_function_log_with_options(request, runtime)

    async def list_function_log_async(
        self,
        request: mpserverless_20190615_models.ListFunctionLogRequest,
    ) -> mpserverless_20190615_models.ListFunctionLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_function_log_with_options_async(request, runtime)

    def list_web_hosting_files_with_options(
        self,
        request: mpserverless_20190615_models.ListWebHostingFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.ListWebHostingFilesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.ListWebHostingFilesResponse(),
            self.do_rpcrequest('ListWebHostingFiles', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_web_hosting_files_with_options_async(
        self,
        request: mpserverless_20190615_models.ListWebHostingFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.ListWebHostingFilesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.ListWebHostingFilesResponse(),
            await self.do_rpcrequest_async('ListWebHostingFiles', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_web_hosting_files(
        self,
        request: mpserverless_20190615_models.ListWebHostingFilesRequest,
    ) -> mpserverless_20190615_models.ListWebHostingFilesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_web_hosting_files_with_options(request, runtime)

    async def list_web_hosting_files_async(
        self,
        request: mpserverless_20190615_models.ListWebHostingFilesRequest,
    ) -> mpserverless_20190615_models.ListWebHostingFilesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_web_hosting_files_with_options_async(request, runtime)

    def describe_file_with_options(
        self,
        request: mpserverless_20190615_models.DescribeFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.DescribeFileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.DescribeFileResponse(),
            self.do_rpcrequest('DescribeFile', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_file_with_options_async(
        self,
        request: mpserverless_20190615_models.DescribeFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.DescribeFileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.DescribeFileResponse(),
            await self.do_rpcrequest_async('DescribeFile', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_file(
        self,
        request: mpserverless_20190615_models.DescribeFileRequest,
    ) -> mpserverless_20190615_models.DescribeFileResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_file_with_options(request, runtime)

    async def describe_file_async(
        self,
        request: mpserverless_20190615_models.DescribeFileRequest,
    ) -> mpserverless_20190615_models.DescribeFileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_file_with_options_async(request, runtime)

    def move_web_hosting_file_with_options(
        self,
        request: mpserverless_20190615_models.MoveWebHostingFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.MoveWebHostingFileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.MoveWebHostingFileResponse(),
            self.do_rpcrequest('MoveWebHostingFile', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def move_web_hosting_file_with_options_async(
        self,
        request: mpserverless_20190615_models.MoveWebHostingFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.MoveWebHostingFileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.MoveWebHostingFileResponse(),
            await self.do_rpcrequest_async('MoveWebHostingFile', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def move_web_hosting_file(
        self,
        request: mpserverless_20190615_models.MoveWebHostingFileRequest,
    ) -> mpserverless_20190615_models.MoveWebHostingFileResponse:
        runtime = util_models.RuntimeOptions()
        return self.move_web_hosting_file_with_options(request, runtime)

    async def move_web_hosting_file_async(
        self,
        request: mpserverless_20190615_models.MoveWebHostingFileRequest,
    ) -> mpserverless_20190615_models.MoveWebHostingFileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.move_web_hosting_file_with_options_async(request, runtime)

    def create_sms_template_with_options(
        self,
        request: mpserverless_20190615_models.CreateSmsTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.CreateSmsTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.CreateSmsTemplateResponse(),
            self.do_rpcrequest('CreateSmsTemplate', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_sms_template_with_options_async(
        self,
        request: mpserverless_20190615_models.CreateSmsTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.CreateSmsTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.CreateSmsTemplateResponse(),
            await self.do_rpcrequest_async('CreateSmsTemplate', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_sms_template(
        self,
        request: mpserverless_20190615_models.CreateSmsTemplateRequest,
    ) -> mpserverless_20190615_models.CreateSmsTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_sms_template_with_options(request, runtime)

    async def create_sms_template_async(
        self,
        request: mpserverless_20190615_models.CreateSmsTemplateRequest,
    ) -> mpserverless_20190615_models.CreateSmsTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_sms_template_with_options_async(request, runtime)

    def describe_sms_template_status_with_options(
        self,
        request: mpserverless_20190615_models.DescribeSmsTemplateStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.DescribeSmsTemplateStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.DescribeSmsTemplateStatusResponse(),
            self.do_rpcrequest('DescribeSmsTemplateStatus', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_sms_template_status_with_options_async(
        self,
        request: mpserverless_20190615_models.DescribeSmsTemplateStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.DescribeSmsTemplateStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.DescribeSmsTemplateStatusResponse(),
            await self.do_rpcrequest_async('DescribeSmsTemplateStatus', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sms_template_status(
        self,
        request: mpserverless_20190615_models.DescribeSmsTemplateStatusRequest,
    ) -> mpserverless_20190615_models.DescribeSmsTemplateStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sms_template_status_with_options(request, runtime)

    async def describe_sms_template_status_async(
        self,
        request: mpserverless_20190615_models.DescribeSmsTemplateStatusRequest,
    ) -> mpserverless_20190615_models.DescribeSmsTemplateStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sms_template_status_with_options_async(request, runtime)

    def bind_web_hosting_custom_domain_with_options(
        self,
        request: mpserverless_20190615_models.BindWebHostingCustomDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.BindWebHostingCustomDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.BindWebHostingCustomDomainResponse(),
            self.do_rpcrequest('BindWebHostingCustomDomain', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def bind_web_hosting_custom_domain_with_options_async(
        self,
        request: mpserverless_20190615_models.BindWebHostingCustomDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.BindWebHostingCustomDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.BindWebHostingCustomDomainResponse(),
            await self.do_rpcrequest_async('BindWebHostingCustomDomain', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def bind_web_hosting_custom_domain(
        self,
        request: mpserverless_20190615_models.BindWebHostingCustomDomainRequest,
    ) -> mpserverless_20190615_models.BindWebHostingCustomDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.bind_web_hosting_custom_domain_with_options(request, runtime)

    async def bind_web_hosting_custom_domain_async(
        self,
        request: mpserverless_20190615_models.BindWebHostingCustomDomainRequest,
    ) -> mpserverless_20190615_models.BindWebHostingCustomDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.bind_web_hosting_custom_domain_with_options_async(request, runtime)

    def create_function_with_options(
        self,
        request: mpserverless_20190615_models.CreateFunctionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.CreateFunctionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.CreateFunctionResponse(),
            self.do_rpcrequest('CreateFunction', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_function_with_options_async(
        self,
        request: mpserverless_20190615_models.CreateFunctionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.CreateFunctionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.CreateFunctionResponse(),
            await self.do_rpcrequest_async('CreateFunction', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_function(
        self,
        request: mpserverless_20190615_models.CreateFunctionRequest,
    ) -> mpserverless_20190615_models.CreateFunctionResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_function_with_options(request, runtime)

    async def create_function_async(
        self,
        request: mpserverless_20190615_models.CreateFunctionRequest,
    ) -> mpserverless_20190615_models.CreateFunctionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_function_with_options_async(request, runtime)

    def delete_dingtalk_open_platform_config_with_options(
        self,
        request: mpserverless_20190615_models.DeleteDingtalkOpenPlatformConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.DeleteDingtalkOpenPlatformConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.DeleteDingtalkOpenPlatformConfigResponse(),
            self.do_rpcrequest('DeleteDingtalkOpenPlatformConfig', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_dingtalk_open_platform_config_with_options_async(
        self,
        request: mpserverless_20190615_models.DeleteDingtalkOpenPlatformConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.DeleteDingtalkOpenPlatformConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.DeleteDingtalkOpenPlatformConfigResponse(),
            await self.do_rpcrequest_async('DeleteDingtalkOpenPlatformConfig', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_dingtalk_open_platform_config(
        self,
        request: mpserverless_20190615_models.DeleteDingtalkOpenPlatformConfigRequest,
    ) -> mpserverless_20190615_models.DeleteDingtalkOpenPlatformConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_dingtalk_open_platform_config_with_options(request, runtime)

    async def delete_dingtalk_open_platform_config_async(
        self,
        request: mpserverless_20190615_models.DeleteDingtalkOpenPlatformConfigRequest,
    ) -> mpserverless_20190615_models.DeleteDingtalkOpenPlatformConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_dingtalk_open_platform_config_with_options_async(request, runtime)

    def list_extensions_with_options(
        self,
        request: mpserverless_20190615_models.ListExtensionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.ListExtensionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.ListExtensionsResponse(),
            self.do_rpcrequest('ListExtensions', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_extensions_with_options_async(
        self,
        request: mpserverless_20190615_models.ListExtensionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.ListExtensionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.ListExtensionsResponse(),
            await self.do_rpcrequest_async('ListExtensions', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_extensions(
        self,
        request: mpserverless_20190615_models.ListExtensionsRequest,
    ) -> mpserverless_20190615_models.ListExtensionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_extensions_with_options(request, runtime)

    async def list_extensions_async(
        self,
        request: mpserverless_20190615_models.ListExtensionsRequest,
    ) -> mpserverless_20190615_models.ListExtensionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_extensions_with_options_async(request, runtime)

    def enable_sms_service_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.EnableSmsServiceResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            mpserverless_20190615_models.EnableSmsServiceResponse(),
            self.do_rpcrequest('EnableSmsService', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def enable_sms_service_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.EnableSmsServiceResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            mpserverless_20190615_models.EnableSmsServiceResponse(),
            await self.do_rpcrequest_async('EnableSmsService', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enable_sms_service(self) -> mpserverless_20190615_models.EnableSmsServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_sms_service_with_options(runtime)

    async def enable_sms_service_async(self) -> mpserverless_20190615_models.EnableSmsServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_sms_service_with_options_async(runtime)

    def release_builtin_function_template_with_options(
        self,
        request: mpserverless_20190615_models.ReleaseBuiltinFunctionTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.ReleaseBuiltinFunctionTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.ReleaseBuiltinFunctionTemplateResponse(),
            self.do_rpcrequest('ReleaseBuiltinFunctionTemplate', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def release_builtin_function_template_with_options_async(
        self,
        request: mpserverless_20190615_models.ReleaseBuiltinFunctionTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.ReleaseBuiltinFunctionTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.ReleaseBuiltinFunctionTemplateResponse(),
            await self.do_rpcrequest_async('ReleaseBuiltinFunctionTemplate', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def release_builtin_function_template(
        self,
        request: mpserverless_20190615_models.ReleaseBuiltinFunctionTemplateRequest,
    ) -> mpserverless_20190615_models.ReleaseBuiltinFunctionTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.release_builtin_function_template_with_options(request, runtime)

    async def release_builtin_function_template_async(
        self,
        request: mpserverless_20190615_models.ReleaseBuiltinFunctionTemplateRequest,
    ) -> mpserverless_20190615_models.ReleaseBuiltinFunctionTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.release_builtin_function_template_with_options_async(request, runtime)

    def create_sms_sign_with_options(
        self,
        request: mpserverless_20190615_models.CreateSmsSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.CreateSmsSignResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.CreateSmsSignResponse(),
            self.do_rpcrequest('CreateSmsSign', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_sms_sign_with_options_async(
        self,
        request: mpserverless_20190615_models.CreateSmsSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.CreateSmsSignResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.CreateSmsSignResponse(),
            await self.do_rpcrequest_async('CreateSmsSign', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_sms_sign(
        self,
        request: mpserverless_20190615_models.CreateSmsSignRequest,
    ) -> mpserverless_20190615_models.CreateSmsSignResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_sms_sign_with_options(request, runtime)

    async def create_sms_sign_async(
        self,
        request: mpserverless_20190615_models.CreateSmsSignRequest,
    ) -> mpserverless_20190615_models.CreateSmsSignResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_sms_sign_with_options_async(request, runtime)

    def update_function_with_options(
        self,
        request: mpserverless_20190615_models.UpdateFunctionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.UpdateFunctionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.UpdateFunctionResponse(),
            self.do_rpcrequest('UpdateFunction', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_function_with_options_async(
        self,
        request: mpserverless_20190615_models.UpdateFunctionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.UpdateFunctionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.UpdateFunctionResponse(),
            await self.do_rpcrequest_async('UpdateFunction', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_function(
        self,
        request: mpserverless_20190615_models.UpdateFunctionRequest,
    ) -> mpserverless_20190615_models.UpdateFunctionResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_function_with_options(request, runtime)

    async def update_function_async(
        self,
        request: mpserverless_20190615_models.UpdateFunctionRequest,
    ) -> mpserverless_20190615_models.UpdateFunctionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_function_with_options_async(request, runtime)

    def update_http_trigger_config_with_options(
        self,
        request: mpserverless_20190615_models.UpdateHttpTriggerConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.UpdateHttpTriggerConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.UpdateHttpTriggerConfigResponse(),
            self.do_rpcrequest('UpdateHttpTriggerConfig', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_http_trigger_config_with_options_async(
        self,
        request: mpserverless_20190615_models.UpdateHttpTriggerConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.UpdateHttpTriggerConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.UpdateHttpTriggerConfigResponse(),
            await self.do_rpcrequest_async('UpdateHttpTriggerConfig', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_http_trigger_config(
        self,
        request: mpserverless_20190615_models.UpdateHttpTriggerConfigRequest,
    ) -> mpserverless_20190615_models.UpdateHttpTriggerConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_http_trigger_config_with_options(request, runtime)

    async def update_http_trigger_config_async(
        self,
        request: mpserverless_20190615_models.UpdateHttpTriggerConfigRequest,
    ) -> mpserverless_20190615_models.UpdateHttpTriggerConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_http_trigger_config_with_options_async(request, runtime)

    def reset_server_secret_with_options(
        self,
        request: mpserverless_20190615_models.ResetServerSecretRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.ResetServerSecretResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.ResetServerSecretResponse(),
            self.do_rpcrequest('ResetServerSecret', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def reset_server_secret_with_options_async(
        self,
        request: mpserverless_20190615_models.ResetServerSecretRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.ResetServerSecretResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.ResetServerSecretResponse(),
            await self.do_rpcrequest_async('ResetServerSecret', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def reset_server_secret(
        self,
        request: mpserverless_20190615_models.ResetServerSecretRequest,
    ) -> mpserverless_20190615_models.ResetServerSecretResponse:
        runtime = util_models.RuntimeOptions()
        return self.reset_server_secret_with_options(request, runtime)

    async def reset_server_secret_async(
        self,
        request: mpserverless_20190615_models.ResetServerSecretRequest,
    ) -> mpserverless_20190615_models.ResetServerSecretResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_server_secret_with_options_async(request, runtime)

    def get_web_hosting_domain_verification_content_with_options(
        self,
        request: mpserverless_20190615_models.GetWebHostingDomainVerificationContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.GetWebHostingDomainVerificationContentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.GetWebHostingDomainVerificationContentResponse(),
            self.do_rpcrequest('GetWebHostingDomainVerificationContent', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_web_hosting_domain_verification_content_with_options_async(
        self,
        request: mpserverless_20190615_models.GetWebHostingDomainVerificationContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.GetWebHostingDomainVerificationContentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.GetWebHostingDomainVerificationContentResponse(),
            await self.do_rpcrequest_async('GetWebHostingDomainVerificationContent', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_web_hosting_domain_verification_content(
        self,
        request: mpserverless_20190615_models.GetWebHostingDomainVerificationContentRequest,
    ) -> mpserverless_20190615_models.GetWebHostingDomainVerificationContentResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_web_hosting_domain_verification_content_with_options(request, runtime)

    async def get_web_hosting_domain_verification_content_async(
        self,
        request: mpserverless_20190615_models.GetWebHostingDomainVerificationContentRequest,
    ) -> mpserverless_20190615_models.GetWebHostingDomainVerificationContentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_web_hosting_domain_verification_content_with_options_async(request, runtime)

    def update_dingtalk_open_platform_config_with_options(
        self,
        request: mpserverless_20190615_models.UpdateDingtalkOpenPlatformConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.UpdateDingtalkOpenPlatformConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.UpdateDingtalkOpenPlatformConfigResponse(),
            self.do_rpcrequest('UpdateDingtalkOpenPlatformConfig', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_dingtalk_open_platform_config_with_options_async(
        self,
        request: mpserverless_20190615_models.UpdateDingtalkOpenPlatformConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.UpdateDingtalkOpenPlatformConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.UpdateDingtalkOpenPlatformConfigResponse(),
            await self.do_rpcrequest_async('UpdateDingtalkOpenPlatformConfig', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_dingtalk_open_platform_config(
        self,
        request: mpserverless_20190615_models.UpdateDingtalkOpenPlatformConfigRequest,
    ) -> mpserverless_20190615_models.UpdateDingtalkOpenPlatformConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_dingtalk_open_platform_config_with_options(request, runtime)

    async def update_dingtalk_open_platform_config_async(
        self,
        request: mpserverless_20190615_models.UpdateDingtalkOpenPlatformConfigRequest,
    ) -> mpserverless_20190615_models.UpdateDingtalkOpenPlatformConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_dingtalk_open_platform_config_with_options_async(request, runtime)

    def check_mp_serverless_role_exists_with_options(
        self,
        request: mpserverless_20190615_models.CheckMpServerlessRoleExistsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.CheckMpServerlessRoleExistsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.CheckMpServerlessRoleExistsResponse(),
            self.do_rpcrequest('CheckMpServerlessRoleExists', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def check_mp_serverless_role_exists_with_options_async(
        self,
        request: mpserverless_20190615_models.CheckMpServerlessRoleExistsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.CheckMpServerlessRoleExistsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.CheckMpServerlessRoleExistsResponse(),
            await self.do_rpcrequest_async('CheckMpServerlessRoleExists', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_mp_serverless_role_exists(
        self,
        request: mpserverless_20190615_models.CheckMpServerlessRoleExistsRequest,
    ) -> mpserverless_20190615_models.CheckMpServerlessRoleExistsResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_mp_serverless_role_exists_with_options(request, runtime)

    async def check_mp_serverless_role_exists_async(
        self,
        request: mpserverless_20190615_models.CheckMpServerlessRoleExistsRequest,
    ) -> mpserverless_20190615_models.CheckMpServerlessRoleExistsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_mp_serverless_role_exists_with_options_async(request, runtime)

    def enable_extension_with_options(
        self,
        request: mpserverless_20190615_models.EnableExtensionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.EnableExtensionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.EnableExtensionResponse(),
            self.do_rpcrequest('EnableExtension', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def enable_extension_with_options_async(
        self,
        request: mpserverless_20190615_models.EnableExtensionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.EnableExtensionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.EnableExtensionResponse(),
            await self.do_rpcrequest_async('EnableExtension', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enable_extension(
        self,
        request: mpserverless_20190615_models.EnableExtensionRequest,
    ) -> mpserverless_20190615_models.EnableExtensionResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_extension_with_options(request, runtime)

    async def enable_extension_async(
        self,
        request: mpserverless_20190615_models.EnableExtensionRequest,
    ) -> mpserverless_20190615_models.EnableExtensionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_extension_with_options_async(request, runtime)

    def list_sms_signs_for_account_with_options(
        self,
        request: mpserverless_20190615_models.ListSmsSignsForAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.ListSmsSignsForAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.ListSmsSignsForAccountResponse(),
            self.do_rpcrequest('ListSmsSignsForAccount', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_sms_signs_for_account_with_options_async(
        self,
        request: mpserverless_20190615_models.ListSmsSignsForAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.ListSmsSignsForAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.ListSmsSignsForAccountResponse(),
            await self.do_rpcrequest_async('ListSmsSignsForAccount', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_sms_signs_for_account(
        self,
        request: mpserverless_20190615_models.ListSmsSignsForAccountRequest,
    ) -> mpserverless_20190615_models.ListSmsSignsForAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_sms_signs_for_account_with_options(request, runtime)

    async def list_sms_signs_for_account_async(
        self,
        request: mpserverless_20190615_models.ListSmsSignsForAccountRequest,
    ) -> mpserverless_20190615_models.ListSmsSignsForAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_sms_signs_for_account_with_options_async(request, runtime)

    def list_cors_domains_with_options(
        self,
        request: mpserverless_20190615_models.ListCorsDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.ListCorsDomainsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.ListCorsDomainsResponse(),
            self.do_rpcrequest('ListCorsDomains', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_cors_domains_with_options_async(
        self,
        request: mpserverless_20190615_models.ListCorsDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.ListCorsDomainsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.ListCorsDomainsResponse(),
            await self.do_rpcrequest_async('ListCorsDomains', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_cors_domains(
        self,
        request: mpserverless_20190615_models.ListCorsDomainsRequest,
    ) -> mpserverless_20190615_models.ListCorsDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_cors_domains_with_options(request, runtime)

    async def list_cors_domains_async(
        self,
        request: mpserverless_20190615_models.ListCorsDomainsRequest,
    ) -> mpserverless_20190615_models.ListCorsDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_cors_domains_with_options_async(request, runtime)

    def list_dingtalk_open_platform_configs_with_options(
        self,
        request: mpserverless_20190615_models.ListDingtalkOpenPlatformConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.ListDingtalkOpenPlatformConfigsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.ListDingtalkOpenPlatformConfigsResponse(),
            self.do_rpcrequest('ListDingtalkOpenPlatformConfigs', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_dingtalk_open_platform_configs_with_options_async(
        self,
        request: mpserverless_20190615_models.ListDingtalkOpenPlatformConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.ListDingtalkOpenPlatformConfigsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.ListDingtalkOpenPlatformConfigsResponse(),
            await self.do_rpcrequest_async('ListDingtalkOpenPlatformConfigs', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_dingtalk_open_platform_configs(
        self,
        request: mpserverless_20190615_models.ListDingtalkOpenPlatformConfigsRequest,
    ) -> mpserverless_20190615_models.ListDingtalkOpenPlatformConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_dingtalk_open_platform_configs_with_options(request, runtime)

    async def list_dingtalk_open_platform_configs_async(
        self,
        request: mpserverless_20190615_models.ListDingtalkOpenPlatformConfigsRequest,
    ) -> mpserverless_20190615_models.ListDingtalkOpenPlatformConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_dingtalk_open_platform_configs_with_options_async(request, runtime)

    def create_dbexport_task_with_options(
        self,
        request: mpserverless_20190615_models.CreateDBExportTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.CreateDBExportTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.CreateDBExportTaskResponse(),
            self.do_rpcrequest('CreateDBExportTask', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_dbexport_task_with_options_async(
        self,
        request: mpserverless_20190615_models.CreateDBExportTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.CreateDBExportTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.CreateDBExportTaskResponse(),
            await self.do_rpcrequest_async('CreateDBExportTask', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_dbexport_task(
        self,
        request: mpserverless_20190615_models.CreateDBExportTaskRequest,
    ) -> mpserverless_20190615_models.CreateDBExportTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_dbexport_task_with_options(request, runtime)

    async def create_dbexport_task_async(
        self,
        request: mpserverless_20190615_models.CreateDBExportTaskRequest,
    ) -> mpserverless_20190615_models.CreateDBExportTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_dbexport_task_with_options_async(request, runtime)

    def get_web_hosting_config_with_options(
        self,
        request: mpserverless_20190615_models.GetWebHostingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.GetWebHostingConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.GetWebHostingConfigResponse(),
            self.do_rpcrequest('GetWebHostingConfig', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_web_hosting_config_with_options_async(
        self,
        request: mpserverless_20190615_models.GetWebHostingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.GetWebHostingConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.GetWebHostingConfigResponse(),
            await self.do_rpcrequest_async('GetWebHostingConfig', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_web_hosting_config(
        self,
        request: mpserverless_20190615_models.GetWebHostingConfigRequest,
    ) -> mpserverless_20190615_models.GetWebHostingConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_web_hosting_config_with_options(request, runtime)

    async def get_web_hosting_config_async(
        self,
        request: mpserverless_20190615_models.GetWebHostingConfigRequest,
    ) -> mpserverless_20190615_models.GetWebHostingConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_web_hosting_config_with_options_async(request, runtime)

    def unbind_web_hosting_custom_domain_with_options(
        self,
        request: mpserverless_20190615_models.UnbindWebHostingCustomDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.UnbindWebHostingCustomDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.UnbindWebHostingCustomDomainResponse(),
            self.do_rpcrequest('UnbindWebHostingCustomDomain', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def unbind_web_hosting_custom_domain_with_options_async(
        self,
        request: mpserverless_20190615_models.UnbindWebHostingCustomDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.UnbindWebHostingCustomDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.UnbindWebHostingCustomDomainResponse(),
            await self.do_rpcrequest_async('UnbindWebHostingCustomDomain', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def unbind_web_hosting_custom_domain(
        self,
        request: mpserverless_20190615_models.UnbindWebHostingCustomDomainRequest,
    ) -> mpserverless_20190615_models.UnbindWebHostingCustomDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.unbind_web_hosting_custom_domain_with_options(request, runtime)

    async def unbind_web_hosting_custom_domain_async(
        self,
        request: mpserverless_20190615_models.UnbindWebHostingCustomDomainRequest,
    ) -> mpserverless_20190615_models.UnbindWebHostingCustomDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unbind_web_hosting_custom_domain_with_options_async(request, runtime)

    def describe_sms_template_with_options(
        self,
        request: mpserverless_20190615_models.DescribeSmsTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.DescribeSmsTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.DescribeSmsTemplateResponse(),
            self.do_rpcrequest('DescribeSmsTemplate', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_sms_template_with_options_async(
        self,
        request: mpserverless_20190615_models.DescribeSmsTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.DescribeSmsTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.DescribeSmsTemplateResponse(),
            await self.do_rpcrequest_async('DescribeSmsTemplate', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sms_template(
        self,
        request: mpserverless_20190615_models.DescribeSmsTemplateRequest,
    ) -> mpserverless_20190615_models.DescribeSmsTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sms_template_with_options(request, runtime)

    async def describe_sms_template_async(
        self,
        request: mpserverless_20190615_models.DescribeSmsTemplateRequest,
    ) -> mpserverless_20190615_models.DescribeSmsTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sms_template_with_options_async(request, runtime)

    def save_web_hosting_custom_domain_cors_config_with_options(
        self,
        request: mpserverless_20190615_models.SaveWebHostingCustomDomainCorsConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.SaveWebHostingCustomDomainCorsConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.SaveWebHostingCustomDomainCorsConfigResponse(),
            self.do_rpcrequest('SaveWebHostingCustomDomainCorsConfig', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def save_web_hosting_custom_domain_cors_config_with_options_async(
        self,
        request: mpserverless_20190615_models.SaveWebHostingCustomDomainCorsConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.SaveWebHostingCustomDomainCorsConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.SaveWebHostingCustomDomainCorsConfigResponse(),
            await self.do_rpcrequest_async('SaveWebHostingCustomDomainCorsConfig', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def save_web_hosting_custom_domain_cors_config(
        self,
        request: mpserverless_20190615_models.SaveWebHostingCustomDomainCorsConfigRequest,
    ) -> mpserverless_20190615_models.SaveWebHostingCustomDomainCorsConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.save_web_hosting_custom_domain_cors_config_with_options(request, runtime)

    async def save_web_hosting_custom_domain_cors_config_async(
        self,
        request: mpserverless_20190615_models.SaveWebHostingCustomDomainCorsConfigRequest,
    ) -> mpserverless_20190615_models.SaveWebHostingCustomDomainCorsConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_web_hosting_custom_domain_cors_config_with_options_async(request, runtime)

    def batch_delete_web_hosting_files_with_options(
        self,
        request: mpserverless_20190615_models.BatchDeleteWebHostingFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.BatchDeleteWebHostingFilesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.BatchDeleteWebHostingFilesResponse(),
            self.do_rpcrequest('BatchDeleteWebHostingFiles', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def batch_delete_web_hosting_files_with_options_async(
        self,
        request: mpserverless_20190615_models.BatchDeleteWebHostingFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.BatchDeleteWebHostingFilesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.BatchDeleteWebHostingFilesResponse(),
            await self.do_rpcrequest_async('BatchDeleteWebHostingFiles', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def batch_delete_web_hosting_files(
        self,
        request: mpserverless_20190615_models.BatchDeleteWebHostingFilesRequest,
    ) -> mpserverless_20190615_models.BatchDeleteWebHostingFilesResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_delete_web_hosting_files_with_options(request, runtime)

    async def batch_delete_web_hosting_files_async(
        self,
        request: mpserverless_20190615_models.BatchDeleteWebHostingFilesRequest,
    ) -> mpserverless_20190615_models.BatchDeleteWebHostingFilesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_delete_web_hosting_files_with_options_async(request, runtime)

    def delete_cors_domain_with_options(
        self,
        request: mpserverless_20190615_models.DeleteCorsDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.DeleteCorsDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.DeleteCorsDomainResponse(),
            self.do_rpcrequest('DeleteCorsDomain', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_cors_domain_with_options_async(
        self,
        request: mpserverless_20190615_models.DeleteCorsDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.DeleteCorsDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.DeleteCorsDomainResponse(),
            await self.do_rpcrequest_async('DeleteCorsDomain', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_cors_domain(
        self,
        request: mpserverless_20190615_models.DeleteCorsDomainRequest,
    ) -> mpserverless_20190615_models.DeleteCorsDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_cors_domain_with_options(request, runtime)

    async def delete_cors_domain_async(
        self,
        request: mpserverless_20190615_models.DeleteCorsDomainRequest,
    ) -> mpserverless_20190615_models.DeleteCorsDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_cors_domain_with_options_async(request, runtime)

    def describe_http_trigger_config_with_options(
        self,
        request: mpserverless_20190615_models.DescribeHttpTriggerConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.DescribeHttpTriggerConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.DescribeHttpTriggerConfigResponse(),
            self.do_rpcrequest('DescribeHttpTriggerConfig', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_http_trigger_config_with_options_async(
        self,
        request: mpserverless_20190615_models.DescribeHttpTriggerConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.DescribeHttpTriggerConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.DescribeHttpTriggerConfigResponse(),
            await self.do_rpcrequest_async('DescribeHttpTriggerConfig', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_http_trigger_config(
        self,
        request: mpserverless_20190615_models.DescribeHttpTriggerConfigRequest,
    ) -> mpserverless_20190615_models.DescribeHttpTriggerConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_http_trigger_config_with_options(request, runtime)

    async def describe_http_trigger_config_async(
        self,
        request: mpserverless_20190615_models.DescribeHttpTriggerConfigRequest,
    ) -> mpserverless_20190615_models.DescribeHttpTriggerConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_http_trigger_config_with_options_async(request, runtime)

    def save_app_auth_token_with_options(
        self,
        request: mpserverless_20190615_models.SaveAppAuthTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.SaveAppAuthTokenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.SaveAppAuthTokenResponse(),
            self.do_rpcrequest('SaveAppAuthToken', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def save_app_auth_token_with_options_async(
        self,
        request: mpserverless_20190615_models.SaveAppAuthTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.SaveAppAuthTokenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.SaveAppAuthTokenResponse(),
            await self.do_rpcrequest_async('SaveAppAuthToken', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def save_app_auth_token(
        self,
        request: mpserverless_20190615_models.SaveAppAuthTokenRequest,
    ) -> mpserverless_20190615_models.SaveAppAuthTokenResponse:
        runtime = util_models.RuntimeOptions()
        return self.save_app_auth_token_with_options(request, runtime)

    async def save_app_auth_token_async(
        self,
        request: mpserverless_20190615_models.SaveAppAuthTokenRequest,
    ) -> mpserverless_20190615_models.SaveAppAuthTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_app_auth_token_with_options_async(request, runtime)

    def describe_sms_sign_status_with_options(
        self,
        request: mpserverless_20190615_models.DescribeSmsSignStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.DescribeSmsSignStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.DescribeSmsSignStatusResponse(),
            self.do_rpcrequest('DescribeSmsSignStatus', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_sms_sign_status_with_options_async(
        self,
        request: mpserverless_20190615_models.DescribeSmsSignStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.DescribeSmsSignStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.DescribeSmsSignStatusResponse(),
            await self.do_rpcrequest_async('DescribeSmsSignStatus', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sms_sign_status(
        self,
        request: mpserverless_20190615_models.DescribeSmsSignStatusRequest,
    ) -> mpserverless_20190615_models.DescribeSmsSignStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sms_sign_status_with_options(request, runtime)

    async def describe_sms_sign_status_async(
        self,
        request: mpserverless_20190615_models.DescribeSmsSignStatusRequest,
    ) -> mpserverless_20190615_models.DescribeSmsSignStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sms_sign_status_with_options_async(request, runtime)

    def save_wechat_open_platform_config_with_options(
        self,
        request: mpserverless_20190615_models.SaveWechatOpenPlatformConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.SaveWechatOpenPlatformConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.SaveWechatOpenPlatformConfigResponse(),
            self.do_rpcrequest('SaveWechatOpenPlatformConfig', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def save_wechat_open_platform_config_with_options_async(
        self,
        request: mpserverless_20190615_models.SaveWechatOpenPlatformConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.SaveWechatOpenPlatformConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.SaveWechatOpenPlatformConfigResponse(),
            await self.do_rpcrequest_async('SaveWechatOpenPlatformConfig', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def save_wechat_open_platform_config(
        self,
        request: mpserverless_20190615_models.SaveWechatOpenPlatformConfigRequest,
    ) -> mpserverless_20190615_models.SaveWechatOpenPlatformConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.save_wechat_open_platform_config_with_options(request, runtime)

    async def save_wechat_open_platform_config_async(
        self,
        request: mpserverless_20190615_models.SaveWechatOpenPlatformConfigRequest,
    ) -> mpserverless_20190615_models.SaveWechatOpenPlatformConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_wechat_open_platform_config_with_options_async(request, runtime)

    def describe_space_with_options(
        self,
        request: mpserverless_20190615_models.DescribeSpaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.DescribeSpaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.DescribeSpaceResponse(),
            self.do_rpcrequest('DescribeSpace', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_space_with_options_async(
        self,
        request: mpserverless_20190615_models.DescribeSpaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.DescribeSpaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.DescribeSpaceResponse(),
            await self.do_rpcrequest_async('DescribeSpace', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_space(
        self,
        request: mpserverless_20190615_models.DescribeSpaceRequest,
    ) -> mpserverless_20190615_models.DescribeSpaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_space_with_options(request, runtime)

    async def describe_space_async(
        self,
        request: mpserverless_20190615_models.DescribeSpaceRequest,
    ) -> mpserverless_20190615_models.DescribeSpaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_space_with_options_async(request, runtime)

    def rename_dbcollection_with_options(
        self,
        request: mpserverless_20190615_models.RenameDBCollectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.RenameDBCollectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.RenameDBCollectionResponse(),
            self.do_rpcrequest('RenameDBCollection', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def rename_dbcollection_with_options_async(
        self,
        request: mpserverless_20190615_models.RenameDBCollectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.RenameDBCollectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.RenameDBCollectionResponse(),
            await self.do_rpcrequest_async('RenameDBCollection', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def rename_dbcollection(
        self,
        request: mpserverless_20190615_models.RenameDBCollectionRequest,
    ) -> mpserverless_20190615_models.RenameDBCollectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.rename_dbcollection_with_options(request, runtime)

    async def rename_dbcollection_async(
        self,
        request: mpserverless_20190615_models.RenameDBCollectionRequest,
    ) -> mpserverless_20190615_models.RenameDBCollectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.rename_dbcollection_with_options_async(request, runtime)

    def list_sms_signs_with_options(
        self,
        request: mpserverless_20190615_models.ListSmsSignsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.ListSmsSignsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.ListSmsSignsResponse(),
            self.do_rpcrequest('ListSmsSigns', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_sms_signs_with_options_async(
        self,
        request: mpserverless_20190615_models.ListSmsSignsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.ListSmsSignsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.ListSmsSignsResponse(),
            await self.do_rpcrequest_async('ListSmsSigns', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_sms_signs(
        self,
        request: mpserverless_20190615_models.ListSmsSignsRequest,
    ) -> mpserverless_20190615_models.ListSmsSignsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_sms_signs_with_options(request, runtime)

    async def list_sms_signs_async(
        self,
        request: mpserverless_20190615_models.ListSmsSignsRequest,
    ) -> mpserverless_20190615_models.ListSmsSignsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_sms_signs_with_options_async(request, runtime)

    def describe_product_open_status_with_options(
        self,
        request: mpserverless_20190615_models.DescribeProductOpenStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.DescribeProductOpenStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.DescribeProductOpenStatusResponse(),
            self.do_rpcrequest('DescribeProductOpenStatus', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_product_open_status_with_options_async(
        self,
        request: mpserverless_20190615_models.DescribeProductOpenStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.DescribeProductOpenStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.DescribeProductOpenStatusResponse(),
            await self.do_rpcrequest_async('DescribeProductOpenStatus', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_product_open_status(
        self,
        request: mpserverless_20190615_models.DescribeProductOpenStatusRequest,
    ) -> mpserverless_20190615_models.DescribeProductOpenStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_product_open_status_with_options(request, runtime)

    async def describe_product_open_status_async(
        self,
        request: mpserverless_20190615_models.DescribeProductOpenStatusRequest,
    ) -> mpserverless_20190615_models.DescribeProductOpenStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_product_open_status_with_options_async(request, runtime)

    def update_sms_sign_with_options(
        self,
        request: mpserverless_20190615_models.UpdateSmsSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.UpdateSmsSignResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.UpdateSmsSignResponse(),
            self.do_rpcrequest('UpdateSmsSign', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_sms_sign_with_options_async(
        self,
        request: mpserverless_20190615_models.UpdateSmsSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.UpdateSmsSignResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.UpdateSmsSignResponse(),
            await self.do_rpcrequest_async('UpdateSmsSign', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_sms_sign(
        self,
        request: mpserverless_20190615_models.UpdateSmsSignRequest,
    ) -> mpserverless_20190615_models.UpdateSmsSignResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_sms_sign_with_options(request, runtime)

    async def update_sms_sign_async(
        self,
        request: mpserverless_20190615_models.UpdateSmsSignRequest,
    ) -> mpserverless_20190615_models.UpdateSmsSignResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_sms_sign_with_options_async(request, runtime)

    def delete_web_hosting_certificate_with_options(
        self,
        request: mpserverless_20190615_models.DeleteWebHostingCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.DeleteWebHostingCertificateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.DeleteWebHostingCertificateResponse(),
            self.do_rpcrequest('DeleteWebHostingCertificate', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_web_hosting_certificate_with_options_async(
        self,
        request: mpserverless_20190615_models.DeleteWebHostingCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.DeleteWebHostingCertificateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.DeleteWebHostingCertificateResponse(),
            await self.do_rpcrequest_async('DeleteWebHostingCertificate', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_web_hosting_certificate(
        self,
        request: mpserverless_20190615_models.DeleteWebHostingCertificateRequest,
    ) -> mpserverless_20190615_models.DeleteWebHostingCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_web_hosting_certificate_with_options(request, runtime)

    async def delete_web_hosting_certificate_async(
        self,
        request: mpserverless_20190615_models.DeleteWebHostingCertificateRequest,
    ) -> mpserverless_20190615_models.DeleteWebHostingCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_web_hosting_certificate_with_options_async(request, runtime)

    def query_dbbackup_dump_times_with_options(
        self,
        request: mpserverless_20190615_models.QueryDBBackupDumpTimesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.QueryDBBackupDumpTimesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.QueryDBBackupDumpTimesResponse(),
            self.do_rpcrequest('QueryDBBackupDumpTimes', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_dbbackup_dump_times_with_options_async(
        self,
        request: mpserverless_20190615_models.QueryDBBackupDumpTimesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.QueryDBBackupDumpTimesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.QueryDBBackupDumpTimesResponse(),
            await self.do_rpcrequest_async('QueryDBBackupDumpTimes', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_dbbackup_dump_times(
        self,
        request: mpserverless_20190615_models.QueryDBBackupDumpTimesRequest,
    ) -> mpserverless_20190615_models.QueryDBBackupDumpTimesResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_dbbackup_dump_times_with_options(request, runtime)

    async def query_dbbackup_dump_times_async(
        self,
        request: mpserverless_20190615_models.QueryDBBackupDumpTimesRequest,
    ) -> mpserverless_20190615_models.QueryDBBackupDumpTimesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_dbbackup_dump_times_with_options_async(request, runtime)

    def deploy_function_with_options(
        self,
        request: mpserverless_20190615_models.DeployFunctionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.DeployFunctionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.DeployFunctionResponse(),
            self.do_rpcrequest('DeployFunction', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def deploy_function_with_options_async(
        self,
        request: mpserverless_20190615_models.DeployFunctionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.DeployFunctionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.DeployFunctionResponse(),
            await self.do_rpcrequest_async('DeployFunction', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def deploy_function(
        self,
        request: mpserverless_20190615_models.DeployFunctionRequest,
    ) -> mpserverless_20190615_models.DeployFunctionResponse:
        runtime = util_models.RuntimeOptions()
        return self.deploy_function_with_options(request, runtime)

    async def deploy_function_async(
        self,
        request: mpserverless_20190615_models.DeployFunctionRequest,
    ) -> mpserverless_20190615_models.DeployFunctionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.deploy_function_with_options_async(request, runtime)

    def attach_sms_sign_with_options(
        self,
        request: mpserverless_20190615_models.AttachSmsSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.AttachSmsSignResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.AttachSmsSignResponse(),
            self.do_rpcrequest('AttachSmsSign', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def attach_sms_sign_with_options_async(
        self,
        request: mpserverless_20190615_models.AttachSmsSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.AttachSmsSignResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.AttachSmsSignResponse(),
            await self.do_rpcrequest_async('AttachSmsSign', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def attach_sms_sign(
        self,
        request: mpserverless_20190615_models.AttachSmsSignRequest,
    ) -> mpserverless_20190615_models.AttachSmsSignResponse:
        runtime = util_models.RuntimeOptions()
        return self.attach_sms_sign_with_options(request, runtime)

    async def attach_sms_sign_async(
        self,
        request: mpserverless_20190615_models.AttachSmsSignRequest,
    ) -> mpserverless_20190615_models.AttachSmsSignResponse:
        runtime = util_models.RuntimeOptions()
        return await self.attach_sms_sign_with_options_async(request, runtime)

    def update_service_policy_with_options(
        self,
        request: mpserverless_20190615_models.UpdateServicePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.UpdateServicePolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.UpdateServicePolicyResponse(),
            self.do_rpcrequest('UpdateServicePolicy', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_service_policy_with_options_async(
        self,
        request: mpserverless_20190615_models.UpdateServicePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.UpdateServicePolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.UpdateServicePolicyResponse(),
            await self.do_rpcrequest_async('UpdateServicePolicy', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_service_policy(
        self,
        request: mpserverless_20190615_models.UpdateServicePolicyRequest,
    ) -> mpserverless_20190615_models.UpdateServicePolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_service_policy_with_options(request, runtime)

    async def update_service_policy_async(
        self,
        request: mpserverless_20190615_models.UpdateServicePolicyRequest,
    ) -> mpserverless_20190615_models.UpdateServicePolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_service_policy_with_options_async(request, runtime)

    def add_cors_domain_with_options(
        self,
        request: mpserverless_20190615_models.AddCorsDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.AddCorsDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.AddCorsDomainResponse(),
            self.do_rpcrequest('AddCorsDomain', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_cors_domain_with_options_async(
        self,
        request: mpserverless_20190615_models.AddCorsDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.AddCorsDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.AddCorsDomainResponse(),
            await self.do_rpcrequest_async('AddCorsDomain', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_cors_domain(
        self,
        request: mpserverless_20190615_models.AddCorsDomainRequest,
    ) -> mpserverless_20190615_models.AddCorsDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_cors_domain_with_options(request, runtime)

    async def add_cors_domain_async(
        self,
        request: mpserverless_20190615_models.AddCorsDomainRequest,
    ) -> mpserverless_20190615_models.AddCorsDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_cors_domain_with_options_async(request, runtime)

    def describe_web_hosting_file_with_options(
        self,
        request: mpserverless_20190615_models.DescribeWebHostingFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.DescribeWebHostingFileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.DescribeWebHostingFileResponse(),
            self.do_rpcrequest('DescribeWebHostingFile', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_web_hosting_file_with_options_async(
        self,
        request: mpserverless_20190615_models.DescribeWebHostingFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.DescribeWebHostingFileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.DescribeWebHostingFileResponse(),
            await self.do_rpcrequest_async('DescribeWebHostingFile', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_web_hosting_file(
        self,
        request: mpserverless_20190615_models.DescribeWebHostingFileRequest,
    ) -> mpserverless_20190615_models.DescribeWebHostingFileResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_web_hosting_file_with_options(request, runtime)

    async def describe_web_hosting_file_async(
        self,
        request: mpserverless_20190615_models.DescribeWebHostingFileRequest,
    ) -> mpserverless_20190615_models.DescribeWebHostingFileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_web_hosting_file_with_options_async(request, runtime)

    def update_sms_template_with_options(
        self,
        request: mpserverless_20190615_models.UpdateSmsTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.UpdateSmsTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.UpdateSmsTemplateResponse(),
            self.do_rpcrequest('UpdateSmsTemplate', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_sms_template_with_options_async(
        self,
        request: mpserverless_20190615_models.UpdateSmsTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.UpdateSmsTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.UpdateSmsTemplateResponse(),
            await self.do_rpcrequest_async('UpdateSmsTemplate', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_sms_template(
        self,
        request: mpserverless_20190615_models.UpdateSmsTemplateRequest,
    ) -> mpserverless_20190615_models.UpdateSmsTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_sms_template_with_options(request, runtime)

    async def update_sms_template_async(
        self,
        request: mpserverless_20190615_models.UpdateSmsTemplateRequest,
    ) -> mpserverless_20190615_models.UpdateSmsTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_sms_template_with_options_async(request, runtime)

    def verify_builtin_function_template_with_options(
        self,
        request: mpserverless_20190615_models.VerifyBuiltinFunctionTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.VerifyBuiltinFunctionTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.VerifyBuiltinFunctionTemplateResponse(),
            self.do_rpcrequest('VerifyBuiltinFunctionTemplate', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def verify_builtin_function_template_with_options_async(
        self,
        request: mpserverless_20190615_models.VerifyBuiltinFunctionTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.VerifyBuiltinFunctionTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.VerifyBuiltinFunctionTemplateResponse(),
            await self.do_rpcrequest_async('VerifyBuiltinFunctionTemplate', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def verify_builtin_function_template(
        self,
        request: mpserverless_20190615_models.VerifyBuiltinFunctionTemplateRequest,
    ) -> mpserverless_20190615_models.VerifyBuiltinFunctionTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.verify_builtin_function_template_with_options(request, runtime)

    async def verify_builtin_function_template_async(
        self,
        request: mpserverless_20190615_models.VerifyBuiltinFunctionTemplateRequest,
    ) -> mpserverless_20190615_models.VerifyBuiltinFunctionTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.verify_builtin_function_template_with_options_async(request, runtime)

    def delete_web_hosting_file_with_options(
        self,
        request: mpserverless_20190615_models.DeleteWebHostingFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.DeleteWebHostingFileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.DeleteWebHostingFileResponse(),
            self.do_rpcrequest('DeleteWebHostingFile', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_web_hosting_file_with_options_async(
        self,
        request: mpserverless_20190615_models.DeleteWebHostingFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.DeleteWebHostingFileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.DeleteWebHostingFileResponse(),
            await self.do_rpcrequest_async('DeleteWebHostingFile', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_web_hosting_file(
        self,
        request: mpserverless_20190615_models.DeleteWebHostingFileRequest,
    ) -> mpserverless_20190615_models.DeleteWebHostingFileResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_web_hosting_file_with_options(request, runtime)

    async def delete_web_hosting_file_async(
        self,
        request: mpserverless_20190615_models.DeleteWebHostingFileRequest,
    ) -> mpserverless_20190615_models.DeleteWebHostingFileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_web_hosting_file_with_options_async(request, runtime)

    def list_web_hosting_custom_domains_with_options(
        self,
        request: mpserverless_20190615_models.ListWebHostingCustomDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.ListWebHostingCustomDomainsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.ListWebHostingCustomDomainsResponse(),
            self.do_rpcrequest('ListWebHostingCustomDomains', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_web_hosting_custom_domains_with_options_async(
        self,
        request: mpserverless_20190615_models.ListWebHostingCustomDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.ListWebHostingCustomDomainsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.ListWebHostingCustomDomainsResponse(),
            await self.do_rpcrequest_async('ListWebHostingCustomDomains', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_web_hosting_custom_domains(
        self,
        request: mpserverless_20190615_models.ListWebHostingCustomDomainsRequest,
    ) -> mpserverless_20190615_models.ListWebHostingCustomDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_web_hosting_custom_domains_with_options(request, runtime)

    async def list_web_hosting_custom_domains_async(
        self,
        request: mpserverless_20190615_models.ListWebHostingCustomDomainsRequest,
    ) -> mpserverless_20190615_models.ListWebHostingCustomDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_web_hosting_custom_domains_with_options_async(request, runtime)

    def run_dbcommand_with_options(
        self,
        request: mpserverless_20190615_models.RunDBCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.RunDBCommandResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.RunDBCommandResponse(),
            self.do_rpcrequest('RunDBCommand', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def run_dbcommand_with_options_async(
        self,
        request: mpserverless_20190615_models.RunDBCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.RunDBCommandResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.RunDBCommandResponse(),
            await self.do_rpcrequest_async('RunDBCommand', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def run_dbcommand(
        self,
        request: mpserverless_20190615_models.RunDBCommandRequest,
    ) -> mpserverless_20190615_models.RunDBCommandResponse:
        runtime = util_models.RuntimeOptions()
        return self.run_dbcommand_with_options(request, runtime)

    async def run_dbcommand_async(
        self,
        request: mpserverless_20190615_models.RunDBCommandRequest,
    ) -> mpserverless_20190615_models.RunDBCommandResponse:
        runtime = util_models.RuntimeOptions()
        return await self.run_dbcommand_with_options_async(request, runtime)

    def delete_function_with_options(
        self,
        request: mpserverless_20190615_models.DeleteFunctionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.DeleteFunctionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.DeleteFunctionResponse(),
            self.do_rpcrequest('DeleteFunction', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_function_with_options_async(
        self,
        request: mpserverless_20190615_models.DeleteFunctionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mpserverless_20190615_models.DeleteFunctionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mpserverless_20190615_models.DeleteFunctionResponse(),
            await self.do_rpcrequest_async('DeleteFunction', '2019-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_function(
        self,
        request: mpserverless_20190615_models.DeleteFunctionRequest,
    ) -> mpserverless_20190615_models.DeleteFunctionResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_function_with_options(request, runtime)

    async def delete_function_async(
        self,
        request: mpserverless_20190615_models.DeleteFunctionRequest,
    ) -> mpserverless_20190615_models.DeleteFunctionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_function_with_options_async(request, runtime)
