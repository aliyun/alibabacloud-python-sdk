# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_eas20210701 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
from darabonba.runtime import RuntimeOptions
from darabonba.url import Url as DaraURL

"""
"""
class Client(OpenApiClient):

    def __init__(
        self,
        config: open_api_util_models.Config,
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
        if not DaraCore.is_null(endpoint):
            return endpoint
        if not DaraCore.is_null(endpoint_map) and not DaraCore.is_null(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return Utils.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def attach_gateway_domain_with_options(
        self,
        cluster_id: str,
        gateway_id: str,
        tmp_req: main_models.AttachGatewayDomainRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AttachGatewayDomainResponse:
        tmp_req.validate()
        request = main_models.AttachGatewayDomainShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.custom_domain):
            request.custom_domain_shrink = Utils.array_to_string_with_specified_style(tmp_req.custom_domain, 'CustomDomain', 'json')
        query = {}
        if not DaraCore.is_null(request.custom_domain_shrink):
            query['CustomDomain'] = request.custom_domain_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachGatewayDomain',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/gateways/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(gateway_id)}/domain/attach',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachGatewayDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_gateway_domain_with_options_async(
        self,
        cluster_id: str,
        gateway_id: str,
        tmp_req: main_models.AttachGatewayDomainRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AttachGatewayDomainResponse:
        tmp_req.validate()
        request = main_models.AttachGatewayDomainShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.custom_domain):
            request.custom_domain_shrink = Utils.array_to_string_with_specified_style(tmp_req.custom_domain, 'CustomDomain', 'json')
        query = {}
        if not DaraCore.is_null(request.custom_domain_shrink):
            query['CustomDomain'] = request.custom_domain_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachGatewayDomain',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/gateways/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(gateway_id)}/domain/attach',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachGatewayDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_gateway_domain(
        self,
        cluster_id: str,
        gateway_id: str,
        request: main_models.AttachGatewayDomainRequest,
    ) -> main_models.AttachGatewayDomainResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.attach_gateway_domain_with_options(cluster_id, gateway_id, request, headers, runtime)

    async def attach_gateway_domain_async(
        self,
        cluster_id: str,
        gateway_id: str,
        request: main_models.AttachGatewayDomainRequest,
    ) -> main_models.AttachGatewayDomainResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.attach_gateway_domain_with_options_async(cluster_id, gateway_id, request, headers, runtime)

    def clone_service_with_options(
        self,
        cluster_id: str,
        service_name: str,
        tmp_req: main_models.CloneServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CloneServiceResponse:
        tmp_req.validate()
        request = main_models.CloneServiceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.labels):
            request.labels_shrink = Utils.array_to_string_with_specified_style(tmp_req.labels, 'Labels', 'json')
        query = {}
        if not DaraCore.is_null(request.labels_shrink):
            query['Labels'] = request.labels_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'CloneService',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}/clone',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CloneServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def clone_service_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        tmp_req: main_models.CloneServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CloneServiceResponse:
        tmp_req.validate()
        request = main_models.CloneServiceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.labels):
            request.labels_shrink = Utils.array_to_string_with_specified_style(tmp_req.labels, 'Labels', 'json')
        query = {}
        if not DaraCore.is_null(request.labels_shrink):
            query['Labels'] = request.labels_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'CloneService',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}/clone',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CloneServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def clone_service(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.CloneServiceRequest,
    ) -> main_models.CloneServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.clone_service_with_options(cluster_id, service_name, request, headers, runtime)

    async def clone_service_async(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.CloneServiceRequest,
    ) -> main_models.CloneServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.clone_service_with_options_async(cluster_id, service_name, request, headers, runtime)

    def commit_service_with_options(
        self,
        cluster_id: str,
        service_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CommitServiceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'CommitService',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}/commit',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CommitServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def commit_service_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CommitServiceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'CommitService',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}/commit',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CommitServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def commit_service(
        self,
        cluster_id: str,
        service_name: str,
    ) -> main_models.CommitServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.commit_service_with_options(cluster_id, service_name, headers, runtime)

    async def commit_service_async(
        self,
        cluster_id: str,
        service_name: str,
    ) -> main_models.CommitServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.commit_service_with_options_async(cluster_id, service_name, headers, runtime)

    def create_acl_policy_with_options(
        self,
        cluster_id: str,
        gateway_id: str,
        tmp_req: main_models.CreateAclPolicyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAclPolicyResponse:
        tmp_req.validate()
        request = main_models.CreateAclPolicyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.acl_policy_list):
            request.acl_policy_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.acl_policy_list, 'AclPolicyList', 'json')
        query = {}
        if not DaraCore.is_null(request.acl_policy_list_shrink):
            query['AclPolicyList'] = request.acl_policy_list_shrink
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAclPolicy',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/gateways/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(gateway_id)}/acl_policy',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAclPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_acl_policy_with_options_async(
        self,
        cluster_id: str,
        gateway_id: str,
        tmp_req: main_models.CreateAclPolicyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAclPolicyResponse:
        tmp_req.validate()
        request = main_models.CreateAclPolicyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.acl_policy_list):
            request.acl_policy_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.acl_policy_list, 'AclPolicyList', 'json')
        query = {}
        if not DaraCore.is_null(request.acl_policy_list_shrink):
            query['AclPolicyList'] = request.acl_policy_list_shrink
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAclPolicy',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/gateways/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(gateway_id)}/acl_policy',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAclPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_acl_policy(
        self,
        cluster_id: str,
        gateway_id: str,
        request: main_models.CreateAclPolicyRequest,
    ) -> main_models.CreateAclPolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_acl_policy_with_options(cluster_id, gateway_id, request, headers, runtime)

    async def create_acl_policy_async(
        self,
        cluster_id: str,
        gateway_id: str,
        request: main_models.CreateAclPolicyRequest,
    ) -> main_models.CreateAclPolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_acl_policy_with_options_async(cluster_id, gateway_id, request, headers, runtime)

    def create_app_service_with_options(
        self,
        request: main_models.CreateAppServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAppServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.quota_id):
            query['QuotaId'] = request.quota_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not DaraCore.is_null(request.app_type):
            body['AppType'] = request.app_type
        if not DaraCore.is_null(request.app_version):
            body['AppVersion'] = request.app_version
        if not DaraCore.is_null(request.config):
            body['Config'] = request.config
        if not DaraCore.is_null(request.replicas):
            body['Replicas'] = request.replicas
        if not DaraCore.is_null(request.service_name):
            body['ServiceName'] = request.service_name
        if not DaraCore.is_null(request.service_spec):
            body['ServiceSpec'] = request.service_spec
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAppService',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/app_services',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAppServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_app_service_with_options_async(
        self,
        request: main_models.CreateAppServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAppServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.quota_id):
            query['QuotaId'] = request.quota_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not DaraCore.is_null(request.app_type):
            body['AppType'] = request.app_type
        if not DaraCore.is_null(request.app_version):
            body['AppVersion'] = request.app_version
        if not DaraCore.is_null(request.config):
            body['Config'] = request.config
        if not DaraCore.is_null(request.replicas):
            body['Replicas'] = request.replicas
        if not DaraCore.is_null(request.service_name):
            body['ServiceName'] = request.service_name
        if not DaraCore.is_null(request.service_spec):
            body['ServiceSpec'] = request.service_spec
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAppService',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/app_services',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAppServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_app_service(
        self,
        request: main_models.CreateAppServiceRequest,
    ) -> main_models.CreateAppServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_app_service_with_options(request, headers, runtime)

    async def create_app_service_async(
        self,
        request: main_models.CreateAppServiceRequest,
    ) -> main_models.CreateAppServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_app_service_with_options_async(request, headers, runtime)

    def create_benchmark_task_with_options(
        self,
        request: main_models.CreateBenchmarkTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateBenchmarkTaskResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'CreateBenchmarkTask',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/benchmark-tasks',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBenchmarkTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_benchmark_task_with_options_async(
        self,
        request: main_models.CreateBenchmarkTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateBenchmarkTaskResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'CreateBenchmarkTask',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/benchmark-tasks',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBenchmarkTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_benchmark_task(
        self,
        request: main_models.CreateBenchmarkTaskRequest,
    ) -> main_models.CreateBenchmarkTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_benchmark_task_with_options(request, headers, runtime)

    async def create_benchmark_task_async(
        self,
        request: main_models.CreateBenchmarkTaskRequest,
    ) -> main_models.CreateBenchmarkTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_benchmark_task_with_options_async(request, headers, runtime)

    def create_fault_injection_with_options(
        self,
        cluster_id: str,
        service_name: str,
        instance_name: str,
        request: main_models.CreateFaultInjectionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateFaultInjectionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.fault_args):
            body['FaultArgs'] = request.fault_args
        if not DaraCore.is_null(request.fault_type):
            body['FaultType'] = request.fault_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateFaultInjection',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}/instances/{DaraURL.percent_encode(instance_name)}/faults',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFaultInjectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_fault_injection_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        instance_name: str,
        request: main_models.CreateFaultInjectionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateFaultInjectionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.fault_args):
            body['FaultArgs'] = request.fault_args
        if not DaraCore.is_null(request.fault_type):
            body['FaultType'] = request.fault_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateFaultInjection',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}/instances/{DaraURL.percent_encode(instance_name)}/faults',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFaultInjectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_fault_injection(
        self,
        cluster_id: str,
        service_name: str,
        instance_name: str,
        request: main_models.CreateFaultInjectionRequest,
    ) -> main_models.CreateFaultInjectionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_fault_injection_with_options(cluster_id, service_name, instance_name, request, headers, runtime)

    async def create_fault_injection_async(
        self,
        cluster_id: str,
        service_name: str,
        instance_name: str,
        request: main_models.CreateFaultInjectionRequest,
    ) -> main_models.CreateFaultInjectionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_fault_injection_with_options_async(cluster_id, service_name, instance_name, request, headers, runtime)

    def create_gateway_with_options(
        self,
        request: main_models.CreateGatewayRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateGatewayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_name):
            query['ResourceName'] = request.resource_name
        body = {}
        if not DaraCore.is_null(request.auto_renewal):
            body['AutoRenewal'] = request.auto_renewal
        if not DaraCore.is_null(request.charge_type):
            body['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.enable_internet):
            body['EnableInternet'] = request.enable_internet
        if not DaraCore.is_null(request.enable_intranet):
            body['EnableIntranet'] = request.enable_intranet
        if not DaraCore.is_null(request.gateway_type):
            body['GatewayType'] = request.gateway_type
        if not DaraCore.is_null(request.instance_type):
            body['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.replicas):
            body['Replicas'] = request.replicas
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateGateway',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/gateways',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_gateway_with_options_async(
        self,
        request: main_models.CreateGatewayRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateGatewayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_name):
            query['ResourceName'] = request.resource_name
        body = {}
        if not DaraCore.is_null(request.auto_renewal):
            body['AutoRenewal'] = request.auto_renewal
        if not DaraCore.is_null(request.charge_type):
            body['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.enable_internet):
            body['EnableInternet'] = request.enable_internet
        if not DaraCore.is_null(request.enable_intranet):
            body['EnableIntranet'] = request.enable_intranet
        if not DaraCore.is_null(request.gateway_type):
            body['GatewayType'] = request.gateway_type
        if not DaraCore.is_null(request.instance_type):
            body['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.replicas):
            body['Replicas'] = request.replicas
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateGateway',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/gateways',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_gateway(
        self,
        request: main_models.CreateGatewayRequest,
    ) -> main_models.CreateGatewayResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_gateway_with_options(request, headers, runtime)

    async def create_gateway_async(
        self,
        request: main_models.CreateGatewayRequest,
    ) -> main_models.CreateGatewayResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_gateway_with_options_async(request, headers, runtime)

    def create_gateway_intranet_linked_vpc_with_options(
        self,
        cluster_id: str,
        gateway_id: str,
        request: main_models.CreateGatewayIntranetLinkedVpcRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateGatewayIntranetLinkedVpcResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.enable_authoritative_dns):
            query['EnableAuthoritativeDns'] = request.enable_authoritative_dns
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateGatewayIntranetLinkedVpc',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/gateways/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(gateway_id)}/intranet_endpoint_linked_vpc',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateGatewayIntranetLinkedVpcResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_gateway_intranet_linked_vpc_with_options_async(
        self,
        cluster_id: str,
        gateway_id: str,
        request: main_models.CreateGatewayIntranetLinkedVpcRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateGatewayIntranetLinkedVpcResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.enable_authoritative_dns):
            query['EnableAuthoritativeDns'] = request.enable_authoritative_dns
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateGatewayIntranetLinkedVpc',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/gateways/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(gateway_id)}/intranet_endpoint_linked_vpc',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateGatewayIntranetLinkedVpcResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_gateway_intranet_linked_vpc(
        self,
        cluster_id: str,
        gateway_id: str,
        request: main_models.CreateGatewayIntranetLinkedVpcRequest,
    ) -> main_models.CreateGatewayIntranetLinkedVpcResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_gateway_intranet_linked_vpc_with_options(cluster_id, gateway_id, request, headers, runtime)

    async def create_gateway_intranet_linked_vpc_async(
        self,
        cluster_id: str,
        gateway_id: str,
        request: main_models.CreateGatewayIntranetLinkedVpcRequest,
    ) -> main_models.CreateGatewayIntranetLinkedVpcResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_gateway_intranet_linked_vpc_with_options_async(cluster_id, gateway_id, request, headers, runtime)

    def create_gateway_intranet_linked_vpc_peer_with_options(
        self,
        cluster_id: str,
        gateway_id: str,
        tmp_req: main_models.CreateGatewayIntranetLinkedVpcPeerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateGatewayIntranetLinkedVpcPeerResponse:
        tmp_req.validate()
        request = main_models.CreateGatewayIntranetLinkedVpcPeerShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.peer_vpcs):
            request.peer_vpcs_shrink = Utils.array_to_string_with_specified_style(tmp_req.peer_vpcs, 'PeerVpcs', 'json')
        query = {}
        if not DaraCore.is_null(request.peer_vpcs_shrink):
            query['PeerVpcs'] = request.peer_vpcs_shrink
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateGatewayIntranetLinkedVpcPeer',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/gateways/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(gateway_id)}/intranet_endpoint_linked_vpc_peer',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateGatewayIntranetLinkedVpcPeerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_gateway_intranet_linked_vpc_peer_with_options_async(
        self,
        cluster_id: str,
        gateway_id: str,
        tmp_req: main_models.CreateGatewayIntranetLinkedVpcPeerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateGatewayIntranetLinkedVpcPeerResponse:
        tmp_req.validate()
        request = main_models.CreateGatewayIntranetLinkedVpcPeerShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.peer_vpcs):
            request.peer_vpcs_shrink = Utils.array_to_string_with_specified_style(tmp_req.peer_vpcs, 'PeerVpcs', 'json')
        query = {}
        if not DaraCore.is_null(request.peer_vpcs_shrink):
            query['PeerVpcs'] = request.peer_vpcs_shrink
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateGatewayIntranetLinkedVpcPeer',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/gateways/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(gateway_id)}/intranet_endpoint_linked_vpc_peer',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateGatewayIntranetLinkedVpcPeerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_gateway_intranet_linked_vpc_peer(
        self,
        cluster_id: str,
        gateway_id: str,
        request: main_models.CreateGatewayIntranetLinkedVpcPeerRequest,
    ) -> main_models.CreateGatewayIntranetLinkedVpcPeerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_gateway_intranet_linked_vpc_peer_with_options(cluster_id, gateway_id, request, headers, runtime)

    async def create_gateway_intranet_linked_vpc_peer_async(
        self,
        cluster_id: str,
        gateway_id: str,
        request: main_models.CreateGatewayIntranetLinkedVpcPeerRequest,
    ) -> main_models.CreateGatewayIntranetLinkedVpcPeerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_gateway_intranet_linked_vpc_peer_with_options_async(cluster_id, gateway_id, request, headers, runtime)

    def create_resource_with_options(
        self,
        request: main_models.CreateResourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateResourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auto_renewal):
            body['AutoRenewal'] = request.auto_renewal
        if not DaraCore.is_null(request.charge_type):
            body['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.ecs_instance_count):
            body['EcsInstanceCount'] = request.ecs_instance_count
        if not DaraCore.is_null(request.ecs_instance_type):
            body['EcsInstanceType'] = request.ecs_instance_type
        if not DaraCore.is_null(request.labels):
            body['Labels'] = request.labels
        if not DaraCore.is_null(request.resource_name):
            body['ResourceName'] = request.resource_name
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.self_managed_resource_options):
            body['SelfManagedResourceOptions'] = request.self_managed_resource_options
        if not DaraCore.is_null(request.system_disk_size):
            body['SystemDiskSize'] = request.system_disk_size
        if not DaraCore.is_null(request.zone):
            body['Zone'] = request.zone
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateResource',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/resources',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_resource_with_options_async(
        self,
        request: main_models.CreateResourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateResourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auto_renewal):
            body['AutoRenewal'] = request.auto_renewal
        if not DaraCore.is_null(request.charge_type):
            body['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.ecs_instance_count):
            body['EcsInstanceCount'] = request.ecs_instance_count
        if not DaraCore.is_null(request.ecs_instance_type):
            body['EcsInstanceType'] = request.ecs_instance_type
        if not DaraCore.is_null(request.labels):
            body['Labels'] = request.labels
        if not DaraCore.is_null(request.resource_name):
            body['ResourceName'] = request.resource_name
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.self_managed_resource_options):
            body['SelfManagedResourceOptions'] = request.self_managed_resource_options
        if not DaraCore.is_null(request.system_disk_size):
            body['SystemDiskSize'] = request.system_disk_size
        if not DaraCore.is_null(request.zone):
            body['Zone'] = request.zone
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateResource',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/resources',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_resource(
        self,
        request: main_models.CreateResourceRequest,
    ) -> main_models.CreateResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_resource_with_options(request, headers, runtime)

    async def create_resource_async(
        self,
        request: main_models.CreateResourceRequest,
    ) -> main_models.CreateResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_resource_with_options_async(request, headers, runtime)

    def create_resource_instances_with_options(
        self,
        cluster_id: str,
        resource_id: str,
        request: main_models.CreateResourceInstancesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateResourceInstancesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auto_renewal):
            body['AutoRenewal'] = request.auto_renewal
        if not DaraCore.is_null(request.charge_type):
            body['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.ecs_instance_count):
            body['EcsInstanceCount'] = request.ecs_instance_count
        if not DaraCore.is_null(request.ecs_instance_type):
            body['EcsInstanceType'] = request.ecs_instance_type
        if not DaraCore.is_null(request.labels):
            body['Labels'] = request.labels
        if not DaraCore.is_null(request.system_disk_size):
            body['SystemDiskSize'] = request.system_disk_size
        if not DaraCore.is_null(request.user_data):
            body['UserData'] = request.user_data
        if not DaraCore.is_null(request.zone):
            body['Zone'] = request.zone
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateResourceInstances',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/resources/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(resource_id)}/instances',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateResourceInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_resource_instances_with_options_async(
        self,
        cluster_id: str,
        resource_id: str,
        request: main_models.CreateResourceInstancesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateResourceInstancesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auto_renewal):
            body['AutoRenewal'] = request.auto_renewal
        if not DaraCore.is_null(request.charge_type):
            body['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.ecs_instance_count):
            body['EcsInstanceCount'] = request.ecs_instance_count
        if not DaraCore.is_null(request.ecs_instance_type):
            body['EcsInstanceType'] = request.ecs_instance_type
        if not DaraCore.is_null(request.labels):
            body['Labels'] = request.labels
        if not DaraCore.is_null(request.system_disk_size):
            body['SystemDiskSize'] = request.system_disk_size
        if not DaraCore.is_null(request.user_data):
            body['UserData'] = request.user_data
        if not DaraCore.is_null(request.zone):
            body['Zone'] = request.zone
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateResourceInstances',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/resources/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(resource_id)}/instances',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateResourceInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_resource_instances(
        self,
        cluster_id: str,
        resource_id: str,
        request: main_models.CreateResourceInstancesRequest,
    ) -> main_models.CreateResourceInstancesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_resource_instances_with_options(cluster_id, resource_id, request, headers, runtime)

    async def create_resource_instances_async(
        self,
        cluster_id: str,
        resource_id: str,
        request: main_models.CreateResourceInstancesRequest,
    ) -> main_models.CreateResourceInstancesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_resource_instances_with_options_async(cluster_id, resource_id, request, headers, runtime)

    def create_resource_log_with_options(
        self,
        cluster_id: str,
        resource_id: str,
        request: main_models.CreateResourceLogRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateResourceLogResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.log_store):
            body['LogStore'] = request.log_store
        if not DaraCore.is_null(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateResourceLog',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/resources/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(resource_id)}/log',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateResourceLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_resource_log_with_options_async(
        self,
        cluster_id: str,
        resource_id: str,
        request: main_models.CreateResourceLogRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateResourceLogResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.log_store):
            body['LogStore'] = request.log_store
        if not DaraCore.is_null(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateResourceLog',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/resources/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(resource_id)}/log',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateResourceLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_resource_log(
        self,
        cluster_id: str,
        resource_id: str,
        request: main_models.CreateResourceLogRequest,
    ) -> main_models.CreateResourceLogResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_resource_log_with_options(cluster_id, resource_id, request, headers, runtime)

    async def create_resource_log_async(
        self,
        cluster_id: str,
        resource_id: str,
        request: main_models.CreateResourceLogRequest,
    ) -> main_models.CreateResourceLogResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_resource_log_with_options_async(cluster_id, resource_id, request, headers, runtime)

    def create_service_with_options(
        self,
        tmp_req: main_models.CreateServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateServiceResponse:
        tmp_req.validate()
        request = main_models.CreateServiceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.labels):
            request.labels_shrink = Utils.array_to_string_with_specified_style(tmp_req.labels, 'Labels', 'json')
        query = {}
        if not DaraCore.is_null(request.develop):
            query['Develop'] = request.develop
        if not DaraCore.is_null(request.labels_shrink):
            query['Labels'] = request.labels_shrink
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'CreateService',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_service_with_options_async(
        self,
        tmp_req: main_models.CreateServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateServiceResponse:
        tmp_req.validate()
        request = main_models.CreateServiceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.labels):
            request.labels_shrink = Utils.array_to_string_with_specified_style(tmp_req.labels, 'Labels', 'json')
        query = {}
        if not DaraCore.is_null(request.develop):
            query['Develop'] = request.develop
        if not DaraCore.is_null(request.labels_shrink):
            query['Labels'] = request.labels_shrink
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'CreateService',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_service(
        self,
        request: main_models.CreateServiceRequest,
    ) -> main_models.CreateServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_service_with_options(request, headers, runtime)

    async def create_service_async(
        self,
        request: main_models.CreateServiceRequest,
    ) -> main_models.CreateServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_service_with_options_async(request, headers, runtime)

    def create_service_auto_scaler_with_options(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.CreateServiceAutoScalerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateServiceAutoScalerResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.behavior):
            body['behavior'] = request.behavior
        if not DaraCore.is_null(request.max):
            body['max'] = request.max
        if not DaraCore.is_null(request.min):
            body['min'] = request.min
        if not DaraCore.is_null(request.scale_strategies):
            body['scaleStrategies'] = request.scale_strategies
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateServiceAutoScaler',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}/autoscaler',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateServiceAutoScalerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_service_auto_scaler_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.CreateServiceAutoScalerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateServiceAutoScalerResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.behavior):
            body['behavior'] = request.behavior
        if not DaraCore.is_null(request.max):
            body['max'] = request.max
        if not DaraCore.is_null(request.min):
            body['min'] = request.min
        if not DaraCore.is_null(request.scale_strategies):
            body['scaleStrategies'] = request.scale_strategies
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateServiceAutoScaler',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}/autoscaler',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateServiceAutoScalerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_service_auto_scaler(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.CreateServiceAutoScalerRequest,
    ) -> main_models.CreateServiceAutoScalerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_service_auto_scaler_with_options(cluster_id, service_name, request, headers, runtime)

    async def create_service_auto_scaler_async(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.CreateServiceAutoScalerRequest,
    ) -> main_models.CreateServiceAutoScalerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_service_auto_scaler_with_options_async(cluster_id, service_name, request, headers, runtime)

    def create_service_cron_scaler_with_options(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.CreateServiceCronScalerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateServiceCronScalerResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.exclude_dates):
            body['ExcludeDates'] = request.exclude_dates
        if not DaraCore.is_null(request.scale_jobs):
            body['ScaleJobs'] = request.scale_jobs
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateServiceCronScaler',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}/cronscaler',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateServiceCronScalerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_service_cron_scaler_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.CreateServiceCronScalerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateServiceCronScalerResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.exclude_dates):
            body['ExcludeDates'] = request.exclude_dates
        if not DaraCore.is_null(request.scale_jobs):
            body['ScaleJobs'] = request.scale_jobs
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateServiceCronScaler',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}/cronscaler',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateServiceCronScalerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_service_cron_scaler(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.CreateServiceCronScalerRequest,
    ) -> main_models.CreateServiceCronScalerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_service_cron_scaler_with_options(cluster_id, service_name, request, headers, runtime)

    async def create_service_cron_scaler_async(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.CreateServiceCronScalerRequest,
    ) -> main_models.CreateServiceCronScalerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_service_cron_scaler_with_options_async(cluster_id, service_name, request, headers, runtime)

    def create_service_mirror_with_options(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.CreateServiceMirrorRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateServiceMirrorResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.ratio):
            body['Ratio'] = request.ratio
        if not DaraCore.is_null(request.target):
            body['Target'] = request.target
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateServiceMirror',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}/mirror',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateServiceMirrorResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_service_mirror_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.CreateServiceMirrorRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateServiceMirrorResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.ratio):
            body['Ratio'] = request.ratio
        if not DaraCore.is_null(request.target):
            body['Target'] = request.target
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateServiceMirror',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}/mirror',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateServiceMirrorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_service_mirror(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.CreateServiceMirrorRequest,
    ) -> main_models.CreateServiceMirrorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_service_mirror_with_options(cluster_id, service_name, request, headers, runtime)

    async def create_service_mirror_async(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.CreateServiceMirrorRequest,
    ) -> main_models.CreateServiceMirrorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_service_mirror_with_options_async(cluster_id, service_name, request, headers, runtime)

    def create_virtual_resource_with_options(
        self,
        request: main_models.CreateVirtualResourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateVirtualResourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.disable_spot_protection_period):
            body['DisableSpotProtectionPeriod'] = request.disable_spot_protection_period
        if not DaraCore.is_null(request.resources):
            body['Resources'] = request.resources
        if not DaraCore.is_null(request.virtual_resource_name):
            body['VirtualResourceName'] = request.virtual_resource_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateVirtualResource',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/virtualresources',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVirtualResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_virtual_resource_with_options_async(
        self,
        request: main_models.CreateVirtualResourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateVirtualResourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.disable_spot_protection_period):
            body['DisableSpotProtectionPeriod'] = request.disable_spot_protection_period
        if not DaraCore.is_null(request.resources):
            body['Resources'] = request.resources
        if not DaraCore.is_null(request.virtual_resource_name):
            body['VirtualResourceName'] = request.virtual_resource_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateVirtualResource',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/virtualresources',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVirtualResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_virtual_resource(
        self,
        request: main_models.CreateVirtualResourceRequest,
    ) -> main_models.CreateVirtualResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_virtual_resource_with_options(request, headers, runtime)

    async def create_virtual_resource_async(
        self,
        request: main_models.CreateVirtualResourceRequest,
    ) -> main_models.CreateVirtualResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_virtual_resource_with_options_async(request, headers, runtime)

    def delete_acl_policy_with_options(
        self,
        cluster_id: str,
        gateway_id: str,
        tmp_req: main_models.DeleteAclPolicyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAclPolicyResponse:
        tmp_req.validate()
        request = main_models.DeleteAclPolicyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.acl_policy_list):
            request.acl_policy_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.acl_policy_list, 'AclPolicyList', 'json')
        query = {}
        if not DaraCore.is_null(request.acl_policy_list_shrink):
            query['AclPolicyList'] = request.acl_policy_list_shrink
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAclPolicy',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/gateways/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(gateway_id)}/acl_policy',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAclPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_acl_policy_with_options_async(
        self,
        cluster_id: str,
        gateway_id: str,
        tmp_req: main_models.DeleteAclPolicyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAclPolicyResponse:
        tmp_req.validate()
        request = main_models.DeleteAclPolicyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.acl_policy_list):
            request.acl_policy_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.acl_policy_list, 'AclPolicyList', 'json')
        query = {}
        if not DaraCore.is_null(request.acl_policy_list_shrink):
            query['AclPolicyList'] = request.acl_policy_list_shrink
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAclPolicy',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/gateways/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(gateway_id)}/acl_policy',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAclPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_acl_policy(
        self,
        cluster_id: str,
        gateway_id: str,
        request: main_models.DeleteAclPolicyRequest,
    ) -> main_models.DeleteAclPolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_acl_policy_with_options(cluster_id, gateway_id, request, headers, runtime)

    async def delete_acl_policy_async(
        self,
        cluster_id: str,
        gateway_id: str,
        request: main_models.DeleteAclPolicyRequest,
    ) -> main_models.DeleteAclPolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_acl_policy_with_options_async(cluster_id, gateway_id, request, headers, runtime)

    def delete_benchmark_task_with_options(
        self,
        cluster_id: str,
        task_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBenchmarkTaskResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteBenchmarkTask',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/benchmark-tasks/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(task_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBenchmarkTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_benchmark_task_with_options_async(
        self,
        cluster_id: str,
        task_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBenchmarkTaskResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteBenchmarkTask',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/benchmark-tasks/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(task_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBenchmarkTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_benchmark_task(
        self,
        cluster_id: str,
        task_name: str,
    ) -> main_models.DeleteBenchmarkTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_benchmark_task_with_options(cluster_id, task_name, headers, runtime)

    async def delete_benchmark_task_async(
        self,
        cluster_id: str,
        task_name: str,
    ) -> main_models.DeleteBenchmarkTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_benchmark_task_with_options_async(cluster_id, task_name, headers, runtime)

    def delete_fault_injection_with_options(
        self,
        cluster_id: str,
        service_name: str,
        instance_name: str,
        fault_type: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFaultInjectionResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteFaultInjection',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}/instances/{DaraURL.percent_encode(instance_name)}/faults/{DaraURL.percent_encode(fault_type)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFaultInjectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_fault_injection_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        instance_name: str,
        fault_type: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFaultInjectionResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteFaultInjection',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}/instances/{DaraURL.percent_encode(instance_name)}/faults/{DaraURL.percent_encode(fault_type)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFaultInjectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_fault_injection(
        self,
        cluster_id: str,
        service_name: str,
        instance_name: str,
        fault_type: str,
    ) -> main_models.DeleteFaultInjectionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_fault_injection_with_options(cluster_id, service_name, instance_name, fault_type, headers, runtime)

    async def delete_fault_injection_async(
        self,
        cluster_id: str,
        service_name: str,
        instance_name: str,
        fault_type: str,
    ) -> main_models.DeleteFaultInjectionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_fault_injection_with_options_async(cluster_id, service_name, instance_name, fault_type, headers, runtime)

    def delete_gateway_with_options(
        self,
        cluster_id: str,
        gateway_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGatewayResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteGateway',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/gateways/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(gateway_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_gateway_with_options_async(
        self,
        cluster_id: str,
        gateway_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGatewayResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteGateway',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/gateways/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(gateway_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_gateway(
        self,
        cluster_id: str,
        gateway_id: str,
    ) -> main_models.DeleteGatewayResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_gateway_with_options(cluster_id, gateway_id, headers, runtime)

    async def delete_gateway_async(
        self,
        cluster_id: str,
        gateway_id: str,
    ) -> main_models.DeleteGatewayResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_gateway_with_options_async(cluster_id, gateway_id, headers, runtime)

    def delete_gateway_intranet_linked_vpc_with_options(
        self,
        cluster_id: str,
        gateway_id: str,
        request: main_models.DeleteGatewayIntranetLinkedVpcRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGatewayIntranetLinkedVpcResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGatewayIntranetLinkedVpc',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/gateways/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(gateway_id)}/intranet_endpoint_linked_vpc',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGatewayIntranetLinkedVpcResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_gateway_intranet_linked_vpc_with_options_async(
        self,
        cluster_id: str,
        gateway_id: str,
        request: main_models.DeleteGatewayIntranetLinkedVpcRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGatewayIntranetLinkedVpcResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGatewayIntranetLinkedVpc',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/gateways/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(gateway_id)}/intranet_endpoint_linked_vpc',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGatewayIntranetLinkedVpcResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_gateway_intranet_linked_vpc(
        self,
        cluster_id: str,
        gateway_id: str,
        request: main_models.DeleteGatewayIntranetLinkedVpcRequest,
    ) -> main_models.DeleteGatewayIntranetLinkedVpcResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_gateway_intranet_linked_vpc_with_options(cluster_id, gateway_id, request, headers, runtime)

    async def delete_gateway_intranet_linked_vpc_async(
        self,
        cluster_id: str,
        gateway_id: str,
        request: main_models.DeleteGatewayIntranetLinkedVpcRequest,
    ) -> main_models.DeleteGatewayIntranetLinkedVpcResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_gateway_intranet_linked_vpc_with_options_async(cluster_id, gateway_id, request, headers, runtime)

    def delete_gateway_intranet_linked_vpc_peer_with_options(
        self,
        cluster_id: str,
        gateway_id: str,
        tmp_req: main_models.DeleteGatewayIntranetLinkedVpcPeerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGatewayIntranetLinkedVpcPeerResponse:
        tmp_req.validate()
        request = main_models.DeleteGatewayIntranetLinkedVpcPeerShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.peer_vpcs):
            request.peer_vpcs_shrink = Utils.array_to_string_with_specified_style(tmp_req.peer_vpcs, 'PeerVpcs', 'json')
        query = {}
        if not DaraCore.is_null(request.peer_vpcs_shrink):
            query['PeerVpcs'] = request.peer_vpcs_shrink
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGatewayIntranetLinkedVpcPeer',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/gateways/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(gateway_id)}/intranet_endpoint_linked_vpc_peer',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGatewayIntranetLinkedVpcPeerResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_gateway_intranet_linked_vpc_peer_with_options_async(
        self,
        cluster_id: str,
        gateway_id: str,
        tmp_req: main_models.DeleteGatewayIntranetLinkedVpcPeerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGatewayIntranetLinkedVpcPeerResponse:
        tmp_req.validate()
        request = main_models.DeleteGatewayIntranetLinkedVpcPeerShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.peer_vpcs):
            request.peer_vpcs_shrink = Utils.array_to_string_with_specified_style(tmp_req.peer_vpcs, 'PeerVpcs', 'json')
        query = {}
        if not DaraCore.is_null(request.peer_vpcs_shrink):
            query['PeerVpcs'] = request.peer_vpcs_shrink
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGatewayIntranetLinkedVpcPeer',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/gateways/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(gateway_id)}/intranet_endpoint_linked_vpc_peer',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGatewayIntranetLinkedVpcPeerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_gateway_intranet_linked_vpc_peer(
        self,
        cluster_id: str,
        gateway_id: str,
        request: main_models.DeleteGatewayIntranetLinkedVpcPeerRequest,
    ) -> main_models.DeleteGatewayIntranetLinkedVpcPeerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_gateway_intranet_linked_vpc_peer_with_options(cluster_id, gateway_id, request, headers, runtime)

    async def delete_gateway_intranet_linked_vpc_peer_async(
        self,
        cluster_id: str,
        gateway_id: str,
        request: main_models.DeleteGatewayIntranetLinkedVpcPeerRequest,
    ) -> main_models.DeleteGatewayIntranetLinkedVpcPeerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_gateway_intranet_linked_vpc_peer_with_options_async(cluster_id, gateway_id, request, headers, runtime)

    def delete_gateway_label_with_options(
        self,
        cluster_id: str,
        gateway_id: str,
        tmp_req: main_models.DeleteGatewayLabelRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGatewayLabelResponse:
        tmp_req.validate()
        request = main_models.DeleteGatewayLabelShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.label_keys):
            request.label_keys_shrink = Utils.array_to_string_with_specified_style(tmp_req.label_keys, 'LabelKeys', 'json')
        query = {}
        if not DaraCore.is_null(request.label_keys_shrink):
            query['LabelKeys'] = request.label_keys_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGatewayLabel',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/gateways/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(gateway_id)}/label',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGatewayLabelResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_gateway_label_with_options_async(
        self,
        cluster_id: str,
        gateway_id: str,
        tmp_req: main_models.DeleteGatewayLabelRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGatewayLabelResponse:
        tmp_req.validate()
        request = main_models.DeleteGatewayLabelShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.label_keys):
            request.label_keys_shrink = Utils.array_to_string_with_specified_style(tmp_req.label_keys, 'LabelKeys', 'json')
        query = {}
        if not DaraCore.is_null(request.label_keys_shrink):
            query['LabelKeys'] = request.label_keys_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGatewayLabel',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/gateways/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(gateway_id)}/label',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGatewayLabelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_gateway_label(
        self,
        cluster_id: str,
        gateway_id: str,
        request: main_models.DeleteGatewayLabelRequest,
    ) -> main_models.DeleteGatewayLabelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_gateway_label_with_options(cluster_id, gateway_id, request, headers, runtime)

    async def delete_gateway_label_async(
        self,
        cluster_id: str,
        gateway_id: str,
        request: main_models.DeleteGatewayLabelRequest,
    ) -> main_models.DeleteGatewayLabelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_gateway_label_with_options_async(cluster_id, gateway_id, request, headers, runtime)

    def delete_resource_with_options(
        self,
        cluster_id: str,
        resource_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteResourceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteResource',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/resources/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(resource_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_resource_with_options_async(
        self,
        cluster_id: str,
        resource_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteResourceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteResource',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/resources/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(resource_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_resource(
        self,
        cluster_id: str,
        resource_id: str,
    ) -> main_models.DeleteResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_resource_with_options(cluster_id, resource_id, headers, runtime)

    async def delete_resource_async(
        self,
        cluster_id: str,
        resource_id: str,
    ) -> main_models.DeleteResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_resource_with_options_async(cluster_id, resource_id, headers, runtime)

    def delete_resource_dlink_with_options(
        self,
        cluster_id: str,
        resource_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteResourceDLinkResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteResourceDLink',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/resources/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(resource_id)}/dlink',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteResourceDLinkResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_resource_dlink_with_options_async(
        self,
        cluster_id: str,
        resource_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteResourceDLinkResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteResourceDLink',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/resources/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(resource_id)}/dlink',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteResourceDLinkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_resource_dlink(
        self,
        cluster_id: str,
        resource_id: str,
    ) -> main_models.DeleteResourceDLinkResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_resource_dlink_with_options(cluster_id, resource_id, headers, runtime)

    async def delete_resource_dlink_async(
        self,
        cluster_id: str,
        resource_id: str,
    ) -> main_models.DeleteResourceDLinkResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_resource_dlink_with_options_async(cluster_id, resource_id, headers, runtime)

    def delete_resource_instance_label_with_options(
        self,
        cluster_id: str,
        resource_id: str,
        tmp_req: main_models.DeleteResourceInstanceLabelRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteResourceInstanceLabelResponse:
        tmp_req.validate()
        request = main_models.DeleteResourceInstanceLabelShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.instance_ids):
            request.instance_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'simple')
        if not DaraCore.is_null(tmp_req.keys):
            request.keys_shrink = Utils.array_to_string_with_specified_style(tmp_req.keys, 'Keys', 'simple')
        if not DaraCore.is_null(tmp_req.label_keys):
            request.label_keys_shrink = Utils.array_to_string_with_specified_style(tmp_req.label_keys, 'LabelKeys', 'json')
        query = {}
        if not DaraCore.is_null(request.all_instances):
            query['AllInstances'] = request.all_instances
        if not DaraCore.is_null(request.instance_ids_shrink):
            query['InstanceIds'] = request.instance_ids_shrink
        if not DaraCore.is_null(request.keys_shrink):
            query['Keys'] = request.keys_shrink
        if not DaraCore.is_null(request.label_keys_shrink):
            query['LabelKeys'] = request.label_keys_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteResourceInstanceLabel',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/resources/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(resource_id)}/label',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteResourceInstanceLabelResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_resource_instance_label_with_options_async(
        self,
        cluster_id: str,
        resource_id: str,
        tmp_req: main_models.DeleteResourceInstanceLabelRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteResourceInstanceLabelResponse:
        tmp_req.validate()
        request = main_models.DeleteResourceInstanceLabelShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.instance_ids):
            request.instance_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'simple')
        if not DaraCore.is_null(tmp_req.keys):
            request.keys_shrink = Utils.array_to_string_with_specified_style(tmp_req.keys, 'Keys', 'simple')
        if not DaraCore.is_null(tmp_req.label_keys):
            request.label_keys_shrink = Utils.array_to_string_with_specified_style(tmp_req.label_keys, 'LabelKeys', 'json')
        query = {}
        if not DaraCore.is_null(request.all_instances):
            query['AllInstances'] = request.all_instances
        if not DaraCore.is_null(request.instance_ids_shrink):
            query['InstanceIds'] = request.instance_ids_shrink
        if not DaraCore.is_null(request.keys_shrink):
            query['Keys'] = request.keys_shrink
        if not DaraCore.is_null(request.label_keys_shrink):
            query['LabelKeys'] = request.label_keys_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteResourceInstanceLabel',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/resources/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(resource_id)}/label',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteResourceInstanceLabelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_resource_instance_label(
        self,
        cluster_id: str,
        resource_id: str,
        request: main_models.DeleteResourceInstanceLabelRequest,
    ) -> main_models.DeleteResourceInstanceLabelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_resource_instance_label_with_options(cluster_id, resource_id, request, headers, runtime)

    async def delete_resource_instance_label_async(
        self,
        cluster_id: str,
        resource_id: str,
        request: main_models.DeleteResourceInstanceLabelRequest,
    ) -> main_models.DeleteResourceInstanceLabelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_resource_instance_label_with_options_async(cluster_id, resource_id, request, headers, runtime)

    def delete_resource_instances_with_options(
        self,
        cluster_id: str,
        resource_id: str,
        request: main_models.DeleteResourceInstancesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteResourceInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all_failed):
            query['AllFailed'] = request.all_failed
        if not DaraCore.is_null(request.instance_list):
            query['InstanceList'] = request.instance_list
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteResourceInstances',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/resources/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(resource_id)}/instances',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteResourceInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_resource_instances_with_options_async(
        self,
        cluster_id: str,
        resource_id: str,
        request: main_models.DeleteResourceInstancesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteResourceInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all_failed):
            query['AllFailed'] = request.all_failed
        if not DaraCore.is_null(request.instance_list):
            query['InstanceList'] = request.instance_list
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteResourceInstances',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/resources/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(resource_id)}/instances',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteResourceInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_resource_instances(
        self,
        cluster_id: str,
        resource_id: str,
        request: main_models.DeleteResourceInstancesRequest,
    ) -> main_models.DeleteResourceInstancesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_resource_instances_with_options(cluster_id, resource_id, request, headers, runtime)

    async def delete_resource_instances_async(
        self,
        cluster_id: str,
        resource_id: str,
        request: main_models.DeleteResourceInstancesRequest,
    ) -> main_models.DeleteResourceInstancesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_resource_instances_with_options_async(cluster_id, resource_id, request, headers, runtime)

    def delete_resource_log_with_options(
        self,
        cluster_id: str,
        resource_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteResourceLogResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteResourceLog',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/resources/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(resource_id)}/log',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteResourceLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_resource_log_with_options_async(
        self,
        cluster_id: str,
        resource_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteResourceLogResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteResourceLog',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/resources/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(resource_id)}/log',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteResourceLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_resource_log(
        self,
        cluster_id: str,
        resource_id: str,
    ) -> main_models.DeleteResourceLogResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_resource_log_with_options(cluster_id, resource_id, headers, runtime)

    async def delete_resource_log_async(
        self,
        cluster_id: str,
        resource_id: str,
    ) -> main_models.DeleteResourceLogResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_resource_log_with_options_async(cluster_id, resource_id, headers, runtime)

    def delete_service_with_options(
        self,
        cluster_id: str,
        service_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteServiceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteService',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_service_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteServiceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteService',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_service(
        self,
        cluster_id: str,
        service_name: str,
    ) -> main_models.DeleteServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_service_with_options(cluster_id, service_name, headers, runtime)

    async def delete_service_async(
        self,
        cluster_id: str,
        service_name: str,
    ) -> main_models.DeleteServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_service_with_options_async(cluster_id, service_name, headers, runtime)

    def delete_service_auto_scaler_with_options(
        self,
        cluster_id: str,
        service_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteServiceAutoScalerResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteServiceAutoScaler',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}/autoscaler',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteServiceAutoScalerResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_service_auto_scaler_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteServiceAutoScalerResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteServiceAutoScaler',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}/autoscaler',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteServiceAutoScalerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_service_auto_scaler(
        self,
        cluster_id: str,
        service_name: str,
    ) -> main_models.DeleteServiceAutoScalerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_service_auto_scaler_with_options(cluster_id, service_name, headers, runtime)

    async def delete_service_auto_scaler_async(
        self,
        cluster_id: str,
        service_name: str,
    ) -> main_models.DeleteServiceAutoScalerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_service_auto_scaler_with_options_async(cluster_id, service_name, headers, runtime)

    def delete_service_cron_scaler_with_options(
        self,
        cluster_id: str,
        service_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteServiceCronScalerResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteServiceCronScaler',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}/cronscaler',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteServiceCronScalerResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_service_cron_scaler_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteServiceCronScalerResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteServiceCronScaler',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}/cronscaler',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteServiceCronScalerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_service_cron_scaler(
        self,
        cluster_id: str,
        service_name: str,
    ) -> main_models.DeleteServiceCronScalerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_service_cron_scaler_with_options(cluster_id, service_name, headers, runtime)

    async def delete_service_cron_scaler_async(
        self,
        cluster_id: str,
        service_name: str,
    ) -> main_models.DeleteServiceCronScalerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_service_cron_scaler_with_options_async(cluster_id, service_name, headers, runtime)

    def delete_service_instances_with_options(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.DeleteServiceInstancesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteServiceInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.container):
            query['Container'] = request.container
        if not DaraCore.is_null(request.instance_list):
            query['InstanceList'] = request.instance_list
        if not DaraCore.is_null(request.is_replica):
            query['IsReplica'] = request.is_replica
        if not DaraCore.is_null(request.soft_restart):
            query['SoftRestart'] = request.soft_restart
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteServiceInstances',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}/instances',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteServiceInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_service_instances_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.DeleteServiceInstancesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteServiceInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.container):
            query['Container'] = request.container
        if not DaraCore.is_null(request.instance_list):
            query['InstanceList'] = request.instance_list
        if not DaraCore.is_null(request.is_replica):
            query['IsReplica'] = request.is_replica
        if not DaraCore.is_null(request.soft_restart):
            query['SoftRestart'] = request.soft_restart
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteServiceInstances',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}/instances',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteServiceInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_service_instances(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.DeleteServiceInstancesRequest,
    ) -> main_models.DeleteServiceInstancesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_service_instances_with_options(cluster_id, service_name, request, headers, runtime)

    async def delete_service_instances_async(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.DeleteServiceInstancesRequest,
    ) -> main_models.DeleteServiceInstancesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_service_instances_with_options_async(cluster_id, service_name, request, headers, runtime)

    def delete_service_label_with_options(
        self,
        cluster_id: str,
        service_name: str,
        tmp_req: main_models.DeleteServiceLabelRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteServiceLabelResponse:
        tmp_req.validate()
        request = main_models.DeleteServiceLabelShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.keys):
            request.keys_shrink = Utils.array_to_string_with_specified_style(tmp_req.keys, 'Keys', 'simple')
        if not DaraCore.is_null(tmp_req.label_keys):
            request.label_keys_shrink = Utils.array_to_string_with_specified_style(tmp_req.label_keys, 'LabelKeys', 'json')
        query = {}
        if not DaraCore.is_null(request.keys_shrink):
            query['Keys'] = request.keys_shrink
        if not DaraCore.is_null(request.label_keys_shrink):
            query['LabelKeys'] = request.label_keys_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteServiceLabel',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}/label',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteServiceLabelResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_service_label_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        tmp_req: main_models.DeleteServiceLabelRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteServiceLabelResponse:
        tmp_req.validate()
        request = main_models.DeleteServiceLabelShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.keys):
            request.keys_shrink = Utils.array_to_string_with_specified_style(tmp_req.keys, 'Keys', 'simple')
        if not DaraCore.is_null(tmp_req.label_keys):
            request.label_keys_shrink = Utils.array_to_string_with_specified_style(tmp_req.label_keys, 'LabelKeys', 'json')
        query = {}
        if not DaraCore.is_null(request.keys_shrink):
            query['Keys'] = request.keys_shrink
        if not DaraCore.is_null(request.label_keys_shrink):
            query['LabelKeys'] = request.label_keys_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteServiceLabel',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}/label',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteServiceLabelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_service_label(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.DeleteServiceLabelRequest,
    ) -> main_models.DeleteServiceLabelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_service_label_with_options(cluster_id, service_name, request, headers, runtime)

    async def delete_service_label_async(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.DeleteServiceLabelRequest,
    ) -> main_models.DeleteServiceLabelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_service_label_with_options_async(cluster_id, service_name, request, headers, runtime)

    def delete_service_mirror_with_options(
        self,
        cluster_id: str,
        service_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteServiceMirrorResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteServiceMirror',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}/mirror',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteServiceMirrorResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_service_mirror_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteServiceMirrorResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteServiceMirror',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}/mirror',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteServiceMirrorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_service_mirror(
        self,
        cluster_id: str,
        service_name: str,
    ) -> main_models.DeleteServiceMirrorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_service_mirror_with_options(cluster_id, service_name, headers, runtime)

    async def delete_service_mirror_async(
        self,
        cluster_id: str,
        service_name: str,
    ) -> main_models.DeleteServiceMirrorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_service_mirror_with_options_async(cluster_id, service_name, headers, runtime)

    def delete_virtual_resource_with_options(
        self,
        cluster_id: str,
        virtual_resource_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteVirtualResourceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteVirtualResource',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/virtualresources/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(virtual_resource_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteVirtualResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_virtual_resource_with_options_async(
        self,
        cluster_id: str,
        virtual_resource_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteVirtualResourceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteVirtualResource',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/virtualresources/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(virtual_resource_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteVirtualResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_virtual_resource(
        self,
        cluster_id: str,
        virtual_resource_id: str,
    ) -> main_models.DeleteVirtualResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_virtual_resource_with_options(cluster_id, virtual_resource_id, headers, runtime)

    async def delete_virtual_resource_async(
        self,
        cluster_id: str,
        virtual_resource_id: str,
    ) -> main_models.DeleteVirtualResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_virtual_resource_with_options_async(cluster_id, virtual_resource_id, headers, runtime)

    def describe_benchmark_task_with_options(
        self,
        cluster_id: str,
        task_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBenchmarkTaskResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeBenchmarkTask',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/benchmark-tasks/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(task_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBenchmarkTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_benchmark_task_with_options_async(
        self,
        cluster_id: str,
        task_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBenchmarkTaskResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeBenchmarkTask',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/benchmark-tasks/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(task_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBenchmarkTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_benchmark_task(
        self,
        cluster_id: str,
        task_name: str,
    ) -> main_models.DescribeBenchmarkTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_benchmark_task_with_options(cluster_id, task_name, headers, runtime)

    async def describe_benchmark_task_async(
        self,
        cluster_id: str,
        task_name: str,
    ) -> main_models.DescribeBenchmarkTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_benchmark_task_with_options_async(cluster_id, task_name, headers, runtime)

    def describe_benchmark_task_report_with_options(
        self,
        cluster_id: str,
        task_name: str,
        request: main_models.DescribeBenchmarkTaskReportRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBenchmarkTaskReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.report_type):
            query['ReportType'] = request.report_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBenchmarkTaskReport',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/benchmark-tasks/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(task_name)}/report',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBenchmarkTaskReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_benchmark_task_report_with_options_async(
        self,
        cluster_id: str,
        task_name: str,
        request: main_models.DescribeBenchmarkTaskReportRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBenchmarkTaskReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.report_type):
            query['ReportType'] = request.report_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBenchmarkTaskReport',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/benchmark-tasks/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(task_name)}/report',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBenchmarkTaskReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_benchmark_task_report(
        self,
        cluster_id: str,
        task_name: str,
        request: main_models.DescribeBenchmarkTaskReportRequest,
    ) -> main_models.DescribeBenchmarkTaskReportResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_benchmark_task_report_with_options(cluster_id, task_name, request, headers, runtime)

    async def describe_benchmark_task_report_async(
        self,
        cluster_id: str,
        task_name: str,
        request: main_models.DescribeBenchmarkTaskReportRequest,
    ) -> main_models.DescribeBenchmarkTaskReportResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_benchmark_task_report_with_options_async(cluster_id, task_name, request, headers, runtime)

    def describe_gateway_with_options(
        self,
        cluster_id: str,
        gateway_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGatewayResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeGateway',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/gateways/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(gateway_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_gateway_with_options_async(
        self,
        cluster_id: str,
        gateway_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGatewayResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeGateway',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/gateways/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(gateway_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_gateway(
        self,
        cluster_id: str,
        gateway_id: str,
    ) -> main_models.DescribeGatewayResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_gateway_with_options(cluster_id, gateway_id, headers, runtime)

    async def describe_gateway_async(
        self,
        cluster_id: str,
        gateway_id: str,
    ) -> main_models.DescribeGatewayResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_gateway_with_options_async(cluster_id, gateway_id, headers, runtime)

    def describe_group_with_options(
        self,
        cluster_id: str,
        group_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGroupResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeGroup',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/groups/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(group_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_group_with_options_async(
        self,
        cluster_id: str,
        group_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGroupResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeGroup',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/groups/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(group_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_group(
        self,
        cluster_id: str,
        group_name: str,
    ) -> main_models.DescribeGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_group_with_options(cluster_id, group_name, headers, runtime)

    async def describe_group_async(
        self,
        cluster_id: str,
        group_name: str,
    ) -> main_models.DescribeGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_group_with_options_async(cluster_id, group_name, headers, runtime)

    def describe_group_endpoints_with_options(
        self,
        cluster_id: str,
        group_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGroupEndpointsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeGroupEndpoints',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/groups/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(group_name)}/endpoints',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGroupEndpointsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_group_endpoints_with_options_async(
        self,
        cluster_id: str,
        group_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGroupEndpointsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeGroupEndpoints',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/groups/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(group_name)}/endpoints',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGroupEndpointsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_group_endpoints(
        self,
        cluster_id: str,
        group_name: str,
    ) -> main_models.DescribeGroupEndpointsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_group_endpoints_with_options(cluster_id, group_name, headers, runtime)

    async def describe_group_endpoints_async(
        self,
        cluster_id: str,
        group_name: str,
    ) -> main_models.DescribeGroupEndpointsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_group_endpoints_with_options_async(cluster_id, group_name, headers, runtime)

    def describe_machine_spec_with_options(
        self,
        tmp_req: main_models.DescribeMachineSpecRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMachineSpecResponse:
        tmp_req.validate()
        request = main_models.DescribeMachineSpecShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.instance_types):
            request.instance_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.instance_types, 'InstanceTypes', 'simple')
        query = {}
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.instance_types_shrink):
            query['InstanceTypes'] = request.instance_types_shrink
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMachineSpec',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/public/instance_types',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMachineSpecResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_machine_spec_with_options_async(
        self,
        tmp_req: main_models.DescribeMachineSpecRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMachineSpecResponse:
        tmp_req.validate()
        request = main_models.DescribeMachineSpecShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.instance_types):
            request.instance_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.instance_types, 'InstanceTypes', 'simple')
        query = {}
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.instance_types_shrink):
            query['InstanceTypes'] = request.instance_types_shrink
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMachineSpec',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/public/instance_types',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMachineSpecResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_machine_spec(
        self,
        request: main_models.DescribeMachineSpecRequest,
    ) -> main_models.DescribeMachineSpecResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_machine_spec_with_options(request, headers, runtime)

    async def describe_machine_spec_async(
        self,
        request: main_models.DescribeMachineSpecRequest,
    ) -> main_models.DescribeMachineSpecResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_machine_spec_with_options_async(request, headers, runtime)

    def describe_regions_with_options(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/regions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/regions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(self) -> main_models.DescribeRegionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_regions_with_options(headers, runtime)

    async def describe_regions_async(self) -> main_models.DescribeRegionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_regions_with_options_async(headers, runtime)

    def describe_resource_with_options(
        self,
        cluster_id: str,
        resource_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeResourceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeResource',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/resources/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(resource_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_resource_with_options_async(
        self,
        cluster_id: str,
        resource_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeResourceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeResource',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/resources/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(resource_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_resource(
        self,
        cluster_id: str,
        resource_id: str,
    ) -> main_models.DescribeResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_resource_with_options(cluster_id, resource_id, headers, runtime)

    async def describe_resource_async(
        self,
        cluster_id: str,
        resource_id: str,
    ) -> main_models.DescribeResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_resource_with_options_async(cluster_id, resource_id, headers, runtime)

    def describe_resource_dlink_with_options(
        self,
        cluster_id: str,
        resource_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeResourceDLinkResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeResourceDLink',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/resources/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(resource_id)}/dlink',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeResourceDLinkResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_resource_dlink_with_options_async(
        self,
        cluster_id: str,
        resource_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeResourceDLinkResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeResourceDLink',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/resources/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(resource_id)}/dlink',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeResourceDLinkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_resource_dlink(
        self,
        cluster_id: str,
        resource_id: str,
    ) -> main_models.DescribeResourceDLinkResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_resource_dlink_with_options(cluster_id, resource_id, headers, runtime)

    async def describe_resource_dlink_async(
        self,
        cluster_id: str,
        resource_id: str,
    ) -> main_models.DescribeResourceDLinkResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_resource_dlink_with_options_async(cluster_id, resource_id, headers, runtime)

    def describe_resource_log_with_options(
        self,
        cluster_id: str,
        resource_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeResourceLogResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeResourceLog',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/resources/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(resource_id)}/log',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeResourceLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_resource_log_with_options_async(
        self,
        cluster_id: str,
        resource_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeResourceLogResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeResourceLog',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/resources/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(resource_id)}/log',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeResourceLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_resource_log(
        self,
        cluster_id: str,
        resource_id: str,
    ) -> main_models.DescribeResourceLogResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_resource_log_with_options(cluster_id, resource_id, headers, runtime)

    async def describe_resource_log_async(
        self,
        cluster_id: str,
        resource_id: str,
    ) -> main_models.DescribeResourceLogResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_resource_log_with_options_async(cluster_id, resource_id, headers, runtime)

    def describe_service_with_options(
        self,
        cluster_id: str,
        service_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeServiceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeService',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_service_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeServiceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeService',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_service(
        self,
        cluster_id: str,
        service_name: str,
    ) -> main_models.DescribeServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_service_with_options(cluster_id, service_name, headers, runtime)

    async def describe_service_async(
        self,
        cluster_id: str,
        service_name: str,
    ) -> main_models.DescribeServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_service_with_options_async(cluster_id, service_name, headers, runtime)

    def describe_service_auto_scaler_with_options(
        self,
        cluster_id: str,
        service_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeServiceAutoScalerResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeServiceAutoScaler',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}/autoscaler',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeServiceAutoScalerResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_service_auto_scaler_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeServiceAutoScalerResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeServiceAutoScaler',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}/autoscaler',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeServiceAutoScalerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_service_auto_scaler(
        self,
        cluster_id: str,
        service_name: str,
    ) -> main_models.DescribeServiceAutoScalerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_service_auto_scaler_with_options(cluster_id, service_name, headers, runtime)

    async def describe_service_auto_scaler_async(
        self,
        cluster_id: str,
        service_name: str,
    ) -> main_models.DescribeServiceAutoScalerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_service_auto_scaler_with_options_async(cluster_id, service_name, headers, runtime)

    def describe_service_cron_scaler_with_options(
        self,
        cluster_id: str,
        service_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeServiceCronScalerResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeServiceCronScaler',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}/cronscaler',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeServiceCronScalerResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_service_cron_scaler_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeServiceCronScalerResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeServiceCronScaler',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}/cronscaler',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeServiceCronScalerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_service_cron_scaler(
        self,
        cluster_id: str,
        service_name: str,
    ) -> main_models.DescribeServiceCronScalerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_service_cron_scaler_with_options(cluster_id, service_name, headers, runtime)

    async def describe_service_cron_scaler_async(
        self,
        cluster_id: str,
        service_name: str,
    ) -> main_models.DescribeServiceCronScalerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_service_cron_scaler_with_options_async(cluster_id, service_name, headers, runtime)

    def describe_service_diagnosis_with_options(
        self,
        cluster_id: str,
        service_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeServiceDiagnosisResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeServiceDiagnosis',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}/diagnosis',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeServiceDiagnosisResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_service_diagnosis_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeServiceDiagnosisResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeServiceDiagnosis',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}/diagnosis',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeServiceDiagnosisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_service_diagnosis(
        self,
        cluster_id: str,
        service_name: str,
    ) -> main_models.DescribeServiceDiagnosisResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_service_diagnosis_with_options(cluster_id, service_name, headers, runtime)

    async def describe_service_diagnosis_async(
        self,
        cluster_id: str,
        service_name: str,
    ) -> main_models.DescribeServiceDiagnosisResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_service_diagnosis_with_options_async(cluster_id, service_name, headers, runtime)

    def describe_service_endpoints_with_options(
        self,
        cluster_id: str,
        service_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeServiceEndpointsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeServiceEndpoints',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}/endpoints',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeServiceEndpointsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_service_endpoints_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeServiceEndpointsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeServiceEndpoints',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}/endpoints',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeServiceEndpointsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_service_endpoints(
        self,
        cluster_id: str,
        service_name: str,
    ) -> main_models.DescribeServiceEndpointsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_service_endpoints_with_options(cluster_id, service_name, headers, runtime)

    async def describe_service_endpoints_async(
        self,
        cluster_id: str,
        service_name: str,
    ) -> main_models.DescribeServiceEndpointsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_service_endpoints_with_options_async(cluster_id, service_name, headers, runtime)

    def describe_service_event_with_options(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.DescribeServiceEventRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeServiceEventResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.event_type):
            query['EventType'] = request.event_type
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeServiceEvent',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}/events',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeServiceEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_service_event_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.DescribeServiceEventRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeServiceEventResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.event_type):
            query['EventType'] = request.event_type
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeServiceEvent',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}/events',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeServiceEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_service_event(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.DescribeServiceEventRequest,
    ) -> main_models.DescribeServiceEventResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_service_event_with_options(cluster_id, service_name, request, headers, runtime)

    async def describe_service_event_async(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.DescribeServiceEventRequest,
    ) -> main_models.DescribeServiceEventResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_service_event_with_options_async(cluster_id, service_name, request, headers, runtime)

    def describe_service_instance_diagnosis_with_options(
        self,
        cluster_id: str,
        service_name: str,
        instance_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeServiceInstanceDiagnosisResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeServiceInstanceDiagnosis',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}/instances/{DaraURL.percent_encode(instance_name)}/diagnosis',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeServiceInstanceDiagnosisResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_service_instance_diagnosis_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        instance_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeServiceInstanceDiagnosisResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeServiceInstanceDiagnosis',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}/instances/{DaraURL.percent_encode(instance_name)}/diagnosis',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeServiceInstanceDiagnosisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_service_instance_diagnosis(
        self,
        cluster_id: str,
        service_name: str,
        instance_name: str,
    ) -> main_models.DescribeServiceInstanceDiagnosisResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_service_instance_diagnosis_with_options(cluster_id, service_name, instance_name, headers, runtime)

    async def describe_service_instance_diagnosis_async(
        self,
        cluster_id: str,
        service_name: str,
        instance_name: str,
    ) -> main_models.DescribeServiceInstanceDiagnosisResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_service_instance_diagnosis_with_options_async(cluster_id, service_name, instance_name, headers, runtime)

    def describe_service_log_with_options(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.DescribeServiceLogRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeServiceLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.container_name):
            query['ContainerName'] = request.container_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.previous):
            query['Previous'] = request.previous
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeServiceLog',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}/logs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeServiceLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_service_log_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.DescribeServiceLogRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeServiceLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.container_name):
            query['ContainerName'] = request.container_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.previous):
            query['Previous'] = request.previous
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeServiceLog',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}/logs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeServiceLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_service_log(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.DescribeServiceLogRequest,
    ) -> main_models.DescribeServiceLogResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_service_log_with_options(cluster_id, service_name, request, headers, runtime)

    async def describe_service_log_async(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.DescribeServiceLogRequest,
    ) -> main_models.DescribeServiceLogResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_service_log_with_options_async(cluster_id, service_name, request, headers, runtime)

    def describe_service_mirror_with_options(
        self,
        cluster_id: str,
        service_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeServiceMirrorResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeServiceMirror',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}/mirror',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeServiceMirrorResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_service_mirror_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeServiceMirrorResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeServiceMirror',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}/mirror',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeServiceMirrorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_service_mirror(
        self,
        cluster_id: str,
        service_name: str,
    ) -> main_models.DescribeServiceMirrorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_service_mirror_with_options(cluster_id, service_name, headers, runtime)

    async def describe_service_mirror_async(
        self,
        cluster_id: str,
        service_name: str,
    ) -> main_models.DescribeServiceMirrorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_service_mirror_with_options_async(cluster_id, service_name, headers, runtime)

    def describe_service_signed_url_with_options(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.DescribeServiceSignedUrlRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeServiceSignedUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.expire):
            query['Expire'] = request.expire
        if not DaraCore.is_null(request.internal):
            query['Internal'] = request.internal
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeServiceSignedUrl',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}/signed_url',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeServiceSignedUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_service_signed_url_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.DescribeServiceSignedUrlRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeServiceSignedUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.expire):
            query['Expire'] = request.expire
        if not DaraCore.is_null(request.internal):
            query['Internal'] = request.internal
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeServiceSignedUrl',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}/signed_url',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeServiceSignedUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_service_signed_url(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.DescribeServiceSignedUrlRequest,
    ) -> main_models.DescribeServiceSignedUrlResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_service_signed_url_with_options(cluster_id, service_name, request, headers, runtime)

    async def describe_service_signed_url_async(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.DescribeServiceSignedUrlRequest,
    ) -> main_models.DescribeServiceSignedUrlResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_service_signed_url_with_options_async(cluster_id, service_name, request, headers, runtime)

    def describe_spot_discount_history_with_options(
        self,
        request: main_models.DescribeSpotDiscountHistoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSpotDiscountHistoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.is_protect):
            query['IsProtect'] = request.is_protect
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSpotDiscountHistory',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/public/spot_discount',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSpotDiscountHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_spot_discount_history_with_options_async(
        self,
        request: main_models.DescribeSpotDiscountHistoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSpotDiscountHistoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.is_protect):
            query['IsProtect'] = request.is_protect
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSpotDiscountHistory',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/public/spot_discount',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSpotDiscountHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_spot_discount_history(
        self,
        request: main_models.DescribeSpotDiscountHistoryRequest,
    ) -> main_models.DescribeSpotDiscountHistoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_spot_discount_history_with_options(request, headers, runtime)

    async def describe_spot_discount_history_async(
        self,
        request: main_models.DescribeSpotDiscountHistoryRequest,
    ) -> main_models.DescribeSpotDiscountHistoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_spot_discount_history_with_options_async(request, headers, runtime)

    def describe_virtual_resource_with_options(
        self,
        cluster_id: str,
        virtual_resource_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVirtualResourceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeVirtualResource',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/virtualresources/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(virtual_resource_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVirtualResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_virtual_resource_with_options_async(
        self,
        cluster_id: str,
        virtual_resource_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVirtualResourceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeVirtualResource',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/virtualresources/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(virtual_resource_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVirtualResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_virtual_resource(
        self,
        cluster_id: str,
        virtual_resource_id: str,
    ) -> main_models.DescribeVirtualResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_virtual_resource_with_options(cluster_id, virtual_resource_id, headers, runtime)

    async def describe_virtual_resource_async(
        self,
        cluster_id: str,
        virtual_resource_id: str,
    ) -> main_models.DescribeVirtualResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_virtual_resource_with_options_async(cluster_id, virtual_resource_id, headers, runtime)

    def detach_gateway_domain_with_options(
        self,
        cluster_id: str,
        gateway_id: str,
        tmp_req: main_models.DetachGatewayDomainRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DetachGatewayDomainResponse:
        tmp_req.validate()
        request = main_models.DetachGatewayDomainShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.custom_domain):
            request.custom_domain_shrink = Utils.array_to_string_with_specified_style(tmp_req.custom_domain, 'CustomDomain', 'json')
        query = {}
        if not DaraCore.is_null(request.custom_domain_shrink):
            query['CustomDomain'] = request.custom_domain_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachGatewayDomain',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/gateways/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(gateway_id)}/domain/detach',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachGatewayDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_gateway_domain_with_options_async(
        self,
        cluster_id: str,
        gateway_id: str,
        tmp_req: main_models.DetachGatewayDomainRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DetachGatewayDomainResponse:
        tmp_req.validate()
        request = main_models.DetachGatewayDomainShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.custom_domain):
            request.custom_domain_shrink = Utils.array_to_string_with_specified_style(tmp_req.custom_domain, 'CustomDomain', 'json')
        query = {}
        if not DaraCore.is_null(request.custom_domain_shrink):
            query['CustomDomain'] = request.custom_domain_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachGatewayDomain',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/gateways/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(gateway_id)}/domain/detach',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachGatewayDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_gateway_domain(
        self,
        cluster_id: str,
        gateway_id: str,
        request: main_models.DetachGatewayDomainRequest,
    ) -> main_models.DetachGatewayDomainResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.detach_gateway_domain_with_options(cluster_id, gateway_id, request, headers, runtime)

    async def detach_gateway_domain_async(
        self,
        cluster_id: str,
        gateway_id: str,
        request: main_models.DetachGatewayDomainRequest,
    ) -> main_models.DetachGatewayDomainResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.detach_gateway_domain_with_options_async(cluster_id, gateway_id, request, headers, runtime)

    def develop_service_with_options(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.DevelopServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DevelopServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.exit):
            query['Exit'] = request.exit
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DevelopService',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}/develop',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DevelopServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def develop_service_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.DevelopServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DevelopServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.exit):
            query['Exit'] = request.exit
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DevelopService',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}/develop',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DevelopServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def develop_service(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.DevelopServiceRequest,
    ) -> main_models.DevelopServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.develop_service_with_options(cluster_id, service_name, request, headers, runtime)

    async def develop_service_async(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.DevelopServiceRequest,
    ) -> main_models.DevelopServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.develop_service_with_options_async(cluster_id, service_name, request, headers, runtime)

    def list_acl_policy_with_options(
        self,
        cluster_id: str,
        gateway_id: str,
        request: main_models.ListAclPolicyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAclPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAclPolicy',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/gateways/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(gateway_id)}/acl_policy',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAclPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_acl_policy_with_options_async(
        self,
        cluster_id: str,
        gateway_id: str,
        request: main_models.ListAclPolicyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAclPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAclPolicy',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/gateways/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(gateway_id)}/acl_policy',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAclPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_acl_policy(
        self,
        cluster_id: str,
        gateway_id: str,
        request: main_models.ListAclPolicyRequest,
    ) -> main_models.ListAclPolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_acl_policy_with_options(cluster_id, gateway_id, request, headers, runtime)

    async def list_acl_policy_async(
        self,
        cluster_id: str,
        gateway_id: str,
        request: main_models.ListAclPolicyRequest,
    ) -> main_models.ListAclPolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_acl_policy_with_options_async(cluster_id, gateway_id, request, headers, runtime)

    def list_benchmark_task_with_options(
        self,
        request: main_models.ListBenchmarkTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListBenchmarkTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.model_id):
            query['ModelId'] = request.model_id
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.request_method):
            query['RequestMethod'] = request.request_method
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListBenchmarkTask',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/benchmark-tasks',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBenchmarkTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_benchmark_task_with_options_async(
        self,
        request: main_models.ListBenchmarkTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListBenchmarkTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.model_id):
            query['ModelId'] = request.model_id
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.request_method):
            query['RequestMethod'] = request.request_method
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListBenchmarkTask',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/benchmark-tasks',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBenchmarkTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_benchmark_task(
        self,
        request: main_models.ListBenchmarkTaskRequest,
    ) -> main_models.ListBenchmarkTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_benchmark_task_with_options(request, headers, runtime)

    async def list_benchmark_task_async(
        self,
        request: main_models.ListBenchmarkTaskRequest,
    ) -> main_models.ListBenchmarkTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_benchmark_task_with_options_async(request, headers, runtime)

    def list_gateway_with_options(
        self,
        tmp_req: main_models.ListGatewayRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListGatewayResponse:
        tmp_req.validate()
        request = main_models.ListGatewayShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.label):
            request.label_shrink = Utils.array_to_string_with_specified_style(tmp_req.label, 'Label', 'json')
        query = {}
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.gateway_name):
            query['GatewayName'] = request.gateway_name
        if not DaraCore.is_null(request.gateway_type):
            query['GatewayType'] = request.gateway_type
        if not DaraCore.is_null(request.internet_enabled):
            query['InternetEnabled'] = request.internet_enabled
        if not DaraCore.is_null(request.label_shrink):
            query['Label'] = request.label_shrink
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGateway',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/gateways',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_gateway_with_options_async(
        self,
        tmp_req: main_models.ListGatewayRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListGatewayResponse:
        tmp_req.validate()
        request = main_models.ListGatewayShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.label):
            request.label_shrink = Utils.array_to_string_with_specified_style(tmp_req.label, 'Label', 'json')
        query = {}
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.gateway_name):
            query['GatewayName'] = request.gateway_name
        if not DaraCore.is_null(request.gateway_type):
            query['GatewayType'] = request.gateway_type
        if not DaraCore.is_null(request.internet_enabled):
            query['InternetEnabled'] = request.internet_enabled
        if not DaraCore.is_null(request.label_shrink):
            query['Label'] = request.label_shrink
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGateway',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/gateways',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_gateway(
        self,
        request: main_models.ListGatewayRequest,
    ) -> main_models.ListGatewayResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_gateway_with_options(request, headers, runtime)

    async def list_gateway_async(
        self,
        request: main_models.ListGatewayRequest,
    ) -> main_models.ListGatewayResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_gateway_with_options_async(request, headers, runtime)

    def list_gateway_domains_with_options(
        self,
        cluster_id: str,
        gateway_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListGatewayDomainsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListGatewayDomains',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/gateways/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(gateway_id)}/domains',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGatewayDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_gateway_domains_with_options_async(
        self,
        cluster_id: str,
        gateway_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListGatewayDomainsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListGatewayDomains',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/gateways/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(gateway_id)}/domains',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGatewayDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_gateway_domains(
        self,
        cluster_id: str,
        gateway_id: str,
    ) -> main_models.ListGatewayDomainsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_gateway_domains_with_options(cluster_id, gateway_id, headers, runtime)

    async def list_gateway_domains_async(
        self,
        cluster_id: str,
        gateway_id: str,
    ) -> main_models.ListGatewayDomainsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_gateway_domains_with_options_async(cluster_id, gateway_id, headers, runtime)

    def list_gateway_intranet_linked_vpc_with_options(
        self,
        cluster_id: str,
        gateway_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListGatewayIntranetLinkedVpcResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListGatewayIntranetLinkedVpc',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/gateways/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(gateway_id)}/intranet_endpoint_linked_vpc',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGatewayIntranetLinkedVpcResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_gateway_intranet_linked_vpc_with_options_async(
        self,
        cluster_id: str,
        gateway_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListGatewayIntranetLinkedVpcResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListGatewayIntranetLinkedVpc',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/gateways/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(gateway_id)}/intranet_endpoint_linked_vpc',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGatewayIntranetLinkedVpcResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_gateway_intranet_linked_vpc(
        self,
        cluster_id: str,
        gateway_id: str,
    ) -> main_models.ListGatewayIntranetLinkedVpcResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_gateway_intranet_linked_vpc_with_options(cluster_id, gateway_id, headers, runtime)

    async def list_gateway_intranet_linked_vpc_async(
        self,
        cluster_id: str,
        gateway_id: str,
    ) -> main_models.ListGatewayIntranetLinkedVpcResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_gateway_intranet_linked_vpc_with_options_async(cluster_id, gateway_id, headers, runtime)

    def list_gateway_intranet_linked_vpc_peer_with_options(
        self,
        cluster_id: str,
        gateway_id: str,
        request: main_models.ListGatewayIntranetLinkedVpcPeerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListGatewayIntranetLinkedVpcPeerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGatewayIntranetLinkedVpcPeer',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/gateways/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(gateway_id)}/intranet_endpoint_linked_vpc_peer',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGatewayIntranetLinkedVpcPeerResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_gateway_intranet_linked_vpc_peer_with_options_async(
        self,
        cluster_id: str,
        gateway_id: str,
        request: main_models.ListGatewayIntranetLinkedVpcPeerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListGatewayIntranetLinkedVpcPeerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGatewayIntranetLinkedVpcPeer',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/gateways/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(gateway_id)}/intranet_endpoint_linked_vpc_peer',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGatewayIntranetLinkedVpcPeerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_gateway_intranet_linked_vpc_peer(
        self,
        cluster_id: str,
        gateway_id: str,
        request: main_models.ListGatewayIntranetLinkedVpcPeerRequest,
    ) -> main_models.ListGatewayIntranetLinkedVpcPeerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_gateway_intranet_linked_vpc_peer_with_options(cluster_id, gateway_id, request, headers, runtime)

    async def list_gateway_intranet_linked_vpc_peer_async(
        self,
        cluster_id: str,
        gateway_id: str,
        request: main_models.ListGatewayIntranetLinkedVpcPeerRequest,
    ) -> main_models.ListGatewayIntranetLinkedVpcPeerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_gateway_intranet_linked_vpc_peer_with_options_async(cluster_id, gateway_id, request, headers, runtime)

    def list_gateway_intranet_supported_zone_with_options(
        self,
        gateway_id: str,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListGatewayIntranetSupportedZoneResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListGatewayIntranetSupportedZone',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/gateways/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(gateway_id)}/intranet_supported_zone',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGatewayIntranetSupportedZoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_gateway_intranet_supported_zone_with_options_async(
        self,
        gateway_id: str,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListGatewayIntranetSupportedZoneResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListGatewayIntranetSupportedZone',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/gateways/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(gateway_id)}/intranet_supported_zone',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGatewayIntranetSupportedZoneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_gateway_intranet_supported_zone(
        self,
        gateway_id: str,
        cluster_id: str,
    ) -> main_models.ListGatewayIntranetSupportedZoneResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_gateway_intranet_supported_zone_with_options(gateway_id, cluster_id, headers, runtime)

    async def list_gateway_intranet_supported_zone_async(
        self,
        gateway_id: str,
        cluster_id: str,
    ) -> main_models.ListGatewayIntranetSupportedZoneResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_gateway_intranet_supported_zone_with_options_async(gateway_id, cluster_id, headers, runtime)

    def list_groups_with_options(
        self,
        request: main_models.ListGroupsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        if not DaraCore.is_null(request.traffic_mode):
            query['TrafficMode'] = request.traffic_mode
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGroups',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/groups',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_groups_with_options_async(
        self,
        request: main_models.ListGroupsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        if not DaraCore.is_null(request.traffic_mode):
            query['TrafficMode'] = request.traffic_mode
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGroups',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/groups',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_groups(
        self,
        request: main_models.ListGroupsRequest,
    ) -> main_models.ListGroupsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_groups_with_options(request, headers, runtime)

    async def list_groups_async(
        self,
        request: main_models.ListGroupsRequest,
    ) -> main_models.ListGroupsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_groups_with_options_async(request, headers, runtime)

    def list_resource_instance_worker_with_options(
        self,
        cluster_id: str,
        resource_id: str,
        instance_name: str,
        request: main_models.ListResourceInstanceWorkerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListResourceInstanceWorkerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.ready):
            query['Ready'] = request.ready
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.worker_name):
            query['WorkerName'] = request.worker_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResourceInstanceWorker',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/resources/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(resource_id)}/instance/{DaraURL.percent_encode(instance_name)}/workers',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourceInstanceWorkerResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_instance_worker_with_options_async(
        self,
        cluster_id: str,
        resource_id: str,
        instance_name: str,
        request: main_models.ListResourceInstanceWorkerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListResourceInstanceWorkerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.ready):
            query['Ready'] = request.ready
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.worker_name):
            query['WorkerName'] = request.worker_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResourceInstanceWorker',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/resources/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(resource_id)}/instance/{DaraURL.percent_encode(instance_name)}/workers',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourceInstanceWorkerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_instance_worker(
        self,
        cluster_id: str,
        resource_id: str,
        instance_name: str,
        request: main_models.ListResourceInstanceWorkerRequest,
    ) -> main_models.ListResourceInstanceWorkerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_resource_instance_worker_with_options(cluster_id, resource_id, instance_name, request, headers, runtime)

    async def list_resource_instance_worker_async(
        self,
        cluster_id: str,
        resource_id: str,
        instance_name: str,
        request: main_models.ListResourceInstanceWorkerRequest,
    ) -> main_models.ListResourceInstanceWorkerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_resource_instance_worker_with_options_async(cluster_id, resource_id, instance_name, request, headers, runtime)

    def list_resource_instances_with_options(
        self,
        cluster_id: str,
        resource_id: str,
        tmp_req: main_models.ListResourceInstancesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListResourceInstancesResponse:
        tmp_req.validate()
        request = main_models.ListResourceInstancesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.label):
            request.label_shrink = Utils.array_to_string_with_specified_style(tmp_req.label, 'Label', 'json')
        query = {}
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.instance_ip):
            query['InstanceIP'] = request.instance_ip
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.instance_status):
            query['InstanceStatus'] = request.instance_status
        if not DaraCore.is_null(request.label_shrink):
            query['Label'] = request.label_shrink
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        if not DaraCore.is_null(request.zone):
            query['Zone'] = request.zone
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResourceInstances',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/resources/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(resource_id)}/instances',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourceInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_instances_with_options_async(
        self,
        cluster_id: str,
        resource_id: str,
        tmp_req: main_models.ListResourceInstancesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListResourceInstancesResponse:
        tmp_req.validate()
        request = main_models.ListResourceInstancesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.label):
            request.label_shrink = Utils.array_to_string_with_specified_style(tmp_req.label, 'Label', 'json')
        query = {}
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.instance_ip):
            query['InstanceIP'] = request.instance_ip
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.instance_status):
            query['InstanceStatus'] = request.instance_status
        if not DaraCore.is_null(request.label_shrink):
            query['Label'] = request.label_shrink
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        if not DaraCore.is_null(request.zone):
            query['Zone'] = request.zone
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResourceInstances',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/resources/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(resource_id)}/instances',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourceInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_instances(
        self,
        cluster_id: str,
        resource_id: str,
        request: main_models.ListResourceInstancesRequest,
    ) -> main_models.ListResourceInstancesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_resource_instances_with_options(cluster_id, resource_id, request, headers, runtime)

    async def list_resource_instances_async(
        self,
        cluster_id: str,
        resource_id: str,
        request: main_models.ListResourceInstancesRequest,
    ) -> main_models.ListResourceInstancesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_resource_instances_with_options_async(cluster_id, resource_id, request, headers, runtime)

    def list_resource_services_with_options(
        self,
        cluster_id: str,
        resource_id: str,
        request: main_models.ListResourceServicesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListResourceServicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResourceServices',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/resources/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(resource_id)}/services',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourceServicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_services_with_options_async(
        self,
        cluster_id: str,
        resource_id: str,
        request: main_models.ListResourceServicesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListResourceServicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResourceServices',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/resources/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(resource_id)}/services',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourceServicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_services(
        self,
        cluster_id: str,
        resource_id: str,
        request: main_models.ListResourceServicesRequest,
    ) -> main_models.ListResourceServicesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_resource_services_with_options(cluster_id, resource_id, request, headers, runtime)

    async def list_resource_services_async(
        self,
        cluster_id: str,
        resource_id: str,
        request: main_models.ListResourceServicesRequest,
    ) -> main_models.ListResourceServicesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_resource_services_with_options_async(cluster_id, resource_id, request, headers, runtime)

    def list_resources_with_options(
        self,
        request: main_models.ListResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not DaraCore.is_null(request.resource_status):
            query['ResourceStatus'] = request.resource_status
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResources',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/resources',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resources_with_options_async(
        self,
        request: main_models.ListResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not DaraCore.is_null(request.resource_status):
            query['ResourceStatus'] = request.resource_status
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResources',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/resources',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resources(
        self,
        request: main_models.ListResourcesRequest,
    ) -> main_models.ListResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_resources_with_options(request, headers, runtime)

    async def list_resources_async(
        self,
        request: main_models.ListResourcesRequest,
    ) -> main_models.ListResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_resources_with_options_async(request, headers, runtime)

    def list_service_containers_with_options(
        self,
        cluster_id: str,
        service_name: str,
        instance_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListServiceContainersResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListServiceContainers',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}/instances/{DaraURL.percent_encode(instance_name)}/containers',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListServiceContainersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_service_containers_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        instance_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListServiceContainersResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListServiceContainers',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}/instances/{DaraURL.percent_encode(instance_name)}/containers',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListServiceContainersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_service_containers(
        self,
        cluster_id: str,
        service_name: str,
        instance_name: str,
    ) -> main_models.ListServiceContainersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_service_containers_with_options(cluster_id, service_name, instance_name, headers, runtime)

    async def list_service_containers_async(
        self,
        cluster_id: str,
        service_name: str,
        instance_name: str,
    ) -> main_models.ListServiceContainersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_service_containers_with_options_async(cluster_id, service_name, instance_name, headers, runtime)

    def list_service_instance_fault_injection_info_with_options(
        self,
        cluster_id: str,
        service_name: str,
        instance_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListServiceInstanceFaultInjectionInfoResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListServiceInstanceFaultInjectionInfo',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}/instances/{DaraURL.percent_encode(instance_name)}/faults',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListServiceInstanceFaultInjectionInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_service_instance_fault_injection_info_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        instance_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListServiceInstanceFaultInjectionInfoResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListServiceInstanceFaultInjectionInfo',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}/instances/{DaraURL.percent_encode(instance_name)}/faults',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListServiceInstanceFaultInjectionInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_service_instance_fault_injection_info(
        self,
        cluster_id: str,
        service_name: str,
        instance_name: str,
    ) -> main_models.ListServiceInstanceFaultInjectionInfoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_service_instance_fault_injection_info_with_options(cluster_id, service_name, instance_name, headers, runtime)

    async def list_service_instance_fault_injection_info_async(
        self,
        cluster_id: str,
        service_name: str,
        instance_name: str,
    ) -> main_models.ListServiceInstanceFaultInjectionInfoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_service_instance_fault_injection_info_with_options_async(cluster_id, service_name, instance_name, headers, runtime)

    def list_service_instances_with_options(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.ListServiceInstancesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListServiceInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.host_ip):
            query['HostIP'] = request.host_ip
        if not DaraCore.is_null(request.instance_ip):
            query['InstanceIP'] = request.instance_ip
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.instance_status):
            query['InstanceStatus'] = request.instance_status
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.is_spot):
            query['IsSpot'] = request.is_spot
        if not DaraCore.is_null(request.list_replica):
            query['ListReplica'] = request.list_replica
        if not DaraCore.is_null(request.member_type):
            query['MemberType'] = request.member_type
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.quota_id):
            query['QuotaId'] = request.quota_id
        if not DaraCore.is_null(request.replica_name):
            query['ReplicaName'] = request.replica_name
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.role):
            query['Role'] = request.role
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListServiceInstances',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}/instances',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListServiceInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_service_instances_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.ListServiceInstancesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListServiceInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.host_ip):
            query['HostIP'] = request.host_ip
        if not DaraCore.is_null(request.instance_ip):
            query['InstanceIP'] = request.instance_ip
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.instance_status):
            query['InstanceStatus'] = request.instance_status
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.is_spot):
            query['IsSpot'] = request.is_spot
        if not DaraCore.is_null(request.list_replica):
            query['ListReplica'] = request.list_replica
        if not DaraCore.is_null(request.member_type):
            query['MemberType'] = request.member_type
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.quota_id):
            query['QuotaId'] = request.quota_id
        if not DaraCore.is_null(request.replica_name):
            query['ReplicaName'] = request.replica_name
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.role):
            query['Role'] = request.role
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListServiceInstances',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}/instances',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListServiceInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_service_instances(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.ListServiceInstancesRequest,
    ) -> main_models.ListServiceInstancesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_service_instances_with_options(cluster_id, service_name, request, headers, runtime)

    async def list_service_instances_async(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.ListServiceInstancesRequest,
    ) -> main_models.ListServiceInstancesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_service_instances_with_options_async(cluster_id, service_name, request, headers, runtime)

    def list_service_versions_with_options(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.ListServiceVersionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListServiceVersionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListServiceVersions',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}/versions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListServiceVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_service_versions_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.ListServiceVersionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListServiceVersionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListServiceVersions',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}/versions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListServiceVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_service_versions(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.ListServiceVersionsRequest,
    ) -> main_models.ListServiceVersionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_service_versions_with_options(cluster_id, service_name, request, headers, runtime)

    async def list_service_versions_async(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.ListServiceVersionsRequest,
    ) -> main_models.ListServiceVersionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_service_versions_with_options_async(cluster_id, service_name, request, headers, runtime)

    def list_services_with_options(
        self,
        tmp_req: main_models.ListServicesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListServicesResponse:
        tmp_req.validate()
        request = main_models.ListServicesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.label):
            request.label_shrink = Utils.array_to_string_with_specified_style(tmp_req.label, 'Label', 'json')
        query = {}
        if not DaraCore.is_null(request.autoscaler_enabled):
            query['AutoscalerEnabled'] = request.autoscaler_enabled
        if not DaraCore.is_null(request.caller_uid):
            query['CallerUid'] = request.caller_uid
        if not DaraCore.is_null(request.cronscaler_enabled):
            query['CronscalerEnabled'] = request.cronscaler_enabled
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.gateway):
            query['Gateway'] = request.gateway
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.include_no_workspace):
            query['IncludeNoWorkspace'] = request.include_no_workspace
        if not DaraCore.is_null(request.label_shrink):
            query['Label'] = request.label_shrink
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.parent_service_uid):
            query['ParentServiceUid'] = request.parent_service_uid
        if not DaraCore.is_null(request.quota_id):
            query['QuotaId'] = request.quota_id
        if not DaraCore.is_null(request.resource_alias_name):
            query['ResourceAliasName'] = request.resource_alias_name
        if not DaraCore.is_null(request.resource_burstable):
            query['ResourceBurstable'] = request.resource_burstable
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.role):
            query['Role'] = request.role
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        if not DaraCore.is_null(request.service_status):
            query['ServiceStatus'] = request.service_status
        if not DaraCore.is_null(request.service_type):
            query['ServiceType'] = request.service_type
        if not DaraCore.is_null(request.service_uid):
            query['ServiceUid'] = request.service_uid
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        if not DaraCore.is_null(request.traffic_state):
            query['TrafficState'] = request.traffic_state
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListServices',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListServicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_services_with_options_async(
        self,
        tmp_req: main_models.ListServicesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListServicesResponse:
        tmp_req.validate()
        request = main_models.ListServicesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.label):
            request.label_shrink = Utils.array_to_string_with_specified_style(tmp_req.label, 'Label', 'json')
        query = {}
        if not DaraCore.is_null(request.autoscaler_enabled):
            query['AutoscalerEnabled'] = request.autoscaler_enabled
        if not DaraCore.is_null(request.caller_uid):
            query['CallerUid'] = request.caller_uid
        if not DaraCore.is_null(request.cronscaler_enabled):
            query['CronscalerEnabled'] = request.cronscaler_enabled
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.gateway):
            query['Gateway'] = request.gateway
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.include_no_workspace):
            query['IncludeNoWorkspace'] = request.include_no_workspace
        if not DaraCore.is_null(request.label_shrink):
            query['Label'] = request.label_shrink
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.parent_service_uid):
            query['ParentServiceUid'] = request.parent_service_uid
        if not DaraCore.is_null(request.quota_id):
            query['QuotaId'] = request.quota_id
        if not DaraCore.is_null(request.resource_alias_name):
            query['ResourceAliasName'] = request.resource_alias_name
        if not DaraCore.is_null(request.resource_burstable):
            query['ResourceBurstable'] = request.resource_burstable
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.role):
            query['Role'] = request.role
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        if not DaraCore.is_null(request.service_status):
            query['ServiceStatus'] = request.service_status
        if not DaraCore.is_null(request.service_type):
            query['ServiceType'] = request.service_type
        if not DaraCore.is_null(request.service_uid):
            query['ServiceUid'] = request.service_uid
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        if not DaraCore.is_null(request.traffic_state):
            query['TrafficState'] = request.traffic_state
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListServices',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListServicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_services(
        self,
        request: main_models.ListServicesRequest,
    ) -> main_models.ListServicesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_services_with_options(request, headers, runtime)

    async def list_services_async(
        self,
        request: main_models.ListServicesRequest,
    ) -> main_models.ListServicesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_services_with_options_async(request, headers, runtime)

    def list_tenant_addons_with_options(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTenantAddonsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListTenantAddons',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/tenantaddons',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTenantAddonsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tenant_addons_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTenantAddonsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListTenantAddons',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/tenantaddons',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTenantAddonsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tenant_addons(self) -> main_models.ListTenantAddonsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_tenant_addons_with_options(headers, runtime)

    async def list_tenant_addons_async(self) -> main_models.ListTenantAddonsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_tenant_addons_with_options_async(headers, runtime)

    def list_virtual_resource_with_options(
        self,
        request: main_models.ListVirtualResourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListVirtualResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        if not DaraCore.is_null(request.virtual_resource_id):
            query['VirtualResourceId'] = request.virtual_resource_id
        if not DaraCore.is_null(request.virtual_resource_name):
            query['VirtualResourceName'] = request.virtual_resource_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListVirtualResource',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/virtualresources',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVirtualResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_virtual_resource_with_options_async(
        self,
        request: main_models.ListVirtualResourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListVirtualResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        if not DaraCore.is_null(request.virtual_resource_id):
            query['VirtualResourceId'] = request.virtual_resource_id
        if not DaraCore.is_null(request.virtual_resource_name):
            query['VirtualResourceName'] = request.virtual_resource_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListVirtualResource',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/virtualresources',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVirtualResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_virtual_resource(
        self,
        request: main_models.ListVirtualResourceRequest,
    ) -> main_models.ListVirtualResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_virtual_resource_with_options(request, headers, runtime)

    async def list_virtual_resource_async(
        self,
        request: main_models.ListVirtualResourceRequest,
    ) -> main_models.ListVirtualResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_virtual_resource_with_options_async(request, headers, runtime)

    def migrate_resource_instance_with_options(
        self,
        cluster_id: str,
        resource_id: str,
        request: main_models.MigrateResourceInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.MigrateResourceInstanceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dest_resource_id):
            body['DestResourceId'] = request.dest_resource_id
        if not DaraCore.is_null(request.instance_ids):
            body['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.migrate_to_hybrid):
            body['MigrateToHybrid'] = request.migrate_to_hybrid
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'MigrateResourceInstance',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/resources/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(resource_id)}/instances/migrate',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MigrateResourceInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def migrate_resource_instance_with_options_async(
        self,
        cluster_id: str,
        resource_id: str,
        request: main_models.MigrateResourceInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.MigrateResourceInstanceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dest_resource_id):
            body['DestResourceId'] = request.dest_resource_id
        if not DaraCore.is_null(request.instance_ids):
            body['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.migrate_to_hybrid):
            body['MigrateToHybrid'] = request.migrate_to_hybrid
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'MigrateResourceInstance',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/resources/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(resource_id)}/instances/migrate',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MigrateResourceInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def migrate_resource_instance(
        self,
        cluster_id: str,
        resource_id: str,
        request: main_models.MigrateResourceInstanceRequest,
    ) -> main_models.MigrateResourceInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.migrate_resource_instance_with_options(cluster_id, resource_id, request, headers, runtime)

    async def migrate_resource_instance_async(
        self,
        cluster_id: str,
        resource_id: str,
        request: main_models.MigrateResourceInstanceRequest,
    ) -> main_models.MigrateResourceInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.migrate_resource_instance_with_options_async(cluster_id, resource_id, request, headers, runtime)

    def reinstall_tenant_addon_with_options(
        self,
        cluster_id: str,
        tenant_addon_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ReinstallTenantAddonResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ReinstallTenantAddon',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/tenantaddons/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(tenant_addon_name)}/reinstall',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReinstallTenantAddonResponse(),
            self.call_api(params, req, runtime)
        )

    async def reinstall_tenant_addon_with_options_async(
        self,
        cluster_id: str,
        tenant_addon_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ReinstallTenantAddonResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ReinstallTenantAddon',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/tenantaddons/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(tenant_addon_name)}/reinstall',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReinstallTenantAddonResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reinstall_tenant_addon(
        self,
        cluster_id: str,
        tenant_addon_name: str,
    ) -> main_models.ReinstallTenantAddonResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.reinstall_tenant_addon_with_options(cluster_id, tenant_addon_name, headers, runtime)

    async def reinstall_tenant_addon_async(
        self,
        cluster_id: str,
        tenant_addon_name: str,
    ) -> main_models.ReinstallTenantAddonResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.reinstall_tenant_addon_with_options_async(cluster_id, tenant_addon_name, headers, runtime)

    def release_service_with_options(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.ReleaseServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ReleaseServiceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.traffic_state):
            body['TrafficState'] = request.traffic_state
        if not DaraCore.is_null(request.weight):
            body['Weight'] = request.weight
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReleaseService',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}/release',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReleaseServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_service_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.ReleaseServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ReleaseServiceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.traffic_state):
            body['TrafficState'] = request.traffic_state
        if not DaraCore.is_null(request.weight):
            body['Weight'] = request.weight
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReleaseService',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}/release',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReleaseServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_service(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.ReleaseServiceRequest,
    ) -> main_models.ReleaseServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.release_service_with_options(cluster_id, service_name, request, headers, runtime)

    async def release_service_async(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.ReleaseServiceRequest,
    ) -> main_models.ReleaseServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.release_service_with_options_async(cluster_id, service_name, request, headers, runtime)

    def restart_service_with_options(
        self,
        cluster_id: str,
        service_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RestartServiceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'RestartService',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}/restart',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestartServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_service_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RestartServiceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'RestartService',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}/restart',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestartServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_service(
        self,
        cluster_id: str,
        service_name: str,
    ) -> main_models.RestartServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.restart_service_with_options(cluster_id, service_name, headers, runtime)

    async def restart_service_async(
        self,
        cluster_id: str,
        service_name: str,
    ) -> main_models.RestartServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.restart_service_with_options_async(cluster_id, service_name, headers, runtime)

    def start_benchmark_task_with_options(
        self,
        cluster_id: str,
        task_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StartBenchmarkTaskResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'StartBenchmarkTask',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/benchmark-tasks/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(task_name)}/start',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartBenchmarkTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_benchmark_task_with_options_async(
        self,
        cluster_id: str,
        task_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StartBenchmarkTaskResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'StartBenchmarkTask',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/benchmark-tasks/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(task_name)}/start',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartBenchmarkTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_benchmark_task(
        self,
        cluster_id: str,
        task_name: str,
    ) -> main_models.StartBenchmarkTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.start_benchmark_task_with_options(cluster_id, task_name, headers, runtime)

    async def start_benchmark_task_async(
        self,
        cluster_id: str,
        task_name: str,
    ) -> main_models.StartBenchmarkTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.start_benchmark_task_with_options_async(cluster_id, task_name, headers, runtime)

    def start_service_with_options(
        self,
        cluster_id: str,
        service_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StartServiceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'StartService',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}/start',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_service_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StartServiceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'StartService',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}/start',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_service(
        self,
        cluster_id: str,
        service_name: str,
    ) -> main_models.StartServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.start_service_with_options(cluster_id, service_name, headers, runtime)

    async def start_service_async(
        self,
        cluster_id: str,
        service_name: str,
    ) -> main_models.StartServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.start_service_with_options_async(cluster_id, service_name, headers, runtime)

    def stop_benchmark_task_with_options(
        self,
        cluster_id: str,
        task_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopBenchmarkTaskResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'StopBenchmarkTask',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/benchmark-tasks/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(task_name)}/stop',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopBenchmarkTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_benchmark_task_with_options_async(
        self,
        cluster_id: str,
        task_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopBenchmarkTaskResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'StopBenchmarkTask',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/benchmark-tasks/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(task_name)}/stop',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopBenchmarkTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_benchmark_task(
        self,
        cluster_id: str,
        task_name: str,
    ) -> main_models.StopBenchmarkTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.stop_benchmark_task_with_options(cluster_id, task_name, headers, runtime)

    async def stop_benchmark_task_async(
        self,
        cluster_id: str,
        task_name: str,
    ) -> main_models.StopBenchmarkTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.stop_benchmark_task_with_options_async(cluster_id, task_name, headers, runtime)

    def stop_service_with_options(
        self,
        cluster_id: str,
        service_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopServiceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'StopService',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}/stop',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_service_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopServiceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'StopService',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}/stop',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_service(
        self,
        cluster_id: str,
        service_name: str,
    ) -> main_models.StopServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.stop_service_with_options(cluster_id, service_name, headers, runtime)

    async def stop_service_async(
        self,
        cluster_id: str,
        service_name: str,
    ) -> main_models.StopServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.stop_service_with_options_async(cluster_id, service_name, headers, runtime)

    def update_app_service_with_options(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.UpdateAppServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAppServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.quota_id):
            query['QuotaId'] = request.quota_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not DaraCore.is_null(request.app_type):
            body['AppType'] = request.app_type
        if not DaraCore.is_null(request.app_version):
            body['AppVersion'] = request.app_version
        if not DaraCore.is_null(request.config):
            body['Config'] = request.config
        if not DaraCore.is_null(request.replicas):
            body['Replicas'] = request.replicas
        if not DaraCore.is_null(request.service_spec):
            body['ServiceSpec'] = request.service_spec
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAppService',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/app_services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAppServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_app_service_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.UpdateAppServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAppServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.quota_id):
            query['QuotaId'] = request.quota_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not DaraCore.is_null(request.app_type):
            body['AppType'] = request.app_type
        if not DaraCore.is_null(request.app_version):
            body['AppVersion'] = request.app_version
        if not DaraCore.is_null(request.config):
            body['Config'] = request.config
        if not DaraCore.is_null(request.replicas):
            body['Replicas'] = request.replicas
        if not DaraCore.is_null(request.service_spec):
            body['ServiceSpec'] = request.service_spec
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAppService',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/app_services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAppServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_app_service(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.UpdateAppServiceRequest,
    ) -> main_models.UpdateAppServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_app_service_with_options(cluster_id, service_name, request, headers, runtime)

    async def update_app_service_async(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.UpdateAppServiceRequest,
    ) -> main_models.UpdateAppServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_app_service_with_options_async(cluster_id, service_name, request, headers, runtime)

    def update_benchmark_task_with_options(
        self,
        cluster_id: str,
        task_name: str,
        request: main_models.UpdateBenchmarkTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateBenchmarkTaskResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'UpdateBenchmarkTask',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/benchmark-tasks/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(task_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateBenchmarkTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_benchmark_task_with_options_async(
        self,
        cluster_id: str,
        task_name: str,
        request: main_models.UpdateBenchmarkTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateBenchmarkTaskResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'UpdateBenchmarkTask',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/benchmark-tasks/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(task_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateBenchmarkTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_benchmark_task(
        self,
        cluster_id: str,
        task_name: str,
        request: main_models.UpdateBenchmarkTaskRequest,
    ) -> main_models.UpdateBenchmarkTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_benchmark_task_with_options(cluster_id, task_name, request, headers, runtime)

    async def update_benchmark_task_async(
        self,
        cluster_id: str,
        task_name: str,
        request: main_models.UpdateBenchmarkTaskRequest,
    ) -> main_models.UpdateBenchmarkTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_benchmark_task_with_options_async(cluster_id, task_name, request, headers, runtime)

    def update_gateway_with_options(
        self,
        gateway_id: str,
        cluster_id: str,
        request: main_models.UpdateGatewayRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGatewayResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.enable_internet):
            body['EnableInternet'] = request.enable_internet
        if not DaraCore.is_null(request.enable_intranet):
            body['EnableIntranet'] = request.enable_intranet
        if not DaraCore.is_null(request.enable_sslredirection):
            body['EnableSSLRedirection'] = request.enable_sslredirection
        if not DaraCore.is_null(request.instance_type):
            body['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.is_default):
            body['IsDefault'] = request.is_default
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.replicas):
            body['Replicas'] = request.replicas
        if not DaraCore.is_null(request.v_switch_ids):
            body['VSwitchIds'] = request.v_switch_ids
        if not DaraCore.is_null(request.vpc_id):
            body['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGateway',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/gateways/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(gateway_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_gateway_with_options_async(
        self,
        gateway_id: str,
        cluster_id: str,
        request: main_models.UpdateGatewayRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGatewayResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.enable_internet):
            body['EnableInternet'] = request.enable_internet
        if not DaraCore.is_null(request.enable_intranet):
            body['EnableIntranet'] = request.enable_intranet
        if not DaraCore.is_null(request.enable_sslredirection):
            body['EnableSSLRedirection'] = request.enable_sslredirection
        if not DaraCore.is_null(request.instance_type):
            body['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.is_default):
            body['IsDefault'] = request.is_default
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.replicas):
            body['Replicas'] = request.replicas
        if not DaraCore.is_null(request.v_switch_ids):
            body['VSwitchIds'] = request.v_switch_ids
        if not DaraCore.is_null(request.vpc_id):
            body['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGateway',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/gateways/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(gateway_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_gateway(
        self,
        gateway_id: str,
        cluster_id: str,
        request: main_models.UpdateGatewayRequest,
    ) -> main_models.UpdateGatewayResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_gateway_with_options(gateway_id, cluster_id, request, headers, runtime)

    async def update_gateway_async(
        self,
        gateway_id: str,
        cluster_id: str,
        request: main_models.UpdateGatewayRequest,
    ) -> main_models.UpdateGatewayResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_gateway_with_options_async(gateway_id, cluster_id, request, headers, runtime)

    def update_gateway_label_with_options(
        self,
        cluster_id: str,
        gateway_id: str,
        request: main_models.UpdateGatewayLabelRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGatewayLabelResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.labels):
            body['Labels'] = request.labels
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGatewayLabel',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/gateways/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(gateway_id)}/label',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGatewayLabelResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_gateway_label_with_options_async(
        self,
        cluster_id: str,
        gateway_id: str,
        request: main_models.UpdateGatewayLabelRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGatewayLabelResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.labels):
            body['Labels'] = request.labels
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGatewayLabel',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/gateways/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(gateway_id)}/label',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGatewayLabelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_gateway_label(
        self,
        cluster_id: str,
        gateway_id: str,
        request: main_models.UpdateGatewayLabelRequest,
    ) -> main_models.UpdateGatewayLabelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_gateway_label_with_options(cluster_id, gateway_id, request, headers, runtime)

    async def update_gateway_label_async(
        self,
        cluster_id: str,
        gateway_id: str,
        request: main_models.UpdateGatewayLabelRequest,
    ) -> main_models.UpdateGatewayLabelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_gateway_label_with_options_async(cluster_id, gateway_id, request, headers, runtime)

    def update_group_with_options(
        self,
        cluster_id: str,
        group_name: str,
        request: main_models.UpdateGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.traffic_mode):
            body['TrafficMode'] = request.traffic_mode
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGroup',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/groups/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(group_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_group_with_options_async(
        self,
        cluster_id: str,
        group_name: str,
        request: main_models.UpdateGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.traffic_mode):
            body['TrafficMode'] = request.traffic_mode
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGroup',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/groups/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(group_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_group(
        self,
        cluster_id: str,
        group_name: str,
        request: main_models.UpdateGroupRequest,
    ) -> main_models.UpdateGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_group_with_options(cluster_id, group_name, request, headers, runtime)

    async def update_group_async(
        self,
        cluster_id: str,
        group_name: str,
        request: main_models.UpdateGroupRequest,
    ) -> main_models.UpdateGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_group_with_options_async(cluster_id, group_name, request, headers, runtime)

    def update_resource_with_options(
        self,
        cluster_id: str,
        resource_id: str,
        request: main_models.UpdateResourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateResourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.resource_name):
            body['ResourceName'] = request.resource_name
        if not DaraCore.is_null(request.self_managed_resource_options):
            body['SelfManagedResourceOptions'] = request.self_managed_resource_options
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateResource',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/resources/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(resource_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_resource_with_options_async(
        self,
        cluster_id: str,
        resource_id: str,
        request: main_models.UpdateResourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateResourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.resource_name):
            body['ResourceName'] = request.resource_name
        if not DaraCore.is_null(request.self_managed_resource_options):
            body['SelfManagedResourceOptions'] = request.self_managed_resource_options
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateResource',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/resources/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(resource_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_resource(
        self,
        cluster_id: str,
        resource_id: str,
        request: main_models.UpdateResourceRequest,
    ) -> main_models.UpdateResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_resource_with_options(cluster_id, resource_id, request, headers, runtime)

    async def update_resource_async(
        self,
        cluster_id: str,
        resource_id: str,
        request: main_models.UpdateResourceRequest,
    ) -> main_models.UpdateResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_resource_with_options_async(cluster_id, resource_id, request, headers, runtime)

    def update_resource_dlink_with_options(
        self,
        cluster_id: str,
        resource_id: str,
        request: main_models.UpdateResourceDLinkRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateResourceDLinkResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.destination_cidrs):
            body['DestinationCIDRs'] = request.destination_cidrs
        if not DaraCore.is_null(request.security_group_id):
            body['SecurityGroupId'] = request.security_group_id
        if not DaraCore.is_null(request.v_switch_id):
            body['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.v_switch_id_list):
            body['VSwitchIdList'] = request.v_switch_id_list
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateResourceDLink',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/resources/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(resource_id)}/dlink',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateResourceDLinkResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_resource_dlink_with_options_async(
        self,
        cluster_id: str,
        resource_id: str,
        request: main_models.UpdateResourceDLinkRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateResourceDLinkResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.destination_cidrs):
            body['DestinationCIDRs'] = request.destination_cidrs
        if not DaraCore.is_null(request.security_group_id):
            body['SecurityGroupId'] = request.security_group_id
        if not DaraCore.is_null(request.v_switch_id):
            body['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.v_switch_id_list):
            body['VSwitchIdList'] = request.v_switch_id_list
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateResourceDLink',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/resources/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(resource_id)}/dlink',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateResourceDLinkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_resource_dlink(
        self,
        cluster_id: str,
        resource_id: str,
        request: main_models.UpdateResourceDLinkRequest,
    ) -> main_models.UpdateResourceDLinkResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_resource_dlink_with_options(cluster_id, resource_id, request, headers, runtime)

    async def update_resource_dlink_async(
        self,
        cluster_id: str,
        resource_id: str,
        request: main_models.UpdateResourceDLinkRequest,
    ) -> main_models.UpdateResourceDLinkResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_resource_dlink_with_options_async(cluster_id, resource_id, request, headers, runtime)

    def update_resource_instance_with_options(
        self,
        cluster_id: str,
        resource_id: str,
        instance_id: str,
        request: main_models.UpdateResourceInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateResourceInstanceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.action):
            body['Action'] = request.action
        if not DaraCore.is_null(request.new_disk_size):
            body['NewDiskSize'] = request.new_disk_size
        if not DaraCore.is_null(request.reason):
            body['Reason'] = request.reason
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateResourceInstance',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/resources/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(resource_id)}/instances/{DaraURL.percent_encode(instance_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateResourceInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_resource_instance_with_options_async(
        self,
        cluster_id: str,
        resource_id: str,
        instance_id: str,
        request: main_models.UpdateResourceInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateResourceInstanceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.action):
            body['Action'] = request.action
        if not DaraCore.is_null(request.new_disk_size):
            body['NewDiskSize'] = request.new_disk_size
        if not DaraCore.is_null(request.reason):
            body['Reason'] = request.reason
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateResourceInstance',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/resources/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(resource_id)}/instances/{DaraURL.percent_encode(instance_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateResourceInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_resource_instance(
        self,
        cluster_id: str,
        resource_id: str,
        instance_id: str,
        request: main_models.UpdateResourceInstanceRequest,
    ) -> main_models.UpdateResourceInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_resource_instance_with_options(cluster_id, resource_id, instance_id, request, headers, runtime)

    async def update_resource_instance_async(
        self,
        cluster_id: str,
        resource_id: str,
        instance_id: str,
        request: main_models.UpdateResourceInstanceRequest,
    ) -> main_models.UpdateResourceInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_resource_instance_with_options_async(cluster_id, resource_id, instance_id, request, headers, runtime)

    def update_resource_instance_label_with_options(
        self,
        cluster_id: str,
        resource_id: str,
        tmp_req: main_models.UpdateResourceInstanceLabelRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateResourceInstanceLabelResponse:
        tmp_req.validate()
        request = main_models.UpdateResourceInstanceLabelShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.instance_ids):
            request.instance_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'simple')
        query = {}
        if not DaraCore.is_null(request.all_instances):
            query['AllInstances'] = request.all_instances
        if not DaraCore.is_null(request.instance_ids_shrink):
            query['InstanceIds'] = request.instance_ids_shrink
        body = {}
        if not DaraCore.is_null(request.labels):
            body['Labels'] = request.labels
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateResourceInstanceLabel',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/resources/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(resource_id)}/label',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateResourceInstanceLabelResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_resource_instance_label_with_options_async(
        self,
        cluster_id: str,
        resource_id: str,
        tmp_req: main_models.UpdateResourceInstanceLabelRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateResourceInstanceLabelResponse:
        tmp_req.validate()
        request = main_models.UpdateResourceInstanceLabelShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.instance_ids):
            request.instance_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'simple')
        query = {}
        if not DaraCore.is_null(request.all_instances):
            query['AllInstances'] = request.all_instances
        if not DaraCore.is_null(request.instance_ids_shrink):
            query['InstanceIds'] = request.instance_ids_shrink
        body = {}
        if not DaraCore.is_null(request.labels):
            body['Labels'] = request.labels
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateResourceInstanceLabel',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/resources/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(resource_id)}/label',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateResourceInstanceLabelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_resource_instance_label(
        self,
        cluster_id: str,
        resource_id: str,
        request: main_models.UpdateResourceInstanceLabelRequest,
    ) -> main_models.UpdateResourceInstanceLabelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_resource_instance_label_with_options(cluster_id, resource_id, request, headers, runtime)

    async def update_resource_instance_label_async(
        self,
        cluster_id: str,
        resource_id: str,
        request: main_models.UpdateResourceInstanceLabelRequest,
    ) -> main_models.UpdateResourceInstanceLabelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_resource_instance_label_with_options_async(cluster_id, resource_id, request, headers, runtime)

    def update_service_with_options(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.UpdateServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.member_to_update):
            query['MemberToUpdate'] = request.member_to_update
        if not DaraCore.is_null(request.update_type):
            query['UpdateType'] = request.update_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'UpdateService',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_service_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.UpdateServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.member_to_update):
            query['MemberToUpdate'] = request.member_to_update
        if not DaraCore.is_null(request.update_type):
            query['UpdateType'] = request.update_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'UpdateService',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_service(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.UpdateServiceRequest,
    ) -> main_models.UpdateServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_service_with_options(cluster_id, service_name, request, headers, runtime)

    async def update_service_async(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.UpdateServiceRequest,
    ) -> main_models.UpdateServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_service_with_options_async(cluster_id, service_name, request, headers, runtime)

    def update_service_auto_scaler_with_options(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.UpdateServiceAutoScalerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateServiceAutoScalerResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.behavior):
            body['behavior'] = request.behavior
        if not DaraCore.is_null(request.max):
            body['max'] = request.max
        if not DaraCore.is_null(request.min):
            body['min'] = request.min
        if not DaraCore.is_null(request.scale_strategies):
            body['scaleStrategies'] = request.scale_strategies
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateServiceAutoScaler',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}/autoscaler',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateServiceAutoScalerResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_service_auto_scaler_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.UpdateServiceAutoScalerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateServiceAutoScalerResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.behavior):
            body['behavior'] = request.behavior
        if not DaraCore.is_null(request.max):
            body['max'] = request.max
        if not DaraCore.is_null(request.min):
            body['min'] = request.min
        if not DaraCore.is_null(request.scale_strategies):
            body['scaleStrategies'] = request.scale_strategies
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateServiceAutoScaler',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}/autoscaler',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateServiceAutoScalerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_service_auto_scaler(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.UpdateServiceAutoScalerRequest,
    ) -> main_models.UpdateServiceAutoScalerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_service_auto_scaler_with_options(cluster_id, service_name, request, headers, runtime)

    async def update_service_auto_scaler_async(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.UpdateServiceAutoScalerRequest,
    ) -> main_models.UpdateServiceAutoScalerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_service_auto_scaler_with_options_async(cluster_id, service_name, request, headers, runtime)

    def update_service_cron_scaler_with_options(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.UpdateServiceCronScalerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateServiceCronScalerResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.exclude_dates):
            body['ExcludeDates'] = request.exclude_dates
        if not DaraCore.is_null(request.scale_jobs):
            body['ScaleJobs'] = request.scale_jobs
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateServiceCronScaler',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}/cronscaler',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateServiceCronScalerResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_service_cron_scaler_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.UpdateServiceCronScalerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateServiceCronScalerResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.exclude_dates):
            body['ExcludeDates'] = request.exclude_dates
        if not DaraCore.is_null(request.scale_jobs):
            body['ScaleJobs'] = request.scale_jobs
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateServiceCronScaler',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}/cronscaler',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateServiceCronScalerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_service_cron_scaler(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.UpdateServiceCronScalerRequest,
    ) -> main_models.UpdateServiceCronScalerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_service_cron_scaler_with_options(cluster_id, service_name, request, headers, runtime)

    async def update_service_cron_scaler_async(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.UpdateServiceCronScalerRequest,
    ) -> main_models.UpdateServiceCronScalerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_service_cron_scaler_with_options_async(cluster_id, service_name, request, headers, runtime)

    def update_service_instance_with_options(
        self,
        cluster_id: str,
        service_name: str,
        instance_name: str,
        request: main_models.UpdateServiceInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateServiceInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.is_replica):
            query['IsReplica'] = request.is_replica
        body = {}
        if not DaraCore.is_null(request.detach):
            body['Detach'] = request.detach
        if not DaraCore.is_null(request.hibernate):
            body['Hibernate'] = request.hibernate
        if not DaraCore.is_null(request.isolate):
            body['Isolate'] = request.isolate
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateServiceInstance',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}/instances/{DaraURL.percent_encode(instance_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateServiceInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_service_instance_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        instance_name: str,
        request: main_models.UpdateServiceInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateServiceInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.is_replica):
            query['IsReplica'] = request.is_replica
        body = {}
        if not DaraCore.is_null(request.detach):
            body['Detach'] = request.detach
        if not DaraCore.is_null(request.hibernate):
            body['Hibernate'] = request.hibernate
        if not DaraCore.is_null(request.isolate):
            body['Isolate'] = request.isolate
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateServiceInstance',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}/instances/{DaraURL.percent_encode(instance_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateServiceInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_service_instance(
        self,
        cluster_id: str,
        service_name: str,
        instance_name: str,
        request: main_models.UpdateServiceInstanceRequest,
    ) -> main_models.UpdateServiceInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_service_instance_with_options(cluster_id, service_name, instance_name, request, headers, runtime)

    async def update_service_instance_async(
        self,
        cluster_id: str,
        service_name: str,
        instance_name: str,
        request: main_models.UpdateServiceInstanceRequest,
    ) -> main_models.UpdateServiceInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_service_instance_with_options_async(cluster_id, service_name, instance_name, request, headers, runtime)

    def update_service_label_with_options(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.UpdateServiceLabelRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateServiceLabelResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.labels):
            body['Labels'] = request.labels
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateServiceLabel',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}/label',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateServiceLabelResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_service_label_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.UpdateServiceLabelRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateServiceLabelResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.labels):
            body['Labels'] = request.labels
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateServiceLabel',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}/label',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateServiceLabelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_service_label(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.UpdateServiceLabelRequest,
    ) -> main_models.UpdateServiceLabelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_service_label_with_options(cluster_id, service_name, request, headers, runtime)

    async def update_service_label_async(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.UpdateServiceLabelRequest,
    ) -> main_models.UpdateServiceLabelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_service_label_with_options_async(cluster_id, service_name, request, headers, runtime)

    def update_service_mirror_with_options(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.UpdateServiceMirrorRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateServiceMirrorResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.ratio):
            body['Ratio'] = request.ratio
        if not DaraCore.is_null(request.target):
            body['Target'] = request.target
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateServiceMirror',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}/mirror',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateServiceMirrorResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_service_mirror_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.UpdateServiceMirrorRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateServiceMirrorResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.ratio):
            body['Ratio'] = request.ratio
        if not DaraCore.is_null(request.target):
            body['Target'] = request.target
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateServiceMirror',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}/mirror',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateServiceMirrorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_service_mirror(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.UpdateServiceMirrorRequest,
    ) -> main_models.UpdateServiceMirrorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_service_mirror_with_options(cluster_id, service_name, request, headers, runtime)

    async def update_service_mirror_async(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.UpdateServiceMirrorRequest,
    ) -> main_models.UpdateServiceMirrorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_service_mirror_with_options_async(cluster_id, service_name, request, headers, runtime)

    def update_service_safety_lock_with_options(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.UpdateServiceSafetyLockRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateServiceSafetyLockResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lock):
            body['Lock'] = request.lock
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateServiceSafetyLock',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}/lock',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateServiceSafetyLockResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_service_safety_lock_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.UpdateServiceSafetyLockRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateServiceSafetyLockResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lock):
            body['Lock'] = request.lock
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateServiceSafetyLock',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}/lock',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateServiceSafetyLockResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_service_safety_lock(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.UpdateServiceSafetyLockRequest,
    ) -> main_models.UpdateServiceSafetyLockResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_service_safety_lock_with_options(cluster_id, service_name, request, headers, runtime)

    async def update_service_safety_lock_async(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.UpdateServiceSafetyLockRequest,
    ) -> main_models.UpdateServiceSafetyLockResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_service_safety_lock_with_options_async(cluster_id, service_name, request, headers, runtime)

    def update_service_version_with_options(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.UpdateServiceVersionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateServiceVersionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.version):
            body['Version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateServiceVersion',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}/version',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateServiceVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_service_version_with_options_async(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.UpdateServiceVersionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateServiceVersionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.version):
            body['Version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateServiceVersion',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/services/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(service_name)}/version',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateServiceVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_service_version(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.UpdateServiceVersionRequest,
    ) -> main_models.UpdateServiceVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_service_version_with_options(cluster_id, service_name, request, headers, runtime)

    async def update_service_version_async(
        self,
        cluster_id: str,
        service_name: str,
        request: main_models.UpdateServiceVersionRequest,
    ) -> main_models.UpdateServiceVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_service_version_with_options_async(cluster_id, service_name, request, headers, runtime)

    def update_virtual_resource_with_options(
        self,
        cluster_id: str,
        virtual_resource_id: str,
        request: main_models.UpdateVirtualResourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateVirtualResourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.disable_spot_protection_period):
            body['DisableSpotProtectionPeriod'] = request.disable_spot_protection_period
        if not DaraCore.is_null(request.resources):
            body['Resources'] = request.resources
        if not DaraCore.is_null(request.virtual_resource_name):
            body['VirtualResourceName'] = request.virtual_resource_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateVirtualResource',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/virtualresources/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(virtual_resource_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateVirtualResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_virtual_resource_with_options_async(
        self,
        cluster_id: str,
        virtual_resource_id: str,
        request: main_models.UpdateVirtualResourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateVirtualResourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.disable_spot_protection_period):
            body['DisableSpotProtectionPeriod'] = request.disable_spot_protection_period
        if not DaraCore.is_null(request.resources):
            body['Resources'] = request.resources
        if not DaraCore.is_null(request.virtual_resource_name):
            body['VirtualResourceName'] = request.virtual_resource_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateVirtualResource',
            version = '2021-07-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/virtualresources/{DaraURL.percent_encode(cluster_id)}/{DaraURL.percent_encode(virtual_resource_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateVirtualResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_virtual_resource(
        self,
        cluster_id: str,
        virtual_resource_id: str,
        request: main_models.UpdateVirtualResourceRequest,
    ) -> main_models.UpdateVirtualResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_virtual_resource_with_options(cluster_id, virtual_resource_id, request, headers, runtime)

    async def update_virtual_resource_async(
        self,
        cluster_id: str,
        virtual_resource_id: str,
        request: main_models.UpdateVirtualResourceRequest,
    ) -> main_models.UpdateVirtualResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_virtual_resource_with_options_async(cluster_id, virtual_resource_id, request, headers, runtime)
