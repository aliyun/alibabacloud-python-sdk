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
        """
        @deprecated
        
        @param request: CloneFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CloneFlowResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.flow_id):
            body['FlowId'] = request.flow_id
        if not UtilClient.is_unset(request.version_id):
            body['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CloneFlow',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            composer_20181212_models.CloneFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def clone_flow_with_options_async(
        self,
        request: composer_20181212_models.CloneFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> composer_20181212_models.CloneFlowResponse:
        """
        @deprecated
        
        @param request: CloneFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CloneFlowResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.flow_id):
            body['FlowId'] = request.flow_id
        if not UtilClient.is_unset(request.version_id):
            body['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CloneFlow',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            composer_20181212_models.CloneFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def clone_flow(
        self,
        request: composer_20181212_models.CloneFlowRequest,
    ) -> composer_20181212_models.CloneFlowResponse:
        """
        @deprecated
        
        @param request: CloneFlowRequest
        @return: CloneFlowResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.clone_flow_with_options(request, runtime)

    async def clone_flow_async(
        self,
        request: composer_20181212_models.CloneFlowRequest,
    ) -> composer_20181212_models.CloneFlowResponse:
        """
        @deprecated
        
        @param request: CloneFlowRequest
        @return: CloneFlowResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.clone_flow_with_options_async(request, runtime)

    def create_flow_with_options(
        self,
        request: composer_20181212_models.CreateFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> composer_20181212_models.CreateFlowResponse:
        """
        After you create a workflow, the system automatically creates a version for the workflow. You can call the GetVersion operation to obtain the version information.
        
        @param request: CreateFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFlowResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.definition):
            body['Definition'] = request.definition
        if not UtilClient.is_unset(request.flow_description):
            body['FlowDescription'] = request.flow_description
        if not UtilClient.is_unset(request.flow_name):
            body['FlowName'] = request.flow_name
        if not UtilClient.is_unset(request.flow_source):
            body['FlowSource'] = request.flow_source
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFlow',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            composer_20181212_models.CreateFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_flow_with_options_async(
        self,
        request: composer_20181212_models.CreateFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> composer_20181212_models.CreateFlowResponse:
        """
        After you create a workflow, the system automatically creates a version for the workflow. You can call the GetVersion operation to obtain the version information.
        
        @param request: CreateFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFlowResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.definition):
            body['Definition'] = request.definition
        if not UtilClient.is_unset(request.flow_description):
            body['FlowDescription'] = request.flow_description
        if not UtilClient.is_unset(request.flow_name):
            body['FlowName'] = request.flow_name
        if not UtilClient.is_unset(request.flow_source):
            body['FlowSource'] = request.flow_source
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFlow',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            composer_20181212_models.CreateFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_flow(
        self,
        request: composer_20181212_models.CreateFlowRequest,
    ) -> composer_20181212_models.CreateFlowResponse:
        """
        After you create a workflow, the system automatically creates a version for the workflow. You can call the GetVersion operation to obtain the version information.
        
        @param request: CreateFlowRequest
        @return: CreateFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_flow_with_options(request, runtime)

    async def create_flow_async(
        self,
        request: composer_20181212_models.CreateFlowRequest,
    ) -> composer_20181212_models.CreateFlowResponse:
        """
        After you create a workflow, the system automatically creates a version for the workflow. You can call the GetVersion operation to obtain the version information.
        
        @param request: CreateFlowRequest
        @return: CreateFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_flow_with_options_async(request, runtime)

    def delete_flow_with_options(
        self,
        request: composer_20181212_models.DeleteFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> composer_20181212_models.DeleteFlowResponse:
        """
        If you delete a workflow, all the versions and execution records of the workflow are automatically deleted.
        
        @param request: DeleteFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFlowResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.flow_id):
            body['FlowId'] = request.flow_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteFlow',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            composer_20181212_models.DeleteFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_flow_with_options_async(
        self,
        request: composer_20181212_models.DeleteFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> composer_20181212_models.DeleteFlowResponse:
        """
        If you delete a workflow, all the versions and execution records of the workflow are automatically deleted.
        
        @param request: DeleteFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFlowResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.flow_id):
            body['FlowId'] = request.flow_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteFlow',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            composer_20181212_models.DeleteFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_flow(
        self,
        request: composer_20181212_models.DeleteFlowRequest,
    ) -> composer_20181212_models.DeleteFlowResponse:
        """
        If you delete a workflow, all the versions and execution records of the workflow are automatically deleted.
        
        @param request: DeleteFlowRequest
        @return: DeleteFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_flow_with_options(request, runtime)

    async def delete_flow_async(
        self,
        request: composer_20181212_models.DeleteFlowRequest,
    ) -> composer_20181212_models.DeleteFlowResponse:
        """
        If you delete a workflow, all the versions and execution records of the workflow are automatically deleted.
        
        @param request: DeleteFlowRequest
        @return: DeleteFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_flow_with_options_async(request, runtime)

    def disable_flow_with_options(
        self,
        request: composer_20181212_models.DisableFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> composer_20181212_models.DisableFlowResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.flow_id):
            body['FlowId'] = request.flow_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DisableFlow',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            composer_20181212_models.DisableFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_flow_with_options_async(
        self,
        request: composer_20181212_models.DisableFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> composer_20181212_models.DisableFlowResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.flow_id):
            body['FlowId'] = request.flow_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DisableFlow',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            composer_20181212_models.DisableFlowResponse(),
            await self.call_api_async(params, req, runtime)
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
        body = {}
        if not UtilClient.is_unset(request.flow_id):
            body['FlowId'] = request.flow_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnableFlow',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            composer_20181212_models.EnableFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_flow_with_options_async(
        self,
        request: composer_20181212_models.EnableFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> composer_20181212_models.EnableFlowResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.flow_id):
            body['FlowId'] = request.flow_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnableFlow',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            composer_20181212_models.EnableFlowResponse(),
            await self.call_api_async(params, req, runtime)
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
        body = {}
        if not UtilClient.is_unset(request.flow_id):
            body['FlowId'] = request.flow_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetFlow',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            composer_20181212_models.GetFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_flow_with_options_async(
        self,
        request: composer_20181212_models.GetFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> composer_20181212_models.GetFlowResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.flow_id):
            body['FlowId'] = request.flow_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetFlow',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            composer_20181212_models.GetFlowResponse(),
            await self.call_api_async(params, req, runtime)
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
        body = {}
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTemplate',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            composer_20181212_models.GetTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_template_with_options_async(
        self,
        request: composer_20181212_models.GetTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> composer_20181212_models.GetTemplateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTemplate',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            composer_20181212_models.GetTemplateResponse(),
            await self.call_api_async(params, req, runtime)
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
        body = {}
        if not UtilClient.is_unset(request.flow_id):
            body['FlowId'] = request.flow_id
        if not UtilClient.is_unset(request.version_id):
            body['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetVersion',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            composer_20181212_models.GetVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_version_with_options_async(
        self,
        request: composer_20181212_models.GetVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> composer_20181212_models.GetVersionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.flow_id):
            body['FlowId'] = request.flow_id
        if not UtilClient.is_unset(request.version_id):
            body['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetVersion',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            composer_20181212_models.GetVersionResponse(),
            await self.call_api_async(params, req, runtime)
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
        """
        You can call this operation to trigger a workflow to be executed more than 100 times per second. If the desired execution frequency does not exceed 100 times per second, we recommend that you call the InvokeFlow operation.
        *   However, you may need to call the GroupInvokeFlow operation multiple times. For example, assume that you want a workflow to be executed 1,000 times per second and the 1,000 times of execution are divided into ten groups. You need to call the operation ten times for the ten groups and specify a group key for each group.
        *   Each call corresponds to a group execution. Logic Composer automatically determines when a group execution starts. You must set the Data parameter to a JSON array of strings to specify the information required by the execution. Each string provides the information required by one time of execution. The string must use the format of the Data parameter in the InvokeFlow operation.
        
        @param request: GroupInvokeFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GroupInvokeFlowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.data):
            body['Data'] = request.data
        if not UtilClient.is_unset(request.flow_id):
            body['FlowId'] = request.flow_id
        if not UtilClient.is_unset(request.group_key):
            body['GroupKey'] = request.group_key
        if not UtilClient.is_unset(request.total_count):
            body['TotalCount'] = request.total_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GroupInvokeFlow',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            composer_20181212_models.GroupInvokeFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def group_invoke_flow_with_options_async(
        self,
        request: composer_20181212_models.GroupInvokeFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> composer_20181212_models.GroupInvokeFlowResponse:
        """
        You can call this operation to trigger a workflow to be executed more than 100 times per second. If the desired execution frequency does not exceed 100 times per second, we recommend that you call the InvokeFlow operation.
        *   However, you may need to call the GroupInvokeFlow operation multiple times. For example, assume that you want a workflow to be executed 1,000 times per second and the 1,000 times of execution are divided into ten groups. You need to call the operation ten times for the ten groups and specify a group key for each group.
        *   Each call corresponds to a group execution. Logic Composer automatically determines when a group execution starts. You must set the Data parameter to a JSON array of strings to specify the information required by the execution. Each string provides the information required by one time of execution. The string must use the format of the Data parameter in the InvokeFlow operation.
        
        @param request: GroupInvokeFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GroupInvokeFlowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.data):
            body['Data'] = request.data
        if not UtilClient.is_unset(request.flow_id):
            body['FlowId'] = request.flow_id
        if not UtilClient.is_unset(request.group_key):
            body['GroupKey'] = request.group_key
        if not UtilClient.is_unset(request.total_count):
            body['TotalCount'] = request.total_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GroupInvokeFlow',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            composer_20181212_models.GroupInvokeFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def group_invoke_flow(
        self,
        request: composer_20181212_models.GroupInvokeFlowRequest,
    ) -> composer_20181212_models.GroupInvokeFlowResponse:
        """
        You can call this operation to trigger a workflow to be executed more than 100 times per second. If the desired execution frequency does not exceed 100 times per second, we recommend that you call the InvokeFlow operation.
        *   However, you may need to call the GroupInvokeFlow operation multiple times. For example, assume that you want a workflow to be executed 1,000 times per second and the 1,000 times of execution are divided into ten groups. You need to call the operation ten times for the ten groups and specify a group key for each group.
        *   Each call corresponds to a group execution. Logic Composer automatically determines when a group execution starts. You must set the Data parameter to a JSON array of strings to specify the information required by the execution. Each string provides the information required by one time of execution. The string must use the format of the Data parameter in the InvokeFlow operation.
        
        @param request: GroupInvokeFlowRequest
        @return: GroupInvokeFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.group_invoke_flow_with_options(request, runtime)

    async def group_invoke_flow_async(
        self,
        request: composer_20181212_models.GroupInvokeFlowRequest,
    ) -> composer_20181212_models.GroupInvokeFlowResponse:
        """
        You can call this operation to trigger a workflow to be executed more than 100 times per second. If the desired execution frequency does not exceed 100 times per second, we recommend that you call the InvokeFlow operation.
        *   However, you may need to call the GroupInvokeFlow operation multiple times. For example, assume that you want a workflow to be executed 1,000 times per second and the 1,000 times of execution are divided into ten groups. You need to call the operation ten times for the ten groups and specify a group key for each group.
        *   Each call corresponds to a group execution. Logic Composer automatically determines when a group execution starts. You must set the Data parameter to a JSON array of strings to specify the information required by the execution. Each string provides the information required by one time of execution. The string must use the format of the Data parameter in the InvokeFlow operation.
        
        @param request: GroupInvokeFlowRequest
        @return: GroupInvokeFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.group_invoke_flow_with_options_async(request, runtime)

    def invoke_flow_with_options(
        self,
        request: composer_20181212_models.InvokeFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> composer_20181212_models.InvokeFlowResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.data):
            body['Data'] = request.data
        if not UtilClient.is_unset(request.flow_id):
            body['FlowId'] = request.flow_id
        if not UtilClient.is_unset(request.parameters):
            body['Parameters'] = request.parameters
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InvokeFlow',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            composer_20181212_models.InvokeFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def invoke_flow_with_options_async(
        self,
        request: composer_20181212_models.InvokeFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> composer_20181212_models.InvokeFlowResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.data):
            body['Data'] = request.data
        if not UtilClient.is_unset(request.flow_id):
            body['FlowId'] = request.flow_id
        if not UtilClient.is_unset(request.parameters):
            body['Parameters'] = request.parameters
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InvokeFlow',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            composer_20181212_models.InvokeFlowResponse(),
            await self.call_api_async(params, req, runtime)
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
        body = {}
        if not UtilClient.is_unset(request.filter):
            body['Filter'] = request.filter
        if not UtilClient.is_unset(request.flow_name):
            body['FlowName'] = request.flow_name
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListFlows',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            composer_20181212_models.ListFlowsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_flows_with_options_async(
        self,
        request: composer_20181212_models.ListFlowsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> composer_20181212_models.ListFlowsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.filter):
            body['Filter'] = request.filter
        if not UtilClient.is_unset(request.flow_name):
            body['FlowName'] = request.flow_name
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListFlows',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            composer_20181212_models.ListFlowsResponse(),
            await self.call_api_async(params, req, runtime)
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
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            composer_20181212_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: composer_20181212_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> composer_20181212_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            composer_20181212_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
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
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTemplates',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            composer_20181212_models.ListTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_templates_with_options_async(
        self,
        request: composer_20181212_models.ListTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> composer_20181212_models.ListTemplatesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTemplates',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            composer_20181212_models.ListTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
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
        body = {}
        if not UtilClient.is_unset(request.flow_id):
            body['FlowId'] = request.flow_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListVersions',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            composer_20181212_models.ListVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_versions_with_options_async(
        self,
        request: composer_20181212_models.ListVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> composer_20181212_models.ListVersionsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.flow_id):
            body['FlowId'] = request.flow_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListVersions',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            composer_20181212_models.ListVersionsResponse(),
            await self.call_api_async(params, req, runtime)
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
        body = {}
        if not UtilClient.is_unset(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            composer_20181212_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: composer_20181212_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> composer_20181212_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            composer_20181212_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
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
        body = {}
        if not UtilClient.is_unset(request.all):
            body['All'] = request.all
        if not UtilClient.is_unset(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            body['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            composer_20181212_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: composer_20181212_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> composer_20181212_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.all):
            body['All'] = request.all
        if not UtilClient.is_unset(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            body['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            composer_20181212_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
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
        body = {}
        if not UtilClient.is_unset(request.definition):
            body['Definition'] = request.definition
        if not UtilClient.is_unset(request.flow_description):
            body['FlowDescription'] = request.flow_description
        if not UtilClient.is_unset(request.flow_id):
            body['FlowId'] = request.flow_id
        if not UtilClient.is_unset(request.flow_name):
            body['FlowName'] = request.flow_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateFlow',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            composer_20181212_models.UpdateFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_flow_with_options_async(
        self,
        request: composer_20181212_models.UpdateFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> composer_20181212_models.UpdateFlowResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.definition):
            body['Definition'] = request.definition
        if not UtilClient.is_unset(request.flow_description):
            body['FlowDescription'] = request.flow_description
        if not UtilClient.is_unset(request.flow_id):
            body['FlowId'] = request.flow_id
        if not UtilClient.is_unset(request.flow_name):
            body['FlowName'] = request.flow_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateFlow',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            composer_20181212_models.UpdateFlowResponse(),
            await self.call_api_async(params, req, runtime)
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
