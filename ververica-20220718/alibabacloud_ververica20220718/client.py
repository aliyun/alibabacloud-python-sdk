# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ververica20220718 import models as ververica_20220718_models
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
        self.check_config(config)
        self._endpoint = self.get_endpoint('ververica', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_deployment_with_options(
        self,
        namespace: str,
        request: ververica_20220718_models.CreateDeploymentRequest,
        headers: ververica_20220718_models.CreateDeploymentHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.CreateDeploymentResponse:
        """
        @summary create a deployment
        
        @param request: CreateDeploymentRequest
        @param headers: CreateDeploymentHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDeploymentResponse
        """
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateDeployment',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/deployments',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.CreateDeploymentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_deployment_with_options_async(
        self,
        namespace: str,
        request: ververica_20220718_models.CreateDeploymentRequest,
        headers: ververica_20220718_models.CreateDeploymentHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.CreateDeploymentResponse:
        """
        @summary create a deployment
        
        @param request: CreateDeploymentRequest
        @param headers: CreateDeploymentHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDeploymentResponse
        """
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateDeployment',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/deployments',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.CreateDeploymentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_deployment(
        self,
        namespace: str,
        request: ververica_20220718_models.CreateDeploymentRequest,
    ) -> ververica_20220718_models.CreateDeploymentResponse:
        """
        @summary create a deployment
        
        @param request: CreateDeploymentRequest
        @return: CreateDeploymentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.CreateDeploymentHeaders()
        return self.create_deployment_with_options(namespace, request, headers, runtime)

    async def create_deployment_async(
        self,
        namespace: str,
        request: ververica_20220718_models.CreateDeploymentRequest,
    ) -> ververica_20220718_models.CreateDeploymentResponse:
        """
        @summary create a deployment
        
        @param request: CreateDeploymentRequest
        @return: CreateDeploymentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.CreateDeploymentHeaders()
        return await self.create_deployment_with_options_async(namespace, request, headers, runtime)

    def create_member_with_options(
        self,
        namespace: str,
        request: ververica_20220718_models.CreateMemberRequest,
        headers: ververica_20220718_models.CreateMemberHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.CreateMemberResponse:
        """
        @summary 调用CreateMember创建成员。
        
        @param request: CreateMemberRequest
        @param headers: CreateMemberHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMemberResponse
        """
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateMember',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/gateway/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/members',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.CreateMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_member_with_options_async(
        self,
        namespace: str,
        request: ververica_20220718_models.CreateMemberRequest,
        headers: ververica_20220718_models.CreateMemberHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.CreateMemberResponse:
        """
        @summary 调用CreateMember创建成员。
        
        @param request: CreateMemberRequest
        @param headers: CreateMemberHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMemberResponse
        """
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateMember',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/gateway/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/members',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.CreateMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_member(
        self,
        namespace: str,
        request: ververica_20220718_models.CreateMemberRequest,
    ) -> ververica_20220718_models.CreateMemberResponse:
        """
        @summary 调用CreateMember创建成员。
        
        @param request: CreateMemberRequest
        @return: CreateMemberResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.CreateMemberHeaders()
        return self.create_member_with_options(namespace, request, headers, runtime)

    async def create_member_async(
        self,
        namespace: str,
        request: ververica_20220718_models.CreateMemberRequest,
    ) -> ververica_20220718_models.CreateMemberResponse:
        """
        @summary 调用CreateMember创建成员。
        
        @param request: CreateMemberRequest
        @return: CreateMemberResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.CreateMemberHeaders()
        return await self.create_member_with_options_async(namespace, request, headers, runtime)

    def create_savepoint_with_options(
        self,
        namespace: str,
        request: ververica_20220718_models.CreateSavepointRequest,
        headers: ververica_20220718_models.CreateSavepointHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.CreateSavepointResponse:
        """
        @summary 调用CreateSavepoint触发一次savepoint。
        
        @param request: CreateSavepointRequest
        @param headers: CreateSavepointHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSavepointResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.deployment_id):
            body['deploymentId'] = request.deployment_id
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.native_format):
            body['nativeFormat'] = request.native_format
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSavepoint',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/savepoints',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.CreateSavepointResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_savepoint_with_options_async(
        self,
        namespace: str,
        request: ververica_20220718_models.CreateSavepointRequest,
        headers: ververica_20220718_models.CreateSavepointHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.CreateSavepointResponse:
        """
        @summary 调用CreateSavepoint触发一次savepoint。
        
        @param request: CreateSavepointRequest
        @param headers: CreateSavepointHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSavepointResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.deployment_id):
            body['deploymentId'] = request.deployment_id
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.native_format):
            body['nativeFormat'] = request.native_format
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSavepoint',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/savepoints',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.CreateSavepointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_savepoint(
        self,
        namespace: str,
        request: ververica_20220718_models.CreateSavepointRequest,
    ) -> ververica_20220718_models.CreateSavepointResponse:
        """
        @summary 调用CreateSavepoint触发一次savepoint。
        
        @param request: CreateSavepointRequest
        @return: CreateSavepointResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.CreateSavepointHeaders()
        return self.create_savepoint_with_options(namespace, request, headers, runtime)

    async def create_savepoint_async(
        self,
        namespace: str,
        request: ververica_20220718_models.CreateSavepointRequest,
    ) -> ververica_20220718_models.CreateSavepointResponse:
        """
        @summary 调用CreateSavepoint触发一次savepoint。
        
        @param request: CreateSavepointRequest
        @return: CreateSavepointResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.CreateSavepointHeaders()
        return await self.create_savepoint_with_options_async(namespace, request, headers, runtime)

    def create_variable_with_options(
        self,
        namespace: str,
        request: ververica_20220718_models.CreateVariableRequest,
        headers: ververica_20220718_models.CreateVariableHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.CreateVariableResponse:
        """
        @summary 调用CreateVariable创建变量。
        
        @param request: CreateVariableRequest
        @param headers: CreateVariableHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateVariableResponse
        """
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateVariable',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/variables',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.CreateVariableResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_variable_with_options_async(
        self,
        namespace: str,
        request: ververica_20220718_models.CreateVariableRequest,
        headers: ververica_20220718_models.CreateVariableHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.CreateVariableResponse:
        """
        @summary 调用CreateVariable创建变量。
        
        @param request: CreateVariableRequest
        @param headers: CreateVariableHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateVariableResponse
        """
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateVariable',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/variables',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.CreateVariableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_variable(
        self,
        namespace: str,
        request: ververica_20220718_models.CreateVariableRequest,
    ) -> ververica_20220718_models.CreateVariableResponse:
        """
        @summary 调用CreateVariable创建变量。
        
        @param request: CreateVariableRequest
        @return: CreateVariableResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.CreateVariableHeaders()
        return self.create_variable_with_options(namespace, request, headers, runtime)

    async def create_variable_async(
        self,
        namespace: str,
        request: ververica_20220718_models.CreateVariableRequest,
    ) -> ververica_20220718_models.CreateVariableResponse:
        """
        @summary 调用CreateVariable创建变量。
        
        @param request: CreateVariableRequest
        @return: CreateVariableResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.CreateVariableHeaders()
        return await self.create_variable_with_options_async(namespace, request, headers, runtime)

    def delete_deployment_with_options(
        self,
        namespace: str,
        deployment_id: str,
        headers: ververica_20220718_models.DeleteDeploymentHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.DeleteDeploymentResponse:
        """
        @summary delete deployment
        
        @param headers: DeleteDeploymentHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDeploymentResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='DeleteDeployment',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/deployments/{OpenApiUtilClient.get_encode_param(deployment_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.DeleteDeploymentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_deployment_with_options_async(
        self,
        namespace: str,
        deployment_id: str,
        headers: ververica_20220718_models.DeleteDeploymentHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.DeleteDeploymentResponse:
        """
        @summary delete deployment
        
        @param headers: DeleteDeploymentHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDeploymentResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='DeleteDeployment',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/deployments/{OpenApiUtilClient.get_encode_param(deployment_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.DeleteDeploymentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_deployment(
        self,
        namespace: str,
        deployment_id: str,
    ) -> ververica_20220718_models.DeleteDeploymentResponse:
        """
        @summary delete deployment
        
        @return: DeleteDeploymentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.DeleteDeploymentHeaders()
        return self.delete_deployment_with_options(namespace, deployment_id, headers, runtime)

    async def delete_deployment_async(
        self,
        namespace: str,
        deployment_id: str,
    ) -> ververica_20220718_models.DeleteDeploymentResponse:
        """
        @summary delete deployment
        
        @return: DeleteDeploymentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.DeleteDeploymentHeaders()
        return await self.delete_deployment_with_options_async(namespace, deployment_id, headers, runtime)

    def delete_job_with_options(
        self,
        namespace: str,
        job_id: str,
        headers: ververica_20220718_models.DeleteJobHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.DeleteJobResponse:
        """
        @summary delete job
        
        @param headers: DeleteJobHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteJobResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='DeleteJob',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/jobs/{OpenApiUtilClient.get_encode_param(job_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.DeleteJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_job_with_options_async(
        self,
        namespace: str,
        job_id: str,
        headers: ververica_20220718_models.DeleteJobHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.DeleteJobResponse:
        """
        @summary delete job
        
        @param headers: DeleteJobHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteJobResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='DeleteJob',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/jobs/{OpenApiUtilClient.get_encode_param(job_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.DeleteJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_job(
        self,
        namespace: str,
        job_id: str,
    ) -> ververica_20220718_models.DeleteJobResponse:
        """
        @summary delete job
        
        @return: DeleteJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.DeleteJobHeaders()
        return self.delete_job_with_options(namespace, job_id, headers, runtime)

    async def delete_job_async(
        self,
        namespace: str,
        job_id: str,
    ) -> ververica_20220718_models.DeleteJobResponse:
        """
        @summary delete job
        
        @return: DeleteJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.DeleteJobHeaders()
        return await self.delete_job_with_options_async(namespace, job_id, headers, runtime)

    def delete_member_with_options(
        self,
        namespace: str,
        member: str,
        headers: ververica_20220718_models.DeleteMemberHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.DeleteMemberResponse:
        """
        @summary 调用DeleteMember删除成员。
        
        @param headers: DeleteMemberHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMemberResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='DeleteMember',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/gateway/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/members/{OpenApiUtilClient.get_encode_param(member)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.DeleteMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_member_with_options_async(
        self,
        namespace: str,
        member: str,
        headers: ververica_20220718_models.DeleteMemberHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.DeleteMemberResponse:
        """
        @summary 调用DeleteMember删除成员。
        
        @param headers: DeleteMemberHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMemberResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='DeleteMember',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/gateway/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/members/{OpenApiUtilClient.get_encode_param(member)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.DeleteMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_member(
        self,
        namespace: str,
        member: str,
    ) -> ververica_20220718_models.DeleteMemberResponse:
        """
        @summary 调用DeleteMember删除成员。
        
        @return: DeleteMemberResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.DeleteMemberHeaders()
        return self.delete_member_with_options(namespace, member, headers, runtime)

    async def delete_member_async(
        self,
        namespace: str,
        member: str,
    ) -> ververica_20220718_models.DeleteMemberResponse:
        """
        @summary 调用DeleteMember删除成员。
        
        @return: DeleteMemberResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.DeleteMemberHeaders()
        return await self.delete_member_with_options_async(namespace, member, headers, runtime)

    def delete_savepoint_with_options(
        self,
        namespace: str,
        savepoint_id: str,
        headers: ververica_20220718_models.DeleteSavepointHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.DeleteSavepointResponse:
        """
        @summary 调用DeleteSavepoint删除savepoint。
        
        @param headers: DeleteSavepointHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSavepointResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='DeleteSavepoint',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/savepoints/{OpenApiUtilClient.get_encode_param(savepoint_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.DeleteSavepointResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_savepoint_with_options_async(
        self,
        namespace: str,
        savepoint_id: str,
        headers: ververica_20220718_models.DeleteSavepointHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.DeleteSavepointResponse:
        """
        @summary 调用DeleteSavepoint删除savepoint。
        
        @param headers: DeleteSavepointHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSavepointResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='DeleteSavepoint',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/savepoints/{OpenApiUtilClient.get_encode_param(savepoint_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.DeleteSavepointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_savepoint(
        self,
        namespace: str,
        savepoint_id: str,
    ) -> ververica_20220718_models.DeleteSavepointResponse:
        """
        @summary 调用DeleteSavepoint删除savepoint。
        
        @return: DeleteSavepointResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.DeleteSavepointHeaders()
        return self.delete_savepoint_with_options(namespace, savepoint_id, headers, runtime)

    async def delete_savepoint_async(
        self,
        namespace: str,
        savepoint_id: str,
    ) -> ververica_20220718_models.DeleteSavepointResponse:
        """
        @summary 调用DeleteSavepoint删除savepoint。
        
        @return: DeleteSavepointResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.DeleteSavepointHeaders()
        return await self.delete_savepoint_with_options_async(namespace, savepoint_id, headers, runtime)

    def delete_variable_with_options(
        self,
        namespace: str,
        name: str,
        headers: ververica_20220718_models.DeleteVariableHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.DeleteVariableResponse:
        """
        @summary deleta variable
        
        @param headers: DeleteVariableHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteVariableResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='DeleteVariable',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/variables/{OpenApiUtilClient.get_encode_param(name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.DeleteVariableResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_variable_with_options_async(
        self,
        namespace: str,
        name: str,
        headers: ververica_20220718_models.DeleteVariableHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.DeleteVariableResponse:
        """
        @summary deleta variable
        
        @param headers: DeleteVariableHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteVariableResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='DeleteVariable',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/variables/{OpenApiUtilClient.get_encode_param(name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.DeleteVariableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_variable(
        self,
        namespace: str,
        name: str,
    ) -> ververica_20220718_models.DeleteVariableResponse:
        """
        @summary deleta variable
        
        @return: DeleteVariableResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.DeleteVariableHeaders()
        return self.delete_variable_with_options(namespace, name, headers, runtime)

    async def delete_variable_async(
        self,
        namespace: str,
        name: str,
    ) -> ververica_20220718_models.DeleteVariableResponse:
        """
        @summary deleta variable
        
        @return: DeleteVariableResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.DeleteVariableHeaders()
        return await self.delete_variable_with_options_async(namespace, name, headers, runtime)

    def flink_api_proxy_with_options(
        self,
        request: ververica_20220718_models.FlinkApiProxyRequest,
        headers: ververica_20220718_models.FlinkApiProxyHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.FlinkApiProxyResponse:
        """
        @summary 调用FlinkApiProxy代理Flink请求。
        
        @param request: FlinkApiProxyRequest
        @param headers: FlinkApiProxyHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: FlinkApiProxyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.flink_api_path):
            query['flinkApiPath'] = request.flink_api_path
        if not UtilClient.is_unset(request.namespace):
            query['namespace'] = request.namespace
        if not UtilClient.is_unset(request.resource_id):
            query['resourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['resourceType'] = request.resource_type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FlinkApiProxy',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/flink-ui/v2/proxy',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.FlinkApiProxyResponse(),
            self.call_api(params, req, runtime)
        )

    async def flink_api_proxy_with_options_async(
        self,
        request: ververica_20220718_models.FlinkApiProxyRequest,
        headers: ververica_20220718_models.FlinkApiProxyHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.FlinkApiProxyResponse:
        """
        @summary 调用FlinkApiProxy代理Flink请求。
        
        @param request: FlinkApiProxyRequest
        @param headers: FlinkApiProxyHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: FlinkApiProxyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.flink_api_path):
            query['flinkApiPath'] = request.flink_api_path
        if not UtilClient.is_unset(request.namespace):
            query['namespace'] = request.namespace
        if not UtilClient.is_unset(request.resource_id):
            query['resourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['resourceType'] = request.resource_type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FlinkApiProxy',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/flink-ui/v2/proxy',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.FlinkApiProxyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def flink_api_proxy(
        self,
        request: ververica_20220718_models.FlinkApiProxyRequest,
    ) -> ververica_20220718_models.FlinkApiProxyResponse:
        """
        @summary 调用FlinkApiProxy代理Flink请求。
        
        @param request: FlinkApiProxyRequest
        @return: FlinkApiProxyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.FlinkApiProxyHeaders()
        return self.flink_api_proxy_with_options(request, headers, runtime)

    async def flink_api_proxy_async(
        self,
        request: ververica_20220718_models.FlinkApiProxyRequest,
    ) -> ververica_20220718_models.FlinkApiProxyResponse:
        """
        @summary 调用FlinkApiProxy代理Flink请求。
        
        @param request: FlinkApiProxyRequest
        @return: FlinkApiProxyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.FlinkApiProxyHeaders()
        return await self.flink_api_proxy_with_options_async(request, headers, runtime)

    def generate_resource_plan_with_flink_conf_async_with_options(
        self,
        namespace: str,
        deployment_id: str,
        request: ververica_20220718_models.GenerateResourcePlanWithFlinkConfAsyncRequest,
        headers: ververica_20220718_models.GenerateResourcePlanWithFlinkConfAsyncHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.GenerateResourcePlanWithFlinkConfAsyncResponse:
        """
        @summary generate resource plan with flink conf async.
        
        @param request: GenerateResourcePlanWithFlinkConfAsyncRequest
        @param headers: GenerateResourcePlanWithFlinkConfAsyncHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateResourcePlanWithFlinkConfAsyncResponse
        """
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='GenerateResourcePlanWithFlinkConfAsync',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/deployments/{OpenApiUtilClient.get_encode_param(deployment_id)}/resource-plan%3AasyncGenerate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.GenerateResourcePlanWithFlinkConfAsyncResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_resource_plan_with_flink_conf_async_with_options_async(
        self,
        namespace: str,
        deployment_id: str,
        request: ververica_20220718_models.GenerateResourcePlanWithFlinkConfAsyncRequest,
        headers: ververica_20220718_models.GenerateResourcePlanWithFlinkConfAsyncHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.GenerateResourcePlanWithFlinkConfAsyncResponse:
        """
        @summary generate resource plan with flink conf async.
        
        @param request: GenerateResourcePlanWithFlinkConfAsyncRequest
        @param headers: GenerateResourcePlanWithFlinkConfAsyncHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateResourcePlanWithFlinkConfAsyncResponse
        """
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='GenerateResourcePlanWithFlinkConfAsync',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/deployments/{OpenApiUtilClient.get_encode_param(deployment_id)}/resource-plan%3AasyncGenerate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.GenerateResourcePlanWithFlinkConfAsyncResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_resource_plan_with_flink_conf_async(
        self,
        namespace: str,
        deployment_id: str,
        request: ververica_20220718_models.GenerateResourcePlanWithFlinkConfAsyncRequest,
    ) -> ververica_20220718_models.GenerateResourcePlanWithFlinkConfAsyncResponse:
        """
        @summary generate resource plan with flink conf async.
        
        @param request: GenerateResourcePlanWithFlinkConfAsyncRequest
        @return: GenerateResourcePlanWithFlinkConfAsyncResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.GenerateResourcePlanWithFlinkConfAsyncHeaders()
        return self.generate_resource_plan_with_flink_conf_async_with_options(namespace, deployment_id, request, headers, runtime)

    async def generate_resource_plan_with_flink_conf_async_async(
        self,
        namespace: str,
        deployment_id: str,
        request: ververica_20220718_models.GenerateResourcePlanWithFlinkConfAsyncRequest,
    ) -> ververica_20220718_models.GenerateResourcePlanWithFlinkConfAsyncResponse:
        """
        @summary generate resource plan with flink conf async.
        
        @param request: GenerateResourcePlanWithFlinkConfAsyncRequest
        @return: GenerateResourcePlanWithFlinkConfAsyncResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.GenerateResourcePlanWithFlinkConfAsyncHeaders()
        return await self.generate_resource_plan_with_flink_conf_async_with_options_async(namespace, deployment_id, request, headers, runtime)

    def get_deployment_with_options(
        self,
        namespace: str,
        deployment_id: str,
        headers: ververica_20220718_models.GetDeploymentHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.GetDeploymentResponse:
        """
        @summary get a deployment
        
        @param headers: GetDeploymentHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDeploymentResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='GetDeployment',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/deployments/{OpenApiUtilClient.get_encode_param(deployment_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.GetDeploymentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_deployment_with_options_async(
        self,
        namespace: str,
        deployment_id: str,
        headers: ververica_20220718_models.GetDeploymentHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.GetDeploymentResponse:
        """
        @summary get a deployment
        
        @param headers: GetDeploymentHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDeploymentResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='GetDeployment',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/deployments/{OpenApiUtilClient.get_encode_param(deployment_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.GetDeploymentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_deployment(
        self,
        namespace: str,
        deployment_id: str,
    ) -> ververica_20220718_models.GetDeploymentResponse:
        """
        @summary get a deployment
        
        @return: GetDeploymentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.GetDeploymentHeaders()
        return self.get_deployment_with_options(namespace, deployment_id, headers, runtime)

    async def get_deployment_async(
        self,
        namespace: str,
        deployment_id: str,
    ) -> ververica_20220718_models.GetDeploymentResponse:
        """
        @summary get a deployment
        
        @return: GetDeploymentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.GetDeploymentHeaders()
        return await self.get_deployment_with_options_async(namespace, deployment_id, headers, runtime)

    def get_generate_resource_plan_result_with_options(
        self,
        namespace: str,
        ticket_id: str,
        headers: ververica_20220718_models.GetGenerateResourcePlanResultHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.GetGenerateResourcePlanResultResponse:
        """
        @summary 获取生成ResourcePlan异步操作的结果。
        
        @param headers: GetGenerateResourcePlanResultHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetGenerateResourcePlanResultResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='GetGenerateResourcePlanResult',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/deployments/tickets/{OpenApiUtilClient.get_encode_param(ticket_id)}/resource-plan%3AasyncGenerate',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.GetGenerateResourcePlanResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_generate_resource_plan_result_with_options_async(
        self,
        namespace: str,
        ticket_id: str,
        headers: ververica_20220718_models.GetGenerateResourcePlanResultHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.GetGenerateResourcePlanResultResponse:
        """
        @summary 获取生成ResourcePlan异步操作的结果。
        
        @param headers: GetGenerateResourcePlanResultHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetGenerateResourcePlanResultResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='GetGenerateResourcePlanResult',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/deployments/tickets/{OpenApiUtilClient.get_encode_param(ticket_id)}/resource-plan%3AasyncGenerate',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.GetGenerateResourcePlanResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_generate_resource_plan_result(
        self,
        namespace: str,
        ticket_id: str,
    ) -> ververica_20220718_models.GetGenerateResourcePlanResultResponse:
        """
        @summary 获取生成ResourcePlan异步操作的结果。
        
        @return: GetGenerateResourcePlanResultResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.GetGenerateResourcePlanResultHeaders()
        return self.get_generate_resource_plan_result_with_options(namespace, ticket_id, headers, runtime)

    async def get_generate_resource_plan_result_async(
        self,
        namespace: str,
        ticket_id: str,
    ) -> ververica_20220718_models.GetGenerateResourcePlanResultResponse:
        """
        @summary 获取生成ResourcePlan异步操作的结果。
        
        @return: GetGenerateResourcePlanResultResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.GetGenerateResourcePlanResultHeaders()
        return await self.get_generate_resource_plan_result_with_options_async(namespace, ticket_id, headers, runtime)

    def get_job_with_options(
        self,
        namespace: str,
        job_id: str,
        headers: ververica_20220718_models.GetJobHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.GetJobResponse:
        """
        @summary get job
        
        @param headers: GetJobHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetJobResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='GetJob',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/jobs/{OpenApiUtilClient.get_encode_param(job_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.GetJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_job_with_options_async(
        self,
        namespace: str,
        job_id: str,
        headers: ververica_20220718_models.GetJobHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.GetJobResponse:
        """
        @summary get job
        
        @param headers: GetJobHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetJobResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='GetJob',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/jobs/{OpenApiUtilClient.get_encode_param(job_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.GetJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_job(
        self,
        namespace: str,
        job_id: str,
    ) -> ververica_20220718_models.GetJobResponse:
        """
        @summary get job
        
        @return: GetJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.GetJobHeaders()
        return self.get_job_with_options(namespace, job_id, headers, runtime)

    async def get_job_async(
        self,
        namespace: str,
        job_id: str,
    ) -> ververica_20220718_models.GetJobResponse:
        """
        @summary get job
        
        @return: GetJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.GetJobHeaders()
        return await self.get_job_with_options_async(namespace, job_id, headers, runtime)

    def get_member_with_options(
        self,
        namespace: str,
        member: str,
        headers: ververica_20220718_models.GetMemberHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.GetMemberResponse:
        """
        @summary 调用GetMember获取成员。
        
        @param headers: GetMemberHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMemberResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='GetMember',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/gateway/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/members/{OpenApiUtilClient.get_encode_param(member)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.GetMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_member_with_options_async(
        self,
        namespace: str,
        member: str,
        headers: ververica_20220718_models.GetMemberHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.GetMemberResponse:
        """
        @summary 调用GetMember获取成员。
        
        @param headers: GetMemberHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMemberResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='GetMember',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/gateway/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/members/{OpenApiUtilClient.get_encode_param(member)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.GetMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_member(
        self,
        namespace: str,
        member: str,
    ) -> ververica_20220718_models.GetMemberResponse:
        """
        @summary 调用GetMember获取成员。
        
        @return: GetMemberResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.GetMemberHeaders()
        return self.get_member_with_options(namespace, member, headers, runtime)

    async def get_member_async(
        self,
        namespace: str,
        member: str,
    ) -> ververica_20220718_models.GetMemberResponse:
        """
        @summary 调用GetMember获取成员。
        
        @return: GetMemberResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.GetMemberHeaders()
        return await self.get_member_with_options_async(namespace, member, headers, runtime)

    def get_savepoint_with_options(
        self,
        namespace: str,
        savepoint_id: str,
        headers: ververica_20220718_models.GetSavepointHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.GetSavepointResponse:
        """
        @summary 调用GetSavepoint获取savepoint信息。
        
        @param headers: GetSavepointHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSavepointResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='GetSavepoint',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/savepoints/{OpenApiUtilClient.get_encode_param(savepoint_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.GetSavepointResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_savepoint_with_options_async(
        self,
        namespace: str,
        savepoint_id: str,
        headers: ververica_20220718_models.GetSavepointHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.GetSavepointResponse:
        """
        @summary 调用GetSavepoint获取savepoint信息。
        
        @param headers: GetSavepointHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSavepointResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='GetSavepoint',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/savepoints/{OpenApiUtilClient.get_encode_param(savepoint_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.GetSavepointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_savepoint(
        self,
        namespace: str,
        savepoint_id: str,
    ) -> ververica_20220718_models.GetSavepointResponse:
        """
        @summary 调用GetSavepoint获取savepoint信息。
        
        @return: GetSavepointResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.GetSavepointHeaders()
        return self.get_savepoint_with_options(namespace, savepoint_id, headers, runtime)

    async def get_savepoint_async(
        self,
        namespace: str,
        savepoint_id: str,
    ) -> ververica_20220718_models.GetSavepointResponse:
        """
        @summary 调用GetSavepoint获取savepoint信息。
        
        @return: GetSavepointResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.GetSavepointHeaders()
        return await self.get_savepoint_with_options_async(namespace, savepoint_id, headers, runtime)

    def list_deployment_targets_with_options(
        self,
        namespace: str,
        request: ververica_20220718_models.ListDeploymentTargetsRequest,
        headers: ververica_20220718_models.ListDeploymentTargetsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.ListDeploymentTargetsResponse:
        """
        @summary list deployment targets
        
        @param request: ListDeploymentTargetsRequest
        @param headers: ListDeploymentTargetsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDeploymentTargetsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_index):
            query['pageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDeploymentTargets',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/deployment-targets',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.ListDeploymentTargetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_deployment_targets_with_options_async(
        self,
        namespace: str,
        request: ververica_20220718_models.ListDeploymentTargetsRequest,
        headers: ververica_20220718_models.ListDeploymentTargetsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.ListDeploymentTargetsResponse:
        """
        @summary list deployment targets
        
        @param request: ListDeploymentTargetsRequest
        @param headers: ListDeploymentTargetsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDeploymentTargetsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_index):
            query['pageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDeploymentTargets',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/deployment-targets',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.ListDeploymentTargetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_deployment_targets(
        self,
        namespace: str,
        request: ververica_20220718_models.ListDeploymentTargetsRequest,
    ) -> ververica_20220718_models.ListDeploymentTargetsResponse:
        """
        @summary list deployment targets
        
        @param request: ListDeploymentTargetsRequest
        @return: ListDeploymentTargetsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.ListDeploymentTargetsHeaders()
        return self.list_deployment_targets_with_options(namespace, request, headers, runtime)

    async def list_deployment_targets_async(
        self,
        namespace: str,
        request: ververica_20220718_models.ListDeploymentTargetsRequest,
    ) -> ververica_20220718_models.ListDeploymentTargetsResponse:
        """
        @summary list deployment targets
        
        @param request: ListDeploymentTargetsRequest
        @return: ListDeploymentTargetsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.ListDeploymentTargetsHeaders()
        return await self.list_deployment_targets_with_options_async(namespace, request, headers, runtime)

    def list_deployments_with_options(
        self,
        namespace: str,
        request: ververica_20220718_models.ListDeploymentsRequest,
        headers: ververica_20220718_models.ListDeploymentsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.ListDeploymentsResponse:
        """
        @summary list deployments
        
        @param request: ListDeploymentsRequest
        @param headers: ListDeploymentsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDeploymentsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.creator):
            query['creator'] = request.creator
        if not UtilClient.is_unset(request.execution_mode):
            query['executionMode'] = request.execution_mode
        if not UtilClient.is_unset(request.label_key):
            query['labelKey'] = request.label_key
        if not UtilClient.is_unset(request.label_value_array):
            query['labelValueArray'] = request.label_value_array
        if not UtilClient.is_unset(request.modifier):
            query['modifier'] = request.modifier
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.page_index):
            query['pageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDeployments',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/deployments',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.ListDeploymentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_deployments_with_options_async(
        self,
        namespace: str,
        request: ververica_20220718_models.ListDeploymentsRequest,
        headers: ververica_20220718_models.ListDeploymentsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.ListDeploymentsResponse:
        """
        @summary list deployments
        
        @param request: ListDeploymentsRequest
        @param headers: ListDeploymentsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDeploymentsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.creator):
            query['creator'] = request.creator
        if not UtilClient.is_unset(request.execution_mode):
            query['executionMode'] = request.execution_mode
        if not UtilClient.is_unset(request.label_key):
            query['labelKey'] = request.label_key
        if not UtilClient.is_unset(request.label_value_array):
            query['labelValueArray'] = request.label_value_array
        if not UtilClient.is_unset(request.modifier):
            query['modifier'] = request.modifier
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.page_index):
            query['pageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDeployments',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/deployments',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.ListDeploymentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_deployments(
        self,
        namespace: str,
        request: ververica_20220718_models.ListDeploymentsRequest,
    ) -> ververica_20220718_models.ListDeploymentsResponse:
        """
        @summary list deployments
        
        @param request: ListDeploymentsRequest
        @return: ListDeploymentsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.ListDeploymentsHeaders()
        return self.list_deployments_with_options(namespace, request, headers, runtime)

    async def list_deployments_async(
        self,
        namespace: str,
        request: ververica_20220718_models.ListDeploymentsRequest,
    ) -> ververica_20220718_models.ListDeploymentsResponse:
        """
        @summary list deployments
        
        @param request: ListDeploymentsRequest
        @return: ListDeploymentsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.ListDeploymentsHeaders()
        return await self.list_deployments_with_options_async(namespace, request, headers, runtime)

    def list_editable_namespace_with_options(
        self,
        request: ververica_20220718_models.ListEditableNamespaceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.ListEditableNamespaceResponse:
        """
        @summary 列出有编辑权限的项目空间。
        
        @param request: ListEditableNamespaceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEditableNamespaceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace):
            query['namespace'] = request.namespace
        if not UtilClient.is_unset(request.page_index):
            query['pageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEditableNamespace',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/gateway/v2/namespaces/editable',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.ListEditableNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_editable_namespace_with_options_async(
        self,
        request: ververica_20220718_models.ListEditableNamespaceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.ListEditableNamespaceResponse:
        """
        @summary 列出有编辑权限的项目空间。
        
        @param request: ListEditableNamespaceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEditableNamespaceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace):
            query['namespace'] = request.namespace
        if not UtilClient.is_unset(request.page_index):
            query['pageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEditableNamespace',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/gateway/v2/namespaces/editable',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.ListEditableNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_editable_namespace(
        self,
        request: ververica_20220718_models.ListEditableNamespaceRequest,
    ) -> ververica_20220718_models.ListEditableNamespaceResponse:
        """
        @summary 列出有编辑权限的项目空间。
        
        @param request: ListEditableNamespaceRequest
        @return: ListEditableNamespaceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_editable_namespace_with_options(request, headers, runtime)

    async def list_editable_namespace_async(
        self,
        request: ververica_20220718_models.ListEditableNamespaceRequest,
    ) -> ververica_20220718_models.ListEditableNamespaceResponse:
        """
        @summary 列出有编辑权限的项目空间。
        
        @param request: ListEditableNamespaceRequest
        @return: ListEditableNamespaceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_editable_namespace_with_options_async(request, headers, runtime)

    def list_engine_version_metadata_with_options(
        self,
        headers: ververica_20220718_models.ListEngineVersionMetadataHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.ListEngineVersionMetadataResponse:
        """
        @summary 获取系统支持的引擎版本信息。
        
        @param headers: ListEngineVersionMetadataHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEngineVersionMetadataResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='ListEngineVersionMetadata',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/engine-version-meta.json',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.ListEngineVersionMetadataResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_engine_version_metadata_with_options_async(
        self,
        headers: ververica_20220718_models.ListEngineVersionMetadataHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.ListEngineVersionMetadataResponse:
        """
        @summary 获取系统支持的引擎版本信息。
        
        @param headers: ListEngineVersionMetadataHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEngineVersionMetadataResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='ListEngineVersionMetadata',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/engine-version-meta.json',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.ListEngineVersionMetadataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_engine_version_metadata(self) -> ververica_20220718_models.ListEngineVersionMetadataResponse:
        """
        @summary 获取系统支持的引擎版本信息。
        
        @return: ListEngineVersionMetadataResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.ListEngineVersionMetadataHeaders()
        return self.list_engine_version_metadata_with_options(headers, runtime)

    async def list_engine_version_metadata_async(self) -> ververica_20220718_models.ListEngineVersionMetadataResponse:
        """
        @summary 获取系统支持的引擎版本信息。
        
        @return: ListEngineVersionMetadataResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.ListEngineVersionMetadataHeaders()
        return await self.list_engine_version_metadata_with_options_async(headers, runtime)

    def list_jobs_with_options(
        self,
        namespace: str,
        request: ververica_20220718_models.ListJobsRequest,
        headers: ververica_20220718_models.ListJobsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.ListJobsResponse:
        """
        @summary list jobs
        
        @param request: ListJobsRequest
        @param headers: ListJobsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deployment_id):
            query['deploymentId'] = request.deployment_id
        if not UtilClient.is_unset(request.page_index):
            query['pageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_name):
            query['sortName'] = request.sort_name
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobs',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/jobs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.ListJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_jobs_with_options_async(
        self,
        namespace: str,
        request: ververica_20220718_models.ListJobsRequest,
        headers: ververica_20220718_models.ListJobsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.ListJobsResponse:
        """
        @summary list jobs
        
        @param request: ListJobsRequest
        @param headers: ListJobsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deployment_id):
            query['deploymentId'] = request.deployment_id
        if not UtilClient.is_unset(request.page_index):
            query['pageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_name):
            query['sortName'] = request.sort_name
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobs',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/jobs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.ListJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_jobs(
        self,
        namespace: str,
        request: ververica_20220718_models.ListJobsRequest,
    ) -> ververica_20220718_models.ListJobsResponse:
        """
        @summary list jobs
        
        @param request: ListJobsRequest
        @return: ListJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.ListJobsHeaders()
        return self.list_jobs_with_options(namespace, request, headers, runtime)

    async def list_jobs_async(
        self,
        namespace: str,
        request: ververica_20220718_models.ListJobsRequest,
    ) -> ververica_20220718_models.ListJobsResponse:
        """
        @summary list jobs
        
        @param request: ListJobsRequest
        @return: ListJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.ListJobsHeaders()
        return await self.list_jobs_with_options_async(namespace, request, headers, runtime)

    def list_members_with_options(
        self,
        namespace: str,
        request: ververica_20220718_models.ListMembersRequest,
        headers: ververica_20220718_models.ListMembersHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.ListMembersResponse:
        """
        @summary 调用ListMembers接口获取成员列表。
        
        @param request: ListMembersRequest
        @param headers: ListMembersHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMembersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_index):
            query['pageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMembers',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/gateway/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/members',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.ListMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_members_with_options_async(
        self,
        namespace: str,
        request: ververica_20220718_models.ListMembersRequest,
        headers: ververica_20220718_models.ListMembersHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.ListMembersResponse:
        """
        @summary 调用ListMembers接口获取成员列表。
        
        @param request: ListMembersRequest
        @param headers: ListMembersHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMembersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_index):
            query['pageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMembers',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/gateway/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/members',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.ListMembersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_members(
        self,
        namespace: str,
        request: ververica_20220718_models.ListMembersRequest,
    ) -> ververica_20220718_models.ListMembersResponse:
        """
        @summary 调用ListMembers接口获取成员列表。
        
        @param request: ListMembersRequest
        @return: ListMembersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.ListMembersHeaders()
        return self.list_members_with_options(namespace, request, headers, runtime)

    async def list_members_async(
        self,
        namespace: str,
        request: ververica_20220718_models.ListMembersRequest,
    ) -> ververica_20220718_models.ListMembersResponse:
        """
        @summary 调用ListMembers接口获取成员列表。
        
        @param request: ListMembersRequest
        @return: ListMembersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.ListMembersHeaders()
        return await self.list_members_with_options_async(namespace, request, headers, runtime)

    def list_savepoints_with_options(
        self,
        namespace: str,
        request: ververica_20220718_models.ListSavepointsRequest,
        headers: ververica_20220718_models.ListSavepointsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.ListSavepointsResponse:
        """
        @summary 调用ListSavepoints获取满足查询条件的savepoint列表。
        
        @param request: ListSavepointsRequest
        @param headers: ListSavepointsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSavepointsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deployment_id):
            query['deploymentId'] = request.deployment_id
        if not UtilClient.is_unset(request.job_id):
            query['jobId'] = request.job_id
        if not UtilClient.is_unset(request.page_index):
            query['pageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSavepoints',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/savepoints',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.ListSavepointsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_savepoints_with_options_async(
        self,
        namespace: str,
        request: ververica_20220718_models.ListSavepointsRequest,
        headers: ververica_20220718_models.ListSavepointsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.ListSavepointsResponse:
        """
        @summary 调用ListSavepoints获取满足查询条件的savepoint列表。
        
        @param request: ListSavepointsRequest
        @param headers: ListSavepointsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSavepointsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deployment_id):
            query['deploymentId'] = request.deployment_id
        if not UtilClient.is_unset(request.job_id):
            query['jobId'] = request.job_id
        if not UtilClient.is_unset(request.page_index):
            query['pageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSavepoints',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/savepoints',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.ListSavepointsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_savepoints(
        self,
        namespace: str,
        request: ververica_20220718_models.ListSavepointsRequest,
    ) -> ververica_20220718_models.ListSavepointsResponse:
        """
        @summary 调用ListSavepoints获取满足查询条件的savepoint列表。
        
        @param request: ListSavepointsRequest
        @return: ListSavepointsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.ListSavepointsHeaders()
        return self.list_savepoints_with_options(namespace, request, headers, runtime)

    async def list_savepoints_async(
        self,
        namespace: str,
        request: ververica_20220718_models.ListSavepointsRequest,
    ) -> ververica_20220718_models.ListSavepointsResponse:
        """
        @summary 调用ListSavepoints获取满足查询条件的savepoint列表。
        
        @param request: ListSavepointsRequest
        @return: ListSavepointsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.ListSavepointsHeaders()
        return await self.list_savepoints_with_options_async(namespace, request, headers, runtime)

    def list_variables_with_options(
        self,
        namespace: str,
        request: ververica_20220718_models.ListVariablesRequest,
        headers: ververica_20220718_models.ListVariablesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.ListVariablesResponse:
        """
        @summary list variables
        
        @param request: ListVariablesRequest
        @param headers: ListVariablesHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListVariablesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_index):
            query['pageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVariables',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/variables',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.ListVariablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_variables_with_options_async(
        self,
        namespace: str,
        request: ververica_20220718_models.ListVariablesRequest,
        headers: ververica_20220718_models.ListVariablesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.ListVariablesResponse:
        """
        @summary list variables
        
        @param request: ListVariablesRequest
        @param headers: ListVariablesHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListVariablesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_index):
            query['pageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVariables',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/variables',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.ListVariablesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_variables(
        self,
        namespace: str,
        request: ververica_20220718_models.ListVariablesRequest,
    ) -> ververica_20220718_models.ListVariablesResponse:
        """
        @summary list variables
        
        @param request: ListVariablesRequest
        @return: ListVariablesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.ListVariablesHeaders()
        return self.list_variables_with_options(namespace, request, headers, runtime)

    async def list_variables_async(
        self,
        namespace: str,
        request: ververica_20220718_models.ListVariablesRequest,
    ) -> ververica_20220718_models.ListVariablesResponse:
        """
        @summary list variables
        
        @param request: ListVariablesRequest
        @return: ListVariablesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.ListVariablesHeaders()
        return await self.list_variables_with_options_async(namespace, request, headers, runtime)

    def start_job_with_options(
        self,
        namespace: str,
        request: ververica_20220718_models.StartJobRequest,
        headers: ververica_20220718_models.StartJobHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.StartJobResponse:
        """
        @deprecated OpenAPI StartJob is deprecated
        
        @summary start job
        
        @param request: StartJobRequest
        @param headers: StartJobHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartJobResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='StartJob',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/jobs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.StartJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_job_with_options_async(
        self,
        namespace: str,
        request: ververica_20220718_models.StartJobRequest,
        headers: ververica_20220718_models.StartJobHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.StartJobResponse:
        """
        @deprecated OpenAPI StartJob is deprecated
        
        @summary start job
        
        @param request: StartJobRequest
        @param headers: StartJobHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartJobResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='StartJob',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/jobs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.StartJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_job(
        self,
        namespace: str,
        request: ververica_20220718_models.StartJobRequest,
    ) -> ververica_20220718_models.StartJobResponse:
        """
        @deprecated OpenAPI StartJob is deprecated
        
        @summary start job
        
        @param request: StartJobRequest
        @return: StartJobResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.StartJobHeaders()
        return self.start_job_with_options(namespace, request, headers, runtime)

    async def start_job_async(
        self,
        namespace: str,
        request: ververica_20220718_models.StartJobRequest,
    ) -> ververica_20220718_models.StartJobResponse:
        """
        @deprecated OpenAPI StartJob is deprecated
        
        @summary start job
        
        @param request: StartJobRequest
        @return: StartJobResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.StartJobHeaders()
        return await self.start_job_with_options_async(namespace, request, headers, runtime)

    def start_job_with_params_with_options(
        self,
        namespace: str,
        request: ververica_20220718_models.StartJobWithParamsRequest,
        headers: ververica_20220718_models.StartJobWithParamsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.StartJobWithParamsResponse:
        """
        @summary 启动作业实例。
        
        @param request: StartJobWithParamsRequest
        @param headers: StartJobWithParamsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartJobWithParamsResponse
        """
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='StartJobWithParams',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/jobs%3Astart',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.StartJobWithParamsResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_job_with_params_with_options_async(
        self,
        namespace: str,
        request: ververica_20220718_models.StartJobWithParamsRequest,
        headers: ververica_20220718_models.StartJobWithParamsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.StartJobWithParamsResponse:
        """
        @summary 启动作业实例。
        
        @param request: StartJobWithParamsRequest
        @param headers: StartJobWithParamsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartJobWithParamsResponse
        """
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='StartJobWithParams',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/jobs%3Astart',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.StartJobWithParamsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_job_with_params(
        self,
        namespace: str,
        request: ververica_20220718_models.StartJobWithParamsRequest,
    ) -> ververica_20220718_models.StartJobWithParamsResponse:
        """
        @summary 启动作业实例。
        
        @param request: StartJobWithParamsRequest
        @return: StartJobWithParamsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.StartJobWithParamsHeaders()
        return self.start_job_with_params_with_options(namespace, request, headers, runtime)

    async def start_job_with_params_async(
        self,
        namespace: str,
        request: ververica_20220718_models.StartJobWithParamsRequest,
    ) -> ververica_20220718_models.StartJobWithParamsResponse:
        """
        @summary 启动作业实例。
        
        @param request: StartJobWithParamsRequest
        @return: StartJobWithParamsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.StartJobWithParamsHeaders()
        return await self.start_job_with_params_with_options_async(namespace, request, headers, runtime)

    def stop_job_with_options(
        self,
        namespace: str,
        job_id: str,
        request: ververica_20220718_models.StopJobRequest,
        headers: ververica_20220718_models.StopJobHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.StopJobResponse:
        """
        @summary 调用StopJob停止实例。
        
        @param request: StopJobRequest
        @param headers: StopJobHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopJobResponse
        """
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='StopJob',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/jobs/{OpenApiUtilClient.get_encode_param(job_id)}%3Astop',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.StopJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_job_with_options_async(
        self,
        namespace: str,
        job_id: str,
        request: ververica_20220718_models.StopJobRequest,
        headers: ververica_20220718_models.StopJobHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.StopJobResponse:
        """
        @summary 调用StopJob停止实例。
        
        @param request: StopJobRequest
        @param headers: StopJobHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopJobResponse
        """
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='StopJob',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/jobs/{OpenApiUtilClient.get_encode_param(job_id)}%3Astop',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.StopJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_job(
        self,
        namespace: str,
        job_id: str,
        request: ververica_20220718_models.StopJobRequest,
    ) -> ververica_20220718_models.StopJobResponse:
        """
        @summary 调用StopJob停止实例。
        
        @param request: StopJobRequest
        @return: StopJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.StopJobHeaders()
        return self.stop_job_with_options(namespace, job_id, request, headers, runtime)

    async def stop_job_async(
        self,
        namespace: str,
        job_id: str,
        request: ververica_20220718_models.StopJobRequest,
    ) -> ververica_20220718_models.StopJobResponse:
        """
        @summary 调用StopJob停止实例。
        
        @param request: StopJobRequest
        @return: StopJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.StopJobHeaders()
        return await self.stop_job_with_options_async(namespace, job_id, request, headers, runtime)

    def update_deployment_with_options(
        self,
        namespace: str,
        deployment_id: str,
        request: ververica_20220718_models.UpdateDeploymentRequest,
        headers: ververica_20220718_models.UpdateDeploymentHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.UpdateDeploymentResponse:
        """
        @summary update a deployment using patch
        
        @param request: UpdateDeploymentRequest
        @param headers: UpdateDeploymentHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDeploymentResponse
        """
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateDeployment',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/deployments/{OpenApiUtilClient.get_encode_param(deployment_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.UpdateDeploymentResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_deployment_with_options_async(
        self,
        namespace: str,
        deployment_id: str,
        request: ververica_20220718_models.UpdateDeploymentRequest,
        headers: ververica_20220718_models.UpdateDeploymentHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.UpdateDeploymentResponse:
        """
        @summary update a deployment using patch
        
        @param request: UpdateDeploymentRequest
        @param headers: UpdateDeploymentHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDeploymentResponse
        """
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateDeployment',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/deployments/{OpenApiUtilClient.get_encode_param(deployment_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.UpdateDeploymentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_deployment(
        self,
        namespace: str,
        deployment_id: str,
        request: ververica_20220718_models.UpdateDeploymentRequest,
    ) -> ververica_20220718_models.UpdateDeploymentResponse:
        """
        @summary update a deployment using patch
        
        @param request: UpdateDeploymentRequest
        @return: UpdateDeploymentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.UpdateDeploymentHeaders()
        return self.update_deployment_with_options(namespace, deployment_id, request, headers, runtime)

    async def update_deployment_async(
        self,
        namespace: str,
        deployment_id: str,
        request: ververica_20220718_models.UpdateDeploymentRequest,
    ) -> ververica_20220718_models.UpdateDeploymentResponse:
        """
        @summary update a deployment using patch
        
        @param request: UpdateDeploymentRequest
        @return: UpdateDeploymentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.UpdateDeploymentHeaders()
        return await self.update_deployment_with_options_async(namespace, deployment_id, request, headers, runtime)

    def update_member_with_options(
        self,
        namespace: str,
        request: ververica_20220718_models.UpdateMemberRequest,
        headers: ververica_20220718_models.UpdateMemberHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.UpdateMemberResponse:
        """
        @summary 调用UpdateMember更新成员。
        
        @param request: UpdateMemberRequest
        @param headers: UpdateMemberHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateMemberResponse
        """
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateMember',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/gateway/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/members',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.UpdateMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_member_with_options_async(
        self,
        namespace: str,
        request: ververica_20220718_models.UpdateMemberRequest,
        headers: ververica_20220718_models.UpdateMemberHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.UpdateMemberResponse:
        """
        @summary 调用UpdateMember更新成员。
        
        @param request: UpdateMemberRequest
        @param headers: UpdateMemberHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateMemberResponse
        """
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateMember',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/gateway/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/members',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.UpdateMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_member(
        self,
        namespace: str,
        request: ververica_20220718_models.UpdateMemberRequest,
    ) -> ververica_20220718_models.UpdateMemberResponse:
        """
        @summary 调用UpdateMember更新成员。
        
        @param request: UpdateMemberRequest
        @return: UpdateMemberResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.UpdateMemberHeaders()
        return self.update_member_with_options(namespace, request, headers, runtime)

    async def update_member_async(
        self,
        namespace: str,
        request: ververica_20220718_models.UpdateMemberRequest,
    ) -> ververica_20220718_models.UpdateMemberResponse:
        """
        @summary 调用UpdateMember更新成员。
        
        @param request: UpdateMemberRequest
        @return: UpdateMemberResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.UpdateMemberHeaders()
        return await self.update_member_with_options_async(namespace, request, headers, runtime)
