# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_paiflow20210202 import models as paiflow_20210202_models
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
        self._endpoint_rule = 'central'
        self._endpoint_map = {
            'cn-beijing': 'pai.cn-beijing.aliyuncs.com',
            'cn-hangzhou': 'pai.cn-hangzhou.data.aliyun.com',
            'cn-shanghai': 'pai.cn-shanghai.aliyuncs.com',
            'cn-shenzhen': 'pai.cn-shenzhen.aliyuncs.com',
            'cn-hongkong': 'pai.cn-hongkong.aliyuncs.com',
            'ap-southeast-1': 'pai.ap-southeast-1.aliyuncs.com',
            'ap-southeast-2': 'pai.ap-southeast-2.aliyuncs.com',
            'ap-southeast-3': 'pai.ap-southeast-3.aliyuncs.com',
            'ap-southeast-5': 'pai.ap-southeast-5.aliyuncs.com',
            'us-west-1': 'pai.us-west-1.aliyuncs.com',
            'us-east-1': 'pai.us-east-1.aliyuncs.com',
            'eu-central-1': 'pai.eu-central-1.aliyuncs.com',
            'me-east-1': 'pai.me-east-1.aliyuncs.com',
            'ap-south-1': 'pai.ap-south-1.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('paiflow', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_pipeline(
        self,
        request: paiflow_20210202_models.CreatePipelineRequest,
    ) -> paiflow_20210202_models.CreatePipelineResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_pipeline_with_options(request, headers, runtime)

    async def create_pipeline_async(
        self,
        request: paiflow_20210202_models.CreatePipelineRequest,
    ) -> paiflow_20210202_models.CreatePipelineResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_pipeline_with_options_async(request, headers, runtime)

    def create_pipeline_with_options(
        self,
        request: paiflow_20210202_models.CreatePipelineRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiflow_20210202_models.CreatePipelineResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.manifest):
            body['Manifest'] = request.manifest
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePipeline',
            version='2021-02-02',
            protocol='HTTPS',
            pathname=f'/api/v1/pipelines',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiflow_20210202_models.CreatePipelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_pipeline_with_options_async(
        self,
        request: paiflow_20210202_models.CreatePipelineRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiflow_20210202_models.CreatePipelineResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.manifest):
            body['Manifest'] = request.manifest
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePipeline',
            version='2021-02-02',
            protocol='HTTPS',
            pathname=f'/api/v1/pipelines',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiflow_20210202_models.CreatePipelineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_pipeline_release(
        self,
        pipeline_id: str,
        request: paiflow_20210202_models.CreatePipelineReleaseRequest,
    ) -> paiflow_20210202_models.CreatePipelineReleaseResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_pipeline_release_with_options(pipeline_id, request, headers, runtime)

    async def create_pipeline_release_async(
        self,
        pipeline_id: str,
        request: paiflow_20210202_models.CreatePipelineReleaseRequest,
    ) -> paiflow_20210202_models.CreatePipelineReleaseResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_pipeline_release_with_options_async(pipeline_id, request, headers, runtime)

    def create_pipeline_release_with_options(
        self,
        pipeline_id: str,
        request: paiflow_20210202_models.CreatePipelineReleaseRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiflow_20210202_models.CreatePipelineReleaseResponse:
        UtilClient.validate_model(request)
        pipeline_id = OpenApiUtilClient.get_encode_param(pipeline_id)
        body = {}
        if not UtilClient.is_unset(request.target_pipeline_provider):
            body['TargetPipelineProvider'] = request.target_pipeline_provider
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePipelineRelease',
            version='2021-02-02',
            protocol='HTTPS',
            pathname=f'/api/v1/pipelines/{pipeline_id}/releases',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiflow_20210202_models.CreatePipelineReleaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_pipeline_release_with_options_async(
        self,
        pipeline_id: str,
        request: paiflow_20210202_models.CreatePipelineReleaseRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiflow_20210202_models.CreatePipelineReleaseResponse:
        UtilClient.validate_model(request)
        pipeline_id = OpenApiUtilClient.get_encode_param(pipeline_id)
        body = {}
        if not UtilClient.is_unset(request.target_pipeline_provider):
            body['TargetPipelineProvider'] = request.target_pipeline_provider
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePipelineRelease',
            version='2021-02-02',
            protocol='HTTPS',
            pathname=f'/api/v1/pipelines/{pipeline_id}/releases',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiflow_20210202_models.CreatePipelineReleaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_run(
        self,
        request: paiflow_20210202_models.CreateRunRequest,
    ) -> paiflow_20210202_models.CreateRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_run_with_options(request, headers, runtime)

    async def create_run_async(
        self,
        request: paiflow_20210202_models.CreateRunRequest,
    ) -> paiflow_20210202_models.CreateRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_run_with_options_async(request, headers, runtime)

    def create_run_with_options(
        self,
        request: paiflow_20210202_models.CreateRunRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiflow_20210202_models.CreateRunResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accessibility):
            body['Accessibility'] = request.accessibility
        if not UtilClient.is_unset(request.arguments):
            body['Arguments'] = request.arguments
        if not UtilClient.is_unset(request.experiment_id):
            body['ExperimentId'] = request.experiment_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.no_confirm_required):
            body['NoConfirmRequired'] = request.no_confirm_required
        if not UtilClient.is_unset(request.options):
            body['Options'] = request.options
        if not UtilClient.is_unset(request.pipeline_id):
            body['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.pipeline_manifest):
            body['PipelineManifest'] = request.pipeline_manifest
        if not UtilClient.is_unset(request.source):
            body['Source'] = request.source
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateRun',
            version='2021-02-02',
            protocol='HTTPS',
            pathname=f'/api/v1/runs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiflow_20210202_models.CreateRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_run_with_options_async(
        self,
        request: paiflow_20210202_models.CreateRunRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiflow_20210202_models.CreateRunResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accessibility):
            body['Accessibility'] = request.accessibility
        if not UtilClient.is_unset(request.arguments):
            body['Arguments'] = request.arguments
        if not UtilClient.is_unset(request.experiment_id):
            body['ExperimentId'] = request.experiment_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.no_confirm_required):
            body['NoConfirmRequired'] = request.no_confirm_required
        if not UtilClient.is_unset(request.options):
            body['Options'] = request.options
        if not UtilClient.is_unset(request.pipeline_id):
            body['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.pipeline_manifest):
            body['PipelineManifest'] = request.pipeline_manifest
        if not UtilClient.is_unset(request.source):
            body['Source'] = request.source
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateRun',
            version='2021-02-02',
            protocol='HTTPS',
            pathname=f'/api/v1/runs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiflow_20210202_models.CreateRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_pipeline(
        self,
        pipeline_id: str,
    ) -> paiflow_20210202_models.DeletePipelineResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_pipeline_with_options(pipeline_id, headers, runtime)

    async def delete_pipeline_async(
        self,
        pipeline_id: str,
    ) -> paiflow_20210202_models.DeletePipelineResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_pipeline_with_options_async(pipeline_id, headers, runtime)

    def delete_pipeline_with_options(
        self,
        pipeline_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiflow_20210202_models.DeletePipelineResponse:
        pipeline_id = OpenApiUtilClient.get_encode_param(pipeline_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeletePipeline',
            version='2021-02-02',
            protocol='HTTPS',
            pathname=f'/api/v1/pipelines/{pipeline_id}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiflow_20210202_models.DeletePipelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_pipeline_with_options_async(
        self,
        pipeline_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiflow_20210202_models.DeletePipelineResponse:
        pipeline_id = OpenApiUtilClient.get_encode_param(pipeline_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeletePipeline',
            version='2021-02-02',
            protocol='HTTPS',
            pathname=f'/api/v1/pipelines/{pipeline_id}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiflow_20210202_models.DeletePipelineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_run(
        self,
        run_id: str,
    ) -> paiflow_20210202_models.DeleteRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_run_with_options(run_id, headers, runtime)

    async def delete_run_async(
        self,
        run_id: str,
    ) -> paiflow_20210202_models.DeleteRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_run_with_options_async(run_id, headers, runtime)

    def delete_run_with_options(
        self,
        run_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiflow_20210202_models.DeleteRunResponse:
        run_id = OpenApiUtilClient.get_encode_param(run_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteRun',
            version='2021-02-02',
            protocol='HTTPS',
            pathname=f'/api/v1/runs/{run_id}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiflow_20210202_models.DeleteRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_run_with_options_async(
        self,
        run_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiflow_20210202_models.DeleteRunResponse:
        run_id = OpenApiUtilClient.get_encode_param(run_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteRun',
            version='2021-02-02',
            protocol='HTTPS',
            pathname=f'/api/v1/runs/{run_id}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiflow_20210202_models.DeleteRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_caller_provider(self) -> paiflow_20210202_models.GetCallerProviderResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_caller_provider_with_options(headers, runtime)

    async def get_caller_provider_async(self) -> paiflow_20210202_models.GetCallerProviderResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_caller_provider_with_options_async(headers, runtime)

    def get_caller_provider_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiflow_20210202_models.GetCallerProviderResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetCallerProvider',
            version='2021-02-02',
            protocol='HTTPS',
            pathname=f'/api/v1/provider',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiflow_20210202_models.GetCallerProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_caller_provider_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiflow_20210202_models.GetCallerProviderResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetCallerProvider',
            version='2021-02-02',
            protocol='HTTPS',
            pathname=f'/api/v1/provider',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiflow_20210202_models.GetCallerProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_node(
        self,
        run_id: str,
        node_id: str,
        request: paiflow_20210202_models.GetNodeRequest,
    ) -> paiflow_20210202_models.GetNodeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_node_with_options(run_id, node_id, request, headers, runtime)

    async def get_node_async(
        self,
        run_id: str,
        node_id: str,
        request: paiflow_20210202_models.GetNodeRequest,
    ) -> paiflow_20210202_models.GetNodeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_node_with_options_async(run_id, node_id, request, headers, runtime)

    def get_node_with_options(
        self,
        run_id: str,
        node_id: str,
        request: paiflow_20210202_models.GetNodeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiflow_20210202_models.GetNodeResponse:
        UtilClient.validate_model(request)
        run_id = OpenApiUtilClient.get_encode_param(run_id)
        node_id = OpenApiUtilClient.get_encode_param(node_id)
        query = {}
        if not UtilClient.is_unset(request.depth):
            query['Depth'] = request.depth
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetNode',
            version='2021-02-02',
            protocol='HTTPS',
            pathname=f'/api/v1/runs/{run_id}/nodes/{node_id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiflow_20210202_models.GetNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_node_with_options_async(
        self,
        run_id: str,
        node_id: str,
        request: paiflow_20210202_models.GetNodeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiflow_20210202_models.GetNodeResponse:
        UtilClient.validate_model(request)
        run_id = OpenApiUtilClient.get_encode_param(run_id)
        node_id = OpenApiUtilClient.get_encode_param(node_id)
        query = {}
        if not UtilClient.is_unset(request.depth):
            query['Depth'] = request.depth
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetNode',
            version='2021-02-02',
            protocol='HTTPS',
            pathname=f'/api/v1/runs/{run_id}/nodes/{node_id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiflow_20210202_models.GetNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_pipeline(
        self,
        pipeline_id: str,
    ) -> paiflow_20210202_models.GetPipelineResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_pipeline_with_options(pipeline_id, headers, runtime)

    async def get_pipeline_async(
        self,
        pipeline_id: str,
    ) -> paiflow_20210202_models.GetPipelineResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_pipeline_with_options_async(pipeline_id, headers, runtime)

    def get_pipeline_with_options(
        self,
        pipeline_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiflow_20210202_models.GetPipelineResponse:
        pipeline_id = OpenApiUtilClient.get_encode_param(pipeline_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetPipeline',
            version='2021-02-02',
            protocol='HTTPS',
            pathname=f'/api/v1/pipelines/{pipeline_id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiflow_20210202_models.GetPipelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_pipeline_with_options_async(
        self,
        pipeline_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiflow_20210202_models.GetPipelineResponse:
        pipeline_id = OpenApiUtilClient.get_encode_param(pipeline_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetPipeline',
            version='2021-02-02',
            protocol='HTTPS',
            pathname=f'/api/v1/pipelines/{pipeline_id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiflow_20210202_models.GetPipelineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_pipeline_schema(
        self,
        pipeline_id: str,
    ) -> paiflow_20210202_models.GetPipelineSchemaResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_pipeline_schema_with_options(pipeline_id, headers, runtime)

    async def get_pipeline_schema_async(
        self,
        pipeline_id: str,
    ) -> paiflow_20210202_models.GetPipelineSchemaResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_pipeline_schema_with_options_async(pipeline_id, headers, runtime)

    def get_pipeline_schema_with_options(
        self,
        pipeline_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiflow_20210202_models.GetPipelineSchemaResponse:
        pipeline_id = OpenApiUtilClient.get_encode_param(pipeline_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetPipelineSchema',
            version='2021-02-02',
            protocol='HTTPS',
            pathname=f'/api/v1/pipelines/{pipeline_id}/schema',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiflow_20210202_models.GetPipelineSchemaResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_pipeline_schema_with_options_async(
        self,
        pipeline_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiflow_20210202_models.GetPipelineSchemaResponse:
        pipeline_id = OpenApiUtilClient.get_encode_param(pipeline_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetPipelineSchema',
            version='2021-02-02',
            protocol='HTTPS',
            pathname=f'/api/v1/pipelines/{pipeline_id}/schema',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiflow_20210202_models.GetPipelineSchemaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_run(
        self,
        run_id: str,
        request: paiflow_20210202_models.GetRunRequest,
    ) -> paiflow_20210202_models.GetRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_run_with_options(run_id, request, headers, runtime)

    async def get_run_async(
        self,
        run_id: str,
        request: paiflow_20210202_models.GetRunRequest,
    ) -> paiflow_20210202_models.GetRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_run_with_options_async(run_id, request, headers, runtime)

    def get_run_with_options(
        self,
        run_id: str,
        request: paiflow_20210202_models.GetRunRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiflow_20210202_models.GetRunResponse:
        UtilClient.validate_model(request)
        run_id = OpenApiUtilClient.get_encode_param(run_id)
        query = {}
        if not UtilClient.is_unset(request.manifest_type):
            query['ManifestType'] = request.manifest_type
        if not UtilClient.is_unset(request.verbose):
            query['Verbose'] = request.verbose
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRun',
            version='2021-02-02',
            protocol='HTTPS',
            pathname=f'/api/v1/runs/{run_id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiflow_20210202_models.GetRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_run_with_options_async(
        self,
        run_id: str,
        request: paiflow_20210202_models.GetRunRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiflow_20210202_models.GetRunResponse:
        UtilClient.validate_model(request)
        run_id = OpenApiUtilClient.get_encode_param(run_id)
        query = {}
        if not UtilClient.is_unset(request.manifest_type):
            query['ManifestType'] = request.manifest_type
        if not UtilClient.is_unset(request.verbose):
            query['Verbose'] = request.verbose
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRun',
            version='2021-02-02',
            protocol='HTTPS',
            pathname=f'/api/v1/runs/{run_id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiflow_20210202_models.GetRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_run_statistics(
        self,
        request: paiflow_20210202_models.GetRunStatisticsRequest,
    ) -> paiflow_20210202_models.GetRunStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_run_statistics_with_options(request, headers, runtime)

    async def get_run_statistics_async(
        self,
        request: paiflow_20210202_models.GetRunStatisticsRequest,
    ) -> paiflow_20210202_models.GetRunStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_run_statistics_with_options_async(request, headers, runtime)

    def get_run_statistics_with_options(
        self,
        tmp_req: paiflow_20210202_models.GetRunStatisticsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiflow_20210202_models.GetRunStatisticsResponse:
        UtilClient.validate_model(tmp_req)
        request = paiflow_20210202_models.GetRunStatisticsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.status):
            request.status_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.status, 'Status', 'json')
        query = {}
        if not UtilClient.is_unset(request.experiment_id):
            query['ExperimentId'] = request.experiment_id
        if not UtilClient.is_unset(request.is_show_all):
            query['IsShowAll'] = request.is_show_all
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.status_shrink):
            query['Status'] = request.status_shrink
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRunStatistics',
            version='2021-02-02',
            protocol='HTTPS',
            pathname=f'/api/v1/statistics/runs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiflow_20210202_models.GetRunStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_run_statistics_with_options_async(
        self,
        tmp_req: paiflow_20210202_models.GetRunStatisticsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiflow_20210202_models.GetRunStatisticsResponse:
        UtilClient.validate_model(tmp_req)
        request = paiflow_20210202_models.GetRunStatisticsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.status):
            request.status_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.status, 'Status', 'json')
        query = {}
        if not UtilClient.is_unset(request.experiment_id):
            query['ExperimentId'] = request.experiment_id
        if not UtilClient.is_unset(request.is_show_all):
            query['IsShowAll'] = request.is_show_all
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.status_shrink):
            query['Status'] = request.status_shrink
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRunStatistics',
            version='2021-02-02',
            protocol='HTTPS',
            pathname=f'/api/v1/statistics/runs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiflow_20210202_models.GetRunStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_node_logs(
        self,
        run_id: str,
        node_id: str,
        request: paiflow_20210202_models.ListNodeLogsRequest,
    ) -> paiflow_20210202_models.ListNodeLogsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_node_logs_with_options(run_id, node_id, request, headers, runtime)

    async def list_node_logs_async(
        self,
        run_id: str,
        node_id: str,
        request: paiflow_20210202_models.ListNodeLogsRequest,
    ) -> paiflow_20210202_models.ListNodeLogsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_node_logs_with_options_async(run_id, node_id, request, headers, runtime)

    def list_node_logs_with_options(
        self,
        run_id: str,
        node_id: str,
        request: paiflow_20210202_models.ListNodeLogsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiflow_20210202_models.ListNodeLogsResponse:
        UtilClient.validate_model(request)
        run_id = OpenApiUtilClient.get_encode_param(run_id)
        node_id = OpenApiUtilClient.get_encode_param(node_id)
        query = {}
        if not UtilClient.is_unset(request.from_time_in_seconds):
            query['FromTimeInSeconds'] = request.from_time_in_seconds
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.offset):
            query['Offset'] = request.offset
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.reverse):
            query['Reverse'] = request.reverse
        if not UtilClient.is_unset(request.to_time_in_seconds):
            query['ToTimeInSeconds'] = request.to_time_in_seconds
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNodeLogs',
            version='2021-02-02',
            protocol='HTTPS',
            pathname=f'/api/v1/runs/{run_id}/nodes/{node_id}/logs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiflow_20210202_models.ListNodeLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_node_logs_with_options_async(
        self,
        run_id: str,
        node_id: str,
        request: paiflow_20210202_models.ListNodeLogsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiflow_20210202_models.ListNodeLogsResponse:
        UtilClient.validate_model(request)
        run_id = OpenApiUtilClient.get_encode_param(run_id)
        node_id = OpenApiUtilClient.get_encode_param(node_id)
        query = {}
        if not UtilClient.is_unset(request.from_time_in_seconds):
            query['FromTimeInSeconds'] = request.from_time_in_seconds
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.offset):
            query['Offset'] = request.offset
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.reverse):
            query['Reverse'] = request.reverse
        if not UtilClient.is_unset(request.to_time_in_seconds):
            query['ToTimeInSeconds'] = request.to_time_in_seconds
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNodeLogs',
            version='2021-02-02',
            protocol='HTTPS',
            pathname=f'/api/v1/runs/{run_id}/nodes/{node_id}/logs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiflow_20210202_models.ListNodeLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_node_outputs(
        self,
        run_id: str,
        node_id: str,
        request: paiflow_20210202_models.ListNodeOutputsRequest,
    ) -> paiflow_20210202_models.ListNodeOutputsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_node_outputs_with_options(run_id, node_id, request, headers, runtime)

    async def list_node_outputs_async(
        self,
        run_id: str,
        node_id: str,
        request: paiflow_20210202_models.ListNodeOutputsRequest,
    ) -> paiflow_20210202_models.ListNodeOutputsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_node_outputs_with_options_async(run_id, node_id, request, headers, runtime)

    def list_node_outputs_with_options(
        self,
        run_id: str,
        node_id: str,
        request: paiflow_20210202_models.ListNodeOutputsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiflow_20210202_models.ListNodeOutputsResponse:
        UtilClient.validate_model(request)
        run_id = OpenApiUtilClient.get_encode_param(run_id)
        node_id = OpenApiUtilClient.get_encode_param(node_id)
        query = {}
        if not UtilClient.is_unset(request.depth):
            query['Depth'] = request.depth
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNodeOutputs',
            version='2021-02-02',
            protocol='HTTPS',
            pathname=f'/api/v1/runs/{run_id}/nodes/{node_id}/outputs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiflow_20210202_models.ListNodeOutputsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_node_outputs_with_options_async(
        self,
        run_id: str,
        node_id: str,
        request: paiflow_20210202_models.ListNodeOutputsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiflow_20210202_models.ListNodeOutputsResponse:
        UtilClient.validate_model(request)
        run_id = OpenApiUtilClient.get_encode_param(run_id)
        node_id = OpenApiUtilClient.get_encode_param(node_id)
        query = {}
        if not UtilClient.is_unset(request.depth):
            query['Depth'] = request.depth
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNodeOutputs',
            version='2021-02-02',
            protocol='HTTPS',
            pathname=f'/api/v1/runs/{run_id}/nodes/{node_id}/outputs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiflow_20210202_models.ListNodeOutputsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_node_status(
        self,
        run_id: str,
        node_id: str,
        request: paiflow_20210202_models.ListNodeStatusRequest,
    ) -> paiflow_20210202_models.ListNodeStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_node_status_with_options(run_id, node_id, request, headers, runtime)

    async def list_node_status_async(
        self,
        run_id: str,
        node_id: str,
        request: paiflow_20210202_models.ListNodeStatusRequest,
    ) -> paiflow_20210202_models.ListNodeStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_node_status_with_options_async(run_id, node_id, request, headers, runtime)

    def list_node_status_with_options(
        self,
        run_id: str,
        node_id: str,
        request: paiflow_20210202_models.ListNodeStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiflow_20210202_models.ListNodeStatusResponse:
        UtilClient.validate_model(request)
        run_id = OpenApiUtilClient.get_encode_param(run_id)
        node_id = OpenApiUtilClient.get_encode_param(node_id)
        query = {}
        if not UtilClient.is_unset(request.depth):
            query['Depth'] = request.depth
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNodeStatus',
            version='2021-02-02',
            protocol='HTTPS',
            pathname=f'/api/v1/runs/{run_id}/nodes/{node_id}/status',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiflow_20210202_models.ListNodeStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_node_status_with_options_async(
        self,
        run_id: str,
        node_id: str,
        request: paiflow_20210202_models.ListNodeStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiflow_20210202_models.ListNodeStatusResponse:
        UtilClient.validate_model(request)
        run_id = OpenApiUtilClient.get_encode_param(run_id)
        node_id = OpenApiUtilClient.get_encode_param(node_id)
        query = {}
        if not UtilClient.is_unset(request.depth):
            query['Depth'] = request.depth
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNodeStatus',
            version='2021-02-02',
            protocol='HTTPS',
            pathname=f'/api/v1/runs/{run_id}/nodes/{node_id}/status',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiflow_20210202_models.ListNodeStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_pipeline_privileges(
        self,
        pipeline_id: str,
    ) -> paiflow_20210202_models.ListPipelinePrivilegesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_pipeline_privileges_with_options(pipeline_id, headers, runtime)

    async def list_pipeline_privileges_async(
        self,
        pipeline_id: str,
    ) -> paiflow_20210202_models.ListPipelinePrivilegesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_pipeline_privileges_with_options_async(pipeline_id, headers, runtime)

    def list_pipeline_privileges_with_options(
        self,
        pipeline_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiflow_20210202_models.ListPipelinePrivilegesResponse:
        pipeline_id = OpenApiUtilClient.get_encode_param(pipeline_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListPipelinePrivileges',
            version='2021-02-02',
            protocol='HTTPS',
            pathname=f'/api/v1/pipelines/{pipeline_id}/privileges',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiflow_20210202_models.ListPipelinePrivilegesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_pipeline_privileges_with_options_async(
        self,
        pipeline_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiflow_20210202_models.ListPipelinePrivilegesResponse:
        pipeline_id = OpenApiUtilClient.get_encode_param(pipeline_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListPipelinePrivileges',
            version='2021-02-02',
            protocol='HTTPS',
            pathname=f'/api/v1/pipelines/{pipeline_id}/privileges',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiflow_20210202_models.ListPipelinePrivilegesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_pipelines(
        self,
        request: paiflow_20210202_models.ListPipelinesRequest,
    ) -> paiflow_20210202_models.ListPipelinesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_pipelines_with_options(request, headers, runtime)

    async def list_pipelines_async(
        self,
        request: paiflow_20210202_models.ListPipelinesRequest,
    ) -> paiflow_20210202_models.ListPipelinesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_pipelines_with_options_async(request, headers, runtime)

    def list_pipelines_with_options(
        self,
        request: paiflow_20210202_models.ListPipelinesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiflow_20210202_models.ListPipelinesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fuzzy_matching):
            query['FuzzyMatching'] = request.fuzzy_matching
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.pipeline_identifier):
            query['PipelineIdentifier'] = request.pipeline_identifier
        if not UtilClient.is_unset(request.pipeline_provider):
            query['PipelineProvider'] = request.pipeline_provider
        if not UtilClient.is_unset(request.pipeline_version):
            query['PipelineVersion'] = request.pipeline_version
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPipelines',
            version='2021-02-02',
            protocol='HTTPS',
            pathname=f'/api/v1/pipelines',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiflow_20210202_models.ListPipelinesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_pipelines_with_options_async(
        self,
        request: paiflow_20210202_models.ListPipelinesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiflow_20210202_models.ListPipelinesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fuzzy_matching):
            query['FuzzyMatching'] = request.fuzzy_matching
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.pipeline_identifier):
            query['PipelineIdentifier'] = request.pipeline_identifier
        if not UtilClient.is_unset(request.pipeline_provider):
            query['PipelineProvider'] = request.pipeline_provider
        if not UtilClient.is_unset(request.pipeline_version):
            query['PipelineVersion'] = request.pipeline_version
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPipelines',
            version='2021-02-02',
            protocol='HTTPS',
            pathname=f'/api/v1/pipelines',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiflow_20210202_models.ListPipelinesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_runs(
        self,
        request: paiflow_20210202_models.ListRunsRequest,
    ) -> paiflow_20210202_models.ListRunsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_runs_with_options(request, headers, runtime)

    async def list_runs_async(
        self,
        request: paiflow_20210202_models.ListRunsRequest,
    ) -> paiflow_20210202_models.ListRunsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_runs_with_options_async(request, headers, runtime)

    def list_runs_with_options(
        self,
        request: paiflow_20210202_models.ListRunsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiflow_20210202_models.ListRunsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.experiment_id):
            query['ExperimentId'] = request.experiment_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.pipeline_ids):
            query['PipelineIds'] = request.pipeline_ids
        if not UtilClient.is_unset(request.run_id):
            query['RunId'] = request.run_id
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRuns',
            version='2021-02-02',
            protocol='HTTPS',
            pathname=f'/api/v1/runs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiflow_20210202_models.ListRunsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_runs_with_options_async(
        self,
        request: paiflow_20210202_models.ListRunsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiflow_20210202_models.ListRunsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.experiment_id):
            query['ExperimentId'] = request.experiment_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.pipeline_ids):
            query['PipelineIds'] = request.pipeline_ids
        if not UtilClient.is_unset(request.run_id):
            query['RunId'] = request.run_id
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRuns',
            version='2021-02-02',
            protocol='HTTPS',
            pathname=f'/api/v1/runs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiflow_20210202_models.ListRunsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_runs_status(
        self,
        request: paiflow_20210202_models.ListRunsStatusRequest,
    ) -> paiflow_20210202_models.ListRunsStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_runs_status_with_options(request, headers, runtime)

    async def list_runs_status_async(
        self,
        request: paiflow_20210202_models.ListRunsStatusRequest,
    ) -> paiflow_20210202_models.ListRunsStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_runs_status_with_options_async(request, headers, runtime)

    def list_runs_status_with_options(
        self,
        request: paiflow_20210202_models.ListRunsStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiflow_20210202_models.ListRunsStatusResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.nodes):
            body['Nodes'] = request.nodes
        if not UtilClient.is_unset(request.runs):
            body['Runs'] = request.runs
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListRunsStatus',
            version='2021-02-02',
            protocol='HTTPS',
            pathname=f'/api/v1/runs',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiflow_20210202_models.ListRunsStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_runs_status_with_options_async(
        self,
        request: paiflow_20210202_models.ListRunsStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiflow_20210202_models.ListRunsStatusResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.nodes):
            body['Nodes'] = request.nodes
        if not UtilClient.is_unset(request.runs):
            body['Runs'] = request.runs
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListRunsStatus',
            version='2021-02-02',
            protocol='HTTPS',
            pathname=f'/api/v1/runs',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiflow_20210202_models.ListRunsStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_run(
        self,
        run_id: str,
    ) -> paiflow_20210202_models.StartRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_run_with_options(run_id, headers, runtime)

    async def start_run_async(
        self,
        run_id: str,
    ) -> paiflow_20210202_models.StartRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.start_run_with_options_async(run_id, headers, runtime)

    def start_run_with_options(
        self,
        run_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiflow_20210202_models.StartRunResponse:
        run_id = OpenApiUtilClient.get_encode_param(run_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StartRun',
            version='2021-02-02',
            protocol='HTTPS',
            pathname=f'/api/v1/runs/{run_id}/start',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiflow_20210202_models.StartRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_run_with_options_async(
        self,
        run_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiflow_20210202_models.StartRunResponse:
        run_id = OpenApiUtilClient.get_encode_param(run_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StartRun',
            version='2021-02-02',
            protocol='HTTPS',
            pathname=f'/api/v1/runs/{run_id}/start',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiflow_20210202_models.StartRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def terminate_run(
        self,
        run_id: str,
    ) -> paiflow_20210202_models.TerminateRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.terminate_run_with_options(run_id, headers, runtime)

    async def terminate_run_async(
        self,
        run_id: str,
    ) -> paiflow_20210202_models.TerminateRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.terminate_run_with_options_async(run_id, headers, runtime)

    def terminate_run_with_options(
        self,
        run_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiflow_20210202_models.TerminateRunResponse:
        run_id = OpenApiUtilClient.get_encode_param(run_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='TerminateRun',
            version='2021-02-02',
            protocol='HTTPS',
            pathname=f'/api/v1/runs/{run_id}/termination',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiflow_20210202_models.TerminateRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def terminate_run_with_options_async(
        self,
        run_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiflow_20210202_models.TerminateRunResponse:
        run_id = OpenApiUtilClient.get_encode_param(run_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='TerminateRun',
            version='2021-02-02',
            protocol='HTTPS',
            pathname=f'/api/v1/runs/{run_id}/termination',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiflow_20210202_models.TerminateRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_pipeline(
        self,
        pipeline_id: str,
        request: paiflow_20210202_models.UpdatePipelineRequest,
    ) -> paiflow_20210202_models.UpdatePipelineResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_pipeline_with_options(pipeline_id, request, headers, runtime)

    async def update_pipeline_async(
        self,
        pipeline_id: str,
        request: paiflow_20210202_models.UpdatePipelineRequest,
    ) -> paiflow_20210202_models.UpdatePipelineResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_pipeline_with_options_async(pipeline_id, request, headers, runtime)

    def update_pipeline_with_options(
        self,
        pipeline_id: str,
        request: paiflow_20210202_models.UpdatePipelineRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiflow_20210202_models.UpdatePipelineResponse:
        UtilClient.validate_model(request)
        pipeline_id = OpenApiUtilClient.get_encode_param(pipeline_id)
        body = {}
        if not UtilClient.is_unset(request.manifest):
            body['Manifest'] = request.manifest
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdatePipeline',
            version='2021-02-02',
            protocol='HTTPS',
            pathname=f'/api/v1/pipelines/{pipeline_id}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiflow_20210202_models.UpdatePipelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_pipeline_with_options_async(
        self,
        pipeline_id: str,
        request: paiflow_20210202_models.UpdatePipelineRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiflow_20210202_models.UpdatePipelineResponse:
        UtilClient.validate_model(request)
        pipeline_id = OpenApiUtilClient.get_encode_param(pipeline_id)
        body = {}
        if not UtilClient.is_unset(request.manifest):
            body['Manifest'] = request.manifest
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdatePipeline',
            version='2021-02-02',
            protocol='HTTPS',
            pathname=f'/api/v1/pipelines/{pipeline_id}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiflow_20210202_models.UpdatePipelineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_pipeline_privileges(
        self,
        pipeline_id: str,
        request: paiflow_20210202_models.UpdatePipelinePrivilegesRequest,
    ) -> paiflow_20210202_models.UpdatePipelinePrivilegesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_pipeline_privileges_with_options(pipeline_id, request, headers, runtime)

    async def update_pipeline_privileges_async(
        self,
        pipeline_id: str,
        request: paiflow_20210202_models.UpdatePipelinePrivilegesRequest,
    ) -> paiflow_20210202_models.UpdatePipelinePrivilegesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_pipeline_privileges_with_options_async(pipeline_id, request, headers, runtime)

    def update_pipeline_privileges_with_options(
        self,
        pipeline_id: str,
        request: paiflow_20210202_models.UpdatePipelinePrivilegesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiflow_20210202_models.UpdatePipelinePrivilegesResponse:
        UtilClient.validate_model(request)
        pipeline_id = OpenApiUtilClient.get_encode_param(pipeline_id)
        body = {}
        if not UtilClient.is_unset(request.users):
            body['Users'] = request.users
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdatePipelinePrivileges',
            version='2021-02-02',
            protocol='HTTPS',
            pathname=f'/api/v1/pipelines/{pipeline_id}/privileges',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiflow_20210202_models.UpdatePipelinePrivilegesResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_pipeline_privileges_with_options_async(
        self,
        pipeline_id: str,
        request: paiflow_20210202_models.UpdatePipelinePrivilegesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiflow_20210202_models.UpdatePipelinePrivilegesResponse:
        UtilClient.validate_model(request)
        pipeline_id = OpenApiUtilClient.get_encode_param(pipeline_id)
        body = {}
        if not UtilClient.is_unset(request.users):
            body['Users'] = request.users
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdatePipelinePrivileges',
            version='2021-02-02',
            protocol='HTTPS',
            pathname=f'/api/v1/pipelines/{pipeline_id}/privileges',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiflow_20210202_models.UpdatePipelinePrivilegesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_run(
        self,
        run_id: str,
        request: paiflow_20210202_models.UpdateRunRequest,
    ) -> paiflow_20210202_models.UpdateRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_run_with_options(run_id, request, headers, runtime)

    async def update_run_async(
        self,
        run_id: str,
        request: paiflow_20210202_models.UpdateRunRequest,
    ) -> paiflow_20210202_models.UpdateRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_run_with_options_async(run_id, request, headers, runtime)

    def update_run_with_options(
        self,
        run_id: str,
        request: paiflow_20210202_models.UpdateRunRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiflow_20210202_models.UpdateRunResponse:
        UtilClient.validate_model(request)
        run_id = OpenApiUtilClient.get_encode_param(run_id)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateRun',
            version='2021-02-02',
            protocol='HTTPS',
            pathname=f'/api/v1/runs/{run_id}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiflow_20210202_models.UpdateRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_run_with_options_async(
        self,
        run_id: str,
        request: paiflow_20210202_models.UpdateRunRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiflow_20210202_models.UpdateRunResponse:
        UtilClient.validate_model(request)
        run_id = OpenApiUtilClient.get_encode_param(run_id)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateRun',
            version='2021-02-02',
            protocol='HTTPS',
            pathname=f'/api/v1/runs/{run_id}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiflow_20210202_models.UpdateRunResponse(),
            await self.call_api_async(params, req, runtime)
        )
