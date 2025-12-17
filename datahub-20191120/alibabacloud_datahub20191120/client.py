# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_datahub20191120 import models as datahub_20191120_models
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
        self._endpoint = self.get_endpoint('datahub', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def list_projects_with_options(
        self,
        request: datahub_20191120_models.ListProjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> datahub_20191120_models.ListProjectsResponse:
        """
        @summary Query project list information
        
        @param request: ListProjectsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListProjectsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProjects',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            datahub_20191120_models.ListProjectsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_projects_with_options_async(
        self,
        request: datahub_20191120_models.ListProjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> datahub_20191120_models.ListProjectsResponse:
        """
        @summary Query project list information
        
        @param request: ListProjectsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListProjectsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProjects',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            datahub_20191120_models.ListProjectsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_projects(
        self,
        request: datahub_20191120_models.ListProjectsRequest,
    ) -> datahub_20191120_models.ListProjectsResponse:
        """
        @summary Query project list information
        
        @param request: ListProjectsRequest
        @return: ListProjectsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_projects_with_options(request, runtime)

    async def list_projects_async(
        self,
        request: datahub_20191120_models.ListProjectsRequest,
    ) -> datahub_20191120_models.ListProjectsResponse:
        """
        @summary Query project list information
        
        @param request: ListProjectsRequest
        @return: ListProjectsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_projects_with_options_async(request, runtime)

    def open_data_hub_service_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> datahub_20191120_models.OpenDataHubServiceResponse:
        """
        @summary 开通Datahub服务
        
        @param request: OpenDataHubServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OpenDataHubServiceResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='OpenDataHubService',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            datahub_20191120_models.OpenDataHubServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_data_hub_service_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> datahub_20191120_models.OpenDataHubServiceResponse:
        """
        @summary 开通Datahub服务
        
        @param request: OpenDataHubServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OpenDataHubServiceResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='OpenDataHubService',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            datahub_20191120_models.OpenDataHubServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_data_hub_service(self) -> datahub_20191120_models.OpenDataHubServiceResponse:
        """
        @summary 开通Datahub服务
        
        @return: OpenDataHubServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.open_data_hub_service_with_options(runtime)

    async def open_data_hub_service_async(self) -> datahub_20191120_models.OpenDataHubServiceResponse:
        """
        @summary 开通Datahub服务
        
        @return: OpenDataHubServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.open_data_hub_service_with_options_async(runtime)
