# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_maxcompute20220104 import models as max_compute_20220104_models
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
            'ap-northeast-1': 'maxcompute.aliyuncs.com',
            'ap-northeast-2-pop': 'maxcompute.aliyuncs.com',
            'ap-south-1': 'maxcompute.aliyuncs.com',
            'ap-southeast-1': 'maxcompute.aliyuncs.com',
            'ap-southeast-2': 'maxcompute.aliyuncs.com',
            'ap-southeast-3': 'maxcompute.aliyuncs.com',
            'ap-southeast-5': 'maxcompute.aliyuncs.com',
            'cn-beijing': 'maxcompute.aliyuncs.com',
            'cn-beijing-finance-1': 'maxcompute.aliyuncs.com',
            'cn-beijing-finance-pop': 'maxcompute.aliyuncs.com',
            'cn-beijing-gov-1': 'maxcompute.aliyuncs.com',
            'cn-beijing-nu16-b01': 'maxcompute.aliyuncs.com',
            'cn-chengdu': 'maxcompute.aliyuncs.com',
            'cn-edge-1': 'maxcompute.aliyuncs.com',
            'cn-fujian': 'maxcompute.aliyuncs.com',
            'cn-haidian-cm12-c01': 'maxcompute.aliyuncs.com',
            'cn-hangzhou': 'maxcompute.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'maxcompute.aliyuncs.com',
            'cn-hangzhou-finance': 'maxcompute.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'maxcompute.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'maxcompute.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'maxcompute.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'maxcompute.aliyuncs.com',
            'cn-hangzhou-test-306': 'maxcompute.aliyuncs.com',
            'cn-hongkong': 'maxcompute.aliyuncs.com',
            'cn-hongkong-finance-pop': 'maxcompute.aliyuncs.com',
            'cn-huhehaote': 'maxcompute.aliyuncs.com',
            'cn-north-2-gov-1': 'maxcompute.aliyuncs.com',
            'cn-qingdao': 'maxcompute.aliyuncs.com',
            'cn-qingdao-nebula': 'maxcompute.aliyuncs.com',
            'cn-shanghai': 'maxcompute.aliyuncs.com',
            'cn-shanghai-et15-b01': 'maxcompute.aliyuncs.com',
            'cn-shanghai-et2-b01': 'maxcompute.aliyuncs.com',
            'cn-shanghai-finance-1': 'maxcompute.aliyuncs.com',
            'cn-shanghai-inner': 'maxcompute.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'maxcompute.aliyuncs.com',
            'cn-shenzhen': 'maxcompute.aliyuncs.com',
            'cn-shenzhen-finance-1': 'maxcompute.aliyuncs.com',
            'cn-shenzhen-inner': 'maxcompute.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'maxcompute.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'maxcompute.aliyuncs.com',
            'cn-wuhan': 'maxcompute.aliyuncs.com',
            'cn-yushanfang': 'maxcompute.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'maxcompute.aliyuncs.com',
            'cn-zhangjiakou': 'maxcompute.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'maxcompute.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'maxcompute.aliyuncs.com',
            'eu-central-1': 'maxcompute.aliyuncs.com',
            'eu-west-1': 'maxcompute.aliyuncs.com',
            'eu-west-1-oxs': 'maxcompute.aliyuncs.com',
            'me-east-1': 'maxcompute.aliyuncs.com',
            'rus-west-1-pop': 'maxcompute.aliyuncs.com',
            'us-east-1': 'maxcompute.aliyuncs.com',
            'us-west-1': 'maxcompute.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('maxcompute', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_package_with_options(
        self,
        project_name: str,
        request: max_compute_20220104_models.CreatePackageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.CreatePackageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.is_install):
            query['isInstall'] = request.is_install
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='CreatePackage',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_name)}/packages',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.CreatePackageResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_package_with_options_async(
        self,
        project_name: str,
        request: max_compute_20220104_models.CreatePackageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.CreatePackageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.is_install):
            query['isInstall'] = request.is_install
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='CreatePackage',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_name)}/packages',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.CreatePackageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_package(
        self,
        project_name: str,
        request: max_compute_20220104_models.CreatePackageRequest,
    ) -> max_compute_20220104_models.CreatePackageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_package_with_options(project_name, request, headers, runtime)

    async def create_package_async(
        self,
        project_name: str,
        request: max_compute_20220104_models.CreatePackageRequest,
    ) -> max_compute_20220104_models.CreatePackageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_package_with_options_async(project_name, request, headers, runtime)

    def create_project_with_options(
        self,
        request: max_compute_20220104_models.CreateProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.CreateProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='CreateProject',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.CreateProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_project_with_options_async(
        self,
        request: max_compute_20220104_models.CreateProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.CreateProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='CreateProject',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.CreateProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_project(
        self,
        request: max_compute_20220104_models.CreateProjectRequest,
    ) -> max_compute_20220104_models.CreateProjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_project_with_options(request, headers, runtime)

    async def create_project_async(
        self,
        request: max_compute_20220104_models.CreateProjectRequest,
    ) -> max_compute_20220104_models.CreateProjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_project_with_options_async(request, headers, runtime)

    def create_quota_plan_with_options(
        self,
        nickname: str,
        request: max_compute_20220104_models.CreateQuotaPlanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.CreateQuotaPlanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='CreateQuotaPlan',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas/{OpenApiUtilClient.get_encode_param(nickname)}/plans',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.CreateQuotaPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_quota_plan_with_options_async(
        self,
        nickname: str,
        request: max_compute_20220104_models.CreateQuotaPlanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.CreateQuotaPlanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='CreateQuotaPlan',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas/{OpenApiUtilClient.get_encode_param(nickname)}/plans',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.CreateQuotaPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_quota_plan(
        self,
        nickname: str,
        request: max_compute_20220104_models.CreateQuotaPlanRequest,
    ) -> max_compute_20220104_models.CreateQuotaPlanResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_quota_plan_with_options(nickname, request, headers, runtime)

    async def create_quota_plan_async(
        self,
        nickname: str,
        request: max_compute_20220104_models.CreateQuotaPlanRequest,
    ) -> max_compute_20220104_models.CreateQuotaPlanResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_quota_plan_with_options_async(nickname, request, headers, runtime)

    def create_quota_schedule_with_options(
        self,
        nickname: str,
        request: max_compute_20220104_models.CreateQuotaScheduleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.CreateQuotaScheduleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='CreateQuotaSchedule',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas/{OpenApiUtilClient.get_encode_param(nickname)}/schedule',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.CreateQuotaScheduleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_quota_schedule_with_options_async(
        self,
        nickname: str,
        request: max_compute_20220104_models.CreateQuotaScheduleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.CreateQuotaScheduleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='CreateQuotaSchedule',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas/{OpenApiUtilClient.get_encode_param(nickname)}/schedule',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.CreateQuotaScheduleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_quota_schedule(
        self,
        nickname: str,
        request: max_compute_20220104_models.CreateQuotaScheduleRequest,
    ) -> max_compute_20220104_models.CreateQuotaScheduleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_quota_schedule_with_options(nickname, request, headers, runtime)

    async def create_quota_schedule_async(
        self,
        nickname: str,
        request: max_compute_20220104_models.CreateQuotaScheduleRequest,
    ) -> max_compute_20220104_models.CreateQuotaScheduleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_quota_schedule_with_options_async(nickname, request, headers, runtime)

    def create_role_with_options(
        self,
        project_name: str,
        request: max_compute_20220104_models.CreateRoleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.CreateRoleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='CreateRole',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_name)}/roles',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.CreateRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_role_with_options_async(
        self,
        project_name: str,
        request: max_compute_20220104_models.CreateRoleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.CreateRoleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='CreateRole',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_name)}/roles',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.CreateRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_role(
        self,
        project_name: str,
        request: max_compute_20220104_models.CreateRoleRequest,
    ) -> max_compute_20220104_models.CreateRoleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_role_with_options(project_name, request, headers, runtime)

    async def create_role_async(
        self,
        project_name: str,
        request: max_compute_20220104_models.CreateRoleRequest,
    ) -> max_compute_20220104_models.CreateRoleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_role_with_options_async(project_name, request, headers, runtime)

    def delete_quota_plan_with_options(
        self,
        nickname: str,
        plan_name: str,
        request: max_compute_20220104_models.DeleteQuotaPlanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.DeleteQuotaPlanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteQuotaPlan',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas/{OpenApiUtilClient.get_encode_param(nickname)}/plans/{OpenApiUtilClient.get_encode_param(plan_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.DeleteQuotaPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_quota_plan_with_options_async(
        self,
        nickname: str,
        plan_name: str,
        request: max_compute_20220104_models.DeleteQuotaPlanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.DeleteQuotaPlanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteQuotaPlan',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas/{OpenApiUtilClient.get_encode_param(nickname)}/plans/{OpenApiUtilClient.get_encode_param(plan_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.DeleteQuotaPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_quota_plan(
        self,
        nickname: str,
        plan_name: str,
        request: max_compute_20220104_models.DeleteQuotaPlanRequest,
    ) -> max_compute_20220104_models.DeleteQuotaPlanResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_quota_plan_with_options(nickname, plan_name, request, headers, runtime)

    async def delete_quota_plan_async(
        self,
        nickname: str,
        plan_name: str,
        request: max_compute_20220104_models.DeleteQuotaPlanRequest,
    ) -> max_compute_20220104_models.DeleteQuotaPlanResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_quota_plan_with_options_async(nickname, plan_name, request, headers, runtime)

    def get_job_resource_usage_with_options(
        self,
        tmp_req: max_compute_20220104_models.GetJobResourceUsageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetJobResourceUsageResponse:
        UtilClient.validate_model(tmp_req)
        request = max_compute_20220104_models.GetJobResourceUsageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.job_owner_list):
            request.job_owner_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.job_owner_list, 'jobOwnerList', 'simple')
        if not UtilClient.is_unset(tmp_req.quota_nickname_list):
            request.quota_nickname_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.quota_nickname_list, 'quotaNicknameList', 'simple')
        query = {}
        if not UtilClient.is_unset(request.date):
            query['date'] = request.date
        if not UtilClient.is_unset(request.job_owner_list_shrink):
            query['jobOwnerList'] = request.job_owner_list_shrink
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.quota_nickname_list_shrink):
            query['quotaNicknameList'] = request.quota_nickname_list_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJobResourceUsage',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/jobs/resourceUsage',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetJobResourceUsageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_job_resource_usage_with_options_async(
        self,
        tmp_req: max_compute_20220104_models.GetJobResourceUsageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetJobResourceUsageResponse:
        UtilClient.validate_model(tmp_req)
        request = max_compute_20220104_models.GetJobResourceUsageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.job_owner_list):
            request.job_owner_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.job_owner_list, 'jobOwnerList', 'simple')
        if not UtilClient.is_unset(tmp_req.quota_nickname_list):
            request.quota_nickname_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.quota_nickname_list, 'quotaNicknameList', 'simple')
        query = {}
        if not UtilClient.is_unset(request.date):
            query['date'] = request.date
        if not UtilClient.is_unset(request.job_owner_list_shrink):
            query['jobOwnerList'] = request.job_owner_list_shrink
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.quota_nickname_list_shrink):
            query['quotaNicknameList'] = request.quota_nickname_list_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJobResourceUsage',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/jobs/resourceUsage',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetJobResourceUsageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_job_resource_usage(
        self,
        request: max_compute_20220104_models.GetJobResourceUsageRequest,
    ) -> max_compute_20220104_models.GetJobResourceUsageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_job_resource_usage_with_options(request, headers, runtime)

    async def get_job_resource_usage_async(
        self,
        request: max_compute_20220104_models.GetJobResourceUsageRequest,
    ) -> max_compute_20220104_models.GetJobResourceUsageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_job_resource_usage_with_options_async(request, headers, runtime)

    def get_package_with_options(
        self,
        project_name: str,
        package_name: str,
        request: max_compute_20220104_models.GetPackageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetPackageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.source_project):
            query['sourceProject'] = request.source_project
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPackage',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_name)}/packages/{OpenApiUtilClient.get_encode_param(package_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetPackageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_package_with_options_async(
        self,
        project_name: str,
        package_name: str,
        request: max_compute_20220104_models.GetPackageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetPackageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.source_project):
            query['sourceProject'] = request.source_project
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPackage',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_name)}/packages/{OpenApiUtilClient.get_encode_param(package_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetPackageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_package(
        self,
        project_name: str,
        package_name: str,
        request: max_compute_20220104_models.GetPackageRequest,
    ) -> max_compute_20220104_models.GetPackageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_package_with_options(project_name, package_name, request, headers, runtime)

    async def get_package_async(
        self,
        project_name: str,
        package_name: str,
        request: max_compute_20220104_models.GetPackageRequest,
    ) -> max_compute_20220104_models.GetPackageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_package_with_options_async(project_name, package_name, request, headers, runtime)

    def get_project_with_options(
        self,
        project_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetProjectResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetProject',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_project_with_options_async(
        self,
        project_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetProjectResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetProject',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_project(
        self,
        project_name: str,
    ) -> max_compute_20220104_models.GetProjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_project_with_options(project_name, headers, runtime)

    async def get_project_async(
        self,
        project_name: str,
    ) -> max_compute_20220104_models.GetProjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_project_with_options_async(project_name, headers, runtime)

    def get_quota_with_options(
        self,
        nickname: str,
        request: max_compute_20220104_models.GetQuotaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetQuotaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ak_proven):
            query['AkProven'] = request.ak_proven
        if not UtilClient.is_unset(request.mock):
            query['mock'] = request.mock
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQuota',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas/{OpenApiUtilClient.get_encode_param(nickname)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_quota_with_options_async(
        self,
        nickname: str,
        request: max_compute_20220104_models.GetQuotaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetQuotaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ak_proven):
            query['AkProven'] = request.ak_proven
        if not UtilClient.is_unset(request.mock):
            query['mock'] = request.mock
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQuota',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas/{OpenApiUtilClient.get_encode_param(nickname)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_quota(
        self,
        nickname: str,
        request: max_compute_20220104_models.GetQuotaRequest,
    ) -> max_compute_20220104_models.GetQuotaResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_quota_with_options(nickname, request, headers, runtime)

    async def get_quota_async(
        self,
        nickname: str,
        request: max_compute_20220104_models.GetQuotaRequest,
    ) -> max_compute_20220104_models.GetQuotaResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_quota_with_options_async(nickname, request, headers, runtime)

    def get_quota_plan_with_options(
        self,
        nickname: str,
        plan_name: str,
        request: max_compute_20220104_models.GetQuotaPlanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetQuotaPlanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQuotaPlan',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas/{OpenApiUtilClient.get_encode_param(nickname)}/plans/{OpenApiUtilClient.get_encode_param(plan_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetQuotaPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_quota_plan_with_options_async(
        self,
        nickname: str,
        plan_name: str,
        request: max_compute_20220104_models.GetQuotaPlanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetQuotaPlanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQuotaPlan',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas/{OpenApiUtilClient.get_encode_param(nickname)}/plans/{OpenApiUtilClient.get_encode_param(plan_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetQuotaPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_quota_plan(
        self,
        nickname: str,
        plan_name: str,
        request: max_compute_20220104_models.GetQuotaPlanRequest,
    ) -> max_compute_20220104_models.GetQuotaPlanResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_quota_plan_with_options(nickname, plan_name, request, headers, runtime)

    async def get_quota_plan_async(
        self,
        nickname: str,
        plan_name: str,
        request: max_compute_20220104_models.GetQuotaPlanRequest,
    ) -> max_compute_20220104_models.GetQuotaPlanResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_quota_plan_with_options_async(nickname, plan_name, request, headers, runtime)

    def get_quota_schedule_with_options(
        self,
        nickname: str,
        request: max_compute_20220104_models.GetQuotaScheduleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetQuotaScheduleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.display_timezone):
            query['displayTimezone'] = request.display_timezone
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQuotaSchedule',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas/{OpenApiUtilClient.get_encode_param(nickname)}/schedule',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetQuotaScheduleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_quota_schedule_with_options_async(
        self,
        nickname: str,
        request: max_compute_20220104_models.GetQuotaScheduleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetQuotaScheduleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.display_timezone):
            query['displayTimezone'] = request.display_timezone
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQuotaSchedule',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas/{OpenApiUtilClient.get_encode_param(nickname)}/schedule',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetQuotaScheduleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_quota_schedule(
        self,
        nickname: str,
        request: max_compute_20220104_models.GetQuotaScheduleRequest,
    ) -> max_compute_20220104_models.GetQuotaScheduleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_quota_schedule_with_options(nickname, request, headers, runtime)

    async def get_quota_schedule_async(
        self,
        nickname: str,
        request: max_compute_20220104_models.GetQuotaScheduleRequest,
    ) -> max_compute_20220104_models.GetQuotaScheduleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_quota_schedule_with_options_async(nickname, request, headers, runtime)

    def get_role_acl_with_options(
        self,
        project_name: str,
        role_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetRoleAclResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetRoleAcl',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_name)}/roles/{OpenApiUtilClient.get_encode_param(role_name)}/roleAcl',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetRoleAclResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_role_acl_with_options_async(
        self,
        project_name: str,
        role_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetRoleAclResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetRoleAcl',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_name)}/roles/{OpenApiUtilClient.get_encode_param(role_name)}/roleAcl',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetRoleAclResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_role_acl(
        self,
        project_name: str,
        role_name: str,
    ) -> max_compute_20220104_models.GetRoleAclResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_role_acl_with_options(project_name, role_name, headers, runtime)

    async def get_role_acl_async(
        self,
        project_name: str,
        role_name: str,
    ) -> max_compute_20220104_models.GetRoleAclResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_role_acl_with_options_async(project_name, role_name, headers, runtime)

    def get_role_acl_on_object_with_options(
        self,
        project_name: str,
        role_name: str,
        request: max_compute_20220104_models.GetRoleAclOnObjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetRoleAclOnObjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.object_name):
            query['objectName'] = request.object_name
        if not UtilClient.is_unset(request.object_type):
            query['objectType'] = request.object_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRoleAclOnObject',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_name)}/roles/{OpenApiUtilClient.get_encode_param(role_name)}/acl',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetRoleAclOnObjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_role_acl_on_object_with_options_async(
        self,
        project_name: str,
        role_name: str,
        request: max_compute_20220104_models.GetRoleAclOnObjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetRoleAclOnObjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.object_name):
            query['objectName'] = request.object_name
        if not UtilClient.is_unset(request.object_type):
            query['objectType'] = request.object_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRoleAclOnObject',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_name)}/roles/{OpenApiUtilClient.get_encode_param(role_name)}/acl',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetRoleAclOnObjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_role_acl_on_object(
        self,
        project_name: str,
        role_name: str,
        request: max_compute_20220104_models.GetRoleAclOnObjectRequest,
    ) -> max_compute_20220104_models.GetRoleAclOnObjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_role_acl_on_object_with_options(project_name, role_name, request, headers, runtime)

    async def get_role_acl_on_object_async(
        self,
        project_name: str,
        role_name: str,
        request: max_compute_20220104_models.GetRoleAclOnObjectRequest,
    ) -> max_compute_20220104_models.GetRoleAclOnObjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_role_acl_on_object_with_options_async(project_name, role_name, request, headers, runtime)

    def get_role_policy_with_options(
        self,
        project_name: str,
        role_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetRolePolicyResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetRolePolicy',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_name)}/roles/{OpenApiUtilClient.get_encode_param(role_name)}/policy',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetRolePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_role_policy_with_options_async(
        self,
        project_name: str,
        role_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetRolePolicyResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetRolePolicy',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_name)}/roles/{OpenApiUtilClient.get_encode_param(role_name)}/policy',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetRolePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_role_policy(
        self,
        project_name: str,
        role_name: str,
    ) -> max_compute_20220104_models.GetRolePolicyResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_role_policy_with_options(project_name, role_name, headers, runtime)

    async def get_role_policy_async(
        self,
        project_name: str,
        role_name: str,
    ) -> max_compute_20220104_models.GetRolePolicyResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_role_policy_with_options_async(project_name, role_name, headers, runtime)

    def get_running_jobs_with_options(
        self,
        tmp_req: max_compute_20220104_models.GetRunningJobsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetRunningJobsResponse:
        UtilClient.validate_model(tmp_req)
        request = max_compute_20220104_models.GetRunningJobsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.job_owner_list):
            request.job_owner_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.job_owner_list, 'jobOwnerList', 'simple')
        if not UtilClient.is_unset(tmp_req.quota_nickname_list):
            request.quota_nickname_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.quota_nickname_list, 'quotaNicknameList', 'simple')
        query = {}
        if not UtilClient.is_unset(request.from_):
            query['from'] = request.from_
        if not UtilClient.is_unset(request.job_owner_list_shrink):
            query['jobOwnerList'] = request.job_owner_list_shrink
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.quota_nickname_list_shrink):
            query['quotaNicknameList'] = request.quota_nickname_list_shrink
        if not UtilClient.is_unset(request.to):
            query['to'] = request.to
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRunningJobs',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/jobs/runningJobs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetRunningJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_running_jobs_with_options_async(
        self,
        tmp_req: max_compute_20220104_models.GetRunningJobsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetRunningJobsResponse:
        UtilClient.validate_model(tmp_req)
        request = max_compute_20220104_models.GetRunningJobsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.job_owner_list):
            request.job_owner_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.job_owner_list, 'jobOwnerList', 'simple')
        if not UtilClient.is_unset(tmp_req.quota_nickname_list):
            request.quota_nickname_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.quota_nickname_list, 'quotaNicknameList', 'simple')
        query = {}
        if not UtilClient.is_unset(request.from_):
            query['from'] = request.from_
        if not UtilClient.is_unset(request.job_owner_list_shrink):
            query['jobOwnerList'] = request.job_owner_list_shrink
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.quota_nickname_list_shrink):
            query['quotaNicknameList'] = request.quota_nickname_list_shrink
        if not UtilClient.is_unset(request.to):
            query['to'] = request.to
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRunningJobs',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/jobs/runningJobs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetRunningJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_running_jobs(
        self,
        request: max_compute_20220104_models.GetRunningJobsRequest,
    ) -> max_compute_20220104_models.GetRunningJobsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_running_jobs_with_options(request, headers, runtime)

    async def get_running_jobs_async(
        self,
        request: max_compute_20220104_models.GetRunningJobsRequest,
    ) -> max_compute_20220104_models.GetRunningJobsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_running_jobs_with_options_async(request, headers, runtime)

    def get_trusted_projects_with_options(
        self,
        project_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetTrustedProjectsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTrustedProjects',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_name)}/trustedProjects',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetTrustedProjectsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_trusted_projects_with_options_async(
        self,
        project_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetTrustedProjectsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTrustedProjects',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_name)}/trustedProjects',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetTrustedProjectsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_trusted_projects(
        self,
        project_name: str,
    ) -> max_compute_20220104_models.GetTrustedProjectsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_trusted_projects_with_options(project_name, headers, runtime)

    async def get_trusted_projects_async(
        self,
        project_name: str,
    ) -> max_compute_20220104_models.GetTrustedProjectsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_trusted_projects_with_options_async(project_name, headers, runtime)

    def kill_jobs_with_options(
        self,
        request: max_compute_20220104_models.KillJobsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.KillJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='KillJobs',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/jobs/kill',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.KillJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def kill_jobs_with_options_async(
        self,
        request: max_compute_20220104_models.KillJobsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.KillJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='KillJobs',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/jobs/kill',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.KillJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def kill_jobs(
        self,
        request: max_compute_20220104_models.KillJobsRequest,
    ) -> max_compute_20220104_models.KillJobsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.kill_jobs_with_options(request, headers, runtime)

    async def kill_jobs_async(
        self,
        request: max_compute_20220104_models.KillJobsRequest,
    ) -> max_compute_20220104_models.KillJobsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.kill_jobs_with_options_async(request, headers, runtime)

    def list_functions_with_options(
        self,
        project_name: str,
        request: max_compute_20220104_models.ListFunctionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ListFunctionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.marker):
            query['marker'] = request.marker
        if not UtilClient.is_unset(request.max_item):
            query['maxItem'] = request.max_item
        if not UtilClient.is_unset(request.prefix):
            query['prefix'] = request.prefix
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFunctions',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_name)}/functions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListFunctionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_functions_with_options_async(
        self,
        project_name: str,
        request: max_compute_20220104_models.ListFunctionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ListFunctionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.marker):
            query['marker'] = request.marker
        if not UtilClient.is_unset(request.max_item):
            query['maxItem'] = request.max_item
        if not UtilClient.is_unset(request.prefix):
            query['prefix'] = request.prefix
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFunctions',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_name)}/functions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListFunctionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_functions(
        self,
        project_name: str,
        request: max_compute_20220104_models.ListFunctionsRequest,
    ) -> max_compute_20220104_models.ListFunctionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_functions_with_options(project_name, request, headers, runtime)

    async def list_functions_async(
        self,
        project_name: str,
        request: max_compute_20220104_models.ListFunctionsRequest,
    ) -> max_compute_20220104_models.ListFunctionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_functions_with_options_async(project_name, request, headers, runtime)

    def list_packages_with_options(
        self,
        project_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ListPackagesResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListPackages',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_name)}/packages',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListPackagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_packages_with_options_async(
        self,
        project_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ListPackagesResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListPackages',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_name)}/packages',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListPackagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_packages(
        self,
        project_name: str,
    ) -> max_compute_20220104_models.ListPackagesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_packages_with_options(project_name, headers, runtime)

    async def list_packages_async(
        self,
        project_name: str,
    ) -> max_compute_20220104_models.ListPackagesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_packages_with_options_async(project_name, headers, runtime)

    def list_project_users_with_options(
        self,
        project_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ListProjectUsersResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListProjectUsers',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_name)}/users',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListProjectUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_project_users_with_options_async(
        self,
        project_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ListProjectUsersResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListProjectUsers',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_name)}/users',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListProjectUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_project_users(
        self,
        project_name: str,
    ) -> max_compute_20220104_models.ListProjectUsersResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_project_users_with_options(project_name, headers, runtime)

    async def list_project_users_async(
        self,
        project_name: str,
    ) -> max_compute_20220104_models.ListProjectUsersResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_project_users_with_options_async(project_name, headers, runtime)

    def list_projects_with_options(
        self,
        request: max_compute_20220104_models.ListProjectsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ListProjectsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.marker):
            query['marker'] = request.marker
        if not UtilClient.is_unset(request.max_item):
            query['maxItem'] = request.max_item
        if not UtilClient.is_unset(request.prefix):
            query['prefix'] = request.prefix
        if not UtilClient.is_unset(request.quota_name):
            query['quotaName'] = request.quota_name
        if not UtilClient.is_unset(request.quota_nick_name):
            query['quotaNickName'] = request.quota_nick_name
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.sale_tags):
            query['saleTags'] = request.sale_tags
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProjects',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListProjectsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_projects_with_options_async(
        self,
        request: max_compute_20220104_models.ListProjectsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ListProjectsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.marker):
            query['marker'] = request.marker
        if not UtilClient.is_unset(request.max_item):
            query['maxItem'] = request.max_item
        if not UtilClient.is_unset(request.prefix):
            query['prefix'] = request.prefix
        if not UtilClient.is_unset(request.quota_name):
            query['quotaName'] = request.quota_name
        if not UtilClient.is_unset(request.quota_nick_name):
            query['quotaNickName'] = request.quota_nick_name
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.sale_tags):
            query['saleTags'] = request.sale_tags
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProjects',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListProjectsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_projects(
        self,
        request: max_compute_20220104_models.ListProjectsRequest,
    ) -> max_compute_20220104_models.ListProjectsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_projects_with_options(request, headers, runtime)

    async def list_projects_async(
        self,
        request: max_compute_20220104_models.ListProjectsRequest,
    ) -> max_compute_20220104_models.ListProjectsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_projects_with_options_async(request, headers, runtime)

    def list_quotas_with_options(
        self,
        request: max_compute_20220104_models.ListQuotasRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ListQuotasResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.billing_type):
            query['billingType'] = request.billing_type
        if not UtilClient.is_unset(request.marker):
            query['marker'] = request.marker
        if not UtilClient.is_unset(request.max_item):
            query['maxItem'] = request.max_item
        if not UtilClient.is_unset(request.product_id):
            query['productId'] = request.product_id
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.sale_tags):
            query['saleTags'] = request.sale_tags
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListQuotas',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListQuotasResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_quotas_with_options_async(
        self,
        request: max_compute_20220104_models.ListQuotasRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ListQuotasResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.billing_type):
            query['billingType'] = request.billing_type
        if not UtilClient.is_unset(request.marker):
            query['marker'] = request.marker
        if not UtilClient.is_unset(request.max_item):
            query['maxItem'] = request.max_item
        if not UtilClient.is_unset(request.product_id):
            query['productId'] = request.product_id
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.sale_tags):
            query['saleTags'] = request.sale_tags
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListQuotas',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListQuotasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_quotas(
        self,
        request: max_compute_20220104_models.ListQuotasRequest,
    ) -> max_compute_20220104_models.ListQuotasResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_quotas_with_options(request, headers, runtime)

    async def list_quotas_async(
        self,
        request: max_compute_20220104_models.ListQuotasRequest,
    ) -> max_compute_20220104_models.ListQuotasResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_quotas_with_options_async(request, headers, runtime)

    def list_quotas_plans_with_options(
        self,
        nickname: str,
        request: max_compute_20220104_models.ListQuotasPlansRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ListQuotasPlansResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListQuotasPlans',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas/{OpenApiUtilClient.get_encode_param(nickname)}/plans',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListQuotasPlansResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_quotas_plans_with_options_async(
        self,
        nickname: str,
        request: max_compute_20220104_models.ListQuotasPlansRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ListQuotasPlansResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListQuotasPlans',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas/{OpenApiUtilClient.get_encode_param(nickname)}/plans',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListQuotasPlansResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_quotas_plans(
        self,
        nickname: str,
        request: max_compute_20220104_models.ListQuotasPlansRequest,
    ) -> max_compute_20220104_models.ListQuotasPlansResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_quotas_plans_with_options(nickname, request, headers, runtime)

    async def list_quotas_plans_async(
        self,
        nickname: str,
        request: max_compute_20220104_models.ListQuotasPlansRequest,
    ) -> max_compute_20220104_models.ListQuotasPlansResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_quotas_plans_with_options_async(nickname, request, headers, runtime)

    def list_resources_with_options(
        self,
        project_name: str,
        request: max_compute_20220104_models.ListResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ListResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.marker):
            query['marker'] = request.marker
        if not UtilClient.is_unset(request.max_item):
            query['maxItem'] = request.max_item
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResources',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_name)}/resources',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resources_with_options_async(
        self,
        project_name: str,
        request: max_compute_20220104_models.ListResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ListResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.marker):
            query['marker'] = request.marker
        if not UtilClient.is_unset(request.max_item):
            query['maxItem'] = request.max_item
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResources',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_name)}/resources',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resources(
        self,
        project_name: str,
        request: max_compute_20220104_models.ListResourcesRequest,
    ) -> max_compute_20220104_models.ListResourcesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_resources_with_options(project_name, request, headers, runtime)

    async def list_resources_async(
        self,
        project_name: str,
        request: max_compute_20220104_models.ListResourcesRequest,
    ) -> max_compute_20220104_models.ListResourcesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_resources_with_options_async(project_name, request, headers, runtime)

    def list_roles_with_options(
        self,
        project_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ListRolesResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListRoles',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_name)}/roles',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListRolesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_roles_with_options_async(
        self,
        project_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ListRolesResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListRoles',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_name)}/roles',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListRolesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_roles(
        self,
        project_name: str,
    ) -> max_compute_20220104_models.ListRolesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_roles_with_options(project_name, headers, runtime)

    async def list_roles_async(
        self,
        project_name: str,
    ) -> max_compute_20220104_models.ListRolesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_roles_with_options_async(project_name, headers, runtime)

    def list_tables_with_options(
        self,
        project_name: str,
        request: max_compute_20220104_models.ListTablesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ListTablesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.marker):
            query['marker'] = request.marker
        if not UtilClient.is_unset(request.max_item):
            query['maxItem'] = request.max_item
        if not UtilClient.is_unset(request.prefix):
            query['prefix'] = request.prefix
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTables',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_name)}/tables',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListTablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tables_with_options_async(
        self,
        project_name: str,
        request: max_compute_20220104_models.ListTablesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ListTablesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.marker):
            query['marker'] = request.marker
        if not UtilClient.is_unset(request.max_item):
            query['maxItem'] = request.max_item
        if not UtilClient.is_unset(request.prefix):
            query['prefix'] = request.prefix
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTables',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_name)}/tables',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListTablesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tables(
        self,
        project_name: str,
        request: max_compute_20220104_models.ListTablesRequest,
    ) -> max_compute_20220104_models.ListTablesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_tables_with_options(project_name, request, headers, runtime)

    async def list_tables_async(
        self,
        project_name: str,
        request: max_compute_20220104_models.ListTablesRequest,
    ) -> max_compute_20220104_models.ListTablesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_tables_with_options_async(project_name, request, headers, runtime)

    def list_users_with_options(
        self,
        request: max_compute_20220104_models.ListUsersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ListUsersResponse:
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
            action='ListUsers',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/users',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_users_with_options_async(
        self,
        request: max_compute_20220104_models.ListUsersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ListUsersResponse:
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
            action='ListUsers',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/users',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_users(
        self,
        request: max_compute_20220104_models.ListUsersRequest,
    ) -> max_compute_20220104_models.ListUsersResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_users_with_options(request, headers, runtime)

    async def list_users_async(
        self,
        request: max_compute_20220104_models.ListUsersRequest,
    ) -> max_compute_20220104_models.ListUsersResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_users_with_options_async(request, headers, runtime)

    def list_users_by_role_with_options(
        self,
        project_name: str,
        role_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ListUsersByRoleResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListUsersByRole',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_name)}/roles/{OpenApiUtilClient.get_encode_param(role_name)}/users',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListUsersByRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_users_by_role_with_options_async(
        self,
        project_name: str,
        role_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ListUsersByRoleResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListUsersByRole',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_name)}/roles/{OpenApiUtilClient.get_encode_param(role_name)}/users',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListUsersByRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_users_by_role(
        self,
        project_name: str,
        role_name: str,
    ) -> max_compute_20220104_models.ListUsersByRoleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_users_by_role_with_options(project_name, role_name, headers, runtime)

    async def list_users_by_role_async(
        self,
        project_name: str,
        role_name: str,
    ) -> max_compute_20220104_models.ListUsersByRoleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_users_by_role_with_options_async(project_name, role_name, headers, runtime)

    def update_package_with_options(
        self,
        project_name: str,
        package_name: str,
        request: max_compute_20220104_models.UpdatePackageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.UpdatePackageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='UpdatePackage',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_name)}/packages/{OpenApiUtilClient.get_encode_param(package_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.UpdatePackageResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_package_with_options_async(
        self,
        project_name: str,
        package_name: str,
        request: max_compute_20220104_models.UpdatePackageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.UpdatePackageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='UpdatePackage',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_name)}/packages/{OpenApiUtilClient.get_encode_param(package_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.UpdatePackageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_package(
        self,
        project_name: str,
        package_name: str,
        request: max_compute_20220104_models.UpdatePackageRequest,
    ) -> max_compute_20220104_models.UpdatePackageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_package_with_options(project_name, package_name, request, headers, runtime)

    async def update_package_async(
        self,
        project_name: str,
        package_name: str,
        request: max_compute_20220104_models.UpdatePackageRequest,
    ) -> max_compute_20220104_models.UpdatePackageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_package_with_options_async(project_name, package_name, request, headers, runtime)

    def update_project_ip_white_list_with_options(
        self,
        project_name: str,
        request: max_compute_20220104_models.UpdateProjectIpWhiteListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.UpdateProjectIpWhiteListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='UpdateProjectIpWhiteList',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_name)}/ipWhiteList',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.UpdateProjectIpWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_project_ip_white_list_with_options_async(
        self,
        project_name: str,
        request: max_compute_20220104_models.UpdateProjectIpWhiteListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.UpdateProjectIpWhiteListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='UpdateProjectIpWhiteList',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_name)}/ipWhiteList',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.UpdateProjectIpWhiteListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_project_ip_white_list(
        self,
        project_name: str,
        request: max_compute_20220104_models.UpdateProjectIpWhiteListRequest,
    ) -> max_compute_20220104_models.UpdateProjectIpWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_project_ip_white_list_with_options(project_name, request, headers, runtime)

    async def update_project_ip_white_list_async(
        self,
        project_name: str,
        request: max_compute_20220104_models.UpdateProjectIpWhiteListRequest,
    ) -> max_compute_20220104_models.UpdateProjectIpWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_project_ip_white_list_with_options_async(project_name, request, headers, runtime)

    def update_quota_with_options(
        self,
        nickname: str,
        request: max_compute_20220104_models.UpdateQuotaRequest,
        headers: max_compute_20220104_models.UpdateQuotaHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.UpdateQuotaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.ak_proven):
            real_headers['AkProven'] = UtilClient.to_jsonstring(headers.ak_proven)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='UpdateQuota',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas/{OpenApiUtilClient.get_encode_param(nickname)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.UpdateQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_quota_with_options_async(
        self,
        nickname: str,
        request: max_compute_20220104_models.UpdateQuotaRequest,
        headers: max_compute_20220104_models.UpdateQuotaHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.UpdateQuotaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.ak_proven):
            real_headers['AkProven'] = UtilClient.to_jsonstring(headers.ak_proven)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='UpdateQuota',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas/{OpenApiUtilClient.get_encode_param(nickname)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.UpdateQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_quota(
        self,
        nickname: str,
        request: max_compute_20220104_models.UpdateQuotaRequest,
    ) -> max_compute_20220104_models.UpdateQuotaResponse:
        runtime = util_models.RuntimeOptions()
        headers = max_compute_20220104_models.UpdateQuotaHeaders()
        return self.update_quota_with_options(nickname, request, headers, runtime)

    async def update_quota_async(
        self,
        nickname: str,
        request: max_compute_20220104_models.UpdateQuotaRequest,
    ) -> max_compute_20220104_models.UpdateQuotaResponse:
        runtime = util_models.RuntimeOptions()
        headers = max_compute_20220104_models.UpdateQuotaHeaders()
        return await self.update_quota_with_options_async(nickname, request, headers, runtime)

    def update_quota_plan_with_options(
        self,
        nickname: str,
        plan_name: str,
        request: max_compute_20220104_models.UpdateQuotaPlanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.UpdateQuotaPlanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='UpdateQuotaPlan',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas/{OpenApiUtilClient.get_encode_param(nickname)}/plans/{OpenApiUtilClient.get_encode_param(plan_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.UpdateQuotaPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_quota_plan_with_options_async(
        self,
        nickname: str,
        plan_name: str,
        request: max_compute_20220104_models.UpdateQuotaPlanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.UpdateQuotaPlanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='UpdateQuotaPlan',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas/{OpenApiUtilClient.get_encode_param(nickname)}/plans/{OpenApiUtilClient.get_encode_param(plan_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.UpdateQuotaPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_quota_plan(
        self,
        nickname: str,
        plan_name: str,
        request: max_compute_20220104_models.UpdateQuotaPlanRequest,
    ) -> max_compute_20220104_models.UpdateQuotaPlanResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_quota_plan_with_options(nickname, plan_name, request, headers, runtime)

    async def update_quota_plan_async(
        self,
        nickname: str,
        plan_name: str,
        request: max_compute_20220104_models.UpdateQuotaPlanRequest,
    ) -> max_compute_20220104_models.UpdateQuotaPlanResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_quota_plan_with_options_async(nickname, plan_name, request, headers, runtime)

    def update_quota_schedule_with_options(
        self,
        nickname: str,
        request: max_compute_20220104_models.UpdateQuotaScheduleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.UpdateQuotaScheduleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='UpdateQuotaSchedule',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas/{OpenApiUtilClient.get_encode_param(nickname)}/schedule',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.UpdateQuotaScheduleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_quota_schedule_with_options_async(
        self,
        nickname: str,
        request: max_compute_20220104_models.UpdateQuotaScheduleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.UpdateQuotaScheduleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='UpdateQuotaSchedule',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas/{OpenApiUtilClient.get_encode_param(nickname)}/schedule',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.UpdateQuotaScheduleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_quota_schedule(
        self,
        nickname: str,
        request: max_compute_20220104_models.UpdateQuotaScheduleRequest,
    ) -> max_compute_20220104_models.UpdateQuotaScheduleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_quota_schedule_with_options(nickname, request, headers, runtime)

    async def update_quota_schedule_async(
        self,
        nickname: str,
        request: max_compute_20220104_models.UpdateQuotaScheduleRequest,
    ) -> max_compute_20220104_models.UpdateQuotaScheduleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_quota_schedule_with_options_async(nickname, request, headers, runtime)
