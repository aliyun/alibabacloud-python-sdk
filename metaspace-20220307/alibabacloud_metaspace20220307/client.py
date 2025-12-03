# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_metaspace20220307 import models as metaspace_20220307_models
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
        self._endpoint = self.get_endpoint('metaspace', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def apply_coordination_with_code_with_options(
        self,
        request: metaspace_20220307_models.ApplyCoordinationWithCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> metaspace_20220307_models.ApplyCoordinationWithCodeResponse:
        """
        @summary 用协同码发起协同
        
        @param request: ApplyCoordinationWithCodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ApplyCoordinationWithCodeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.coordination_code):
            body['CoordinationCode'] = request.coordination_code
        if not UtilClient.is_unset(request.login_region_id):
            body['LoginRegionId'] = request.login_region_id
        if not UtilClient.is_unset(request.login_token):
            body['LoginToken'] = request.login_token
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.uuid):
            body['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ApplyCoordinationWithCode',
            version='2022-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            metaspace_20220307_models.ApplyCoordinationWithCodeResponse(),
            self.do_rpcrequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    async def apply_coordination_with_code_with_options_async(
        self,
        request: metaspace_20220307_models.ApplyCoordinationWithCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> metaspace_20220307_models.ApplyCoordinationWithCodeResponse:
        """
        @summary 用协同码发起协同
        
        @param request: ApplyCoordinationWithCodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ApplyCoordinationWithCodeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.coordination_code):
            body['CoordinationCode'] = request.coordination_code
        if not UtilClient.is_unset(request.login_region_id):
            body['LoginRegionId'] = request.login_region_id
        if not UtilClient.is_unset(request.login_token):
            body['LoginToken'] = request.login_token
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.uuid):
            body['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ApplyCoordinationWithCode',
            version='2022-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            metaspace_20220307_models.ApplyCoordinationWithCodeResponse(),
            await self.do_rpcrequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    def apply_coordination_with_code(
        self,
        request: metaspace_20220307_models.ApplyCoordinationWithCodeRequest,
    ) -> metaspace_20220307_models.ApplyCoordinationWithCodeResponse:
        """
        @summary 用协同码发起协同
        
        @param request: ApplyCoordinationWithCodeRequest
        @return: ApplyCoordinationWithCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.apply_coordination_with_code_with_options(request, runtime)

    async def apply_coordination_with_code_async(
        self,
        request: metaspace_20220307_models.ApplyCoordinationWithCodeRequest,
    ) -> metaspace_20220307_models.ApplyCoordinationWithCodeResponse:
        """
        @summary 用协同码发起协同
        
        @param request: ApplyCoordinationWithCodeRequest
        @return: ApplyCoordinationWithCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.apply_coordination_with_code_with_options_async(request, runtime)

    def end_all_coordination_by_owner_with_options(
        self,
        request: metaspace_20220307_models.EndAllCoordinationByOwnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> metaspace_20220307_models.EndAllCoordinationByOwnerResponse:
        """
        @summary Owner主动结束本次协同，同步失效协同码
        
        @param request: EndAllCoordinationByOwnerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EndAllCoordinationByOwnerResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.login_region_id):
            body['LoginRegionId'] = request.login_region_id
        if not UtilClient.is_unset(request.login_token):
            body['LoginToken'] = request.login_token
        if not UtilClient.is_unset(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_region_id):
            body['ResourceRegionId'] = request.resource_region_id
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EndAllCoordinationByOwner',
            version='2022-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            metaspace_20220307_models.EndAllCoordinationByOwnerResponse(),
            self.do_rpcrequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    async def end_all_coordination_by_owner_with_options_async(
        self,
        request: metaspace_20220307_models.EndAllCoordinationByOwnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> metaspace_20220307_models.EndAllCoordinationByOwnerResponse:
        """
        @summary Owner主动结束本次协同，同步失效协同码
        
        @param request: EndAllCoordinationByOwnerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EndAllCoordinationByOwnerResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.login_region_id):
            body['LoginRegionId'] = request.login_region_id
        if not UtilClient.is_unset(request.login_token):
            body['LoginToken'] = request.login_token
        if not UtilClient.is_unset(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_region_id):
            body['ResourceRegionId'] = request.resource_region_id
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EndAllCoordinationByOwner',
            version='2022-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            metaspace_20220307_models.EndAllCoordinationByOwnerResponse(),
            await self.do_rpcrequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    def end_all_coordination_by_owner(
        self,
        request: metaspace_20220307_models.EndAllCoordinationByOwnerRequest,
    ) -> metaspace_20220307_models.EndAllCoordinationByOwnerResponse:
        """
        @summary Owner主动结束本次协同，同步失效协同码
        
        @param request: EndAllCoordinationByOwnerRequest
        @return: EndAllCoordinationByOwnerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.end_all_coordination_by_owner_with_options(request, runtime)

    async def end_all_coordination_by_owner_async(
        self,
        request: metaspace_20220307_models.EndAllCoordinationByOwnerRequest,
    ) -> metaspace_20220307_models.EndAllCoordinationByOwnerResponse:
        """
        @summary Owner主动结束本次协同，同步失效协同码
        
        @param request: EndAllCoordinationByOwnerRequest
        @return: EndAllCoordinationByOwnerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.end_all_coordination_by_owner_with_options_async(request, runtime)

    def generate_coordination_code_with_options(
        self,
        request: metaspace_20220307_models.GenerateCoordinationCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> metaspace_20220307_models.GenerateCoordinationCodeResponse:
        """
        @summary 生成协同码
        
        @param request: GenerateCoordinationCodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateCoordinationCodeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.login_region_id):
            body['LoginRegionId'] = request.login_region_id
        if not UtilClient.is_unset(request.login_token):
            body['LoginToken'] = request.login_token
        if not UtilClient.is_unset(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_name):
            body['ResourceName'] = request.resource_name
        if not UtilClient.is_unset(request.resource_region_id):
            body['ResourceRegionId'] = request.resource_region_id
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateCoordinationCode',
            version='2022-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            metaspace_20220307_models.GenerateCoordinationCodeResponse(),
            self.do_rpcrequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    async def generate_coordination_code_with_options_async(
        self,
        request: metaspace_20220307_models.GenerateCoordinationCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> metaspace_20220307_models.GenerateCoordinationCodeResponse:
        """
        @summary 生成协同码
        
        @param request: GenerateCoordinationCodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateCoordinationCodeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.login_region_id):
            body['LoginRegionId'] = request.login_region_id
        if not UtilClient.is_unset(request.login_token):
            body['LoginToken'] = request.login_token
        if not UtilClient.is_unset(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_name):
            body['ResourceName'] = request.resource_name
        if not UtilClient.is_unset(request.resource_region_id):
            body['ResourceRegionId'] = request.resource_region_id
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateCoordinationCode',
            version='2022-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            metaspace_20220307_models.GenerateCoordinationCodeResponse(),
            await self.do_rpcrequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    def generate_coordination_code(
        self,
        request: metaspace_20220307_models.GenerateCoordinationCodeRequest,
    ) -> metaspace_20220307_models.GenerateCoordinationCodeResponse:
        """
        @summary 生成协同码
        
        @param request: GenerateCoordinationCodeRequest
        @return: GenerateCoordinationCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.generate_coordination_code_with_options(request, runtime)

    async def generate_coordination_code_async(
        self,
        request: metaspace_20220307_models.GenerateCoordinationCodeRequest,
    ) -> metaspace_20220307_models.GenerateCoordinationCodeResponse:
        """
        @summary 生成协同码
        
        @param request: GenerateCoordinationCodeRequest
        @return: GenerateCoordinationCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.generate_coordination_code_with_options_async(request, runtime)
