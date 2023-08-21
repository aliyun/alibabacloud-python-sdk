# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ecs_workbench20220220 import models as ecs_workbench_20220220_models
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
        self._endpoint = self.get_endpoint('ecs-workbench', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def login_instance_with_options(
        self,
        request: ecs_workbench_20220220_models.LoginInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_workbench_20220220_models.LoginInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_login_info):
            query['InstanceLoginInfo'] = request.instance_login_info
        if not UtilClient.is_unset(request.partner_info):
            query['PartnerInfo'] = request.partner_info
        if not UtilClient.is_unset(request.user_account):
            query['UserAccount'] = request.user_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LoginInstance',
            version='2022-02-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_workbench_20220220_models.LoginInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def login_instance_with_options_async(
        self,
        request: ecs_workbench_20220220_models.LoginInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_workbench_20220220_models.LoginInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_login_info):
            query['InstanceLoginInfo'] = request.instance_login_info
        if not UtilClient.is_unset(request.partner_info):
            query['PartnerInfo'] = request.partner_info
        if not UtilClient.is_unset(request.user_account):
            query['UserAccount'] = request.user_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LoginInstance',
            version='2022-02-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_workbench_20220220_models.LoginInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def login_instance(
        self,
        request: ecs_workbench_20220220_models.LoginInstanceRequest,
    ) -> ecs_workbench_20220220_models.LoginInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.login_instance_with_options(request, runtime)

    async def login_instance_async(
        self,
        request: ecs_workbench_20220220_models.LoginInstanceRequest,
    ) -> ecs_workbench_20220220_models.LoginInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.login_instance_with_options_async(request, runtime)
