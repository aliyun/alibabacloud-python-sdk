# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_mpaas20201028 import models as m_paa_s20201028_models
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
            'cn-hangzhou': 'mpaas.aliyuncs.com',
            'ap-northeast-1': 'mpaas.aliyuncs.com',
            'ap-northeast-2-pop': 'mpaas.aliyuncs.com',
            'ap-south-1': 'mpaas.aliyuncs.com',
            'ap-southeast-1': 'mpaas.aliyuncs.com',
            'ap-southeast-2': 'mpaas.aliyuncs.com',
            'ap-southeast-3': 'mpaas.aliyuncs.com',
            'ap-southeast-5': 'mpaas.aliyuncs.com',
            'cn-beijing': 'mpaas.aliyuncs.com',
            'cn-beijing-finance-1': 'mpaas.aliyuncs.com',
            'cn-beijing-finance-pop': 'mpaas.aliyuncs.com',
            'cn-beijing-gov-1': 'mpaas.aliyuncs.com',
            'cn-beijing-nu16-b01': 'mpaas.aliyuncs.com',
            'cn-chengdu': 'mpaas.aliyuncs.com',
            'cn-edge-1': 'mpaas.aliyuncs.com',
            'cn-fujian': 'mpaas.aliyuncs.com',
            'cn-haidian-cm12-c01': 'mpaas.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'mpaas.aliyuncs.com',
            'cn-hangzhou-finance': 'mpaas.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'mpaas.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'mpaas.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'mpaas.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'mpaas.aliyuncs.com',
            'cn-hangzhou-test-306': 'mpaas.aliyuncs.com',
            'cn-hongkong': 'mpaas.aliyuncs.com',
            'cn-hongkong-finance-pop': 'mpaas.aliyuncs.com',
            'cn-huhehaote': 'mpaas.aliyuncs.com',
            'cn-north-2-gov-1': 'mpaas.aliyuncs.com',
            'cn-qingdao': 'mpaas.aliyuncs.com',
            'cn-qingdao-nebula': 'mpaas.aliyuncs.com',
            'cn-shanghai': 'mpaas.aliyuncs.com',
            'cn-shanghai-et15-b01': 'mpaas.aliyuncs.com',
            'cn-shanghai-et2-b01': 'mpaas.aliyuncs.com',
            'cn-shanghai-finance-1': 'mpaas.aliyuncs.com',
            'cn-shanghai-inner': 'mpaas.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'mpaas.aliyuncs.com',
            'cn-shenzhen': 'mpaas.aliyuncs.com',
            'cn-shenzhen-finance-1': 'mpaas.aliyuncs.com',
            'cn-shenzhen-inner': 'mpaas.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'mpaas.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'mpaas.aliyuncs.com',
            'cn-wuhan': 'mpaas.aliyuncs.com',
            'cn-yushanfang': 'mpaas.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'mpaas.aliyuncs.com',
            'cn-zhangjiakou': 'mpaas.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'mpaas.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'mpaas.aliyuncs.com',
            'eu-central-1': 'mpaas.aliyuncs.com',
            'eu-west-1': 'mpaas.aliyuncs.com',
            'eu-west-1-oxs': 'mpaas.aliyuncs.com',
            'me-east-1': 'mpaas.aliyuncs.com',
            'rus-west-1-pop': 'mpaas.aliyuncs.com',
            'us-east-1': 'mpaas.aliyuncs.com',
            'us-west-1': 'mpaas.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('mpaas', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_mds_mini_config_with_options(
        self,
        request: m_paa_s20201028_models.AddMdsMiniConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.AddMdsMiniConfigResponse:
        """
        @param request: AddMdsMiniConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddMdsMiniConfigResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.mpaas_mappcenter_mini_config_add_json_str):
            body['MpaasMappcenterMiniConfigAddJsonStr'] = request.mpaas_mappcenter_mini_config_add_json_str
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddMdsMiniConfig',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.AddMdsMiniConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_mds_mini_config_with_options_async(
        self,
        request: m_paa_s20201028_models.AddMdsMiniConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.AddMdsMiniConfigResponse:
        """
        @param request: AddMdsMiniConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddMdsMiniConfigResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.mpaas_mappcenter_mini_config_add_json_str):
            body['MpaasMappcenterMiniConfigAddJsonStr'] = request.mpaas_mappcenter_mini_config_add_json_str
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddMdsMiniConfig',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.AddMdsMiniConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_mds_mini_config(
        self,
        request: m_paa_s20201028_models.AddMdsMiniConfigRequest,
    ) -> m_paa_s20201028_models.AddMdsMiniConfigResponse:
        """
        @param request: AddMdsMiniConfigRequest
        @return: AddMdsMiniConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_mds_mini_config_with_options(request, runtime)

    async def add_mds_mini_config_async(
        self,
        request: m_paa_s20201028_models.AddMdsMiniConfigRequest,
    ) -> m_paa_s20201028_models.AddMdsMiniConfigResponse:
        """
        @param request: AddMdsMiniConfigRequest
        @return: AddMdsMiniConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_mds_mini_config_with_options_async(request, runtime)

    def cancel_push_scheduler_with_options(
        self,
        request: m_paa_s20201028_models.CancelPushSchedulerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.CancelPushSchedulerResponse:
        """
        @param request: CancelPushSchedulerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelPushSchedulerResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.unique_ids):
            body['UniqueIds'] = request.unique_ids
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelPushScheduler',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.CancelPushSchedulerResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_push_scheduler_with_options_async(
        self,
        request: m_paa_s20201028_models.CancelPushSchedulerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.CancelPushSchedulerResponse:
        """
        @param request: CancelPushSchedulerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelPushSchedulerResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.unique_ids):
            body['UniqueIds'] = request.unique_ids
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelPushScheduler',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.CancelPushSchedulerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_push_scheduler(
        self,
        request: m_paa_s20201028_models.CancelPushSchedulerRequest,
    ) -> m_paa_s20201028_models.CancelPushSchedulerResponse:
        """
        @param request: CancelPushSchedulerRequest
        @return: CancelPushSchedulerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cancel_push_scheduler_with_options(request, runtime)

    async def cancel_push_scheduler_async(
        self,
        request: m_paa_s20201028_models.CancelPushSchedulerRequest,
    ) -> m_paa_s20201028_models.CancelPushSchedulerResponse:
        """
        @param request: CancelPushSchedulerRequest
        @return: CancelPushSchedulerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.cancel_push_scheduler_with_options_async(request, runtime)

    def change_mcube_mini_task_status_with_options(
        self,
        request: m_paa_s20201028_models.ChangeMcubeMiniTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.ChangeMcubeMiniTaskStatusResponse:
        """
        @param request: ChangeMcubeMiniTaskStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeMcubeMiniTaskStatusResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.biz_type):
            body['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.package_id):
            body['PackageId'] = request.package_id
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_status):
            body['TaskStatus'] = request.task_status
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ChangeMcubeMiniTaskStatus',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.ChangeMcubeMiniTaskStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_mcube_mini_task_status_with_options_async(
        self,
        request: m_paa_s20201028_models.ChangeMcubeMiniTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.ChangeMcubeMiniTaskStatusResponse:
        """
        @param request: ChangeMcubeMiniTaskStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeMcubeMiniTaskStatusResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.biz_type):
            body['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.package_id):
            body['PackageId'] = request.package_id
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_status):
            body['TaskStatus'] = request.task_status
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ChangeMcubeMiniTaskStatus',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.ChangeMcubeMiniTaskStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_mcube_mini_task_status(
        self,
        request: m_paa_s20201028_models.ChangeMcubeMiniTaskStatusRequest,
    ) -> m_paa_s20201028_models.ChangeMcubeMiniTaskStatusResponse:
        """
        @param request: ChangeMcubeMiniTaskStatusRequest
        @return: ChangeMcubeMiniTaskStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.change_mcube_mini_task_status_with_options(request, runtime)

    async def change_mcube_mini_task_status_async(
        self,
        request: m_paa_s20201028_models.ChangeMcubeMiniTaskStatusRequest,
    ) -> m_paa_s20201028_models.ChangeMcubeMiniTaskStatusResponse:
        """
        @param request: ChangeMcubeMiniTaskStatusRequest
        @return: ChangeMcubeMiniTaskStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.change_mcube_mini_task_status_with_options_async(request, runtime)

    def change_mcube_nebula_task_status_with_options(
        self,
        request: m_paa_s20201028_models.ChangeMcubeNebulaTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.ChangeMcubeNebulaTaskStatusResponse:
        """
        @param request: ChangeMcubeNebulaTaskStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeMcubeNebulaTaskStatusResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.biz_type):
            body['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.package_id):
            body['PackageId'] = request.package_id
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_status):
            body['TaskStatus'] = request.task_status
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ChangeMcubeNebulaTaskStatus',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.ChangeMcubeNebulaTaskStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_mcube_nebula_task_status_with_options_async(
        self,
        request: m_paa_s20201028_models.ChangeMcubeNebulaTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.ChangeMcubeNebulaTaskStatusResponse:
        """
        @param request: ChangeMcubeNebulaTaskStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeMcubeNebulaTaskStatusResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.biz_type):
            body['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.package_id):
            body['PackageId'] = request.package_id
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_status):
            body['TaskStatus'] = request.task_status
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ChangeMcubeNebulaTaskStatus',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.ChangeMcubeNebulaTaskStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_mcube_nebula_task_status(
        self,
        request: m_paa_s20201028_models.ChangeMcubeNebulaTaskStatusRequest,
    ) -> m_paa_s20201028_models.ChangeMcubeNebulaTaskStatusResponse:
        """
        @param request: ChangeMcubeNebulaTaskStatusRequest
        @return: ChangeMcubeNebulaTaskStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.change_mcube_nebula_task_status_with_options(request, runtime)

    async def change_mcube_nebula_task_status_async(
        self,
        request: m_paa_s20201028_models.ChangeMcubeNebulaTaskStatusRequest,
    ) -> m_paa_s20201028_models.ChangeMcubeNebulaTaskStatusResponse:
        """
        @param request: ChangeMcubeNebulaTaskStatusRequest
        @return: ChangeMcubeNebulaTaskStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.change_mcube_nebula_task_status_with_options_async(request, runtime)

    def change_mcube_public_task_status_with_options(
        self,
        request: m_paa_s20201028_models.ChangeMcubePublicTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.ChangeMcubePublicTaskStatusResponse:
        """
        @param request: ChangeMcubePublicTaskStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeMcubePublicTaskStatusResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_status):
            body['TaskStatus'] = request.task_status
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ChangeMcubePublicTaskStatus',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.ChangeMcubePublicTaskStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_mcube_public_task_status_with_options_async(
        self,
        request: m_paa_s20201028_models.ChangeMcubePublicTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.ChangeMcubePublicTaskStatusResponse:
        """
        @param request: ChangeMcubePublicTaskStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeMcubePublicTaskStatusResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_status):
            body['TaskStatus'] = request.task_status
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ChangeMcubePublicTaskStatus',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.ChangeMcubePublicTaskStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_mcube_public_task_status(
        self,
        request: m_paa_s20201028_models.ChangeMcubePublicTaskStatusRequest,
    ) -> m_paa_s20201028_models.ChangeMcubePublicTaskStatusResponse:
        """
        @param request: ChangeMcubePublicTaskStatusRequest
        @return: ChangeMcubePublicTaskStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.change_mcube_public_task_status_with_options(request, runtime)

    async def change_mcube_public_task_status_async(
        self,
        request: m_paa_s20201028_models.ChangeMcubePublicTaskStatusRequest,
    ) -> m_paa_s20201028_models.ChangeMcubePublicTaskStatusResponse:
        """
        @param request: ChangeMcubePublicTaskStatusRequest
        @return: ChangeMcubePublicTaskStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.change_mcube_public_task_status_with_options_async(request, runtime)

    def change_mds_cube_task_status_with_options(
        self,
        request: m_paa_s20201028_models.ChangeMdsCubeTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.ChangeMdsCubeTaskStatusResponse:
        """
        @param request: ChangeMdsCubeTaskStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeMdsCubeTaskStatusResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.task_status):
            body['TaskStatus'] = request.task_status
        if not UtilClient.is_unset(request.template_resource_id):
            body['TemplateResourceId'] = request.template_resource_id
        if not UtilClient.is_unset(request.template_task_id):
            body['TemplateTaskId'] = request.template_task_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ChangeMdsCubeTaskStatus',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.ChangeMdsCubeTaskStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_mds_cube_task_status_with_options_async(
        self,
        request: m_paa_s20201028_models.ChangeMdsCubeTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.ChangeMdsCubeTaskStatusResponse:
        """
        @param request: ChangeMdsCubeTaskStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeMdsCubeTaskStatusResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.task_status):
            body['TaskStatus'] = request.task_status
        if not UtilClient.is_unset(request.template_resource_id):
            body['TemplateResourceId'] = request.template_resource_id
        if not UtilClient.is_unset(request.template_task_id):
            body['TemplateTaskId'] = request.template_task_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ChangeMdsCubeTaskStatus',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.ChangeMdsCubeTaskStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_mds_cube_task_status(
        self,
        request: m_paa_s20201028_models.ChangeMdsCubeTaskStatusRequest,
    ) -> m_paa_s20201028_models.ChangeMdsCubeTaskStatusResponse:
        """
        @param request: ChangeMdsCubeTaskStatusRequest
        @return: ChangeMdsCubeTaskStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.change_mds_cube_task_status_with_options(request, runtime)

    async def change_mds_cube_task_status_async(
        self,
        request: m_paa_s20201028_models.ChangeMdsCubeTaskStatusRequest,
    ) -> m_paa_s20201028_models.ChangeMdsCubeTaskStatusResponse:
        """
        @param request: ChangeMdsCubeTaskStatusRequest
        @return: ChangeMdsCubeTaskStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.change_mds_cube_task_status_with_options_async(request, runtime)

    def copy_mcdp_group_with_options(
        self,
        request: m_paa_s20201028_models.CopyMcdpGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.CopyMcdpGroupResponse:
        """
        @param request: CopyMcdpGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CopyMcdpGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.mpaas_mappcenter_mcdp_group_copy_json_str):
            body['MpaasMappcenterMcdpGroupCopyJsonStr'] = request.mpaas_mappcenter_mcdp_group_copy_json_str
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CopyMcdpGroup',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.CopyMcdpGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def copy_mcdp_group_with_options_async(
        self,
        request: m_paa_s20201028_models.CopyMcdpGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.CopyMcdpGroupResponse:
        """
        @param request: CopyMcdpGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CopyMcdpGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.mpaas_mappcenter_mcdp_group_copy_json_str):
            body['MpaasMappcenterMcdpGroupCopyJsonStr'] = request.mpaas_mappcenter_mcdp_group_copy_json_str
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CopyMcdpGroup',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.CopyMcdpGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def copy_mcdp_group(
        self,
        request: m_paa_s20201028_models.CopyMcdpGroupRequest,
    ) -> m_paa_s20201028_models.CopyMcdpGroupResponse:
        """
        @param request: CopyMcdpGroupRequest
        @return: CopyMcdpGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.copy_mcdp_group_with_options(request, runtime)

    async def copy_mcdp_group_async(
        self,
        request: m_paa_s20201028_models.CopyMcdpGroupRequest,
    ) -> m_paa_s20201028_models.CopyMcdpGroupResponse:
        """
        @param request: CopyMcdpGroupRequest
        @return: CopyMcdpGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.copy_mcdp_group_with_options_async(request, runtime)

    def create_link_with_options(
        self,
        request: m_paa_s20201028_models.CreateLinkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.CreateLinkResponse:
        """
        @summary 创建短链
        
        @param request: CreateLinkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLinkResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.cors):
            body['Cors'] = request.cors
        if not UtilClient.is_unset(request.domain):
            body['Domain'] = request.domain
        if not UtilClient.is_unset(request.dynamicfield):
            body['Dynamicfield'] = request.dynamicfield
        if not UtilClient.is_unset(request.target_url):
            body['TargetUrl'] = request.target_url
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLink',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.CreateLinkResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_link_with_options_async(
        self,
        request: m_paa_s20201028_models.CreateLinkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.CreateLinkResponse:
        """
        @summary 创建短链
        
        @param request: CreateLinkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLinkResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.cors):
            body['Cors'] = request.cors
        if not UtilClient.is_unset(request.domain):
            body['Domain'] = request.domain
        if not UtilClient.is_unset(request.dynamicfield):
            body['Dynamicfield'] = request.dynamicfield
        if not UtilClient.is_unset(request.target_url):
            body['TargetUrl'] = request.target_url
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLink',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.CreateLinkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_link(
        self,
        request: m_paa_s20201028_models.CreateLinkRequest,
    ) -> m_paa_s20201028_models.CreateLinkResponse:
        """
        @summary 创建短链
        
        @param request: CreateLinkRequest
        @return: CreateLinkResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_link_with_options(request, runtime)

    async def create_link_async(
        self,
        request: m_paa_s20201028_models.CreateLinkRequest,
    ) -> m_paa_s20201028_models.CreateLinkResponse:
        """
        @summary 创建短链
        
        @param request: CreateLinkRequest
        @return: CreateLinkResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_link_with_options_async(request, runtime)

    def create_mcdp_group_with_options(
        self,
        request: m_paa_s20201028_models.CreateMcdpGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.CreateMcdpGroupResponse:
        """
        @param request: CreateMcdpGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMcdpGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.mpaas_mappcenter_mcdp_group_create_json_str):
            body['MpaasMappcenterMcdpGroupCreateJsonStr'] = request.mpaas_mappcenter_mcdp_group_create_json_str
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMcdpGroup',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.CreateMcdpGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_mcdp_group_with_options_async(
        self,
        request: m_paa_s20201028_models.CreateMcdpGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.CreateMcdpGroupResponse:
        """
        @param request: CreateMcdpGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMcdpGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.mpaas_mappcenter_mcdp_group_create_json_str):
            body['MpaasMappcenterMcdpGroupCreateJsonStr'] = request.mpaas_mappcenter_mcdp_group_create_json_str
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMcdpGroup',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.CreateMcdpGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_mcdp_group(
        self,
        request: m_paa_s20201028_models.CreateMcdpGroupRequest,
    ) -> m_paa_s20201028_models.CreateMcdpGroupResponse:
        """
        @param request: CreateMcdpGroupRequest
        @return: CreateMcdpGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_mcdp_group_with_options(request, runtime)

    async def create_mcdp_group_async(
        self,
        request: m_paa_s20201028_models.CreateMcdpGroupRequest,
    ) -> m_paa_s20201028_models.CreateMcdpGroupResponse:
        """
        @param request: CreateMcdpGroupRequest
        @return: CreateMcdpGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_mcdp_group_with_options_async(request, runtime)

    def create_mcdp_material_with_options(
        self,
        request: m_paa_s20201028_models.CreateMcdpMaterialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.CreateMcdpMaterialResponse:
        """
        @param request: CreateMcdpMaterialRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMcdpMaterialResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.mpaas_mappcenter_mcdp_material_create_json_str):
            body['MpaasMappcenterMcdpMaterialCreateJsonStr'] = request.mpaas_mappcenter_mcdp_material_create_json_str
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMcdpMaterial',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.CreateMcdpMaterialResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_mcdp_material_with_options_async(
        self,
        request: m_paa_s20201028_models.CreateMcdpMaterialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.CreateMcdpMaterialResponse:
        """
        @param request: CreateMcdpMaterialRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMcdpMaterialResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.mpaas_mappcenter_mcdp_material_create_json_str):
            body['MpaasMappcenterMcdpMaterialCreateJsonStr'] = request.mpaas_mappcenter_mcdp_material_create_json_str
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMcdpMaterial',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.CreateMcdpMaterialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_mcdp_material(
        self,
        request: m_paa_s20201028_models.CreateMcdpMaterialRequest,
    ) -> m_paa_s20201028_models.CreateMcdpMaterialResponse:
        """
        @param request: CreateMcdpMaterialRequest
        @return: CreateMcdpMaterialResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_mcdp_material_with_options(request, runtime)

    async def create_mcdp_material_async(
        self,
        request: m_paa_s20201028_models.CreateMcdpMaterialRequest,
    ) -> m_paa_s20201028_models.CreateMcdpMaterialResponse:
        """
        @param request: CreateMcdpMaterialRequest
        @return: CreateMcdpMaterialResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_mcdp_material_with_options_async(request, runtime)

    def create_mcdp_zone_with_options(
        self,
        request: m_paa_s20201028_models.CreateMcdpZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.CreateMcdpZoneResponse:
        """
        @param request: CreateMcdpZoneRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMcdpZoneResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.mpaas_mappcenter_mcdp_zone_create_json_str):
            body['MpaasMappcenterMcdpZoneCreateJsonStr'] = request.mpaas_mappcenter_mcdp_zone_create_json_str
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMcdpZone',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.CreateMcdpZoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_mcdp_zone_with_options_async(
        self,
        request: m_paa_s20201028_models.CreateMcdpZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.CreateMcdpZoneResponse:
        """
        @param request: CreateMcdpZoneRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMcdpZoneResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.mpaas_mappcenter_mcdp_zone_create_json_str):
            body['MpaasMappcenterMcdpZoneCreateJsonStr'] = request.mpaas_mappcenter_mcdp_zone_create_json_str
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMcdpZone',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.CreateMcdpZoneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_mcdp_zone(
        self,
        request: m_paa_s20201028_models.CreateMcdpZoneRequest,
    ) -> m_paa_s20201028_models.CreateMcdpZoneResponse:
        """
        @param request: CreateMcdpZoneRequest
        @return: CreateMcdpZoneResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_mcdp_zone_with_options(request, runtime)

    async def create_mcdp_zone_async(
        self,
        request: m_paa_s20201028_models.CreateMcdpZoneRequest,
    ) -> m_paa_s20201028_models.CreateMcdpZoneResponse:
        """
        @param request: CreateMcdpZoneRequest
        @return: CreateMcdpZoneResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_mcdp_zone_with_options_async(request, runtime)

    def create_mcube_mini_app_with_options(
        self,
        request: m_paa_s20201028_models.CreateMcubeMiniAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.CreateMcubeMiniAppResponse:
        """
        @param request: CreateMcubeMiniAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMcubeMiniAppResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.h_5id):
            body['H5Id'] = request.h_5id
        if not UtilClient.is_unset(request.h_5name):
            body['H5Name'] = request.h_5name
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMcubeMiniApp',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.CreateMcubeMiniAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_mcube_mini_app_with_options_async(
        self,
        request: m_paa_s20201028_models.CreateMcubeMiniAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.CreateMcubeMiniAppResponse:
        """
        @param request: CreateMcubeMiniAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMcubeMiniAppResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.h_5id):
            body['H5Id'] = request.h_5id
        if not UtilClient.is_unset(request.h_5name):
            body['H5Name'] = request.h_5name
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMcubeMiniApp',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.CreateMcubeMiniAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_mcube_mini_app(
        self,
        request: m_paa_s20201028_models.CreateMcubeMiniAppRequest,
    ) -> m_paa_s20201028_models.CreateMcubeMiniAppResponse:
        """
        @param request: CreateMcubeMiniAppRequest
        @return: CreateMcubeMiniAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_mcube_mini_app_with_options(request, runtime)

    async def create_mcube_mini_app_async(
        self,
        request: m_paa_s20201028_models.CreateMcubeMiniAppRequest,
    ) -> m_paa_s20201028_models.CreateMcubeMiniAppResponse:
        """
        @param request: CreateMcubeMiniAppRequest
        @return: CreateMcubeMiniAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_mcube_mini_app_with_options_async(request, runtime)

    def create_mcube_mini_task_with_options(
        self,
        request: m_paa_s20201028_models.CreateMcubeMiniTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.CreateMcubeMiniTaskResponse:
        """
        @param request: CreateMcubeMiniTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMcubeMiniTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.grey_config_info):
            body['GreyConfigInfo'] = request.grey_config_info
        if not UtilClient.is_unset(request.grey_endtime_data):
            body['GreyEndtimeData'] = request.grey_endtime_data
        if not UtilClient.is_unset(request.grey_num):
            body['GreyNum'] = request.grey_num
        if not UtilClient.is_unset(request.memo):
            body['Memo'] = request.memo
        if not UtilClient.is_unset(request.package_id):
            body['PackageId'] = request.package_id
        if not UtilClient.is_unset(request.publish_mode):
            body['PublishMode'] = request.publish_mode
        if not UtilClient.is_unset(request.publish_type):
            body['PublishType'] = request.publish_type
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.whitelist_ids):
            body['WhitelistIds'] = request.whitelist_ids
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMcubeMiniTask',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.CreateMcubeMiniTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_mcube_mini_task_with_options_async(
        self,
        request: m_paa_s20201028_models.CreateMcubeMiniTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.CreateMcubeMiniTaskResponse:
        """
        @param request: CreateMcubeMiniTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMcubeMiniTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.grey_config_info):
            body['GreyConfigInfo'] = request.grey_config_info
        if not UtilClient.is_unset(request.grey_endtime_data):
            body['GreyEndtimeData'] = request.grey_endtime_data
        if not UtilClient.is_unset(request.grey_num):
            body['GreyNum'] = request.grey_num
        if not UtilClient.is_unset(request.memo):
            body['Memo'] = request.memo
        if not UtilClient.is_unset(request.package_id):
            body['PackageId'] = request.package_id
        if not UtilClient.is_unset(request.publish_mode):
            body['PublishMode'] = request.publish_mode
        if not UtilClient.is_unset(request.publish_type):
            body['PublishType'] = request.publish_type
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.whitelist_ids):
            body['WhitelistIds'] = request.whitelist_ids
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMcubeMiniTask',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.CreateMcubeMiniTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_mcube_mini_task(
        self,
        request: m_paa_s20201028_models.CreateMcubeMiniTaskRequest,
    ) -> m_paa_s20201028_models.CreateMcubeMiniTaskResponse:
        """
        @param request: CreateMcubeMiniTaskRequest
        @return: CreateMcubeMiniTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_mcube_mini_task_with_options(request, runtime)

    async def create_mcube_mini_task_async(
        self,
        request: m_paa_s20201028_models.CreateMcubeMiniTaskRequest,
    ) -> m_paa_s20201028_models.CreateMcubeMiniTaskResponse:
        """
        @param request: CreateMcubeMiniTaskRequest
        @return: CreateMcubeMiniTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_mcube_mini_task_with_options_async(request, runtime)

    def create_mcube_nebula_app_with_options(
        self,
        request: m_paa_s20201028_models.CreateMcubeNebulaAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.CreateMcubeNebulaAppResponse:
        """
        @param request: CreateMcubeNebulaAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMcubeNebulaAppResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.h_5id):
            body['H5Id'] = request.h_5id
        if not UtilClient.is_unset(request.h_5name):
            body['H5Name'] = request.h_5name
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMcubeNebulaApp',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.CreateMcubeNebulaAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_mcube_nebula_app_with_options_async(
        self,
        request: m_paa_s20201028_models.CreateMcubeNebulaAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.CreateMcubeNebulaAppResponse:
        """
        @param request: CreateMcubeNebulaAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMcubeNebulaAppResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.h_5id):
            body['H5Id'] = request.h_5id
        if not UtilClient.is_unset(request.h_5name):
            body['H5Name'] = request.h_5name
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMcubeNebulaApp',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.CreateMcubeNebulaAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_mcube_nebula_app(
        self,
        request: m_paa_s20201028_models.CreateMcubeNebulaAppRequest,
    ) -> m_paa_s20201028_models.CreateMcubeNebulaAppResponse:
        """
        @param request: CreateMcubeNebulaAppRequest
        @return: CreateMcubeNebulaAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_mcube_nebula_app_with_options(request, runtime)

    async def create_mcube_nebula_app_async(
        self,
        request: m_paa_s20201028_models.CreateMcubeNebulaAppRequest,
    ) -> m_paa_s20201028_models.CreateMcubeNebulaAppResponse:
        """
        @param request: CreateMcubeNebulaAppRequest
        @return: CreateMcubeNebulaAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_mcube_nebula_app_with_options_async(request, runtime)

    def create_mcube_nebula_resource_with_options(
        self,
        request: m_paa_s20201028_models.CreateMcubeNebulaResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.CreateMcubeNebulaResourceResponse:
        """
        @param request: CreateMcubeNebulaResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMcubeNebulaResourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.auto_install):
            body['AutoInstall'] = request.auto_install
        if not UtilClient.is_unset(request.client_version_max):
            body['ClientVersionMax'] = request.client_version_max
        if not UtilClient.is_unset(request.client_version_min):
            body['ClientVersionMin'] = request.client_version_min
        if not UtilClient.is_unset(request.custom_domain_name):
            body['CustomDomainName'] = request.custom_domain_name
        if not UtilClient.is_unset(request.extend_info):
            body['ExtendInfo'] = request.extend_info
        if not UtilClient.is_unset(request.file_url):
            body['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.h_5id):
            body['H5Id'] = request.h_5id
        if not UtilClient.is_unset(request.h_5name):
            body['H5Name'] = request.h_5name
        if not UtilClient.is_unset(request.h_5version):
            body['H5Version'] = request.h_5version
        if not UtilClient.is_unset(request.install_type):
            body['InstallType'] = request.install_type
        if not UtilClient.is_unset(request.main_url):
            body['MainUrl'] = request.main_url
        if not UtilClient.is_unset(request.onex_flag):
            body['OnexFlag'] = request.onex_flag
        if not UtilClient.is_unset(request.platform):
            body['Platform'] = request.platform
        if not UtilClient.is_unset(request.repeat_nebula):
            body['RepeatNebula'] = request.repeat_nebula
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.sub_url):
            body['SubUrl'] = request.sub_url
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.vhost):
            body['Vhost'] = request.vhost
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMcubeNebulaResource',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.CreateMcubeNebulaResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_mcube_nebula_resource_with_options_async(
        self,
        request: m_paa_s20201028_models.CreateMcubeNebulaResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.CreateMcubeNebulaResourceResponse:
        """
        @param request: CreateMcubeNebulaResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMcubeNebulaResourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.auto_install):
            body['AutoInstall'] = request.auto_install
        if not UtilClient.is_unset(request.client_version_max):
            body['ClientVersionMax'] = request.client_version_max
        if not UtilClient.is_unset(request.client_version_min):
            body['ClientVersionMin'] = request.client_version_min
        if not UtilClient.is_unset(request.custom_domain_name):
            body['CustomDomainName'] = request.custom_domain_name
        if not UtilClient.is_unset(request.extend_info):
            body['ExtendInfo'] = request.extend_info
        if not UtilClient.is_unset(request.file_url):
            body['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.h_5id):
            body['H5Id'] = request.h_5id
        if not UtilClient.is_unset(request.h_5name):
            body['H5Name'] = request.h_5name
        if not UtilClient.is_unset(request.h_5version):
            body['H5Version'] = request.h_5version
        if not UtilClient.is_unset(request.install_type):
            body['InstallType'] = request.install_type
        if not UtilClient.is_unset(request.main_url):
            body['MainUrl'] = request.main_url
        if not UtilClient.is_unset(request.onex_flag):
            body['OnexFlag'] = request.onex_flag
        if not UtilClient.is_unset(request.platform):
            body['Platform'] = request.platform
        if not UtilClient.is_unset(request.repeat_nebula):
            body['RepeatNebula'] = request.repeat_nebula
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.sub_url):
            body['SubUrl'] = request.sub_url
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.vhost):
            body['Vhost'] = request.vhost
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMcubeNebulaResource',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.CreateMcubeNebulaResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_mcube_nebula_resource(
        self,
        request: m_paa_s20201028_models.CreateMcubeNebulaResourceRequest,
    ) -> m_paa_s20201028_models.CreateMcubeNebulaResourceResponse:
        """
        @param request: CreateMcubeNebulaResourceRequest
        @return: CreateMcubeNebulaResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_mcube_nebula_resource_with_options(request, runtime)

    async def create_mcube_nebula_resource_async(
        self,
        request: m_paa_s20201028_models.CreateMcubeNebulaResourceRequest,
    ) -> m_paa_s20201028_models.CreateMcubeNebulaResourceResponse:
        """
        @param request: CreateMcubeNebulaResourceRequest
        @return: CreateMcubeNebulaResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_mcube_nebula_resource_with_options_async(request, runtime)

    def create_mcube_nebula_task_with_options(
        self,
        request: m_paa_s20201028_models.CreateMcubeNebulaTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.CreateMcubeNebulaTaskResponse:
        """
        @param request: CreateMcubeNebulaTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMcubeNebulaTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_code):
            body['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.biz_type):
            body['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.creator):
            body['Creator'] = request.creator
        if not UtilClient.is_unset(request.gmt_create):
            body['GmtCreate'] = request.gmt_create
        if not UtilClient.is_unset(request.gmt_modified):
            body['GmtModified'] = request.gmt_modified
        if not UtilClient.is_unset(request.gmt_modified_str):
            body['GmtModifiedStr'] = request.gmt_modified_str
        if not UtilClient.is_unset(request.grey_config_info):
            body['GreyConfigInfo'] = request.grey_config_info
        if not UtilClient.is_unset(request.grey_endtime):
            body['GreyEndtime'] = request.grey_endtime
        if not UtilClient.is_unset(request.grey_endtime_data):
            body['GreyEndtimeData'] = request.grey_endtime_data
        if not UtilClient.is_unset(request.grey_endtime_str):
            body['GreyEndtimeStr'] = request.grey_endtime_str
        if not UtilClient.is_unset(request.grey_num):
            body['GreyNum'] = request.grey_num
        if not UtilClient.is_unset(request.grey_url):
            body['GreyUrl'] = request.grey_url
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.memo):
            body['Memo'] = request.memo
        if not UtilClient.is_unset(request.modifier):
            body['Modifier'] = request.modifier
        if not UtilClient.is_unset(request.package_id):
            body['PackageId'] = request.package_id
        if not UtilClient.is_unset(request.percent):
            body['Percent'] = request.percent
        if not UtilClient.is_unset(request.platform):
            body['Platform'] = request.platform
        if not UtilClient.is_unset(request.product_id):
            body['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.product_version):
            body['ProductVersion'] = request.product_version
        if not UtilClient.is_unset(request.publish_mode):
            body['PublishMode'] = request.publish_mode
        if not UtilClient.is_unset(request.publish_type):
            body['PublishType'] = request.publish_type
        if not UtilClient.is_unset(request.release_version):
            body['ReleaseVersion'] = request.release_version
        if not UtilClient.is_unset(request.res_ids):
            body['ResIds'] = request.res_ids
        if not UtilClient.is_unset(request.serial_version_uid):
            body['SerialVersionUID'] = request.serial_version_uid
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.sync_mode):
            body['SyncMode'] = request.sync_mode
        if not UtilClient.is_unset(request.sync_result):
            body['SyncResult'] = request.sync_result
        if not UtilClient.is_unset(request.task_name):
            body['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.task_status):
            body['TaskStatus'] = request.task_status
        if not UtilClient.is_unset(request.task_type):
            body['TaskType'] = request.task_type
        if not UtilClient.is_unset(request.task_version):
            body['TaskVersion'] = request.task_version
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.upgrade_notice_num):
            body['UpgradeNoticeNum'] = request.upgrade_notice_num
        if not UtilClient.is_unset(request.upgrade_progress):
            body['UpgradeProgress'] = request.upgrade_progress
        if not UtilClient.is_unset(request.whitelist_ids):
            body['WhitelistIds'] = request.whitelist_ids
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMcubeNebulaTask',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.CreateMcubeNebulaTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_mcube_nebula_task_with_options_async(
        self,
        request: m_paa_s20201028_models.CreateMcubeNebulaTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.CreateMcubeNebulaTaskResponse:
        """
        @param request: CreateMcubeNebulaTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMcubeNebulaTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_code):
            body['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.biz_type):
            body['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.creator):
            body['Creator'] = request.creator
        if not UtilClient.is_unset(request.gmt_create):
            body['GmtCreate'] = request.gmt_create
        if not UtilClient.is_unset(request.gmt_modified):
            body['GmtModified'] = request.gmt_modified
        if not UtilClient.is_unset(request.gmt_modified_str):
            body['GmtModifiedStr'] = request.gmt_modified_str
        if not UtilClient.is_unset(request.grey_config_info):
            body['GreyConfigInfo'] = request.grey_config_info
        if not UtilClient.is_unset(request.grey_endtime):
            body['GreyEndtime'] = request.grey_endtime
        if not UtilClient.is_unset(request.grey_endtime_data):
            body['GreyEndtimeData'] = request.grey_endtime_data
        if not UtilClient.is_unset(request.grey_endtime_str):
            body['GreyEndtimeStr'] = request.grey_endtime_str
        if not UtilClient.is_unset(request.grey_num):
            body['GreyNum'] = request.grey_num
        if not UtilClient.is_unset(request.grey_url):
            body['GreyUrl'] = request.grey_url
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.memo):
            body['Memo'] = request.memo
        if not UtilClient.is_unset(request.modifier):
            body['Modifier'] = request.modifier
        if not UtilClient.is_unset(request.package_id):
            body['PackageId'] = request.package_id
        if not UtilClient.is_unset(request.percent):
            body['Percent'] = request.percent
        if not UtilClient.is_unset(request.platform):
            body['Platform'] = request.platform
        if not UtilClient.is_unset(request.product_id):
            body['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.product_version):
            body['ProductVersion'] = request.product_version
        if not UtilClient.is_unset(request.publish_mode):
            body['PublishMode'] = request.publish_mode
        if not UtilClient.is_unset(request.publish_type):
            body['PublishType'] = request.publish_type
        if not UtilClient.is_unset(request.release_version):
            body['ReleaseVersion'] = request.release_version
        if not UtilClient.is_unset(request.res_ids):
            body['ResIds'] = request.res_ids
        if not UtilClient.is_unset(request.serial_version_uid):
            body['SerialVersionUID'] = request.serial_version_uid
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.sync_mode):
            body['SyncMode'] = request.sync_mode
        if not UtilClient.is_unset(request.sync_result):
            body['SyncResult'] = request.sync_result
        if not UtilClient.is_unset(request.task_name):
            body['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.task_status):
            body['TaskStatus'] = request.task_status
        if not UtilClient.is_unset(request.task_type):
            body['TaskType'] = request.task_type
        if not UtilClient.is_unset(request.task_version):
            body['TaskVersion'] = request.task_version
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.upgrade_notice_num):
            body['UpgradeNoticeNum'] = request.upgrade_notice_num
        if not UtilClient.is_unset(request.upgrade_progress):
            body['UpgradeProgress'] = request.upgrade_progress
        if not UtilClient.is_unset(request.whitelist_ids):
            body['WhitelistIds'] = request.whitelist_ids
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMcubeNebulaTask',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.CreateMcubeNebulaTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_mcube_nebula_task(
        self,
        request: m_paa_s20201028_models.CreateMcubeNebulaTaskRequest,
    ) -> m_paa_s20201028_models.CreateMcubeNebulaTaskResponse:
        """
        @param request: CreateMcubeNebulaTaskRequest
        @return: CreateMcubeNebulaTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_mcube_nebula_task_with_options(request, runtime)

    async def create_mcube_nebula_task_async(
        self,
        request: m_paa_s20201028_models.CreateMcubeNebulaTaskRequest,
    ) -> m_paa_s20201028_models.CreateMcubeNebulaTaskResponse:
        """
        @param request: CreateMcubeNebulaTaskRequest
        @return: CreateMcubeNebulaTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_mcube_nebula_task_with_options_async(request, runtime)

    def create_mcube_upgrade_package_with_options(
        self,
        request: m_paa_s20201028_models.CreateMcubeUpgradePackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.CreateMcubeUpgradePackageResponse:
        """
        @param request: CreateMcubeUpgradePackageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMcubeUpgradePackageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_version):
            body['AppVersion'] = request.app_version
        if not UtilClient.is_unset(request.appstore_url):
            body['AppstoreUrl'] = request.appstore_url
        if not UtilClient.is_unset(request.bundle_id):
            body['BundleId'] = request.bundle_id
        if not UtilClient.is_unset(request.custom_domain_name):
            body['CustomDomainName'] = request.custom_domain_name
        if not UtilClient.is_unset(request.desc):
            body['Desc'] = request.desc
        if not UtilClient.is_unset(request.download_url):
            body['DownloadUrl'] = request.download_url
        if not UtilClient.is_unset(request.file_url):
            body['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.harmony_label):
            body['HarmonyLabel'] = request.harmony_label
        if not UtilClient.is_unset(request.icon_file_url):
            body['IconFileUrl'] = request.icon_file_url
        if not UtilClient.is_unset(request.install_amount):
            body['InstallAmount'] = request.install_amount
        if not UtilClient.is_unset(request.ios_symbolfile_url):
            body['IosSymbolfileUrl'] = request.ios_symbolfile_url
        if not UtilClient.is_unset(request.is_enterprise):
            body['IsEnterprise'] = request.is_enterprise
        if not UtilClient.is_unset(request.large_icon_url):
            body['LargeIconUrl'] = request.large_icon_url
        if not UtilClient.is_unset(request.need_check):
            body['NeedCheck'] = request.need_check
        if not UtilClient.is_unset(request.onex_flag):
            body['OnexFlag'] = request.onex_flag
        if not UtilClient.is_unset(request.platform):
            body['Platform'] = request.platform
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.valid_days):
            body['ValidDays'] = request.valid_days
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMcubeUpgradePackage',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.CreateMcubeUpgradePackageResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_mcube_upgrade_package_with_options_async(
        self,
        request: m_paa_s20201028_models.CreateMcubeUpgradePackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.CreateMcubeUpgradePackageResponse:
        """
        @param request: CreateMcubeUpgradePackageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMcubeUpgradePackageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_version):
            body['AppVersion'] = request.app_version
        if not UtilClient.is_unset(request.appstore_url):
            body['AppstoreUrl'] = request.appstore_url
        if not UtilClient.is_unset(request.bundle_id):
            body['BundleId'] = request.bundle_id
        if not UtilClient.is_unset(request.custom_domain_name):
            body['CustomDomainName'] = request.custom_domain_name
        if not UtilClient.is_unset(request.desc):
            body['Desc'] = request.desc
        if not UtilClient.is_unset(request.download_url):
            body['DownloadUrl'] = request.download_url
        if not UtilClient.is_unset(request.file_url):
            body['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.harmony_label):
            body['HarmonyLabel'] = request.harmony_label
        if not UtilClient.is_unset(request.icon_file_url):
            body['IconFileUrl'] = request.icon_file_url
        if not UtilClient.is_unset(request.install_amount):
            body['InstallAmount'] = request.install_amount
        if not UtilClient.is_unset(request.ios_symbolfile_url):
            body['IosSymbolfileUrl'] = request.ios_symbolfile_url
        if not UtilClient.is_unset(request.is_enterprise):
            body['IsEnterprise'] = request.is_enterprise
        if not UtilClient.is_unset(request.large_icon_url):
            body['LargeIconUrl'] = request.large_icon_url
        if not UtilClient.is_unset(request.need_check):
            body['NeedCheck'] = request.need_check
        if not UtilClient.is_unset(request.onex_flag):
            body['OnexFlag'] = request.onex_flag
        if not UtilClient.is_unset(request.platform):
            body['Platform'] = request.platform
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.valid_days):
            body['ValidDays'] = request.valid_days
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMcubeUpgradePackage',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.CreateMcubeUpgradePackageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_mcube_upgrade_package(
        self,
        request: m_paa_s20201028_models.CreateMcubeUpgradePackageRequest,
    ) -> m_paa_s20201028_models.CreateMcubeUpgradePackageResponse:
        """
        @param request: CreateMcubeUpgradePackageRequest
        @return: CreateMcubeUpgradePackageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_mcube_upgrade_package_with_options(request, runtime)

    async def create_mcube_upgrade_package_async(
        self,
        request: m_paa_s20201028_models.CreateMcubeUpgradePackageRequest,
    ) -> m_paa_s20201028_models.CreateMcubeUpgradePackageResponse:
        """
        @param request: CreateMcubeUpgradePackageRequest
        @return: CreateMcubeUpgradePackageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_mcube_upgrade_package_with_options_async(request, runtime)

    def create_mcube_upgrade_task_with_options(
        self,
        request: m_paa_s20201028_models.CreateMcubeUpgradeTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.CreateMcubeUpgradeTaskResponse:
        """
        @param request: CreateMcubeUpgradeTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMcubeUpgradeTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.grey_config_info):
            body['GreyConfigInfo'] = request.grey_config_info
        if not UtilClient.is_unset(request.grey_endtime_data):
            body['GreyEndtimeData'] = request.grey_endtime_data
        if not UtilClient.is_unset(request.grey_num):
            body['GreyNum'] = request.grey_num
        if not UtilClient.is_unset(request.history_force):
            body['HistoryForce'] = request.history_force
        if not UtilClient.is_unset(request.memo):
            body['Memo'] = request.memo
        if not UtilClient.is_unset(request.package_info_id):
            body['PackageInfoId'] = request.package_info_id
        if not UtilClient.is_unset(request.publish_mode):
            body['PublishMode'] = request.publish_mode
        if not UtilClient.is_unset(request.publish_type):
            body['PublishType'] = request.publish_type
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.upgrade_content):
            body['UpgradeContent'] = request.upgrade_content
        if not UtilClient.is_unset(request.upgrade_type):
            body['UpgradeType'] = request.upgrade_type
        if not UtilClient.is_unset(request.whitelist_ids):
            body['WhitelistIds'] = request.whitelist_ids
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMcubeUpgradeTask',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.CreateMcubeUpgradeTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_mcube_upgrade_task_with_options_async(
        self,
        request: m_paa_s20201028_models.CreateMcubeUpgradeTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.CreateMcubeUpgradeTaskResponse:
        """
        @param request: CreateMcubeUpgradeTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMcubeUpgradeTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.grey_config_info):
            body['GreyConfigInfo'] = request.grey_config_info
        if not UtilClient.is_unset(request.grey_endtime_data):
            body['GreyEndtimeData'] = request.grey_endtime_data
        if not UtilClient.is_unset(request.grey_num):
            body['GreyNum'] = request.grey_num
        if not UtilClient.is_unset(request.history_force):
            body['HistoryForce'] = request.history_force
        if not UtilClient.is_unset(request.memo):
            body['Memo'] = request.memo
        if not UtilClient.is_unset(request.package_info_id):
            body['PackageInfoId'] = request.package_info_id
        if not UtilClient.is_unset(request.publish_mode):
            body['PublishMode'] = request.publish_mode
        if not UtilClient.is_unset(request.publish_type):
            body['PublishType'] = request.publish_type
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.upgrade_content):
            body['UpgradeContent'] = request.upgrade_content
        if not UtilClient.is_unset(request.upgrade_type):
            body['UpgradeType'] = request.upgrade_type
        if not UtilClient.is_unset(request.whitelist_ids):
            body['WhitelistIds'] = request.whitelist_ids
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMcubeUpgradeTask',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.CreateMcubeUpgradeTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_mcube_upgrade_task(
        self,
        request: m_paa_s20201028_models.CreateMcubeUpgradeTaskRequest,
    ) -> m_paa_s20201028_models.CreateMcubeUpgradeTaskResponse:
        """
        @param request: CreateMcubeUpgradeTaskRequest
        @return: CreateMcubeUpgradeTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_mcube_upgrade_task_with_options(request, runtime)

    async def create_mcube_upgrade_task_async(
        self,
        request: m_paa_s20201028_models.CreateMcubeUpgradeTaskRequest,
    ) -> m_paa_s20201028_models.CreateMcubeUpgradeTaskResponse:
        """
        @param request: CreateMcubeUpgradeTaskRequest
        @return: CreateMcubeUpgradeTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_mcube_upgrade_task_with_options_async(request, runtime)

    def create_mcube_vhost_with_options(
        self,
        request: m_paa_s20201028_models.CreateMcubeVhostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.CreateMcubeVhostResponse:
        """
        @param request: CreateMcubeVhostRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMcubeVhostResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.vhost):
            body['Vhost'] = request.vhost
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMcubeVhost',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.CreateMcubeVhostResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_mcube_vhost_with_options_async(
        self,
        request: m_paa_s20201028_models.CreateMcubeVhostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.CreateMcubeVhostResponse:
        """
        @param request: CreateMcubeVhostRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMcubeVhostResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.vhost):
            body['Vhost'] = request.vhost
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMcubeVhost',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.CreateMcubeVhostResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_mcube_vhost(
        self,
        request: m_paa_s20201028_models.CreateMcubeVhostRequest,
    ) -> m_paa_s20201028_models.CreateMcubeVhostResponse:
        """
        @param request: CreateMcubeVhostRequest
        @return: CreateMcubeVhostResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_mcube_vhost_with_options(request, runtime)

    async def create_mcube_vhost_async(
        self,
        request: m_paa_s20201028_models.CreateMcubeVhostRequest,
    ) -> m_paa_s20201028_models.CreateMcubeVhostResponse:
        """
        @param request: CreateMcubeVhostRequest
        @return: CreateMcubeVhostResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_mcube_vhost_with_options_async(request, runtime)

    def create_mcube_whitelist_with_options(
        self,
        request: m_paa_s20201028_models.CreateMcubeWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.CreateMcubeWhitelistResponse:
        """
        @param request: CreateMcubeWhitelistRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMcubeWhitelistResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.white_list_name):
            body['WhiteListName'] = request.white_list_name
        if not UtilClient.is_unset(request.whitelist_type):
            body['WhitelistType'] = request.whitelist_type
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMcubeWhitelist',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.CreateMcubeWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_mcube_whitelist_with_options_async(
        self,
        request: m_paa_s20201028_models.CreateMcubeWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.CreateMcubeWhitelistResponse:
        """
        @param request: CreateMcubeWhitelistRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMcubeWhitelistResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.white_list_name):
            body['WhiteListName'] = request.white_list_name
        if not UtilClient.is_unset(request.whitelist_type):
            body['WhitelistType'] = request.whitelist_type
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMcubeWhitelist',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.CreateMcubeWhitelistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_mcube_whitelist(
        self,
        request: m_paa_s20201028_models.CreateMcubeWhitelistRequest,
    ) -> m_paa_s20201028_models.CreateMcubeWhitelistResponse:
        """
        @param request: CreateMcubeWhitelistRequest
        @return: CreateMcubeWhitelistResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_mcube_whitelist_with_options(request, runtime)

    async def create_mcube_whitelist_async(
        self,
        request: m_paa_s20201028_models.CreateMcubeWhitelistRequest,
    ) -> m_paa_s20201028_models.CreateMcubeWhitelistResponse:
        """
        @param request: CreateMcubeWhitelistRequest
        @return: CreateMcubeWhitelistResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_mcube_whitelist_with_options_async(request, runtime)

    def create_mcube_whitelist_for_ide_with_options(
        self,
        request: m_paa_s20201028_models.CreateMcubeWhitelistForIdeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.CreateMcubeWhitelistForIdeResponse:
        """
        @param request: CreateMcubeWhitelistForIdeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMcubeWhitelistForIdeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        if not UtilClient.is_unset(request.whitelist_value):
            body['WhitelistValue'] = request.whitelist_value
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMcubeWhitelistForIde',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.CreateMcubeWhitelistForIdeResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_mcube_whitelist_for_ide_with_options_async(
        self,
        request: m_paa_s20201028_models.CreateMcubeWhitelistForIdeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.CreateMcubeWhitelistForIdeResponse:
        """
        @param request: CreateMcubeWhitelistForIdeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMcubeWhitelistForIdeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        if not UtilClient.is_unset(request.whitelist_value):
            body['WhitelistValue'] = request.whitelist_value
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMcubeWhitelistForIde',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.CreateMcubeWhitelistForIdeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_mcube_whitelist_for_ide(
        self,
        request: m_paa_s20201028_models.CreateMcubeWhitelistForIdeRequest,
    ) -> m_paa_s20201028_models.CreateMcubeWhitelistForIdeResponse:
        """
        @param request: CreateMcubeWhitelistForIdeRequest
        @return: CreateMcubeWhitelistForIdeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_mcube_whitelist_for_ide_with_options(request, runtime)

    async def create_mcube_whitelist_for_ide_async(
        self,
        request: m_paa_s20201028_models.CreateMcubeWhitelistForIdeRequest,
    ) -> m_paa_s20201028_models.CreateMcubeWhitelistForIdeResponse:
        """
        @param request: CreateMcubeWhitelistForIdeRequest
        @return: CreateMcubeWhitelistForIdeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_mcube_whitelist_for_ide_with_options_async(request, runtime)

    def create_mds_cube_resource_with_options(
        self,
        request: m_paa_s20201028_models.CreateMdsCubeResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.CreateMdsCubeResourceResponse:
        """
        @param request: CreateMdsCubeResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMdsCubeResourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.android_max_version):
            body['AndroidMaxVersion'] = request.android_max_version
        if not UtilClient.is_unset(request.android_min_version):
            body['AndroidMinVersion'] = request.android_min_version
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.extend_info):
            body['ExtendInfo'] = request.extend_info
        if not UtilClient.is_unset(request.file_url):
            body['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.ios_max_version):
            body['IosMaxVersion'] = request.ios_max_version
        if not UtilClient.is_unset(request.ios_min_version):
            body['IosMinVersion'] = request.ios_min_version
        if not UtilClient.is_unset(request.mock_data_url):
            body['MockDataUrl'] = request.mock_data_url
        if not UtilClient.is_unset(request.onex_flag):
            body['OnexFlag'] = request.onex_flag
        if not UtilClient.is_unset(request.platform):
            body['Platform'] = request.platform
        if not UtilClient.is_unset(request.preview_picture_url):
            body['PreviewPictureUrl'] = request.preview_picture_url
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_resource_desc):
            body['TemplateResourceDesc'] = request.template_resource_desc
        if not UtilClient.is_unset(request.template_resource_version):
            body['TemplateResourceVersion'] = request.template_resource_version
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMdsCubeResource',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.CreateMdsCubeResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_mds_cube_resource_with_options_async(
        self,
        request: m_paa_s20201028_models.CreateMdsCubeResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.CreateMdsCubeResourceResponse:
        """
        @param request: CreateMdsCubeResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMdsCubeResourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.android_max_version):
            body['AndroidMaxVersion'] = request.android_max_version
        if not UtilClient.is_unset(request.android_min_version):
            body['AndroidMinVersion'] = request.android_min_version
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.extend_info):
            body['ExtendInfo'] = request.extend_info
        if not UtilClient.is_unset(request.file_url):
            body['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.ios_max_version):
            body['IosMaxVersion'] = request.ios_max_version
        if not UtilClient.is_unset(request.ios_min_version):
            body['IosMinVersion'] = request.ios_min_version
        if not UtilClient.is_unset(request.mock_data_url):
            body['MockDataUrl'] = request.mock_data_url
        if not UtilClient.is_unset(request.onex_flag):
            body['OnexFlag'] = request.onex_flag
        if not UtilClient.is_unset(request.platform):
            body['Platform'] = request.platform
        if not UtilClient.is_unset(request.preview_picture_url):
            body['PreviewPictureUrl'] = request.preview_picture_url
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_resource_desc):
            body['TemplateResourceDesc'] = request.template_resource_desc
        if not UtilClient.is_unset(request.template_resource_version):
            body['TemplateResourceVersion'] = request.template_resource_version
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMdsCubeResource',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.CreateMdsCubeResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_mds_cube_resource(
        self,
        request: m_paa_s20201028_models.CreateMdsCubeResourceRequest,
    ) -> m_paa_s20201028_models.CreateMdsCubeResourceResponse:
        """
        @param request: CreateMdsCubeResourceRequest
        @return: CreateMdsCubeResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_mds_cube_resource_with_options(request, runtime)

    async def create_mds_cube_resource_async(
        self,
        request: m_paa_s20201028_models.CreateMdsCubeResourceRequest,
    ) -> m_paa_s20201028_models.CreateMdsCubeResourceResponse:
        """
        @param request: CreateMdsCubeResourceRequest
        @return: CreateMdsCubeResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_mds_cube_resource_with_options_async(request, runtime)

    def create_mds_cube_task_with_options(
        self,
        request: m_paa_s20201028_models.CreateMdsCubeTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.CreateMdsCubeTaskResponse:
        """
        @param request: CreateMdsCubeTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMdsCubeTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.grey_config_info):
            body['GreyConfigInfo'] = request.grey_config_info
        if not UtilClient.is_unset(request.grey_endtime_data):
            body['GreyEndtimeData'] = request.grey_endtime_data
        if not UtilClient.is_unset(request.grey_num):
            body['GreyNum'] = request.grey_num
        if not UtilClient.is_unset(request.publish_mode):
            body['PublishMode'] = request.publish_mode
        if not UtilClient.is_unset(request.publish_type):
            body['PublishType'] = request.publish_type
        if not UtilClient.is_unset(request.task_desc):
            body['TaskDesc'] = request.task_desc
        if not UtilClient.is_unset(request.template_resource_id):
            body['TemplateResourceId'] = request.template_resource_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.whitelist_ids):
            body['WhitelistIds'] = request.whitelist_ids
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMdsCubeTask',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.CreateMdsCubeTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_mds_cube_task_with_options_async(
        self,
        request: m_paa_s20201028_models.CreateMdsCubeTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.CreateMdsCubeTaskResponse:
        """
        @param request: CreateMdsCubeTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMdsCubeTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.grey_config_info):
            body['GreyConfigInfo'] = request.grey_config_info
        if not UtilClient.is_unset(request.grey_endtime_data):
            body['GreyEndtimeData'] = request.grey_endtime_data
        if not UtilClient.is_unset(request.grey_num):
            body['GreyNum'] = request.grey_num
        if not UtilClient.is_unset(request.publish_mode):
            body['PublishMode'] = request.publish_mode
        if not UtilClient.is_unset(request.publish_type):
            body['PublishType'] = request.publish_type
        if not UtilClient.is_unset(request.task_desc):
            body['TaskDesc'] = request.task_desc
        if not UtilClient.is_unset(request.template_resource_id):
            body['TemplateResourceId'] = request.template_resource_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.whitelist_ids):
            body['WhitelistIds'] = request.whitelist_ids
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMdsCubeTask',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.CreateMdsCubeTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_mds_cube_task(
        self,
        request: m_paa_s20201028_models.CreateMdsCubeTaskRequest,
    ) -> m_paa_s20201028_models.CreateMdsCubeTaskResponse:
        """
        @param request: CreateMdsCubeTaskRequest
        @return: CreateMdsCubeTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_mds_cube_task_with_options(request, runtime)

    async def create_mds_cube_task_async(
        self,
        request: m_paa_s20201028_models.CreateMdsCubeTaskRequest,
    ) -> m_paa_s20201028_models.CreateMdsCubeTaskResponse:
        """
        @param request: CreateMdsCubeTaskRequest
        @return: CreateMdsCubeTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_mds_cube_task_with_options_async(request, runtime)

    def create_mds_cube_template_with_options(
        self,
        request: m_paa_s20201028_models.CreateMdsCubeTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.CreateMdsCubeTemplateResponse:
        """
        @param request: CreateMdsCubeTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMdsCubeTemplateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.template_desc):
            body['TemplateDesc'] = request.template_desc
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_name):
            body['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMdsCubeTemplate',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.CreateMdsCubeTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_mds_cube_template_with_options_async(
        self,
        request: m_paa_s20201028_models.CreateMdsCubeTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.CreateMdsCubeTemplateResponse:
        """
        @param request: CreateMdsCubeTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMdsCubeTemplateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.template_desc):
            body['TemplateDesc'] = request.template_desc
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_name):
            body['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMdsCubeTemplate',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.CreateMdsCubeTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_mds_cube_template(
        self,
        request: m_paa_s20201028_models.CreateMdsCubeTemplateRequest,
    ) -> m_paa_s20201028_models.CreateMdsCubeTemplateResponse:
        """
        @param request: CreateMdsCubeTemplateRequest
        @return: CreateMdsCubeTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_mds_cube_template_with_options(request, runtime)

    async def create_mds_cube_template_async(
        self,
        request: m_paa_s20201028_models.CreateMdsCubeTemplateRequest,
    ) -> m_paa_s20201028_models.CreateMdsCubeTemplateResponse:
        """
        @param request: CreateMdsCubeTemplateRequest
        @return: CreateMdsCubeTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_mds_cube_template_with_options_async(request, runtime)

    def create_mds_miniprogram_task_with_options(
        self,
        request: m_paa_s20201028_models.CreateMdsMiniprogramTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.CreateMdsMiniprogramTaskResponse:
        """
        @param request: CreateMdsMiniprogramTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMdsMiniprogramTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.grey_config_info):
            body['GreyConfigInfo'] = request.grey_config_info
        if not UtilClient.is_unset(request.grey_endtime_data):
            body['GreyEndtimeData'] = request.grey_endtime_data
        if not UtilClient.is_unset(request.grey_num):
            body['GreyNum'] = request.grey_num
        if not UtilClient.is_unset(request.h_5id):
            body['H5Id'] = request.h_5id
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.memo):
            body['Memo'] = request.memo
        if not UtilClient.is_unset(request.package_id):
            body['PackageId'] = request.package_id
        if not UtilClient.is_unset(request.publish_mode):
            body['PublishMode'] = request.publish_mode
        if not UtilClient.is_unset(request.publish_type):
            body['PublishType'] = request.publish_type
        if not UtilClient.is_unset(request.sync_mode):
            body['SyncMode'] = request.sync_mode
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.whitelist_ids):
            body['WhitelistIds'] = request.whitelist_ids
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMdsMiniprogramTask',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.CreateMdsMiniprogramTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_mds_miniprogram_task_with_options_async(
        self,
        request: m_paa_s20201028_models.CreateMdsMiniprogramTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.CreateMdsMiniprogramTaskResponse:
        """
        @param request: CreateMdsMiniprogramTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMdsMiniprogramTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.grey_config_info):
            body['GreyConfigInfo'] = request.grey_config_info
        if not UtilClient.is_unset(request.grey_endtime_data):
            body['GreyEndtimeData'] = request.grey_endtime_data
        if not UtilClient.is_unset(request.grey_num):
            body['GreyNum'] = request.grey_num
        if not UtilClient.is_unset(request.h_5id):
            body['H5Id'] = request.h_5id
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.memo):
            body['Memo'] = request.memo
        if not UtilClient.is_unset(request.package_id):
            body['PackageId'] = request.package_id
        if not UtilClient.is_unset(request.publish_mode):
            body['PublishMode'] = request.publish_mode
        if not UtilClient.is_unset(request.publish_type):
            body['PublishType'] = request.publish_type
        if not UtilClient.is_unset(request.sync_mode):
            body['SyncMode'] = request.sync_mode
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.whitelist_ids):
            body['WhitelistIds'] = request.whitelist_ids
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMdsMiniprogramTask',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.CreateMdsMiniprogramTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_mds_miniprogram_task(
        self,
        request: m_paa_s20201028_models.CreateMdsMiniprogramTaskRequest,
    ) -> m_paa_s20201028_models.CreateMdsMiniprogramTaskResponse:
        """
        @param request: CreateMdsMiniprogramTaskRequest
        @return: CreateMdsMiniprogramTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_mds_miniprogram_task_with_options(request, runtime)

    async def create_mds_miniprogram_task_async(
        self,
        request: m_paa_s20201028_models.CreateMdsMiniprogramTaskRequest,
    ) -> m_paa_s20201028_models.CreateMdsMiniprogramTaskResponse:
        """
        @param request: CreateMdsMiniprogramTaskRequest
        @return: CreateMdsMiniprogramTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_mds_miniprogram_task_with_options_async(request, runtime)

    def create_open_global_data_with_options(
        self,
        request: m_paa_s20201028_models.CreateOpenGlobalDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.CreateOpenGlobalDataResponse:
        """
        @param request: CreateOpenGlobalDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateOpenGlobalDataResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_max_version):
            body['AppMaxVersion'] = request.app_max_version
        if not UtilClient.is_unset(request.app_min_version):
            body['AppMinVersion'] = request.app_min_version
        if not UtilClient.is_unset(request.biz_type):
            body['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.ext_attr_str):
            body['ExtAttrStr'] = request.ext_attr_str
        if not UtilClient.is_unset(request.max_uid):
            body['MaxUid'] = request.max_uid
        if not UtilClient.is_unset(request.min_uid):
            body['MinUid'] = request.min_uid
        if not UtilClient.is_unset(request.os_type):
            body['OsType'] = request.os_type
        if not UtilClient.is_unset(request.payload):
            body['Payload'] = request.payload
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.third_msg_id):
            body['ThirdMsgId'] = request.third_msg_id
        if not UtilClient.is_unset(request.uids):
            body['Uids'] = request.uids
        if not UtilClient.is_unset(request.valid_time_end):
            body['ValidTimeEnd'] = request.valid_time_end
        if not UtilClient.is_unset(request.valid_time_start):
            body['ValidTimeStart'] = request.valid_time_start
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOpenGlobalData',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.CreateOpenGlobalDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_open_global_data_with_options_async(
        self,
        request: m_paa_s20201028_models.CreateOpenGlobalDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.CreateOpenGlobalDataResponse:
        """
        @param request: CreateOpenGlobalDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateOpenGlobalDataResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_max_version):
            body['AppMaxVersion'] = request.app_max_version
        if not UtilClient.is_unset(request.app_min_version):
            body['AppMinVersion'] = request.app_min_version
        if not UtilClient.is_unset(request.biz_type):
            body['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.ext_attr_str):
            body['ExtAttrStr'] = request.ext_attr_str
        if not UtilClient.is_unset(request.max_uid):
            body['MaxUid'] = request.max_uid
        if not UtilClient.is_unset(request.min_uid):
            body['MinUid'] = request.min_uid
        if not UtilClient.is_unset(request.os_type):
            body['OsType'] = request.os_type
        if not UtilClient.is_unset(request.payload):
            body['Payload'] = request.payload
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.third_msg_id):
            body['ThirdMsgId'] = request.third_msg_id
        if not UtilClient.is_unset(request.uids):
            body['Uids'] = request.uids
        if not UtilClient.is_unset(request.valid_time_end):
            body['ValidTimeEnd'] = request.valid_time_end
        if not UtilClient.is_unset(request.valid_time_start):
            body['ValidTimeStart'] = request.valid_time_start
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOpenGlobalData',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.CreateOpenGlobalDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_open_global_data(
        self,
        request: m_paa_s20201028_models.CreateOpenGlobalDataRequest,
    ) -> m_paa_s20201028_models.CreateOpenGlobalDataResponse:
        """
        @param request: CreateOpenGlobalDataRequest
        @return: CreateOpenGlobalDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_open_global_data_with_options(request, runtime)

    async def create_open_global_data_async(
        self,
        request: m_paa_s20201028_models.CreateOpenGlobalDataRequest,
    ) -> m_paa_s20201028_models.CreateOpenGlobalDataResponse:
        """
        @param request: CreateOpenGlobalDataRequest
        @return: CreateOpenGlobalDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_open_global_data_with_options_async(request, runtime)

    def create_open_single_data_with_options(
        self,
        request: m_paa_s20201028_models.CreateOpenSingleDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.CreateOpenSingleDataResponse:
        """
        @param request: CreateOpenSingleDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateOpenSingleDataResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_max_version):
            body['AppMaxVersion'] = request.app_max_version
        if not UtilClient.is_unset(request.app_min_version):
            body['AppMinVersion'] = request.app_min_version
        if not UtilClient.is_unset(request.biz_type):
            body['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.check_online):
            body['CheckOnline'] = request.check_online
        if not UtilClient.is_unset(request.ext_attr_str):
            body['ExtAttrStr'] = request.ext_attr_str
        if not UtilClient.is_unset(request.link_token):
            body['LinkToken'] = request.link_token
        if not UtilClient.is_unset(request.os_type):
            body['OsType'] = request.os_type
        if not UtilClient.is_unset(request.payload):
            body['Payload'] = request.payload
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.third_msg_id):
            body['ThirdMsgId'] = request.third_msg_id
        if not UtilClient.is_unset(request.valid_time_end):
            body['ValidTimeEnd'] = request.valid_time_end
        if not UtilClient.is_unset(request.valid_time_start):
            body['ValidTimeStart'] = request.valid_time_start
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOpenSingleData',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.CreateOpenSingleDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_open_single_data_with_options_async(
        self,
        request: m_paa_s20201028_models.CreateOpenSingleDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.CreateOpenSingleDataResponse:
        """
        @param request: CreateOpenSingleDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateOpenSingleDataResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_max_version):
            body['AppMaxVersion'] = request.app_max_version
        if not UtilClient.is_unset(request.app_min_version):
            body['AppMinVersion'] = request.app_min_version
        if not UtilClient.is_unset(request.biz_type):
            body['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.check_online):
            body['CheckOnline'] = request.check_online
        if not UtilClient.is_unset(request.ext_attr_str):
            body['ExtAttrStr'] = request.ext_attr_str
        if not UtilClient.is_unset(request.link_token):
            body['LinkToken'] = request.link_token
        if not UtilClient.is_unset(request.os_type):
            body['OsType'] = request.os_type
        if not UtilClient.is_unset(request.payload):
            body['Payload'] = request.payload
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.third_msg_id):
            body['ThirdMsgId'] = request.third_msg_id
        if not UtilClient.is_unset(request.valid_time_end):
            body['ValidTimeEnd'] = request.valid_time_end
        if not UtilClient.is_unset(request.valid_time_start):
            body['ValidTimeStart'] = request.valid_time_start
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOpenSingleData',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.CreateOpenSingleDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_open_single_data(
        self,
        request: m_paa_s20201028_models.CreateOpenSingleDataRequest,
    ) -> m_paa_s20201028_models.CreateOpenSingleDataResponse:
        """
        @param request: CreateOpenSingleDataRequest
        @return: CreateOpenSingleDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_open_single_data_with_options(request, runtime)

    async def create_open_single_data_async(
        self,
        request: m_paa_s20201028_models.CreateOpenSingleDataRequest,
    ) -> m_paa_s20201028_models.CreateOpenSingleDataResponse:
        """
        @param request: CreateOpenSingleDataRequest
        @return: CreateOpenSingleDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_open_single_data_with_options_async(request, runtime)

    def create_template_with_options(
        self,
        request: m_paa_s20201028_models.CreateTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.CreateTemplateResponse:
        """
        @summary 创建模版
        
        @param request: CreateTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTemplateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.desc_info):
            body['DescInfo'] = request.desc_info
        if not UtilClient.is_unset(request.icon_urls):
            body['IconUrls'] = request.icon_urls
        if not UtilClient.is_unset(request.image_urls):
            body['ImageUrls'] = request.image_urls
        if not UtilClient.is_unset(request.jump_action):
            body['JumpAction'] = request.jump_action
        if not UtilClient.is_unset(request.push_style):
            body['PushStyle'] = request.push_style
        if not UtilClient.is_unset(request.show_style):
            body['ShowStyle'] = request.show_style
        if not UtilClient.is_unset(request.template_name):
            body['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        if not UtilClient.is_unset(request.uri):
            body['Uri'] = request.uri
        if not UtilClient.is_unset(request.variables):
            body['Variables'] = request.variables
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTemplate',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.CreateTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_template_with_options_async(
        self,
        request: m_paa_s20201028_models.CreateTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.CreateTemplateResponse:
        """
        @summary 创建模版
        
        @param request: CreateTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTemplateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.desc_info):
            body['DescInfo'] = request.desc_info
        if not UtilClient.is_unset(request.icon_urls):
            body['IconUrls'] = request.icon_urls
        if not UtilClient.is_unset(request.image_urls):
            body['ImageUrls'] = request.image_urls
        if not UtilClient.is_unset(request.jump_action):
            body['JumpAction'] = request.jump_action
        if not UtilClient.is_unset(request.push_style):
            body['PushStyle'] = request.push_style
        if not UtilClient.is_unset(request.show_style):
            body['ShowStyle'] = request.show_style
        if not UtilClient.is_unset(request.template_name):
            body['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        if not UtilClient.is_unset(request.uri):
            body['Uri'] = request.uri
        if not UtilClient.is_unset(request.variables):
            body['Variables'] = request.variables
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTemplate',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.CreateTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_template(
        self,
        request: m_paa_s20201028_models.CreateTemplateRequest,
    ) -> m_paa_s20201028_models.CreateTemplateResponse:
        """
        @summary 创建模版
        
        @param request: CreateTemplateRequest
        @return: CreateTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_template_with_options(request, runtime)

    async def create_template_async(
        self,
        request: m_paa_s20201028_models.CreateTemplateRequest,
    ) -> m_paa_s20201028_models.CreateTemplateResponse:
        """
        @summary 创建模版
        
        @param request: CreateTemplateRequest
        @return: CreateTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_template_with_options_async(request, runtime)

    def delete_cubecard_whitelist_content_with_options(
        self,
        request: m_paa_s20201028_models.DeleteCubecardWhitelistContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.DeleteCubecardWhitelistContentResponse:
        """
        @param request: DeleteCubecardWhitelistContentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCubecardWhitelistContentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.whitelist_id):
            body['WhitelistId'] = request.whitelist_id
        if not UtilClient.is_unset(request.whitelist_value):
            body['WhitelistValue'] = request.whitelist_value
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteCubecardWhitelistContent',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.DeleteCubecardWhitelistContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cubecard_whitelist_content_with_options_async(
        self,
        request: m_paa_s20201028_models.DeleteCubecardWhitelistContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.DeleteCubecardWhitelistContentResponse:
        """
        @param request: DeleteCubecardWhitelistContentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCubecardWhitelistContentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.whitelist_id):
            body['WhitelistId'] = request.whitelist_id
        if not UtilClient.is_unset(request.whitelist_value):
            body['WhitelistValue'] = request.whitelist_value
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteCubecardWhitelistContent',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.DeleteCubecardWhitelistContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cubecard_whitelist_content(
        self,
        request: m_paa_s20201028_models.DeleteCubecardWhitelistContentRequest,
    ) -> m_paa_s20201028_models.DeleteCubecardWhitelistContentResponse:
        """
        @param request: DeleteCubecardWhitelistContentRequest
        @return: DeleteCubecardWhitelistContentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_cubecard_whitelist_content_with_options(request, runtime)

    async def delete_cubecard_whitelist_content_async(
        self,
        request: m_paa_s20201028_models.DeleteCubecardWhitelistContentRequest,
    ) -> m_paa_s20201028_models.DeleteCubecardWhitelistContentResponse:
        """
        @param request: DeleteCubecardWhitelistContentRequest
        @return: DeleteCubecardWhitelistContentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_cubecard_whitelist_content_with_options_async(request, runtime)

    def delete_mcdp_aim_with_options(
        self,
        request: m_paa_s20201028_models.DeleteMcdpAimRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.DeleteMcdpAimResponse:
        """
        @param request: DeleteMcdpAimRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMcdpAimResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.mpaas_mappcenter_mcdp_aim_delete_json_str):
            body['MpaasMappcenterMcdpAimDeleteJsonStr'] = request.mpaas_mappcenter_mcdp_aim_delete_json_str
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteMcdpAim',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.DeleteMcdpAimResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_mcdp_aim_with_options_async(
        self,
        request: m_paa_s20201028_models.DeleteMcdpAimRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.DeleteMcdpAimResponse:
        """
        @param request: DeleteMcdpAimRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMcdpAimResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.mpaas_mappcenter_mcdp_aim_delete_json_str):
            body['MpaasMappcenterMcdpAimDeleteJsonStr'] = request.mpaas_mappcenter_mcdp_aim_delete_json_str
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteMcdpAim',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.DeleteMcdpAimResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_mcdp_aim(
        self,
        request: m_paa_s20201028_models.DeleteMcdpAimRequest,
    ) -> m_paa_s20201028_models.DeleteMcdpAimResponse:
        """
        @param request: DeleteMcdpAimRequest
        @return: DeleteMcdpAimResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_mcdp_aim_with_options(request, runtime)

    async def delete_mcdp_aim_async(
        self,
        request: m_paa_s20201028_models.DeleteMcdpAimRequest,
    ) -> m_paa_s20201028_models.DeleteMcdpAimResponse:
        """
        @param request: DeleteMcdpAimRequest
        @return: DeleteMcdpAimResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_mcdp_aim_with_options_async(request, runtime)

    def delete_mcdp_crowd_with_options(
        self,
        request: m_paa_s20201028_models.DeleteMcdpCrowdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.DeleteMcdpCrowdResponse:
        """
        @param request: DeleteMcdpCrowdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMcdpCrowdResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.mpaas_mappcenter_mcdp_crowd_delete_json_str):
            body['MpaasMappcenterMcdpCrowdDeleteJsonStr'] = request.mpaas_mappcenter_mcdp_crowd_delete_json_str
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteMcdpCrowd',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.DeleteMcdpCrowdResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_mcdp_crowd_with_options_async(
        self,
        request: m_paa_s20201028_models.DeleteMcdpCrowdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.DeleteMcdpCrowdResponse:
        """
        @param request: DeleteMcdpCrowdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMcdpCrowdResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.mpaas_mappcenter_mcdp_crowd_delete_json_str):
            body['MpaasMappcenterMcdpCrowdDeleteJsonStr'] = request.mpaas_mappcenter_mcdp_crowd_delete_json_str
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteMcdpCrowd',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.DeleteMcdpCrowdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_mcdp_crowd(
        self,
        request: m_paa_s20201028_models.DeleteMcdpCrowdRequest,
    ) -> m_paa_s20201028_models.DeleteMcdpCrowdResponse:
        """
        @param request: DeleteMcdpCrowdRequest
        @return: DeleteMcdpCrowdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_mcdp_crowd_with_options(request, runtime)

    async def delete_mcdp_crowd_async(
        self,
        request: m_paa_s20201028_models.DeleteMcdpCrowdRequest,
    ) -> m_paa_s20201028_models.DeleteMcdpCrowdResponse:
        """
        @param request: DeleteMcdpCrowdRequest
        @return: DeleteMcdpCrowdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_mcdp_crowd_with_options_async(request, runtime)

    def delete_mcdp_zone_with_options(
        self,
        request: m_paa_s20201028_models.DeleteMcdpZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.DeleteMcdpZoneResponse:
        """
        @param request: DeleteMcdpZoneRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMcdpZoneResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.mpaas_mappcenter_mcdp_zone_delete_json_str):
            body['MpaasMappcenterMcdpZoneDeleteJsonStr'] = request.mpaas_mappcenter_mcdp_zone_delete_json_str
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteMcdpZone',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.DeleteMcdpZoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_mcdp_zone_with_options_async(
        self,
        request: m_paa_s20201028_models.DeleteMcdpZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.DeleteMcdpZoneResponse:
        """
        @param request: DeleteMcdpZoneRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMcdpZoneResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.mpaas_mappcenter_mcdp_zone_delete_json_str):
            body['MpaasMappcenterMcdpZoneDeleteJsonStr'] = request.mpaas_mappcenter_mcdp_zone_delete_json_str
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteMcdpZone',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.DeleteMcdpZoneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_mcdp_zone(
        self,
        request: m_paa_s20201028_models.DeleteMcdpZoneRequest,
    ) -> m_paa_s20201028_models.DeleteMcdpZoneResponse:
        """
        @param request: DeleteMcdpZoneRequest
        @return: DeleteMcdpZoneResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_mcdp_zone_with_options(request, runtime)

    async def delete_mcdp_zone_async(
        self,
        request: m_paa_s20201028_models.DeleteMcdpZoneRequest,
    ) -> m_paa_s20201028_models.DeleteMcdpZoneResponse:
        """
        @param request: DeleteMcdpZoneRequest
        @return: DeleteMcdpZoneResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_mcdp_zone_with_options_async(request, runtime)

    def delete_mcube_mini_app_with_options(
        self,
        request: m_paa_s20201028_models.DeleteMcubeMiniAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.DeleteMcubeMiniAppResponse:
        """
        @param request: DeleteMcubeMiniAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMcubeMiniAppResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.h_5id):
            body['H5Id'] = request.h_5id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteMcubeMiniApp',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.DeleteMcubeMiniAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_mcube_mini_app_with_options_async(
        self,
        request: m_paa_s20201028_models.DeleteMcubeMiniAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.DeleteMcubeMiniAppResponse:
        """
        @param request: DeleteMcubeMiniAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMcubeMiniAppResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.h_5id):
            body['H5Id'] = request.h_5id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteMcubeMiniApp',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.DeleteMcubeMiniAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_mcube_mini_app(
        self,
        request: m_paa_s20201028_models.DeleteMcubeMiniAppRequest,
    ) -> m_paa_s20201028_models.DeleteMcubeMiniAppResponse:
        """
        @param request: DeleteMcubeMiniAppRequest
        @return: DeleteMcubeMiniAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_mcube_mini_app_with_options(request, runtime)

    async def delete_mcube_mini_app_async(
        self,
        request: m_paa_s20201028_models.DeleteMcubeMiniAppRequest,
    ) -> m_paa_s20201028_models.DeleteMcubeMiniAppResponse:
        """
        @param request: DeleteMcubeMiniAppRequest
        @return: DeleteMcubeMiniAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_mcube_mini_app_with_options_async(request, runtime)

    def delete_mcube_nebula_app_with_options(
        self,
        request: m_paa_s20201028_models.DeleteMcubeNebulaAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.DeleteMcubeNebulaAppResponse:
        """
        @param request: DeleteMcubeNebulaAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMcubeNebulaAppResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.h_5id):
            body['H5Id'] = request.h_5id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteMcubeNebulaApp',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.DeleteMcubeNebulaAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_mcube_nebula_app_with_options_async(
        self,
        request: m_paa_s20201028_models.DeleteMcubeNebulaAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.DeleteMcubeNebulaAppResponse:
        """
        @param request: DeleteMcubeNebulaAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMcubeNebulaAppResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.h_5id):
            body['H5Id'] = request.h_5id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteMcubeNebulaApp',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.DeleteMcubeNebulaAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_mcube_nebula_app(
        self,
        request: m_paa_s20201028_models.DeleteMcubeNebulaAppRequest,
    ) -> m_paa_s20201028_models.DeleteMcubeNebulaAppResponse:
        """
        @param request: DeleteMcubeNebulaAppRequest
        @return: DeleteMcubeNebulaAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_mcube_nebula_app_with_options(request, runtime)

    async def delete_mcube_nebula_app_async(
        self,
        request: m_paa_s20201028_models.DeleteMcubeNebulaAppRequest,
    ) -> m_paa_s20201028_models.DeleteMcubeNebulaAppResponse:
        """
        @param request: DeleteMcubeNebulaAppRequest
        @return: DeleteMcubeNebulaAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_mcube_nebula_app_with_options_async(request, runtime)

    def delete_mcube_upgrade_resource_with_options(
        self,
        request: m_paa_s20201028_models.DeleteMcubeUpgradeResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.DeleteMcubeUpgradeResourceResponse:
        """
        @param request: DeleteMcubeUpgradeResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMcubeUpgradeResourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.platform):
            body['Platform'] = request.platform
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteMcubeUpgradeResource',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.DeleteMcubeUpgradeResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_mcube_upgrade_resource_with_options_async(
        self,
        request: m_paa_s20201028_models.DeleteMcubeUpgradeResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.DeleteMcubeUpgradeResourceResponse:
        """
        @param request: DeleteMcubeUpgradeResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMcubeUpgradeResourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.platform):
            body['Platform'] = request.platform
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteMcubeUpgradeResource',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.DeleteMcubeUpgradeResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_mcube_upgrade_resource(
        self,
        request: m_paa_s20201028_models.DeleteMcubeUpgradeResourceRequest,
    ) -> m_paa_s20201028_models.DeleteMcubeUpgradeResourceResponse:
        """
        @param request: DeleteMcubeUpgradeResourceRequest
        @return: DeleteMcubeUpgradeResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_mcube_upgrade_resource_with_options(request, runtime)

    async def delete_mcube_upgrade_resource_async(
        self,
        request: m_paa_s20201028_models.DeleteMcubeUpgradeResourceRequest,
    ) -> m_paa_s20201028_models.DeleteMcubeUpgradeResourceResponse:
        """
        @param request: DeleteMcubeUpgradeResourceRequest
        @return: DeleteMcubeUpgradeResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_mcube_upgrade_resource_with_options_async(request, runtime)

    def delete_mcube_whitelist_with_options(
        self,
        request: m_paa_s20201028_models.DeleteMcubeWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.DeleteMcubeWhitelistResponse:
        """
        @param request: DeleteMcubeWhitelistRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMcubeWhitelistResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteMcubeWhitelist',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.DeleteMcubeWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_mcube_whitelist_with_options_async(
        self,
        request: m_paa_s20201028_models.DeleteMcubeWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.DeleteMcubeWhitelistResponse:
        """
        @param request: DeleteMcubeWhitelistRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMcubeWhitelistResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteMcubeWhitelist',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.DeleteMcubeWhitelistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_mcube_whitelist(
        self,
        request: m_paa_s20201028_models.DeleteMcubeWhitelistRequest,
    ) -> m_paa_s20201028_models.DeleteMcubeWhitelistResponse:
        """
        @param request: DeleteMcubeWhitelistRequest
        @return: DeleteMcubeWhitelistResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_mcube_whitelist_with_options(request, runtime)

    async def delete_mcube_whitelist_async(
        self,
        request: m_paa_s20201028_models.DeleteMcubeWhitelistRequest,
    ) -> m_paa_s20201028_models.DeleteMcubeWhitelistResponse:
        """
        @param request: DeleteMcubeWhitelistRequest
        @return: DeleteMcubeWhitelistResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_mcube_whitelist_with_options_async(request, runtime)

    def delete_mds_cube_template_with_options(
        self,
        request: m_paa_s20201028_models.DeleteMdsCubeTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.DeleteMdsCubeTemplateResponse:
        """
        @param request: DeleteMdsCubeTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMdsCubeTemplateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteMdsCubeTemplate',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.DeleteMdsCubeTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_mds_cube_template_with_options_async(
        self,
        request: m_paa_s20201028_models.DeleteMdsCubeTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.DeleteMdsCubeTemplateResponse:
        """
        @param request: DeleteMdsCubeTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMdsCubeTemplateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteMdsCubeTemplate',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.DeleteMdsCubeTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_mds_cube_template(
        self,
        request: m_paa_s20201028_models.DeleteMdsCubeTemplateRequest,
    ) -> m_paa_s20201028_models.DeleteMdsCubeTemplateResponse:
        """
        @param request: DeleteMdsCubeTemplateRequest
        @return: DeleteMdsCubeTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_mds_cube_template_with_options(request, runtime)

    async def delete_mds_cube_template_async(
        self,
        request: m_paa_s20201028_models.DeleteMdsCubeTemplateRequest,
    ) -> m_paa_s20201028_models.DeleteMdsCubeTemplateResponse:
        """
        @param request: DeleteMdsCubeTemplateRequest
        @return: DeleteMdsCubeTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_mds_cube_template_with_options_async(request, runtime)

    def delete_mds_whitelist_content_with_options(
        self,
        request: m_paa_s20201028_models.DeleteMdsWhitelistContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.DeleteMdsWhitelistContentResponse:
        """
        @param request: DeleteMdsWhitelistContentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMdsWhitelistContentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.whitelist_id):
            body['WhitelistId'] = request.whitelist_id
        if not UtilClient.is_unset(request.whitelist_value):
            body['WhitelistValue'] = request.whitelist_value
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteMdsWhitelistContent',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.DeleteMdsWhitelistContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_mds_whitelist_content_with_options_async(
        self,
        request: m_paa_s20201028_models.DeleteMdsWhitelistContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.DeleteMdsWhitelistContentResponse:
        """
        @param request: DeleteMdsWhitelistContentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMdsWhitelistContentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.whitelist_id):
            body['WhitelistId'] = request.whitelist_id
        if not UtilClient.is_unset(request.whitelist_value):
            body['WhitelistValue'] = request.whitelist_value
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteMdsWhitelistContent',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.DeleteMdsWhitelistContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_mds_whitelist_content(
        self,
        request: m_paa_s20201028_models.DeleteMdsWhitelistContentRequest,
    ) -> m_paa_s20201028_models.DeleteMdsWhitelistContentResponse:
        """
        @param request: DeleteMdsWhitelistContentRequest
        @return: DeleteMdsWhitelistContentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_mds_whitelist_content_with_options(request, runtime)

    async def delete_mds_whitelist_content_async(
        self,
        request: m_paa_s20201028_models.DeleteMdsWhitelistContentRequest,
    ) -> m_paa_s20201028_models.DeleteMdsWhitelistContentResponse:
        """
        @param request: DeleteMdsWhitelistContentRequest
        @return: DeleteMdsWhitelistContentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_mds_whitelist_content_with_options_async(request, runtime)

    def delete_template_with_options(
        self,
        request: m_paa_s20201028_models.DeleteTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.DeleteTemplateResponse:
        """
        @summary 删除模版
        
        @param request: DeleteTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTemplateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_name):
            body['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteTemplate',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.DeleteTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_template_with_options_async(
        self,
        request: m_paa_s20201028_models.DeleteTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.DeleteTemplateResponse:
        """
        @summary 删除模版
        
        @param request: DeleteTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTemplateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_name):
            body['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteTemplate',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.DeleteTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_template(
        self,
        request: m_paa_s20201028_models.DeleteTemplateRequest,
    ) -> m_paa_s20201028_models.DeleteTemplateResponse:
        """
        @summary 删除模版
        
        @param request: DeleteTemplateRequest
        @return: DeleteTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_template_with_options(request, runtime)

    async def delete_template_async(
        self,
        request: m_paa_s20201028_models.DeleteTemplateRequest,
    ) -> m_paa_s20201028_models.DeleteTemplateResponse:
        """
        @summary 删除模版
        
        @param request: DeleteTemplateRequest
        @return: DeleteTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_template_with_options_async(request, runtime)

    def exist_mcube_rsa_key_with_options(
        self,
        request: m_paa_s20201028_models.ExistMcubeRsaKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.ExistMcubeRsaKeyResponse:
        """
        @param request: ExistMcubeRsaKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExistMcubeRsaKeyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExistMcubeRsaKey',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.ExistMcubeRsaKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def exist_mcube_rsa_key_with_options_async(
        self,
        request: m_paa_s20201028_models.ExistMcubeRsaKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.ExistMcubeRsaKeyResponse:
        """
        @param request: ExistMcubeRsaKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExistMcubeRsaKeyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExistMcubeRsaKey',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.ExistMcubeRsaKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def exist_mcube_rsa_key(
        self,
        request: m_paa_s20201028_models.ExistMcubeRsaKeyRequest,
    ) -> m_paa_s20201028_models.ExistMcubeRsaKeyResponse:
        """
        @param request: ExistMcubeRsaKeyRequest
        @return: ExistMcubeRsaKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.exist_mcube_rsa_key_with_options(request, runtime)

    async def exist_mcube_rsa_key_async(
        self,
        request: m_paa_s20201028_models.ExistMcubeRsaKeyRequest,
    ) -> m_paa_s20201028_models.ExistMcubeRsaKeyResponse:
        """
        @param request: ExistMcubeRsaKeyRequest
        @return: ExistMcubeRsaKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.exist_mcube_rsa_key_with_options_async(request, runtime)

    def export_mapp_center_app_config_with_options(
        self,
        request: m_paa_s20201028_models.ExportMappCenterAppConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.ExportMappCenterAppConfigResponse:
        """
        @param request: ExportMappCenterAppConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExportMappCenterAppConfigResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.apk_file_url):
            body['ApkFileUrl'] = request.apk_file_url
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.cert_rsa_base_64):
            body['CertRsaBase64'] = request.cert_rsa_base_64
        if not UtilClient.is_unset(request.identifier):
            body['Identifier'] = request.identifier
        if not UtilClient.is_unset(request.onex_flag):
            body['OnexFlag'] = request.onex_flag
        if not UtilClient.is_unset(request.system_type):
            body['SystemType'] = request.system_type
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExportMappCenterAppConfig',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.ExportMappCenterAppConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_mapp_center_app_config_with_options_async(
        self,
        request: m_paa_s20201028_models.ExportMappCenterAppConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.ExportMappCenterAppConfigResponse:
        """
        @param request: ExportMappCenterAppConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExportMappCenterAppConfigResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.apk_file_url):
            body['ApkFileUrl'] = request.apk_file_url
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.cert_rsa_base_64):
            body['CertRsaBase64'] = request.cert_rsa_base_64
        if not UtilClient.is_unset(request.identifier):
            body['Identifier'] = request.identifier
        if not UtilClient.is_unset(request.onex_flag):
            body['OnexFlag'] = request.onex_flag
        if not UtilClient.is_unset(request.system_type):
            body['SystemType'] = request.system_type
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExportMappCenterAppConfig',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.ExportMappCenterAppConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_mapp_center_app_config(
        self,
        request: m_paa_s20201028_models.ExportMappCenterAppConfigRequest,
    ) -> m_paa_s20201028_models.ExportMappCenterAppConfigResponse:
        """
        @param request: ExportMappCenterAppConfigRequest
        @return: ExportMappCenterAppConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.export_mapp_center_app_config_with_options(request, runtime)

    async def export_mapp_center_app_config_async(
        self,
        request: m_paa_s20201028_models.ExportMappCenterAppConfigRequest,
    ) -> m_paa_s20201028_models.ExportMappCenterAppConfigResponse:
        """
        @param request: ExportMappCenterAppConfigRequest
        @return: ExportMappCenterAppConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.export_mapp_center_app_config_with_options_async(request, runtime)

    def get_file_token_for_upload_to_msa_with_options(
        self,
        request: m_paa_s20201028_models.GetFileTokenForUploadToMsaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.GetFileTokenForUploadToMsaResponse:
        """
        @param request: GetFileTokenForUploadToMsaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFileTokenForUploadToMsaResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.onex_flag):
            body['OnexFlag'] = request.onex_flag
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetFileTokenForUploadToMsa',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.GetFileTokenForUploadToMsaResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_file_token_for_upload_to_msa_with_options_async(
        self,
        request: m_paa_s20201028_models.GetFileTokenForUploadToMsaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.GetFileTokenForUploadToMsaResponse:
        """
        @param request: GetFileTokenForUploadToMsaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFileTokenForUploadToMsaResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.onex_flag):
            body['OnexFlag'] = request.onex_flag
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetFileTokenForUploadToMsa',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.GetFileTokenForUploadToMsaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_file_token_for_upload_to_msa(
        self,
        request: m_paa_s20201028_models.GetFileTokenForUploadToMsaRequest,
    ) -> m_paa_s20201028_models.GetFileTokenForUploadToMsaResponse:
        """
        @param request: GetFileTokenForUploadToMsaRequest
        @return: GetFileTokenForUploadToMsaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_file_token_for_upload_to_msa_with_options(request, runtime)

    async def get_file_token_for_upload_to_msa_async(
        self,
        request: m_paa_s20201028_models.GetFileTokenForUploadToMsaRequest,
    ) -> m_paa_s20201028_models.GetFileTokenForUploadToMsaResponse:
        """
        @param request: GetFileTokenForUploadToMsaRequest
        @return: GetFileTokenForUploadToMsaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_file_token_for_upload_to_msa_with_options_async(request, runtime)

    def get_log_url_in_msa_with_options(
        self,
        request: m_paa_s20201028_models.GetLogUrlInMsaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.GetLogUrlInMsaResponse:
        """
        @param request: GetLogUrlInMsaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLogUrlInMsaResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetLogUrlInMsa',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.GetLogUrlInMsaResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_log_url_in_msa_with_options_async(
        self,
        request: m_paa_s20201028_models.GetLogUrlInMsaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.GetLogUrlInMsaResponse:
        """
        @param request: GetLogUrlInMsaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLogUrlInMsaResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetLogUrlInMsa',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.GetLogUrlInMsaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_log_url_in_msa(
        self,
        request: m_paa_s20201028_models.GetLogUrlInMsaRequest,
    ) -> m_paa_s20201028_models.GetLogUrlInMsaResponse:
        """
        @param request: GetLogUrlInMsaRequest
        @return: GetLogUrlInMsaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_log_url_in_msa_with_options(request, runtime)

    async def get_log_url_in_msa_async(
        self,
        request: m_paa_s20201028_models.GetLogUrlInMsaRequest,
    ) -> m_paa_s20201028_models.GetLogUrlInMsaResponse:
        """
        @param request: GetLogUrlInMsaRequest
        @return: GetLogUrlInMsaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_log_url_in_msa_with_options_async(request, runtime)

    def get_mcube_file_token_with_options(
        self,
        request: m_paa_s20201028_models.GetMcubeFileTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.GetMcubeFileTokenResponse:
        """
        @param request: GetMcubeFileTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMcubeFileTokenResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.onex_flag):
            body['OnexFlag'] = request.onex_flag
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetMcubeFileToken',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.GetMcubeFileTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_mcube_file_token_with_options_async(
        self,
        request: m_paa_s20201028_models.GetMcubeFileTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.GetMcubeFileTokenResponse:
        """
        @param request: GetMcubeFileTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMcubeFileTokenResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.onex_flag):
            body['OnexFlag'] = request.onex_flag
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetMcubeFileToken',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.GetMcubeFileTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_mcube_file_token(
        self,
        request: m_paa_s20201028_models.GetMcubeFileTokenRequest,
    ) -> m_paa_s20201028_models.GetMcubeFileTokenResponse:
        """
        @param request: GetMcubeFileTokenRequest
        @return: GetMcubeFileTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_mcube_file_token_with_options(request, runtime)

    async def get_mcube_file_token_async(
        self,
        request: m_paa_s20201028_models.GetMcubeFileTokenRequest,
    ) -> m_paa_s20201028_models.GetMcubeFileTokenResponse:
        """
        @param request: GetMcubeFileTokenRequest
        @return: GetMcubeFileTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_mcube_file_token_with_options_async(request, runtime)

    def get_mcube_nebula_resource_with_options(
        self,
        request: m_paa_s20201028_models.GetMcubeNebulaResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.GetMcubeNebulaResourceResponse:
        """
        @param request: GetMcubeNebulaResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMcubeNebulaResourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetMcubeNebulaResource',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.GetMcubeNebulaResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_mcube_nebula_resource_with_options_async(
        self,
        request: m_paa_s20201028_models.GetMcubeNebulaResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.GetMcubeNebulaResourceResponse:
        """
        @param request: GetMcubeNebulaResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMcubeNebulaResourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetMcubeNebulaResource',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.GetMcubeNebulaResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_mcube_nebula_resource(
        self,
        request: m_paa_s20201028_models.GetMcubeNebulaResourceRequest,
    ) -> m_paa_s20201028_models.GetMcubeNebulaResourceResponse:
        """
        @param request: GetMcubeNebulaResourceRequest
        @return: GetMcubeNebulaResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_mcube_nebula_resource_with_options(request, runtime)

    async def get_mcube_nebula_resource_async(
        self,
        request: m_paa_s20201028_models.GetMcubeNebulaResourceRequest,
    ) -> m_paa_s20201028_models.GetMcubeNebulaResourceResponse:
        """
        @param request: GetMcubeNebulaResourceRequest
        @return: GetMcubeNebulaResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_mcube_nebula_resource_with_options_async(request, runtime)

    def get_mcube_nebula_task_detail_with_options(
        self,
        request: m_paa_s20201028_models.GetMcubeNebulaTaskDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.GetMcubeNebulaTaskDetailResponse:
        """
        @param request: GetMcubeNebulaTaskDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMcubeNebulaTaskDetailResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetMcubeNebulaTaskDetail',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.GetMcubeNebulaTaskDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_mcube_nebula_task_detail_with_options_async(
        self,
        request: m_paa_s20201028_models.GetMcubeNebulaTaskDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.GetMcubeNebulaTaskDetailResponse:
        """
        @param request: GetMcubeNebulaTaskDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMcubeNebulaTaskDetailResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetMcubeNebulaTaskDetail',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.GetMcubeNebulaTaskDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_mcube_nebula_task_detail(
        self,
        request: m_paa_s20201028_models.GetMcubeNebulaTaskDetailRequest,
    ) -> m_paa_s20201028_models.GetMcubeNebulaTaskDetailResponse:
        """
        @param request: GetMcubeNebulaTaskDetailRequest
        @return: GetMcubeNebulaTaskDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_mcube_nebula_task_detail_with_options(request, runtime)

    async def get_mcube_nebula_task_detail_async(
        self,
        request: m_paa_s20201028_models.GetMcubeNebulaTaskDetailRequest,
    ) -> m_paa_s20201028_models.GetMcubeNebulaTaskDetailResponse:
        """
        @param request: GetMcubeNebulaTaskDetailRequest
        @return: GetMcubeNebulaTaskDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_mcube_nebula_task_detail_with_options_async(request, runtime)

    def get_mcube_upgrade_package_info_with_options(
        self,
        request: m_paa_s20201028_models.GetMcubeUpgradePackageInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.GetMcubeUpgradePackageInfoResponse:
        """
        @param request: GetMcubeUpgradePackageInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMcubeUpgradePackageInfoResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.package_id):
            body['PackageId'] = request.package_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetMcubeUpgradePackageInfo',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.GetMcubeUpgradePackageInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_mcube_upgrade_package_info_with_options_async(
        self,
        request: m_paa_s20201028_models.GetMcubeUpgradePackageInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.GetMcubeUpgradePackageInfoResponse:
        """
        @param request: GetMcubeUpgradePackageInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMcubeUpgradePackageInfoResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.package_id):
            body['PackageId'] = request.package_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetMcubeUpgradePackageInfo',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.GetMcubeUpgradePackageInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_mcube_upgrade_package_info(
        self,
        request: m_paa_s20201028_models.GetMcubeUpgradePackageInfoRequest,
    ) -> m_paa_s20201028_models.GetMcubeUpgradePackageInfoResponse:
        """
        @param request: GetMcubeUpgradePackageInfoRequest
        @return: GetMcubeUpgradePackageInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_mcube_upgrade_package_info_with_options(request, runtime)

    async def get_mcube_upgrade_package_info_async(
        self,
        request: m_paa_s20201028_models.GetMcubeUpgradePackageInfoRequest,
    ) -> m_paa_s20201028_models.GetMcubeUpgradePackageInfoResponse:
        """
        @param request: GetMcubeUpgradePackageInfoRequest
        @return: GetMcubeUpgradePackageInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_mcube_upgrade_package_info_with_options_async(request, runtime)

    def get_mcube_upgrade_task_info_with_options(
        self,
        request: m_paa_s20201028_models.GetMcubeUpgradeTaskInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.GetMcubeUpgradeTaskInfoResponse:
        """
        @param request: GetMcubeUpgradeTaskInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMcubeUpgradeTaskInfoResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetMcubeUpgradeTaskInfo',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.GetMcubeUpgradeTaskInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_mcube_upgrade_task_info_with_options_async(
        self,
        request: m_paa_s20201028_models.GetMcubeUpgradeTaskInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.GetMcubeUpgradeTaskInfoResponse:
        """
        @param request: GetMcubeUpgradeTaskInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMcubeUpgradeTaskInfoResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetMcubeUpgradeTaskInfo',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.GetMcubeUpgradeTaskInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_mcube_upgrade_task_info(
        self,
        request: m_paa_s20201028_models.GetMcubeUpgradeTaskInfoRequest,
    ) -> m_paa_s20201028_models.GetMcubeUpgradeTaskInfoResponse:
        """
        @param request: GetMcubeUpgradeTaskInfoRequest
        @return: GetMcubeUpgradeTaskInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_mcube_upgrade_task_info_with_options(request, runtime)

    async def get_mcube_upgrade_task_info_async(
        self,
        request: m_paa_s20201028_models.GetMcubeUpgradeTaskInfoRequest,
    ) -> m_paa_s20201028_models.GetMcubeUpgradeTaskInfoResponse:
        """
        @param request: GetMcubeUpgradeTaskInfoRequest
        @return: GetMcubeUpgradeTaskInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_mcube_upgrade_task_info_with_options_async(request, runtime)

    def get_mds_mini_config_with_options(
        self,
        request: m_paa_s20201028_models.GetMdsMiniConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.GetMdsMiniConfigResponse:
        """
        @param request: GetMdsMiniConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMdsMiniConfigResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.h_5id):
            body['H5Id'] = request.h_5id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetMdsMiniConfig',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.GetMdsMiniConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_mds_mini_config_with_options_async(
        self,
        request: m_paa_s20201028_models.GetMdsMiniConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.GetMdsMiniConfigResponse:
        """
        @param request: GetMdsMiniConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMdsMiniConfigResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.h_5id):
            body['H5Id'] = request.h_5id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetMdsMiniConfig',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.GetMdsMiniConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_mds_mini_config(
        self,
        request: m_paa_s20201028_models.GetMdsMiniConfigRequest,
    ) -> m_paa_s20201028_models.GetMdsMiniConfigResponse:
        """
        @param request: GetMdsMiniConfigRequest
        @return: GetMdsMiniConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_mds_mini_config_with_options(request, runtime)

    async def get_mds_mini_config_async(
        self,
        request: m_paa_s20201028_models.GetMdsMiniConfigRequest,
    ) -> m_paa_s20201028_models.GetMdsMiniConfigResponse:
        """
        @param request: GetMdsMiniConfigRequest
        @return: GetMdsMiniConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_mds_mini_config_with_options_async(request, runtime)

    def get_template_with_options(
        self,
        request: m_paa_s20201028_models.GetTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.GetTemplateResponse:
        """
        @summary 获取模版
        
        @param request: GetTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTemplateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_name):
            body['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTemplate',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.GetTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_template_with_options_async(
        self,
        request: m_paa_s20201028_models.GetTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.GetTemplateResponse:
        """
        @summary 获取模版
        
        @param request: GetTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTemplateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_name):
            body['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTemplate',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.GetTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_template(
        self,
        request: m_paa_s20201028_models.GetTemplateRequest,
    ) -> m_paa_s20201028_models.GetTemplateResponse:
        """
        @summary 获取模版
        
        @param request: GetTemplateRequest
        @return: GetTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_template_with_options(request, runtime)

    async def get_template_async(
        self,
        request: m_paa_s20201028_models.GetTemplateRequest,
    ) -> m_paa_s20201028_models.GetTemplateResponse:
        """
        @summary 获取模版
        
        @param request: GetTemplateRequest
        @return: GetTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_template_with_options_async(request, runtime)

    def get_user_app_donwload_url_in_msa_with_options(
        self,
        request: m_paa_s20201028_models.GetUserAppDonwloadUrlInMsaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.GetUserAppDonwloadUrlInMsaResponse:
        """
        @param request: GetUserAppDonwloadUrlInMsaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserAppDonwloadUrlInMsaResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUserAppDonwloadUrlInMsa',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.GetUserAppDonwloadUrlInMsaResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_app_donwload_url_in_msa_with_options_async(
        self,
        request: m_paa_s20201028_models.GetUserAppDonwloadUrlInMsaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.GetUserAppDonwloadUrlInMsaResponse:
        """
        @param request: GetUserAppDonwloadUrlInMsaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserAppDonwloadUrlInMsaResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUserAppDonwloadUrlInMsa',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.GetUserAppDonwloadUrlInMsaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_app_donwload_url_in_msa(
        self,
        request: m_paa_s20201028_models.GetUserAppDonwloadUrlInMsaRequest,
    ) -> m_paa_s20201028_models.GetUserAppDonwloadUrlInMsaResponse:
        """
        @param request: GetUserAppDonwloadUrlInMsaRequest
        @return: GetUserAppDonwloadUrlInMsaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_user_app_donwload_url_in_msa_with_options(request, runtime)

    async def get_user_app_donwload_url_in_msa_async(
        self,
        request: m_paa_s20201028_models.GetUserAppDonwloadUrlInMsaRequest,
    ) -> m_paa_s20201028_models.GetUserAppDonwloadUrlInMsaResponse:
        """
        @param request: GetUserAppDonwloadUrlInMsaRequest
        @return: GetUserAppDonwloadUrlInMsaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_user_app_donwload_url_in_msa_with_options_async(request, runtime)

    def get_user_app_enhance_process_in_msa_with_options(
        self,
        request: m_paa_s20201028_models.GetUserAppEnhanceProcessInMsaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.GetUserAppEnhanceProcessInMsaResponse:
        """
        @param request: GetUserAppEnhanceProcessInMsaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserAppEnhanceProcessInMsaResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUserAppEnhanceProcessInMsa',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.GetUserAppEnhanceProcessInMsaResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_app_enhance_process_in_msa_with_options_async(
        self,
        request: m_paa_s20201028_models.GetUserAppEnhanceProcessInMsaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.GetUserAppEnhanceProcessInMsaResponse:
        """
        @param request: GetUserAppEnhanceProcessInMsaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserAppEnhanceProcessInMsaResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUserAppEnhanceProcessInMsa',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.GetUserAppEnhanceProcessInMsaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_app_enhance_process_in_msa(
        self,
        request: m_paa_s20201028_models.GetUserAppEnhanceProcessInMsaRequest,
    ) -> m_paa_s20201028_models.GetUserAppEnhanceProcessInMsaResponse:
        """
        @param request: GetUserAppEnhanceProcessInMsaRequest
        @return: GetUserAppEnhanceProcessInMsaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_user_app_enhance_process_in_msa_with_options(request, runtime)

    async def get_user_app_enhance_process_in_msa_async(
        self,
        request: m_paa_s20201028_models.GetUserAppEnhanceProcessInMsaRequest,
    ) -> m_paa_s20201028_models.GetUserAppEnhanceProcessInMsaResponse:
        """
        @param request: GetUserAppEnhanceProcessInMsaRequest
        @return: GetUserAppEnhanceProcessInMsaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_user_app_enhance_process_in_msa_with_options_async(request, runtime)

    def get_user_app_upload_process_in_msa_with_options(
        self,
        request: m_paa_s20201028_models.GetUserAppUploadProcessInMsaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.GetUserAppUploadProcessInMsaResponse:
        """
        @param request: GetUserAppUploadProcessInMsaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserAppUploadProcessInMsaResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUserAppUploadProcessInMsa',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.GetUserAppUploadProcessInMsaResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_app_upload_process_in_msa_with_options_async(
        self,
        request: m_paa_s20201028_models.GetUserAppUploadProcessInMsaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.GetUserAppUploadProcessInMsaResponse:
        """
        @param request: GetUserAppUploadProcessInMsaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserAppUploadProcessInMsaResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUserAppUploadProcessInMsa',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.GetUserAppUploadProcessInMsaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_app_upload_process_in_msa(
        self,
        request: m_paa_s20201028_models.GetUserAppUploadProcessInMsaRequest,
    ) -> m_paa_s20201028_models.GetUserAppUploadProcessInMsaResponse:
        """
        @param request: GetUserAppUploadProcessInMsaRequest
        @return: GetUserAppUploadProcessInMsaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_user_app_upload_process_in_msa_with_options(request, runtime)

    async def get_user_app_upload_process_in_msa_async(
        self,
        request: m_paa_s20201028_models.GetUserAppUploadProcessInMsaRequest,
    ) -> m_paa_s20201028_models.GetUserAppUploadProcessInMsaResponse:
        """
        @param request: GetUserAppUploadProcessInMsaRequest
        @return: GetUserAppUploadProcessInMsaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_user_app_upload_process_in_msa_with_options_async(request, runtime)

    def list_analysis_core_index_with_options(
        self,
        request: m_paa_s20201028_models.ListAnalysisCoreIndexRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.ListAnalysisCoreIndexResponse:
        """
        @summary 查询报表
        
        @param request: ListAnalysisCoreIndexRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAnalysisCoreIndexResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel):
            body['Channel'] = request.channel
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.platform):
            body['Platform'] = request.platform
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListAnalysisCoreIndex',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.ListAnalysisCoreIndexResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_analysis_core_index_with_options_async(
        self,
        request: m_paa_s20201028_models.ListAnalysisCoreIndexRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.ListAnalysisCoreIndexResponse:
        """
        @summary 查询报表
        
        @param request: ListAnalysisCoreIndexRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAnalysisCoreIndexResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel):
            body['Channel'] = request.channel
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.platform):
            body['Platform'] = request.platform
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListAnalysisCoreIndex',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.ListAnalysisCoreIndexResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_analysis_core_index(
        self,
        request: m_paa_s20201028_models.ListAnalysisCoreIndexRequest,
    ) -> m_paa_s20201028_models.ListAnalysisCoreIndexResponse:
        """
        @summary 查询报表
        
        @param request: ListAnalysisCoreIndexRequest
        @return: ListAnalysisCoreIndexResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_analysis_core_index_with_options(request, runtime)

    async def list_analysis_core_index_async(
        self,
        request: m_paa_s20201028_models.ListAnalysisCoreIndexRequest,
    ) -> m_paa_s20201028_models.ListAnalysisCoreIndexResponse:
        """
        @summary 查询报表
        
        @param request: ListAnalysisCoreIndexRequest
        @return: ListAnalysisCoreIndexResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_analysis_core_index_with_options_async(request, runtime)

    def list_cubecard_apps_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.ListCubecardAppsResponse:
        """
        @param request: ListCubecardAppsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCubecardAppsResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListCubecardApps',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.ListCubecardAppsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cubecard_apps_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.ListCubecardAppsResponse:
        """
        @param request: ListCubecardAppsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCubecardAppsResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListCubecardApps',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.ListCubecardAppsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cubecard_apps(self) -> m_paa_s20201028_models.ListCubecardAppsResponse:
        """
        @return: ListCubecardAppsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_cubecard_apps_with_options(runtime)

    async def list_cubecard_apps_async(self) -> m_paa_s20201028_models.ListCubecardAppsResponse:
        """
        @return: ListCubecardAppsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_cubecard_apps_with_options_async(runtime)

    def list_mapp_center_apps_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.ListMappCenterAppsResponse:
        """
        @param request: ListMappCenterAppsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMappCenterAppsResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListMappCenterApps',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.ListMappCenterAppsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_mapp_center_apps_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.ListMappCenterAppsResponse:
        """
        @param request: ListMappCenterAppsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMappCenterAppsResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListMappCenterApps',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.ListMappCenterAppsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_mapp_center_apps(self) -> m_paa_s20201028_models.ListMappCenterAppsResponse:
        """
        @return: ListMappCenterAppsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_mapp_center_apps_with_options(runtime)

    async def list_mapp_center_apps_async(self) -> m_paa_s20201028_models.ListMappCenterAppsResponse:
        """
        @return: ListMappCenterAppsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_mapp_center_apps_with_options_async(runtime)

    def list_mapp_center_workspaces_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.ListMappCenterWorkspacesResponse:
        """
        @param request: ListMappCenterWorkspacesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMappCenterWorkspacesResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListMappCenterWorkspaces',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.ListMappCenterWorkspacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_mapp_center_workspaces_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.ListMappCenterWorkspacesResponse:
        """
        @param request: ListMappCenterWorkspacesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMappCenterWorkspacesResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListMappCenterWorkspaces',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.ListMappCenterWorkspacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_mapp_center_workspaces(self) -> m_paa_s20201028_models.ListMappCenterWorkspacesResponse:
        """
        @return: ListMappCenterWorkspacesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_mapp_center_workspaces_with_options(runtime)

    async def list_mapp_center_workspaces_async(self) -> m_paa_s20201028_models.ListMappCenterWorkspacesResponse:
        """
        @return: ListMappCenterWorkspacesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_mapp_center_workspaces_with_options_async(runtime)

    def list_mcdp_aim_with_options(
        self,
        request: m_paa_s20201028_models.ListMcdpAimRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.ListMcdpAimResponse:
        """
        @param request: ListMcdpAimRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMcdpAimResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.empty_tag):
            body['EmptyTag'] = request.empty_tag
        if not UtilClient.is_unset(request.keyword):
            body['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort):
            body['Sort'] = request.sort
        if not UtilClient.is_unset(request.sort_field):
            body['SortField'] = request.sort_field
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMcdpAim',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.ListMcdpAimResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_mcdp_aim_with_options_async(
        self,
        request: m_paa_s20201028_models.ListMcdpAimRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.ListMcdpAimResponse:
        """
        @param request: ListMcdpAimRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMcdpAimResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.empty_tag):
            body['EmptyTag'] = request.empty_tag
        if not UtilClient.is_unset(request.keyword):
            body['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort):
            body['Sort'] = request.sort
        if not UtilClient.is_unset(request.sort_field):
            body['SortField'] = request.sort_field
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMcdpAim',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.ListMcdpAimResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_mcdp_aim(
        self,
        request: m_paa_s20201028_models.ListMcdpAimRequest,
    ) -> m_paa_s20201028_models.ListMcdpAimResponse:
        """
        @param request: ListMcdpAimRequest
        @return: ListMcdpAimResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_mcdp_aim_with_options(request, runtime)

    async def list_mcdp_aim_async(
        self,
        request: m_paa_s20201028_models.ListMcdpAimRequest,
    ) -> m_paa_s20201028_models.ListMcdpAimResponse:
        """
        @param request: ListMcdpAimRequest
        @return: ListMcdpAimResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_mcdp_aim_with_options_async(request, runtime)

    def list_mcube_mini_apps_with_options(
        self,
        request: m_paa_s20201028_models.ListMcubeMiniAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.ListMcubeMiniAppsResponse:
        """
        @param request: ListMcubeMiniAppsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMcubeMiniAppsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.keyword):
            body['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_num):
            body['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMcubeMiniApps',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.ListMcubeMiniAppsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_mcube_mini_apps_with_options_async(
        self,
        request: m_paa_s20201028_models.ListMcubeMiniAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.ListMcubeMiniAppsResponse:
        """
        @param request: ListMcubeMiniAppsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMcubeMiniAppsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.keyword):
            body['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_num):
            body['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMcubeMiniApps',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.ListMcubeMiniAppsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_mcube_mini_apps(
        self,
        request: m_paa_s20201028_models.ListMcubeMiniAppsRequest,
    ) -> m_paa_s20201028_models.ListMcubeMiniAppsResponse:
        """
        @param request: ListMcubeMiniAppsRequest
        @return: ListMcubeMiniAppsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_mcube_mini_apps_with_options(request, runtime)

    async def list_mcube_mini_apps_async(
        self,
        request: m_paa_s20201028_models.ListMcubeMiniAppsRequest,
    ) -> m_paa_s20201028_models.ListMcubeMiniAppsResponse:
        """
        @param request: ListMcubeMiniAppsRequest
        @return: ListMcubeMiniAppsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_mcube_mini_apps_with_options_async(request, runtime)

    def list_mcube_mini_packages_with_options(
        self,
        request: m_paa_s20201028_models.ListMcubeMiniPackagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.ListMcubeMiniPackagesResponse:
        """
        @param request: ListMcubeMiniPackagesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMcubeMiniPackagesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.h_5id):
            body['H5Id'] = request.h_5id
        if not UtilClient.is_unset(request.package_types):
            body['PackageTypes'] = request.package_types
        if not UtilClient.is_unset(request.page_num):
            body['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMcubeMiniPackages',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.ListMcubeMiniPackagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_mcube_mini_packages_with_options_async(
        self,
        request: m_paa_s20201028_models.ListMcubeMiniPackagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.ListMcubeMiniPackagesResponse:
        """
        @param request: ListMcubeMiniPackagesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMcubeMiniPackagesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.h_5id):
            body['H5Id'] = request.h_5id
        if not UtilClient.is_unset(request.package_types):
            body['PackageTypes'] = request.package_types
        if not UtilClient.is_unset(request.page_num):
            body['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMcubeMiniPackages',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.ListMcubeMiniPackagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_mcube_mini_packages(
        self,
        request: m_paa_s20201028_models.ListMcubeMiniPackagesRequest,
    ) -> m_paa_s20201028_models.ListMcubeMiniPackagesResponse:
        """
        @param request: ListMcubeMiniPackagesRequest
        @return: ListMcubeMiniPackagesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_mcube_mini_packages_with_options(request, runtime)

    async def list_mcube_mini_packages_async(
        self,
        request: m_paa_s20201028_models.ListMcubeMiniPackagesRequest,
    ) -> m_paa_s20201028_models.ListMcubeMiniPackagesResponse:
        """
        @param request: ListMcubeMiniPackagesRequest
        @return: ListMcubeMiniPackagesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_mcube_mini_packages_with_options_async(request, runtime)

    def list_mcube_mini_tasks_with_options(
        self,
        request: m_paa_s20201028_models.ListMcubeMiniTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.ListMcubeMiniTasksResponse:
        """
        @param request: ListMcubeMiniTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMcubeMiniTasksResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMcubeMiniTasks',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.ListMcubeMiniTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_mcube_mini_tasks_with_options_async(
        self,
        request: m_paa_s20201028_models.ListMcubeMiniTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.ListMcubeMiniTasksResponse:
        """
        @param request: ListMcubeMiniTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMcubeMiniTasksResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMcubeMiniTasks',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.ListMcubeMiniTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_mcube_mini_tasks(
        self,
        request: m_paa_s20201028_models.ListMcubeMiniTasksRequest,
    ) -> m_paa_s20201028_models.ListMcubeMiniTasksResponse:
        """
        @param request: ListMcubeMiniTasksRequest
        @return: ListMcubeMiniTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_mcube_mini_tasks_with_options(request, runtime)

    async def list_mcube_mini_tasks_async(
        self,
        request: m_paa_s20201028_models.ListMcubeMiniTasksRequest,
    ) -> m_paa_s20201028_models.ListMcubeMiniTasksResponse:
        """
        @param request: ListMcubeMiniTasksRequest
        @return: ListMcubeMiniTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_mcube_mini_tasks_with_options_async(request, runtime)

    def list_mcube_nebula_apps_with_options(
        self,
        request: m_paa_s20201028_models.ListMcubeNebulaAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.ListMcubeNebulaAppsResponse:
        """
        @param request: ListMcubeNebulaAppsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMcubeNebulaAppsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.keyword):
            body['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_num):
            body['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMcubeNebulaApps',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.ListMcubeNebulaAppsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_mcube_nebula_apps_with_options_async(
        self,
        request: m_paa_s20201028_models.ListMcubeNebulaAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.ListMcubeNebulaAppsResponse:
        """
        @param request: ListMcubeNebulaAppsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMcubeNebulaAppsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.keyword):
            body['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_num):
            body['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMcubeNebulaApps',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.ListMcubeNebulaAppsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_mcube_nebula_apps(
        self,
        request: m_paa_s20201028_models.ListMcubeNebulaAppsRequest,
    ) -> m_paa_s20201028_models.ListMcubeNebulaAppsResponse:
        """
        @param request: ListMcubeNebulaAppsRequest
        @return: ListMcubeNebulaAppsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_mcube_nebula_apps_with_options(request, runtime)

    async def list_mcube_nebula_apps_async(
        self,
        request: m_paa_s20201028_models.ListMcubeNebulaAppsRequest,
    ) -> m_paa_s20201028_models.ListMcubeNebulaAppsResponse:
        """
        @param request: ListMcubeNebulaAppsRequest
        @return: ListMcubeNebulaAppsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_mcube_nebula_apps_with_options_async(request, runtime)

    def list_mcube_nebula_resources_with_options(
        self,
        request: m_paa_s20201028_models.ListMcubeNebulaResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.ListMcubeNebulaResourcesResponse:
        """
        @param request: ListMcubeNebulaResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMcubeNebulaResourcesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.h_5id):
            body['H5Id'] = request.h_5id
        if not UtilClient.is_unset(request.page_num):
            body['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMcubeNebulaResources',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.ListMcubeNebulaResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_mcube_nebula_resources_with_options_async(
        self,
        request: m_paa_s20201028_models.ListMcubeNebulaResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.ListMcubeNebulaResourcesResponse:
        """
        @param request: ListMcubeNebulaResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMcubeNebulaResourcesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.h_5id):
            body['H5Id'] = request.h_5id
        if not UtilClient.is_unset(request.page_num):
            body['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMcubeNebulaResources',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.ListMcubeNebulaResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_mcube_nebula_resources(
        self,
        request: m_paa_s20201028_models.ListMcubeNebulaResourcesRequest,
    ) -> m_paa_s20201028_models.ListMcubeNebulaResourcesResponse:
        """
        @param request: ListMcubeNebulaResourcesRequest
        @return: ListMcubeNebulaResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_mcube_nebula_resources_with_options(request, runtime)

    async def list_mcube_nebula_resources_async(
        self,
        request: m_paa_s20201028_models.ListMcubeNebulaResourcesRequest,
    ) -> m_paa_s20201028_models.ListMcubeNebulaResourcesResponse:
        """
        @param request: ListMcubeNebulaResourcesRequest
        @return: ListMcubeNebulaResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_mcube_nebula_resources_with_options_async(request, runtime)

    def list_mcube_nebula_tasks_with_options(
        self,
        request: m_paa_s20201028_models.ListMcubeNebulaTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.ListMcubeNebulaTasksResponse:
        """
        @param request: ListMcubeNebulaTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMcubeNebulaTasksResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMcubeNebulaTasks',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.ListMcubeNebulaTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_mcube_nebula_tasks_with_options_async(
        self,
        request: m_paa_s20201028_models.ListMcubeNebulaTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.ListMcubeNebulaTasksResponse:
        """
        @param request: ListMcubeNebulaTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMcubeNebulaTasksResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMcubeNebulaTasks',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.ListMcubeNebulaTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_mcube_nebula_tasks(
        self,
        request: m_paa_s20201028_models.ListMcubeNebulaTasksRequest,
    ) -> m_paa_s20201028_models.ListMcubeNebulaTasksResponse:
        """
        @param request: ListMcubeNebulaTasksRequest
        @return: ListMcubeNebulaTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_mcube_nebula_tasks_with_options(request, runtime)

    async def list_mcube_nebula_tasks_async(
        self,
        request: m_paa_s20201028_models.ListMcubeNebulaTasksRequest,
    ) -> m_paa_s20201028_models.ListMcubeNebulaTasksResponse:
        """
        @param request: ListMcubeNebulaTasksRequest
        @return: ListMcubeNebulaTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_mcube_nebula_tasks_with_options_async(request, runtime)

    def list_mcube_upgrade_packages_with_options(
        self,
        request: m_paa_s20201028_models.ListMcubeUpgradePackagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.ListMcubeUpgradePackagesResponse:
        """
        @param request: ListMcubeUpgradePackagesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMcubeUpgradePackagesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.page_num):
            body['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMcubeUpgradePackages',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.ListMcubeUpgradePackagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_mcube_upgrade_packages_with_options_async(
        self,
        request: m_paa_s20201028_models.ListMcubeUpgradePackagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.ListMcubeUpgradePackagesResponse:
        """
        @param request: ListMcubeUpgradePackagesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMcubeUpgradePackagesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.page_num):
            body['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMcubeUpgradePackages',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.ListMcubeUpgradePackagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_mcube_upgrade_packages(
        self,
        request: m_paa_s20201028_models.ListMcubeUpgradePackagesRequest,
    ) -> m_paa_s20201028_models.ListMcubeUpgradePackagesResponse:
        """
        @param request: ListMcubeUpgradePackagesRequest
        @return: ListMcubeUpgradePackagesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_mcube_upgrade_packages_with_options(request, runtime)

    async def list_mcube_upgrade_packages_async(
        self,
        request: m_paa_s20201028_models.ListMcubeUpgradePackagesRequest,
    ) -> m_paa_s20201028_models.ListMcubeUpgradePackagesResponse:
        """
        @param request: ListMcubeUpgradePackagesRequest
        @return: ListMcubeUpgradePackagesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_mcube_upgrade_packages_with_options_async(request, runtime)

    def list_mcube_upgrade_tasks_with_options(
        self,
        request: m_paa_s20201028_models.ListMcubeUpgradeTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.ListMcubeUpgradeTasksResponse:
        """
        @param request: ListMcubeUpgradeTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMcubeUpgradeTasksResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.package_id):
            body['PackageId'] = request.package_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMcubeUpgradeTasks',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.ListMcubeUpgradeTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_mcube_upgrade_tasks_with_options_async(
        self,
        request: m_paa_s20201028_models.ListMcubeUpgradeTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.ListMcubeUpgradeTasksResponse:
        """
        @param request: ListMcubeUpgradeTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMcubeUpgradeTasksResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.package_id):
            body['PackageId'] = request.package_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMcubeUpgradeTasks',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.ListMcubeUpgradeTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_mcube_upgrade_tasks(
        self,
        request: m_paa_s20201028_models.ListMcubeUpgradeTasksRequest,
    ) -> m_paa_s20201028_models.ListMcubeUpgradeTasksResponse:
        """
        @param request: ListMcubeUpgradeTasksRequest
        @return: ListMcubeUpgradeTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_mcube_upgrade_tasks_with_options(request, runtime)

    async def list_mcube_upgrade_tasks_async(
        self,
        request: m_paa_s20201028_models.ListMcubeUpgradeTasksRequest,
    ) -> m_paa_s20201028_models.ListMcubeUpgradeTasksResponse:
        """
        @param request: ListMcubeUpgradeTasksRequest
        @return: ListMcubeUpgradeTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_mcube_upgrade_tasks_with_options_async(request, runtime)

    def list_mcube_whitelists_with_options(
        self,
        request: m_paa_s20201028_models.ListMcubeWhitelistsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.ListMcubeWhitelistsResponse:
        """
        @param request: ListMcubeWhitelistsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMcubeWhitelistsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.page_num):
            body['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.whitelist_name):
            body['WhitelistName'] = request.whitelist_name
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMcubeWhitelists',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.ListMcubeWhitelistsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_mcube_whitelists_with_options_async(
        self,
        request: m_paa_s20201028_models.ListMcubeWhitelistsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.ListMcubeWhitelistsResponse:
        """
        @param request: ListMcubeWhitelistsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMcubeWhitelistsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.page_num):
            body['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.whitelist_name):
            body['WhitelistName'] = request.whitelist_name
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMcubeWhitelists',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.ListMcubeWhitelistsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_mcube_whitelists(
        self,
        request: m_paa_s20201028_models.ListMcubeWhitelistsRequest,
    ) -> m_paa_s20201028_models.ListMcubeWhitelistsResponse:
        """
        @param request: ListMcubeWhitelistsRequest
        @return: ListMcubeWhitelistsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_mcube_whitelists_with_options(request, runtime)

    async def list_mcube_whitelists_async(
        self,
        request: m_paa_s20201028_models.ListMcubeWhitelistsRequest,
    ) -> m_paa_s20201028_models.ListMcubeWhitelistsResponse:
        """
        @param request: ListMcubeWhitelistsRequest
        @return: ListMcubeWhitelistsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_mcube_whitelists_with_options_async(request, runtime)

    def list_mds_cube_resources_with_options(
        self,
        request: m_paa_s20201028_models.ListMdsCubeResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.ListMdsCubeResourcesResponse:
        """
        @param request: ListMdsCubeResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMdsCubeResourcesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.page_num):
            body['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        if not UtilClient.is_unset(request.test):
            body['test'] = request.test
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMdsCubeResources',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.ListMdsCubeResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_mds_cube_resources_with_options_async(
        self,
        request: m_paa_s20201028_models.ListMdsCubeResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.ListMdsCubeResourcesResponse:
        """
        @param request: ListMdsCubeResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMdsCubeResourcesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.page_num):
            body['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        if not UtilClient.is_unset(request.test):
            body['test'] = request.test
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMdsCubeResources',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.ListMdsCubeResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_mds_cube_resources(
        self,
        request: m_paa_s20201028_models.ListMdsCubeResourcesRequest,
    ) -> m_paa_s20201028_models.ListMdsCubeResourcesResponse:
        """
        @param request: ListMdsCubeResourcesRequest
        @return: ListMdsCubeResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_mds_cube_resources_with_options(request, runtime)

    async def list_mds_cube_resources_async(
        self,
        request: m_paa_s20201028_models.ListMdsCubeResourcesRequest,
    ) -> m_paa_s20201028_models.ListMdsCubeResourcesResponse:
        """
        @param request: ListMdsCubeResourcesRequest
        @return: ListMdsCubeResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_mds_cube_resources_with_options_async(request, runtime)

    def list_mds_cube_tasks_with_options(
        self,
        request: m_paa_s20201028_models.ListMdsCubeTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.ListMdsCubeTasksResponse:
        """
        @param request: ListMdsCubeTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMdsCubeTasksResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.page_num):
            body['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.template_resource_id):
            body['TemplateResourceId'] = request.template_resource_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMdsCubeTasks',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.ListMdsCubeTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_mds_cube_tasks_with_options_async(
        self,
        request: m_paa_s20201028_models.ListMdsCubeTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.ListMdsCubeTasksResponse:
        """
        @param request: ListMdsCubeTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMdsCubeTasksResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.page_num):
            body['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.template_resource_id):
            body['TemplateResourceId'] = request.template_resource_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMdsCubeTasks',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.ListMdsCubeTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_mds_cube_tasks(
        self,
        request: m_paa_s20201028_models.ListMdsCubeTasksRequest,
    ) -> m_paa_s20201028_models.ListMdsCubeTasksResponse:
        """
        @param request: ListMdsCubeTasksRequest
        @return: ListMdsCubeTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_mds_cube_tasks_with_options(request, runtime)

    async def list_mds_cube_tasks_async(
        self,
        request: m_paa_s20201028_models.ListMdsCubeTasksRequest,
    ) -> m_paa_s20201028_models.ListMdsCubeTasksResponse:
        """
        @param request: ListMdsCubeTasksRequest
        @return: ListMdsCubeTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_mds_cube_tasks_with_options_async(request, runtime)

    def list_mds_cube_templates_with_options(
        self,
        request: m_paa_s20201028_models.ListMdsCubeTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.ListMdsCubeTemplatesResponse:
        """
        @param request: ListMdsCubeTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMdsCubeTemplatesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.keyword):
            body['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_num):
            body['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMdsCubeTemplates',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.ListMdsCubeTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_mds_cube_templates_with_options_async(
        self,
        request: m_paa_s20201028_models.ListMdsCubeTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.ListMdsCubeTemplatesResponse:
        """
        @param request: ListMdsCubeTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMdsCubeTemplatesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.keyword):
            body['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_num):
            body['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMdsCubeTemplates',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.ListMdsCubeTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_mds_cube_templates(
        self,
        request: m_paa_s20201028_models.ListMdsCubeTemplatesRequest,
    ) -> m_paa_s20201028_models.ListMdsCubeTemplatesResponse:
        """
        @param request: ListMdsCubeTemplatesRequest
        @return: ListMdsCubeTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_mds_cube_templates_with_options(request, runtime)

    async def list_mds_cube_templates_async(
        self,
        request: m_paa_s20201028_models.ListMdsCubeTemplatesRequest,
    ) -> m_paa_s20201028_models.ListMdsCubeTemplatesResponse:
        """
        @param request: ListMdsCubeTemplatesRequest
        @return: ListMdsCubeTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_mds_cube_templates_with_options_async(request, runtime)

    def list_mgs_api_with_options(
        self,
        request: m_paa_s20201028_models.ListMgsApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.ListMgsApiResponse:
        """
        @param request: ListMgsApiRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMgsApiResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.api_status):
            body['ApiStatus'] = request.api_status
        if not UtilClient.is_unset(request.api_type):
            body['ApiType'] = request.api_type
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.format):
            body['Format'] = request.format
        if not UtilClient.is_unset(request.host):
            body['Host'] = request.host
        if not UtilClient.is_unset(request.need_encrypt):
            body['NeedEncrypt'] = request.need_encrypt
        if not UtilClient.is_unset(request.need_etag):
            body['NeedEtag'] = request.need_etag
        if not UtilClient.is_unset(request.need_sign):
            body['NeedSign'] = request.need_sign
        if not UtilClient.is_unset(request.operation_type):
            body['OperationType'] = request.operation_type
        if not UtilClient.is_unset(request.opt_fuzzy):
            body['OptFuzzy'] = request.opt_fuzzy
        if not UtilClient.is_unset(request.page_index):
            body['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sys_id):
            body['SysId'] = request.sys_id
        if not UtilClient.is_unset(request.sys_name):
            body['SysName'] = request.sys_name
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMgsApi',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.ListMgsApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_mgs_api_with_options_async(
        self,
        request: m_paa_s20201028_models.ListMgsApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.ListMgsApiResponse:
        """
        @param request: ListMgsApiRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMgsApiResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.api_status):
            body['ApiStatus'] = request.api_status
        if not UtilClient.is_unset(request.api_type):
            body['ApiType'] = request.api_type
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.format):
            body['Format'] = request.format
        if not UtilClient.is_unset(request.host):
            body['Host'] = request.host
        if not UtilClient.is_unset(request.need_encrypt):
            body['NeedEncrypt'] = request.need_encrypt
        if not UtilClient.is_unset(request.need_etag):
            body['NeedEtag'] = request.need_etag
        if not UtilClient.is_unset(request.need_sign):
            body['NeedSign'] = request.need_sign
        if not UtilClient.is_unset(request.operation_type):
            body['OperationType'] = request.operation_type
        if not UtilClient.is_unset(request.opt_fuzzy):
            body['OptFuzzy'] = request.opt_fuzzy
        if not UtilClient.is_unset(request.page_index):
            body['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sys_id):
            body['SysId'] = request.sys_id
        if not UtilClient.is_unset(request.sys_name):
            body['SysName'] = request.sys_name
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMgsApi',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.ListMgsApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_mgs_api(
        self,
        request: m_paa_s20201028_models.ListMgsApiRequest,
    ) -> m_paa_s20201028_models.ListMgsApiResponse:
        """
        @param request: ListMgsApiRequest
        @return: ListMgsApiResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_mgs_api_with_options(request, runtime)

    async def list_mgs_api_async(
        self,
        request: m_paa_s20201028_models.ListMgsApiRequest,
    ) -> m_paa_s20201028_models.ListMgsApiResponse:
        """
        @param request: ListMgsApiRequest
        @return: ListMgsApiResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_mgs_api_with_options_async(request, runtime)

    def list_template_page_with_options(
        self,
        request: m_paa_s20201028_models.ListTemplatePageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.ListTemplatePageResponse:
        """
        @summary 分页查询模版列表
        
        @param request: ListTemplatePageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTemplatePageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTemplatePage',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.ListTemplatePageResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_template_page_with_options_async(
        self,
        request: m_paa_s20201028_models.ListTemplatePageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.ListTemplatePageResponse:
        """
        @summary 分页查询模版列表
        
        @param request: ListTemplatePageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTemplatePageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTemplatePage',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.ListTemplatePageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_template_page(
        self,
        request: m_paa_s20201028_models.ListTemplatePageRequest,
    ) -> m_paa_s20201028_models.ListTemplatePageResponse:
        """
        @summary 分页查询模版列表
        
        @param request: ListTemplatePageRequest
        @return: ListTemplatePageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_template_page_with_options(request, runtime)

    async def list_template_page_async(
        self,
        request: m_paa_s20201028_models.ListTemplatePageRequest,
    ) -> m_paa_s20201028_models.ListTemplatePageResponse:
        """
        @summary 分页查询模版列表
        
        @param request: ListTemplatePageRequest
        @return: ListTemplatePageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_template_page_with_options_async(request, runtime)

    def m_trsocrservice_with_options(
        self,
        request: m_paa_s20201028_models.MTRSOCRServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.MTRSOCRServiceResponse:
        """
        @summary OCR通用接口
        
        @param request: MTRSOCRServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MTRSOCRServiceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.image_raw):
            body['ImageRaw'] = request.image_raw
        if not UtilClient.is_unset(request.mask):
            body['Mask'] = request.mask
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MTRSOCRService',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.MTRSOCRServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def m_trsocrservice_with_options_async(
        self,
        request: m_paa_s20201028_models.MTRSOCRServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.MTRSOCRServiceResponse:
        """
        @summary OCR通用接口
        
        @param request: MTRSOCRServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MTRSOCRServiceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.image_raw):
            body['ImageRaw'] = request.image_raw
        if not UtilClient.is_unset(request.mask):
            body['Mask'] = request.mask
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MTRSOCRService',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.MTRSOCRServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def m_trsocrservice(
        self,
        request: m_paa_s20201028_models.MTRSOCRServiceRequest,
    ) -> m_paa_s20201028_models.MTRSOCRServiceResponse:
        """
        @summary OCR通用接口
        
        @param request: MTRSOCRServiceRequest
        @return: MTRSOCRServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.m_trsocrservice_with_options(request, runtime)

    async def m_trsocrservice_async(
        self,
        request: m_paa_s20201028_models.MTRSOCRServiceRequest,
    ) -> m_paa_s20201028_models.MTRSOCRServiceResponse:
        """
        @summary OCR通用接口
        
        @param request: MTRSOCRServiceRequest
        @return: MTRSOCRServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.m_trsocrservice_with_options_async(request, runtime)

    def push_bind_with_options(
        self,
        request: m_paa_s20201028_models.PushBindRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.PushBindResponse:
        """
        @param request: PushBindRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PushBindResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.delivery_token):
            body['DeliveryToken'] = request.delivery_token
        if not UtilClient.is_unset(request.os_type):
            body['OsType'] = request.os_type
        if not UtilClient.is_unset(request.phone_number):
            body['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PushBind',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.PushBindResponse(),
            self.call_api(params, req, runtime)
        )

    async def push_bind_with_options_async(
        self,
        request: m_paa_s20201028_models.PushBindRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.PushBindResponse:
        """
        @param request: PushBindRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PushBindResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.delivery_token):
            body['DeliveryToken'] = request.delivery_token
        if not UtilClient.is_unset(request.os_type):
            body['OsType'] = request.os_type
        if not UtilClient.is_unset(request.phone_number):
            body['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PushBind',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.PushBindResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def push_bind(
        self,
        request: m_paa_s20201028_models.PushBindRequest,
    ) -> m_paa_s20201028_models.PushBindResponse:
        """
        @param request: PushBindRequest
        @return: PushBindResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.push_bind_with_options(request, runtime)

    async def push_bind_async(
        self,
        request: m_paa_s20201028_models.PushBindRequest,
    ) -> m_paa_s20201028_models.PushBindResponse:
        """
        @param request: PushBindRequest
        @return: PushBindResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.push_bind_with_options_async(request, runtime)

    def push_broadcast_with_options(
        self,
        tmp_req: m_paa_s20201028_models.PushBroadcastRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.PushBroadcastResponse:
        """
        @param tmp_req: PushBroadcastRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PushBroadcastResponse
        """
        UtilClient.validate_model(tmp_req)
        request = m_paa_s20201028_models.PushBroadcastShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.notify_level):
            request.notify_level_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notify_level, 'NotifyLevel', 'json')
        if not UtilClient.is_unset(tmp_req.third_channel_category):
            request.third_channel_category_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.third_channel_category, 'ThirdChannelCategory', 'json')
        body = {}
        if not UtilClient.is_unset(request.android_channel):
            body['AndroidChannel'] = request.android_channel
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.bind_end_time):
            body['BindEndTime'] = request.bind_end_time
        if not UtilClient.is_unset(request.bind_period):
            body['BindPeriod'] = request.bind_period
        if not UtilClient.is_unset(request.bind_start_time):
            body['BindStartTime'] = request.bind_start_time
        if not UtilClient.is_unset(request.channel_id):
            body['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.classification):
            body['Classification'] = request.classification
        if not UtilClient.is_unset(request.delivery_type):
            body['DeliveryType'] = request.delivery_type
        if not UtilClient.is_unset(request.expired_seconds):
            body['ExpiredSeconds'] = request.expired_seconds
        if not UtilClient.is_unset(request.extended_params):
            body['ExtendedParams'] = request.extended_params
        if not UtilClient.is_unset(request.mi_channel_id):
            body['MiChannelId'] = request.mi_channel_id
        if not UtilClient.is_unset(request.msgkey):
            body['Msgkey'] = request.msgkey
        if not UtilClient.is_unset(request.notify_level_shrink):
            body['NotifyLevel'] = request.notify_level_shrink
        if not UtilClient.is_unset(request.notify_type):
            body['NotifyType'] = request.notify_type
        if not UtilClient.is_unset(request.push_action):
            body['PushAction'] = request.push_action
        if not UtilClient.is_unset(request.push_status):
            body['PushStatus'] = request.push_status
        if not UtilClient.is_unset(request.silent):
            body['Silent'] = request.silent
        if not UtilClient.is_unset(request.strategy_content):
            body['StrategyContent'] = request.strategy_content
        if not UtilClient.is_unset(request.strategy_type):
            body['StrategyType'] = request.strategy_type
        if not UtilClient.is_unset(request.task_name):
            body['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.template_key_value):
            body['TemplateKeyValue'] = request.template_key_value
        if not UtilClient.is_unset(request.template_name):
            body['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.third_channel_category_shrink):
            body['ThirdChannelCategory'] = request.third_channel_category_shrink
        if not UtilClient.is_unset(request.time_mode):
            body['TimeMode'] = request.time_mode
        if not UtilClient.is_unset(request.transparent_message_payload):
            body['TransparentMessagePayload'] = request.transparent_message_payload
        if not UtilClient.is_unset(request.transparent_message_urgency):
            body['TransparentMessageUrgency'] = request.transparent_message_urgency
        if not UtilClient.is_unset(request.un_bind_end_time):
            body['UnBindEndTime'] = request.un_bind_end_time
        if not UtilClient.is_unset(request.un_bind_period):
            body['UnBindPeriod'] = request.un_bind_period
        if not UtilClient.is_unset(request.un_bind_start_time):
            body['UnBindStartTime'] = request.un_bind_start_time
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PushBroadcast',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.PushBroadcastResponse(),
            self.call_api(params, req, runtime)
        )

    async def push_broadcast_with_options_async(
        self,
        tmp_req: m_paa_s20201028_models.PushBroadcastRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.PushBroadcastResponse:
        """
        @param tmp_req: PushBroadcastRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PushBroadcastResponse
        """
        UtilClient.validate_model(tmp_req)
        request = m_paa_s20201028_models.PushBroadcastShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.notify_level):
            request.notify_level_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notify_level, 'NotifyLevel', 'json')
        if not UtilClient.is_unset(tmp_req.third_channel_category):
            request.third_channel_category_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.third_channel_category, 'ThirdChannelCategory', 'json')
        body = {}
        if not UtilClient.is_unset(request.android_channel):
            body['AndroidChannel'] = request.android_channel
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.bind_end_time):
            body['BindEndTime'] = request.bind_end_time
        if not UtilClient.is_unset(request.bind_period):
            body['BindPeriod'] = request.bind_period
        if not UtilClient.is_unset(request.bind_start_time):
            body['BindStartTime'] = request.bind_start_time
        if not UtilClient.is_unset(request.channel_id):
            body['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.classification):
            body['Classification'] = request.classification
        if not UtilClient.is_unset(request.delivery_type):
            body['DeliveryType'] = request.delivery_type
        if not UtilClient.is_unset(request.expired_seconds):
            body['ExpiredSeconds'] = request.expired_seconds
        if not UtilClient.is_unset(request.extended_params):
            body['ExtendedParams'] = request.extended_params
        if not UtilClient.is_unset(request.mi_channel_id):
            body['MiChannelId'] = request.mi_channel_id
        if not UtilClient.is_unset(request.msgkey):
            body['Msgkey'] = request.msgkey
        if not UtilClient.is_unset(request.notify_level_shrink):
            body['NotifyLevel'] = request.notify_level_shrink
        if not UtilClient.is_unset(request.notify_type):
            body['NotifyType'] = request.notify_type
        if not UtilClient.is_unset(request.push_action):
            body['PushAction'] = request.push_action
        if not UtilClient.is_unset(request.push_status):
            body['PushStatus'] = request.push_status
        if not UtilClient.is_unset(request.silent):
            body['Silent'] = request.silent
        if not UtilClient.is_unset(request.strategy_content):
            body['StrategyContent'] = request.strategy_content
        if not UtilClient.is_unset(request.strategy_type):
            body['StrategyType'] = request.strategy_type
        if not UtilClient.is_unset(request.task_name):
            body['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.template_key_value):
            body['TemplateKeyValue'] = request.template_key_value
        if not UtilClient.is_unset(request.template_name):
            body['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.third_channel_category_shrink):
            body['ThirdChannelCategory'] = request.third_channel_category_shrink
        if not UtilClient.is_unset(request.time_mode):
            body['TimeMode'] = request.time_mode
        if not UtilClient.is_unset(request.transparent_message_payload):
            body['TransparentMessagePayload'] = request.transparent_message_payload
        if not UtilClient.is_unset(request.transparent_message_urgency):
            body['TransparentMessageUrgency'] = request.transparent_message_urgency
        if not UtilClient.is_unset(request.un_bind_end_time):
            body['UnBindEndTime'] = request.un_bind_end_time
        if not UtilClient.is_unset(request.un_bind_period):
            body['UnBindPeriod'] = request.un_bind_period
        if not UtilClient.is_unset(request.un_bind_start_time):
            body['UnBindStartTime'] = request.un_bind_start_time
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PushBroadcast',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.PushBroadcastResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def push_broadcast(
        self,
        request: m_paa_s20201028_models.PushBroadcastRequest,
    ) -> m_paa_s20201028_models.PushBroadcastResponse:
        """
        @param request: PushBroadcastRequest
        @return: PushBroadcastResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.push_broadcast_with_options(request, runtime)

    async def push_broadcast_async(
        self,
        request: m_paa_s20201028_models.PushBroadcastRequest,
    ) -> m_paa_s20201028_models.PushBroadcastResponse:
        """
        @param request: PushBroadcastRequest
        @return: PushBroadcastResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.push_broadcast_with_options_async(request, runtime)

    def push_multiple_with_options(
        self,
        tmp_req: m_paa_s20201028_models.PushMultipleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.PushMultipleResponse:
        """
        @param tmp_req: PushMultipleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PushMultipleResponse
        """
        UtilClient.validate_model(tmp_req)
        request = m_paa_s20201028_models.PushMultipleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.notify_level):
            request.notify_level_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notify_level, 'NotifyLevel', 'json')
        if not UtilClient.is_unset(tmp_req.third_channel_category):
            request.third_channel_category_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.third_channel_category, 'ThirdChannelCategory', 'json')
        body = {}
        if not UtilClient.is_unset(request.activity_content_state):
            body['ActivityContentState'] = request.activity_content_state
        if not UtilClient.is_unset(request.activity_event):
            body['ActivityEvent'] = request.activity_event
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            body['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.classification):
            body['Classification'] = request.classification
        if not UtilClient.is_unset(request.delivery_type):
            body['DeliveryType'] = request.delivery_type
        if not UtilClient.is_unset(request.dismissal_date):
            body['DismissalDate'] = request.dismissal_date
        if not UtilClient.is_unset(request.expired_seconds):
            body['ExpiredSeconds'] = request.expired_seconds
        if not UtilClient.is_unset(request.extended_params):
            body['ExtendedParams'] = request.extended_params
        if not UtilClient.is_unset(request.mi_channel_id):
            body['MiChannelId'] = request.mi_channel_id
        if not UtilClient.is_unset(request.notify_level_shrink):
            body['NotifyLevel'] = request.notify_level_shrink
        if not UtilClient.is_unset(request.notify_type):
            body['NotifyType'] = request.notify_type
        if not UtilClient.is_unset(request.push_action):
            body['PushAction'] = request.push_action
        if not UtilClient.is_unset(request.silent):
            body['Silent'] = request.silent
        if not UtilClient.is_unset(request.strategy_content):
            body['StrategyContent'] = request.strategy_content
        if not UtilClient.is_unset(request.strategy_type):
            body['StrategyType'] = request.strategy_type
        if not UtilClient.is_unset(request.target_msg):
            body['TargetMsg'] = request.target_msg
        if not UtilClient.is_unset(request.task_name):
            body['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.template_name):
            body['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.third_channel_category_shrink):
            body['ThirdChannelCategory'] = request.third_channel_category_shrink
        if not UtilClient.is_unset(request.transparent_message_payload):
            body['TransparentMessagePayload'] = request.transparent_message_payload
        if not UtilClient.is_unset(request.transparent_message_urgency):
            body['TransparentMessageUrgency'] = request.transparent_message_urgency
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PushMultiple',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.PushMultipleResponse(),
            self.call_api(params, req, runtime)
        )

    async def push_multiple_with_options_async(
        self,
        tmp_req: m_paa_s20201028_models.PushMultipleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.PushMultipleResponse:
        """
        @param tmp_req: PushMultipleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PushMultipleResponse
        """
        UtilClient.validate_model(tmp_req)
        request = m_paa_s20201028_models.PushMultipleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.notify_level):
            request.notify_level_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notify_level, 'NotifyLevel', 'json')
        if not UtilClient.is_unset(tmp_req.third_channel_category):
            request.third_channel_category_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.third_channel_category, 'ThirdChannelCategory', 'json')
        body = {}
        if not UtilClient.is_unset(request.activity_content_state):
            body['ActivityContentState'] = request.activity_content_state
        if not UtilClient.is_unset(request.activity_event):
            body['ActivityEvent'] = request.activity_event
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            body['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.classification):
            body['Classification'] = request.classification
        if not UtilClient.is_unset(request.delivery_type):
            body['DeliveryType'] = request.delivery_type
        if not UtilClient.is_unset(request.dismissal_date):
            body['DismissalDate'] = request.dismissal_date
        if not UtilClient.is_unset(request.expired_seconds):
            body['ExpiredSeconds'] = request.expired_seconds
        if not UtilClient.is_unset(request.extended_params):
            body['ExtendedParams'] = request.extended_params
        if not UtilClient.is_unset(request.mi_channel_id):
            body['MiChannelId'] = request.mi_channel_id
        if not UtilClient.is_unset(request.notify_level_shrink):
            body['NotifyLevel'] = request.notify_level_shrink
        if not UtilClient.is_unset(request.notify_type):
            body['NotifyType'] = request.notify_type
        if not UtilClient.is_unset(request.push_action):
            body['PushAction'] = request.push_action
        if not UtilClient.is_unset(request.silent):
            body['Silent'] = request.silent
        if not UtilClient.is_unset(request.strategy_content):
            body['StrategyContent'] = request.strategy_content
        if not UtilClient.is_unset(request.strategy_type):
            body['StrategyType'] = request.strategy_type
        if not UtilClient.is_unset(request.target_msg):
            body['TargetMsg'] = request.target_msg
        if not UtilClient.is_unset(request.task_name):
            body['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.template_name):
            body['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.third_channel_category_shrink):
            body['ThirdChannelCategory'] = request.third_channel_category_shrink
        if not UtilClient.is_unset(request.transparent_message_payload):
            body['TransparentMessagePayload'] = request.transparent_message_payload
        if not UtilClient.is_unset(request.transparent_message_urgency):
            body['TransparentMessageUrgency'] = request.transparent_message_urgency
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PushMultiple',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.PushMultipleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def push_multiple(
        self,
        request: m_paa_s20201028_models.PushMultipleRequest,
    ) -> m_paa_s20201028_models.PushMultipleResponse:
        """
        @param request: PushMultipleRequest
        @return: PushMultipleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.push_multiple_with_options(request, runtime)

    async def push_multiple_async(
        self,
        request: m_paa_s20201028_models.PushMultipleRequest,
    ) -> m_paa_s20201028_models.PushMultipleResponse:
        """
        @param request: PushMultipleRequest
        @return: PushMultipleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.push_multiple_with_options_async(request, runtime)

    def push_query_device_state_with_options(
        self,
        request: m_paa_s20201028_models.PushQueryDeviceStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.PushQueryDeviceStateResponse:
        """
        @summary 查询设备状态信息
        
        @param request: PushQueryDeviceStateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PushQueryDeviceStateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.target):
            body['Target'] = request.target
        if not UtilClient.is_unset(request.target_type):
            body['TargetType'] = request.target_type
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PushQueryDeviceState',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.PushQueryDeviceStateResponse(),
            self.call_api(params, req, runtime)
        )

    async def push_query_device_state_with_options_async(
        self,
        request: m_paa_s20201028_models.PushQueryDeviceStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.PushQueryDeviceStateResponse:
        """
        @summary 查询设备状态信息
        
        @param request: PushQueryDeviceStateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PushQueryDeviceStateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.target):
            body['Target'] = request.target
        if not UtilClient.is_unset(request.target_type):
            body['TargetType'] = request.target_type
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PushQueryDeviceState',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.PushQueryDeviceStateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def push_query_device_state(
        self,
        request: m_paa_s20201028_models.PushQueryDeviceStateRequest,
    ) -> m_paa_s20201028_models.PushQueryDeviceStateResponse:
        """
        @summary 查询设备状态信息
        
        @param request: PushQueryDeviceStateRequest
        @return: PushQueryDeviceStateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.push_query_device_state_with_options(request, runtime)

    async def push_query_device_state_async(
        self,
        request: m_paa_s20201028_models.PushQueryDeviceStateRequest,
    ) -> m_paa_s20201028_models.PushQueryDeviceStateResponse:
        """
        @summary 查询设备状态信息
        
        @param request: PushQueryDeviceStateRequest
        @return: PushQueryDeviceStateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.push_query_device_state_with_options_async(request, runtime)

    def push_report_with_options(
        self,
        request: m_paa_s20201028_models.PushReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.PushReportResponse:
        """
        @param request: PushReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PushReportResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_version):
            body['AppVersion'] = request.app_version
        if not UtilClient.is_unset(request.channel):
            body['Channel'] = request.channel
        if not UtilClient.is_unset(request.connect_type):
            body['ConnectType'] = request.connect_type
        if not UtilClient.is_unset(request.delivery_token):
            body['DeliveryToken'] = request.delivery_token
        if not UtilClient.is_unset(request.imei):
            body['Imei'] = request.imei
        if not UtilClient.is_unset(request.imsi):
            body['Imsi'] = request.imsi
        if not UtilClient.is_unset(request.model):
            body['Model'] = request.model
        if not UtilClient.is_unset(request.os_type):
            body['OsType'] = request.os_type
        if not UtilClient.is_unset(request.push_version):
            body['PushVersion'] = request.push_version
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.third_channel):
            body['ThirdChannel'] = request.third_channel
        if not UtilClient.is_unset(request.third_channel_device_token):
            body['ThirdChannelDeviceToken'] = request.third_channel_device_token
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PushReport',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.PushReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def push_report_with_options_async(
        self,
        request: m_paa_s20201028_models.PushReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.PushReportResponse:
        """
        @param request: PushReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PushReportResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_version):
            body['AppVersion'] = request.app_version
        if not UtilClient.is_unset(request.channel):
            body['Channel'] = request.channel
        if not UtilClient.is_unset(request.connect_type):
            body['ConnectType'] = request.connect_type
        if not UtilClient.is_unset(request.delivery_token):
            body['DeliveryToken'] = request.delivery_token
        if not UtilClient.is_unset(request.imei):
            body['Imei'] = request.imei
        if not UtilClient.is_unset(request.imsi):
            body['Imsi'] = request.imsi
        if not UtilClient.is_unset(request.model):
            body['Model'] = request.model
        if not UtilClient.is_unset(request.os_type):
            body['OsType'] = request.os_type
        if not UtilClient.is_unset(request.push_version):
            body['PushVersion'] = request.push_version
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.third_channel):
            body['ThirdChannel'] = request.third_channel
        if not UtilClient.is_unset(request.third_channel_device_token):
            body['ThirdChannelDeviceToken'] = request.third_channel_device_token
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PushReport',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.PushReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def push_report(
        self,
        request: m_paa_s20201028_models.PushReportRequest,
    ) -> m_paa_s20201028_models.PushReportResponse:
        """
        @param request: PushReportRequest
        @return: PushReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.push_report_with_options(request, runtime)

    async def push_report_async(
        self,
        request: m_paa_s20201028_models.PushReportRequest,
    ) -> m_paa_s20201028_models.PushReportResponse:
        """
        @param request: PushReportRequest
        @return: PushReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.push_report_with_options_async(request, runtime)

    def push_simple_with_options(
        self,
        tmp_req: m_paa_s20201028_models.PushSimpleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.PushSimpleResponse:
        """
        @summary 极简推送
        
        @param tmp_req: PushSimpleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PushSimpleResponse
        """
        UtilClient.validate_model(tmp_req)
        request = m_paa_s20201028_models.PushSimpleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.notify_level):
            request.notify_level_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notify_level, 'NotifyLevel', 'json')
        if not UtilClient.is_unset(tmp_req.third_channel_category):
            request.third_channel_category_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.third_channel_category, 'ThirdChannelCategory', 'json')
        body = {}
        if not UtilClient.is_unset(request.activity_content_state):
            body['ActivityContentState'] = request.activity_content_state
        if not UtilClient.is_unset(request.activity_event):
            body['ActivityEvent'] = request.activity_event
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            body['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.classification):
            body['Classification'] = request.classification
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.delivery_type):
            body['DeliveryType'] = request.delivery_type
        if not UtilClient.is_unset(request.dismissal_date):
            body['DismissalDate'] = request.dismissal_date
        if not UtilClient.is_unset(request.expired_seconds):
            body['ExpiredSeconds'] = request.expired_seconds
        if not UtilClient.is_unset(request.extended_params):
            body['ExtendedParams'] = request.extended_params
        if not UtilClient.is_unset(request.icon_urls):
            body['IconUrls'] = request.icon_urls
        if not UtilClient.is_unset(request.image_urls):
            body['ImageUrls'] = request.image_urls
        if not UtilClient.is_unset(request.mi_channel_id):
            body['MiChannelId'] = request.mi_channel_id
        if not UtilClient.is_unset(request.notify_level_shrink):
            body['NotifyLevel'] = request.notify_level_shrink
        if not UtilClient.is_unset(request.notify_type):
            body['NotifyType'] = request.notify_type
        if not UtilClient.is_unset(request.push_action):
            body['PushAction'] = request.push_action
        if not UtilClient.is_unset(request.push_style):
            body['PushStyle'] = request.push_style
        if not UtilClient.is_unset(request.silent):
            body['Silent'] = request.silent
        if not UtilClient.is_unset(request.sms_sign_name):
            body['SmsSignName'] = request.sms_sign_name
        if not UtilClient.is_unset(request.sms_strategy):
            body['SmsStrategy'] = request.sms_strategy
        if not UtilClient.is_unset(request.sms_template_code):
            body['SmsTemplateCode'] = request.sms_template_code
        if not UtilClient.is_unset(request.sms_template_param):
            body['SmsTemplateParam'] = request.sms_template_param
        if not UtilClient.is_unset(request.strategy_content):
            body['StrategyContent'] = request.strategy_content
        if not UtilClient.is_unset(request.strategy_type):
            body['StrategyType'] = request.strategy_type
        if not UtilClient.is_unset(request.target_msgkey):
            body['TargetMsgkey'] = request.target_msgkey
        if not UtilClient.is_unset(request.task_name):
            body['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.third_channel_category_shrink):
            body['ThirdChannelCategory'] = request.third_channel_category_shrink
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        if not UtilClient.is_unset(request.transparent_message_payload):
            body['TransparentMessagePayload'] = request.transparent_message_payload
        if not UtilClient.is_unset(request.transparent_message_urgency):
            body['TransparentMessageUrgency'] = request.transparent_message_urgency
        if not UtilClient.is_unset(request.uri):
            body['Uri'] = request.uri
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PushSimple',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.PushSimpleResponse(),
            self.call_api(params, req, runtime)
        )

    async def push_simple_with_options_async(
        self,
        tmp_req: m_paa_s20201028_models.PushSimpleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.PushSimpleResponse:
        """
        @summary 极简推送
        
        @param tmp_req: PushSimpleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PushSimpleResponse
        """
        UtilClient.validate_model(tmp_req)
        request = m_paa_s20201028_models.PushSimpleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.notify_level):
            request.notify_level_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notify_level, 'NotifyLevel', 'json')
        if not UtilClient.is_unset(tmp_req.third_channel_category):
            request.third_channel_category_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.third_channel_category, 'ThirdChannelCategory', 'json')
        body = {}
        if not UtilClient.is_unset(request.activity_content_state):
            body['ActivityContentState'] = request.activity_content_state
        if not UtilClient.is_unset(request.activity_event):
            body['ActivityEvent'] = request.activity_event
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            body['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.classification):
            body['Classification'] = request.classification
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.delivery_type):
            body['DeliveryType'] = request.delivery_type
        if not UtilClient.is_unset(request.dismissal_date):
            body['DismissalDate'] = request.dismissal_date
        if not UtilClient.is_unset(request.expired_seconds):
            body['ExpiredSeconds'] = request.expired_seconds
        if not UtilClient.is_unset(request.extended_params):
            body['ExtendedParams'] = request.extended_params
        if not UtilClient.is_unset(request.icon_urls):
            body['IconUrls'] = request.icon_urls
        if not UtilClient.is_unset(request.image_urls):
            body['ImageUrls'] = request.image_urls
        if not UtilClient.is_unset(request.mi_channel_id):
            body['MiChannelId'] = request.mi_channel_id
        if not UtilClient.is_unset(request.notify_level_shrink):
            body['NotifyLevel'] = request.notify_level_shrink
        if not UtilClient.is_unset(request.notify_type):
            body['NotifyType'] = request.notify_type
        if not UtilClient.is_unset(request.push_action):
            body['PushAction'] = request.push_action
        if not UtilClient.is_unset(request.push_style):
            body['PushStyle'] = request.push_style
        if not UtilClient.is_unset(request.silent):
            body['Silent'] = request.silent
        if not UtilClient.is_unset(request.sms_sign_name):
            body['SmsSignName'] = request.sms_sign_name
        if not UtilClient.is_unset(request.sms_strategy):
            body['SmsStrategy'] = request.sms_strategy
        if not UtilClient.is_unset(request.sms_template_code):
            body['SmsTemplateCode'] = request.sms_template_code
        if not UtilClient.is_unset(request.sms_template_param):
            body['SmsTemplateParam'] = request.sms_template_param
        if not UtilClient.is_unset(request.strategy_content):
            body['StrategyContent'] = request.strategy_content
        if not UtilClient.is_unset(request.strategy_type):
            body['StrategyType'] = request.strategy_type
        if not UtilClient.is_unset(request.target_msgkey):
            body['TargetMsgkey'] = request.target_msgkey
        if not UtilClient.is_unset(request.task_name):
            body['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.third_channel_category_shrink):
            body['ThirdChannelCategory'] = request.third_channel_category_shrink
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        if not UtilClient.is_unset(request.transparent_message_payload):
            body['TransparentMessagePayload'] = request.transparent_message_payload
        if not UtilClient.is_unset(request.transparent_message_urgency):
            body['TransparentMessageUrgency'] = request.transparent_message_urgency
        if not UtilClient.is_unset(request.uri):
            body['Uri'] = request.uri
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PushSimple',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.PushSimpleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def push_simple(
        self,
        request: m_paa_s20201028_models.PushSimpleRequest,
    ) -> m_paa_s20201028_models.PushSimpleResponse:
        """
        @summary 极简推送
        
        @param request: PushSimpleRequest
        @return: PushSimpleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.push_simple_with_options(request, runtime)

    async def push_simple_async(
        self,
        request: m_paa_s20201028_models.PushSimpleRequest,
    ) -> m_paa_s20201028_models.PushSimpleResponse:
        """
        @summary 极简推送
        
        @param request: PushSimpleRequest
        @return: PushSimpleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.push_simple_with_options_async(request, runtime)

    def push_template_with_options(
        self,
        tmp_req: m_paa_s20201028_models.PushTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.PushTemplateResponse:
        """
        @param tmp_req: PushTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PushTemplateResponse
        """
        UtilClient.validate_model(tmp_req)
        request = m_paa_s20201028_models.PushTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.notify_level):
            request.notify_level_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notify_level, 'NotifyLevel', 'json')
        if not UtilClient.is_unset(tmp_req.third_channel_category):
            request.third_channel_category_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.third_channel_category, 'ThirdChannelCategory', 'json')
        body = {}
        if not UtilClient.is_unset(request.activity_content_state):
            body['ActivityContentState'] = request.activity_content_state
        if not UtilClient.is_unset(request.activity_event):
            body['ActivityEvent'] = request.activity_event
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            body['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.classification):
            body['Classification'] = request.classification
        if not UtilClient.is_unset(request.delivery_type):
            body['DeliveryType'] = request.delivery_type
        if not UtilClient.is_unset(request.dismissal_date):
            body['DismissalDate'] = request.dismissal_date
        if not UtilClient.is_unset(request.expired_seconds):
            body['ExpiredSeconds'] = request.expired_seconds
        if not UtilClient.is_unset(request.extended_params):
            body['ExtendedParams'] = request.extended_params
        if not UtilClient.is_unset(request.mi_channel_id):
            body['MiChannelId'] = request.mi_channel_id
        if not UtilClient.is_unset(request.notify_level_shrink):
            body['NotifyLevel'] = request.notify_level_shrink
        if not UtilClient.is_unset(request.notify_type):
            body['NotifyType'] = request.notify_type
        if not UtilClient.is_unset(request.push_action):
            body['PushAction'] = request.push_action
        if not UtilClient.is_unset(request.silent):
            body['Silent'] = request.silent
        if not UtilClient.is_unset(request.sms_sign_name):
            body['SmsSignName'] = request.sms_sign_name
        if not UtilClient.is_unset(request.sms_strategy):
            body['SmsStrategy'] = request.sms_strategy
        if not UtilClient.is_unset(request.sms_template_code):
            body['SmsTemplateCode'] = request.sms_template_code
        if not UtilClient.is_unset(request.sms_template_param):
            body['SmsTemplateParam'] = request.sms_template_param
        if not UtilClient.is_unset(request.strategy_content):
            body['StrategyContent'] = request.strategy_content
        if not UtilClient.is_unset(request.strategy_type):
            body['StrategyType'] = request.strategy_type
        if not UtilClient.is_unset(request.target_msgkey):
            body['TargetMsgkey'] = request.target_msgkey
        if not UtilClient.is_unset(request.task_name):
            body['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.template_key_value):
            body['TemplateKeyValue'] = request.template_key_value
        if not UtilClient.is_unset(request.template_name):
            body['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.third_channel_category_shrink):
            body['ThirdChannelCategory'] = request.third_channel_category_shrink
        if not UtilClient.is_unset(request.transparent_message_payload):
            body['TransparentMessagePayload'] = request.transparent_message_payload
        if not UtilClient.is_unset(request.transparent_message_urgency):
            body['TransparentMessageUrgency'] = request.transparent_message_urgency
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PushTemplate',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.PushTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def push_template_with_options_async(
        self,
        tmp_req: m_paa_s20201028_models.PushTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.PushTemplateResponse:
        """
        @param tmp_req: PushTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PushTemplateResponse
        """
        UtilClient.validate_model(tmp_req)
        request = m_paa_s20201028_models.PushTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.notify_level):
            request.notify_level_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notify_level, 'NotifyLevel', 'json')
        if not UtilClient.is_unset(tmp_req.third_channel_category):
            request.third_channel_category_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.third_channel_category, 'ThirdChannelCategory', 'json')
        body = {}
        if not UtilClient.is_unset(request.activity_content_state):
            body['ActivityContentState'] = request.activity_content_state
        if not UtilClient.is_unset(request.activity_event):
            body['ActivityEvent'] = request.activity_event
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            body['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.classification):
            body['Classification'] = request.classification
        if not UtilClient.is_unset(request.delivery_type):
            body['DeliveryType'] = request.delivery_type
        if not UtilClient.is_unset(request.dismissal_date):
            body['DismissalDate'] = request.dismissal_date
        if not UtilClient.is_unset(request.expired_seconds):
            body['ExpiredSeconds'] = request.expired_seconds
        if not UtilClient.is_unset(request.extended_params):
            body['ExtendedParams'] = request.extended_params
        if not UtilClient.is_unset(request.mi_channel_id):
            body['MiChannelId'] = request.mi_channel_id
        if not UtilClient.is_unset(request.notify_level_shrink):
            body['NotifyLevel'] = request.notify_level_shrink
        if not UtilClient.is_unset(request.notify_type):
            body['NotifyType'] = request.notify_type
        if not UtilClient.is_unset(request.push_action):
            body['PushAction'] = request.push_action
        if not UtilClient.is_unset(request.silent):
            body['Silent'] = request.silent
        if not UtilClient.is_unset(request.sms_sign_name):
            body['SmsSignName'] = request.sms_sign_name
        if not UtilClient.is_unset(request.sms_strategy):
            body['SmsStrategy'] = request.sms_strategy
        if not UtilClient.is_unset(request.sms_template_code):
            body['SmsTemplateCode'] = request.sms_template_code
        if not UtilClient.is_unset(request.sms_template_param):
            body['SmsTemplateParam'] = request.sms_template_param
        if not UtilClient.is_unset(request.strategy_content):
            body['StrategyContent'] = request.strategy_content
        if not UtilClient.is_unset(request.strategy_type):
            body['StrategyType'] = request.strategy_type
        if not UtilClient.is_unset(request.target_msgkey):
            body['TargetMsgkey'] = request.target_msgkey
        if not UtilClient.is_unset(request.task_name):
            body['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.template_key_value):
            body['TemplateKeyValue'] = request.template_key_value
        if not UtilClient.is_unset(request.template_name):
            body['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.third_channel_category_shrink):
            body['ThirdChannelCategory'] = request.third_channel_category_shrink
        if not UtilClient.is_unset(request.transparent_message_payload):
            body['TransparentMessagePayload'] = request.transparent_message_payload
        if not UtilClient.is_unset(request.transparent_message_urgency):
            body['TransparentMessageUrgency'] = request.transparent_message_urgency
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PushTemplate',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.PushTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def push_template(
        self,
        request: m_paa_s20201028_models.PushTemplateRequest,
    ) -> m_paa_s20201028_models.PushTemplateResponse:
        """
        @param request: PushTemplateRequest
        @return: PushTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.push_template_with_options(request, runtime)

    async def push_template_async(
        self,
        request: m_paa_s20201028_models.PushTemplateRequest,
    ) -> m_paa_s20201028_models.PushTemplateResponse:
        """
        @param request: PushTemplateRequest
        @return: PushTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.push_template_with_options_async(request, runtime)

    def push_un_bind_with_options(
        self,
        request: m_paa_s20201028_models.PushUnBindRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.PushUnBindResponse:
        """
        @param request: PushUnBindRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PushUnBindResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.delivery_token):
            body['DeliveryToken'] = request.delivery_token
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PushUnBind',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.PushUnBindResponse(),
            self.call_api(params, req, runtime)
        )

    async def push_un_bind_with_options_async(
        self,
        request: m_paa_s20201028_models.PushUnBindRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.PushUnBindResponse:
        """
        @param request: PushUnBindRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PushUnBindResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.delivery_token):
            body['DeliveryToken'] = request.delivery_token
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PushUnBind',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.PushUnBindResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def push_un_bind(
        self,
        request: m_paa_s20201028_models.PushUnBindRequest,
    ) -> m_paa_s20201028_models.PushUnBindResponse:
        """
        @param request: PushUnBindRequest
        @return: PushUnBindResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.push_un_bind_with_options(request, runtime)

    async def push_un_bind_async(
        self,
        request: m_paa_s20201028_models.PushUnBindRequest,
    ) -> m_paa_s20201028_models.PushUnBindResponse:
        """
        @param request: PushUnBindRequest
        @return: PushUnBindResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.push_un_bind_with_options_async(request, runtime)

    def query_cubecard_filetoken_with_options(
        self,
        request: m_paa_s20201028_models.QueryCubecardFiletokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.QueryCubecardFiletokenResponse:
        """
        @param request: QueryCubecardFiletokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryCubecardFiletokenResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.onex_flag):
            body['OnexFlag'] = request.onex_flag
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryCubecardFiletoken',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.QueryCubecardFiletokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_cubecard_filetoken_with_options_async(
        self,
        request: m_paa_s20201028_models.QueryCubecardFiletokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.QueryCubecardFiletokenResponse:
        """
        @param request: QueryCubecardFiletokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryCubecardFiletokenResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.onex_flag):
            body['OnexFlag'] = request.onex_flag
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryCubecardFiletoken',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.QueryCubecardFiletokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_cubecard_filetoken(
        self,
        request: m_paa_s20201028_models.QueryCubecardFiletokenRequest,
    ) -> m_paa_s20201028_models.QueryCubecardFiletokenResponse:
        """
        @param request: QueryCubecardFiletokenRequest
        @return: QueryCubecardFiletokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_cubecard_filetoken_with_options(request, runtime)

    async def query_cubecard_filetoken_async(
        self,
        request: m_paa_s20201028_models.QueryCubecardFiletokenRequest,
    ) -> m_paa_s20201028_models.QueryCubecardFiletokenResponse:
        """
        @param request: QueryCubecardFiletokenRequest
        @return: QueryCubecardFiletokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_cubecard_filetoken_with_options_async(request, runtime)

    def query_info_from_mdp_with_options(
        self,
        request: m_paa_s20201028_models.QueryInfoFromMdpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.QueryInfoFromMdpResponse:
        """
        @summary 查询Device+服务的
        
        @param request: QueryInfoFromMdpRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryInfoFromMdpResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.mobile):
            body['Mobile'] = request.mobile
        if not UtilClient.is_unset(request.mobile_md_5):
            body['MobileMd5'] = request.mobile_md_5
        if not UtilClient.is_unset(request.mobile_sha_256):
            body['MobileSha256'] = request.mobile_sha_256
        if not UtilClient.is_unset(request.mobile_sm_3):
            body['MobileSm3'] = request.mobile_sm_3
        if not UtilClient.is_unset(request.risk_scene):
            body['RiskScene'] = request.risk_scene
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryInfoFromMdp',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.QueryInfoFromMdpResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_info_from_mdp_with_options_async(
        self,
        request: m_paa_s20201028_models.QueryInfoFromMdpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.QueryInfoFromMdpResponse:
        """
        @summary 查询Device+服务的
        
        @param request: QueryInfoFromMdpRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryInfoFromMdpResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.mobile):
            body['Mobile'] = request.mobile
        if not UtilClient.is_unset(request.mobile_md_5):
            body['MobileMd5'] = request.mobile_md_5
        if not UtilClient.is_unset(request.mobile_sha_256):
            body['MobileSha256'] = request.mobile_sha_256
        if not UtilClient.is_unset(request.mobile_sm_3):
            body['MobileSm3'] = request.mobile_sm_3
        if not UtilClient.is_unset(request.risk_scene):
            body['RiskScene'] = request.risk_scene
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryInfoFromMdp',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.QueryInfoFromMdpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_info_from_mdp(
        self,
        request: m_paa_s20201028_models.QueryInfoFromMdpRequest,
    ) -> m_paa_s20201028_models.QueryInfoFromMdpResponse:
        """
        @summary 查询Device+服务的
        
        @param request: QueryInfoFromMdpRequest
        @return: QueryInfoFromMdpResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_info_from_mdp_with_options(request, runtime)

    async def query_info_from_mdp_async(
        self,
        request: m_paa_s20201028_models.QueryInfoFromMdpRequest,
    ) -> m_paa_s20201028_models.QueryInfoFromMdpResponse:
        """
        @summary 查询Device+服务的
        
        @param request: QueryInfoFromMdpRequest
        @return: QueryInfoFromMdpResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_info_from_mdp_with_options_async(request, runtime)

    def query_link_with_options(
        self,
        request: m_paa_s20201028_models.QueryLinkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.QueryLinkResponse:
        """
        @summary 查询短链
        
        @param request: QueryLinkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryLinkResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.url):
            body['Url'] = request.url
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryLink',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.QueryLinkResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_link_with_options_async(
        self,
        request: m_paa_s20201028_models.QueryLinkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.QueryLinkResponse:
        """
        @summary 查询短链
        
        @param request: QueryLinkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryLinkResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.url):
            body['Url'] = request.url
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryLink',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.QueryLinkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_link(
        self,
        request: m_paa_s20201028_models.QueryLinkRequest,
    ) -> m_paa_s20201028_models.QueryLinkResponse:
        """
        @summary 查询短链
        
        @param request: QueryLinkRequest
        @return: QueryLinkResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_link_with_options(request, runtime)

    async def query_link_async(
        self,
        request: m_paa_s20201028_models.QueryLinkRequest,
    ) -> m_paa_s20201028_models.QueryLinkResponse:
        """
        @summary 查询短链
        
        @param request: QueryLinkRequest
        @return: QueryLinkResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_link_with_options_async(request, runtime)

    def query_mapp_center_app_with_options(
        self,
        request: m_paa_s20201028_models.QueryMappCenterAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.QueryMappCenterAppResponse:
        """
        @param request: QueryMappCenterAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMappCenterAppResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryMappCenterApp',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.QueryMappCenterAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_mapp_center_app_with_options_async(
        self,
        request: m_paa_s20201028_models.QueryMappCenterAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.QueryMappCenterAppResponse:
        """
        @param request: QueryMappCenterAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMappCenterAppResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryMappCenterApp',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.QueryMappCenterAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_mapp_center_app(
        self,
        request: m_paa_s20201028_models.QueryMappCenterAppRequest,
    ) -> m_paa_s20201028_models.QueryMappCenterAppResponse:
        """
        @param request: QueryMappCenterAppRequest
        @return: QueryMappCenterAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_mapp_center_app_with_options(request, runtime)

    async def query_mapp_center_app_async(
        self,
        request: m_paa_s20201028_models.QueryMappCenterAppRequest,
    ) -> m_paa_s20201028_models.QueryMappCenterAppResponse:
        """
        @param request: QueryMappCenterAppRequest
        @return: QueryMappCenterAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_mapp_center_app_with_options_async(request, runtime)

    def query_mcdp_aim_with_options(
        self,
        request: m_paa_s20201028_models.QueryMcdpAimRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.QueryMcdpAimResponse:
        """
        @param request: QueryMcdpAimRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMcdpAimResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryMcdpAim',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.QueryMcdpAimResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_mcdp_aim_with_options_async(
        self,
        request: m_paa_s20201028_models.QueryMcdpAimRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.QueryMcdpAimResponse:
        """
        @param request: QueryMcdpAimRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMcdpAimResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryMcdpAim',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.QueryMcdpAimResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_mcdp_aim(
        self,
        request: m_paa_s20201028_models.QueryMcdpAimRequest,
    ) -> m_paa_s20201028_models.QueryMcdpAimResponse:
        """
        @param request: QueryMcdpAimRequest
        @return: QueryMcdpAimResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_mcdp_aim_with_options(request, runtime)

    async def query_mcdp_aim_async(
        self,
        request: m_paa_s20201028_models.QueryMcdpAimRequest,
    ) -> m_paa_s20201028_models.QueryMcdpAimResponse:
        """
        @param request: QueryMcdpAimRequest
        @return: QueryMcdpAimResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_mcdp_aim_with_options_async(request, runtime)

    def query_mcdp_zone_with_options(
        self,
        request: m_paa_s20201028_models.QueryMcdpZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.QueryMcdpZoneResponse:
        """
        @param request: QueryMcdpZoneRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMcdpZoneResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryMcdpZone',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.QueryMcdpZoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_mcdp_zone_with_options_async(
        self,
        request: m_paa_s20201028_models.QueryMcdpZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.QueryMcdpZoneResponse:
        """
        @param request: QueryMcdpZoneRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMcdpZoneResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryMcdpZone',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.QueryMcdpZoneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_mcdp_zone(
        self,
        request: m_paa_s20201028_models.QueryMcdpZoneRequest,
    ) -> m_paa_s20201028_models.QueryMcdpZoneResponse:
        """
        @param request: QueryMcdpZoneRequest
        @return: QueryMcdpZoneResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_mcdp_zone_with_options(request, runtime)

    async def query_mcdp_zone_async(
        self,
        request: m_paa_s20201028_models.QueryMcdpZoneRequest,
    ) -> m_paa_s20201028_models.QueryMcdpZoneResponse:
        """
        @param request: QueryMcdpZoneRequest
        @return: QueryMcdpZoneResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_mcdp_zone_with_options_async(request, runtime)

    def query_mcube_mini_package_with_options(
        self,
        request: m_paa_s20201028_models.QueryMcubeMiniPackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.QueryMcubeMiniPackageResponse:
        """
        @param request: QueryMcubeMiniPackageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMcubeMiniPackageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.h_5id):
            body['H5Id'] = request.h_5id
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryMcubeMiniPackage',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.QueryMcubeMiniPackageResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_mcube_mini_package_with_options_async(
        self,
        request: m_paa_s20201028_models.QueryMcubeMiniPackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.QueryMcubeMiniPackageResponse:
        """
        @param request: QueryMcubeMiniPackageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMcubeMiniPackageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.h_5id):
            body['H5Id'] = request.h_5id
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryMcubeMiniPackage',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.QueryMcubeMiniPackageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_mcube_mini_package(
        self,
        request: m_paa_s20201028_models.QueryMcubeMiniPackageRequest,
    ) -> m_paa_s20201028_models.QueryMcubeMiniPackageResponse:
        """
        @param request: QueryMcubeMiniPackageRequest
        @return: QueryMcubeMiniPackageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_mcube_mini_package_with_options(request, runtime)

    async def query_mcube_mini_package_async(
        self,
        request: m_paa_s20201028_models.QueryMcubeMiniPackageRequest,
    ) -> m_paa_s20201028_models.QueryMcubeMiniPackageResponse:
        """
        @param request: QueryMcubeMiniPackageRequest
        @return: QueryMcubeMiniPackageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_mcube_mini_package_with_options_async(request, runtime)

    def query_mcube_mini_task_with_options(
        self,
        request: m_paa_s20201028_models.QueryMcubeMiniTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.QueryMcubeMiniTaskResponse:
        """
        @param request: QueryMcubeMiniTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMcubeMiniTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryMcubeMiniTask',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.QueryMcubeMiniTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_mcube_mini_task_with_options_async(
        self,
        request: m_paa_s20201028_models.QueryMcubeMiniTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.QueryMcubeMiniTaskResponse:
        """
        @param request: QueryMcubeMiniTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMcubeMiniTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryMcubeMiniTask',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.QueryMcubeMiniTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_mcube_mini_task(
        self,
        request: m_paa_s20201028_models.QueryMcubeMiniTaskRequest,
    ) -> m_paa_s20201028_models.QueryMcubeMiniTaskResponse:
        """
        @param request: QueryMcubeMiniTaskRequest
        @return: QueryMcubeMiniTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_mcube_mini_task_with_options(request, runtime)

    async def query_mcube_mini_task_async(
        self,
        request: m_paa_s20201028_models.QueryMcubeMiniTaskRequest,
    ) -> m_paa_s20201028_models.QueryMcubeMiniTaskResponse:
        """
        @param request: QueryMcubeMiniTaskRequest
        @return: QueryMcubeMiniTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_mcube_mini_task_with_options_async(request, runtime)

    def query_mcube_vhost_with_options(
        self,
        request: m_paa_s20201028_models.QueryMcubeVhostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.QueryMcubeVhostResponse:
        """
        @param request: QueryMcubeVhostRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMcubeVhostResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryMcubeVhost',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.QueryMcubeVhostResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_mcube_vhost_with_options_async(
        self,
        request: m_paa_s20201028_models.QueryMcubeVhostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.QueryMcubeVhostResponse:
        """
        @param request: QueryMcubeVhostRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMcubeVhostResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryMcubeVhost',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.QueryMcubeVhostResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_mcube_vhost(
        self,
        request: m_paa_s20201028_models.QueryMcubeVhostRequest,
    ) -> m_paa_s20201028_models.QueryMcubeVhostResponse:
        """
        @param request: QueryMcubeVhostRequest
        @return: QueryMcubeVhostResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_mcube_vhost_with_options(request, runtime)

    async def query_mcube_vhost_async(
        self,
        request: m_paa_s20201028_models.QueryMcubeVhostRequest,
    ) -> m_paa_s20201028_models.QueryMcubeVhostResponse:
        """
        @param request: QueryMcubeVhostRequest
        @return: QueryMcubeVhostResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_mcube_vhost_with_options_async(request, runtime)

    def query_mds_upgrade_task_detail_with_options(
        self,
        request: m_paa_s20201028_models.QueryMdsUpgradeTaskDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.QueryMdsUpgradeTaskDetailResponse:
        """
        @param request: QueryMdsUpgradeTaskDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMdsUpgradeTaskDetailResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryMdsUpgradeTaskDetail',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.QueryMdsUpgradeTaskDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_mds_upgrade_task_detail_with_options_async(
        self,
        request: m_paa_s20201028_models.QueryMdsUpgradeTaskDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.QueryMdsUpgradeTaskDetailResponse:
        """
        @param request: QueryMdsUpgradeTaskDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMdsUpgradeTaskDetailResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryMdsUpgradeTaskDetail',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.QueryMdsUpgradeTaskDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_mds_upgrade_task_detail(
        self,
        request: m_paa_s20201028_models.QueryMdsUpgradeTaskDetailRequest,
    ) -> m_paa_s20201028_models.QueryMdsUpgradeTaskDetailResponse:
        """
        @param request: QueryMdsUpgradeTaskDetailRequest
        @return: QueryMdsUpgradeTaskDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_mds_upgrade_task_detail_with_options(request, runtime)

    async def query_mds_upgrade_task_detail_async(
        self,
        request: m_paa_s20201028_models.QueryMdsUpgradeTaskDetailRequest,
    ) -> m_paa_s20201028_models.QueryMdsUpgradeTaskDetailResponse:
        """
        @param request: QueryMdsUpgradeTaskDetailRequest
        @return: QueryMdsUpgradeTaskDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_mds_upgrade_task_detail_with_options_async(request, runtime)

    def query_mgs_apipage_with_options(
        self,
        request: m_paa_s20201028_models.QueryMgsApipageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.QueryMgsApipageResponse:
        """
        @param request: QueryMgsApipageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMgsApipageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.api_status):
            body['ApiStatus'] = request.api_status
        if not UtilClient.is_unset(request.api_type):
            body['ApiType'] = request.api_type
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.format):
            body['Format'] = request.format
        if not UtilClient.is_unset(request.host):
            body['Host'] = request.host
        if not UtilClient.is_unset(request.need_encrypt):
            body['NeedEncrypt'] = request.need_encrypt
        if not UtilClient.is_unset(request.need_etag):
            body['NeedEtag'] = request.need_etag
        if not UtilClient.is_unset(request.need_sign):
            body['NeedSign'] = request.need_sign
        if not UtilClient.is_unset(request.operation_type):
            body['OperationType'] = request.operation_type
        if not UtilClient.is_unset(request.opt_fuzzy):
            body['OptFuzzy'] = request.opt_fuzzy
        if not UtilClient.is_unset(request.page_index):
            body['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sys_id):
            body['SysId'] = request.sys_id
        if not UtilClient.is_unset(request.sys_name):
            body['SysName'] = request.sys_name
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryMgsApipage',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.QueryMgsApipageResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_mgs_apipage_with_options_async(
        self,
        request: m_paa_s20201028_models.QueryMgsApipageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.QueryMgsApipageResponse:
        """
        @param request: QueryMgsApipageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMgsApipageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.api_status):
            body['ApiStatus'] = request.api_status
        if not UtilClient.is_unset(request.api_type):
            body['ApiType'] = request.api_type
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.format):
            body['Format'] = request.format
        if not UtilClient.is_unset(request.host):
            body['Host'] = request.host
        if not UtilClient.is_unset(request.need_encrypt):
            body['NeedEncrypt'] = request.need_encrypt
        if not UtilClient.is_unset(request.need_etag):
            body['NeedEtag'] = request.need_etag
        if not UtilClient.is_unset(request.need_sign):
            body['NeedSign'] = request.need_sign
        if not UtilClient.is_unset(request.operation_type):
            body['OperationType'] = request.operation_type
        if not UtilClient.is_unset(request.opt_fuzzy):
            body['OptFuzzy'] = request.opt_fuzzy
        if not UtilClient.is_unset(request.page_index):
            body['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sys_id):
            body['SysId'] = request.sys_id
        if not UtilClient.is_unset(request.sys_name):
            body['SysName'] = request.sys_name
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryMgsApipage',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.QueryMgsApipageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_mgs_apipage(
        self,
        request: m_paa_s20201028_models.QueryMgsApipageRequest,
    ) -> m_paa_s20201028_models.QueryMgsApipageResponse:
        """
        @param request: QueryMgsApipageRequest
        @return: QueryMgsApipageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_mgs_apipage_with_options(request, runtime)

    async def query_mgs_apipage_async(
        self,
        request: m_paa_s20201028_models.QueryMgsApipageRequest,
    ) -> m_paa_s20201028_models.QueryMgsApipageResponse:
        """
        @param request: QueryMgsApipageRequest
        @return: QueryMgsApipageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_mgs_apipage_with_options_async(request, runtime)

    def query_mgs_apirest_with_options(
        self,
        request: m_paa_s20201028_models.QueryMgsApirestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.QueryMgsApirestResponse:
        """
        @param request: QueryMgsApirestRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMgsApirestResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.format):
            body['Format'] = request.format
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryMgsApirest',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.QueryMgsApirestResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_mgs_apirest_with_options_async(
        self,
        request: m_paa_s20201028_models.QueryMgsApirestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.QueryMgsApirestResponse:
        """
        @param request: QueryMgsApirestRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMgsApirestResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.format):
            body['Format'] = request.format
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryMgsApirest',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.QueryMgsApirestResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_mgs_apirest(
        self,
        request: m_paa_s20201028_models.QueryMgsApirestRequest,
    ) -> m_paa_s20201028_models.QueryMgsApirestResponse:
        """
        @param request: QueryMgsApirestRequest
        @return: QueryMgsApirestResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_mgs_apirest_with_options(request, runtime)

    async def query_mgs_apirest_async(
        self,
        request: m_paa_s20201028_models.QueryMgsApirestRequest,
    ) -> m_paa_s20201028_models.QueryMgsApirestResponse:
        """
        @param request: QueryMgsApirestRequest
        @return: QueryMgsApirestResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_mgs_apirest_with_options_async(request, runtime)

    def query_mgs_testreqbodyautogen_with_options(
        self,
        request: m_paa_s20201028_models.QueryMgsTestreqbodyautogenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.QueryMgsTestreqbodyautogenResponse:
        """
        @param request: QueryMgsTestreqbodyautogenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMgsTestreqbodyautogenResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.format):
            body['Format'] = request.format
        if not UtilClient.is_unset(request.mpaas_mappcenter_mgs_testreqbodyautogen_query_json_str):
            body['MpaasMappcenterMgsTestreqbodyautogenQueryJsonStr'] = request.mpaas_mappcenter_mgs_testreqbodyautogen_query_json_str
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryMgsTestreqbodyautogen',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.QueryMgsTestreqbodyautogenResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_mgs_testreqbodyautogen_with_options_async(
        self,
        request: m_paa_s20201028_models.QueryMgsTestreqbodyautogenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.QueryMgsTestreqbodyautogenResponse:
        """
        @param request: QueryMgsTestreqbodyautogenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMgsTestreqbodyautogenResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.format):
            body['Format'] = request.format
        if not UtilClient.is_unset(request.mpaas_mappcenter_mgs_testreqbodyautogen_query_json_str):
            body['MpaasMappcenterMgsTestreqbodyautogenQueryJsonStr'] = request.mpaas_mappcenter_mgs_testreqbodyautogen_query_json_str
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryMgsTestreqbodyautogen',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.QueryMgsTestreqbodyautogenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_mgs_testreqbodyautogen(
        self,
        request: m_paa_s20201028_models.QueryMgsTestreqbodyautogenRequest,
    ) -> m_paa_s20201028_models.QueryMgsTestreqbodyautogenResponse:
        """
        @param request: QueryMgsTestreqbodyautogenRequest
        @return: QueryMgsTestreqbodyautogenResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_mgs_testreqbodyautogen_with_options(request, runtime)

    async def query_mgs_testreqbodyautogen_async(
        self,
        request: m_paa_s20201028_models.QueryMgsTestreqbodyautogenRequest,
    ) -> m_paa_s20201028_models.QueryMgsTestreqbodyautogenResponse:
        """
        @param request: QueryMgsTestreqbodyautogenRequest
        @return: QueryMgsTestreqbodyautogenResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_mgs_testreqbodyautogen_with_options_async(request, runtime)

    def query_mps_scheduler_list_with_options(
        self,
        request: m_paa_s20201028_models.QueryMpsSchedulerListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.QueryMpsSchedulerListResponse:
        """
        @param request: QueryMpsSchedulerListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMpsSchedulerListResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.unique_id):
            body['UniqueId'] = request.unique_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryMpsSchedulerList',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.QueryMpsSchedulerListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_mps_scheduler_list_with_options_async(
        self,
        request: m_paa_s20201028_models.QueryMpsSchedulerListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.QueryMpsSchedulerListResponse:
        """
        @param request: QueryMpsSchedulerListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMpsSchedulerListResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.unique_id):
            body['UniqueId'] = request.unique_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryMpsSchedulerList',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.QueryMpsSchedulerListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_mps_scheduler_list(
        self,
        request: m_paa_s20201028_models.QueryMpsSchedulerListRequest,
    ) -> m_paa_s20201028_models.QueryMpsSchedulerListResponse:
        """
        @param request: QueryMpsSchedulerListRequest
        @return: QueryMpsSchedulerListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_mps_scheduler_list_with_options(request, runtime)

    async def query_mps_scheduler_list_async(
        self,
        request: m_paa_s20201028_models.QueryMpsSchedulerListRequest,
    ) -> m_paa_s20201028_models.QueryMpsSchedulerListResponse:
        """
        @param request: QueryMpsSchedulerListRequest
        @return: QueryMpsSchedulerListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_mps_scheduler_list_with_options_async(request, runtime)

    def query_push_analysis_core_index_with_options(
        self,
        request: m_paa_s20201028_models.QueryPushAnalysisCoreIndexRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.QueryPushAnalysisCoreIndexResponse:
        """
        @param request: QueryPushAnalysisCoreIndexRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryPushAnalysisCoreIndexResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel):
            body['Channel'] = request.channel
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.platform):
            body['Platform'] = request.platform
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryPushAnalysisCoreIndex',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.QueryPushAnalysisCoreIndexResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_push_analysis_core_index_with_options_async(
        self,
        request: m_paa_s20201028_models.QueryPushAnalysisCoreIndexRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.QueryPushAnalysisCoreIndexResponse:
        """
        @param request: QueryPushAnalysisCoreIndexRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryPushAnalysisCoreIndexResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel):
            body['Channel'] = request.channel
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.platform):
            body['Platform'] = request.platform
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryPushAnalysisCoreIndex',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.QueryPushAnalysisCoreIndexResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_push_analysis_core_index(
        self,
        request: m_paa_s20201028_models.QueryPushAnalysisCoreIndexRequest,
    ) -> m_paa_s20201028_models.QueryPushAnalysisCoreIndexResponse:
        """
        @param request: QueryPushAnalysisCoreIndexRequest
        @return: QueryPushAnalysisCoreIndexResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_push_analysis_core_index_with_options(request, runtime)

    async def query_push_analysis_core_index_async(
        self,
        request: m_paa_s20201028_models.QueryPushAnalysisCoreIndexRequest,
    ) -> m_paa_s20201028_models.QueryPushAnalysisCoreIndexResponse:
        """
        @param request: QueryPushAnalysisCoreIndexRequest
        @return: QueryPushAnalysisCoreIndexResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_push_analysis_core_index_with_options_async(request, runtime)

    def query_push_analysis_task_detail_with_options(
        self,
        request: m_paa_s20201028_models.QueryPushAnalysisTaskDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.QueryPushAnalysisTaskDetailResponse:
        """
        @param request: QueryPushAnalysisTaskDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryPushAnalysisTaskDetailResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryPushAnalysisTaskDetail',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.QueryPushAnalysisTaskDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_push_analysis_task_detail_with_options_async(
        self,
        request: m_paa_s20201028_models.QueryPushAnalysisTaskDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.QueryPushAnalysisTaskDetailResponse:
        """
        @param request: QueryPushAnalysisTaskDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryPushAnalysisTaskDetailResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryPushAnalysisTaskDetail',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.QueryPushAnalysisTaskDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_push_analysis_task_detail(
        self,
        request: m_paa_s20201028_models.QueryPushAnalysisTaskDetailRequest,
    ) -> m_paa_s20201028_models.QueryPushAnalysisTaskDetailResponse:
        """
        @param request: QueryPushAnalysisTaskDetailRequest
        @return: QueryPushAnalysisTaskDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_push_analysis_task_detail_with_options(request, runtime)

    async def query_push_analysis_task_detail_async(
        self,
        request: m_paa_s20201028_models.QueryPushAnalysisTaskDetailRequest,
    ) -> m_paa_s20201028_models.QueryPushAnalysisTaskDetailResponse:
        """
        @param request: QueryPushAnalysisTaskDetailRequest
        @return: QueryPushAnalysisTaskDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_push_analysis_task_detail_with_options_async(request, runtime)

    def query_push_analysis_task_list_with_options(
        self,
        request: m_paa_s20201028_models.QueryPushAnalysisTaskListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.QueryPushAnalysisTaskListResponse:
        """
        @param request: QueryPushAnalysisTaskListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryPushAnalysisTaskListResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_name):
            body['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryPushAnalysisTaskList',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.QueryPushAnalysisTaskListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_push_analysis_task_list_with_options_async(
        self,
        request: m_paa_s20201028_models.QueryPushAnalysisTaskListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.QueryPushAnalysisTaskListResponse:
        """
        @param request: QueryPushAnalysisTaskListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryPushAnalysisTaskListResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_name):
            body['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryPushAnalysisTaskList',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.QueryPushAnalysisTaskListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_push_analysis_task_list(
        self,
        request: m_paa_s20201028_models.QueryPushAnalysisTaskListRequest,
    ) -> m_paa_s20201028_models.QueryPushAnalysisTaskListResponse:
        """
        @param request: QueryPushAnalysisTaskListRequest
        @return: QueryPushAnalysisTaskListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_push_analysis_task_list_with_options(request, runtime)

    async def query_push_analysis_task_list_async(
        self,
        request: m_paa_s20201028_models.QueryPushAnalysisTaskListRequest,
    ) -> m_paa_s20201028_models.QueryPushAnalysisTaskListResponse:
        """
        @param request: QueryPushAnalysisTaskListRequest
        @return: QueryPushAnalysisTaskListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_push_analysis_task_list_with_options_async(request, runtime)

    def query_push_scheduler_list_with_options(
        self,
        request: m_paa_s20201028_models.QueryPushSchedulerListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.QueryPushSchedulerListResponse:
        """
        @param request: QueryPushSchedulerListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryPushSchedulerListResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.unique_id):
            body['UniqueId'] = request.unique_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryPushSchedulerList',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.QueryPushSchedulerListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_push_scheduler_list_with_options_async(
        self,
        request: m_paa_s20201028_models.QueryPushSchedulerListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.QueryPushSchedulerListResponse:
        """
        @param request: QueryPushSchedulerListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryPushSchedulerListResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.unique_id):
            body['UniqueId'] = request.unique_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryPushSchedulerList',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.QueryPushSchedulerListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_push_scheduler_list(
        self,
        request: m_paa_s20201028_models.QueryPushSchedulerListRequest,
    ) -> m_paa_s20201028_models.QueryPushSchedulerListResponse:
        """
        @param request: QueryPushSchedulerListRequest
        @return: QueryPushSchedulerListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_push_scheduler_list_with_options(request, runtime)

    async def query_push_scheduler_list_async(
        self,
        request: m_paa_s20201028_models.QueryPushSchedulerListRequest,
    ) -> m_paa_s20201028_models.QueryPushSchedulerListResponse:
        """
        @param request: QueryPushSchedulerListRequest
        @return: QueryPushSchedulerListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_push_scheduler_list_with_options_async(request, runtime)

    def revoke_push_message_with_options(
        self,
        request: m_paa_s20201028_models.RevokePushMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.RevokePushMessageResponse:
        """
        @param request: RevokePushMessageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RevokePushMessageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.message_id):
            body['MessageId'] = request.message_id
        if not UtilClient.is_unset(request.target_id):
            body['TargetId'] = request.target_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RevokePushMessage',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.RevokePushMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def revoke_push_message_with_options_async(
        self,
        request: m_paa_s20201028_models.RevokePushMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.RevokePushMessageResponse:
        """
        @param request: RevokePushMessageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RevokePushMessageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.message_id):
            body['MessageId'] = request.message_id
        if not UtilClient.is_unset(request.target_id):
            body['TargetId'] = request.target_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RevokePushMessage',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.RevokePushMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revoke_push_message(
        self,
        request: m_paa_s20201028_models.RevokePushMessageRequest,
    ) -> m_paa_s20201028_models.RevokePushMessageResponse:
        """
        @param request: RevokePushMessageRequest
        @return: RevokePushMessageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.revoke_push_message_with_options(request, runtime)

    async def revoke_push_message_async(
        self,
        request: m_paa_s20201028_models.RevokePushMessageRequest,
    ) -> m_paa_s20201028_models.RevokePushMessageResponse:
        """
        @param request: RevokePushMessageRequest
        @return: RevokePushMessageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.revoke_push_message_with_options_async(request, runtime)

    def revoke_push_task_with_options(
        self,
        request: m_paa_s20201028_models.RevokePushTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.RevokePushTaskResponse:
        """
        @param request: RevokePushTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RevokePushTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RevokePushTask',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.RevokePushTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def revoke_push_task_with_options_async(
        self,
        request: m_paa_s20201028_models.RevokePushTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.RevokePushTaskResponse:
        """
        @param request: RevokePushTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RevokePushTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RevokePushTask',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.RevokePushTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revoke_push_task(
        self,
        request: m_paa_s20201028_models.RevokePushTaskRequest,
    ) -> m_paa_s20201028_models.RevokePushTaskResponse:
        """
        @param request: RevokePushTaskRequest
        @return: RevokePushTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.revoke_push_task_with_options(request, runtime)

    async def revoke_push_task_async(
        self,
        request: m_paa_s20201028_models.RevokePushTaskRequest,
    ) -> m_paa_s20201028_models.RevokePushTaskResponse:
        """
        @param request: RevokePushTaskRequest
        @return: RevokePushTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.revoke_push_task_with_options_async(request, runtime)

    def run_msa_diff_with_options(
        self,
        request: m_paa_s20201028_models.RunMsaDiffRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.RunMsaDiffResponse:
        """
        @param request: RunMsaDiffRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunMsaDiffResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.mpaas_mappcenter_msa_diff_run_json_str):
            body['MpaasMappcenterMsaDiffRunJsonStr'] = request.mpaas_mappcenter_msa_diff_run_json_str
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunMsaDiff',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.RunMsaDiffResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_msa_diff_with_options_async(
        self,
        request: m_paa_s20201028_models.RunMsaDiffRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.RunMsaDiffResponse:
        """
        @param request: RunMsaDiffRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunMsaDiffResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.mpaas_mappcenter_msa_diff_run_json_str):
            body['MpaasMappcenterMsaDiffRunJsonStr'] = request.mpaas_mappcenter_msa_diff_run_json_str
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunMsaDiff',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.RunMsaDiffResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_msa_diff(
        self,
        request: m_paa_s20201028_models.RunMsaDiffRequest,
    ) -> m_paa_s20201028_models.RunMsaDiffResponse:
        """
        @param request: RunMsaDiffRequest
        @return: RunMsaDiffResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.run_msa_diff_with_options(request, runtime)

    async def run_msa_diff_async(
        self,
        request: m_paa_s20201028_models.RunMsaDiffRequest,
    ) -> m_paa_s20201028_models.RunMsaDiffResponse:
        """
        @param request: RunMsaDiffRequest
        @return: RunMsaDiffResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.run_msa_diff_with_options_async(request, runtime)

    def save_mgs_apirest_with_options(
        self,
        request: m_paa_s20201028_models.SaveMgsApirestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.SaveMgsApirestResponse:
        """
        @param request: SaveMgsApirestRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveMgsApirestResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.mpaas_mappcenter_mgs_apirest_save_json_str):
            body['MpaasMappcenterMgsApirestSaveJsonStr'] = request.mpaas_mappcenter_mgs_apirest_save_json_str
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SaveMgsApirest',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.SaveMgsApirestResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_mgs_apirest_with_options_async(
        self,
        request: m_paa_s20201028_models.SaveMgsApirestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.SaveMgsApirestResponse:
        """
        @param request: SaveMgsApirestRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveMgsApirestResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.mpaas_mappcenter_mgs_apirest_save_json_str):
            body['MpaasMappcenterMgsApirestSaveJsonStr'] = request.mpaas_mappcenter_mgs_apirest_save_json_str
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SaveMgsApirest',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.SaveMgsApirestResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_mgs_apirest(
        self,
        request: m_paa_s20201028_models.SaveMgsApirestRequest,
    ) -> m_paa_s20201028_models.SaveMgsApirestResponse:
        """
        @param request: SaveMgsApirestRequest
        @return: SaveMgsApirestResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_mgs_apirest_with_options(request, runtime)

    async def save_mgs_apirest_async(
        self,
        request: m_paa_s20201028_models.SaveMgsApirestRequest,
    ) -> m_paa_s20201028_models.SaveMgsApirestResponse:
        """
        @param request: SaveMgsApirestRequest
        @return: SaveMgsApirestResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_mgs_apirest_with_options_async(request, runtime)

    def start_user_app_async_enhance_in_msa_with_options(
        self,
        request: m_paa_s20201028_models.StartUserAppAsyncEnhanceInMsaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.StartUserAppAsyncEnhanceInMsaResponse:
        """
        @param request: StartUserAppAsyncEnhanceInMsaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartUserAppAsyncEnhanceInMsaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_shield_config):
            query['NewShieldConfig'] = request.new_shield_config
        body = {}
        if not UtilClient.is_unset(request.apk_protector):
            body['ApkProtector'] = request.apk_protector
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.assets_file_list):
            body['AssetsFileList'] = request.assets_file_list
        if not UtilClient.is_unset(request.classes):
            body['Classes'] = request.classes
        if not UtilClient.is_unset(request.dalvik_debugger):
            body['DalvikDebugger'] = request.dalvik_debugger
        if not UtilClient.is_unset(request.emulator_environment):
            body['EmulatorEnvironment'] = request.emulator_environment
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.java_hook):
            body['JavaHook'] = request.java_hook
        if not UtilClient.is_unset(request.memory_dump):
            body['MemoryDump'] = request.memory_dump
        if not UtilClient.is_unset(request.native_debugger):
            body['NativeDebugger'] = request.native_debugger
        if not UtilClient.is_unset(request.native_hook):
            body['NativeHook'] = request.native_hook
        if not UtilClient.is_unset(request.package_tampered):
            body['PackageTampered'] = request.package_tampered
        if not UtilClient.is_unset(request.root):
            body['Root'] = request.root
        if not UtilClient.is_unset(request.run_mode):
            body['RunMode'] = request.run_mode
        if not UtilClient.is_unset(request.so_file_list):
            body['SoFileList'] = request.so_file_list
        if not UtilClient.is_unset(request.task_type):
            body['TaskType'] = request.task_type
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.total_switch):
            body['TotalSwitch'] = request.total_switch
        if not UtilClient.is_unset(request.use_ashield):
            body['UseAShield'] = request.use_ashield
        if not UtilClient.is_unset(request.use_yshield):
            body['UseYShield'] = request.use_yshield
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartUserAppAsyncEnhanceInMsa',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.StartUserAppAsyncEnhanceInMsaResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_user_app_async_enhance_in_msa_with_options_async(
        self,
        request: m_paa_s20201028_models.StartUserAppAsyncEnhanceInMsaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.StartUserAppAsyncEnhanceInMsaResponse:
        """
        @param request: StartUserAppAsyncEnhanceInMsaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartUserAppAsyncEnhanceInMsaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_shield_config):
            query['NewShieldConfig'] = request.new_shield_config
        body = {}
        if not UtilClient.is_unset(request.apk_protector):
            body['ApkProtector'] = request.apk_protector
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.assets_file_list):
            body['AssetsFileList'] = request.assets_file_list
        if not UtilClient.is_unset(request.classes):
            body['Classes'] = request.classes
        if not UtilClient.is_unset(request.dalvik_debugger):
            body['DalvikDebugger'] = request.dalvik_debugger
        if not UtilClient.is_unset(request.emulator_environment):
            body['EmulatorEnvironment'] = request.emulator_environment
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.java_hook):
            body['JavaHook'] = request.java_hook
        if not UtilClient.is_unset(request.memory_dump):
            body['MemoryDump'] = request.memory_dump
        if not UtilClient.is_unset(request.native_debugger):
            body['NativeDebugger'] = request.native_debugger
        if not UtilClient.is_unset(request.native_hook):
            body['NativeHook'] = request.native_hook
        if not UtilClient.is_unset(request.package_tampered):
            body['PackageTampered'] = request.package_tampered
        if not UtilClient.is_unset(request.root):
            body['Root'] = request.root
        if not UtilClient.is_unset(request.run_mode):
            body['RunMode'] = request.run_mode
        if not UtilClient.is_unset(request.so_file_list):
            body['SoFileList'] = request.so_file_list
        if not UtilClient.is_unset(request.task_type):
            body['TaskType'] = request.task_type
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.total_switch):
            body['TotalSwitch'] = request.total_switch
        if not UtilClient.is_unset(request.use_ashield):
            body['UseAShield'] = request.use_ashield
        if not UtilClient.is_unset(request.use_yshield):
            body['UseYShield'] = request.use_yshield
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartUserAppAsyncEnhanceInMsa',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.StartUserAppAsyncEnhanceInMsaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_user_app_async_enhance_in_msa(
        self,
        request: m_paa_s20201028_models.StartUserAppAsyncEnhanceInMsaRequest,
    ) -> m_paa_s20201028_models.StartUserAppAsyncEnhanceInMsaResponse:
        """
        @param request: StartUserAppAsyncEnhanceInMsaRequest
        @return: StartUserAppAsyncEnhanceInMsaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_user_app_async_enhance_in_msa_with_options(request, runtime)

    async def start_user_app_async_enhance_in_msa_async(
        self,
        request: m_paa_s20201028_models.StartUserAppAsyncEnhanceInMsaRequest,
    ) -> m_paa_s20201028_models.StartUserAppAsyncEnhanceInMsaResponse:
        """
        @param request: StartUserAppAsyncEnhanceInMsaRequest
        @return: StartUserAppAsyncEnhanceInMsaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_user_app_async_enhance_in_msa_with_options_async(request, runtime)

    def update_link_with_options(
        self,
        request: m_paa_s20201028_models.UpdateLinkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.UpdateLinkResponse:
        """
        @summary 更新短链
        
        @param request: UpdateLinkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateLinkResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.cors):
            body['Cors'] = request.cors
        if not UtilClient.is_unset(request.domain):
            body['Domain'] = request.domain
        if not UtilClient.is_unset(request.dynamicfield):
            body['Dynamicfield'] = request.dynamicfield
        if not UtilClient.is_unset(request.target_url):
            body['TargetUrl'] = request.target_url
        if not UtilClient.is_unset(request.url):
            body['Url'] = request.url
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLink',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.UpdateLinkResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_link_with_options_async(
        self,
        request: m_paa_s20201028_models.UpdateLinkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.UpdateLinkResponse:
        """
        @summary 更新短链
        
        @param request: UpdateLinkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateLinkResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.cors):
            body['Cors'] = request.cors
        if not UtilClient.is_unset(request.domain):
            body['Domain'] = request.domain
        if not UtilClient.is_unset(request.dynamicfield):
            body['Dynamicfield'] = request.dynamicfield
        if not UtilClient.is_unset(request.target_url):
            body['TargetUrl'] = request.target_url
        if not UtilClient.is_unset(request.url):
            body['Url'] = request.url
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLink',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.UpdateLinkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_link(
        self,
        request: m_paa_s20201028_models.UpdateLinkRequest,
    ) -> m_paa_s20201028_models.UpdateLinkResponse:
        """
        @summary 更新短链
        
        @param request: UpdateLinkRequest
        @return: UpdateLinkResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_link_with_options(request, runtime)

    async def update_link_async(
        self,
        request: m_paa_s20201028_models.UpdateLinkRequest,
    ) -> m_paa_s20201028_models.UpdateLinkResponse:
        """
        @summary 更新短链
        
        @param request: UpdateLinkRequest
        @return: UpdateLinkResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_link_with_options_async(request, runtime)

    def update_mcube_whitelist_with_options(
        self,
        request: m_paa_s20201028_models.UpdateMcubeWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.UpdateMcubeWhitelistResponse:
        """
        @param request: UpdateMcubeWhitelistRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateMcubeWhitelistResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.key_ids):
            body['KeyIds'] = request.key_ids
        if not UtilClient.is_unset(request.onex_flag):
            body['OnexFlag'] = request.onex_flag
        if not UtilClient.is_unset(request.oss_url):
            body['OssUrl'] = request.oss_url
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateMcubeWhitelist',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.UpdateMcubeWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_mcube_whitelist_with_options_async(
        self,
        request: m_paa_s20201028_models.UpdateMcubeWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.UpdateMcubeWhitelistResponse:
        """
        @param request: UpdateMcubeWhitelistRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateMcubeWhitelistResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.key_ids):
            body['KeyIds'] = request.key_ids
        if not UtilClient.is_unset(request.onex_flag):
            body['OnexFlag'] = request.onex_flag
        if not UtilClient.is_unset(request.oss_url):
            body['OssUrl'] = request.oss_url
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateMcubeWhitelist',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.UpdateMcubeWhitelistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_mcube_whitelist(
        self,
        request: m_paa_s20201028_models.UpdateMcubeWhitelistRequest,
    ) -> m_paa_s20201028_models.UpdateMcubeWhitelistResponse:
        """
        @param request: UpdateMcubeWhitelistRequest
        @return: UpdateMcubeWhitelistResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_mcube_whitelist_with_options(request, runtime)

    async def update_mcube_whitelist_async(
        self,
        request: m_paa_s20201028_models.UpdateMcubeWhitelistRequest,
    ) -> m_paa_s20201028_models.UpdateMcubeWhitelistResponse:
        """
        @param request: UpdateMcubeWhitelistRequest
        @return: UpdateMcubeWhitelistResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_mcube_whitelist_with_options_async(request, runtime)

    def update_mds_cube_resource_with_options(
        self,
        request: m_paa_s20201028_models.UpdateMdsCubeResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.UpdateMdsCubeResourceResponse:
        """
        @param request: UpdateMdsCubeResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateMdsCubeResourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.mock_data_url):
            body['MockDataUrl'] = request.mock_data_url
        if not UtilClient.is_unset(request.onex_flag):
            body['OnexFlag'] = request.onex_flag
        if not UtilClient.is_unset(request.template_resource_id):
            body['TemplateResourceId'] = request.template_resource_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateMdsCubeResource',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.UpdateMdsCubeResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_mds_cube_resource_with_options_async(
        self,
        request: m_paa_s20201028_models.UpdateMdsCubeResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.UpdateMdsCubeResourceResponse:
        """
        @param request: UpdateMdsCubeResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateMdsCubeResourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.mock_data_url):
            body['MockDataUrl'] = request.mock_data_url
        if not UtilClient.is_unset(request.onex_flag):
            body['OnexFlag'] = request.onex_flag
        if not UtilClient.is_unset(request.template_resource_id):
            body['TemplateResourceId'] = request.template_resource_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateMdsCubeResource',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.UpdateMdsCubeResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_mds_cube_resource(
        self,
        request: m_paa_s20201028_models.UpdateMdsCubeResourceRequest,
    ) -> m_paa_s20201028_models.UpdateMdsCubeResourceResponse:
        """
        @param request: UpdateMdsCubeResourceRequest
        @return: UpdateMdsCubeResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_mds_cube_resource_with_options(request, runtime)

    async def update_mds_cube_resource_async(
        self,
        request: m_paa_s20201028_models.UpdateMdsCubeResourceRequest,
    ) -> m_paa_s20201028_models.UpdateMdsCubeResourceResponse:
        """
        @param request: UpdateMdsCubeResourceRequest
        @return: UpdateMdsCubeResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_mds_cube_resource_with_options_async(request, runtime)

    def update_mpaas_app_info_with_options(
        self,
        request: m_paa_s20201028_models.UpdateMpaasAppInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.UpdateMpaasAppInfoResponse:
        """
        @param request: UpdateMpaasAppInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateMpaasAppInfoResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.icon_file_url):
            body['IconFileUrl'] = request.icon_file_url
        if not UtilClient.is_unset(request.identifier):
            body['Identifier'] = request.identifier
        if not UtilClient.is_unset(request.onex_flag):
            body['OnexFlag'] = request.onex_flag
        if not UtilClient.is_unset(request.system_type):
            body['SystemType'] = request.system_type
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateMpaasAppInfo',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.UpdateMpaasAppInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_mpaas_app_info_with_options_async(
        self,
        request: m_paa_s20201028_models.UpdateMpaasAppInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.UpdateMpaasAppInfoResponse:
        """
        @param request: UpdateMpaasAppInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateMpaasAppInfoResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.icon_file_url):
            body['IconFileUrl'] = request.icon_file_url
        if not UtilClient.is_unset(request.identifier):
            body['Identifier'] = request.identifier
        if not UtilClient.is_unset(request.onex_flag):
            body['OnexFlag'] = request.onex_flag
        if not UtilClient.is_unset(request.system_type):
            body['SystemType'] = request.system_type
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateMpaasAppInfo',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.UpdateMpaasAppInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_mpaas_app_info(
        self,
        request: m_paa_s20201028_models.UpdateMpaasAppInfoRequest,
    ) -> m_paa_s20201028_models.UpdateMpaasAppInfoResponse:
        """
        @param request: UpdateMpaasAppInfoRequest
        @return: UpdateMpaasAppInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_mpaas_app_info_with_options(request, runtime)

    async def update_mpaas_app_info_async(
        self,
        request: m_paa_s20201028_models.UpdateMpaasAppInfoRequest,
    ) -> m_paa_s20201028_models.UpdateMpaasAppInfoResponse:
        """
        @param request: UpdateMpaasAppInfoRequest
        @return: UpdateMpaasAppInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_mpaas_app_info_with_options_async(request, runtime)

    def upload_bitcode_to_msa_with_options(
        self,
        request: m_paa_s20201028_models.UploadBitcodeToMsaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.UploadBitcodeToMsaResponse:
        """
        @summary 上传字节码到msa进行加固
        
        @param request: UploadBitcodeToMsaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UploadBitcodeToMsaResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.bitcode):
            body['Bitcode'] = request.bitcode
        if not UtilClient.is_unset(request.code_version):
            body['CodeVersion'] = request.code_version
        if not UtilClient.is_unset(request.license):
            body['License'] = request.license
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UploadBitcodeToMsa',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.UploadBitcodeToMsaResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_bitcode_to_msa_with_options_async(
        self,
        request: m_paa_s20201028_models.UploadBitcodeToMsaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.UploadBitcodeToMsaResponse:
        """
        @summary 上传字节码到msa进行加固
        
        @param request: UploadBitcodeToMsaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UploadBitcodeToMsaResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.bitcode):
            body['Bitcode'] = request.bitcode
        if not UtilClient.is_unset(request.code_version):
            body['CodeVersion'] = request.code_version
        if not UtilClient.is_unset(request.license):
            body['License'] = request.license
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UploadBitcodeToMsa',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.UploadBitcodeToMsaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_bitcode_to_msa(
        self,
        request: m_paa_s20201028_models.UploadBitcodeToMsaRequest,
    ) -> m_paa_s20201028_models.UploadBitcodeToMsaResponse:
        """
        @summary 上传字节码到msa进行加固
        
        @param request: UploadBitcodeToMsaRequest
        @return: UploadBitcodeToMsaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upload_bitcode_to_msa_with_options(request, runtime)

    async def upload_bitcode_to_msa_async(
        self,
        request: m_paa_s20201028_models.UploadBitcodeToMsaRequest,
    ) -> m_paa_s20201028_models.UploadBitcodeToMsaResponse:
        """
        @summary 上传字节码到msa进行加固
        
        @param request: UploadBitcodeToMsaRequest
        @return: UploadBitcodeToMsaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.upload_bitcode_to_msa_with_options_async(request, runtime)

    def upload_mcube_mini_package_with_options(
        self,
        request: m_paa_s20201028_models.UploadMcubeMiniPackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.UploadMcubeMiniPackageResponse:
        """
        @param request: UploadMcubeMiniPackageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UploadMcubeMiniPackageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.auto_install):
            body['AutoInstall'] = request.auto_install
        if not UtilClient.is_unset(request.client_version_max):
            body['ClientVersionMax'] = request.client_version_max
        if not UtilClient.is_unset(request.client_version_min):
            body['ClientVersionMin'] = request.client_version_min
        if not UtilClient.is_unset(request.enable_keep_alive):
            body['EnableKeepAlive'] = request.enable_keep_alive
        if not UtilClient.is_unset(request.enable_option_menu):
            body['EnableOptionMenu'] = request.enable_option_menu
        if not UtilClient.is_unset(request.enable_tab_bar):
            body['EnableTabBar'] = request.enable_tab_bar
        if not UtilClient.is_unset(request.extend_info):
            body['ExtendInfo'] = request.extend_info
        if not UtilClient.is_unset(request.h_5id):
            body['H5Id'] = request.h_5id
        if not UtilClient.is_unset(request.h_5name):
            body['H5Name'] = request.h_5name
        if not UtilClient.is_unset(request.h_5version):
            body['H5Version'] = request.h_5version
        if not UtilClient.is_unset(request.icon_file_url):
            body['IconFileUrl'] = request.icon_file_url
        if not UtilClient.is_unset(request.icon_url):
            body['IconUrl'] = request.icon_url
        if not UtilClient.is_unset(request.install_type):
            body['InstallType'] = request.install_type
        if not UtilClient.is_unset(request.main_url):
            body['MainUrl'] = request.main_url
        if not UtilClient.is_unset(request.onex_flag):
            body['OnexFlag'] = request.onex_flag
        if not UtilClient.is_unset(request.package_type):
            body['PackageType'] = request.package_type
        if not UtilClient.is_unset(request.platform):
            body['Platform'] = request.platform
        if not UtilClient.is_unset(request.resource_file_url):
            body['ResourceFileUrl'] = request.resource_file_url
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        if not UtilClient.is_unset(request.uuid):
            body['Uuid'] = request.uuid
        if not UtilClient.is_unset(request.vhost):
            body['Vhost'] = request.vhost
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UploadMcubeMiniPackage',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.UploadMcubeMiniPackageResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_mcube_mini_package_with_options_async(
        self,
        request: m_paa_s20201028_models.UploadMcubeMiniPackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.UploadMcubeMiniPackageResponse:
        """
        @param request: UploadMcubeMiniPackageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UploadMcubeMiniPackageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.auto_install):
            body['AutoInstall'] = request.auto_install
        if not UtilClient.is_unset(request.client_version_max):
            body['ClientVersionMax'] = request.client_version_max
        if not UtilClient.is_unset(request.client_version_min):
            body['ClientVersionMin'] = request.client_version_min
        if not UtilClient.is_unset(request.enable_keep_alive):
            body['EnableKeepAlive'] = request.enable_keep_alive
        if not UtilClient.is_unset(request.enable_option_menu):
            body['EnableOptionMenu'] = request.enable_option_menu
        if not UtilClient.is_unset(request.enable_tab_bar):
            body['EnableTabBar'] = request.enable_tab_bar
        if not UtilClient.is_unset(request.extend_info):
            body['ExtendInfo'] = request.extend_info
        if not UtilClient.is_unset(request.h_5id):
            body['H5Id'] = request.h_5id
        if not UtilClient.is_unset(request.h_5name):
            body['H5Name'] = request.h_5name
        if not UtilClient.is_unset(request.h_5version):
            body['H5Version'] = request.h_5version
        if not UtilClient.is_unset(request.icon_file_url):
            body['IconFileUrl'] = request.icon_file_url
        if not UtilClient.is_unset(request.icon_url):
            body['IconUrl'] = request.icon_url
        if not UtilClient.is_unset(request.install_type):
            body['InstallType'] = request.install_type
        if not UtilClient.is_unset(request.main_url):
            body['MainUrl'] = request.main_url
        if not UtilClient.is_unset(request.onex_flag):
            body['OnexFlag'] = request.onex_flag
        if not UtilClient.is_unset(request.package_type):
            body['PackageType'] = request.package_type
        if not UtilClient.is_unset(request.platform):
            body['Platform'] = request.platform
        if not UtilClient.is_unset(request.resource_file_url):
            body['ResourceFileUrl'] = request.resource_file_url
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        if not UtilClient.is_unset(request.uuid):
            body['Uuid'] = request.uuid
        if not UtilClient.is_unset(request.vhost):
            body['Vhost'] = request.vhost
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UploadMcubeMiniPackage',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.UploadMcubeMiniPackageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_mcube_mini_package(
        self,
        request: m_paa_s20201028_models.UploadMcubeMiniPackageRequest,
    ) -> m_paa_s20201028_models.UploadMcubeMiniPackageResponse:
        """
        @param request: UploadMcubeMiniPackageRequest
        @return: UploadMcubeMiniPackageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upload_mcube_mini_package_with_options(request, runtime)

    async def upload_mcube_mini_package_async(
        self,
        request: m_paa_s20201028_models.UploadMcubeMiniPackageRequest,
    ) -> m_paa_s20201028_models.UploadMcubeMiniPackageResponse:
        """
        @param request: UploadMcubeMiniPackageRequest
        @return: UploadMcubeMiniPackageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.upload_mcube_mini_package_with_options_async(request, runtime)

    def upload_mcube_rsa_key_with_options(
        self,
        request: m_paa_s20201028_models.UploadMcubeRsaKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.UploadMcubeRsaKeyResponse:
        """
        @param request: UploadMcubeRsaKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UploadMcubeRsaKeyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.file_url):
            body['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.onex_flag):
            body['OnexFlag'] = request.onex_flag
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UploadMcubeRsaKey',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.UploadMcubeRsaKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_mcube_rsa_key_with_options_async(
        self,
        request: m_paa_s20201028_models.UploadMcubeRsaKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.UploadMcubeRsaKeyResponse:
        """
        @param request: UploadMcubeRsaKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UploadMcubeRsaKeyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.file_url):
            body['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.onex_flag):
            body['OnexFlag'] = request.onex_flag
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UploadMcubeRsaKey',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.UploadMcubeRsaKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_mcube_rsa_key(
        self,
        request: m_paa_s20201028_models.UploadMcubeRsaKeyRequest,
    ) -> m_paa_s20201028_models.UploadMcubeRsaKeyResponse:
        """
        @param request: UploadMcubeRsaKeyRequest
        @return: UploadMcubeRsaKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upload_mcube_rsa_key_with_options(request, runtime)

    async def upload_mcube_rsa_key_async(
        self,
        request: m_paa_s20201028_models.UploadMcubeRsaKeyRequest,
    ) -> m_paa_s20201028_models.UploadMcubeRsaKeyResponse:
        """
        @param request: UploadMcubeRsaKeyRequest
        @return: UploadMcubeRsaKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.upload_mcube_rsa_key_with_options_async(request, runtime)

    def upload_user_app_to_msa_with_options(
        self,
        request: m_paa_s20201028_models.UploadUserAppToMsaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.UploadUserAppToMsaResponse:
        """
        @param request: UploadUserAppToMsaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UploadUserAppToMsaResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.file_name):
            body['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_url):
            body['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.use_yshield):
            body['UseYShield'] = request.use_yshield
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UploadUserAppToMsa',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.UploadUserAppToMsaResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_user_app_to_msa_with_options_async(
        self,
        request: m_paa_s20201028_models.UploadUserAppToMsaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> m_paa_s20201028_models.UploadUserAppToMsaResponse:
        """
        @param request: UploadUserAppToMsaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UploadUserAppToMsaResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.file_name):
            body['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_url):
            body['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.use_yshield):
            body['UseYShield'] = request.use_yshield
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UploadUserAppToMsa',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.UploadUserAppToMsaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_user_app_to_msa(
        self,
        request: m_paa_s20201028_models.UploadUserAppToMsaRequest,
    ) -> m_paa_s20201028_models.UploadUserAppToMsaResponse:
        """
        @param request: UploadUserAppToMsaRequest
        @return: UploadUserAppToMsaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upload_user_app_to_msa_with_options(request, runtime)

    async def upload_user_app_to_msa_async(
        self,
        request: m_paa_s20201028_models.UploadUserAppToMsaRequest,
    ) -> m_paa_s20201028_models.UploadUserAppToMsaResponse:
        """
        @param request: UploadUserAppToMsaRequest
        @return: UploadUserAppToMsaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.upload_user_app_to_msa_with_options_async(request, runtime)
