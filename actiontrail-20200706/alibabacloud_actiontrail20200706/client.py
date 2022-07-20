# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_actiontrail20200706 import models as actiontrail_20200706_models
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
            'rus-west-1-pop': 'actiontrail.ap-northeast-1.aliyuncs.com'
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def create_delivery_history_job_with_options(
        self,
        request: actiontrail_20200706_models.CreateDeliveryHistoryJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.CreateDeliveryHistoryJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.trail_name):
            query['TrailName'] = request.trail_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDeliveryHistoryJob',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.CreateDeliveryHistoryJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_delivery_history_job_with_options_async(
        self,
        request: actiontrail_20200706_models.CreateDeliveryHistoryJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.CreateDeliveryHistoryJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.trail_name):
            query['TrailName'] = request.trail_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDeliveryHistoryJob',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.CreateDeliveryHistoryJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_delivery_history_job(
        self,
        request: actiontrail_20200706_models.CreateDeliveryHistoryJobRequest,
    ) -> actiontrail_20200706_models.CreateDeliveryHistoryJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_delivery_history_job_with_options(request, runtime)

    async def create_delivery_history_job_async(
        self,
        request: actiontrail_20200706_models.CreateDeliveryHistoryJobRequest,
    ) -> actiontrail_20200706_models.CreateDeliveryHistoryJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_delivery_history_job_with_options_async(request, runtime)

    def create_trail_with_options(
        self,
        request: actiontrail_20200706_models.CreateTrailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.CreateTrailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_rw):
            query['EventRW'] = request.event_rw
        if not UtilClient.is_unset(request.is_organization_trail):
            query['IsOrganizationTrail'] = request.is_organization_trail
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.oss_bucket_name):
            query['OssBucketName'] = request.oss_bucket_name
        if not UtilClient.is_unset(request.oss_key_prefix):
            query['OssKeyPrefix'] = request.oss_key_prefix
        if not UtilClient.is_unset(request.oss_write_role_arn):
            query['OssWriteRoleArn'] = request.oss_write_role_arn
        if not UtilClient.is_unset(request.sls_project_arn):
            query['SlsProjectArn'] = request.sls_project_arn
        if not UtilClient.is_unset(request.sls_write_role_arn):
            query['SlsWriteRoleArn'] = request.sls_write_role_arn
        if not UtilClient.is_unset(request.trail_region):
            query['TrailRegion'] = request.trail_region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTrail',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.CreateTrailResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_trail_with_options_async(
        self,
        request: actiontrail_20200706_models.CreateTrailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.CreateTrailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_rw):
            query['EventRW'] = request.event_rw
        if not UtilClient.is_unset(request.is_organization_trail):
            query['IsOrganizationTrail'] = request.is_organization_trail
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.oss_bucket_name):
            query['OssBucketName'] = request.oss_bucket_name
        if not UtilClient.is_unset(request.oss_key_prefix):
            query['OssKeyPrefix'] = request.oss_key_prefix
        if not UtilClient.is_unset(request.oss_write_role_arn):
            query['OssWriteRoleArn'] = request.oss_write_role_arn
        if not UtilClient.is_unset(request.sls_project_arn):
            query['SlsProjectArn'] = request.sls_project_arn
        if not UtilClient.is_unset(request.sls_write_role_arn):
            query['SlsWriteRoleArn'] = request.sls_write_role_arn
        if not UtilClient.is_unset(request.trail_region):
            query['TrailRegion'] = request.trail_region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTrail',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.CreateTrailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_trail(
        self,
        request: actiontrail_20200706_models.CreateTrailRequest,
    ) -> actiontrail_20200706_models.CreateTrailResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_trail_with_options(request, runtime)

    async def create_trail_async(
        self,
        request: actiontrail_20200706_models.CreateTrailRequest,
    ) -> actiontrail_20200706_models.CreateTrailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_trail_with_options_async(request, runtime)

    def delete_delivery_history_job_with_options(
        self,
        request: actiontrail_20200706_models.DeleteDeliveryHistoryJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.DeleteDeliveryHistoryJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDeliveryHistoryJob',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.DeleteDeliveryHistoryJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_delivery_history_job_with_options_async(
        self,
        request: actiontrail_20200706_models.DeleteDeliveryHistoryJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.DeleteDeliveryHistoryJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDeliveryHistoryJob',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.DeleteDeliveryHistoryJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_delivery_history_job(
        self,
        request: actiontrail_20200706_models.DeleteDeliveryHistoryJobRequest,
    ) -> actiontrail_20200706_models.DeleteDeliveryHistoryJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_delivery_history_job_with_options(request, runtime)

    async def delete_delivery_history_job_async(
        self,
        request: actiontrail_20200706_models.DeleteDeliveryHistoryJobRequest,
    ) -> actiontrail_20200706_models.DeleteDeliveryHistoryJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_delivery_history_job_with_options_async(request, runtime)

    def delete_trail_with_options(
        self,
        request: actiontrail_20200706_models.DeleteTrailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.DeleteTrailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTrail',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.DeleteTrailResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_trail_with_options_async(
        self,
        request: actiontrail_20200706_models.DeleteTrailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.DeleteTrailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTrail',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.DeleteTrailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_trail(
        self,
        request: actiontrail_20200706_models.DeleteTrailRequest,
    ) -> actiontrail_20200706_models.DeleteTrailResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_trail_with_options(request, runtime)

    async def delete_trail_async(
        self,
        request: actiontrail_20200706_models.DeleteTrailRequest,
    ) -> actiontrail_20200706_models.DeleteTrailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_trail_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: actiontrail_20200706_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: actiontrail_20200706_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: actiontrail_20200706_models.DescribeRegionsRequest,
    ) -> actiontrail_20200706_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: actiontrail_20200706_models.DescribeRegionsRequest,
    ) -> actiontrail_20200706_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_trails_with_options(
        self,
        request: actiontrail_20200706_models.DescribeTrailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.DescribeTrailsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.include_organization_trail):
            query['IncludeOrganizationTrail'] = request.include_organization_trail
        if not UtilClient.is_unset(request.include_shadow_trails):
            query['IncludeShadowTrails'] = request.include_shadow_trails
        if not UtilClient.is_unset(request.name_list):
            query['NameList'] = request.name_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTrails',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.DescribeTrailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_trails_with_options_async(
        self,
        request: actiontrail_20200706_models.DescribeTrailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.DescribeTrailsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.include_organization_trail):
            query['IncludeOrganizationTrail'] = request.include_organization_trail
        if not UtilClient.is_unset(request.include_shadow_trails):
            query['IncludeShadowTrails'] = request.include_shadow_trails
        if not UtilClient.is_unset(request.name_list):
            query['NameList'] = request.name_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTrails',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.DescribeTrailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_trails(
        self,
        request: actiontrail_20200706_models.DescribeTrailsRequest,
    ) -> actiontrail_20200706_models.DescribeTrailsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_trails_with_options(request, runtime)

    async def describe_trails_async(
        self,
        request: actiontrail_20200706_models.DescribeTrailsRequest,
    ) -> actiontrail_20200706_models.DescribeTrailsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_trails_with_options_async(request, runtime)

    def get_access_key_last_used_events_with_options(
        self,
        request: actiontrail_20200706_models.GetAccessKeyLastUsedEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.GetAccessKeyLastUsedEventsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_key):
            query['AccessKey'] = request.access_key
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAccessKeyLastUsedEvents',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.GetAccessKeyLastUsedEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_access_key_last_used_events_with_options_async(
        self,
        request: actiontrail_20200706_models.GetAccessKeyLastUsedEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.GetAccessKeyLastUsedEventsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_key):
            query['AccessKey'] = request.access_key
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAccessKeyLastUsedEvents',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.GetAccessKeyLastUsedEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_access_key_last_used_events(
        self,
        request: actiontrail_20200706_models.GetAccessKeyLastUsedEventsRequest,
    ) -> actiontrail_20200706_models.GetAccessKeyLastUsedEventsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_access_key_last_used_events_with_options(request, runtime)

    async def get_access_key_last_used_events_async(
        self,
        request: actiontrail_20200706_models.GetAccessKeyLastUsedEventsRequest,
    ) -> actiontrail_20200706_models.GetAccessKeyLastUsedEventsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_access_key_last_used_events_with_options_async(request, runtime)

    def get_access_key_last_used_info_with_options(
        self,
        request: actiontrail_20200706_models.GetAccessKeyLastUsedInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.GetAccessKeyLastUsedInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_key):
            query['AccessKey'] = request.access_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAccessKeyLastUsedInfo',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.GetAccessKeyLastUsedInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_access_key_last_used_info_with_options_async(
        self,
        request: actiontrail_20200706_models.GetAccessKeyLastUsedInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.GetAccessKeyLastUsedInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_key):
            query['AccessKey'] = request.access_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAccessKeyLastUsedInfo',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.GetAccessKeyLastUsedInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_access_key_last_used_info(
        self,
        request: actiontrail_20200706_models.GetAccessKeyLastUsedInfoRequest,
    ) -> actiontrail_20200706_models.GetAccessKeyLastUsedInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_access_key_last_used_info_with_options(request, runtime)

    async def get_access_key_last_used_info_async(
        self,
        request: actiontrail_20200706_models.GetAccessKeyLastUsedInfoRequest,
    ) -> actiontrail_20200706_models.GetAccessKeyLastUsedInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_access_key_last_used_info_with_options_async(request, runtime)

    def get_access_key_last_used_ips_with_options(
        self,
        request: actiontrail_20200706_models.GetAccessKeyLastUsedIpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.GetAccessKeyLastUsedIpsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_key):
            query['AccessKey'] = request.access_key
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAccessKeyLastUsedIps',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.GetAccessKeyLastUsedIpsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_access_key_last_used_ips_with_options_async(
        self,
        request: actiontrail_20200706_models.GetAccessKeyLastUsedIpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.GetAccessKeyLastUsedIpsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_key):
            query['AccessKey'] = request.access_key
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAccessKeyLastUsedIps',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.GetAccessKeyLastUsedIpsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_access_key_last_used_ips(
        self,
        request: actiontrail_20200706_models.GetAccessKeyLastUsedIpsRequest,
    ) -> actiontrail_20200706_models.GetAccessKeyLastUsedIpsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_access_key_last_used_ips_with_options(request, runtime)

    async def get_access_key_last_used_ips_async(
        self,
        request: actiontrail_20200706_models.GetAccessKeyLastUsedIpsRequest,
    ) -> actiontrail_20200706_models.GetAccessKeyLastUsedIpsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_access_key_last_used_ips_with_options_async(request, runtime)

    def get_access_key_last_used_products_with_options(
        self,
        request: actiontrail_20200706_models.GetAccessKeyLastUsedProductsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.GetAccessKeyLastUsedProductsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_key):
            query['AccessKey'] = request.access_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAccessKeyLastUsedProducts',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.GetAccessKeyLastUsedProductsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_access_key_last_used_products_with_options_async(
        self,
        request: actiontrail_20200706_models.GetAccessKeyLastUsedProductsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.GetAccessKeyLastUsedProductsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_key):
            query['AccessKey'] = request.access_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAccessKeyLastUsedProducts',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.GetAccessKeyLastUsedProductsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_access_key_last_used_products(
        self,
        request: actiontrail_20200706_models.GetAccessKeyLastUsedProductsRequest,
    ) -> actiontrail_20200706_models.GetAccessKeyLastUsedProductsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_access_key_last_used_products_with_options(request, runtime)

    async def get_access_key_last_used_products_async(
        self,
        request: actiontrail_20200706_models.GetAccessKeyLastUsedProductsRequest,
    ) -> actiontrail_20200706_models.GetAccessKeyLastUsedProductsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_access_key_last_used_products_with_options_async(request, runtime)

    def get_access_key_last_used_resources_with_options(
        self,
        request: actiontrail_20200706_models.GetAccessKeyLastUsedResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.GetAccessKeyLastUsedResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_key):
            query['AccessKey'] = request.access_key
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAccessKeyLastUsedResources',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.GetAccessKeyLastUsedResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_access_key_last_used_resources_with_options_async(
        self,
        request: actiontrail_20200706_models.GetAccessKeyLastUsedResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.GetAccessKeyLastUsedResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_key):
            query['AccessKey'] = request.access_key
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAccessKeyLastUsedResources',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.GetAccessKeyLastUsedResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_access_key_last_used_resources(
        self,
        request: actiontrail_20200706_models.GetAccessKeyLastUsedResourcesRequest,
    ) -> actiontrail_20200706_models.GetAccessKeyLastUsedResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_access_key_last_used_resources_with_options(request, runtime)

    async def get_access_key_last_used_resources_async(
        self,
        request: actiontrail_20200706_models.GetAccessKeyLastUsedResourcesRequest,
    ) -> actiontrail_20200706_models.GetAccessKeyLastUsedResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_access_key_last_used_resources_with_options_async(request, runtime)

    def get_delivery_history_job_with_options(
        self,
        request: actiontrail_20200706_models.GetDeliveryHistoryJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.GetDeliveryHistoryJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDeliveryHistoryJob',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.GetDeliveryHistoryJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_delivery_history_job_with_options_async(
        self,
        request: actiontrail_20200706_models.GetDeliveryHistoryJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.GetDeliveryHistoryJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDeliveryHistoryJob',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.GetDeliveryHistoryJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_delivery_history_job(
        self,
        request: actiontrail_20200706_models.GetDeliveryHistoryJobRequest,
    ) -> actiontrail_20200706_models.GetDeliveryHistoryJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_delivery_history_job_with_options(request, runtime)

    async def get_delivery_history_job_async(
        self,
        request: actiontrail_20200706_models.GetDeliveryHistoryJobRequest,
    ) -> actiontrail_20200706_models.GetDeliveryHistoryJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_delivery_history_job_with_options_async(request, runtime)

    def get_trail_status_with_options(
        self,
        request: actiontrail_20200706_models.GetTrailStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.GetTrailStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.is_organization_trail):
            query['IsOrganizationTrail'] = request.is_organization_trail
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTrailStatus',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.GetTrailStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_trail_status_with_options_async(
        self,
        request: actiontrail_20200706_models.GetTrailStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.GetTrailStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.is_organization_trail):
            query['IsOrganizationTrail'] = request.is_organization_trail
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTrailStatus',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.GetTrailStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_trail_status(
        self,
        request: actiontrail_20200706_models.GetTrailStatusRequest,
    ) -> actiontrail_20200706_models.GetTrailStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_trail_status_with_options(request, runtime)

    async def get_trail_status_async(
        self,
        request: actiontrail_20200706_models.GetTrailStatusRequest,
    ) -> actiontrail_20200706_models.GetTrailStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_trail_status_with_options_async(request, runtime)

    def list_delivery_history_jobs_with_options(
        self,
        request: actiontrail_20200706_models.ListDeliveryHistoryJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.ListDeliveryHistoryJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDeliveryHistoryJobs',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.ListDeliveryHistoryJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_delivery_history_jobs_with_options_async(
        self,
        request: actiontrail_20200706_models.ListDeliveryHistoryJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.ListDeliveryHistoryJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDeliveryHistoryJobs',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.ListDeliveryHistoryJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_delivery_history_jobs(
        self,
        request: actiontrail_20200706_models.ListDeliveryHistoryJobsRequest,
    ) -> actiontrail_20200706_models.ListDeliveryHistoryJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_delivery_history_jobs_with_options(request, runtime)

    async def list_delivery_history_jobs_async(
        self,
        request: actiontrail_20200706_models.ListDeliveryHistoryJobsRequest,
    ) -> actiontrail_20200706_models.ListDeliveryHistoryJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_delivery_history_jobs_with_options_async(request, runtime)

    def lookup_events_with_options(
        self,
        request: actiontrail_20200706_models.LookupEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.LookupEventsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.lookup_attribute):
            query['LookupAttribute'] = request.lookup_attribute
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LookupEvents',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.LookupEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def lookup_events_with_options_async(
        self,
        request: actiontrail_20200706_models.LookupEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.LookupEventsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.lookup_attribute):
            query['LookupAttribute'] = request.lookup_attribute
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LookupEvents',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.LookupEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def lookup_events(
        self,
        request: actiontrail_20200706_models.LookupEventsRequest,
    ) -> actiontrail_20200706_models.LookupEventsResponse:
        runtime = util_models.RuntimeOptions()
        return self.lookup_events_with_options(request, runtime)

    async def lookup_events_async(
        self,
        request: actiontrail_20200706_models.LookupEventsRequest,
    ) -> actiontrail_20200706_models.LookupEventsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.lookup_events_with_options_async(request, runtime)

    def start_logging_with_options(
        self,
        request: actiontrail_20200706_models.StartLoggingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.StartLoggingResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartLogging',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.StartLoggingResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_logging_with_options_async(
        self,
        request: actiontrail_20200706_models.StartLoggingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.StartLoggingResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartLogging',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.StartLoggingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_logging(
        self,
        request: actiontrail_20200706_models.StartLoggingRequest,
    ) -> actiontrail_20200706_models.StartLoggingResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_logging_with_options(request, runtime)

    async def start_logging_async(
        self,
        request: actiontrail_20200706_models.StartLoggingRequest,
    ) -> actiontrail_20200706_models.StartLoggingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_logging_with_options_async(request, runtime)

    def stop_logging_with_options(
        self,
        request: actiontrail_20200706_models.StopLoggingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.StopLoggingResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopLogging',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.StopLoggingResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_logging_with_options_async(
        self,
        request: actiontrail_20200706_models.StopLoggingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.StopLoggingResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopLogging',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.StopLoggingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_logging(
        self,
        request: actiontrail_20200706_models.StopLoggingRequest,
    ) -> actiontrail_20200706_models.StopLoggingResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_logging_with_options(request, runtime)

    async def stop_logging_async(
        self,
        request: actiontrail_20200706_models.StopLoggingRequest,
    ) -> actiontrail_20200706_models.StopLoggingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_logging_with_options_async(request, runtime)

    def update_trail_with_options(
        self,
        request: actiontrail_20200706_models.UpdateTrailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.UpdateTrailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_rw):
            query['EventRW'] = request.event_rw
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.oss_bucket_name):
            query['OssBucketName'] = request.oss_bucket_name
        if not UtilClient.is_unset(request.oss_key_prefix):
            query['OssKeyPrefix'] = request.oss_key_prefix
        if not UtilClient.is_unset(request.oss_write_role_arn):
            query['OssWriteRoleArn'] = request.oss_write_role_arn
        if not UtilClient.is_unset(request.sls_project_arn):
            query['SlsProjectArn'] = request.sls_project_arn
        if not UtilClient.is_unset(request.sls_write_role_arn):
            query['SlsWriteRoleArn'] = request.sls_write_role_arn
        if not UtilClient.is_unset(request.trail_region):
            query['TrailRegion'] = request.trail_region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateTrail',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.UpdateTrailResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_trail_with_options_async(
        self,
        request: actiontrail_20200706_models.UpdateTrailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.UpdateTrailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_rw):
            query['EventRW'] = request.event_rw
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.oss_bucket_name):
            query['OssBucketName'] = request.oss_bucket_name
        if not UtilClient.is_unset(request.oss_key_prefix):
            query['OssKeyPrefix'] = request.oss_key_prefix
        if not UtilClient.is_unset(request.oss_write_role_arn):
            query['OssWriteRoleArn'] = request.oss_write_role_arn
        if not UtilClient.is_unset(request.sls_project_arn):
            query['SlsProjectArn'] = request.sls_project_arn
        if not UtilClient.is_unset(request.sls_write_role_arn):
            query['SlsWriteRoleArn'] = request.sls_write_role_arn
        if not UtilClient.is_unset(request.trail_region):
            query['TrailRegion'] = request.trail_region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateTrail',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.UpdateTrailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_trail(
        self,
        request: actiontrail_20200706_models.UpdateTrailRequest,
    ) -> actiontrail_20200706_models.UpdateTrailResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_trail_with_options(request, runtime)

    async def update_trail_async(
        self,
        request: actiontrail_20200706_models.UpdateTrailRequest,
    ) -> actiontrail_20200706_models.UpdateTrailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_trail_with_options_async(request, runtime)
