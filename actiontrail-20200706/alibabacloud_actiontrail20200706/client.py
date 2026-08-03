# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_actiontrail20200706 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
from darabonba.runtime import RuntimeOptions

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
            'ap-northeast-2-pop': 'actiontrail.ap-northeast-1.aliyuncs.com',
            'cn-beijing-finance-1': 'actiontrail.aliyuncs.com',
            'cn-beijing-finance-pop': 'actiontrail.aliyuncs.com',
            'cn-beijing-gov-1': 'actiontrail.aliyuncs.com',
            'cn-beijing-nu16-b01': 'actiontrail.aliyuncs.com',
            'cn-edge-1': 'actiontrail.aliyuncs.com',
            'cn-fujian': 'actiontrail.aliyuncs.com',
            'cn-haidian-cm12-c01': 'actiontrail.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'actiontrail.aliyuncs.com',
            'cn-hangzhou-finance': 'actiontrail.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'actiontrail.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'actiontrail.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'actiontrail.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'actiontrail.aliyuncs.com',
            'cn-hangzhou-test-306': 'actiontrail.aliyuncs.com',
            'cn-hongkong-finance-pop': 'actiontrail.aliyuncs.com',
            'cn-qingdao-nebula': 'actiontrail.aliyuncs.com',
            'cn-shanghai-et15-b01': 'actiontrail.aliyuncs.com',
            'cn-shanghai-et2-b01': 'actiontrail.aliyuncs.com',
            'cn-shanghai-inner': 'actiontrail.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'actiontrail.aliyuncs.com',
            'cn-shenzhen-finance-1': 'actiontrail.aliyuncs.com',
            'cn-shenzhen-inner': 'actiontrail.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'actiontrail.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'actiontrail.aliyuncs.com',
            'cn-wuhan': 'actiontrail.aliyuncs.com',
            'cn-yushanfang': 'actiontrail.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'actiontrail.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'actiontrail.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'actiontrail.aliyuncs.com',
            'eu-west-1-oxs': 'actiontrail.ap-northeast-1.aliyuncs.com',
            'rus-west-1-pop': 'actiontrail.ap-northeast-1.aliyuncs.com',
            'us-west-1': 'actiontrail.us-west-1.aliyuncs.com',
            'us-southeast-1': 'actiontrail.us-southeast-1.aliyuncs.com',
            'us-east-1': 'actiontrail.us-east-1.aliyuncs.com',
            'na-south-1': 'actiontrail.na-south-1.aliyuncs.com',
            'me-east-1': 'actiontrail.me-east-1.aliyuncs.com',
            'me-central-1': 'actiontrail.me-central-1.aliyuncs.com',
            'eu-west-2': 'actiontrail.eu-west-2.aliyuncs.com',
            'eu-west-1': 'actiontrail.eu-west-1.aliyuncs.com',
            'eu-central-1': 'actiontrail.eu-central-1.aliyuncs.com',
            'cn-zhongwei': 'actiontrail.cn-zhongwei.aliyuncs.com',
            'cn-zhangjiakou': 'actiontrail.cn-zhangjiakou.aliyuncs.com',
            'cn-wulanchabu': 'actiontrail.cn-wulanchabu.aliyuncs.com',
            'cn-shenzhen': 'actiontrail.cn-shenzhen.aliyuncs.com',
            'cn-shanghai-finance-1': 'actiontrail.cn-shanghai-finance-1.aliyuncs.com',
            'cn-shanghai': 'actiontrail.cn-shanghai.aliyuncs.com',
            'cn-qingdao': 'actiontrail.cn-qingdao.aliyuncs.com',
            'cn-north-2-gov-1': 'actiontrail.cn-north-2-gov-1.aliyuncs.com',
            'cn-nanjing': 'actiontrail.cn-nanjing.aliyuncs.com',
            'cn-huhehaote': 'actiontrail.cn-huhehaote.aliyuncs.com',
            'cn-hongkong': 'actiontrail.cn-hongkong.aliyuncs.com',
            'cn-heyuan': 'actiontrail.cn-heyuan.aliyuncs.com',
            'cn-hangzhou': 'actiontrail.cn-hangzhou.aliyuncs.com',
            'cn-guangzhou': 'actiontrail.cn-guangzhou.aliyuncs.com',
            'cn-chengdu': 'actiontrail.cn-chengdu.aliyuncs.com',
            'cn-beijing': 'actiontrail.cn-beijing.aliyuncs.com',
            'ap-southeast-8': 'actiontrail.ap-southeast-8.aliyuncs.com',
            'ap-southeast-7': 'actiontrail.ap-southeast-7.aliyuncs.com',
            'ap-southeast-6': 'actiontrail.ap-southeast-6.aliyuncs.com',
            'ap-southeast-5': 'actiontrail.ap-southeast-5.aliyuncs.com',
            'ap-southeast-3': 'actiontrail.ap-southeast-3.aliyuncs.com',
            'ap-southeast-1': 'actiontrail.ap-southeast-1.aliyuncs.com',
            'ap-northeast-2': 'actiontrail.ap-northeast-2.aliyuncs.com',
            'ap-northeast-1': 'actiontrail.ap-northeast-1.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('actiontrail', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_advanced_query_history_with_options(
        self,
        request: main_models.CreateAdvancedQueryHistoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAdvancedQueryHistoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.query_sql):
            query['QuerySql'] = request.query_sql
        if not DaraCore.is_null(request.simple_query):
            query['SimpleQuery'] = request.simple_query
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAdvancedQueryHistory',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAdvancedQueryHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_advanced_query_history_with_options_async(
        self,
        request: main_models.CreateAdvancedQueryHistoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAdvancedQueryHistoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.query_sql):
            query['QuerySql'] = request.query_sql
        if not DaraCore.is_null(request.simple_query):
            query['SimpleQuery'] = request.simple_query
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAdvancedQueryHistory',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAdvancedQueryHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_advanced_query_history(
        self,
        request: main_models.CreateAdvancedQueryHistoryRequest,
    ) -> main_models.CreateAdvancedQueryHistoryResponse:
        runtime = RuntimeOptions()
        return self.create_advanced_query_history_with_options(request, runtime)

    async def create_advanced_query_history_async(
        self,
        request: main_models.CreateAdvancedQueryHistoryRequest,
    ) -> main_models.CreateAdvancedQueryHistoryResponse:
        runtime = RuntimeOptions()
        return await self.create_advanced_query_history_with_options_async(request, runtime)

    def create_advanced_query_template_with_options(
        self,
        request: main_models.CreateAdvancedQueryTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAdvancedQueryTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.simple_query):
            query['SimpleQuery'] = request.simple_query
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.template_sql):
            query['TemplateSql'] = request.template_sql
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAdvancedQueryTemplate',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAdvancedQueryTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_advanced_query_template_with_options_async(
        self,
        request: main_models.CreateAdvancedQueryTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAdvancedQueryTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.simple_query):
            query['SimpleQuery'] = request.simple_query
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.template_sql):
            query['TemplateSql'] = request.template_sql
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAdvancedQueryTemplate',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAdvancedQueryTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_advanced_query_template(
        self,
        request: main_models.CreateAdvancedQueryTemplateRequest,
    ) -> main_models.CreateAdvancedQueryTemplateResponse:
        runtime = RuntimeOptions()
        return self.create_advanced_query_template_with_options(request, runtime)

    async def create_advanced_query_template_async(
        self,
        request: main_models.CreateAdvancedQueryTemplateRequest,
    ) -> main_models.CreateAdvancedQueryTemplateResponse:
        runtime = RuntimeOptions()
        return await self.create_advanced_query_template_with_options_async(request, runtime)

    def create_delivery_history_job_with_options(
        self,
        request: main_models.CreateDeliveryHistoryJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDeliveryHistoryJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.trail_name):
            query['TrailName'] = request.trail_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDeliveryHistoryJob',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDeliveryHistoryJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_delivery_history_job_with_options_async(
        self,
        request: main_models.CreateDeliveryHistoryJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDeliveryHistoryJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.trail_name):
            query['TrailName'] = request.trail_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDeliveryHistoryJob',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDeliveryHistoryJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_delivery_history_job(
        self,
        request: main_models.CreateDeliveryHistoryJobRequest,
    ) -> main_models.CreateDeliveryHistoryJobResponse:
        runtime = RuntimeOptions()
        return self.create_delivery_history_job_with_options(request, runtime)

    async def create_delivery_history_job_async(
        self,
        request: main_models.CreateDeliveryHistoryJobRequest,
    ) -> main_models.CreateDeliveryHistoryJobResponse:
        runtime = RuntimeOptions()
        return await self.create_delivery_history_job_with_options_async(request, runtime)

    def create_trail_with_options(
        self,
        request: main_models.CreateTrailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTrailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.event_rw):
            query['EventRW'] = request.event_rw
        if not DaraCore.is_null(request.is_organization_trail):
            query['IsOrganizationTrail'] = request.is_organization_trail
        if not DaraCore.is_null(request.max_compute_project_arn):
            query['MaxComputeProjectArn'] = request.max_compute_project_arn
        if not DaraCore.is_null(request.max_compute_write_role_arn):
            query['MaxComputeWriteRoleArn'] = request.max_compute_write_role_arn
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.oss_bucket_name):
            query['OssBucketName'] = request.oss_bucket_name
        if not DaraCore.is_null(request.oss_key_prefix):
            query['OssKeyPrefix'] = request.oss_key_prefix
        if not DaraCore.is_null(request.oss_write_role_arn):
            query['OssWriteRoleArn'] = request.oss_write_role_arn
        if not DaraCore.is_null(request.sls_project_arn):
            query['SlsProjectArn'] = request.sls_project_arn
        if not DaraCore.is_null(request.sls_write_role_arn):
            query['SlsWriteRoleArn'] = request.sls_write_role_arn
        if not DaraCore.is_null(request.trail_region):
            query['TrailRegion'] = request.trail_region
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTrail',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTrailResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_trail_with_options_async(
        self,
        request: main_models.CreateTrailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTrailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.event_rw):
            query['EventRW'] = request.event_rw
        if not DaraCore.is_null(request.is_organization_trail):
            query['IsOrganizationTrail'] = request.is_organization_trail
        if not DaraCore.is_null(request.max_compute_project_arn):
            query['MaxComputeProjectArn'] = request.max_compute_project_arn
        if not DaraCore.is_null(request.max_compute_write_role_arn):
            query['MaxComputeWriteRoleArn'] = request.max_compute_write_role_arn
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.oss_bucket_name):
            query['OssBucketName'] = request.oss_bucket_name
        if not DaraCore.is_null(request.oss_key_prefix):
            query['OssKeyPrefix'] = request.oss_key_prefix
        if not DaraCore.is_null(request.oss_write_role_arn):
            query['OssWriteRoleArn'] = request.oss_write_role_arn
        if not DaraCore.is_null(request.sls_project_arn):
            query['SlsProjectArn'] = request.sls_project_arn
        if not DaraCore.is_null(request.sls_write_role_arn):
            query['SlsWriteRoleArn'] = request.sls_write_role_arn
        if not DaraCore.is_null(request.trail_region):
            query['TrailRegion'] = request.trail_region
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTrail',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTrailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_trail(
        self,
        request: main_models.CreateTrailRequest,
    ) -> main_models.CreateTrailResponse:
        runtime = RuntimeOptions()
        return self.create_trail_with_options(request, runtime)

    async def create_trail_async(
        self,
        request: main_models.CreateTrailRequest,
    ) -> main_models.CreateTrailResponse:
        runtime = RuntimeOptions()
        return await self.create_trail_with_options_async(request, runtime)

    def delete_advanced_query_history_with_options(
        self,
        request: main_models.DeleteAdvancedQueryHistoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAdvancedQueryHistoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.query_id):
            query['QueryId'] = request.query_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAdvancedQueryHistory',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAdvancedQueryHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_advanced_query_history_with_options_async(
        self,
        request: main_models.DeleteAdvancedQueryHistoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAdvancedQueryHistoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.query_id):
            query['QueryId'] = request.query_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAdvancedQueryHistory',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAdvancedQueryHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_advanced_query_history(
        self,
        request: main_models.DeleteAdvancedQueryHistoryRequest,
    ) -> main_models.DeleteAdvancedQueryHistoryResponse:
        runtime = RuntimeOptions()
        return self.delete_advanced_query_history_with_options(request, runtime)

    async def delete_advanced_query_history_async(
        self,
        request: main_models.DeleteAdvancedQueryHistoryRequest,
    ) -> main_models.DeleteAdvancedQueryHistoryResponse:
        runtime = RuntimeOptions()
        return await self.delete_advanced_query_history_with_options_async(request, runtime)

    def delete_advanced_query_template_with_options(
        self,
        request: main_models.DeleteAdvancedQueryTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAdvancedQueryTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAdvancedQueryTemplate',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAdvancedQueryTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_advanced_query_template_with_options_async(
        self,
        request: main_models.DeleteAdvancedQueryTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAdvancedQueryTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAdvancedQueryTemplate',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAdvancedQueryTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_advanced_query_template(
        self,
        request: main_models.DeleteAdvancedQueryTemplateRequest,
    ) -> main_models.DeleteAdvancedQueryTemplateResponse:
        runtime = RuntimeOptions()
        return self.delete_advanced_query_template_with_options(request, runtime)

    async def delete_advanced_query_template_async(
        self,
        request: main_models.DeleteAdvancedQueryTemplateRequest,
    ) -> main_models.DeleteAdvancedQueryTemplateResponse:
        runtime = RuntimeOptions()
        return await self.delete_advanced_query_template_with_options_async(request, runtime)

    def delete_data_event_selector_with_options(
        self,
        request: main_models.DeleteDataEventSelectorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataEventSelectorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.trail_name):
            query['TrailName'] = request.trail_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataEventSelector',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataEventSelectorResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_data_event_selector_with_options_async(
        self,
        request: main_models.DeleteDataEventSelectorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataEventSelectorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.trail_name):
            query['TrailName'] = request.trail_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataEventSelector',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataEventSelectorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_data_event_selector(
        self,
        request: main_models.DeleteDataEventSelectorRequest,
    ) -> main_models.DeleteDataEventSelectorResponse:
        runtime = RuntimeOptions()
        return self.delete_data_event_selector_with_options(request, runtime)

    async def delete_data_event_selector_async(
        self,
        request: main_models.DeleteDataEventSelectorRequest,
    ) -> main_models.DeleteDataEventSelectorResponse:
        runtime = RuntimeOptions()
        return await self.delete_data_event_selector_with_options_async(request, runtime)

    def delete_delivery_history_job_with_options(
        self,
        request: main_models.DeleteDeliveryHistoryJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDeliveryHistoryJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDeliveryHistoryJob',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDeliveryHistoryJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_delivery_history_job_with_options_async(
        self,
        request: main_models.DeleteDeliveryHistoryJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDeliveryHistoryJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDeliveryHistoryJob',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDeliveryHistoryJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_delivery_history_job(
        self,
        request: main_models.DeleteDeliveryHistoryJobRequest,
    ) -> main_models.DeleteDeliveryHistoryJobResponse:
        runtime = RuntimeOptions()
        return self.delete_delivery_history_job_with_options(request, runtime)

    async def delete_delivery_history_job_async(
        self,
        request: main_models.DeleteDeliveryHistoryJobRequest,
    ) -> main_models.DeleteDeliveryHistoryJobResponse:
        runtime = RuntimeOptions()
        return await self.delete_delivery_history_job_with_options_async(request, runtime)

    def delete_trail_with_options(
        self,
        request: main_models.DeleteTrailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTrailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTrail',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTrailResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_trail_with_options_async(
        self,
        request: main_models.DeleteTrailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTrailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTrail',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTrailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_trail(
        self,
        request: main_models.DeleteTrailRequest,
    ) -> main_models.DeleteTrailResponse:
        runtime = RuntimeOptions()
        return self.delete_trail_with_options(request, runtime)

    async def delete_trail_async(
        self,
        request: main_models.DeleteTrailRequest,
    ) -> main_models.DeleteTrailResponse:
        runtime = RuntimeOptions()
        return await self.delete_trail_with_options_async(request, runtime)

    def describe_advanced_query_history_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAdvancedQueryHistoryResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeAdvancedQueryHistory',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAdvancedQueryHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_advanced_query_history_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAdvancedQueryHistoryResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeAdvancedQueryHistory',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAdvancedQueryHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_advanced_query_history(self) -> main_models.DescribeAdvancedQueryHistoryResponse:
        runtime = RuntimeOptions()
        return self.describe_advanced_query_history_with_options(runtime)

    async def describe_advanced_query_history_async(self) -> main_models.DescribeAdvancedQueryHistoryResponse:
        runtime = RuntimeOptions()
        return await self.describe_advanced_query_history_with_options_async(runtime)

    def describe_advanced_query_template_with_options(
        self,
        request: main_models.DescribeAdvancedQueryTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAdvancedQueryTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAdvancedQueryTemplate',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAdvancedQueryTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_advanced_query_template_with_options_async(
        self,
        request: main_models.DescribeAdvancedQueryTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAdvancedQueryTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAdvancedQueryTemplate',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAdvancedQueryTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_advanced_query_template(
        self,
        request: main_models.DescribeAdvancedQueryTemplateRequest,
    ) -> main_models.DescribeAdvancedQueryTemplateResponse:
        runtime = RuntimeOptions()
        return self.describe_advanced_query_template_with_options(request, runtime)

    async def describe_advanced_query_template_async(
        self,
        request: main_models.DescribeAdvancedQueryTemplateRequest,
    ) -> main_models.DescribeAdvancedQueryTemplateResponse:
        runtime = RuntimeOptions()
        return await self.describe_advanced_query_template_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: main_models.DescribeRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: main_models.DescribeRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: main_models.DescribeRegionsRequest,
    ) -> main_models.DescribeRegionsResponse:
        runtime = RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: main_models.DescribeRegionsRequest,
    ) -> main_models.DescribeRegionsResponse:
        runtime = RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_resource_life_cycle_events_with_options(
        self,
        request: main_models.DescribeResourceLifeCycleEventsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeResourceLifeCycleEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeResourceLifeCycleEvents',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeResourceLifeCycleEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_resource_life_cycle_events_with_options_async(
        self,
        request: main_models.DescribeResourceLifeCycleEventsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeResourceLifeCycleEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeResourceLifeCycleEvents',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeResourceLifeCycleEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_resource_life_cycle_events(
        self,
        request: main_models.DescribeResourceLifeCycleEventsRequest,
    ) -> main_models.DescribeResourceLifeCycleEventsResponse:
        runtime = RuntimeOptions()
        return self.describe_resource_life_cycle_events_with_options(request, runtime)

    async def describe_resource_life_cycle_events_async(
        self,
        request: main_models.DescribeResourceLifeCycleEventsRequest,
    ) -> main_models.DescribeResourceLifeCycleEventsResponse:
        runtime = RuntimeOptions()
        return await self.describe_resource_life_cycle_events_with_options_async(request, runtime)

    def describe_scenes_with_options(
        self,
        request: main_models.DescribeScenesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeScenesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.search_code):
            query['SearchCode'] = request.search_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeScenes',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeScenesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scenes_with_options_async(
        self,
        request: main_models.DescribeScenesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeScenesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.search_code):
            query['SearchCode'] = request.search_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeScenes',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeScenesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scenes(
        self,
        request: main_models.DescribeScenesRequest,
    ) -> main_models.DescribeScenesResponse:
        runtime = RuntimeOptions()
        return self.describe_scenes_with_options(request, runtime)

    async def describe_scenes_async(
        self,
        request: main_models.DescribeScenesRequest,
    ) -> main_models.DescribeScenesResponse:
        runtime = RuntimeOptions()
        return await self.describe_scenes_with_options_async(request, runtime)

    def describe_search_templates_with_options(
        self,
        request: main_models.DescribeSearchTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSearchTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSearchTemplates',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSearchTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_search_templates_with_options_async(
        self,
        request: main_models.DescribeSearchTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSearchTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSearchTemplates',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSearchTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_search_templates(
        self,
        request: main_models.DescribeSearchTemplatesRequest,
    ) -> main_models.DescribeSearchTemplatesResponse:
        runtime = RuntimeOptions()
        return self.describe_search_templates_with_options(request, runtime)

    async def describe_search_templates_async(
        self,
        request: main_models.DescribeSearchTemplatesRequest,
    ) -> main_models.DescribeSearchTemplatesResponse:
        runtime = RuntimeOptions()
        return await self.describe_search_templates_with_options_async(request, runtime)

    def describe_trail_delivery_metric_data_with_options(
        self,
        request: main_models.DescribeTrailDeliveryMetricDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTrailDeliveryMetricDataResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTrailDeliveryMetricData',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTrailDeliveryMetricDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_trail_delivery_metric_data_with_options_async(
        self,
        request: main_models.DescribeTrailDeliveryMetricDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTrailDeliveryMetricDataResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTrailDeliveryMetricData',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTrailDeliveryMetricDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_trail_delivery_metric_data(
        self,
        request: main_models.DescribeTrailDeliveryMetricDataRequest,
    ) -> main_models.DescribeTrailDeliveryMetricDataResponse:
        runtime = RuntimeOptions()
        return self.describe_trail_delivery_metric_data_with_options(request, runtime)

    async def describe_trail_delivery_metric_data_async(
        self,
        request: main_models.DescribeTrailDeliveryMetricDataRequest,
    ) -> main_models.DescribeTrailDeliveryMetricDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_trail_delivery_metric_data_with_options_async(request, runtime)

    def describe_trails_with_options(
        self,
        request: main_models.DescribeTrailsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTrailsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.include_organization_trail):
            query['IncludeOrganizationTrail'] = request.include_organization_trail
        if not DaraCore.is_null(request.include_shadow_trails):
            query['IncludeShadowTrails'] = request.include_shadow_trails
        if not DaraCore.is_null(request.name_list):
            query['NameList'] = request.name_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTrails',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTrailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_trails_with_options_async(
        self,
        request: main_models.DescribeTrailsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTrailsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.include_organization_trail):
            query['IncludeOrganizationTrail'] = request.include_organization_trail
        if not DaraCore.is_null(request.include_shadow_trails):
            query['IncludeShadowTrails'] = request.include_shadow_trails
        if not DaraCore.is_null(request.name_list):
            query['NameList'] = request.name_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTrails',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTrailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_trails(
        self,
        request: main_models.DescribeTrailsRequest,
    ) -> main_models.DescribeTrailsResponse:
        runtime = RuntimeOptions()
        return self.describe_trails_with_options(request, runtime)

    async def describe_trails_async(
        self,
        request: main_models.DescribeTrailsRequest,
    ) -> main_models.DescribeTrailsResponse:
        runtime = RuntimeOptions()
        return await self.describe_trails_with_options_async(request, runtime)

    def describe_user_alert_count_with_options(
        self,
        request: main_models.DescribeUserAlertCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserAlertCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserAlertCount',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserAlertCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_alert_count_with_options_async(
        self,
        request: main_models.DescribeUserAlertCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserAlertCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserAlertCount',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserAlertCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_alert_count(
        self,
        request: main_models.DescribeUserAlertCountRequest,
    ) -> main_models.DescribeUserAlertCountResponse:
        runtime = RuntimeOptions()
        return self.describe_user_alert_count_with_options(request, runtime)

    async def describe_user_alert_count_async(
        self,
        request: main_models.DescribeUserAlertCountRequest,
    ) -> main_models.DescribeUserAlertCountResponse:
        runtime = RuntimeOptions()
        return await self.describe_user_alert_count_with_options_async(request, runtime)

    def describe_user_log_count_with_options(
        self,
        request: main_models.DescribeUserLogCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserLogCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserLogCount',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserLogCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_log_count_with_options_async(
        self,
        request: main_models.DescribeUserLogCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserLogCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserLogCount',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserLogCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_log_count(
        self,
        request: main_models.DescribeUserLogCountRequest,
    ) -> main_models.DescribeUserLogCountResponse:
        runtime = RuntimeOptions()
        return self.describe_user_log_count_with_options(request, runtime)

    async def describe_user_log_count_async(
        self,
        request: main_models.DescribeUserLogCountRequest,
    ) -> main_models.DescribeUserLogCountResponse:
        runtime = RuntimeOptions()
        return await self.describe_user_log_count_with_options_async(request, runtime)

    def describe_user_trail_count_with_options(
        self,
        request: main_models.DescribeUserTrailCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserTrailCountResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeUserTrailCount',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserTrailCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_trail_count_with_options_async(
        self,
        request: main_models.DescribeUserTrailCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserTrailCountResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeUserTrailCount',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserTrailCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_trail_count(
        self,
        request: main_models.DescribeUserTrailCountRequest,
    ) -> main_models.DescribeUserTrailCountResponse:
        runtime = RuntimeOptions()
        return self.describe_user_trail_count_with_options(request, runtime)

    async def describe_user_trail_count_async(
        self,
        request: main_models.DescribeUserTrailCountRequest,
    ) -> main_models.DescribeUserTrailCountResponse:
        runtime = RuntimeOptions()
        return await self.describe_user_trail_count_with_options_async(request, runtime)

    def disable_insight_with_options(
        self,
        request: main_models.DisableInsightRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableInsightResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.insight_type):
            query['InsightType'] = request.insight_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableInsight',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableInsightResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_insight_with_options_async(
        self,
        request: main_models.DisableInsightRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableInsightResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.insight_type):
            query['InsightType'] = request.insight_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableInsight',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableInsightResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_insight(
        self,
        request: main_models.DisableInsightRequest,
    ) -> main_models.DisableInsightResponse:
        runtime = RuntimeOptions()
        return self.disable_insight_with_options(request, runtime)

    async def disable_insight_async(
        self,
        request: main_models.DisableInsightRequest,
    ) -> main_models.DisableInsightResponse:
        runtime = RuntimeOptions()
        return await self.disable_insight_with_options_async(request, runtime)

    def enable_insight_with_options(
        self,
        request: main_models.EnableInsightRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableInsightResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.insight_type):
            query['InsightType'] = request.insight_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableInsight',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableInsightResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_insight_with_options_async(
        self,
        request: main_models.EnableInsightRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableInsightResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.insight_type):
            query['InsightType'] = request.insight_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableInsight',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableInsightResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_insight(
        self,
        request: main_models.EnableInsightRequest,
    ) -> main_models.EnableInsightResponse:
        runtime = RuntimeOptions()
        return self.enable_insight_with_options(request, runtime)

    async def enable_insight_async(
        self,
        request: main_models.EnableInsightRequest,
    ) -> main_models.EnableInsightResponse:
        runtime = RuntimeOptions()
        return await self.enable_insight_with_options_async(request, runtime)

    def get_access_key_last_used_events_with_options(
        self,
        request: main_models.GetAccessKeyLastUsedEventsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAccessKeyLastUsedEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_key):
            query['AccessKey'] = request.access_key
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAccessKeyLastUsedEvents',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAccessKeyLastUsedEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_access_key_last_used_events_with_options_async(
        self,
        request: main_models.GetAccessKeyLastUsedEventsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAccessKeyLastUsedEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_key):
            query['AccessKey'] = request.access_key
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAccessKeyLastUsedEvents',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAccessKeyLastUsedEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_access_key_last_used_events(
        self,
        request: main_models.GetAccessKeyLastUsedEventsRequest,
    ) -> main_models.GetAccessKeyLastUsedEventsResponse:
        runtime = RuntimeOptions()
        return self.get_access_key_last_used_events_with_options(request, runtime)

    async def get_access_key_last_used_events_async(
        self,
        request: main_models.GetAccessKeyLastUsedEventsRequest,
    ) -> main_models.GetAccessKeyLastUsedEventsResponse:
        runtime = RuntimeOptions()
        return await self.get_access_key_last_used_events_with_options_async(request, runtime)

    def get_access_key_last_used_info_with_options(
        self,
        request: main_models.GetAccessKeyLastUsedInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAccessKeyLastUsedInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_key):
            query['AccessKey'] = request.access_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAccessKeyLastUsedInfo',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAccessKeyLastUsedInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_access_key_last_used_info_with_options_async(
        self,
        request: main_models.GetAccessKeyLastUsedInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAccessKeyLastUsedInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_key):
            query['AccessKey'] = request.access_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAccessKeyLastUsedInfo',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAccessKeyLastUsedInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_access_key_last_used_info(
        self,
        request: main_models.GetAccessKeyLastUsedInfoRequest,
    ) -> main_models.GetAccessKeyLastUsedInfoResponse:
        runtime = RuntimeOptions()
        return self.get_access_key_last_used_info_with_options(request, runtime)

    async def get_access_key_last_used_info_async(
        self,
        request: main_models.GetAccessKeyLastUsedInfoRequest,
    ) -> main_models.GetAccessKeyLastUsedInfoResponse:
        runtime = RuntimeOptions()
        return await self.get_access_key_last_used_info_with_options_async(request, runtime)

    def get_access_key_last_used_ips_with_options(
        self,
        request: main_models.GetAccessKeyLastUsedIpsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAccessKeyLastUsedIpsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_key):
            query['AccessKey'] = request.access_key
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAccessKeyLastUsedIps',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAccessKeyLastUsedIpsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_access_key_last_used_ips_with_options_async(
        self,
        request: main_models.GetAccessKeyLastUsedIpsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAccessKeyLastUsedIpsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_key):
            query['AccessKey'] = request.access_key
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAccessKeyLastUsedIps',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAccessKeyLastUsedIpsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_access_key_last_used_ips(
        self,
        request: main_models.GetAccessKeyLastUsedIpsRequest,
    ) -> main_models.GetAccessKeyLastUsedIpsResponse:
        runtime = RuntimeOptions()
        return self.get_access_key_last_used_ips_with_options(request, runtime)

    async def get_access_key_last_used_ips_async(
        self,
        request: main_models.GetAccessKeyLastUsedIpsRequest,
    ) -> main_models.GetAccessKeyLastUsedIpsResponse:
        runtime = RuntimeOptions()
        return await self.get_access_key_last_used_ips_with_options_async(request, runtime)

    def get_access_key_last_used_products_with_options(
        self,
        request: main_models.GetAccessKeyLastUsedProductsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAccessKeyLastUsedProductsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_key):
            query['AccessKey'] = request.access_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAccessKeyLastUsedProducts',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAccessKeyLastUsedProductsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_access_key_last_used_products_with_options_async(
        self,
        request: main_models.GetAccessKeyLastUsedProductsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAccessKeyLastUsedProductsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_key):
            query['AccessKey'] = request.access_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAccessKeyLastUsedProducts',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAccessKeyLastUsedProductsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_access_key_last_used_products(
        self,
        request: main_models.GetAccessKeyLastUsedProductsRequest,
    ) -> main_models.GetAccessKeyLastUsedProductsResponse:
        runtime = RuntimeOptions()
        return self.get_access_key_last_used_products_with_options(request, runtime)

    async def get_access_key_last_used_products_async(
        self,
        request: main_models.GetAccessKeyLastUsedProductsRequest,
    ) -> main_models.GetAccessKeyLastUsedProductsResponse:
        runtime = RuntimeOptions()
        return await self.get_access_key_last_used_products_with_options_async(request, runtime)

    def get_access_key_last_used_resources_with_options(
        self,
        request: main_models.GetAccessKeyLastUsedResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAccessKeyLastUsedResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_key):
            query['AccessKey'] = request.access_key
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAccessKeyLastUsedResources',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAccessKeyLastUsedResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_access_key_last_used_resources_with_options_async(
        self,
        request: main_models.GetAccessKeyLastUsedResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAccessKeyLastUsedResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_key):
            query['AccessKey'] = request.access_key
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAccessKeyLastUsedResources',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAccessKeyLastUsedResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_access_key_last_used_resources(
        self,
        request: main_models.GetAccessKeyLastUsedResourcesRequest,
    ) -> main_models.GetAccessKeyLastUsedResourcesResponse:
        runtime = RuntimeOptions()
        return self.get_access_key_last_used_resources_with_options(request, runtime)

    async def get_access_key_last_used_resources_async(
        self,
        request: main_models.GetAccessKeyLastUsedResourcesRequest,
    ) -> main_models.GetAccessKeyLastUsedResourcesResponse:
        runtime = RuntimeOptions()
        return await self.get_access_key_last_used_resources_with_options_async(request, runtime)

    def get_advanced_query_template_with_options(
        self,
        request: main_models.GetAdvancedQueryTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAdvancedQueryTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAdvancedQueryTemplate',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAdvancedQueryTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_advanced_query_template_with_options_async(
        self,
        request: main_models.GetAdvancedQueryTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAdvancedQueryTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAdvancedQueryTemplate',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAdvancedQueryTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_advanced_query_template(
        self,
        request: main_models.GetAdvancedQueryTemplateRequest,
    ) -> main_models.GetAdvancedQueryTemplateResponse:
        runtime = RuntimeOptions()
        return self.get_advanced_query_template_with_options(request, runtime)

    async def get_advanced_query_template_async(
        self,
        request: main_models.GetAdvancedQueryTemplateRequest,
    ) -> main_models.GetAdvancedQueryTemplateResponse:
        runtime = RuntimeOptions()
        return await self.get_advanced_query_template_with_options_async(request, runtime)

    def get_data_event_selector_with_options(
        self,
        request: main_models.GetDataEventSelectorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataEventSelectorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.trail_name):
            query['TrailName'] = request.trail_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataEventSelector',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataEventSelectorResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_event_selector_with_options_async(
        self,
        request: main_models.GetDataEventSelectorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataEventSelectorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.trail_name):
            query['TrailName'] = request.trail_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataEventSelector',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataEventSelectorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_event_selector(
        self,
        request: main_models.GetDataEventSelectorRequest,
    ) -> main_models.GetDataEventSelectorResponse:
        runtime = RuntimeOptions()
        return self.get_data_event_selector_with_options(request, runtime)

    async def get_data_event_selector_async(
        self,
        request: main_models.GetDataEventSelectorRequest,
    ) -> main_models.GetDataEventSelectorResponse:
        runtime = RuntimeOptions()
        return await self.get_data_event_selector_with_options_async(request, runtime)

    def get_delivery_history_job_with_options(
        self,
        request: main_models.GetDeliveryHistoryJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDeliveryHistoryJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDeliveryHistoryJob',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDeliveryHistoryJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_delivery_history_job_with_options_async(
        self,
        request: main_models.GetDeliveryHistoryJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDeliveryHistoryJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDeliveryHistoryJob',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDeliveryHistoryJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_delivery_history_job(
        self,
        request: main_models.GetDeliveryHistoryJobRequest,
    ) -> main_models.GetDeliveryHistoryJobResponse:
        runtime = RuntimeOptions()
        return self.get_delivery_history_job_with_options(request, runtime)

    async def get_delivery_history_job_async(
        self,
        request: main_models.GetDeliveryHistoryJobRequest,
    ) -> main_models.GetDeliveryHistoryJobResponse:
        runtime = RuntimeOptions()
        return await self.get_delivery_history_job_with_options_async(request, runtime)

    def get_global_events_storage_region_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetGlobalEventsStorageRegionResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetGlobalEventsStorageRegion',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGlobalEventsStorageRegionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_global_events_storage_region_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetGlobalEventsStorageRegionResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetGlobalEventsStorageRegion',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGlobalEventsStorageRegionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_global_events_storage_region(self) -> main_models.GetGlobalEventsStorageRegionResponse:
        runtime = RuntimeOptions()
        return self.get_global_events_storage_region_with_options(runtime)

    async def get_global_events_storage_region_async(self) -> main_models.GetGlobalEventsStorageRegionResponse:
        runtime = RuntimeOptions()
        return await self.get_global_events_storage_region_with_options_async(runtime)

    def get_governance_metrics_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetGovernanceMetricsResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetGovernanceMetrics',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGovernanceMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_governance_metrics_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetGovernanceMetricsResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetGovernanceMetrics',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGovernanceMetricsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_governance_metrics(self) -> main_models.GetGovernanceMetricsResponse:
        runtime = RuntimeOptions()
        return self.get_governance_metrics_with_options(runtime)

    async def get_governance_metrics_async(self) -> main_models.GetGovernanceMetricsResponse:
        runtime = RuntimeOptions()
        return await self.get_governance_metrics_with_options_async(runtime)

    def get_insight_selectors_with_options(
        self,
        request: main_models.GetInsightSelectorsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInsightSelectorsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.trail_name):
            query['TrailName'] = request.trail_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInsightSelectors',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInsightSelectorsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_insight_selectors_with_options_async(
        self,
        request: main_models.GetInsightSelectorsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInsightSelectorsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.trail_name):
            query['TrailName'] = request.trail_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInsightSelectors',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInsightSelectorsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_insight_selectors(
        self,
        request: main_models.GetInsightSelectorsRequest,
    ) -> main_models.GetInsightSelectorsResponse:
        runtime = RuntimeOptions()
        return self.get_insight_selectors_with_options(request, runtime)

    async def get_insight_selectors_async(
        self,
        request: main_models.GetInsightSelectorsRequest,
    ) -> main_models.GetInsightSelectorsResponse:
        runtime = RuntimeOptions()
        return await self.get_insight_selectors_with_options_async(request, runtime)

    def get_insight_types_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetInsightTypesResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetInsightTypes',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInsightTypesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_insight_types_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetInsightTypesResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetInsightTypes',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInsightTypesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_insight_types(self) -> main_models.GetInsightTypesResponse:
        runtime = RuntimeOptions()
        return self.get_insight_types_with_options(runtime)

    async def get_insight_types_async(self) -> main_models.GetInsightTypesResponse:
        runtime = RuntimeOptions()
        return await self.get_insight_types_with_options_async(runtime)

    def get_insights_events_count_with_options(
        self,
        request: main_models.GetInsightsEventsCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInsightsEventsCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.date):
            query['Date'] = request.date
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInsightsEventsCount',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInsightsEventsCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_insights_events_count_with_options_async(
        self,
        request: main_models.GetInsightsEventsCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInsightsEventsCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.date):
            query['Date'] = request.date
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInsightsEventsCount',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInsightsEventsCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_insights_events_count(
        self,
        request: main_models.GetInsightsEventsCountRequest,
    ) -> main_models.GetInsightsEventsCountResponse:
        runtime = RuntimeOptions()
        return self.get_insights_events_count_with_options(request, runtime)

    async def get_insights_events_count_async(
        self,
        request: main_models.GetInsightsEventsCountRequest,
    ) -> main_models.GetInsightsEventsCountResponse:
        runtime = RuntimeOptions()
        return await self.get_insights_events_count_with_options_async(request, runtime)

    def get_trail_status_with_options(
        self,
        request: main_models.GetTrailStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTrailStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.is_organization_trail):
            query['IsOrganizationTrail'] = request.is_organization_trail
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTrailStatus',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTrailStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_trail_status_with_options_async(
        self,
        request: main_models.GetTrailStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTrailStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.is_organization_trail):
            query['IsOrganizationTrail'] = request.is_organization_trail
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTrailStatus',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTrailStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_trail_status(
        self,
        request: main_models.GetTrailStatusRequest,
    ) -> main_models.GetTrailStatusResponse:
        runtime = RuntimeOptions()
        return self.get_trail_status_with_options(request, runtime)

    async def get_trail_status_async(
        self,
        request: main_models.GetTrailStatusRequest,
    ) -> main_models.GetTrailStatusResponse:
        runtime = RuntimeOptions()
        return await self.get_trail_status_with_options_async(request, runtime)

    def list_data_event_selectors_with_options(
        self,
        request: main_models.ListDataEventSelectorsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataEventSelectorsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataEventSelectors',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataEventSelectorsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_event_selectors_with_options_async(
        self,
        request: main_models.ListDataEventSelectorsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataEventSelectorsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataEventSelectors',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataEventSelectorsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_event_selectors(
        self,
        request: main_models.ListDataEventSelectorsRequest,
    ) -> main_models.ListDataEventSelectorsResponse:
        runtime = RuntimeOptions()
        return self.list_data_event_selectors_with_options(request, runtime)

    async def list_data_event_selectors_async(
        self,
        request: main_models.ListDataEventSelectorsRequest,
    ) -> main_models.ListDataEventSelectorsResponse:
        runtime = RuntimeOptions()
        return await self.list_data_event_selectors_with_options_async(request, runtime)

    def list_data_event_services_with_options(
        self,
        request: main_models.ListDataEventServicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataEventServicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataEventServices',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataEventServicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_event_services_with_options_async(
        self,
        request: main_models.ListDataEventServicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataEventServicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataEventServices',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataEventServicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_event_services(
        self,
        request: main_models.ListDataEventServicesRequest,
    ) -> main_models.ListDataEventServicesResponse:
        runtime = RuntimeOptions()
        return self.list_data_event_services_with_options(request, runtime)

    async def list_data_event_services_async(
        self,
        request: main_models.ListDataEventServicesRequest,
    ) -> main_models.ListDataEventServicesResponse:
        runtime = RuntimeOptions()
        return await self.list_data_event_services_with_options_async(request, runtime)

    def list_delivery_history_jobs_with_options(
        self,
        request: main_models.ListDeliveryHistoryJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDeliveryHistoryJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDeliveryHistoryJobs',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDeliveryHistoryJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_delivery_history_jobs_with_options_async(
        self,
        request: main_models.ListDeliveryHistoryJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDeliveryHistoryJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDeliveryHistoryJobs',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDeliveryHistoryJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_delivery_history_jobs(
        self,
        request: main_models.ListDeliveryHistoryJobsRequest,
    ) -> main_models.ListDeliveryHistoryJobsResponse:
        runtime = RuntimeOptions()
        return self.list_delivery_history_jobs_with_options(request, runtime)

    async def list_delivery_history_jobs_async(
        self,
        request: main_models.ListDeliveryHistoryJobsRequest,
    ) -> main_models.ListDeliveryHistoryJobsResponse:
        runtime = RuntimeOptions()
        return await self.list_delivery_history_jobs_with_options_async(request, runtime)

    def lookup_events_with_options(
        self,
        request: main_models.LookupEventsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.LookupEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lookup_attribute):
            query['LookupAttribute'] = request.lookup_attribute
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'LookupEvents',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.LookupEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def lookup_events_with_options_async(
        self,
        request: main_models.LookupEventsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.LookupEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lookup_attribute):
            query['LookupAttribute'] = request.lookup_attribute
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'LookupEvents',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.LookupEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def lookup_events(
        self,
        request: main_models.LookupEventsRequest,
    ) -> main_models.LookupEventsResponse:
        runtime = RuntimeOptions()
        return self.lookup_events_with_options(request, runtime)

    async def lookup_events_async(
        self,
        request: main_models.LookupEventsRequest,
    ) -> main_models.LookupEventsResponse:
        runtime = RuntimeOptions()
        return await self.lookup_events_with_options_async(request, runtime)

    def lookup_insight_events_with_options(
        self,
        request: main_models.LookupInsightEventsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.LookupInsightEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lookup_attribute):
            query['LookupAttribute'] = request.lookup_attribute
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'LookupInsightEvents',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.LookupInsightEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def lookup_insight_events_with_options_async(
        self,
        request: main_models.LookupInsightEventsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.LookupInsightEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lookup_attribute):
            query['LookupAttribute'] = request.lookup_attribute
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'LookupInsightEvents',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.LookupInsightEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def lookup_insight_events(
        self,
        request: main_models.LookupInsightEventsRequest,
    ) -> main_models.LookupInsightEventsResponse:
        runtime = RuntimeOptions()
        return self.lookup_insight_events_with_options(request, runtime)

    async def lookup_insight_events_async(
        self,
        request: main_models.LookupInsightEventsRequest,
    ) -> main_models.LookupInsightEventsResponse:
        runtime = RuntimeOptions()
        return await self.lookup_insight_events_with_options_async(request, runtime)

    def put_data_event_selector_with_options(
        self,
        request: main_models.PutDataEventSelectorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PutDataEventSelectorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.event_selectors):
            query['EventSelectors'] = request.event_selectors
        if not DaraCore.is_null(request.is_trail_all_region):
            query['IsTrailAllRegion'] = request.is_trail_all_region
        if not DaraCore.is_null(request.trail_name):
            query['TrailName'] = request.trail_name
        if not DaraCore.is_null(request.trail_region_ids):
            query['TrailRegionIds'] = request.trail_region_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PutDataEventSelector',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutDataEventSelectorResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_data_event_selector_with_options_async(
        self,
        request: main_models.PutDataEventSelectorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PutDataEventSelectorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.event_selectors):
            query['EventSelectors'] = request.event_selectors
        if not DaraCore.is_null(request.is_trail_all_region):
            query['IsTrailAllRegion'] = request.is_trail_all_region
        if not DaraCore.is_null(request.trail_name):
            query['TrailName'] = request.trail_name
        if not DaraCore.is_null(request.trail_region_ids):
            query['TrailRegionIds'] = request.trail_region_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PutDataEventSelector',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutDataEventSelectorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_data_event_selector(
        self,
        request: main_models.PutDataEventSelectorRequest,
    ) -> main_models.PutDataEventSelectorResponse:
        runtime = RuntimeOptions()
        return self.put_data_event_selector_with_options(request, runtime)

    async def put_data_event_selector_async(
        self,
        request: main_models.PutDataEventSelectorRequest,
    ) -> main_models.PutDataEventSelectorResponse:
        runtime = RuntimeOptions()
        return await self.put_data_event_selector_with_options_async(request, runtime)

    def put_insight_selectors_with_options(
        self,
        request: main_models.PutInsightSelectorsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PutInsightSelectorsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.insight_selectors):
            query['InsightSelectors'] = request.insight_selectors
        if not DaraCore.is_null(request.trail_name):
            query['TrailName'] = request.trail_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PutInsightSelectors',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutInsightSelectorsResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_insight_selectors_with_options_async(
        self,
        request: main_models.PutInsightSelectorsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PutInsightSelectorsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.insight_selectors):
            query['InsightSelectors'] = request.insight_selectors
        if not DaraCore.is_null(request.trail_name):
            query['TrailName'] = request.trail_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PutInsightSelectors',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutInsightSelectorsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_insight_selectors(
        self,
        request: main_models.PutInsightSelectorsRequest,
    ) -> main_models.PutInsightSelectorsResponse:
        runtime = RuntimeOptions()
        return self.put_insight_selectors_with_options(request, runtime)

    async def put_insight_selectors_async(
        self,
        request: main_models.PutInsightSelectorsRequest,
    ) -> main_models.PutInsightSelectorsResponse:
        runtime = RuntimeOptions()
        return await self.put_insight_selectors_with_options_async(request, runtime)

    def start_logging_with_options(
        self,
        request: main_models.StartLoggingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartLoggingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartLogging',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartLoggingResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_logging_with_options_async(
        self,
        request: main_models.StartLoggingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartLoggingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartLogging',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartLoggingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_logging(
        self,
        request: main_models.StartLoggingRequest,
    ) -> main_models.StartLoggingResponse:
        runtime = RuntimeOptions()
        return self.start_logging_with_options(request, runtime)

    async def start_logging_async(
        self,
        request: main_models.StartLoggingRequest,
    ) -> main_models.StartLoggingResponse:
        runtime = RuntimeOptions()
        return await self.start_logging_with_options_async(request, runtime)

    def stop_logging_with_options(
        self,
        request: main_models.StopLoggingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopLoggingResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopLogging',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopLoggingResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_logging_with_options_async(
        self,
        request: main_models.StopLoggingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopLoggingResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopLogging',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopLoggingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_logging(
        self,
        request: main_models.StopLoggingRequest,
    ) -> main_models.StopLoggingResponse:
        runtime = RuntimeOptions()
        return self.stop_logging_with_options(request, runtime)

    async def stop_logging_async(
        self,
        request: main_models.StopLoggingRequest,
    ) -> main_models.StopLoggingResponse:
        runtime = RuntimeOptions()
        return await self.stop_logging_with_options_async(request, runtime)

    def update_advanced_query_template_with_options(
        self,
        request: main_models.UpdateAdvancedQueryTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAdvancedQueryTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.simple_query):
            query['SimpleQuery'] = request.simple_query
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.template_sql):
            query['TemplateSql'] = request.template_sql
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAdvancedQueryTemplate',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAdvancedQueryTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_advanced_query_template_with_options_async(
        self,
        request: main_models.UpdateAdvancedQueryTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAdvancedQueryTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.simple_query):
            query['SimpleQuery'] = request.simple_query
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.template_sql):
            query['TemplateSql'] = request.template_sql
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAdvancedQueryTemplate',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAdvancedQueryTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_advanced_query_template(
        self,
        request: main_models.UpdateAdvancedQueryTemplateRequest,
    ) -> main_models.UpdateAdvancedQueryTemplateResponse:
        runtime = RuntimeOptions()
        return self.update_advanced_query_template_with_options(request, runtime)

    async def update_advanced_query_template_async(
        self,
        request: main_models.UpdateAdvancedQueryTemplateRequest,
    ) -> main_models.UpdateAdvancedQueryTemplateResponse:
        runtime = RuntimeOptions()
        return await self.update_advanced_query_template_with_options_async(request, runtime)

    def update_global_events_storage_region_with_options(
        self,
        request: main_models.UpdateGlobalEventsStorageRegionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGlobalEventsStorageRegionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.storage_region):
            query['StorageRegion'] = request.storage_region
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGlobalEventsStorageRegion',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGlobalEventsStorageRegionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_global_events_storage_region_with_options_async(
        self,
        request: main_models.UpdateGlobalEventsStorageRegionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGlobalEventsStorageRegionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.storage_region):
            query['StorageRegion'] = request.storage_region
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGlobalEventsStorageRegion',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGlobalEventsStorageRegionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_global_events_storage_region(
        self,
        request: main_models.UpdateGlobalEventsStorageRegionRequest,
    ) -> main_models.UpdateGlobalEventsStorageRegionResponse:
        runtime = RuntimeOptions()
        return self.update_global_events_storage_region_with_options(request, runtime)

    async def update_global_events_storage_region_async(
        self,
        request: main_models.UpdateGlobalEventsStorageRegionRequest,
    ) -> main_models.UpdateGlobalEventsStorageRegionResponse:
        runtime = RuntimeOptions()
        return await self.update_global_events_storage_region_with_options_async(request, runtime)

    def update_trail_with_options(
        self,
        request: main_models.UpdateTrailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTrailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.event_rw):
            query['EventRW'] = request.event_rw
        if not DaraCore.is_null(request.max_compute_project_arn):
            query['MaxComputeProjectArn'] = request.max_compute_project_arn
        if not DaraCore.is_null(request.max_compute_write_role_arn):
            query['MaxComputeWriteRoleArn'] = request.max_compute_write_role_arn
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.oss_bucket_name):
            query['OssBucketName'] = request.oss_bucket_name
        if not DaraCore.is_null(request.oss_key_prefix):
            query['OssKeyPrefix'] = request.oss_key_prefix
        if not DaraCore.is_null(request.oss_write_role_arn):
            query['OssWriteRoleArn'] = request.oss_write_role_arn
        if not DaraCore.is_null(request.sls_project_arn):
            query['SlsProjectArn'] = request.sls_project_arn
        if not DaraCore.is_null(request.sls_write_role_arn):
            query['SlsWriteRoleArn'] = request.sls_write_role_arn
        if not DaraCore.is_null(request.trail_region):
            query['TrailRegion'] = request.trail_region
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTrail',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTrailResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_trail_with_options_async(
        self,
        request: main_models.UpdateTrailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTrailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.event_rw):
            query['EventRW'] = request.event_rw
        if not DaraCore.is_null(request.max_compute_project_arn):
            query['MaxComputeProjectArn'] = request.max_compute_project_arn
        if not DaraCore.is_null(request.max_compute_write_role_arn):
            query['MaxComputeWriteRoleArn'] = request.max_compute_write_role_arn
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.oss_bucket_name):
            query['OssBucketName'] = request.oss_bucket_name
        if not DaraCore.is_null(request.oss_key_prefix):
            query['OssKeyPrefix'] = request.oss_key_prefix
        if not DaraCore.is_null(request.oss_write_role_arn):
            query['OssWriteRoleArn'] = request.oss_write_role_arn
        if not DaraCore.is_null(request.sls_project_arn):
            query['SlsProjectArn'] = request.sls_project_arn
        if not DaraCore.is_null(request.sls_write_role_arn):
            query['SlsWriteRoleArn'] = request.sls_write_role_arn
        if not DaraCore.is_null(request.trail_region):
            query['TrailRegion'] = request.trail_region
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTrail',
            version = '2020-07-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTrailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_trail(
        self,
        request: main_models.UpdateTrailRequest,
    ) -> main_models.UpdateTrailResponse:
        runtime = RuntimeOptions()
        return self.update_trail_with_options(request, runtime)

    async def update_trail_async(
        self,
        request: main_models.UpdateTrailRequest,
    ) -> main_models.UpdateTrailResponse:
        runtime = RuntimeOptions()
        return await self.update_trail_with_options_async(request, runtime)
