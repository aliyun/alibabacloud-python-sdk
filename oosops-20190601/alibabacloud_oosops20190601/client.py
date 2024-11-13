# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_oosops20190601 import models as oosops_20190601_models
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
        self._endpoint = self.get_endpoint('oosops', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def audit_public_template_registration_with_options(
        self,
        request: oosops_20190601_models.AuditPublicTemplateRegistrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.AuditPublicTemplateRegistrationResponse:
        """
        @param request: AuditPublicTemplateRegistrationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AuditPublicTemplateRegistrationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_action):
            query['AuditAction'] = request.audit_action
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.registration_id):
            query['RegistrationId'] = request.registration_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AuditPublicTemplateRegistration',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.AuditPublicTemplateRegistrationResponse(),
            self.call_api(params, req, runtime)
        )

    async def audit_public_template_registration_with_options_async(
        self,
        request: oosops_20190601_models.AuditPublicTemplateRegistrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.AuditPublicTemplateRegistrationResponse:
        """
        @param request: AuditPublicTemplateRegistrationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AuditPublicTemplateRegistrationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_action):
            query['AuditAction'] = request.audit_action
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.registration_id):
            query['RegistrationId'] = request.registration_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AuditPublicTemplateRegistration',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.AuditPublicTemplateRegistrationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def audit_public_template_registration(
        self,
        request: oosops_20190601_models.AuditPublicTemplateRegistrationRequest,
    ) -> oosops_20190601_models.AuditPublicTemplateRegistrationResponse:
        """
        @param request: AuditPublicTemplateRegistrationRequest
        @return: AuditPublicTemplateRegistrationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.audit_public_template_registration_with_options(request, runtime)

    async def audit_public_template_registration_async(
        self,
        request: oosops_20190601_models.AuditPublicTemplateRegistrationRequest,
    ) -> oosops_20190601_models.AuditPublicTemplateRegistrationResponse:
        """
        @param request: AuditPublicTemplateRegistrationRequest
        @return: AuditPublicTemplateRegistrationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.audit_public_template_registration_with_options_async(request, runtime)

    def create_action_with_options(
        self,
        request: oosops_20190601_models.CreateActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.CreateActionResponse:
        """
        @param request: CreateActionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateActionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_name):
            query['ActionName'] = request.action_name
        if not UtilClient.is_unset(request.action_type):
            query['ActionType'] = request.action_type
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.popularity):
            query['Popularity'] = request.popularity
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAction',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.CreateActionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_action_with_options_async(
        self,
        request: oosops_20190601_models.CreateActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.CreateActionResponse:
        """
        @param request: CreateActionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateActionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_name):
            query['ActionName'] = request.action_name
        if not UtilClient.is_unset(request.action_type):
            query['ActionType'] = request.action_type
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.popularity):
            query['Popularity'] = request.popularity
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAction',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.CreateActionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_action(
        self,
        request: oosops_20190601_models.CreateActionRequest,
    ) -> oosops_20190601_models.CreateActionResponse:
        """
        @param request: CreateActionRequest
        @return: CreateActionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_action_with_options(request, runtime)

    async def create_action_async(
        self,
        request: oosops_20190601_models.CreateActionRequest,
    ) -> oosops_20190601_models.CreateActionResponse:
        """
        @param request: CreateActionRequest
        @return: CreateActionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_action_with_options_async(request, runtime)

    def create_public_parameter_with_options(
        self,
        request: oosops_20190601_models.CreatePublicParameterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.CreatePublicParameterResponse:
        """
        @summary 创建一个公共参数。
        
        @param request: CreatePublicParameterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePublicParameterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.constraints):
            query['Constraints'] = request.constraints
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.parameter_type):
            query['ParameterType'] = request.parameter_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePublicParameter',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.CreatePublicParameterResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_public_parameter_with_options_async(
        self,
        request: oosops_20190601_models.CreatePublicParameterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.CreatePublicParameterResponse:
        """
        @summary 创建一个公共参数。
        
        @param request: CreatePublicParameterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePublicParameterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.constraints):
            query['Constraints'] = request.constraints
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.parameter_type):
            query['ParameterType'] = request.parameter_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePublicParameter',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.CreatePublicParameterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_public_parameter(
        self,
        request: oosops_20190601_models.CreatePublicParameterRequest,
    ) -> oosops_20190601_models.CreatePublicParameterResponse:
        """
        @summary 创建一个公共参数。
        
        @param request: CreatePublicParameterRequest
        @return: CreatePublicParameterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_public_parameter_with_options(request, runtime)

    async def create_public_parameter_async(
        self,
        request: oosops_20190601_models.CreatePublicParameterRequest,
    ) -> oosops_20190601_models.CreatePublicParameterResponse:
        """
        @summary 创建一个公共参数。
        
        @param request: CreatePublicParameterRequest
        @return: CreatePublicParameterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_public_parameter_with_options_async(request, runtime)

    def create_public_patch_baseline_with_options(
        self,
        request: oosops_20190601_models.CreatePublicPatchBaselineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.CreatePublicPatchBaselineResponse:
        """
        @param request: CreatePublicPatchBaselineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePublicPatchBaselineResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.approval_rules):
            query['ApprovalRules'] = request.approval_rules
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.operation_system):
            query['OperationSystem'] = request.operation_system
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePublicPatchBaseline',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.CreatePublicPatchBaselineResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_public_patch_baseline_with_options_async(
        self,
        request: oosops_20190601_models.CreatePublicPatchBaselineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.CreatePublicPatchBaselineResponse:
        """
        @param request: CreatePublicPatchBaselineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePublicPatchBaselineResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.approval_rules):
            query['ApprovalRules'] = request.approval_rules
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.operation_system):
            query['OperationSystem'] = request.operation_system
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePublicPatchBaseline',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.CreatePublicPatchBaselineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_public_patch_baseline(
        self,
        request: oosops_20190601_models.CreatePublicPatchBaselineRequest,
    ) -> oosops_20190601_models.CreatePublicPatchBaselineResponse:
        """
        @param request: CreatePublicPatchBaselineRequest
        @return: CreatePublicPatchBaselineResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_public_patch_baseline_with_options(request, runtime)

    async def create_public_patch_baseline_async(
        self,
        request: oosops_20190601_models.CreatePublicPatchBaselineRequest,
    ) -> oosops_20190601_models.CreatePublicPatchBaselineResponse:
        """
        @param request: CreatePublicPatchBaselineRequest
        @return: CreatePublicPatchBaselineResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_public_patch_baseline_with_options_async(request, runtime)

    def create_public_template_with_options(
        self,
        request: oosops_20190601_models.CreatePublicTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.CreatePublicTemplateResponse:
        """
        @param request: CreatePublicTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePublicTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.is_example):
            query['IsExample'] = request.is_example
        if not UtilClient.is_unset(request.popularity):
            query['Popularity'] = request.popularity
        if not UtilClient.is_unset(request.publisher):
            query['Publisher'] = request.publisher
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.version_name):
            query['VersionName'] = request.version_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePublicTemplate',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.CreatePublicTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_public_template_with_options_async(
        self,
        request: oosops_20190601_models.CreatePublicTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.CreatePublicTemplateResponse:
        """
        @param request: CreatePublicTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePublicTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.is_example):
            query['IsExample'] = request.is_example
        if not UtilClient.is_unset(request.popularity):
            query['Popularity'] = request.popularity
        if not UtilClient.is_unset(request.publisher):
            query['Publisher'] = request.publisher
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.version_name):
            query['VersionName'] = request.version_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePublicTemplate',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.CreatePublicTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_public_template(
        self,
        request: oosops_20190601_models.CreatePublicTemplateRequest,
    ) -> oosops_20190601_models.CreatePublicTemplateResponse:
        """
        @param request: CreatePublicTemplateRequest
        @return: CreatePublicTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_public_template_with_options(request, runtime)

    async def create_public_template_async(
        self,
        request: oosops_20190601_models.CreatePublicTemplateRequest,
    ) -> oosops_20190601_models.CreatePublicTemplateResponse:
        """
        @param request: CreatePublicTemplateRequest
        @return: CreatePublicTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_public_template_with_options_async(request, runtime)

    def delete_failure_msg_with_options(
        self,
        request: oosops_20190601_models.DeleteFailureMsgRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.DeleteFailureMsgResponse:
        """
        @param request: DeleteFailureMsgRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFailureMsgResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.operation):
            query['Operation'] = request.operation
        if not UtilClient.is_unset(request.request_fingerprint):
            query['RequestFingerprint'] = request.request_fingerprint
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFailureMsg',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.DeleteFailureMsgResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_failure_msg_with_options_async(
        self,
        request: oosops_20190601_models.DeleteFailureMsgRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.DeleteFailureMsgResponse:
        """
        @param request: DeleteFailureMsgRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFailureMsgResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.operation):
            query['Operation'] = request.operation
        if not UtilClient.is_unset(request.request_fingerprint):
            query['RequestFingerprint'] = request.request_fingerprint
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFailureMsg',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.DeleteFailureMsgResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_failure_msg(
        self,
        request: oosops_20190601_models.DeleteFailureMsgRequest,
    ) -> oosops_20190601_models.DeleteFailureMsgResponse:
        """
        @param request: DeleteFailureMsgRequest
        @return: DeleteFailureMsgResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_failure_msg_with_options(request, runtime)

    async def delete_failure_msg_async(
        self,
        request: oosops_20190601_models.DeleteFailureMsgRequest,
    ) -> oosops_20190601_models.DeleteFailureMsgResponse:
        """
        @param request: DeleteFailureMsgRequest
        @return: DeleteFailureMsgResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_failure_msg_with_options_async(request, runtime)

    def delete_public_parameter_with_options(
        self,
        request: oosops_20190601_models.DeletePublicParameterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.DeletePublicParameterResponse:
        """
        @summary 删除公共参数。
        
        @param request: DeletePublicParameterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePublicParameterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePublicParameter',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.DeletePublicParameterResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_public_parameter_with_options_async(
        self,
        request: oosops_20190601_models.DeletePublicParameterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.DeletePublicParameterResponse:
        """
        @summary 删除公共参数。
        
        @param request: DeletePublicParameterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePublicParameterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePublicParameter',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.DeletePublicParameterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_public_parameter(
        self,
        request: oosops_20190601_models.DeletePublicParameterRequest,
    ) -> oosops_20190601_models.DeletePublicParameterResponse:
        """
        @summary 删除公共参数。
        
        @param request: DeletePublicParameterRequest
        @return: DeletePublicParameterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_public_parameter_with_options(request, runtime)

    async def delete_public_parameter_async(
        self,
        request: oosops_20190601_models.DeletePublicParameterRequest,
    ) -> oosops_20190601_models.DeletePublicParameterResponse:
        """
        @summary 删除公共参数。
        
        @param request: DeletePublicParameterRequest
        @return: DeletePublicParameterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_public_parameter_with_options_async(request, runtime)

    def delete_public_patch_baseline_with_options(
        self,
        request: oosops_20190601_models.DeletePublicPatchBaselineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.DeletePublicPatchBaselineResponse:
        """
        @param request: DeletePublicPatchBaselineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePublicPatchBaselineResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePublicPatchBaseline',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.DeletePublicPatchBaselineResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_public_patch_baseline_with_options_async(
        self,
        request: oosops_20190601_models.DeletePublicPatchBaselineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.DeletePublicPatchBaselineResponse:
        """
        @param request: DeletePublicPatchBaselineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePublicPatchBaselineResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePublicPatchBaseline',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.DeletePublicPatchBaselineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_public_patch_baseline(
        self,
        request: oosops_20190601_models.DeletePublicPatchBaselineRequest,
    ) -> oosops_20190601_models.DeletePublicPatchBaselineResponse:
        """
        @param request: DeletePublicPatchBaselineRequest
        @return: DeletePublicPatchBaselineResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_public_patch_baseline_with_options(request, runtime)

    async def delete_public_patch_baseline_async(
        self,
        request: oosops_20190601_models.DeletePublicPatchBaselineRequest,
    ) -> oosops_20190601_models.DeletePublicPatchBaselineResponse:
        """
        @param request: DeletePublicPatchBaselineRequest
        @return: DeletePublicPatchBaselineResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_public_patch_baseline_with_options_async(request, runtime)

    def delete_public_template_with_options(
        self,
        request: oosops_20190601_models.DeletePublicTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.DeletePublicTemplateResponse:
        """
        @param request: DeletePublicTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePublicTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePublicTemplate',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.DeletePublicTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_public_template_with_options_async(
        self,
        request: oosops_20190601_models.DeletePublicTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.DeletePublicTemplateResponse:
        """
        @param request: DeletePublicTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePublicTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePublicTemplate',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.DeletePublicTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_public_template(
        self,
        request: oosops_20190601_models.DeletePublicTemplateRequest,
    ) -> oosops_20190601_models.DeletePublicTemplateResponse:
        """
        @param request: DeletePublicTemplateRequest
        @return: DeletePublicTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_public_template_with_options(request, runtime)

    async def delete_public_template_async(
        self,
        request: oosops_20190601_models.DeletePublicTemplateRequest,
    ) -> oosops_20190601_models.DeletePublicTemplateResponse:
        """
        @param request: DeletePublicTemplateRequest
        @return: DeletePublicTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_public_template_with_options_async(request, runtime)

    def do_check_resource_with_options(
        self,
        request: oosops_20190601_models.DoCheckResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.DoCheckResourceResponse:
        """
        @param request: DoCheckResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DoCheckResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bid):
            query['bid'] = request.bid
        if not UtilClient.is_unset(request.country):
            query['country'] = request.country
        if not UtilClient.is_unset(request.gmt_wakeup):
            query['gmtWakeup'] = request.gmt_wakeup
        if not UtilClient.is_unset(request.hid):
            query['hid'] = request.hid
        if not UtilClient.is_unset(request.interrupt):
            query['interrupt'] = request.interrupt
        if not UtilClient.is_unset(request.invoker):
            query['invoker'] = request.invoker
        if not UtilClient.is_unset(request.level):
            query['level'] = request.level
        if not UtilClient.is_unset(request.message):
            query['message'] = request.message
        if not UtilClient.is_unset(request.pk):
            query['pk'] = request.pk
        if not UtilClient.is_unset(request.prompt):
            query['prompt'] = request.prompt
        if not UtilClient.is_unset(request.success):
            query['success'] = request.success
        if not UtilClient.is_unset(request.task_extra_data):
            query['taskExtraData'] = request.task_extra_data
        if not UtilClient.is_unset(request.task_identifier):
            query['taskIdentifier'] = request.task_identifier
        if not UtilClient.is_unset(request.url):
            query['url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DoCheckResource',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.DoCheckResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def do_check_resource_with_options_async(
        self,
        request: oosops_20190601_models.DoCheckResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.DoCheckResourceResponse:
        """
        @param request: DoCheckResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DoCheckResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bid):
            query['bid'] = request.bid
        if not UtilClient.is_unset(request.country):
            query['country'] = request.country
        if not UtilClient.is_unset(request.gmt_wakeup):
            query['gmtWakeup'] = request.gmt_wakeup
        if not UtilClient.is_unset(request.hid):
            query['hid'] = request.hid
        if not UtilClient.is_unset(request.interrupt):
            query['interrupt'] = request.interrupt
        if not UtilClient.is_unset(request.invoker):
            query['invoker'] = request.invoker
        if not UtilClient.is_unset(request.level):
            query['level'] = request.level
        if not UtilClient.is_unset(request.message):
            query['message'] = request.message
        if not UtilClient.is_unset(request.pk):
            query['pk'] = request.pk
        if not UtilClient.is_unset(request.prompt):
            query['prompt'] = request.prompt
        if not UtilClient.is_unset(request.success):
            query['success'] = request.success
        if not UtilClient.is_unset(request.task_extra_data):
            query['taskExtraData'] = request.task_extra_data
        if not UtilClient.is_unset(request.task_identifier):
            query['taskIdentifier'] = request.task_identifier
        if not UtilClient.is_unset(request.url):
            query['url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DoCheckResource',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.DoCheckResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def do_check_resource(
        self,
        request: oosops_20190601_models.DoCheckResourceRequest,
    ) -> oosops_20190601_models.DoCheckResourceResponse:
        """
        @param request: DoCheckResourceRequest
        @return: DoCheckResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.do_check_resource_with_options(request, runtime)

    async def do_check_resource_async(
        self,
        request: oosops_20190601_models.DoCheckResourceRequest,
    ) -> oosops_20190601_models.DoCheckResourceResponse:
        """
        @param request: DoCheckResourceRequest
        @return: DoCheckResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.do_check_resource_with_options_async(request, runtime)

    def get_action_with_options(
        self,
        request: oosops_20190601_models.GetActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.GetActionResponse:
        """
        @summary 获取action的详细信息
        
        @param request: GetActionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetActionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_name):
            query['ActionName'] = request.action_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAction',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.GetActionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_action_with_options_async(
        self,
        request: oosops_20190601_models.GetActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.GetActionResponse:
        """
        @summary 获取action的详细信息
        
        @param request: GetActionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetActionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_name):
            query['ActionName'] = request.action_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAction',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.GetActionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_action(
        self,
        request: oosops_20190601_models.GetActionRequest,
    ) -> oosops_20190601_models.GetActionResponse:
        """
        @summary 获取action的详细信息
        
        @param request: GetActionRequest
        @return: GetActionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_action_with_options(request, runtime)

    async def get_action_async(
        self,
        request: oosops_20190601_models.GetActionRequest,
    ) -> oosops_20190601_models.GetActionResponse:
        """
        @summary 获取action的详细信息
        
        @param request: GetActionRequest
        @return: GetActionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_action_with_options_async(request, runtime)

    def get_flow_control_with_options(
        self,
        request: oosops_20190601_models.GetFlowControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.GetFlowControlResponse:
        """
        @param request: GetFlowControlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFlowControlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api):
            query['Api'] = request.api
        if not UtilClient.is_unset(request.service):
            query['Service'] = request.service
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFlowControl',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.GetFlowControlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_flow_control_with_options_async(
        self,
        request: oosops_20190601_models.GetFlowControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.GetFlowControlResponse:
        """
        @param request: GetFlowControlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFlowControlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api):
            query['Api'] = request.api
        if not UtilClient.is_unset(request.service):
            query['Service'] = request.service
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFlowControl',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.GetFlowControlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_flow_control(
        self,
        request: oosops_20190601_models.GetFlowControlRequest,
    ) -> oosops_20190601_models.GetFlowControlResponse:
        """
        @param request: GetFlowControlRequest
        @return: GetFlowControlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_flow_control_with_options(request, runtime)

    async def get_flow_control_async(
        self,
        request: oosops_20190601_models.GetFlowControlRequest,
    ) -> oosops_20190601_models.GetFlowControlResponse:
        """
        @param request: GetFlowControlRequest
        @return: GetFlowControlResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_flow_control_with_options_async(request, runtime)

    def get_public_parameter_with_options(
        self,
        request: oosops_20190601_models.GetPublicParameterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.GetPublicParameterResponse:
        """
        @summary 获取一个公共参数，包括参数值。
        
        @param request: GetPublicParameterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPublicParameterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.parameter_version):
            query['ParameterVersion'] = request.parameter_version
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPublicParameter',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.GetPublicParameterResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_public_parameter_with_options_async(
        self,
        request: oosops_20190601_models.GetPublicParameterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.GetPublicParameterResponse:
        """
        @summary 获取一个公共参数，包括参数值。
        
        @param request: GetPublicParameterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPublicParameterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.parameter_version):
            query['ParameterVersion'] = request.parameter_version
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPublicParameter',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.GetPublicParameterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_public_parameter(
        self,
        request: oosops_20190601_models.GetPublicParameterRequest,
    ) -> oosops_20190601_models.GetPublicParameterResponse:
        """
        @summary 获取一个公共参数，包括参数值。
        
        @param request: GetPublicParameterRequest
        @return: GetPublicParameterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_public_parameter_with_options(request, runtime)

    async def get_public_parameter_async(
        self,
        request: oosops_20190601_models.GetPublicParameterRequest,
    ) -> oosops_20190601_models.GetPublicParameterResponse:
        """
        @summary 获取一个公共参数，包括参数值。
        
        @param request: GetPublicParameterRequest
        @return: GetPublicParameterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_public_parameter_with_options_async(request, runtime)

    def get_public_patch_baseline_with_options(
        self,
        request: oosops_20190601_models.GetPublicPatchBaselineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.GetPublicPatchBaselineResponse:
        """
        @param request: GetPublicPatchBaselineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPublicPatchBaselineResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPublicPatchBaseline',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.GetPublicPatchBaselineResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_public_patch_baseline_with_options_async(
        self,
        request: oosops_20190601_models.GetPublicPatchBaselineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.GetPublicPatchBaselineResponse:
        """
        @param request: GetPublicPatchBaselineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPublicPatchBaselineResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPublicPatchBaseline',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.GetPublicPatchBaselineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_public_patch_baseline(
        self,
        request: oosops_20190601_models.GetPublicPatchBaselineRequest,
    ) -> oosops_20190601_models.GetPublicPatchBaselineResponse:
        """
        @param request: GetPublicPatchBaselineRequest
        @return: GetPublicPatchBaselineResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_public_patch_baseline_with_options(request, runtime)

    async def get_public_patch_baseline_async(
        self,
        request: oosops_20190601_models.GetPublicPatchBaselineRequest,
    ) -> oosops_20190601_models.GetPublicPatchBaselineResponse:
        """
        @param request: GetPublicPatchBaselineRequest
        @return: GetPublicPatchBaselineResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_public_patch_baseline_with_options_async(request, runtime)

    def get_public_template_with_options(
        self,
        request: oosops_20190601_models.GetPublicTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.GetPublicTemplateResponse:
        """
        @param request: GetPublicTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPublicTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.template_version):
            query['TemplateVersion'] = request.template_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPublicTemplate',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.GetPublicTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_public_template_with_options_async(
        self,
        request: oosops_20190601_models.GetPublicTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.GetPublicTemplateResponse:
        """
        @param request: GetPublicTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPublicTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.template_version):
            query['TemplateVersion'] = request.template_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPublicTemplate',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.GetPublicTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_public_template(
        self,
        request: oosops_20190601_models.GetPublicTemplateRequest,
    ) -> oosops_20190601_models.GetPublicTemplateResponse:
        """
        @param request: GetPublicTemplateRequest
        @return: GetPublicTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_public_template_with_options(request, runtime)

    async def get_public_template_async(
        self,
        request: oosops_20190601_models.GetPublicTemplateRequest,
    ) -> oosops_20190601_models.GetPublicTemplateResponse:
        """
        @param request: GetPublicTemplateRequest
        @return: GetPublicTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_public_template_with_options_async(request, runtime)

    def get_quota_with_options(
        self,
        request: oosops_20190601_models.GetQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.GetQuotaResponse:
        """
        @param request: GetQuotaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQuotaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.quota_name):
            query['QuotaName'] = request.quota_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQuota',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.GetQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_quota_with_options_async(
        self,
        request: oosops_20190601_models.GetQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.GetQuotaResponse:
        """
        @param request: GetQuotaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQuotaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.quota_name):
            query['QuotaName'] = request.quota_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQuota',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.GetQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_quota(
        self,
        request: oosops_20190601_models.GetQuotaRequest,
    ) -> oosops_20190601_models.GetQuotaResponse:
        """
        @param request: GetQuotaRequest
        @return: GetQuotaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_quota_with_options(request, runtime)

    async def get_quota_async(
        self,
        request: oosops_20190601_models.GetQuotaRequest,
    ) -> oosops_20190601_models.GetQuotaResponse:
        """
        @param request: GetQuotaRequest
        @return: GetQuotaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_quota_with_options_async(request, runtime)

    def get_user_execution_template_with_options(
        self,
        request: oosops_20190601_models.GetUserExecutionTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.GetUserExecutionTemplateResponse:
        """
        @param request: GetUserExecutionTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserExecutionTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.execution_id):
            query['ExecutionId'] = request.execution_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserExecutionTemplate',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.GetUserExecutionTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_execution_template_with_options_async(
        self,
        request: oosops_20190601_models.GetUserExecutionTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.GetUserExecutionTemplateResponse:
        """
        @param request: GetUserExecutionTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserExecutionTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.execution_id):
            query['ExecutionId'] = request.execution_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserExecutionTemplate',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.GetUserExecutionTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_execution_template(
        self,
        request: oosops_20190601_models.GetUserExecutionTemplateRequest,
    ) -> oosops_20190601_models.GetUserExecutionTemplateResponse:
        """
        @param request: GetUserExecutionTemplateRequest
        @return: GetUserExecutionTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_user_execution_template_with_options(request, runtime)

    async def get_user_execution_template_async(
        self,
        request: oosops_20190601_models.GetUserExecutionTemplateRequest,
    ) -> oosops_20190601_models.GetUserExecutionTemplateResponse:
        """
        @param request: GetUserExecutionTemplateRequest
        @return: GetUserExecutionTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_user_execution_template_with_options_async(request, runtime)

    def get_user_template_with_options(
        self,
        request: oosops_20190601_models.GetUserTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.GetUserTemplateResponse:
        """
        @param request: GetUserTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.template_version):
            query['TemplateVersion'] = request.template_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserTemplate',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.GetUserTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_template_with_options_async(
        self,
        request: oosops_20190601_models.GetUserTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.GetUserTemplateResponse:
        """
        @param request: GetUserTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.template_version):
            query['TemplateVersion'] = request.template_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserTemplate',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.GetUserTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_template(
        self,
        request: oosops_20190601_models.GetUserTemplateRequest,
    ) -> oosops_20190601_models.GetUserTemplateResponse:
        """
        @param request: GetUserTemplateRequest
        @return: GetUserTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_user_template_with_options(request, runtime)

    async def get_user_template_async(
        self,
        request: oosops_20190601_models.GetUserTemplateRequest,
    ) -> oosops_20190601_models.GetUserTemplateResponse:
        """
        @param request: GetUserTemplateRequest
        @return: GetUserTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_user_template_with_options_async(request, runtime)

    def list_actions_with_options(
        self,
        request: oosops_20190601_models.ListActionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.ListActionsResponse:
        """
        @param request: ListActionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListActionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.oosaction_name):
            query['OOSActionName'] = request.oosaction_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListActions',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.ListActionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_actions_with_options_async(
        self,
        request: oosops_20190601_models.ListActionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.ListActionsResponse:
        """
        @param request: ListActionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListActionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.oosaction_name):
            query['OOSActionName'] = request.oosaction_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListActions',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.ListActionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_actions(
        self,
        request: oosops_20190601_models.ListActionsRequest,
    ) -> oosops_20190601_models.ListActionsResponse:
        """
        @param request: ListActionsRequest
        @return: ListActionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_actions_with_options(request, runtime)

    async def list_actions_async(
        self,
        request: oosops_20190601_models.ListActionsRequest,
    ) -> oosops_20190601_models.ListActionsResponse:
        """
        @param request: ListActionsRequest
        @return: ListActionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_actions_with_options_async(request, runtime)

    def list_default_quota_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.ListDefaultQuotaResponse:
        """
        @param request: ListDefaultQuotaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDefaultQuotaResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListDefaultQuota',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.ListDefaultQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_default_quota_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.ListDefaultQuotaResponse:
        """
        @param request: ListDefaultQuotaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDefaultQuotaResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListDefaultQuota',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.ListDefaultQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_default_quota(self) -> oosops_20190601_models.ListDefaultQuotaResponse:
        """
        @return: ListDefaultQuotaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_default_quota_with_options(runtime)

    async def list_default_quota_async(self) -> oosops_20190601_models.ListDefaultQuotaResponse:
        """
        @return: ListDefaultQuotaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_default_quota_with_options_async(runtime)

    def list_failure_msgs_with_options(
        self,
        request: oosops_20190601_models.ListFailureMsgsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.ListFailureMsgsResponse:
        """
        @param request: ListFailureMsgsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFailureMsgsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.request_fingerprint):
            query['RequestFingerprint'] = request.request_fingerprint
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFailureMsgs',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.ListFailureMsgsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_failure_msgs_with_options_async(
        self,
        request: oosops_20190601_models.ListFailureMsgsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.ListFailureMsgsResponse:
        """
        @param request: ListFailureMsgsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFailureMsgsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.request_fingerprint):
            query['RequestFingerprint'] = request.request_fingerprint
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFailureMsgs',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.ListFailureMsgsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_failure_msgs(
        self,
        request: oosops_20190601_models.ListFailureMsgsRequest,
    ) -> oosops_20190601_models.ListFailureMsgsResponse:
        """
        @param request: ListFailureMsgsRequest
        @return: ListFailureMsgsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_failure_msgs_with_options(request, runtime)

    async def list_failure_msgs_async(
        self,
        request: oosops_20190601_models.ListFailureMsgsRequest,
    ) -> oosops_20190601_models.ListFailureMsgsResponse:
        """
        @param request: ListFailureMsgsRequest
        @return: ListFailureMsgsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_failure_msgs_with_options_async(request, runtime)

    def list_ooslogs_with_options(
        self,
        request: oosops_20190601_models.ListOOSLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.ListOOSLogsResponse:
        """
        @param request: ListOOSLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListOOSLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.execution_id):
            query['ExecutionId'] = request.execution_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.request_fingerprint):
            query['RequestFingerprint'] = request.request_fingerprint
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOOSLogs',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.ListOOSLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ooslogs_with_options_async(
        self,
        request: oosops_20190601_models.ListOOSLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.ListOOSLogsResponse:
        """
        @param request: ListOOSLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListOOSLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.execution_id):
            query['ExecutionId'] = request.execution_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.request_fingerprint):
            query['RequestFingerprint'] = request.request_fingerprint
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOOSLogs',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.ListOOSLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ooslogs(
        self,
        request: oosops_20190601_models.ListOOSLogsRequest,
    ) -> oosops_20190601_models.ListOOSLogsResponse:
        """
        @param request: ListOOSLogsRequest
        @return: ListOOSLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_ooslogs_with_options(request, runtime)

    async def list_ooslogs_async(
        self,
        request: oosops_20190601_models.ListOOSLogsRequest,
    ) -> oosops_20190601_models.ListOOSLogsResponse:
        """
        @param request: ListOOSLogsRequest
        @return: ListOOSLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_ooslogs_with_options_async(request, runtime)

    def list_public_parameters_with_options(
        self,
        request: oosops_20190601_models.ListPublicParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.ListPublicParametersResponse:
        """
        @summary 查询公共参数。支持多种查询
        
        @param request: ListPublicParametersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPublicParametersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.parameter_type):
            query['ParameterType'] = request.parameter_type
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.recursive):
            query['Recursive'] = request.recursive
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sort_field):
            query['SortField'] = request.sort_field
        if not UtilClient.is_unset(request.sort_order):
            query['SortOrder'] = request.sort_order
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPublicParameters',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.ListPublicParametersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_public_parameters_with_options_async(
        self,
        request: oosops_20190601_models.ListPublicParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.ListPublicParametersResponse:
        """
        @summary 查询公共参数。支持多种查询
        
        @param request: ListPublicParametersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPublicParametersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.parameter_type):
            query['ParameterType'] = request.parameter_type
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.recursive):
            query['Recursive'] = request.recursive
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sort_field):
            query['SortField'] = request.sort_field
        if not UtilClient.is_unset(request.sort_order):
            query['SortOrder'] = request.sort_order
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPublicParameters',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.ListPublicParametersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_public_parameters(
        self,
        request: oosops_20190601_models.ListPublicParametersRequest,
    ) -> oosops_20190601_models.ListPublicParametersResponse:
        """
        @summary 查询公共参数。支持多种查询
        
        @param request: ListPublicParametersRequest
        @return: ListPublicParametersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_public_parameters_with_options(request, runtime)

    async def list_public_parameters_async(
        self,
        request: oosops_20190601_models.ListPublicParametersRequest,
    ) -> oosops_20190601_models.ListPublicParametersResponse:
        """
        @summary 查询公共参数。支持多种查询
        
        @param request: ListPublicParametersRequest
        @return: ListPublicParametersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_public_parameters_with_options_async(request, runtime)

    def list_public_patch_baselines_with_options(
        self,
        request: oosops_20190601_models.ListPublicPatchBaselinesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.ListPublicPatchBaselinesResponse:
        """
        @param request: ListPublicPatchBaselinesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPublicPatchBaselinesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.operation_system):
            query['OperationSystem'] = request.operation_system
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.share_type):
            query['ShareType'] = request.share_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPublicPatchBaselines',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.ListPublicPatchBaselinesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_public_patch_baselines_with_options_async(
        self,
        request: oosops_20190601_models.ListPublicPatchBaselinesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.ListPublicPatchBaselinesResponse:
        """
        @param request: ListPublicPatchBaselinesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPublicPatchBaselinesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.operation_system):
            query['OperationSystem'] = request.operation_system
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.share_type):
            query['ShareType'] = request.share_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPublicPatchBaselines',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.ListPublicPatchBaselinesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_public_patch_baselines(
        self,
        request: oosops_20190601_models.ListPublicPatchBaselinesRequest,
    ) -> oosops_20190601_models.ListPublicPatchBaselinesResponse:
        """
        @param request: ListPublicPatchBaselinesRequest
        @return: ListPublicPatchBaselinesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_public_patch_baselines_with_options(request, runtime)

    async def list_public_patch_baselines_async(
        self,
        request: oosops_20190601_models.ListPublicPatchBaselinesRequest,
    ) -> oosops_20190601_models.ListPublicPatchBaselinesResponse:
        """
        @param request: ListPublicPatchBaselinesRequest
        @return: ListPublicPatchBaselinesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_public_patch_baselines_with_options_async(request, runtime)

    def list_public_template_registrations_with_options(
        self,
        request: oosops_20190601_models.ListPublicTemplateRegistrationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.ListPublicTemplateRegistrationsResponse:
        """
        @param request: ListPublicTemplateRegistrationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPublicTemplateRegistrationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.registration_id):
            query['RegistrationId'] = request.registration_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPublicTemplateRegistrations',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.ListPublicTemplateRegistrationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_public_template_registrations_with_options_async(
        self,
        request: oosops_20190601_models.ListPublicTemplateRegistrationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.ListPublicTemplateRegistrationsResponse:
        """
        @param request: ListPublicTemplateRegistrationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPublicTemplateRegistrationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.registration_id):
            query['RegistrationId'] = request.registration_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPublicTemplateRegistrations',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.ListPublicTemplateRegistrationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_public_template_registrations(
        self,
        request: oosops_20190601_models.ListPublicTemplateRegistrationsRequest,
    ) -> oosops_20190601_models.ListPublicTemplateRegistrationsResponse:
        """
        @param request: ListPublicTemplateRegistrationsRequest
        @return: ListPublicTemplateRegistrationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_public_template_registrations_with_options(request, runtime)

    async def list_public_template_registrations_async(
        self,
        request: oosops_20190601_models.ListPublicTemplateRegistrationsRequest,
    ) -> oosops_20190601_models.ListPublicTemplateRegistrationsResponse:
        """
        @param request: ListPublicTemplateRegistrationsRequest
        @return: ListPublicTemplateRegistrationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_public_template_registrations_with_options_async(request, runtime)

    def list_public_templates_with_options(
        self,
        request: oosops_20190601_models.ListPublicTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.ListPublicTemplatesResponse:
        """
        @param request: ListPublicTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPublicTemplatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.created_by):
            query['CreatedBy'] = request.created_by
        if not UtilClient.is_unset(request.created_date_after):
            query['CreatedDateAfter'] = request.created_date_after
        if not UtilClient.is_unset(request.created_date_before):
            query['CreatedDateBefore'] = request.created_date_before
        if not UtilClient.is_unset(request.is_example):
            query['IsExample'] = request.is_example
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.popularity):
            query['Popularity'] = request.popularity
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.share_type):
            query['ShareType'] = request.share_type
        if not UtilClient.is_unset(request.sort_field):
            query['SortField'] = request.sort_field
        if not UtilClient.is_unset(request.sort_order):
            query['SortOrder'] = request.sort_order
        if not UtilClient.is_unset(request.template_format):
            query['TemplateFormat'] = request.template_format
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPublicTemplates',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.ListPublicTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_public_templates_with_options_async(
        self,
        request: oosops_20190601_models.ListPublicTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.ListPublicTemplatesResponse:
        """
        @param request: ListPublicTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPublicTemplatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.created_by):
            query['CreatedBy'] = request.created_by
        if not UtilClient.is_unset(request.created_date_after):
            query['CreatedDateAfter'] = request.created_date_after
        if not UtilClient.is_unset(request.created_date_before):
            query['CreatedDateBefore'] = request.created_date_before
        if not UtilClient.is_unset(request.is_example):
            query['IsExample'] = request.is_example
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.popularity):
            query['Popularity'] = request.popularity
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.share_type):
            query['ShareType'] = request.share_type
        if not UtilClient.is_unset(request.sort_field):
            query['SortField'] = request.sort_field
        if not UtilClient.is_unset(request.sort_order):
            query['SortOrder'] = request.sort_order
        if not UtilClient.is_unset(request.template_format):
            query['TemplateFormat'] = request.template_format
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPublicTemplates',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.ListPublicTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_public_templates(
        self,
        request: oosops_20190601_models.ListPublicTemplatesRequest,
    ) -> oosops_20190601_models.ListPublicTemplatesResponse:
        """
        @param request: ListPublicTemplatesRequest
        @return: ListPublicTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_public_templates_with_options(request, runtime)

    async def list_public_templates_async(
        self,
        request: oosops_20190601_models.ListPublicTemplatesRequest,
    ) -> oosops_20190601_models.ListPublicTemplatesResponse:
        """
        @param request: ListPublicTemplatesRequest
        @return: ListPublicTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_public_templates_with_options_async(request, runtime)

    def list_user_execution_logs_with_options(
        self,
        request: oosops_20190601_models.ListUserExecutionLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.ListUserExecutionLogsResponse:
        """
        @param request: ListUserExecutionLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserExecutionLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.execution_id):
            query['ExecutionId'] = request.execution_id
        if not UtilClient.is_unset(request.log_type):
            query['LogType'] = request.log_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.task_execution_id):
            query['TaskExecutionId'] = request.task_execution_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserExecutionLogs',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.ListUserExecutionLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_execution_logs_with_options_async(
        self,
        request: oosops_20190601_models.ListUserExecutionLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.ListUserExecutionLogsResponse:
        """
        @param request: ListUserExecutionLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserExecutionLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.execution_id):
            query['ExecutionId'] = request.execution_id
        if not UtilClient.is_unset(request.log_type):
            query['LogType'] = request.log_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.task_execution_id):
            query['TaskExecutionId'] = request.task_execution_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserExecutionLogs',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.ListUserExecutionLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_execution_logs(
        self,
        request: oosops_20190601_models.ListUserExecutionLogsRequest,
    ) -> oosops_20190601_models.ListUserExecutionLogsResponse:
        """
        @param request: ListUserExecutionLogsRequest
        @return: ListUserExecutionLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_user_execution_logs_with_options(request, runtime)

    async def list_user_execution_logs_async(
        self,
        request: oosops_20190601_models.ListUserExecutionLogsRequest,
    ) -> oosops_20190601_models.ListUserExecutionLogsResponse:
        """
        @param request: ListUserExecutionLogsRequest
        @return: ListUserExecutionLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_user_execution_logs_with_options_async(request, runtime)

    def list_user_executions_with_options(
        self,
        request: oosops_20190601_models.ListUserExecutionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.ListUserExecutionsResponse:
        """
        @param request: ListUserExecutionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserExecutionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.end_date_after):
            query['EndDateAfter'] = request.end_date_after
        if not UtilClient.is_unset(request.end_date_before):
            query['EndDateBefore'] = request.end_date_before
        if not UtilClient.is_unset(request.executed_by):
            query['ExecutedBy'] = request.executed_by
        if not UtilClient.is_unset(request.execution_id):
            query['ExecutionId'] = request.execution_id
        if not UtilClient.is_unset(request.include_child_execution):
            query['IncludeChildExecution'] = request.include_child_execution
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.parent_execution_id):
            query['ParentExecutionId'] = request.parent_execution_id
        if not UtilClient.is_unset(request.ram_role):
            query['RamRole'] = request.ram_role
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sort_field):
            query['SortField'] = request.sort_field
        if not UtilClient.is_unset(request.sort_order):
            query['SortOrder'] = request.sort_order
        if not UtilClient.is_unset(request.start_date_after):
            query['StartDateAfter'] = request.start_date_after
        if not UtilClient.is_unset(request.start_date_before):
            query['StartDateBefore'] = request.start_date_before
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserExecutions',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.ListUserExecutionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_executions_with_options_async(
        self,
        request: oosops_20190601_models.ListUserExecutionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.ListUserExecutionsResponse:
        """
        @param request: ListUserExecutionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserExecutionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.end_date_after):
            query['EndDateAfter'] = request.end_date_after
        if not UtilClient.is_unset(request.end_date_before):
            query['EndDateBefore'] = request.end_date_before
        if not UtilClient.is_unset(request.executed_by):
            query['ExecutedBy'] = request.executed_by
        if not UtilClient.is_unset(request.execution_id):
            query['ExecutionId'] = request.execution_id
        if not UtilClient.is_unset(request.include_child_execution):
            query['IncludeChildExecution'] = request.include_child_execution
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.parent_execution_id):
            query['ParentExecutionId'] = request.parent_execution_id
        if not UtilClient.is_unset(request.ram_role):
            query['RamRole'] = request.ram_role
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sort_field):
            query['SortField'] = request.sort_field
        if not UtilClient.is_unset(request.sort_order):
            query['SortOrder'] = request.sort_order
        if not UtilClient.is_unset(request.start_date_after):
            query['StartDateAfter'] = request.start_date_after
        if not UtilClient.is_unset(request.start_date_before):
            query['StartDateBefore'] = request.start_date_before
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserExecutions',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.ListUserExecutionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_executions(
        self,
        request: oosops_20190601_models.ListUserExecutionsRequest,
    ) -> oosops_20190601_models.ListUserExecutionsResponse:
        """
        @param request: ListUserExecutionsRequest
        @return: ListUserExecutionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_user_executions_with_options(request, runtime)

    async def list_user_executions_async(
        self,
        request: oosops_20190601_models.ListUserExecutionsRequest,
    ) -> oosops_20190601_models.ListUserExecutionsResponse:
        """
        @param request: ListUserExecutionsRequest
        @return: ListUserExecutionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_user_executions_with_options_async(request, runtime)

    def list_user_instance_patch_states_with_options(
        self,
        request: oosops_20190601_models.ListUserInstancePatchStatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.ListUserInstancePatchStatesResponse:
        """
        @param request: ListUserInstancePatchStatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserInstancePatchStatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserInstancePatchStates',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.ListUserInstancePatchStatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_instance_patch_states_with_options_async(
        self,
        request: oosops_20190601_models.ListUserInstancePatchStatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.ListUserInstancePatchStatesResponse:
        """
        @param request: ListUserInstancePatchStatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserInstancePatchStatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserInstancePatchStates',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.ListUserInstancePatchStatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_instance_patch_states(
        self,
        request: oosops_20190601_models.ListUserInstancePatchStatesRequest,
    ) -> oosops_20190601_models.ListUserInstancePatchStatesResponse:
        """
        @param request: ListUserInstancePatchStatesRequest
        @return: ListUserInstancePatchStatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_user_instance_patch_states_with_options(request, runtime)

    async def list_user_instance_patch_states_async(
        self,
        request: oosops_20190601_models.ListUserInstancePatchStatesRequest,
    ) -> oosops_20190601_models.ListUserInstancePatchStatesResponse:
        """
        @param request: ListUserInstancePatchStatesRequest
        @return: ListUserInstancePatchStatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_user_instance_patch_states_with_options_async(request, runtime)

    def list_user_instance_patches_with_options(
        self,
        request: oosops_20190601_models.ListUserInstancePatchesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.ListUserInstancePatchesResponse:
        """
        @param request: ListUserInstancePatchesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserInstancePatchesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserInstancePatches',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.ListUserInstancePatchesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_instance_patches_with_options_async(
        self,
        request: oosops_20190601_models.ListUserInstancePatchesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.ListUserInstancePatchesResponse:
        """
        @param request: ListUserInstancePatchesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserInstancePatchesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserInstancePatches',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.ListUserInstancePatchesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_instance_patches(
        self,
        request: oosops_20190601_models.ListUserInstancePatchesRequest,
    ) -> oosops_20190601_models.ListUserInstancePatchesResponse:
        """
        @param request: ListUserInstancePatchesRequest
        @return: ListUserInstancePatchesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_user_instance_patches_with_options(request, runtime)

    async def list_user_instance_patches_async(
        self,
        request: oosops_20190601_models.ListUserInstancePatchesRequest,
    ) -> oosops_20190601_models.ListUserInstancePatchesResponse:
        """
        @param request: ListUserInstancePatchesRequest
        @return: ListUserInstancePatchesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_user_instance_patches_with_options_async(request, runtime)

    def list_user_inventory_entries_with_options(
        self,
        request: oosops_20190601_models.ListUserInventoryEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.ListUserInventoryEntriesResponse:
        """
        @param request: ListUserInventoryEntriesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserInventoryEntriesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type_name):
            query['TypeName'] = request.type_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserInventoryEntries',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.ListUserInventoryEntriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_inventory_entries_with_options_async(
        self,
        request: oosops_20190601_models.ListUserInventoryEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.ListUserInventoryEntriesResponse:
        """
        @param request: ListUserInventoryEntriesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserInventoryEntriesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type_name):
            query['TypeName'] = request.type_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserInventoryEntries',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.ListUserInventoryEntriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_inventory_entries(
        self,
        request: oosops_20190601_models.ListUserInventoryEntriesRequest,
    ) -> oosops_20190601_models.ListUserInventoryEntriesResponse:
        """
        @param request: ListUserInventoryEntriesRequest
        @return: ListUserInventoryEntriesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_user_inventory_entries_with_options(request, runtime)

    async def list_user_inventory_entries_async(
        self,
        request: oosops_20190601_models.ListUserInventoryEntriesRequest,
    ) -> oosops_20190601_models.ListUserInventoryEntriesResponse:
        """
        @param request: ListUserInventoryEntriesRequest
        @return: ListUserInventoryEntriesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_user_inventory_entries_with_options_async(request, runtime)

    def list_user_task_executions_with_options(
        self,
        request: oosops_20190601_models.ListUserTaskExecutionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.ListUserTaskExecutionsResponse:
        """
        @param request: ListUserTaskExecutionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserTaskExecutionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.end_date_after):
            query['EndDateAfter'] = request.end_date_after
        if not UtilClient.is_unset(request.end_date_before):
            query['EndDateBefore'] = request.end_date_before
        if not UtilClient.is_unset(request.execution_id):
            query['ExecutionId'] = request.execution_id
        if not UtilClient.is_unset(request.include_child_task_execution):
            query['IncludeChildTaskExecution'] = request.include_child_task_execution
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.parent_task_execution_id):
            query['ParentTaskExecutionId'] = request.parent_task_execution_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sort_field):
            query['SortField'] = request.sort_field
        if not UtilClient.is_unset(request.sort_order):
            query['SortOrder'] = request.sort_order
        if not UtilClient.is_unset(request.start_date_after):
            query['StartDateAfter'] = request.start_date_after
        if not UtilClient.is_unset(request.start_date_before):
            query['StartDateBefore'] = request.start_date_before
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_action):
            query['TaskAction'] = request.task_action
        if not UtilClient.is_unset(request.task_execution_id):
            query['TaskExecutionId'] = request.task_execution_id
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserTaskExecutions',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.ListUserTaskExecutionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_task_executions_with_options_async(
        self,
        request: oosops_20190601_models.ListUserTaskExecutionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.ListUserTaskExecutionsResponse:
        """
        @param request: ListUserTaskExecutionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserTaskExecutionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.end_date_after):
            query['EndDateAfter'] = request.end_date_after
        if not UtilClient.is_unset(request.end_date_before):
            query['EndDateBefore'] = request.end_date_before
        if not UtilClient.is_unset(request.execution_id):
            query['ExecutionId'] = request.execution_id
        if not UtilClient.is_unset(request.include_child_task_execution):
            query['IncludeChildTaskExecution'] = request.include_child_task_execution
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.parent_task_execution_id):
            query['ParentTaskExecutionId'] = request.parent_task_execution_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sort_field):
            query['SortField'] = request.sort_field
        if not UtilClient.is_unset(request.sort_order):
            query['SortOrder'] = request.sort_order
        if not UtilClient.is_unset(request.start_date_after):
            query['StartDateAfter'] = request.start_date_after
        if not UtilClient.is_unset(request.start_date_before):
            query['StartDateBefore'] = request.start_date_before
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_action):
            query['TaskAction'] = request.task_action
        if not UtilClient.is_unset(request.task_execution_id):
            query['TaskExecutionId'] = request.task_execution_id
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserTaskExecutions',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.ListUserTaskExecutionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_task_executions(
        self,
        request: oosops_20190601_models.ListUserTaskExecutionsRequest,
    ) -> oosops_20190601_models.ListUserTaskExecutionsResponse:
        """
        @param request: ListUserTaskExecutionsRequest
        @return: ListUserTaskExecutionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_user_task_executions_with_options(request, runtime)

    async def list_user_task_executions_async(
        self,
        request: oosops_20190601_models.ListUserTaskExecutionsRequest,
    ) -> oosops_20190601_models.ListUserTaskExecutionsResponse:
        """
        @param request: ListUserTaskExecutionsRequest
        @return: ListUserTaskExecutionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_user_task_executions_with_options_async(request, runtime)

    def list_user_templates_with_options(
        self,
        request: oosops_20190601_models.ListUserTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.ListUserTemplatesResponse:
        """
        @param request: ListUserTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserTemplatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.created_by):
            query['CreatedBy'] = request.created_by
        if not UtilClient.is_unset(request.created_date_after):
            query['CreatedDateAfter'] = request.created_date_after
        if not UtilClient.is_unset(request.created_date_before):
            query['CreatedDateBefore'] = request.created_date_before
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.popularity):
            query['Popularity'] = request.popularity
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.share_type):
            query['ShareType'] = request.share_type
        if not UtilClient.is_unset(request.sort_field):
            query['SortField'] = request.sort_field
        if not UtilClient.is_unset(request.sort_order):
            query['SortOrder'] = request.sort_order
        if not UtilClient.is_unset(request.template_format):
            query['TemplateFormat'] = request.template_format
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserTemplates',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.ListUserTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_templates_with_options_async(
        self,
        request: oosops_20190601_models.ListUserTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.ListUserTemplatesResponse:
        """
        @param request: ListUserTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserTemplatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.created_by):
            query['CreatedBy'] = request.created_by
        if not UtilClient.is_unset(request.created_date_after):
            query['CreatedDateAfter'] = request.created_date_after
        if not UtilClient.is_unset(request.created_date_before):
            query['CreatedDateBefore'] = request.created_date_before
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.popularity):
            query['Popularity'] = request.popularity
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.share_type):
            query['ShareType'] = request.share_type
        if not UtilClient.is_unset(request.sort_field):
            query['SortField'] = request.sort_field
        if not UtilClient.is_unset(request.sort_order):
            query['SortOrder'] = request.sort_order
        if not UtilClient.is_unset(request.template_format):
            query['TemplateFormat'] = request.template_format
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserTemplates',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.ListUserTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_templates(
        self,
        request: oosops_20190601_models.ListUserTemplatesRequest,
    ) -> oosops_20190601_models.ListUserTemplatesResponse:
        """
        @param request: ListUserTemplatesRequest
        @return: ListUserTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_user_templates_with_options(request, runtime)

    async def list_user_templates_async(
        self,
        request: oosops_20190601_models.ListUserTemplatesRequest,
    ) -> oosops_20190601_models.ListUserTemplatesResponse:
        """
        @param request: ListUserTemplatesRequest
        @return: ListUserTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_user_templates_with_options_async(request, runtime)

    def reset_timer_trigger_execution_with_options(
        self,
        request: oosops_20190601_models.ResetTimerTriggerExecutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.ResetTimerTriggerExecutionResponse:
        """
        @param request: ResetTimerTriggerExecutionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetTimerTriggerExecutionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.execution_id):
            query['ExecutionId'] = request.execution_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetTimerTriggerExecution',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.ResetTimerTriggerExecutionResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_timer_trigger_execution_with_options_async(
        self,
        request: oosops_20190601_models.ResetTimerTriggerExecutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.ResetTimerTriggerExecutionResponse:
        """
        @param request: ResetTimerTriggerExecutionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetTimerTriggerExecutionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.execution_id):
            query['ExecutionId'] = request.execution_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetTimerTriggerExecution',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.ResetTimerTriggerExecutionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_timer_trigger_execution(
        self,
        request: oosops_20190601_models.ResetTimerTriggerExecutionRequest,
    ) -> oosops_20190601_models.ResetTimerTriggerExecutionResponse:
        """
        @param request: ResetTimerTriggerExecutionRequest
        @return: ResetTimerTriggerExecutionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reset_timer_trigger_execution_with_options(request, runtime)

    async def reset_timer_trigger_execution_async(
        self,
        request: oosops_20190601_models.ResetTimerTriggerExecutionRequest,
    ) -> oosops_20190601_models.ResetTimerTriggerExecutionResponse:
        """
        @param request: ResetTimerTriggerExecutionRequest
        @return: ResetTimerTriggerExecutionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.reset_timer_trigger_execution_with_options_async(request, runtime)

    def reset_user_execution_with_options(
        self,
        request: oosops_20190601_models.ResetUserExecutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.ResetUserExecutionResponse:
        """
        @param request: ResetUserExecutionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetUserExecutionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.execution_id):
            query['ExecutionId'] = request.execution_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetUserExecution',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.ResetUserExecutionResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_user_execution_with_options_async(
        self,
        request: oosops_20190601_models.ResetUserExecutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.ResetUserExecutionResponse:
        """
        @param request: ResetUserExecutionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetUserExecutionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.execution_id):
            query['ExecutionId'] = request.execution_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetUserExecution',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.ResetUserExecutionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_user_execution(
        self,
        request: oosops_20190601_models.ResetUserExecutionRequest,
    ) -> oosops_20190601_models.ResetUserExecutionResponse:
        """
        @param request: ResetUserExecutionRequest
        @return: ResetUserExecutionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reset_user_execution_with_options(request, runtime)

    async def reset_user_execution_async(
        self,
        request: oosops_20190601_models.ResetUserExecutionRequest,
    ) -> oosops_20190601_models.ResetUserExecutionResponse:
        """
        @param request: ResetUserExecutionRequest
        @return: ResetUserExecutionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.reset_user_execution_with_options_async(request, runtime)

    def set_flow_control_with_options(
        self,
        request: oosops_20190601_models.SetFlowControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.SetFlowControlResponse:
        """
        @param request: SetFlowControlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetFlowControlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api):
            query['Api'] = request.api
        if not UtilClient.is_unset(request.service):
            query['Service'] = request.service
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetFlowControl',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.SetFlowControlResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_flow_control_with_options_async(
        self,
        request: oosops_20190601_models.SetFlowControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.SetFlowControlResponse:
        """
        @param request: SetFlowControlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetFlowControlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api):
            query['Api'] = request.api
        if not UtilClient.is_unset(request.service):
            query['Service'] = request.service
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetFlowControl',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.SetFlowControlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_flow_control(
        self,
        request: oosops_20190601_models.SetFlowControlRequest,
    ) -> oosops_20190601_models.SetFlowControlResponse:
        """
        @param request: SetFlowControlRequest
        @return: SetFlowControlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_flow_control_with_options(request, runtime)

    async def set_flow_control_async(
        self,
        request: oosops_20190601_models.SetFlowControlRequest,
    ) -> oosops_20190601_models.SetFlowControlResponse:
        """
        @param request: SetFlowControlRequest
        @return: SetFlowControlResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_flow_control_with_options_async(request, runtime)

    def set_quota_with_options(
        self,
        request: oosops_20190601_models.SetQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.SetQuotaResponse:
        """
        @param request: SetQuotaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetQuotaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.quota_name):
            query['QuotaName'] = request.quota_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetQuota',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.SetQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_quota_with_options_async(
        self,
        request: oosops_20190601_models.SetQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.SetQuotaResponse:
        """
        @param request: SetQuotaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetQuotaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.quota_name):
            query['QuotaName'] = request.quota_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetQuota',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.SetQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_quota(
        self,
        request: oosops_20190601_models.SetQuotaRequest,
    ) -> oosops_20190601_models.SetQuotaResponse:
        """
        @param request: SetQuotaRequest
        @return: SetQuotaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_quota_with_options(request, runtime)

    async def set_quota_async(
        self,
        request: oosops_20190601_models.SetQuotaRequest,
    ) -> oosops_20190601_models.SetQuotaResponse:
        """
        @param request: SetQuotaRequest
        @return: SetQuotaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_quota_with_options_async(request, runtime)

    def terminate_user_execution_with_options(
        self,
        request: oosops_20190601_models.TerminateUserExecutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.TerminateUserExecutionResponse:
        """
        @param request: TerminateUserExecutionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TerminateUserExecutionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.execution_id):
            query['ExecutionId'] = request.execution_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TerminateUserExecution',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.TerminateUserExecutionResponse(),
            self.call_api(params, req, runtime)
        )

    async def terminate_user_execution_with_options_async(
        self,
        request: oosops_20190601_models.TerminateUserExecutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.TerminateUserExecutionResponse:
        """
        @param request: TerminateUserExecutionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TerminateUserExecutionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.execution_id):
            query['ExecutionId'] = request.execution_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TerminateUserExecution',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.TerminateUserExecutionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def terminate_user_execution(
        self,
        request: oosops_20190601_models.TerminateUserExecutionRequest,
    ) -> oosops_20190601_models.TerminateUserExecutionResponse:
        """
        @param request: TerminateUserExecutionRequest
        @return: TerminateUserExecutionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.terminate_user_execution_with_options(request, runtime)

    async def terminate_user_execution_async(
        self,
        request: oosops_20190601_models.TerminateUserExecutionRequest,
    ) -> oosops_20190601_models.TerminateUserExecutionResponse:
        """
        @param request: TerminateUserExecutionRequest
        @return: TerminateUserExecutionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.terminate_user_execution_with_options_async(request, runtime)

    def update_action_with_options(
        self,
        request: oosops_20190601_models.UpdateActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.UpdateActionResponse:
        """
        @param request: UpdateActionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateActionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_name):
            query['ActionName'] = request.action_name
        if not UtilClient.is_unset(request.action_type):
            query['ActionType'] = request.action_type
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.popularity):
            query['Popularity'] = request.popularity
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAction',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.UpdateActionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_action_with_options_async(
        self,
        request: oosops_20190601_models.UpdateActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.UpdateActionResponse:
        """
        @param request: UpdateActionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateActionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_name):
            query['ActionName'] = request.action_name
        if not UtilClient.is_unset(request.action_type):
            query['ActionType'] = request.action_type
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.popularity):
            query['Popularity'] = request.popularity
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAction',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.UpdateActionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_action(
        self,
        request: oosops_20190601_models.UpdateActionRequest,
    ) -> oosops_20190601_models.UpdateActionResponse:
        """
        @param request: UpdateActionRequest
        @return: UpdateActionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_action_with_options(request, runtime)

    async def update_action_async(
        self,
        request: oosops_20190601_models.UpdateActionRequest,
    ) -> oosops_20190601_models.UpdateActionResponse:
        """
        @param request: UpdateActionRequest
        @return: UpdateActionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_action_with_options_async(request, runtime)

    def update_public_parameter_with_options(
        self,
        request: oosops_20190601_models.UpdatePublicParameterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.UpdatePublicParameterResponse:
        """
        @summary 更新一个已存在的公共参数。
        
        @param request: UpdatePublicParameterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdatePublicParameterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePublicParameter',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.UpdatePublicParameterResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_public_parameter_with_options_async(
        self,
        request: oosops_20190601_models.UpdatePublicParameterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.UpdatePublicParameterResponse:
        """
        @summary 更新一个已存在的公共参数。
        
        @param request: UpdatePublicParameterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdatePublicParameterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePublicParameter',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.UpdatePublicParameterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_public_parameter(
        self,
        request: oosops_20190601_models.UpdatePublicParameterRequest,
    ) -> oosops_20190601_models.UpdatePublicParameterResponse:
        """
        @summary 更新一个已存在的公共参数。
        
        @param request: UpdatePublicParameterRequest
        @return: UpdatePublicParameterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_public_parameter_with_options(request, runtime)

    async def update_public_parameter_async(
        self,
        request: oosops_20190601_models.UpdatePublicParameterRequest,
    ) -> oosops_20190601_models.UpdatePublicParameterResponse:
        """
        @summary 更新一个已存在的公共参数。
        
        @param request: UpdatePublicParameterRequest
        @return: UpdatePublicParameterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_public_parameter_with_options_async(request, runtime)

    def update_public_patch_baseline_with_options(
        self,
        request: oosops_20190601_models.UpdatePublicPatchBaselineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.UpdatePublicPatchBaselineResponse:
        """
        @param request: UpdatePublicPatchBaselineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdatePublicPatchBaselineResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.approval_rules):
            query['ApprovalRules'] = request.approval_rules
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePublicPatchBaseline',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.UpdatePublicPatchBaselineResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_public_patch_baseline_with_options_async(
        self,
        request: oosops_20190601_models.UpdatePublicPatchBaselineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.UpdatePublicPatchBaselineResponse:
        """
        @param request: UpdatePublicPatchBaselineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdatePublicPatchBaselineResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.approval_rules):
            query['ApprovalRules'] = request.approval_rules
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePublicPatchBaseline',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.UpdatePublicPatchBaselineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_public_patch_baseline(
        self,
        request: oosops_20190601_models.UpdatePublicPatchBaselineRequest,
    ) -> oosops_20190601_models.UpdatePublicPatchBaselineResponse:
        """
        @param request: UpdatePublicPatchBaselineRequest
        @return: UpdatePublicPatchBaselineResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_public_patch_baseline_with_options(request, runtime)

    async def update_public_patch_baseline_async(
        self,
        request: oosops_20190601_models.UpdatePublicPatchBaselineRequest,
    ) -> oosops_20190601_models.UpdatePublicPatchBaselineResponse:
        """
        @param request: UpdatePublicPatchBaselineRequest
        @return: UpdatePublicPatchBaselineResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_public_patch_baseline_with_options_async(request, runtime)

    def update_public_template_with_options(
        self,
        request: oosops_20190601_models.UpdatePublicTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.UpdatePublicTemplateResponse:
        """
        @param request: UpdatePublicTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdatePublicTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.popularity):
            query['Popularity'] = request.popularity
        if not UtilClient.is_unset(request.publisher):
            query['Publisher'] = request.publisher
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.version_name):
            query['VersionName'] = request.version_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePublicTemplate',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.UpdatePublicTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_public_template_with_options_async(
        self,
        request: oosops_20190601_models.UpdatePublicTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.UpdatePublicTemplateResponse:
        """
        @param request: UpdatePublicTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdatePublicTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.popularity):
            query['Popularity'] = request.popularity
        if not UtilClient.is_unset(request.publisher):
            query['Publisher'] = request.publisher
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.version_name):
            query['VersionName'] = request.version_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePublicTemplate',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.UpdatePublicTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_public_template(
        self,
        request: oosops_20190601_models.UpdatePublicTemplateRequest,
    ) -> oosops_20190601_models.UpdatePublicTemplateResponse:
        """
        @param request: UpdatePublicTemplateRequest
        @return: UpdatePublicTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_public_template_with_options(request, runtime)

    async def update_public_template_async(
        self,
        request: oosops_20190601_models.UpdatePublicTemplateRequest,
    ) -> oosops_20190601_models.UpdatePublicTemplateResponse:
        """
        @param request: UpdatePublicTemplateRequest
        @return: UpdatePublicTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_public_template_with_options_async(request, runtime)

    def validate_public_template_content_with_options(
        self,
        request: oosops_20190601_models.ValidatePublicTemplateContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.ValidatePublicTemplateContentResponse:
        """
        @param request: ValidatePublicTemplateContentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ValidatePublicTemplateContentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ValidatePublicTemplateContent',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.ValidatePublicTemplateContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def validate_public_template_content_with_options_async(
        self,
        request: oosops_20190601_models.ValidatePublicTemplateContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oosops_20190601_models.ValidatePublicTemplateContentResponse:
        """
        @param request: ValidatePublicTemplateContentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ValidatePublicTemplateContentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ValidatePublicTemplateContent',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oosops_20190601_models.ValidatePublicTemplateContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def validate_public_template_content(
        self,
        request: oosops_20190601_models.ValidatePublicTemplateContentRequest,
    ) -> oosops_20190601_models.ValidatePublicTemplateContentResponse:
        """
        @param request: ValidatePublicTemplateContentRequest
        @return: ValidatePublicTemplateContentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.validate_public_template_content_with_options(request, runtime)

    async def validate_public_template_content_async(
        self,
        request: oosops_20190601_models.ValidatePublicTemplateContentRequest,
    ) -> oosops_20190601_models.ValidatePublicTemplateContentResponse:
        """
        @param request: ValidatePublicTemplateContentRequest
        @return: ValidatePublicTemplateContentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.validate_public_template_content_with_options_async(request, runtime)
