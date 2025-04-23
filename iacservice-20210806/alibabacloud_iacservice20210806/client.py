# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_iacservice20210806 import models as ia_cservice_20210806_models
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
        self._signature_algorithm = 'v2'
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('iacservice', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def associate_group_with_options(
        self,
        group_id: str,
        request: ia_cservice_20210806_models.AssociateGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.AssociateGroupResponse:
        """
        @summary 分组关联
        
        @param request: AssociateGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AssociateGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.project_id):
            body['projectId'] = request.project_id
        if not UtilClient.is_unset(request.resource_ids):
            body['resourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_type):
            body['resourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AssociateGroup',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/group/{OpenApiUtilClient.get_encode_param(group_id)}/associate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.AssociateGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def associate_group_with_options_async(
        self,
        group_id: str,
        request: ia_cservice_20210806_models.AssociateGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.AssociateGroupResponse:
        """
        @summary 分组关联
        
        @param request: AssociateGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AssociateGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.project_id):
            body['projectId'] = request.project_id
        if not UtilClient.is_unset(request.resource_ids):
            body['resourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_type):
            body['resourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AssociateGroup',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/group/{OpenApiUtilClient.get_encode_param(group_id)}/associate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.AssociateGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def associate_group(
        self,
        group_id: str,
        request: ia_cservice_20210806_models.AssociateGroupRequest,
    ) -> ia_cservice_20210806_models.AssociateGroupResponse:
        """
        @summary 分组关联
        
        @param request: AssociateGroupRequest
        @return: AssociateGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.associate_group_with_options(group_id, request, headers, runtime)

    async def associate_group_async(
        self,
        group_id: str,
        request: ia_cservice_20210806_models.AssociateGroupRequest,
    ) -> ia_cservice_20210806_models.AssociateGroupResponse:
        """
        @summary 分组关联
        
        @param request: AssociateGroupRequest
        @return: AssociateGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.associate_group_with_options_async(group_id, request, headers, runtime)

    def associate_parameter_set_with_options(
        self,
        request: ia_cservice_20210806_models.AssociateParameterSetRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.AssociateParameterSetResponse:
        """
        @summary 将参数集关联资源
        
        @param request: AssociateParameterSetRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AssociateParameterSetResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.parameter_set_ids):
            body['parameterSetIds'] = request.parameter_set_ids
        if not UtilClient.is_unset(request.resource_id):
            body['resourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            body['resourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AssociateParameterSet',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/parameterSets/operations/associate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.AssociateParameterSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def associate_parameter_set_with_options_async(
        self,
        request: ia_cservice_20210806_models.AssociateParameterSetRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.AssociateParameterSetResponse:
        """
        @summary 将参数集关联资源
        
        @param request: AssociateParameterSetRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AssociateParameterSetResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.parameter_set_ids):
            body['parameterSetIds'] = request.parameter_set_ids
        if not UtilClient.is_unset(request.resource_id):
            body['resourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            body['resourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AssociateParameterSet',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/parameterSets/operations/associate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.AssociateParameterSetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def associate_parameter_set(
        self,
        request: ia_cservice_20210806_models.AssociateParameterSetRequest,
    ) -> ia_cservice_20210806_models.AssociateParameterSetResponse:
        """
        @summary 将参数集关联资源
        
        @param request: AssociateParameterSetRequest
        @return: AssociateParameterSetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.associate_parameter_set_with_options(request, headers, runtime)

    async def associate_parameter_set_async(
        self,
        request: ia_cservice_20210806_models.AssociateParameterSetRequest,
    ) -> ia_cservice_20210806_models.AssociateParameterSetResponse:
        """
        @summary 将参数集关联资源
        
        @param request: AssociateParameterSetRequest
        @return: AssociateParameterSetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.associate_parameter_set_with_options_async(request, headers, runtime)

    def attach_rabbitmq_publisher_with_options(
        self,
        publisher_id: str,
        request: ia_cservice_20210806_models.AttachRabbitmqPublisherRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.AttachRabbitmqPublisherResponse:
        """
        @summary 将消息发布者挂载到任务
        
        @param request: AttachRabbitmqPublisherRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachRabbitmqPublisherResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['taskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AttachRabbitmqPublisher',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/publishers/{OpenApiUtilClient.get_encode_param(publisher_id)}/attach',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.AttachRabbitmqPublisherResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_rabbitmq_publisher_with_options_async(
        self,
        publisher_id: str,
        request: ia_cservice_20210806_models.AttachRabbitmqPublisherRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.AttachRabbitmqPublisherResponse:
        """
        @summary 将消息发布者挂载到任务
        
        @param request: AttachRabbitmqPublisherRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachRabbitmqPublisherResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['taskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AttachRabbitmqPublisher',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/publishers/{OpenApiUtilClient.get_encode_param(publisher_id)}/attach',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.AttachRabbitmqPublisherResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_rabbitmq_publisher(
        self,
        publisher_id: str,
        request: ia_cservice_20210806_models.AttachRabbitmqPublisherRequest,
    ) -> ia_cservice_20210806_models.AttachRabbitmqPublisherResponse:
        """
        @summary 将消息发布者挂载到任务
        
        @param request: AttachRabbitmqPublisherRequest
        @return: AttachRabbitmqPublisherResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.attach_rabbitmq_publisher_with_options(publisher_id, request, headers, runtime)

    async def attach_rabbitmq_publisher_async(
        self,
        publisher_id: str,
        request: ia_cservice_20210806_models.AttachRabbitmqPublisherRequest,
    ) -> ia_cservice_20210806_models.AttachRabbitmqPublisherResponse:
        """
        @summary 将消息发布者挂载到任务
        
        @param request: AttachRabbitmqPublisherRequest
        @return: AttachRabbitmqPublisherResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.attach_rabbitmq_publisher_with_options_async(publisher_id, request, headers, runtime)

    def cancel_project_build_with_options(
        self,
        project_id: str,
        project_build_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.CancelProjectBuildResponse:
        """
        @summary 取消执行
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelProjectBuildResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CancelProjectBuild',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/project/{OpenApiUtilClient.get_encode_param(project_id)}/build/{OpenApiUtilClient.get_encode_param(project_build_id)}/cancel',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.CancelProjectBuildResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_project_build_with_options_async(
        self,
        project_id: str,
        project_build_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.CancelProjectBuildResponse:
        """
        @summary 取消执行
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelProjectBuildResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CancelProjectBuild',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/project/{OpenApiUtilClient.get_encode_param(project_id)}/build/{OpenApiUtilClient.get_encode_param(project_build_id)}/cancel',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.CancelProjectBuildResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_project_build(
        self,
        project_id: str,
        project_build_id: str,
    ) -> ia_cservice_20210806_models.CancelProjectBuildResponse:
        """
        @summary 取消执行
        
        @return: CancelProjectBuildResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.cancel_project_build_with_options(project_id, project_build_id, headers, runtime)

    async def cancel_project_build_async(
        self,
        project_id: str,
        project_build_id: str,
    ) -> ia_cservice_20210806_models.CancelProjectBuildResponse:
        """
        @summary 取消执行
        
        @return: CancelProjectBuildResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.cancel_project_build_with_options_async(project_id, project_build_id, headers, runtime)

    def cancel_ram_policy_export_task_with_options(
        self,
        ram_policy_export_task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.CancelRamPolicyExportTaskResponse:
        """
        @summary 取消RAM策略导出任务
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelRamPolicyExportTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CancelRamPolicyExportTask',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/ramPolicyExportTasks/{OpenApiUtilClient.get_encode_param(ram_policy_export_task_id)}/cancel',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.CancelRamPolicyExportTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_ram_policy_export_task_with_options_async(
        self,
        ram_policy_export_task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.CancelRamPolicyExportTaskResponse:
        """
        @summary 取消RAM策略导出任务
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelRamPolicyExportTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CancelRamPolicyExportTask',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/ramPolicyExportTasks/{OpenApiUtilClient.get_encode_param(ram_policy_export_task_id)}/cancel',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.CancelRamPolicyExportTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_ram_policy_export_task(
        self,
        ram_policy_export_task_id: str,
    ) -> ia_cservice_20210806_models.CancelRamPolicyExportTaskResponse:
        """
        @summary 取消RAM策略导出任务
        
        @return: CancelRamPolicyExportTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.cancel_ram_policy_export_task_with_options(ram_policy_export_task_id, headers, runtime)

    async def cancel_ram_policy_export_task_async(
        self,
        ram_policy_export_task_id: str,
    ) -> ia_cservice_20210806_models.CancelRamPolicyExportTaskResponse:
        """
        @summary 取消RAM策略导出任务
        
        @return: CancelRamPolicyExportTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.cancel_ram_policy_export_task_with_options_async(ram_policy_export_task_id, headers, runtime)

    def cancel_resource_export_task_with_options(
        self,
        export_task_id: str,
        request: ia_cservice_20210806_models.CancelResourceExportTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.CancelResourceExportTaskResponse:
        """
        @summary 取消资源导出任务
        
        @param request: CancelResourceExportTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelResourceExportTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.ram_role):
            body['ramRole'] = request.ram_role
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelResourceExportTask',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/exportTasks/cancel/{OpenApiUtilClient.get_encode_param(export_task_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.CancelResourceExportTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_resource_export_task_with_options_async(
        self,
        export_task_id: str,
        request: ia_cservice_20210806_models.CancelResourceExportTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.CancelResourceExportTaskResponse:
        """
        @summary 取消资源导出任务
        
        @param request: CancelResourceExportTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelResourceExportTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.ram_role):
            body['ramRole'] = request.ram_role
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelResourceExportTask',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/exportTasks/cancel/{OpenApiUtilClient.get_encode_param(export_task_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.CancelResourceExportTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_resource_export_task(
        self,
        export_task_id: str,
        request: ia_cservice_20210806_models.CancelResourceExportTaskRequest,
    ) -> ia_cservice_20210806_models.CancelResourceExportTaskResponse:
        """
        @summary 取消资源导出任务
        
        @param request: CancelResourceExportTaskRequest
        @return: CancelResourceExportTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.cancel_resource_export_task_with_options(export_task_id, request, headers, runtime)

    async def cancel_resource_export_task_async(
        self,
        export_task_id: str,
        request: ia_cservice_20210806_models.CancelResourceExportTaskRequest,
    ) -> ia_cservice_20210806_models.CancelResourceExportTaskResponse:
        """
        @summary 取消资源导出任务
        
        @param request: CancelResourceExportTaskRequest
        @return: CancelResourceExportTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.cancel_resource_export_task_with_options_async(export_task_id, request, headers, runtime)

    def check_resource_name_with_options(
        self,
        request: ia_cservice_20210806_models.CheckResourceNameRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.CheckResourceNameResponse:
        """
        @summary 校验资源名称
        
        @param request: CheckResourceNameRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckResourceNameResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.parent_id):
            query['parentId'] = request.parent_id
        if not UtilClient.is_unset(request.resource_type):
            query['resourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckResourceName',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/check/name',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.CheckResourceNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_resource_name_with_options_async(
        self,
        request: ia_cservice_20210806_models.CheckResourceNameRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.CheckResourceNameResponse:
        """
        @summary 校验资源名称
        
        @param request: CheckResourceNameRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckResourceNameResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.parent_id):
            query['parentId'] = request.parent_id
        if not UtilClient.is_unset(request.resource_type):
            query['resourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckResourceName',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/check/name',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.CheckResourceNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_resource_name(
        self,
        request: ia_cservice_20210806_models.CheckResourceNameRequest,
    ) -> ia_cservice_20210806_models.CheckResourceNameResponse:
        """
        @summary 校验资源名称
        
        @param request: CheckResourceNameRequest
        @return: CheckResourceNameResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.check_resource_name_with_options(request, headers, runtime)

    async def check_resource_name_async(
        self,
        request: ia_cservice_20210806_models.CheckResourceNameRequest,
    ) -> ia_cservice_20210806_models.CheckResourceNameResponse:
        """
        @summary 校验资源名称
        
        @param request: CheckResourceNameRequest
        @return: CheckResourceNameResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.check_resource_name_with_options_async(request, headers, runtime)

    def clone_group_with_options(
        self,
        group_id: str,
        request: ia_cservice_20210806_models.CloneGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.CloneGroupResponse:
        """
        @summary 克隆分组
        
        @param request: CloneGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CloneGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.project_id):
            body['projectId'] = request.project_id
        if not UtilClient.is_unset(request.resource_types):
            body['resourceTypes'] = request.resource_types
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CloneGroup',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/group/{OpenApiUtilClient.get_encode_param(group_id)}/clone',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.CloneGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def clone_group_with_options_async(
        self,
        group_id: str,
        request: ia_cservice_20210806_models.CloneGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.CloneGroupResponse:
        """
        @summary 克隆分组
        
        @param request: CloneGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CloneGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.project_id):
            body['projectId'] = request.project_id
        if not UtilClient.is_unset(request.resource_types):
            body['resourceTypes'] = request.resource_types
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CloneGroup',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/group/{OpenApiUtilClient.get_encode_param(group_id)}/clone',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.CloneGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def clone_group(
        self,
        group_id: str,
        request: ia_cservice_20210806_models.CloneGroupRequest,
    ) -> ia_cservice_20210806_models.CloneGroupResponse:
        """
        @summary 克隆分组
        
        @param request: CloneGroupRequest
        @return: CloneGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.clone_group_with_options(group_id, request, headers, runtime)

    async def clone_group_async(
        self,
        group_id: str,
        request: ia_cservice_20210806_models.CloneGroupRequest,
    ) -> ia_cservice_20210806_models.CloneGroupResponse:
        """
        @summary 克隆分组
        
        @param request: CloneGroupRequest
        @return: CloneGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.clone_group_with_options_async(group_id, request, headers, runtime)

    def clone_module_with_options(
        self,
        request: ia_cservice_20210806_models.CloneModuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.CloneModuleResponse:
        """
        @summary 克隆模版
        
        @param request: CloneModuleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CloneModuleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.module_id):
            body['moduleId'] = request.module_id
        if not UtilClient.is_unset(request.module_source):
            body['moduleSource'] = request.module_source
        if not UtilClient.is_unset(request.module_version):
            body['moduleVersion'] = request.module_version
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CloneModule',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/modules/operations/clone',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.CloneModuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def clone_module_with_options_async(
        self,
        request: ia_cservice_20210806_models.CloneModuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.CloneModuleResponse:
        """
        @summary 克隆模版
        
        @param request: CloneModuleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CloneModuleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.module_id):
            body['moduleId'] = request.module_id
        if not UtilClient.is_unset(request.module_source):
            body['moduleSource'] = request.module_source
        if not UtilClient.is_unset(request.module_version):
            body['moduleVersion'] = request.module_version
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CloneModule',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/modules/operations/clone',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.CloneModuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def clone_module(
        self,
        request: ia_cservice_20210806_models.CloneModuleRequest,
    ) -> ia_cservice_20210806_models.CloneModuleResponse:
        """
        @summary 克隆模版
        
        @param request: CloneModuleRequest
        @return: CloneModuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.clone_module_with_options(request, headers, runtime)

    async def clone_module_async(
        self,
        request: ia_cservice_20210806_models.CloneModuleRequest,
    ) -> ia_cservice_20210806_models.CloneModuleResponse:
        """
        @summary 克隆模版
        
        @param request: CloneModuleRequest
        @return: CloneModuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.clone_module_with_options_async(request, headers, runtime)

    def create_authorization_with_options(
        self,
        request: ia_cservice_20210806_models.CreateAuthorizationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.CreateAuthorizationResponse:
        """
        @summary 创建共享
        
        @param request: CreateAuthorizationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAuthorizationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.due_time):
            body['dueTime'] = request.due_time
        if not UtilClient.is_unset(request.module_id):
            body['moduleId'] = request.module_id
        if not UtilClient.is_unset(request.module_version):
            body['moduleVersion'] = request.module_version
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.uid):
            body['uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAuthorization',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/authorizations',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.CreateAuthorizationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_authorization_with_options_async(
        self,
        request: ia_cservice_20210806_models.CreateAuthorizationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.CreateAuthorizationResponse:
        """
        @summary 创建共享
        
        @param request: CreateAuthorizationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAuthorizationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.due_time):
            body['dueTime'] = request.due_time
        if not UtilClient.is_unset(request.module_id):
            body['moduleId'] = request.module_id
        if not UtilClient.is_unset(request.module_version):
            body['moduleVersion'] = request.module_version
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.uid):
            body['uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAuthorization',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/authorizations',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.CreateAuthorizationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_authorization(
        self,
        request: ia_cservice_20210806_models.CreateAuthorizationRequest,
    ) -> ia_cservice_20210806_models.CreateAuthorizationResponse:
        """
        @summary 创建共享
        
        @param request: CreateAuthorizationRequest
        @return: CreateAuthorizationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_authorization_with_options(request, headers, runtime)

    async def create_authorization_async(
        self,
        request: ia_cservice_20210806_models.CreateAuthorizationRequest,
    ) -> ia_cservice_20210806_models.CreateAuthorizationResponse:
        """
        @summary 创建共享
        
        @param request: CreateAuthorizationRequest
        @return: CreateAuthorizationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_authorization_with_options_async(request, headers, runtime)

    def create_explorer_task_with_options(
        self,
        request: ia_cservice_20210806_models.CreateExplorerTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.CreateExplorerTaskResponse:
        """
        @summary 创建Explorer任务
        
        @param request: CreateExplorerTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateExplorerTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.init_module_state):
            body['InitModuleState'] = request.init_module_state
        if not UtilClient.is_unset(request.terraform_version):
            body['TerraformVersion'] = request.terraform_version
        if not UtilClient.is_unset(request.auto_apply):
            body['autoApply'] = request.auto_apply
        if not UtilClient.is_unset(request.auto_destroy):
            body['autoDestroy'] = request.auto_destroy
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.init_module_state):
            body['initModuleState'] = request.init_module_state
        if not UtilClient.is_unset(request.module_id):
            body['moduleId'] = request.module_id
        if not UtilClient.is_unset(request.module_version):
            body['moduleVersion'] = request.module_version
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.skip_property_validation):
            body['skipPropertyValidation'] = request.skip_property_validation
        if not UtilClient.is_unset(request.terraform_provider_version):
            body['terraformProviderVersion'] = request.terraform_provider_version
        if not UtilClient.is_unset(request.trigger_value):
            body['triggerValue'] = request.trigger_value
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateExplorerTask',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/explorerTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.CreateExplorerTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_explorer_task_with_options_async(
        self,
        request: ia_cservice_20210806_models.CreateExplorerTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.CreateExplorerTaskResponse:
        """
        @summary 创建Explorer任务
        
        @param request: CreateExplorerTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateExplorerTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.init_module_state):
            body['InitModuleState'] = request.init_module_state
        if not UtilClient.is_unset(request.terraform_version):
            body['TerraformVersion'] = request.terraform_version
        if not UtilClient.is_unset(request.auto_apply):
            body['autoApply'] = request.auto_apply
        if not UtilClient.is_unset(request.auto_destroy):
            body['autoDestroy'] = request.auto_destroy
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.init_module_state):
            body['initModuleState'] = request.init_module_state
        if not UtilClient.is_unset(request.module_id):
            body['moduleId'] = request.module_id
        if not UtilClient.is_unset(request.module_version):
            body['moduleVersion'] = request.module_version
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.skip_property_validation):
            body['skipPropertyValidation'] = request.skip_property_validation
        if not UtilClient.is_unset(request.terraform_provider_version):
            body['terraformProviderVersion'] = request.terraform_provider_version
        if not UtilClient.is_unset(request.trigger_value):
            body['triggerValue'] = request.trigger_value
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateExplorerTask',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/explorerTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.CreateExplorerTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_explorer_task(
        self,
        request: ia_cservice_20210806_models.CreateExplorerTaskRequest,
    ) -> ia_cservice_20210806_models.CreateExplorerTaskResponse:
        """
        @summary 创建Explorer任务
        
        @param request: CreateExplorerTaskRequest
        @return: CreateExplorerTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_explorer_task_with_options(request, headers, runtime)

    async def create_explorer_task_async(
        self,
        request: ia_cservice_20210806_models.CreateExplorerTaskRequest,
    ) -> ia_cservice_20210806_models.CreateExplorerTaskResponse:
        """
        @summary 创建Explorer任务
        
        @param request: CreateExplorerTaskRequest
        @return: CreateExplorerTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_explorer_task_with_options_async(request, headers, runtime)

    def create_group_with_options(
        self,
        request: ia_cservice_20210806_models.CreateGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.CreateGroupResponse:
        """
        @summary 创建分组
        
        @param request: CreateGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_destroy):
            body['autoDestroy'] = request.auto_destroy
        if not UtilClient.is_unset(request.auto_trigger):
            body['autoTrigger'] = request.auto_trigger
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.forced_setting):
            body['forcedSetting'] = request.forced_setting
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.notify_config):
            body['notifyConfig'] = request.notify_config
        if not UtilClient.is_unset(request.notify_operation_types):
            body['notifyOperationTypes'] = request.notify_operation_types
        if not UtilClient.is_unset(request.project_id):
            body['projectId'] = request.project_id
        if not UtilClient.is_unset(request.ram_role):
            body['ramRole'] = request.ram_role
        if not UtilClient.is_unset(request.report_export_field):
            body['reportExportField'] = request.report_export_field
        if not UtilClient.is_unset(request.report_export_path):
            body['reportExportPath'] = request.report_export_path
        if not UtilClient.is_unset(request.terraform_provider_version):
            body['terraformProviderVersion'] = request.terraform_provider_version
        if not UtilClient.is_unset(request.trigger_config):
            body['triggerConfig'] = request.trigger_config
        if not UtilClient.is_unset(request.trigger_resource_type):
            body['triggerResourceType'] = request.trigger_resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateGroup',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/group',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.CreateGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_group_with_options_async(
        self,
        request: ia_cservice_20210806_models.CreateGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.CreateGroupResponse:
        """
        @summary 创建分组
        
        @param request: CreateGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_destroy):
            body['autoDestroy'] = request.auto_destroy
        if not UtilClient.is_unset(request.auto_trigger):
            body['autoTrigger'] = request.auto_trigger
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.forced_setting):
            body['forcedSetting'] = request.forced_setting
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.notify_config):
            body['notifyConfig'] = request.notify_config
        if not UtilClient.is_unset(request.notify_operation_types):
            body['notifyOperationTypes'] = request.notify_operation_types
        if not UtilClient.is_unset(request.project_id):
            body['projectId'] = request.project_id
        if not UtilClient.is_unset(request.ram_role):
            body['ramRole'] = request.ram_role
        if not UtilClient.is_unset(request.report_export_field):
            body['reportExportField'] = request.report_export_field
        if not UtilClient.is_unset(request.report_export_path):
            body['reportExportPath'] = request.report_export_path
        if not UtilClient.is_unset(request.terraform_provider_version):
            body['terraformProviderVersion'] = request.terraform_provider_version
        if not UtilClient.is_unset(request.trigger_config):
            body['triggerConfig'] = request.trigger_config
        if not UtilClient.is_unset(request.trigger_resource_type):
            body['triggerResourceType'] = request.trigger_resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateGroup',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/group',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.CreateGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_group(
        self,
        request: ia_cservice_20210806_models.CreateGroupRequest,
    ) -> ia_cservice_20210806_models.CreateGroupResponse:
        """
        @summary 创建分组
        
        @param request: CreateGroupRequest
        @return: CreateGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_group_with_options(request, headers, runtime)

    async def create_group_async(
        self,
        request: ia_cservice_20210806_models.CreateGroupRequest,
    ) -> ia_cservice_20210806_models.CreateGroupResponse:
        """
        @summary 创建分组
        
        @param request: CreateGroupRequest
        @return: CreateGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_group_with_options_async(request, headers, runtime)

    def create_job_with_options(
        self,
        task_id: str,
        request: ia_cservice_20210806_models.CreateJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.CreateJobResponse:
        """
        @summary 创建作业
        
        @param request: CreateJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateJobResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.execute_type):
            body['executeType'] = request.execute_type
        if not UtilClient.is_unset(request.sub_command):
            body['subCommand'] = request.sub_command
        if not UtilClient.is_unset(request.task_type):
            body['taskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateJob',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/tasks/{OpenApiUtilClient.get_encode_param(task_id)}/jobs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.CreateJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_job_with_options_async(
        self,
        task_id: str,
        request: ia_cservice_20210806_models.CreateJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.CreateJobResponse:
        """
        @summary 创建作业
        
        @param request: CreateJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateJobResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.execute_type):
            body['executeType'] = request.execute_type
        if not UtilClient.is_unset(request.sub_command):
            body['subCommand'] = request.sub_command
        if not UtilClient.is_unset(request.task_type):
            body['taskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateJob',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/tasks/{OpenApiUtilClient.get_encode_param(task_id)}/jobs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.CreateJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_job(
        self,
        task_id: str,
        request: ia_cservice_20210806_models.CreateJobRequest,
    ) -> ia_cservice_20210806_models.CreateJobResponse:
        """
        @summary 创建作业
        
        @param request: CreateJobRequest
        @return: CreateJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_job_with_options(task_id, request, headers, runtime)

    async def create_job_async(
        self,
        task_id: str,
        request: ia_cservice_20210806_models.CreateJobRequest,
    ) -> ia_cservice_20210806_models.CreateJobResponse:
        """
        @summary 创建作业
        
        @param request: CreateJobRequest
        @return: CreateJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_job_with_options_async(task_id, request, headers, runtime)

    def create_module_with_options(
        self,
        request: ia_cservice_20210806_models.CreateModuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.CreateModuleResponse:
        """
        @summary 创建模版
        
        @param request: CreateModuleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateModuleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.group_info):
            body['groupInfo'] = request.group_info
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.source):
            body['source'] = request.source
        if not UtilClient.is_unset(request.source_path):
            body['sourcePath'] = request.source_path
        if not UtilClient.is_unset(request.state_path):
            body['statePath'] = request.state_path
        if not UtilClient.is_unset(request.version_strategy):
            body['versionStrategy'] = request.version_strategy
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateModule',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/modules',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.CreateModuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_module_with_options_async(
        self,
        request: ia_cservice_20210806_models.CreateModuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.CreateModuleResponse:
        """
        @summary 创建模版
        
        @param request: CreateModuleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateModuleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.group_info):
            body['groupInfo'] = request.group_info
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.source):
            body['source'] = request.source
        if not UtilClient.is_unset(request.source_path):
            body['sourcePath'] = request.source_path
        if not UtilClient.is_unset(request.state_path):
            body['statePath'] = request.state_path
        if not UtilClient.is_unset(request.version_strategy):
            body['versionStrategy'] = request.version_strategy
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateModule',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/modules',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.CreateModuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_module(
        self,
        request: ia_cservice_20210806_models.CreateModuleRequest,
    ) -> ia_cservice_20210806_models.CreateModuleResponse:
        """
        @summary 创建模版
        
        @param request: CreateModuleRequest
        @return: CreateModuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_module_with_options(request, headers, runtime)

    async def create_module_async(
        self,
        request: ia_cservice_20210806_models.CreateModuleRequest,
    ) -> ia_cservice_20210806_models.CreateModuleResponse:
        """
        @summary 创建模版
        
        @param request: CreateModuleRequest
        @return: CreateModuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_module_with_options_async(request, headers, runtime)

    def create_module_version_with_options(
        self,
        module_id: str,
        request: ia_cservice_20210806_models.CreateModuleVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.CreateModuleVersionResponse:
        """
        @summary 创建模版版本
        
        @param request: CreateModuleVersionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateModuleVersionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateModuleVersion',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/modules/{OpenApiUtilClient.get_encode_param(module_id)}/versions',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.CreateModuleVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_module_version_with_options_async(
        self,
        module_id: str,
        request: ia_cservice_20210806_models.CreateModuleVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.CreateModuleVersionResponse:
        """
        @summary 创建模版版本
        
        @param request: CreateModuleVersionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateModuleVersionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateModuleVersion',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/modules/{OpenApiUtilClient.get_encode_param(module_id)}/versions',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.CreateModuleVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_module_version(
        self,
        module_id: str,
        request: ia_cservice_20210806_models.CreateModuleVersionRequest,
    ) -> ia_cservice_20210806_models.CreateModuleVersionResponse:
        """
        @summary 创建模版版本
        
        @param request: CreateModuleVersionRequest
        @return: CreateModuleVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_module_version_with_options(module_id, request, headers, runtime)

    async def create_module_version_async(
        self,
        module_id: str,
        request: ia_cservice_20210806_models.CreateModuleVersionRequest,
    ) -> ia_cservice_20210806_models.CreateModuleVersionResponse:
        """
        @summary 创建模版版本
        
        @param request: CreateModuleVersionRequest
        @return: CreateModuleVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_module_version_with_options_async(module_id, request, headers, runtime)

    def create_parameter_set_with_options(
        self,
        request: ia_cservice_20210806_models.CreateParameterSetRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.CreateParameterSetResponse:
        """
        @summary 创建参数集
        
        @param request: CreateParameterSetRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateParameterSetResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.parameters):
            body['parameters'] = request.parameters
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateParameterSet',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/parameterSets',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.CreateParameterSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_parameter_set_with_options_async(
        self,
        request: ia_cservice_20210806_models.CreateParameterSetRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.CreateParameterSetResponse:
        """
        @summary 创建参数集
        
        @param request: CreateParameterSetRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateParameterSetResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.parameters):
            body['parameters'] = request.parameters
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateParameterSet',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/parameterSets',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.CreateParameterSetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_parameter_set(
        self,
        request: ia_cservice_20210806_models.CreateParameterSetRequest,
    ) -> ia_cservice_20210806_models.CreateParameterSetResponse:
        """
        @summary 创建参数集
        
        @param request: CreateParameterSetRequest
        @return: CreateParameterSetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_parameter_set_with_options(request, headers, runtime)

    async def create_parameter_set_async(
        self,
        request: ia_cservice_20210806_models.CreateParameterSetRequest,
    ) -> ia_cservice_20210806_models.CreateParameterSetResponse:
        """
        @summary 创建参数集
        
        @param request: CreateParameterSetRequest
        @return: CreateParameterSetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_parameter_set_with_options_async(request, headers, runtime)

    def create_project_with_options(
        self,
        request: ia_cservice_20210806_models.CreateProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.CreateProjectResponse:
        """
        @summary 创建项目
        
        @param request: CreateProjectRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateProjectResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProject',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/project',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.CreateProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_project_with_options_async(
        self,
        request: ia_cservice_20210806_models.CreateProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.CreateProjectResponse:
        """
        @summary 创建项目
        
        @param request: CreateProjectRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateProjectResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProject',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/project',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.CreateProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_project(
        self,
        request: ia_cservice_20210806_models.CreateProjectRequest,
    ) -> ia_cservice_20210806_models.CreateProjectResponse:
        """
        @summary 创建项目
        
        @param request: CreateProjectRequest
        @return: CreateProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_project_with_options(request, headers, runtime)

    async def create_project_async(
        self,
        request: ia_cservice_20210806_models.CreateProjectRequest,
    ) -> ia_cservice_20210806_models.CreateProjectResponse:
        """
        @summary 创建项目
        
        @param request: CreateProjectRequest
        @return: CreateProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_project_with_options_async(request, headers, runtime)

    def create_project_build_with_options(
        self,
        project_id: str,
        request: ia_cservice_20210806_models.CreateProjectBuildRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.CreateProjectBuildResponse:
        """
        @summary 构建项目批次
        
        @param request: CreateProjectBuildRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateProjectBuildResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.group_id):
            body['groupId'] = request.group_id
        if not UtilClient.is_unset(request.project_build_action):
            body['projectBuildAction'] = request.project_build_action
        if not UtilClient.is_unset(request.task_ids):
            body['taskIds'] = request.task_ids
        if not UtilClient.is_unset(request.task_policies):
            body['taskPolicies'] = request.task_policies
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProjectBuild',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/project/{OpenApiUtilClient.get_encode_param(project_id)}/build',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.CreateProjectBuildResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_project_build_with_options_async(
        self,
        project_id: str,
        request: ia_cservice_20210806_models.CreateProjectBuildRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.CreateProjectBuildResponse:
        """
        @summary 构建项目批次
        
        @param request: CreateProjectBuildRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateProjectBuildResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.group_id):
            body['groupId'] = request.group_id
        if not UtilClient.is_unset(request.project_build_action):
            body['projectBuildAction'] = request.project_build_action
        if not UtilClient.is_unset(request.task_ids):
            body['taskIds'] = request.task_ids
        if not UtilClient.is_unset(request.task_policies):
            body['taskPolicies'] = request.task_policies
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProjectBuild',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/project/{OpenApiUtilClient.get_encode_param(project_id)}/build',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.CreateProjectBuildResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_project_build(
        self,
        project_id: str,
        request: ia_cservice_20210806_models.CreateProjectBuildRequest,
    ) -> ia_cservice_20210806_models.CreateProjectBuildResponse:
        """
        @summary 构建项目批次
        
        @param request: CreateProjectBuildRequest
        @return: CreateProjectBuildResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_project_build_with_options(project_id, request, headers, runtime)

    async def create_project_build_async(
        self,
        project_id: str,
        request: ia_cservice_20210806_models.CreateProjectBuildRequest,
    ) -> ia_cservice_20210806_models.CreateProjectBuildResponse:
        """
        @summary 构建项目批次
        
        @param request: CreateProjectBuildRequest
        @return: CreateProjectBuildResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_project_build_with_options_async(project_id, request, headers, runtime)

    def create_rabbitmq_publisher_with_options(
        self,
        request: ia_cservice_20210806_models.CreateRabbitmqPublisherRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.CreateRabbitmqPublisherResponse:
        """
        @summary 创建消息发布者
        
        @param request: CreateRabbitmqPublisherRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRabbitmqPublisherResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.exchange_name):
            body['exchangeName'] = request.exchange_name
        if not UtilClient.is_unset(request.exchange_type):
            body['exchangeType'] = request.exchange_type
        if not UtilClient.is_unset(request.host_name):
            body['hostName'] = request.host_name
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.password):
            body['password'] = request.password
        if not UtilClient.is_unset(request.port):
            body['port'] = request.port
        if not UtilClient.is_unset(request.user_name):
            body['userName'] = request.user_name
        if not UtilClient.is_unset(request.virtual_host):
            body['virtualHost'] = request.virtual_host
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateRabbitmqPublisher',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/publishers',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.CreateRabbitmqPublisherResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_rabbitmq_publisher_with_options_async(
        self,
        request: ia_cservice_20210806_models.CreateRabbitmqPublisherRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.CreateRabbitmqPublisherResponse:
        """
        @summary 创建消息发布者
        
        @param request: CreateRabbitmqPublisherRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRabbitmqPublisherResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.exchange_name):
            body['exchangeName'] = request.exchange_name
        if not UtilClient.is_unset(request.exchange_type):
            body['exchangeType'] = request.exchange_type
        if not UtilClient.is_unset(request.host_name):
            body['hostName'] = request.host_name
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.password):
            body['password'] = request.password
        if not UtilClient.is_unset(request.port):
            body['port'] = request.port
        if not UtilClient.is_unset(request.user_name):
            body['userName'] = request.user_name
        if not UtilClient.is_unset(request.virtual_host):
            body['virtualHost'] = request.virtual_host
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateRabbitmqPublisher',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/publishers',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.CreateRabbitmqPublisherResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_rabbitmq_publisher(
        self,
        request: ia_cservice_20210806_models.CreateRabbitmqPublisherRequest,
    ) -> ia_cservice_20210806_models.CreateRabbitmqPublisherResponse:
        """
        @summary 创建消息发布者
        
        @param request: CreateRabbitmqPublisherRequest
        @return: CreateRabbitmqPublisherResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_rabbitmq_publisher_with_options(request, headers, runtime)

    async def create_rabbitmq_publisher_async(
        self,
        request: ia_cservice_20210806_models.CreateRabbitmqPublisherRequest,
    ) -> ia_cservice_20210806_models.CreateRabbitmqPublisherResponse:
        """
        @summary 创建消息发布者
        
        @param request: CreateRabbitmqPublisherRequest
        @return: CreateRabbitmqPublisherResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_rabbitmq_publisher_with_options_async(request, headers, runtime)

    def create_ram_policy_export_task_with_options(
        self,
        request: ia_cservice_20210806_models.CreateRamPolicyExportTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.CreateRamPolicyExportTaskResponse:
        """
        @summary 创建RAM策略导出任务
        
        @param request: CreateRamPolicyExportTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRamPolicyExportTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.authorization_account_ids):
            body['authorizationAccountIds'] = request.authorization_account_ids
        if not UtilClient.is_unset(request.authorization_actions):
            body['authorizationActions'] = request.authorization_actions
        if not UtilClient.is_unset(request.authorization_region_ids):
            body['authorizationRegionIds'] = request.authorization_region_ids
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.module_id):
            body['moduleId'] = request.module_id
        if not UtilClient.is_unset(request.module_version):
            body['moduleVersion'] = request.module_version
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.ram_role):
            body['ramRole'] = request.ram_role
        if not UtilClient.is_unset(request.terraform_provider_version):
            body['terraformProviderVersion'] = request.terraform_provider_version
        if not UtilClient.is_unset(request.trigger_strategy):
            body['triggerStrategy'] = request.trigger_strategy
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateRamPolicyExportTask',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/ramPolicyExportTasks',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.CreateRamPolicyExportTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ram_policy_export_task_with_options_async(
        self,
        request: ia_cservice_20210806_models.CreateRamPolicyExportTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.CreateRamPolicyExportTaskResponse:
        """
        @summary 创建RAM策略导出任务
        
        @param request: CreateRamPolicyExportTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRamPolicyExportTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.authorization_account_ids):
            body['authorizationAccountIds'] = request.authorization_account_ids
        if not UtilClient.is_unset(request.authorization_actions):
            body['authorizationActions'] = request.authorization_actions
        if not UtilClient.is_unset(request.authorization_region_ids):
            body['authorizationRegionIds'] = request.authorization_region_ids
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.module_id):
            body['moduleId'] = request.module_id
        if not UtilClient.is_unset(request.module_version):
            body['moduleVersion'] = request.module_version
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.ram_role):
            body['ramRole'] = request.ram_role
        if not UtilClient.is_unset(request.terraform_provider_version):
            body['terraformProviderVersion'] = request.terraform_provider_version
        if not UtilClient.is_unset(request.trigger_strategy):
            body['triggerStrategy'] = request.trigger_strategy
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateRamPolicyExportTask',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/ramPolicyExportTasks',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.CreateRamPolicyExportTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ram_policy_export_task(
        self,
        request: ia_cservice_20210806_models.CreateRamPolicyExportTaskRequest,
    ) -> ia_cservice_20210806_models.CreateRamPolicyExportTaskResponse:
        """
        @summary 创建RAM策略导出任务
        
        @param request: CreateRamPolicyExportTaskRequest
        @return: CreateRamPolicyExportTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_ram_policy_export_task_with_options(request, headers, runtime)

    async def create_ram_policy_export_task_async(
        self,
        request: ia_cservice_20210806_models.CreateRamPolicyExportTaskRequest,
    ) -> ia_cservice_20210806_models.CreateRamPolicyExportTaskResponse:
        """
        @summary 创建RAM策略导出任务
        
        @param request: CreateRamPolicyExportTaskRequest
        @return: CreateRamPolicyExportTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_ram_policy_export_task_with_options_async(request, headers, runtime)

    def create_resource_export_task_with_options(
        self,
        request: ia_cservice_20210806_models.CreateResourceExportTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.CreateResourceExportTaskResponse:
        """
        @summary 创建导出任务
        
        @param request: CreateResourceExportTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateResourceExportTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.config_path):
            body['configPath'] = request.config_path
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.exclude_rules):
            body['excludeRules'] = request.exclude_rules
        if not UtilClient.is_unset(request.export_to_module):
            body['exportToModule'] = request.export_to_module
        if not UtilClient.is_unset(request.include_rules):
            body['includeRules'] = request.include_rules
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.ram_role):
            body['ramRole'] = request.ram_role
        if not UtilClient.is_unset(request.terraform_provider_version):
            body['terraformProviderVersion'] = request.terraform_provider_version
        if not UtilClient.is_unset(request.terraform_version):
            body['terraformVersion'] = request.terraform_version
        if not UtilClient.is_unset(request.trigger_strategy):
            body['triggerStrategy'] = request.trigger_strategy
        if not UtilClient.is_unset(request.variables):
            body['variables'] = request.variables
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateResourceExportTask',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/exportTasks',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.CreateResourceExportTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_resource_export_task_with_options_async(
        self,
        request: ia_cservice_20210806_models.CreateResourceExportTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.CreateResourceExportTaskResponse:
        """
        @summary 创建导出任务
        
        @param request: CreateResourceExportTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateResourceExportTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.config_path):
            body['configPath'] = request.config_path
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.exclude_rules):
            body['excludeRules'] = request.exclude_rules
        if not UtilClient.is_unset(request.export_to_module):
            body['exportToModule'] = request.export_to_module
        if not UtilClient.is_unset(request.include_rules):
            body['includeRules'] = request.include_rules
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.ram_role):
            body['ramRole'] = request.ram_role
        if not UtilClient.is_unset(request.terraform_provider_version):
            body['terraformProviderVersion'] = request.terraform_provider_version
        if not UtilClient.is_unset(request.terraform_version):
            body['terraformVersion'] = request.terraform_version
        if not UtilClient.is_unset(request.trigger_strategy):
            body['triggerStrategy'] = request.trigger_strategy
        if not UtilClient.is_unset(request.variables):
            body['variables'] = request.variables
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateResourceExportTask',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/exportTasks',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.CreateResourceExportTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_resource_export_task(
        self,
        request: ia_cservice_20210806_models.CreateResourceExportTaskRequest,
    ) -> ia_cservice_20210806_models.CreateResourceExportTaskResponse:
        """
        @summary 创建导出任务
        
        @param request: CreateResourceExportTaskRequest
        @return: CreateResourceExportTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_resource_export_task_with_options(request, headers, runtime)

    async def create_resource_export_task_async(
        self,
        request: ia_cservice_20210806_models.CreateResourceExportTaskRequest,
    ) -> ia_cservice_20210806_models.CreateResourceExportTaskResponse:
        """
        @summary 创建导出任务
        
        @param request: CreateResourceExportTaskRequest
        @return: CreateResourceExportTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_resource_export_task_with_options_async(request, headers, runtime)

    def create_task_with_options(
        self,
        request: ia_cservice_20210806_models.CreateTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.CreateTaskResponse:
        """
        @summary 创建任务
        
        @param request: CreateTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_apply):
            body['autoApply'] = request.auto_apply
        if not UtilClient.is_unset(request.auto_destroy):
            body['autoDestroy'] = request.auto_destroy
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.group_info):
            body['groupInfo'] = request.group_info
        if not UtilClient.is_unset(request.init_module_state):
            body['initModuleState'] = request.init_module_state
        if not UtilClient.is_unset(request.module_id):
            body['moduleId'] = request.module_id
        if not UtilClient.is_unset(request.module_version):
            body['moduleVersion'] = request.module_version
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.parameters):
            body['parameters'] = request.parameters
        if not UtilClient.is_unset(request.protection_strategy):
            body['protectionStrategy'] = request.protection_strategy
        if not UtilClient.is_unset(request.ram_role):
            body['ramRole'] = request.ram_role
        if not UtilClient.is_unset(request.skip_property_validation):
            body['skipPropertyValidation'] = request.skip_property_validation
        if not UtilClient.is_unset(request.task_backend):
            body['taskBackend'] = request.task_backend
        if not UtilClient.is_unset(request.terraform_version):
            body['terraformVersion'] = request.terraform_version
        if not UtilClient.is_unset(request.trigger_strategy):
            body['triggerStrategy'] = request.trigger_strategy
        if not UtilClient.is_unset(request.trigger_value):
            body['triggerValue'] = request.trigger_value
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTask',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/tasks',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.CreateTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_task_with_options_async(
        self,
        request: ia_cservice_20210806_models.CreateTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.CreateTaskResponse:
        """
        @summary 创建任务
        
        @param request: CreateTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_apply):
            body['autoApply'] = request.auto_apply
        if not UtilClient.is_unset(request.auto_destroy):
            body['autoDestroy'] = request.auto_destroy
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.group_info):
            body['groupInfo'] = request.group_info
        if not UtilClient.is_unset(request.init_module_state):
            body['initModuleState'] = request.init_module_state
        if not UtilClient.is_unset(request.module_id):
            body['moduleId'] = request.module_id
        if not UtilClient.is_unset(request.module_version):
            body['moduleVersion'] = request.module_version
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.parameters):
            body['parameters'] = request.parameters
        if not UtilClient.is_unset(request.protection_strategy):
            body['protectionStrategy'] = request.protection_strategy
        if not UtilClient.is_unset(request.ram_role):
            body['ramRole'] = request.ram_role
        if not UtilClient.is_unset(request.skip_property_validation):
            body['skipPropertyValidation'] = request.skip_property_validation
        if not UtilClient.is_unset(request.task_backend):
            body['taskBackend'] = request.task_backend
        if not UtilClient.is_unset(request.terraform_version):
            body['terraformVersion'] = request.terraform_version
        if not UtilClient.is_unset(request.trigger_strategy):
            body['triggerStrategy'] = request.trigger_strategy
        if not UtilClient.is_unset(request.trigger_value):
            body['triggerValue'] = request.trigger_value
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTask',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/tasks',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.CreateTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_task(
        self,
        request: ia_cservice_20210806_models.CreateTaskRequest,
    ) -> ia_cservice_20210806_models.CreateTaskResponse:
        """
        @summary 创建任务
        
        @param request: CreateTaskRequest
        @return: CreateTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_task_with_options(request, headers, runtime)

    async def create_task_async(
        self,
        request: ia_cservice_20210806_models.CreateTaskRequest,
    ) -> ia_cservice_20210806_models.CreateTaskResponse:
        """
        @summary 创建任务
        
        @param request: CreateTaskRequest
        @return: CreateTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_task_with_options_async(request, headers, runtime)

    def delete_authorization_with_options(
        self,
        authorization_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.DeleteAuthorizationResponse:
        """
        @summary 删除共享
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAuthorizationResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteAuthorization',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/authorizations/{OpenApiUtilClient.get_encode_param(authorization_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.DeleteAuthorizationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_authorization_with_options_async(
        self,
        authorization_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.DeleteAuthorizationResponse:
        """
        @summary 删除共享
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAuthorizationResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteAuthorization',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/authorizations/{OpenApiUtilClient.get_encode_param(authorization_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.DeleteAuthorizationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_authorization(
        self,
        authorization_id: str,
    ) -> ia_cservice_20210806_models.DeleteAuthorizationResponse:
        """
        @summary 删除共享
        
        @return: DeleteAuthorizationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_authorization_with_options(authorization_id, headers, runtime)

    async def delete_authorization_async(
        self,
        authorization_id: str,
    ) -> ia_cservice_20210806_models.DeleteAuthorizationResponse:
        """
        @summary 删除共享
        
        @return: DeleteAuthorizationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_authorization_with_options_async(authorization_id, headers, runtime)

    def delete_group_with_options(
        self,
        group_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.DeleteGroupResponse:
        """
        @summary 删除分组
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteGroupResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteGroup',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/group/{OpenApiUtilClient.get_encode_param(group_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.DeleteGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_group_with_options_async(
        self,
        group_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.DeleteGroupResponse:
        """
        @summary 删除分组
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteGroupResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteGroup',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/group/{OpenApiUtilClient.get_encode_param(group_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.DeleteGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_group(
        self,
        group_id: str,
    ) -> ia_cservice_20210806_models.DeleteGroupResponse:
        """
        @summary 删除分组
        
        @return: DeleteGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_group_with_options(group_id, headers, runtime)

    async def delete_group_async(
        self,
        group_id: str,
    ) -> ia_cservice_20210806_models.DeleteGroupResponse:
        """
        @summary 删除分组
        
        @return: DeleteGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_group_with_options_async(group_id, headers, runtime)

    def delete_module_with_options(
        self,
        module_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.DeleteModuleResponse:
        """
        @summary 删除模版
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteModuleResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteModule',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/modules/{OpenApiUtilClient.get_encode_param(module_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.DeleteModuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_module_with_options_async(
        self,
        module_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.DeleteModuleResponse:
        """
        @summary 删除模版
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteModuleResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteModule',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/modules/{OpenApiUtilClient.get_encode_param(module_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.DeleteModuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_module(
        self,
        module_id: str,
    ) -> ia_cservice_20210806_models.DeleteModuleResponse:
        """
        @summary 删除模版
        
        @return: DeleteModuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_module_with_options(module_id, headers, runtime)

    async def delete_module_async(
        self,
        module_id: str,
    ) -> ia_cservice_20210806_models.DeleteModuleResponse:
        """
        @summary 删除模版
        
        @return: DeleteModuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_module_with_options_async(module_id, headers, runtime)

    def delete_parameter_set_with_options(
        self,
        parameter_set_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.DeleteParameterSetResponse:
        """
        @summary 删除参数集
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteParameterSetResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteParameterSet',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/parameterSets/{OpenApiUtilClient.get_encode_param(parameter_set_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.DeleteParameterSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_parameter_set_with_options_async(
        self,
        parameter_set_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.DeleteParameterSetResponse:
        """
        @summary 删除参数集
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteParameterSetResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteParameterSet',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/parameterSets/{OpenApiUtilClient.get_encode_param(parameter_set_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.DeleteParameterSetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_parameter_set(
        self,
        parameter_set_id: str,
    ) -> ia_cservice_20210806_models.DeleteParameterSetResponse:
        """
        @summary 删除参数集
        
        @return: DeleteParameterSetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_parameter_set_with_options(parameter_set_id, headers, runtime)

    async def delete_parameter_set_async(
        self,
        parameter_set_id: str,
    ) -> ia_cservice_20210806_models.DeleteParameterSetResponse:
        """
        @summary 删除参数集
        
        @return: DeleteParameterSetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_parameter_set_with_options_async(parameter_set_id, headers, runtime)

    def delete_project_with_options(
        self,
        project_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.DeleteProjectResponse:
        """
        @summary 删除项目
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteProjectResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteProject',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/project/{OpenApiUtilClient.get_encode_param(project_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.DeleteProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_project_with_options_async(
        self,
        project_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.DeleteProjectResponse:
        """
        @summary 删除项目
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteProjectResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteProject',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/project/{OpenApiUtilClient.get_encode_param(project_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.DeleteProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_project(
        self,
        project_id: str,
    ) -> ia_cservice_20210806_models.DeleteProjectResponse:
        """
        @summary 删除项目
        
        @return: DeleteProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_project_with_options(project_id, headers, runtime)

    async def delete_project_async(
        self,
        project_id: str,
    ) -> ia_cservice_20210806_models.DeleteProjectResponse:
        """
        @summary 删除项目
        
        @return: DeleteProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_project_with_options_async(project_id, headers, runtime)

    def delete_rabbitmq_publisher_with_options(
        self,
        publisher_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.DeleteRabbitmqPublisherResponse:
        """
        @summary 删除消息发布者
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRabbitmqPublisherResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteRabbitmqPublisher',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/publishers/{OpenApiUtilClient.get_encode_param(publisher_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.DeleteRabbitmqPublisherResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_rabbitmq_publisher_with_options_async(
        self,
        publisher_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.DeleteRabbitmqPublisherResponse:
        """
        @summary 删除消息发布者
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRabbitmqPublisherResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteRabbitmqPublisher',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/publishers/{OpenApiUtilClient.get_encode_param(publisher_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.DeleteRabbitmqPublisherResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_rabbitmq_publisher(
        self,
        publisher_id: str,
    ) -> ia_cservice_20210806_models.DeleteRabbitmqPublisherResponse:
        """
        @summary 删除消息发布者
        
        @return: DeleteRabbitmqPublisherResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_rabbitmq_publisher_with_options(publisher_id, headers, runtime)

    async def delete_rabbitmq_publisher_async(
        self,
        publisher_id: str,
    ) -> ia_cservice_20210806_models.DeleteRabbitmqPublisherResponse:
        """
        @summary 删除消息发布者
        
        @return: DeleteRabbitmqPublisherResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_rabbitmq_publisher_with_options_async(publisher_id, headers, runtime)

    def delete_ram_policy_export_task_with_options(
        self,
        ram_policy_export_task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.DeleteRamPolicyExportTaskResponse:
        """
        @summary 删除RAM策略导出任务
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRamPolicyExportTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteRamPolicyExportTask',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/ramPolicyExportTasks/{OpenApiUtilClient.get_encode_param(ram_policy_export_task_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.DeleteRamPolicyExportTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ram_policy_export_task_with_options_async(
        self,
        ram_policy_export_task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.DeleteRamPolicyExportTaskResponse:
        """
        @summary 删除RAM策略导出任务
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRamPolicyExportTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteRamPolicyExportTask',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/ramPolicyExportTasks/{OpenApiUtilClient.get_encode_param(ram_policy_export_task_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.DeleteRamPolicyExportTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_ram_policy_export_task(
        self,
        ram_policy_export_task_id: str,
    ) -> ia_cservice_20210806_models.DeleteRamPolicyExportTaskResponse:
        """
        @summary 删除RAM策略导出任务
        
        @return: DeleteRamPolicyExportTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_ram_policy_export_task_with_options(ram_policy_export_task_id, headers, runtime)

    async def delete_ram_policy_export_task_async(
        self,
        ram_policy_export_task_id: str,
    ) -> ia_cservice_20210806_models.DeleteRamPolicyExportTaskResponse:
        """
        @summary 删除RAM策略导出任务
        
        @return: DeleteRamPolicyExportTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_ram_policy_export_task_with_options_async(ram_policy_export_task_id, headers, runtime)

    def delete_ram_policy_export_task_version_with_options(
        self,
        ram_policy_export_task_id: str,
        export_version: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.DeleteRamPolicyExportTaskVersionResponse:
        """
        @summary 删除RAM策略导出任务版本
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRamPolicyExportTaskVersionResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteRamPolicyExportTaskVersion',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/ramPolicyExportTasks/{OpenApiUtilClient.get_encode_param(ram_policy_export_task_id)}/versions/{OpenApiUtilClient.get_encode_param(export_version)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.DeleteRamPolicyExportTaskVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ram_policy_export_task_version_with_options_async(
        self,
        ram_policy_export_task_id: str,
        export_version: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.DeleteRamPolicyExportTaskVersionResponse:
        """
        @summary 删除RAM策略导出任务版本
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRamPolicyExportTaskVersionResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteRamPolicyExportTaskVersion',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/ramPolicyExportTasks/{OpenApiUtilClient.get_encode_param(ram_policy_export_task_id)}/versions/{OpenApiUtilClient.get_encode_param(export_version)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.DeleteRamPolicyExportTaskVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_ram_policy_export_task_version(
        self,
        ram_policy_export_task_id: str,
        export_version: str,
    ) -> ia_cservice_20210806_models.DeleteRamPolicyExportTaskVersionResponse:
        """
        @summary 删除RAM策略导出任务版本
        
        @return: DeleteRamPolicyExportTaskVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_ram_policy_export_task_version_with_options(ram_policy_export_task_id, export_version, headers, runtime)

    async def delete_ram_policy_export_task_version_async(
        self,
        ram_policy_export_task_id: str,
        export_version: str,
    ) -> ia_cservice_20210806_models.DeleteRamPolicyExportTaskVersionResponse:
        """
        @summary 删除RAM策略导出任务版本
        
        @return: DeleteRamPolicyExportTaskVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_ram_policy_export_task_version_with_options_async(ram_policy_export_task_id, export_version, headers, runtime)

    def delete_resource_export_task_with_options(
        self,
        export_task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.DeleteResourceExportTaskResponse:
        """
        @summary 删除任务
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteResourceExportTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteResourceExportTask',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/exportTasks/{OpenApiUtilClient.get_encode_param(export_task_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.DeleteResourceExportTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_resource_export_task_with_options_async(
        self,
        export_task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.DeleteResourceExportTaskResponse:
        """
        @summary 删除任务
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteResourceExportTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteResourceExportTask',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/exportTasks/{OpenApiUtilClient.get_encode_param(export_task_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.DeleteResourceExportTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_resource_export_task(
        self,
        export_task_id: str,
    ) -> ia_cservice_20210806_models.DeleteResourceExportTaskResponse:
        """
        @summary 删除任务
        
        @return: DeleteResourceExportTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_resource_export_task_with_options(export_task_id, headers, runtime)

    async def delete_resource_export_task_async(
        self,
        export_task_id: str,
    ) -> ia_cservice_20210806_models.DeleteResourceExportTaskResponse:
        """
        @summary 删除任务
        
        @return: DeleteResourceExportTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_resource_export_task_with_options_async(export_task_id, headers, runtime)

    def delete_scene_testing_task_with_options(
        self,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.DeleteSceneTestingTaskResponse:
        """
        @summary 删除场景化测试任务
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSceneTestingTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteSceneTestingTask',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/sceneTestingTask/{OpenApiUtilClient.get_encode_param(task_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.DeleteSceneTestingTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_scene_testing_task_with_options_async(
        self,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.DeleteSceneTestingTaskResponse:
        """
        @summary 删除场景化测试任务
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSceneTestingTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteSceneTestingTask',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/sceneTestingTask/{OpenApiUtilClient.get_encode_param(task_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.DeleteSceneTestingTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_scene_testing_task(
        self,
        task_id: str,
    ) -> ia_cservice_20210806_models.DeleteSceneTestingTaskResponse:
        """
        @summary 删除场景化测试任务
        
        @return: DeleteSceneTestingTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_scene_testing_task_with_options(task_id, headers, runtime)

    async def delete_scene_testing_task_async(
        self,
        task_id: str,
    ) -> ia_cservice_20210806_models.DeleteSceneTestingTaskResponse:
        """
        @summary 删除场景化测试任务
        
        @return: DeleteSceneTestingTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_scene_testing_task_with_options_async(task_id, headers, runtime)

    def delete_task_with_options(
        self,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.DeleteTaskResponse:
        """
        @summary 删除任务
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteTask',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/tasks/{OpenApiUtilClient.get_encode_param(task_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.DeleteTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_task_with_options_async(
        self,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.DeleteTaskResponse:
        """
        @summary 删除任务
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteTask',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/tasks/{OpenApiUtilClient.get_encode_param(task_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.DeleteTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_task(
        self,
        task_id: str,
    ) -> ia_cservice_20210806_models.DeleteTaskResponse:
        """
        @summary 删除任务
        
        @return: DeleteTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_task_with_options(task_id, headers, runtime)

    async def delete_task_async(
        self,
        task_id: str,
    ) -> ia_cservice_20210806_models.DeleteTaskResponse:
        """
        @summary 删除任务
        
        @return: DeleteTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_task_with_options_async(task_id, headers, runtime)

    def detach_rabbitmq_publisher_with_options(
        self,
        publisher_id: str,
        request: ia_cservice_20210806_models.DetachRabbitmqPublisherRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.DetachRabbitmqPublisherResponse:
        """
        @summary 将消息发布者从任务上卸载
        
        @param request: DetachRabbitmqPublisherRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachRabbitmqPublisherResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['taskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetachRabbitmqPublisher',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/publishers/{OpenApiUtilClient.get_encode_param(publisher_id)}/detach',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.DetachRabbitmqPublisherResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_rabbitmq_publisher_with_options_async(
        self,
        publisher_id: str,
        request: ia_cservice_20210806_models.DetachRabbitmqPublisherRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.DetachRabbitmqPublisherResponse:
        """
        @summary 将消息发布者从任务上卸载
        
        @param request: DetachRabbitmqPublisherRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachRabbitmqPublisherResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['taskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetachRabbitmqPublisher',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/publishers/{OpenApiUtilClient.get_encode_param(publisher_id)}/detach',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.DetachRabbitmqPublisherResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_rabbitmq_publisher(
        self,
        publisher_id: str,
        request: ia_cservice_20210806_models.DetachRabbitmqPublisherRequest,
    ) -> ia_cservice_20210806_models.DetachRabbitmqPublisherResponse:
        """
        @summary 将消息发布者从任务上卸载
        
        @param request: DetachRabbitmqPublisherRequest
        @return: DetachRabbitmqPublisherResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.detach_rabbitmq_publisher_with_options(publisher_id, request, headers, runtime)

    async def detach_rabbitmq_publisher_async(
        self,
        publisher_id: str,
        request: ia_cservice_20210806_models.DetachRabbitmqPublisherRequest,
    ) -> ia_cservice_20210806_models.DetachRabbitmqPublisherResponse:
        """
        @summary 将消息发布者从任务上卸载
        
        @param request: DetachRabbitmqPublisherRequest
        @return: DetachRabbitmqPublisherResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.detach_rabbitmq_publisher_with_options_async(publisher_id, request, headers, runtime)

    def dissociate_group_with_options(
        self,
        project_id: str,
        group_id: str,
        request: ia_cservice_20210806_models.DissociateGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.DissociateGroupResponse:
        """
        @summary 取消关联分组
        
        @param request: DissociateGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DissociateGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.resource_ids):
            body['resourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_type):
            body['resourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DissociateGroup',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/group/{OpenApiUtilClient.get_encode_param(group_id)}/dissociate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.DissociateGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def dissociate_group_with_options_async(
        self,
        project_id: str,
        group_id: str,
        request: ia_cservice_20210806_models.DissociateGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.DissociateGroupResponse:
        """
        @summary 取消关联分组
        
        @param request: DissociateGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DissociateGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.resource_ids):
            body['resourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_type):
            body['resourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DissociateGroup',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/group/{OpenApiUtilClient.get_encode_param(group_id)}/dissociate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.DissociateGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dissociate_group(
        self,
        project_id: str,
        group_id: str,
        request: ia_cservice_20210806_models.DissociateGroupRequest,
    ) -> ia_cservice_20210806_models.DissociateGroupResponse:
        """
        @summary 取消关联分组
        
        @param request: DissociateGroupRequest
        @return: DissociateGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.dissociate_group_with_options(project_id, group_id, request, headers, runtime)

    async def dissociate_group_async(
        self,
        project_id: str,
        group_id: str,
        request: ia_cservice_20210806_models.DissociateGroupRequest,
    ) -> ia_cservice_20210806_models.DissociateGroupResponse:
        """
        @summary 取消关联分组
        
        @param request: DissociateGroupRequest
        @return: DissociateGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.dissociate_group_with_options_async(project_id, group_id, request, headers, runtime)

    def dissociate_parameter_set_with_options(
        self,
        request: ia_cservice_20210806_models.DissociateParameterSetRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.DissociateParameterSetResponse:
        """
        @summary 解除参数集关联资源关系
        
        @param request: DissociateParameterSetRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DissociateParameterSetResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.parameter_set_ids):
            body['parameterSetIds'] = request.parameter_set_ids
        if not UtilClient.is_unset(request.resource_id):
            body['resourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            body['resourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DissociateParameterSet',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/parameterSets/operations/dissociate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.DissociateParameterSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def dissociate_parameter_set_with_options_async(
        self,
        request: ia_cservice_20210806_models.DissociateParameterSetRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.DissociateParameterSetResponse:
        """
        @summary 解除参数集关联资源关系
        
        @param request: DissociateParameterSetRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DissociateParameterSetResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.parameter_set_ids):
            body['parameterSetIds'] = request.parameter_set_ids
        if not UtilClient.is_unset(request.resource_id):
            body['resourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            body['resourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DissociateParameterSet',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/parameterSets/operations/dissociate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.DissociateParameterSetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dissociate_parameter_set(
        self,
        request: ia_cservice_20210806_models.DissociateParameterSetRequest,
    ) -> ia_cservice_20210806_models.DissociateParameterSetResponse:
        """
        @summary 解除参数集关联资源关系
        
        @param request: DissociateParameterSetRequest
        @return: DissociateParameterSetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.dissociate_parameter_set_with_options(request, headers, runtime)

    async def dissociate_parameter_set_async(
        self,
        request: ia_cservice_20210806_models.DissociateParameterSetRequest,
    ) -> ia_cservice_20210806_models.DissociateParameterSetResponse:
        """
        @summary 解除参数集关联资源关系
        
        @param request: DissociateParameterSetRequest
        @return: DissociateParameterSetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.dissociate_parameter_set_with_options_async(request, headers, runtime)

    def execute_ram_policy_export_task_with_options(
        self,
        ram_policy_export_task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ExecuteRamPolicyExportTaskResponse:
        """
        @summary 执行RAM策略导出任务
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteRamPolicyExportTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ExecuteRamPolicyExportTask',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/ramPolicyExportTasks/{OpenApiUtilClient.get_encode_param(ram_policy_export_task_id)}/execute',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ExecuteRamPolicyExportTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_ram_policy_export_task_with_options_async(
        self,
        ram_policy_export_task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ExecuteRamPolicyExportTaskResponse:
        """
        @summary 执行RAM策略导出任务
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteRamPolicyExportTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ExecuteRamPolicyExportTask',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/ramPolicyExportTasks/{OpenApiUtilClient.get_encode_param(ram_policy_export_task_id)}/execute',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ExecuteRamPolicyExportTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_ram_policy_export_task(
        self,
        ram_policy_export_task_id: str,
    ) -> ia_cservice_20210806_models.ExecuteRamPolicyExportTaskResponse:
        """
        @summary 执行RAM策略导出任务
        
        @return: ExecuteRamPolicyExportTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.execute_ram_policy_export_task_with_options(ram_policy_export_task_id, headers, runtime)

    async def execute_ram_policy_export_task_async(
        self,
        ram_policy_export_task_id: str,
    ) -> ia_cservice_20210806_models.ExecuteRamPolicyExportTaskResponse:
        """
        @summary 执行RAM策略导出任务
        
        @return: ExecuteRamPolicyExportTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.execute_ram_policy_export_task_with_options_async(ram_policy_export_task_id, headers, runtime)

    def execute_resource_export_task_with_options(
        self,
        export_task_id: str,
        request: ia_cservice_20210806_models.ExecuteResourceExportTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ExecuteResourceExportTaskResponse:
        """
        @summary 执行资源导出任务
        
        @param request: ExecuteResourceExportTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteResourceExportTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.ram_role):
            body['ramRole'] = request.ram_role
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteResourceExportTask',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/exportTasks/execute/{OpenApiUtilClient.get_encode_param(export_task_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ExecuteResourceExportTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_resource_export_task_with_options_async(
        self,
        export_task_id: str,
        request: ia_cservice_20210806_models.ExecuteResourceExportTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ExecuteResourceExportTaskResponse:
        """
        @summary 执行资源导出任务
        
        @param request: ExecuteResourceExportTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteResourceExportTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.ram_role):
            body['ramRole'] = request.ram_role
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteResourceExportTask',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/exportTasks/execute/{OpenApiUtilClient.get_encode_param(export_task_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ExecuteResourceExportTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_resource_export_task(
        self,
        export_task_id: str,
        request: ia_cservice_20210806_models.ExecuteResourceExportTaskRequest,
    ) -> ia_cservice_20210806_models.ExecuteResourceExportTaskResponse:
        """
        @summary 执行资源导出任务
        
        @param request: ExecuteResourceExportTaskRequest
        @return: ExecuteResourceExportTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.execute_resource_export_task_with_options(export_task_id, request, headers, runtime)

    async def execute_resource_export_task_async(
        self,
        export_task_id: str,
        request: ia_cservice_20210806_models.ExecuteResourceExportTaskRequest,
    ) -> ia_cservice_20210806_models.ExecuteResourceExportTaskResponse:
        """
        @summary 执行资源导出任务
        
        @param request: ExecuteResourceExportTaskRequest
        @return: ExecuteResourceExportTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.execute_resource_export_task_with_options_async(export_task_id, request, headers, runtime)

    def get_explorer_task_with_options(
        self,
        explorer_task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.GetExplorerTaskResponse:
        """
        @summary 查询Explorer任务详情
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetExplorerTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetExplorerTask',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/explorerTask/{OpenApiUtilClient.get_encode_param(explorer_task_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GetExplorerTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_explorer_task_with_options_async(
        self,
        explorer_task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.GetExplorerTaskResponse:
        """
        @summary 查询Explorer任务详情
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetExplorerTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetExplorerTask',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/explorerTask/{OpenApiUtilClient.get_encode_param(explorer_task_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GetExplorerTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_explorer_task(
        self,
        explorer_task_id: str,
    ) -> ia_cservice_20210806_models.GetExplorerTaskResponse:
        """
        @summary 查询Explorer任务详情
        
        @return: GetExplorerTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_explorer_task_with_options(explorer_task_id, headers, runtime)

    async def get_explorer_task_async(
        self,
        explorer_task_id: str,
    ) -> ia_cservice_20210806_models.GetExplorerTaskResponse:
        """
        @summary 查询Explorer任务详情
        
        @return: GetExplorerTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_explorer_task_with_options_async(explorer_task_id, headers, runtime)

    def get_group_with_options(
        self,
        group_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.GetGroupResponse:
        """
        @summary 查询分组
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetGroupResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetGroup',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/group/{OpenApiUtilClient.get_encode_param(group_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GetGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_group_with_options_async(
        self,
        group_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.GetGroupResponse:
        """
        @summary 查询分组
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetGroupResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetGroup',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/group/{OpenApiUtilClient.get_encode_param(group_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GetGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_group(
        self,
        group_id: str,
    ) -> ia_cservice_20210806_models.GetGroupResponse:
        """
        @summary 查询分组
        
        @return: GetGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_group_with_options(group_id, headers, runtime)

    async def get_group_async(
        self,
        group_id: str,
    ) -> ia_cservice_20210806_models.GetGroupResponse:
        """
        @summary 查询分组
        
        @return: GetGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_group_with_options_async(group_id, headers, runtime)

    def get_job_with_options(
        self,
        task_id: str,
        job_id: str,
        request: ia_cservice_20210806_models.GetJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.GetJobResponse:
        """
        @summary 作业详情
        
        @param request: GetJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_type):
            query['taskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJob',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/tasks/{OpenApiUtilClient.get_encode_param(task_id)}/jobs/{OpenApiUtilClient.get_encode_param(job_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GetJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_job_with_options_async(
        self,
        task_id: str,
        job_id: str,
        request: ia_cservice_20210806_models.GetJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.GetJobResponse:
        """
        @summary 作业详情
        
        @param request: GetJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_type):
            query['taskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJob',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/tasks/{OpenApiUtilClient.get_encode_param(task_id)}/jobs/{OpenApiUtilClient.get_encode_param(job_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GetJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_job(
        self,
        task_id: str,
        job_id: str,
        request: ia_cservice_20210806_models.GetJobRequest,
    ) -> ia_cservice_20210806_models.GetJobResponse:
        """
        @summary 作业详情
        
        @param request: GetJobRequest
        @return: GetJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_job_with_options(task_id, job_id, request, headers, runtime)

    async def get_job_async(
        self,
        task_id: str,
        job_id: str,
        request: ia_cservice_20210806_models.GetJobRequest,
    ) -> ia_cservice_20210806_models.GetJobResponse:
        """
        @summary 作业详情
        
        @param request: GetJobRequest
        @return: GetJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_job_with_options_async(task_id, job_id, request, headers, runtime)

    def get_module_with_options(
        self,
        module_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.GetModuleResponse:
        """
        @summary 获取模版详情
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetModuleResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetModule',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/modules/{OpenApiUtilClient.get_encode_param(module_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GetModuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_module_with_options_async(
        self,
        module_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.GetModuleResponse:
        """
        @summary 获取模版详情
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetModuleResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetModule',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/modules/{OpenApiUtilClient.get_encode_param(module_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GetModuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_module(
        self,
        module_id: str,
    ) -> ia_cservice_20210806_models.GetModuleResponse:
        """
        @summary 获取模版详情
        
        @return: GetModuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_module_with_options(module_id, headers, runtime)

    async def get_module_async(
        self,
        module_id: str,
    ) -> ia_cservice_20210806_models.GetModuleResponse:
        """
        @summary 获取模版详情
        
        @return: GetModuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_module_with_options_async(module_id, headers, runtime)

    def get_module_version_with_options(
        self,
        module_id: str,
        module_version: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.GetModuleVersionResponse:
        """
        @summary 模版版本详情
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetModuleVersionResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetModuleVersion',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/modules/{OpenApiUtilClient.get_encode_param(module_id)}/versions/{OpenApiUtilClient.get_encode_param(module_version)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GetModuleVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_module_version_with_options_async(
        self,
        module_id: str,
        module_version: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.GetModuleVersionResponse:
        """
        @summary 模版版本详情
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetModuleVersionResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetModuleVersion',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/modules/{OpenApiUtilClient.get_encode_param(module_id)}/versions/{OpenApiUtilClient.get_encode_param(module_version)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GetModuleVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_module_version(
        self,
        module_id: str,
        module_version: str,
    ) -> ia_cservice_20210806_models.GetModuleVersionResponse:
        """
        @summary 模版版本详情
        
        @return: GetModuleVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_module_version_with_options(module_id, module_version, headers, runtime)

    async def get_module_version_async(
        self,
        module_id: str,
        module_version: str,
    ) -> ia_cservice_20210806_models.GetModuleVersionResponse:
        """
        @summary 模版版本详情
        
        @return: GetModuleVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_module_version_with_options_async(module_id, module_version, headers, runtime)

    def get_parameter_set_with_options(
        self,
        parameter_set_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.GetParameterSetResponse:
        """
        @summary 参数集详情
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetParameterSetResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetParameterSet',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/parameterSets/{OpenApiUtilClient.get_encode_param(parameter_set_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GetParameterSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_parameter_set_with_options_async(
        self,
        parameter_set_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.GetParameterSetResponse:
        """
        @summary 参数集详情
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetParameterSetResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetParameterSet',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/parameterSets/{OpenApiUtilClient.get_encode_param(parameter_set_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GetParameterSetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_parameter_set(
        self,
        parameter_set_id: str,
    ) -> ia_cservice_20210806_models.GetParameterSetResponse:
        """
        @summary 参数集详情
        
        @return: GetParameterSetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_parameter_set_with_options(parameter_set_id, headers, runtime)

    async def get_parameter_set_async(
        self,
        parameter_set_id: str,
    ) -> ia_cservice_20210806_models.GetParameterSetResponse:
        """
        @summary 参数集详情
        
        @return: GetParameterSetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_parameter_set_with_options_async(parameter_set_id, headers, runtime)

    def get_project_with_options(
        self,
        project_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.GetProjectResponse:
        """
        @summary 查询项目
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetProjectResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetProject',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/project/{OpenApiUtilClient.get_encode_param(project_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GetProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_project_with_options_async(
        self,
        project_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.GetProjectResponse:
        """
        @summary 查询项目
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetProjectResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetProject',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/project/{OpenApiUtilClient.get_encode_param(project_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GetProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_project(
        self,
        project_id: str,
    ) -> ia_cservice_20210806_models.GetProjectResponse:
        """
        @summary 查询项目
        
        @return: GetProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_project_with_options(project_id, headers, runtime)

    async def get_project_async(
        self,
        project_id: str,
    ) -> ia_cservice_20210806_models.GetProjectResponse:
        """
        @summary 查询项目
        
        @return: GetProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_project_with_options_async(project_id, headers, runtime)

    def get_project_build_context_with_options(
        self,
        project_id: str,
        project_build_id: str,
        request: ia_cservice_20210806_models.GetProjectBuildContextRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.GetProjectBuildContextResponse:
        """
        @summary 项目批次概览
        
        @param request: GetProjectBuildContextRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetProjectBuildContextResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.is_pass_assert_check):
            query['isPassAssertCheck'] = request.is_pass_assert_check
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProjectBuildContext',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/project/{OpenApiUtilClient.get_encode_param(project_id)}/build/{OpenApiUtilClient.get_encode_param(project_build_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GetProjectBuildContextResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_project_build_context_with_options_async(
        self,
        project_id: str,
        project_build_id: str,
        request: ia_cservice_20210806_models.GetProjectBuildContextRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.GetProjectBuildContextResponse:
        """
        @summary 项目批次概览
        
        @param request: GetProjectBuildContextRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetProjectBuildContextResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.is_pass_assert_check):
            query['isPassAssertCheck'] = request.is_pass_assert_check
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProjectBuildContext',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/project/{OpenApiUtilClient.get_encode_param(project_id)}/build/{OpenApiUtilClient.get_encode_param(project_build_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GetProjectBuildContextResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_project_build_context(
        self,
        project_id: str,
        project_build_id: str,
        request: ia_cservice_20210806_models.GetProjectBuildContextRequest,
    ) -> ia_cservice_20210806_models.GetProjectBuildContextResponse:
        """
        @summary 项目批次概览
        
        @param request: GetProjectBuildContextRequest
        @return: GetProjectBuildContextResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_project_build_context_with_options(project_id, project_build_id, request, headers, runtime)

    async def get_project_build_context_async(
        self,
        project_id: str,
        project_build_id: str,
        request: ia_cservice_20210806_models.GetProjectBuildContextRequest,
    ) -> ia_cservice_20210806_models.GetProjectBuildContextResponse:
        """
        @summary 项目批次概览
        
        @param request: GetProjectBuildContextRequest
        @return: GetProjectBuildContextResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_project_build_context_with_options_async(project_id, project_build_id, request, headers, runtime)

    def get_rabbitmq_publisher_with_options(
        self,
        publisher_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.GetRabbitmqPublisherResponse:
        """
        @summary 获取消息发布者详情
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRabbitmqPublisherResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetRabbitmqPublisher',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/publishers/{OpenApiUtilClient.get_encode_param(publisher_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GetRabbitmqPublisherResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_rabbitmq_publisher_with_options_async(
        self,
        publisher_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.GetRabbitmqPublisherResponse:
        """
        @summary 获取消息发布者详情
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRabbitmqPublisherResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetRabbitmqPublisher',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/publishers/{OpenApiUtilClient.get_encode_param(publisher_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GetRabbitmqPublisherResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_rabbitmq_publisher(
        self,
        publisher_id: str,
    ) -> ia_cservice_20210806_models.GetRabbitmqPublisherResponse:
        """
        @summary 获取消息发布者详情
        
        @return: GetRabbitmqPublisherResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_rabbitmq_publisher_with_options(publisher_id, headers, runtime)

    async def get_rabbitmq_publisher_async(
        self,
        publisher_id: str,
    ) -> ia_cservice_20210806_models.GetRabbitmqPublisherResponse:
        """
        @summary 获取消息发布者详情
        
        @return: GetRabbitmqPublisherResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_rabbitmq_publisher_with_options_async(publisher_id, headers, runtime)

    def get_ram_policy_export_task_with_options(
        self,
        ram_policy_export_task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.GetRamPolicyExportTaskResponse:
        """
        @summary 获取RAM策略导出任务详情
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRamPolicyExportTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetRamPolicyExportTask',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/ramPolicyExportTasks/{OpenApiUtilClient.get_encode_param(ram_policy_export_task_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GetRamPolicyExportTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ram_policy_export_task_with_options_async(
        self,
        ram_policy_export_task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.GetRamPolicyExportTaskResponse:
        """
        @summary 获取RAM策略导出任务详情
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRamPolicyExportTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetRamPolicyExportTask',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/ramPolicyExportTasks/{OpenApiUtilClient.get_encode_param(ram_policy_export_task_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GetRamPolicyExportTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ram_policy_export_task(
        self,
        ram_policy_export_task_id: str,
    ) -> ia_cservice_20210806_models.GetRamPolicyExportTaskResponse:
        """
        @summary 获取RAM策略导出任务详情
        
        @return: GetRamPolicyExportTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_ram_policy_export_task_with_options(ram_policy_export_task_id, headers, runtime)

    async def get_ram_policy_export_task_async(
        self,
        ram_policy_export_task_id: str,
    ) -> ia_cservice_20210806_models.GetRamPolicyExportTaskResponse:
        """
        @summary 获取RAM策略导出任务详情
        
        @return: GetRamPolicyExportTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_ram_policy_export_task_with_options_async(ram_policy_export_task_id, headers, runtime)

    def get_ram_policy_export_task_version_with_options(
        self,
        ram_policy_export_task_id: str,
        export_version: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.GetRamPolicyExportTaskVersionResponse:
        """
        @summary 获取RAM策略导出任务版本详情
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRamPolicyExportTaskVersionResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetRamPolicyExportTaskVersion',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/ramPolicyExportTasks/{OpenApiUtilClient.get_encode_param(ram_policy_export_task_id)}/versions/{OpenApiUtilClient.get_encode_param(export_version)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GetRamPolicyExportTaskVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ram_policy_export_task_version_with_options_async(
        self,
        ram_policy_export_task_id: str,
        export_version: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.GetRamPolicyExportTaskVersionResponse:
        """
        @summary 获取RAM策略导出任务版本详情
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRamPolicyExportTaskVersionResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetRamPolicyExportTaskVersion',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/ramPolicyExportTasks/{OpenApiUtilClient.get_encode_param(ram_policy_export_task_id)}/versions/{OpenApiUtilClient.get_encode_param(export_version)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GetRamPolicyExportTaskVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ram_policy_export_task_version(
        self,
        ram_policy_export_task_id: str,
        export_version: str,
    ) -> ia_cservice_20210806_models.GetRamPolicyExportTaskVersionResponse:
        """
        @summary 获取RAM策略导出任务版本详情
        
        @return: GetRamPolicyExportTaskVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_ram_policy_export_task_version_with_options(ram_policy_export_task_id, export_version, headers, runtime)

    async def get_ram_policy_export_task_version_async(
        self,
        ram_policy_export_task_id: str,
        export_version: str,
    ) -> ia_cservice_20210806_models.GetRamPolicyExportTaskVersionResponse:
        """
        @summary 获取RAM策略导出任务版本详情
        
        @return: GetRamPolicyExportTaskVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_ram_policy_export_task_version_with_options_async(ram_policy_export_task_id, export_version, headers, runtime)

    def get_resource_export_task_with_options(
        self,
        export_task_id: str,
        request: ia_cservice_20210806_models.GetResourceExportTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.GetResourceExportTaskResponse:
        """
        @summary 查询导出任务详情
        
        @param request: GetResourceExportTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetResourceExportTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.export_version):
            query['exportVersion'] = request.export_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceExportTask',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/exportTasks/{OpenApiUtilClient.get_encode_param(export_task_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GetResourceExportTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_export_task_with_options_async(
        self,
        export_task_id: str,
        request: ia_cservice_20210806_models.GetResourceExportTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.GetResourceExportTaskResponse:
        """
        @summary 查询导出任务详情
        
        @param request: GetResourceExportTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetResourceExportTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.export_version):
            query['exportVersion'] = request.export_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceExportTask',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/exportTasks/{OpenApiUtilClient.get_encode_param(export_task_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GetResourceExportTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_export_task(
        self,
        export_task_id: str,
        request: ia_cservice_20210806_models.GetResourceExportTaskRequest,
    ) -> ia_cservice_20210806_models.GetResourceExportTaskResponse:
        """
        @summary 查询导出任务详情
        
        @param request: GetResourceExportTaskRequest
        @return: GetResourceExportTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_resource_export_task_with_options(export_task_id, request, headers, runtime)

    async def get_resource_export_task_async(
        self,
        export_task_id: str,
        request: ia_cservice_20210806_models.GetResourceExportTaskRequest,
    ) -> ia_cservice_20210806_models.GetResourceExportTaskResponse:
        """
        @summary 查询导出任务详情
        
        @param request: GetResourceExportTaskRequest
        @return: GetResourceExportTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_resource_export_task_with_options_async(export_task_id, request, headers, runtime)

    def get_task_with_options(
        self,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.GetTaskResponse:
        """
        @summary 查询任务详情
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTask',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/tasks/{OpenApiUtilClient.get_encode_param(task_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GetTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_task_with_options_async(
        self,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.GetTaskResponse:
        """
        @summary 查询任务详情
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTask',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/tasks/{OpenApiUtilClient.get_encode_param(task_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GetTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_task(
        self,
        task_id: str,
    ) -> ia_cservice_20210806_models.GetTaskResponse:
        """
        @summary 查询任务详情
        
        @return: GetTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_task_with_options(task_id, headers, runtime)

    async def get_task_async(
        self,
        task_id: str,
    ) -> ia_cservice_20210806_models.GetTaskResponse:
        """
        @summary 查询任务详情
        
        @return: GetTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_task_with_options_async(task_id, headers, runtime)

    def get_task_policy_with_options(
        self,
        group_id: str,
        request: ia_cservice_20210806_models.GetTaskPolicyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.GetTaskPolicyResponse:
        """
        @summary 查询分组优先级详情
        
        @param request: GetTaskPolicyRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTaskPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTaskPolicy',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/group/task/policy/{OpenApiUtilClient.get_encode_param(group_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GetTaskPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_task_policy_with_options_async(
        self,
        group_id: str,
        request: ia_cservice_20210806_models.GetTaskPolicyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.GetTaskPolicyResponse:
        """
        @summary 查询分组优先级详情
        
        @param request: GetTaskPolicyRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTaskPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTaskPolicy',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/group/task/policy/{OpenApiUtilClient.get_encode_param(group_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GetTaskPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_task_policy(
        self,
        group_id: str,
        request: ia_cservice_20210806_models.GetTaskPolicyRequest,
    ) -> ia_cservice_20210806_models.GetTaskPolicyResponse:
        """
        @summary 查询分组优先级详情
        
        @param request: GetTaskPolicyRequest
        @return: GetTaskPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_task_policy_with_options(group_id, request, headers, runtime)

    async def get_task_policy_async(
        self,
        group_id: str,
        request: ia_cservice_20210806_models.GetTaskPolicyRequest,
    ) -> ia_cservice_20210806_models.GetTaskPolicyResponse:
        """
        @summary 查询分组优先级详情
        
        @param request: GetTaskPolicyRequest
        @return: GetTaskPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_task_policy_with_options_async(group_id, request, headers, runtime)

    def list_authorizations_with_options(
        self,
        request: ia_cservice_20210806_models.ListAuthorizationsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListAuthorizationsResponse:
        """
        @summary 获取共享列表
        
        @param request: ListAuthorizationsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAuthorizationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authorization_id):
            query['authorizationId'] = request.authorization_id
        if not UtilClient.is_unset(request.authorization_type):
            query['authorizationType'] = request.authorization_type
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAuthorizations',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/authorizations',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListAuthorizationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_authorizations_with_options_async(
        self,
        request: ia_cservice_20210806_models.ListAuthorizationsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListAuthorizationsResponse:
        """
        @summary 获取共享列表
        
        @param request: ListAuthorizationsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAuthorizationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authorization_id):
            query['authorizationId'] = request.authorization_id
        if not UtilClient.is_unset(request.authorization_type):
            query['authorizationType'] = request.authorization_type
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAuthorizations',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/authorizations',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListAuthorizationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_authorizations(
        self,
        request: ia_cservice_20210806_models.ListAuthorizationsRequest,
    ) -> ia_cservice_20210806_models.ListAuthorizationsResponse:
        """
        @summary 获取共享列表
        
        @param request: ListAuthorizationsRequest
        @return: ListAuthorizationsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_authorizations_with_options(request, headers, runtime)

    async def list_authorizations_async(
        self,
        request: ia_cservice_20210806_models.ListAuthorizationsRequest,
    ) -> ia_cservice_20210806_models.ListAuthorizationsResponse:
        """
        @summary 获取共享列表
        
        @param request: ListAuthorizationsRequest
        @return: ListAuthorizationsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_authorizations_with_options_async(request, headers, runtime)

    def list_available_terraform_versions_with_options(
        self,
        request: ia_cservice_20210806_models.ListAvailableTerraformVersionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListAvailableTerraformVersionsResponse:
        """
        @summary terraform版本
        
        @param request: ListAvailableTerraformVersionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAvailableTerraformVersionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_word):
            query['keyWord'] = request.key_word
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAvailableTerraformVersions',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/version/terraform',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListAvailableTerraformVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_available_terraform_versions_with_options_async(
        self,
        request: ia_cservice_20210806_models.ListAvailableTerraformVersionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListAvailableTerraformVersionsResponse:
        """
        @summary terraform版本
        
        @param request: ListAvailableTerraformVersionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAvailableTerraformVersionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_word):
            query['keyWord'] = request.key_word
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAvailableTerraformVersions',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/version/terraform',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListAvailableTerraformVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_available_terraform_versions(
        self,
        request: ia_cservice_20210806_models.ListAvailableTerraformVersionsRequest,
    ) -> ia_cservice_20210806_models.ListAvailableTerraformVersionsResponse:
        """
        @summary terraform版本
        
        @param request: ListAvailableTerraformVersionsRequest
        @return: ListAvailableTerraformVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_available_terraform_versions_with_options(request, headers, runtime)

    async def list_available_terraform_versions_async(
        self,
        request: ia_cservice_20210806_models.ListAvailableTerraformVersionsRequest,
    ) -> ia_cservice_20210806_models.ListAvailableTerraformVersionsResponse:
        """
        @summary terraform版本
        
        @param request: ListAvailableTerraformVersionsRequest
        @return: ListAvailableTerraformVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_available_terraform_versions_with_options_async(request, headers, runtime)

    def list_explorer_tasks_with_options(
        self,
        explorer_task_id: str,
        request: ia_cservice_20210806_models.ListExplorerTasksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListExplorerTasksResponse:
        """
        @summary 列举Explorer任务
        
        @param request: ListExplorerTasksRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListExplorerTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.max_result):
            query['maxResult'] = request.max_result
        if not UtilClient.is_unset(request.module_id):
            query['moduleId'] = request.module_id
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListExplorerTasks',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/explorerTask',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListExplorerTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_explorer_tasks_with_options_async(
        self,
        explorer_task_id: str,
        request: ia_cservice_20210806_models.ListExplorerTasksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListExplorerTasksResponse:
        """
        @summary 列举Explorer任务
        
        @param request: ListExplorerTasksRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListExplorerTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.max_result):
            query['maxResult'] = request.max_result
        if not UtilClient.is_unset(request.module_id):
            query['moduleId'] = request.module_id
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListExplorerTasks',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/explorerTask',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListExplorerTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_explorer_tasks(
        self,
        explorer_task_id: str,
        request: ia_cservice_20210806_models.ListExplorerTasksRequest,
    ) -> ia_cservice_20210806_models.ListExplorerTasksResponse:
        """
        @summary 列举Explorer任务
        
        @param request: ListExplorerTasksRequest
        @return: ListExplorerTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_explorer_tasks_with_options(explorer_task_id, request, headers, runtime)

    async def list_explorer_tasks_async(
        self,
        explorer_task_id: str,
        request: ia_cservice_20210806_models.ListExplorerTasksRequest,
    ) -> ia_cservice_20210806_models.ListExplorerTasksResponse:
        """
        @summary 列举Explorer任务
        
        @param request: ListExplorerTasksRequest
        @return: ListExplorerTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_explorer_tasks_with_options_async(explorer_task_id, request, headers, runtime)

    def list_group_with_options(
        self,
        tmp_req: ia_cservice_20210806_models.ListGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListGroupResponse:
        """
        @summary 查询分组列表
        
        @param tmp_req: ListGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListGroupResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ia_cservice_20210806_models.ListGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'tag', 'json')
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['projectId'] = request.project_id
        if not UtilClient.is_unset(request.tag_shrink):
            query['tag'] = request.tag_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGroup',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/group',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_group_with_options_async(
        self,
        tmp_req: ia_cservice_20210806_models.ListGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListGroupResponse:
        """
        @summary 查询分组列表
        
        @param tmp_req: ListGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListGroupResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ia_cservice_20210806_models.ListGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'tag', 'json')
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['projectId'] = request.project_id
        if not UtilClient.is_unset(request.tag_shrink):
            query['tag'] = request.tag_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGroup',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/group',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_group(
        self,
        request: ia_cservice_20210806_models.ListGroupRequest,
    ) -> ia_cservice_20210806_models.ListGroupResponse:
        """
        @summary 查询分组列表
        
        @param request: ListGroupRequest
        @return: ListGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_group_with_options(request, headers, runtime)

    async def list_group_async(
        self,
        request: ia_cservice_20210806_models.ListGroupRequest,
    ) -> ia_cservice_20210806_models.ListGroupResponse:
        """
        @summary 查询分组列表
        
        @param request: ListGroupRequest
        @return: ListGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_group_with_options_async(request, headers, runtime)

    def list_jobs_with_options(
        self,
        task_id: str,
        request: ia_cservice_20210806_models.ListJobsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListJobsResponse:
        """
        @summary 作业列表
        
        @param request: ListJobsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        if not UtilClient.is_unset(request.task_type):
            query['taskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobs',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/tasks/{OpenApiUtilClient.get_encode_param(task_id)}/jobs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_jobs_with_options_async(
        self,
        task_id: str,
        request: ia_cservice_20210806_models.ListJobsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListJobsResponse:
        """
        @summary 作业列表
        
        @param request: ListJobsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        if not UtilClient.is_unset(request.task_type):
            query['taskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobs',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/tasks/{OpenApiUtilClient.get_encode_param(task_id)}/jobs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_jobs(
        self,
        task_id: str,
        request: ia_cservice_20210806_models.ListJobsRequest,
    ) -> ia_cservice_20210806_models.ListJobsResponse:
        """
        @summary 作业列表
        
        @param request: ListJobsRequest
        @return: ListJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_jobs_with_options(task_id, request, headers, runtime)

    async def list_jobs_async(
        self,
        task_id: str,
        request: ia_cservice_20210806_models.ListJobsRequest,
    ) -> ia_cservice_20210806_models.ListJobsResponse:
        """
        @summary 作业列表
        
        @param request: ListJobsRequest
        @return: ListJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_jobs_with_options_async(task_id, request, headers, runtime)

    def list_module_version_with_options(
        self,
        module_id: str,
        request: ia_cservice_20210806_models.ListModuleVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListModuleVersionResponse:
        """
        @summary 模版版本列表
        
        @param request: ListModuleVersionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListModuleVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListModuleVersion',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/modules/{OpenApiUtilClient.get_encode_param(module_id)}/versions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListModuleVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_module_version_with_options_async(
        self,
        module_id: str,
        request: ia_cservice_20210806_models.ListModuleVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListModuleVersionResponse:
        """
        @summary 模版版本列表
        
        @param request: ListModuleVersionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListModuleVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListModuleVersion',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/modules/{OpenApiUtilClient.get_encode_param(module_id)}/versions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListModuleVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_module_version(
        self,
        module_id: str,
        request: ia_cservice_20210806_models.ListModuleVersionRequest,
    ) -> ia_cservice_20210806_models.ListModuleVersionResponse:
        """
        @summary 模版版本列表
        
        @param request: ListModuleVersionRequest
        @return: ListModuleVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_module_version_with_options(module_id, request, headers, runtime)

    async def list_module_version_async(
        self,
        module_id: str,
        request: ia_cservice_20210806_models.ListModuleVersionRequest,
    ) -> ia_cservice_20210806_models.ListModuleVersionResponse:
        """
        @summary 模版版本列表
        
        @param request: ListModuleVersionRequest
        @return: ListModuleVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_module_version_with_options_async(module_id, request, headers, runtime)

    def list_modules_with_options(
        self,
        tmp_req: ia_cservice_20210806_models.ListModulesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListModulesResponse:
        """
        @summary 列举模版
        
        @param tmp_req: ListModulesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListModulesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ia_cservice_20210806_models.ListModulesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.exclude_module_ids):
            request.exclude_module_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.exclude_module_ids, 'excludeModuleIds', 'simple')
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'tag', 'json')
        query = {}
        if not UtilClient.is_unset(request.exclude_module_ids_shrink):
            query['excludeModuleIds'] = request.exclude_module_ids_shrink
        if not UtilClient.is_unset(request.group_id):
            query['groupId'] = request.group_id
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['projectId'] = request.project_id
        if not UtilClient.is_unset(request.tag_shrink):
            query['tag'] = request.tag_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListModules',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/modules',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListModulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_modules_with_options_async(
        self,
        tmp_req: ia_cservice_20210806_models.ListModulesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListModulesResponse:
        """
        @summary 列举模版
        
        @param tmp_req: ListModulesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListModulesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ia_cservice_20210806_models.ListModulesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.exclude_module_ids):
            request.exclude_module_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.exclude_module_ids, 'excludeModuleIds', 'simple')
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'tag', 'json')
        query = {}
        if not UtilClient.is_unset(request.exclude_module_ids_shrink):
            query['excludeModuleIds'] = request.exclude_module_ids_shrink
        if not UtilClient.is_unset(request.group_id):
            query['groupId'] = request.group_id
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['projectId'] = request.project_id
        if not UtilClient.is_unset(request.tag_shrink):
            query['tag'] = request.tag_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListModules',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/modules',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListModulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_modules(
        self,
        request: ia_cservice_20210806_models.ListModulesRequest,
    ) -> ia_cservice_20210806_models.ListModulesResponse:
        """
        @summary 列举模版
        
        @param request: ListModulesRequest
        @return: ListModulesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_modules_with_options(request, headers, runtime)

    async def list_modules_async(
        self,
        request: ia_cservice_20210806_models.ListModulesRequest,
    ) -> ia_cservice_20210806_models.ListModulesResponse:
        """
        @summary 列举模版
        
        @param request: ListModulesRequest
        @return: ListModulesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_modules_with_options_async(request, headers, runtime)

    def list_parameter_set_relation_with_options(
        self,
        request: ia_cservice_20210806_models.ListParameterSetRelationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListParameterSetRelationResponse:
        """
        @summary 关联到资源的参数集列表
        
        @param request: ListParameterSetRelationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListParameterSetRelationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_id):
            query['resourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['resourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListParameterSetRelation',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/parameterSets/operations/relation',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListParameterSetRelationResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_parameter_set_relation_with_options_async(
        self,
        request: ia_cservice_20210806_models.ListParameterSetRelationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListParameterSetRelationResponse:
        """
        @summary 关联到资源的参数集列表
        
        @param request: ListParameterSetRelationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListParameterSetRelationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_id):
            query['resourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['resourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListParameterSetRelation',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/parameterSets/operations/relation',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListParameterSetRelationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_parameter_set_relation(
        self,
        request: ia_cservice_20210806_models.ListParameterSetRelationRequest,
    ) -> ia_cservice_20210806_models.ListParameterSetRelationResponse:
        """
        @summary 关联到资源的参数集列表
        
        @param request: ListParameterSetRelationRequest
        @return: ListParameterSetRelationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_parameter_set_relation_with_options(request, headers, runtime)

    async def list_parameter_set_relation_async(
        self,
        request: ia_cservice_20210806_models.ListParameterSetRelationRequest,
    ) -> ia_cservice_20210806_models.ListParameterSetRelationResponse:
        """
        @summary 关联到资源的参数集列表
        
        @param request: ListParameterSetRelationRequest
        @return: ListParameterSetRelationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_parameter_set_relation_with_options_async(request, headers, runtime)

    def list_parameter_sets_with_options(
        self,
        request: ia_cservice_20210806_models.ListParameterSetsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListParameterSetsResponse:
        """
        @summary 参数集列表
        
        @param request: ListParameterSetsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListParameterSetsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListParameterSets',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/parameterSets',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListParameterSetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_parameter_sets_with_options_async(
        self,
        request: ia_cservice_20210806_models.ListParameterSetsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListParameterSetsResponse:
        """
        @summary 参数集列表
        
        @param request: ListParameterSetsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListParameterSetsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListParameterSets',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/parameterSets',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListParameterSetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_parameter_sets(
        self,
        request: ia_cservice_20210806_models.ListParameterSetsRequest,
    ) -> ia_cservice_20210806_models.ListParameterSetsResponse:
        """
        @summary 参数集列表
        
        @param request: ListParameterSetsRequest
        @return: ListParameterSetsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_parameter_sets_with_options(request, headers, runtime)

    async def list_parameter_sets_async(
        self,
        request: ia_cservice_20210806_models.ListParameterSetsRequest,
    ) -> ia_cservice_20210806_models.ListParameterSetsResponse:
        """
        @summary 参数集列表
        
        @param request: ListParameterSetsRequest
        @return: ListParameterSetsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_parameter_sets_with_options_async(request, headers, runtime)

    def list_project_with_options(
        self,
        tmp_req: ia_cservice_20210806_models.ListProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListProjectResponse:
        """
        @summary 查询项目列表
        
        @param tmp_req: ListProjectRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListProjectResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ia_cservice_20210806_models.ListProjectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'tag', 'json')
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.tag_shrink):
            query['tag'] = request.tag_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProject',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/project',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_project_with_options_async(
        self,
        tmp_req: ia_cservice_20210806_models.ListProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListProjectResponse:
        """
        @summary 查询项目列表
        
        @param tmp_req: ListProjectRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListProjectResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ia_cservice_20210806_models.ListProjectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'tag', 'json')
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.tag_shrink):
            query['tag'] = request.tag_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProject',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/project',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_project(
        self,
        request: ia_cservice_20210806_models.ListProjectRequest,
    ) -> ia_cservice_20210806_models.ListProjectResponse:
        """
        @summary 查询项目列表
        
        @param request: ListProjectRequest
        @return: ListProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_project_with_options(request, headers, runtime)

    async def list_project_async(
        self,
        request: ia_cservice_20210806_models.ListProjectRequest,
    ) -> ia_cservice_20210806_models.ListProjectResponse:
        """
        @summary 查询项目列表
        
        @param request: ListProjectRequest
        @return: ListProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_project_with_options_async(request, headers, runtime)

    def list_project_builds_with_options(
        self,
        project_id: str,
        request: ia_cservice_20210806_models.ListProjectBuildsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListProjectBuildsResponse:
        """
        @summary 项目批次列表
        
        @param request: ListProjectBuildsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListProjectBuildsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['groupId'] = request.group_id
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_build_action):
            query['projectBuildAction'] = request.project_build_action
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProjectBuilds',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/project/{OpenApiUtilClient.get_encode_param(project_id)}/build',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListProjectBuildsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_project_builds_with_options_async(
        self,
        project_id: str,
        request: ia_cservice_20210806_models.ListProjectBuildsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListProjectBuildsResponse:
        """
        @summary 项目批次列表
        
        @param request: ListProjectBuildsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListProjectBuildsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['groupId'] = request.group_id
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_build_action):
            query['projectBuildAction'] = request.project_build_action
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProjectBuilds',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/project/{OpenApiUtilClient.get_encode_param(project_id)}/build',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListProjectBuildsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_project_builds(
        self,
        project_id: str,
        request: ia_cservice_20210806_models.ListProjectBuildsRequest,
    ) -> ia_cservice_20210806_models.ListProjectBuildsResponse:
        """
        @summary 项目批次列表
        
        @param request: ListProjectBuildsRequest
        @return: ListProjectBuildsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_project_builds_with_options(project_id, request, headers, runtime)

    async def list_project_builds_async(
        self,
        project_id: str,
        request: ia_cservice_20210806_models.ListProjectBuildsRequest,
    ) -> ia_cservice_20210806_models.ListProjectBuildsResponse:
        """
        @summary 项目批次列表
        
        @param request: ListProjectBuildsRequest
        @return: ListProjectBuildsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_project_builds_with_options_async(project_id, request, headers, runtime)

    def list_rabbitmq_publishers_with_options(
        self,
        request: ia_cservice_20210806_models.ListRabbitmqPublishersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListRabbitmqPublishersResponse:
        """
        @summary 获取消息发布者列表
        
        @param request: ListRabbitmqPublishersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRabbitmqPublishersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRabbitmqPublishers',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/publishers',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListRabbitmqPublishersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_rabbitmq_publishers_with_options_async(
        self,
        request: ia_cservice_20210806_models.ListRabbitmqPublishersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListRabbitmqPublishersResponse:
        """
        @summary 获取消息发布者列表
        
        @param request: ListRabbitmqPublishersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRabbitmqPublishersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRabbitmqPublishers',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/publishers',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListRabbitmqPublishersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_rabbitmq_publishers(
        self,
        request: ia_cservice_20210806_models.ListRabbitmqPublishersRequest,
    ) -> ia_cservice_20210806_models.ListRabbitmqPublishersResponse:
        """
        @summary 获取消息发布者列表
        
        @param request: ListRabbitmqPublishersRequest
        @return: ListRabbitmqPublishersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_rabbitmq_publishers_with_options(request, headers, runtime)

    async def list_rabbitmq_publishers_async(
        self,
        request: ia_cservice_20210806_models.ListRabbitmqPublishersRequest,
    ) -> ia_cservice_20210806_models.ListRabbitmqPublishersResponse:
        """
        @summary 获取消息发布者列表
        
        @param request: ListRabbitmqPublishersRequest
        @return: ListRabbitmqPublishersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_rabbitmq_publishers_with_options_async(request, headers, runtime)

    def list_ram_policy_export_task_versions_with_options(
        self,
        ram_policy_export_task_id: str,
        request: ia_cservice_20210806_models.ListRamPolicyExportTaskVersionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListRamPolicyExportTaskVersionsResponse:
        """
        @summary 获取RAM策略导出任务版本列表
        
        @param request: ListRamPolicyExportTaskVersionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRamPolicyExportTaskVersionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRamPolicyExportTaskVersions',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/ramPolicyExportTasks/{OpenApiUtilClient.get_encode_param(ram_policy_export_task_id)}/versions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListRamPolicyExportTaskVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ram_policy_export_task_versions_with_options_async(
        self,
        ram_policy_export_task_id: str,
        request: ia_cservice_20210806_models.ListRamPolicyExportTaskVersionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListRamPolicyExportTaskVersionsResponse:
        """
        @summary 获取RAM策略导出任务版本列表
        
        @param request: ListRamPolicyExportTaskVersionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRamPolicyExportTaskVersionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRamPolicyExportTaskVersions',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/ramPolicyExportTasks/{OpenApiUtilClient.get_encode_param(ram_policy_export_task_id)}/versions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListRamPolicyExportTaskVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ram_policy_export_task_versions(
        self,
        ram_policy_export_task_id: str,
        request: ia_cservice_20210806_models.ListRamPolicyExportTaskVersionsRequest,
    ) -> ia_cservice_20210806_models.ListRamPolicyExportTaskVersionsResponse:
        """
        @summary 获取RAM策略导出任务版本列表
        
        @param request: ListRamPolicyExportTaskVersionsRequest
        @return: ListRamPolicyExportTaskVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_ram_policy_export_task_versions_with_options(ram_policy_export_task_id, request, headers, runtime)

    async def list_ram_policy_export_task_versions_async(
        self,
        ram_policy_export_task_id: str,
        request: ia_cservice_20210806_models.ListRamPolicyExportTaskVersionsRequest,
    ) -> ia_cservice_20210806_models.ListRamPolicyExportTaskVersionsResponse:
        """
        @summary 获取RAM策略导出任务版本列表
        
        @param request: ListRamPolicyExportTaskVersionsRequest
        @return: ListRamPolicyExportTaskVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_ram_policy_export_task_versions_with_options_async(ram_policy_export_task_id, request, headers, runtime)

    def list_ram_policy_export_tasks_with_options(
        self,
        request: ia_cservice_20210806_models.ListRamPolicyExportTasksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListRamPolicyExportTasksResponse:
        """
        @summary 获取RAM策略导出任务列表
        
        @param request: ListRamPolicyExportTasksRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRamPolicyExportTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.module_id):
            query['moduleId'] = request.module_id
        if not UtilClient.is_unset(request.module_version):
            query['moduleVersion'] = request.module_version
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRamPolicyExportTasks',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/ramPolicyExportTasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListRamPolicyExportTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ram_policy_export_tasks_with_options_async(
        self,
        request: ia_cservice_20210806_models.ListRamPolicyExportTasksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListRamPolicyExportTasksResponse:
        """
        @summary 获取RAM策略导出任务列表
        
        @param request: ListRamPolicyExportTasksRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRamPolicyExportTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.module_id):
            query['moduleId'] = request.module_id
        if not UtilClient.is_unset(request.module_version):
            query['moduleVersion'] = request.module_version
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRamPolicyExportTasks',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/ramPolicyExportTasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListRamPolicyExportTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ram_policy_export_tasks(
        self,
        request: ia_cservice_20210806_models.ListRamPolicyExportTasksRequest,
    ) -> ia_cservice_20210806_models.ListRamPolicyExportTasksResponse:
        """
        @summary 获取RAM策略导出任务列表
        
        @param request: ListRamPolicyExportTasksRequest
        @return: ListRamPolicyExportTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_ram_policy_export_tasks_with_options(request, headers, runtime)

    async def list_ram_policy_export_tasks_async(
        self,
        request: ia_cservice_20210806_models.ListRamPolicyExportTasksRequest,
    ) -> ia_cservice_20210806_models.ListRamPolicyExportTasksResponse:
        """
        @summary 获取RAM策略导出任务列表
        
        @param request: ListRamPolicyExportTasksRequest
        @return: ListRamPolicyExportTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_ram_policy_export_tasks_with_options_async(request, headers, runtime)

    def list_resource_export_task_versions_with_options(
        self,
        export_task_id: str,
        request: ia_cservice_20210806_models.ListResourceExportTaskVersionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListResourceExportTaskVersionsResponse:
        """
        @summary 获取任务版本列表
        
        @param request: ListResourceExportTaskVersionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResourceExportTaskVersionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.export_version):
            query['exportVersion'] = request.export_version
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceExportTaskVersions',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/exportTasks/{OpenApiUtilClient.get_encode_param(export_task_id)}/exportVersions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListResourceExportTaskVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_export_task_versions_with_options_async(
        self,
        export_task_id: str,
        request: ia_cservice_20210806_models.ListResourceExportTaskVersionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListResourceExportTaskVersionsResponse:
        """
        @summary 获取任务版本列表
        
        @param request: ListResourceExportTaskVersionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResourceExportTaskVersionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.export_version):
            query['exportVersion'] = request.export_version
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceExportTaskVersions',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/exportTasks/{OpenApiUtilClient.get_encode_param(export_task_id)}/exportVersions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListResourceExportTaskVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_export_task_versions(
        self,
        export_task_id: str,
        request: ia_cservice_20210806_models.ListResourceExportTaskVersionsRequest,
    ) -> ia_cservice_20210806_models.ListResourceExportTaskVersionsResponse:
        """
        @summary 获取任务版本列表
        
        @param request: ListResourceExportTaskVersionsRequest
        @return: ListResourceExportTaskVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_resource_export_task_versions_with_options(export_task_id, request, headers, runtime)

    async def list_resource_export_task_versions_async(
        self,
        export_task_id: str,
        request: ia_cservice_20210806_models.ListResourceExportTaskVersionsRequest,
    ) -> ia_cservice_20210806_models.ListResourceExportTaskVersionsResponse:
        """
        @summary 获取任务版本列表
        
        @param request: ListResourceExportTaskVersionsRequest
        @return: ListResourceExportTaskVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_resource_export_task_versions_with_options_async(export_task_id, request, headers, runtime)

    def list_resource_export_tasks_with_options(
        self,
        request: ia_cservice_20210806_models.ListResourceExportTasksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListResourceExportTasksResponse:
        """
        @summary 查询导出任务列表
        
        @param request: ListResourceExportTasksRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResourceExportTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.export_task_id):
            query['exportTaskId'] = request.export_task_id
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceExportTasks',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/exportTasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListResourceExportTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_export_tasks_with_options_async(
        self,
        request: ia_cservice_20210806_models.ListResourceExportTasksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListResourceExportTasksResponse:
        """
        @summary 查询导出任务列表
        
        @param request: ListResourceExportTasksRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResourceExportTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.export_task_id):
            query['exportTaskId'] = request.export_task_id
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceExportTasks',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/exportTasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListResourceExportTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_export_tasks(
        self,
        request: ia_cservice_20210806_models.ListResourceExportTasksRequest,
    ) -> ia_cservice_20210806_models.ListResourceExportTasksResponse:
        """
        @summary 查询导出任务列表
        
        @param request: ListResourceExportTasksRequest
        @return: ListResourceExportTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_resource_export_tasks_with_options(request, headers, runtime)

    async def list_resource_export_tasks_async(
        self,
        request: ia_cservice_20210806_models.ListResourceExportTasksRequest,
    ) -> ia_cservice_20210806_models.ListResourceExportTasksResponse:
        """
        @summary 查询导出任务列表
        
        @param request: ListResourceExportTasksRequest
        @return: ListResourceExportTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_resource_export_tasks_with_options_async(request, headers, runtime)

    def list_resources_with_options(
        self,
        request: ia_cservice_20210806_models.ListResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListResourcesResponse:
        """
        @summary 资源列表
        
        @param request: ListResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.source_type):
            query['sourceType'] = request.source_type
        if not UtilClient.is_unset(request.source_value):
            query['sourceValue'] = request.source_value
        if not UtilClient.is_unset(request.spec_type):
            query['specType'] = request.spec_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResources',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/resources/stateparser',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resources_with_options_async(
        self,
        request: ia_cservice_20210806_models.ListResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListResourcesResponse:
        """
        @summary 资源列表
        
        @param request: ListResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.source_type):
            query['sourceType'] = request.source_type
        if not UtilClient.is_unset(request.source_value):
            query['sourceValue'] = request.source_value
        if not UtilClient.is_unset(request.spec_type):
            query['specType'] = request.spec_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResources',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/resources/stateparser',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resources(
        self,
        request: ia_cservice_20210806_models.ListResourcesRequest,
    ) -> ia_cservice_20210806_models.ListResourcesResponse:
        """
        @summary 资源列表
        
        @param request: ListResourcesRequest
        @return: ListResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_resources_with_options(request, headers, runtime)

    async def list_resources_async(
        self,
        request: ia_cservice_20210806_models.ListResourcesRequest,
    ) -> ia_cservice_20210806_models.ListResourcesResponse:
        """
        @summary 资源列表
        
        @param request: ListResourcesRequest
        @return: ListResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_resources_with_options_async(request, headers, runtime)

    def list_tasks_with_options(
        self,
        tmp_req: ia_cservice_20210806_models.ListTasksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListTasksResponse:
        """
        @summary 任务列表
        
        @param tmp_req: ListTasksRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTasksResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ia_cservice_20210806_models.ListTasksShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.exclude_task_ids):
            request.exclude_task_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.exclude_task_ids, 'excludeTaskIds', 'simple')
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'tag', 'json')
        query = {}
        if not UtilClient.is_unset(request.exclude_task_ids_shrink):
            query['excludeTaskIds'] = request.exclude_task_ids_shrink
        if not UtilClient.is_unset(request.group_id):
            query['groupId'] = request.group_id
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.module_id):
            query['moduleId'] = request.module_id
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['projectId'] = request.project_id
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        if not UtilClient.is_unset(request.tag_shrink):
            query['tag'] = request.tag_shrink
        if not UtilClient.is_unset(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTasks',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/tasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tasks_with_options_async(
        self,
        tmp_req: ia_cservice_20210806_models.ListTasksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListTasksResponse:
        """
        @summary 任务列表
        
        @param tmp_req: ListTasksRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTasksResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ia_cservice_20210806_models.ListTasksShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.exclude_task_ids):
            request.exclude_task_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.exclude_task_ids, 'excludeTaskIds', 'simple')
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'tag', 'json')
        query = {}
        if not UtilClient.is_unset(request.exclude_task_ids_shrink):
            query['excludeTaskIds'] = request.exclude_task_ids_shrink
        if not UtilClient.is_unset(request.group_id):
            query['groupId'] = request.group_id
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.module_id):
            query['moduleId'] = request.module_id
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['projectId'] = request.project_id
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        if not UtilClient.is_unset(request.tag_shrink):
            query['tag'] = request.tag_shrink
        if not UtilClient.is_unset(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTasks',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/tasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tasks(
        self,
        request: ia_cservice_20210806_models.ListTasksRequest,
    ) -> ia_cservice_20210806_models.ListTasksResponse:
        """
        @summary 任务列表
        
        @param request: ListTasksRequest
        @return: ListTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_tasks_with_options(request, headers, runtime)

    async def list_tasks_async(
        self,
        request: ia_cservice_20210806_models.ListTasksRequest,
    ) -> ia_cservice_20210806_models.ListTasksResponse:
        """
        @summary 任务列表
        
        @param request: ListTasksRequest
        @return: ListTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_tasks_with_options_async(request, headers, runtime)

    def list_terraform_provider_versions_with_options(
        self,
        request: ia_cservice_20210806_models.ListTerraformProviderVersionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListTerraformProviderVersionsResponse:
        """
        @summary terraformProvider版本
        
        @param request: ListTerraformProviderVersionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTerraformProviderVersionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.usage):
            query['usage'] = request.usage
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTerraformProviderVersions',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/version/terraform/provider',
            method='GET',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListTerraformProviderVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_terraform_provider_versions_with_options_async(
        self,
        request: ia_cservice_20210806_models.ListTerraformProviderVersionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListTerraformProviderVersionsResponse:
        """
        @summary terraformProvider版本
        
        @param request: ListTerraformProviderVersionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTerraformProviderVersionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.usage):
            query['usage'] = request.usage
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTerraformProviderVersions',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/version/terraform/provider',
            method='GET',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListTerraformProviderVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_terraform_provider_versions(
        self,
        request: ia_cservice_20210806_models.ListTerraformProviderVersionsRequest,
    ) -> ia_cservice_20210806_models.ListTerraformProviderVersionsResponse:
        """
        @summary terraformProvider版本
        
        @param request: ListTerraformProviderVersionsRequest
        @return: ListTerraformProviderVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_terraform_provider_versions_with_options(request, headers, runtime)

    async def list_terraform_provider_versions_async(
        self,
        request: ia_cservice_20210806_models.ListTerraformProviderVersionsRequest,
    ) -> ia_cservice_20210806_models.ListTerraformProviderVersionsResponse:
        """
        @summary terraformProvider版本
        
        @param request: ListTerraformProviderVersionsRequest
        @return: ListTerraformProviderVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_terraform_provider_versions_with_options_async(request, headers, runtime)

    def operate_job_with_options(
        self,
        task_id: str,
        job_id: str,
        operation_type: str,
        request: ia_cservice_20210806_models.OperateJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.OperateJobResponse:
        """
        @summary 控制作业
        
        @param request: OperateJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: OperateJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.comment):
            query['comment'] = request.comment
        if not UtilClient.is_unset(request.task_type):
            query['taskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OperateJob',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/tasks/{OpenApiUtilClient.get_encode_param(task_id)}/jobs/{OpenApiUtilClient.get_encode_param(job_id)}/operation/{OpenApiUtilClient.get_encode_param(operation_type)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.OperateJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def operate_job_with_options_async(
        self,
        task_id: str,
        job_id: str,
        operation_type: str,
        request: ia_cservice_20210806_models.OperateJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.OperateJobResponse:
        """
        @summary 控制作业
        
        @param request: OperateJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: OperateJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.comment):
            query['comment'] = request.comment
        if not UtilClient.is_unset(request.task_type):
            query['taskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OperateJob',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/tasks/{OpenApiUtilClient.get_encode_param(task_id)}/jobs/{OpenApiUtilClient.get_encode_param(job_id)}/operation/{OpenApiUtilClient.get_encode_param(operation_type)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.OperateJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def operate_job(
        self,
        task_id: str,
        job_id: str,
        operation_type: str,
        request: ia_cservice_20210806_models.OperateJobRequest,
    ) -> ia_cservice_20210806_models.OperateJobResponse:
        """
        @summary 控制作业
        
        @param request: OperateJobRequest
        @return: OperateJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.operate_job_with_options(task_id, job_id, operation_type, request, headers, runtime)

    async def operate_job_async(
        self,
        task_id: str,
        job_id: str,
        operation_type: str,
        request: ia_cservice_20210806_models.OperateJobRequest,
    ) -> ia_cservice_20210806_models.OperateJobResponse:
        """
        @summary 控制作业
        
        @param request: OperateJobRequest
        @return: OperateJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.operate_job_with_options_async(task_id, job_id, operation_type, request, headers, runtime)

    def remove_resource_export_task_version_with_options(
        self,
        export_task_id: str,
        export_version: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.RemoveResourceExportTaskVersionResponse:
        """
        @summary 移除导出任务版本
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveResourceExportTaskVersionResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RemoveResourceExportTaskVersion',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/exportTasks/{OpenApiUtilClient.get_encode_param(export_task_id)}/{OpenApiUtilClient.get_encode_param(export_version)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.RemoveResourceExportTaskVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_resource_export_task_version_with_options_async(
        self,
        export_task_id: str,
        export_version: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.RemoveResourceExportTaskVersionResponse:
        """
        @summary 移除导出任务版本
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveResourceExportTaskVersionResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RemoveResourceExportTaskVersion',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/exportTasks/{OpenApiUtilClient.get_encode_param(export_task_id)}/{OpenApiUtilClient.get_encode_param(export_version)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.RemoveResourceExportTaskVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_resource_export_task_version(
        self,
        export_task_id: str,
        export_version: str,
    ) -> ia_cservice_20210806_models.RemoveResourceExportTaskVersionResponse:
        """
        @summary 移除导出任务版本
        
        @return: RemoveResourceExportTaskVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.remove_resource_export_task_version_with_options(export_task_id, export_version, headers, runtime)

    async def remove_resource_export_task_version_async(
        self,
        export_task_id: str,
        export_version: str,
    ) -> ia_cservice_20210806_models.RemoveResourceExportTaskVersionResponse:
        """
        @summary 移除导出任务版本
        
        @return: RemoveResourceExportTaskVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.remove_resource_export_task_version_with_options_async(export_task_id, export_version, headers, runtime)

    def tag_resources_with_options(
        self,
        request: ia_cservice_20210806_models.TagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.TagResourcesResponse:
        """
        @summary 打标签接口
        
        @param request: TagResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['regionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_ids):
            body['resourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_type):
            body['resourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/tags',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: ia_cservice_20210806_models.TagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.TagResourcesResponse:
        """
        @summary 打标签接口
        
        @param request: TagResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['regionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_ids):
            body['resourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_type):
            body['resourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/tags',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: ia_cservice_20210806_models.TagResourcesRequest,
    ) -> ia_cservice_20210806_models.TagResourcesResponse:
        """
        @summary 打标签接口
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.tag_resources_with_options(request, headers, runtime)

    async def tag_resources_async(
        self,
        request: ia_cservice_20210806_models.TagResourcesRequest,
    ) -> ia_cservice_20210806_models.TagResourcesResponse:
        """
        @summary 打标签接口
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.tag_resources_with_options_async(request, headers, runtime)

    def update_authorization_attribute_with_options(
        self,
        authorization_id: str,
        request: ia_cservice_20210806_models.UpdateAuthorizationAttributeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.UpdateAuthorizationAttributeResponse:
        """
        @summary 更新共享
        
        @param request: UpdateAuthorizationAttributeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAuthorizationAttributeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.due_time):
            body['dueTime'] = request.due_time
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAuthorizationAttribute',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/authorizations/{OpenApiUtilClient.get_encode_param(authorization_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.UpdateAuthorizationAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_authorization_attribute_with_options_async(
        self,
        authorization_id: str,
        request: ia_cservice_20210806_models.UpdateAuthorizationAttributeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.UpdateAuthorizationAttributeResponse:
        """
        @summary 更新共享
        
        @param request: UpdateAuthorizationAttributeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAuthorizationAttributeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.due_time):
            body['dueTime'] = request.due_time
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAuthorizationAttribute',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/authorizations/{OpenApiUtilClient.get_encode_param(authorization_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.UpdateAuthorizationAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_authorization_attribute(
        self,
        authorization_id: str,
        request: ia_cservice_20210806_models.UpdateAuthorizationAttributeRequest,
    ) -> ia_cservice_20210806_models.UpdateAuthorizationAttributeResponse:
        """
        @summary 更新共享
        
        @param request: UpdateAuthorizationAttributeRequest
        @return: UpdateAuthorizationAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_authorization_attribute_with_options(authorization_id, request, headers, runtime)

    async def update_authorization_attribute_async(
        self,
        authorization_id: str,
        request: ia_cservice_20210806_models.UpdateAuthorizationAttributeRequest,
    ) -> ia_cservice_20210806_models.UpdateAuthorizationAttributeResponse:
        """
        @summary 更新共享
        
        @param request: UpdateAuthorizationAttributeRequest
        @return: UpdateAuthorizationAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_authorization_attribute_with_options_async(authorization_id, request, headers, runtime)

    def update_explorer_task_attribute_with_options(
        self,
        explorer_task_id: str,
        request: ia_cservice_20210806_models.UpdateExplorerTaskAttributeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.UpdateExplorerTaskAttributeResponse:
        """
        @summary 修改Explorer任务
        
        @param request: UpdateExplorerTaskAttributeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateExplorerTaskAttributeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_apply):
            body['autoApply'] = request.auto_apply
        if not UtilClient.is_unset(request.explorer_task_name):
            body['explorerTaskName'] = request.explorer_task_name
        if not UtilClient.is_unset(request.module_id):
            body['moduleId'] = request.module_id
        if not UtilClient.is_unset(request.module_version):
            body['moduleVersion'] = request.module_version
        if not UtilClient.is_unset(request.terraform_provider_version):
            body['terraformProviderVersion'] = request.terraform_provider_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateExplorerTaskAttribute',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/explorerTask/{OpenApiUtilClient.get_encode_param(explorer_task_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.UpdateExplorerTaskAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_explorer_task_attribute_with_options_async(
        self,
        explorer_task_id: str,
        request: ia_cservice_20210806_models.UpdateExplorerTaskAttributeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.UpdateExplorerTaskAttributeResponse:
        """
        @summary 修改Explorer任务
        
        @param request: UpdateExplorerTaskAttributeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateExplorerTaskAttributeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_apply):
            body['autoApply'] = request.auto_apply
        if not UtilClient.is_unset(request.explorer_task_name):
            body['explorerTaskName'] = request.explorer_task_name
        if not UtilClient.is_unset(request.module_id):
            body['moduleId'] = request.module_id
        if not UtilClient.is_unset(request.module_version):
            body['moduleVersion'] = request.module_version
        if not UtilClient.is_unset(request.terraform_provider_version):
            body['terraformProviderVersion'] = request.terraform_provider_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateExplorerTaskAttribute',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/explorerTask/{OpenApiUtilClient.get_encode_param(explorer_task_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.UpdateExplorerTaskAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_explorer_task_attribute(
        self,
        explorer_task_id: str,
        request: ia_cservice_20210806_models.UpdateExplorerTaskAttributeRequest,
    ) -> ia_cservice_20210806_models.UpdateExplorerTaskAttributeResponse:
        """
        @summary 修改Explorer任务
        
        @param request: UpdateExplorerTaskAttributeRequest
        @return: UpdateExplorerTaskAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_explorer_task_attribute_with_options(explorer_task_id, request, headers, runtime)

    async def update_explorer_task_attribute_async(
        self,
        explorer_task_id: str,
        request: ia_cservice_20210806_models.UpdateExplorerTaskAttributeRequest,
    ) -> ia_cservice_20210806_models.UpdateExplorerTaskAttributeResponse:
        """
        @summary 修改Explorer任务
        
        @param request: UpdateExplorerTaskAttributeRequest
        @return: UpdateExplorerTaskAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_explorer_task_attribute_with_options_async(explorer_task_id, request, headers, runtime)

    def update_group_with_options(
        self,
        group_id: str,
        request: ia_cservice_20210806_models.UpdateGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.UpdateGroupResponse:
        """
        @summary 修改分组
        
        @param request: UpdateGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_destroy):
            body['autoDestroy'] = request.auto_destroy
        if not UtilClient.is_unset(request.auto_trigger):
            body['autoTrigger'] = request.auto_trigger
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.forced_setting):
            body['forcedSetting'] = request.forced_setting
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.notify_config):
            body['notifyConfig'] = request.notify_config
        if not UtilClient.is_unset(request.notify_operation_types):
            body['notifyOperationTypes'] = request.notify_operation_types
        if not UtilClient.is_unset(request.ram_role):
            body['ramRole'] = request.ram_role
        if not UtilClient.is_unset(request.report_export_field):
            body['reportExportField'] = request.report_export_field
        if not UtilClient.is_unset(request.report_export_path):
            body['reportExportPath'] = request.report_export_path
        if not UtilClient.is_unset(request.terraform_provider_version):
            body['terraformProviderVersion'] = request.terraform_provider_version
        if not UtilClient.is_unset(request.trigger_config):
            body['triggerConfig'] = request.trigger_config
        if not UtilClient.is_unset(request.trigger_resource_type):
            body['triggerResourceType'] = request.trigger_resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateGroup',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/group/{OpenApiUtilClient.get_encode_param(group_id)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.UpdateGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_group_with_options_async(
        self,
        group_id: str,
        request: ia_cservice_20210806_models.UpdateGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.UpdateGroupResponse:
        """
        @summary 修改分组
        
        @param request: UpdateGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_destroy):
            body['autoDestroy'] = request.auto_destroy
        if not UtilClient.is_unset(request.auto_trigger):
            body['autoTrigger'] = request.auto_trigger
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.forced_setting):
            body['forcedSetting'] = request.forced_setting
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.notify_config):
            body['notifyConfig'] = request.notify_config
        if not UtilClient.is_unset(request.notify_operation_types):
            body['notifyOperationTypes'] = request.notify_operation_types
        if not UtilClient.is_unset(request.ram_role):
            body['ramRole'] = request.ram_role
        if not UtilClient.is_unset(request.report_export_field):
            body['reportExportField'] = request.report_export_field
        if not UtilClient.is_unset(request.report_export_path):
            body['reportExportPath'] = request.report_export_path
        if not UtilClient.is_unset(request.terraform_provider_version):
            body['terraformProviderVersion'] = request.terraform_provider_version
        if not UtilClient.is_unset(request.trigger_config):
            body['triggerConfig'] = request.trigger_config
        if not UtilClient.is_unset(request.trigger_resource_type):
            body['triggerResourceType'] = request.trigger_resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateGroup',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/group/{OpenApiUtilClient.get_encode_param(group_id)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.UpdateGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_group(
        self,
        group_id: str,
        request: ia_cservice_20210806_models.UpdateGroupRequest,
    ) -> ia_cservice_20210806_models.UpdateGroupResponse:
        """
        @summary 修改分组
        
        @param request: UpdateGroupRequest
        @return: UpdateGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_group_with_options(group_id, request, headers, runtime)

    async def update_group_async(
        self,
        group_id: str,
        request: ia_cservice_20210806_models.UpdateGroupRequest,
    ) -> ia_cservice_20210806_models.UpdateGroupResponse:
        """
        @summary 修改分组
        
        @param request: UpdateGroupRequest
        @return: UpdateGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_group_with_options_async(group_id, request, headers, runtime)

    def update_module_attribute_with_options(
        self,
        module_id: str,
        request: ia_cservice_20210806_models.UpdateModuleAttributeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.UpdateModuleAttributeResponse:
        """
        @summary 更新模版
        
        @param request: UpdateModuleAttributeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateModuleAttributeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.group_info):
            body['groupInfo'] = request.group_info
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.source):
            body['source'] = request.source
        if not UtilClient.is_unset(request.source_path):
            body['sourcePath'] = request.source_path
        if not UtilClient.is_unset(request.state_path):
            body['statePath'] = request.state_path
        if not UtilClient.is_unset(request.version_strategy):
            body['versionStrategy'] = request.version_strategy
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateModuleAttribute',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/modules/{OpenApiUtilClient.get_encode_param(module_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.UpdateModuleAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_module_attribute_with_options_async(
        self,
        module_id: str,
        request: ia_cservice_20210806_models.UpdateModuleAttributeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.UpdateModuleAttributeResponse:
        """
        @summary 更新模版
        
        @param request: UpdateModuleAttributeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateModuleAttributeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.group_info):
            body['groupInfo'] = request.group_info
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.source):
            body['source'] = request.source
        if not UtilClient.is_unset(request.source_path):
            body['sourcePath'] = request.source_path
        if not UtilClient.is_unset(request.state_path):
            body['statePath'] = request.state_path
        if not UtilClient.is_unset(request.version_strategy):
            body['versionStrategy'] = request.version_strategy
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateModuleAttribute',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/modules/{OpenApiUtilClient.get_encode_param(module_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.UpdateModuleAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_module_attribute(
        self,
        module_id: str,
        request: ia_cservice_20210806_models.UpdateModuleAttributeRequest,
    ) -> ia_cservice_20210806_models.UpdateModuleAttributeResponse:
        """
        @summary 更新模版
        
        @param request: UpdateModuleAttributeRequest
        @return: UpdateModuleAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_module_attribute_with_options(module_id, request, headers, runtime)

    async def update_module_attribute_async(
        self,
        module_id: str,
        request: ia_cservice_20210806_models.UpdateModuleAttributeRequest,
    ) -> ia_cservice_20210806_models.UpdateModuleAttributeResponse:
        """
        @summary 更新模版
        
        @param request: UpdateModuleAttributeRequest
        @return: UpdateModuleAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_module_attribute_with_options_async(module_id, request, headers, runtime)

    def update_parameter_set_attribute_with_options(
        self,
        parameter_set_id: str,
        request: ia_cservice_20210806_models.UpdateParameterSetAttributeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.UpdateParameterSetAttributeResponse:
        """
        @summary 更新参数集
        
        @param request: UpdateParameterSetAttributeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateParameterSetAttributeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.parameters):
            body['parameters'] = request.parameters
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateParameterSetAttribute',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/parameterSets/{OpenApiUtilClient.get_encode_param(parameter_set_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.UpdateParameterSetAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_parameter_set_attribute_with_options_async(
        self,
        parameter_set_id: str,
        request: ia_cservice_20210806_models.UpdateParameterSetAttributeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.UpdateParameterSetAttributeResponse:
        """
        @summary 更新参数集
        
        @param request: UpdateParameterSetAttributeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateParameterSetAttributeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.parameters):
            body['parameters'] = request.parameters
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateParameterSetAttribute',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/parameterSets/{OpenApiUtilClient.get_encode_param(parameter_set_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.UpdateParameterSetAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_parameter_set_attribute(
        self,
        parameter_set_id: str,
        request: ia_cservice_20210806_models.UpdateParameterSetAttributeRequest,
    ) -> ia_cservice_20210806_models.UpdateParameterSetAttributeResponse:
        """
        @summary 更新参数集
        
        @param request: UpdateParameterSetAttributeRequest
        @return: UpdateParameterSetAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_parameter_set_attribute_with_options(parameter_set_id, request, headers, runtime)

    async def update_parameter_set_attribute_async(
        self,
        parameter_set_id: str,
        request: ia_cservice_20210806_models.UpdateParameterSetAttributeRequest,
    ) -> ia_cservice_20210806_models.UpdateParameterSetAttributeResponse:
        """
        @summary 更新参数集
        
        @param request: UpdateParameterSetAttributeRequest
        @return: UpdateParameterSetAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_parameter_set_attribute_with_options_async(parameter_set_id, request, headers, runtime)

    def update_project_with_options(
        self,
        project_id: str,
        request: ia_cservice_20210806_models.UpdateProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.UpdateProjectResponse:
        """
        @summary 修改项目
        
        @param request: UpdateProjectRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateProjectResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProject',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/project/{OpenApiUtilClient.get_encode_param(project_id)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.UpdateProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_project_with_options_async(
        self,
        project_id: str,
        request: ia_cservice_20210806_models.UpdateProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.UpdateProjectResponse:
        """
        @summary 修改项目
        
        @param request: UpdateProjectRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateProjectResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProject',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/project/{OpenApiUtilClient.get_encode_param(project_id)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.UpdateProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_project(
        self,
        project_id: str,
        request: ia_cservice_20210806_models.UpdateProjectRequest,
    ) -> ia_cservice_20210806_models.UpdateProjectResponse:
        """
        @summary 修改项目
        
        @param request: UpdateProjectRequest
        @return: UpdateProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_project_with_options(project_id, request, headers, runtime)

    async def update_project_async(
        self,
        project_id: str,
        request: ia_cservice_20210806_models.UpdateProjectRequest,
    ) -> ia_cservice_20210806_models.UpdateProjectResponse:
        """
        @summary 修改项目
        
        @param request: UpdateProjectRequest
        @return: UpdateProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_project_with_options_async(project_id, request, headers, runtime)

    def update_rabbitmq_publisher_attribute_with_options(
        self,
        publisher_id: str,
        request: ia_cservice_20210806_models.UpdateRabbitmqPublisherAttributeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.UpdateRabbitmqPublisherAttributeResponse:
        """
        @summary 更新消息发布者
        
        @param request: UpdateRabbitmqPublisherAttributeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateRabbitmqPublisherAttributeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.exchange_name):
            body['exchangeName'] = request.exchange_name
        if not UtilClient.is_unset(request.exchange_type):
            body['exchangeType'] = request.exchange_type
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateRabbitmqPublisherAttribute',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/publishers/{OpenApiUtilClient.get_encode_param(publisher_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.UpdateRabbitmqPublisherAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_rabbitmq_publisher_attribute_with_options_async(
        self,
        publisher_id: str,
        request: ia_cservice_20210806_models.UpdateRabbitmqPublisherAttributeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.UpdateRabbitmqPublisherAttributeResponse:
        """
        @summary 更新消息发布者
        
        @param request: UpdateRabbitmqPublisherAttributeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateRabbitmqPublisherAttributeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.exchange_name):
            body['exchangeName'] = request.exchange_name
        if not UtilClient.is_unset(request.exchange_type):
            body['exchangeType'] = request.exchange_type
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateRabbitmqPublisherAttribute',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/publishers/{OpenApiUtilClient.get_encode_param(publisher_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.UpdateRabbitmqPublisherAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_rabbitmq_publisher_attribute(
        self,
        publisher_id: str,
        request: ia_cservice_20210806_models.UpdateRabbitmqPublisherAttributeRequest,
    ) -> ia_cservice_20210806_models.UpdateRabbitmqPublisherAttributeResponse:
        """
        @summary 更新消息发布者
        
        @param request: UpdateRabbitmqPublisherAttributeRequest
        @return: UpdateRabbitmqPublisherAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_rabbitmq_publisher_attribute_with_options(publisher_id, request, headers, runtime)

    async def update_rabbitmq_publisher_attribute_async(
        self,
        publisher_id: str,
        request: ia_cservice_20210806_models.UpdateRabbitmqPublisherAttributeRequest,
    ) -> ia_cservice_20210806_models.UpdateRabbitmqPublisherAttributeResponse:
        """
        @summary 更新消息发布者
        
        @param request: UpdateRabbitmqPublisherAttributeRequest
        @return: UpdateRabbitmqPublisherAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_rabbitmq_publisher_attribute_with_options_async(publisher_id, request, headers, runtime)

    def update_ram_policy_export_task_attribute_with_options(
        self,
        ram_policy_export_task_id: str,
        request: ia_cservice_20210806_models.UpdateRamPolicyExportTaskAttributeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.UpdateRamPolicyExportTaskAttributeResponse:
        """
        @summary 修改RAM策略导出任务
        
        @param request: UpdateRamPolicyExportTaskAttributeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateRamPolicyExportTaskAttributeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.authorization_account_ids):
            body['authorizationAccountIds'] = request.authorization_account_ids
        if not UtilClient.is_unset(request.authorization_actions):
            body['authorizationActions'] = request.authorization_actions
        if not UtilClient.is_unset(request.authorization_region_ids):
            body['authorizationRegionIds'] = request.authorization_region_ids
        if not UtilClient.is_unset(request.module_id):
            body['moduleId'] = request.module_id
        if not UtilClient.is_unset(request.module_version):
            body['moduleVersion'] = request.module_version
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.ram_role):
            body['ramRole'] = request.ram_role
        if not UtilClient.is_unset(request.trigger_strategy):
            body['triggerStrategy'] = request.trigger_strategy
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateRamPolicyExportTaskAttribute',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/ramPolicyExportTasks/{OpenApiUtilClient.get_encode_param(ram_policy_export_task_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.UpdateRamPolicyExportTaskAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_ram_policy_export_task_attribute_with_options_async(
        self,
        ram_policy_export_task_id: str,
        request: ia_cservice_20210806_models.UpdateRamPolicyExportTaskAttributeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.UpdateRamPolicyExportTaskAttributeResponse:
        """
        @summary 修改RAM策略导出任务
        
        @param request: UpdateRamPolicyExportTaskAttributeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateRamPolicyExportTaskAttributeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.authorization_account_ids):
            body['authorizationAccountIds'] = request.authorization_account_ids
        if not UtilClient.is_unset(request.authorization_actions):
            body['authorizationActions'] = request.authorization_actions
        if not UtilClient.is_unset(request.authorization_region_ids):
            body['authorizationRegionIds'] = request.authorization_region_ids
        if not UtilClient.is_unset(request.module_id):
            body['moduleId'] = request.module_id
        if not UtilClient.is_unset(request.module_version):
            body['moduleVersion'] = request.module_version
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.ram_role):
            body['ramRole'] = request.ram_role
        if not UtilClient.is_unset(request.trigger_strategy):
            body['triggerStrategy'] = request.trigger_strategy
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateRamPolicyExportTaskAttribute',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/ramPolicyExportTasks/{OpenApiUtilClient.get_encode_param(ram_policy_export_task_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.UpdateRamPolicyExportTaskAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_ram_policy_export_task_attribute(
        self,
        ram_policy_export_task_id: str,
        request: ia_cservice_20210806_models.UpdateRamPolicyExportTaskAttributeRequest,
    ) -> ia_cservice_20210806_models.UpdateRamPolicyExportTaskAttributeResponse:
        """
        @summary 修改RAM策略导出任务
        
        @param request: UpdateRamPolicyExportTaskAttributeRequest
        @return: UpdateRamPolicyExportTaskAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_ram_policy_export_task_attribute_with_options(ram_policy_export_task_id, request, headers, runtime)

    async def update_ram_policy_export_task_attribute_async(
        self,
        ram_policy_export_task_id: str,
        request: ia_cservice_20210806_models.UpdateRamPolicyExportTaskAttributeRequest,
    ) -> ia_cservice_20210806_models.UpdateRamPolicyExportTaskAttributeResponse:
        """
        @summary 修改RAM策略导出任务
        
        @param request: UpdateRamPolicyExportTaskAttributeRequest
        @return: UpdateRamPolicyExportTaskAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_ram_policy_export_task_attribute_with_options_async(ram_policy_export_task_id, request, headers, runtime)

    def update_resource_export_task_attribute_with_options(
        self,
        export_task_id: str,
        request: ia_cservice_20210806_models.UpdateResourceExportTaskAttributeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.UpdateResourceExportTaskAttributeResponse:
        """
        @summary 更新导出任务
        
        @param request: UpdateResourceExportTaskAttributeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateResourceExportTaskAttributeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.config_path):
            body['configPath'] = request.config_path
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.exclude_rules):
            body['excludeRules'] = request.exclude_rules
        if not UtilClient.is_unset(request.export_to_module):
            body['exportToModule'] = request.export_to_module
        if not UtilClient.is_unset(request.include_rules):
            body['includeRules'] = request.include_rules
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.ram_role):
            body['ramRole'] = request.ram_role
        if not UtilClient.is_unset(request.terraform_provider_version):
            body['terraformProviderVersion'] = request.terraform_provider_version
        if not UtilClient.is_unset(request.terraform_version):
            body['terraformVersion'] = request.terraform_version
        if not UtilClient.is_unset(request.trigger_strategy):
            body['triggerStrategy'] = request.trigger_strategy
        if not UtilClient.is_unset(request.variables):
            body['variables'] = request.variables
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateResourceExportTaskAttribute',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/exportTasks/{OpenApiUtilClient.get_encode_param(export_task_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.UpdateResourceExportTaskAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_resource_export_task_attribute_with_options_async(
        self,
        export_task_id: str,
        request: ia_cservice_20210806_models.UpdateResourceExportTaskAttributeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.UpdateResourceExportTaskAttributeResponse:
        """
        @summary 更新导出任务
        
        @param request: UpdateResourceExportTaskAttributeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateResourceExportTaskAttributeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.config_path):
            body['configPath'] = request.config_path
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.exclude_rules):
            body['excludeRules'] = request.exclude_rules
        if not UtilClient.is_unset(request.export_to_module):
            body['exportToModule'] = request.export_to_module
        if not UtilClient.is_unset(request.include_rules):
            body['includeRules'] = request.include_rules
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.ram_role):
            body['ramRole'] = request.ram_role
        if not UtilClient.is_unset(request.terraform_provider_version):
            body['terraformProviderVersion'] = request.terraform_provider_version
        if not UtilClient.is_unset(request.terraform_version):
            body['terraformVersion'] = request.terraform_version
        if not UtilClient.is_unset(request.trigger_strategy):
            body['triggerStrategy'] = request.trigger_strategy
        if not UtilClient.is_unset(request.variables):
            body['variables'] = request.variables
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateResourceExportTaskAttribute',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/exportTasks/{OpenApiUtilClient.get_encode_param(export_task_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.UpdateResourceExportTaskAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_resource_export_task_attribute(
        self,
        export_task_id: str,
        request: ia_cservice_20210806_models.UpdateResourceExportTaskAttributeRequest,
    ) -> ia_cservice_20210806_models.UpdateResourceExportTaskAttributeResponse:
        """
        @summary 更新导出任务
        
        @param request: UpdateResourceExportTaskAttributeRequest
        @return: UpdateResourceExportTaskAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_resource_export_task_attribute_with_options(export_task_id, request, headers, runtime)

    async def update_resource_export_task_attribute_async(
        self,
        export_task_id: str,
        request: ia_cservice_20210806_models.UpdateResourceExportTaskAttributeRequest,
    ) -> ia_cservice_20210806_models.UpdateResourceExportTaskAttributeResponse:
        """
        @summary 更新导出任务
        
        @param request: UpdateResourceExportTaskAttributeRequest
        @return: UpdateResourceExportTaskAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_resource_export_task_attribute_with_options_async(export_task_id, request, headers, runtime)

    def update_task_attribute_with_options(
        self,
        task_id: str,
        request: ia_cservice_20210806_models.UpdateTaskAttributeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.UpdateTaskAttributeResponse:
        """
        @summary 修改任务
        
        @param request: UpdateTaskAttributeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateTaskAttributeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_apply):
            body['autoApply'] = request.auto_apply
        if not UtilClient.is_unset(request.auto_destroy):
            body['autoDestroy'] = request.auto_destroy
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.group_info):
            body['groupInfo'] = request.group_info
        if not UtilClient.is_unset(request.init_module_state):
            body['initModuleState'] = request.init_module_state
        if not UtilClient.is_unset(request.module_id):
            body['moduleId'] = request.module_id
        if not UtilClient.is_unset(request.module_version):
            body['moduleVersion'] = request.module_version
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.parameters):
            body['parameters'] = request.parameters
        if not UtilClient.is_unset(request.protection_strategy):
            body['protectionStrategy'] = request.protection_strategy
        if not UtilClient.is_unset(request.ram_role):
            body['ramRole'] = request.ram_role
        if not UtilClient.is_unset(request.skip_property_validation):
            body['skipPropertyValidation'] = request.skip_property_validation
        if not UtilClient.is_unset(request.terraform_version):
            body['terraformVersion'] = request.terraform_version
        if not UtilClient.is_unset(request.trigger_strategy):
            body['triggerStrategy'] = request.trigger_strategy
        if not UtilClient.is_unset(request.trigger_value):
            body['triggerValue'] = request.trigger_value
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTaskAttribute',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/tasks/{OpenApiUtilClient.get_encode_param(task_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.UpdateTaskAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_task_attribute_with_options_async(
        self,
        task_id: str,
        request: ia_cservice_20210806_models.UpdateTaskAttributeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.UpdateTaskAttributeResponse:
        """
        @summary 修改任务
        
        @param request: UpdateTaskAttributeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateTaskAttributeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_apply):
            body['autoApply'] = request.auto_apply
        if not UtilClient.is_unset(request.auto_destroy):
            body['autoDestroy'] = request.auto_destroy
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.group_info):
            body['groupInfo'] = request.group_info
        if not UtilClient.is_unset(request.init_module_state):
            body['initModuleState'] = request.init_module_state
        if not UtilClient.is_unset(request.module_id):
            body['moduleId'] = request.module_id
        if not UtilClient.is_unset(request.module_version):
            body['moduleVersion'] = request.module_version
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.parameters):
            body['parameters'] = request.parameters
        if not UtilClient.is_unset(request.protection_strategy):
            body['protectionStrategy'] = request.protection_strategy
        if not UtilClient.is_unset(request.ram_role):
            body['ramRole'] = request.ram_role
        if not UtilClient.is_unset(request.skip_property_validation):
            body['skipPropertyValidation'] = request.skip_property_validation
        if not UtilClient.is_unset(request.terraform_version):
            body['terraformVersion'] = request.terraform_version
        if not UtilClient.is_unset(request.trigger_strategy):
            body['triggerStrategy'] = request.trigger_strategy
        if not UtilClient.is_unset(request.trigger_value):
            body['triggerValue'] = request.trigger_value
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTaskAttribute',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/tasks/{OpenApiUtilClient.get_encode_param(task_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.UpdateTaskAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_task_attribute(
        self,
        task_id: str,
        request: ia_cservice_20210806_models.UpdateTaskAttributeRequest,
    ) -> ia_cservice_20210806_models.UpdateTaskAttributeResponse:
        """
        @summary 修改任务
        
        @param request: UpdateTaskAttributeRequest
        @return: UpdateTaskAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_task_attribute_with_options(task_id, request, headers, runtime)

    async def update_task_attribute_async(
        self,
        task_id: str,
        request: ia_cservice_20210806_models.UpdateTaskAttributeRequest,
    ) -> ia_cservice_20210806_models.UpdateTaskAttributeResponse:
        """
        @summary 修改任务
        
        @param request: UpdateTaskAttributeRequest
        @return: UpdateTaskAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_task_attribute_with_options_async(task_id, request, headers, runtime)

    def update_task_policy_with_options(
        self,
        group_id: str,
        request: ia_cservice_20210806_models.UpdateTaskPolicyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.UpdateTaskPolicyResponse:
        """
        @summary 修改分组优先级配置
        
        @param request: UpdateTaskPolicyRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateTaskPolicyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.task_policies):
            body['taskPolicies'] = request.task_policies
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTaskPolicy',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/group/task/policy/{OpenApiUtilClient.get_encode_param(group_id)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.UpdateTaskPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_task_policy_with_options_async(
        self,
        group_id: str,
        request: ia_cservice_20210806_models.UpdateTaskPolicyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.UpdateTaskPolicyResponse:
        """
        @summary 修改分组优先级配置
        
        @param request: UpdateTaskPolicyRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateTaskPolicyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.task_policies):
            body['taskPolicies'] = request.task_policies
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTaskPolicy',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/group/task/policy/{OpenApiUtilClient.get_encode_param(group_id)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.UpdateTaskPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_task_policy(
        self,
        group_id: str,
        request: ia_cservice_20210806_models.UpdateTaskPolicyRequest,
    ) -> ia_cservice_20210806_models.UpdateTaskPolicyResponse:
        """
        @summary 修改分组优先级配置
        
        @param request: UpdateTaskPolicyRequest
        @return: UpdateTaskPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_task_policy_with_options(group_id, request, headers, runtime)

    async def update_task_policy_async(
        self,
        group_id: str,
        request: ia_cservice_20210806_models.UpdateTaskPolicyRequest,
    ) -> ia_cservice_20210806_models.UpdateTaskPolicyResponse:
        """
        @summary 修改分组优先级配置
        
        @param request: UpdateTaskPolicyRequest
        @return: UpdateTaskPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_task_policy_with_options_async(group_id, request, headers, runtime)
