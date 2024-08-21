# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_hsm20231113 import models as hsm_20231113_models
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
        self._endpoint = self.get_endpoint('hsm', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def config_cluster_subnet_with_options(
        self,
        tmp_req: hsm_20231113_models.ConfigClusterSubnetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.ConfigClusterSubnetResponse:
        """
        @summary 配置集群子网
        
        @param tmp_req: ConfigClusterSubnetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigClusterSubnetResponse
        """
        UtilClient.validate_model(tmp_req)
        request = hsm_20231113_models.ConfigClusterSubnetShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.v_switch_ids):
            request.v_switch_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.v_switch_ids, 'VSwitchIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.v_switch_ids_shrink):
            body['VSwitchIds'] = request.v_switch_ids_shrink
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ConfigClusterSubnet',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.ConfigClusterSubnetResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_cluster_subnet_with_options_async(
        self,
        tmp_req: hsm_20231113_models.ConfigClusterSubnetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hsm_20231113_models.ConfigClusterSubnetResponse:
        """
        @summary 配置集群子网
        
        @param tmp_req: ConfigClusterSubnetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigClusterSubnetResponse
        """
        UtilClient.validate_model(tmp_req)
        request = hsm_20231113_models.ConfigClusterSubnetShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.v_switch_ids):
            request.v_switch_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.v_switch_ids, 'VSwitchIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.v_switch_ids_shrink):
            body['VSwitchIds'] = request.v_switch_ids_shrink
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ConfigClusterSubnet',
            version='2023-11-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hsm_20231113_models.ConfigClusterSubnetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def config_cluster_subnet(
        self,
        request: hsm_20231113_models.ConfigClusterSubnetRequest,
    ) -> hsm_20231113_models.ConfigClusterSubnetResponse:
        """
        @summary 配置集群子网
        
        @param request: ConfigClusterSubnetRequest
        @return: ConfigClusterSubnetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.config_cluster_subnet_with_options(request, runtime)

    async def config_cluster_subnet_async(
        self,
        request: hsm_20231113_models.ConfigClusterSubnetRequest,
    ) -> hsm_20231113_models.ConfigClusterSubnetResponse:
        """
        @summary 配置集群子网
        
        @param request: ConfigClusterSubnetRequest
        @return: ConfigClusterSubnetResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.config_cluster_subnet_with_options_async(request, runtime)
