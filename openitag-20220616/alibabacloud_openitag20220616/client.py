# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_openitag20220616 import models as open_itag_20220616_models
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
        self._endpoint = self.get_endpoint('openitag', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_work_node_workforce(
        self,
        tenant_id: str,
        task_id: str,
        work_node_id: str,
        request: open_itag_20220616_models.AddWorkNodeWorkforceRequest,
    ) -> open_itag_20220616_models.AddWorkNodeWorkforceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_work_node_workforce_with_options(tenant_id, task_id, work_node_id, request, headers, runtime)

    async def add_work_node_workforce_async(
        self,
        tenant_id: str,
        task_id: str,
        work_node_id: str,
        request: open_itag_20220616_models.AddWorkNodeWorkforceRequest,
    ) -> open_itag_20220616_models.AddWorkNodeWorkforceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.add_work_node_workforce_with_options_async(tenant_id, task_id, work_node_id, request, headers, runtime)

    def add_work_node_workforce_with_options(
        self,
        tenant_id: str,
        task_id: str,
        work_node_id: str,
        request: open_itag_20220616_models.AddWorkNodeWorkforceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_itag_20220616_models.AddWorkNodeWorkforceResponse:
        UtilClient.validate_model(request)
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        task_id = OpenApiUtilClient.get_encode_param(task_id)
        work_node_id = OpenApiUtilClient.get_encode_param(work_node_id)
        body = {}
        if not UtilClient.is_unset(request.user_ids):
            body['UserIds'] = request.user_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddWorkNodeWorkforce',
            version='2022-06-16',
            protocol='HTTPS',
            pathname=f'/openapi/api/v1/tenants/{tenant_id}/tasks/{task_id}/worknodes/{work_node_id}/workforce',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.AddWorkNodeWorkforceResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_work_node_workforce_with_options_async(
        self,
        tenant_id: str,
        task_id: str,
        work_node_id: str,
        request: open_itag_20220616_models.AddWorkNodeWorkforceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_itag_20220616_models.AddWorkNodeWorkforceResponse:
        UtilClient.validate_model(request)
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        task_id = OpenApiUtilClient.get_encode_param(task_id)
        work_node_id = OpenApiUtilClient.get_encode_param(work_node_id)
        body = {}
        if not UtilClient.is_unset(request.user_ids):
            body['UserIds'] = request.user_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddWorkNodeWorkforce',
            version='2022-06-16',
            protocol='HTTPS',
            pathname=f'/openapi/api/v1/tenants/{tenant_id}/tasks/{task_id}/worknodes/{work_node_id}/workforce',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.AddWorkNodeWorkforceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_task(
        self,
        tenant_id: str,
        request: open_itag_20220616_models.CreateTaskRequest,
    ) -> open_itag_20220616_models.CreateTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_task_with_options(tenant_id, request, headers, runtime)

    async def create_task_async(
        self,
        tenant_id: str,
        request: open_itag_20220616_models.CreateTaskRequest,
    ) -> open_itag_20220616_models.CreateTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_task_with_options_async(tenant_id, request, headers, runtime)

    def create_task_with_options(
        self,
        tenant_id: str,
        request: open_itag_20220616_models.CreateTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_itag_20220616_models.CreateTaskResponse:
        UtilClient.validate_model(request)
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.body))
        )
        params = open_api_models.Params(
            action='CreateTask',
            version='2022-06-16',
            protocol='HTTPS',
            pathname=f'/openapi/api/v1/tenants/{tenant_id}/tasks',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.CreateTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_task_with_options_async(
        self,
        tenant_id: str,
        request: open_itag_20220616_models.CreateTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_itag_20220616_models.CreateTaskResponse:
        UtilClient.validate_model(request)
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.body))
        )
        params = open_api_models.Params(
            action='CreateTask',
            version='2022-06-16',
            protocol='HTTPS',
            pathname=f'/openapi/api/v1/tenants/{tenant_id}/tasks',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.CreateTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_template(
        self,
        tenant_id: str,
        request: open_itag_20220616_models.CreateTemplateRequest,
    ) -> open_itag_20220616_models.CreateTemplateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_template_with_options(tenant_id, request, headers, runtime)

    async def create_template_async(
        self,
        tenant_id: str,
        request: open_itag_20220616_models.CreateTemplateRequest,
    ) -> open_itag_20220616_models.CreateTemplateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_template_with_options_async(tenant_id, request, headers, runtime)

    def create_template_with_options(
        self,
        tenant_id: str,
        request: open_itag_20220616_models.CreateTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_itag_20220616_models.CreateTemplateResponse:
        UtilClient.validate_model(request)
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.body))
        )
        params = open_api_models.Params(
            action='CreateTemplate',
            version='2022-06-16',
            protocol='HTTPS',
            pathname=f'/openapi/api/v1/tenants/{tenant_id}/templates',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.CreateTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_template_with_options_async(
        self,
        tenant_id: str,
        request: open_itag_20220616_models.CreateTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_itag_20220616_models.CreateTemplateResponse:
        UtilClient.validate_model(request)
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.body))
        )
        params = open_api_models.Params(
            action='CreateTemplate',
            version='2022-06-16',
            protocol='HTTPS',
            pathname=f'/openapi/api/v1/tenants/{tenant_id}/templates',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.CreateTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_user(
        self,
        tenant_id: str,
        request: open_itag_20220616_models.CreateUserRequest,
    ) -> open_itag_20220616_models.CreateUserResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_user_with_options(tenant_id, request, headers, runtime)

    async def create_user_async(
        self,
        tenant_id: str,
        request: open_itag_20220616_models.CreateUserRequest,
    ) -> open_itag_20220616_models.CreateUserResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_user_with_options_async(tenant_id, request, headers, runtime)

    def create_user_with_options(
        self,
        tenant_id: str,
        request: open_itag_20220616_models.CreateUserRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_itag_20220616_models.CreateUserResponse:
        UtilClient.validate_model(request)
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        body = {}
        if not UtilClient.is_unset(request.account_no):
            body['AccountNo'] = request.account_no
        if not UtilClient.is_unset(request.account_type):
            body['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.role):
            body['Role'] = request.role
        if not UtilClient.is_unset(request.user_name):
            body['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateUser',
            version='2022-06-16',
            protocol='HTTPS',
            pathname=f'/openapi/api/v1/tenants/{tenant_id}/users',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.CreateUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_user_with_options_async(
        self,
        tenant_id: str,
        request: open_itag_20220616_models.CreateUserRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_itag_20220616_models.CreateUserResponse:
        UtilClient.validate_model(request)
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        body = {}
        if not UtilClient.is_unset(request.account_no):
            body['AccountNo'] = request.account_no
        if not UtilClient.is_unset(request.account_type):
            body['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.role):
            body['Role'] = request.role
        if not UtilClient.is_unset(request.user_name):
            body['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateUser',
            version='2022-06-16',
            protocol='HTTPS',
            pathname=f'/openapi/api/v1/tenants/{tenant_id}/users',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.CreateUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_task(
        self,
        tenant_id: str,
        task_id: str,
    ) -> open_itag_20220616_models.DeleteTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_task_with_options(tenant_id, task_id, headers, runtime)

    async def delete_task_async(
        self,
        tenant_id: str,
        task_id: str,
    ) -> open_itag_20220616_models.DeleteTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_task_with_options_async(tenant_id, task_id, headers, runtime)

    def delete_task_with_options(
        self,
        tenant_id: str,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_itag_20220616_models.DeleteTaskResponse:
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        task_id = OpenApiUtilClient.get_encode_param(task_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteTask',
            version='2022-06-16',
            protocol='HTTPS',
            pathname=f'/openapi/api/v1/tenants/{tenant_id}/tasks/{task_id}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.DeleteTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_task_with_options_async(
        self,
        tenant_id: str,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_itag_20220616_models.DeleteTaskResponse:
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        task_id = OpenApiUtilClient.get_encode_param(task_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteTask',
            version='2022-06-16',
            protocol='HTTPS',
            pathname=f'/openapi/api/v1/tenants/{tenant_id}/tasks/{task_id}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.DeleteTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_template(
        self,
        tenant_id: str,
        template_id: str,
    ) -> open_itag_20220616_models.DeleteTemplateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_template_with_options(tenant_id, template_id, headers, runtime)

    async def delete_template_async(
        self,
        tenant_id: str,
        template_id: str,
    ) -> open_itag_20220616_models.DeleteTemplateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_template_with_options_async(tenant_id, template_id, headers, runtime)

    def delete_template_with_options(
        self,
        tenant_id: str,
        template_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_itag_20220616_models.DeleteTemplateResponse:
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        template_id = OpenApiUtilClient.get_encode_param(template_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteTemplate',
            version='2022-06-16',
            protocol='HTTPS',
            pathname=f'/openapi/api/v1/tenants/{tenant_id}/templates/{template_id}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.DeleteTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_template_with_options_async(
        self,
        tenant_id: str,
        template_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_itag_20220616_models.DeleteTemplateResponse:
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        template_id = OpenApiUtilClient.get_encode_param(template_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteTemplate',
            version='2022-06-16',
            protocol='HTTPS',
            pathname=f'/openapi/api/v1/tenants/{tenant_id}/templates/{template_id}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.DeleteTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_user(
        self,
        tenant_id: str,
        user_id: str,
    ) -> open_itag_20220616_models.DeleteUserResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_user_with_options(tenant_id, user_id, headers, runtime)

    async def delete_user_async(
        self,
        tenant_id: str,
        user_id: str,
    ) -> open_itag_20220616_models.DeleteUserResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_user_with_options_async(tenant_id, user_id, headers, runtime)

    def delete_user_with_options(
        self,
        tenant_id: str,
        user_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_itag_20220616_models.DeleteUserResponse:
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        user_id = OpenApiUtilClient.get_encode_param(user_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteUser',
            version='2022-06-16',
            protocol='HTTPS',
            pathname=f'/openapi/api/v1/tenants/{tenant_id}/users/{user_id}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.DeleteUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_user_with_options_async(
        self,
        tenant_id: str,
        user_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_itag_20220616_models.DeleteUserResponse:
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        user_id = OpenApiUtilClient.get_encode_param(user_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteUser',
            version='2022-06-16',
            protocol='HTTPS',
            pathname=f'/openapi/api/v1/tenants/{tenant_id}/users/{user_id}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.DeleteUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_annotations(
        self,
        tenant_id: str,
        task_id: str,
        request: open_itag_20220616_models.ExportAnnotationsRequest,
    ) -> open_itag_20220616_models.ExportAnnotationsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.export_annotations_with_options(tenant_id, task_id, request, headers, runtime)

    async def export_annotations_async(
        self,
        tenant_id: str,
        task_id: str,
        request: open_itag_20220616_models.ExportAnnotationsRequest,
    ) -> open_itag_20220616_models.ExportAnnotationsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.export_annotations_with_options_async(tenant_id, task_id, request, headers, runtime)

    def export_annotations_with_options(
        self,
        tenant_id: str,
        task_id: str,
        request: open_itag_20220616_models.ExportAnnotationsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_itag_20220616_models.ExportAnnotationsResponse:
        UtilClient.validate_model(request)
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        task_id = OpenApiUtilClient.get_encode_param(task_id)
        query = {}
        if not UtilClient.is_unset(request.oss_path):
            query['OssPath'] = request.oss_path
        if not UtilClient.is_unset(request.register_dataset):
            query['RegisterDataset'] = request.register_dataset
        if not UtilClient.is_unset(request.target):
            query['Target'] = request.target
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportAnnotations',
            version='2022-06-16',
            protocol='HTTPS',
            pathname=f'/openapi/api/v1/tenants/{tenant_id}/tasks/{task_id}/annotations/export',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.ExportAnnotationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_annotations_with_options_async(
        self,
        tenant_id: str,
        task_id: str,
        request: open_itag_20220616_models.ExportAnnotationsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_itag_20220616_models.ExportAnnotationsResponse:
        UtilClient.validate_model(request)
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        task_id = OpenApiUtilClient.get_encode_param(task_id)
        query = {}
        if not UtilClient.is_unset(request.oss_path):
            query['OssPath'] = request.oss_path
        if not UtilClient.is_unset(request.register_dataset):
            query['RegisterDataset'] = request.register_dataset
        if not UtilClient.is_unset(request.target):
            query['Target'] = request.target
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportAnnotations',
            version='2022-06-16',
            protocol='HTTPS',
            pathname=f'/openapi/api/v1/tenants/{tenant_id}/tasks/{task_id}/annotations/export',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.ExportAnnotationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_job(
        self,
        tenant_id: str,
        job_id: str,
        request: open_itag_20220616_models.GetJobRequest,
    ) -> open_itag_20220616_models.GetJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_job_with_options(tenant_id, job_id, request, headers, runtime)

    async def get_job_async(
        self,
        tenant_id: str,
        job_id: str,
        request: open_itag_20220616_models.GetJobRequest,
    ) -> open_itag_20220616_models.GetJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_job_with_options_async(tenant_id, job_id, request, headers, runtime)

    def get_job_with_options(
        self,
        tenant_id: str,
        job_id: str,
        request: open_itag_20220616_models.GetJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_itag_20220616_models.GetJobResponse:
        UtilClient.validate_model(request)
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        job_id = OpenApiUtilClient.get_encode_param(job_id)
        query = {}
        if not UtilClient.is_unset(request.job_type):
            query['JobType'] = request.job_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJob',
            version='2022-06-16',
            protocol='HTTPS',
            pathname=f'/openapi/api/v1/tenants/{tenant_id}/jobs/{job_id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.GetJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_job_with_options_async(
        self,
        tenant_id: str,
        job_id: str,
        request: open_itag_20220616_models.GetJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_itag_20220616_models.GetJobResponse:
        UtilClient.validate_model(request)
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        job_id = OpenApiUtilClient.get_encode_param(job_id)
        query = {}
        if not UtilClient.is_unset(request.job_type):
            query['JobType'] = request.job_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJob',
            version='2022-06-16',
            protocol='HTTPS',
            pathname=f'/openapi/api/v1/tenants/{tenant_id}/jobs/{job_id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.GetJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_subtask(
        self,
        tenant_id: str,
        task_id: str,
        subtask_id: str,
    ) -> open_itag_20220616_models.GetSubtaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_subtask_with_options(tenant_id, task_id, subtask_id, headers, runtime)

    async def get_subtask_async(
        self,
        tenant_id: str,
        task_id: str,
        subtask_id: str,
    ) -> open_itag_20220616_models.GetSubtaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_subtask_with_options_async(tenant_id, task_id, subtask_id, headers, runtime)

    def get_subtask_with_options(
        self,
        tenant_id: str,
        task_id: str,
        subtask_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_itag_20220616_models.GetSubtaskResponse:
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        task_id = OpenApiUtilClient.get_encode_param(task_id)
        subtask_id = OpenApiUtilClient.get_encode_param(subtask_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetSubtask',
            version='2022-06-16',
            protocol='HTTPS',
            pathname=f'/openapi/api/v1/tenants/{tenant_id}/tasks/{task_id}/subtasks/{subtask_id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.GetSubtaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_subtask_with_options_async(
        self,
        tenant_id: str,
        task_id: str,
        subtask_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_itag_20220616_models.GetSubtaskResponse:
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        task_id = OpenApiUtilClient.get_encode_param(task_id)
        subtask_id = OpenApiUtilClient.get_encode_param(subtask_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetSubtask',
            version='2022-06-16',
            protocol='HTTPS',
            pathname=f'/openapi/api/v1/tenants/{tenant_id}/tasks/{task_id}/subtasks/{subtask_id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.GetSubtaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_subtask_item(
        self,
        tenant_id: str,
        task_id: str,
        subtask_id: str,
        item_id: str,
    ) -> open_itag_20220616_models.GetSubtaskItemResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_subtask_item_with_options(tenant_id, task_id, subtask_id, item_id, headers, runtime)

    async def get_subtask_item_async(
        self,
        tenant_id: str,
        task_id: str,
        subtask_id: str,
        item_id: str,
    ) -> open_itag_20220616_models.GetSubtaskItemResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_subtask_item_with_options_async(tenant_id, task_id, subtask_id, item_id, headers, runtime)

    def get_subtask_item_with_options(
        self,
        tenant_id: str,
        task_id: str,
        subtask_id: str,
        item_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_itag_20220616_models.GetSubtaskItemResponse:
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        task_id = OpenApiUtilClient.get_encode_param(task_id)
        subtask_id = OpenApiUtilClient.get_encode_param(subtask_id)
        item_id = OpenApiUtilClient.get_encode_param(item_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetSubtaskItem',
            version='2022-06-16',
            protocol='HTTPS',
            pathname=f'/openapi/api/v1/tenants/{tenant_id}/tasks/{task_id}/subtasks/{subtask_id}/items/{item_id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.GetSubtaskItemResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_subtask_item_with_options_async(
        self,
        tenant_id: str,
        task_id: str,
        subtask_id: str,
        item_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_itag_20220616_models.GetSubtaskItemResponse:
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        task_id = OpenApiUtilClient.get_encode_param(task_id)
        subtask_id = OpenApiUtilClient.get_encode_param(subtask_id)
        item_id = OpenApiUtilClient.get_encode_param(item_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetSubtaskItem',
            version='2022-06-16',
            protocol='HTTPS',
            pathname=f'/openapi/api/v1/tenants/{tenant_id}/tasks/{task_id}/subtasks/{subtask_id}/items/{item_id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.GetSubtaskItemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_task(
        self,
        tenant_id: str,
        task_id: str,
    ) -> open_itag_20220616_models.GetTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_task_with_options(tenant_id, task_id, headers, runtime)

    async def get_task_async(
        self,
        tenant_id: str,
        task_id: str,
    ) -> open_itag_20220616_models.GetTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_task_with_options_async(tenant_id, task_id, headers, runtime)

    def get_task_with_options(
        self,
        tenant_id: str,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_itag_20220616_models.GetTaskResponse:
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        task_id = OpenApiUtilClient.get_encode_param(task_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTask',
            version='2022-06-16',
            protocol='HTTPS',
            pathname=f'/openapi/api/v1/tenants/{tenant_id}/tasks/{task_id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.GetTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_task_with_options_async(
        self,
        tenant_id: str,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_itag_20220616_models.GetTaskResponse:
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        task_id = OpenApiUtilClient.get_encode_param(task_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTask',
            version='2022-06-16',
            protocol='HTTPS',
            pathname=f'/openapi/api/v1/tenants/{tenant_id}/tasks/{task_id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.GetTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_task_statistics(
        self,
        tenant_id: str,
        task_id: str,
        request: open_itag_20220616_models.GetTaskStatisticsRequest,
    ) -> open_itag_20220616_models.GetTaskStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_task_statistics_with_options(tenant_id, task_id, request, headers, runtime)

    async def get_task_statistics_async(
        self,
        tenant_id: str,
        task_id: str,
        request: open_itag_20220616_models.GetTaskStatisticsRequest,
    ) -> open_itag_20220616_models.GetTaskStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_task_statistics_with_options_async(tenant_id, task_id, request, headers, runtime)

    def get_task_statistics_with_options(
        self,
        tenant_id: str,
        task_id: str,
        request: open_itag_20220616_models.GetTaskStatisticsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_itag_20220616_models.GetTaskStatisticsResponse:
        UtilClient.validate_model(request)
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        task_id = OpenApiUtilClient.get_encode_param(task_id)
        query = {}
        if not UtilClient.is_unset(request.stat_type):
            query['StatType'] = request.stat_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTaskStatistics',
            version='2022-06-16',
            protocol='HTTPS',
            pathname=f'/openapi/api/v1/tenants/{tenant_id}/tasks/{task_id}/statistics',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.GetTaskStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_task_statistics_with_options_async(
        self,
        tenant_id: str,
        task_id: str,
        request: open_itag_20220616_models.GetTaskStatisticsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_itag_20220616_models.GetTaskStatisticsResponse:
        UtilClient.validate_model(request)
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        task_id = OpenApiUtilClient.get_encode_param(task_id)
        query = {}
        if not UtilClient.is_unset(request.stat_type):
            query['StatType'] = request.stat_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTaskStatistics',
            version='2022-06-16',
            protocol='HTTPS',
            pathname=f'/openapi/api/v1/tenants/{tenant_id}/tasks/{task_id}/statistics',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.GetTaskStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_task_status(
        self,
        tenant_id: str,
        task_id: str,
    ) -> open_itag_20220616_models.GetTaskStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_task_status_with_options(tenant_id, task_id, headers, runtime)

    async def get_task_status_async(
        self,
        tenant_id: str,
        task_id: str,
    ) -> open_itag_20220616_models.GetTaskStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_task_status_with_options_async(tenant_id, task_id, headers, runtime)

    def get_task_status_with_options(
        self,
        tenant_id: str,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_itag_20220616_models.GetTaskStatusResponse:
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        task_id = OpenApiUtilClient.get_encode_param(task_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTaskStatus',
            version='2022-06-16',
            protocol='HTTPS',
            pathname=f'/openapi/api/v1/tenants/{tenant_id}/tasks/{task_id}/status',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.GetTaskStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_task_status_with_options_async(
        self,
        tenant_id: str,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_itag_20220616_models.GetTaskStatusResponse:
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        task_id = OpenApiUtilClient.get_encode_param(task_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTaskStatus',
            version='2022-06-16',
            protocol='HTTPS',
            pathname=f'/openapi/api/v1/tenants/{tenant_id}/tasks/{task_id}/status',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.GetTaskStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_task_template(
        self,
        tenant_id: str,
        task_id: str,
    ) -> open_itag_20220616_models.GetTaskTemplateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_task_template_with_options(tenant_id, task_id, headers, runtime)

    async def get_task_template_async(
        self,
        tenant_id: str,
        task_id: str,
    ) -> open_itag_20220616_models.GetTaskTemplateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_task_template_with_options_async(tenant_id, task_id, headers, runtime)

    def get_task_template_with_options(
        self,
        tenant_id: str,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_itag_20220616_models.GetTaskTemplateResponse:
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        task_id = OpenApiUtilClient.get_encode_param(task_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTaskTemplate',
            version='2022-06-16',
            protocol='HTTPS',
            pathname=f'/openapi/api/v1/tenants/{tenant_id}/tasks/{task_id}/template',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.GetTaskTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_task_template_with_options_async(
        self,
        tenant_id: str,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_itag_20220616_models.GetTaskTemplateResponse:
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        task_id = OpenApiUtilClient.get_encode_param(task_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTaskTemplate',
            version='2022-06-16',
            protocol='HTTPS',
            pathname=f'/openapi/api/v1/tenants/{tenant_id}/tasks/{task_id}/template',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.GetTaskTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_task_template_questions(
        self,
        tenant_id: str,
        task_id: str,
    ) -> open_itag_20220616_models.GetTaskTemplateQuestionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_task_template_questions_with_options(tenant_id, task_id, headers, runtime)

    async def get_task_template_questions_async(
        self,
        tenant_id: str,
        task_id: str,
    ) -> open_itag_20220616_models.GetTaskTemplateQuestionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_task_template_questions_with_options_async(tenant_id, task_id, headers, runtime)

    def get_task_template_questions_with_options(
        self,
        tenant_id: str,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_itag_20220616_models.GetTaskTemplateQuestionsResponse:
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        task_id = OpenApiUtilClient.get_encode_param(task_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTaskTemplateQuestions',
            version='2022-06-16',
            protocol='HTTPS',
            pathname=f'/openapi/api/v1/tenants/{tenant_id}/tasks/{task_id}/template/questions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.GetTaskTemplateQuestionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_task_template_questions_with_options_async(
        self,
        tenant_id: str,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_itag_20220616_models.GetTaskTemplateQuestionsResponse:
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        task_id = OpenApiUtilClient.get_encode_param(task_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTaskTemplateQuestions',
            version='2022-06-16',
            protocol='HTTPS',
            pathname=f'/openapi/api/v1/tenants/{tenant_id}/tasks/{task_id}/template/questions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.GetTaskTemplateQuestionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_task_template_views(
        self,
        tenant_id: str,
        task_id: str,
    ) -> open_itag_20220616_models.GetTaskTemplateViewsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_task_template_views_with_options(tenant_id, task_id, headers, runtime)

    async def get_task_template_views_async(
        self,
        tenant_id: str,
        task_id: str,
    ) -> open_itag_20220616_models.GetTaskTemplateViewsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_task_template_views_with_options_async(tenant_id, task_id, headers, runtime)

    def get_task_template_views_with_options(
        self,
        tenant_id: str,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_itag_20220616_models.GetTaskTemplateViewsResponse:
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        task_id = OpenApiUtilClient.get_encode_param(task_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTaskTemplateViews',
            version='2022-06-16',
            protocol='HTTPS',
            pathname=f'/openapi/api/v1/tenants/{tenant_id}/tasks/{task_id}/template/views',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.GetTaskTemplateViewsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_task_template_views_with_options_async(
        self,
        tenant_id: str,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_itag_20220616_models.GetTaskTemplateViewsResponse:
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        task_id = OpenApiUtilClient.get_encode_param(task_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTaskTemplateViews',
            version='2022-06-16',
            protocol='HTTPS',
            pathname=f'/openapi/api/v1/tenants/{tenant_id}/tasks/{task_id}/template/views',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.GetTaskTemplateViewsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_task_workforce(
        self,
        tenant_id: str,
        task_id: str,
    ) -> open_itag_20220616_models.GetTaskWorkforceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_task_workforce_with_options(tenant_id, task_id, headers, runtime)

    async def get_task_workforce_async(
        self,
        tenant_id: str,
        task_id: str,
    ) -> open_itag_20220616_models.GetTaskWorkforceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_task_workforce_with_options_async(tenant_id, task_id, headers, runtime)

    def get_task_workforce_with_options(
        self,
        tenant_id: str,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_itag_20220616_models.GetTaskWorkforceResponse:
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        task_id = OpenApiUtilClient.get_encode_param(task_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTaskWorkforce',
            version='2022-06-16',
            protocol='HTTPS',
            pathname=f'/openapi/api/v1/tenants/{tenant_id}/tasks/{task_id}/workforce',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.GetTaskWorkforceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_task_workforce_with_options_async(
        self,
        tenant_id: str,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_itag_20220616_models.GetTaskWorkforceResponse:
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        task_id = OpenApiUtilClient.get_encode_param(task_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTaskWorkforce',
            version='2022-06-16',
            protocol='HTTPS',
            pathname=f'/openapi/api/v1/tenants/{tenant_id}/tasks/{task_id}/workforce',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.GetTaskWorkforceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_task_workforce_statistic(
        self,
        tenant_id: str,
        task_id: str,
        request: open_itag_20220616_models.GetTaskWorkforceStatisticRequest,
    ) -> open_itag_20220616_models.GetTaskWorkforceStatisticResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_task_workforce_statistic_with_options(tenant_id, task_id, request, headers, runtime)

    async def get_task_workforce_statistic_async(
        self,
        tenant_id: str,
        task_id: str,
        request: open_itag_20220616_models.GetTaskWorkforceStatisticRequest,
    ) -> open_itag_20220616_models.GetTaskWorkforceStatisticResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_task_workforce_statistic_with_options_async(tenant_id, task_id, request, headers, runtime)

    def get_task_workforce_statistic_with_options(
        self,
        tenant_id: str,
        task_id: str,
        request: open_itag_20220616_models.GetTaskWorkforceStatisticRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_itag_20220616_models.GetTaskWorkforceStatisticResponse:
        UtilClient.validate_model(request)
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        task_id = OpenApiUtilClient.get_encode_param(task_id)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.stat_type):
            query['StatType'] = request.stat_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTaskWorkforceStatistic',
            version='2022-06-16',
            protocol='HTTPS',
            pathname=f'/openapi/api/v1/tenants/{tenant_id}/tasks/{task_id}/workforce/statistic',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.GetTaskWorkforceStatisticResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_task_workforce_statistic_with_options_async(
        self,
        tenant_id: str,
        task_id: str,
        request: open_itag_20220616_models.GetTaskWorkforceStatisticRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_itag_20220616_models.GetTaskWorkforceStatisticResponse:
        UtilClient.validate_model(request)
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        task_id = OpenApiUtilClient.get_encode_param(task_id)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.stat_type):
            query['StatType'] = request.stat_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTaskWorkforceStatistic',
            version='2022-06-16',
            protocol='HTTPS',
            pathname=f'/openapi/api/v1/tenants/{tenant_id}/tasks/{task_id}/workforce/statistic',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.GetTaskWorkforceStatisticResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_template(
        self,
        tenant_id: str,
        template_id: str,
    ) -> open_itag_20220616_models.GetTemplateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_template_with_options(tenant_id, template_id, headers, runtime)

    async def get_template_async(
        self,
        tenant_id: str,
        template_id: str,
    ) -> open_itag_20220616_models.GetTemplateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_template_with_options_async(tenant_id, template_id, headers, runtime)

    def get_template_with_options(
        self,
        tenant_id: str,
        template_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_itag_20220616_models.GetTemplateResponse:
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        template_id = OpenApiUtilClient.get_encode_param(template_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTemplate',
            version='2022-06-16',
            protocol='HTTPS',
            pathname=f'/openapi/api/v1/tenants/{tenant_id}/templates/{template_id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.GetTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_template_with_options_async(
        self,
        tenant_id: str,
        template_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_itag_20220616_models.GetTemplateResponse:
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        template_id = OpenApiUtilClient.get_encode_param(template_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTemplate',
            version='2022-06-16',
            protocol='HTTPS',
            pathname=f'/openapi/api/v1/tenants/{tenant_id}/templates/{template_id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.GetTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_template_questions(
        self,
        tenant_id: str,
        template_id: str,
    ) -> open_itag_20220616_models.GetTemplateQuestionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_template_questions_with_options(tenant_id, template_id, headers, runtime)

    async def get_template_questions_async(
        self,
        tenant_id: str,
        template_id: str,
    ) -> open_itag_20220616_models.GetTemplateQuestionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_template_questions_with_options_async(tenant_id, template_id, headers, runtime)

    def get_template_questions_with_options(
        self,
        tenant_id: str,
        template_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_itag_20220616_models.GetTemplateQuestionsResponse:
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        template_id = OpenApiUtilClient.get_encode_param(template_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTemplateQuestions',
            version='2022-06-16',
            protocol='HTTPS',
            pathname=f'/openapi/api/v1/tenants/{tenant_id}/templates/{template_id}/questions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.GetTemplateQuestionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_template_questions_with_options_async(
        self,
        tenant_id: str,
        template_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_itag_20220616_models.GetTemplateQuestionsResponse:
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        template_id = OpenApiUtilClient.get_encode_param(template_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTemplateQuestions',
            version='2022-06-16',
            protocol='HTTPS',
            pathname=f'/openapi/api/v1/tenants/{tenant_id}/templates/{template_id}/questions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.GetTemplateQuestionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_template_view(
        self,
        tenant_id: str,
        template_id: str,
    ) -> open_itag_20220616_models.GetTemplateViewResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_template_view_with_options(tenant_id, template_id, headers, runtime)

    async def get_template_view_async(
        self,
        tenant_id: str,
        template_id: str,
    ) -> open_itag_20220616_models.GetTemplateViewResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_template_view_with_options_async(tenant_id, template_id, headers, runtime)

    def get_template_view_with_options(
        self,
        tenant_id: str,
        template_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_itag_20220616_models.GetTemplateViewResponse:
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        template_id = OpenApiUtilClient.get_encode_param(template_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTemplateView',
            version='2022-06-16',
            protocol='HTTPS',
            pathname=f'/openapi/api/v1/tenants/{tenant_id}/templates/{template_id}/views',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.GetTemplateViewResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_template_view_with_options_async(
        self,
        tenant_id: str,
        template_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_itag_20220616_models.GetTemplateViewResponse:
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        template_id = OpenApiUtilClient.get_encode_param(template_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTemplateView',
            version='2022-06-16',
            protocol='HTTPS',
            pathname=f'/openapi/api/v1/tenants/{tenant_id}/templates/{template_id}/views',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.GetTemplateViewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_tenant(
        self,
        tenant_id: str,
    ) -> open_itag_20220616_models.GetTenantResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_tenant_with_options(tenant_id, headers, runtime)

    async def get_tenant_async(
        self,
        tenant_id: str,
    ) -> open_itag_20220616_models.GetTenantResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_tenant_with_options_async(tenant_id, headers, runtime)

    def get_tenant_with_options(
        self,
        tenant_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_itag_20220616_models.GetTenantResponse:
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTenant',
            version='2022-06-16',
            protocol='HTTPS',
            pathname=f'/openapi/api/v1/tenants/{tenant_id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.GetTenantResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_tenant_with_options_async(
        self,
        tenant_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_itag_20220616_models.GetTenantResponse:
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTenant',
            version='2022-06-16',
            protocol='HTTPS',
            pathname=f'/openapi/api/v1/tenants/{tenant_id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.GetTenantResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user(
        self,
        tenant_id: str,
        user_id: str,
    ) -> open_itag_20220616_models.GetUserResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_user_with_options(tenant_id, user_id, headers, runtime)

    async def get_user_async(
        self,
        tenant_id: str,
        user_id: str,
    ) -> open_itag_20220616_models.GetUserResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_user_with_options_async(tenant_id, user_id, headers, runtime)

    def get_user_with_options(
        self,
        tenant_id: str,
        user_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_itag_20220616_models.GetUserResponse:
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        user_id = OpenApiUtilClient.get_encode_param(user_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetUser',
            version='2022-06-16',
            protocol='HTTPS',
            pathname=f'/openapi/api/v1/tenants/{tenant_id}/users/{user_id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.GetUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_with_options_async(
        self,
        tenant_id: str,
        user_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_itag_20220616_models.GetUserResponse:
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        user_id = OpenApiUtilClient.get_encode_param(user_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetUser',
            version='2022-06-16',
            protocol='HTTPS',
            pathname=f'/openapi/api/v1/tenants/{tenant_id}/users/{user_id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.GetUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_jobs(
        self,
        tenant_id: str,
        request: open_itag_20220616_models.ListJobsRequest,
    ) -> open_itag_20220616_models.ListJobsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_jobs_with_options(tenant_id, request, headers, runtime)

    async def list_jobs_async(
        self,
        tenant_id: str,
        request: open_itag_20220616_models.ListJobsRequest,
    ) -> open_itag_20220616_models.ListJobsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_jobs_with_options_async(tenant_id, request, headers, runtime)

    def list_jobs_with_options(
        self,
        tenant_id: str,
        request: open_itag_20220616_models.ListJobsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_itag_20220616_models.ListJobsResponse:
        UtilClient.validate_model(request)
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        query = {}
        if not UtilClient.is_unset(request.job_type):
            query['JobType'] = request.job_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobs',
            version='2022-06-16',
            protocol='HTTPS',
            pathname=f'/openapi/api/v1/tenants/{tenant_id}/jobs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.ListJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_jobs_with_options_async(
        self,
        tenant_id: str,
        request: open_itag_20220616_models.ListJobsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_itag_20220616_models.ListJobsResponse:
        UtilClient.validate_model(request)
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        query = {}
        if not UtilClient.is_unset(request.job_type):
            query['JobType'] = request.job_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobs',
            version='2022-06-16',
            protocol='HTTPS',
            pathname=f'/openapi/api/v1/tenants/{tenant_id}/jobs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.ListJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_subtask_items(
        self,
        tenant_id: str,
        task_id: str,
        subtask_id: str,
        request: open_itag_20220616_models.ListSubtaskItemsRequest,
    ) -> open_itag_20220616_models.ListSubtaskItemsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_subtask_items_with_options(tenant_id, task_id, subtask_id, request, headers, runtime)

    async def list_subtask_items_async(
        self,
        tenant_id: str,
        task_id: str,
        subtask_id: str,
        request: open_itag_20220616_models.ListSubtaskItemsRequest,
    ) -> open_itag_20220616_models.ListSubtaskItemsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_subtask_items_with_options_async(tenant_id, task_id, subtask_id, request, headers, runtime)

    def list_subtask_items_with_options(
        self,
        tenant_id: str,
        task_id: str,
        subtask_id: str,
        request: open_itag_20220616_models.ListSubtaskItemsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_itag_20220616_models.ListSubtaskItemsResponse:
        UtilClient.validate_model(request)
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        task_id = OpenApiUtilClient.get_encode_param(task_id)
        subtask_id = OpenApiUtilClient.get_encode_param(subtask_id)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSubtaskItems',
            version='2022-06-16',
            protocol='HTTPS',
            pathname=f'/openapi/api/v1/tenants/{tenant_id}/tasks/{task_id}/subtasks/{subtask_id}/items',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.ListSubtaskItemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_subtask_items_with_options_async(
        self,
        tenant_id: str,
        task_id: str,
        subtask_id: str,
        request: open_itag_20220616_models.ListSubtaskItemsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_itag_20220616_models.ListSubtaskItemsResponse:
        UtilClient.validate_model(request)
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        task_id = OpenApiUtilClient.get_encode_param(task_id)
        subtask_id = OpenApiUtilClient.get_encode_param(subtask_id)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSubtaskItems',
            version='2022-06-16',
            protocol='HTTPS',
            pathname=f'/openapi/api/v1/tenants/{tenant_id}/tasks/{task_id}/subtasks/{subtask_id}/items',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.ListSubtaskItemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_subtasks(
        self,
        tenant_id: str,
        task_id: str,
        request: open_itag_20220616_models.ListSubtasksRequest,
    ) -> open_itag_20220616_models.ListSubtasksResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_subtasks_with_options(tenant_id, task_id, request, headers, runtime)

    async def list_subtasks_async(
        self,
        tenant_id: str,
        task_id: str,
        request: open_itag_20220616_models.ListSubtasksRequest,
    ) -> open_itag_20220616_models.ListSubtasksResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_subtasks_with_options_async(tenant_id, task_id, request, headers, runtime)

    def list_subtasks_with_options(
        self,
        tenant_id: str,
        task_id: str,
        request: open_itag_20220616_models.ListSubtasksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_itag_20220616_models.ListSubtasksResponse:
        UtilClient.validate_model(request)
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        task_id = OpenApiUtilClient.get_encode_param(task_id)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSubtasks',
            version='2022-06-16',
            protocol='HTTPS',
            pathname=f'/openapi/api/v1/tenants/{tenant_id}/tasks/{task_id}/subtasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.ListSubtasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_subtasks_with_options_async(
        self,
        tenant_id: str,
        task_id: str,
        request: open_itag_20220616_models.ListSubtasksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_itag_20220616_models.ListSubtasksResponse:
        UtilClient.validate_model(request)
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        task_id = OpenApiUtilClient.get_encode_param(task_id)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSubtasks',
            version='2022-06-16',
            protocol='HTTPS',
            pathname=f'/openapi/api/v1/tenants/{tenant_id}/tasks/{task_id}/subtasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.ListSubtasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tasks(
        self,
        tenant_id: str,
        request: open_itag_20220616_models.ListTasksRequest,
    ) -> open_itag_20220616_models.ListTasksResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_tasks_with_options(tenant_id, request, headers, runtime)

    async def list_tasks_async(
        self,
        tenant_id: str,
        request: open_itag_20220616_models.ListTasksRequest,
    ) -> open_itag_20220616_models.ListTasksResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_tasks_with_options_async(tenant_id, request, headers, runtime)

    def list_tasks_with_options(
        self,
        tenant_id: str,
        request: open_itag_20220616_models.ListTasksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_itag_20220616_models.ListTasksResponse:
        UtilClient.validate_model(request)
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTasks',
            version='2022-06-16',
            protocol='HTTPS',
            pathname=f'/openapi/api/v1/tenants/{tenant_id}/tasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.ListTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tasks_with_options_async(
        self,
        tenant_id: str,
        request: open_itag_20220616_models.ListTasksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_itag_20220616_models.ListTasksResponse:
        UtilClient.validate_model(request)
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTasks',
            version='2022-06-16',
            protocol='HTTPS',
            pathname=f'/openapi/api/v1/tenants/{tenant_id}/tasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.ListTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_templates(
        self,
        tenant_id: str,
        request: open_itag_20220616_models.ListTemplatesRequest,
    ) -> open_itag_20220616_models.ListTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_templates_with_options(tenant_id, request, headers, runtime)

    async def list_templates_async(
        self,
        tenant_id: str,
        request: open_itag_20220616_models.ListTemplatesRequest,
    ) -> open_itag_20220616_models.ListTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_templates_with_options_async(tenant_id, request, headers, runtime)

    def list_templates_with_options(
        self,
        tenant_id: str,
        request: open_itag_20220616_models.ListTemplatesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_itag_20220616_models.ListTemplatesResponse:
        UtilClient.validate_model(request)
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            query['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTemplates',
            version='2022-06-16',
            protocol='HTTPS',
            pathname=f'/openapi/api/v1/tenants/{tenant_id}/templates',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.ListTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_templates_with_options_async(
        self,
        tenant_id: str,
        request: open_itag_20220616_models.ListTemplatesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_itag_20220616_models.ListTemplatesResponse:
        UtilClient.validate_model(request)
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            query['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTemplates',
            version='2022-06-16',
            protocol='HTTPS',
            pathname=f'/openapi/api/v1/tenants/{tenant_id}/templates',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.ListTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tenants(
        self,
        request: open_itag_20220616_models.ListTenantsRequest,
    ) -> open_itag_20220616_models.ListTenantsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_tenants_with_options(request, headers, runtime)

    async def list_tenants_async(
        self,
        request: open_itag_20220616_models.ListTenantsRequest,
    ) -> open_itag_20220616_models.ListTenantsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_tenants_with_options_async(request, headers, runtime)

    def list_tenants_with_options(
        self,
        request: open_itag_20220616_models.ListTenantsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_itag_20220616_models.ListTenantsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTenants',
            version='2022-06-16',
            protocol='HTTPS',
            pathname=f'/openapi/api/v1/tenants',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.ListTenantsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tenants_with_options_async(
        self,
        request: open_itag_20220616_models.ListTenantsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_itag_20220616_models.ListTenantsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTenants',
            version='2022-06-16',
            protocol='HTTPS',
            pathname=f'/openapi/api/v1/tenants',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.ListTenantsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_users(
        self,
        tenant_id: str,
        request: open_itag_20220616_models.ListUsersRequest,
    ) -> open_itag_20220616_models.ListUsersResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_users_with_options(tenant_id, request, headers, runtime)

    async def list_users_async(
        self,
        tenant_id: str,
        request: open_itag_20220616_models.ListUsersRequest,
    ) -> open_itag_20220616_models.ListUsersResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_users_with_options_async(tenant_id, request, headers, runtime)

    def list_users_with_options(
        self,
        tenant_id: str,
        request: open_itag_20220616_models.ListUsersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_itag_20220616_models.ListUsersResponse:
        UtilClient.validate_model(request)
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUsers',
            version='2022-06-16',
            protocol='HTTPS',
            pathname=f'/openapi/api/v1/tenants/{tenant_id}/users',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.ListUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_users_with_options_async(
        self,
        tenant_id: str,
        request: open_itag_20220616_models.ListUsersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_itag_20220616_models.ListUsersResponse:
        UtilClient.validate_model(request)
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUsers',
            version='2022-06-16',
            protocol='HTTPS',
            pathname=f'/openapi/api/v1/tenants/{tenant_id}/users',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.ListUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_work_node_workforce(
        self,
        tenant_id: str,
        task_id: str,
        work_node_id: str,
        request: open_itag_20220616_models.RemoveWorkNodeWorkforceRequest,
    ) -> open_itag_20220616_models.RemoveWorkNodeWorkforceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.remove_work_node_workforce_with_options(tenant_id, task_id, work_node_id, request, headers, runtime)

    async def remove_work_node_workforce_async(
        self,
        tenant_id: str,
        task_id: str,
        work_node_id: str,
        request: open_itag_20220616_models.RemoveWorkNodeWorkforceRequest,
    ) -> open_itag_20220616_models.RemoveWorkNodeWorkforceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.remove_work_node_workforce_with_options_async(tenant_id, task_id, work_node_id, request, headers, runtime)

    def remove_work_node_workforce_with_options(
        self,
        tenant_id: str,
        task_id: str,
        work_node_id: str,
        request: open_itag_20220616_models.RemoveWorkNodeWorkforceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_itag_20220616_models.RemoveWorkNodeWorkforceResponse:
        UtilClient.validate_model(request)
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        task_id = OpenApiUtilClient.get_encode_param(task_id)
        work_node_id = OpenApiUtilClient.get_encode_param(work_node_id)
        body = {}
        if not UtilClient.is_unset(request.user_ids):
            body['UserIds'] = request.user_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveWorkNodeWorkforce',
            version='2022-06-16',
            protocol='HTTPS',
            pathname=f'/openapi/api/v1/tenants/{tenant_id}/tasks/{task_id}/worknodes/{work_node_id}/workforce',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.RemoveWorkNodeWorkforceResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_work_node_workforce_with_options_async(
        self,
        tenant_id: str,
        task_id: str,
        work_node_id: str,
        request: open_itag_20220616_models.RemoveWorkNodeWorkforceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_itag_20220616_models.RemoveWorkNodeWorkforceResponse:
        UtilClient.validate_model(request)
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        task_id = OpenApiUtilClient.get_encode_param(task_id)
        work_node_id = OpenApiUtilClient.get_encode_param(work_node_id)
        body = {}
        if not UtilClient.is_unset(request.user_ids):
            body['UserIds'] = request.user_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveWorkNodeWorkforce',
            version='2022-06-16',
            protocol='HTTPS',
            pathname=f'/openapi/api/v1/tenants/{tenant_id}/tasks/{task_id}/worknodes/{work_node_id}/workforce',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.RemoveWorkNodeWorkforceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_task(
        self,
        tenant_id: str,
        task_id: str,
        request: open_itag_20220616_models.UpdateTaskRequest,
    ) -> open_itag_20220616_models.UpdateTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_task_with_options(tenant_id, task_id, request, headers, runtime)

    async def update_task_async(
        self,
        tenant_id: str,
        task_id: str,
        request: open_itag_20220616_models.UpdateTaskRequest,
    ) -> open_itag_20220616_models.UpdateTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_task_with_options_async(tenant_id, task_id, request, headers, runtime)

    def update_task_with_options(
        self,
        tenant_id: str,
        task_id: str,
        request: open_itag_20220616_models.UpdateTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_itag_20220616_models.UpdateTaskResponse:
        UtilClient.validate_model(request)
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        task_id = OpenApiUtilClient.get_encode_param(task_id)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.body))
        )
        params = open_api_models.Params(
            action='UpdateTask',
            version='2022-06-16',
            protocol='HTTPS',
            pathname=f'/openapi/api/v1/tenants/{tenant_id}/tasks/{task_id}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.UpdateTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_task_with_options_async(
        self,
        tenant_id: str,
        task_id: str,
        request: open_itag_20220616_models.UpdateTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_itag_20220616_models.UpdateTaskResponse:
        UtilClient.validate_model(request)
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        task_id = OpenApiUtilClient.get_encode_param(task_id)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.body))
        )
        params = open_api_models.Params(
            action='UpdateTask',
            version='2022-06-16',
            protocol='HTTPS',
            pathname=f'/openapi/api/v1/tenants/{tenant_id}/tasks/{task_id}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.UpdateTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_task_workforce(
        self,
        tenant_id: str,
        task_id: str,
        request: open_itag_20220616_models.UpdateTaskWorkforceRequest,
    ) -> open_itag_20220616_models.UpdateTaskWorkforceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_task_workforce_with_options(tenant_id, task_id, request, headers, runtime)

    async def update_task_workforce_async(
        self,
        tenant_id: str,
        task_id: str,
        request: open_itag_20220616_models.UpdateTaskWorkforceRequest,
    ) -> open_itag_20220616_models.UpdateTaskWorkforceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_task_workforce_with_options_async(tenant_id, task_id, request, headers, runtime)

    def update_task_workforce_with_options(
        self,
        tenant_id: str,
        task_id: str,
        request: open_itag_20220616_models.UpdateTaskWorkforceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_itag_20220616_models.UpdateTaskWorkforceResponse:
        UtilClient.validate_model(request)
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        task_id = OpenApiUtilClient.get_encode_param(task_id)
        body = {}
        if not UtilClient.is_unset(request.workforce):
            body['Workforce'] = request.workforce
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTaskWorkforce',
            version='2022-06-16',
            protocol='HTTPS',
            pathname=f'/openapi/api/v1/tenants/{tenant_id}/tasks/{task_id}/workforce',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.UpdateTaskWorkforceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_task_workforce_with_options_async(
        self,
        tenant_id: str,
        task_id: str,
        request: open_itag_20220616_models.UpdateTaskWorkforceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_itag_20220616_models.UpdateTaskWorkforceResponse:
        UtilClient.validate_model(request)
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        task_id = OpenApiUtilClient.get_encode_param(task_id)
        body = {}
        if not UtilClient.is_unset(request.workforce):
            body['Workforce'] = request.workforce
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTaskWorkforce',
            version='2022-06-16',
            protocol='HTTPS',
            pathname=f'/openapi/api/v1/tenants/{tenant_id}/tasks/{task_id}/workforce',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.UpdateTaskWorkforceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_template(
        self,
        tenant_id: str,
        template_id: str,
        request: open_itag_20220616_models.UpdateTemplateRequest,
    ) -> open_itag_20220616_models.UpdateTemplateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_template_with_options(tenant_id, template_id, request, headers, runtime)

    async def update_template_async(
        self,
        tenant_id: str,
        template_id: str,
        request: open_itag_20220616_models.UpdateTemplateRequest,
    ) -> open_itag_20220616_models.UpdateTemplateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_template_with_options_async(tenant_id, template_id, request, headers, runtime)

    def update_template_with_options(
        self,
        tenant_id: str,
        template_id: str,
        request: open_itag_20220616_models.UpdateTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_itag_20220616_models.UpdateTemplateResponse:
        UtilClient.validate_model(request)
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        template_id = OpenApiUtilClient.get_encode_param(template_id)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.body))
        )
        params = open_api_models.Params(
            action='UpdateTemplate',
            version='2022-06-16',
            protocol='HTTPS',
            pathname=f'/openapi/api/v1/tenants/{tenant_id}/templates/{template_id}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.UpdateTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_template_with_options_async(
        self,
        tenant_id: str,
        template_id: str,
        request: open_itag_20220616_models.UpdateTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_itag_20220616_models.UpdateTemplateResponse:
        UtilClient.validate_model(request)
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        template_id = OpenApiUtilClient.get_encode_param(template_id)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.body))
        )
        params = open_api_models.Params(
            action='UpdateTemplate',
            version='2022-06-16',
            protocol='HTTPS',
            pathname=f'/openapi/api/v1/tenants/{tenant_id}/templates/{template_id}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.UpdateTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_tenant(
        self,
        tenant_id: str,
        request: open_itag_20220616_models.UpdateTenantRequest,
    ) -> open_itag_20220616_models.UpdateTenantResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_tenant_with_options(tenant_id, request, headers, runtime)

    async def update_tenant_async(
        self,
        tenant_id: str,
        request: open_itag_20220616_models.UpdateTenantRequest,
    ) -> open_itag_20220616_models.UpdateTenantResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_tenant_with_options_async(tenant_id, request, headers, runtime)

    def update_tenant_with_options(
        self,
        tenant_id: str,
        request: open_itag_20220616_models.UpdateTenantRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_itag_20220616_models.UpdateTenantResponse:
        UtilClient.validate_model(request)
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.tenant_name):
            body['TenantName'] = request.tenant_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTenant',
            version='2022-06-16',
            protocol='HTTPS',
            pathname=f'/openapi/api/v1/tenants/{tenant_id}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.UpdateTenantResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_tenant_with_options_async(
        self,
        tenant_id: str,
        request: open_itag_20220616_models.UpdateTenantRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_itag_20220616_models.UpdateTenantResponse:
        UtilClient.validate_model(request)
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.tenant_name):
            body['TenantName'] = request.tenant_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTenant',
            version='2022-06-16',
            protocol='HTTPS',
            pathname=f'/openapi/api/v1/tenants/{tenant_id}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.UpdateTenantResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_user(
        self,
        tenant_id: str,
        user_id: str,
        request: open_itag_20220616_models.UpdateUserRequest,
    ) -> open_itag_20220616_models.UpdateUserResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_user_with_options(tenant_id, user_id, request, headers, runtime)

    async def update_user_async(
        self,
        tenant_id: str,
        user_id: str,
        request: open_itag_20220616_models.UpdateUserRequest,
    ) -> open_itag_20220616_models.UpdateUserResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_user_with_options_async(tenant_id, user_id, request, headers, runtime)

    def update_user_with_options(
        self,
        tenant_id: str,
        user_id: str,
        request: open_itag_20220616_models.UpdateUserRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_itag_20220616_models.UpdateUserResponse:
        UtilClient.validate_model(request)
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        user_id = OpenApiUtilClient.get_encode_param(user_id)
        body = {}
        if not UtilClient.is_unset(request.role):
            body['Role'] = request.role
        if not UtilClient.is_unset(request.user_name):
            body['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateUser',
            version='2022-06-16',
            protocol='HTTPS',
            pathname=f'/openapi/api/v1/tenants/{tenant_id}/users/{user_id}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.UpdateUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_user_with_options_async(
        self,
        tenant_id: str,
        user_id: str,
        request: open_itag_20220616_models.UpdateUserRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_itag_20220616_models.UpdateUserResponse:
        UtilClient.validate_model(request)
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        user_id = OpenApiUtilClient.get_encode_param(user_id)
        body = {}
        if not UtilClient.is_unset(request.role):
            body['Role'] = request.role
        if not UtilClient.is_unset(request.user_name):
            body['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateUser',
            version='2022-06-16',
            protocol='HTTPS',
            pathname=f'/openapi/api/v1/tenants/{tenant_id}/users/{user_id}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.UpdateUserResponse(),
            await self.call_api_async(params, req, runtime)
        )
