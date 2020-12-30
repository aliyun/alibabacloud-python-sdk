# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dbs20190306 import models as dbs_20190306_models
from alibabacloud_tea_util import models as util_models


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
            'cn-qingdao': 'dbs-api.cn-hangzhou.aliyuncs.com',
            'cn-beijing': 'dbs-api.cn-hangzhou.aliyuncs.com',
            'cn-chengdu': 'dbs-api.cn-chengdu.aliyuncs.com',
            'cn-zhangjiakou': 'dbs-api.cn-hangzhou.aliyuncs.com',
            'cn-huhehaote': 'dbs-api.cn-huhehaote.aliyuncs.com',
            'cn-hangzhou': 'dbs-api.cn-hangzhou.aliyuncs.com',
            'cn-shanghai': 'dbs-api.cn-hangzhou.aliyuncs.com',
            'cn-shenzhen': 'dbs-api.cn-hangzhou.aliyuncs.com',
            'cn-hongkong': 'dbs-api.cn-hangzhou.aliyuncs.com',
            'ap-southeast-1': 'dbs-api.ap-southeast-1.aliyuncs.com',
            'ap-southeast-2': 'dbs-api.ap-southeast-2.aliyuncs.com',
            'ap-southeast-3': 'dbs-api.ap-southeast-3.aliyuncs.com',
            'ap-southeast-5': 'dbs-api.ap-southeast-5.aliyuncs.com',
            'ap-northeast-1': 'dbs-api.ap-northeast-1.aliyuncs.com',
            'us-west-1': 'dbs-api.cn-hangzhou.aliyuncs.com',
            'us-east-1': 'dbs-api.cn-hangzhou.aliyuncs.com',
            'eu-central-1': 'dbs-api.eu-central-1.aliyuncs.com',
            'cn-hangzhou-finance': 'dbs-api.cn-hangzhou.aliyuncs.com',
            'cn-shanghai-finance-1': 'dbs-api.cn-hangzhou.aliyuncs.com',
            'cn-shenzhen-finance-1': 'dbs-api.cn-hangzhou.aliyuncs.com',
            'ap-south-1': 'dbs-api.ap-south-1.aliyuncs.com',
            'eu-west-1': 'dbs-api.eu-west-1.aliyuncs.com',
            'me-east-1': 'dbs-api.me-east-1.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('dbs', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def configure_backup_plan_with_options(
        self,
        request: dbs_20190306_models.ConfigureBackupPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.ConfigureBackupPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dbs_20190306_models.ConfigureBackupPlanResponse().from_map(
            self.do_rpcrequest('ConfigureBackupPlan', '2019-03-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def configure_backup_plan_with_options_async(
        self,
        request: dbs_20190306_models.ConfigureBackupPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.ConfigureBackupPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dbs_20190306_models.ConfigureBackupPlanResponse().from_map(
            await self.do_rpcrequest_async('ConfigureBackupPlan', '2019-03-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def configure_backup_plan(
        self,
        request: dbs_20190306_models.ConfigureBackupPlanRequest,
    ) -> dbs_20190306_models.ConfigureBackupPlanResponse:
        runtime = util_models.RuntimeOptions()
        return self.configure_backup_plan_with_options(request, runtime)

    async def configure_backup_plan_async(
        self,
        request: dbs_20190306_models.ConfigureBackupPlanRequest,
    ) -> dbs_20190306_models.ConfigureBackupPlanResponse:
        runtime = util_models.RuntimeOptions()
        return await self.configure_backup_plan_with_options_async(request, runtime)

    def create_backup_plan_with_options(
        self,
        request: dbs_20190306_models.CreateBackupPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.CreateBackupPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dbs_20190306_models.CreateBackupPlanResponse().from_map(
            self.do_rpcrequest('CreateBackupPlan', '2019-03-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_backup_plan_with_options_async(
        self,
        request: dbs_20190306_models.CreateBackupPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.CreateBackupPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dbs_20190306_models.CreateBackupPlanResponse().from_map(
            await self.do_rpcrequest_async('CreateBackupPlan', '2019-03-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_backup_plan(
        self,
        request: dbs_20190306_models.CreateBackupPlanRequest,
    ) -> dbs_20190306_models.CreateBackupPlanResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_backup_plan_with_options(request, runtime)

    async def create_backup_plan_async(
        self,
        request: dbs_20190306_models.CreateBackupPlanRequest,
    ) -> dbs_20190306_models.CreateBackupPlanResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_backup_plan_with_options_async(request, runtime)

    def create_full_backup_set_download_with_options(
        self,
        request: dbs_20190306_models.CreateFullBackupSetDownloadRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.CreateFullBackupSetDownloadResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dbs_20190306_models.CreateFullBackupSetDownloadResponse().from_map(
            self.do_rpcrequest('CreateFullBackupSetDownload', '2019-03-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_full_backup_set_download_with_options_async(
        self,
        request: dbs_20190306_models.CreateFullBackupSetDownloadRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.CreateFullBackupSetDownloadResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dbs_20190306_models.CreateFullBackupSetDownloadResponse().from_map(
            await self.do_rpcrequest_async('CreateFullBackupSetDownload', '2019-03-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_full_backup_set_download(
        self,
        request: dbs_20190306_models.CreateFullBackupSetDownloadRequest,
    ) -> dbs_20190306_models.CreateFullBackupSetDownloadResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_full_backup_set_download_with_options(request, runtime)

    async def create_full_backup_set_download_async(
        self,
        request: dbs_20190306_models.CreateFullBackupSetDownloadRequest,
    ) -> dbs_20190306_models.CreateFullBackupSetDownloadResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_full_backup_set_download_with_options_async(request, runtime)

    def create_get_dblist_from_agent_task_with_options(
        self,
        request: dbs_20190306_models.CreateGetDBListFromAgentTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.CreateGetDBListFromAgentTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dbs_20190306_models.CreateGetDBListFromAgentTaskResponse().from_map(
            self.do_rpcrequest('CreateGetDBListFromAgentTask', '2019-03-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_get_dblist_from_agent_task_with_options_async(
        self,
        request: dbs_20190306_models.CreateGetDBListFromAgentTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.CreateGetDBListFromAgentTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dbs_20190306_models.CreateGetDBListFromAgentTaskResponse().from_map(
            await self.do_rpcrequest_async('CreateGetDBListFromAgentTask', '2019-03-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_get_dblist_from_agent_task(
        self,
        request: dbs_20190306_models.CreateGetDBListFromAgentTaskRequest,
    ) -> dbs_20190306_models.CreateGetDBListFromAgentTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_get_dblist_from_agent_task_with_options(request, runtime)

    async def create_get_dblist_from_agent_task_async(
        self,
        request: dbs_20190306_models.CreateGetDBListFromAgentTaskRequest,
    ) -> dbs_20190306_models.CreateGetDBListFromAgentTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_get_dblist_from_agent_task_with_options_async(request, runtime)

    def create_increment_backup_set_download_with_options(
        self,
        request: dbs_20190306_models.CreateIncrementBackupSetDownloadRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.CreateIncrementBackupSetDownloadResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dbs_20190306_models.CreateIncrementBackupSetDownloadResponse().from_map(
            self.do_rpcrequest('CreateIncrementBackupSetDownload', '2019-03-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_increment_backup_set_download_with_options_async(
        self,
        request: dbs_20190306_models.CreateIncrementBackupSetDownloadRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.CreateIncrementBackupSetDownloadResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dbs_20190306_models.CreateIncrementBackupSetDownloadResponse().from_map(
            await self.do_rpcrequest_async('CreateIncrementBackupSetDownload', '2019-03-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_increment_backup_set_download(
        self,
        request: dbs_20190306_models.CreateIncrementBackupSetDownloadRequest,
    ) -> dbs_20190306_models.CreateIncrementBackupSetDownloadResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_increment_backup_set_download_with_options(request, runtime)

    async def create_increment_backup_set_download_async(
        self,
        request: dbs_20190306_models.CreateIncrementBackupSetDownloadRequest,
    ) -> dbs_20190306_models.CreateIncrementBackupSetDownloadResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_increment_backup_set_download_with_options_async(request, runtime)

    def create_restore_task_with_options(
        self,
        request: dbs_20190306_models.CreateRestoreTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.CreateRestoreTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dbs_20190306_models.CreateRestoreTaskResponse().from_map(
            self.do_rpcrequest('CreateRestoreTask', '2019-03-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_restore_task_with_options_async(
        self,
        request: dbs_20190306_models.CreateRestoreTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.CreateRestoreTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dbs_20190306_models.CreateRestoreTaskResponse().from_map(
            await self.do_rpcrequest_async('CreateRestoreTask', '2019-03-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_restore_task(
        self,
        request: dbs_20190306_models.CreateRestoreTaskRequest,
    ) -> dbs_20190306_models.CreateRestoreTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_restore_task_with_options(request, runtime)

    async def create_restore_task_async(
        self,
        request: dbs_20190306_models.CreateRestoreTaskRequest,
    ) -> dbs_20190306_models.CreateRestoreTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_restore_task_with_options_async(request, runtime)

    def describe_backup_gateway_list_with_options(
        self,
        request: dbs_20190306_models.DescribeBackupGatewayListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.DescribeBackupGatewayListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dbs_20190306_models.DescribeBackupGatewayListResponse().from_map(
            self.do_rpcrequest('DescribeBackupGatewayList', '2019-03-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_backup_gateway_list_with_options_async(
        self,
        request: dbs_20190306_models.DescribeBackupGatewayListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.DescribeBackupGatewayListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dbs_20190306_models.DescribeBackupGatewayListResponse().from_map(
            await self.do_rpcrequest_async('DescribeBackupGatewayList', '2019-03-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_backup_gateway_list(
        self,
        request: dbs_20190306_models.DescribeBackupGatewayListRequest,
    ) -> dbs_20190306_models.DescribeBackupGatewayListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_gateway_list_with_options(request, runtime)

    async def describe_backup_gateway_list_async(
        self,
        request: dbs_20190306_models.DescribeBackupGatewayListRequest,
    ) -> dbs_20190306_models.DescribeBackupGatewayListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_gateway_list_with_options_async(request, runtime)

    def describe_backup_plan_billing_with_options(
        self,
        request: dbs_20190306_models.DescribeBackupPlanBillingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.DescribeBackupPlanBillingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dbs_20190306_models.DescribeBackupPlanBillingResponse().from_map(
            self.do_rpcrequest('DescribeBackupPlanBilling', '2019-03-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_backup_plan_billing_with_options_async(
        self,
        request: dbs_20190306_models.DescribeBackupPlanBillingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.DescribeBackupPlanBillingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dbs_20190306_models.DescribeBackupPlanBillingResponse().from_map(
            await self.do_rpcrequest_async('DescribeBackupPlanBilling', '2019-03-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_backup_plan_billing(
        self,
        request: dbs_20190306_models.DescribeBackupPlanBillingRequest,
    ) -> dbs_20190306_models.DescribeBackupPlanBillingResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_plan_billing_with_options(request, runtime)

    async def describe_backup_plan_billing_async(
        self,
        request: dbs_20190306_models.DescribeBackupPlanBillingRequest,
    ) -> dbs_20190306_models.DescribeBackupPlanBillingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_plan_billing_with_options_async(request, runtime)

    def describe_backup_plan_list_with_options(
        self,
        request: dbs_20190306_models.DescribeBackupPlanListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.DescribeBackupPlanListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dbs_20190306_models.DescribeBackupPlanListResponse().from_map(
            self.do_rpcrequest('DescribeBackupPlanList', '2019-03-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_backup_plan_list_with_options_async(
        self,
        request: dbs_20190306_models.DescribeBackupPlanListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.DescribeBackupPlanListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dbs_20190306_models.DescribeBackupPlanListResponse().from_map(
            await self.do_rpcrequest_async('DescribeBackupPlanList', '2019-03-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_backup_plan_list(
        self,
        request: dbs_20190306_models.DescribeBackupPlanListRequest,
    ) -> dbs_20190306_models.DescribeBackupPlanListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_plan_list_with_options(request, runtime)

    async def describe_backup_plan_list_async(
        self,
        request: dbs_20190306_models.DescribeBackupPlanListRequest,
    ) -> dbs_20190306_models.DescribeBackupPlanListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_plan_list_with_options_async(request, runtime)

    def describe_backup_set_download_task_list_with_options(
        self,
        request: dbs_20190306_models.DescribeBackupSetDownloadTaskListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.DescribeBackupSetDownloadTaskListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dbs_20190306_models.DescribeBackupSetDownloadTaskListResponse().from_map(
            self.do_rpcrequest('DescribeBackupSetDownloadTaskList', '2019-03-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_backup_set_download_task_list_with_options_async(
        self,
        request: dbs_20190306_models.DescribeBackupSetDownloadTaskListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.DescribeBackupSetDownloadTaskListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dbs_20190306_models.DescribeBackupSetDownloadTaskListResponse().from_map(
            await self.do_rpcrequest_async('DescribeBackupSetDownloadTaskList', '2019-03-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_backup_set_download_task_list(
        self,
        request: dbs_20190306_models.DescribeBackupSetDownloadTaskListRequest,
    ) -> dbs_20190306_models.DescribeBackupSetDownloadTaskListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_set_download_task_list_with_options(request, runtime)

    async def describe_backup_set_download_task_list_async(
        self,
        request: dbs_20190306_models.DescribeBackupSetDownloadTaskListRequest,
    ) -> dbs_20190306_models.DescribeBackupSetDownloadTaskListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_set_download_task_list_with_options_async(request, runtime)

    def describe_full_backup_list_with_options(
        self,
        request: dbs_20190306_models.DescribeFullBackupListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.DescribeFullBackupListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dbs_20190306_models.DescribeFullBackupListResponse().from_map(
            self.do_rpcrequest('DescribeFullBackupList', '2019-03-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_full_backup_list_with_options_async(
        self,
        request: dbs_20190306_models.DescribeFullBackupListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.DescribeFullBackupListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dbs_20190306_models.DescribeFullBackupListResponse().from_map(
            await self.do_rpcrequest_async('DescribeFullBackupList', '2019-03-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_full_backup_list(
        self,
        request: dbs_20190306_models.DescribeFullBackupListRequest,
    ) -> dbs_20190306_models.DescribeFullBackupListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_full_backup_list_with_options(request, runtime)

    async def describe_full_backup_list_async(
        self,
        request: dbs_20190306_models.DescribeFullBackupListRequest,
    ) -> dbs_20190306_models.DescribeFullBackupListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_full_backup_list_with_options_async(request, runtime)

    def describe_increment_backup_list_with_options(
        self,
        request: dbs_20190306_models.DescribeIncrementBackupListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.DescribeIncrementBackupListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dbs_20190306_models.DescribeIncrementBackupListResponse().from_map(
            self.do_rpcrequest('DescribeIncrementBackupList', '2019-03-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_increment_backup_list_with_options_async(
        self,
        request: dbs_20190306_models.DescribeIncrementBackupListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.DescribeIncrementBackupListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dbs_20190306_models.DescribeIncrementBackupListResponse().from_map(
            await self.do_rpcrequest_async('DescribeIncrementBackupList', '2019-03-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_increment_backup_list(
        self,
        request: dbs_20190306_models.DescribeIncrementBackupListRequest,
    ) -> dbs_20190306_models.DescribeIncrementBackupListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_increment_backup_list_with_options(request, runtime)

    async def describe_increment_backup_list_async(
        self,
        request: dbs_20190306_models.DescribeIncrementBackupListRequest,
    ) -> dbs_20190306_models.DescribeIncrementBackupListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_increment_backup_list_with_options_async(request, runtime)

    def describe_job_error_code_with_options(
        self,
        request: dbs_20190306_models.DescribeJobErrorCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.DescribeJobErrorCodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dbs_20190306_models.DescribeJobErrorCodeResponse().from_map(
            self.do_rpcrequest('DescribeJobErrorCode', '2019-03-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_job_error_code_with_options_async(
        self,
        request: dbs_20190306_models.DescribeJobErrorCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.DescribeJobErrorCodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dbs_20190306_models.DescribeJobErrorCodeResponse().from_map(
            await self.do_rpcrequest_async('DescribeJobErrorCode', '2019-03-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_job_error_code(
        self,
        request: dbs_20190306_models.DescribeJobErrorCodeRequest,
    ) -> dbs_20190306_models.DescribeJobErrorCodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_job_error_code_with_options(request, runtime)

    async def describe_job_error_code_async(
        self,
        request: dbs_20190306_models.DescribeJobErrorCodeRequest,
    ) -> dbs_20190306_models.DescribeJobErrorCodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_job_error_code_with_options_async(request, runtime)

    def describe_node_cidr_list_with_options(
        self,
        request: dbs_20190306_models.DescribeNodeCidrListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.DescribeNodeCidrListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dbs_20190306_models.DescribeNodeCidrListResponse().from_map(
            self.do_rpcrequest('DescribeNodeCidrList', '2019-03-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_node_cidr_list_with_options_async(
        self,
        request: dbs_20190306_models.DescribeNodeCidrListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.DescribeNodeCidrListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dbs_20190306_models.DescribeNodeCidrListResponse().from_map(
            await self.do_rpcrequest_async('DescribeNodeCidrList', '2019-03-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_node_cidr_list(
        self,
        request: dbs_20190306_models.DescribeNodeCidrListRequest,
    ) -> dbs_20190306_models.DescribeNodeCidrListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_node_cidr_list_with_options(request, runtime)

    async def describe_node_cidr_list_async(
        self,
        request: dbs_20190306_models.DescribeNodeCidrListRequest,
    ) -> dbs_20190306_models.DescribeNodeCidrListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_node_cidr_list_with_options_async(request, runtime)

    def describe_pre_check_progress_list_with_options(
        self,
        request: dbs_20190306_models.DescribePreCheckProgressListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.DescribePreCheckProgressListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dbs_20190306_models.DescribePreCheckProgressListResponse().from_map(
            self.do_rpcrequest('DescribePreCheckProgressList', '2019-03-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_pre_check_progress_list_with_options_async(
        self,
        request: dbs_20190306_models.DescribePreCheckProgressListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.DescribePreCheckProgressListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dbs_20190306_models.DescribePreCheckProgressListResponse().from_map(
            await self.do_rpcrequest_async('DescribePreCheckProgressList', '2019-03-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_pre_check_progress_list(
        self,
        request: dbs_20190306_models.DescribePreCheckProgressListRequest,
    ) -> dbs_20190306_models.DescribePreCheckProgressListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_pre_check_progress_list_with_options(request, runtime)

    async def describe_pre_check_progress_list_async(
        self,
        request: dbs_20190306_models.DescribePreCheckProgressListRequest,
    ) -> dbs_20190306_models.DescribePreCheckProgressListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_pre_check_progress_list_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: dbs_20190306_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dbs_20190306_models.DescribeRegionsResponse().from_map(
            self.do_rpcrequest('DescribeRegions', '2019-03-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: dbs_20190306_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dbs_20190306_models.DescribeRegionsResponse().from_map(
            await self.do_rpcrequest_async('DescribeRegions', '2019-03-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_regions(
        self,
        request: dbs_20190306_models.DescribeRegionsRequest,
    ) -> dbs_20190306_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: dbs_20190306_models.DescribeRegionsRequest,
    ) -> dbs_20190306_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_restore_range_info_with_options(
        self,
        request: dbs_20190306_models.DescribeRestoreRangeInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.DescribeRestoreRangeInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dbs_20190306_models.DescribeRestoreRangeInfoResponse().from_map(
            self.do_rpcrequest('DescribeRestoreRangeInfo', '2019-03-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_restore_range_info_with_options_async(
        self,
        request: dbs_20190306_models.DescribeRestoreRangeInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.DescribeRestoreRangeInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dbs_20190306_models.DescribeRestoreRangeInfoResponse().from_map(
            await self.do_rpcrequest_async('DescribeRestoreRangeInfo', '2019-03-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_restore_range_info(
        self,
        request: dbs_20190306_models.DescribeRestoreRangeInfoRequest,
    ) -> dbs_20190306_models.DescribeRestoreRangeInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_restore_range_info_with_options(request, runtime)

    async def describe_restore_range_info_async(
        self,
        request: dbs_20190306_models.DescribeRestoreRangeInfoRequest,
    ) -> dbs_20190306_models.DescribeRestoreRangeInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_restore_range_info_with_options_async(request, runtime)

    def describe_restore_task_list_with_options(
        self,
        request: dbs_20190306_models.DescribeRestoreTaskListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.DescribeRestoreTaskListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dbs_20190306_models.DescribeRestoreTaskListResponse().from_map(
            self.do_rpcrequest('DescribeRestoreTaskList', '2019-03-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_restore_task_list_with_options_async(
        self,
        request: dbs_20190306_models.DescribeRestoreTaskListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.DescribeRestoreTaskListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dbs_20190306_models.DescribeRestoreTaskListResponse().from_map(
            await self.do_rpcrequest_async('DescribeRestoreTaskList', '2019-03-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_restore_task_list(
        self,
        request: dbs_20190306_models.DescribeRestoreTaskListRequest,
    ) -> dbs_20190306_models.DescribeRestoreTaskListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_restore_task_list_with_options(request, runtime)

    async def describe_restore_task_list_async(
        self,
        request: dbs_20190306_models.DescribeRestoreTaskListRequest,
    ) -> dbs_20190306_models.DescribeRestoreTaskListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_restore_task_list_with_options_async(request, runtime)

    def disable_backup_log_with_options(
        self,
        request: dbs_20190306_models.DisableBackupLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.DisableBackupLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dbs_20190306_models.DisableBackupLogResponse().from_map(
            self.do_rpcrequest('DisableBackupLog', '2019-03-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def disable_backup_log_with_options_async(
        self,
        request: dbs_20190306_models.DisableBackupLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.DisableBackupLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dbs_20190306_models.DisableBackupLogResponse().from_map(
            await self.do_rpcrequest_async('DisableBackupLog', '2019-03-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def disable_backup_log(
        self,
        request: dbs_20190306_models.DisableBackupLogRequest,
    ) -> dbs_20190306_models.DisableBackupLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_backup_log_with_options(request, runtime)

    async def disable_backup_log_async(
        self,
        request: dbs_20190306_models.DisableBackupLogRequest,
    ) -> dbs_20190306_models.DisableBackupLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_backup_log_with_options_async(request, runtime)

    def enable_backup_log_with_options(
        self,
        request: dbs_20190306_models.EnableBackupLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.EnableBackupLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dbs_20190306_models.EnableBackupLogResponse().from_map(
            self.do_rpcrequest('EnableBackupLog', '2019-03-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def enable_backup_log_with_options_async(
        self,
        request: dbs_20190306_models.EnableBackupLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.EnableBackupLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dbs_20190306_models.EnableBackupLogResponse().from_map(
            await self.do_rpcrequest_async('EnableBackupLog', '2019-03-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enable_backup_log(
        self,
        request: dbs_20190306_models.EnableBackupLogRequest,
    ) -> dbs_20190306_models.EnableBackupLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_backup_log_with_options(request, runtime)

    async def enable_backup_log_async(
        self,
        request: dbs_20190306_models.EnableBackupLogRequest,
    ) -> dbs_20190306_models.EnableBackupLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_backup_log_with_options_async(request, runtime)

    def get_dblist_from_agent_with_options(
        self,
        request: dbs_20190306_models.GetDBListFromAgentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.GetDBListFromAgentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dbs_20190306_models.GetDBListFromAgentResponse().from_map(
            self.do_rpcrequest('GetDBListFromAgent', '2019-03-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_dblist_from_agent_with_options_async(
        self,
        request: dbs_20190306_models.GetDBListFromAgentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.GetDBListFromAgentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dbs_20190306_models.GetDBListFromAgentResponse().from_map(
            await self.do_rpcrequest_async('GetDBListFromAgent', '2019-03-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_dblist_from_agent(
        self,
        request: dbs_20190306_models.GetDBListFromAgentRequest,
    ) -> dbs_20190306_models.GetDBListFromAgentResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_dblist_from_agent_with_options(request, runtime)

    async def get_dblist_from_agent_async(
        self,
        request: dbs_20190306_models.GetDBListFromAgentRequest,
    ) -> dbs_20190306_models.GetDBListFromAgentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_dblist_from_agent_with_options_async(request, runtime)

    def modify_backup_objects_with_options(
        self,
        request: dbs_20190306_models.ModifyBackupObjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.ModifyBackupObjectsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dbs_20190306_models.ModifyBackupObjectsResponse().from_map(
            self.do_rpcrequest('ModifyBackupObjects', '2019-03-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_backup_objects_with_options_async(
        self,
        request: dbs_20190306_models.ModifyBackupObjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.ModifyBackupObjectsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dbs_20190306_models.ModifyBackupObjectsResponse().from_map(
            await self.do_rpcrequest_async('ModifyBackupObjects', '2019-03-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_backup_objects(
        self,
        request: dbs_20190306_models.ModifyBackupObjectsRequest,
    ) -> dbs_20190306_models.ModifyBackupObjectsResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_backup_objects_with_options(request, runtime)

    async def modify_backup_objects_async(
        self,
        request: dbs_20190306_models.ModifyBackupObjectsRequest,
    ) -> dbs_20190306_models.ModifyBackupObjectsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_backup_objects_with_options_async(request, runtime)

    def modify_backup_plan_name_with_options(
        self,
        request: dbs_20190306_models.ModifyBackupPlanNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.ModifyBackupPlanNameResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dbs_20190306_models.ModifyBackupPlanNameResponse().from_map(
            self.do_rpcrequest('ModifyBackupPlanName', '2019-03-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_backup_plan_name_with_options_async(
        self,
        request: dbs_20190306_models.ModifyBackupPlanNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.ModifyBackupPlanNameResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dbs_20190306_models.ModifyBackupPlanNameResponse().from_map(
            await self.do_rpcrequest_async('ModifyBackupPlanName', '2019-03-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_backup_plan_name(
        self,
        request: dbs_20190306_models.ModifyBackupPlanNameRequest,
    ) -> dbs_20190306_models.ModifyBackupPlanNameResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_backup_plan_name_with_options(request, runtime)

    async def modify_backup_plan_name_async(
        self,
        request: dbs_20190306_models.ModifyBackupPlanNameRequest,
    ) -> dbs_20190306_models.ModifyBackupPlanNameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_backup_plan_name_with_options_async(request, runtime)

    def modify_backup_set_download_rules_with_options(
        self,
        request: dbs_20190306_models.ModifyBackupSetDownloadRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.ModifyBackupSetDownloadRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dbs_20190306_models.ModifyBackupSetDownloadRulesResponse().from_map(
            self.do_rpcrequest('ModifyBackupSetDownloadRules', '2019-03-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_backup_set_download_rules_with_options_async(
        self,
        request: dbs_20190306_models.ModifyBackupSetDownloadRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.ModifyBackupSetDownloadRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dbs_20190306_models.ModifyBackupSetDownloadRulesResponse().from_map(
            await self.do_rpcrequest_async('ModifyBackupSetDownloadRules', '2019-03-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_backup_set_download_rules(
        self,
        request: dbs_20190306_models.ModifyBackupSetDownloadRulesRequest,
    ) -> dbs_20190306_models.ModifyBackupSetDownloadRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_backup_set_download_rules_with_options(request, runtime)

    async def modify_backup_set_download_rules_async(
        self,
        request: dbs_20190306_models.ModifyBackupSetDownloadRulesRequest,
    ) -> dbs_20190306_models.ModifyBackupSetDownloadRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_backup_set_download_rules_with_options_async(request, runtime)

    def modify_backup_source_endpoint_with_options(
        self,
        request: dbs_20190306_models.ModifyBackupSourceEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.ModifyBackupSourceEndpointResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dbs_20190306_models.ModifyBackupSourceEndpointResponse().from_map(
            self.do_rpcrequest('ModifyBackupSourceEndpoint', '2019-03-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_backup_source_endpoint_with_options_async(
        self,
        request: dbs_20190306_models.ModifyBackupSourceEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.ModifyBackupSourceEndpointResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dbs_20190306_models.ModifyBackupSourceEndpointResponse().from_map(
            await self.do_rpcrequest_async('ModifyBackupSourceEndpoint', '2019-03-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_backup_source_endpoint(
        self,
        request: dbs_20190306_models.ModifyBackupSourceEndpointRequest,
    ) -> dbs_20190306_models.ModifyBackupSourceEndpointResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_backup_source_endpoint_with_options(request, runtime)

    async def modify_backup_source_endpoint_async(
        self,
        request: dbs_20190306_models.ModifyBackupSourceEndpointRequest,
    ) -> dbs_20190306_models.ModifyBackupSourceEndpointResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_backup_source_endpoint_with_options_async(request, runtime)

    def modify_backup_strategy_with_options(
        self,
        request: dbs_20190306_models.ModifyBackupStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.ModifyBackupStrategyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dbs_20190306_models.ModifyBackupStrategyResponse().from_map(
            self.do_rpcrequest('ModifyBackupStrategy', '2019-03-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_backup_strategy_with_options_async(
        self,
        request: dbs_20190306_models.ModifyBackupStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.ModifyBackupStrategyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dbs_20190306_models.ModifyBackupStrategyResponse().from_map(
            await self.do_rpcrequest_async('ModifyBackupStrategy', '2019-03-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_backup_strategy(
        self,
        request: dbs_20190306_models.ModifyBackupStrategyRequest,
    ) -> dbs_20190306_models.ModifyBackupStrategyResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_backup_strategy_with_options(request, runtime)

    async def modify_backup_strategy_async(
        self,
        request: dbs_20190306_models.ModifyBackupStrategyRequest,
    ) -> dbs_20190306_models.ModifyBackupStrategyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_backup_strategy_with_options_async(request, runtime)

    def modify_storage_strategy_with_options(
        self,
        request: dbs_20190306_models.ModifyStorageStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.ModifyStorageStrategyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dbs_20190306_models.ModifyStorageStrategyResponse().from_map(
            self.do_rpcrequest('ModifyStorageStrategy', '2019-03-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_storage_strategy_with_options_async(
        self,
        request: dbs_20190306_models.ModifyStorageStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.ModifyStorageStrategyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dbs_20190306_models.ModifyStorageStrategyResponse().from_map(
            await self.do_rpcrequest_async('ModifyStorageStrategy', '2019-03-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_storage_strategy(
        self,
        request: dbs_20190306_models.ModifyStorageStrategyRequest,
    ) -> dbs_20190306_models.ModifyStorageStrategyResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_storage_strategy_with_options(request, runtime)

    async def modify_storage_strategy_async(
        self,
        request: dbs_20190306_models.ModifyStorageStrategyRequest,
    ) -> dbs_20190306_models.ModifyStorageStrategyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_storage_strategy_with_options_async(request, runtime)

    def release_backup_plan_with_options(
        self,
        request: dbs_20190306_models.ReleaseBackupPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.ReleaseBackupPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dbs_20190306_models.ReleaseBackupPlanResponse().from_map(
            self.do_rpcrequest('ReleaseBackupPlan', '2019-03-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def release_backup_plan_with_options_async(
        self,
        request: dbs_20190306_models.ReleaseBackupPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.ReleaseBackupPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dbs_20190306_models.ReleaseBackupPlanResponse().from_map(
            await self.do_rpcrequest_async('ReleaseBackupPlan', '2019-03-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def release_backup_plan(
        self,
        request: dbs_20190306_models.ReleaseBackupPlanRequest,
    ) -> dbs_20190306_models.ReleaseBackupPlanResponse:
        runtime = util_models.RuntimeOptions()
        return self.release_backup_plan_with_options(request, runtime)

    async def release_backup_plan_async(
        self,
        request: dbs_20190306_models.ReleaseBackupPlanRequest,
    ) -> dbs_20190306_models.ReleaseBackupPlanResponse:
        runtime = util_models.RuntimeOptions()
        return await self.release_backup_plan_with_options_async(request, runtime)

    def renew_backup_plan_with_options(
        self,
        request: dbs_20190306_models.RenewBackupPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.RenewBackupPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dbs_20190306_models.RenewBackupPlanResponse().from_map(
            self.do_rpcrequest('RenewBackupPlan', '2019-03-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def renew_backup_plan_with_options_async(
        self,
        request: dbs_20190306_models.RenewBackupPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.RenewBackupPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dbs_20190306_models.RenewBackupPlanResponse().from_map(
            await self.do_rpcrequest_async('RenewBackupPlan', '2019-03-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def renew_backup_plan(
        self,
        request: dbs_20190306_models.RenewBackupPlanRequest,
    ) -> dbs_20190306_models.RenewBackupPlanResponse:
        runtime = util_models.RuntimeOptions()
        return self.renew_backup_plan_with_options(request, runtime)

    async def renew_backup_plan_async(
        self,
        request: dbs_20190306_models.RenewBackupPlanRequest,
    ) -> dbs_20190306_models.RenewBackupPlanResponse:
        runtime = util_models.RuntimeOptions()
        return await self.renew_backup_plan_with_options_async(request, runtime)

    def start_backup_plan_with_options(
        self,
        request: dbs_20190306_models.StartBackupPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.StartBackupPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dbs_20190306_models.StartBackupPlanResponse().from_map(
            self.do_rpcrequest('StartBackupPlan', '2019-03-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_backup_plan_with_options_async(
        self,
        request: dbs_20190306_models.StartBackupPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.StartBackupPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dbs_20190306_models.StartBackupPlanResponse().from_map(
            await self.do_rpcrequest_async('StartBackupPlan', '2019-03-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_backup_plan(
        self,
        request: dbs_20190306_models.StartBackupPlanRequest,
    ) -> dbs_20190306_models.StartBackupPlanResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_backup_plan_with_options(request, runtime)

    async def start_backup_plan_async(
        self,
        request: dbs_20190306_models.StartBackupPlanRequest,
    ) -> dbs_20190306_models.StartBackupPlanResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_backup_plan_with_options_async(request, runtime)

    def start_restore_task_with_options(
        self,
        request: dbs_20190306_models.StartRestoreTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.StartRestoreTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dbs_20190306_models.StartRestoreTaskResponse().from_map(
            self.do_rpcrequest('StartRestoreTask', '2019-03-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_restore_task_with_options_async(
        self,
        request: dbs_20190306_models.StartRestoreTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.StartRestoreTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dbs_20190306_models.StartRestoreTaskResponse().from_map(
            await self.do_rpcrequest_async('StartRestoreTask', '2019-03-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_restore_task(
        self,
        request: dbs_20190306_models.StartRestoreTaskRequest,
    ) -> dbs_20190306_models.StartRestoreTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_restore_task_with_options(request, runtime)

    async def start_restore_task_async(
        self,
        request: dbs_20190306_models.StartRestoreTaskRequest,
    ) -> dbs_20190306_models.StartRestoreTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_restore_task_with_options_async(request, runtime)

    def start_task_with_options(
        self,
        request: dbs_20190306_models.StartTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.StartTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dbs_20190306_models.StartTaskResponse().from_map(
            self.do_rpcrequest('StartTask', '2019-03-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_task_with_options_async(
        self,
        request: dbs_20190306_models.StartTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.StartTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dbs_20190306_models.StartTaskResponse().from_map(
            await self.do_rpcrequest_async('StartTask', '2019-03-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_task(
        self,
        request: dbs_20190306_models.StartTaskRequest,
    ) -> dbs_20190306_models.StartTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_task_with_options(request, runtime)

    async def start_task_async(
        self,
        request: dbs_20190306_models.StartTaskRequest,
    ) -> dbs_20190306_models.StartTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_task_with_options_async(request, runtime)

    def stop_backup_plan_with_options(
        self,
        request: dbs_20190306_models.StopBackupPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.StopBackupPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dbs_20190306_models.StopBackupPlanResponse().from_map(
            self.do_rpcrequest('StopBackupPlan', '2019-03-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def stop_backup_plan_with_options_async(
        self,
        request: dbs_20190306_models.StopBackupPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.StopBackupPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dbs_20190306_models.StopBackupPlanResponse().from_map(
            await self.do_rpcrequest_async('StopBackupPlan', '2019-03-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_backup_plan(
        self,
        request: dbs_20190306_models.StopBackupPlanRequest,
    ) -> dbs_20190306_models.StopBackupPlanResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_backup_plan_with_options(request, runtime)

    async def stop_backup_plan_async(
        self,
        request: dbs_20190306_models.StopBackupPlanRequest,
    ) -> dbs_20190306_models.StopBackupPlanResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_backup_plan_with_options_async(request, runtime)

    def upgrade_backup_plan_with_options(
        self,
        request: dbs_20190306_models.UpgradeBackupPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.UpgradeBackupPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dbs_20190306_models.UpgradeBackupPlanResponse().from_map(
            self.do_rpcrequest('UpgradeBackupPlan', '2019-03-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def upgrade_backup_plan_with_options_async(
        self,
        request: dbs_20190306_models.UpgradeBackupPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.UpgradeBackupPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dbs_20190306_models.UpgradeBackupPlanResponse().from_map(
            await self.do_rpcrequest_async('UpgradeBackupPlan', '2019-03-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upgrade_backup_plan(
        self,
        request: dbs_20190306_models.UpgradeBackupPlanRequest,
    ) -> dbs_20190306_models.UpgradeBackupPlanResponse:
        runtime = util_models.RuntimeOptions()
        return self.upgrade_backup_plan_with_options(request, runtime)

    async def upgrade_backup_plan_async(
        self,
        request: dbs_20190306_models.UpgradeBackupPlanRequest,
    ) -> dbs_20190306_models.UpgradeBackupPlanResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_backup_plan_with_options_async(request, runtime)
