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
        """
        @summary 暂停任务
        
        @param request: AbortRunRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AbortRunResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.run_id):
            query['RunId'] = request.run_id
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AbortRun',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.AbortRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def abort_run_with_options_async(
        self,
        request: easy_gene_20210315_models.AbortRunRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.AbortRunResponse:
        """
        @summary 暂停任务
        
        @param request: AbortRunRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AbortRunResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.run_id):
            query['RunId'] = request.run_id
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AbortRun',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.AbortRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def abort_run(
        self,
        request: easy_gene_20210315_models.AbortRunRequest,
    ) -> easy_gene_20210315_models.AbortRunResponse:
        """
        @summary 暂停任务
        
        @param request: AbortRunRequest
        @return: AbortRunResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.abort_run_with_options(request, runtime)

    async def abort_run_async(
        self,
        request: easy_gene_20210315_models.AbortRunRequest,
    ) -> easy_gene_20210315_models.AbortRunResponse:
        """
        @summary 暂停任务
        
        @param request: AbortRunRequest
        @return: AbortRunResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.abort_run_with_options_async(request, runtime)

    def abort_submission_with_options(
        self,
        request: easy_gene_20210315_models.AbortSubmissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.AbortSubmissionResponse:
        """
        @summary 取消投递
        
        @param request: AbortSubmissionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AbortSubmissionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.submission_id):
            query['SubmissionId'] = request.submission_id
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AbortSubmission',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.AbortSubmissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def abort_submission_with_options_async(
        self,
        request: easy_gene_20210315_models.AbortSubmissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.AbortSubmissionResponse:
        """
        @summary 取消投递
        
        @param request: AbortSubmissionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AbortSubmissionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.submission_id):
            query['SubmissionId'] = request.submission_id
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AbortSubmission',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.AbortSubmissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def abort_submission(
        self,
        request: easy_gene_20210315_models.AbortSubmissionRequest,
    ) -> easy_gene_20210315_models.AbortSubmissionResponse:
        """
        @summary 取消投递
        
        @param request: AbortSubmissionRequest
        @return: AbortSubmissionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.abort_submission_with_options(request, runtime)

    async def abort_submission_async(
        self,
        request: easy_gene_20210315_models.AbortSubmissionRequest,
    ) -> easy_gene_20210315_models.AbortSubmissionResponse:
        """
        @summary 取消投递
        
        @param request: AbortSubmissionRequest
        @return: AbortSubmissionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.abort_submission_with_options_async(request, runtime)

    def copy_public_entity_with_options(
        self,
        request: easy_gene_20210315_models.CopyPublicEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.CopyPublicEntityResponse:
        """
        @summary 拷贝公共数据集的数据表格
        
        @param request: CopyPublicEntityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CopyPublicEntityResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset):
            query['Dataset'] = request.dataset
        if not UtilClient.is_unset(request.entity_type):
            query['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CopyPublicEntity',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.CopyPublicEntityResponse(),
            self.call_api(params, req, runtime)
        )

    async def copy_public_entity_with_options_async(
        self,
        request: easy_gene_20210315_models.CopyPublicEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.CopyPublicEntityResponse:
        """
        @summary 拷贝公共数据集的数据表格
        
        @param request: CopyPublicEntityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CopyPublicEntityResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset):
            query['Dataset'] = request.dataset
        if not UtilClient.is_unset(request.entity_type):
            query['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CopyPublicEntity',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.CopyPublicEntityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def copy_public_entity(
        self,
        request: easy_gene_20210315_models.CopyPublicEntityRequest,
    ) -> easy_gene_20210315_models.CopyPublicEntityResponse:
        """
        @summary 拷贝公共数据集的数据表格
        
        @param request: CopyPublicEntityRequest
        @return: CopyPublicEntityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.copy_public_entity_with_options(request, runtime)

    async def copy_public_entity_async(
        self,
        request: easy_gene_20210315_models.CopyPublicEntityRequest,
    ) -> easy_gene_20210315_models.CopyPublicEntityResponse:
        """
        @summary 拷贝公共数据集的数据表格
        
        @param request: CopyPublicEntityRequest
        @return: CopyPublicEntityResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.copy_public_entity_with_options_async(request, runtime)

    def create_app_with_options(
        self,
        tmp_req: easy_gene_20210315_models.CreateAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.CreateAppResponse:
        """
        @summary 创建应用
        
        @param tmp_req: CreateAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAppResponse
        """
        UtilClient.validate_model(tmp_req)
        request = easy_gene_20210315_models.CreateAppShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.configs):
            request.configs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.configs, 'Configs', 'json')
        if not UtilClient.is_unset(tmp_req.dependencies):
            request.dependencies_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dependencies, 'Dependencies', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_type):
            query['AppType'] = request.app_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.language_version):
            query['LanguageVersion'] = request.language_version
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.revision_comment):
            query['RevisionComment'] = request.revision_comment
        if not UtilClient.is_unset(request.revision_tag):
            query['RevisionTag'] = request.revision_tag
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        body = {}
        if not UtilClient.is_unset(request.configs_shrink):
            body['Configs'] = request.configs_shrink
        if not UtilClient.is_unset(request.definition):
            body['Definition'] = request.definition
        if not UtilClient.is_unset(request.dependencies_shrink):
            body['Dependencies'] = request.dependencies_shrink
        if not UtilClient.is_unset(request.documentation):
            body['Documentation'] = request.documentation
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateApp',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.CreateAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_app_with_options_async(
        self,
        tmp_req: easy_gene_20210315_models.CreateAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.CreateAppResponse:
        """
        @summary 创建应用
        
        @param tmp_req: CreateAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAppResponse
        """
        UtilClient.validate_model(tmp_req)
        request = easy_gene_20210315_models.CreateAppShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.configs):
            request.configs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.configs, 'Configs', 'json')
        if not UtilClient.is_unset(tmp_req.dependencies):
            request.dependencies_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dependencies, 'Dependencies', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_type):
            query['AppType'] = request.app_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.language_version):
            query['LanguageVersion'] = request.language_version
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.revision_comment):
            query['RevisionComment'] = request.revision_comment
        if not UtilClient.is_unset(request.revision_tag):
            query['RevisionTag'] = request.revision_tag
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        body = {}
        if not UtilClient.is_unset(request.configs_shrink):
            body['Configs'] = request.configs_shrink
        if not UtilClient.is_unset(request.definition):
            body['Definition'] = request.definition
        if not UtilClient.is_unset(request.dependencies_shrink):
            body['Dependencies'] = request.dependencies_shrink
        if not UtilClient.is_unset(request.documentation):
            body['Documentation'] = request.documentation
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateApp',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.CreateAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_app(
        self,
        request: easy_gene_20210315_models.CreateAppRequest,
    ) -> easy_gene_20210315_models.CreateAppResponse:
        """
        @summary 创建应用
        
        @param request: CreateAppRequest
        @return: CreateAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_app_with_options(request, runtime)

    async def create_app_async(
        self,
        request: easy_gene_20210315_models.CreateAppRequest,
    ) -> easy_gene_20210315_models.CreateAppResponse:
        """
        @summary 创建应用
        
        @param request: CreateAppRequest
        @return: CreateAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_app_with_options_async(request, runtime)

    def create_entity_with_options(
        self,
        tmp_req: easy_gene_20210315_models.CreateEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.CreateEntityResponse:
        """
        @summary 创建数据表格
        
        @param tmp_req: CreateEntityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateEntityResponse
        """
        UtilClient.validate_model(tmp_req)
        request = easy_gene_20210315_models.CreateEntityShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.entity_items):
            request.entity_items_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.entity_items, 'EntityItems', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.entity_type):
            query['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        body = {}
        if not UtilClient.is_unset(request.entity_items_shrink):
            body['EntityItems'] = request.entity_items_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateEntity',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.CreateEntityResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_entity_with_options_async(
        self,
        tmp_req: easy_gene_20210315_models.CreateEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.CreateEntityResponse:
        """
        @summary 创建数据表格
        
        @param tmp_req: CreateEntityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateEntityResponse
        """
        UtilClient.validate_model(tmp_req)
        request = easy_gene_20210315_models.CreateEntityShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.entity_items):
            request.entity_items_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.entity_items, 'EntityItems', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.entity_type):
            query['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        body = {}
        if not UtilClient.is_unset(request.entity_items_shrink):
            body['EntityItems'] = request.entity_items_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateEntity',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.CreateEntityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_entity(
        self,
        request: easy_gene_20210315_models.CreateEntityRequest,
    ) -> easy_gene_20210315_models.CreateEntityResponse:
        """
        @summary 创建数据表格
        
        @param request: CreateEntityRequest
        @return: CreateEntityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_entity_with_options(request, runtime)

    async def create_entity_async(
        self,
        request: easy_gene_20210315_models.CreateEntityRequest,
    ) -> easy_gene_20210315_models.CreateEntityResponse:
        """
        @summary 创建数据表格
        
        @param request: CreateEntityRequest
        @return: CreateEntityResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_entity_with_options_async(request, runtime)

    def create_run_with_options(
        self,
        tmp_req: easy_gene_20210315_models.CreateRunRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.CreateRunResponse:
        """
        @summary 创建任务
        
        @param tmp_req: CreateRunRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRunResponse
        """
        UtilClient.validate_model(tmp_req)
        request = easy_gene_20210315_models.CreateRunShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.execute_options):
            request.execute_options_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.execute_options, 'ExecuteOptions', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_revision):
            query['AppRevision'] = request.app_revision
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.default_runtime):
            query['DefaultRuntime'] = request.default_runtime
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.execute_directory):
            query['ExecuteDirectory'] = request.execute_directory
        if not UtilClient.is_unset(request.execute_options_shrink):
            query['ExecuteOptions'] = request.execute_options_shrink
        if not UtilClient.is_unset(request.inputs):
            query['Inputs'] = request.inputs
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        if not UtilClient.is_unset(request.output_folder):
            query['OutputFolder'] = request.output_folder
        if not UtilClient.is_unset(request.revision_tag):
            query['RevisionTag'] = request.revision_tag
        if not UtilClient.is_unset(request.role):
            query['Role'] = request.role
        if not UtilClient.is_unset(request.run_name):
            query['RunName'] = request.run_name
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRun',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.CreateRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_run_with_options_async(
        self,
        tmp_req: easy_gene_20210315_models.CreateRunRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.CreateRunResponse:
        """
        @summary 创建任务
        
        @param tmp_req: CreateRunRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRunResponse
        """
        UtilClient.validate_model(tmp_req)
        request = easy_gene_20210315_models.CreateRunShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.execute_options):
            request.execute_options_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.execute_options, 'ExecuteOptions', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_revision):
            query['AppRevision'] = request.app_revision
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.default_runtime):
            query['DefaultRuntime'] = request.default_runtime
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.execute_directory):
            query['ExecuteDirectory'] = request.execute_directory
        if not UtilClient.is_unset(request.execute_options_shrink):
            query['ExecuteOptions'] = request.execute_options_shrink
        if not UtilClient.is_unset(request.inputs):
            query['Inputs'] = request.inputs
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        if not UtilClient.is_unset(request.output_folder):
            query['OutputFolder'] = request.output_folder
        if not UtilClient.is_unset(request.revision_tag):
            query['RevisionTag'] = request.revision_tag
        if not UtilClient.is_unset(request.role):
            query['Role'] = request.role
        if not UtilClient.is_unset(request.run_name):
            query['RunName'] = request.run_name
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRun',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.CreateRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_run(
        self,
        request: easy_gene_20210315_models.CreateRunRequest,
    ) -> easy_gene_20210315_models.CreateRunResponse:
        """
        @summary 创建任务
        
        @param request: CreateRunRequest
        @return: CreateRunResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_run_with_options(request, runtime)

    async def create_run_async(
        self,
        request: easy_gene_20210315_models.CreateRunRequest,
    ) -> easy_gene_20210315_models.CreateRunResponse:
        """
        @summary 创建任务
        
        @param request: CreateRunRequest
        @return: CreateRunResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_run_with_options_async(request, runtime)

    def create_submission_with_options(
        self,
        tmp_req: easy_gene_20210315_models.CreateSubmissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.CreateSubmissionResponse:
        """
        @summary 创建提交
        
        @param tmp_req: CreateSubmissionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSubmissionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = easy_gene_20210315_models.CreateSubmissionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.entity_names):
            request.entity_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.entity_names, 'EntityNames', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.default_runtime):
            query['DefaultRuntime'] = request.default_runtime
        if not UtilClient.is_unset(request.entity_names_shrink):
            query['EntityNames'] = request.entity_names_shrink
        if not UtilClient.is_unset(request.entity_type):
            query['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.execute_directory):
            query['ExecuteDirectory'] = request.execute_directory
        if not UtilClient.is_unset(request.execute_options):
            query['ExecuteOptions'] = request.execute_options
        if not UtilClient.is_unset(request.inputs):
            query['Inputs'] = request.inputs
        if not UtilClient.is_unset(request.output_folder):
            query['OutputFolder'] = request.output_folder
        if not UtilClient.is_unset(request.outputs):
            query['Outputs'] = request.outputs
        if not UtilClient.is_unset(request.revision):
            query['Revision'] = request.revision
        if not UtilClient.is_unset(request.revision_tag):
            query['RevisionTag'] = request.revision_tag
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSubmission',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.CreateSubmissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_submission_with_options_async(
        self,
        tmp_req: easy_gene_20210315_models.CreateSubmissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.CreateSubmissionResponse:
        """
        @summary 创建提交
        
        @param tmp_req: CreateSubmissionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSubmissionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = easy_gene_20210315_models.CreateSubmissionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.entity_names):
            request.entity_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.entity_names, 'EntityNames', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.default_runtime):
            query['DefaultRuntime'] = request.default_runtime
        if not UtilClient.is_unset(request.entity_names_shrink):
            query['EntityNames'] = request.entity_names_shrink
        if not UtilClient.is_unset(request.entity_type):
            query['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.execute_directory):
            query['ExecuteDirectory'] = request.execute_directory
        if not UtilClient.is_unset(request.execute_options):
            query['ExecuteOptions'] = request.execute_options
        if not UtilClient.is_unset(request.inputs):
            query['Inputs'] = request.inputs
        if not UtilClient.is_unset(request.output_folder):
            query['OutputFolder'] = request.output_folder
        if not UtilClient.is_unset(request.outputs):
            query['Outputs'] = request.outputs
        if not UtilClient.is_unset(request.revision):
            query['Revision'] = request.revision
        if not UtilClient.is_unset(request.revision_tag):
            query['RevisionTag'] = request.revision_tag
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSubmission',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.CreateSubmissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_submission(
        self,
        request: easy_gene_20210315_models.CreateSubmissionRequest,
    ) -> easy_gene_20210315_models.CreateSubmissionResponse:
        """
        @summary 创建提交
        
        @param request: CreateSubmissionRequest
        @return: CreateSubmissionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_submission_with_options(request, runtime)

    async def create_submission_async(
        self,
        request: easy_gene_20210315_models.CreateSubmissionRequest,
    ) -> easy_gene_20210315_models.CreateSubmissionResponse:
        """
        @summary 创建提交
        
        @param request: CreateSubmissionRequest
        @return: CreateSubmissionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_submission_with_options_async(request, runtime)

    def create_template_with_options(
        self,
        tmp_req: easy_gene_20210315_models.CreateTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.CreateTemplateResponse:
        """
        @summary 创建应用模板
        
        @param tmp_req: CreateTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTemplateResponse
        """
        UtilClient.validate_model(tmp_req)
        request = easy_gene_20210315_models.CreateTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.inputs_expression):
            request.inputs_expression_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.inputs_expression, 'InputsExpression', 'json')
        if not UtilClient.is_unset(tmp_req.outputs_expression):
            request.outputs_expression_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.outputs_expression, 'OutputsExpression', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_revision):
            query['AppRevision'] = request.app_revision
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        if not UtilClient.is_unset(request.revision_tag):
            query['RevisionTag'] = request.revision_tag
        if not UtilClient.is_unset(request.root_entity):
            query['RootEntity'] = request.root_entity
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        body = {}
        if not UtilClient.is_unset(request.inputs_expression_shrink):
            body['InputsExpression'] = request.inputs_expression_shrink
        if not UtilClient.is_unset(request.outputs_expression_shrink):
            body['OutputsExpression'] = request.outputs_expression_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTemplate',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.CreateTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_template_with_options_async(
        self,
        tmp_req: easy_gene_20210315_models.CreateTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.CreateTemplateResponse:
        """
        @summary 创建应用模板
        
        @param tmp_req: CreateTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTemplateResponse
        """
        UtilClient.validate_model(tmp_req)
        request = easy_gene_20210315_models.CreateTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.inputs_expression):
            request.inputs_expression_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.inputs_expression, 'InputsExpression', 'json')
        if not UtilClient.is_unset(tmp_req.outputs_expression):
            request.outputs_expression_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.outputs_expression, 'OutputsExpression', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_revision):
            query['AppRevision'] = request.app_revision
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        if not UtilClient.is_unset(request.revision_tag):
            query['RevisionTag'] = request.revision_tag
        if not UtilClient.is_unset(request.root_entity):
            query['RootEntity'] = request.root_entity
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        body = {}
        if not UtilClient.is_unset(request.inputs_expression_shrink):
            body['InputsExpression'] = request.inputs_expression_shrink
        if not UtilClient.is_unset(request.outputs_expression_shrink):
            body['OutputsExpression'] = request.outputs_expression_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTemplate',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.CreateTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_template(
        self,
        request: easy_gene_20210315_models.CreateTemplateRequest,
    ) -> easy_gene_20210315_models.CreateTemplateResponse:
        """
        @summary 创建应用模板
        
        @param request: CreateTemplateRequest
        @return: CreateTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_template_with_options(request, runtime)

    async def create_template_async(
        self,
        request: easy_gene_20210315_models.CreateTemplateRequest,
    ) -> easy_gene_20210315_models.CreateTemplateResponse:
        """
        @summary 创建应用模板
        
        @param request: CreateTemplateRequest
        @return: CreateTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_template_with_options_async(request, runtime)

    def create_workspace_with_options(
        self,
        request: easy_gene_20210315_models.CreateWorkspaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.CreateWorkspaceResponse:
        """
        @summary 创建工作空间
        
        @param request: CreateWorkspaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateWorkspaceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.job_lifecycle):
            query['JobLifecycle'] = request.job_lifecycle
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        if not UtilClient.is_unset(request.role):
            query['Role'] = request.role
        if not UtilClient.is_unset(request.storage):
            query['Storage'] = request.storage
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateWorkspace',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.CreateWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_workspace_with_options_async(
        self,
        request: easy_gene_20210315_models.CreateWorkspaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.CreateWorkspaceResponse:
        """
        @summary 创建工作空间
        
        @param request: CreateWorkspaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateWorkspaceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.job_lifecycle):
            query['JobLifecycle'] = request.job_lifecycle
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        if not UtilClient.is_unset(request.role):
            query['Role'] = request.role
        if not UtilClient.is_unset(request.storage):
            query['Storage'] = request.storage
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateWorkspace',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.CreateWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_workspace(
        self,
        request: easy_gene_20210315_models.CreateWorkspaceRequest,
    ) -> easy_gene_20210315_models.CreateWorkspaceResponse:
        """
        @summary 创建工作空间
        
        @param request: CreateWorkspaceRequest
        @return: CreateWorkspaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_workspace_with_options(request, runtime)

    async def create_workspace_async(
        self,
        request: easy_gene_20210315_models.CreateWorkspaceRequest,
    ) -> easy_gene_20210315_models.CreateWorkspaceResponse:
        """
        @summary 创建工作空间
        
        @param request: CreateWorkspaceRequest
        @return: CreateWorkspaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_workspace_with_options_async(request, runtime)

    def delete_app_with_options(
        self,
        request: easy_gene_20210315_models.DeleteAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.DeleteAppResponse:
        """
        @summary 删除应用
        
        @param request: DeleteAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAppResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.revision):
            query['Revision'] = request.revision
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApp',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.DeleteAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_app_with_options_async(
        self,
        request: easy_gene_20210315_models.DeleteAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.DeleteAppResponse:
        """
        @summary 删除应用
        
        @param request: DeleteAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAppResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.revision):
            query['Revision'] = request.revision
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApp',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.DeleteAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_app(
        self,
        request: easy_gene_20210315_models.DeleteAppRequest,
    ) -> easy_gene_20210315_models.DeleteAppResponse:
        """
        @summary 删除应用
        
        @param request: DeleteAppRequest
        @return: DeleteAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_app_with_options(request, runtime)

    async def delete_app_async(
        self,
        request: easy_gene_20210315_models.DeleteAppRequest,
    ) -> easy_gene_20210315_models.DeleteAppResponse:
        """
        @summary 删除应用
        
        @param request: DeleteAppRequest
        @return: DeleteAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_app_with_options_async(request, runtime)

    def delete_entity_with_options(
        self,
        request: easy_gene_20210315_models.DeleteEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.DeleteEntityResponse:
        """
        @summary 删除实体表格
        
        @param request: DeleteEntityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteEntityResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.entity_type):
            query['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEntity',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.DeleteEntityResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_entity_with_options_async(
        self,
        request: easy_gene_20210315_models.DeleteEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.DeleteEntityResponse:
        """
        @summary 删除实体表格
        
        @param request: DeleteEntityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteEntityResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.entity_type):
            query['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEntity',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.DeleteEntityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_entity(
        self,
        request: easy_gene_20210315_models.DeleteEntityRequest,
    ) -> easy_gene_20210315_models.DeleteEntityResponse:
        """
        @summary 删除实体表格
        
        @param request: DeleteEntityRequest
        @return: DeleteEntityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_entity_with_options(request, runtime)

    async def delete_entity_async(
        self,
        request: easy_gene_20210315_models.DeleteEntityRequest,
    ) -> easy_gene_20210315_models.DeleteEntityResponse:
        """
        @summary 删除实体表格
        
        @param request: DeleteEntityRequest
        @return: DeleteEntityResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_entity_with_options_async(request, runtime)

    def delete_entity_items_with_options(
        self,
        tmp_req: easy_gene_20210315_models.DeleteEntityItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.DeleteEntityItemsResponse:
        """
        @summary 删除数据表格的条目
        
        @param tmp_req: DeleteEntityItemsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteEntityItemsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = easy_gene_20210315_models.DeleteEntityItemsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.entity_names):
            request.entity_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.entity_names, 'EntityNames', 'json')
        query = {}
        if not UtilClient.is_unset(request.entity_names_shrink):
            query['EntityNames'] = request.entity_names_shrink
        if not UtilClient.is_unset(request.entity_type):
            query['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEntityItems',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.DeleteEntityItemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_entity_items_with_options_async(
        self,
        tmp_req: easy_gene_20210315_models.DeleteEntityItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.DeleteEntityItemsResponse:
        """
        @summary 删除数据表格的条目
        
        @param tmp_req: DeleteEntityItemsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteEntityItemsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = easy_gene_20210315_models.DeleteEntityItemsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.entity_names):
            request.entity_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.entity_names, 'EntityNames', 'json')
        query = {}
        if not UtilClient.is_unset(request.entity_names_shrink):
            query['EntityNames'] = request.entity_names_shrink
        if not UtilClient.is_unset(request.entity_type):
            query['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEntityItems',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.DeleteEntityItemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_entity_items(
        self,
        request: easy_gene_20210315_models.DeleteEntityItemsRequest,
    ) -> easy_gene_20210315_models.DeleteEntityItemsResponse:
        """
        @summary 删除数据表格的条目
        
        @param request: DeleteEntityItemsRequest
        @return: DeleteEntityItemsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_entity_items_with_options(request, runtime)

    async def delete_entity_items_async(
        self,
        request: easy_gene_20210315_models.DeleteEntityItemsRequest,
    ) -> easy_gene_20210315_models.DeleteEntityItemsResponse:
        """
        @summary 删除数据表格的条目
        
        @param request: DeleteEntityItemsRequest
        @return: DeleteEntityItemsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_entity_items_with_options_async(request, runtime)

    def delete_run_with_options(
        self,
        request: easy_gene_20210315_models.DeleteRunRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.DeleteRunResponse:
        """
        @summary 删除任务
        
        @param request: DeleteRunRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRunResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.run_id):
            query['RunId'] = request.run_id
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRun',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.DeleteRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_run_with_options_async(
        self,
        request: easy_gene_20210315_models.DeleteRunRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.DeleteRunResponse:
        """
        @summary 删除任务
        
        @param request: DeleteRunRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRunResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.run_id):
            query['RunId'] = request.run_id
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRun',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.DeleteRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_run(
        self,
        request: easy_gene_20210315_models.DeleteRunRequest,
    ) -> easy_gene_20210315_models.DeleteRunResponse:
        """
        @summary 删除任务
        
        @param request: DeleteRunRequest
        @return: DeleteRunResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_run_with_options(request, runtime)

    async def delete_run_async(
        self,
        request: easy_gene_20210315_models.DeleteRunRequest,
    ) -> easy_gene_20210315_models.DeleteRunResponse:
        """
        @summary 删除任务
        
        @param request: DeleteRunRequest
        @return: DeleteRunResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_run_with_options_async(request, runtime)

    def delete_submission_with_options(
        self,
        request: easy_gene_20210315_models.DeleteSubmissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.DeleteSubmissionResponse:
        """
        @summary 删除投递
        
        @param request: DeleteSubmissionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSubmissionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.submission_id):
            query['SubmissionId'] = request.submission_id
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSubmission',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.DeleteSubmissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_submission_with_options_async(
        self,
        request: easy_gene_20210315_models.DeleteSubmissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.DeleteSubmissionResponse:
        """
        @summary 删除投递
        
        @param request: DeleteSubmissionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSubmissionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.submission_id):
            query['SubmissionId'] = request.submission_id
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSubmission',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.DeleteSubmissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_submission(
        self,
        request: easy_gene_20210315_models.DeleteSubmissionRequest,
    ) -> easy_gene_20210315_models.DeleteSubmissionResponse:
        """
        @summary 删除投递
        
        @param request: DeleteSubmissionRequest
        @return: DeleteSubmissionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_submission_with_options(request, runtime)

    async def delete_submission_async(
        self,
        request: easy_gene_20210315_models.DeleteSubmissionRequest,
    ) -> easy_gene_20210315_models.DeleteSubmissionResponse:
        """
        @summary 删除投递
        
        @param request: DeleteSubmissionRequest
        @return: DeleteSubmissionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_submission_with_options_async(request, runtime)

    def delete_template_with_options(
        self,
        request: easy_gene_20210315_models.DeleteTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.DeleteTemplateResponse:
        """
        @summary 删除应用模板
        
        @param request: DeleteTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTemplate',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.DeleteTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_template_with_options_async(
        self,
        request: easy_gene_20210315_models.DeleteTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.DeleteTemplateResponse:
        """
        @summary 删除应用模板
        
        @param request: DeleteTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTemplate',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.DeleteTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_template(
        self,
        request: easy_gene_20210315_models.DeleteTemplateRequest,
    ) -> easy_gene_20210315_models.DeleteTemplateResponse:
        """
        @summary 删除应用模板
        
        @param request: DeleteTemplateRequest
        @return: DeleteTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_template_with_options(request, runtime)

    async def delete_template_async(
        self,
        request: easy_gene_20210315_models.DeleteTemplateRequest,
    ) -> easy_gene_20210315_models.DeleteTemplateResponse:
        """
        @summary 删除应用模板
        
        @param request: DeleteTemplateRequest
        @return: DeleteTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_template_with_options_async(request, runtime)

    def delete_workspace_with_options(
        self,
        request: easy_gene_20210315_models.DeleteWorkspaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.DeleteWorkspaceResponse:
        """
        @summary 删除工作空间
        
        @param request: DeleteWorkspaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteWorkspaceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteWorkspace',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.DeleteWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_workspace_with_options_async(
        self,
        request: easy_gene_20210315_models.DeleteWorkspaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.DeleteWorkspaceResponse:
        """
        @summary 删除工作空间
        
        @param request: DeleteWorkspaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteWorkspaceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteWorkspace',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.DeleteWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_workspace(
        self,
        request: easy_gene_20210315_models.DeleteWorkspaceRequest,
    ) -> easy_gene_20210315_models.DeleteWorkspaceResponse:
        """
        @summary 删除工作空间
        
        @param request: DeleteWorkspaceRequest
        @return: DeleteWorkspaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_workspace_with_options(request, runtime)

    async def delete_workspace_async(
        self,
        request: easy_gene_20210315_models.DeleteWorkspaceRequest,
    ) -> easy_gene_20210315_models.DeleteWorkspaceResponse:
        """
        @summary 删除工作空间
        
        @param request: DeleteWorkspaceRequest
        @return: DeleteWorkspaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_workspace_with_options_async(request, runtime)

    def download_entity_with_options(
        self,
        tmp_req: easy_gene_20210315_models.DownloadEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.DownloadEntityResponse:
        """
        @summary 下载数据表格
        
        @param tmp_req: DownloadEntityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DownloadEntityResponse
        """
        UtilClient.validate_model(tmp_req)
        request = easy_gene_20210315_models.DownloadEntityShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.entity_names):
            request.entity_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.entity_names, 'EntityNames', 'json')
        query = {}
        if not UtilClient.is_unset(request.entity_names_shrink):
            query['EntityNames'] = request.entity_names_shrink
        if not UtilClient.is_unset(request.entity_type):
            query['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DownloadEntity',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.DownloadEntityResponse(),
            self.call_api(params, req, runtime)
        )

    async def download_entity_with_options_async(
        self,
        tmp_req: easy_gene_20210315_models.DownloadEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.DownloadEntityResponse:
        """
        @summary 下载数据表格
        
        @param tmp_req: DownloadEntityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DownloadEntityResponse
        """
        UtilClient.validate_model(tmp_req)
        request = easy_gene_20210315_models.DownloadEntityShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.entity_names):
            request.entity_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.entity_names, 'EntityNames', 'json')
        query = {}
        if not UtilClient.is_unset(request.entity_names_shrink):
            query['EntityNames'] = request.entity_names_shrink
        if not UtilClient.is_unset(request.entity_type):
            query['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DownloadEntity',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.DownloadEntityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def download_entity(
        self,
        request: easy_gene_20210315_models.DownloadEntityRequest,
    ) -> easy_gene_20210315_models.DownloadEntityResponse:
        """
        @summary 下载数据表格
        
        @param request: DownloadEntityRequest
        @return: DownloadEntityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.download_entity_with_options(request, runtime)

    async def download_entity_async(
        self,
        request: easy_gene_20210315_models.DownloadEntityRequest,
    ) -> easy_gene_20210315_models.DownloadEntityResponse:
        """
        @summary 下载数据表格
        
        @param request: DownloadEntityRequest
        @return: DownloadEntityResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.download_entity_with_options_async(request, runtime)

    def get_app_with_options(
        self,
        request: easy_gene_20210315_models.GetAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.GetAppResponse:
        """
        @summary 查询应用详情
        
        @param request: GetAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAppResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.revision):
            query['Revision'] = request.revision
        if not UtilClient.is_unset(request.revision_tag):
            query['RevisionTag'] = request.revision_tag
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApp',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.GetAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_app_with_options_async(
        self,
        request: easy_gene_20210315_models.GetAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.GetAppResponse:
        """
        @summary 查询应用详情
        
        @param request: GetAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAppResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.revision):
            query['Revision'] = request.revision
        if not UtilClient.is_unset(request.revision_tag):
            query['RevisionTag'] = request.revision_tag
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApp',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.GetAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_app(
        self,
        request: easy_gene_20210315_models.GetAppRequest,
    ) -> easy_gene_20210315_models.GetAppResponse:
        """
        @summary 查询应用详情
        
        @param request: GetAppRequest
        @return: GetAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_app_with_options(request, runtime)

    async def get_app_async(
        self,
        request: easy_gene_20210315_models.GetAppRequest,
    ) -> easy_gene_20210315_models.GetAppResponse:
        """
        @summary 查询应用详情
        
        @param request: GetAppRequest
        @return: GetAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_app_with_options_async(request, runtime)

    def get_entity_with_options(
        self,
        request: easy_gene_20210315_models.GetEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.GetEntityResponse:
        """
        @summary 查询数据表格信息
        
        @param request: GetEntityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEntityResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.entity_type):
            query['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEntity',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.GetEntityResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_entity_with_options_async(
        self,
        request: easy_gene_20210315_models.GetEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.GetEntityResponse:
        """
        @summary 查询数据表格信息
        
        @param request: GetEntityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEntityResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.entity_type):
            query['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEntity',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.GetEntityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_entity(
        self,
        request: easy_gene_20210315_models.GetEntityRequest,
    ) -> easy_gene_20210315_models.GetEntityResponse:
        """
        @summary 查询数据表格信息
        
        @param request: GetEntityRequest
        @return: GetEntityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_entity_with_options(request, runtime)

    async def get_entity_async(
        self,
        request: easy_gene_20210315_models.GetEntityRequest,
    ) -> easy_gene_20210315_models.GetEntityResponse:
        """
        @summary 查询数据表格信息
        
        @param request: GetEntityRequest
        @return: GetEntityResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_entity_with_options_async(request, runtime)

    def get_global_app_with_options(
        self,
        tmp_req: easy_gene_20210315_models.GetGlobalAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.GetGlobalAppResponse:
        """
        @summary 查询平台公共应用详情
        
        @param tmp_req: GetGlobalAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetGlobalAppResponse
        """
        UtilClient.validate_model(tmp_req)
        request = easy_gene_20210315_models.GetGlobalAppShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.attributes):
            request.attributes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.attributes, 'Attributes', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetGlobalApp',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.GetGlobalAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_global_app_with_options_async(
        self,
        tmp_req: easy_gene_20210315_models.GetGlobalAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.GetGlobalAppResponse:
        """
        @summary 查询平台公共应用详情
        
        @param tmp_req: GetGlobalAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetGlobalAppResponse
        """
        UtilClient.validate_model(tmp_req)
        request = easy_gene_20210315_models.GetGlobalAppShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.attributes):
            request.attributes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.attributes, 'Attributes', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetGlobalApp',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.GetGlobalAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_global_app(
        self,
        request: easy_gene_20210315_models.GetGlobalAppRequest,
    ) -> easy_gene_20210315_models.GetGlobalAppResponse:
        """
        @summary 查询平台公共应用详情
        
        @param request: GetGlobalAppRequest
        @return: GetGlobalAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_global_app_with_options(request, runtime)

    async def get_global_app_async(
        self,
        request: easy_gene_20210315_models.GetGlobalAppRequest,
    ) -> easy_gene_20210315_models.GetGlobalAppResponse:
        """
        @summary 查询平台公共应用详情
        
        @param request: GetGlobalAppRequest
        @return: GetGlobalAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_global_app_with_options_async(request, runtime)

    def get_public_dataset_with_options(
        self,
        tmp_req: easy_gene_20210315_models.GetPublicDatasetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.GetPublicDatasetResponse:
        """
        @summary 查询平台公共数据集详情
        
        @param tmp_req: GetPublicDatasetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPublicDatasetResponse
        """
        UtilClient.validate_model(tmp_req)
        request = easy_gene_20210315_models.GetPublicDatasetShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.attributes):
            request.attributes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.attributes, 'Attributes', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPublicDataset',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.GetPublicDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_public_dataset_with_options_async(
        self,
        tmp_req: easy_gene_20210315_models.GetPublicDatasetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.GetPublicDatasetResponse:
        """
        @summary 查询平台公共数据集详情
        
        @param tmp_req: GetPublicDatasetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPublicDatasetResponse
        """
        UtilClient.validate_model(tmp_req)
        request = easy_gene_20210315_models.GetPublicDatasetShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.attributes):
            request.attributes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.attributes, 'Attributes', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPublicDataset',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.GetPublicDatasetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_public_dataset(
        self,
        request: easy_gene_20210315_models.GetPublicDatasetRequest,
    ) -> easy_gene_20210315_models.GetPublicDatasetResponse:
        """
        @summary 查询平台公共数据集详情
        
        @param request: GetPublicDatasetRequest
        @return: GetPublicDatasetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_public_dataset_with_options(request, runtime)

    async def get_public_dataset_async(
        self,
        request: easy_gene_20210315_models.GetPublicDatasetRequest,
    ) -> easy_gene_20210315_models.GetPublicDatasetResponse:
        """
        @summary 查询平台公共数据集详情
        
        @param request: GetPublicDatasetRequest
        @return: GetPublicDatasetResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_public_dataset_with_options_async(request, runtime)

    def get_public_dataset_entity_with_options(
        self,
        request: easy_gene_20210315_models.GetPublicDatasetEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.GetPublicDatasetEntityResponse:
        """
        @summary 查询平台公共数据集特定的实体定义
        
        @param request: GetPublicDatasetEntityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPublicDatasetEntityResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPublicDatasetEntity',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.GetPublicDatasetEntityResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_public_dataset_entity_with_options_async(
        self,
        request: easy_gene_20210315_models.GetPublicDatasetEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.GetPublicDatasetEntityResponse:
        """
        @summary 查询平台公共数据集特定的实体定义
        
        @param request: GetPublicDatasetEntityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPublicDatasetEntityResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPublicDatasetEntity',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.GetPublicDatasetEntityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_public_dataset_entity(
        self,
        request: easy_gene_20210315_models.GetPublicDatasetEntityRequest,
    ) -> easy_gene_20210315_models.GetPublicDatasetEntityResponse:
        """
        @summary 查询平台公共数据集特定的实体定义
        
        @param request: GetPublicDatasetEntityRequest
        @return: GetPublicDatasetEntityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_public_dataset_entity_with_options(request, runtime)

    async def get_public_dataset_entity_async(
        self,
        request: easy_gene_20210315_models.GetPublicDatasetEntityRequest,
    ) -> easy_gene_20210315_models.GetPublicDatasetEntityResponse:
        """
        @summary 查询平台公共数据集特定的实体定义
        
        @param request: GetPublicDatasetEntityRequest
        @return: GetPublicDatasetEntityResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_public_dataset_entity_with_options_async(request, runtime)

    def get_run_with_options(
        self,
        request: easy_gene_20210315_models.GetRunRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.GetRunResponse:
        """
        @summary 获取任务详情
        
        @param request: GetRunRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRunResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRun',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.GetRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_run_with_options_async(
        self,
        request: easy_gene_20210315_models.GetRunRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.GetRunResponse:
        """
        @summary 获取任务详情
        
        @param request: GetRunRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRunResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRun',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.GetRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_run(
        self,
        request: easy_gene_20210315_models.GetRunRequest,
    ) -> easy_gene_20210315_models.GetRunResponse:
        """
        @summary 获取任务详情
        
        @param request: GetRunRequest
        @return: GetRunResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_run_with_options(request, runtime)

    async def get_run_async(
        self,
        request: easy_gene_20210315_models.GetRunRequest,
    ) -> easy_gene_20210315_models.GetRunResponse:
        """
        @summary 获取任务详情
        
        @param request: GetRunRequest
        @return: GetRunResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_run_with_options_async(request, runtime)

    def get_submission_with_options(
        self,
        request: easy_gene_20210315_models.GetSubmissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.GetSubmissionResponse:
        """
        @summary 获取投递详情
        
        @param request: GetSubmissionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSubmissionResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSubmission',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.GetSubmissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_submission_with_options_async(
        self,
        request: easy_gene_20210315_models.GetSubmissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.GetSubmissionResponse:
        """
        @summary 获取投递详情
        
        @param request: GetSubmissionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSubmissionResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSubmission',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.GetSubmissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_submission(
        self,
        request: easy_gene_20210315_models.GetSubmissionRequest,
    ) -> easy_gene_20210315_models.GetSubmissionResponse:
        """
        @summary 获取投递详情
        
        @param request: GetSubmissionRequest
        @return: GetSubmissionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_submission_with_options(request, runtime)

    async def get_submission_async(
        self,
        request: easy_gene_20210315_models.GetSubmissionRequest,
    ) -> easy_gene_20210315_models.GetSubmissionResponse:
        """
        @summary 获取投递详情
        
        @param request: GetSubmissionRequest
        @return: GetSubmissionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_submission_with_options_async(request, runtime)

    def get_template_with_options(
        self,
        request: easy_gene_20210315_models.GetTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.GetTemplateResponse:
        """
        @summary 查询应用模板的详情
        
        @param request: GetTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTemplate',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.GetTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_template_with_options_async(
        self,
        request: easy_gene_20210315_models.GetTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.GetTemplateResponse:
        """
        @summary 查询应用模板的详情
        
        @param request: GetTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTemplate',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.GetTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_template(
        self,
        request: easy_gene_20210315_models.GetTemplateRequest,
    ) -> easy_gene_20210315_models.GetTemplateResponse:
        """
        @summary 查询应用模板的详情
        
        @param request: GetTemplateRequest
        @return: GetTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_template_with_options(request, runtime)

    async def get_template_async(
        self,
        request: easy_gene_20210315_models.GetTemplateRequest,
    ) -> easy_gene_20210315_models.GetTemplateResponse:
        """
        @summary 查询应用模板的详情
        
        @param request: GetTemplateRequest
        @return: GetTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_template_with_options_async(request, runtime)

    def get_workspace_with_options(
        self,
        request: easy_gene_20210315_models.GetWorkspaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.GetWorkspaceResponse:
        """
        @summary 查询工作空间详情
        
        @param request: GetWorkspaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWorkspaceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWorkspace',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.GetWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_workspace_with_options_async(
        self,
        request: easy_gene_20210315_models.GetWorkspaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.GetWorkspaceResponse:
        """
        @summary 查询工作空间详情
        
        @param request: GetWorkspaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWorkspaceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWorkspace',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.GetWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_workspace(
        self,
        request: easy_gene_20210315_models.GetWorkspaceRequest,
    ) -> easy_gene_20210315_models.GetWorkspaceResponse:
        """
        @summary 查询工作空间详情
        
        @param request: GetWorkspaceRequest
        @return: GetWorkspaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_workspace_with_options(request, runtime)

    async def get_workspace_async(
        self,
        request: easy_gene_20210315_models.GetWorkspaceRequest,
    ) -> easy_gene_20210315_models.GetWorkspaceResponse:
        """
        @summary 查询工作空间详情
        
        @param request: GetWorkspaceRequest
        @return: GetWorkspaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_workspace_with_options_async(request, runtime)

    def import_app_with_options(
        self,
        request: easy_gene_20210315_models.ImportAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.ImportAppResponse:
        """
        @summary 导入应用。
        
        @param request: ImportAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImportAppResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImportApp',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ImportAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_app_with_options_async(
        self,
        request: easy_gene_20210315_models.ImportAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.ImportAppResponse:
        """
        @summary 导入应用。
        
        @param request: ImportAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImportAppResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImportApp',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ImportAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_app(
        self,
        request: easy_gene_20210315_models.ImportAppRequest,
    ) -> easy_gene_20210315_models.ImportAppResponse:
        """
        @summary 导入应用。
        
        @param request: ImportAppRequest
        @return: ImportAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.import_app_with_options(request, runtime)

    async def import_app_async(
        self,
        request: easy_gene_20210315_models.ImportAppRequest,
    ) -> easy_gene_20210315_models.ImportAppResponse:
        """
        @summary 导入应用。
        
        @param request: ImportAppRequest
        @return: ImportAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.import_app_with_options_async(request, runtime)

    def install_global_app_with_options(
        self,
        request: easy_gene_20210315_models.InstallGlobalAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.InstallGlobalAppResponse:
        """
        @summary 安装平台公共应用到工作空间中。
        
        @param request: InstallGlobalAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InstallGlobalAppResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.installed_app_name):
            query['InstalledAppName'] = request.installed_app_name
        if not UtilClient.is_unset(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InstallGlobalApp',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.InstallGlobalAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def install_global_app_with_options_async(
        self,
        request: easy_gene_20210315_models.InstallGlobalAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.InstallGlobalAppResponse:
        """
        @summary 安装平台公共应用到工作空间中。
        
        @param request: InstallGlobalAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InstallGlobalAppResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.installed_app_name):
            query['InstalledAppName'] = request.installed_app_name
        if not UtilClient.is_unset(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InstallGlobalApp',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.InstallGlobalAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def install_global_app(
        self,
        request: easy_gene_20210315_models.InstallGlobalAppRequest,
    ) -> easy_gene_20210315_models.InstallGlobalAppResponse:
        """
        @summary 安装平台公共应用到工作空间中。
        
        @param request: InstallGlobalAppRequest
        @return: InstallGlobalAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.install_global_app_with_options(request, runtime)

    async def install_global_app_async(
        self,
        request: easy_gene_20210315_models.InstallGlobalAppRequest,
    ) -> easy_gene_20210315_models.InstallGlobalAppResponse:
        """
        @summary 安装平台公共应用到工作空间中。
        
        @param request: InstallGlobalAppRequest
        @return: InstallGlobalAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.install_global_app_with_options_async(request, runtime)

    def list_apps_with_options(
        self,
        request: easy_gene_20210315_models.ListAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.ListAppsResponse:
        """
        @summary 列出应用
        
        @param request: ListAppsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAppsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_type):
            query['AppType'] = request.app_type
        if not UtilClient.is_unset(request.is_reversed):
            query['IsReversed'] = request.is_reversed
        if not UtilClient.is_unset(request.label_selector):
            query['LabelSelector'] = request.label_selector
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        if not UtilClient.is_unset(request.search):
            query['Search'] = request.search
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApps',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListAppsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_apps_with_options_async(
        self,
        request: easy_gene_20210315_models.ListAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.ListAppsResponse:
        """
        @summary 列出应用
        
        @param request: ListAppsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAppsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_type):
            query['AppType'] = request.app_type
        if not UtilClient.is_unset(request.is_reversed):
            query['IsReversed'] = request.is_reversed
        if not UtilClient.is_unset(request.label_selector):
            query['LabelSelector'] = request.label_selector
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        if not UtilClient.is_unset(request.search):
            query['Search'] = request.search
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApps',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListAppsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_apps(
        self,
        request: easy_gene_20210315_models.ListAppsRequest,
    ) -> easy_gene_20210315_models.ListAppsResponse:
        """
        @summary 列出应用
        
        @param request: ListAppsRequest
        @return: ListAppsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_apps_with_options(request, runtime)

    async def list_apps_async(
        self,
        request: easy_gene_20210315_models.ListAppsRequest,
    ) -> easy_gene_20210315_models.ListAppsResponse:
        """
        @summary 列出应用
        
        @param request: ListAppsRequest
        @return: ListAppsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_apps_with_options_async(request, runtime)

    def list_authorized_software_with_options(
        self,
        request: easy_gene_20210315_models.ListAuthorizedSoftwareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.ListAuthorizedSoftwareResponse:
        """
        @summary 获取平台第三方软件列表
        
        @param request: ListAuthorizedSoftwareRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAuthorizedSoftwareResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAuthorizedSoftware',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListAuthorizedSoftwareResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_authorized_software_with_options_async(
        self,
        request: easy_gene_20210315_models.ListAuthorizedSoftwareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.ListAuthorizedSoftwareResponse:
        """
        @summary 获取平台第三方软件列表
        
        @param request: ListAuthorizedSoftwareRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAuthorizedSoftwareResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAuthorizedSoftware',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListAuthorizedSoftwareResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_authorized_software(
        self,
        request: easy_gene_20210315_models.ListAuthorizedSoftwareRequest,
    ) -> easy_gene_20210315_models.ListAuthorizedSoftwareResponse:
        """
        @summary 获取平台第三方软件列表
        
        @param request: ListAuthorizedSoftwareRequest
        @return: ListAuthorizedSoftwareResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_authorized_software_with_options(request, runtime)

    async def list_authorized_software_async(
        self,
        request: easy_gene_20210315_models.ListAuthorizedSoftwareRequest,
    ) -> easy_gene_20210315_models.ListAuthorizedSoftwareResponse:
        """
        @summary 获取平台第三方软件列表
        
        @param request: ListAuthorizedSoftwareRequest
        @return: ListAuthorizedSoftwareResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_authorized_software_with_options_async(request, runtime)

    def list_container_images_with_options(
        self,
        request: easy_gene_20210315_models.ListContainerImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.ListContainerImagesResponse:
        """
        @summary 获取平台公共容器镜像列表
        
        @param request: ListContainerImagesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListContainerImagesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListContainerImages',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListContainerImagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_container_images_with_options_async(
        self,
        request: easy_gene_20210315_models.ListContainerImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.ListContainerImagesResponse:
        """
        @summary 获取平台公共容器镜像列表
        
        @param request: ListContainerImagesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListContainerImagesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListContainerImages',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListContainerImagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_container_images(
        self,
        request: easy_gene_20210315_models.ListContainerImagesRequest,
    ) -> easy_gene_20210315_models.ListContainerImagesResponse:
        """
        @summary 获取平台公共容器镜像列表
        
        @param request: ListContainerImagesRequest
        @return: ListContainerImagesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_container_images_with_options(request, runtime)

    async def list_container_images_async(
        self,
        request: easy_gene_20210315_models.ListContainerImagesRequest,
    ) -> easy_gene_20210315_models.ListContainerImagesResponse:
        """
        @summary 获取平台公共容器镜像列表
        
        @param request: ListContainerImagesRequest
        @return: ListContainerImagesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_container_images_with_options_async(request, runtime)

    def list_entities_with_options(
        self,
        request: easy_gene_20210315_models.ListEntitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.ListEntitiesResponse:
        """
        @summary 列出数据实体列表
        
        @param request: ListEntitiesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEntitiesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEntities',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListEntitiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_entities_with_options_async(
        self,
        request: easy_gene_20210315_models.ListEntitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.ListEntitiesResponse:
        """
        @summary 列出数据实体列表
        
        @param request: ListEntitiesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEntitiesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEntities',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListEntitiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_entities(
        self,
        request: easy_gene_20210315_models.ListEntitiesRequest,
    ) -> easy_gene_20210315_models.ListEntitiesResponse:
        """
        @summary 列出数据实体列表
        
        @param request: ListEntitiesRequest
        @return: ListEntitiesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_entities_with_options(request, runtime)

    async def list_entities_async(
        self,
        request: easy_gene_20210315_models.ListEntitiesRequest,
    ) -> easy_gene_20210315_models.ListEntitiesResponse:
        """
        @summary 列出数据实体列表
        
        @param request: ListEntitiesRequest
        @return: ListEntitiesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_entities_with_options_async(request, runtime)

    def list_entity_items_with_options(
        self,
        request: easy_gene_20210315_models.ListEntityItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.ListEntityItemsResponse:
        """
        @summary 列出数据表格的条目
        
        @param request: ListEntityItemsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEntityItemsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.entity_type):
            query['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.is_reversed):
            query['IsReversed'] = request.is_reversed
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.search):
            query['Search'] = request.search
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEntityItems',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListEntityItemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_entity_items_with_options_async(
        self,
        request: easy_gene_20210315_models.ListEntityItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.ListEntityItemsResponse:
        """
        @summary 列出数据表格的条目
        
        @param request: ListEntityItemsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEntityItemsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.entity_type):
            query['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.is_reversed):
            query['IsReversed'] = request.is_reversed
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.search):
            query['Search'] = request.search
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEntityItems',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListEntityItemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_entity_items(
        self,
        request: easy_gene_20210315_models.ListEntityItemsRequest,
    ) -> easy_gene_20210315_models.ListEntityItemsResponse:
        """
        @summary 列出数据表格的条目
        
        @param request: ListEntityItemsRequest
        @return: ListEntityItemsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_entity_items_with_options(request, runtime)

    async def list_entity_items_async(
        self,
        request: easy_gene_20210315_models.ListEntityItemsRequest,
    ) -> easy_gene_20210315_models.ListEntityItemsResponse:
        """
        @summary 列出数据表格的条目
        
        @param request: ListEntityItemsRequest
        @return: ListEntityItemsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_entity_items_with_options_async(request, runtime)

    def list_global_apps_with_options(
        self,
        request: easy_gene_20210315_models.ListGlobalAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.ListGlobalAppsResponse:
        """
        @summary 获取平台公共应用列表
        
        @param request: ListGlobalAppsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListGlobalAppsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGlobalApps',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListGlobalAppsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_global_apps_with_options_async(
        self,
        request: easy_gene_20210315_models.ListGlobalAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.ListGlobalAppsResponse:
        """
        @summary 获取平台公共应用列表
        
        @param request: ListGlobalAppsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListGlobalAppsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGlobalApps',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListGlobalAppsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_global_apps(
        self,
        request: easy_gene_20210315_models.ListGlobalAppsRequest,
    ) -> easy_gene_20210315_models.ListGlobalAppsResponse:
        """
        @summary 获取平台公共应用列表
        
        @param request: ListGlobalAppsRequest
        @return: ListGlobalAppsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_global_apps_with_options(request, runtime)

    async def list_global_apps_async(
        self,
        request: easy_gene_20210315_models.ListGlobalAppsRequest,
    ) -> easy_gene_20210315_models.ListGlobalAppsResponse:
        """
        @summary 获取平台公共应用列表
        
        @param request: ListGlobalAppsRequest
        @return: ListGlobalAppsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_global_apps_with_options_async(request, runtime)

    def list_public_dataset_with_options(
        self,
        request: easy_gene_20210315_models.ListPublicDatasetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.ListPublicDatasetResponse:
        """
        @summary 获取平台公共数据集列表
        
        @param request: ListPublicDatasetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPublicDatasetResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPublicDataset',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListPublicDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_public_dataset_with_options_async(
        self,
        request: easy_gene_20210315_models.ListPublicDatasetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.ListPublicDatasetResponse:
        """
        @summary 获取平台公共数据集列表
        
        @param request: ListPublicDatasetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPublicDatasetResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPublicDataset',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListPublicDatasetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_public_dataset(
        self,
        request: easy_gene_20210315_models.ListPublicDatasetRequest,
    ) -> easy_gene_20210315_models.ListPublicDatasetResponse:
        """
        @summary 获取平台公共数据集列表
        
        @param request: ListPublicDatasetRequest
        @return: ListPublicDatasetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_public_dataset_with_options(request, runtime)

    async def list_public_dataset_async(
        self,
        request: easy_gene_20210315_models.ListPublicDatasetRequest,
    ) -> easy_gene_20210315_models.ListPublicDatasetResponse:
        """
        @summary 获取平台公共数据集列表
        
        @param request: ListPublicDatasetRequest
        @return: ListPublicDatasetResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_public_dataset_with_options_async(request, runtime)

    def list_public_dataset_entities_with_options(
        self,
        request: easy_gene_20210315_models.ListPublicDatasetEntitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.ListPublicDatasetEntitiesResponse:
        """
        @summary 查询平台公共数据集包含的实体列表
        
        @param request: ListPublicDatasetEntitiesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPublicDatasetEntitiesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPublicDatasetEntities',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListPublicDatasetEntitiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_public_dataset_entities_with_options_async(
        self,
        request: easy_gene_20210315_models.ListPublicDatasetEntitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.ListPublicDatasetEntitiesResponse:
        """
        @summary 查询平台公共数据集包含的实体列表
        
        @param request: ListPublicDatasetEntitiesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPublicDatasetEntitiesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPublicDatasetEntities',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListPublicDatasetEntitiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_public_dataset_entities(
        self,
        request: easy_gene_20210315_models.ListPublicDatasetEntitiesRequest,
    ) -> easy_gene_20210315_models.ListPublicDatasetEntitiesResponse:
        """
        @summary 查询平台公共数据集包含的实体列表
        
        @param request: ListPublicDatasetEntitiesRequest
        @return: ListPublicDatasetEntitiesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_public_dataset_entities_with_options(request, runtime)

    async def list_public_dataset_entities_async(
        self,
        request: easy_gene_20210315_models.ListPublicDatasetEntitiesRequest,
    ) -> easy_gene_20210315_models.ListPublicDatasetEntitiesResponse:
        """
        @summary 查询平台公共数据集包含的实体列表
        
        @param request: ListPublicDatasetEntitiesRequest
        @return: ListPublicDatasetEntitiesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_public_dataset_entities_with_options_async(request, runtime)

    def list_public_dataset_entity_items_with_options(
        self,
        request: easy_gene_20210315_models.ListPublicDatasetEntityItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.ListPublicDatasetEntityItemsResponse:
        """
        @summary 查询平台公共数据集特定的实体表格数据
        
        @param request: ListPublicDatasetEntityItemsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPublicDatasetEntityItemsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPublicDatasetEntityItems',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListPublicDatasetEntityItemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_public_dataset_entity_items_with_options_async(
        self,
        request: easy_gene_20210315_models.ListPublicDatasetEntityItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.ListPublicDatasetEntityItemsResponse:
        """
        @summary 查询平台公共数据集特定的实体表格数据
        
        @param request: ListPublicDatasetEntityItemsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPublicDatasetEntityItemsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPublicDatasetEntityItems',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListPublicDatasetEntityItemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_public_dataset_entity_items(
        self,
        request: easy_gene_20210315_models.ListPublicDatasetEntityItemsRequest,
    ) -> easy_gene_20210315_models.ListPublicDatasetEntityItemsResponse:
        """
        @summary 查询平台公共数据集特定的实体表格数据
        
        @param request: ListPublicDatasetEntityItemsRequest
        @return: ListPublicDatasetEntityItemsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_public_dataset_entity_items_with_options(request, runtime)

    async def list_public_dataset_entity_items_async(
        self,
        request: easy_gene_20210315_models.ListPublicDatasetEntityItemsRequest,
    ) -> easy_gene_20210315_models.ListPublicDatasetEntityItemsResponse:
        """
        @summary 查询平台公共数据集特定的实体表格数据
        
        @param request: ListPublicDatasetEntityItemsRequest
        @return: ListPublicDatasetEntityItemsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_public_dataset_entity_items_with_options_async(request, runtime)

    def list_public_dataset_tags_with_options(
        self,
        request: easy_gene_20210315_models.ListPublicDatasetTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.ListPublicDatasetTagsResponse:
        """
        @summary 列出所有公共数据集标签
        
        @param request: ListPublicDatasetTagsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPublicDatasetTagsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPublicDatasetTags',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListPublicDatasetTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_public_dataset_tags_with_options_async(
        self,
        request: easy_gene_20210315_models.ListPublicDatasetTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.ListPublicDatasetTagsResponse:
        """
        @summary 列出所有公共数据集标签
        
        @param request: ListPublicDatasetTagsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPublicDatasetTagsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPublicDatasetTags',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListPublicDatasetTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_public_dataset_tags(
        self,
        request: easy_gene_20210315_models.ListPublicDatasetTagsRequest,
    ) -> easy_gene_20210315_models.ListPublicDatasetTagsResponse:
        """
        @summary 列出所有公共数据集标签
        
        @param request: ListPublicDatasetTagsRequest
        @return: ListPublicDatasetTagsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_public_dataset_tags_with_options(request, runtime)

    async def list_public_dataset_tags_async(
        self,
        request: easy_gene_20210315_models.ListPublicDatasetTagsRequest,
    ) -> easy_gene_20210315_models.ListPublicDatasetTagsResponse:
        """
        @summary 列出所有公共数据集标签
        
        @param request: ListPublicDatasetTagsRequest
        @return: ListPublicDatasetTagsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_public_dataset_tags_with_options_async(request, runtime)

    def list_regions_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.ListRegionsResponse:
        """
        @summary 查询基因分析平台产品的可用地域。
        
        @param request: ListRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRegionsResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListRegions',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_regions_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.ListRegionsResponse:
        """
        @summary 查询基因分析平台产品的可用地域。
        
        @param request: ListRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRegionsResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListRegions',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_regions(self) -> easy_gene_20210315_models.ListRegionsResponse:
        """
        @summary 查询基因分析平台产品的可用地域。
        
        @return: ListRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_regions_with_options(runtime)

    async def list_regions_async(self) -> easy_gene_20210315_models.ListRegionsResponse:
        """
        @summary 查询基因分析平台产品的可用地域。
        
        @return: ListRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_regions_with_options_async(runtime)

    def list_runs_with_options(
        self,
        request: easy_gene_20210315_models.ListRunsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.ListRunsResponse:
        """
        @summary 列出任务
        
        @param request: ListRunsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRunsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRuns',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListRunsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_runs_with_options_async(
        self,
        request: easy_gene_20210315_models.ListRunsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.ListRunsResponse:
        """
        @summary 列出任务
        
        @param request: ListRunsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRunsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRuns',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListRunsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_runs(
        self,
        request: easy_gene_20210315_models.ListRunsRequest,
    ) -> easy_gene_20210315_models.ListRunsResponse:
        """
        @summary 列出任务
        
        @param request: ListRunsRequest
        @return: ListRunsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_runs_with_options(request, runtime)

    async def list_runs_async(
        self,
        request: easy_gene_20210315_models.ListRunsRequest,
    ) -> easy_gene_20210315_models.ListRunsResponse:
        """
        @summary 列出任务
        
        @param request: ListRunsRequest
        @return: ListRunsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_runs_with_options_async(request, runtime)

    def list_submissions_with_options(
        self,
        request: easy_gene_20210315_models.ListSubmissionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.ListSubmissionsResponse:
        """
        @summary 列出投递
        
        @param request: ListSubmissionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSubmissionsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSubmissions',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListSubmissionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_submissions_with_options_async(
        self,
        request: easy_gene_20210315_models.ListSubmissionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.ListSubmissionsResponse:
        """
        @summary 列出投递
        
        @param request: ListSubmissionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSubmissionsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSubmissions',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListSubmissionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_submissions(
        self,
        request: easy_gene_20210315_models.ListSubmissionsRequest,
    ) -> easy_gene_20210315_models.ListSubmissionsResponse:
        """
        @summary 列出投递
        
        @param request: ListSubmissionsRequest
        @return: ListSubmissionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_submissions_with_options(request, runtime)

    async def list_submissions_async(
        self,
        request: easy_gene_20210315_models.ListSubmissionsRequest,
    ) -> easy_gene_20210315_models.ListSubmissionsResponse:
        """
        @summary 列出投递
        
        @param request: ListSubmissionsRequest
        @return: ListSubmissionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_submissions_with_options_async(request, runtime)

    def list_templates_with_options(
        self,
        request: easy_gene_20210315_models.ListTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.ListTemplatesResponse:
        """
        @summary 列出应用模板
        
        @param request: ListTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTemplatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.is_reversed):
            query['IsReversed'] = request.is_reversed
        if not UtilClient.is_unset(request.label_selector):
            query['LabelSelector'] = request.label_selector
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.search):
            query['Search'] = request.search
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTemplates',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_templates_with_options_async(
        self,
        request: easy_gene_20210315_models.ListTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.ListTemplatesResponse:
        """
        @summary 列出应用模板
        
        @param request: ListTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTemplatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.is_reversed):
            query['IsReversed'] = request.is_reversed
        if not UtilClient.is_unset(request.label_selector):
            query['LabelSelector'] = request.label_selector
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.search):
            query['Search'] = request.search
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTemplates',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_templates(
        self,
        request: easy_gene_20210315_models.ListTemplatesRequest,
    ) -> easy_gene_20210315_models.ListTemplatesResponse:
        """
        @summary 列出应用模板
        
        @param request: ListTemplatesRequest
        @return: ListTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_templates_with_options(request, runtime)

    async def list_templates_async(
        self,
        request: easy_gene_20210315_models.ListTemplatesRequest,
    ) -> easy_gene_20210315_models.ListTemplatesResponse:
        """
        @summary 列出应用模板
        
        @param request: ListTemplatesRequest
        @return: ListTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_templates_with_options_async(request, runtime)

    def list_user_active_runs_with_options(
        self,
        request: easy_gene_20210315_models.ListUserActiveRunsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.ListUserActiveRunsResponse:
        """
        @summary 最近任务列表
        
        @param request: ListUserActiveRunsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserActiveRunsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserActiveRuns',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListUserActiveRunsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_active_runs_with_options_async(
        self,
        request: easy_gene_20210315_models.ListUserActiveRunsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.ListUserActiveRunsResponse:
        """
        @summary 最近任务列表
        
        @param request: ListUserActiveRunsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserActiveRunsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserActiveRuns',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListUserActiveRunsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_active_runs(
        self,
        request: easy_gene_20210315_models.ListUserActiveRunsRequest,
    ) -> easy_gene_20210315_models.ListUserActiveRunsResponse:
        """
        @summary 最近任务列表
        
        @param request: ListUserActiveRunsRequest
        @return: ListUserActiveRunsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_user_active_runs_with_options(request, runtime)

    async def list_user_active_runs_async(
        self,
        request: easy_gene_20210315_models.ListUserActiveRunsRequest,
    ) -> easy_gene_20210315_models.ListUserActiveRunsResponse:
        """
        @summary 最近任务列表
        
        @param request: ListUserActiveRunsRequest
        @return: ListUserActiveRunsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_user_active_runs_with_options_async(request, runtime)

    def list_workspaces_with_options(
        self,
        request: easy_gene_20210315_models.ListWorkspacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.ListWorkspacesResponse:
        """
        @summary 列出工作空间
        
        @param request: ListWorkspacesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWorkspacesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWorkspaces',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListWorkspacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_workspaces_with_options_async(
        self,
        request: easy_gene_20210315_models.ListWorkspacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.ListWorkspacesResponse:
        """
        @summary 列出工作空间
        
        @param request: ListWorkspacesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWorkspacesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWorkspaces',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListWorkspacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_workspaces(
        self,
        request: easy_gene_20210315_models.ListWorkspacesRequest,
    ) -> easy_gene_20210315_models.ListWorkspacesResponse:
        """
        @summary 列出工作空间
        
        @param request: ListWorkspacesRequest
        @return: ListWorkspacesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_workspaces_with_options(request, runtime)

    async def list_workspaces_async(
        self,
        request: easy_gene_20210315_models.ListWorkspacesRequest,
    ) -> easy_gene_20210315_models.ListWorkspacesResponse:
        """
        @summary 列出工作空间
        
        @param request: ListWorkspacesRequest
        @return: ListWorkspacesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_workspaces_with_options_async(request, runtime)

    def resume_submission_with_options(
        self,
        request: easy_gene_20210315_models.ResumeSubmissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.ResumeSubmissionResponse:
        """
        @summary 恢复投递
        
        @param request: ResumeSubmissionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResumeSubmissionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.submission_id):
            query['SubmissionId'] = request.submission_id
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResumeSubmission',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ResumeSubmissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def resume_submission_with_options_async(
        self,
        request: easy_gene_20210315_models.ResumeSubmissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.ResumeSubmissionResponse:
        """
        @summary 恢复投递
        
        @param request: ResumeSubmissionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResumeSubmissionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.submission_id):
            query['SubmissionId'] = request.submission_id
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResumeSubmission',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ResumeSubmissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resume_submission(
        self,
        request: easy_gene_20210315_models.ResumeSubmissionRequest,
    ) -> easy_gene_20210315_models.ResumeSubmissionResponse:
        """
        @summary 恢复投递
        
        @param request: ResumeSubmissionRequest
        @return: ResumeSubmissionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.resume_submission_with_options(request, runtime)

    async def resume_submission_async(
        self,
        request: easy_gene_20210315_models.ResumeSubmissionRequest,
    ) -> easy_gene_20210315_models.ResumeSubmissionResponse:
        """
        @summary 恢复投递
        
        @param request: ResumeSubmissionRequest
        @return: ResumeSubmissionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.resume_submission_with_options_async(request, runtime)

    def tag_app_with_options(
        self,
        request: easy_gene_20210315_models.TagAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.TagAppResponse:
        """
        @summary 应用版本打标
        
        @param request: TagAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagAppResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_revision):
            query['AppRevision'] = request.app_revision
        if not UtilClient.is_unset(request.revision_tag):
            query['RevisionTag'] = request.revision_tag
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagApp',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.TagAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_app_with_options_async(
        self,
        request: easy_gene_20210315_models.TagAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.TagAppResponse:
        """
        @summary 应用版本打标
        
        @param request: TagAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagAppResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_revision):
            query['AppRevision'] = request.app_revision
        if not UtilClient.is_unset(request.revision_tag):
            query['RevisionTag'] = request.revision_tag
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagApp',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.TagAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_app(
        self,
        request: easy_gene_20210315_models.TagAppRequest,
    ) -> easy_gene_20210315_models.TagAppResponse:
        """
        @summary 应用版本打标
        
        @param request: TagAppRequest
        @return: TagAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.tag_app_with_options(request, runtime)

    async def tag_app_async(
        self,
        request: easy_gene_20210315_models.TagAppRequest,
    ) -> easy_gene_20210315_models.TagAppResponse:
        """
        @summary 应用版本打标
        
        @param request: TagAppRequest
        @return: TagAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.tag_app_with_options_async(request, runtime)

    def update_entity_with_options(
        self,
        tmp_req: easy_gene_20210315_models.UpdateEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.UpdateEntityResponse:
        """
        @deprecated OpenAPI UpdateEntity is deprecated, please use EasyGene::2021-03-15::UpdateEntityItems instead.
        
        @summary 修改数据表格
        
        @param tmp_req: UpdateEntityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateEntityResponse
        Deprecated
        """
        UtilClient.validate_model(tmp_req)
        request = easy_gene_20210315_models.UpdateEntityShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.entity_items):
            request.entity_items_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.entity_items, 'EntityItems', 'json')
        query = {}
        if not UtilClient.is_unset(request.entity_type):
            query['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        body = {}
        if not UtilClient.is_unset(request.entity_items_shrink):
            body['EntityItems'] = request.entity_items_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateEntity',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.UpdateEntityResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_entity_with_options_async(
        self,
        tmp_req: easy_gene_20210315_models.UpdateEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.UpdateEntityResponse:
        """
        @deprecated OpenAPI UpdateEntity is deprecated, please use EasyGene::2021-03-15::UpdateEntityItems instead.
        
        @summary 修改数据表格
        
        @param tmp_req: UpdateEntityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateEntityResponse
        Deprecated
        """
        UtilClient.validate_model(tmp_req)
        request = easy_gene_20210315_models.UpdateEntityShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.entity_items):
            request.entity_items_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.entity_items, 'EntityItems', 'json')
        query = {}
        if not UtilClient.is_unset(request.entity_type):
            query['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        body = {}
        if not UtilClient.is_unset(request.entity_items_shrink):
            body['EntityItems'] = request.entity_items_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateEntity',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.UpdateEntityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_entity(
        self,
        request: easy_gene_20210315_models.UpdateEntityRequest,
    ) -> easy_gene_20210315_models.UpdateEntityResponse:
        """
        @deprecated OpenAPI UpdateEntity is deprecated, please use EasyGene::2021-03-15::UpdateEntityItems instead.
        
        @summary 修改数据表格
        
        @param request: UpdateEntityRequest
        @return: UpdateEntityResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.update_entity_with_options(request, runtime)

    async def update_entity_async(
        self,
        request: easy_gene_20210315_models.UpdateEntityRequest,
    ) -> easy_gene_20210315_models.UpdateEntityResponse:
        """
        @deprecated OpenAPI UpdateEntity is deprecated, please use EasyGene::2021-03-15::UpdateEntityItems instead.
        
        @summary 修改数据表格
        
        @param request: UpdateEntityRequest
        @return: UpdateEntityResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_entity_with_options_async(request, runtime)

    def update_entity_items_with_options(
        self,
        tmp_req: easy_gene_20210315_models.UpdateEntityItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.UpdateEntityItemsResponse:
        """
        @summary 修改表格数据
        
        @param tmp_req: UpdateEntityItemsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateEntityItemsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = easy_gene_20210315_models.UpdateEntityItemsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.entity_items):
            request.entity_items_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.entity_items, 'EntityItems', 'json')
        query = {}
        if not UtilClient.is_unset(request.entity_type):
            query['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        body = {}
        if not UtilClient.is_unset(request.entity_items_shrink):
            body['EntityItems'] = request.entity_items_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateEntityItems',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.UpdateEntityItemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_entity_items_with_options_async(
        self,
        tmp_req: easy_gene_20210315_models.UpdateEntityItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.UpdateEntityItemsResponse:
        """
        @summary 修改表格数据
        
        @param tmp_req: UpdateEntityItemsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateEntityItemsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = easy_gene_20210315_models.UpdateEntityItemsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.entity_items):
            request.entity_items_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.entity_items, 'EntityItems', 'json')
        query = {}
        if not UtilClient.is_unset(request.entity_type):
            query['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        body = {}
        if not UtilClient.is_unset(request.entity_items_shrink):
            body['EntityItems'] = request.entity_items_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateEntityItems',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.UpdateEntityItemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_entity_items(
        self,
        request: easy_gene_20210315_models.UpdateEntityItemsRequest,
    ) -> easy_gene_20210315_models.UpdateEntityItemsResponse:
        """
        @summary 修改表格数据
        
        @param request: UpdateEntityItemsRequest
        @return: UpdateEntityItemsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_entity_items_with_options(request, runtime)

    async def update_entity_items_async(
        self,
        request: easy_gene_20210315_models.UpdateEntityItemsRequest,
    ) -> easy_gene_20210315_models.UpdateEntityItemsResponse:
        """
        @summary 修改表格数据
        
        @param request: UpdateEntityItemsRequest
        @return: UpdateEntityItemsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_entity_items_with_options_async(request, runtime)

    def update_template_with_options(
        self,
        tmp_req: easy_gene_20210315_models.UpdateTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.UpdateTemplateResponse:
        """
        @summary 修改应用模板
        
        @param tmp_req: UpdateTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateTemplateResponse
        """
        UtilClient.validate_model(tmp_req)
        request = easy_gene_20210315_models.UpdateTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.inputs_expression):
            request.inputs_expression_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.inputs_expression, 'InputsExpression', 'json')
        if not UtilClient.is_unset(tmp_req.outputs_expression):
            request.outputs_expression_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.outputs_expression, 'OutputsExpression', 'json')
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        if not UtilClient.is_unset(request.root_entity):
            query['RootEntity'] = request.root_entity
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        body = {}
        if not UtilClient.is_unset(request.inputs_expression_shrink):
            body['InputsExpression'] = request.inputs_expression_shrink
        if not UtilClient.is_unset(request.outputs_expression_shrink):
            body['OutputsExpression'] = request.outputs_expression_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTemplate',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.UpdateTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_template_with_options_async(
        self,
        tmp_req: easy_gene_20210315_models.UpdateTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.UpdateTemplateResponse:
        """
        @summary 修改应用模板
        
        @param tmp_req: UpdateTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateTemplateResponse
        """
        UtilClient.validate_model(tmp_req)
        request = easy_gene_20210315_models.UpdateTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.inputs_expression):
            request.inputs_expression_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.inputs_expression, 'InputsExpression', 'json')
        if not UtilClient.is_unset(tmp_req.outputs_expression):
            request.outputs_expression_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.outputs_expression, 'OutputsExpression', 'json')
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        if not UtilClient.is_unset(request.root_entity):
            query['RootEntity'] = request.root_entity
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        body = {}
        if not UtilClient.is_unset(request.inputs_expression_shrink):
            body['InputsExpression'] = request.inputs_expression_shrink
        if not UtilClient.is_unset(request.outputs_expression_shrink):
            body['OutputsExpression'] = request.outputs_expression_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTemplate',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.UpdateTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_template(
        self,
        request: easy_gene_20210315_models.UpdateTemplateRequest,
    ) -> easy_gene_20210315_models.UpdateTemplateResponse:
        """
        @summary 修改应用模板
        
        @param request: UpdateTemplateRequest
        @return: UpdateTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_template_with_options(request, runtime)

    async def update_template_async(
        self,
        request: easy_gene_20210315_models.UpdateTemplateRequest,
    ) -> easy_gene_20210315_models.UpdateTemplateResponse:
        """
        @summary 修改应用模板
        
        @param request: UpdateTemplateRequest
        @return: UpdateTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_template_with_options_async(request, runtime)

    def update_workspace_with_options(
        self,
        request: easy_gene_20210315_models.UpdateWorkspaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.UpdateWorkspaceResponse:
        """
        @summary 修改工作空间
        
        @param request: UpdateWorkspaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateWorkspaceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.job_lifecycle):
            query['JobLifecycle'] = request.job_lifecycle
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        if not UtilClient.is_unset(request.role):
            query['Role'] = request.role
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateWorkspace',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.UpdateWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_workspace_with_options_async(
        self,
        request: easy_gene_20210315_models.UpdateWorkspaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.UpdateWorkspaceResponse:
        """
        @summary 修改工作空间
        
        @param request: UpdateWorkspaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateWorkspaceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.job_lifecycle):
            query['JobLifecycle'] = request.job_lifecycle
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        if not UtilClient.is_unset(request.role):
            query['Role'] = request.role
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateWorkspace',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.UpdateWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_workspace(
        self,
        request: easy_gene_20210315_models.UpdateWorkspaceRequest,
    ) -> easy_gene_20210315_models.UpdateWorkspaceResponse:
        """
        @summary 修改工作空间
        
        @param request: UpdateWorkspaceRequest
        @return: UpdateWorkspaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_workspace_with_options(request, runtime)

    async def update_workspace_async(
        self,
        request: easy_gene_20210315_models.UpdateWorkspaceRequest,
    ) -> easy_gene_20210315_models.UpdateWorkspaceResponse:
        """
        @summary 修改工作空间
        
        @param request: UpdateWorkspaceRequest
        @return: UpdateWorkspaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_workspace_with_options_async(request, runtime)

    def upload_entity_with_options(
        self,
        request: easy_gene_20210315_models.UploadEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.UploadEntityResponse:
        """
        @summary 上传数据表格
        
        @param request: UploadEntityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UploadEntityResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.entity_csvfile):
            query['EntityCSVFile'] = request.entity_csvfile
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadEntity',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.UploadEntityResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_entity_with_options_async(
        self,
        request: easy_gene_20210315_models.UploadEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> easy_gene_20210315_models.UploadEntityResponse:
        """
        @summary 上传数据表格
        
        @param request: UploadEntityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UploadEntityResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.entity_csvfile):
            query['EntityCSVFile'] = request.entity_csvfile
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadEntity',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.UploadEntityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_entity(
        self,
        request: easy_gene_20210315_models.UploadEntityRequest,
    ) -> easy_gene_20210315_models.UploadEntityResponse:
        """
        @summary 上传数据表格
        
        @param request: UploadEntityRequest
        @return: UploadEntityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upload_entity_with_options(request, runtime)

    async def upload_entity_async(
        self,
        request: easy_gene_20210315_models.UploadEntityRequest,
    ) -> easy_gene_20210315_models.UploadEntityResponse:
        """
        @summary 上传数据表格
        
        @param request: UploadEntityRequest
        @return: UploadEntityResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.upload_entity_with_options_async(request, runtime)
