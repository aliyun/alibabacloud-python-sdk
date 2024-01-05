# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_igraph20210621 import models as igraph_20210621_models
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
        self._endpoint = self.get_endpoint('igraph', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_graph_with_options(
        self,
        instance_id: str,
        graph_name: str,
        request: igraph_20210621_models.CreateGraphRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> igraph_20210621_models.CreateGraphResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace):
            query['namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='CreateGraph',
            version='2021-06-21',
            protocol='HTTPS',
            pathname=f'/openapi/igraph/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/graphs/{OpenApiUtilClient.get_encode_param(graph_name)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            igraph_20210621_models.CreateGraphResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_graph_with_options_async(
        self,
        instance_id: str,
        graph_name: str,
        request: igraph_20210621_models.CreateGraphRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> igraph_20210621_models.CreateGraphResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace):
            query['namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='CreateGraph',
            version='2021-06-21',
            protocol='HTTPS',
            pathname=f'/openapi/igraph/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/graphs/{OpenApiUtilClient.get_encode_param(graph_name)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            igraph_20210621_models.CreateGraphResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_graph(
        self,
        instance_id: str,
        graph_name: str,
        request: igraph_20210621_models.CreateGraphRequest,
    ) -> igraph_20210621_models.CreateGraphResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_graph_with_options(instance_id, graph_name, request, headers, runtime)

    async def create_graph_async(
        self,
        instance_id: str,
        graph_name: str,
        request: igraph_20210621_models.CreateGraphRequest,
    ) -> igraph_20210621_models.CreateGraphResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_graph_with_options_async(instance_id, graph_name, request, headers, runtime)

    def create_graph_schema_with_options(
        self,
        instance_id: str,
        graph_name: str,
        request: igraph_20210621_models.CreateGraphSchemaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> igraph_20210621_models.CreateGraphSchemaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace):
            query['namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='CreateGraphSchema',
            version='2021-06-21',
            protocol='HTTPS',
            pathname=f'/openapi/igraph/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/graphs/{OpenApiUtilClient.get_encode_param(graph_name)}/schemas',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            igraph_20210621_models.CreateGraphSchemaResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_graph_schema_with_options_async(
        self,
        instance_id: str,
        graph_name: str,
        request: igraph_20210621_models.CreateGraphSchemaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> igraph_20210621_models.CreateGraphSchemaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace):
            query['namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='CreateGraphSchema',
            version='2021-06-21',
            protocol='HTTPS',
            pathname=f'/openapi/igraph/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/graphs/{OpenApiUtilClient.get_encode_param(graph_name)}/schemas',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            igraph_20210621_models.CreateGraphSchemaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_graph_schema(
        self,
        instance_id: str,
        graph_name: str,
        request: igraph_20210621_models.CreateGraphSchemaRequest,
    ) -> igraph_20210621_models.CreateGraphSchemaResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_graph_schema_with_options(instance_id, graph_name, request, headers, runtime)

    async def create_graph_schema_async(
        self,
        instance_id: str,
        graph_name: str,
        request: igraph_20210621_models.CreateGraphSchemaRequest,
    ) -> igraph_20210621_models.CreateGraphSchemaResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_graph_schema_with_options_async(instance_id, graph_name, request, headers, runtime)

    def delete_graph_with_options(
        self,
        instance_id: str,
        graph_name: str,
        request: igraph_20210621_models.DeleteGraphRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> igraph_20210621_models.DeleteGraphResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace):
            query['namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGraph',
            version='2021-06-21',
            protocol='HTTPS',
            pathname=f'/openapi/igraph/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/graphs/{OpenApiUtilClient.get_encode_param(graph_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            igraph_20210621_models.DeleteGraphResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_graph_with_options_async(
        self,
        instance_id: str,
        graph_name: str,
        request: igraph_20210621_models.DeleteGraphRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> igraph_20210621_models.DeleteGraphResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace):
            query['namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGraph',
            version='2021-06-21',
            protocol='HTTPS',
            pathname=f'/openapi/igraph/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/graphs/{OpenApiUtilClient.get_encode_param(graph_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            igraph_20210621_models.DeleteGraphResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_graph(
        self,
        instance_id: str,
        graph_name: str,
        request: igraph_20210621_models.DeleteGraphRequest,
    ) -> igraph_20210621_models.DeleteGraphResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_graph_with_options(instance_id, graph_name, request, headers, runtime)

    async def delete_graph_async(
        self,
        instance_id: str,
        graph_name: str,
        request: igraph_20210621_models.DeleteGraphRequest,
    ) -> igraph_20210621_models.DeleteGraphResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_graph_with_options_async(instance_id, graph_name, request, headers, runtime)

    def get_graph_with_options(
        self,
        instance_id: str,
        graph_name: str,
        request: igraph_20210621_models.GetGraphRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> igraph_20210621_models.GetGraphResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace):
            query['namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetGraph',
            version='2021-06-21',
            protocol='HTTPS',
            pathname=f'/openapi/igraph/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/graphs/{OpenApiUtilClient.get_encode_param(graph_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            igraph_20210621_models.GetGraphResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_graph_with_options_async(
        self,
        instance_id: str,
        graph_name: str,
        request: igraph_20210621_models.GetGraphRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> igraph_20210621_models.GetGraphResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace):
            query['namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetGraph',
            version='2021-06-21',
            protocol='HTTPS',
            pathname=f'/openapi/igraph/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/graphs/{OpenApiUtilClient.get_encode_param(graph_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            igraph_20210621_models.GetGraphResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_graph(
        self,
        instance_id: str,
        graph_name: str,
        request: igraph_20210621_models.GetGraphRequest,
    ) -> igraph_20210621_models.GetGraphResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_graph_with_options(instance_id, graph_name, request, headers, runtime)

    async def get_graph_async(
        self,
        instance_id: str,
        graph_name: str,
        request: igraph_20210621_models.GetGraphRequest,
    ) -> igraph_20210621_models.GetGraphResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_graph_with_options_async(instance_id, graph_name, request, headers, runtime)

    def get_graph_schema_with_options(
        self,
        instance_id: str,
        graph_name: str,
        graph_schema_name: str,
        request: igraph_20210621_models.GetGraphSchemaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> igraph_20210621_models.GetGraphSchemaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace):
            query['namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetGraphSchema',
            version='2021-06-21',
            protocol='HTTPS',
            pathname=f'/openapi/igraph/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/graphs/{OpenApiUtilClient.get_encode_param(graph_name)}/schemas/{OpenApiUtilClient.get_encode_param(graph_schema_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            igraph_20210621_models.GetGraphSchemaResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_graph_schema_with_options_async(
        self,
        instance_id: str,
        graph_name: str,
        graph_schema_name: str,
        request: igraph_20210621_models.GetGraphSchemaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> igraph_20210621_models.GetGraphSchemaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace):
            query['namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetGraphSchema',
            version='2021-06-21',
            protocol='HTTPS',
            pathname=f'/openapi/igraph/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/graphs/{OpenApiUtilClient.get_encode_param(graph_name)}/schemas/{OpenApiUtilClient.get_encode_param(graph_schema_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            igraph_20210621_models.GetGraphSchemaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_graph_schema(
        self,
        instance_id: str,
        graph_name: str,
        graph_schema_name: str,
        request: igraph_20210621_models.GetGraphSchemaRequest,
    ) -> igraph_20210621_models.GetGraphSchemaResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_graph_schema_with_options(instance_id, graph_name, graph_schema_name, request, headers, runtime)

    async def get_graph_schema_async(
        self,
        instance_id: str,
        graph_name: str,
        graph_schema_name: str,
        request: igraph_20210621_models.GetGraphSchemaRequest,
    ) -> igraph_20210621_models.GetGraphSchemaResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_graph_schema_with_options_async(instance_id, graph_name, graph_schema_name, request, headers, runtime)

    def get_igraph_label_back_flow_with_options(
        self,
        graph_name: str,
        instance_id: str,
        label_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> igraph_20210621_models.GetIgraphLabelBackFlowResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetIgraphLabelBackFlow',
            version='2021-06-21',
            protocol='HTTPS',
            pathname=f'/openapi/igraph/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/graphs/{OpenApiUtilClient.get_encode_param(graph_name)}/label/{OpenApiUtilClient.get_encode_param(label_name)}/backflow',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            igraph_20210621_models.GetIgraphLabelBackFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_igraph_label_back_flow_with_options_async(
        self,
        graph_name: str,
        instance_id: str,
        label_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> igraph_20210621_models.GetIgraphLabelBackFlowResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetIgraphLabelBackFlow',
            version='2021-06-21',
            protocol='HTTPS',
            pathname=f'/openapi/igraph/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/graphs/{OpenApiUtilClient.get_encode_param(graph_name)}/label/{OpenApiUtilClient.get_encode_param(label_name)}/backflow',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            igraph_20210621_models.GetIgraphLabelBackFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_igraph_label_back_flow(
        self,
        graph_name: str,
        instance_id: str,
        label_name: str,
    ) -> igraph_20210621_models.GetIgraphLabelBackFlowResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_igraph_label_back_flow_with_options(graph_name, instance_id, label_name, headers, runtime)

    async def get_igraph_label_back_flow_async(
        self,
        graph_name: str,
        instance_id: str,
        label_name: str,
    ) -> igraph_20210621_models.GetIgraphLabelBackFlowResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_igraph_label_back_flow_with_options_async(graph_name, instance_id, label_name, headers, runtime)

    def get_igraph_label_last_backflow_with_options(
        self,
        instance_id: str,
        graph_name: str,
        label_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> igraph_20210621_models.GetIgraphLabelLastBackflowResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetIgraphLabelLastBackflow',
            version='2021-06-21',
            protocol='HTTPS',
            pathname=f'/openapi/igraph/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/graphs/{OpenApiUtilClient.get_encode_param(graph_name)}/label/{OpenApiUtilClient.get_encode_param(label_name)}/backflow/last',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            igraph_20210621_models.GetIgraphLabelLastBackflowResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_igraph_label_last_backflow_with_options_async(
        self,
        instance_id: str,
        graph_name: str,
        label_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> igraph_20210621_models.GetIgraphLabelLastBackflowResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetIgraphLabelLastBackflow',
            version='2021-06-21',
            protocol='HTTPS',
            pathname=f'/openapi/igraph/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/graphs/{OpenApiUtilClient.get_encode_param(graph_name)}/label/{OpenApiUtilClient.get_encode_param(label_name)}/backflow/last',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            igraph_20210621_models.GetIgraphLabelLastBackflowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_igraph_label_last_backflow(
        self,
        instance_id: str,
        graph_name: str,
        label_name: str,
    ) -> igraph_20210621_models.GetIgraphLabelLastBackflowResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_igraph_label_last_backflow_with_options(instance_id, graph_name, label_name, headers, runtime)

    async def get_igraph_label_last_backflow_async(
        self,
        instance_id: str,
        graph_name: str,
        label_name: str,
    ) -> igraph_20210621_models.GetIgraphLabelLastBackflowResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_igraph_label_last_backflow_with_options_async(instance_id, graph_name, label_name, headers, runtime)

    def get_igraph_table_detail_with_options(
        self,
        instance_id: str,
        graph_name: str,
        table_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> igraph_20210621_models.GetIgraphTableDetailResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetIgraphTableDetail',
            version='2021-06-21',
            protocol='HTTPS',
            pathname=f'/openapi/igraph/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/graphs/{OpenApiUtilClient.get_encode_param(graph_name)}/tables/{OpenApiUtilClient.get_encode_param(table_name)}/detail',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            igraph_20210621_models.GetIgraphTableDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_igraph_table_detail_with_options_async(
        self,
        instance_id: str,
        graph_name: str,
        table_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> igraph_20210621_models.GetIgraphTableDetailResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetIgraphTableDetail',
            version='2021-06-21',
            protocol='HTTPS',
            pathname=f'/openapi/igraph/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/graphs/{OpenApiUtilClient.get_encode_param(graph_name)}/tables/{OpenApiUtilClient.get_encode_param(table_name)}/detail',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            igraph_20210621_models.GetIgraphTableDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_igraph_table_detail(
        self,
        instance_id: str,
        graph_name: str,
        table_name: str,
    ) -> igraph_20210621_models.GetIgraphTableDetailResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_igraph_table_detail_with_options(instance_id, graph_name, table_name, headers, runtime)

    async def get_igraph_table_detail_async(
        self,
        instance_id: str,
        graph_name: str,
        table_name: str,
    ) -> igraph_20210621_models.GetIgraphTableDetailResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_igraph_table_detail_with_options_async(instance_id, graph_name, table_name, headers, runtime)

    def get_igraph_tables_back_flow_with_options(
        self,
        instance_id: str,
        graph_name: str,
        request: igraph_20210621_models.GetIgraphTablesBackFlowRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> igraph_20210621_models.GetIgraphTablesBackFlowResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace):
            query['namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetIgraphTablesBackFlow',
            version='2021-06-21',
            protocol='HTTPS',
            pathname=f'/openapi/igraph/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/graphs/{OpenApiUtilClient.get_encode_param(graph_name)}/backflows',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            igraph_20210621_models.GetIgraphTablesBackFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_igraph_tables_back_flow_with_options_async(
        self,
        instance_id: str,
        graph_name: str,
        request: igraph_20210621_models.GetIgraphTablesBackFlowRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> igraph_20210621_models.GetIgraphTablesBackFlowResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace):
            query['namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetIgraphTablesBackFlow',
            version='2021-06-21',
            protocol='HTTPS',
            pathname=f'/openapi/igraph/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/graphs/{OpenApiUtilClient.get_encode_param(graph_name)}/backflows',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            igraph_20210621_models.GetIgraphTablesBackFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_igraph_tables_back_flow(
        self,
        instance_id: str,
        graph_name: str,
        request: igraph_20210621_models.GetIgraphTablesBackFlowRequest,
    ) -> igraph_20210621_models.GetIgraphTablesBackFlowResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_igraph_tables_back_flow_with_options(instance_id, graph_name, request, headers, runtime)

    async def get_igraph_tables_back_flow_async(
        self,
        instance_id: str,
        graph_name: str,
        request: igraph_20210621_models.GetIgraphTablesBackFlowRequest,
    ) -> igraph_20210621_models.GetIgraphTablesBackFlowResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_igraph_tables_back_flow_with_options_async(instance_id, graph_name, request, headers, runtime)

    def get_instance_with_options(
        self,
        instance_id: str,
        request: igraph_20210621_models.GetInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> igraph_20210621_models.GetInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace):
            query['namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstance',
            version='2021-06-21',
            protocol='HTTPS',
            pathname=f'/openapi/igraph/instances/{OpenApiUtilClient.get_encode_param(instance_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            igraph_20210621_models.GetInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_with_options_async(
        self,
        instance_id: str,
        request: igraph_20210621_models.GetInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> igraph_20210621_models.GetInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace):
            query['namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstance',
            version='2021-06-21',
            protocol='HTTPS',
            pathname=f'/openapi/igraph/instances/{OpenApiUtilClient.get_encode_param(instance_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            igraph_20210621_models.GetInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance(
        self,
        instance_id: str,
        request: igraph_20210621_models.GetInstanceRequest,
    ) -> igraph_20210621_models.GetInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_instance_with_options(instance_id, request, headers, runtime)

    async def get_instance_async(
        self,
        instance_id: str,
        request: igraph_20210621_models.GetInstanceRequest,
    ) -> igraph_20210621_models.GetInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_instance_with_options_async(instance_id, request, headers, runtime)

    def get_instance_digest_with_options(
        self,
        instance_id: str,
        request: igraph_20210621_models.GetInstanceDigestRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> igraph_20210621_models.GetInstanceDigestResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace):
            query['namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstanceDigest',
            version='2021-06-21',
            protocol='HTTPS',
            pathname=f'/openapi/igraph/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/digest',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            igraph_20210621_models.GetInstanceDigestResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_digest_with_options_async(
        self,
        instance_id: str,
        request: igraph_20210621_models.GetInstanceDigestRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> igraph_20210621_models.GetInstanceDigestResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace):
            query['namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstanceDigest',
            version='2021-06-21',
            protocol='HTTPS',
            pathname=f'/openapi/igraph/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/digest',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            igraph_20210621_models.GetInstanceDigestResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance_digest(
        self,
        instance_id: str,
        request: igraph_20210621_models.GetInstanceDigestRequest,
    ) -> igraph_20210621_models.GetInstanceDigestResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_instance_digest_with_options(instance_id, request, headers, runtime)

    async def get_instance_digest_async(
        self,
        instance_id: str,
        request: igraph_20210621_models.GetInstanceDigestRequest,
    ) -> igraph_20210621_models.GetInstanceDigestResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_instance_digest_with_options_async(instance_id, request, headers, runtime)

    def get_table_detail_with_options(
        self,
        instance_id: str,
        table_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> igraph_20210621_models.GetTableDetailResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTableDetail',
            version='2021-06-21',
            protocol='HTTPS',
            pathname=f'/openapi/igraph/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/tables/{OpenApiUtilClient.get_encode_param(table_name)}/detail',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            igraph_20210621_models.GetTableDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_table_detail_with_options_async(
        self,
        instance_id: str,
        table_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> igraph_20210621_models.GetTableDetailResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTableDetail',
            version='2021-06-21',
            protocol='HTTPS',
            pathname=f'/openapi/igraph/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/tables/{OpenApiUtilClient.get_encode_param(table_name)}/detail',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            igraph_20210621_models.GetTableDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_table_detail(
        self,
        instance_id: str,
        table_name: str,
    ) -> igraph_20210621_models.GetTableDetailResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_table_detail_with_options(instance_id, table_name, headers, runtime)

    async def get_table_detail_async(
        self,
        instance_id: str,
        table_name: str,
    ) -> igraph_20210621_models.GetTableDetailResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_table_detail_with_options_async(instance_id, table_name, headers, runtime)

    def get_table_last_backflow_with_options(
        self,
        instance_id: str,
        table_name: str,
        request: igraph_20210621_models.GetTableLastBackflowRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> igraph_20210621_models.GetTableLastBackflowResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.partition):
            query['partition'] = request.partition
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTableLastBackflow',
            version='2021-06-21',
            protocol='HTTPS',
            pathname=f'/openapi/igraph/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/table/{OpenApiUtilClient.get_encode_param(table_name)}/backflow/last',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            igraph_20210621_models.GetTableLastBackflowResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_table_last_backflow_with_options_async(
        self,
        instance_id: str,
        table_name: str,
        request: igraph_20210621_models.GetTableLastBackflowRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> igraph_20210621_models.GetTableLastBackflowResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.partition):
            query['partition'] = request.partition
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTableLastBackflow',
            version='2021-06-21',
            protocol='HTTPS',
            pathname=f'/openapi/igraph/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/table/{OpenApiUtilClient.get_encode_param(table_name)}/backflow/last',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            igraph_20210621_models.GetTableLastBackflowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_table_last_backflow(
        self,
        instance_id: str,
        table_name: str,
        request: igraph_20210621_models.GetTableLastBackflowRequest,
    ) -> igraph_20210621_models.GetTableLastBackflowResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_table_last_backflow_with_options(instance_id, table_name, request, headers, runtime)

    async def get_table_last_backflow_async(
        self,
        instance_id: str,
        table_name: str,
        request: igraph_20210621_models.GetTableLastBackflowRequest,
    ) -> igraph_20210621_models.GetTableLastBackflowResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_table_last_backflow_with_options_async(instance_id, table_name, request, headers, runtime)

    def list_demo_graph_schemas_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> igraph_20210621_models.ListDemoGraphSchemasResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListDemoGraphSchemas',
            version='2021-06-21',
            protocol='HTTPS',
            pathname=f'/openapi/igraph/instances/demo/schemas',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            igraph_20210621_models.ListDemoGraphSchemasResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_demo_graph_schemas_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> igraph_20210621_models.ListDemoGraphSchemasResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListDemoGraphSchemas',
            version='2021-06-21',
            protocol='HTTPS',
            pathname=f'/openapi/igraph/instances/demo/schemas',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            igraph_20210621_models.ListDemoGraphSchemasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_demo_graph_schemas(self) -> igraph_20210621_models.ListDemoGraphSchemasResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_demo_graph_schemas_with_options(headers, runtime)

    async def list_demo_graph_schemas_async(self) -> igraph_20210621_models.ListDemoGraphSchemasResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_demo_graph_schemas_with_options_async(headers, runtime)

    def list_graph_schemas_with_options(
        self,
        instance_id: str,
        graph_name: str,
        request: igraph_20210621_models.ListGraphSchemasRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> igraph_20210621_models.ListGraphSchemasResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace):
            query['namespace'] = request.namespace
        if not UtilClient.is_unset(request.page_limit):
            query['pageLimit'] = request.page_limit
        if not UtilClient.is_unset(request.page_start):
            query['pageStart'] = request.page_start
        if not UtilClient.is_unset(request.return_spec):
            query['returnSpec'] = request.return_spec
        if not UtilClient.is_unset(request.schema_status):
            query['schemaStatus'] = request.schema_status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGraphSchemas',
            version='2021-06-21',
            protocol='HTTPS',
            pathname=f'/openapi/igraph/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/graphs/{OpenApiUtilClient.get_encode_param(graph_name)}/schemas',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            igraph_20210621_models.ListGraphSchemasResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_graph_schemas_with_options_async(
        self,
        instance_id: str,
        graph_name: str,
        request: igraph_20210621_models.ListGraphSchemasRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> igraph_20210621_models.ListGraphSchemasResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace):
            query['namespace'] = request.namespace
        if not UtilClient.is_unset(request.page_limit):
            query['pageLimit'] = request.page_limit
        if not UtilClient.is_unset(request.page_start):
            query['pageStart'] = request.page_start
        if not UtilClient.is_unset(request.return_spec):
            query['returnSpec'] = request.return_spec
        if not UtilClient.is_unset(request.schema_status):
            query['schemaStatus'] = request.schema_status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGraphSchemas',
            version='2021-06-21',
            protocol='HTTPS',
            pathname=f'/openapi/igraph/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/graphs/{OpenApiUtilClient.get_encode_param(graph_name)}/schemas',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            igraph_20210621_models.ListGraphSchemasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_graph_schemas(
        self,
        instance_id: str,
        graph_name: str,
        request: igraph_20210621_models.ListGraphSchemasRequest,
    ) -> igraph_20210621_models.ListGraphSchemasResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_graph_schemas_with_options(instance_id, graph_name, request, headers, runtime)

    async def list_graph_schemas_async(
        self,
        instance_id: str,
        graph_name: str,
        request: igraph_20210621_models.ListGraphSchemasRequest,
    ) -> igraph_20210621_models.ListGraphSchemasResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_graph_schemas_with_options_async(instance_id, graph_name, request, headers, runtime)

    def list_igraph_instances_with_options(
        self,
        tmp_req: igraph_20210621_models.ListIgraphInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> igraph_20210621_models.ListIgraphInstancesResponse:
        UtilClient.validate_model(tmp_req)
        request = igraph_20210621_models.ListIgraphInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.page_continue):
            query['pageContinue'] = request.page_continue
        if not UtilClient.is_unset(request.page_limit):
            query['pageLimit'] = request.page_limit
        if not UtilClient.is_unset(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tags_shrink):
            query['tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIgraphInstances',
            version='2021-06-21',
            protocol='HTTPS',
            pathname=f'/openapi/igraph/instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            igraph_20210621_models.ListIgraphInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_igraph_instances_with_options_async(
        self,
        tmp_req: igraph_20210621_models.ListIgraphInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> igraph_20210621_models.ListIgraphInstancesResponse:
        UtilClient.validate_model(tmp_req)
        request = igraph_20210621_models.ListIgraphInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.page_continue):
            query['pageContinue'] = request.page_continue
        if not UtilClient.is_unset(request.page_limit):
            query['pageLimit'] = request.page_limit
        if not UtilClient.is_unset(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tags_shrink):
            query['tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIgraphInstances',
            version='2021-06-21',
            protocol='HTTPS',
            pathname=f'/openapi/igraph/instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            igraph_20210621_models.ListIgraphInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_igraph_instances(
        self,
        request: igraph_20210621_models.ListIgraphInstancesRequest,
    ) -> igraph_20210621_models.ListIgraphInstancesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_igraph_instances_with_options(request, headers, runtime)

    async def list_igraph_instances_async(
        self,
        request: igraph_20210621_models.ListIgraphInstancesRequest,
    ) -> igraph_20210621_models.ListIgraphInstancesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_igraph_instances_with_options_async(request, headers, runtime)

    def list_instance_graph_with_options(
        self,
        instance_id: str,
        request: igraph_20210621_models.ListInstanceGraphRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> igraph_20210621_models.ListInstanceGraphResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace):
            query['namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstanceGraph',
            version='2021-06-21',
            protocol='HTTPS',
            pathname=f'/openapi/igraph/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/graphs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            igraph_20210621_models.ListInstanceGraphResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instance_graph_with_options_async(
        self,
        instance_id: str,
        request: igraph_20210621_models.ListInstanceGraphRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> igraph_20210621_models.ListInstanceGraphResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace):
            query['namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstanceGraph',
            version='2021-06-21',
            protocol='HTTPS',
            pathname=f'/openapi/igraph/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/graphs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            igraph_20210621_models.ListInstanceGraphResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instance_graph(
        self,
        instance_id: str,
        request: igraph_20210621_models.ListInstanceGraphRequest,
    ) -> igraph_20210621_models.ListInstanceGraphResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_instance_graph_with_options(instance_id, request, headers, runtime)

    async def list_instance_graph_async(
        self,
        instance_id: str,
        request: igraph_20210621_models.ListInstanceGraphRequest,
    ) -> igraph_20210621_models.ListInstanceGraphResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_instance_graph_with_options_async(instance_id, request, headers, runtime)

    def publish_graph_schema_with_options(
        self,
        instance_id: str,
        graph_name: str,
        graph_schema_name: str,
        request: igraph_20210621_models.PublishGraphSchemaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> igraph_20210621_models.PublishGraphSchemaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace):
            query['namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PublishGraphSchema',
            version='2021-06-21',
            protocol='HTTPS',
            pathname=f'/openapi/igraph/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/graphs/{OpenApiUtilClient.get_encode_param(graph_name)}/schemas/{OpenApiUtilClient.get_encode_param(graph_schema_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            igraph_20210621_models.PublishGraphSchemaResponse(),
            self.call_api(params, req, runtime)
        )

    async def publish_graph_schema_with_options_async(
        self,
        instance_id: str,
        graph_name: str,
        graph_schema_name: str,
        request: igraph_20210621_models.PublishGraphSchemaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> igraph_20210621_models.PublishGraphSchemaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace):
            query['namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PublishGraphSchema',
            version='2021-06-21',
            protocol='HTTPS',
            pathname=f'/openapi/igraph/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/graphs/{OpenApiUtilClient.get_encode_param(graph_name)}/schemas/{OpenApiUtilClient.get_encode_param(graph_schema_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            igraph_20210621_models.PublishGraphSchemaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def publish_graph_schema(
        self,
        instance_id: str,
        graph_name: str,
        graph_schema_name: str,
        request: igraph_20210621_models.PublishGraphSchemaRequest,
    ) -> igraph_20210621_models.PublishGraphSchemaResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.publish_graph_schema_with_options(instance_id, graph_name, graph_schema_name, request, headers, runtime)

    async def publish_graph_schema_async(
        self,
        instance_id: str,
        graph_name: str,
        graph_schema_name: str,
        request: igraph_20210621_models.PublishGraphSchemaRequest,
    ) -> igraph_20210621_models.PublishGraphSchemaResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.publish_graph_schema_with_options_async(instance_id, graph_name, graph_schema_name, request, headers, runtime)

    def search_igraph_demo_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> igraph_20210621_models.SearchIgraphDemoResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='SearchIgraphDemo',
            version='2021-06-21',
            protocol='HTTPS',
            pathname=f'/openapi/igraph/tool/actions/search_demo',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            igraph_20210621_models.SearchIgraphDemoResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_igraph_demo_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> igraph_20210621_models.SearchIgraphDemoResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='SearchIgraphDemo',
            version='2021-06-21',
            protocol='HTTPS',
            pathname=f'/openapi/igraph/tool/actions/search_demo',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            igraph_20210621_models.SearchIgraphDemoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_igraph_demo(self) -> igraph_20210621_models.SearchIgraphDemoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.search_igraph_demo_with_options(headers, runtime)

    async def search_igraph_demo_async(self) -> igraph_20210621_models.SearchIgraphDemoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.search_igraph_demo_with_options_async(headers, runtime)

    def trigger_label_backflow_with_options(
        self,
        instance_id: str,
        graph_name: str,
        label_name: str,
        request: igraph_20210621_models.TriggerLabelBackflowRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> igraph_20210621_models.TriggerLabelBackflowResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.odps_partition):
            query['odpsPartition'] = request.odps_partition
        if not UtilClient.is_unset(request.timestamp):
            query['timestamp'] = request.timestamp
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TriggerLabelBackflow',
            version='2021-06-21',
            protocol='HTTPS',
            pathname=f'/openapi/igraph/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/graphs/{OpenApiUtilClient.get_encode_param(graph_name)}/label/{OpenApiUtilClient.get_encode_param(label_name)}/backflow',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            igraph_20210621_models.TriggerLabelBackflowResponse(),
            self.call_api(params, req, runtime)
        )

    async def trigger_label_backflow_with_options_async(
        self,
        instance_id: str,
        graph_name: str,
        label_name: str,
        request: igraph_20210621_models.TriggerLabelBackflowRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> igraph_20210621_models.TriggerLabelBackflowResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.odps_partition):
            query['odpsPartition'] = request.odps_partition
        if not UtilClient.is_unset(request.timestamp):
            query['timestamp'] = request.timestamp
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TriggerLabelBackflow',
            version='2021-06-21',
            protocol='HTTPS',
            pathname=f'/openapi/igraph/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/graphs/{OpenApiUtilClient.get_encode_param(graph_name)}/label/{OpenApiUtilClient.get_encode_param(label_name)}/backflow',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            igraph_20210621_models.TriggerLabelBackflowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def trigger_label_backflow(
        self,
        instance_id: str,
        graph_name: str,
        label_name: str,
        request: igraph_20210621_models.TriggerLabelBackflowRequest,
    ) -> igraph_20210621_models.TriggerLabelBackflowResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.trigger_label_backflow_with_options(instance_id, graph_name, label_name, request, headers, runtime)

    async def trigger_label_backflow_async(
        self,
        instance_id: str,
        graph_name: str,
        label_name: str,
        request: igraph_20210621_models.TriggerLabelBackflowRequest,
    ) -> igraph_20210621_models.TriggerLabelBackflowResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.trigger_label_backflow_with_options_async(instance_id, graph_name, label_name, request, headers, runtime)

    def update_graph_description_with_options(
        self,
        instance_id: str,
        graph_name: str,
        request: igraph_20210621_models.UpdateGraphDescriptionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> igraph_20210621_models.UpdateGraphDescriptionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace):
            query['namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGraphDescription',
            version='2021-06-21',
            protocol='HTTPS',
            pathname=f'/openapi/igraph/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/graphs/{OpenApiUtilClient.get_encode_param(graph_name)}/description',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            igraph_20210621_models.UpdateGraphDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_graph_description_with_options_async(
        self,
        instance_id: str,
        graph_name: str,
        request: igraph_20210621_models.UpdateGraphDescriptionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> igraph_20210621_models.UpdateGraphDescriptionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace):
            query['namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGraphDescription',
            version='2021-06-21',
            protocol='HTTPS',
            pathname=f'/openapi/igraph/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/graphs/{OpenApiUtilClient.get_encode_param(graph_name)}/description',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            igraph_20210621_models.UpdateGraphDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_graph_description(
        self,
        instance_id: str,
        graph_name: str,
        request: igraph_20210621_models.UpdateGraphDescriptionRequest,
    ) -> igraph_20210621_models.UpdateGraphDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_graph_description_with_options(instance_id, graph_name, request, headers, runtime)

    async def update_graph_description_async(
        self,
        instance_id: str,
        graph_name: str,
        request: igraph_20210621_models.UpdateGraphDescriptionRequest,
    ) -> igraph_20210621_models.UpdateGraphDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_graph_description_with_options_async(instance_id, graph_name, request, headers, runtime)
