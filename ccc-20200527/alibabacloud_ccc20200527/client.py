# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ccc20200527 import models as ccc20200527_models
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
        self._endpoint_map = {
            'ap-northeast-1': 'ccc.aliyuncs.com',
            'ap-south-1': 'ccc.aliyuncs.com',
            'ap-southeast-1': 'ccc.aliyuncs.com',
            'ap-southeast-2': 'ccc.aliyuncs.com',
            'ap-southeast-3': 'ccc.aliyuncs.com',
            'ap-southeast-5': 'ccc.aliyuncs.com',
            'cn-beijing': 'ccc.aliyuncs.com',
            'cn-chengdu': 'ccc.aliyuncs.com',
            'cn-hongkong': 'ccc.aliyuncs.com',
            'cn-huhehaote': 'ccc.aliyuncs.com',
            'cn-qingdao': 'ccc.aliyuncs.com',
            'cn-shenzhen': 'ccc.aliyuncs.com',
            'cn-zhangjiakou': 'ccc.aliyuncs.com',
            'eu-central-1': 'ccc.aliyuncs.com',
            'eu-west-1': 'ccc.aliyuncs.com',
            'me-east-1': 'ccc.aliyuncs.com',
            'us-east-1': 'ccc.aliyuncs.com',
            'us-west-1': 'ccc.aliyuncs.com',
            'cn-hangzhou-finance': 'ccc.aliyuncs.com',
            'cn-shenzhen-finance-1': 'ccc.aliyuncs.com',
            'cn-shanghai-finance-1': 'ccc.aliyuncs.com',
            'cn-north-2-gov-1': 'ccc.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('ccc', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def check_service_linked_role_for_deleting_with_options(
        self,
        request: ccc20200527_models.CheckServiceLinkedRoleForDeletingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200527_models.CheckServiceLinkedRoleForDeletingResponse:
        """
        @param request: CheckServiceLinkedRoleForDeletingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckServiceLinkedRoleForDeletingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deletion_task_id):
            query['DeletionTaskId'] = request.deletion_task_id
        if not UtilClient.is_unset(request.role_arn):
            query['RoleArn'] = request.role_arn
        if not UtilClient.is_unset(request.spiregion_id):
            query['SPIRegionId'] = request.spiregion_id
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckServiceLinkedRoleForDeleting',
            version='2020-05-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200527_models.CheckServiceLinkedRoleForDeletingResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_service_linked_role_for_deleting_with_options_async(
        self,
        request: ccc20200527_models.CheckServiceLinkedRoleForDeletingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20200527_models.CheckServiceLinkedRoleForDeletingResponse:
        """
        @param request: CheckServiceLinkedRoleForDeletingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckServiceLinkedRoleForDeletingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deletion_task_id):
            query['DeletionTaskId'] = request.deletion_task_id
        if not UtilClient.is_unset(request.role_arn):
            query['RoleArn'] = request.role_arn
        if not UtilClient.is_unset(request.spiregion_id):
            query['SPIRegionId'] = request.spiregion_id
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckServiceLinkedRoleForDeleting',
            version='2020-05-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccc20200527_models.CheckServiceLinkedRoleForDeletingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_service_linked_role_for_deleting(
        self,
        request: ccc20200527_models.CheckServiceLinkedRoleForDeletingRequest,
    ) -> ccc20200527_models.CheckServiceLinkedRoleForDeletingResponse:
        """
        @param request: CheckServiceLinkedRoleForDeletingRequest
        @return: CheckServiceLinkedRoleForDeletingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_service_linked_role_for_deleting_with_options(request, runtime)

    async def check_service_linked_role_for_deleting_async(
        self,
        request: ccc20200527_models.CheckServiceLinkedRoleForDeletingRequest,
    ) -> ccc20200527_models.CheckServiceLinkedRoleForDeletingResponse:
        """
        @param request: CheckServiceLinkedRoleForDeletingRequest
        @return: CheckServiceLinkedRoleForDeletingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.check_service_linked_role_for_deleting_with_options_async(request, runtime)
