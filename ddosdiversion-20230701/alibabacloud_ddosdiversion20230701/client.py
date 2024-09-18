# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ddosdiversion20230701 import models as ddos_diversion_20230701_models
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
        self._endpoint = self.get_endpoint('ddosdiversion', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def config_net_status_with_options(
        self,
        request: ddos_diversion_20230701_models.ConfigNetStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddos_diversion_20230701_models.ConfigNetStatusResponse:
        """
        @summary Configures the advertising of a CIDR block.
        
        @param request: ConfigNetStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigNetStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.net):
            query['Net'] = request.net
        if not UtilClient.is_unset(request.regions):
            query['Regions'] = request.regions
        if not UtilClient.is_unset(request.sale_id):
            query['SaleId'] = request.sale_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.sub_nets):
            query['SubNets'] = request.sub_nets
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigNetStatus',
            version='2023-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddos_diversion_20230701_models.ConfigNetStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_net_status_with_options_async(
        self,
        request: ddos_diversion_20230701_models.ConfigNetStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddos_diversion_20230701_models.ConfigNetStatusResponse:
        """
        @summary Configures the advertising of a CIDR block.
        
        @param request: ConfigNetStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigNetStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.net):
            query['Net'] = request.net
        if not UtilClient.is_unset(request.regions):
            query['Regions'] = request.regions
        if not UtilClient.is_unset(request.sale_id):
            query['SaleId'] = request.sale_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.sub_nets):
            query['SubNets'] = request.sub_nets
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigNetStatus',
            version='2023-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddos_diversion_20230701_models.ConfigNetStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def config_net_status(
        self,
        request: ddos_diversion_20230701_models.ConfigNetStatusRequest,
    ) -> ddos_diversion_20230701_models.ConfigNetStatusResponse:
        """
        @summary Configures the advertising of a CIDR block.
        
        @param request: ConfigNetStatusRequest
        @return: ConfigNetStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.config_net_status_with_options(request, runtime)

    async def config_net_status_async(
        self,
        request: ddos_diversion_20230701_models.ConfigNetStatusRequest,
    ) -> ddos_diversion_20230701_models.ConfigNetStatusResponse:
        """
        @summary Configures the advertising of a CIDR block.
        
        @param request: ConfigNetStatusRequest
        @return: ConfigNetStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.config_net_status_with_options_async(request, runtime)

    def list_instance_with_options(
        self,
        request: ddos_diversion_20230701_models.ListInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddos_diversion_20230701_models.ListInstanceResponse:
        """
        @summary Queries anti-DDoS diversion instances.
        
        @param request: ListInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.num):
            query['Num'] = request.num
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.sale_id):
            query['SaleId'] = request.sale_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstance',
            version='2023-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddos_diversion_20230701_models.ListInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instance_with_options_async(
        self,
        request: ddos_diversion_20230701_models.ListInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddos_diversion_20230701_models.ListInstanceResponse:
        """
        @summary Queries anti-DDoS diversion instances.
        
        @param request: ListInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.num):
            query['Num'] = request.num
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.sale_id):
            query['SaleId'] = request.sale_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstance',
            version='2023-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddos_diversion_20230701_models.ListInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instance(
        self,
        request: ddos_diversion_20230701_models.ListInstanceRequest,
    ) -> ddos_diversion_20230701_models.ListInstanceResponse:
        """
        @summary Queries anti-DDoS diversion instances.
        
        @param request: ListInstanceRequest
        @return: ListInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_instance_with_options(request, runtime)

    async def list_instance_async(
        self,
        request: ddos_diversion_20230701_models.ListInstanceRequest,
    ) -> ddos_diversion_20230701_models.ListInstanceResponse:
        """
        @summary Queries anti-DDoS diversion instances.
        
        @param request: ListInstanceRequest
        @return: ListInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_instance_with_options_async(request, runtime)

    def query_net_list_with_options(
        self,
        request: ddos_diversion_20230701_models.QueryNetListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddos_diversion_20230701_models.QueryNetListResponse:
        """
        @summary Queries the CIDR blocks of an anti-DDoS diversion instance.
        
        @param request: QueryNetListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryNetListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.main_net):
            query['MainNet'] = request.main_net
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.net):
            query['Net'] = request.net
        if not UtilClient.is_unset(request.num):
            query['Num'] = request.num
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.sale_id):
            query['SaleId'] = request.sale_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryNetList',
            version='2023-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddos_diversion_20230701_models.QueryNetListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_net_list_with_options_async(
        self,
        request: ddos_diversion_20230701_models.QueryNetListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddos_diversion_20230701_models.QueryNetListResponse:
        """
        @summary Queries the CIDR blocks of an anti-DDoS diversion instance.
        
        @param request: QueryNetListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryNetListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.main_net):
            query['MainNet'] = request.main_net
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.net):
            query['Net'] = request.net
        if not UtilClient.is_unset(request.num):
            query['Num'] = request.num
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.sale_id):
            query['SaleId'] = request.sale_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryNetList',
            version='2023-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddos_diversion_20230701_models.QueryNetListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_net_list(
        self,
        request: ddos_diversion_20230701_models.QueryNetListRequest,
    ) -> ddos_diversion_20230701_models.QueryNetListResponse:
        """
        @summary Queries the CIDR blocks of an anti-DDoS diversion instance.
        
        @param request: QueryNetListRequest
        @return: QueryNetListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_net_list_with_options(request, runtime)

    async def query_net_list_async(
        self,
        request: ddos_diversion_20230701_models.QueryNetListRequest,
    ) -> ddos_diversion_20230701_models.QueryNetListResponse:
        """
        @summary Queries the CIDR blocks of an anti-DDoS diversion instance.
        
        @param request: QueryNetListRequest
        @return: QueryNetListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_net_list_with_options_async(request, runtime)
