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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.associate_group_with_options(group_id, request, headers, runtime)

    async def associate_group_async(
        self,
        group_id: str,
        request: ia_cservice_20210806_models.AssociateGroupRequest,
    ) -> ia_cservice_20210806_models.AssociateGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.associate_group_with_options_async(group_id, request, headers, runtime)

    def associate_parameter_set_with_options(
        self,
        request: ia_cservice_20210806_models.AssociateParameterSetRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.AssociateParameterSetResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.associate_parameter_set_with_options(request, headers, runtime)

    async def associate_parameter_set_async(
        self,
        request: ia_cservice_20210806_models.AssociateParameterSetRequest,
    ) -> ia_cservice_20210806_models.AssociateParameterSetResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.attach_rabbitmq_publisher_with_options(publisher_id, request, headers, runtime)

    async def attach_rabbitmq_publisher_async(
        self,
        publisher_id: str,
        request: ia_cservice_20210806_models.AttachRabbitmqPublisherRequest,
    ) -> ia_cservice_20210806_models.AttachRabbitmqPublisherResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.attach_rabbitmq_publisher_with_options_async(publisher_id, request, headers, runtime)

    def cancel_ram_policy_export_task_with_options(
        self,
        ram_policy_export_task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.CancelRamPolicyExportTaskResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.cancel_ram_policy_export_task_with_options(ram_policy_export_task_id, headers, runtime)

    async def cancel_ram_policy_export_task_async(
        self,
        ram_policy_export_task_id: str,
    ) -> ia_cservice_20210806_models.CancelRamPolicyExportTaskResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.cancel_resource_export_task_with_options(export_task_id, request, headers, runtime)

    async def cancel_resource_export_task_async(
        self,
        export_task_id: str,
        request: ia_cservice_20210806_models.CancelResourceExportTaskRequest,
    ) -> ia_cservice_20210806_models.CancelResourceExportTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.cancel_resource_export_task_with_options_async(export_task_id, request, headers, runtime)

    def check_resource_name_with_options(
        self,
        request: ia_cservice_20210806_models.CheckResourceNameRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.CheckResourceNameResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.check_resource_name_with_options(request, headers, runtime)

    async def check_resource_name_async(
        self,
        request: ia_cservice_20210806_models.CheckResourceNameRequest,
    ) -> ia_cservice_20210806_models.CheckResourceNameResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.clone_group_with_options(group_id, request, headers, runtime)

    async def clone_group_async(
        self,
        group_id: str,
        request: ia_cservice_20210806_models.CloneGroupRequest,
    ) -> ia_cservice_20210806_models.CloneGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.clone_group_with_options_async(group_id, request, headers, runtime)

    def clone_module_with_options(
        self,
        request: ia_cservice_20210806_models.CloneModuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.CloneModuleResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.clone_module_with_options(request, headers, runtime)

    async def clone_module_async(
        self,
        request: ia_cservice_20210806_models.CloneModuleRequest,
    ) -> ia_cservice_20210806_models.CloneModuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.clone_module_with_options_async(request, headers, runtime)

    def create_authorization_with_options(
        self,
        request: ia_cservice_20210806_models.CreateAuthorizationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.CreateAuthorizationResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_authorization_with_options(request, headers, runtime)

    async def create_authorization_async(
        self,
        request: ia_cservice_20210806_models.CreateAuthorizationRequest,
    ) -> ia_cservice_20210806_models.CreateAuthorizationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_authorization_with_options_async(request, headers, runtime)

    def create_group_with_options(
        self,
        request: ia_cservice_20210806_models.CreateGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.CreateGroupResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_group_with_options(request, headers, runtime)

    async def create_group_async(
        self,
        request: ia_cservice_20210806_models.CreateGroupRequest,
    ) -> ia_cservice_20210806_models.CreateGroupResponse:
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
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.sub_command):
            body['subCommand'] = request.sub_command
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
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.sub_command):
            body['subCommand'] = request.sub_command
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_job_with_options(task_id, request, headers, runtime)

    async def create_job_async(
        self,
        task_id: str,
        request: ia_cservice_20210806_models.CreateJobRequest,
    ) -> ia_cservice_20210806_models.CreateJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_job_with_options_async(task_id, request, headers, runtime)

    def create_module_with_options(
        self,
        request: ia_cservice_20210806_models.CreateModuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.CreateModuleResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_module_with_options(request, headers, runtime)

    async def create_module_async(
        self,
        request: ia_cservice_20210806_models.CreateModuleRequest,
    ) -> ia_cservice_20210806_models.CreateModuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_module_with_options_async(request, headers, runtime)

    def create_module_market_with_options(
        self,
        request: ia_cservice_20210806_models.CreateModuleMarketRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.CreateModuleMarketResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.code_url):
            body['codeUrl'] = request.code_url
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.module_detail):
            body['moduleDetail'] = request.module_detail
        if not UtilClient.is_unset(request.module_id):
            body['moduleId'] = request.module_id
        if not UtilClient.is_unset(request.module_version):
            body['moduleVersion'] = request.module_version
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateModuleMarket',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/moduleMarkets',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.CreateModuleMarketResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_module_market_with_options_async(
        self,
        request: ia_cservice_20210806_models.CreateModuleMarketRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.CreateModuleMarketResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.code_url):
            body['codeUrl'] = request.code_url
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.module_detail):
            body['moduleDetail'] = request.module_detail
        if not UtilClient.is_unset(request.module_id):
            body['moduleId'] = request.module_id
        if not UtilClient.is_unset(request.module_version):
            body['moduleVersion'] = request.module_version
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateModuleMarket',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/moduleMarkets',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.CreateModuleMarketResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_module_market(
        self,
        request: ia_cservice_20210806_models.CreateModuleMarketRequest,
    ) -> ia_cservice_20210806_models.CreateModuleMarketResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_module_market_with_options(request, headers, runtime)

    async def create_module_market_async(
        self,
        request: ia_cservice_20210806_models.CreateModuleMarketRequest,
    ) -> ia_cservice_20210806_models.CreateModuleMarketResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_module_market_with_options_async(request, headers, runtime)

    def create_module_version_with_options(
        self,
        module_id: str,
        request: ia_cservice_20210806_models.CreateModuleVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.CreateModuleVersionResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_module_version_with_options(module_id, request, headers, runtime)

    async def create_module_version_async(
        self,
        module_id: str,
        request: ia_cservice_20210806_models.CreateModuleVersionRequest,
    ) -> ia_cservice_20210806_models.CreateModuleVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_module_version_with_options_async(module_id, request, headers, runtime)

    def create_parameter_set_with_options(
        self,
        request: ia_cservice_20210806_models.CreateParameterSetRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.CreateParameterSetResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_parameter_set_with_options(request, headers, runtime)

    async def create_parameter_set_async(
        self,
        request: ia_cservice_20210806_models.CreateParameterSetRequest,
    ) -> ia_cservice_20210806_models.CreateParameterSetResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_parameter_set_with_options_async(request, headers, runtime)

    def create_project_with_options(
        self,
        request: ia_cservice_20210806_models.CreateProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.CreateProjectResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_project_with_options(request, headers, runtime)

    async def create_project_async(
        self,
        request: ia_cservice_20210806_models.CreateProjectRequest,
    ) -> ia_cservice_20210806_models.CreateProjectResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_project_build_with_options(project_id, request, headers, runtime)

    async def create_project_build_async(
        self,
        project_id: str,
        request: ia_cservice_20210806_models.CreateProjectBuildRequest,
    ) -> ia_cservice_20210806_models.CreateProjectBuildResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_project_build_with_options_async(project_id, request, headers, runtime)

    def create_rabbitmq_publisher_with_options(
        self,
        request: ia_cservice_20210806_models.CreateRabbitmqPublisherRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.CreateRabbitmqPublisherResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_rabbitmq_publisher_with_options(request, headers, runtime)

    async def create_rabbitmq_publisher_async(
        self,
        request: ia_cservice_20210806_models.CreateRabbitmqPublisherRequest,
    ) -> ia_cservice_20210806_models.CreateRabbitmqPublisherResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_rabbitmq_publisher_with_options_async(request, headers, runtime)

    def create_ram_policy_export_task_with_options(
        self,
        request: ia_cservice_20210806_models.CreateRamPolicyExportTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.CreateRamPolicyExportTaskResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_ram_policy_export_task_with_options(request, headers, runtime)

    async def create_ram_policy_export_task_async(
        self,
        request: ia_cservice_20210806_models.CreateRamPolicyExportTaskRequest,
    ) -> ia_cservice_20210806_models.CreateRamPolicyExportTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_ram_policy_export_task_with_options_async(request, headers, runtime)

    def create_resource_export_task_with_options(
        self,
        request: ia_cservice_20210806_models.CreateResourceExportTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.CreateResourceExportTaskResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
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
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_resource_export_task_with_options(request, headers, runtime)

    async def create_resource_export_task_async(
        self,
        request: ia_cservice_20210806_models.CreateResourceExportTaskRequest,
    ) -> ia_cservice_20210806_models.CreateResourceExportTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_resource_export_task_with_options_async(request, headers, runtime)

    def create_task_with_options(
        self,
        request: ia_cservice_20210806_models.CreateTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.CreateTaskResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_task_with_options(request, headers, runtime)

    async def create_task_async(
        self,
        request: ia_cservice_20210806_models.CreateTaskRequest,
    ) -> ia_cservice_20210806_models.CreateTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_task_with_options_async(request, headers, runtime)

    def delete_authorization_with_options(
        self,
        authorization_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.DeleteAuthorizationResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_authorization_with_options(authorization_id, headers, runtime)

    async def delete_authorization_async(
        self,
        authorization_id: str,
    ) -> ia_cservice_20210806_models.DeleteAuthorizationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_authorization_with_options_async(authorization_id, headers, runtime)

    def delete_group_with_options(
        self,
        group_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.DeleteGroupResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_group_with_options(group_id, headers, runtime)

    async def delete_group_async(
        self,
        group_id: str,
    ) -> ia_cservice_20210806_models.DeleteGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_group_with_options_async(group_id, headers, runtime)

    def delete_module_with_options(
        self,
        module_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.DeleteModuleResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_module_with_options(module_id, headers, runtime)

    async def delete_module_async(
        self,
        module_id: str,
    ) -> ia_cservice_20210806_models.DeleteModuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_module_with_options_async(module_id, headers, runtime)

    def delete_parameter_set_with_options(
        self,
        parameter_set_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.DeleteParameterSetResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_parameter_set_with_options(parameter_set_id, headers, runtime)

    async def delete_parameter_set_async(
        self,
        parameter_set_id: str,
    ) -> ia_cservice_20210806_models.DeleteParameterSetResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_parameter_set_with_options_async(parameter_set_id, headers, runtime)

    def delete_project_with_options(
        self,
        project_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.DeleteProjectResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_project_with_options(project_id, headers, runtime)

    async def delete_project_async(
        self,
        project_id: str,
    ) -> ia_cservice_20210806_models.DeleteProjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_project_with_options_async(project_id, headers, runtime)

    def delete_rabbitmq_publisher_with_options(
        self,
        publisher_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.DeleteRabbitmqPublisherResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_rabbitmq_publisher_with_options(publisher_id, headers, runtime)

    async def delete_rabbitmq_publisher_async(
        self,
        publisher_id: str,
    ) -> ia_cservice_20210806_models.DeleteRabbitmqPublisherResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_rabbitmq_publisher_with_options_async(publisher_id, headers, runtime)

    def delete_ram_policy_export_task_with_options(
        self,
        ram_policy_export_task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.DeleteRamPolicyExportTaskResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_ram_policy_export_task_with_options(ram_policy_export_task_id, headers, runtime)

    async def delete_ram_policy_export_task_async(
        self,
        ram_policy_export_task_id: str,
    ) -> ia_cservice_20210806_models.DeleteRamPolicyExportTaskResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_ram_policy_export_task_version_with_options(ram_policy_export_task_id, export_version, headers, runtime)

    async def delete_ram_policy_export_task_version_async(
        self,
        ram_policy_export_task_id: str,
        export_version: str,
    ) -> ia_cservice_20210806_models.DeleteRamPolicyExportTaskVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_ram_policy_export_task_version_with_options_async(ram_policy_export_task_id, export_version, headers, runtime)

    def delete_resource_export_task_with_options(
        self,
        export_task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.DeleteResourceExportTaskResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_resource_export_task_with_options(export_task_id, headers, runtime)

    async def delete_resource_export_task_async(
        self,
        export_task_id: str,
    ) -> ia_cservice_20210806_models.DeleteResourceExportTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_resource_export_task_with_options_async(export_task_id, headers, runtime)

    def delete_scene_testing_task_with_options(
        self,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.DeleteSceneTestingTaskResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_scene_testing_task_with_options(task_id, headers, runtime)

    async def delete_scene_testing_task_async(
        self,
        task_id: str,
    ) -> ia_cservice_20210806_models.DeleteSceneTestingTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_scene_testing_task_with_options_async(task_id, headers, runtime)

    def delete_task_with_options(
        self,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.DeleteTaskResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_task_with_options(task_id, headers, runtime)

    async def delete_task_async(
        self,
        task_id: str,
    ) -> ia_cservice_20210806_models.DeleteTaskResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.detach_rabbitmq_publisher_with_options(publisher_id, request, headers, runtime)

    async def detach_rabbitmq_publisher_async(
        self,
        publisher_id: str,
        request: ia_cservice_20210806_models.DetachRabbitmqPublisherRequest,
    ) -> ia_cservice_20210806_models.DetachRabbitmqPublisherResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.dissociate_group_with_options(project_id, group_id, request, headers, runtime)

    async def dissociate_group_async(
        self,
        project_id: str,
        group_id: str,
        request: ia_cservice_20210806_models.DissociateGroupRequest,
    ) -> ia_cservice_20210806_models.DissociateGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.dissociate_group_with_options_async(project_id, group_id, request, headers, runtime)

    def dissociate_parameter_set_with_options(
        self,
        request: ia_cservice_20210806_models.DissociateParameterSetRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.DissociateParameterSetResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.dissociate_parameter_set_with_options(request, headers, runtime)

    async def dissociate_parameter_set_async(
        self,
        request: ia_cservice_20210806_models.DissociateParameterSetRequest,
    ) -> ia_cservice_20210806_models.DissociateParameterSetResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.dissociate_parameter_set_with_options_async(request, headers, runtime)

    def execute_ram_policy_export_task_with_options(
        self,
        ram_policy_export_task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ExecuteRamPolicyExportTaskResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.execute_ram_policy_export_task_with_options(ram_policy_export_task_id, headers, runtime)

    async def execute_ram_policy_export_task_async(
        self,
        ram_policy_export_task_id: str,
    ) -> ia_cservice_20210806_models.ExecuteRamPolicyExportTaskResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.execute_resource_export_task_with_options(export_task_id, request, headers, runtime)

    async def execute_resource_export_task_async(
        self,
        export_task_id: str,
        request: ia_cservice_20210806_models.ExecuteResourceExportTaskRequest,
    ) -> ia_cservice_20210806_models.ExecuteResourceExportTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.execute_resource_export_task_with_options_async(export_task_id, request, headers, runtime)

    def get_group_with_options(
        self,
        group_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.GetGroupResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_group_with_options(group_id, headers, runtime)

    async def get_group_async(
        self,
        group_id: str,
    ) -> ia_cservice_20210806_models.GetGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_group_with_options_async(group_id, headers, runtime)

    def get_job_with_options(
        self,
        task_id: str,
        job_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.GetJobResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
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
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.GetJobResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
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
    ) -> ia_cservice_20210806_models.GetJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_job_with_options(task_id, job_id, headers, runtime)

    async def get_job_async(
        self,
        task_id: str,
        job_id: str,
    ) -> ia_cservice_20210806_models.GetJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_job_with_options_async(task_id, job_id, headers, runtime)

    def get_module_with_options(
        self,
        module_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.GetModuleResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_module_with_options(module_id, headers, runtime)

    async def get_module_async(
        self,
        module_id: str,
    ) -> ia_cservice_20210806_models.GetModuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_module_with_options_async(module_id, headers, runtime)

    def get_module_market_with_options(
        self,
        module_market_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.GetModuleMarketResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetModuleMarket',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/moduleMarkets/{OpenApiUtilClient.get_encode_param(module_market_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GetModuleMarketResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_module_market_with_options_async(
        self,
        module_market_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.GetModuleMarketResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetModuleMarket',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/moduleMarkets/{OpenApiUtilClient.get_encode_param(module_market_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GetModuleMarketResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_module_market(
        self,
        module_market_id: str,
    ) -> ia_cservice_20210806_models.GetModuleMarketResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_module_market_with_options(module_market_id, headers, runtime)

    async def get_module_market_async(
        self,
        module_market_id: str,
    ) -> ia_cservice_20210806_models.GetModuleMarketResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_module_market_with_options_async(module_market_id, headers, runtime)

    def get_module_version_with_options(
        self,
        module_id: str,
        module_version: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.GetModuleVersionResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_module_version_with_options(module_id, module_version, headers, runtime)

    async def get_module_version_async(
        self,
        module_id: str,
        module_version: str,
    ) -> ia_cservice_20210806_models.GetModuleVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_module_version_with_options_async(module_id, module_version, headers, runtime)

    def get_parameter_set_with_options(
        self,
        parameter_set_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.GetParameterSetResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_parameter_set_with_options(parameter_set_id, headers, runtime)

    async def get_parameter_set_async(
        self,
        parameter_set_id: str,
    ) -> ia_cservice_20210806_models.GetParameterSetResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_parameter_set_with_options_async(parameter_set_id, headers, runtime)

    def get_project_with_options(
        self,
        project_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.GetProjectResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_project_with_options(project_id, headers, runtime)

    async def get_project_async(
        self,
        project_id: str,
    ) -> ia_cservice_20210806_models.GetProjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_project_with_options_async(project_id, headers, runtime)

    def get_project_build_config_with_options(
        self,
        project_id: str,
        request: ia_cservice_20210806_models.GetProjectBuildConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.GetProjectBuildConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_build_id):
            query['projectBuildId'] = request.project_build_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProjectBuildConfig',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/project/{OpenApiUtilClient.get_encode_param(project_id)}/buildConfig',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GetProjectBuildConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_project_build_config_with_options_async(
        self,
        project_id: str,
        request: ia_cservice_20210806_models.GetProjectBuildConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.GetProjectBuildConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_build_id):
            query['projectBuildId'] = request.project_build_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProjectBuildConfig',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/project/{OpenApiUtilClient.get_encode_param(project_id)}/buildConfig',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GetProjectBuildConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_project_build_config(
        self,
        project_id: str,
        request: ia_cservice_20210806_models.GetProjectBuildConfigRequest,
    ) -> ia_cservice_20210806_models.GetProjectBuildConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_project_build_config_with_options(project_id, request, headers, runtime)

    async def get_project_build_config_async(
        self,
        project_id: str,
        request: ia_cservice_20210806_models.GetProjectBuildConfigRequest,
    ) -> ia_cservice_20210806_models.GetProjectBuildConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_project_build_config_with_options_async(project_id, request, headers, runtime)

    def get_project_build_context_with_options(
        self,
        project_id: str,
        project_build_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.GetProjectBuildContextResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
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
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.GetProjectBuildContextResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
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
    ) -> ia_cservice_20210806_models.GetProjectBuildContextResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_project_build_context_with_options(project_id, project_build_id, headers, runtime)

    async def get_project_build_context_async(
        self,
        project_id: str,
        project_build_id: str,
    ) -> ia_cservice_20210806_models.GetProjectBuildContextResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_project_build_context_with_options_async(project_id, project_build_id, headers, runtime)

    def get_project_job_summary_with_options(
        self,
        project_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.GetProjectJobSummaryResponse:
        """
        @deprecated
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetProjectJobSummaryResponse
        Deprecated
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetProjectJobSummary',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/project/{OpenApiUtilClient.get_encode_param(project_id)}/job/statistics',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GetProjectJobSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_project_job_summary_with_options_async(
        self,
        project_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.GetProjectJobSummaryResponse:
        """
        @deprecated
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetProjectJobSummaryResponse
        Deprecated
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetProjectJobSummary',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/project/{OpenApiUtilClient.get_encode_param(project_id)}/job/statistics',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GetProjectJobSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_project_job_summary(
        self,
        project_id: str,
    ) -> ia_cservice_20210806_models.GetProjectJobSummaryResponse:
        """
        @deprecated
        
        @return: GetProjectJobSummaryResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_project_job_summary_with_options(project_id, headers, runtime)

    async def get_project_job_summary_async(
        self,
        project_id: str,
    ) -> ia_cservice_20210806_models.GetProjectJobSummaryResponse:
        """
        @deprecated
        
        @return: GetProjectJobSummaryResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_project_job_summary_with_options_async(project_id, headers, runtime)

    def get_project_resource_summary_with_options(
        self,
        project_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.GetProjectResourceSummaryResponse:
        """
        @deprecated
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetProjectResourceSummaryResponse
        Deprecated
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetProjectResourceSummary',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/project/{OpenApiUtilClient.get_encode_param(project_id)}/resource/statistics',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GetProjectResourceSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_project_resource_summary_with_options_async(
        self,
        project_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.GetProjectResourceSummaryResponse:
        """
        @deprecated
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetProjectResourceSummaryResponse
        Deprecated
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetProjectResourceSummary',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/project/{OpenApiUtilClient.get_encode_param(project_id)}/resource/statistics',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GetProjectResourceSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_project_resource_summary(
        self,
        project_id: str,
    ) -> ia_cservice_20210806_models.GetProjectResourceSummaryResponse:
        """
        @deprecated
        
        @return: GetProjectResourceSummaryResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_project_resource_summary_with_options(project_id, headers, runtime)

    async def get_project_resource_summary_async(
        self,
        project_id: str,
    ) -> ia_cservice_20210806_models.GetProjectResourceSummaryResponse:
        """
        @deprecated
        
        @return: GetProjectResourceSummaryResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_project_resource_summary_with_options_async(project_id, headers, runtime)

    def get_rabbitmq_publisher_with_options(
        self,
        publisher_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.GetRabbitmqPublisherResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_rabbitmq_publisher_with_options(publisher_id, headers, runtime)

    async def get_rabbitmq_publisher_async(
        self,
        publisher_id: str,
    ) -> ia_cservice_20210806_models.GetRabbitmqPublisherResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_rabbitmq_publisher_with_options_async(publisher_id, headers, runtime)

    def get_ram_policy_export_task_with_options(
        self,
        ram_policy_export_task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.GetRamPolicyExportTaskResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_ram_policy_export_task_with_options(ram_policy_export_task_id, headers, runtime)

    async def get_ram_policy_export_task_async(
        self,
        ram_policy_export_task_id: str,
    ) -> ia_cservice_20210806_models.GetRamPolicyExportTaskResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_ram_policy_export_task_version_with_options(ram_policy_export_task_id, export_version, headers, runtime)

    async def get_ram_policy_export_task_version_async(
        self,
        ram_policy_export_task_id: str,
        export_version: str,
    ) -> ia_cservice_20210806_models.GetRamPolicyExportTaskVersionResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_resource_export_task_with_options(export_task_id, request, headers, runtime)

    async def get_resource_export_task_async(
        self,
        export_task_id: str,
        request: ia_cservice_20210806_models.GetResourceExportTaskRequest,
    ) -> ia_cservice_20210806_models.GetResourceExportTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_resource_export_task_with_options_async(export_task_id, request, headers, runtime)

    def get_task_with_options(
        self,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.GetTaskResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_task_with_options(task_id, headers, runtime)

    async def get_task_async(
        self,
        task_id: str,
    ) -> ia_cservice_20210806_models.GetTaskResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_task_policy_with_options(group_id, request, headers, runtime)

    async def get_task_policy_async(
        self,
        group_id: str,
        request: ia_cservice_20210806_models.GetTaskPolicyRequest,
    ) -> ia_cservice_20210806_models.GetTaskPolicyResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_task_policy_with_options_async(group_id, request, headers, runtime)

    def list_authorizations_with_options(
        self,
        request: ia_cservice_20210806_models.ListAuthorizationsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListAuthorizationsResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_authorizations_with_options(request, headers, runtime)

    async def list_authorizations_async(
        self,
        request: ia_cservice_20210806_models.ListAuthorizationsRequest,
    ) -> ia_cservice_20210806_models.ListAuthorizationsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_authorizations_with_options_async(request, headers, runtime)

    def list_available_terraform_versions_with_options(
        self,
        request: ia_cservice_20210806_models.ListAvailableTerraformVersionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListAvailableTerraformVersionsResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_available_terraform_versions_with_options(request, headers, runtime)

    async def list_available_terraform_versions_async(
        self,
        request: ia_cservice_20210806_models.ListAvailableTerraformVersionsRequest,
    ) -> ia_cservice_20210806_models.ListAvailableTerraformVersionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_available_terraform_versions_with_options_async(request, headers, runtime)

    def list_group_with_options(
        self,
        request: ia_cservice_20210806_models.ListGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['projectId'] = request.project_id
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
        request: ia_cservice_20210806_models.ListGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['projectId'] = request.project_id
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_group_with_options(request, headers, runtime)

    async def list_group_async(
        self,
        request: ia_cservice_20210806_models.ListGroupRequest,
    ) -> ia_cservice_20210806_models.ListGroupResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_jobs_with_options(task_id, request, headers, runtime)

    async def list_jobs_async(
        self,
        task_id: str,
        request: ia_cservice_20210806_models.ListJobsRequest,
    ) -> ia_cservice_20210806_models.ListJobsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_jobs_with_options_async(task_id, request, headers, runtime)

    def list_module_markets_with_options(
        self,
        request: ia_cservice_20210806_models.ListModuleMarketsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListModuleMarketsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListModuleMarkets',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/moduleMarkets',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListModuleMarketsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_module_markets_with_options_async(
        self,
        request: ia_cservice_20210806_models.ListModuleMarketsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListModuleMarketsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListModuleMarkets',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/moduleMarkets',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListModuleMarketsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_module_markets(
        self,
        request: ia_cservice_20210806_models.ListModuleMarketsRequest,
    ) -> ia_cservice_20210806_models.ListModuleMarketsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_module_markets_with_options(request, headers, runtime)

    async def list_module_markets_async(
        self,
        request: ia_cservice_20210806_models.ListModuleMarketsRequest,
    ) -> ia_cservice_20210806_models.ListModuleMarketsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_module_markets_with_options_async(request, headers, runtime)

    def list_module_version_with_options(
        self,
        module_id: str,
        request: ia_cservice_20210806_models.ListModuleVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListModuleVersionResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_module_version_with_options(module_id, request, headers, runtime)

    async def list_module_version_async(
        self,
        module_id: str,
        request: ia_cservice_20210806_models.ListModuleVersionRequest,
    ) -> ia_cservice_20210806_models.ListModuleVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_module_version_with_options_async(module_id, request, headers, runtime)

    def list_modules_with_options(
        self,
        request: ia_cservice_20210806_models.ListModulesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListModulesResponse:
        UtilClient.validate_model(request)
        query = {}
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
        request: ia_cservice_20210806_models.ListModulesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListModulesResponse:
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_modules_with_options(request, headers, runtime)

    async def list_modules_async(
        self,
        request: ia_cservice_20210806_models.ListModulesRequest,
    ) -> ia_cservice_20210806_models.ListModulesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_modules_with_options_async(request, headers, runtime)

    def list_parameter_set_relation_with_options(
        self,
        request: ia_cservice_20210806_models.ListParameterSetRelationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListParameterSetRelationResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_parameter_set_relation_with_options(request, headers, runtime)

    async def list_parameter_set_relation_async(
        self,
        request: ia_cservice_20210806_models.ListParameterSetRelationRequest,
    ) -> ia_cservice_20210806_models.ListParameterSetRelationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_parameter_set_relation_with_options_async(request, headers, runtime)

    def list_parameter_sets_with_options(
        self,
        request: ia_cservice_20210806_models.ListParameterSetsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListParameterSetsResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_parameter_sets_with_options(request, headers, runtime)

    async def list_parameter_sets_async(
        self,
        request: ia_cservice_20210806_models.ListParameterSetsRequest,
    ) -> ia_cservice_20210806_models.ListParameterSetsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_parameter_sets_with_options_async(request, headers, runtime)

    def list_project_with_options(
        self,
        request: ia_cservice_20210806_models.ListProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
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
        request: ia_cservice_20210806_models.ListProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_project_with_options(request, headers, runtime)

    async def list_project_async(
        self,
        request: ia_cservice_20210806_models.ListProjectRequest,
    ) -> ia_cservice_20210806_models.ListProjectResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_project_builds_with_options(project_id, request, headers, runtime)

    async def list_project_builds_async(
        self,
        project_id: str,
        request: ia_cservice_20210806_models.ListProjectBuildsRequest,
    ) -> ia_cservice_20210806_models.ListProjectBuildsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_project_builds_with_options_async(project_id, request, headers, runtime)

    def list_rabbitmq_publishers_with_options(
        self,
        request: ia_cservice_20210806_models.ListRabbitmqPublishersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListRabbitmqPublishersResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_rabbitmq_publishers_with_options(request, headers, runtime)

    async def list_rabbitmq_publishers_async(
        self,
        request: ia_cservice_20210806_models.ListRabbitmqPublishersRequest,
    ) -> ia_cservice_20210806_models.ListRabbitmqPublishersResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_ram_policy_export_task_versions_with_options(ram_policy_export_task_id, request, headers, runtime)

    async def list_ram_policy_export_task_versions_async(
        self,
        ram_policy_export_task_id: str,
        request: ia_cservice_20210806_models.ListRamPolicyExportTaskVersionsRequest,
    ) -> ia_cservice_20210806_models.ListRamPolicyExportTaskVersionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_ram_policy_export_task_versions_with_options_async(ram_policy_export_task_id, request, headers, runtime)

    def list_ram_policy_export_tasks_with_options(
        self,
        request: ia_cservice_20210806_models.ListRamPolicyExportTasksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListRamPolicyExportTasksResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_ram_policy_export_tasks_with_options(request, headers, runtime)

    async def list_ram_policy_export_tasks_async(
        self,
        request: ia_cservice_20210806_models.ListRamPolicyExportTasksRequest,
    ) -> ia_cservice_20210806_models.ListRamPolicyExportTasksResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_resource_export_task_versions_with_options(export_task_id, request, headers, runtime)

    async def list_resource_export_task_versions_async(
        self,
        export_task_id: str,
        request: ia_cservice_20210806_models.ListResourceExportTaskVersionsRequest,
    ) -> ia_cservice_20210806_models.ListResourceExportTaskVersionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_resource_export_task_versions_with_options_async(export_task_id, request, headers, runtime)

    def list_resource_export_tasks_with_options(
        self,
        request: ia_cservice_20210806_models.ListResourceExportTasksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListResourceExportTasksResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_resource_export_tasks_with_options(request, headers, runtime)

    async def list_resource_export_tasks_async(
        self,
        request: ia_cservice_20210806_models.ListResourceExportTasksRequest,
    ) -> ia_cservice_20210806_models.ListResourceExportTasksResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_resource_export_tasks_with_options_async(request, headers, runtime)

    def list_resources_with_options(
        self,
        request: ia_cservice_20210806_models.ListResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListResourcesResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_resources_with_options(request, headers, runtime)

    async def list_resources_async(
        self,
        request: ia_cservice_20210806_models.ListResourcesRequest,
    ) -> ia_cservice_20210806_models.ListResourcesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_resources_with_options_async(request, headers, runtime)

    def list_task_resource_with_options(
        self,
        task_id: str,
        request: ia_cservice_20210806_models.ListTaskResourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListTaskResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTaskResource',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/tasks/{OpenApiUtilClient.get_encode_param(task_id)}/resources',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListTaskResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_task_resource_with_options_async(
        self,
        task_id: str,
        request: ia_cservice_20210806_models.ListTaskResourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListTaskResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTaskResource',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/tasks/{OpenApiUtilClient.get_encode_param(task_id)}/resources',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListTaskResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_task_resource(
        self,
        task_id: str,
        request: ia_cservice_20210806_models.ListTaskResourceRequest,
    ) -> ia_cservice_20210806_models.ListTaskResourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_task_resource_with_options(task_id, request, headers, runtime)

    async def list_task_resource_async(
        self,
        task_id: str,
        request: ia_cservice_20210806_models.ListTaskResourceRequest,
    ) -> ia_cservice_20210806_models.ListTaskResourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_task_resource_with_options_async(task_id, request, headers, runtime)

    def list_tasks_with_options(
        self,
        request: ia_cservice_20210806_models.ListTasksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListTasksResponse:
        UtilClient.validate_model(request)
        query = {}
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
        request: ia_cservice_20210806_models.ListTasksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListTasksResponse:
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_tasks_with_options(request, headers, runtime)

    async def list_tasks_async(
        self,
        request: ia_cservice_20210806_models.ListTasksRequest,
    ) -> ia_cservice_20210806_models.ListTasksResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_tasks_with_options_async(request, headers, runtime)

    def list_terraform_provider_versions_with_options(
        self,
        request: ia_cservice_20210806_models.ListTerraformProviderVersionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListTerraformProviderVersionsResponse:
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
            action='ListTerraformProviderVersions',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/version/terraform/provider',
            method='GET',
            auth_type='AK',
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
            action='ListTerraformProviderVersions',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/version/terraform/provider',
            method='GET',
            auth_type='AK',
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_terraform_provider_versions_with_options(request, headers, runtime)

    async def list_terraform_provider_versions_async(
        self,
        request: ia_cservice_20210806_models.ListTerraformProviderVersionsRequest,
    ) -> ia_cservice_20210806_models.ListTerraformProviderVersionsResponse:
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.comment):
            query['comment'] = request.comment
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.comment):
            query['comment'] = request.comment
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.remove_resource_export_task_version_with_options(export_task_id, export_version, headers, runtime)

    async def remove_resource_export_task_version_async(
        self,
        export_task_id: str,
        export_version: str,
    ) -> ia_cservice_20210806_models.RemoveResourceExportTaskVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.remove_resource_export_task_version_with_options_async(export_task_id, export_version, headers, runtime)

    def update_authorization_attribute_with_options(
        self,
        authorization_id: str,
        request: ia_cservice_20210806_models.UpdateAuthorizationAttributeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.UpdateAuthorizationAttributeResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_authorization_attribute_with_options(authorization_id, request, headers, runtime)

    async def update_authorization_attribute_async(
        self,
        authorization_id: str,
        request: ia_cservice_20210806_models.UpdateAuthorizationAttributeRequest,
    ) -> ia_cservice_20210806_models.UpdateAuthorizationAttributeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_authorization_attribute_with_options_async(authorization_id, request, headers, runtime)

    def update_group_with_options(
        self,
        group_id: str,
        request: ia_cservice_20210806_models.UpdateGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.UpdateGroupResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_group_with_options(group_id, request, headers, runtime)

    async def update_group_async(
        self,
        group_id: str,
        request: ia_cservice_20210806_models.UpdateGroupRequest,
    ) -> ia_cservice_20210806_models.UpdateGroupResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_module_attribute_with_options(module_id, request, headers, runtime)

    async def update_module_attribute_async(
        self,
        module_id: str,
        request: ia_cservice_20210806_models.UpdateModuleAttributeRequest,
    ) -> ia_cservice_20210806_models.UpdateModuleAttributeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_module_attribute_with_options_async(module_id, request, headers, runtime)

    def update_module_market_attribute_with_options(
        self,
        module_market_id: str,
        request: ia_cservice_20210806_models.UpdateModuleMarketAttributeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.UpdateModuleMarketAttributeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.module_detail):
            body['moduleDetail'] = request.module_detail
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateModuleMarketAttribute',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/moduleMarkets/{OpenApiUtilClient.get_encode_param(module_market_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.UpdateModuleMarketAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_module_market_attribute_with_options_async(
        self,
        module_market_id: str,
        request: ia_cservice_20210806_models.UpdateModuleMarketAttributeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.UpdateModuleMarketAttributeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.module_detail):
            body['moduleDetail'] = request.module_detail
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateModuleMarketAttribute',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/moduleMarkets/{OpenApiUtilClient.get_encode_param(module_market_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.UpdateModuleMarketAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_module_market_attribute(
        self,
        module_market_id: str,
        request: ia_cservice_20210806_models.UpdateModuleMarketAttributeRequest,
    ) -> ia_cservice_20210806_models.UpdateModuleMarketAttributeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_module_market_attribute_with_options(module_market_id, request, headers, runtime)

    async def update_module_market_attribute_async(
        self,
        module_market_id: str,
        request: ia_cservice_20210806_models.UpdateModuleMarketAttributeRequest,
    ) -> ia_cservice_20210806_models.UpdateModuleMarketAttributeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_module_market_attribute_with_options_async(module_market_id, request, headers, runtime)

    def update_parameter_set_attribute_with_options(
        self,
        parameter_set_id: str,
        request: ia_cservice_20210806_models.UpdateParameterSetAttributeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.UpdateParameterSetAttributeResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_parameter_set_attribute_with_options(parameter_set_id, request, headers, runtime)

    async def update_parameter_set_attribute_async(
        self,
        parameter_set_id: str,
        request: ia_cservice_20210806_models.UpdateParameterSetAttributeRequest,
    ) -> ia_cservice_20210806_models.UpdateParameterSetAttributeResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_project_with_options(project_id, request, headers, runtime)

    async def update_project_async(
        self,
        project_id: str,
        request: ia_cservice_20210806_models.UpdateProjectRequest,
    ) -> ia_cservice_20210806_models.UpdateProjectResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_rabbitmq_publisher_attribute_with_options(publisher_id, request, headers, runtime)

    async def update_rabbitmq_publisher_attribute_async(
        self,
        publisher_id: str,
        request: ia_cservice_20210806_models.UpdateRabbitmqPublisherAttributeRequest,
    ) -> ia_cservice_20210806_models.UpdateRabbitmqPublisherAttributeResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_ram_policy_export_task_attribute_with_options(ram_policy_export_task_id, request, headers, runtime)

    async def update_ram_policy_export_task_attribute_async(
        self,
        ram_policy_export_task_id: str,
        request: ia_cservice_20210806_models.UpdateRamPolicyExportTaskAttributeRequest,
    ) -> ia_cservice_20210806_models.UpdateRamPolicyExportTaskAttributeResponse:
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
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
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
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_resource_export_task_attribute_with_options(export_task_id, request, headers, runtime)

    async def update_resource_export_task_attribute_async(
        self,
        export_task_id: str,
        request: ia_cservice_20210806_models.UpdateResourceExportTaskAttributeRequest,
    ) -> ia_cservice_20210806_models.UpdateResourceExportTaskAttributeResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_task_attribute_with_options(task_id, request, headers, runtime)

    async def update_task_attribute_async(
        self,
        task_id: str,
        request: ia_cservice_20210806_models.UpdateTaskAttributeRequest,
    ) -> ia_cservice_20210806_models.UpdateTaskAttributeResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_task_policy_with_options(group_id, request, headers, runtime)

    async def update_task_policy_async(
        self,
        group_id: str,
        request: ia_cservice_20210806_models.UpdateTaskPolicyRequest,
    ) -> ia_cservice_20210806_models.UpdateTaskPolicyResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_task_policy_with_options_async(group_id, request, headers, runtime)
