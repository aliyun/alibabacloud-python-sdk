# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_marketplaceintl20221230 import models as marketplace_intl_20221230_models
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
        self._endpoint = self.get_endpoint('marketplaceintl', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def describe_seller_instances_with_options(
        self,
        request: marketplace_intl_20221230_models.DescribeSellerInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> marketplace_intl_20221230_models.DescribeSellerInstancesResponse:
        """
        @summary 卖家查询实例列表
        
        @param request: DescribeSellerInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSellerInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_status):
            query['InstanceStatus'] = request.instance_status
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSellerInstances',
            version='2022-12-30',
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
                marketplace_intl_20221230_models.DescribeSellerInstancesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                marketplace_intl_20221230_models.DescribeSellerInstancesResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_seller_instances_with_options_async(
        self,
        request: marketplace_intl_20221230_models.DescribeSellerInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> marketplace_intl_20221230_models.DescribeSellerInstancesResponse:
        """
        @summary 卖家查询实例列表
        
        @param request: DescribeSellerInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSellerInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_status):
            query['InstanceStatus'] = request.instance_status
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSellerInstances',
            version='2022-12-30',
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
                marketplace_intl_20221230_models.DescribeSellerInstancesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                marketplace_intl_20221230_models.DescribeSellerInstancesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_seller_instances(
        self,
        request: marketplace_intl_20221230_models.DescribeSellerInstancesRequest,
    ) -> marketplace_intl_20221230_models.DescribeSellerInstancesResponse:
        """
        @summary 卖家查询实例列表
        
        @param request: DescribeSellerInstancesRequest
        @return: DescribeSellerInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_seller_instances_with_options(request, runtime)

    async def describe_seller_instances_async(
        self,
        request: marketplace_intl_20221230_models.DescribeSellerInstancesRequest,
    ) -> marketplace_intl_20221230_models.DescribeSellerInstancesResponse:
        """
        @summary 卖家查询实例列表
        
        @param request: DescribeSellerInstancesRequest
        @return: DescribeSellerInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_seller_instances_with_options_async(request, runtime)

    def notice_instance_user_with_options(
        self,
        request: marketplace_intl_20221230_models.NoticeInstanceUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> marketplace_intl_20221230_models.NoticeInstanceUserResponse:
        """
        @summary isv推送实例消息给用户
        
        @param request: NoticeInstanceUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: NoticeInstanceUserResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.notice_param):
            body['NoticeParam'] = request.notice_param
        if not UtilClient.is_unset(request.notice_type):
            body['NoticeType'] = request.notice_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='NoticeInstanceUser',
            version='2022-12-30',
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
                marketplace_intl_20221230_models.NoticeInstanceUserResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                marketplace_intl_20221230_models.NoticeInstanceUserResponse(),
                self.execute(params, req, runtime)
            )

    async def notice_instance_user_with_options_async(
        self,
        request: marketplace_intl_20221230_models.NoticeInstanceUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> marketplace_intl_20221230_models.NoticeInstanceUserResponse:
        """
        @summary isv推送实例消息给用户
        
        @param request: NoticeInstanceUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: NoticeInstanceUserResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.notice_param):
            body['NoticeParam'] = request.notice_param
        if not UtilClient.is_unset(request.notice_type):
            body['NoticeType'] = request.notice_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='NoticeInstanceUser',
            version='2022-12-30',
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
                marketplace_intl_20221230_models.NoticeInstanceUserResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                marketplace_intl_20221230_models.NoticeInstanceUserResponse(),
                await self.execute_async(params, req, runtime)
            )

    def notice_instance_user(
        self,
        request: marketplace_intl_20221230_models.NoticeInstanceUserRequest,
    ) -> marketplace_intl_20221230_models.NoticeInstanceUserResponse:
        """
        @summary isv推送实例消息给用户
        
        @param request: NoticeInstanceUserRequest
        @return: NoticeInstanceUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.notice_instance_user_with_options(request, runtime)

    async def notice_instance_user_async(
        self,
        request: marketplace_intl_20221230_models.NoticeInstanceUserRequest,
    ) -> marketplace_intl_20221230_models.NoticeInstanceUserResponse:
        """
        @summary isv推送实例消息给用户
        
        @param request: NoticeInstanceUserRequest
        @return: NoticeInstanceUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.notice_instance_user_with_options_async(request, runtime)

    def push_metering_data_with_options(
        self,
        request: marketplace_intl_20221230_models.PushMeteringDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> marketplace_intl_20221230_models.PushMeteringDataResponse:
        """
        @summary 国际云市场推送计量数据
        
        @param request: PushMeteringDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PushMeteringDataResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.gmt_create):
            body['GmtCreate'] = request.gmt_create
        if not UtilClient.is_unset(request.metering_data):
            body['MeteringData'] = request.metering_data
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PushMeteringData',
            version='2022-12-30',
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
                marketplace_intl_20221230_models.PushMeteringDataResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                marketplace_intl_20221230_models.PushMeteringDataResponse(),
                self.execute(params, req, runtime)
            )

    async def push_metering_data_with_options_async(
        self,
        request: marketplace_intl_20221230_models.PushMeteringDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> marketplace_intl_20221230_models.PushMeteringDataResponse:
        """
        @summary 国际云市场推送计量数据
        
        @param request: PushMeteringDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PushMeteringDataResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.gmt_create):
            body['GmtCreate'] = request.gmt_create
        if not UtilClient.is_unset(request.metering_data):
            body['MeteringData'] = request.metering_data
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PushMeteringData',
            version='2022-12-30',
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
                marketplace_intl_20221230_models.PushMeteringDataResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                marketplace_intl_20221230_models.PushMeteringDataResponse(),
                await self.execute_async(params, req, runtime)
            )

    def push_metering_data(
        self,
        request: marketplace_intl_20221230_models.PushMeteringDataRequest,
    ) -> marketplace_intl_20221230_models.PushMeteringDataResponse:
        """
        @summary 国际云市场推送计量数据
        
        @param request: PushMeteringDataRequest
        @return: PushMeteringDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.push_metering_data_with_options(request, runtime)

    async def push_metering_data_async(
        self,
        request: marketplace_intl_20221230_models.PushMeteringDataRequest,
    ) -> marketplace_intl_20221230_models.PushMeteringDataResponse:
        """
        @summary 国际云市场推送计量数据
        
        @param request: PushMeteringDataRequest
        @return: PushMeteringDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.push_metering_data_with_options_async(request, runtime)
