# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_wuying_personal_pc20251111 import models as wuying_personal_pc_20251111_models
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
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('wuying-personal-pc', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_desktop_image_with_options(
        self,
        tmp_req: wuying_personal_pc_20251111_models.CreateDesktopImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wuying_personal_pc_20251111_models.CreateDesktopImageResponse:
        """
        @summary 创建桌面镜像
        
        @param tmp_req: CreateDesktopImageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDesktopImageResponse
        """
        UtilClient.validate_model(tmp_req)
        request = wuying_personal_pc_20251111_models.CreateDesktopImageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.start_up_file_path_list):
            request.start_up_file_path_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.start_up_file_path_list, 'StartUpFilePathList', 'json')
        query = {}
        if not UtilClient.is_unset(request.api_key):
            query['ApiKey'] = request.api_key
        if not UtilClient.is_unset(request.auto_clean_user_data):
            query['AutoCleanUserData'] = request.auto_clean_user_data
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.disk_type):
            query['DiskType'] = request.disk_type
        if not UtilClient.is_unset(request.enable_start_up_config):
            query['EnableStartUpConfig'] = request.enable_start_up_config
        if not UtilClient.is_unset(request.image_name):
            query['ImageName'] = request.image_name
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.start_up_file_path_list_shrink):
            query['StartUpFilePathList'] = request.start_up_file_path_list_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDesktopImage',
            version='2025-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wuying_personal_pc_20251111_models.CreateDesktopImageResponse(),
            self.do_rpcrequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    async def create_desktop_image_with_options_async(
        self,
        tmp_req: wuying_personal_pc_20251111_models.CreateDesktopImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wuying_personal_pc_20251111_models.CreateDesktopImageResponse:
        """
        @summary 创建桌面镜像
        
        @param tmp_req: CreateDesktopImageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDesktopImageResponse
        """
        UtilClient.validate_model(tmp_req)
        request = wuying_personal_pc_20251111_models.CreateDesktopImageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.start_up_file_path_list):
            request.start_up_file_path_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.start_up_file_path_list, 'StartUpFilePathList', 'json')
        query = {}
        if not UtilClient.is_unset(request.api_key):
            query['ApiKey'] = request.api_key
        if not UtilClient.is_unset(request.auto_clean_user_data):
            query['AutoCleanUserData'] = request.auto_clean_user_data
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.disk_type):
            query['DiskType'] = request.disk_type
        if not UtilClient.is_unset(request.enable_start_up_config):
            query['EnableStartUpConfig'] = request.enable_start_up_config
        if not UtilClient.is_unset(request.image_name):
            query['ImageName'] = request.image_name
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.start_up_file_path_list_shrink):
            query['StartUpFilePathList'] = request.start_up_file_path_list_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDesktopImage',
            version='2025-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wuying_personal_pc_20251111_models.CreateDesktopImageResponse(),
            await self.do_rpcrequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    def create_desktop_image(
        self,
        request: wuying_personal_pc_20251111_models.CreateDesktopImageRequest,
    ) -> wuying_personal_pc_20251111_models.CreateDesktopImageResponse:
        """
        @summary 创建桌面镜像
        
        @param request: CreateDesktopImageRequest
        @return: CreateDesktopImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_desktop_image_with_options(request, runtime)

    async def create_desktop_image_async(
        self,
        request: wuying_personal_pc_20251111_models.CreateDesktopImageRequest,
    ) -> wuying_personal_pc_20251111_models.CreateDesktopImageResponse:
        """
        @summary 创建桌面镜像
        
        @param request: CreateDesktopImageRequest
        @return: CreateDesktopImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_desktop_image_with_options_async(request, runtime)

    def create_order_with_options(
        self,
        tmp_req: wuying_personal_pc_20251111_models.CreateOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wuying_personal_pc_20251111_models.CreateOrderResponse:
        """
        @summary 下单套餐包和核时包
        
        @param tmp_req: CreateOrderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateOrderResponse
        """
        UtilClient.validate_model(tmp_req)
        request = wuying_personal_pc_20251111_models.CreateOrderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dynamic_product_params):
            request.dynamic_product_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dynamic_product_params, 'DynamicProductParams', 'json')
        query = {}
        if not UtilClient.is_unset(request.api_key):
            query['ApiKey'] = request.api_key
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.dynamic_product_params_shrink):
            query['DynamicProductParams'] = request.dynamic_product_params_shrink
        if not UtilClient.is_unset(request.operation_type):
            query['OperationType'] = request.operation_type
        if not UtilClient.is_unset(request.order_from):
            query['OrderFrom'] = request.order_from
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateOrder',
            version='2025-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wuying_personal_pc_20251111_models.CreateOrderResponse(),
            self.do_rpcrequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    async def create_order_with_options_async(
        self,
        tmp_req: wuying_personal_pc_20251111_models.CreateOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wuying_personal_pc_20251111_models.CreateOrderResponse:
        """
        @summary 下单套餐包和核时包
        
        @param tmp_req: CreateOrderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateOrderResponse
        """
        UtilClient.validate_model(tmp_req)
        request = wuying_personal_pc_20251111_models.CreateOrderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dynamic_product_params):
            request.dynamic_product_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dynamic_product_params, 'DynamicProductParams', 'json')
        query = {}
        if not UtilClient.is_unset(request.api_key):
            query['ApiKey'] = request.api_key
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.dynamic_product_params_shrink):
            query['DynamicProductParams'] = request.dynamic_product_params_shrink
        if not UtilClient.is_unset(request.operation_type):
            query['OperationType'] = request.operation_type
        if not UtilClient.is_unset(request.order_from):
            query['OrderFrom'] = request.order_from
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateOrder',
            version='2025-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wuying_personal_pc_20251111_models.CreateOrderResponse(),
            await self.do_rpcrequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    def create_order(
        self,
        request: wuying_personal_pc_20251111_models.CreateOrderRequest,
    ) -> wuying_personal_pc_20251111_models.CreateOrderResponse:
        """
        @summary 下单套餐包和核时包
        
        @param request: CreateOrderRequest
        @return: CreateOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_order_with_options(request, runtime)

    async def create_order_async(
        self,
        request: wuying_personal_pc_20251111_models.CreateOrderRequest,
    ) -> wuying_personal_pc_20251111_models.CreateOrderResponse:
        """
        @summary 下单套餐包和核时包
        
        @param request: CreateOrderRequest
        @return: CreateOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_order_with_options_async(request, runtime)

    def delete_desktop_with_options(
        self,
        request: wuying_personal_pc_20251111_models.DeleteDesktopRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wuying_personal_pc_20251111_models.DeleteDesktopResponse:
        """
        @summary 删除云桌面
        
        @param request: DeleteDesktopRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDesktopResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_key):
            query['ApiKey'] = request.api_key
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDesktop',
            version='2025-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wuying_personal_pc_20251111_models.DeleteDesktopResponse(),
            self.do_rpcrequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    async def delete_desktop_with_options_async(
        self,
        request: wuying_personal_pc_20251111_models.DeleteDesktopRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wuying_personal_pc_20251111_models.DeleteDesktopResponse:
        """
        @summary 删除云桌面
        
        @param request: DeleteDesktopRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDesktopResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_key):
            query['ApiKey'] = request.api_key
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDesktop',
            version='2025-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wuying_personal_pc_20251111_models.DeleteDesktopResponse(),
            await self.do_rpcrequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    def delete_desktop(
        self,
        request: wuying_personal_pc_20251111_models.DeleteDesktopRequest,
    ) -> wuying_personal_pc_20251111_models.DeleteDesktopResponse:
        """
        @summary 删除云桌面
        
        @param request: DeleteDesktopRequest
        @return: DeleteDesktopResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_desktop_with_options(request, runtime)

    async def delete_desktop_async(
        self,
        request: wuying_personal_pc_20251111_models.DeleteDesktopRequest,
    ) -> wuying_personal_pc_20251111_models.DeleteDesktopResponse:
        """
        @summary 删除云桌面
        
        @param request: DeleteDesktopRequest
        @return: DeleteDesktopResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_desktop_with_options_async(request, runtime)

    def delete_desktop_image_with_options(
        self,
        request: wuying_personal_pc_20251111_models.DeleteDesktopImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wuying_personal_pc_20251111_models.DeleteDesktopImageResponse:
        """
        @summary 删除桌面镜像
        
        @param request: DeleteDesktopImageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDesktopImageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_key):
            query['ApiKey'] = request.api_key
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.is_clean_image_code):
            query['IsCleanImageCode'] = request.is_clean_image_code
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDesktopImage',
            version='2025-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wuying_personal_pc_20251111_models.DeleteDesktopImageResponse(),
            self.do_rpcrequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    async def delete_desktop_image_with_options_async(
        self,
        request: wuying_personal_pc_20251111_models.DeleteDesktopImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wuying_personal_pc_20251111_models.DeleteDesktopImageResponse:
        """
        @summary 删除桌面镜像
        
        @param request: DeleteDesktopImageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDesktopImageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_key):
            query['ApiKey'] = request.api_key
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.is_clean_image_code):
            query['IsCleanImageCode'] = request.is_clean_image_code
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDesktopImage',
            version='2025-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wuying_personal_pc_20251111_models.DeleteDesktopImageResponse(),
            await self.do_rpcrequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    def delete_desktop_image(
        self,
        request: wuying_personal_pc_20251111_models.DeleteDesktopImageRequest,
    ) -> wuying_personal_pc_20251111_models.DeleteDesktopImageResponse:
        """
        @summary 删除桌面镜像
        
        @param request: DeleteDesktopImageRequest
        @return: DeleteDesktopImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_desktop_image_with_options(request, runtime)

    async def delete_desktop_image_async(
        self,
        request: wuying_personal_pc_20251111_models.DeleteDesktopImageRequest,
    ) -> wuying_personal_pc_20251111_models.DeleteDesktopImageResponse:
        """
        @summary 删除桌面镜像
        
        @param request: DeleteDesktopImageRequest
        @return: DeleteDesktopImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_desktop_image_with_options_async(request, runtime)

    def describe_accessible_images_with_options(
        self,
        request: wuying_personal_pc_20251111_models.DescribeAccessibleImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wuying_personal_pc_20251111_models.DescribeAccessibleImagesResponse:
        """
        @summary 查询用户可变更的镜像
        
        @param request: DescribeAccessibleImagesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAccessibleImagesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_key):
            query['ApiKey'] = request.api_key
        if not UtilClient.is_unset(request.biz_source):
            query['BizSource'] = request.biz_source
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.desktop_type):
            query['DesktopType'] = request.desktop_type
        if not UtilClient.is_unset(request.image_type):
            query['ImageType'] = request.image_type
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.scene):
            query['Scene'] = request.scene
        if not UtilClient.is_unset(request.search_key):
            query['SearchKey'] = request.search_key
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccessibleImages',
            version='2025-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wuying_personal_pc_20251111_models.DescribeAccessibleImagesResponse(),
            self.do_rpcrequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    async def describe_accessible_images_with_options_async(
        self,
        request: wuying_personal_pc_20251111_models.DescribeAccessibleImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wuying_personal_pc_20251111_models.DescribeAccessibleImagesResponse:
        """
        @summary 查询用户可变更的镜像
        
        @param request: DescribeAccessibleImagesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAccessibleImagesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_key):
            query['ApiKey'] = request.api_key
        if not UtilClient.is_unset(request.biz_source):
            query['BizSource'] = request.biz_source
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.desktop_type):
            query['DesktopType'] = request.desktop_type
        if not UtilClient.is_unset(request.image_type):
            query['ImageType'] = request.image_type
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.scene):
            query['Scene'] = request.scene
        if not UtilClient.is_unset(request.search_key):
            query['SearchKey'] = request.search_key
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccessibleImages',
            version='2025-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wuying_personal_pc_20251111_models.DescribeAccessibleImagesResponse(),
            await self.do_rpcrequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    def describe_accessible_images(
        self,
        request: wuying_personal_pc_20251111_models.DescribeAccessibleImagesRequest,
    ) -> wuying_personal_pc_20251111_models.DescribeAccessibleImagesResponse:
        """
        @summary 查询用户可变更的镜像
        
        @param request: DescribeAccessibleImagesRequest
        @return: DescribeAccessibleImagesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_accessible_images_with_options(request, runtime)

    async def describe_accessible_images_async(
        self,
        request: wuying_personal_pc_20251111_models.DescribeAccessibleImagesRequest,
    ) -> wuying_personal_pc_20251111_models.DescribeAccessibleImagesResponse:
        """
        @summary 查询用户可变更的镜像
        
        @param request: DescribeAccessibleImagesRequest
        @return: DescribeAccessibleImagesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_accessible_images_with_options_async(request, runtime)

    def describe_core_package_list_with_options(
        self,
        request: wuying_personal_pc_20251111_models.DescribeCorePackageListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wuying_personal_pc_20251111_models.DescribeCorePackageListResponse:
        """
        @summary 查询核时包包列表
        
        @param request: DescribeCorePackageListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCorePackageListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_key):
            query['ApiKey'] = request.api_key
        if not UtilClient.is_unset(request.query_deduction_instances):
            query['QueryDeductionInstances'] = request.query_deduction_instances
        if not UtilClient.is_unset(request.query_scenario):
            query['QueryScenario'] = request.query_scenario
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCorePackageList',
            version='2025-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wuying_personal_pc_20251111_models.DescribeCorePackageListResponse(),
            self.do_rpcrequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    async def describe_core_package_list_with_options_async(
        self,
        request: wuying_personal_pc_20251111_models.DescribeCorePackageListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wuying_personal_pc_20251111_models.DescribeCorePackageListResponse:
        """
        @summary 查询核时包包列表
        
        @param request: DescribeCorePackageListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCorePackageListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_key):
            query['ApiKey'] = request.api_key
        if not UtilClient.is_unset(request.query_deduction_instances):
            query['QueryDeductionInstances'] = request.query_deduction_instances
        if not UtilClient.is_unset(request.query_scenario):
            query['QueryScenario'] = request.query_scenario
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCorePackageList',
            version='2025-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wuying_personal_pc_20251111_models.DescribeCorePackageListResponse(),
            await self.do_rpcrequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    def describe_core_package_list(
        self,
        request: wuying_personal_pc_20251111_models.DescribeCorePackageListRequest,
    ) -> wuying_personal_pc_20251111_models.DescribeCorePackageListResponse:
        """
        @summary 查询核时包包列表
        
        @param request: DescribeCorePackageListRequest
        @return: DescribeCorePackageListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_core_package_list_with_options(request, runtime)

    async def describe_core_package_list_async(
        self,
        request: wuying_personal_pc_20251111_models.DescribeCorePackageListRequest,
    ) -> wuying_personal_pc_20251111_models.DescribeCorePackageListResponse:
        """
        @summary 查询核时包包列表
        
        @param request: DescribeCorePackageListRequest
        @return: DescribeCorePackageListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_core_package_list_with_options_async(request, runtime)

    def describe_desktops_with_options(
        self,
        request: wuying_personal_pc_20251111_models.DescribeDesktopsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wuying_personal_pc_20251111_models.DescribeDesktopsResponse:
        """
        @summary 软终端分tab查询云桌面列表 & 组织信息
        
        @param request: DescribeDesktopsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDesktopsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_key):
            query['ApiKey'] = request.api_key
        if not UtilClient.is_unset(request.display_type):
            query['DisplayType'] = request.display_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDesktops',
            version='2025-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wuying_personal_pc_20251111_models.DescribeDesktopsResponse(),
            self.do_rpcrequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    async def describe_desktops_with_options_async(
        self,
        request: wuying_personal_pc_20251111_models.DescribeDesktopsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wuying_personal_pc_20251111_models.DescribeDesktopsResponse:
        """
        @summary 软终端分tab查询云桌面列表 & 组织信息
        
        @param request: DescribeDesktopsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDesktopsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_key):
            query['ApiKey'] = request.api_key
        if not UtilClient.is_unset(request.display_type):
            query['DisplayType'] = request.display_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDesktops',
            version='2025-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wuying_personal_pc_20251111_models.DescribeDesktopsResponse(),
            await self.do_rpcrequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    def describe_desktops(
        self,
        request: wuying_personal_pc_20251111_models.DescribeDesktopsRequest,
    ) -> wuying_personal_pc_20251111_models.DescribeDesktopsResponse:
        """
        @summary 软终端分tab查询云桌面列表 & 组织信息
        
        @param request: DescribeDesktopsRequest
        @return: DescribeDesktopsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_desktops_with_options(request, runtime)

    async def describe_desktops_async(
        self,
        request: wuying_personal_pc_20251111_models.DescribeDesktopsRequest,
    ) -> wuying_personal_pc_20251111_models.DescribeDesktopsResponse:
        """
        @summary 软终端分tab查询云桌面列表 & 组织信息
        
        @param request: DescribeDesktopsRequest
        @return: DescribeDesktopsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_desktops_with_options_async(request, runtime)

    def describe_image_detail_with_options(
        self,
        request: wuying_personal_pc_20251111_models.DescribeImageDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wuying_personal_pc_20251111_models.DescribeImageDetailResponse:
        """
        @summary 根据分享码查询镜像
        
        @param request: DescribeImageDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeImageDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_key):
            query['ApiKey'] = request.api_key
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.share_code):
            query['ShareCode'] = request.share_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImageDetail',
            version='2025-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wuying_personal_pc_20251111_models.DescribeImageDetailResponse(),
            self.do_rpcrequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    async def describe_image_detail_with_options_async(
        self,
        request: wuying_personal_pc_20251111_models.DescribeImageDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wuying_personal_pc_20251111_models.DescribeImageDetailResponse:
        """
        @summary 根据分享码查询镜像
        
        @param request: DescribeImageDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeImageDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_key):
            query['ApiKey'] = request.api_key
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.share_code):
            query['ShareCode'] = request.share_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImageDetail',
            version='2025-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wuying_personal_pc_20251111_models.DescribeImageDetailResponse(),
            await self.do_rpcrequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    def describe_image_detail(
        self,
        request: wuying_personal_pc_20251111_models.DescribeImageDetailRequest,
    ) -> wuying_personal_pc_20251111_models.DescribeImageDetailResponse:
        """
        @summary 根据分享码查询镜像
        
        @param request: DescribeImageDetailRequest
        @return: DescribeImageDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_image_detail_with_options(request, runtime)

    async def describe_image_detail_async(
        self,
        request: wuying_personal_pc_20251111_models.DescribeImageDetailRequest,
    ) -> wuying_personal_pc_20251111_models.DescribeImageDetailResponse:
        """
        @summary 根据分享码查询镜像
        
        @param request: DescribeImageDetailRequest
        @return: DescribeImageDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_image_detail_with_options_async(request, runtime)

    def describe_package_orders_with_options(
        self,
        tmp_req: wuying_personal_pc_20251111_models.DescribePackageOrdersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wuying_personal_pc_20251111_models.DescribePackageOrdersResponse:
        """
        @summary 查询套餐包订单列表
        
        @param tmp_req: DescribePackageOrdersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePackageOrdersResponse
        """
        UtilClient.validate_model(tmp_req)
        request = wuying_personal_pc_20251111_models.DescribePackageOrdersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.desktop_id_list):
            request.desktop_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.desktop_id_list, 'DesktopIdList', 'json')
        if not UtilClient.is_unset(tmp_req.order_id_list):
            request.order_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.order_id_list, 'OrderIdList', 'json')
        if not UtilClient.is_unset(tmp_req.order_status_list):
            request.order_status_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.order_status_list, 'OrderStatusList', 'json')
        if not UtilClient.is_unset(tmp_req.product_type_list):
            request.product_type_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.product_type_list, 'ProductTypeList', 'json')
        if not UtilClient.is_unset(tmp_req.resource_id_list):
            request.resource_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_id_list, 'ResourceIdList', 'json')
        query = {}
        if not UtilClient.is_unset(request.api_key):
            query['ApiKey'] = request.api_key
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.desktop_id_list_shrink):
            query['DesktopIdList'] = request.desktop_id_list_shrink
        if not UtilClient.is_unset(request.order_id_list_shrink):
            query['OrderIdList'] = request.order_id_list_shrink
        if not UtilClient.is_unset(request.order_status_list_shrink):
            query['OrderStatusList'] = request.order_status_list_shrink
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_type_list_shrink):
            query['ProductTypeList'] = request.product_type_list_shrink
        if not UtilClient.is_unset(request.resource_id_list_shrink):
            query['ResourceIdList'] = request.resource_id_list_shrink
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePackageOrders',
            version='2025-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wuying_personal_pc_20251111_models.DescribePackageOrdersResponse(),
            self.do_rpcrequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    async def describe_package_orders_with_options_async(
        self,
        tmp_req: wuying_personal_pc_20251111_models.DescribePackageOrdersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wuying_personal_pc_20251111_models.DescribePackageOrdersResponse:
        """
        @summary 查询套餐包订单列表
        
        @param tmp_req: DescribePackageOrdersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePackageOrdersResponse
        """
        UtilClient.validate_model(tmp_req)
        request = wuying_personal_pc_20251111_models.DescribePackageOrdersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.desktop_id_list):
            request.desktop_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.desktop_id_list, 'DesktopIdList', 'json')
        if not UtilClient.is_unset(tmp_req.order_id_list):
            request.order_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.order_id_list, 'OrderIdList', 'json')
        if not UtilClient.is_unset(tmp_req.order_status_list):
            request.order_status_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.order_status_list, 'OrderStatusList', 'json')
        if not UtilClient.is_unset(tmp_req.product_type_list):
            request.product_type_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.product_type_list, 'ProductTypeList', 'json')
        if not UtilClient.is_unset(tmp_req.resource_id_list):
            request.resource_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_id_list, 'ResourceIdList', 'json')
        query = {}
        if not UtilClient.is_unset(request.api_key):
            query['ApiKey'] = request.api_key
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.desktop_id_list_shrink):
            query['DesktopIdList'] = request.desktop_id_list_shrink
        if not UtilClient.is_unset(request.order_id_list_shrink):
            query['OrderIdList'] = request.order_id_list_shrink
        if not UtilClient.is_unset(request.order_status_list_shrink):
            query['OrderStatusList'] = request.order_status_list_shrink
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_type_list_shrink):
            query['ProductTypeList'] = request.product_type_list_shrink
        if not UtilClient.is_unset(request.resource_id_list_shrink):
            query['ResourceIdList'] = request.resource_id_list_shrink
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePackageOrders',
            version='2025-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wuying_personal_pc_20251111_models.DescribePackageOrdersResponse(),
            await self.do_rpcrequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    def describe_package_orders(
        self,
        request: wuying_personal_pc_20251111_models.DescribePackageOrdersRequest,
    ) -> wuying_personal_pc_20251111_models.DescribePackageOrdersResponse:
        """
        @summary 查询套餐包订单列表
        
        @param request: DescribePackageOrdersRequest
        @return: DescribePackageOrdersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_package_orders_with_options(request, runtime)

    async def describe_package_orders_async(
        self,
        request: wuying_personal_pc_20251111_models.DescribePackageOrdersRequest,
    ) -> wuying_personal_pc_20251111_models.DescribePackageOrdersResponse:
        """
        @summary 查询套餐包订单列表
        
        @param request: DescribePackageOrdersRequest
        @return: DescribePackageOrdersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_package_orders_with_options_async(request, runtime)

    def generate_wuying_server_scene_url_with_options(
        self,
        request: wuying_personal_pc_20251111_models.GenerateWuyingServerSceneUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wuying_personal_pc_20251111_models.GenerateWuyingServerSceneUrlResponse:
        """
        @summary 生成无影工作站的场景url
        
        @param request: GenerateWuyingServerSceneUrlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateWuyingServerSceneUrlResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_id):
            body['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIp'] = request.client_ip
        if not UtilClient.is_unset(request.client_os):
            body['ClientOS'] = request.client_os
        if not UtilClient.is_unset(request.client_type):
            body['ClientType'] = request.client_type
        if not UtilClient.is_unset(request.client_version):
            body['ClientVersion'] = request.client_version
        if not UtilClient.is_unset(request.end_user_id):
            body['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.login_region_id):
            body['LoginRegionId'] = request.login_region_id
        if not UtilClient.is_unset(request.login_token):
            body['LoginToken'] = request.login_token
        if not UtilClient.is_unset(request.product_type):
            body['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.scene):
            body['Scene'] = request.scene
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.uuid):
            body['Uuid'] = request.uuid
        if not UtilClient.is_unset(request.wuying_server_id):
            body['WuyingServerId'] = request.wuying_server_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateWuyingServerSceneUrl',
            version='2025-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wuying_personal_pc_20251111_models.GenerateWuyingServerSceneUrlResponse(),
            self.do_rpcrequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    async def generate_wuying_server_scene_url_with_options_async(
        self,
        request: wuying_personal_pc_20251111_models.GenerateWuyingServerSceneUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wuying_personal_pc_20251111_models.GenerateWuyingServerSceneUrlResponse:
        """
        @summary 生成无影工作站的场景url
        
        @param request: GenerateWuyingServerSceneUrlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateWuyingServerSceneUrlResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_id):
            body['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIp'] = request.client_ip
        if not UtilClient.is_unset(request.client_os):
            body['ClientOS'] = request.client_os
        if not UtilClient.is_unset(request.client_type):
            body['ClientType'] = request.client_type
        if not UtilClient.is_unset(request.client_version):
            body['ClientVersion'] = request.client_version
        if not UtilClient.is_unset(request.end_user_id):
            body['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.login_region_id):
            body['LoginRegionId'] = request.login_region_id
        if not UtilClient.is_unset(request.login_token):
            body['LoginToken'] = request.login_token
        if not UtilClient.is_unset(request.product_type):
            body['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.scene):
            body['Scene'] = request.scene
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.uuid):
            body['Uuid'] = request.uuid
        if not UtilClient.is_unset(request.wuying_server_id):
            body['WuyingServerId'] = request.wuying_server_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateWuyingServerSceneUrl',
            version='2025-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wuying_personal_pc_20251111_models.GenerateWuyingServerSceneUrlResponse(),
            await self.do_rpcrequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    def generate_wuying_server_scene_url(
        self,
        request: wuying_personal_pc_20251111_models.GenerateWuyingServerSceneUrlRequest,
    ) -> wuying_personal_pc_20251111_models.GenerateWuyingServerSceneUrlResponse:
        """
        @summary 生成无影工作站的场景url
        
        @param request: GenerateWuyingServerSceneUrlRequest
        @return: GenerateWuyingServerSceneUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.generate_wuying_server_scene_url_with_options(request, runtime)

    async def generate_wuying_server_scene_url_async(
        self,
        request: wuying_personal_pc_20251111_models.GenerateWuyingServerSceneUrlRequest,
    ) -> wuying_personal_pc_20251111_models.GenerateWuyingServerSceneUrlResponse:
        """
        @summary 生成无影工作站的场景url
        
        @param request: GenerateWuyingServerSceneUrlRequest
        @return: GenerateWuyingServerSceneUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.generate_wuying_server_scene_url_with_options_async(request, runtime)

    def get_product_list_with_options(
        self,
        request: wuying_personal_pc_20251111_models.GetProductListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wuying_personal_pc_20251111_models.GetProductListResponse:
        """
        @summary 查询展示商品列表
        
        @param request: GetProductListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetProductListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_key):
            query['ApiKey'] = request.api_key
        if not UtilClient.is_unset(request.config_version):
            query['ConfigVersion'] = request.config_version
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProductList',
            version='2025-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wuying_personal_pc_20251111_models.GetProductListResponse(),
            self.do_rpcrequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    async def get_product_list_with_options_async(
        self,
        request: wuying_personal_pc_20251111_models.GetProductListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wuying_personal_pc_20251111_models.GetProductListResponse:
        """
        @summary 查询展示商品列表
        
        @param request: GetProductListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetProductListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_key):
            query['ApiKey'] = request.api_key
        if not UtilClient.is_unset(request.config_version):
            query['ConfigVersion'] = request.config_version
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProductList',
            version='2025-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wuying_personal_pc_20251111_models.GetProductListResponse(),
            await self.do_rpcrequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    def get_product_list(
        self,
        request: wuying_personal_pc_20251111_models.GetProductListRequest,
    ) -> wuying_personal_pc_20251111_models.GetProductListResponse:
        """
        @summary 查询展示商品列表
        
        @param request: GetProductListRequest
        @return: GetProductListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_product_list_with_options(request, runtime)

    async def get_product_list_async(
        self,
        request: wuying_personal_pc_20251111_models.GetProductListRequest,
    ) -> wuying_personal_pc_20251111_models.GetProductListResponse:
        """
        @summary 查询展示商品列表
        
        @param request: GetProductListRequest
        @return: GetProductListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_product_list_with_options_async(request, runtime)

    def get_user_info_with_options(
        self,
        request: wuying_personal_pc_20251111_models.GetUserInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wuying_personal_pc_20251111_models.GetUserInfoResponse:
        """
        @summary 获取用户信息
        
        @param request: GetUserInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_key):
            query['ApiKey'] = request.api_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserInfo',
            version='2025-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wuying_personal_pc_20251111_models.GetUserInfoResponse(),
            self.do_rpcrequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    async def get_user_info_with_options_async(
        self,
        request: wuying_personal_pc_20251111_models.GetUserInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wuying_personal_pc_20251111_models.GetUserInfoResponse:
        """
        @summary 获取用户信息
        
        @param request: GetUserInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_key):
            query['ApiKey'] = request.api_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserInfo',
            version='2025-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wuying_personal_pc_20251111_models.GetUserInfoResponse(),
            await self.do_rpcrequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    def get_user_info(
        self,
        request: wuying_personal_pc_20251111_models.GetUserInfoRequest,
    ) -> wuying_personal_pc_20251111_models.GetUserInfoResponse:
        """
        @summary 获取用户信息
        
        @param request: GetUserInfoRequest
        @return: GetUserInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_user_info_with_options(request, runtime)

    async def get_user_info_async(
        self,
        request: wuying_personal_pc_20251111_models.GetUserInfoRequest,
    ) -> wuying_personal_pc_20251111_models.GetUserInfoResponse:
        """
        @summary 获取用户信息
        
        @param request: GetUserInfoRequest
        @return: GetUserInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_user_info_with_options_async(request, runtime)

    def start_desktop_with_options(
        self,
        request: wuying_personal_pc_20251111_models.StartDesktopRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wuying_personal_pc_20251111_models.StartDesktopResponse:
        """
        @summary 开机
        
        @param request: StartDesktopRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartDesktopResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_key):
            query['ApiKey'] = request.api_key
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartDesktop',
            version='2025-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wuying_personal_pc_20251111_models.StartDesktopResponse(),
            self.do_rpcrequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    async def start_desktop_with_options_async(
        self,
        request: wuying_personal_pc_20251111_models.StartDesktopRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wuying_personal_pc_20251111_models.StartDesktopResponse:
        """
        @summary 开机
        
        @param request: StartDesktopRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartDesktopResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_key):
            query['ApiKey'] = request.api_key
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartDesktop',
            version='2025-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wuying_personal_pc_20251111_models.StartDesktopResponse(),
            await self.do_rpcrequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    def start_desktop(
        self,
        request: wuying_personal_pc_20251111_models.StartDesktopRequest,
    ) -> wuying_personal_pc_20251111_models.StartDesktopResponse:
        """
        @summary 开机
        
        @param request: StartDesktopRequest
        @return: StartDesktopResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_desktop_with_options(request, runtime)

    async def start_desktop_async(
        self,
        request: wuying_personal_pc_20251111_models.StartDesktopRequest,
    ) -> wuying_personal_pc_20251111_models.StartDesktopResponse:
        """
        @summary 开机
        
        @param request: StartDesktopRequest
        @return: StartDesktopResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_desktop_with_options_async(request, runtime)

    def stop_desktop_with_options(
        self,
        request: wuying_personal_pc_20251111_models.StopDesktopRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wuying_personal_pc_20251111_models.StopDesktopResponse:
        """
        @summary 关机
        
        @param request: StopDesktopRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopDesktopResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_key):
            query['ApiKey'] = request.api_key
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopDesktop',
            version='2025-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wuying_personal_pc_20251111_models.StopDesktopResponse(),
            self.do_rpcrequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    async def stop_desktop_with_options_async(
        self,
        request: wuying_personal_pc_20251111_models.StopDesktopRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wuying_personal_pc_20251111_models.StopDesktopResponse:
        """
        @summary 关机
        
        @param request: StopDesktopRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopDesktopResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_key):
            query['ApiKey'] = request.api_key
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopDesktop',
            version='2025-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wuying_personal_pc_20251111_models.StopDesktopResponse(),
            await self.do_rpcrequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    def stop_desktop(
        self,
        request: wuying_personal_pc_20251111_models.StopDesktopRequest,
    ) -> wuying_personal_pc_20251111_models.StopDesktopResponse:
        """
        @summary 关机
        
        @param request: StopDesktopRequest
        @return: StopDesktopResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_desktop_with_options(request, runtime)

    async def stop_desktop_async(
        self,
        request: wuying_personal_pc_20251111_models.StopDesktopRequest,
    ) -> wuying_personal_pc_20251111_models.StopDesktopResponse:
        """
        @summary 关机
        
        @param request: StopDesktopRequest
        @return: StopDesktopResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_desktop_with_options_async(request, runtime)
