# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dataworks_public20240518 import models as dataworks_public_20240518_models
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
            'ap-northeast-1': 'dataworks.ap-northeast-1.aliyuncs.com',
            'ap-south-1': 'dataworks.ap-south-1.aliyuncs.com',
            'ap-southeast-1': 'dataworks.ap-southeast-1.aliyuncs.com',
            'ap-southeast-2': 'dataworks.ap-southeast-2.aliyuncs.com',
            'ap-southeast-3': 'dataworks.ap-southeast-3.aliyuncs.com',
            'ap-southeast-5': 'dataworks.ap-southeast-5.aliyuncs.com',
            'cn-beijing': 'dataworks.cn-beijing.aliyuncs.com',
            'cn-chengdu': 'dataworks.cn-chengdu.aliyuncs.com',
            'cn-hangzhou': 'dataworks.cn-hangzhou.aliyuncs.com',
            'cn-hongkong': 'dataworks.cn-hongkong.aliyuncs.com',
            'cn-huhehaote': 'dataworks.aliyuncs.com',
            'cn-qingdao': 'dataworks.aliyuncs.com',
            'cn-shanghai': 'dataworks.cn-shanghai.aliyuncs.com',
            'cn-shenzhen': 'dataworks.cn-shenzhen.aliyuncs.com',
            'cn-zhangjiakou': 'dataworks.aliyuncs.com',
            'eu-central-1': 'dataworks.eu-central-1.aliyuncs.com',
            'eu-west-1': 'dataworks.eu-west-1.aliyuncs.com',
            'me-east-1': 'dataworks.me-east-1.aliyuncs.com',
            'us-east-1': 'dataworks.us-east-1.aliyuncs.com',
            'us-west-1': 'dataworks.us-west-1.aliyuncs.com',
            'cn-hangzhou-finance': 'dataworks.aliyuncs.com',
            'cn-shenzhen-finance-1': 'dataworks.aliyuncs.com',
            'cn-shanghai-finance-1': 'dataworks.aliyuncs.com',
            'cn-north-2-gov-1': 'dataworks.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('dataworks-public', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def abolish_deployment_with_options(
        self,
        request: dataworks_public_20240518_models.AbolishDeploymentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.AbolishDeploymentResponse:
        """
        @summary 终止发布流程
        
        @param request: AbolishDeploymentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AbolishDeploymentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AbolishDeployment',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.AbolishDeploymentResponse(),
            self.call_api(params, req, runtime)
        )

    async def abolish_deployment_with_options_async(
        self,
        request: dataworks_public_20240518_models.AbolishDeploymentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.AbolishDeploymentResponse:
        """
        @summary 终止发布流程
        
        @param request: AbolishDeploymentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AbolishDeploymentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AbolishDeployment',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.AbolishDeploymentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def abolish_deployment(
        self,
        request: dataworks_public_20240518_models.AbolishDeploymentRequest,
    ) -> dataworks_public_20240518_models.AbolishDeploymentResponse:
        """
        @summary 终止发布流程
        
        @param request: AbolishDeploymentRequest
        @return: AbolishDeploymentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.abolish_deployment_with_options(request, runtime)

    async def abolish_deployment_async(
        self,
        request: dataworks_public_20240518_models.AbolishDeploymentRequest,
    ) -> dataworks_public_20240518_models.AbolishDeploymentResponse:
        """
        @summary 终止发布流程
        
        @param request: AbolishDeploymentRequest
        @return: AbolishDeploymentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.abolish_deployment_with_options_async(request, runtime)

    def create_deployment_with_options(
        self,
        tmp_req: dataworks_public_20240518_models.CreateDeploymentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.CreateDeploymentResponse:
        """
        @summary 创建发布流程
        
        @param tmp_req: CreateDeploymentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDeploymentResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20240518_models.CreateDeploymentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.object_ids):
            request.object_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.object_ids, 'ObjectIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.object_ids_shrink):
            body['ObjectIds'] = request.object_ids_shrink
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDeployment',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.CreateDeploymentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_deployment_with_options_async(
        self,
        tmp_req: dataworks_public_20240518_models.CreateDeploymentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.CreateDeploymentResponse:
        """
        @summary 创建发布流程
        
        @param tmp_req: CreateDeploymentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDeploymentResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataworks_public_20240518_models.CreateDeploymentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.object_ids):
            request.object_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.object_ids, 'ObjectIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.object_ids_shrink):
            body['ObjectIds'] = request.object_ids_shrink
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDeployment',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.CreateDeploymentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_deployment(
        self,
        request: dataworks_public_20240518_models.CreateDeploymentRequest,
    ) -> dataworks_public_20240518_models.CreateDeploymentResponse:
        """
        @summary 创建发布流程
        
        @param request: CreateDeploymentRequest
        @return: CreateDeploymentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_deployment_with_options(request, runtime)

    async def create_deployment_async(
        self,
        request: dataworks_public_20240518_models.CreateDeploymentRequest,
    ) -> dataworks_public_20240518_models.CreateDeploymentResponse:
        """
        @summary 创建发布流程
        
        @param request: CreateDeploymentRequest
        @return: CreateDeploymentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_deployment_with_options_async(request, runtime)

    def create_function_with_options(
        self,
        request: dataworks_public_20240518_models.CreateFunctionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.CreateFunctionResponse:
        """
        @summary 创建udf函数
        
        @param request: CreateFunctionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFunctionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.spec):
            body['Spec'] = request.spec
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFunction',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.CreateFunctionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_function_with_options_async(
        self,
        request: dataworks_public_20240518_models.CreateFunctionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.CreateFunctionResponse:
        """
        @summary 创建udf函数
        
        @param request: CreateFunctionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFunctionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.spec):
            body['Spec'] = request.spec
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFunction',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.CreateFunctionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_function(
        self,
        request: dataworks_public_20240518_models.CreateFunctionRequest,
    ) -> dataworks_public_20240518_models.CreateFunctionResponse:
        """
        @summary 创建udf函数
        
        @param request: CreateFunctionRequest
        @return: CreateFunctionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_function_with_options(request, runtime)

    async def create_function_async(
        self,
        request: dataworks_public_20240518_models.CreateFunctionRequest,
    ) -> dataworks_public_20240518_models.CreateFunctionResponse:
        """
        @summary 创建udf函数
        
        @param request: CreateFunctionRequest
        @return: CreateFunctionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_function_with_options_async(request, runtime)

    def create_node_with_options(
        self,
        request: dataworks_public_20240518_models.CreateNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.CreateNodeResponse:
        """
        @summary 创建节点
        
        @param request: CreateNodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateNodeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.container_id):
            body['ContainerId'] = request.container_id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.scene):
            body['Scene'] = request.scene
        if not UtilClient.is_unset(request.spec):
            body['Spec'] = request.spec
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateNode',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.CreateNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_node_with_options_async(
        self,
        request: dataworks_public_20240518_models.CreateNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.CreateNodeResponse:
        """
        @summary 创建节点
        
        @param request: CreateNodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateNodeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.container_id):
            body['ContainerId'] = request.container_id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.scene):
            body['Scene'] = request.scene
        if not UtilClient.is_unset(request.spec):
            body['Spec'] = request.spec
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateNode',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.CreateNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_node(
        self,
        request: dataworks_public_20240518_models.CreateNodeRequest,
    ) -> dataworks_public_20240518_models.CreateNodeResponse:
        """
        @summary 创建节点
        
        @param request: CreateNodeRequest
        @return: CreateNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_node_with_options(request, runtime)

    async def create_node_async(
        self,
        request: dataworks_public_20240518_models.CreateNodeRequest,
    ) -> dataworks_public_20240518_models.CreateNodeResponse:
        """
        @summary 创建节点
        
        @param request: CreateNodeRequest
        @return: CreateNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_node_with_options_async(request, runtime)

    def create_resource_with_options(
        self,
        request: dataworks_public_20240518_models.CreateResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.CreateResourceResponse:
        """
        @summary 创建资源文件
        
        @param request: CreateResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateResourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.spec):
            body['Spec'] = request.spec
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateResource',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.CreateResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_resource_with_options_async(
        self,
        request: dataworks_public_20240518_models.CreateResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.CreateResourceResponse:
        """
        @summary 创建资源文件
        
        @param request: CreateResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateResourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.spec):
            body['Spec'] = request.spec
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateResource',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.CreateResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_resource(
        self,
        request: dataworks_public_20240518_models.CreateResourceRequest,
    ) -> dataworks_public_20240518_models.CreateResourceResponse:
        """
        @summary 创建资源文件
        
        @param request: CreateResourceRequest
        @return: CreateResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_resource_with_options(request, runtime)

    async def create_resource_async(
        self,
        request: dataworks_public_20240518_models.CreateResourceRequest,
    ) -> dataworks_public_20240518_models.CreateResourceResponse:
        """
        @summary 创建资源文件
        
        @param request: CreateResourceRequest
        @return: CreateResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_resource_with_options_async(request, runtime)

    def create_workflow_definition_with_options(
        self,
        request: dataworks_public_20240518_models.CreateWorkflowDefinitionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.CreateWorkflowDefinitionResponse:
        """
        @summary 创建工作流
        
        @param request: CreateWorkflowDefinitionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateWorkflowDefinitionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.spec):
            body['Spec'] = request.spec
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWorkflowDefinition',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.CreateWorkflowDefinitionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_workflow_definition_with_options_async(
        self,
        request: dataworks_public_20240518_models.CreateWorkflowDefinitionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.CreateWorkflowDefinitionResponse:
        """
        @summary 创建工作流
        
        @param request: CreateWorkflowDefinitionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateWorkflowDefinitionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.spec):
            body['Spec'] = request.spec
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWorkflowDefinition',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.CreateWorkflowDefinitionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_workflow_definition(
        self,
        request: dataworks_public_20240518_models.CreateWorkflowDefinitionRequest,
    ) -> dataworks_public_20240518_models.CreateWorkflowDefinitionResponse:
        """
        @summary 创建工作流
        
        @param request: CreateWorkflowDefinitionRequest
        @return: CreateWorkflowDefinitionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_workflow_definition_with_options(request, runtime)

    async def create_workflow_definition_async(
        self,
        request: dataworks_public_20240518_models.CreateWorkflowDefinitionRequest,
    ) -> dataworks_public_20240518_models.CreateWorkflowDefinitionResponse:
        """
        @summary 创建工作流
        
        @param request: CreateWorkflowDefinitionRequest
        @return: CreateWorkflowDefinitionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_workflow_definition_with_options_async(request, runtime)

    def delete_function_with_options(
        self,
        request: dataworks_public_20240518_models.DeleteFunctionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.DeleteFunctionResponse:
        """
        @summary 删除udf函数
        
        @param request: DeleteFunctionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFunctionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteFunction',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.DeleteFunctionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_function_with_options_async(
        self,
        request: dataworks_public_20240518_models.DeleteFunctionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.DeleteFunctionResponse:
        """
        @summary 删除udf函数
        
        @param request: DeleteFunctionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFunctionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteFunction',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.DeleteFunctionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_function(
        self,
        request: dataworks_public_20240518_models.DeleteFunctionRequest,
    ) -> dataworks_public_20240518_models.DeleteFunctionResponse:
        """
        @summary 删除udf函数
        
        @param request: DeleteFunctionRequest
        @return: DeleteFunctionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_function_with_options(request, runtime)

    async def delete_function_async(
        self,
        request: dataworks_public_20240518_models.DeleteFunctionRequest,
    ) -> dataworks_public_20240518_models.DeleteFunctionResponse:
        """
        @summary 删除udf函数
        
        @param request: DeleteFunctionRequest
        @return: DeleteFunctionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_function_with_options_async(request, runtime)

    def delete_node_with_options(
        self,
        request: dataworks_public_20240518_models.DeleteNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.DeleteNodeResponse:
        """
        @summary 删除节点
        
        @param request: DeleteNodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteNodeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteNode',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.DeleteNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_node_with_options_async(
        self,
        request: dataworks_public_20240518_models.DeleteNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.DeleteNodeResponse:
        """
        @summary 删除节点
        
        @param request: DeleteNodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteNodeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteNode',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.DeleteNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_node(
        self,
        request: dataworks_public_20240518_models.DeleteNodeRequest,
    ) -> dataworks_public_20240518_models.DeleteNodeResponse:
        """
        @summary 删除节点
        
        @param request: DeleteNodeRequest
        @return: DeleteNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_node_with_options(request, runtime)

    async def delete_node_async(
        self,
        request: dataworks_public_20240518_models.DeleteNodeRequest,
    ) -> dataworks_public_20240518_models.DeleteNodeResponse:
        """
        @summary 删除节点
        
        @param request: DeleteNodeRequest
        @return: DeleteNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_node_with_options_async(request, runtime)

    def delete_resource_with_options(
        self,
        request: dataworks_public_20240518_models.DeleteResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.DeleteResourceResponse:
        """
        @summary 删除资源文件
        
        @param request: DeleteResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteResourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteResource',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.DeleteResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_resource_with_options_async(
        self,
        request: dataworks_public_20240518_models.DeleteResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.DeleteResourceResponse:
        """
        @summary 删除资源文件
        
        @param request: DeleteResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteResourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteResource',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.DeleteResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_resource(
        self,
        request: dataworks_public_20240518_models.DeleteResourceRequest,
    ) -> dataworks_public_20240518_models.DeleteResourceResponse:
        """
        @summary 删除资源文件
        
        @param request: DeleteResourceRequest
        @return: DeleteResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_resource_with_options(request, runtime)

    async def delete_resource_async(
        self,
        request: dataworks_public_20240518_models.DeleteResourceRequest,
    ) -> dataworks_public_20240518_models.DeleteResourceResponse:
        """
        @summary 删除资源文件
        
        @param request: DeleteResourceRequest
        @return: DeleteResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_resource_with_options_async(request, runtime)

    def delete_workflow_definition_with_options(
        self,
        request: dataworks_public_20240518_models.DeleteWorkflowDefinitionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.DeleteWorkflowDefinitionResponse:
        """
        @summary 删除工作流
        
        @param request: DeleteWorkflowDefinitionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteWorkflowDefinitionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteWorkflowDefinition',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.DeleteWorkflowDefinitionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_workflow_definition_with_options_async(
        self,
        request: dataworks_public_20240518_models.DeleteWorkflowDefinitionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.DeleteWorkflowDefinitionResponse:
        """
        @summary 删除工作流
        
        @param request: DeleteWorkflowDefinitionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteWorkflowDefinitionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteWorkflowDefinition',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.DeleteWorkflowDefinitionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_workflow_definition(
        self,
        request: dataworks_public_20240518_models.DeleteWorkflowDefinitionRequest,
    ) -> dataworks_public_20240518_models.DeleteWorkflowDefinitionResponse:
        """
        @summary 删除工作流
        
        @param request: DeleteWorkflowDefinitionRequest
        @return: DeleteWorkflowDefinitionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_workflow_definition_with_options(request, runtime)

    async def delete_workflow_definition_async(
        self,
        request: dataworks_public_20240518_models.DeleteWorkflowDefinitionRequest,
    ) -> dataworks_public_20240518_models.DeleteWorkflowDefinitionResponse:
        """
        @summary 删除工作流
        
        @param request: DeleteWorkflowDefinitionRequest
        @return: DeleteWorkflowDefinitionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_workflow_definition_with_options_async(request, runtime)

    def exec_deployment_stage_with_options(
        self,
        request: dataworks_public_20240518_models.ExecDeploymentStageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ExecDeploymentStageResponse:
        """
        @summary 执行Deployment一个阶段
        
        @param request: ExecDeploymentStageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecDeploymentStageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        body = {}
        if not UtilClient.is_unset(request.code):
            body['Code'] = request.code
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecDeploymentStage',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ExecDeploymentStageResponse(),
            self.call_api(params, req, runtime)
        )

    async def exec_deployment_stage_with_options_async(
        self,
        request: dataworks_public_20240518_models.ExecDeploymentStageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ExecDeploymentStageResponse:
        """
        @summary 执行Deployment一个阶段
        
        @param request: ExecDeploymentStageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecDeploymentStageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        body = {}
        if not UtilClient.is_unset(request.code):
            body['Code'] = request.code
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecDeploymentStage',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ExecDeploymentStageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def exec_deployment_stage(
        self,
        request: dataworks_public_20240518_models.ExecDeploymentStageRequest,
    ) -> dataworks_public_20240518_models.ExecDeploymentStageResponse:
        """
        @summary 执行Deployment一个阶段
        
        @param request: ExecDeploymentStageRequest
        @return: ExecDeploymentStageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.exec_deployment_stage_with_options(request, runtime)

    async def exec_deployment_stage_async(
        self,
        request: dataworks_public_20240518_models.ExecDeploymentStageRequest,
    ) -> dataworks_public_20240518_models.ExecDeploymentStageResponse:
        """
        @summary 执行Deployment一个阶段
        
        @param request: ExecDeploymentStageRequest
        @return: ExecDeploymentStageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.exec_deployment_stage_with_options_async(request, runtime)

    def get_deployment_with_options(
        self,
        request: dataworks_public_20240518_models.GetDeploymentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.GetDeploymentResponse:
        """
        @summary 获取发布流程详情
        
        @param request: GetDeploymentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDeploymentResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDeployment',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.GetDeploymentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_deployment_with_options_async(
        self,
        request: dataworks_public_20240518_models.GetDeploymentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.GetDeploymentResponse:
        """
        @summary 获取发布流程详情
        
        @param request: GetDeploymentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDeploymentResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDeployment',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.GetDeploymentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_deployment(
        self,
        request: dataworks_public_20240518_models.GetDeploymentRequest,
    ) -> dataworks_public_20240518_models.GetDeploymentResponse:
        """
        @summary 获取发布流程详情
        
        @param request: GetDeploymentRequest
        @return: GetDeploymentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_deployment_with_options(request, runtime)

    async def get_deployment_async(
        self,
        request: dataworks_public_20240518_models.GetDeploymentRequest,
    ) -> dataworks_public_20240518_models.GetDeploymentResponse:
        """
        @summary 获取发布流程详情
        
        @param request: GetDeploymentRequest
        @return: GetDeploymentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_deployment_with_options_async(request, runtime)

    def get_function_with_options(
        self,
        request: dataworks_public_20240518_models.GetFunctionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.GetFunctionResponse:
        """
        @summary 获取函数信息
        
        @param request: GetFunctionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFunctionResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFunction',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.GetFunctionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_function_with_options_async(
        self,
        request: dataworks_public_20240518_models.GetFunctionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.GetFunctionResponse:
        """
        @summary 获取函数信息
        
        @param request: GetFunctionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFunctionResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFunction',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.GetFunctionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_function(
        self,
        request: dataworks_public_20240518_models.GetFunctionRequest,
    ) -> dataworks_public_20240518_models.GetFunctionResponse:
        """
        @summary 获取函数信息
        
        @param request: GetFunctionRequest
        @return: GetFunctionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_function_with_options(request, runtime)

    async def get_function_async(
        self,
        request: dataworks_public_20240518_models.GetFunctionRequest,
    ) -> dataworks_public_20240518_models.GetFunctionResponse:
        """
        @summary 获取函数信息
        
        @param request: GetFunctionRequest
        @return: GetFunctionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_function_with_options_async(request, runtime)

    def get_node_with_options(
        self,
        request: dataworks_public_20240518_models.GetNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.GetNodeResponse:
        """
        @param request: GetNodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetNodeResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetNode',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.GetNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_node_with_options_async(
        self,
        request: dataworks_public_20240518_models.GetNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.GetNodeResponse:
        """
        @param request: GetNodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetNodeResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetNode',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.GetNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_node(
        self,
        request: dataworks_public_20240518_models.GetNodeRequest,
    ) -> dataworks_public_20240518_models.GetNodeResponse:
        """
        @param request: GetNodeRequest
        @return: GetNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_node_with_options(request, runtime)

    async def get_node_async(
        self,
        request: dataworks_public_20240518_models.GetNodeRequest,
    ) -> dataworks_public_20240518_models.GetNodeResponse:
        """
        @param request: GetNodeRequest
        @return: GetNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_node_with_options_async(request, runtime)

    def get_resource_with_options(
        self,
        request: dataworks_public_20240518_models.GetResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.GetResourceResponse:
        """
        @summary 获取资源文件
        
        @param request: GetResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetResourceResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResource',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.GetResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_with_options_async(
        self,
        request: dataworks_public_20240518_models.GetResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.GetResourceResponse:
        """
        @summary 获取资源文件
        
        @param request: GetResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetResourceResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResource',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.GetResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource(
        self,
        request: dataworks_public_20240518_models.GetResourceRequest,
    ) -> dataworks_public_20240518_models.GetResourceResponse:
        """
        @summary 获取资源文件
        
        @param request: GetResourceRequest
        @return: GetResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_resource_with_options(request, runtime)

    async def get_resource_async(
        self,
        request: dataworks_public_20240518_models.GetResourceRequest,
    ) -> dataworks_public_20240518_models.GetResourceResponse:
        """
        @summary 获取资源文件
        
        @param request: GetResourceRequest
        @return: GetResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_resource_with_options_async(request, runtime)

    def get_workflow_definition_with_options(
        self,
        request: dataworks_public_20240518_models.GetWorkflowDefinitionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.GetWorkflowDefinitionResponse:
        """
        @summary 获取工作流详情
        
        @param request: GetWorkflowDefinitionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWorkflowDefinitionResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWorkflowDefinition',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.GetWorkflowDefinitionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_workflow_definition_with_options_async(
        self,
        request: dataworks_public_20240518_models.GetWorkflowDefinitionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.GetWorkflowDefinitionResponse:
        """
        @summary 获取工作流详情
        
        @param request: GetWorkflowDefinitionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWorkflowDefinitionResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWorkflowDefinition',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.GetWorkflowDefinitionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_workflow_definition(
        self,
        request: dataworks_public_20240518_models.GetWorkflowDefinitionRequest,
    ) -> dataworks_public_20240518_models.GetWorkflowDefinitionResponse:
        """
        @summary 获取工作流详情
        
        @param request: GetWorkflowDefinitionRequest
        @return: GetWorkflowDefinitionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_workflow_definition_with_options(request, runtime)

    async def get_workflow_definition_async(
        self,
        request: dataworks_public_20240518_models.GetWorkflowDefinitionRequest,
    ) -> dataworks_public_20240518_models.GetWorkflowDefinitionResponse:
        """
        @summary 获取工作流详情
        
        @param request: GetWorkflowDefinitionRequest
        @return: GetWorkflowDefinitionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_workflow_definition_with_options_async(request, runtime)

    def list_deployments_with_options(
        self,
        request: dataworks_public_20240518_models.ListDeploymentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ListDeploymentsResponse:
        """
        @summary 分页获取发布流程
        
        @param request: ListDeploymentsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDeploymentsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDeployments',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ListDeploymentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_deployments_with_options_async(
        self,
        request: dataworks_public_20240518_models.ListDeploymentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ListDeploymentsResponse:
        """
        @summary 分页获取发布流程
        
        @param request: ListDeploymentsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDeploymentsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDeployments',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ListDeploymentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_deployments(
        self,
        request: dataworks_public_20240518_models.ListDeploymentsRequest,
    ) -> dataworks_public_20240518_models.ListDeploymentsResponse:
        """
        @summary 分页获取发布流程
        
        @param request: ListDeploymentsRequest
        @return: ListDeploymentsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_deployments_with_options(request, runtime)

    async def list_deployments_async(
        self,
        request: dataworks_public_20240518_models.ListDeploymentsRequest,
    ) -> dataworks_public_20240518_models.ListDeploymentsResponse:
        """
        @summary 分页获取发布流程
        
        @param request: ListDeploymentsRequest
        @return: ListDeploymentsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_deployments_with_options_async(request, runtime)

    def list_functions_with_options(
        self,
        request: dataworks_public_20240518_models.ListFunctionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ListFunctionsResponse:
        """
        @summary 获取udf函数列表
        
        @param request: ListFunctionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFunctionsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFunctions',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ListFunctionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_functions_with_options_async(
        self,
        request: dataworks_public_20240518_models.ListFunctionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ListFunctionsResponse:
        """
        @summary 获取udf函数列表
        
        @param request: ListFunctionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFunctionsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFunctions',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ListFunctionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_functions(
        self,
        request: dataworks_public_20240518_models.ListFunctionsRequest,
    ) -> dataworks_public_20240518_models.ListFunctionsResponse:
        """
        @summary 获取udf函数列表
        
        @param request: ListFunctionsRequest
        @return: ListFunctionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_functions_with_options(request, runtime)

    async def list_functions_async(
        self,
        request: dataworks_public_20240518_models.ListFunctionsRequest,
    ) -> dataworks_public_20240518_models.ListFunctionsResponse:
        """
        @summary 获取udf函数列表
        
        @param request: ListFunctionsRequest
        @return: ListFunctionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_functions_with_options_async(request, runtime)

    def list_node_dependencies_with_options(
        self,
        request: dataworks_public_20240518_models.ListNodeDependenciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ListNodeDependenciesResponse:
        """
        @summary 获取节点依赖列表
        
        @param request: ListNodeDependenciesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListNodeDependenciesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNodeDependencies',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ListNodeDependenciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_node_dependencies_with_options_async(
        self,
        request: dataworks_public_20240518_models.ListNodeDependenciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ListNodeDependenciesResponse:
        """
        @summary 获取节点依赖列表
        
        @param request: ListNodeDependenciesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListNodeDependenciesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNodeDependencies',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ListNodeDependenciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_node_dependencies(
        self,
        request: dataworks_public_20240518_models.ListNodeDependenciesRequest,
    ) -> dataworks_public_20240518_models.ListNodeDependenciesResponse:
        """
        @summary 获取节点依赖列表
        
        @param request: ListNodeDependenciesRequest
        @return: ListNodeDependenciesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_node_dependencies_with_options(request, runtime)

    async def list_node_dependencies_async(
        self,
        request: dataworks_public_20240518_models.ListNodeDependenciesRequest,
    ) -> dataworks_public_20240518_models.ListNodeDependenciesResponse:
        """
        @summary 获取节点依赖列表
        
        @param request: ListNodeDependenciesRequest
        @return: ListNodeDependenciesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_node_dependencies_with_options_async(request, runtime)

    def list_nodes_with_options(
        self,
        request: dataworks_public_20240518_models.ListNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ListNodesResponse:
        """
        @summary 获取节点列表
        
        @param request: ListNodesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListNodesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNodes',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ListNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_nodes_with_options_async(
        self,
        request: dataworks_public_20240518_models.ListNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ListNodesResponse:
        """
        @summary 获取节点列表
        
        @param request: ListNodesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListNodesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNodes',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ListNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_nodes(
        self,
        request: dataworks_public_20240518_models.ListNodesRequest,
    ) -> dataworks_public_20240518_models.ListNodesResponse:
        """
        @summary 获取节点列表
        
        @param request: ListNodesRequest
        @return: ListNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_nodes_with_options(request, runtime)

    async def list_nodes_async(
        self,
        request: dataworks_public_20240518_models.ListNodesRequest,
    ) -> dataworks_public_20240518_models.ListNodesResponse:
        """
        @summary 获取节点列表
        
        @param request: ListNodesRequest
        @return: ListNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_nodes_with_options_async(request, runtime)

    def list_resources_with_options(
        self,
        request: dataworks_public_20240518_models.ListResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ListResourcesResponse:
        """
        @summary 分页获取资源文件
        
        @param request: ListResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResourcesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResources',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ListResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resources_with_options_async(
        self,
        request: dataworks_public_20240518_models.ListResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ListResourcesResponse:
        """
        @summary 分页获取资源文件
        
        @param request: ListResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResourcesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResources',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ListResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resources(
        self,
        request: dataworks_public_20240518_models.ListResourcesRequest,
    ) -> dataworks_public_20240518_models.ListResourcesResponse:
        """
        @summary 分页获取资源文件
        
        @param request: ListResourcesRequest
        @return: ListResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_resources_with_options(request, runtime)

    async def list_resources_async(
        self,
        request: dataworks_public_20240518_models.ListResourcesRequest,
    ) -> dataworks_public_20240518_models.ListResourcesResponse:
        """
        @summary 分页获取资源文件
        
        @param request: ListResourcesRequest
        @return: ListResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_resources_with_options_async(request, runtime)

    def list_workflow_definitions_with_options(
        self,
        request: dataworks_public_20240518_models.ListWorkflowDefinitionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ListWorkflowDefinitionsResponse:
        """
        @summary 获取workflowDefinition的列表
        
        @param request: ListWorkflowDefinitionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWorkflowDefinitionsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWorkflowDefinitions',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ListWorkflowDefinitionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_workflow_definitions_with_options_async(
        self,
        request: dataworks_public_20240518_models.ListWorkflowDefinitionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.ListWorkflowDefinitionsResponse:
        """
        @summary 获取workflowDefinition的列表
        
        @param request: ListWorkflowDefinitionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWorkflowDefinitionsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWorkflowDefinitions',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.ListWorkflowDefinitionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_workflow_definitions(
        self,
        request: dataworks_public_20240518_models.ListWorkflowDefinitionsRequest,
    ) -> dataworks_public_20240518_models.ListWorkflowDefinitionsResponse:
        """
        @summary 获取workflowDefinition的列表
        
        @param request: ListWorkflowDefinitionsRequest
        @return: ListWorkflowDefinitionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_workflow_definitions_with_options(request, runtime)

    async def list_workflow_definitions_async(
        self,
        request: dataworks_public_20240518_models.ListWorkflowDefinitionsRequest,
    ) -> dataworks_public_20240518_models.ListWorkflowDefinitionsResponse:
        """
        @summary 获取workflowDefinition的列表
        
        @param request: ListWorkflowDefinitionsRequest
        @return: ListWorkflowDefinitionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_workflow_definitions_with_options_async(request, runtime)

    def move_function_with_options(
        self,
        request: dataworks_public_20240518_models.MoveFunctionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.MoveFunctionResponse:
        """
        @summary 移动funciton的路径
        
        @param request: MoveFunctionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MoveFunctionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.path):
            body['Path'] = request.path
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MoveFunction',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.MoveFunctionResponse(),
            self.call_api(params, req, runtime)
        )

    async def move_function_with_options_async(
        self,
        request: dataworks_public_20240518_models.MoveFunctionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.MoveFunctionResponse:
        """
        @summary 移动funciton的路径
        
        @param request: MoveFunctionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MoveFunctionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.path):
            body['Path'] = request.path
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MoveFunction',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.MoveFunctionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def move_function(
        self,
        request: dataworks_public_20240518_models.MoveFunctionRequest,
    ) -> dataworks_public_20240518_models.MoveFunctionResponse:
        """
        @summary 移动funciton的路径
        
        @param request: MoveFunctionRequest
        @return: MoveFunctionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.move_function_with_options(request, runtime)

    async def move_function_async(
        self,
        request: dataworks_public_20240518_models.MoveFunctionRequest,
    ) -> dataworks_public_20240518_models.MoveFunctionResponse:
        """
        @summary 移动funciton的路径
        
        @param request: MoveFunctionRequest
        @return: MoveFunctionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.move_function_with_options_async(request, runtime)

    def move_node_with_options(
        self,
        request: dataworks_public_20240518_models.MoveNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.MoveNodeResponse:
        """
        @summary 移动节点路径
        
        @param request: MoveNodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MoveNodeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.path):
            body['Path'] = request.path
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MoveNode',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.MoveNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def move_node_with_options_async(
        self,
        request: dataworks_public_20240518_models.MoveNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.MoveNodeResponse:
        """
        @summary 移动节点路径
        
        @param request: MoveNodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MoveNodeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.path):
            body['Path'] = request.path
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MoveNode',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.MoveNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def move_node(
        self,
        request: dataworks_public_20240518_models.MoveNodeRequest,
    ) -> dataworks_public_20240518_models.MoveNodeResponse:
        """
        @summary 移动节点路径
        
        @param request: MoveNodeRequest
        @return: MoveNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.move_node_with_options(request, runtime)

    async def move_node_async(
        self,
        request: dataworks_public_20240518_models.MoveNodeRequest,
    ) -> dataworks_public_20240518_models.MoveNodeResponse:
        """
        @summary 移动节点路径
        
        @param request: MoveNodeRequest
        @return: MoveNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.move_node_with_options_async(request, runtime)

    def move_resource_with_options(
        self,
        request: dataworks_public_20240518_models.MoveResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.MoveResourceResponse:
        """
        @summary 移动资源文件路径
        
        @param request: MoveResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MoveResourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.path):
            body['Path'] = request.path
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MoveResource',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.MoveResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def move_resource_with_options_async(
        self,
        request: dataworks_public_20240518_models.MoveResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.MoveResourceResponse:
        """
        @summary 移动资源文件路径
        
        @param request: MoveResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MoveResourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.path):
            body['Path'] = request.path
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MoveResource',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.MoveResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def move_resource(
        self,
        request: dataworks_public_20240518_models.MoveResourceRequest,
    ) -> dataworks_public_20240518_models.MoveResourceResponse:
        """
        @summary 移动资源文件路径
        
        @param request: MoveResourceRequest
        @return: MoveResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.move_resource_with_options(request, runtime)

    async def move_resource_async(
        self,
        request: dataworks_public_20240518_models.MoveResourceRequest,
    ) -> dataworks_public_20240518_models.MoveResourceResponse:
        """
        @summary 移动资源文件路径
        
        @param request: MoveResourceRequest
        @return: MoveResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.move_resource_with_options_async(request, runtime)

    def move_workflow_definition_with_options(
        self,
        request: dataworks_public_20240518_models.MoveWorkflowDefinitionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.MoveWorkflowDefinitionResponse:
        """
        @summary 移动工作流的路径
        
        @param request: MoveWorkflowDefinitionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MoveWorkflowDefinitionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.path):
            body['Path'] = request.path
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MoveWorkflowDefinition',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.MoveWorkflowDefinitionResponse(),
            self.call_api(params, req, runtime)
        )

    async def move_workflow_definition_with_options_async(
        self,
        request: dataworks_public_20240518_models.MoveWorkflowDefinitionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.MoveWorkflowDefinitionResponse:
        """
        @summary 移动工作流的路径
        
        @param request: MoveWorkflowDefinitionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MoveWorkflowDefinitionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.path):
            body['Path'] = request.path
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MoveWorkflowDefinition',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.MoveWorkflowDefinitionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def move_workflow_definition(
        self,
        request: dataworks_public_20240518_models.MoveWorkflowDefinitionRequest,
    ) -> dataworks_public_20240518_models.MoveWorkflowDefinitionResponse:
        """
        @summary 移动工作流的路径
        
        @param request: MoveWorkflowDefinitionRequest
        @return: MoveWorkflowDefinitionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.move_workflow_definition_with_options(request, runtime)

    async def move_workflow_definition_async(
        self,
        request: dataworks_public_20240518_models.MoveWorkflowDefinitionRequest,
    ) -> dataworks_public_20240518_models.MoveWorkflowDefinitionResponse:
        """
        @summary 移动工作流的路径
        
        @param request: MoveWorkflowDefinitionRequest
        @return: MoveWorkflowDefinitionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.move_workflow_definition_with_options_async(request, runtime)

    def rename_function_with_options(
        self,
        request: dataworks_public_20240518_models.RenameFunctionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.RenameFunctionResponse:
        """
        @summary 对function重命名
        
        @param request: RenameFunctionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RenameFunctionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RenameFunction',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.RenameFunctionResponse(),
            self.call_api(params, req, runtime)
        )

    async def rename_function_with_options_async(
        self,
        request: dataworks_public_20240518_models.RenameFunctionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.RenameFunctionResponse:
        """
        @summary 对function重命名
        
        @param request: RenameFunctionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RenameFunctionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RenameFunction',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.RenameFunctionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rename_function(
        self,
        request: dataworks_public_20240518_models.RenameFunctionRequest,
    ) -> dataworks_public_20240518_models.RenameFunctionResponse:
        """
        @summary 对function重命名
        
        @param request: RenameFunctionRequest
        @return: RenameFunctionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.rename_function_with_options(request, runtime)

    async def rename_function_async(
        self,
        request: dataworks_public_20240518_models.RenameFunctionRequest,
    ) -> dataworks_public_20240518_models.RenameFunctionResponse:
        """
        @summary 对function重命名
        
        @param request: RenameFunctionRequest
        @return: RenameFunctionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.rename_function_with_options_async(request, runtime)

    def rename_node_with_options(
        self,
        request: dataworks_public_20240518_models.RenameNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.RenameNodeResponse:
        """
        @summary 重命名节点
        
        @param request: RenameNodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RenameNodeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RenameNode',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.RenameNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def rename_node_with_options_async(
        self,
        request: dataworks_public_20240518_models.RenameNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.RenameNodeResponse:
        """
        @summary 重命名节点
        
        @param request: RenameNodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RenameNodeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RenameNode',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.RenameNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rename_node(
        self,
        request: dataworks_public_20240518_models.RenameNodeRequest,
    ) -> dataworks_public_20240518_models.RenameNodeResponse:
        """
        @summary 重命名节点
        
        @param request: RenameNodeRequest
        @return: RenameNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.rename_node_with_options(request, runtime)

    async def rename_node_async(
        self,
        request: dataworks_public_20240518_models.RenameNodeRequest,
    ) -> dataworks_public_20240518_models.RenameNodeResponse:
        """
        @summary 重命名节点
        
        @param request: RenameNodeRequest
        @return: RenameNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.rename_node_with_options_async(request, runtime)

    def rename_resource_with_options(
        self,
        request: dataworks_public_20240518_models.RenameResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.RenameResourceResponse:
        """
        @summary 对资源文件重命名
        
        @param request: RenameResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RenameResourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RenameResource',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.RenameResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def rename_resource_with_options_async(
        self,
        request: dataworks_public_20240518_models.RenameResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.RenameResourceResponse:
        """
        @summary 对资源文件重命名
        
        @param request: RenameResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RenameResourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RenameResource',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.RenameResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rename_resource(
        self,
        request: dataworks_public_20240518_models.RenameResourceRequest,
    ) -> dataworks_public_20240518_models.RenameResourceResponse:
        """
        @summary 对资源文件重命名
        
        @param request: RenameResourceRequest
        @return: RenameResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.rename_resource_with_options(request, runtime)

    async def rename_resource_async(
        self,
        request: dataworks_public_20240518_models.RenameResourceRequest,
    ) -> dataworks_public_20240518_models.RenameResourceResponse:
        """
        @summary 对资源文件重命名
        
        @param request: RenameResourceRequest
        @return: RenameResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.rename_resource_with_options_async(request, runtime)

    def rename_workflow_definition_with_options(
        self,
        request: dataworks_public_20240518_models.RenameWorkflowDefinitionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.RenameWorkflowDefinitionResponse:
        """
        @summary 重命名工作流
        
        @param request: RenameWorkflowDefinitionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RenameWorkflowDefinitionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenameWorkflowDefinition',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.RenameWorkflowDefinitionResponse(),
            self.call_api(params, req, runtime)
        )

    async def rename_workflow_definition_with_options_async(
        self,
        request: dataworks_public_20240518_models.RenameWorkflowDefinitionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.RenameWorkflowDefinitionResponse:
        """
        @summary 重命名工作流
        
        @param request: RenameWorkflowDefinitionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RenameWorkflowDefinitionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenameWorkflowDefinition',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.RenameWorkflowDefinitionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rename_workflow_definition(
        self,
        request: dataworks_public_20240518_models.RenameWorkflowDefinitionRequest,
    ) -> dataworks_public_20240518_models.RenameWorkflowDefinitionResponse:
        """
        @summary 重命名工作流
        
        @param request: RenameWorkflowDefinitionRequest
        @return: RenameWorkflowDefinitionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.rename_workflow_definition_with_options(request, runtime)

    async def rename_workflow_definition_async(
        self,
        request: dataworks_public_20240518_models.RenameWorkflowDefinitionRequest,
    ) -> dataworks_public_20240518_models.RenameWorkflowDefinitionResponse:
        """
        @summary 重命名工作流
        
        @param request: RenameWorkflowDefinitionRequest
        @return: RenameWorkflowDefinitionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.rename_workflow_definition_with_options_async(request, runtime)

    def update_function_with_options(
        self,
        request: dataworks_public_20240518_models.UpdateFunctionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.UpdateFunctionResponse:
        """
        @summary 更新udf函数
        
        @param request: UpdateFunctionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateFunctionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.spec):
            body['Spec'] = request.spec
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateFunction',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.UpdateFunctionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_function_with_options_async(
        self,
        request: dataworks_public_20240518_models.UpdateFunctionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.UpdateFunctionResponse:
        """
        @summary 更新udf函数
        
        @param request: UpdateFunctionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateFunctionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.spec):
            body['Spec'] = request.spec
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateFunction',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.UpdateFunctionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_function(
        self,
        request: dataworks_public_20240518_models.UpdateFunctionRequest,
    ) -> dataworks_public_20240518_models.UpdateFunctionResponse:
        """
        @summary 更新udf函数
        
        @param request: UpdateFunctionRequest
        @return: UpdateFunctionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_function_with_options(request, runtime)

    async def update_function_async(
        self,
        request: dataworks_public_20240518_models.UpdateFunctionRequest,
    ) -> dataworks_public_20240518_models.UpdateFunctionResponse:
        """
        @summary 更新udf函数
        
        @param request: UpdateFunctionRequest
        @return: UpdateFunctionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_function_with_options_async(request, runtime)

    def update_node_with_options(
        self,
        request: dataworks_public_20240518_models.UpdateNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.UpdateNodeResponse:
        """
        @summary 更新节点
        
        @param request: UpdateNodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateNodeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.spec):
            body['Spec'] = request.spec
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateNode',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.UpdateNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_node_with_options_async(
        self,
        request: dataworks_public_20240518_models.UpdateNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.UpdateNodeResponse:
        """
        @summary 更新节点
        
        @param request: UpdateNodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateNodeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.spec):
            body['Spec'] = request.spec
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateNode',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.UpdateNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_node(
        self,
        request: dataworks_public_20240518_models.UpdateNodeRequest,
    ) -> dataworks_public_20240518_models.UpdateNodeResponse:
        """
        @summary 更新节点
        
        @param request: UpdateNodeRequest
        @return: UpdateNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_node_with_options(request, runtime)

    async def update_node_async(
        self,
        request: dataworks_public_20240518_models.UpdateNodeRequest,
    ) -> dataworks_public_20240518_models.UpdateNodeResponse:
        """
        @summary 更新节点
        
        @param request: UpdateNodeRequest
        @return: UpdateNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_node_with_options_async(request, runtime)

    def update_resource_with_options(
        self,
        request: dataworks_public_20240518_models.UpdateResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.UpdateResourceResponse:
        """
        @summary 更新资源文件
        
        @param request: UpdateResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateResourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.spec):
            body['Spec'] = request.spec
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateResource',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.UpdateResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_resource_with_options_async(
        self,
        request: dataworks_public_20240518_models.UpdateResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.UpdateResourceResponse:
        """
        @summary 更新资源文件
        
        @param request: UpdateResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateResourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.spec):
            body['Spec'] = request.spec
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateResource',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.UpdateResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_resource(
        self,
        request: dataworks_public_20240518_models.UpdateResourceRequest,
    ) -> dataworks_public_20240518_models.UpdateResourceResponse:
        """
        @summary 更新资源文件
        
        @param request: UpdateResourceRequest
        @return: UpdateResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_resource_with_options(request, runtime)

    async def update_resource_async(
        self,
        request: dataworks_public_20240518_models.UpdateResourceRequest,
    ) -> dataworks_public_20240518_models.UpdateResourceResponse:
        """
        @summary 更新资源文件
        
        @param request: UpdateResourceRequest
        @return: UpdateResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_resource_with_options_async(request, runtime)

    def update_workflow_definition_with_options(
        self,
        request: dataworks_public_20240518_models.UpdateWorkflowDefinitionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.UpdateWorkflowDefinitionResponse:
        """
        @summary 更新工作流
        
        @param request: UpdateWorkflowDefinitionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateWorkflowDefinitionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.spec):
            body['Spec'] = request.spec
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateWorkflowDefinition',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.UpdateWorkflowDefinitionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_workflow_definition_with_options_async(
        self,
        request: dataworks_public_20240518_models.UpdateWorkflowDefinitionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20240518_models.UpdateWorkflowDefinitionResponse:
        """
        @summary 更新工作流
        
        @param request: UpdateWorkflowDefinitionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateWorkflowDefinitionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.spec):
            body['Spec'] = request.spec
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateWorkflowDefinition',
            version='2024-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataworks_public_20240518_models.UpdateWorkflowDefinitionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_workflow_definition(
        self,
        request: dataworks_public_20240518_models.UpdateWorkflowDefinitionRequest,
    ) -> dataworks_public_20240518_models.UpdateWorkflowDefinitionResponse:
        """
        @summary 更新工作流
        
        @param request: UpdateWorkflowDefinitionRequest
        @return: UpdateWorkflowDefinitionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_workflow_definition_with_options(request, runtime)

    async def update_workflow_definition_async(
        self,
        request: dataworks_public_20240518_models.UpdateWorkflowDefinitionRequest,
    ) -> dataworks_public_20240518_models.UpdateWorkflowDefinitionResponse:
        """
        @summary 更新工作流
        
        @param request: UpdateWorkflowDefinitionRequest
        @return: UpdateWorkflowDefinitionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_workflow_definition_with_options_async(request, runtime)
