# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_mhub20170825 import models as mhub_20170825_models
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
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('mhub', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_app_with_options(
        self,
        request: mhub_20170825_models.CreateAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mhub_20170825_models.CreateAppResponse:
        """
        @param request: CreateAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAppResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bundle_id):
            query['BundleId'] = request.bundle_id
        if not UtilClient.is_unset(request.encoded_icon):
            query['EncodedIcon'] = request.encoded_icon
        if not UtilClient.is_unset(request.industry_id):
            query['IndustryId'] = request.industry_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.package_name):
            query['PackageName'] = request.package_name
        if not UtilClient.is_unset(request.product_id):
            query['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateApp',
            version='2017-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                mhub_20170825_models.CreateAppResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                mhub_20170825_models.CreateAppResponse(),
                self.execute(params, req, runtime)
            )

    async def create_app_with_options_async(
        self,
        request: mhub_20170825_models.CreateAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mhub_20170825_models.CreateAppResponse:
        """
        @param request: CreateAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAppResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bundle_id):
            query['BundleId'] = request.bundle_id
        if not UtilClient.is_unset(request.encoded_icon):
            query['EncodedIcon'] = request.encoded_icon
        if not UtilClient.is_unset(request.industry_id):
            query['IndustryId'] = request.industry_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.package_name):
            query['PackageName'] = request.package_name
        if not UtilClient.is_unset(request.product_id):
            query['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateApp',
            version='2017-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                mhub_20170825_models.CreateAppResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                mhub_20170825_models.CreateAppResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_app(
        self,
        request: mhub_20170825_models.CreateAppRequest,
    ) -> mhub_20170825_models.CreateAppResponse:
        """
        @param request: CreateAppRequest
        @return: CreateAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_app_with_options(request, runtime)

    async def create_app_async(
        self,
        request: mhub_20170825_models.CreateAppRequest,
    ) -> mhub_20170825_models.CreateAppResponse:
        """
        @param request: CreateAppRequest
        @return: CreateAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_app_with_options_async(request, runtime)

    def create_product_with_options(
        self,
        request: mhub_20170825_models.CreateProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mhub_20170825_models.CreateProductResponse:
        """
        @param request: CreateProductRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateProductResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateProduct',
            version='2017-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                mhub_20170825_models.CreateProductResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                mhub_20170825_models.CreateProductResponse(),
                self.execute(params, req, runtime)
            )

    async def create_product_with_options_async(
        self,
        request: mhub_20170825_models.CreateProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mhub_20170825_models.CreateProductResponse:
        """
        @param request: CreateProductRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateProductResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateProduct',
            version='2017-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                mhub_20170825_models.CreateProductResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                mhub_20170825_models.CreateProductResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_product(
        self,
        request: mhub_20170825_models.CreateProductRequest,
    ) -> mhub_20170825_models.CreateProductResponse:
        """
        @param request: CreateProductRequest
        @return: CreateProductResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_product_with_options(request, runtime)

    async def create_product_async(
        self,
        request: mhub_20170825_models.CreateProductRequest,
    ) -> mhub_20170825_models.CreateProductResponse:
        """
        @param request: CreateProductRequest
        @return: CreateProductResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_product_with_options_async(request, runtime)

    def delete_app_with_options(
        self,
        request: mhub_20170825_models.DeleteAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mhub_20170825_models.DeleteAppResponse:
        """
        @param request: DeleteAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAppResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApp',
            version='2017-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                mhub_20170825_models.DeleteAppResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                mhub_20170825_models.DeleteAppResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_app_with_options_async(
        self,
        request: mhub_20170825_models.DeleteAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mhub_20170825_models.DeleteAppResponse:
        """
        @param request: DeleteAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAppResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApp',
            version='2017-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                mhub_20170825_models.DeleteAppResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                mhub_20170825_models.DeleteAppResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_app(
        self,
        request: mhub_20170825_models.DeleteAppRequest,
    ) -> mhub_20170825_models.DeleteAppResponse:
        """
        @param request: DeleteAppRequest
        @return: DeleteAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_app_with_options(request, runtime)

    async def delete_app_async(
        self,
        request: mhub_20170825_models.DeleteAppRequest,
    ) -> mhub_20170825_models.DeleteAppResponse:
        """
        @param request: DeleteAppRequest
        @return: DeleteAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_app_with_options_async(request, runtime)

    def delete_product_with_options(
        self,
        request: mhub_20170825_models.DeleteProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mhub_20170825_models.DeleteProductResponse:
        """
        @param request: DeleteProductRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteProductResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.product_id):
            query['ProductId'] = request.product_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteProduct',
            version='2017-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                mhub_20170825_models.DeleteProductResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                mhub_20170825_models.DeleteProductResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_product_with_options_async(
        self,
        request: mhub_20170825_models.DeleteProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mhub_20170825_models.DeleteProductResponse:
        """
        @param request: DeleteProductRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteProductResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.product_id):
            query['ProductId'] = request.product_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteProduct',
            version='2017-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                mhub_20170825_models.DeleteProductResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                mhub_20170825_models.DeleteProductResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_product(
        self,
        request: mhub_20170825_models.DeleteProductRequest,
    ) -> mhub_20170825_models.DeleteProductResponse:
        """
        @param request: DeleteProductRequest
        @return: DeleteProductResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_product_with_options(request, runtime)

    async def delete_product_async(
        self,
        request: mhub_20170825_models.DeleteProductRequest,
    ) -> mhub_20170825_models.DeleteProductResponse:
        """
        @param request: DeleteProductRequest
        @return: DeleteProductResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_product_with_options_async(request, runtime)

    def describe_dashboard_with_options(
        self,
        request: mhub_20170825_models.DescribeDashboardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mhub_20170825_models.DescribeDashboardResponse:
        """
        @summary 获取emas dashboard
        
        @param request: DescribeDashboardRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDashboardResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.app_type):
            query['AppType'] = request.app_type
        if not UtilClient.is_unset(request.app_version):
            query['AppVersion'] = request.app_version
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.proxy_action):
            query['ProxyAction'] = request.proxy_action
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDashboard',
            version='2017-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                mhub_20170825_models.DescribeDashboardResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                mhub_20170825_models.DescribeDashboardResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_dashboard_with_options_async(
        self,
        request: mhub_20170825_models.DescribeDashboardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mhub_20170825_models.DescribeDashboardResponse:
        """
        @summary 获取emas dashboard
        
        @param request: DescribeDashboardRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDashboardResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.app_type):
            query['AppType'] = request.app_type
        if not UtilClient.is_unset(request.app_version):
            query['AppVersion'] = request.app_version
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.proxy_action):
            query['ProxyAction'] = request.proxy_action
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDashboard',
            version='2017-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                mhub_20170825_models.DescribeDashboardResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                mhub_20170825_models.DescribeDashboardResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_dashboard(
        self,
        request: mhub_20170825_models.DescribeDashboardRequest,
    ) -> mhub_20170825_models.DescribeDashboardResponse:
        """
        @summary 获取emas dashboard
        
        @param request: DescribeDashboardRequest
        @return: DescribeDashboardResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dashboard_with_options(request, runtime)

    async def describe_dashboard_async(
        self,
        request: mhub_20170825_models.DescribeDashboardRequest,
    ) -> mhub_20170825_models.DescribeDashboardResponse:
        """
        @summary 获取emas dashboard
        
        @param request: DescribeDashboardRequest
        @return: DescribeDashboardResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dashboard_with_options_async(request, runtime)

    def list_apps_with_options(
        self,
        request: mhub_20170825_models.ListAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mhub_20170825_models.ListAppsResponse:
        """
        @summary 展示用户应用列表
        
        @param request: ListAppsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAppsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.os_type):
            query['OsType'] = request.os_type
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_id):
            query['ProductId'] = request.product_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApps',
            version='2017-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                mhub_20170825_models.ListAppsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                mhub_20170825_models.ListAppsResponse(),
                self.execute(params, req, runtime)
            )

    async def list_apps_with_options_async(
        self,
        request: mhub_20170825_models.ListAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mhub_20170825_models.ListAppsResponse:
        """
        @summary 展示用户应用列表
        
        @param request: ListAppsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAppsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.os_type):
            query['OsType'] = request.os_type
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_id):
            query['ProductId'] = request.product_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApps',
            version='2017-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                mhub_20170825_models.ListAppsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                mhub_20170825_models.ListAppsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_apps(
        self,
        request: mhub_20170825_models.ListAppsRequest,
    ) -> mhub_20170825_models.ListAppsResponse:
        """
        @summary 展示用户应用列表
        
        @param request: ListAppsRequest
        @return: ListAppsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_apps_with_options(request, runtime)

    async def list_apps_async(
        self,
        request: mhub_20170825_models.ListAppsRequest,
    ) -> mhub_20170825_models.ListAppsResponse:
        """
        @summary 展示用户应用列表
        
        @param request: ListAppsRequest
        @return: ListAppsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_apps_with_options_async(request, runtime)

    def list_products_with_options(
        self,
        request: mhub_20170825_models.ListProductsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mhub_20170825_models.ListProductsResponse:
        """
        @param request: ListProductsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListProductsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.offset):
            query['Offset'] = request.offset
        if not UtilClient.is_unset(request.product_name):
            query['ProductName'] = request.product_name
        if not UtilClient.is_unset(request.simple):
            query['Simple'] = request.simple
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProducts',
            version='2017-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                mhub_20170825_models.ListProductsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                mhub_20170825_models.ListProductsResponse(),
                self.execute(params, req, runtime)
            )

    async def list_products_with_options_async(
        self,
        request: mhub_20170825_models.ListProductsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mhub_20170825_models.ListProductsResponse:
        """
        @param request: ListProductsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListProductsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.offset):
            query['Offset'] = request.offset
        if not UtilClient.is_unset(request.product_name):
            query['ProductName'] = request.product_name
        if not UtilClient.is_unset(request.simple):
            query['Simple'] = request.simple
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProducts',
            version='2017-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                mhub_20170825_models.ListProductsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                mhub_20170825_models.ListProductsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_products(
        self,
        request: mhub_20170825_models.ListProductsRequest,
    ) -> mhub_20170825_models.ListProductsResponse:
        """
        @param request: ListProductsRequest
        @return: ListProductsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_products_with_options(request, runtime)

    async def list_products_async(
        self,
        request: mhub_20170825_models.ListProductsRequest,
    ) -> mhub_20170825_models.ListProductsResponse:
        """
        @param request: ListProductsRequest
        @return: ListProductsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_products_with_options_async(request, runtime)

    def modify_app_with_options(
        self,
        request: mhub_20170825_models.ModifyAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mhub_20170825_models.ModifyAppResponse:
        """
        @param request: ModifyAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAppResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.bundle_id):
            query['BundleId'] = request.bundle_id
        if not UtilClient.is_unset(request.encoded_icon):
            query['EncodedIcon'] = request.encoded_icon
        if not UtilClient.is_unset(request.industry_id):
            query['IndustryId'] = request.industry_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.package_name):
            query['PackageName'] = request.package_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyApp',
            version='2017-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                mhub_20170825_models.ModifyAppResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                mhub_20170825_models.ModifyAppResponse(),
                self.execute(params, req, runtime)
            )

    async def modify_app_with_options_async(
        self,
        request: mhub_20170825_models.ModifyAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mhub_20170825_models.ModifyAppResponse:
        """
        @param request: ModifyAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAppResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.bundle_id):
            query['BundleId'] = request.bundle_id
        if not UtilClient.is_unset(request.encoded_icon):
            query['EncodedIcon'] = request.encoded_icon
        if not UtilClient.is_unset(request.industry_id):
            query['IndustryId'] = request.industry_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.package_name):
            query['PackageName'] = request.package_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyApp',
            version='2017-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                mhub_20170825_models.ModifyAppResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                mhub_20170825_models.ModifyAppResponse(),
                await self.execute_async(params, req, runtime)
            )

    def modify_app(
        self,
        request: mhub_20170825_models.ModifyAppRequest,
    ) -> mhub_20170825_models.ModifyAppResponse:
        """
        @param request: ModifyAppRequest
        @return: ModifyAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_app_with_options(request, runtime)

    async def modify_app_async(
        self,
        request: mhub_20170825_models.ModifyAppRequest,
    ) -> mhub_20170825_models.ModifyAppResponse:
        """
        @param request: ModifyAppRequest
        @return: ModifyAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_app_with_options_async(request, runtime)

    def modify_product_with_options(
        self,
        request: mhub_20170825_models.ModifyProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mhub_20170825_models.ModifyProductResponse:
        """
        @param request: ModifyProductRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyProductResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.product_id):
            query['ProductId'] = request.product_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyProduct',
            version='2017-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                mhub_20170825_models.ModifyProductResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                mhub_20170825_models.ModifyProductResponse(),
                self.execute(params, req, runtime)
            )

    async def modify_product_with_options_async(
        self,
        request: mhub_20170825_models.ModifyProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mhub_20170825_models.ModifyProductResponse:
        """
        @param request: ModifyProductRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyProductResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.product_id):
            query['ProductId'] = request.product_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyProduct',
            version='2017-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                mhub_20170825_models.ModifyProductResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                mhub_20170825_models.ModifyProductResponse(),
                await self.execute_async(params, req, runtime)
            )

    def modify_product(
        self,
        request: mhub_20170825_models.ModifyProductRequest,
    ) -> mhub_20170825_models.ModifyProductResponse:
        """
        @param request: ModifyProductRequest
        @return: ModifyProductResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_product_with_options(request, runtime)

    async def modify_product_async(
        self,
        request: mhub_20170825_models.ModifyProductRequest,
    ) -> mhub_20170825_models.ModifyProductResponse:
        """
        @param request: ModifyProductRequest
        @return: ModifyProductResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_product_with_options_async(request, runtime)

    def open_emas_service_with_options(
        self,
        request: mhub_20170825_models.OpenEmasServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mhub_20170825_models.OpenEmasServiceResponse:
        """
        @param request: OpenEmasServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OpenEmasServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenEmasService',
            version='2017-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                mhub_20170825_models.OpenEmasServiceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                mhub_20170825_models.OpenEmasServiceResponse(),
                self.execute(params, req, runtime)
            )

    async def open_emas_service_with_options_async(
        self,
        request: mhub_20170825_models.OpenEmasServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mhub_20170825_models.OpenEmasServiceResponse:
        """
        @param request: OpenEmasServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OpenEmasServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenEmasService',
            version='2017-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                mhub_20170825_models.OpenEmasServiceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                mhub_20170825_models.OpenEmasServiceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def open_emas_service(
        self,
        request: mhub_20170825_models.OpenEmasServiceRequest,
    ) -> mhub_20170825_models.OpenEmasServiceResponse:
        """
        @param request: OpenEmasServiceRequest
        @return: OpenEmasServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.open_emas_service_with_options(request, runtime)

    async def open_emas_service_async(
        self,
        request: mhub_20170825_models.OpenEmasServiceRequest,
    ) -> mhub_20170825_models.OpenEmasServiceResponse:
        """
        @param request: OpenEmasServiceRequest
        @return: OpenEmasServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.open_emas_service_with_options_async(request, runtime)

    def query_app_info_with_options(
        self,
        request: mhub_20170825_models.QueryAppInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mhub_20170825_models.QueryAppInfoResponse:
        """
        @param request: QueryAppInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryAppInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAppInfo',
            version='2017-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                mhub_20170825_models.QueryAppInfoResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                mhub_20170825_models.QueryAppInfoResponse(),
                self.execute(params, req, runtime)
            )

    async def query_app_info_with_options_async(
        self,
        request: mhub_20170825_models.QueryAppInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mhub_20170825_models.QueryAppInfoResponse:
        """
        @param request: QueryAppInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryAppInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAppInfo',
            version='2017-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                mhub_20170825_models.QueryAppInfoResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                mhub_20170825_models.QueryAppInfoResponse(),
                await self.execute_async(params, req, runtime)
            )

    def query_app_info(
        self,
        request: mhub_20170825_models.QueryAppInfoRequest,
    ) -> mhub_20170825_models.QueryAppInfoResponse:
        """
        @param request: QueryAppInfoRequest
        @return: QueryAppInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_app_info_with_options(request, runtime)

    async def query_app_info_async(
        self,
        request: mhub_20170825_models.QueryAppInfoRequest,
    ) -> mhub_20170825_models.QueryAppInfoResponse:
        """
        @param request: QueryAppInfoRequest
        @return: QueryAppInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_app_info_with_options_async(request, runtime)

    def query_app_security_info_with_options(
        self,
        request: mhub_20170825_models.QueryAppSecurityInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mhub_20170825_models.QueryAppSecurityInfoResponse:
        """
        @summary 查询应用对应的安全字段
        
        @param request: QueryAppSecurityInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryAppSecurityInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAppSecurityInfo',
            version='2017-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                mhub_20170825_models.QueryAppSecurityInfoResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                mhub_20170825_models.QueryAppSecurityInfoResponse(),
                self.execute(params, req, runtime)
            )

    async def query_app_security_info_with_options_async(
        self,
        request: mhub_20170825_models.QueryAppSecurityInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mhub_20170825_models.QueryAppSecurityInfoResponse:
        """
        @summary 查询应用对应的安全字段
        
        @param request: QueryAppSecurityInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryAppSecurityInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAppSecurityInfo',
            version='2017-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                mhub_20170825_models.QueryAppSecurityInfoResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                mhub_20170825_models.QueryAppSecurityInfoResponse(),
                await self.execute_async(params, req, runtime)
            )

    def query_app_security_info(
        self,
        request: mhub_20170825_models.QueryAppSecurityInfoRequest,
    ) -> mhub_20170825_models.QueryAppSecurityInfoResponse:
        """
        @summary 查询应用对应的安全字段
        
        @param request: QueryAppSecurityInfoRequest
        @return: QueryAppSecurityInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_app_security_info_with_options(request, runtime)

    async def query_app_security_info_async(
        self,
        request: mhub_20170825_models.QueryAppSecurityInfoRequest,
    ) -> mhub_20170825_models.QueryAppSecurityInfoResponse:
        """
        @summary 查询应用对应的安全字段
        
        @param request: QueryAppSecurityInfoRequest
        @return: QueryAppSecurityInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_app_security_info_with_options_async(request, runtime)

    def query_product_info_with_options(
        self,
        request: mhub_20170825_models.QueryProductInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mhub_20170825_models.QueryProductInfoResponse:
        """
        @param request: QueryProductInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryProductInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.product_id):
            query['ProductId'] = request.product_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryProductInfo',
            version='2017-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                mhub_20170825_models.QueryProductInfoResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                mhub_20170825_models.QueryProductInfoResponse(),
                self.execute(params, req, runtime)
            )

    async def query_product_info_with_options_async(
        self,
        request: mhub_20170825_models.QueryProductInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mhub_20170825_models.QueryProductInfoResponse:
        """
        @param request: QueryProductInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryProductInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.product_id):
            query['ProductId'] = request.product_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryProductInfo',
            version='2017-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                mhub_20170825_models.QueryProductInfoResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                mhub_20170825_models.QueryProductInfoResponse(),
                await self.execute_async(params, req, runtime)
            )

    def query_product_info(
        self,
        request: mhub_20170825_models.QueryProductInfoRequest,
    ) -> mhub_20170825_models.QueryProductInfoResponse:
        """
        @param request: QueryProductInfoRequest
        @return: QueryProductInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_product_info_with_options(request, runtime)

    async def query_product_info_async(
        self,
        request: mhub_20170825_models.QueryProductInfoRequest,
    ) -> mhub_20170825_models.QueryProductInfoResponse:
        """
        @param request: QueryProductInfoRequest
        @return: QueryProductInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_product_info_with_options_async(request, runtime)
