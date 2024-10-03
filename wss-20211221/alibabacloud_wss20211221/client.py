# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_gateway_pop.client import Client as GatewayClientClient
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_tea_util import models as util_models
from alibabacloud_wss20211221 import models as wss_20211221_models
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
        self._product_id = 'wss'
        gateway_client = GatewayClientClient()
        self._spi = gateway_client
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('wss', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def describe_delivery_address_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> wss_20211221_models.DescribeDeliveryAddressResponse:
        """
        @param request: DescribeDeliveryAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDeliveryAddressResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeDeliveryAddress',
            version='2021-12-21',
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
                wss_20211221_models.DescribeDeliveryAddressResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                wss_20211221_models.DescribeDeliveryAddressResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_delivery_address_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> wss_20211221_models.DescribeDeliveryAddressResponse:
        """
        @param request: DescribeDeliveryAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDeliveryAddressResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeDeliveryAddress',
            version='2021-12-21',
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
                wss_20211221_models.DescribeDeliveryAddressResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                wss_20211221_models.DescribeDeliveryAddressResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_delivery_address(self) -> wss_20211221_models.DescribeDeliveryAddressResponse:
        """
        @return: DescribeDeliveryAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_delivery_address_with_options(runtime)

    async def describe_delivery_address_async(self) -> wss_20211221_models.DescribeDeliveryAddressResponse:
        """
        @return: DescribeDeliveryAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_delivery_address_with_options_async(runtime)

    def describe_package_deductions_with_options(
        self,
        request: wss_20211221_models.DescribePackageDeductionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wss_20211221_models.DescribePackageDeductionsResponse:
        """
        @summary 查询核时包抵扣明细
        
        @param request: DescribePackageDeductionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePackageDeductionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.package_ids):
            query['PackageIds'] = request.package_ids
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePackageDeductions',
            version='2021-12-21',
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
                wss_20211221_models.DescribePackageDeductionsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                wss_20211221_models.DescribePackageDeductionsResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_package_deductions_with_options_async(
        self,
        request: wss_20211221_models.DescribePackageDeductionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wss_20211221_models.DescribePackageDeductionsResponse:
        """
        @summary 查询核时包抵扣明细
        
        @param request: DescribePackageDeductionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePackageDeductionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.package_ids):
            query['PackageIds'] = request.package_ids
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePackageDeductions',
            version='2021-12-21',
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
                wss_20211221_models.DescribePackageDeductionsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                wss_20211221_models.DescribePackageDeductionsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_package_deductions(
        self,
        request: wss_20211221_models.DescribePackageDeductionsRequest,
    ) -> wss_20211221_models.DescribePackageDeductionsResponse:
        """
        @summary 查询核时包抵扣明细
        
        @param request: DescribePackageDeductionsRequest
        @return: DescribePackageDeductionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_package_deductions_with_options(request, runtime)

    async def describe_package_deductions_async(
        self,
        request: wss_20211221_models.DescribePackageDeductionsRequest,
    ) -> wss_20211221_models.DescribePackageDeductionsResponse:
        """
        @summary 查询核时包抵扣明细
        
        @param request: DescribePackageDeductionsRequest
        @return: DescribePackageDeductionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_package_deductions_with_options_async(request, runtime)
