# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_composer20181212 import models as composer_20181212_models
from alibabacloud_tea_util import models as util_models


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
        self._endpoint = self.get_endpoint('composer', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def clone_flow_with_options(
        self,
        request: composer_20181212_models.CloneFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> composer_20181212_models.CloneFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            composer_20181212_models.CloneFlowResponse(),
            self.do_rpcrequest('CloneFlow', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def clone_flow_with_options_async(
        self,
        request: composer_20181212_models.CloneFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> composer_20181212_models.CloneFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            composer_20181212_models.CloneFlowResponse(),
            await self.do_rpcrequest_async('CloneFlow', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def clone_flow(
        self,
        request: composer_20181212_models.CloneFlowRequest,
    ) -> composer_20181212_models.CloneFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.clone_flow_with_options(request, runtime)

    async def clone_flow_async(
        self,
        request: composer_20181212_models.CloneFlowRequest,
    ) -> composer_20181212_models.CloneFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.clone_flow_with_options_async(request, runtime)

    def create_flow_with_options(
        self,
        request: composer_20181212_models.CreateFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> composer_20181212_models.CreateFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            composer_20181212_models.CreateFlowResponse(),
            self.do_rpcrequest('CreateFlow', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_flow_with_options_async(
        self,
        request: composer_20181212_models.CreateFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> composer_20181212_models.CreateFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            composer_20181212_models.CreateFlowResponse(),
            await self.do_rpcrequest_async('CreateFlow', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_flow(
        self,
        request: composer_20181212_models.CreateFlowRequest,
    ) -> composer_20181212_models.CreateFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_flow_with_options(request, runtime)

    async def create_flow_async(
        self,
        request: composer_20181212_models.CreateFlowRequest,
    ) -> composer_20181212_models.CreateFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_flow_with_options_async(request, runtime)

    def delete_flow_with_options(
        self,
        request: composer_20181212_models.DeleteFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> composer_20181212_models.DeleteFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            composer_20181212_models.DeleteFlowResponse(),
            self.do_rpcrequest('DeleteFlow', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_flow_with_options_async(
        self,
        request: composer_20181212_models.DeleteFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> composer_20181212_models.DeleteFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            composer_20181212_models.DeleteFlowResponse(),
            await self.do_rpcrequest_async('DeleteFlow', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_flow(
        self,
        request: composer_20181212_models.DeleteFlowRequest,
    ) -> composer_20181212_models.DeleteFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_flow_with_options(request, runtime)

    async def delete_flow_async(
        self,
        request: composer_20181212_models.DeleteFlowRequest,
    ) -> composer_20181212_models.DeleteFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_flow_with_options_async(request, runtime)

    def disable_flow_with_options(
        self,
        request: composer_20181212_models.DisableFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> composer_20181212_models.DisableFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            composer_20181212_models.DisableFlowResponse(),
            self.do_rpcrequest('DisableFlow', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def disable_flow_with_options_async(
        self,
        request: composer_20181212_models.DisableFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> composer_20181212_models.DisableFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            composer_20181212_models.DisableFlowResponse(),
            await self.do_rpcrequest_async('DisableFlow', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def disable_flow(
        self,
        request: composer_20181212_models.DisableFlowRequest,
    ) -> composer_20181212_models.DisableFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_flow_with_options(request, runtime)

    async def disable_flow_async(
        self,
        request: composer_20181212_models.DisableFlowRequest,
    ) -> composer_20181212_models.DisableFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_flow_with_options_async(request, runtime)

    def enable_flow_with_options(
        self,
        request: composer_20181212_models.EnableFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> composer_20181212_models.EnableFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            composer_20181212_models.EnableFlowResponse(),
            self.do_rpcrequest('EnableFlow', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def enable_flow_with_options_async(
        self,
        request: composer_20181212_models.EnableFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> composer_20181212_models.EnableFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            composer_20181212_models.EnableFlowResponse(),
            await self.do_rpcrequest_async('EnableFlow', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enable_flow(
        self,
        request: composer_20181212_models.EnableFlowRequest,
    ) -> composer_20181212_models.EnableFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_flow_with_options(request, runtime)

    async def enable_flow_async(
        self,
        request: composer_20181212_models.EnableFlowRequest,
    ) -> composer_20181212_models.EnableFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_flow_with_options_async(request, runtime)

    def get_flow_with_options(
        self,
        request: composer_20181212_models.GetFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> composer_20181212_models.GetFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            composer_20181212_models.GetFlowResponse(),
            self.do_rpcrequest('GetFlow', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_flow_with_options_async(
        self,
        request: composer_20181212_models.GetFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> composer_20181212_models.GetFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            composer_20181212_models.GetFlowResponse(),
            await self.do_rpcrequest_async('GetFlow', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_flow(
        self,
        request: composer_20181212_models.GetFlowRequest,
    ) -> composer_20181212_models.GetFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_flow_with_options(request, runtime)

    async def get_flow_async(
        self,
        request: composer_20181212_models.GetFlowRequest,
    ) -> composer_20181212_models.GetFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_flow_with_options_async(request, runtime)

    def get_template_with_options(
        self,
        request: composer_20181212_models.GetTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> composer_20181212_models.GetTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            composer_20181212_models.GetTemplateResponse(),
            self.do_rpcrequest('GetTemplate', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_template_with_options_async(
        self,
        request: composer_20181212_models.GetTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> composer_20181212_models.GetTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            composer_20181212_models.GetTemplateResponse(),
            await self.do_rpcrequest_async('GetTemplate', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_template(
        self,
        request: composer_20181212_models.GetTemplateRequest,
    ) -> composer_20181212_models.GetTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_template_with_options(request, runtime)

    async def get_template_async(
        self,
        request: composer_20181212_models.GetTemplateRequest,
    ) -> composer_20181212_models.GetTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_template_with_options_async(request, runtime)

    def get_version_with_options(
        self,
        request: composer_20181212_models.GetVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> composer_20181212_models.GetVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            composer_20181212_models.GetVersionResponse(),
            self.do_rpcrequest('GetVersion', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_version_with_options_async(
        self,
        request: composer_20181212_models.GetVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> composer_20181212_models.GetVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            composer_20181212_models.GetVersionResponse(),
            await self.do_rpcrequest_async('GetVersion', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_version(
        self,
        request: composer_20181212_models.GetVersionRequest,
    ) -> composer_20181212_models.GetVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_version_with_options(request, runtime)

    async def get_version_async(
        self,
        request: composer_20181212_models.GetVersionRequest,
    ) -> composer_20181212_models.GetVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_version_with_options_async(request, runtime)

    def group_invoke_flow_with_options(
        self,
        request: composer_20181212_models.GroupInvokeFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> composer_20181212_models.GroupInvokeFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            composer_20181212_models.GroupInvokeFlowResponse(),
            self.do_rpcrequest('GroupInvokeFlow', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def group_invoke_flow_with_options_async(
        self,
        request: composer_20181212_models.GroupInvokeFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> composer_20181212_models.GroupInvokeFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            composer_20181212_models.GroupInvokeFlowResponse(),
            await self.do_rpcrequest_async('GroupInvokeFlow', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def group_invoke_flow(
        self,
        request: composer_20181212_models.GroupInvokeFlowRequest,
    ) -> composer_20181212_models.GroupInvokeFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.group_invoke_flow_with_options(request, runtime)

    async def group_invoke_flow_async(
        self,
        request: composer_20181212_models.GroupInvokeFlowRequest,
    ) -> composer_20181212_models.GroupInvokeFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.group_invoke_flow_with_options_async(request, runtime)

    def invoke_flow_with_options(
        self,
        request: composer_20181212_models.InvokeFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> composer_20181212_models.InvokeFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            composer_20181212_models.InvokeFlowResponse(),
            self.do_rpcrequest('InvokeFlow', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def invoke_flow_with_options_async(
        self,
        request: composer_20181212_models.InvokeFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> composer_20181212_models.InvokeFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            composer_20181212_models.InvokeFlowResponse(),
            await self.do_rpcrequest_async('InvokeFlow', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def invoke_flow(
        self,
        request: composer_20181212_models.InvokeFlowRequest,
    ) -> composer_20181212_models.InvokeFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.invoke_flow_with_options(request, runtime)

    async def invoke_flow_async(
        self,
        request: composer_20181212_models.InvokeFlowRequest,
    ) -> composer_20181212_models.InvokeFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.invoke_flow_with_options_async(request, runtime)

    def list_flows_with_options(
        self,
        request: composer_20181212_models.ListFlowsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> composer_20181212_models.ListFlowsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            composer_20181212_models.ListFlowsResponse(),
            self.do_rpcrequest('ListFlows', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_flows_with_options_async(
        self,
        request: composer_20181212_models.ListFlowsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> composer_20181212_models.ListFlowsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            composer_20181212_models.ListFlowsResponse(),
            await self.do_rpcrequest_async('ListFlows', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_flows(
        self,
        request: composer_20181212_models.ListFlowsRequest,
    ) -> composer_20181212_models.ListFlowsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_flows_with_options(request, runtime)

    async def list_flows_async(
        self,
        request: composer_20181212_models.ListFlowsRequest,
    ) -> composer_20181212_models.ListFlowsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_flows_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: composer_20181212_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> composer_20181212_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            composer_20181212_models.ListTagResourcesResponse(),
            self.do_rpcrequest('ListTagResources', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: composer_20181212_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> composer_20181212_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            composer_20181212_models.ListTagResourcesResponse(),
            await self.do_rpcrequest_async('ListTagResources', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag_resources(
        self,
        request: composer_20181212_models.ListTagResourcesRequest,
    ) -> composer_20181212_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: composer_20181212_models.ListTagResourcesRequest,
    ) -> composer_20181212_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def list_templates_with_options(
        self,
        request: composer_20181212_models.ListTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> composer_20181212_models.ListTemplatesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            composer_20181212_models.ListTemplatesResponse(),
            self.do_rpcrequest('ListTemplates', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_templates_with_options_async(
        self,
        request: composer_20181212_models.ListTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> composer_20181212_models.ListTemplatesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            composer_20181212_models.ListTemplatesResponse(),
            await self.do_rpcrequest_async('ListTemplates', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_templates(
        self,
        request: composer_20181212_models.ListTemplatesRequest,
    ) -> composer_20181212_models.ListTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_templates_with_options(request, runtime)

    async def list_templates_async(
        self,
        request: composer_20181212_models.ListTemplatesRequest,
    ) -> composer_20181212_models.ListTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_templates_with_options_async(request, runtime)

    def list_versions_with_options(
        self,
        request: composer_20181212_models.ListVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> composer_20181212_models.ListVersionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            composer_20181212_models.ListVersionsResponse(),
            self.do_rpcrequest('ListVersions', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_versions_with_options_async(
        self,
        request: composer_20181212_models.ListVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> composer_20181212_models.ListVersionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            composer_20181212_models.ListVersionsResponse(),
            await self.do_rpcrequest_async('ListVersions', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_versions(
        self,
        request: composer_20181212_models.ListVersionsRequest,
    ) -> composer_20181212_models.ListVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_versions_with_options(request, runtime)

    async def list_versions_async(
        self,
        request: composer_20181212_models.ListVersionsRequest,
    ) -> composer_20181212_models.ListVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_versions_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: composer_20181212_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> composer_20181212_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            composer_20181212_models.TagResourcesResponse(),
            self.do_rpcrequest('TagResources', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: composer_20181212_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> composer_20181212_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            composer_20181212_models.TagResourcesResponse(),
            await self.do_rpcrequest_async('TagResources', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def tag_resources(
        self,
        request: composer_20181212_models.TagResourcesRequest,
    ) -> composer_20181212_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: composer_20181212_models.TagResourcesRequest,
    ) -> composer_20181212_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: composer_20181212_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> composer_20181212_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            composer_20181212_models.UntagResourcesResponse(),
            self.do_rpcrequest('UntagResources', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: composer_20181212_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> composer_20181212_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            composer_20181212_models.UntagResourcesResponse(),
            await self.do_rpcrequest_async('UntagResources', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def untag_resources(
        self,
        request: composer_20181212_models.UntagResourcesRequest,
    ) -> composer_20181212_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: composer_20181212_models.UntagResourcesRequest,
    ) -> composer_20181212_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def update_flow_with_options(
        self,
        request: composer_20181212_models.UpdateFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> composer_20181212_models.UpdateFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            composer_20181212_models.UpdateFlowResponse(),
            self.do_rpcrequest('UpdateFlow', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_flow_with_options_async(
        self,
        request: composer_20181212_models.UpdateFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> composer_20181212_models.UpdateFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            composer_20181212_models.UpdateFlowResponse(),
            await self.do_rpcrequest_async('UpdateFlow', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_flow(
        self,
        request: composer_20181212_models.UpdateFlowRequest,
    ) -> composer_20181212_models.UpdateFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_flow_with_options(request, runtime)

    async def update_flow_async(
        self,
        request: composer_20181212_models.UpdateFlowRequest,
    ) -> composer_20181212_models.UpdateFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_flow_with_options_async(request, runtime)
