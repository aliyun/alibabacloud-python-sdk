# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations
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
        self._endpoint_rule = ''
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

    def create_pipeline_run_with_options(
        self,
        request: paiflow_20210202_models.CreatePipelineRunRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiflow_20210202_models.CreatePipelineRunResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accessibility):
            body['Accessibility'] = request.accessibility
        if not UtilClient.is_unset(request.arguments):
            body['Arguments'] = request.arguments
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
        if not UtilClient.is_unset(request.source_id):
            body['SourceId'] = request.source_id
        if not UtilClient.is_unset(request.source_type):
            body['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePipelineRun',
            version='2021-02-02',
            protocol='HTTPS',
            pathname=f'/api/v1/pipelineruns',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiflow_20210202_models.CreatePipelineRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_pipeline_run_with_options_async(
        self,
        request: paiflow_20210202_models.CreatePipelineRunRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiflow_20210202_models.CreatePipelineRunResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accessibility):
            body['Accessibility'] = request.accessibility
        if not UtilClient.is_unset(request.arguments):
            body['Arguments'] = request.arguments
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
        if not UtilClient.is_unset(request.source_id):
            body['SourceId'] = request.source_id
        if not UtilClient.is_unset(request.source_type):
            body['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePipelineRun',
            version='2021-02-02',
            protocol='HTTPS',
            pathname=f'/api/v1/pipelineruns',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiflow_20210202_models.CreatePipelineRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_pipeline_run(
        self,
        request: paiflow_20210202_models.CreatePipelineRunRequest,
    ) -> paiflow_20210202_models.CreatePipelineRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_pipeline_run_with_options(request, headers, runtime)

    async def create_pipeline_run_async(
        self,
        request: paiflow_20210202_models.CreatePipelineRunRequest,
    ) -> paiflow_20210202_models.CreatePipelineRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_pipeline_run_with_options_async(request, headers, runtime)

    def delete_pipeline_with_options(
        self,
        pipeline_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiflow_20210202_models.DeletePipelineResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeletePipeline',
            version='2021-02-02',
            protocol='HTTPS',
            pathname=f'/api/v1/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}',
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
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeletePipeline',
            version='2021-02-02',
            protocol='HTTPS',
            pathname=f'/api/v1/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}',
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

    def delete_pipeline_run_with_options(
        self,
        pipeline_run_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiflow_20210202_models.DeletePipelineRunResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeletePipelineRun',
            version='2021-02-02',
            protocol='HTTPS',
            pathname=f'/api/v1/pipelineruns/{OpenApiUtilClient.get_encode_param(pipeline_run_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiflow_20210202_models.DeletePipelineRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_pipeline_run_with_options_async(
        self,
        pipeline_run_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiflow_20210202_models.DeletePipelineRunResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeletePipelineRun',
            version='2021-02-02',
            protocol='HTTPS',
            pathname=f'/api/v1/pipelineruns/{OpenApiUtilClient.get_encode_param(pipeline_run_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiflow_20210202_models.DeletePipelineRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_pipeline_run(
        self,
        pipeline_run_id: str,
    ) -> paiflow_20210202_models.DeletePipelineRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_pipeline_run_with_options(pipeline_run_id, headers, runtime)

    async def delete_pipeline_run_async(
        self,
        pipeline_run_id: str,
    ) -> paiflow_20210202_models.DeletePipelineRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_pipeline_run_with_options_async(pipeline_run_id, headers, runtime)

    def get_pipeline_with_options(
        self,
        pipeline_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiflow_20210202_models.GetPipelineResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetPipeline',
            version='2021-02-02',
            protocol='HTTPS',
            pathname=f'/api/v1/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}',
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
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetPipeline',
            version='2021-02-02',
            protocol='HTTPS',
            pathname=f'/api/v1/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}',
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

    def get_pipeline_run_with_options(
        self,
        pipeline_run_id: str,
        request: paiflow_20210202_models.GetPipelineRunRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiflow_20210202_models.GetPipelineRunResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.manifest_type):
            query['ManifestType'] = request.manifest_type
        if not UtilClient.is_unset(request.token_id):
            query['TokenId'] = request.token_id
        if not UtilClient.is_unset(request.verbose):
            query['Verbose'] = request.verbose
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPipelineRun',
            version='2021-02-02',
            protocol='HTTPS',
            pathname=f'/api/v1/pipelineruns/{OpenApiUtilClient.get_encode_param(pipeline_run_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiflow_20210202_models.GetPipelineRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_pipeline_run_with_options_async(
        self,
        pipeline_run_id: str,
        request: paiflow_20210202_models.GetPipelineRunRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiflow_20210202_models.GetPipelineRunResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.manifest_type):
            query['ManifestType'] = request.manifest_type
        if not UtilClient.is_unset(request.token_id):
            query['TokenId'] = request.token_id
        if not UtilClient.is_unset(request.verbose):
            query['Verbose'] = request.verbose
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPipelineRun',
            version='2021-02-02',
            protocol='HTTPS',
            pathname=f'/api/v1/pipelineruns/{OpenApiUtilClient.get_encode_param(pipeline_run_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiflow_20210202_models.GetPipelineRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_pipeline_run(
        self,
        pipeline_run_id: str,
        request: paiflow_20210202_models.GetPipelineRunRequest,
    ) -> paiflow_20210202_models.GetPipelineRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_pipeline_run_with_options(pipeline_run_id, request, headers, runtime)

    async def get_pipeline_run_async(
        self,
        pipeline_run_id: str,
        request: paiflow_20210202_models.GetPipelineRunRequest,
    ) -> paiflow_20210202_models.GetPipelineRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_pipeline_run_with_options_async(pipeline_run_id, request, headers, runtime)

    def get_pipeline_run_node_with_options(
        self,
        pipeline_run_id: str,
        node_id: str,
        request: paiflow_20210202_models.GetPipelineRunNodeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiflow_20210202_models.GetPipelineRunNodeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.depth):
            query['Depth'] = request.depth
        if not UtilClient.is_unset(request.token_id):
            query['TokenId'] = request.token_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPipelineRunNode',
            version='2021-02-02',
            protocol='HTTPS',
            pathname=f'/api/v1/pipelineruns/{OpenApiUtilClient.get_encode_param(pipeline_run_id)}/nodes/{OpenApiUtilClient.get_encode_param(node_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiflow_20210202_models.GetPipelineRunNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_pipeline_run_node_with_options_async(
        self,
        pipeline_run_id: str,
        node_id: str,
        request: paiflow_20210202_models.GetPipelineRunNodeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiflow_20210202_models.GetPipelineRunNodeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.depth):
            query['Depth'] = request.depth
        if not UtilClient.is_unset(request.token_id):
            query['TokenId'] = request.token_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPipelineRunNode',
            version='2021-02-02',
            protocol='HTTPS',
            pathname=f'/api/v1/pipelineruns/{OpenApiUtilClient.get_encode_param(pipeline_run_id)}/nodes/{OpenApiUtilClient.get_encode_param(node_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiflow_20210202_models.GetPipelineRunNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_pipeline_run_node(
        self,
        pipeline_run_id: str,
        node_id: str,
        request: paiflow_20210202_models.GetPipelineRunNodeRequest,
    ) -> paiflow_20210202_models.GetPipelineRunNodeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_pipeline_run_node_with_options(pipeline_run_id, node_id, request, headers, runtime)

    async def get_pipeline_run_node_async(
        self,
        pipeline_run_id: str,
        node_id: str,
        request: paiflow_20210202_models.GetPipelineRunNodeRequest,
    ) -> paiflow_20210202_models.GetPipelineRunNodeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_pipeline_run_node_with_options_async(pipeline_run_id, node_id, request, headers, runtime)

    def list_pipeline_run_node_logs_with_options(
        self,
        pipeline_run_id: str,
        node_id: str,
        request: paiflow_20210202_models.ListPipelineRunNodeLogsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiflow_20210202_models.ListPipelineRunNodeLogsResponse:
        UtilClient.validate_model(request)
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
        if not UtilClient.is_unset(request.token_id):
            query['TokenId'] = request.token_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPipelineRunNodeLogs',
            version='2021-02-02',
            protocol='HTTPS',
            pathname=f'/api/v1/pipelineruns/{OpenApiUtilClient.get_encode_param(pipeline_run_id)}/nodes/{OpenApiUtilClient.get_encode_param(node_id)}/logs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiflow_20210202_models.ListPipelineRunNodeLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_pipeline_run_node_logs_with_options_async(
        self,
        pipeline_run_id: str,
        node_id: str,
        request: paiflow_20210202_models.ListPipelineRunNodeLogsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiflow_20210202_models.ListPipelineRunNodeLogsResponse:
        UtilClient.validate_model(request)
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
        if not UtilClient.is_unset(request.token_id):
            query['TokenId'] = request.token_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPipelineRunNodeLogs',
            version='2021-02-02',
            protocol='HTTPS',
            pathname=f'/api/v1/pipelineruns/{OpenApiUtilClient.get_encode_param(pipeline_run_id)}/nodes/{OpenApiUtilClient.get_encode_param(node_id)}/logs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiflow_20210202_models.ListPipelineRunNodeLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_pipeline_run_node_logs(
        self,
        pipeline_run_id: str,
        node_id: str,
        request: paiflow_20210202_models.ListPipelineRunNodeLogsRequest,
    ) -> paiflow_20210202_models.ListPipelineRunNodeLogsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_pipeline_run_node_logs_with_options(pipeline_run_id, node_id, request, headers, runtime)

    async def list_pipeline_run_node_logs_async(
        self,
        pipeline_run_id: str,
        node_id: str,
        request: paiflow_20210202_models.ListPipelineRunNodeLogsRequest,
    ) -> paiflow_20210202_models.ListPipelineRunNodeLogsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_pipeline_run_node_logs_with_options_async(pipeline_run_id, node_id, request, headers, runtime)

    def list_pipeline_run_node_outputs_with_options(
        self,
        pipeline_run_id: str,
        node_id: str,
        request: paiflow_20210202_models.ListPipelineRunNodeOutputsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiflow_20210202_models.ListPipelineRunNodeOutputsResponse:
        UtilClient.validate_model(request)
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
        if not UtilClient.is_unset(request.token_id):
            query['TokenId'] = request.token_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPipelineRunNodeOutputs',
            version='2021-02-02',
            protocol='HTTPS',
            pathname=f'/api/v1/pipelineruns/{OpenApiUtilClient.get_encode_param(pipeline_run_id)}/nodes/{OpenApiUtilClient.get_encode_param(node_id)}/outputs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiflow_20210202_models.ListPipelineRunNodeOutputsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_pipeline_run_node_outputs_with_options_async(
        self,
        pipeline_run_id: str,
        node_id: str,
        request: paiflow_20210202_models.ListPipelineRunNodeOutputsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiflow_20210202_models.ListPipelineRunNodeOutputsResponse:
        UtilClient.validate_model(request)
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
        if not UtilClient.is_unset(request.token_id):
            query['TokenId'] = request.token_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPipelineRunNodeOutputs',
            version='2021-02-02',
            protocol='HTTPS',
            pathname=f'/api/v1/pipelineruns/{OpenApiUtilClient.get_encode_param(pipeline_run_id)}/nodes/{OpenApiUtilClient.get_encode_param(node_id)}/outputs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiflow_20210202_models.ListPipelineRunNodeOutputsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_pipeline_run_node_outputs(
        self,
        pipeline_run_id: str,
        node_id: str,
        request: paiflow_20210202_models.ListPipelineRunNodeOutputsRequest,
    ) -> paiflow_20210202_models.ListPipelineRunNodeOutputsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_pipeline_run_node_outputs_with_options(pipeline_run_id, node_id, request, headers, runtime)

    async def list_pipeline_run_node_outputs_async(
        self,
        pipeline_run_id: str,
        node_id: str,
        request: paiflow_20210202_models.ListPipelineRunNodeOutputsRequest,
    ) -> paiflow_20210202_models.ListPipelineRunNodeOutputsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_pipeline_run_node_outputs_with_options_async(pipeline_run_id, node_id, request, headers, runtime)

    def list_pipeline_run_node_status_with_options(
        self,
        pipeline_run_id: str,
        node_id: str,
        request: paiflow_20210202_models.ListPipelineRunNodeStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiflow_20210202_models.ListPipelineRunNodeStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.depth):
            query['Depth'] = request.depth
        if not UtilClient.is_unset(request.token_id):
            query['TokenId'] = request.token_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPipelineRunNodeStatus',
            version='2021-02-02',
            protocol='HTTPS',
            pathname=f'/api/v1/pipelineruns/{OpenApiUtilClient.get_encode_param(pipeline_run_id)}/nodes/{OpenApiUtilClient.get_encode_param(node_id)}/status',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiflow_20210202_models.ListPipelineRunNodeStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_pipeline_run_node_status_with_options_async(
        self,
        pipeline_run_id: str,
        node_id: str,
        request: paiflow_20210202_models.ListPipelineRunNodeStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiflow_20210202_models.ListPipelineRunNodeStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.depth):
            query['Depth'] = request.depth
        if not UtilClient.is_unset(request.token_id):
            query['TokenId'] = request.token_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPipelineRunNodeStatus',
            version='2021-02-02',
            protocol='HTTPS',
            pathname=f'/api/v1/pipelineruns/{OpenApiUtilClient.get_encode_param(pipeline_run_id)}/nodes/{OpenApiUtilClient.get_encode_param(node_id)}/status',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiflow_20210202_models.ListPipelineRunNodeStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_pipeline_run_node_status(
        self,
        pipeline_run_id: str,
        node_id: str,
        request: paiflow_20210202_models.ListPipelineRunNodeStatusRequest,
    ) -> paiflow_20210202_models.ListPipelineRunNodeStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_pipeline_run_node_status_with_options(pipeline_run_id, node_id, request, headers, runtime)

    async def list_pipeline_run_node_status_async(
        self,
        pipeline_run_id: str,
        node_id: str,
        request: paiflow_20210202_models.ListPipelineRunNodeStatusRequest,
    ) -> paiflow_20210202_models.ListPipelineRunNodeStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_pipeline_run_node_status_with_options_async(pipeline_run_id, node_id, request, headers, runtime)

    def list_pipeline_runs_with_options(
        self,
        request: paiflow_20210202_models.ListPipelineRunsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiflow_20210202_models.ListPipelineRunsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.pipeline_ids):
            query['PipelineIds'] = request.pipeline_ids
        if not UtilClient.is_unset(request.pipeline_run_id):
            query['PipelineRunId'] = request.pipeline_run_id
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.source_id):
            query['SourceId'] = request.source_id
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
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
            action='ListPipelineRuns',
            version='2021-02-02',
            protocol='HTTPS',
            pathname=f'/api/v1/pipelineruns',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiflow_20210202_models.ListPipelineRunsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_pipeline_runs_with_options_async(
        self,
        request: paiflow_20210202_models.ListPipelineRunsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiflow_20210202_models.ListPipelineRunsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.pipeline_ids):
            query['PipelineIds'] = request.pipeline_ids
        if not UtilClient.is_unset(request.pipeline_run_id):
            query['PipelineRunId'] = request.pipeline_run_id
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.source_id):
            query['SourceId'] = request.source_id
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
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
            action='ListPipelineRuns',
            version='2021-02-02',
            protocol='HTTPS',
            pathname=f'/api/v1/pipelineruns',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiflow_20210202_models.ListPipelineRunsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_pipeline_runs(
        self,
        request: paiflow_20210202_models.ListPipelineRunsRequest,
    ) -> paiflow_20210202_models.ListPipelineRunsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_pipeline_runs_with_options(request, headers, runtime)

    async def list_pipeline_runs_async(
        self,
        request: paiflow_20210202_models.ListPipelineRunsRequest,
    ) -> paiflow_20210202_models.ListPipelineRunsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_pipeline_runs_with_options_async(request, headers, runtime)

    def list_pipeline_runs_status_with_options(
        self,
        request: paiflow_20210202_models.ListPipelineRunsStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiflow_20210202_models.ListPipelineRunsStatusResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.nodes):
            body['Nodes'] = request.nodes
        if not UtilClient.is_unset(request.output_type):
            body['OutputType'] = request.output_type
        if not UtilClient.is_unset(request.pipeline_runs):
            body['PipelineRuns'] = request.pipeline_runs
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListPipelineRunsStatus',
            version='2021-02-02',
            protocol='HTTPS',
            pathname=f'/api/v1/pipelineruns',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiflow_20210202_models.ListPipelineRunsStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_pipeline_runs_status_with_options_async(
        self,
        request: paiflow_20210202_models.ListPipelineRunsStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiflow_20210202_models.ListPipelineRunsStatusResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.nodes):
            body['Nodes'] = request.nodes
        if not UtilClient.is_unset(request.output_type):
            body['OutputType'] = request.output_type
        if not UtilClient.is_unset(request.pipeline_runs):
            body['PipelineRuns'] = request.pipeline_runs
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListPipelineRunsStatus',
            version='2021-02-02',
            protocol='HTTPS',
            pathname=f'/api/v1/pipelineruns',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiflow_20210202_models.ListPipelineRunsStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_pipeline_runs_status(
        self,
        request: paiflow_20210202_models.ListPipelineRunsStatusRequest,
    ) -> paiflow_20210202_models.ListPipelineRunsStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_pipeline_runs_status_with_options(request, headers, runtime)

    async def list_pipeline_runs_status_async(
        self,
        request: paiflow_20210202_models.ListPipelineRunsStatusRequest,
    ) -> paiflow_20210202_models.ListPipelineRunsStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_pipeline_runs_status_with_options_async(request, headers, runtime)

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

    def rerun_pipeline_run_with_options(
        self,
        pipeline_run_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiflow_20210202_models.RerunPipelineRunResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RerunPipelineRun',
            version='2021-02-02',
            protocol='HTTPS',
            pathname=f'/api/v1/pipelineruns/{OpenApiUtilClient.get_encode_param(pipeline_run_id)}/rerun',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiflow_20210202_models.RerunPipelineRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def rerun_pipeline_run_with_options_async(
        self,
        pipeline_run_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiflow_20210202_models.RerunPipelineRunResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RerunPipelineRun',
            version='2021-02-02',
            protocol='HTTPS',
            pathname=f'/api/v1/pipelineruns/{OpenApiUtilClient.get_encode_param(pipeline_run_id)}/rerun',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiflow_20210202_models.RerunPipelineRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rerun_pipeline_run(
        self,
        pipeline_run_id: str,
    ) -> paiflow_20210202_models.RerunPipelineRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.rerun_pipeline_run_with_options(pipeline_run_id, headers, runtime)

    async def rerun_pipeline_run_async(
        self,
        pipeline_run_id: str,
    ) -> paiflow_20210202_models.RerunPipelineRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.rerun_pipeline_run_with_options_async(pipeline_run_id, headers, runtime)

    def start_pipeline_run_with_options(
        self,
        pipeline_run_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiflow_20210202_models.StartPipelineRunResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StartPipelineRun',
            version='2021-02-02',
            protocol='HTTPS',
            pathname=f'/api/v1/pipelineruns/{OpenApiUtilClient.get_encode_param(pipeline_run_id)}/start',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiflow_20210202_models.StartPipelineRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_pipeline_run_with_options_async(
        self,
        pipeline_run_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiflow_20210202_models.StartPipelineRunResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StartPipelineRun',
            version='2021-02-02',
            protocol='HTTPS',
            pathname=f'/api/v1/pipelineruns/{OpenApiUtilClient.get_encode_param(pipeline_run_id)}/start',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiflow_20210202_models.StartPipelineRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_pipeline_run(
        self,
        pipeline_run_id: str,
    ) -> paiflow_20210202_models.StartPipelineRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_pipeline_run_with_options(pipeline_run_id, headers, runtime)

    async def start_pipeline_run_async(
        self,
        pipeline_run_id: str,
    ) -> paiflow_20210202_models.StartPipelineRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.start_pipeline_run_with_options_async(pipeline_run_id, headers, runtime)

    def terminate_pipeline_run_with_options(
        self,
        pipeline_run_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiflow_20210202_models.TerminatePipelineRunResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='TerminatePipelineRun',
            version='2021-02-02',
            protocol='HTTPS',
            pathname=f'/api/v1/pipelineruns/{OpenApiUtilClient.get_encode_param(pipeline_run_id)}/termination',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiflow_20210202_models.TerminatePipelineRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def terminate_pipeline_run_with_options_async(
        self,
        pipeline_run_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiflow_20210202_models.TerminatePipelineRunResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='TerminatePipelineRun',
            version='2021-02-02',
            protocol='HTTPS',
            pathname=f'/api/v1/pipelineruns/{OpenApiUtilClient.get_encode_param(pipeline_run_id)}/termination',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiflow_20210202_models.TerminatePipelineRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def terminate_pipeline_run(
        self,
        pipeline_run_id: str,
    ) -> paiflow_20210202_models.TerminatePipelineRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.terminate_pipeline_run_with_options(pipeline_run_id, headers, runtime)

    async def terminate_pipeline_run_async(
        self,
        pipeline_run_id: str,
    ) -> paiflow_20210202_models.TerminatePipelineRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.terminate_pipeline_run_with_options_async(pipeline_run_id, headers, runtime)

    def update_pipeline_with_options(
        self,
        pipeline_id: str,
        request: paiflow_20210202_models.UpdatePipelineRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiflow_20210202_models.UpdatePipelineResponse:
        UtilClient.validate_model(request)
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
            pathname=f'/api/v1/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}',
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
            pathname=f'/api/v1/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}',
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

    def update_pipeline_run_with_options(
        self,
        pipeline_run_id: str,
        request: paiflow_20210202_models.UpdatePipelineRunRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiflow_20210202_models.UpdatePipelineRunResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdatePipelineRun',
            version='2021-02-02',
            protocol='HTTPS',
            pathname=f'/api/v1/pipelineruns/{OpenApiUtilClient.get_encode_param(pipeline_run_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiflow_20210202_models.UpdatePipelineRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_pipeline_run_with_options_async(
        self,
        pipeline_run_id: str,
        request: paiflow_20210202_models.UpdatePipelineRunRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiflow_20210202_models.UpdatePipelineRunResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdatePipelineRun',
            version='2021-02-02',
            protocol='HTTPS',
            pathname=f'/api/v1/pipelineruns/{OpenApiUtilClient.get_encode_param(pipeline_run_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiflow_20210202_models.UpdatePipelineRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_pipeline_run(
        self,
        pipeline_run_id: str,
        request: paiflow_20210202_models.UpdatePipelineRunRequest,
    ) -> paiflow_20210202_models.UpdatePipelineRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_pipeline_run_with_options(pipeline_run_id, request, headers, runtime)

    async def update_pipeline_run_async(
        self,
        pipeline_run_id: str,
        request: paiflow_20210202_models.UpdatePipelineRunRequest,
    ) -> paiflow_20210202_models.UpdatePipelineRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_pipeline_run_with_options_async(pipeline_run_id, request, headers, runtime)
