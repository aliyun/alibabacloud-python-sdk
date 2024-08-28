# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_eas20210701 import models as eas_20210701_models
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
            'cn-beijing': 'pai-eas.cn-beijing.aliyuncs.com',
            'cn-zhangjiakou': 'pai-eas.cn-zhangjiakou.aliyuncs.com',
            'cn-hangzhou': 'pai-eas.cn-hangzhou.aliyuncs.com',
            'cn-shanghai': 'pai-eas.cn-shanghai.aliyuncs.com',
            'cn-shenzhen': 'pai-eas.cn-shenzhen.aliyuncs.com',
            'cn-hongkong': 'pai-eas.cn-hongkong.aliyuncs.com',
            'ap-southeast-1': 'pai-eas.ap-southeast-1.aliyuncs.com',
            'ap-southeast-5': 'pai-eas.ap-southeast-5.aliyuncs.com',
            'us-east-1': 'pai-eas.us-east-1.aliyuncs.com',
            'us-west-1': 'pai-eas.us-west-1.aliyuncs.com',
            'eu-central-1': 'pai-eas.eu-central-1.aliyuncs.com',
            'ap-south-1': 'pai-eas.ap-south-1.aliyuncs.com',
            'cn-shanghai-finance-1': 'pai-eas.cn-shanghai-finance-1.aliyuncs.com',
            'cn-north-2-gov-1': 'pai-eas.cn-north-2-gov-1.aliyuncs.com',
            'cn-chengdu': 'pai-eas.cn-chengdu.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('eas', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def clone_service_with_options(
        self,
        cluster_id: str,
        service_name: str,
        tmp_req: eas_20210701_models.CloneServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.CloneServiceResponse:
        """
        @summary Clones a service.
        
        @param tmp_req: CloneServiceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CloneServiceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eas_20210701_models.CloneServiceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.labels):
            request.labels_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.labels, 'Labels', 'json')
        query = {}
        if not UtilClient.is_unset(request.labels_shrink):
            query['Labels'] = request.labels_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='CloneService',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/clone',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.CloneServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def clone_service_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        tmp_req: eas_20210701_models.CloneServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.CloneServiceResponse:
        """
        @summary Clones a service.
        
        @param tmp_req: CloneServiceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CloneServiceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eas_20210701_models.CloneServiceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.labels):
            request.labels_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.labels, 'Labels', 'json')
        query = {}
        if not UtilClient.is_unset(request.labels_shrink):
            query['Labels'] = request.labels_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='CloneService',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/clone',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.CloneServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def clone_service(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.CloneServiceRequest,
    ) -> eas_20210701_models.CloneServiceResponse:
        """
        @summary Clones a service.
        
        @param request: CloneServiceRequest
        @return: CloneServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.clone_service_with_options(cluster_id, service_name, request, headers, runtime)

    async def clone_service_async(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.CloneServiceRequest,
    ) -> eas_20210701_models.CloneServiceResponse:
        """
        @summary Clones a service.
        
        @param request: CloneServiceRequest
        @return: CloneServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.clone_service_with_options_async(cluster_id, service_name, request, headers, runtime)

    def commit_service_with_options(
        self,
        cluster_id: str,
        service_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.CommitServiceResponse:
        """
        @summary Commits the Worker0 container in the custom container service and deploys the container as a new image.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CommitServiceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CommitService',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/commit',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.CommitServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def commit_service_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.CommitServiceResponse:
        """
        @summary Commits the Worker0 container in the custom container service and deploys the container as a new image.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CommitServiceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CommitService',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/commit',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.CommitServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def commit_service(
        self,
        cluster_id: str,
        service_name: str,
    ) -> eas_20210701_models.CommitServiceResponse:
        """
        @summary Commits the Worker0 container in the custom container service and deploys the container as a new image.
        
        @return: CommitServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.commit_service_with_options(cluster_id, service_name, headers, runtime)

    async def commit_service_async(
        self,
        cluster_id: str,
        service_name: str,
    ) -> eas_20210701_models.CommitServiceResponse:
        """
        @summary Commits the Worker0 container in the custom container service and deploys the container as a new image.
        
        @return: CommitServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.commit_service_with_options_async(cluster_id, service_name, headers, runtime)

    def create_acl_policy_with_options(
        self,
        cluster_id: str,
        gateway_id: str,
        tmp_req: eas_20210701_models.CreateAclPolicyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.CreateAclPolicyResponse:
        """
        @summary 创建网关访问权限ACL Policy
        
        @param tmp_req: CreateAclPolicyRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAclPolicyResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eas_20210701_models.CreateAclPolicyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.acl_policy_list):
            request.acl_policy_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.acl_policy_list, 'AclPolicyList', 'json')
        query = {}
        if not UtilClient.is_unset(request.acl_policy_list_shrink):
            query['AclPolicyList'] = request.acl_policy_list_shrink
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAclPolicy',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/gateways/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(gateway_id)}/acl_policy',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.CreateAclPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_acl_policy_with_options_async(
        self,
        cluster_id: str,
        gateway_id: str,
        tmp_req: eas_20210701_models.CreateAclPolicyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.CreateAclPolicyResponse:
        """
        @summary 创建网关访问权限ACL Policy
        
        @param tmp_req: CreateAclPolicyRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAclPolicyResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eas_20210701_models.CreateAclPolicyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.acl_policy_list):
            request.acl_policy_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.acl_policy_list, 'AclPolicyList', 'json')
        query = {}
        if not UtilClient.is_unset(request.acl_policy_list_shrink):
            query['AclPolicyList'] = request.acl_policy_list_shrink
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAclPolicy',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/gateways/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(gateway_id)}/acl_policy',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.CreateAclPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_acl_policy(
        self,
        cluster_id: str,
        gateway_id: str,
        request: eas_20210701_models.CreateAclPolicyRequest,
    ) -> eas_20210701_models.CreateAclPolicyResponse:
        """
        @summary 创建网关访问权限ACL Policy
        
        @param request: CreateAclPolicyRequest
        @return: CreateAclPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_acl_policy_with_options(cluster_id, gateway_id, request, headers, runtime)

    async def create_acl_policy_async(
        self,
        cluster_id: str,
        gateway_id: str,
        request: eas_20210701_models.CreateAclPolicyRequest,
    ) -> eas_20210701_models.CreateAclPolicyResponse:
        """
        @summary 创建网关访问权限ACL Policy
        
        @param request: CreateAclPolicyRequest
        @return: CreateAclPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_acl_policy_with_options_async(cluster_id, gateway_id, request, headers, runtime)

    def create_app_service_with_options(
        self,
        request: eas_20210701_models.CreateAppServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.CreateAppServiceResponse:
        """
        @summary Creates an application service.
        
        @param request: CreateAppServiceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAppServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.quota_id):
            query['QuotaId'] = request.quota_id
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.app_type):
            body['AppType'] = request.app_type
        if not UtilClient.is_unset(request.app_version):
            body['AppVersion'] = request.app_version
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        if not UtilClient.is_unset(request.replicas):
            body['Replicas'] = request.replicas
        if not UtilClient.is_unset(request.service_name):
            body['ServiceName'] = request.service_name
        if not UtilClient.is_unset(request.service_spec):
            body['ServiceSpec'] = request.service_spec
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAppService',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/app_services',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.CreateAppServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_app_service_with_options_async(
        self,
        request: eas_20210701_models.CreateAppServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.CreateAppServiceResponse:
        """
        @summary Creates an application service.
        
        @param request: CreateAppServiceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAppServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.quota_id):
            query['QuotaId'] = request.quota_id
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.app_type):
            body['AppType'] = request.app_type
        if not UtilClient.is_unset(request.app_version):
            body['AppVersion'] = request.app_version
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        if not UtilClient.is_unset(request.replicas):
            body['Replicas'] = request.replicas
        if not UtilClient.is_unset(request.service_name):
            body['ServiceName'] = request.service_name
        if not UtilClient.is_unset(request.service_spec):
            body['ServiceSpec'] = request.service_spec
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAppService',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/app_services',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.CreateAppServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_app_service(
        self,
        request: eas_20210701_models.CreateAppServiceRequest,
    ) -> eas_20210701_models.CreateAppServiceResponse:
        """
        @summary Creates an application service.
        
        @param request: CreateAppServiceRequest
        @return: CreateAppServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_app_service_with_options(request, headers, runtime)

    async def create_app_service_async(
        self,
        request: eas_20210701_models.CreateAppServiceRequest,
    ) -> eas_20210701_models.CreateAppServiceResponse:
        """
        @summary Creates an application service.
        
        @param request: CreateAppServiceRequest
        @return: CreateAppServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_app_service_with_options_async(request, headers, runtime)

    def create_benchmark_task_with_options(
        self,
        request: eas_20210701_models.CreateBenchmarkTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.CreateBenchmarkTaskResponse:
        """
        @summary Creates a stress testing task.
        
        @param request: CreateBenchmarkTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateBenchmarkTaskResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='CreateBenchmarkTask',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/benchmark-tasks',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.CreateBenchmarkTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_benchmark_task_with_options_async(
        self,
        request: eas_20210701_models.CreateBenchmarkTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.CreateBenchmarkTaskResponse:
        """
        @summary Creates a stress testing task.
        
        @param request: CreateBenchmarkTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateBenchmarkTaskResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='CreateBenchmarkTask',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/benchmark-tasks',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.CreateBenchmarkTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_benchmark_task(
        self,
        request: eas_20210701_models.CreateBenchmarkTaskRequest,
    ) -> eas_20210701_models.CreateBenchmarkTaskResponse:
        """
        @summary Creates a stress testing task.
        
        @param request: CreateBenchmarkTaskRequest
        @return: CreateBenchmarkTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_benchmark_task_with_options(request, headers, runtime)

    async def create_benchmark_task_async(
        self,
        request: eas_20210701_models.CreateBenchmarkTaskRequest,
    ) -> eas_20210701_models.CreateBenchmarkTaskResponse:
        """
        @summary Creates a stress testing task.
        
        @param request: CreateBenchmarkTaskRequest
        @return: CreateBenchmarkTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_benchmark_task_with_options_async(request, headers, runtime)

    def create_gateway_with_options(
        self,
        request: eas_20210701_models.CreateGatewayRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.CreateGatewayResponse:
        """
        @summary Creates a private gateway. You can create a private gateway only in a self-managed resource group.
        
        @param request: CreateGatewayRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateGatewayResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_name):
            query['ResourceName'] = request.resource_name
        body = {}
        if not UtilClient.is_unset(request.enable_internet):
            body['EnableInternet'] = request.enable_internet
        if not UtilClient.is_unset(request.enable_intranet):
            body['EnableIntranet'] = request.enable_intranet
        if not UtilClient.is_unset(request.instance_type):
            body['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.replicas):
            body['Replicas'] = request.replicas
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateGateway',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/gateways',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.CreateGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_gateway_with_options_async(
        self,
        request: eas_20210701_models.CreateGatewayRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.CreateGatewayResponse:
        """
        @summary Creates a private gateway. You can create a private gateway only in a self-managed resource group.
        
        @param request: CreateGatewayRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateGatewayResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_name):
            query['ResourceName'] = request.resource_name
        body = {}
        if not UtilClient.is_unset(request.enable_internet):
            body['EnableInternet'] = request.enable_internet
        if not UtilClient.is_unset(request.enable_intranet):
            body['EnableIntranet'] = request.enable_intranet
        if not UtilClient.is_unset(request.instance_type):
            body['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.replicas):
            body['Replicas'] = request.replicas
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateGateway',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/gateways',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.CreateGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_gateway(
        self,
        request: eas_20210701_models.CreateGatewayRequest,
    ) -> eas_20210701_models.CreateGatewayResponse:
        """
        @summary Creates a private gateway. You can create a private gateway only in a self-managed resource group.
        
        @param request: CreateGatewayRequest
        @return: CreateGatewayResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_gateway_with_options(request, headers, runtime)

    async def create_gateway_async(
        self,
        request: eas_20210701_models.CreateGatewayRequest,
    ) -> eas_20210701_models.CreateGatewayResponse:
        """
        @summary Creates a private gateway. You can create a private gateway only in a self-managed resource group.
        
        @param request: CreateGatewayRequest
        @return: CreateGatewayResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_gateway_with_options_async(request, headers, runtime)

    def create_gateway_intranet_linked_vpc_with_options(
        self,
        cluster_id: str,
        gateway_id: str,
        request: eas_20210701_models.CreateGatewayIntranetLinkedVpcRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.CreateGatewayIntranetLinkedVpcResponse:
        """
        @summary Creates an internal endpoint of a private gateway.
        
        @param request: CreateGatewayIntranetLinkedVpcRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateGatewayIntranetLinkedVpcResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGatewayIntranetLinkedVpc',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/gateways/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(gateway_id)}/intranet_endpoint_linked_vpc',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.CreateGatewayIntranetLinkedVpcResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_gateway_intranet_linked_vpc_with_options_async(
        self,
        cluster_id: str,
        gateway_id: str,
        request: eas_20210701_models.CreateGatewayIntranetLinkedVpcRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.CreateGatewayIntranetLinkedVpcResponse:
        """
        @summary Creates an internal endpoint of a private gateway.
        
        @param request: CreateGatewayIntranetLinkedVpcRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateGatewayIntranetLinkedVpcResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGatewayIntranetLinkedVpc',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/gateways/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(gateway_id)}/intranet_endpoint_linked_vpc',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.CreateGatewayIntranetLinkedVpcResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_gateway_intranet_linked_vpc(
        self,
        cluster_id: str,
        gateway_id: str,
        request: eas_20210701_models.CreateGatewayIntranetLinkedVpcRequest,
    ) -> eas_20210701_models.CreateGatewayIntranetLinkedVpcResponse:
        """
        @summary Creates an internal endpoint of a private gateway.
        
        @param request: CreateGatewayIntranetLinkedVpcRequest
        @return: CreateGatewayIntranetLinkedVpcResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_gateway_intranet_linked_vpc_with_options(cluster_id, gateway_id, request, headers, runtime)

    async def create_gateway_intranet_linked_vpc_async(
        self,
        cluster_id: str,
        gateway_id: str,
        request: eas_20210701_models.CreateGatewayIntranetLinkedVpcRequest,
    ) -> eas_20210701_models.CreateGatewayIntranetLinkedVpcResponse:
        """
        @summary Creates an internal endpoint of a private gateway.
        
        @param request: CreateGatewayIntranetLinkedVpcRequest
        @return: CreateGatewayIntranetLinkedVpcResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_gateway_intranet_linked_vpc_with_options_async(cluster_id, gateway_id, request, headers, runtime)

    def create_resource_with_options(
        self,
        request: eas_20210701_models.CreateResourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.CreateResourceResponse:
        """
        @summary Creates a resource group.
        
        @description *Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/144261.html) of Elastic Algorithm Service (EAS).
        
        @param request: CreateResourceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateResourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_renewal):
            body['AutoRenewal'] = request.auto_renewal
        if not UtilClient.is_unset(request.charge_type):
            body['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.ecs_instance_count):
            body['EcsInstanceCount'] = request.ecs_instance_count
        if not UtilClient.is_unset(request.ecs_instance_type):
            body['EcsInstanceType'] = request.ecs_instance_type
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.self_managed_resource_options):
            body['SelfManagedResourceOptions'] = request.self_managed_resource_options
        if not UtilClient.is_unset(request.system_disk_size):
            body['SystemDiskSize'] = request.system_disk_size
        if not UtilClient.is_unset(request.zone):
            body['Zone'] = request.zone
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateResource',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/resources',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.CreateResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_resource_with_options_async(
        self,
        request: eas_20210701_models.CreateResourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.CreateResourceResponse:
        """
        @summary Creates a resource group.
        
        @description *Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/144261.html) of Elastic Algorithm Service (EAS).
        
        @param request: CreateResourceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateResourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_renewal):
            body['AutoRenewal'] = request.auto_renewal
        if not UtilClient.is_unset(request.charge_type):
            body['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.ecs_instance_count):
            body['EcsInstanceCount'] = request.ecs_instance_count
        if not UtilClient.is_unset(request.ecs_instance_type):
            body['EcsInstanceType'] = request.ecs_instance_type
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.self_managed_resource_options):
            body['SelfManagedResourceOptions'] = request.self_managed_resource_options
        if not UtilClient.is_unset(request.system_disk_size):
            body['SystemDiskSize'] = request.system_disk_size
        if not UtilClient.is_unset(request.zone):
            body['Zone'] = request.zone
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateResource',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/resources',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.CreateResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_resource(
        self,
        request: eas_20210701_models.CreateResourceRequest,
    ) -> eas_20210701_models.CreateResourceResponse:
        """
        @summary Creates a resource group.
        
        @description *Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/144261.html) of Elastic Algorithm Service (EAS).
        
        @param request: CreateResourceRequest
        @return: CreateResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_resource_with_options(request, headers, runtime)

    async def create_resource_async(
        self,
        request: eas_20210701_models.CreateResourceRequest,
    ) -> eas_20210701_models.CreateResourceResponse:
        """
        @summary Creates a resource group.
        
        @description *Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/144261.html) of Elastic Algorithm Service (EAS).
        
        @param request: CreateResourceRequest
        @return: CreateResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_resource_with_options_async(request, headers, runtime)

    def create_resource_instances_with_options(
        self,
        cluster_id: str,
        resource_id: str,
        request: eas_20210701_models.CreateResourceInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.CreateResourceInstancesResponse:
        """
        @summary Creates instances in a dedicated resource group.
        
        @param request: CreateResourceInstancesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateResourceInstancesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_renewal):
            body['AutoRenewal'] = request.auto_renewal
        if not UtilClient.is_unset(request.charge_type):
            body['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.ecs_instance_count):
            body['EcsInstanceCount'] = request.ecs_instance_count
        if not UtilClient.is_unset(request.ecs_instance_type):
            body['EcsInstanceType'] = request.ecs_instance_type
        if not UtilClient.is_unset(request.system_disk_size):
            body['SystemDiskSize'] = request.system_disk_size
        if not UtilClient.is_unset(request.user_data):
            body['UserData'] = request.user_data
        if not UtilClient.is_unset(request.zone):
            body['Zone'] = request.zone
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateResourceInstances',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/resources/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(resource_id)}/instances',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.CreateResourceInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_resource_instances_with_options_async(
        self,
        cluster_id: str,
        resource_id: str,
        request: eas_20210701_models.CreateResourceInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.CreateResourceInstancesResponse:
        """
        @summary Creates instances in a dedicated resource group.
        
        @param request: CreateResourceInstancesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateResourceInstancesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_renewal):
            body['AutoRenewal'] = request.auto_renewal
        if not UtilClient.is_unset(request.charge_type):
            body['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.ecs_instance_count):
            body['EcsInstanceCount'] = request.ecs_instance_count
        if not UtilClient.is_unset(request.ecs_instance_type):
            body['EcsInstanceType'] = request.ecs_instance_type
        if not UtilClient.is_unset(request.system_disk_size):
            body['SystemDiskSize'] = request.system_disk_size
        if not UtilClient.is_unset(request.user_data):
            body['UserData'] = request.user_data
        if not UtilClient.is_unset(request.zone):
            body['Zone'] = request.zone
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateResourceInstances',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/resources/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(resource_id)}/instances',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.CreateResourceInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_resource_instances(
        self,
        cluster_id: str,
        resource_id: str,
        request: eas_20210701_models.CreateResourceInstancesRequest,
    ) -> eas_20210701_models.CreateResourceInstancesResponse:
        """
        @summary Creates instances in a dedicated resource group.
        
        @param request: CreateResourceInstancesRequest
        @return: CreateResourceInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_resource_instances_with_options(cluster_id, resource_id, request, headers, runtime)

    async def create_resource_instances_async(
        self,
        cluster_id: str,
        resource_id: str,
        request: eas_20210701_models.CreateResourceInstancesRequest,
    ) -> eas_20210701_models.CreateResourceInstancesResponse:
        """
        @summary Creates instances in a dedicated resource group.
        
        @param request: CreateResourceInstancesRequest
        @return: CreateResourceInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_resource_instances_with_options_async(cluster_id, resource_id, request, headers, runtime)

    def create_resource_log_with_options(
        self,
        cluster_id: str,
        resource_id: str,
        request: eas_20210701_models.CreateResourceLogRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.CreateResourceLogResponse:
        """
        @summary Enables the LogShipper feature of Log Service for a resource group.
        
        @param request: CreateResourceLogRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateResourceLogResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.log_store):
            body['LogStore'] = request.log_store
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateResourceLog',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/resources/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(resource_id)}/log',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.CreateResourceLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_resource_log_with_options_async(
        self,
        cluster_id: str,
        resource_id: str,
        request: eas_20210701_models.CreateResourceLogRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.CreateResourceLogResponse:
        """
        @summary Enables the LogShipper feature of Log Service for a resource group.
        
        @param request: CreateResourceLogRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateResourceLogResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.log_store):
            body['LogStore'] = request.log_store
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateResourceLog',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/resources/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(resource_id)}/log',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.CreateResourceLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_resource_log(
        self,
        cluster_id: str,
        resource_id: str,
        request: eas_20210701_models.CreateResourceLogRequest,
    ) -> eas_20210701_models.CreateResourceLogResponse:
        """
        @summary Enables the LogShipper feature of Log Service for a resource group.
        
        @param request: CreateResourceLogRequest
        @return: CreateResourceLogResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_resource_log_with_options(cluster_id, resource_id, request, headers, runtime)

    async def create_resource_log_async(
        self,
        cluster_id: str,
        resource_id: str,
        request: eas_20210701_models.CreateResourceLogRequest,
    ) -> eas_20210701_models.CreateResourceLogResponse:
        """
        @summary Enables the LogShipper feature of Log Service for a resource group.
        
        @param request: CreateResourceLogRequest
        @return: CreateResourceLogResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_resource_log_with_options_async(cluster_id, resource_id, request, headers, runtime)

    def create_service_with_options(
        self,
        tmp_req: eas_20210701_models.CreateServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.CreateServiceResponse:
        """
        @summary Creates a model service in Elastic Algorithm Service (EAS).
        
        @description *Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/144261.html) of Elastic Algorithm Service (EAS).
        
        @param tmp_req: CreateServiceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateServiceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eas_20210701_models.CreateServiceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.labels):
            request.labels_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.labels, 'Labels', 'json')
        query = {}
        if not UtilClient.is_unset(request.develop):
            query['Develop'] = request.develop
        if not UtilClient.is_unset(request.labels_shrink):
            query['Labels'] = request.labels_shrink
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='CreateService',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.CreateServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_service_with_options_async(
        self,
        tmp_req: eas_20210701_models.CreateServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.CreateServiceResponse:
        """
        @summary Creates a model service in Elastic Algorithm Service (EAS).
        
        @description *Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/144261.html) of Elastic Algorithm Service (EAS).
        
        @param tmp_req: CreateServiceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateServiceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eas_20210701_models.CreateServiceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.labels):
            request.labels_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.labels, 'Labels', 'json')
        query = {}
        if not UtilClient.is_unset(request.develop):
            query['Develop'] = request.develop
        if not UtilClient.is_unset(request.labels_shrink):
            query['Labels'] = request.labels_shrink
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='CreateService',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.CreateServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_service(
        self,
        request: eas_20210701_models.CreateServiceRequest,
    ) -> eas_20210701_models.CreateServiceResponse:
        """
        @summary Creates a model service in Elastic Algorithm Service (EAS).
        
        @description *Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/144261.html) of Elastic Algorithm Service (EAS).
        
        @param request: CreateServiceRequest
        @return: CreateServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_service_with_options(request, headers, runtime)

    async def create_service_async(
        self,
        request: eas_20210701_models.CreateServiceRequest,
    ) -> eas_20210701_models.CreateServiceResponse:
        """
        @summary Creates a model service in Elastic Algorithm Service (EAS).
        
        @description *Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/144261.html) of Elastic Algorithm Service (EAS).
        
        @param request: CreateServiceRequest
        @return: CreateServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_service_with_options_async(request, headers, runtime)

    def create_service_auto_scaler_with_options(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.CreateServiceAutoScalerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.CreateServiceAutoScalerResponse:
        """
        @summary Enables the Autoscaler feature and creates an Autoscaler controller for a service.
        
        @param request: CreateServiceAutoScalerRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateServiceAutoScalerResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.behavior):
            body['behavior'] = request.behavior
        if not UtilClient.is_unset(request.max):
            body['max'] = request.max
        if not UtilClient.is_unset(request.min):
            body['min'] = request.min
        if not UtilClient.is_unset(request.scale_strategies):
            body['scaleStrategies'] = request.scale_strategies
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateServiceAutoScaler',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/autoscaler',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.CreateServiceAutoScalerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_service_auto_scaler_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.CreateServiceAutoScalerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.CreateServiceAutoScalerResponse:
        """
        @summary Enables the Autoscaler feature and creates an Autoscaler controller for a service.
        
        @param request: CreateServiceAutoScalerRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateServiceAutoScalerResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.behavior):
            body['behavior'] = request.behavior
        if not UtilClient.is_unset(request.max):
            body['max'] = request.max
        if not UtilClient.is_unset(request.min):
            body['min'] = request.min
        if not UtilClient.is_unset(request.scale_strategies):
            body['scaleStrategies'] = request.scale_strategies
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateServiceAutoScaler',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/autoscaler',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.CreateServiceAutoScalerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_service_auto_scaler(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.CreateServiceAutoScalerRequest,
    ) -> eas_20210701_models.CreateServiceAutoScalerResponse:
        """
        @summary Enables the Autoscaler feature and creates an Autoscaler controller for a service.
        
        @param request: CreateServiceAutoScalerRequest
        @return: CreateServiceAutoScalerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_service_auto_scaler_with_options(cluster_id, service_name, request, headers, runtime)

    async def create_service_auto_scaler_async(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.CreateServiceAutoScalerRequest,
    ) -> eas_20210701_models.CreateServiceAutoScalerResponse:
        """
        @summary Enables the Autoscaler feature and creates an Autoscaler controller for a service.
        
        @param request: CreateServiceAutoScalerRequest
        @return: CreateServiceAutoScalerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_service_auto_scaler_with_options_async(cluster_id, service_name, request, headers, runtime)

    def create_service_cron_scaler_with_options(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.CreateServiceCronScalerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.CreateServiceCronScalerResponse:
        """
        @summary Enables the Cron Horizontal Pod Autoscaler (CronHPA) feature for a service.
        
        @param request: CreateServiceCronScalerRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateServiceCronScalerResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.exclude_dates):
            body['ExcludeDates'] = request.exclude_dates
        if not UtilClient.is_unset(request.scale_jobs):
            body['ScaleJobs'] = request.scale_jobs
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateServiceCronScaler',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/cronscaler',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.CreateServiceCronScalerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_service_cron_scaler_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.CreateServiceCronScalerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.CreateServiceCronScalerResponse:
        """
        @summary Enables the Cron Horizontal Pod Autoscaler (CronHPA) feature for a service.
        
        @param request: CreateServiceCronScalerRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateServiceCronScalerResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.exclude_dates):
            body['ExcludeDates'] = request.exclude_dates
        if not UtilClient.is_unset(request.scale_jobs):
            body['ScaleJobs'] = request.scale_jobs
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateServiceCronScaler',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/cronscaler',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.CreateServiceCronScalerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_service_cron_scaler(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.CreateServiceCronScalerRequest,
    ) -> eas_20210701_models.CreateServiceCronScalerResponse:
        """
        @summary Enables the Cron Horizontal Pod Autoscaler (CronHPA) feature for a service.
        
        @param request: CreateServiceCronScalerRequest
        @return: CreateServiceCronScalerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_service_cron_scaler_with_options(cluster_id, service_name, request, headers, runtime)

    async def create_service_cron_scaler_async(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.CreateServiceCronScalerRequest,
    ) -> eas_20210701_models.CreateServiceCronScalerResponse:
        """
        @summary Enables the Cron Horizontal Pod Autoscaler (CronHPA) feature for a service.
        
        @param request: CreateServiceCronScalerRequest
        @return: CreateServiceCronScalerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_service_cron_scaler_with_options_async(cluster_id, service_name, request, headers, runtime)

    def create_service_mirror_with_options(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.CreateServiceMirrorRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.CreateServiceMirrorResponse:
        """
        @summary Enables the traffic mirroring feature for a service. After the feature is enabled, requests received by the service can be mirrored to another service.
        
        @param request: CreateServiceMirrorRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateServiceMirrorResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ratio):
            body['Ratio'] = request.ratio
        if not UtilClient.is_unset(request.target):
            body['Target'] = request.target
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateServiceMirror',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/mirror',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.CreateServiceMirrorResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_service_mirror_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.CreateServiceMirrorRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.CreateServiceMirrorResponse:
        """
        @summary Enables the traffic mirroring feature for a service. After the feature is enabled, requests received by the service can be mirrored to another service.
        
        @param request: CreateServiceMirrorRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateServiceMirrorResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ratio):
            body['Ratio'] = request.ratio
        if not UtilClient.is_unset(request.target):
            body['Target'] = request.target
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateServiceMirror',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/mirror',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.CreateServiceMirrorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_service_mirror(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.CreateServiceMirrorRequest,
    ) -> eas_20210701_models.CreateServiceMirrorResponse:
        """
        @summary Enables the traffic mirroring feature for a service. After the feature is enabled, requests received by the service can be mirrored to another service.
        
        @param request: CreateServiceMirrorRequest
        @return: CreateServiceMirrorResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_service_mirror_with_options(cluster_id, service_name, request, headers, runtime)

    async def create_service_mirror_async(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.CreateServiceMirrorRequest,
    ) -> eas_20210701_models.CreateServiceMirrorResponse:
        """
        @summary Enables the traffic mirroring feature for a service. After the feature is enabled, requests received by the service can be mirrored to another service.
        
        @param request: CreateServiceMirrorRequest
        @return: CreateServiceMirrorResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_service_mirror_with_options_async(cluster_id, service_name, request, headers, runtime)

    def delete_acl_policy_with_options(
        self,
        cluster_id: str,
        gateway_id: str,
        tmp_req: eas_20210701_models.DeleteAclPolicyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DeleteAclPolicyResponse:
        """
        @summary 移除网关acl policy entry
        
        @param tmp_req: DeleteAclPolicyRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAclPolicyResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eas_20210701_models.DeleteAclPolicyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.acl_policy_list):
            request.acl_policy_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.acl_policy_list, 'AclPolicyList', 'json')
        query = {}
        if not UtilClient.is_unset(request.acl_policy_list_shrink):
            query['AclPolicyList'] = request.acl_policy_list_shrink
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAclPolicy',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/gateways/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(gateway_id)}/acl_policy',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DeleteAclPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_acl_policy_with_options_async(
        self,
        cluster_id: str,
        gateway_id: str,
        tmp_req: eas_20210701_models.DeleteAclPolicyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DeleteAclPolicyResponse:
        """
        @summary 移除网关acl policy entry
        
        @param tmp_req: DeleteAclPolicyRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAclPolicyResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eas_20210701_models.DeleteAclPolicyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.acl_policy_list):
            request.acl_policy_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.acl_policy_list, 'AclPolicyList', 'json')
        query = {}
        if not UtilClient.is_unset(request.acl_policy_list_shrink):
            query['AclPolicyList'] = request.acl_policy_list_shrink
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAclPolicy',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/gateways/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(gateway_id)}/acl_policy',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DeleteAclPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_acl_policy(
        self,
        cluster_id: str,
        gateway_id: str,
        request: eas_20210701_models.DeleteAclPolicyRequest,
    ) -> eas_20210701_models.DeleteAclPolicyResponse:
        """
        @summary 移除网关acl policy entry
        
        @param request: DeleteAclPolicyRequest
        @return: DeleteAclPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_acl_policy_with_options(cluster_id, gateway_id, request, headers, runtime)

    async def delete_acl_policy_async(
        self,
        cluster_id: str,
        gateway_id: str,
        request: eas_20210701_models.DeleteAclPolicyRequest,
    ) -> eas_20210701_models.DeleteAclPolicyResponse:
        """
        @summary 移除网关acl policy entry
        
        @param request: DeleteAclPolicyRequest
        @return: DeleteAclPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_acl_policy_with_options_async(cluster_id, gateway_id, request, headers, runtime)

    def delete_benchmark_task_with_options(
        self,
        cluster_id: str,
        task_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DeleteBenchmarkTaskResponse:
        """
        @summary Deletes a stress testing task.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteBenchmarkTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteBenchmarkTask',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/benchmark-tasks/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(task_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DeleteBenchmarkTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_benchmark_task_with_options_async(
        self,
        cluster_id: str,
        task_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DeleteBenchmarkTaskResponse:
        """
        @summary Deletes a stress testing task.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteBenchmarkTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteBenchmarkTask',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/benchmark-tasks/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(task_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DeleteBenchmarkTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_benchmark_task(
        self,
        cluster_id: str,
        task_name: str,
    ) -> eas_20210701_models.DeleteBenchmarkTaskResponse:
        """
        @summary Deletes a stress testing task.
        
        @return: DeleteBenchmarkTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_benchmark_task_with_options(cluster_id, task_name, headers, runtime)

    async def delete_benchmark_task_async(
        self,
        cluster_id: str,
        task_name: str,
    ) -> eas_20210701_models.DeleteBenchmarkTaskResponse:
        """
        @summary Deletes a stress testing task.
        
        @return: DeleteBenchmarkTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_benchmark_task_with_options_async(cluster_id, task_name, headers, runtime)

    def delete_gateway_with_options(
        self,
        cluster_id: str,
        gateway_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DeleteGatewayResponse:
        """
        @summary Deletes a private gateway.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteGatewayResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteGateway',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/gateways/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(gateway_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DeleteGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_gateway_with_options_async(
        self,
        cluster_id: str,
        gateway_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DeleteGatewayResponse:
        """
        @summary Deletes a private gateway.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteGatewayResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteGateway',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/gateways/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(gateway_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DeleteGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_gateway(
        self,
        cluster_id: str,
        gateway_id: str,
    ) -> eas_20210701_models.DeleteGatewayResponse:
        """
        @summary Deletes a private gateway.
        
        @return: DeleteGatewayResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_gateway_with_options(cluster_id, gateway_id, headers, runtime)

    async def delete_gateway_async(
        self,
        cluster_id: str,
        gateway_id: str,
    ) -> eas_20210701_models.DeleteGatewayResponse:
        """
        @summary Deletes a private gateway.
        
        @return: DeleteGatewayResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_gateway_with_options_async(cluster_id, gateway_id, headers, runtime)

    def delete_gateway_intranet_linked_vpc_with_options(
        self,
        cluster_id: str,
        gateway_id: str,
        request: eas_20210701_models.DeleteGatewayIntranetLinkedVpcRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DeleteGatewayIntranetLinkedVpcResponse:
        """
        @summary 删除网关内网访问端点
        
        @param request: DeleteGatewayIntranetLinkedVpcRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteGatewayIntranetLinkedVpcResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGatewayIntranetLinkedVpc',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/gateways/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(gateway_id)}/intranet_endpoint_linked_vpc',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DeleteGatewayIntranetLinkedVpcResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_gateway_intranet_linked_vpc_with_options_async(
        self,
        cluster_id: str,
        gateway_id: str,
        request: eas_20210701_models.DeleteGatewayIntranetLinkedVpcRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DeleteGatewayIntranetLinkedVpcResponse:
        """
        @summary 删除网关内网访问端点
        
        @param request: DeleteGatewayIntranetLinkedVpcRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteGatewayIntranetLinkedVpcResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGatewayIntranetLinkedVpc',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/gateways/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(gateway_id)}/intranet_endpoint_linked_vpc',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DeleteGatewayIntranetLinkedVpcResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_gateway_intranet_linked_vpc(
        self,
        cluster_id: str,
        gateway_id: str,
        request: eas_20210701_models.DeleteGatewayIntranetLinkedVpcRequest,
    ) -> eas_20210701_models.DeleteGatewayIntranetLinkedVpcResponse:
        """
        @summary 删除网关内网访问端点
        
        @param request: DeleteGatewayIntranetLinkedVpcRequest
        @return: DeleteGatewayIntranetLinkedVpcResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_gateway_intranet_linked_vpc_with_options(cluster_id, gateway_id, request, headers, runtime)

    async def delete_gateway_intranet_linked_vpc_async(
        self,
        cluster_id: str,
        gateway_id: str,
        request: eas_20210701_models.DeleteGatewayIntranetLinkedVpcRequest,
    ) -> eas_20210701_models.DeleteGatewayIntranetLinkedVpcResponse:
        """
        @summary 删除网关内网访问端点
        
        @param request: DeleteGatewayIntranetLinkedVpcRequest
        @return: DeleteGatewayIntranetLinkedVpcResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_gateway_intranet_linked_vpc_with_options_async(cluster_id, gateway_id, request, headers, runtime)

    def delete_resource_with_options(
        self,
        cluster_id: str,
        resource_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DeleteResourceResponse:
        """
        @summary Deletes a resource group that contains no resources or instances.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteResourceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteResource',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/resources/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(resource_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DeleteResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_resource_with_options_async(
        self,
        cluster_id: str,
        resource_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DeleteResourceResponse:
        """
        @summary Deletes a resource group that contains no resources or instances.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteResourceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteResource',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/resources/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(resource_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DeleteResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_resource(
        self,
        cluster_id: str,
        resource_id: str,
    ) -> eas_20210701_models.DeleteResourceResponse:
        """
        @summary Deletes a resource group that contains no resources or instances.
        
        @return: DeleteResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_resource_with_options(cluster_id, resource_id, headers, runtime)

    async def delete_resource_async(
        self,
        cluster_id: str,
        resource_id: str,
    ) -> eas_20210701_models.DeleteResourceResponse:
        """
        @summary Deletes a resource group that contains no resources or instances.
        
        @return: DeleteResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_resource_with_options_async(cluster_id, resource_id, headers, runtime)

    def delete_resource_dlink_with_options(
        self,
        cluster_id: str,
        resource_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DeleteResourceDLinkResponse:
        """
        @summary Disables the virtual private cloud (VPC) direct connection feature for a dedicated resource group.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteResourceDLinkResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteResourceDLink',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/resources/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(resource_id)}/dlink',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DeleteResourceDLinkResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_resource_dlink_with_options_async(
        self,
        cluster_id: str,
        resource_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DeleteResourceDLinkResponse:
        """
        @summary Disables the virtual private cloud (VPC) direct connection feature for a dedicated resource group.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteResourceDLinkResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteResourceDLink',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/resources/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(resource_id)}/dlink',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DeleteResourceDLinkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_resource_dlink(
        self,
        cluster_id: str,
        resource_id: str,
    ) -> eas_20210701_models.DeleteResourceDLinkResponse:
        """
        @summary Disables the virtual private cloud (VPC) direct connection feature for a dedicated resource group.
        
        @return: DeleteResourceDLinkResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_resource_dlink_with_options(cluster_id, resource_id, headers, runtime)

    async def delete_resource_dlink_async(
        self,
        cluster_id: str,
        resource_id: str,
    ) -> eas_20210701_models.DeleteResourceDLinkResponse:
        """
        @summary Disables the virtual private cloud (VPC) direct connection feature for a dedicated resource group.
        
        @return: DeleteResourceDLinkResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_resource_dlink_with_options_async(cluster_id, resource_id, headers, runtime)

    def delete_resource_instances_with_options(
        self,
        cluster_id: str,
        resource_id: str,
        request: eas_20210701_models.DeleteResourceInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DeleteResourceInstancesResponse:
        """
        @summary Deletes instances in a dedicated resource group. You can delete only pay-as-you-go instances as a regular user.
        
        @param request: DeleteResourceInstancesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteResourceInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all_failed):
            query['AllFailed'] = request.all_failed
        if not UtilClient.is_unset(request.instance_list):
            query['InstanceList'] = request.instance_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteResourceInstances',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/resources/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(resource_id)}/instances',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DeleteResourceInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_resource_instances_with_options_async(
        self,
        cluster_id: str,
        resource_id: str,
        request: eas_20210701_models.DeleteResourceInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DeleteResourceInstancesResponse:
        """
        @summary Deletes instances in a dedicated resource group. You can delete only pay-as-you-go instances as a regular user.
        
        @param request: DeleteResourceInstancesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteResourceInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all_failed):
            query['AllFailed'] = request.all_failed
        if not UtilClient.is_unset(request.instance_list):
            query['InstanceList'] = request.instance_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteResourceInstances',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/resources/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(resource_id)}/instances',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DeleteResourceInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_resource_instances(
        self,
        cluster_id: str,
        resource_id: str,
        request: eas_20210701_models.DeleteResourceInstancesRequest,
    ) -> eas_20210701_models.DeleteResourceInstancesResponse:
        """
        @summary Deletes instances in a dedicated resource group. You can delete only pay-as-you-go instances as a regular user.
        
        @param request: DeleteResourceInstancesRequest
        @return: DeleteResourceInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_resource_instances_with_options(cluster_id, resource_id, request, headers, runtime)

    async def delete_resource_instances_async(
        self,
        cluster_id: str,
        resource_id: str,
        request: eas_20210701_models.DeleteResourceInstancesRequest,
    ) -> eas_20210701_models.DeleteResourceInstancesResponse:
        """
        @summary Deletes instances in a dedicated resource group. You can delete only pay-as-you-go instances as a regular user.
        
        @param request: DeleteResourceInstancesRequest
        @return: DeleteResourceInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_resource_instances_with_options_async(cluster_id, resource_id, request, headers, runtime)

    def delete_resource_log_with_options(
        self,
        cluster_id: str,
        resource_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DeleteResourceLogResponse:
        """
        @summary Disables the LogShipper feature of Log Service for a dedicated resource group.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteResourceLogResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteResourceLog',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/resources/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(resource_id)}/log',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DeleteResourceLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_resource_log_with_options_async(
        self,
        cluster_id: str,
        resource_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DeleteResourceLogResponse:
        """
        @summary Disables the LogShipper feature of Log Service for a dedicated resource group.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteResourceLogResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteResourceLog',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/resources/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(resource_id)}/log',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DeleteResourceLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_resource_log(
        self,
        cluster_id: str,
        resource_id: str,
    ) -> eas_20210701_models.DeleteResourceLogResponse:
        """
        @summary Disables the LogShipper feature of Log Service for a dedicated resource group.
        
        @return: DeleteResourceLogResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_resource_log_with_options(cluster_id, resource_id, headers, runtime)

    async def delete_resource_log_async(
        self,
        cluster_id: str,
        resource_id: str,
    ) -> eas_20210701_models.DeleteResourceLogResponse:
        """
        @summary Disables the LogShipper feature of Log Service for a dedicated resource group.
        
        @return: DeleteResourceLogResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_resource_log_with_options_async(cluster_id, resource_id, headers, runtime)

    def delete_service_with_options(
        self,
        cluster_id: str,
        service_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DeleteServiceResponse:
        """
        @summary Deletes a service.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteServiceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteService',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DeleteServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_service_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DeleteServiceResponse:
        """
        @summary Deletes a service.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteServiceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteService',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DeleteServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_service(
        self,
        cluster_id: str,
        service_name: str,
    ) -> eas_20210701_models.DeleteServiceResponse:
        """
        @summary Deletes a service.
        
        @return: DeleteServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_service_with_options(cluster_id, service_name, headers, runtime)

    async def delete_service_async(
        self,
        cluster_id: str,
        service_name: str,
    ) -> eas_20210701_models.DeleteServiceResponse:
        """
        @summary Deletes a service.
        
        @return: DeleteServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_service_with_options_async(cluster_id, service_name, headers, runtime)

    def delete_service_auto_scaler_with_options(
        self,
        cluster_id: str,
        service_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DeleteServiceAutoScalerResponse:
        """
        @summary Deletes the existing Autoscaler controller and disables the Autoscaler feature for a service.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteServiceAutoScalerResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteServiceAutoScaler',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/autoscaler',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DeleteServiceAutoScalerResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_service_auto_scaler_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DeleteServiceAutoScalerResponse:
        """
        @summary Deletes the existing Autoscaler controller and disables the Autoscaler feature for a service.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteServiceAutoScalerResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteServiceAutoScaler',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/autoscaler',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DeleteServiceAutoScalerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_service_auto_scaler(
        self,
        cluster_id: str,
        service_name: str,
    ) -> eas_20210701_models.DeleteServiceAutoScalerResponse:
        """
        @summary Deletes the existing Autoscaler controller and disables the Autoscaler feature for a service.
        
        @return: DeleteServiceAutoScalerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_service_auto_scaler_with_options(cluster_id, service_name, headers, runtime)

    async def delete_service_auto_scaler_async(
        self,
        cluster_id: str,
        service_name: str,
    ) -> eas_20210701_models.DeleteServiceAutoScalerResponse:
        """
        @summary Deletes the existing Autoscaler controller and disables the Autoscaler feature for a service.
        
        @return: DeleteServiceAutoScalerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_service_auto_scaler_with_options_async(cluster_id, service_name, headers, runtime)

    def delete_service_cron_scaler_with_options(
        self,
        cluster_id: str,
        service_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DeleteServiceCronScalerResponse:
        """
        @summary Disables the Cronscaler feature for a service.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteServiceCronScalerResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteServiceCronScaler',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/cronscaler',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DeleteServiceCronScalerResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_service_cron_scaler_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DeleteServiceCronScalerResponse:
        """
        @summary Disables the Cronscaler feature for a service.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteServiceCronScalerResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteServiceCronScaler',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/cronscaler',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DeleteServiceCronScalerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_service_cron_scaler(
        self,
        cluster_id: str,
        service_name: str,
    ) -> eas_20210701_models.DeleteServiceCronScalerResponse:
        """
        @summary Disables the Cronscaler feature for a service.
        
        @return: DeleteServiceCronScalerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_service_cron_scaler_with_options(cluster_id, service_name, headers, runtime)

    async def delete_service_cron_scaler_async(
        self,
        cluster_id: str,
        service_name: str,
    ) -> eas_20210701_models.DeleteServiceCronScalerResponse:
        """
        @summary Disables the Cronscaler feature for a service.
        
        @return: DeleteServiceCronScalerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_service_cron_scaler_with_options_async(cluster_id, service_name, headers, runtime)

    def delete_service_instances_with_options(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.DeleteServiceInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DeleteServiceInstancesResponse:
        """
        @summary Restarts the instances of a service.
        
        @param request: DeleteServiceInstancesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteServiceInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.container):
            query['Container'] = request.container
        if not UtilClient.is_unset(request.instance_list):
            query['InstanceList'] = request.instance_list
        if not UtilClient.is_unset(request.soft_restart):
            query['SoftRestart'] = request.soft_restart
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteServiceInstances',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/instances',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DeleteServiceInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_service_instances_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.DeleteServiceInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DeleteServiceInstancesResponse:
        """
        @summary Restarts the instances of a service.
        
        @param request: DeleteServiceInstancesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteServiceInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.container):
            query['Container'] = request.container
        if not UtilClient.is_unset(request.instance_list):
            query['InstanceList'] = request.instance_list
        if not UtilClient.is_unset(request.soft_restart):
            query['SoftRestart'] = request.soft_restart
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteServiceInstances',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/instances',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DeleteServiceInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_service_instances(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.DeleteServiceInstancesRequest,
    ) -> eas_20210701_models.DeleteServiceInstancesResponse:
        """
        @summary Restarts the instances of a service.
        
        @param request: DeleteServiceInstancesRequest
        @return: DeleteServiceInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_service_instances_with_options(cluster_id, service_name, request, headers, runtime)

    async def delete_service_instances_async(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.DeleteServiceInstancesRequest,
    ) -> eas_20210701_models.DeleteServiceInstancesResponse:
        """
        @summary Restarts the instances of a service.
        
        @param request: DeleteServiceInstancesRequest
        @return: DeleteServiceInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_service_instances_with_options_async(cluster_id, service_name, request, headers, runtime)

    def delete_service_label_with_options(
        self,
        cluster_id: str,
        service_name: str,
        tmp_req: eas_20210701_models.DeleteServiceLabelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DeleteServiceLabelResponse:
        """
        @summary Deletes existing service tags.
        
        @param tmp_req: DeleteServiceLabelRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteServiceLabelResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eas_20210701_models.DeleteServiceLabelShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.keys):
            request.keys_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.keys, 'Keys', 'simple')
        query = {}
        if not UtilClient.is_unset(request.keys_shrink):
            query['Keys'] = request.keys_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteServiceLabel',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/label',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DeleteServiceLabelResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_service_label_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        tmp_req: eas_20210701_models.DeleteServiceLabelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DeleteServiceLabelResponse:
        """
        @summary Deletes existing service tags.
        
        @param tmp_req: DeleteServiceLabelRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteServiceLabelResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eas_20210701_models.DeleteServiceLabelShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.keys):
            request.keys_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.keys, 'Keys', 'simple')
        query = {}
        if not UtilClient.is_unset(request.keys_shrink):
            query['Keys'] = request.keys_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteServiceLabel',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/label',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DeleteServiceLabelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_service_label(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.DeleteServiceLabelRequest,
    ) -> eas_20210701_models.DeleteServiceLabelResponse:
        """
        @summary Deletes existing service tags.
        
        @param request: DeleteServiceLabelRequest
        @return: DeleteServiceLabelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_service_label_with_options(cluster_id, service_name, request, headers, runtime)

    async def delete_service_label_async(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.DeleteServiceLabelRequest,
    ) -> eas_20210701_models.DeleteServiceLabelResponse:
        """
        @summary Deletes existing service tags.
        
        @param request: DeleteServiceLabelRequest
        @return: DeleteServiceLabelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_service_label_with_options_async(cluster_id, service_name, request, headers, runtime)

    def delete_service_mirror_with_options(
        self,
        cluster_id: str,
        service_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DeleteServiceMirrorResponse:
        """
        @summary Disables the traffic mirroring feature for a service.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteServiceMirrorResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteServiceMirror',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/mirror',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DeleteServiceMirrorResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_service_mirror_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DeleteServiceMirrorResponse:
        """
        @summary Disables the traffic mirroring feature for a service.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteServiceMirrorResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteServiceMirror',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/mirror',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DeleteServiceMirrorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_service_mirror(
        self,
        cluster_id: str,
        service_name: str,
    ) -> eas_20210701_models.DeleteServiceMirrorResponse:
        """
        @summary Disables the traffic mirroring feature for a service.
        
        @return: DeleteServiceMirrorResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_service_mirror_with_options(cluster_id, service_name, headers, runtime)

    async def delete_service_mirror_async(
        self,
        cluster_id: str,
        service_name: str,
    ) -> eas_20210701_models.DeleteServiceMirrorResponse:
        """
        @summary Disables the traffic mirroring feature for a service.
        
        @return: DeleteServiceMirrorResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_service_mirror_with_options_async(cluster_id, service_name, headers, runtime)

    def describe_benchmark_task_with_options(
        self,
        cluster_id: str,
        task_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DescribeBenchmarkTaskResponse:
        """
        @summary Queries details about the configurations of a stress testing task.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBenchmarkTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeBenchmarkTask',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/benchmark-tasks/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(task_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DescribeBenchmarkTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_benchmark_task_with_options_async(
        self,
        cluster_id: str,
        task_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DescribeBenchmarkTaskResponse:
        """
        @summary Queries details about the configurations of a stress testing task.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBenchmarkTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeBenchmarkTask',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/benchmark-tasks/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(task_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DescribeBenchmarkTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_benchmark_task(
        self,
        cluster_id: str,
        task_name: str,
    ) -> eas_20210701_models.DescribeBenchmarkTaskResponse:
        """
        @summary Queries details about the configurations of a stress testing task.
        
        @return: DescribeBenchmarkTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_benchmark_task_with_options(cluster_id, task_name, headers, runtime)

    async def describe_benchmark_task_async(
        self,
        cluster_id: str,
        task_name: str,
    ) -> eas_20210701_models.DescribeBenchmarkTaskResponse:
        """
        @summary Queries details about the configurations of a stress testing task.
        
        @return: DescribeBenchmarkTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_benchmark_task_with_options_async(cluster_id, task_name, headers, runtime)

    def describe_benchmark_task_report_with_options(
        self,
        cluster_id: str,
        task_name: str,
        request: eas_20210701_models.DescribeBenchmarkTaskReportRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DescribeBenchmarkTaskReportResponse:
        """
        @summary Queries the report of a stress testing task.
        
        @param request: DescribeBenchmarkTaskReportRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBenchmarkTaskReportResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.report_type):
            query['ReportType'] = request.report_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBenchmarkTaskReport',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/benchmark-tasks/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(task_name)}/report',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DescribeBenchmarkTaskReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_benchmark_task_report_with_options_async(
        self,
        cluster_id: str,
        task_name: str,
        request: eas_20210701_models.DescribeBenchmarkTaskReportRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DescribeBenchmarkTaskReportResponse:
        """
        @summary Queries the report of a stress testing task.
        
        @param request: DescribeBenchmarkTaskReportRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBenchmarkTaskReportResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.report_type):
            query['ReportType'] = request.report_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBenchmarkTaskReport',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/benchmark-tasks/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(task_name)}/report',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DescribeBenchmarkTaskReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_benchmark_task_report(
        self,
        cluster_id: str,
        task_name: str,
        request: eas_20210701_models.DescribeBenchmarkTaskReportRequest,
    ) -> eas_20210701_models.DescribeBenchmarkTaskReportResponse:
        """
        @summary Queries the report of a stress testing task.
        
        @param request: DescribeBenchmarkTaskReportRequest
        @return: DescribeBenchmarkTaskReportResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_benchmark_task_report_with_options(cluster_id, task_name, request, headers, runtime)

    async def describe_benchmark_task_report_async(
        self,
        cluster_id: str,
        task_name: str,
        request: eas_20210701_models.DescribeBenchmarkTaskReportRequest,
    ) -> eas_20210701_models.DescribeBenchmarkTaskReportResponse:
        """
        @summary Queries the report of a stress testing task.
        
        @param request: DescribeBenchmarkTaskReportRequest
        @return: DescribeBenchmarkTaskReportResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_benchmark_task_report_with_options_async(cluster_id, task_name, request, headers, runtime)

    def describe_gateway_with_options(
        self,
        cluster_id: str,
        gateway_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DescribeGatewayResponse:
        """
        @summary Queries the details of a private gateway.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGatewayResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeGateway',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/gateways/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(gateway_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DescribeGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_gateway_with_options_async(
        self,
        cluster_id: str,
        gateway_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DescribeGatewayResponse:
        """
        @summary Queries the details of a private gateway.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGatewayResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeGateway',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/gateways/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(gateway_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DescribeGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_gateway(
        self,
        cluster_id: str,
        gateway_id: str,
    ) -> eas_20210701_models.DescribeGatewayResponse:
        """
        @summary Queries the details of a private gateway.
        
        @return: DescribeGatewayResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_gateway_with_options(cluster_id, gateway_id, headers, runtime)

    async def describe_gateway_async(
        self,
        cluster_id: str,
        gateway_id: str,
    ) -> eas_20210701_models.DescribeGatewayResponse:
        """
        @summary Queries the details of a private gateway.
        
        @return: DescribeGatewayResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_gateway_with_options_async(cluster_id, gateway_id, headers, runtime)

    def describe_group_with_options(
        self,
        cluster_id: str,
        group_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DescribeGroupResponse:
        """
        @summary Queries the information about a service group.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGroupResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeGroup',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/groups/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(group_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DescribeGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_group_with_options_async(
        self,
        cluster_id: str,
        group_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DescribeGroupResponse:
        """
        @summary Queries the information about a service group.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGroupResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeGroup',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/groups/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(group_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DescribeGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_group(
        self,
        cluster_id: str,
        group_name: str,
    ) -> eas_20210701_models.DescribeGroupResponse:
        """
        @summary Queries the information about a service group.
        
        @return: DescribeGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_group_with_options(cluster_id, group_name, headers, runtime)

    async def describe_group_async(
        self,
        cluster_id: str,
        group_name: str,
    ) -> eas_20210701_models.DescribeGroupResponse:
        """
        @summary Queries the information about a service group.
        
        @return: DescribeGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_group_with_options_async(cluster_id, group_name, headers, runtime)

    def describe_resource_with_options(
        self,
        cluster_id: str,
        resource_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DescribeResourceResponse:
        """
        @summary Queries the information about a resource group.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeResourceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeResource',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/resources/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(resource_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DescribeResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_resource_with_options_async(
        self,
        cluster_id: str,
        resource_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DescribeResourceResponse:
        """
        @summary Queries the information about a resource group.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeResourceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeResource',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/resources/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(resource_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DescribeResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_resource(
        self,
        cluster_id: str,
        resource_id: str,
    ) -> eas_20210701_models.DescribeResourceResponse:
        """
        @summary Queries the information about a resource group.
        
        @return: DescribeResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_resource_with_options(cluster_id, resource_id, headers, runtime)

    async def describe_resource_async(
        self,
        cluster_id: str,
        resource_id: str,
    ) -> eas_20210701_models.DescribeResourceResponse:
        """
        @summary Queries the information about a resource group.
        
        @return: DescribeResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_resource_with_options_async(cluster_id, resource_id, headers, runtime)

    def describe_resource_dlink_with_options(
        self,
        cluster_id: str,
        resource_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DescribeResourceDLinkResponse:
        """
        @summary Queries detailed configurations about a virtual private cloud (VPC) direct connection of a dedicated resource group.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeResourceDLinkResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeResourceDLink',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/resources/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(resource_id)}/dlink',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DescribeResourceDLinkResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_resource_dlink_with_options_async(
        self,
        cluster_id: str,
        resource_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DescribeResourceDLinkResponse:
        """
        @summary Queries detailed configurations about a virtual private cloud (VPC) direct connection of a dedicated resource group.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeResourceDLinkResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeResourceDLink',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/resources/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(resource_id)}/dlink',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DescribeResourceDLinkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_resource_dlink(
        self,
        cluster_id: str,
        resource_id: str,
    ) -> eas_20210701_models.DescribeResourceDLinkResponse:
        """
        @summary Queries detailed configurations about a virtual private cloud (VPC) direct connection of a dedicated resource group.
        
        @return: DescribeResourceDLinkResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_resource_dlink_with_options(cluster_id, resource_id, headers, runtime)

    async def describe_resource_dlink_async(
        self,
        cluster_id: str,
        resource_id: str,
    ) -> eas_20210701_models.DescribeResourceDLinkResponse:
        """
        @summary Queries detailed configurations about a virtual private cloud (VPC) direct connection of a dedicated resource group.
        
        @return: DescribeResourceDLinkResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_resource_dlink_with_options_async(cluster_id, resource_id, headers, runtime)

    def describe_resource_log_with_options(
        self,
        cluster_id: str,
        resource_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DescribeResourceLogResponse:
        """
        @summary Queries the details about the LogShipper configurations of Log Service for a dedicated resource group.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeResourceLogResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeResourceLog',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/resources/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(resource_id)}/log',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DescribeResourceLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_resource_log_with_options_async(
        self,
        cluster_id: str,
        resource_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DescribeResourceLogResponse:
        """
        @summary Queries the details about the LogShipper configurations of Log Service for a dedicated resource group.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeResourceLogResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeResourceLog',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/resources/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(resource_id)}/log',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DescribeResourceLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_resource_log(
        self,
        cluster_id: str,
        resource_id: str,
    ) -> eas_20210701_models.DescribeResourceLogResponse:
        """
        @summary Queries the details about the LogShipper configurations of Log Service for a dedicated resource group.
        
        @return: DescribeResourceLogResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_resource_log_with_options(cluster_id, resource_id, headers, runtime)

    async def describe_resource_log_async(
        self,
        cluster_id: str,
        resource_id: str,
    ) -> eas_20210701_models.DescribeResourceLogResponse:
        """
        @summary Queries the details about the LogShipper configurations of Log Service for a dedicated resource group.
        
        @return: DescribeResourceLogResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_resource_log_with_options_async(cluster_id, resource_id, headers, runtime)

    def describe_service_with_options(
        self,
        cluster_id: str,
        service_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DescribeServiceResponse:
        """
        @summary Queries the details about a service.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeServiceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeService',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DescribeServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_service_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DescribeServiceResponse:
        """
        @summary Queries the details about a service.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeServiceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeService',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DescribeServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_service(
        self,
        cluster_id: str,
        service_name: str,
    ) -> eas_20210701_models.DescribeServiceResponse:
        """
        @summary Queries the details about a service.
        
        @return: DescribeServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_service_with_options(cluster_id, service_name, headers, runtime)

    async def describe_service_async(
        self,
        cluster_id: str,
        service_name: str,
    ) -> eas_20210701_models.DescribeServiceResponse:
        """
        @summary Queries the details about a service.
        
        @return: DescribeServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_service_with_options_async(cluster_id, service_name, headers, runtime)

    def describe_service_auto_scaler_with_options(
        self,
        cluster_id: str,
        service_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DescribeServiceAutoScalerResponse:
        """
        @summary Queries information about the Autoscaler configurations of a service.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeServiceAutoScalerResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeServiceAutoScaler',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/autoscaler',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DescribeServiceAutoScalerResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_service_auto_scaler_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DescribeServiceAutoScalerResponse:
        """
        @summary Queries information about the Autoscaler configurations of a service.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeServiceAutoScalerResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeServiceAutoScaler',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/autoscaler',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DescribeServiceAutoScalerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_service_auto_scaler(
        self,
        cluster_id: str,
        service_name: str,
    ) -> eas_20210701_models.DescribeServiceAutoScalerResponse:
        """
        @summary Queries information about the Autoscaler configurations of a service.
        
        @return: DescribeServiceAutoScalerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_service_auto_scaler_with_options(cluster_id, service_name, headers, runtime)

    async def describe_service_auto_scaler_async(
        self,
        cluster_id: str,
        service_name: str,
    ) -> eas_20210701_models.DescribeServiceAutoScalerResponse:
        """
        @summary Queries information about the Autoscaler configurations of a service.
        
        @return: DescribeServiceAutoScalerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_service_auto_scaler_with_options_async(cluster_id, service_name, headers, runtime)

    def describe_service_cron_scaler_with_options(
        self,
        cluster_id: str,
        service_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DescribeServiceCronScalerResponse:
        """
        @summary Queries the Cron Horizontal Pod Autoscaler (CronHPA) configurations of a service.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeServiceCronScalerResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeServiceCronScaler',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/cronscaler',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DescribeServiceCronScalerResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_service_cron_scaler_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DescribeServiceCronScalerResponse:
        """
        @summary Queries the Cron Horizontal Pod Autoscaler (CronHPA) configurations of a service.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeServiceCronScalerResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeServiceCronScaler',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/cronscaler',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DescribeServiceCronScalerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_service_cron_scaler(
        self,
        cluster_id: str,
        service_name: str,
    ) -> eas_20210701_models.DescribeServiceCronScalerResponse:
        """
        @summary Queries the Cron Horizontal Pod Autoscaler (CronHPA) configurations of a service.
        
        @return: DescribeServiceCronScalerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_service_cron_scaler_with_options(cluster_id, service_name, headers, runtime)

    async def describe_service_cron_scaler_async(
        self,
        cluster_id: str,
        service_name: str,
    ) -> eas_20210701_models.DescribeServiceCronScalerResponse:
        """
        @summary Queries the Cron Horizontal Pod Autoscaler (CronHPA) configurations of a service.
        
        @return: DescribeServiceCronScalerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_service_cron_scaler_with_options_async(cluster_id, service_name, headers, runtime)

    def describe_service_diagnosis_with_options(
        self,
        cluster_id: str,
        service_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DescribeServiceDiagnosisResponse:
        """
        @summary Queries the diagnostics details of a service.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeServiceDiagnosisResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeServiceDiagnosis',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/diagnosis',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DescribeServiceDiagnosisResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_service_diagnosis_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DescribeServiceDiagnosisResponse:
        """
        @summary Queries the diagnostics details of a service.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeServiceDiagnosisResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeServiceDiagnosis',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/diagnosis',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DescribeServiceDiagnosisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_service_diagnosis(
        self,
        cluster_id: str,
        service_name: str,
    ) -> eas_20210701_models.DescribeServiceDiagnosisResponse:
        """
        @summary Queries the diagnostics details of a service.
        
        @return: DescribeServiceDiagnosisResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_service_diagnosis_with_options(cluster_id, service_name, headers, runtime)

    async def describe_service_diagnosis_async(
        self,
        cluster_id: str,
        service_name: str,
    ) -> eas_20210701_models.DescribeServiceDiagnosisResponse:
        """
        @summary Queries the diagnostics details of a service.
        
        @return: DescribeServiceDiagnosisResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_service_diagnosis_with_options_async(cluster_id, service_name, headers, runtime)

    def describe_service_event_with_options(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.DescribeServiceEventRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DescribeServiceEventResponse:
        """
        @summary Queries information about recent service deployment events.
        
        @param request: DescribeServiceEventRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeServiceEventResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.event_type):
            query['EventType'] = request.event_type
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeServiceEvent',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/events',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DescribeServiceEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_service_event_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.DescribeServiceEventRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DescribeServiceEventResponse:
        """
        @summary Queries information about recent service deployment events.
        
        @param request: DescribeServiceEventRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeServiceEventResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.event_type):
            query['EventType'] = request.event_type
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeServiceEvent',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/events',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DescribeServiceEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_service_event(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.DescribeServiceEventRequest,
    ) -> eas_20210701_models.DescribeServiceEventResponse:
        """
        @summary Queries information about recent service deployment events.
        
        @param request: DescribeServiceEventRequest
        @return: DescribeServiceEventResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_service_event_with_options(cluster_id, service_name, request, headers, runtime)

    async def describe_service_event_async(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.DescribeServiceEventRequest,
    ) -> eas_20210701_models.DescribeServiceEventResponse:
        """
        @summary Queries information about recent service deployment events.
        
        @param request: DescribeServiceEventRequest
        @return: DescribeServiceEventResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_service_event_with_options_async(cluster_id, service_name, request, headers, runtime)

    def describe_service_instance_diagnosis_with_options(
        self,
        cluster_id: str,
        service_name: str,
        instance_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DescribeServiceInstanceDiagnosisResponse:
        """
        @summary Queries the diagnostics details of an instance that runs Elastic Algorithm Service (EAS).
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeServiceInstanceDiagnosisResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeServiceInstanceDiagnosis',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/instances/{OpenApiUtilClient.get_encode_param(instance_name)}/diagnosis',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DescribeServiceInstanceDiagnosisResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_service_instance_diagnosis_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        instance_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DescribeServiceInstanceDiagnosisResponse:
        """
        @summary Queries the diagnostics details of an instance that runs Elastic Algorithm Service (EAS).
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeServiceInstanceDiagnosisResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeServiceInstanceDiagnosis',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/instances/{OpenApiUtilClient.get_encode_param(instance_name)}/diagnosis',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DescribeServiceInstanceDiagnosisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_service_instance_diagnosis(
        self,
        cluster_id: str,
        service_name: str,
        instance_name: str,
    ) -> eas_20210701_models.DescribeServiceInstanceDiagnosisResponse:
        """
        @summary Queries the diagnostics details of an instance that runs Elastic Algorithm Service (EAS).
        
        @return: DescribeServiceInstanceDiagnosisResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_service_instance_diagnosis_with_options(cluster_id, service_name, instance_name, headers, runtime)

    async def describe_service_instance_diagnosis_async(
        self,
        cluster_id: str,
        service_name: str,
        instance_name: str,
    ) -> eas_20210701_models.DescribeServiceInstanceDiagnosisResponse:
        """
        @summary Queries the diagnostics details of an instance that runs Elastic Algorithm Service (EAS).
        
        @return: DescribeServiceInstanceDiagnosisResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_service_instance_diagnosis_with_options_async(cluster_id, service_name, instance_name, headers, runtime)

    def describe_service_log_with_options(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.DescribeServiceLogRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DescribeServiceLogResponse:
        """
        @summary Queries the information about the logs of a service.
        
        @param request: DescribeServiceLogRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeServiceLogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.container_name):
            query['ContainerName'] = request.container_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.previous):
            query['Previous'] = request.previous
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeServiceLog',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/logs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DescribeServiceLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_service_log_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.DescribeServiceLogRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DescribeServiceLogResponse:
        """
        @summary Queries the information about the logs of a service.
        
        @param request: DescribeServiceLogRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeServiceLogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.container_name):
            query['ContainerName'] = request.container_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.previous):
            query['Previous'] = request.previous
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeServiceLog',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/logs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DescribeServiceLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_service_log(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.DescribeServiceLogRequest,
    ) -> eas_20210701_models.DescribeServiceLogResponse:
        """
        @summary Queries the information about the logs of a service.
        
        @param request: DescribeServiceLogRequest
        @return: DescribeServiceLogResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_service_log_with_options(cluster_id, service_name, request, headers, runtime)

    async def describe_service_log_async(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.DescribeServiceLogRequest,
    ) -> eas_20210701_models.DescribeServiceLogResponse:
        """
        @summary Queries the information about the logs of a service.
        
        @param request: DescribeServiceLogRequest
        @return: DescribeServiceLogResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_service_log_with_options_async(cluster_id, service_name, request, headers, runtime)

    def describe_service_mirror_with_options(
        self,
        cluster_id: str,
        service_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DescribeServiceMirrorResponse:
        """
        @summary Queries details about the traffic mirroring settings of a service.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeServiceMirrorResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeServiceMirror',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/mirror',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DescribeServiceMirrorResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_service_mirror_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DescribeServiceMirrorResponse:
        """
        @summary Queries details about the traffic mirroring settings of a service.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeServiceMirrorResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeServiceMirror',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/mirror',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DescribeServiceMirrorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_service_mirror(
        self,
        cluster_id: str,
        service_name: str,
    ) -> eas_20210701_models.DescribeServiceMirrorResponse:
        """
        @summary Queries details about the traffic mirroring settings of a service.
        
        @return: DescribeServiceMirrorResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_service_mirror_with_options(cluster_id, service_name, headers, runtime)

    async def describe_service_mirror_async(
        self,
        cluster_id: str,
        service_name: str,
    ) -> eas_20210701_models.DescribeServiceMirrorResponse:
        """
        @summary Queries details about the traffic mirroring settings of a service.
        
        @return: DescribeServiceMirrorResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_service_mirror_with_options_async(cluster_id, service_name, headers, runtime)

    def describe_spot_discount_history_with_options(
        self,
        request: eas_20210701_models.DescribeSpotDiscountHistoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DescribeSpotDiscountHistoryResponse:
        """
        @summary Queries the historical prices of preemptible instances. For more information about preemptible instances, see Create and use preemptible instances.
        
        @param request: DescribeSpotDiscountHistoryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSpotDiscountHistoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.is_protect):
            query['IsProtect'] = request.is_protect
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSpotDiscountHistory',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/public/spot_discount',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DescribeSpotDiscountHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_spot_discount_history_with_options_async(
        self,
        request: eas_20210701_models.DescribeSpotDiscountHistoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DescribeSpotDiscountHistoryResponse:
        """
        @summary Queries the historical prices of preemptible instances. For more information about preemptible instances, see Create and use preemptible instances.
        
        @param request: DescribeSpotDiscountHistoryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSpotDiscountHistoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.is_protect):
            query['IsProtect'] = request.is_protect
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSpotDiscountHistory',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/public/spot_discount',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DescribeSpotDiscountHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_spot_discount_history(
        self,
        request: eas_20210701_models.DescribeSpotDiscountHistoryRequest,
    ) -> eas_20210701_models.DescribeSpotDiscountHistoryResponse:
        """
        @summary Queries the historical prices of preemptible instances. For more information about preemptible instances, see Create and use preemptible instances.
        
        @param request: DescribeSpotDiscountHistoryRequest
        @return: DescribeSpotDiscountHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_spot_discount_history_with_options(request, headers, runtime)

    async def describe_spot_discount_history_async(
        self,
        request: eas_20210701_models.DescribeSpotDiscountHistoryRequest,
    ) -> eas_20210701_models.DescribeSpotDiscountHistoryResponse:
        """
        @summary Queries the historical prices of preemptible instances. For more information about preemptible instances, see Create and use preemptible instances.
        
        @param request: DescribeSpotDiscountHistoryRequest
        @return: DescribeSpotDiscountHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_spot_discount_history_with_options_async(request, headers, runtime)

    def develop_service_with_options(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.DevelopServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DevelopServiceResponse:
        """
        @summary Switches a container service to development mode or exits development mode.
        
        @param request: DevelopServiceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DevelopServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.exit):
            query['Exit'] = request.exit
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DevelopService',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/develop',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DevelopServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def develop_service_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.DevelopServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.DevelopServiceResponse:
        """
        @summary Switches a container service to development mode or exits development mode.
        
        @param request: DevelopServiceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DevelopServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.exit):
            query['Exit'] = request.exit
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DevelopService',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/develop',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DevelopServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def develop_service(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.DevelopServiceRequest,
    ) -> eas_20210701_models.DevelopServiceResponse:
        """
        @summary Switches a container service to development mode or exits development mode.
        
        @param request: DevelopServiceRequest
        @return: DevelopServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.develop_service_with_options(cluster_id, service_name, request, headers, runtime)

    async def develop_service_async(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.DevelopServiceRequest,
    ) -> eas_20210701_models.DevelopServiceResponse:
        """
        @summary Switches a container service to development mode or exits development mode.
        
        @param request: DevelopServiceRequest
        @return: DevelopServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.develop_service_with_options_async(cluster_id, service_name, request, headers, runtime)

    def list_acl_policy_with_options(
        self,
        cluster_id: str,
        gateway_id: str,
        request: eas_20210701_models.ListAclPolicyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.ListAclPolicyResponse:
        """
        @summary 查询网关所有ACL Policy
        
        @param request: ListAclPolicyRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAclPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAclPolicy',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/gateways/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(gateway_id)}/acl_policy',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.ListAclPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_acl_policy_with_options_async(
        self,
        cluster_id: str,
        gateway_id: str,
        request: eas_20210701_models.ListAclPolicyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.ListAclPolicyResponse:
        """
        @summary 查询网关所有ACL Policy
        
        @param request: ListAclPolicyRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAclPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAclPolicy',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/gateways/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(gateway_id)}/acl_policy',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.ListAclPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_acl_policy(
        self,
        cluster_id: str,
        gateway_id: str,
        request: eas_20210701_models.ListAclPolicyRequest,
    ) -> eas_20210701_models.ListAclPolicyResponse:
        """
        @summary 查询网关所有ACL Policy
        
        @param request: ListAclPolicyRequest
        @return: ListAclPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_acl_policy_with_options(cluster_id, gateway_id, request, headers, runtime)

    async def list_acl_policy_async(
        self,
        cluster_id: str,
        gateway_id: str,
        request: eas_20210701_models.ListAclPolicyRequest,
    ) -> eas_20210701_models.ListAclPolicyResponse:
        """
        @summary 查询网关所有ACL Policy
        
        @param request: ListAclPolicyRequest
        @return: ListAclPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_acl_policy_with_options_async(cluster_id, gateway_id, request, headers, runtime)

    def list_benchmark_task_with_options(
        self,
        request: eas_20210701_models.ListBenchmarkTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.ListBenchmarkTaskResponse:
        """
        @summary Queries a list of stress testing tasks that are created by the current user.
        
        @param request: ListBenchmarkTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListBenchmarkTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBenchmarkTask',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/benchmark-tasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.ListBenchmarkTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_benchmark_task_with_options_async(
        self,
        request: eas_20210701_models.ListBenchmarkTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.ListBenchmarkTaskResponse:
        """
        @summary Queries a list of stress testing tasks that are created by the current user.
        
        @param request: ListBenchmarkTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListBenchmarkTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBenchmarkTask',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/benchmark-tasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.ListBenchmarkTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_benchmark_task(
        self,
        request: eas_20210701_models.ListBenchmarkTaskRequest,
    ) -> eas_20210701_models.ListBenchmarkTaskResponse:
        """
        @summary Queries a list of stress testing tasks that are created by the current user.
        
        @param request: ListBenchmarkTaskRequest
        @return: ListBenchmarkTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_benchmark_task_with_options(request, headers, runtime)

    async def list_benchmark_task_async(
        self,
        request: eas_20210701_models.ListBenchmarkTaskRequest,
    ) -> eas_20210701_models.ListBenchmarkTaskResponse:
        """
        @summary Queries a list of stress testing tasks that are created by the current user.
        
        @param request: ListBenchmarkTaskRequest
        @return: ListBenchmarkTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_benchmark_task_with_options_async(request, headers, runtime)

    def list_gateway_with_options(
        self,
        request: eas_20210701_models.ListGatewayRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.ListGatewayResponse:
        """
        @summary 列举gateway
        
        @param request: ListGatewayRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListGatewayResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.gateway_name):
            query['GatewayName'] = request.gateway_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGateway',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/gateways',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.ListGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_gateway_with_options_async(
        self,
        request: eas_20210701_models.ListGatewayRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.ListGatewayResponse:
        """
        @summary 列举gateway
        
        @param request: ListGatewayRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListGatewayResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.gateway_name):
            query['GatewayName'] = request.gateway_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGateway',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/gateways',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.ListGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_gateway(
        self,
        request: eas_20210701_models.ListGatewayRequest,
    ) -> eas_20210701_models.ListGatewayResponse:
        """
        @summary 列举gateway
        
        @param request: ListGatewayRequest
        @return: ListGatewayResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_gateway_with_options(request, headers, runtime)

    async def list_gateway_async(
        self,
        request: eas_20210701_models.ListGatewayRequest,
    ) -> eas_20210701_models.ListGatewayResponse:
        """
        @summary 列举gateway
        
        @param request: ListGatewayRequest
        @return: ListGatewayResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_gateway_with_options_async(request, headers, runtime)

    def list_gateway_intranet_linked_vpc_with_options(
        self,
        cluster_id: str,
        gateway_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.ListGatewayIntranetLinkedVpcResponse:
        """
        @summary Queries a list of the internal endpoints of a private gateway.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListGatewayIntranetLinkedVpcResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListGatewayIntranetLinkedVpc',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/gateways/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(gateway_id)}/intranet_endpoint_linked_vpc',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.ListGatewayIntranetLinkedVpcResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_gateway_intranet_linked_vpc_with_options_async(
        self,
        cluster_id: str,
        gateway_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.ListGatewayIntranetLinkedVpcResponse:
        """
        @summary Queries a list of the internal endpoints of a private gateway.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListGatewayIntranetLinkedVpcResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListGatewayIntranetLinkedVpc',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/gateways/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(gateway_id)}/intranet_endpoint_linked_vpc',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.ListGatewayIntranetLinkedVpcResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_gateway_intranet_linked_vpc(
        self,
        cluster_id: str,
        gateway_id: str,
    ) -> eas_20210701_models.ListGatewayIntranetLinkedVpcResponse:
        """
        @summary Queries a list of the internal endpoints of a private gateway.
        
        @return: ListGatewayIntranetLinkedVpcResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_gateway_intranet_linked_vpc_with_options(cluster_id, gateway_id, headers, runtime)

    async def list_gateway_intranet_linked_vpc_async(
        self,
        cluster_id: str,
        gateway_id: str,
    ) -> eas_20210701_models.ListGatewayIntranetLinkedVpcResponse:
        """
        @summary Queries a list of the internal endpoints of a private gateway.
        
        @return: ListGatewayIntranetLinkedVpcResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_gateway_intranet_linked_vpc_with_options_async(cluster_id, gateway_id, headers, runtime)

    def list_groups_with_options(
        self,
        request: eas_20210701_models.ListGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.ListGroupsResponse:
        """
        @summary Queries created service groups.
        
        @param request: ListGroupsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGroups',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/groups',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.ListGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_groups_with_options_async(
        self,
        request: eas_20210701_models.ListGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.ListGroupsResponse:
        """
        @summary Queries created service groups.
        
        @param request: ListGroupsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGroups',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/groups',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.ListGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_groups(
        self,
        request: eas_20210701_models.ListGroupsRequest,
    ) -> eas_20210701_models.ListGroupsResponse:
        """
        @summary Queries created service groups.
        
        @param request: ListGroupsRequest
        @return: ListGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_groups_with_options(request, headers, runtime)

    async def list_groups_async(
        self,
        request: eas_20210701_models.ListGroupsRequest,
    ) -> eas_20210701_models.ListGroupsResponse:
        """
        @summary Queries created service groups.
        
        @param request: ListGroupsRequest
        @return: ListGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_groups_with_options_async(request, headers, runtime)

    def list_resource_instance_worker_with_options(
        self,
        cluster_id: str,
        resource_id: str,
        instance_name: str,
        request: eas_20210701_models.ListResourceInstanceWorkerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.ListResourceInstanceWorkerResponse:
        """
        @summary Queries a list of workers in a resource group.
        
        @param request: ListResourceInstanceWorkerRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResourceInstanceWorkerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceInstanceWorker',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/resources/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(resource_id)}/instance/{OpenApiUtilClient.get_encode_param(instance_name)}/workers',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.ListResourceInstanceWorkerResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_instance_worker_with_options_async(
        self,
        cluster_id: str,
        resource_id: str,
        instance_name: str,
        request: eas_20210701_models.ListResourceInstanceWorkerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.ListResourceInstanceWorkerResponse:
        """
        @summary Queries a list of workers in a resource group.
        
        @param request: ListResourceInstanceWorkerRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResourceInstanceWorkerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceInstanceWorker',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/resources/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(resource_id)}/instance/{OpenApiUtilClient.get_encode_param(instance_name)}/workers',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.ListResourceInstanceWorkerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_instance_worker(
        self,
        cluster_id: str,
        resource_id: str,
        instance_name: str,
        request: eas_20210701_models.ListResourceInstanceWorkerRequest,
    ) -> eas_20210701_models.ListResourceInstanceWorkerResponse:
        """
        @summary Queries a list of workers in a resource group.
        
        @param request: ListResourceInstanceWorkerRequest
        @return: ListResourceInstanceWorkerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_resource_instance_worker_with_options(cluster_id, resource_id, instance_name, request, headers, runtime)

    async def list_resource_instance_worker_async(
        self,
        cluster_id: str,
        resource_id: str,
        instance_name: str,
        request: eas_20210701_models.ListResourceInstanceWorkerRequest,
    ) -> eas_20210701_models.ListResourceInstanceWorkerResponse:
        """
        @summary Queries a list of workers in a resource group.
        
        @param request: ListResourceInstanceWorkerRequest
        @return: ListResourceInstanceWorkerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_resource_instance_worker_with_options_async(cluster_id, resource_id, instance_name, request, headers, runtime)

    def list_resource_instances_with_options(
        self,
        cluster_id: str,
        resource_id: str,
        request: eas_20210701_models.ListResourceInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.ListResourceInstancesResponse:
        """
        @summary Queries a list of instances in a dedicated resource group.
        
        @param request: ListResourceInstancesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResourceInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.instance_ip):
            query['InstanceIP'] = request.instance_ip
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_status):
            query['InstanceStatus'] = request.instance_status
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceInstances',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/resources/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(resource_id)}/instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.ListResourceInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_instances_with_options_async(
        self,
        cluster_id: str,
        resource_id: str,
        request: eas_20210701_models.ListResourceInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.ListResourceInstancesResponse:
        """
        @summary Queries a list of instances in a dedicated resource group.
        
        @param request: ListResourceInstancesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResourceInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.instance_ip):
            query['InstanceIP'] = request.instance_ip
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_status):
            query['InstanceStatus'] = request.instance_status
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceInstances',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/resources/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(resource_id)}/instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.ListResourceInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_instances(
        self,
        cluster_id: str,
        resource_id: str,
        request: eas_20210701_models.ListResourceInstancesRequest,
    ) -> eas_20210701_models.ListResourceInstancesResponse:
        """
        @summary Queries a list of instances in a dedicated resource group.
        
        @param request: ListResourceInstancesRequest
        @return: ListResourceInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_resource_instances_with_options(cluster_id, resource_id, request, headers, runtime)

    async def list_resource_instances_async(
        self,
        cluster_id: str,
        resource_id: str,
        request: eas_20210701_models.ListResourceInstancesRequest,
    ) -> eas_20210701_models.ListResourceInstancesResponse:
        """
        @summary Queries a list of instances in a dedicated resource group.
        
        @param request: ListResourceInstancesRequest
        @return: ListResourceInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_resource_instances_with_options_async(cluster_id, resource_id, request, headers, runtime)

    def list_resource_services_with_options(
        self,
        cluster_id: str,
        resource_id: str,
        request: eas_20210701_models.ListResourceServicesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.ListResourceServicesResponse:
        """
        @deprecated OpenAPI ListResourceServices is deprecated
        
        @summary Queries a list of services that are deployed in the dedicated resource group.
        
        @param request: ListResourceServicesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResourceServicesResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceServices',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/resources/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(resource_id)}/services',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.ListResourceServicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_services_with_options_async(
        self,
        cluster_id: str,
        resource_id: str,
        request: eas_20210701_models.ListResourceServicesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.ListResourceServicesResponse:
        """
        @deprecated OpenAPI ListResourceServices is deprecated
        
        @summary Queries a list of services that are deployed in the dedicated resource group.
        
        @param request: ListResourceServicesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResourceServicesResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceServices',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/resources/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(resource_id)}/services',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.ListResourceServicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_services(
        self,
        cluster_id: str,
        resource_id: str,
        request: eas_20210701_models.ListResourceServicesRequest,
    ) -> eas_20210701_models.ListResourceServicesResponse:
        """
        @deprecated OpenAPI ListResourceServices is deprecated
        
        @summary Queries a list of services that are deployed in the dedicated resource group.
        
        @param request: ListResourceServicesRequest
        @return: ListResourceServicesResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_resource_services_with_options(cluster_id, resource_id, request, headers, runtime)

    async def list_resource_services_async(
        self,
        cluster_id: str,
        resource_id: str,
        request: eas_20210701_models.ListResourceServicesRequest,
    ) -> eas_20210701_models.ListResourceServicesResponse:
        """
        @deprecated OpenAPI ListResourceServices is deprecated
        
        @summary Queries a list of services that are deployed in the dedicated resource group.
        
        @param request: ListResourceServicesRequest
        @return: ListResourceServicesResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_resource_services_with_options_async(cluster_id, resource_id, request, headers, runtime)

    def list_resources_with_options(
        self,
        request: eas_20210701_models.ListResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.ListResourcesResponse:
        """
        @summary Queries a list of dedicated resource groups for the current user.
        
        @param request: ListResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResources',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/resources',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.ListResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resources_with_options_async(
        self,
        request: eas_20210701_models.ListResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.ListResourcesResponse:
        """
        @summary Queries a list of dedicated resource groups for the current user.
        
        @param request: ListResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResources',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/resources',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.ListResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resources(
        self,
        request: eas_20210701_models.ListResourcesRequest,
    ) -> eas_20210701_models.ListResourcesResponse:
        """
        @summary Queries a list of dedicated resource groups for the current user.
        
        @param request: ListResourcesRequest
        @return: ListResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_resources_with_options(request, headers, runtime)

    async def list_resources_async(
        self,
        request: eas_20210701_models.ListResourcesRequest,
    ) -> eas_20210701_models.ListResourcesResponse:
        """
        @summary Queries a list of dedicated resource groups for the current user.
        
        @param request: ListResourcesRequest
        @return: ListResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_resources_with_options_async(request, headers, runtime)

    def list_service_containers_with_options(
        self,
        cluster_id: str,
        service_name: str,
        instance_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.ListServiceContainersResponse:
        """
        @summary Queries the containers of a service.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServiceContainersResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListServiceContainers',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/instances/{OpenApiUtilClient.get_encode_param(instance_name)}/containers',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.ListServiceContainersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_service_containers_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        instance_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.ListServiceContainersResponse:
        """
        @summary Queries the containers of a service.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServiceContainersResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListServiceContainers',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/instances/{OpenApiUtilClient.get_encode_param(instance_name)}/containers',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.ListServiceContainersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_service_containers(
        self,
        cluster_id: str,
        service_name: str,
        instance_name: str,
    ) -> eas_20210701_models.ListServiceContainersResponse:
        """
        @summary Queries the containers of a service.
        
        @return: ListServiceContainersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_service_containers_with_options(cluster_id, service_name, instance_name, headers, runtime)

    async def list_service_containers_async(
        self,
        cluster_id: str,
        service_name: str,
        instance_name: str,
    ) -> eas_20210701_models.ListServiceContainersResponse:
        """
        @summary Queries the containers of a service.
        
        @return: ListServiceContainersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_service_containers_with_options_async(cluster_id, service_name, instance_name, headers, runtime)

    def list_service_instances_with_options(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.ListServiceInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.ListServiceInstancesResponse:
        """
        @summary Queries instances of a service.
        
        @param request: ListServiceInstancesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServiceInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.host_ip):
            query['HostIP'] = request.host_ip
        if not UtilClient.is_unset(request.instance_ip):
            query['InstanceIP'] = request.instance_ip
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_status):
            query['InstanceStatus'] = request.instance_status
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.is_spot):
            query['IsSpot'] = request.is_spot
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.role):
            query['Role'] = request.role
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServiceInstances',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.ListServiceInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_service_instances_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.ListServiceInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.ListServiceInstancesResponse:
        """
        @summary Queries instances of a service.
        
        @param request: ListServiceInstancesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServiceInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.host_ip):
            query['HostIP'] = request.host_ip
        if not UtilClient.is_unset(request.instance_ip):
            query['InstanceIP'] = request.instance_ip
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_status):
            query['InstanceStatus'] = request.instance_status
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.is_spot):
            query['IsSpot'] = request.is_spot
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.role):
            query['Role'] = request.role
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServiceInstances',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.ListServiceInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_service_instances(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.ListServiceInstancesRequest,
    ) -> eas_20210701_models.ListServiceInstancesResponse:
        """
        @summary Queries instances of a service.
        
        @param request: ListServiceInstancesRequest
        @return: ListServiceInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_service_instances_with_options(cluster_id, service_name, request, headers, runtime)

    async def list_service_instances_async(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.ListServiceInstancesRequest,
    ) -> eas_20210701_models.ListServiceInstancesResponse:
        """
        @summary Queries instances of a service.
        
        @param request: ListServiceInstancesRequest
        @return: ListServiceInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_service_instances_with_options_async(cluster_id, service_name, request, headers, runtime)

    def list_service_versions_with_options(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.ListServiceVersionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.ListServiceVersionsResponse:
        """
        @summary Queries the information about the historical versions of a service.
        
        @param request: ListServiceVersionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServiceVersionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServiceVersions',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/versions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.ListServiceVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_service_versions_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.ListServiceVersionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.ListServiceVersionsResponse:
        """
        @summary Queries the information about the historical versions of a service.
        
        @param request: ListServiceVersionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServiceVersionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServiceVersions',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/versions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.ListServiceVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_service_versions(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.ListServiceVersionsRequest,
    ) -> eas_20210701_models.ListServiceVersionsResponse:
        """
        @summary Queries the information about the historical versions of a service.
        
        @param request: ListServiceVersionsRequest
        @return: ListServiceVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_service_versions_with_options(cluster_id, service_name, request, headers, runtime)

    async def list_service_versions_async(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.ListServiceVersionsRequest,
    ) -> eas_20210701_models.ListServiceVersionsResponse:
        """
        @summary Queries the information about the historical versions of a service.
        
        @param request: ListServiceVersionsRequest
        @return: ListServiceVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_service_versions_with_options_async(cluster_id, service_name, request, headers, runtime)

    def list_services_with_options(
        self,
        tmp_req: eas_20210701_models.ListServicesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.ListServicesResponse:
        """
        @summary Queries a list of services that are created by the current user.
        
        @param tmp_req: ListServicesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServicesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eas_20210701_models.ListServicesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.label):
            request.label_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.label, 'Label', 'json')
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.gateway):
            query['Gateway'] = request.gateway
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.label_shrink):
            query['Label'] = request.label_shrink
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.parent_service_uid):
            query['ParentServiceUid'] = request.parent_service_uid
        if not UtilClient.is_unset(request.quota_id):
            query['QuotaId'] = request.quota_id
        if not UtilClient.is_unset(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        if not UtilClient.is_unset(request.service_status):
            query['ServiceStatus'] = request.service_status
        if not UtilClient.is_unset(request.service_type):
            query['ServiceType'] = request.service_type
        if not UtilClient.is_unset(request.service_uid):
            query['ServiceUid'] = request.service_uid
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServices',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.ListServicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_services_with_options_async(
        self,
        tmp_req: eas_20210701_models.ListServicesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.ListServicesResponse:
        """
        @summary Queries a list of services that are created by the current user.
        
        @param tmp_req: ListServicesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServicesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eas_20210701_models.ListServicesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.label):
            request.label_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.label, 'Label', 'json')
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.gateway):
            query['Gateway'] = request.gateway
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.label_shrink):
            query['Label'] = request.label_shrink
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.parent_service_uid):
            query['ParentServiceUid'] = request.parent_service_uid
        if not UtilClient.is_unset(request.quota_id):
            query['QuotaId'] = request.quota_id
        if not UtilClient.is_unset(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        if not UtilClient.is_unset(request.service_status):
            query['ServiceStatus'] = request.service_status
        if not UtilClient.is_unset(request.service_type):
            query['ServiceType'] = request.service_type
        if not UtilClient.is_unset(request.service_uid):
            query['ServiceUid'] = request.service_uid
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServices',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.ListServicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_services(
        self,
        request: eas_20210701_models.ListServicesRequest,
    ) -> eas_20210701_models.ListServicesResponse:
        """
        @summary Queries a list of services that are created by the current user.
        
        @param request: ListServicesRequest
        @return: ListServicesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_services_with_options(request, headers, runtime)

    async def list_services_async(
        self,
        request: eas_20210701_models.ListServicesRequest,
    ) -> eas_20210701_models.ListServicesResponse:
        """
        @summary Queries a list of services that are created by the current user.
        
        @param request: ListServicesRequest
        @return: ListServicesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_services_with_options_async(request, headers, runtime)

    def list_tenant_addons_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.ListTenantAddonsResponse:
        """
        @summary 获取租户配置列表
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTenantAddonsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListTenantAddons',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/tenantaddons',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.ListTenantAddonsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tenant_addons_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.ListTenantAddonsResponse:
        """
        @summary 获取租户配置列表
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTenantAddonsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListTenantAddons',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/tenantaddons',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.ListTenantAddonsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tenant_addons(self) -> eas_20210701_models.ListTenantAddonsResponse:
        """
        @summary 获取租户配置列表
        
        @return: ListTenantAddonsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_tenant_addons_with_options(headers, runtime)

    async def list_tenant_addons_async(self) -> eas_20210701_models.ListTenantAddonsResponse:
        """
        @summary 获取租户配置列表
        
        @return: ListTenantAddonsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_tenant_addons_with_options_async(headers, runtime)

    def reinstall_tenant_addon_with_options(
        self,
        cluster_id: str,
        tenant_addon_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.ReinstallTenantAddonResponse:
        """
        @summary 重置租户配置
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReinstallTenantAddonResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ReinstallTenantAddon',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/tenantaddons/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(tenant_addon_name)}/reinstall',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.ReinstallTenantAddonResponse(),
            self.call_api(params, req, runtime)
        )

    async def reinstall_tenant_addon_with_options_async(
        self,
        cluster_id: str,
        tenant_addon_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.ReinstallTenantAddonResponse:
        """
        @summary 重置租户配置
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReinstallTenantAddonResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ReinstallTenantAddon',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/tenantaddons/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(tenant_addon_name)}/reinstall',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.ReinstallTenantAddonResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reinstall_tenant_addon(
        self,
        cluster_id: str,
        tenant_addon_name: str,
    ) -> eas_20210701_models.ReinstallTenantAddonResponse:
        """
        @summary 重置租户配置
        
        @return: ReinstallTenantAddonResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.reinstall_tenant_addon_with_options(cluster_id, tenant_addon_name, headers, runtime)

    async def reinstall_tenant_addon_async(
        self,
        cluster_id: str,
        tenant_addon_name: str,
    ) -> eas_20210701_models.ReinstallTenantAddonResponse:
        """
        @summary 重置租户配置
        
        @return: ReinstallTenantAddonResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.reinstall_tenant_addon_with_options_async(cluster_id, tenant_addon_name, headers, runtime)

    def release_service_with_options(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.ReleaseServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.ReleaseServiceResponse:
        """
        @summary Performs canary release or blue-green release of a service.
        
        @param request: ReleaseServiceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseServiceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.traffic_state):
            body['TrafficState'] = request.traffic_state
        if not UtilClient.is_unset(request.weight):
            body['Weight'] = request.weight
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReleaseService',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/release',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.ReleaseServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_service_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.ReleaseServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.ReleaseServiceResponse:
        """
        @summary Performs canary release or blue-green release of a service.
        
        @param request: ReleaseServiceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseServiceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.traffic_state):
            body['TrafficState'] = request.traffic_state
        if not UtilClient.is_unset(request.weight):
            body['Weight'] = request.weight
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReleaseService',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/release',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.ReleaseServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_service(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.ReleaseServiceRequest,
    ) -> eas_20210701_models.ReleaseServiceResponse:
        """
        @summary Performs canary release or blue-green release of a service.
        
        @param request: ReleaseServiceRequest
        @return: ReleaseServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.release_service_with_options(cluster_id, service_name, request, headers, runtime)

    async def release_service_async(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.ReleaseServiceRequest,
    ) -> eas_20210701_models.ReleaseServiceResponse:
        """
        @summary Performs canary release or blue-green release of a service.
        
        @param request: ReleaseServiceRequest
        @return: ReleaseServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.release_service_with_options_async(cluster_id, service_name, request, headers, runtime)

    def restart_service_with_options(
        self,
        cluster_id: str,
        service_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.RestartServiceResponse:
        """
        @summary Restarts a service.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestartServiceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RestartService',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/restart',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.RestartServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_service_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.RestartServiceResponse:
        """
        @summary Restarts a service.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestartServiceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RestartService',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/restart',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.RestartServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_service(
        self,
        cluster_id: str,
        service_name: str,
    ) -> eas_20210701_models.RestartServiceResponse:
        """
        @summary Restarts a service.
        
        @return: RestartServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.restart_service_with_options(cluster_id, service_name, headers, runtime)

    async def restart_service_async(
        self,
        cluster_id: str,
        service_name: str,
    ) -> eas_20210701_models.RestartServiceResponse:
        """
        @summary Restarts a service.
        
        @return: RestartServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.restart_service_with_options_async(cluster_id, service_name, headers, runtime)

    def start_benchmark_task_with_options(
        self,
        cluster_id: str,
        task_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.StartBenchmarkTaskResponse:
        """
        @summary Starts a stress testing task.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartBenchmarkTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StartBenchmarkTask',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/benchmark-tasks/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(task_name)}/start',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.StartBenchmarkTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_benchmark_task_with_options_async(
        self,
        cluster_id: str,
        task_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.StartBenchmarkTaskResponse:
        """
        @summary Starts a stress testing task.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartBenchmarkTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StartBenchmarkTask',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/benchmark-tasks/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(task_name)}/start',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.StartBenchmarkTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_benchmark_task(
        self,
        cluster_id: str,
        task_name: str,
    ) -> eas_20210701_models.StartBenchmarkTaskResponse:
        """
        @summary Starts a stress testing task.
        
        @return: StartBenchmarkTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_benchmark_task_with_options(cluster_id, task_name, headers, runtime)

    async def start_benchmark_task_async(
        self,
        cluster_id: str,
        task_name: str,
    ) -> eas_20210701_models.StartBenchmarkTaskResponse:
        """
        @summary Starts a stress testing task.
        
        @return: StartBenchmarkTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.start_benchmark_task_with_options_async(cluster_id, task_name, headers, runtime)

    def start_service_with_options(
        self,
        cluster_id: str,
        service_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.StartServiceResponse:
        """
        @summary Starts a service.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartServiceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StartService',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/start',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.StartServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_service_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.StartServiceResponse:
        """
        @summary Starts a service.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartServiceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StartService',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/start',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.StartServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_service(
        self,
        cluster_id: str,
        service_name: str,
    ) -> eas_20210701_models.StartServiceResponse:
        """
        @summary Starts a service.
        
        @return: StartServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_service_with_options(cluster_id, service_name, headers, runtime)

    async def start_service_async(
        self,
        cluster_id: str,
        service_name: str,
    ) -> eas_20210701_models.StartServiceResponse:
        """
        @summary Starts a service.
        
        @return: StartServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.start_service_with_options_async(cluster_id, service_name, headers, runtime)

    def stop_benchmark_task_with_options(
        self,
        cluster_id: str,
        task_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.StopBenchmarkTaskResponse:
        """
        @summary Stops a stress testing task.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopBenchmarkTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopBenchmarkTask',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/benchmark-tasks/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(task_name)}/stop',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.StopBenchmarkTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_benchmark_task_with_options_async(
        self,
        cluster_id: str,
        task_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.StopBenchmarkTaskResponse:
        """
        @summary Stops a stress testing task.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopBenchmarkTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopBenchmarkTask',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/benchmark-tasks/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(task_name)}/stop',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.StopBenchmarkTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_benchmark_task(
        self,
        cluster_id: str,
        task_name: str,
    ) -> eas_20210701_models.StopBenchmarkTaskResponse:
        """
        @summary Stops a stress testing task.
        
        @return: StopBenchmarkTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_benchmark_task_with_options(cluster_id, task_name, headers, runtime)

    async def stop_benchmark_task_async(
        self,
        cluster_id: str,
        task_name: str,
    ) -> eas_20210701_models.StopBenchmarkTaskResponse:
        """
        @summary Stops a stress testing task.
        
        @return: StopBenchmarkTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.stop_benchmark_task_with_options_async(cluster_id, task_name, headers, runtime)

    def stop_service_with_options(
        self,
        cluster_id: str,
        service_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.StopServiceResponse:
        """
        @summary Stops a running service.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopServiceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopService',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/stop',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.StopServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_service_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.StopServiceResponse:
        """
        @summary Stops a running service.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopServiceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopService',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/stop',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.StopServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_service(
        self,
        cluster_id: str,
        service_name: str,
    ) -> eas_20210701_models.StopServiceResponse:
        """
        @summary Stops a running service.
        
        @return: StopServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_service_with_options(cluster_id, service_name, headers, runtime)

    async def stop_service_async(
        self,
        cluster_id: str,
        service_name: str,
    ) -> eas_20210701_models.StopServiceResponse:
        """
        @summary Stops a running service.
        
        @return: StopServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.stop_service_with_options_async(cluster_id, service_name, headers, runtime)

    def update_app_service_with_options(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.UpdateAppServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.UpdateAppServiceResponse:
        """
        @summary Updates an application service.
        
        @param request: UpdateAppServiceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAppServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.quota_id):
            query['QuotaId'] = request.quota_id
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.app_type):
            body['AppType'] = request.app_type
        if not UtilClient.is_unset(request.app_version):
            body['AppVersion'] = request.app_version
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        if not UtilClient.is_unset(request.replicas):
            body['Replicas'] = request.replicas
        if not UtilClient.is_unset(request.service_spec):
            body['ServiceSpec'] = request.service_spec
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAppService',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/app_services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.UpdateAppServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_app_service_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.UpdateAppServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.UpdateAppServiceResponse:
        """
        @summary Updates an application service.
        
        @param request: UpdateAppServiceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAppServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.quota_id):
            query['QuotaId'] = request.quota_id
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.app_type):
            body['AppType'] = request.app_type
        if not UtilClient.is_unset(request.app_version):
            body['AppVersion'] = request.app_version
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        if not UtilClient.is_unset(request.replicas):
            body['Replicas'] = request.replicas
        if not UtilClient.is_unset(request.service_spec):
            body['ServiceSpec'] = request.service_spec
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAppService',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/app_services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.UpdateAppServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_app_service(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.UpdateAppServiceRequest,
    ) -> eas_20210701_models.UpdateAppServiceResponse:
        """
        @summary Updates an application service.
        
        @param request: UpdateAppServiceRequest
        @return: UpdateAppServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_app_service_with_options(cluster_id, service_name, request, headers, runtime)

    async def update_app_service_async(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.UpdateAppServiceRequest,
    ) -> eas_20210701_models.UpdateAppServiceResponse:
        """
        @summary Updates an application service.
        
        @param request: UpdateAppServiceRequest
        @return: UpdateAppServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_app_service_with_options_async(cluster_id, service_name, request, headers, runtime)

    def update_benchmark_task_with_options(
        self,
        cluster_id: str,
        task_name: str,
        request: eas_20210701_models.UpdateBenchmarkTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.UpdateBenchmarkTaskResponse:
        """
        @summary Updates a stress testing task.
        
        @param request: UpdateBenchmarkTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateBenchmarkTaskResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='UpdateBenchmarkTask',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/benchmark-tasks/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(task_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.UpdateBenchmarkTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_benchmark_task_with_options_async(
        self,
        cluster_id: str,
        task_name: str,
        request: eas_20210701_models.UpdateBenchmarkTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.UpdateBenchmarkTaskResponse:
        """
        @summary Updates a stress testing task.
        
        @param request: UpdateBenchmarkTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateBenchmarkTaskResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='UpdateBenchmarkTask',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/benchmark-tasks/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(task_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.UpdateBenchmarkTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_benchmark_task(
        self,
        cluster_id: str,
        task_name: str,
        request: eas_20210701_models.UpdateBenchmarkTaskRequest,
    ) -> eas_20210701_models.UpdateBenchmarkTaskResponse:
        """
        @summary Updates a stress testing task.
        
        @param request: UpdateBenchmarkTaskRequest
        @return: UpdateBenchmarkTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_benchmark_task_with_options(cluster_id, task_name, request, headers, runtime)

    async def update_benchmark_task_async(
        self,
        cluster_id: str,
        task_name: str,
        request: eas_20210701_models.UpdateBenchmarkTaskRequest,
    ) -> eas_20210701_models.UpdateBenchmarkTaskResponse:
        """
        @summary Updates a stress testing task.
        
        @param request: UpdateBenchmarkTaskRequest
        @return: UpdateBenchmarkTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_benchmark_task_with_options_async(cluster_id, task_name, request, headers, runtime)

    def update_gateway_with_options(
        self,
        gateway_id: str,
        cluster_id: str,
        request: eas_20210701_models.UpdateGatewayRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.UpdateGatewayResponse:
        """
        @summary Update a private gateway.
        
        @param request: UpdateGatewayRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateGatewayResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.enable_internet):
            body['EnableInternet'] = request.enable_internet
        if not UtilClient.is_unset(request.enable_intranet):
            body['EnableIntranet'] = request.enable_intranet
        if not UtilClient.is_unset(request.instance_type):
            body['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.is_default):
            body['IsDefault'] = request.is_default
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.replicas):
            body['Replicas'] = request.replicas
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateGateway',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/gateways/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(gateway_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.UpdateGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_gateway_with_options_async(
        self,
        gateway_id: str,
        cluster_id: str,
        request: eas_20210701_models.UpdateGatewayRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.UpdateGatewayResponse:
        """
        @summary Update a private gateway.
        
        @param request: UpdateGatewayRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateGatewayResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.enable_internet):
            body['EnableInternet'] = request.enable_internet
        if not UtilClient.is_unset(request.enable_intranet):
            body['EnableIntranet'] = request.enable_intranet
        if not UtilClient.is_unset(request.instance_type):
            body['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.is_default):
            body['IsDefault'] = request.is_default
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.replicas):
            body['Replicas'] = request.replicas
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateGateway',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/gateways/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(gateway_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.UpdateGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_gateway(
        self,
        gateway_id: str,
        cluster_id: str,
        request: eas_20210701_models.UpdateGatewayRequest,
    ) -> eas_20210701_models.UpdateGatewayResponse:
        """
        @summary Update a private gateway.
        
        @param request: UpdateGatewayRequest
        @return: UpdateGatewayResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_gateway_with_options(gateway_id, cluster_id, request, headers, runtime)

    async def update_gateway_async(
        self,
        gateway_id: str,
        cluster_id: str,
        request: eas_20210701_models.UpdateGatewayRequest,
    ) -> eas_20210701_models.UpdateGatewayResponse:
        """
        @summary Update a private gateway.
        
        @param request: UpdateGatewayRequest
        @return: UpdateGatewayResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_gateway_with_options_async(gateway_id, cluster_id, request, headers, runtime)

    def update_resource_with_options(
        self,
        cluster_id: str,
        resource_id: str,
        request: eas_20210701_models.UpdateResourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.UpdateResourceResponse:
        """
        @summary Updates the information about a dedicated resource group. Only the name of a dedicated resource group can be updated.
        
        @param request: UpdateResourceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateResourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.resource_name):
            body['ResourceName'] = request.resource_name
        if not UtilClient.is_unset(request.self_managed_resource_options):
            body['SelfManagedResourceOptions'] = request.self_managed_resource_options
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateResource',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/resources/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(resource_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.UpdateResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_resource_with_options_async(
        self,
        cluster_id: str,
        resource_id: str,
        request: eas_20210701_models.UpdateResourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.UpdateResourceResponse:
        """
        @summary Updates the information about a dedicated resource group. Only the name of a dedicated resource group can be updated.
        
        @param request: UpdateResourceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateResourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.resource_name):
            body['ResourceName'] = request.resource_name
        if not UtilClient.is_unset(request.self_managed_resource_options):
            body['SelfManagedResourceOptions'] = request.self_managed_resource_options
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateResource',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/resources/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(resource_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.UpdateResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_resource(
        self,
        cluster_id: str,
        resource_id: str,
        request: eas_20210701_models.UpdateResourceRequest,
    ) -> eas_20210701_models.UpdateResourceResponse:
        """
        @summary Updates the information about a dedicated resource group. Only the name of a dedicated resource group can be updated.
        
        @param request: UpdateResourceRequest
        @return: UpdateResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_resource_with_options(cluster_id, resource_id, request, headers, runtime)

    async def update_resource_async(
        self,
        cluster_id: str,
        resource_id: str,
        request: eas_20210701_models.UpdateResourceRequest,
    ) -> eas_20210701_models.UpdateResourceResponse:
        """
        @summary Updates the information about a dedicated resource group. Only the name of a dedicated resource group can be updated.
        
        @param request: UpdateResourceRequest
        @return: UpdateResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_resource_with_options_async(cluster_id, resource_id, request, headers, runtime)

    def update_resource_dlink_with_options(
        self,
        cluster_id: str,
        resource_id: str,
        request: eas_20210701_models.UpdateResourceDLinkRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.UpdateResourceDLinkResponse:
        """
        @summary Updates the configurations of a virtual private cloud (VPC) direct connection for a dedicated resource group.
        
        @param request: UpdateResourceDLinkRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateResourceDLinkResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.destination_cidrs):
            body['DestinationCIDRs'] = request.destination_cidrs
        if not UtilClient.is_unset(request.security_group_id):
            body['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.v_switch_id):
            body['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.v_switch_id_list):
            body['VSwitchIdList'] = request.v_switch_id_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateResourceDLink',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/resources/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(resource_id)}/dlink',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.UpdateResourceDLinkResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_resource_dlink_with_options_async(
        self,
        cluster_id: str,
        resource_id: str,
        request: eas_20210701_models.UpdateResourceDLinkRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.UpdateResourceDLinkResponse:
        """
        @summary Updates the configurations of a virtual private cloud (VPC) direct connection for a dedicated resource group.
        
        @param request: UpdateResourceDLinkRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateResourceDLinkResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.destination_cidrs):
            body['DestinationCIDRs'] = request.destination_cidrs
        if not UtilClient.is_unset(request.security_group_id):
            body['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.v_switch_id):
            body['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.v_switch_id_list):
            body['VSwitchIdList'] = request.v_switch_id_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateResourceDLink',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/resources/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(resource_id)}/dlink',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.UpdateResourceDLinkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_resource_dlink(
        self,
        cluster_id: str,
        resource_id: str,
        request: eas_20210701_models.UpdateResourceDLinkRequest,
    ) -> eas_20210701_models.UpdateResourceDLinkResponse:
        """
        @summary Updates the configurations of a virtual private cloud (VPC) direct connection for a dedicated resource group.
        
        @param request: UpdateResourceDLinkRequest
        @return: UpdateResourceDLinkResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_resource_dlink_with_options(cluster_id, resource_id, request, headers, runtime)

    async def update_resource_dlink_async(
        self,
        cluster_id: str,
        resource_id: str,
        request: eas_20210701_models.UpdateResourceDLinkRequest,
    ) -> eas_20210701_models.UpdateResourceDLinkResponse:
        """
        @summary Updates the configurations of a virtual private cloud (VPC) direct connection for a dedicated resource group.
        
        @param request: UpdateResourceDLinkRequest
        @return: UpdateResourceDLinkResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_resource_dlink_with_options_async(cluster_id, resource_id, request, headers, runtime)

    def update_resource_instance_with_options(
        self,
        cluster_id: str,
        resource_id: str,
        instance_id: str,
        request: eas_20210701_models.UpdateResourceInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.UpdateResourceInstanceResponse:
        """
        @summary Updates the service scheduling status of an instance in a dedicated resource group.
        
        @param request: UpdateResourceInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateResourceInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.action):
            body['Action'] = request.action
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateResourceInstance',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/resources/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(resource_id)}/instances/{OpenApiUtilClient.get_encode_param(instance_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.UpdateResourceInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_resource_instance_with_options_async(
        self,
        cluster_id: str,
        resource_id: str,
        instance_id: str,
        request: eas_20210701_models.UpdateResourceInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.UpdateResourceInstanceResponse:
        """
        @summary Updates the service scheduling status of an instance in a dedicated resource group.
        
        @param request: UpdateResourceInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateResourceInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.action):
            body['Action'] = request.action
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateResourceInstance',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/resources/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(resource_id)}/instances/{OpenApiUtilClient.get_encode_param(instance_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.UpdateResourceInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_resource_instance(
        self,
        cluster_id: str,
        resource_id: str,
        instance_id: str,
        request: eas_20210701_models.UpdateResourceInstanceRequest,
    ) -> eas_20210701_models.UpdateResourceInstanceResponse:
        """
        @summary Updates the service scheduling status of an instance in a dedicated resource group.
        
        @param request: UpdateResourceInstanceRequest
        @return: UpdateResourceInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_resource_instance_with_options(cluster_id, resource_id, instance_id, request, headers, runtime)

    async def update_resource_instance_async(
        self,
        cluster_id: str,
        resource_id: str,
        instance_id: str,
        request: eas_20210701_models.UpdateResourceInstanceRequest,
    ) -> eas_20210701_models.UpdateResourceInstanceResponse:
        """
        @summary Updates the service scheduling status of an instance in a dedicated resource group.
        
        @param request: UpdateResourceInstanceRequest
        @return: UpdateResourceInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_resource_instance_with_options_async(cluster_id, resource_id, instance_id, request, headers, runtime)

    def update_service_with_options(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.UpdateServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.UpdateServiceResponse:
        """
        @summary Updates a model or processor of a service. If only the metadata.instance field is updated, manual scaling can be performed.
        
        @param request: UpdateServiceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.update_type):
            query['UpdateType'] = request.update_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='UpdateService',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.UpdateServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_service_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.UpdateServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.UpdateServiceResponse:
        """
        @summary Updates a model or processor of a service. If only the metadata.instance field is updated, manual scaling can be performed.
        
        @param request: UpdateServiceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.update_type):
            query['UpdateType'] = request.update_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='UpdateService',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.UpdateServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_service(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.UpdateServiceRequest,
    ) -> eas_20210701_models.UpdateServiceResponse:
        """
        @summary Updates a model or processor of a service. If only the metadata.instance field is updated, manual scaling can be performed.
        
        @param request: UpdateServiceRequest
        @return: UpdateServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_service_with_options(cluster_id, service_name, request, headers, runtime)

    async def update_service_async(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.UpdateServiceRequest,
    ) -> eas_20210701_models.UpdateServiceResponse:
        """
        @summary Updates a model or processor of a service. If only the metadata.instance field is updated, manual scaling can be performed.
        
        @param request: UpdateServiceRequest
        @return: UpdateServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_service_with_options_async(cluster_id, service_name, request, headers, runtime)

    def update_service_auto_scaler_with_options(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.UpdateServiceAutoScalerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.UpdateServiceAutoScalerResponse:
        """
        @summary Updates the Autoscaler configurations of a service.
        
        @param request: UpdateServiceAutoScalerRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateServiceAutoScalerResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.behavior):
            body['behavior'] = request.behavior
        if not UtilClient.is_unset(request.max):
            body['max'] = request.max
        if not UtilClient.is_unset(request.min):
            body['min'] = request.min
        if not UtilClient.is_unset(request.scale_strategies):
            body['scaleStrategies'] = request.scale_strategies
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateServiceAutoScaler',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/autoscaler',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.UpdateServiceAutoScalerResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_service_auto_scaler_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.UpdateServiceAutoScalerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.UpdateServiceAutoScalerResponse:
        """
        @summary Updates the Autoscaler configurations of a service.
        
        @param request: UpdateServiceAutoScalerRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateServiceAutoScalerResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.behavior):
            body['behavior'] = request.behavior
        if not UtilClient.is_unset(request.max):
            body['max'] = request.max
        if not UtilClient.is_unset(request.min):
            body['min'] = request.min
        if not UtilClient.is_unset(request.scale_strategies):
            body['scaleStrategies'] = request.scale_strategies
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateServiceAutoScaler',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/autoscaler',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.UpdateServiceAutoScalerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_service_auto_scaler(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.UpdateServiceAutoScalerRequest,
    ) -> eas_20210701_models.UpdateServiceAutoScalerResponse:
        """
        @summary Updates the Autoscaler configurations of a service.
        
        @param request: UpdateServiceAutoScalerRequest
        @return: UpdateServiceAutoScalerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_service_auto_scaler_with_options(cluster_id, service_name, request, headers, runtime)

    async def update_service_auto_scaler_async(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.UpdateServiceAutoScalerRequest,
    ) -> eas_20210701_models.UpdateServiceAutoScalerResponse:
        """
        @summary Updates the Autoscaler configurations of a service.
        
        @param request: UpdateServiceAutoScalerRequest
        @return: UpdateServiceAutoScalerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_service_auto_scaler_with_options_async(cluster_id, service_name, request, headers, runtime)

    def update_service_cron_scaler_with_options(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.UpdateServiceCronScalerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.UpdateServiceCronScalerResponse:
        """
        @summary Updates the Cron Horizontal Pod Autoscaler (CronHPA) settings of a service.
        
        @param request: UpdateServiceCronScalerRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateServiceCronScalerResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.exclude_dates):
            body['ExcludeDates'] = request.exclude_dates
        if not UtilClient.is_unset(request.scale_jobs):
            body['ScaleJobs'] = request.scale_jobs
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateServiceCronScaler',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/cronscaler',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.UpdateServiceCronScalerResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_service_cron_scaler_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.UpdateServiceCronScalerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.UpdateServiceCronScalerResponse:
        """
        @summary Updates the Cron Horizontal Pod Autoscaler (CronHPA) settings of a service.
        
        @param request: UpdateServiceCronScalerRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateServiceCronScalerResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.exclude_dates):
            body['ExcludeDates'] = request.exclude_dates
        if not UtilClient.is_unset(request.scale_jobs):
            body['ScaleJobs'] = request.scale_jobs
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateServiceCronScaler',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/cronscaler',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.UpdateServiceCronScalerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_service_cron_scaler(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.UpdateServiceCronScalerRequest,
    ) -> eas_20210701_models.UpdateServiceCronScalerResponse:
        """
        @summary Updates the Cron Horizontal Pod Autoscaler (CronHPA) settings of a service.
        
        @param request: UpdateServiceCronScalerRequest
        @return: UpdateServiceCronScalerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_service_cron_scaler_with_options(cluster_id, service_name, request, headers, runtime)

    async def update_service_cron_scaler_async(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.UpdateServiceCronScalerRequest,
    ) -> eas_20210701_models.UpdateServiceCronScalerResponse:
        """
        @summary Updates the Cron Horizontal Pod Autoscaler (CronHPA) settings of a service.
        
        @param request: UpdateServiceCronScalerRequest
        @return: UpdateServiceCronScalerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_service_cron_scaler_with_options_async(cluster_id, service_name, request, headers, runtime)

    def update_service_instance_with_options(
        self,
        cluster_id: str,
        service_name: str,
        instance_name: str,
        request: eas_20210701_models.UpdateServiceInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.UpdateServiceInstanceResponse:
        """
        @summary Updates attributes of service instances. Only isolation can be performed for service instances.
        
        @param request: UpdateServiceInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateServiceInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.isolate):
            body['Isolate'] = request.isolate
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateServiceInstance',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/instances/{OpenApiUtilClient.get_encode_param(instance_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.UpdateServiceInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_service_instance_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        instance_name: str,
        request: eas_20210701_models.UpdateServiceInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.UpdateServiceInstanceResponse:
        """
        @summary Updates attributes of service instances. Only isolation can be performed for service instances.
        
        @param request: UpdateServiceInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateServiceInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.isolate):
            body['Isolate'] = request.isolate
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateServiceInstance',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/instances/{OpenApiUtilClient.get_encode_param(instance_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.UpdateServiceInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_service_instance(
        self,
        cluster_id: str,
        service_name: str,
        instance_name: str,
        request: eas_20210701_models.UpdateServiceInstanceRequest,
    ) -> eas_20210701_models.UpdateServiceInstanceResponse:
        """
        @summary Updates attributes of service instances. Only isolation can be performed for service instances.
        
        @param request: UpdateServiceInstanceRequest
        @return: UpdateServiceInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_service_instance_with_options(cluster_id, service_name, instance_name, request, headers, runtime)

    async def update_service_instance_async(
        self,
        cluster_id: str,
        service_name: str,
        instance_name: str,
        request: eas_20210701_models.UpdateServiceInstanceRequest,
    ) -> eas_20210701_models.UpdateServiceInstanceResponse:
        """
        @summary Updates attributes of service instances. Only isolation can be performed for service instances.
        
        @param request: UpdateServiceInstanceRequest
        @return: UpdateServiceInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_service_instance_with_options_async(cluster_id, service_name, instance_name, request, headers, runtime)

    def update_service_label_with_options(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.UpdateServiceLabelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.UpdateServiceLabelResponse:
        """
        @summary Adds service tags or updates existing service tags.
        
        @param request: UpdateServiceLabelRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateServiceLabelResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateServiceLabel',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/label',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.UpdateServiceLabelResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_service_label_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.UpdateServiceLabelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.UpdateServiceLabelResponse:
        """
        @summary Adds service tags or updates existing service tags.
        
        @param request: UpdateServiceLabelRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateServiceLabelResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateServiceLabel',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/label',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.UpdateServiceLabelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_service_label(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.UpdateServiceLabelRequest,
    ) -> eas_20210701_models.UpdateServiceLabelResponse:
        """
        @summary Adds service tags or updates existing service tags.
        
        @param request: UpdateServiceLabelRequest
        @return: UpdateServiceLabelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_service_label_with_options(cluster_id, service_name, request, headers, runtime)

    async def update_service_label_async(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.UpdateServiceLabelRequest,
    ) -> eas_20210701_models.UpdateServiceLabelResponse:
        """
        @summary Adds service tags or updates existing service tags.
        
        @param request: UpdateServiceLabelRequest
        @return: UpdateServiceLabelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_service_label_with_options_async(cluster_id, service_name, request, headers, runtime)

    def update_service_mirror_with_options(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.UpdateServiceMirrorRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.UpdateServiceMirrorResponse:
        """
        @summary Updates the traffic mirroring configurations of a service.
        
        @param request: UpdateServiceMirrorRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateServiceMirrorResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ratio):
            body['Ratio'] = request.ratio
        if not UtilClient.is_unset(request.target):
            body['Target'] = request.target
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateServiceMirror',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/mirror',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.UpdateServiceMirrorResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_service_mirror_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.UpdateServiceMirrorRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.UpdateServiceMirrorResponse:
        """
        @summary Updates the traffic mirroring configurations of a service.
        
        @param request: UpdateServiceMirrorRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateServiceMirrorResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ratio):
            body['Ratio'] = request.ratio
        if not UtilClient.is_unset(request.target):
            body['Target'] = request.target
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateServiceMirror',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/mirror',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.UpdateServiceMirrorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_service_mirror(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.UpdateServiceMirrorRequest,
    ) -> eas_20210701_models.UpdateServiceMirrorResponse:
        """
        @summary Updates the traffic mirroring configurations of a service.
        
        @param request: UpdateServiceMirrorRequest
        @return: UpdateServiceMirrorResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_service_mirror_with_options(cluster_id, service_name, request, headers, runtime)

    async def update_service_mirror_async(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.UpdateServiceMirrorRequest,
    ) -> eas_20210701_models.UpdateServiceMirrorResponse:
        """
        @summary Updates the traffic mirroring configurations of a service.
        
        @param request: UpdateServiceMirrorRequest
        @return: UpdateServiceMirrorResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_service_mirror_with_options_async(cluster_id, service_name, request, headers, runtime)

    def update_service_safety_lock_with_options(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.UpdateServiceSafetyLockRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.UpdateServiceSafetyLockResponse:
        """
        @summary Updates the safety lock of a service to minimize misoperations on the service.
        
        @param request: UpdateServiceSafetyLockRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateServiceSafetyLockResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lock):
            body['Lock'] = request.lock
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateServiceSafetyLock',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/lock',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.UpdateServiceSafetyLockResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_service_safety_lock_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.UpdateServiceSafetyLockRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.UpdateServiceSafetyLockResponse:
        """
        @summary Updates the safety lock of a service to minimize misoperations on the service.
        
        @param request: UpdateServiceSafetyLockRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateServiceSafetyLockResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lock):
            body['Lock'] = request.lock
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateServiceSafetyLock',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/lock',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.UpdateServiceSafetyLockResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_service_safety_lock(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.UpdateServiceSafetyLockRequest,
    ) -> eas_20210701_models.UpdateServiceSafetyLockResponse:
        """
        @summary Updates the safety lock of a service to minimize misoperations on the service.
        
        @param request: UpdateServiceSafetyLockRequest
        @return: UpdateServiceSafetyLockResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_service_safety_lock_with_options(cluster_id, service_name, request, headers, runtime)

    async def update_service_safety_lock_async(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.UpdateServiceSafetyLockRequest,
    ) -> eas_20210701_models.UpdateServiceSafetyLockResponse:
        """
        @summary Updates the safety lock of a service to minimize misoperations on the service.
        
        @param request: UpdateServiceSafetyLockRequest
        @return: UpdateServiceSafetyLockResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_service_safety_lock_with_options_async(cluster_id, service_name, request, headers, runtime)

    def update_service_version_with_options(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.UpdateServiceVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.UpdateServiceVersionResponse:
        """
        @summary Updates the version of a service or rolls back the service to a specific version.
        
        @param request: UpdateServiceVersionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateServiceVersionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateServiceVersion',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/version',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.UpdateServiceVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_service_version_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.UpdateServiceVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eas_20210701_models.UpdateServiceVersionResponse:
        """
        @summary Updates the version of a service or rolls back the service to a specific version.
        
        @param request: UpdateServiceVersionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateServiceVersionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateServiceVersion',
            version='2021-07-01',
            protocol='HTTPS',
            pathname=f'/api/v2/services/{OpenApiUtilClient.get_encode_param(cluster_id)}/{OpenApiUtilClient.get_encode_param(service_name)}/version',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.UpdateServiceVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_service_version(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.UpdateServiceVersionRequest,
    ) -> eas_20210701_models.UpdateServiceVersionResponse:
        """
        @summary Updates the version of a service or rolls back the service to a specific version.
        
        @param request: UpdateServiceVersionRequest
        @return: UpdateServiceVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_service_version_with_options(cluster_id, service_name, request, headers, runtime)

    async def update_service_version_async(
        self,
        cluster_id: str,
        service_name: str,
        request: eas_20210701_models.UpdateServiceVersionRequest,
    ) -> eas_20210701_models.UpdateServiceVersionResponse:
        """
        @summary Updates the version of a service or rolls back the service to a specific version.
        
        @param request: UpdateServiceVersionRequest
        @return: UpdateServiceVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_service_version_with_options_async(cluster_id, service_name, request, headers, runtime)
