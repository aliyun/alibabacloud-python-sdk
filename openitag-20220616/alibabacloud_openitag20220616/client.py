# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_openitag20220616 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
from darabonba.runtime import RuntimeOptions
from darabonba.url import Url as DaraURL

"""
"""
class Client(OpenApiClient):

    def __init__(
        self,
        config: open_api_util_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'cn-shenzhen': 'openitag.cn-shenzhen.aliyuncs.com',
            'cn-shanghai': 'openitag.cn-shanghai.aliyuncs.com',
            'cn-hangzhou': 'openitag.cn-hangzhou.aliyuncs.com',
            'cn-beijing': 'openitag.cn-beijing.aliyuncs.com'
        }
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
        if not DaraCore.is_null(endpoint):
            return endpoint
        if not DaraCore.is_null(endpoint_map) and not DaraCore.is_null(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return Utils.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_work_node_workforce_with_options(
        self,
        tenant_id: str,
        task_id: str,
        work_node_id: str,
        request: main_models.AddWorkNodeWorkforceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AddWorkNodeWorkforceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.user_ids):
            body['UserIds'] = request.user_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddWorkNodeWorkforce',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = f'/openapi/api/v1/tenants/{DaraURL.percent_encode(tenant_id)}/tasks/{DaraURL.percent_encode(task_id)}/worknodes/{DaraURL.percent_encode(work_node_id)}/workforce',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddWorkNodeWorkforceResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_work_node_workforce_with_options_async(
        self,
        tenant_id: str,
        task_id: str,
        work_node_id: str,
        request: main_models.AddWorkNodeWorkforceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AddWorkNodeWorkforceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.user_ids):
            body['UserIds'] = request.user_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddWorkNodeWorkforce',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = f'/openapi/api/v1/tenants/{DaraURL.percent_encode(tenant_id)}/tasks/{DaraURL.percent_encode(task_id)}/worknodes/{DaraURL.percent_encode(work_node_id)}/workforce',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddWorkNodeWorkforceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_work_node_workforce(
        self,
        tenant_id: str,
        task_id: str,
        work_node_id: str,
        request: main_models.AddWorkNodeWorkforceRequest,
    ) -> main_models.AddWorkNodeWorkforceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.add_work_node_workforce_with_options(tenant_id, task_id, work_node_id, request, headers, runtime)

    async def add_work_node_workforce_async(
        self,
        tenant_id: str,
        task_id: str,
        work_node_id: str,
        request: main_models.AddWorkNodeWorkforceRequest,
    ) -> main_models.AddWorkNodeWorkforceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.add_work_node_workforce_with_options_async(tenant_id, task_id, work_node_id, request, headers, runtime)

    def append_all_data_to_task_with_options(
        self,
        tenant_id: str,
        task_id: str,
        request: main_models.AppendAllDataToTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AppendAllDataToTaskResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'AppendAllDataToTask',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = f'/openapi/api/v1/tenants/{DaraURL.percent_encode(tenant_id)}/tasks/{DaraURL.percent_encode(task_id)}/appendAllDataToTask',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AppendAllDataToTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def append_all_data_to_task_with_options_async(
        self,
        tenant_id: str,
        task_id: str,
        request: main_models.AppendAllDataToTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AppendAllDataToTaskResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'AppendAllDataToTask',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = f'/openapi/api/v1/tenants/{DaraURL.percent_encode(tenant_id)}/tasks/{DaraURL.percent_encode(task_id)}/appendAllDataToTask',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AppendAllDataToTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def append_all_data_to_task(
        self,
        tenant_id: str,
        task_id: str,
        request: main_models.AppendAllDataToTaskRequest,
    ) -> main_models.AppendAllDataToTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.append_all_data_to_task_with_options(tenant_id, task_id, request, headers, runtime)

    async def append_all_data_to_task_async(
        self,
        tenant_id: str,
        task_id: str,
        request: main_models.AppendAllDataToTaskRequest,
    ) -> main_models.AppendAllDataToTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.append_all_data_to_task_with_options_async(tenant_id, task_id, request, headers, runtime)

    def create_task_with_options(
        self,
        tenant_id: str,
        request: main_models.CreateTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateTaskResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTask',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = f'/openapi/api/v1/tenants/{DaraURL.percent_encode(tenant_id)}/tasks',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_task_with_options_async(
        self,
        tenant_id: str,
        request: main_models.CreateTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateTaskResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTask',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = f'/openapi/api/v1/tenants/{DaraURL.percent_encode(tenant_id)}/tasks',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_task(
        self,
        tenant_id: str,
        request: main_models.CreateTaskRequest,
    ) -> main_models.CreateTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_task_with_options(tenant_id, request, headers, runtime)

    async def create_task_async(
        self,
        tenant_id: str,
        request: main_models.CreateTaskRequest,
    ) -> main_models.CreateTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_task_with_options_async(tenant_id, request, headers, runtime)

    def create_template_with_options(
        self,
        tenant_id: str,
        request: main_models.CreateTemplateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateTemplateResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTemplate',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = f'/openapi/api/v1/tenants/{DaraURL.percent_encode(tenant_id)}/templates',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_template_with_options_async(
        self,
        tenant_id: str,
        request: main_models.CreateTemplateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateTemplateResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTemplate',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = f'/openapi/api/v1/tenants/{DaraURL.percent_encode(tenant_id)}/templates',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_template(
        self,
        tenant_id: str,
        request: main_models.CreateTemplateRequest,
    ) -> main_models.CreateTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_template_with_options(tenant_id, request, headers, runtime)

    async def create_template_async(
        self,
        tenant_id: str,
        request: main_models.CreateTemplateRequest,
    ) -> main_models.CreateTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_template_with_options_async(tenant_id, request, headers, runtime)

    def create_user_with_options(
        self,
        tenant_id: str,
        request: main_models.CreateUserRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateUserResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.account_type):
            body['AccountType'] = request.account_type
        if not DaraCore.is_null(request.role):
            body['Role'] = request.role
        if not DaraCore.is_null(request.user_name):
            body['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateUser',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = f'/openapi/api/v1/tenants/{DaraURL.percent_encode(tenant_id)}/users',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_user_with_options_async(
        self,
        tenant_id: str,
        request: main_models.CreateUserRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateUserResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_no):
            body['AccountNo'] = request.account_no
        if not DaraCore.is_null(request.account_type):
            body['AccountType'] = request.account_type
        if not DaraCore.is_null(request.role):
            body['Role'] = request.role
        if not DaraCore.is_null(request.user_name):
            body['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateUser',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = f'/openapi/api/v1/tenants/{DaraURL.percent_encode(tenant_id)}/users',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_user(
        self,
        tenant_id: str,
        request: main_models.CreateUserRequest,
    ) -> main_models.CreateUserResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_user_with_options(tenant_id, request, headers, runtime)

    async def create_user_async(
        self,
        tenant_id: str,
        request: main_models.CreateUserRequest,
    ) -> main_models.CreateUserResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_user_with_options_async(tenant_id, request, headers, runtime)

    def delete_task_with_options(
        self,
        tenant_id: str,
        task_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTaskResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteTask',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = f'/openapi/api/v1/tenants/{DaraURL.percent_encode(tenant_id)}/tasks/{DaraURL.percent_encode(task_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_task_with_options_async(
        self,
        tenant_id: str,
        task_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTaskResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteTask',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = f'/openapi/api/v1/tenants/{DaraURL.percent_encode(tenant_id)}/tasks/{DaraURL.percent_encode(task_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_task(
        self,
        tenant_id: str,
        task_id: str,
    ) -> main_models.DeleteTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_task_with_options(tenant_id, task_id, headers, runtime)

    async def delete_task_async(
        self,
        tenant_id: str,
        task_id: str,
    ) -> main_models.DeleteTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_task_with_options_async(tenant_id, task_id, headers, runtime)

    def delete_template_with_options(
        self,
        tenant_id: str,
        template_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTemplateResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteTemplate',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = f'/openapi/api/v1/tenants/{DaraURL.percent_encode(tenant_id)}/templates/{DaraURL.percent_encode(template_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_template_with_options_async(
        self,
        tenant_id: str,
        template_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTemplateResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteTemplate',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = f'/openapi/api/v1/tenants/{DaraURL.percent_encode(tenant_id)}/templates/{DaraURL.percent_encode(template_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_template(
        self,
        tenant_id: str,
        template_id: str,
    ) -> main_models.DeleteTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_template_with_options(tenant_id, template_id, headers, runtime)

    async def delete_template_async(
        self,
        tenant_id: str,
        template_id: str,
    ) -> main_models.DeleteTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_template_with_options_async(tenant_id, template_id, headers, runtime)

    def delete_user_with_options(
        self,
        tenant_id: str,
        user_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUserResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteUser',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = f'/openapi/api/v1/tenants/{DaraURL.percent_encode(tenant_id)}/users/{DaraURL.percent_encode(user_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_user_with_options_async(
        self,
        tenant_id: str,
        user_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUserResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteUser',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = f'/openapi/api/v1/tenants/{DaraURL.percent_encode(tenant_id)}/users/{DaraURL.percent_encode(user_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_user(
        self,
        tenant_id: str,
        user_id: str,
    ) -> main_models.DeleteUserResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_user_with_options(tenant_id, user_id, headers, runtime)

    async def delete_user_async(
        self,
        tenant_id: str,
        user_id: str,
    ) -> main_models.DeleteUserResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_user_with_options_async(tenant_id, user_id, headers, runtime)

    def export_annotations_with_options(
        self,
        tenant_id: str,
        task_id: str,
        request: main_models.ExportAnnotationsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExportAnnotationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.oss_path):
            query['OssPath'] = request.oss_path
        if not DaraCore.is_null(request.register_dataset):
            query['RegisterDataset'] = request.register_dataset
        if not DaraCore.is_null(request.target):
            query['Target'] = request.target
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExportAnnotations',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = f'/openapi/api/v1/tenants/{DaraURL.percent_encode(tenant_id)}/tasks/{DaraURL.percent_encode(task_id)}/annotations/export',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExportAnnotationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_annotations_with_options_async(
        self,
        tenant_id: str,
        task_id: str,
        request: main_models.ExportAnnotationsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExportAnnotationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.oss_path):
            query['OssPath'] = request.oss_path
        if not DaraCore.is_null(request.register_dataset):
            query['RegisterDataset'] = request.register_dataset
        if not DaraCore.is_null(request.target):
            query['Target'] = request.target
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExportAnnotations',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = f'/openapi/api/v1/tenants/{DaraURL.percent_encode(tenant_id)}/tasks/{DaraURL.percent_encode(task_id)}/annotations/export',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExportAnnotationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_annotations(
        self,
        tenant_id: str,
        task_id: str,
        request: main_models.ExportAnnotationsRequest,
    ) -> main_models.ExportAnnotationsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.export_annotations_with_options(tenant_id, task_id, request, headers, runtime)

    async def export_annotations_async(
        self,
        tenant_id: str,
        task_id: str,
        request: main_models.ExportAnnotationsRequest,
    ) -> main_models.ExportAnnotationsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.export_annotations_with_options_async(tenant_id, task_id, request, headers, runtime)

    def get_job_with_options(
        self,
        tenant_id: str,
        job_id: str,
        request: main_models.GetJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_type):
            query['JobType'] = request.job_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetJob',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = f'/openapi/api/v1/tenants/{DaraURL.percent_encode(tenant_id)}/jobs/{DaraURL.percent_encode(job_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_job_with_options_async(
        self,
        tenant_id: str,
        job_id: str,
        request: main_models.GetJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_type):
            query['JobType'] = request.job_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetJob',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = f'/openapi/api/v1/tenants/{DaraURL.percent_encode(tenant_id)}/jobs/{DaraURL.percent_encode(job_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_job(
        self,
        tenant_id: str,
        job_id: str,
        request: main_models.GetJobRequest,
    ) -> main_models.GetJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_job_with_options(tenant_id, job_id, request, headers, runtime)

    async def get_job_async(
        self,
        tenant_id: str,
        job_id: str,
        request: main_models.GetJobRequest,
    ) -> main_models.GetJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_job_with_options_async(tenant_id, job_id, request, headers, runtime)

    def get_subtask_with_options(
        self,
        tenant_id: str,
        task_id: str,
        subtask_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSubtaskResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetSubtask',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = f'/openapi/api/v1/tenants/{DaraURL.percent_encode(tenant_id)}/tasks/{DaraURL.percent_encode(task_id)}/subtasks/{DaraURL.percent_encode(subtask_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSubtaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_subtask_with_options_async(
        self,
        tenant_id: str,
        task_id: str,
        subtask_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSubtaskResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetSubtask',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = f'/openapi/api/v1/tenants/{DaraURL.percent_encode(tenant_id)}/tasks/{DaraURL.percent_encode(task_id)}/subtasks/{DaraURL.percent_encode(subtask_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSubtaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_subtask(
        self,
        tenant_id: str,
        task_id: str,
        subtask_id: str,
    ) -> main_models.GetSubtaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_subtask_with_options(tenant_id, task_id, subtask_id, headers, runtime)

    async def get_subtask_async(
        self,
        tenant_id: str,
        task_id: str,
        subtask_id: str,
    ) -> main_models.GetSubtaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_subtask_with_options_async(tenant_id, task_id, subtask_id, headers, runtime)

    def get_subtask_item_with_options(
        self,
        tenant_id: str,
        task_id: str,
        subtask_id: str,
        item_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSubtaskItemResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetSubtaskItem',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = f'/openapi/api/v1/tenants/{DaraURL.percent_encode(tenant_id)}/tasks/{DaraURL.percent_encode(task_id)}/subtasks/{DaraURL.percent_encode(subtask_id)}/items/{DaraURL.percent_encode(item_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSubtaskItemResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_subtask_item_with_options_async(
        self,
        tenant_id: str,
        task_id: str,
        subtask_id: str,
        item_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSubtaskItemResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetSubtaskItem',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = f'/openapi/api/v1/tenants/{DaraURL.percent_encode(tenant_id)}/tasks/{DaraURL.percent_encode(task_id)}/subtasks/{DaraURL.percent_encode(subtask_id)}/items/{DaraURL.percent_encode(item_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSubtaskItemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_subtask_item(
        self,
        tenant_id: str,
        task_id: str,
        subtask_id: str,
        item_id: str,
    ) -> main_models.GetSubtaskItemResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_subtask_item_with_options(tenant_id, task_id, subtask_id, item_id, headers, runtime)

    async def get_subtask_item_async(
        self,
        tenant_id: str,
        task_id: str,
        subtask_id: str,
        item_id: str,
    ) -> main_models.GetSubtaskItemResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_subtask_item_with_options_async(tenant_id, task_id, subtask_id, item_id, headers, runtime)

    def get_task_with_options(
        self,
        tenant_id: str,
        task_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTaskResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetTask',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = f'/openapi/api/v1/tenants/{DaraURL.percent_encode(tenant_id)}/tasks/{DaraURL.percent_encode(task_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_task_with_options_async(
        self,
        tenant_id: str,
        task_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTaskResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetTask',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = f'/openapi/api/v1/tenants/{DaraURL.percent_encode(tenant_id)}/tasks/{DaraURL.percent_encode(task_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_task(
        self,
        tenant_id: str,
        task_id: str,
    ) -> main_models.GetTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_task_with_options(tenant_id, task_id, headers, runtime)

    async def get_task_async(
        self,
        tenant_id: str,
        task_id: str,
    ) -> main_models.GetTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_task_with_options_async(tenant_id, task_id, headers, runtime)

    def get_task_statistics_with_options(
        self,
        tenant_id: str,
        task_id: str,
        request: main_models.GetTaskStatisticsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTaskStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.stat_type):
            query['StatType'] = request.stat_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTaskStatistics',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = f'/openapi/api/v1/tenants/{DaraURL.percent_encode(tenant_id)}/tasks/{DaraURL.percent_encode(task_id)}/statistics',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTaskStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_task_statistics_with_options_async(
        self,
        tenant_id: str,
        task_id: str,
        request: main_models.GetTaskStatisticsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTaskStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.stat_type):
            query['StatType'] = request.stat_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTaskStatistics',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = f'/openapi/api/v1/tenants/{DaraURL.percent_encode(tenant_id)}/tasks/{DaraURL.percent_encode(task_id)}/statistics',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTaskStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_task_statistics(
        self,
        tenant_id: str,
        task_id: str,
        request: main_models.GetTaskStatisticsRequest,
    ) -> main_models.GetTaskStatisticsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_task_statistics_with_options(tenant_id, task_id, request, headers, runtime)

    async def get_task_statistics_async(
        self,
        tenant_id: str,
        task_id: str,
        request: main_models.GetTaskStatisticsRequest,
    ) -> main_models.GetTaskStatisticsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_task_statistics_with_options_async(tenant_id, task_id, request, headers, runtime)

    def get_task_status_with_options(
        self,
        tenant_id: str,
        task_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTaskStatusResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetTaskStatus',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = f'/openapi/api/v1/tenants/{DaraURL.percent_encode(tenant_id)}/tasks/{DaraURL.percent_encode(task_id)}/status',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTaskStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_task_status_with_options_async(
        self,
        tenant_id: str,
        task_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTaskStatusResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetTaskStatus',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = f'/openapi/api/v1/tenants/{DaraURL.percent_encode(tenant_id)}/tasks/{DaraURL.percent_encode(task_id)}/status',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTaskStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_task_status(
        self,
        tenant_id: str,
        task_id: str,
    ) -> main_models.GetTaskStatusResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_task_status_with_options(tenant_id, task_id, headers, runtime)

    async def get_task_status_async(
        self,
        tenant_id: str,
        task_id: str,
    ) -> main_models.GetTaskStatusResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_task_status_with_options_async(tenant_id, task_id, headers, runtime)

    def get_task_template_with_options(
        self,
        tenant_id: str,
        task_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTaskTemplateResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetTaskTemplate',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = f'/openapi/api/v1/tenants/{DaraURL.percent_encode(tenant_id)}/tasks/{DaraURL.percent_encode(task_id)}/template',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTaskTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_task_template_with_options_async(
        self,
        tenant_id: str,
        task_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTaskTemplateResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetTaskTemplate',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = f'/openapi/api/v1/tenants/{DaraURL.percent_encode(tenant_id)}/tasks/{DaraURL.percent_encode(task_id)}/template',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTaskTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_task_template(
        self,
        tenant_id: str,
        task_id: str,
    ) -> main_models.GetTaskTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_task_template_with_options(tenant_id, task_id, headers, runtime)

    async def get_task_template_async(
        self,
        tenant_id: str,
        task_id: str,
    ) -> main_models.GetTaskTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_task_template_with_options_async(tenant_id, task_id, headers, runtime)

    def get_task_template_questions_with_options(
        self,
        tenant_id: str,
        task_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTaskTemplateQuestionsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetTaskTemplateQuestions',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = f'/openapi/api/v1/tenants/{DaraURL.percent_encode(tenant_id)}/tasks/{DaraURL.percent_encode(task_id)}/template/questions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTaskTemplateQuestionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_task_template_questions_with_options_async(
        self,
        tenant_id: str,
        task_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTaskTemplateQuestionsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetTaskTemplateQuestions',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = f'/openapi/api/v1/tenants/{DaraURL.percent_encode(tenant_id)}/tasks/{DaraURL.percent_encode(task_id)}/template/questions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTaskTemplateQuestionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_task_template_questions(
        self,
        tenant_id: str,
        task_id: str,
    ) -> main_models.GetTaskTemplateQuestionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_task_template_questions_with_options(tenant_id, task_id, headers, runtime)

    async def get_task_template_questions_async(
        self,
        tenant_id: str,
        task_id: str,
    ) -> main_models.GetTaskTemplateQuestionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_task_template_questions_with_options_async(tenant_id, task_id, headers, runtime)

    def get_task_template_views_with_options(
        self,
        tenant_id: str,
        task_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTaskTemplateViewsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetTaskTemplateViews',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = f'/openapi/api/v1/tenants/{DaraURL.percent_encode(tenant_id)}/tasks/{DaraURL.percent_encode(task_id)}/template/views',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTaskTemplateViewsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_task_template_views_with_options_async(
        self,
        tenant_id: str,
        task_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTaskTemplateViewsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetTaskTemplateViews',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = f'/openapi/api/v1/tenants/{DaraURL.percent_encode(tenant_id)}/tasks/{DaraURL.percent_encode(task_id)}/template/views',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTaskTemplateViewsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_task_template_views(
        self,
        tenant_id: str,
        task_id: str,
    ) -> main_models.GetTaskTemplateViewsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_task_template_views_with_options(tenant_id, task_id, headers, runtime)

    async def get_task_template_views_async(
        self,
        tenant_id: str,
        task_id: str,
    ) -> main_models.GetTaskTemplateViewsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_task_template_views_with_options_async(tenant_id, task_id, headers, runtime)

    def get_task_workforce_with_options(
        self,
        tenant_id: str,
        task_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTaskWorkforceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetTaskWorkforce',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = f'/openapi/api/v1/tenants/{DaraURL.percent_encode(tenant_id)}/tasks/{DaraURL.percent_encode(task_id)}/workforce',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTaskWorkforceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_task_workforce_with_options_async(
        self,
        tenant_id: str,
        task_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTaskWorkforceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetTaskWorkforce',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = f'/openapi/api/v1/tenants/{DaraURL.percent_encode(tenant_id)}/tasks/{DaraURL.percent_encode(task_id)}/workforce',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTaskWorkforceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_task_workforce(
        self,
        tenant_id: str,
        task_id: str,
    ) -> main_models.GetTaskWorkforceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_task_workforce_with_options(tenant_id, task_id, headers, runtime)

    async def get_task_workforce_async(
        self,
        tenant_id: str,
        task_id: str,
    ) -> main_models.GetTaskWorkforceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_task_workforce_with_options_async(tenant_id, task_id, headers, runtime)

    def get_task_workforce_statistic_with_options(
        self,
        tenant_id: str,
        task_id: str,
        request: main_models.GetTaskWorkforceStatisticRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTaskWorkforceStatisticResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.stat_type):
            query['StatType'] = request.stat_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTaskWorkforceStatistic',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = f'/openapi/api/v1/tenants/{DaraURL.percent_encode(tenant_id)}/tasks/{DaraURL.percent_encode(task_id)}/workforce/statistic',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTaskWorkforceStatisticResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_task_workforce_statistic_with_options_async(
        self,
        tenant_id: str,
        task_id: str,
        request: main_models.GetTaskWorkforceStatisticRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTaskWorkforceStatisticResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.stat_type):
            query['StatType'] = request.stat_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTaskWorkforceStatistic',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = f'/openapi/api/v1/tenants/{DaraURL.percent_encode(tenant_id)}/tasks/{DaraURL.percent_encode(task_id)}/workforce/statistic',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTaskWorkforceStatisticResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_task_workforce_statistic(
        self,
        tenant_id: str,
        task_id: str,
        request: main_models.GetTaskWorkforceStatisticRequest,
    ) -> main_models.GetTaskWorkforceStatisticResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_task_workforce_statistic_with_options(tenant_id, task_id, request, headers, runtime)

    async def get_task_workforce_statistic_async(
        self,
        tenant_id: str,
        task_id: str,
        request: main_models.GetTaskWorkforceStatisticRequest,
    ) -> main_models.GetTaskWorkforceStatisticResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_task_workforce_statistic_with_options_async(tenant_id, task_id, request, headers, runtime)

    def get_template_with_options(
        self,
        tenant_id: str,
        template_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTemplateResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetTemplate',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = f'/openapi/api/v1/tenants/{DaraURL.percent_encode(tenant_id)}/templates/{DaraURL.percent_encode(template_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_template_with_options_async(
        self,
        tenant_id: str,
        template_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTemplateResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetTemplate',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = f'/openapi/api/v1/tenants/{DaraURL.percent_encode(tenant_id)}/templates/{DaraURL.percent_encode(template_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_template(
        self,
        tenant_id: str,
        template_id: str,
    ) -> main_models.GetTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_template_with_options(tenant_id, template_id, headers, runtime)

    async def get_template_async(
        self,
        tenant_id: str,
        template_id: str,
    ) -> main_models.GetTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_template_with_options_async(tenant_id, template_id, headers, runtime)

    def get_template_questions_with_options(
        self,
        tenant_id: str,
        template_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTemplateQuestionsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetTemplateQuestions',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = f'/openapi/api/v1/tenants/{DaraURL.percent_encode(tenant_id)}/templates/{DaraURL.percent_encode(template_id)}/questions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTemplateQuestionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_template_questions_with_options_async(
        self,
        tenant_id: str,
        template_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTemplateQuestionsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetTemplateQuestions',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = f'/openapi/api/v1/tenants/{DaraURL.percent_encode(tenant_id)}/templates/{DaraURL.percent_encode(template_id)}/questions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTemplateQuestionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_template_questions(
        self,
        tenant_id: str,
        template_id: str,
    ) -> main_models.GetTemplateQuestionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_template_questions_with_options(tenant_id, template_id, headers, runtime)

    async def get_template_questions_async(
        self,
        tenant_id: str,
        template_id: str,
    ) -> main_models.GetTemplateQuestionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_template_questions_with_options_async(tenant_id, template_id, headers, runtime)

    def get_template_view_with_options(
        self,
        tenant_id: str,
        template_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTemplateViewResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetTemplateView',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = f'/openapi/api/v1/tenants/{DaraURL.percent_encode(tenant_id)}/templates/{DaraURL.percent_encode(template_id)}/views',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTemplateViewResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_template_view_with_options_async(
        self,
        tenant_id: str,
        template_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTemplateViewResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetTemplateView',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = f'/openapi/api/v1/tenants/{DaraURL.percent_encode(tenant_id)}/templates/{DaraURL.percent_encode(template_id)}/views',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTemplateViewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_template_view(
        self,
        tenant_id: str,
        template_id: str,
    ) -> main_models.GetTemplateViewResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_template_view_with_options(tenant_id, template_id, headers, runtime)

    async def get_template_view_async(
        self,
        tenant_id: str,
        template_id: str,
    ) -> main_models.GetTemplateViewResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_template_view_with_options_async(tenant_id, template_id, headers, runtime)

    def get_tenant_with_options(
        self,
        tenant_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTenantResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetTenant',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = f'/openapi/api/v1/tenants/{DaraURL.percent_encode(tenant_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTenantResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_tenant_with_options_async(
        self,
        tenant_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTenantResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetTenant',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = f'/openapi/api/v1/tenants/{DaraURL.percent_encode(tenant_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTenantResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_tenant(
        self,
        tenant_id: str,
    ) -> main_models.GetTenantResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_tenant_with_options(tenant_id, headers, runtime)

    async def get_tenant_async(
        self,
        tenant_id: str,
    ) -> main_models.GetTenantResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_tenant_with_options_async(tenant_id, headers, runtime)

    def get_user_with_options(
        self,
        tenant_id: str,
        user_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetUserResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetUser',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = f'/openapi/api/v1/tenants/{DaraURL.percent_encode(tenant_id)}/users/{DaraURL.percent_encode(user_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_with_options_async(
        self,
        tenant_id: str,
        user_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetUserResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetUser',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = f'/openapi/api/v1/tenants/{DaraURL.percent_encode(tenant_id)}/users/{DaraURL.percent_encode(user_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user(
        self,
        tenant_id: str,
        user_id: str,
    ) -> main_models.GetUserResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_user_with_options(tenant_id, user_id, headers, runtime)

    async def get_user_async(
        self,
        tenant_id: str,
        user_id: str,
    ) -> main_models.GetUserResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_user_with_options_async(tenant_id, user_id, headers, runtime)

    def list_jobs_with_options(
        self,
        tenant_id: str,
        request: main_models.ListJobsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_type):
            query['JobType'] = request.job_type
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListJobs',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = f'/openapi/api/v1/tenants/{DaraURL.percent_encode(tenant_id)}/jobs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_jobs_with_options_async(
        self,
        tenant_id: str,
        request: main_models.ListJobsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_type):
            query['JobType'] = request.job_type
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListJobs',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = f'/openapi/api/v1/tenants/{DaraURL.percent_encode(tenant_id)}/jobs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_jobs(
        self,
        tenant_id: str,
        request: main_models.ListJobsRequest,
    ) -> main_models.ListJobsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_jobs_with_options(tenant_id, request, headers, runtime)

    async def list_jobs_async(
        self,
        tenant_id: str,
        request: main_models.ListJobsRequest,
    ) -> main_models.ListJobsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_jobs_with_options_async(tenant_id, request, headers, runtime)

    def list_subtask_items_with_options(
        self,
        tenant_id: str,
        task_id: str,
        subtask_id: str,
        request: main_models.ListSubtaskItemsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSubtaskItemsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSubtaskItems',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = f'/openapi/api/v1/tenants/{DaraURL.percent_encode(tenant_id)}/tasks/{DaraURL.percent_encode(task_id)}/subtasks/{DaraURL.percent_encode(subtask_id)}/items',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSubtaskItemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_subtask_items_with_options_async(
        self,
        tenant_id: str,
        task_id: str,
        subtask_id: str,
        request: main_models.ListSubtaskItemsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSubtaskItemsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSubtaskItems',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = f'/openapi/api/v1/tenants/{DaraURL.percent_encode(tenant_id)}/tasks/{DaraURL.percent_encode(task_id)}/subtasks/{DaraURL.percent_encode(subtask_id)}/items',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSubtaskItemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_subtask_items(
        self,
        tenant_id: str,
        task_id: str,
        subtask_id: str,
        request: main_models.ListSubtaskItemsRequest,
    ) -> main_models.ListSubtaskItemsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_subtask_items_with_options(tenant_id, task_id, subtask_id, request, headers, runtime)

    async def list_subtask_items_async(
        self,
        tenant_id: str,
        task_id: str,
        subtask_id: str,
        request: main_models.ListSubtaskItemsRequest,
    ) -> main_models.ListSubtaskItemsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_subtask_items_with_options_async(tenant_id, task_id, subtask_id, request, headers, runtime)

    def list_subtasks_with_options(
        self,
        tenant_id: str,
        task_id: str,
        request: main_models.ListSubtasksRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSubtasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSubtasks',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = f'/openapi/api/v1/tenants/{DaraURL.percent_encode(tenant_id)}/tasks/{DaraURL.percent_encode(task_id)}/subtasks',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSubtasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_subtasks_with_options_async(
        self,
        tenant_id: str,
        task_id: str,
        request: main_models.ListSubtasksRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSubtasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSubtasks',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = f'/openapi/api/v1/tenants/{DaraURL.percent_encode(tenant_id)}/tasks/{DaraURL.percent_encode(task_id)}/subtasks',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSubtasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_subtasks(
        self,
        tenant_id: str,
        task_id: str,
        request: main_models.ListSubtasksRequest,
    ) -> main_models.ListSubtasksResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_subtasks_with_options(tenant_id, task_id, request, headers, runtime)

    async def list_subtasks_async(
        self,
        tenant_id: str,
        task_id: str,
        request: main_models.ListSubtasksRequest,
    ) -> main_models.ListSubtasksResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_subtasks_with_options_async(tenant_id, task_id, request, headers, runtime)

    def list_tasks_with_options(
        self,
        tenant_id: str,
        request: main_models.ListTasksRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTasks',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = f'/openapi/api/v1/tenants/{DaraURL.percent_encode(tenant_id)}/tasks',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tasks_with_options_async(
        self,
        tenant_id: str,
        request: main_models.ListTasksRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTasks',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = f'/openapi/api/v1/tenants/{DaraURL.percent_encode(tenant_id)}/tasks',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tasks(
        self,
        tenant_id: str,
        request: main_models.ListTasksRequest,
    ) -> main_models.ListTasksResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_tasks_with_options(tenant_id, request, headers, runtime)

    async def list_tasks_async(
        self,
        tenant_id: str,
        request: main_models.ListTasksRequest,
    ) -> main_models.ListTasksResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_tasks_with_options_async(tenant_id, request, headers, runtime)

    def list_templates_with_options(
        self,
        tenant_id: str,
        tmp_req: main_models.ListTemplatesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTemplatesResponse:
        tmp_req.validate()
        request = main_models.ListTemplatesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.types):
            request.types_shrink = Utils.array_to_string_with_specified_style(tmp_req.types, 'Types', 'simple')
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.search_key):
            query['SearchKey'] = request.search_key
        if not DaraCore.is_null(request.types_shrink):
            query['Types'] = request.types_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTemplates',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = f'/openapi/api/v1/tenants/{DaraURL.percent_encode(tenant_id)}/templates',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_templates_with_options_async(
        self,
        tenant_id: str,
        tmp_req: main_models.ListTemplatesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTemplatesResponse:
        tmp_req.validate()
        request = main_models.ListTemplatesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.types):
            request.types_shrink = Utils.array_to_string_with_specified_style(tmp_req.types, 'Types', 'simple')
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.search_key):
            query['SearchKey'] = request.search_key
        if not DaraCore.is_null(request.types_shrink):
            query['Types'] = request.types_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTemplates',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = f'/openapi/api/v1/tenants/{DaraURL.percent_encode(tenant_id)}/templates',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_templates(
        self,
        tenant_id: str,
        request: main_models.ListTemplatesRequest,
    ) -> main_models.ListTemplatesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_templates_with_options(tenant_id, request, headers, runtime)

    async def list_templates_async(
        self,
        tenant_id: str,
        request: main_models.ListTemplatesRequest,
    ) -> main_models.ListTemplatesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_templates_with_options_async(tenant_id, request, headers, runtime)

    def list_tenants_with_options(
        self,
        request: main_models.ListTenantsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTenantsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTenants',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = f'/openapi/api/v1/tenants',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTenantsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tenants_with_options_async(
        self,
        request: main_models.ListTenantsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTenantsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTenants',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = f'/openapi/api/v1/tenants',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTenantsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tenants(
        self,
        request: main_models.ListTenantsRequest,
    ) -> main_models.ListTenantsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_tenants_with_options(request, headers, runtime)

    async def list_tenants_async(
        self,
        request: main_models.ListTenantsRequest,
    ) -> main_models.ListTenantsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_tenants_with_options_async(request, headers, runtime)

    def list_users_with_options(
        self,
        tenant_id: str,
        request: main_models.ListUsersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUsers',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = f'/openapi/api/v1/tenants/{DaraURL.percent_encode(tenant_id)}/users',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_users_with_options_async(
        self,
        tenant_id: str,
        request: main_models.ListUsersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUsers',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = f'/openapi/api/v1/tenants/{DaraURL.percent_encode(tenant_id)}/users',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_users(
        self,
        tenant_id: str,
        request: main_models.ListUsersRequest,
    ) -> main_models.ListUsersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_users_with_options(tenant_id, request, headers, runtime)

    async def list_users_async(
        self,
        tenant_id: str,
        request: main_models.ListUsersRequest,
    ) -> main_models.ListUsersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_users_with_options_async(tenant_id, request, headers, runtime)

    def remove_work_node_workforce_with_options(
        self,
        tenant_id: str,
        task_id: str,
        work_node_id: str,
        request: main_models.RemoveWorkNodeWorkforceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RemoveWorkNodeWorkforceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.user_ids):
            body['UserIds'] = request.user_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RemoveWorkNodeWorkforce',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = f'/openapi/api/v1/tenants/{DaraURL.percent_encode(tenant_id)}/tasks/{DaraURL.percent_encode(task_id)}/worknodes/{DaraURL.percent_encode(work_node_id)}/workforce',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveWorkNodeWorkforceResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_work_node_workforce_with_options_async(
        self,
        tenant_id: str,
        task_id: str,
        work_node_id: str,
        request: main_models.RemoveWorkNodeWorkforceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RemoveWorkNodeWorkforceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.user_ids):
            body['UserIds'] = request.user_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RemoveWorkNodeWorkforce',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = f'/openapi/api/v1/tenants/{DaraURL.percent_encode(tenant_id)}/tasks/{DaraURL.percent_encode(task_id)}/worknodes/{DaraURL.percent_encode(work_node_id)}/workforce',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveWorkNodeWorkforceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_work_node_workforce(
        self,
        tenant_id: str,
        task_id: str,
        work_node_id: str,
        request: main_models.RemoveWorkNodeWorkforceRequest,
    ) -> main_models.RemoveWorkNodeWorkforceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.remove_work_node_workforce_with_options(tenant_id, task_id, work_node_id, request, headers, runtime)

    async def remove_work_node_workforce_async(
        self,
        tenant_id: str,
        task_id: str,
        work_node_id: str,
        request: main_models.RemoveWorkNodeWorkforceRequest,
    ) -> main_models.RemoveWorkNodeWorkforceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.remove_work_node_workforce_with_options_async(tenant_id, task_id, work_node_id, request, headers, runtime)

    def update_task_with_options(
        self,
        tenant_id: str,
        task_id: str,
        request: main_models.UpdateTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTaskResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTask',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = f'/openapi/api/v1/tenants/{DaraURL.percent_encode(tenant_id)}/tasks/{DaraURL.percent_encode(task_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_task_with_options_async(
        self,
        tenant_id: str,
        task_id: str,
        request: main_models.UpdateTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTaskResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTask',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = f'/openapi/api/v1/tenants/{DaraURL.percent_encode(tenant_id)}/tasks/{DaraURL.percent_encode(task_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_task(
        self,
        tenant_id: str,
        task_id: str,
        request: main_models.UpdateTaskRequest,
    ) -> main_models.UpdateTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_task_with_options(tenant_id, task_id, request, headers, runtime)

    async def update_task_async(
        self,
        tenant_id: str,
        task_id: str,
        request: main_models.UpdateTaskRequest,
    ) -> main_models.UpdateTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_task_with_options_async(tenant_id, task_id, request, headers, runtime)

    def update_task_workforce_with_options(
        self,
        tenant_id: str,
        task_id: str,
        request: main_models.UpdateTaskWorkforceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTaskWorkforceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.workforce):
            body['Workforce'] = request.workforce
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTaskWorkforce',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = f'/openapi/api/v1/tenants/{DaraURL.percent_encode(tenant_id)}/tasks/{DaraURL.percent_encode(task_id)}/workforce',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTaskWorkforceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_task_workforce_with_options_async(
        self,
        tenant_id: str,
        task_id: str,
        request: main_models.UpdateTaskWorkforceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTaskWorkforceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.workforce):
            body['Workforce'] = request.workforce
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTaskWorkforce',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = f'/openapi/api/v1/tenants/{DaraURL.percent_encode(tenant_id)}/tasks/{DaraURL.percent_encode(task_id)}/workforce',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTaskWorkforceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_task_workforce(
        self,
        tenant_id: str,
        task_id: str,
        request: main_models.UpdateTaskWorkforceRequest,
    ) -> main_models.UpdateTaskWorkforceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_task_workforce_with_options(tenant_id, task_id, request, headers, runtime)

    async def update_task_workforce_async(
        self,
        tenant_id: str,
        task_id: str,
        request: main_models.UpdateTaskWorkforceRequest,
    ) -> main_models.UpdateTaskWorkforceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_task_workforce_with_options_async(tenant_id, task_id, request, headers, runtime)

    def update_template_with_options(
        self,
        tenant_id: str,
        template_id: str,
        request: main_models.UpdateTemplateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTemplateResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTemplate',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = f'/openapi/api/v1/tenants/{DaraURL.percent_encode(tenant_id)}/templates/{DaraURL.percent_encode(template_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_template_with_options_async(
        self,
        tenant_id: str,
        template_id: str,
        request: main_models.UpdateTemplateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTemplateResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTemplate',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = f'/openapi/api/v1/tenants/{DaraURL.percent_encode(tenant_id)}/templates/{DaraURL.percent_encode(template_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_template(
        self,
        tenant_id: str,
        template_id: str,
        request: main_models.UpdateTemplateRequest,
    ) -> main_models.UpdateTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_template_with_options(tenant_id, template_id, request, headers, runtime)

    async def update_template_async(
        self,
        tenant_id: str,
        template_id: str,
        request: main_models.UpdateTemplateRequest,
    ) -> main_models.UpdateTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_template_with_options_async(tenant_id, template_id, request, headers, runtime)

    def update_tenant_with_options(
        self,
        tenant_id: str,
        request: main_models.UpdateTenantRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTenantResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.tenant_name):
            body['TenantName'] = request.tenant_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTenant',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = f'/openapi/api/v1/tenants/{DaraURL.percent_encode(tenant_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTenantResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_tenant_with_options_async(
        self,
        tenant_id: str,
        request: main_models.UpdateTenantRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTenantResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.tenant_name):
            body['TenantName'] = request.tenant_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTenant',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = f'/openapi/api/v1/tenants/{DaraURL.percent_encode(tenant_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTenantResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_tenant(
        self,
        tenant_id: str,
        request: main_models.UpdateTenantRequest,
    ) -> main_models.UpdateTenantResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_tenant_with_options(tenant_id, request, headers, runtime)

    async def update_tenant_async(
        self,
        tenant_id: str,
        request: main_models.UpdateTenantRequest,
    ) -> main_models.UpdateTenantResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_tenant_with_options_async(tenant_id, request, headers, runtime)

    def update_user_with_options(
        self,
        tenant_id: str,
        user_id: str,
        request: main_models.UpdateUserRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUserResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.role):
            body['Role'] = request.role
        if not DaraCore.is_null(request.user_name):
            body['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUser',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = f'/openapi/api/v1/tenants/{DaraURL.percent_encode(tenant_id)}/users/{DaraURL.percent_encode(user_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_user_with_options_async(
        self,
        tenant_id: str,
        user_id: str,
        request: main_models.UpdateUserRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUserResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.role):
            body['Role'] = request.role
        if not DaraCore.is_null(request.user_name):
            body['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUser',
            version = '2022-06-16',
            protocol = 'HTTPS',
            pathname = f'/openapi/api/v1/tenants/{DaraURL.percent_encode(tenant_id)}/users/{DaraURL.percent_encode(user_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_user(
        self,
        tenant_id: str,
        user_id: str,
        request: main_models.UpdateUserRequest,
    ) -> main_models.UpdateUserResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_user_with_options(tenant_id, user_id, request, headers, runtime)

    async def update_user_async(
        self,
        tenant_id: str,
        user_id: str,
        request: main_models.UpdateUserRequest,
    ) -> main_models.UpdateUserResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_user_with_options_async(tenant_id, user_id, request, headers, runtime)
