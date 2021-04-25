# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_easygene20210315 import models as easy_gene_20210315_models
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
        self._endpoint = self.get_endpoint('easygene', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def abort_run_with_options(
        self,
        request: easy_gene_20210315_models.AbortRunRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.AbortRunResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.AbortRunResponse(),
            self.do_rpcrequest('AbortRun', '2021-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def abort_run_with_options_async(
        self,
        request: easy_gene_20210315_models.AbortRunRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.AbortRunResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.AbortRunResponse(),
            await self.do_rpcrequest_async('AbortRun', '2021-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def abort_run(
        self,
        request: easy_gene_20210315_models.AbortRunRequest,
    ) -> easy_gene_20210315_models.AbortRunResponse:
        runtime = util_models.RuntimeOptions()
        return self.abort_run_with_options(request, runtime)

    async def abort_run_async(
        self,
        request: easy_gene_20210315_models.AbortRunRequest,
    ) -> easy_gene_20210315_models.AbortRunResponse:
        runtime = util_models.RuntimeOptions()
        return await self.abort_run_with_options_async(request, runtime)

    def abort_submission_with_options(
        self,
        request: easy_gene_20210315_models.AbortSubmissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.AbortSubmissionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.AbortSubmissionResponse(),
            self.do_rpcrequest('AbortSubmission', '2021-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def abort_submission_with_options_async(
        self,
        request: easy_gene_20210315_models.AbortSubmissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.AbortSubmissionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.AbortSubmissionResponse(),
            await self.do_rpcrequest_async('AbortSubmission', '2021-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def abort_submission(
        self,
        request: easy_gene_20210315_models.AbortSubmissionRequest,
    ) -> easy_gene_20210315_models.AbortSubmissionResponse:
        runtime = util_models.RuntimeOptions()
        return self.abort_submission_with_options(request, runtime)

    async def abort_submission_async(
        self,
        request: easy_gene_20210315_models.AbortSubmissionRequest,
    ) -> easy_gene_20210315_models.AbortSubmissionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.abort_submission_with_options_async(request, runtime)

    def create_app_with_options(
        self,
        tmp_req: easy_gene_20210315_models.CreateAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.CreateAppResponse:
        UtilClient.validate_model(tmp_req)
        request = easy_gene_20210315_models.CreateAppShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dependencies):
            request.dependencies_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dependencies, 'Dependencies', 'json')
        if not UtilClient.is_unset(tmp_req.configs):
            request.configs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.configs, 'Configs', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.CreateAppResponse(),
            self.do_rpcrequest('CreateApp', '2021-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_app_with_options_async(
        self,
        tmp_req: easy_gene_20210315_models.CreateAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.CreateAppResponse:
        UtilClient.validate_model(tmp_req)
        request = easy_gene_20210315_models.CreateAppShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dependencies):
            request.dependencies_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dependencies, 'Dependencies', 'json')
        if not UtilClient.is_unset(tmp_req.configs):
            request.configs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.configs, 'Configs', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.CreateAppResponse(),
            await self.do_rpcrequest_async('CreateApp', '2021-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_app(
        self,
        request: easy_gene_20210315_models.CreateAppRequest,
    ) -> easy_gene_20210315_models.CreateAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_app_with_options(request, runtime)

    async def create_app_async(
        self,
        request: easy_gene_20210315_models.CreateAppRequest,
    ) -> easy_gene_20210315_models.CreateAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_app_with_options_async(request, runtime)

    def create_entity_with_options(
        self,
        tmp_req: easy_gene_20210315_models.CreateEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.CreateEntityResponse:
        UtilClient.validate_model(tmp_req)
        request = easy_gene_20210315_models.CreateEntityShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.entity_items):
            request.entity_items_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.entity_items, 'EntityItems', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.CreateEntityResponse(),
            self.do_rpcrequest('CreateEntity', '2021-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_entity_with_options_async(
        self,
        tmp_req: easy_gene_20210315_models.CreateEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.CreateEntityResponse:
        UtilClient.validate_model(tmp_req)
        request = easy_gene_20210315_models.CreateEntityShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.entity_items):
            request.entity_items_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.entity_items, 'EntityItems', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.CreateEntityResponse(),
            await self.do_rpcrequest_async('CreateEntity', '2021-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_entity(
        self,
        request: easy_gene_20210315_models.CreateEntityRequest,
    ) -> easy_gene_20210315_models.CreateEntityResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_entity_with_options(request, runtime)

    async def create_entity_async(
        self,
        request: easy_gene_20210315_models.CreateEntityRequest,
    ) -> easy_gene_20210315_models.CreateEntityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_entity_with_options_async(request, runtime)

    def create_run_with_options(
        self,
        request: easy_gene_20210315_models.CreateRunRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.CreateRunResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.CreateRunResponse(),
            self.do_rpcrequest('CreateRun', '2021-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_run_with_options_async(
        self,
        request: easy_gene_20210315_models.CreateRunRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.CreateRunResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.CreateRunResponse(),
            await self.do_rpcrequest_async('CreateRun', '2021-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_run(
        self,
        request: easy_gene_20210315_models.CreateRunRequest,
    ) -> easy_gene_20210315_models.CreateRunResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_run_with_options(request, runtime)

    async def create_run_async(
        self,
        request: easy_gene_20210315_models.CreateRunRequest,
    ) -> easy_gene_20210315_models.CreateRunResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_run_with_options_async(request, runtime)

    def create_submission_with_options(
        self,
        tmp_req: easy_gene_20210315_models.CreateSubmissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.CreateSubmissionResponse:
        UtilClient.validate_model(tmp_req)
        request = easy_gene_20210315_models.CreateSubmissionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.entity_names):
            request.entity_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.entity_names, 'EntityNames', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.CreateSubmissionResponse(),
            self.do_rpcrequest('CreateSubmission', '2021-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_submission_with_options_async(
        self,
        tmp_req: easy_gene_20210315_models.CreateSubmissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.CreateSubmissionResponse:
        UtilClient.validate_model(tmp_req)
        request = easy_gene_20210315_models.CreateSubmissionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.entity_names):
            request.entity_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.entity_names, 'EntityNames', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.CreateSubmissionResponse(),
            await self.do_rpcrequest_async('CreateSubmission', '2021-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_submission(
        self,
        request: easy_gene_20210315_models.CreateSubmissionRequest,
    ) -> easy_gene_20210315_models.CreateSubmissionResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_submission_with_options(request, runtime)

    async def create_submission_async(
        self,
        request: easy_gene_20210315_models.CreateSubmissionRequest,
    ) -> easy_gene_20210315_models.CreateSubmissionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_submission_with_options_async(request, runtime)

    def create_template_with_options(
        self,
        tmp_req: easy_gene_20210315_models.CreateTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.CreateTemplateResponse:
        UtilClient.validate_model(tmp_req)
        request = easy_gene_20210315_models.CreateTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.inputs):
            request.inputs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.inputs, 'Inputs', 'json')
        if not UtilClient.is_unset(tmp_req.outputs):
            request.outputs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.outputs, 'Outputs', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.CreateTemplateResponse(),
            self.do_rpcrequest('CreateTemplate', '2021-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_template_with_options_async(
        self,
        tmp_req: easy_gene_20210315_models.CreateTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.CreateTemplateResponse:
        UtilClient.validate_model(tmp_req)
        request = easy_gene_20210315_models.CreateTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.inputs):
            request.inputs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.inputs, 'Inputs', 'json')
        if not UtilClient.is_unset(tmp_req.outputs):
            request.outputs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.outputs, 'Outputs', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.CreateTemplateResponse(),
            await self.do_rpcrequest_async('CreateTemplate', '2021-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_template(
        self,
        request: easy_gene_20210315_models.CreateTemplateRequest,
    ) -> easy_gene_20210315_models.CreateTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_template_with_options(request, runtime)

    async def create_template_async(
        self,
        request: easy_gene_20210315_models.CreateTemplateRequest,
    ) -> easy_gene_20210315_models.CreateTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_template_with_options_async(request, runtime)

    def create_workspace_with_options(
        self,
        request: easy_gene_20210315_models.CreateWorkspaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.CreateWorkspaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.CreateWorkspaceResponse(),
            self.do_rpcrequest('CreateWorkspace', '2021-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_workspace_with_options_async(
        self,
        request: easy_gene_20210315_models.CreateWorkspaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.CreateWorkspaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.CreateWorkspaceResponse(),
            await self.do_rpcrequest_async('CreateWorkspace', '2021-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_workspace(
        self,
        request: easy_gene_20210315_models.CreateWorkspaceRequest,
    ) -> easy_gene_20210315_models.CreateWorkspaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_workspace_with_options(request, runtime)

    async def create_workspace_async(
        self,
        request: easy_gene_20210315_models.CreateWorkspaceRequest,
    ) -> easy_gene_20210315_models.CreateWorkspaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_workspace_with_options_async(request, runtime)

    def delete_app_with_options(
        self,
        request: easy_gene_20210315_models.DeleteAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.DeleteAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.DeleteAppResponse(),
            self.do_rpcrequest('DeleteApp', '2021-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_app_with_options_async(
        self,
        request: easy_gene_20210315_models.DeleteAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.DeleteAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.DeleteAppResponse(),
            await self.do_rpcrequest_async('DeleteApp', '2021-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_app(
        self,
        request: easy_gene_20210315_models.DeleteAppRequest,
    ) -> easy_gene_20210315_models.DeleteAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_app_with_options(request, runtime)

    async def delete_app_async(
        self,
        request: easy_gene_20210315_models.DeleteAppRequest,
    ) -> easy_gene_20210315_models.DeleteAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_app_with_options_async(request, runtime)

    def delete_entity_items_with_options(
        self,
        tmp_req: easy_gene_20210315_models.DeleteEntityItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.DeleteEntityItemsResponse:
        UtilClient.validate_model(tmp_req)
        request = easy_gene_20210315_models.DeleteEntityItemsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.entity_names):
            request.entity_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.entity_names, 'EntityNames', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.DeleteEntityItemsResponse(),
            self.do_rpcrequest('DeleteEntityItems', '2021-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_entity_items_with_options_async(
        self,
        tmp_req: easy_gene_20210315_models.DeleteEntityItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.DeleteEntityItemsResponse:
        UtilClient.validate_model(tmp_req)
        request = easy_gene_20210315_models.DeleteEntityItemsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.entity_names):
            request.entity_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.entity_names, 'EntityNames', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.DeleteEntityItemsResponse(),
            await self.do_rpcrequest_async('DeleteEntityItems', '2021-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_entity_items(
        self,
        request: easy_gene_20210315_models.DeleteEntityItemsRequest,
    ) -> easy_gene_20210315_models.DeleteEntityItemsResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_entity_items_with_options(request, runtime)

    async def delete_entity_items_async(
        self,
        request: easy_gene_20210315_models.DeleteEntityItemsRequest,
    ) -> easy_gene_20210315_models.DeleteEntityItemsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_entity_items_with_options_async(request, runtime)

    def delete_run_with_options(
        self,
        request: easy_gene_20210315_models.DeleteRunRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.DeleteRunResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.DeleteRunResponse(),
            self.do_rpcrequest('DeleteRun', '2021-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_run_with_options_async(
        self,
        request: easy_gene_20210315_models.DeleteRunRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.DeleteRunResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.DeleteRunResponse(),
            await self.do_rpcrequest_async('DeleteRun', '2021-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_run(
        self,
        request: easy_gene_20210315_models.DeleteRunRequest,
    ) -> easy_gene_20210315_models.DeleteRunResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_run_with_options(request, runtime)

    async def delete_run_async(
        self,
        request: easy_gene_20210315_models.DeleteRunRequest,
    ) -> easy_gene_20210315_models.DeleteRunResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_run_with_options_async(request, runtime)

    def delete_submission_with_options(
        self,
        request: easy_gene_20210315_models.DeleteSubmissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.DeleteSubmissionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.DeleteSubmissionResponse(),
            self.do_rpcrequest('DeleteSubmission', '2021-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_submission_with_options_async(
        self,
        request: easy_gene_20210315_models.DeleteSubmissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.DeleteSubmissionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.DeleteSubmissionResponse(),
            await self.do_rpcrequest_async('DeleteSubmission', '2021-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_submission(
        self,
        request: easy_gene_20210315_models.DeleteSubmissionRequest,
    ) -> easy_gene_20210315_models.DeleteSubmissionResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_submission_with_options(request, runtime)

    async def delete_submission_async(
        self,
        request: easy_gene_20210315_models.DeleteSubmissionRequest,
    ) -> easy_gene_20210315_models.DeleteSubmissionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_submission_with_options_async(request, runtime)

    def delete_template_with_options(
        self,
        request: easy_gene_20210315_models.DeleteTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.DeleteTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.DeleteTemplateResponse(),
            self.do_rpcrequest('DeleteTemplate', '2021-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_template_with_options_async(
        self,
        request: easy_gene_20210315_models.DeleteTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.DeleteTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.DeleteTemplateResponse(),
            await self.do_rpcrequest_async('DeleteTemplate', '2021-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_template(
        self,
        request: easy_gene_20210315_models.DeleteTemplateRequest,
    ) -> easy_gene_20210315_models.DeleteTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_template_with_options(request, runtime)

    async def delete_template_async(
        self,
        request: easy_gene_20210315_models.DeleteTemplateRequest,
    ) -> easy_gene_20210315_models.DeleteTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_template_with_options_async(request, runtime)

    def delete_workspace_with_options(
        self,
        request: easy_gene_20210315_models.DeleteWorkspaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.DeleteWorkspaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.DeleteWorkspaceResponse(),
            self.do_rpcrequest('DeleteWorkspace', '2021-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_workspace_with_options_async(
        self,
        request: easy_gene_20210315_models.DeleteWorkspaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.DeleteWorkspaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.DeleteWorkspaceResponse(),
            await self.do_rpcrequest_async('DeleteWorkspace', '2021-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_workspace(
        self,
        request: easy_gene_20210315_models.DeleteWorkspaceRequest,
    ) -> easy_gene_20210315_models.DeleteWorkspaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_workspace_with_options(request, runtime)

    async def delete_workspace_async(
        self,
        request: easy_gene_20210315_models.DeleteWorkspaceRequest,
    ) -> easy_gene_20210315_models.DeleteWorkspaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_workspace_with_options_async(request, runtime)

    def download_entity_with_options(
        self,
        tmp_req: easy_gene_20210315_models.DownloadEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.DownloadEntityResponse:
        UtilClient.validate_model(tmp_req)
        request = easy_gene_20210315_models.DownloadEntityShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.entity_names):
            request.entity_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.entity_names, 'EntityNames', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.DownloadEntityResponse(),
            self.do_rpcrequest('DownloadEntity', '2021-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def download_entity_with_options_async(
        self,
        tmp_req: easy_gene_20210315_models.DownloadEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.DownloadEntityResponse:
        UtilClient.validate_model(tmp_req)
        request = easy_gene_20210315_models.DownloadEntityShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.entity_names):
            request.entity_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.entity_names, 'EntityNames', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.DownloadEntityResponse(),
            await self.do_rpcrequest_async('DownloadEntity', '2021-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def download_entity(
        self,
        request: easy_gene_20210315_models.DownloadEntityRequest,
    ) -> easy_gene_20210315_models.DownloadEntityResponse:
        runtime = util_models.RuntimeOptions()
        return self.download_entity_with_options(request, runtime)

    async def download_entity_async(
        self,
        request: easy_gene_20210315_models.DownloadEntityRequest,
    ) -> easy_gene_20210315_models.DownloadEntityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.download_entity_with_options_async(request, runtime)

    def get_app_with_options(
        self,
        request: easy_gene_20210315_models.GetAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.GetAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.GetAppResponse(),
            self.do_rpcrequest('GetApp', '2021-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_app_with_options_async(
        self,
        request: easy_gene_20210315_models.GetAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.GetAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.GetAppResponse(),
            await self.do_rpcrequest_async('GetApp', '2021-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_app(
        self,
        request: easy_gene_20210315_models.GetAppRequest,
    ) -> easy_gene_20210315_models.GetAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_app_with_options(request, runtime)

    async def get_app_async(
        self,
        request: easy_gene_20210315_models.GetAppRequest,
    ) -> easy_gene_20210315_models.GetAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_app_with_options_async(request, runtime)

    def get_entity_with_options(
        self,
        request: easy_gene_20210315_models.GetEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.GetEntityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.GetEntityResponse(),
            self.do_rpcrequest('GetEntity', '2021-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_entity_with_options_async(
        self,
        request: easy_gene_20210315_models.GetEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.GetEntityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.GetEntityResponse(),
            await self.do_rpcrequest_async('GetEntity', '2021-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_entity(
        self,
        request: easy_gene_20210315_models.GetEntityRequest,
    ) -> easy_gene_20210315_models.GetEntityResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_entity_with_options(request, runtime)

    async def get_entity_async(
        self,
        request: easy_gene_20210315_models.GetEntityRequest,
    ) -> easy_gene_20210315_models.GetEntityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_entity_with_options_async(request, runtime)

    def get_global_app_with_options(
        self,
        request: easy_gene_20210315_models.GetGlobalAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.GetGlobalAppResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.GetGlobalAppResponse(),
            self.do_rpcrequest('GetGlobalApp', '2021-03-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_global_app_with_options_async(
        self,
        request: easy_gene_20210315_models.GetGlobalAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.GetGlobalAppResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.GetGlobalAppResponse(),
            await self.do_rpcrequest_async('GetGlobalApp', '2021-03-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_global_app(
        self,
        request: easy_gene_20210315_models.GetGlobalAppRequest,
    ) -> easy_gene_20210315_models.GetGlobalAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_global_app_with_options(request, runtime)

    async def get_global_app_async(
        self,
        request: easy_gene_20210315_models.GetGlobalAppRequest,
    ) -> easy_gene_20210315_models.GetGlobalAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_global_app_with_options_async(request, runtime)

    def get_public_dataset_with_options(
        self,
        tmp_req: easy_gene_20210315_models.GetPublicDatasetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.GetPublicDatasetResponse:
        UtilClient.validate_model(tmp_req)
        request = easy_gene_20210315_models.GetPublicDatasetShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.attributes):
            request.attributes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.attributes, 'Attributes', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.GetPublicDatasetResponse(),
            self.do_rpcrequest('GetPublicDataset', '2021-03-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_public_dataset_with_options_async(
        self,
        tmp_req: easy_gene_20210315_models.GetPublicDatasetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.GetPublicDatasetResponse:
        UtilClient.validate_model(tmp_req)
        request = easy_gene_20210315_models.GetPublicDatasetShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.attributes):
            request.attributes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.attributes, 'Attributes', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.GetPublicDatasetResponse(),
            await self.do_rpcrequest_async('GetPublicDataset', '2021-03-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_public_dataset(
        self,
        request: easy_gene_20210315_models.GetPublicDatasetRequest,
    ) -> easy_gene_20210315_models.GetPublicDatasetResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_public_dataset_with_options(request, runtime)

    async def get_public_dataset_async(
        self,
        request: easy_gene_20210315_models.GetPublicDatasetRequest,
    ) -> easy_gene_20210315_models.GetPublicDatasetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_public_dataset_with_options_async(request, runtime)

    def get_public_dataset_entity_with_options(
        self,
        request: easy_gene_20210315_models.GetPublicDatasetEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.GetPublicDatasetEntityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.GetPublicDatasetEntityResponse(),
            self.do_rpcrequest('GetPublicDatasetEntity', '2021-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_public_dataset_entity_with_options_async(
        self,
        request: easy_gene_20210315_models.GetPublicDatasetEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.GetPublicDatasetEntityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.GetPublicDatasetEntityResponse(),
            await self.do_rpcrequest_async('GetPublicDatasetEntity', '2021-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_public_dataset_entity(
        self,
        request: easy_gene_20210315_models.GetPublicDatasetEntityRequest,
    ) -> easy_gene_20210315_models.GetPublicDatasetEntityResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_public_dataset_entity_with_options(request, runtime)

    async def get_public_dataset_entity_async(
        self,
        request: easy_gene_20210315_models.GetPublicDatasetEntityRequest,
    ) -> easy_gene_20210315_models.GetPublicDatasetEntityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_public_dataset_entity_with_options_async(request, runtime)

    def get_run_with_options(
        self,
        request: easy_gene_20210315_models.GetRunRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.GetRunResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.GetRunResponse(),
            self.do_rpcrequest('GetRun', '2021-03-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_run_with_options_async(
        self,
        request: easy_gene_20210315_models.GetRunRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.GetRunResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.GetRunResponse(),
            await self.do_rpcrequest_async('GetRun', '2021-03-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_run(
        self,
        request: easy_gene_20210315_models.GetRunRequest,
    ) -> easy_gene_20210315_models.GetRunResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_run_with_options(request, runtime)

    async def get_run_async(
        self,
        request: easy_gene_20210315_models.GetRunRequest,
    ) -> easy_gene_20210315_models.GetRunResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_run_with_options_async(request, runtime)

    def get_submission_with_options(
        self,
        request: easy_gene_20210315_models.GetSubmissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.GetSubmissionResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.GetSubmissionResponse(),
            self.do_rpcrequest('GetSubmission', '2021-03-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_submission_with_options_async(
        self,
        request: easy_gene_20210315_models.GetSubmissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.GetSubmissionResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.GetSubmissionResponse(),
            await self.do_rpcrequest_async('GetSubmission', '2021-03-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_submission(
        self,
        request: easy_gene_20210315_models.GetSubmissionRequest,
    ) -> easy_gene_20210315_models.GetSubmissionResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_submission_with_options(request, runtime)

    async def get_submission_async(
        self,
        request: easy_gene_20210315_models.GetSubmissionRequest,
    ) -> easy_gene_20210315_models.GetSubmissionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_submission_with_options_async(request, runtime)

    def get_template_with_options(
        self,
        request: easy_gene_20210315_models.GetTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.GetTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.GetTemplateResponse(),
            self.do_rpcrequest('GetTemplate', '2021-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_template_with_options_async(
        self,
        request: easy_gene_20210315_models.GetTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.GetTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.GetTemplateResponse(),
            await self.do_rpcrequest_async('GetTemplate', '2021-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_template(
        self,
        request: easy_gene_20210315_models.GetTemplateRequest,
    ) -> easy_gene_20210315_models.GetTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_template_with_options(request, runtime)

    async def get_template_async(
        self,
        request: easy_gene_20210315_models.GetTemplateRequest,
    ) -> easy_gene_20210315_models.GetTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_template_with_options_async(request, runtime)

    def get_workspace_with_options(
        self,
        request: easy_gene_20210315_models.GetWorkspaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.GetWorkspaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.GetWorkspaceResponse(),
            self.do_rpcrequest('GetWorkspace', '2021-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_workspace_with_options_async(
        self,
        request: easy_gene_20210315_models.GetWorkspaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.GetWorkspaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.GetWorkspaceResponse(),
            await self.do_rpcrequest_async('GetWorkspace', '2021-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_workspace(
        self,
        request: easy_gene_20210315_models.GetWorkspaceRequest,
    ) -> easy_gene_20210315_models.GetWorkspaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_workspace_with_options(request, runtime)

    async def get_workspace_async(
        self,
        request: easy_gene_20210315_models.GetWorkspaceRequest,
    ) -> easy_gene_20210315_models.GetWorkspaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_workspace_with_options_async(request, runtime)

    def install_global_app_with_options(
        self,
        request: easy_gene_20210315_models.InstallGlobalAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.InstallGlobalAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.InstallGlobalAppResponse(),
            self.do_rpcrequest('InstallGlobalApp', '2021-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def install_global_app_with_options_async(
        self,
        request: easy_gene_20210315_models.InstallGlobalAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.InstallGlobalAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.InstallGlobalAppResponse(),
            await self.do_rpcrequest_async('InstallGlobalApp', '2021-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def install_global_app(
        self,
        request: easy_gene_20210315_models.InstallGlobalAppRequest,
    ) -> easy_gene_20210315_models.InstallGlobalAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.install_global_app_with_options(request, runtime)

    async def install_global_app_async(
        self,
        request: easy_gene_20210315_models.InstallGlobalAppRequest,
    ) -> easy_gene_20210315_models.InstallGlobalAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.install_global_app_with_options_async(request, runtime)

    def list_apps_with_options(
        self,
        request: easy_gene_20210315_models.ListAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.ListAppsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListAppsResponse(),
            self.do_rpcrequest('ListApps', '2021-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_apps_with_options_async(
        self,
        request: easy_gene_20210315_models.ListAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.ListAppsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListAppsResponse(),
            await self.do_rpcrequest_async('ListApps', '2021-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_apps(
        self,
        request: easy_gene_20210315_models.ListAppsRequest,
    ) -> easy_gene_20210315_models.ListAppsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_apps_with_options(request, runtime)

    async def list_apps_async(
        self,
        request: easy_gene_20210315_models.ListAppsRequest,
    ) -> easy_gene_20210315_models.ListAppsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_apps_with_options_async(request, runtime)

    def list_authorized_software_with_options(
        self,
        request: easy_gene_20210315_models.ListAuthorizedSoftwareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.ListAuthorizedSoftwareResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListAuthorizedSoftwareResponse(),
            self.do_rpcrequest('ListAuthorizedSoftware', '2021-03-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_authorized_software_with_options_async(
        self,
        request: easy_gene_20210315_models.ListAuthorizedSoftwareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.ListAuthorizedSoftwareResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListAuthorizedSoftwareResponse(),
            await self.do_rpcrequest_async('ListAuthorizedSoftware', '2021-03-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_authorized_software(
        self,
        request: easy_gene_20210315_models.ListAuthorizedSoftwareRequest,
    ) -> easy_gene_20210315_models.ListAuthorizedSoftwareResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_authorized_software_with_options(request, runtime)

    async def list_authorized_software_async(
        self,
        request: easy_gene_20210315_models.ListAuthorizedSoftwareRequest,
    ) -> easy_gene_20210315_models.ListAuthorizedSoftwareResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_authorized_software_with_options_async(request, runtime)

    def list_container_images_with_options(
        self,
        request: easy_gene_20210315_models.ListContainerImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.ListContainerImagesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListContainerImagesResponse(),
            self.do_rpcrequest('ListContainerImages', '2021-03-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_container_images_with_options_async(
        self,
        request: easy_gene_20210315_models.ListContainerImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.ListContainerImagesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListContainerImagesResponse(),
            await self.do_rpcrequest_async('ListContainerImages', '2021-03-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_container_images(
        self,
        request: easy_gene_20210315_models.ListContainerImagesRequest,
    ) -> easy_gene_20210315_models.ListContainerImagesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_container_images_with_options(request, runtime)

    async def list_container_images_async(
        self,
        request: easy_gene_20210315_models.ListContainerImagesRequest,
    ) -> easy_gene_20210315_models.ListContainerImagesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_container_images_with_options_async(request, runtime)

    def list_entities_with_options(
        self,
        request: easy_gene_20210315_models.ListEntitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.ListEntitiesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListEntitiesResponse(),
            self.do_rpcrequest('ListEntities', '2021-03-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_entities_with_options_async(
        self,
        request: easy_gene_20210315_models.ListEntitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.ListEntitiesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListEntitiesResponse(),
            await self.do_rpcrequest_async('ListEntities', '2021-03-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_entities(
        self,
        request: easy_gene_20210315_models.ListEntitiesRequest,
    ) -> easy_gene_20210315_models.ListEntitiesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_entities_with_options(request, runtime)

    async def list_entities_async(
        self,
        request: easy_gene_20210315_models.ListEntitiesRequest,
    ) -> easy_gene_20210315_models.ListEntitiesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_entities_with_options_async(request, runtime)

    def list_entity_items_with_options(
        self,
        request: easy_gene_20210315_models.ListEntityItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.ListEntityItemsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListEntityItemsResponse(),
            self.do_rpcrequest('ListEntityItems', '2021-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_entity_items_with_options_async(
        self,
        request: easy_gene_20210315_models.ListEntityItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.ListEntityItemsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListEntityItemsResponse(),
            await self.do_rpcrequest_async('ListEntityItems', '2021-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_entity_items(
        self,
        request: easy_gene_20210315_models.ListEntityItemsRequest,
    ) -> easy_gene_20210315_models.ListEntityItemsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_entity_items_with_options(request, runtime)

    async def list_entity_items_async(
        self,
        request: easy_gene_20210315_models.ListEntityItemsRequest,
    ) -> easy_gene_20210315_models.ListEntityItemsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_entity_items_with_options_async(request, runtime)

    def list_global_apps_with_options(
        self,
        request: easy_gene_20210315_models.ListGlobalAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.ListGlobalAppsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListGlobalAppsResponse(),
            self.do_rpcrequest('ListGlobalApps', '2021-03-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_global_apps_with_options_async(
        self,
        request: easy_gene_20210315_models.ListGlobalAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.ListGlobalAppsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListGlobalAppsResponse(),
            await self.do_rpcrequest_async('ListGlobalApps', '2021-03-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_global_apps(
        self,
        request: easy_gene_20210315_models.ListGlobalAppsRequest,
    ) -> easy_gene_20210315_models.ListGlobalAppsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_global_apps_with_options(request, runtime)

    async def list_global_apps_async(
        self,
        request: easy_gene_20210315_models.ListGlobalAppsRequest,
    ) -> easy_gene_20210315_models.ListGlobalAppsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_global_apps_with_options_async(request, runtime)

    def list_public_dataset_with_options(
        self,
        request: easy_gene_20210315_models.ListPublicDatasetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.ListPublicDatasetResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListPublicDatasetResponse(),
            self.do_rpcrequest('ListPublicDataset', '2021-03-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_public_dataset_with_options_async(
        self,
        request: easy_gene_20210315_models.ListPublicDatasetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.ListPublicDatasetResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListPublicDatasetResponse(),
            await self.do_rpcrequest_async('ListPublicDataset', '2021-03-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_public_dataset(
        self,
        request: easy_gene_20210315_models.ListPublicDatasetRequest,
    ) -> easy_gene_20210315_models.ListPublicDatasetResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_public_dataset_with_options(request, runtime)

    async def list_public_dataset_async(
        self,
        request: easy_gene_20210315_models.ListPublicDatasetRequest,
    ) -> easy_gene_20210315_models.ListPublicDatasetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_public_dataset_with_options_async(request, runtime)

    def list_public_dataset_entities_with_options(
        self,
        request: easy_gene_20210315_models.ListPublicDatasetEntitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.ListPublicDatasetEntitiesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListPublicDatasetEntitiesResponse(),
            self.do_rpcrequest('ListPublicDatasetEntities', '2021-03-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_public_dataset_entities_with_options_async(
        self,
        request: easy_gene_20210315_models.ListPublicDatasetEntitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.ListPublicDatasetEntitiesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListPublicDatasetEntitiesResponse(),
            await self.do_rpcrequest_async('ListPublicDatasetEntities', '2021-03-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_public_dataset_entities(
        self,
        request: easy_gene_20210315_models.ListPublicDatasetEntitiesRequest,
    ) -> easy_gene_20210315_models.ListPublicDatasetEntitiesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_public_dataset_entities_with_options(request, runtime)

    async def list_public_dataset_entities_async(
        self,
        request: easy_gene_20210315_models.ListPublicDatasetEntitiesRequest,
    ) -> easy_gene_20210315_models.ListPublicDatasetEntitiesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_public_dataset_entities_with_options_async(request, runtime)

    def list_public_dataset_entity_items_with_options(
        self,
        request: easy_gene_20210315_models.ListPublicDatasetEntityItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.ListPublicDatasetEntityItemsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListPublicDatasetEntityItemsResponse(),
            self.do_rpcrequest('ListPublicDatasetEntityItems', '2021-03-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_public_dataset_entity_items_with_options_async(
        self,
        request: easy_gene_20210315_models.ListPublicDatasetEntityItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.ListPublicDatasetEntityItemsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListPublicDatasetEntityItemsResponse(),
            await self.do_rpcrequest_async('ListPublicDatasetEntityItems', '2021-03-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_public_dataset_entity_items(
        self,
        request: easy_gene_20210315_models.ListPublicDatasetEntityItemsRequest,
    ) -> easy_gene_20210315_models.ListPublicDatasetEntityItemsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_public_dataset_entity_items_with_options(request, runtime)

    async def list_public_dataset_entity_items_async(
        self,
        request: easy_gene_20210315_models.ListPublicDatasetEntityItemsRequest,
    ) -> easy_gene_20210315_models.ListPublicDatasetEntityItemsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_public_dataset_entity_items_with_options_async(request, runtime)

    def list_public_dataset_tags_with_options(
        self,
        request: easy_gene_20210315_models.ListPublicDatasetTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.ListPublicDatasetTagsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListPublicDatasetTagsResponse(),
            self.do_rpcrequest('ListPublicDatasetTags', '2021-03-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_public_dataset_tags_with_options_async(
        self,
        request: easy_gene_20210315_models.ListPublicDatasetTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.ListPublicDatasetTagsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListPublicDatasetTagsResponse(),
            await self.do_rpcrequest_async('ListPublicDatasetTags', '2021-03-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_public_dataset_tags(
        self,
        request: easy_gene_20210315_models.ListPublicDatasetTagsRequest,
    ) -> easy_gene_20210315_models.ListPublicDatasetTagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_public_dataset_tags_with_options(request, runtime)

    async def list_public_dataset_tags_async(
        self,
        request: easy_gene_20210315_models.ListPublicDatasetTagsRequest,
    ) -> easy_gene_20210315_models.ListPublicDatasetTagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_public_dataset_tags_with_options_async(request, runtime)

    def list_regions_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.ListRegionsResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            easy_gene_20210315_models.ListRegionsResponse(),
            self.do_rpcrequest('ListRegions', '2021-03-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_regions_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.ListRegionsResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            easy_gene_20210315_models.ListRegionsResponse(),
            await self.do_rpcrequest_async('ListRegions', '2021-03-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_regions(self) -> easy_gene_20210315_models.ListRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_regions_with_options(runtime)

    async def list_regions_async(self) -> easy_gene_20210315_models.ListRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_regions_with_options_async(runtime)

    def list_runs_with_options(
        self,
        request: easy_gene_20210315_models.ListRunsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.ListRunsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListRunsResponse(),
            self.do_rpcrequest('ListRuns', '2021-03-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_runs_with_options_async(
        self,
        request: easy_gene_20210315_models.ListRunsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.ListRunsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListRunsResponse(),
            await self.do_rpcrequest_async('ListRuns', '2021-03-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_runs(
        self,
        request: easy_gene_20210315_models.ListRunsRequest,
    ) -> easy_gene_20210315_models.ListRunsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_runs_with_options(request, runtime)

    async def list_runs_async(
        self,
        request: easy_gene_20210315_models.ListRunsRequest,
    ) -> easy_gene_20210315_models.ListRunsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_runs_with_options_async(request, runtime)

    def list_submissions_with_options(
        self,
        request: easy_gene_20210315_models.ListSubmissionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.ListSubmissionsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListSubmissionsResponse(),
            self.do_rpcrequest('ListSubmissions', '2021-03-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_submissions_with_options_async(
        self,
        request: easy_gene_20210315_models.ListSubmissionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.ListSubmissionsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListSubmissionsResponse(),
            await self.do_rpcrequest_async('ListSubmissions', '2021-03-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_submissions(
        self,
        request: easy_gene_20210315_models.ListSubmissionsRequest,
    ) -> easy_gene_20210315_models.ListSubmissionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_submissions_with_options(request, runtime)

    async def list_submissions_async(
        self,
        request: easy_gene_20210315_models.ListSubmissionsRequest,
    ) -> easy_gene_20210315_models.ListSubmissionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_submissions_with_options_async(request, runtime)

    def list_templates_with_options(
        self,
        request: easy_gene_20210315_models.ListTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.ListTemplatesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListTemplatesResponse(),
            self.do_rpcrequest('ListTemplates', '2021-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_templates_with_options_async(
        self,
        request: easy_gene_20210315_models.ListTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.ListTemplatesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListTemplatesResponse(),
            await self.do_rpcrequest_async('ListTemplates', '2021-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_templates(
        self,
        request: easy_gene_20210315_models.ListTemplatesRequest,
    ) -> easy_gene_20210315_models.ListTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_templates_with_options(request, runtime)

    async def list_templates_async(
        self,
        request: easy_gene_20210315_models.ListTemplatesRequest,
    ) -> easy_gene_20210315_models.ListTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_templates_with_options_async(request, runtime)

    def list_user_active_runs_with_options(
        self,
        request: easy_gene_20210315_models.ListUserActiveRunsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.ListUserActiveRunsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListUserActiveRunsResponse(),
            self.do_rpcrequest('ListUserActiveRuns', '2021-03-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_user_active_runs_with_options_async(
        self,
        request: easy_gene_20210315_models.ListUserActiveRunsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.ListUserActiveRunsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListUserActiveRunsResponse(),
            await self.do_rpcrequest_async('ListUserActiveRuns', '2021-03-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_user_active_runs(
        self,
        request: easy_gene_20210315_models.ListUserActiveRunsRequest,
    ) -> easy_gene_20210315_models.ListUserActiveRunsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_user_active_runs_with_options(request, runtime)

    async def list_user_active_runs_async(
        self,
        request: easy_gene_20210315_models.ListUserActiveRunsRequest,
    ) -> easy_gene_20210315_models.ListUserActiveRunsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_user_active_runs_with_options_async(request, runtime)

    def list_workspaces_with_options(
        self,
        request: easy_gene_20210315_models.ListWorkspacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.ListWorkspacesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListWorkspacesResponse(),
            self.do_rpcrequest('ListWorkspaces', '2021-03-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_workspaces_with_options_async(
        self,
        request: easy_gene_20210315_models.ListWorkspacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.ListWorkspacesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListWorkspacesResponse(),
            await self.do_rpcrequest_async('ListWorkspaces', '2021-03-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_workspaces(
        self,
        request: easy_gene_20210315_models.ListWorkspacesRequest,
    ) -> easy_gene_20210315_models.ListWorkspacesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_workspaces_with_options(request, runtime)

    async def list_workspaces_async(
        self,
        request: easy_gene_20210315_models.ListWorkspacesRequest,
    ) -> easy_gene_20210315_models.ListWorkspacesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_workspaces_with_options_async(request, runtime)

    def parse_app_inputs_with_options(
        self,
        tmp_req: easy_gene_20210315_models.ParseAppInputsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.ParseAppInputsResponse:
        UtilClient.validate_model(tmp_req)
        request = easy_gene_20210315_models.ParseAppInputsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dependencies):
            request.dependencies_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dependencies, 'Dependencies', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ParseAppInputsResponse(),
            self.do_rpcrequest('ParseAppInputs', '2021-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def parse_app_inputs_with_options_async(
        self,
        tmp_req: easy_gene_20210315_models.ParseAppInputsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.ParseAppInputsResponse:
        UtilClient.validate_model(tmp_req)
        request = easy_gene_20210315_models.ParseAppInputsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dependencies):
            request.dependencies_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dependencies, 'Dependencies', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ParseAppInputsResponse(),
            await self.do_rpcrequest_async('ParseAppInputs', '2021-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def parse_app_inputs(
        self,
        request: easy_gene_20210315_models.ParseAppInputsRequest,
    ) -> easy_gene_20210315_models.ParseAppInputsResponse:
        runtime = util_models.RuntimeOptions()
        return self.parse_app_inputs_with_options(request, runtime)

    async def parse_app_inputs_async(
        self,
        request: easy_gene_20210315_models.ParseAppInputsRequest,
    ) -> easy_gene_20210315_models.ParseAppInputsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.parse_app_inputs_with_options_async(request, runtime)

    def resume_submission_with_options(
        self,
        request: easy_gene_20210315_models.ResumeSubmissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.ResumeSubmissionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ResumeSubmissionResponse(),
            self.do_rpcrequest('ResumeSubmission', '2021-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def resume_submission_with_options_async(
        self,
        request: easy_gene_20210315_models.ResumeSubmissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.ResumeSubmissionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ResumeSubmissionResponse(),
            await self.do_rpcrequest_async('ResumeSubmission', '2021-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def resume_submission(
        self,
        request: easy_gene_20210315_models.ResumeSubmissionRequest,
    ) -> easy_gene_20210315_models.ResumeSubmissionResponse:
        runtime = util_models.RuntimeOptions()
        return self.resume_submission_with_options(request, runtime)

    async def resume_submission_async(
        self,
        request: easy_gene_20210315_models.ResumeSubmissionRequest,
    ) -> easy_gene_20210315_models.ResumeSubmissionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.resume_submission_with_options_async(request, runtime)

    def update_entity_with_options(
        self,
        tmp_req: easy_gene_20210315_models.UpdateEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.UpdateEntityResponse:
        UtilClient.validate_model(tmp_req)
        request = easy_gene_20210315_models.UpdateEntityShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.entity_items):
            request.entity_items_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.entity_items, 'EntityItems', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.UpdateEntityResponse(),
            self.do_rpcrequest('UpdateEntity', '2021-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_entity_with_options_async(
        self,
        tmp_req: easy_gene_20210315_models.UpdateEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.UpdateEntityResponse:
        UtilClient.validate_model(tmp_req)
        request = easy_gene_20210315_models.UpdateEntityShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.entity_items):
            request.entity_items_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.entity_items, 'EntityItems', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.UpdateEntityResponse(),
            await self.do_rpcrequest_async('UpdateEntity', '2021-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_entity(
        self,
        request: easy_gene_20210315_models.UpdateEntityRequest,
    ) -> easy_gene_20210315_models.UpdateEntityResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_entity_with_options(request, runtime)

    async def update_entity_async(
        self,
        request: easy_gene_20210315_models.UpdateEntityRequest,
    ) -> easy_gene_20210315_models.UpdateEntityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_entity_with_options_async(request, runtime)

    def update_template_with_options(
        self,
        tmp_req: easy_gene_20210315_models.UpdateTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.UpdateTemplateResponse:
        UtilClient.validate_model(tmp_req)
        request = easy_gene_20210315_models.UpdateTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.inputs):
            request.inputs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.inputs, 'Inputs', 'json')
        if not UtilClient.is_unset(tmp_req.outputs):
            request.outputs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.outputs, 'Outputs', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.UpdateTemplateResponse(),
            self.do_rpcrequest('UpdateTemplate', '2021-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_template_with_options_async(
        self,
        tmp_req: easy_gene_20210315_models.UpdateTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.UpdateTemplateResponse:
        UtilClient.validate_model(tmp_req)
        request = easy_gene_20210315_models.UpdateTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.inputs):
            request.inputs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.inputs, 'Inputs', 'json')
        if not UtilClient.is_unset(tmp_req.outputs):
            request.outputs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.outputs, 'Outputs', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.UpdateTemplateResponse(),
            await self.do_rpcrequest_async('UpdateTemplate', '2021-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_template(
        self,
        request: easy_gene_20210315_models.UpdateTemplateRequest,
    ) -> easy_gene_20210315_models.UpdateTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_template_with_options(request, runtime)

    async def update_template_async(
        self,
        request: easy_gene_20210315_models.UpdateTemplateRequest,
    ) -> easy_gene_20210315_models.UpdateTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_template_with_options_async(request, runtime)

    def update_workspace_with_options(
        self,
        request: easy_gene_20210315_models.UpdateWorkspaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.UpdateWorkspaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.UpdateWorkspaceResponse(),
            self.do_rpcrequest('UpdateWorkspace', '2021-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_workspace_with_options_async(
        self,
        request: easy_gene_20210315_models.UpdateWorkspaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.UpdateWorkspaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.UpdateWorkspaceResponse(),
            await self.do_rpcrequest_async('UpdateWorkspace', '2021-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_workspace(
        self,
        request: easy_gene_20210315_models.UpdateWorkspaceRequest,
    ) -> easy_gene_20210315_models.UpdateWorkspaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_workspace_with_options(request, runtime)

    async def update_workspace_async(
        self,
        request: easy_gene_20210315_models.UpdateWorkspaceRequest,
    ) -> easy_gene_20210315_models.UpdateWorkspaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_workspace_with_options_async(request, runtime)

    def upload_entity_with_options(
        self,
        request: easy_gene_20210315_models.UploadEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.UploadEntityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.UploadEntityResponse(),
            self.do_rpcrequest('UploadEntity', '2021-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def upload_entity_with_options_async(
        self,
        request: easy_gene_20210315_models.UploadEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.UploadEntityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.UploadEntityResponse(),
            await self.do_rpcrequest_async('UploadEntity', '2021-03-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upload_entity(
        self,
        request: easy_gene_20210315_models.UploadEntityRequest,
    ) -> easy_gene_20210315_models.UploadEntityResponse:
        runtime = util_models.RuntimeOptions()
        return self.upload_entity_with_options(request, runtime)

    async def upload_entity_async(
        self,
        request: easy_gene_20210315_models.UploadEntityRequest,
    ) -> easy_gene_20210315_models.UploadEntityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upload_entity_with_options_async(request, runtime)
