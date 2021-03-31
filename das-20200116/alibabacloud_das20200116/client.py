# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_das20200116 import models as das20200116_models
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
        self._endpoint_rule = 'central'
        self._endpoint_map = {
            'cn-shanghai': 'das.cn-shanghai.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('das', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def access_hdminstance_with_options(
        self,
        request: das20200116_models.AccessHDMInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.AccessHDMInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.AccessHDMInstanceResponse(),
            self.do_rpcrequest('AccessHDMInstance', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def access_hdminstance_with_options_async(
        self,
        request: das20200116_models.AccessHDMInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.AccessHDMInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.AccessHDMInstanceResponse(),
            await self.do_rpcrequest_async('AccessHDMInstance', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def access_hdminstance(
        self,
        request: das20200116_models.AccessHDMInstanceRequest,
    ) -> das20200116_models.AccessHDMInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.access_hdminstance_with_options(request, runtime)

    async def access_hdminstance_async(
        self,
        request: das20200116_models.AccessHDMInstanceRequest,
    ) -> das20200116_models.AccessHDMInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.access_hdminstance_with_options_async(request, runtime)

    def add_hdminstance_with_options(
        self,
        request: das20200116_models.AddHDMInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.AddHDMInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.AddHDMInstanceResponse(),
            self.do_rpcrequest('AddHDMInstance', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_hdminstance_with_options_async(
        self,
        request: das20200116_models.AddHDMInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.AddHDMInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.AddHDMInstanceResponse(),
            await self.do_rpcrequest_async('AddHDMInstance', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_hdminstance(
        self,
        request: das20200116_models.AddHDMInstanceRequest,
    ) -> das20200116_models.AddHDMInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_hdminstance_with_options(request, runtime)

    async def add_hdminstance_async(
        self,
        request: das20200116_models.AddHDMInstanceRequest,
    ) -> das20200116_models.AddHDMInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_hdminstance_with_options_async(request, runtime)

    def create_cache_analysis_job_with_options(
        self,
        request: das20200116_models.CreateCacheAnalysisJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.CreateCacheAnalysisJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.CreateCacheAnalysisJobResponse(),
            self.do_rpcrequest('CreateCacheAnalysisJob', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_cache_analysis_job_with_options_async(
        self,
        request: das20200116_models.CreateCacheAnalysisJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.CreateCacheAnalysisJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.CreateCacheAnalysisJobResponse(),
            await self.do_rpcrequest_async('CreateCacheAnalysisJob', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_cache_analysis_job(
        self,
        request: das20200116_models.CreateCacheAnalysisJobRequest,
    ) -> das20200116_models.CreateCacheAnalysisJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_cache_analysis_job_with_options(request, runtime)

    async def create_cache_analysis_job_async(
        self,
        request: das20200116_models.CreateCacheAnalysisJobRequest,
    ) -> das20200116_models.CreateCacheAnalysisJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_cache_analysis_job_with_options_async(request, runtime)

    def create_diagnostic_report_with_options(
        self,
        request: das20200116_models.CreateDiagnosticReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.CreateDiagnosticReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.CreateDiagnosticReportResponse(),
            self.do_rpcrequest('CreateDiagnosticReport', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_diagnostic_report_with_options_async(
        self,
        request: das20200116_models.CreateDiagnosticReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.CreateDiagnosticReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.CreateDiagnosticReportResponse(),
            await self.do_rpcrequest_async('CreateDiagnosticReport', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_diagnostic_report(
        self,
        request: das20200116_models.CreateDiagnosticReportRequest,
    ) -> das20200116_models.CreateDiagnosticReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_diagnostic_report_with_options(request, runtime)

    async def create_diagnostic_report_async(
        self,
        request: das20200116_models.CreateDiagnosticReportRequest,
    ) -> das20200116_models.CreateDiagnosticReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_diagnostic_report_with_options_async(request, runtime)

    def describe_cache_analysis_job_with_options(
        self,
        request: das20200116_models.DescribeCacheAnalysisJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeCacheAnalysisJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.DescribeCacheAnalysisJobResponse(),
            self.do_rpcrequest('DescribeCacheAnalysisJob', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cache_analysis_job_with_options_async(
        self,
        request: das20200116_models.DescribeCacheAnalysisJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeCacheAnalysisJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.DescribeCacheAnalysisJobResponse(),
            await self.do_rpcrequest_async('DescribeCacheAnalysisJob', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cache_analysis_job(
        self,
        request: das20200116_models.DescribeCacheAnalysisJobRequest,
    ) -> das20200116_models.DescribeCacheAnalysisJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cache_analysis_job_with_options(request, runtime)

    async def describe_cache_analysis_job_async(
        self,
        request: das20200116_models.DescribeCacheAnalysisJobRequest,
    ) -> das20200116_models.DescribeCacheAnalysisJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cache_analysis_job_with_options_async(request, runtime)

    def describe_cache_analysis_jobs_with_options(
        self,
        request: das20200116_models.DescribeCacheAnalysisJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeCacheAnalysisJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.DescribeCacheAnalysisJobsResponse(),
            self.do_rpcrequest('DescribeCacheAnalysisJobs', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cache_analysis_jobs_with_options_async(
        self,
        request: das20200116_models.DescribeCacheAnalysisJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeCacheAnalysisJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.DescribeCacheAnalysisJobsResponse(),
            await self.do_rpcrequest_async('DescribeCacheAnalysisJobs', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cache_analysis_jobs(
        self,
        request: das20200116_models.DescribeCacheAnalysisJobsRequest,
    ) -> das20200116_models.DescribeCacheAnalysisJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cache_analysis_jobs_with_options(request, runtime)

    async def describe_cache_analysis_jobs_async(
        self,
        request: das20200116_models.DescribeCacheAnalysisJobsRequest,
    ) -> das20200116_models.DescribeCacheAnalysisJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cache_analysis_jobs_with_options_async(request, runtime)

    def describe_diagnostic_report_list_with_options(
        self,
        request: das20200116_models.DescribeDiagnosticReportListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeDiagnosticReportListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.DescribeDiagnosticReportListResponse(),
            self.do_rpcrequest('DescribeDiagnosticReportList', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_diagnostic_report_list_with_options_async(
        self,
        request: das20200116_models.DescribeDiagnosticReportListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeDiagnosticReportListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.DescribeDiagnosticReportListResponse(),
            await self.do_rpcrequest_async('DescribeDiagnosticReportList', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_diagnostic_report_list(
        self,
        request: das20200116_models.DescribeDiagnosticReportListRequest,
    ) -> das20200116_models.DescribeDiagnosticReportListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_diagnostic_report_list_with_options(request, runtime)

    async def describe_diagnostic_report_list_async(
        self,
        request: das20200116_models.DescribeDiagnosticReportListRequest,
    ) -> das20200116_models.DescribeDiagnosticReportListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_diagnostic_report_list_with_options_async(request, runtime)

    def describe_hot_keys_with_options(
        self,
        request: das20200116_models.DescribeHotKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeHotKeysResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.DescribeHotKeysResponse(),
            self.do_rpcrequest('DescribeHotKeys', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_hot_keys_with_options_async(
        self,
        request: das20200116_models.DescribeHotKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeHotKeysResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.DescribeHotKeysResponse(),
            await self.do_rpcrequest_async('DescribeHotKeys', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_hot_keys(
        self,
        request: das20200116_models.DescribeHotKeysRequest,
    ) -> das20200116_models.DescribeHotKeysResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_hot_keys_with_options(request, runtime)

    async def describe_hot_keys_async(
        self,
        request: das20200116_models.DescribeHotKeysRequest,
    ) -> das20200116_models.DescribeHotKeysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_hot_keys_with_options_async(request, runtime)

    def get_autonomous_notify_event_content_with_options(
        self,
        request: das20200116_models.GetAutonomousNotifyEventContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetAutonomousNotifyEventContentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.GetAutonomousNotifyEventContentResponse(),
            self.do_rpcrequest('GetAutonomousNotifyEventContent', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_autonomous_notify_event_content_with_options_async(
        self,
        request: das20200116_models.GetAutonomousNotifyEventContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetAutonomousNotifyEventContentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.GetAutonomousNotifyEventContentResponse(),
            await self.do_rpcrequest_async('GetAutonomousNotifyEventContent', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_autonomous_notify_event_content(
        self,
        request: das20200116_models.GetAutonomousNotifyEventContentRequest,
    ) -> das20200116_models.GetAutonomousNotifyEventContentResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_autonomous_notify_event_content_with_options(request, runtime)

    async def get_autonomous_notify_event_content_async(
        self,
        request: das20200116_models.GetAutonomousNotifyEventContentRequest,
    ) -> das20200116_models.GetAutonomousNotifyEventContentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_autonomous_notify_event_content_with_options_async(request, runtime)

    def get_autonomous_notify_event_detail_with_options(
        self,
        request: das20200116_models.GetAutonomousNotifyEventDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetAutonomousNotifyEventDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.GetAutonomousNotifyEventDetailResponse(),
            self.do_rpcrequest('GetAutonomousNotifyEventDetail', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_autonomous_notify_event_detail_with_options_async(
        self,
        request: das20200116_models.GetAutonomousNotifyEventDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetAutonomousNotifyEventDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.GetAutonomousNotifyEventDetailResponse(),
            await self.do_rpcrequest_async('GetAutonomousNotifyEventDetail', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_autonomous_notify_event_detail(
        self,
        request: das20200116_models.GetAutonomousNotifyEventDetailRequest,
    ) -> das20200116_models.GetAutonomousNotifyEventDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_autonomous_notify_event_detail_with_options(request, runtime)

    async def get_autonomous_notify_event_detail_async(
        self,
        request: das20200116_models.GetAutonomousNotifyEventDetailRequest,
    ) -> das20200116_models.GetAutonomousNotifyEventDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_autonomous_notify_event_detail_with_options_async(request, runtime)

    def get_autonomous_notify_events_with_options(
        self,
        request: das20200116_models.GetAutonomousNotifyEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetAutonomousNotifyEventsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.GetAutonomousNotifyEventsResponse(),
            self.do_rpcrequest('GetAutonomousNotifyEvents', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_autonomous_notify_events_with_options_async(
        self,
        request: das20200116_models.GetAutonomousNotifyEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetAutonomousNotifyEventsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.GetAutonomousNotifyEventsResponse(),
            await self.do_rpcrequest_async('GetAutonomousNotifyEvents', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_autonomous_notify_events(
        self,
        request: das20200116_models.GetAutonomousNotifyEventsRequest,
    ) -> das20200116_models.GetAutonomousNotifyEventsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_autonomous_notify_events_with_options(request, runtime)

    async def get_autonomous_notify_events_async(
        self,
        request: das20200116_models.GetAutonomousNotifyEventsRequest,
    ) -> das20200116_models.GetAutonomousNotifyEventsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_autonomous_notify_events_with_options_async(request, runtime)

    def get_autonomous_notify_events_in_range_with_options(
        self,
        request: das20200116_models.GetAutonomousNotifyEventsInRangeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetAutonomousNotifyEventsInRangeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.GetAutonomousNotifyEventsInRangeResponse(),
            self.do_rpcrequest('GetAutonomousNotifyEventsInRange', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_autonomous_notify_events_in_range_with_options_async(
        self,
        request: das20200116_models.GetAutonomousNotifyEventsInRangeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetAutonomousNotifyEventsInRangeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.GetAutonomousNotifyEventsInRangeResponse(),
            await self.do_rpcrequest_async('GetAutonomousNotifyEventsInRange', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_autonomous_notify_events_in_range(
        self,
        request: das20200116_models.GetAutonomousNotifyEventsInRangeRequest,
    ) -> das20200116_models.GetAutonomousNotifyEventsInRangeResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_autonomous_notify_events_in_range_with_options(request, runtime)

    async def get_autonomous_notify_events_in_range_async(
        self,
        request: das20200116_models.GetAutonomousNotifyEventsInRangeRequest,
    ) -> das20200116_models.GetAutonomousNotifyEventsInRangeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_autonomous_notify_events_in_range_with_options_async(request, runtime)

    def get_auto_resource_optimize_config_with_options(
        self,
        request: das20200116_models.GetAutoResourceOptimizeConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetAutoResourceOptimizeConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.GetAutoResourceOptimizeConfigResponse(),
            self.do_rpcrequest('GetAutoResourceOptimizeConfig', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_auto_resource_optimize_config_with_options_async(
        self,
        request: das20200116_models.GetAutoResourceOptimizeConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetAutoResourceOptimizeConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.GetAutoResourceOptimizeConfigResponse(),
            await self.do_rpcrequest_async('GetAutoResourceOptimizeConfig', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_auto_resource_optimize_config(
        self,
        request: das20200116_models.GetAutoResourceOptimizeConfigRequest,
    ) -> das20200116_models.GetAutoResourceOptimizeConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_auto_resource_optimize_config_with_options(request, runtime)

    async def get_auto_resource_optimize_config_async(
        self,
        request: das20200116_models.GetAutoResourceOptimizeConfigRequest,
    ) -> das20200116_models.GetAutoResourceOptimizeConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_auto_resource_optimize_config_with_options_async(request, runtime)

    def get_endpoint_switch_task_with_options(
        self,
        request: das20200116_models.GetEndpointSwitchTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetEndpointSwitchTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.GetEndpointSwitchTaskResponse(),
            self.do_rpcrequest('GetEndpointSwitchTask', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_endpoint_switch_task_with_options_async(
        self,
        request: das20200116_models.GetEndpointSwitchTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetEndpointSwitchTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.GetEndpointSwitchTaskResponse(),
            await self.do_rpcrequest_async('GetEndpointSwitchTask', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_endpoint_switch_task(
        self,
        request: das20200116_models.GetEndpointSwitchTaskRequest,
    ) -> das20200116_models.GetEndpointSwitchTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_endpoint_switch_task_with_options(request, runtime)

    async def get_endpoint_switch_task_async(
        self,
        request: das20200116_models.GetEndpointSwitchTaskRequest,
    ) -> das20200116_models.GetEndpointSwitchTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_endpoint_switch_task_with_options_async(request, runtime)

    def get_event_overview_with_options(
        self,
        request: das20200116_models.GetEventOverviewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetEventOverviewResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.GetEventOverviewResponse(),
            self.do_rpcrequest('GetEventOverview', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_event_overview_with_options_async(
        self,
        request: das20200116_models.GetEventOverviewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetEventOverviewResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.GetEventOverviewResponse(),
            await self.do_rpcrequest_async('GetEventOverview', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_event_overview(
        self,
        request: das20200116_models.GetEventOverviewRequest,
    ) -> das20200116_models.GetEventOverviewResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_event_overview_with_options(request, runtime)

    async def get_event_overview_async(
        self,
        request: das20200116_models.GetEventOverviewRequest,
    ) -> das20200116_models.GetEventOverviewResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_event_overview_with_options_async(request, runtime)

    def get_hdmaliyun_resource_sync_result_with_options(
        self,
        request: das20200116_models.GetHDMAliyunResourceSyncResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetHDMAliyunResourceSyncResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.GetHDMAliyunResourceSyncResultResponse(),
            self.do_rpcrequest('GetHDMAliyunResourceSyncResult', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_hdmaliyun_resource_sync_result_with_options_async(
        self,
        request: das20200116_models.GetHDMAliyunResourceSyncResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetHDMAliyunResourceSyncResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.GetHDMAliyunResourceSyncResultResponse(),
            await self.do_rpcrequest_async('GetHDMAliyunResourceSyncResult', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_hdmaliyun_resource_sync_result(
        self,
        request: das20200116_models.GetHDMAliyunResourceSyncResultRequest,
    ) -> das20200116_models.GetHDMAliyunResourceSyncResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_hdmaliyun_resource_sync_result_with_options(request, runtime)

    async def get_hdmaliyun_resource_sync_result_async(
        self,
        request: das20200116_models.GetHDMAliyunResourceSyncResultRequest,
    ) -> das20200116_models.GetHDMAliyunResourceSyncResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_hdmaliyun_resource_sync_result_with_options_async(request, runtime)

    def get_hdmlast_aliyun_resource_sync_result_with_options(
        self,
        request: das20200116_models.GetHDMLastAliyunResourceSyncResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetHDMLastAliyunResourceSyncResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.GetHDMLastAliyunResourceSyncResultResponse(),
            self.do_rpcrequest('GetHDMLastAliyunResourceSyncResult', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_hdmlast_aliyun_resource_sync_result_with_options_async(
        self,
        request: das20200116_models.GetHDMLastAliyunResourceSyncResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetHDMLastAliyunResourceSyncResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.GetHDMLastAliyunResourceSyncResultResponse(),
            await self.do_rpcrequest_async('GetHDMLastAliyunResourceSyncResult', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_hdmlast_aliyun_resource_sync_result(
        self,
        request: das20200116_models.GetHDMLastAliyunResourceSyncResultRequest,
    ) -> das20200116_models.GetHDMLastAliyunResourceSyncResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_hdmlast_aliyun_resource_sync_result_with_options(request, runtime)

    async def get_hdmlast_aliyun_resource_sync_result_async(
        self,
        request: das20200116_models.GetHDMLastAliyunResourceSyncResultRequest,
    ) -> das20200116_models.GetHDMLastAliyunResourceSyncResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_hdmlast_aliyun_resource_sync_result_with_options_async(request, runtime)

    def get_instance_inspections_with_options(
        self,
        request: das20200116_models.GetInstanceInspectionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetInstanceInspectionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.GetInstanceInspectionsResponse(),
            self.do_rpcrequest('GetInstanceInspections', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_instance_inspections_with_options_async(
        self,
        request: das20200116_models.GetInstanceInspectionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetInstanceInspectionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.GetInstanceInspectionsResponse(),
            await self.do_rpcrequest_async('GetInstanceInspections', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_instance_inspections(
        self,
        request: das20200116_models.GetInstanceInspectionsRequest,
    ) -> das20200116_models.GetInstanceInspectionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_instance_inspections_with_options(request, runtime)

    async def get_instance_inspections_async(
        self,
        request: das20200116_models.GetInstanceInspectionsRequest,
    ) -> das20200116_models.GetInstanceInspectionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_instance_inspections_with_options_async(request, runtime)

    def get_resource_optimize_history_list_with_options(
        self,
        request: das20200116_models.GetResourceOptimizeHistoryListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetResourceOptimizeHistoryListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.GetResourceOptimizeHistoryListResponse(),
            self.do_rpcrequest('GetResourceOptimizeHistoryList', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_resource_optimize_history_list_with_options_async(
        self,
        request: das20200116_models.GetResourceOptimizeHistoryListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetResourceOptimizeHistoryListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.GetResourceOptimizeHistoryListResponse(),
            await self.do_rpcrequest_async('GetResourceOptimizeHistoryList', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_resource_optimize_history_list(
        self,
        request: das20200116_models.GetResourceOptimizeHistoryListRequest,
    ) -> das20200116_models.GetResourceOptimizeHistoryListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_resource_optimize_history_list_with_options(request, runtime)

    async def get_resource_optimize_history_list_async(
        self,
        request: das20200116_models.GetResourceOptimizeHistoryListRequest,
    ) -> das20200116_models.GetResourceOptimizeHistoryListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_resource_optimize_history_list_with_options_async(request, runtime)

    def stop_or_rollback_optimize_task_with_options(
        self,
        request: das20200116_models.StopOrRollbackOptimizeTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.StopOrRollbackOptimizeTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.StopOrRollbackOptimizeTaskResponse(),
            self.do_rpcrequest('StopOrRollbackOptimizeTask', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def stop_or_rollback_optimize_task_with_options_async(
        self,
        request: das20200116_models.StopOrRollbackOptimizeTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.StopOrRollbackOptimizeTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.StopOrRollbackOptimizeTaskResponse(),
            await self.do_rpcrequest_async('StopOrRollbackOptimizeTask', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_or_rollback_optimize_task(
        self,
        request: das20200116_models.StopOrRollbackOptimizeTaskRequest,
    ) -> das20200116_models.StopOrRollbackOptimizeTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_or_rollback_optimize_task_with_options(request, runtime)

    async def stop_or_rollback_optimize_task_async(
        self,
        request: das20200116_models.StopOrRollbackOptimizeTaskRequest,
    ) -> das20200116_models.StopOrRollbackOptimizeTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_or_rollback_optimize_task_with_options_async(request, runtime)

    def sync_hdmaliyun_resource_with_options(
        self,
        request: das20200116_models.SyncHDMAliyunResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.SyncHDMAliyunResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.SyncHDMAliyunResourceResponse(),
            self.do_rpcrequest('SyncHDMAliyunResource', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def sync_hdmaliyun_resource_with_options_async(
        self,
        request: das20200116_models.SyncHDMAliyunResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.SyncHDMAliyunResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.SyncHDMAliyunResourceResponse(),
            await self.do_rpcrequest_async('SyncHDMAliyunResource', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def sync_hdmaliyun_resource(
        self,
        request: das20200116_models.SyncHDMAliyunResourceRequest,
    ) -> das20200116_models.SyncHDMAliyunResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.sync_hdmaliyun_resource_with_options(request, runtime)

    async def sync_hdmaliyun_resource_async(
        self,
        request: das20200116_models.SyncHDMAliyunResourceRequest,
    ) -> das20200116_models.SyncHDMAliyunResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.sync_hdmaliyun_resource_with_options_async(request, runtime)

    def turn_off_auto_resource_optimize_with_options(
        self,
        request: das20200116_models.TurnOffAutoResourceOptimizeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.TurnOffAutoResourceOptimizeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.TurnOffAutoResourceOptimizeResponse(),
            self.do_rpcrequest('TurnOffAutoResourceOptimize', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def turn_off_auto_resource_optimize_with_options_async(
        self,
        request: das20200116_models.TurnOffAutoResourceOptimizeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.TurnOffAutoResourceOptimizeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.TurnOffAutoResourceOptimizeResponse(),
            await self.do_rpcrequest_async('TurnOffAutoResourceOptimize', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def turn_off_auto_resource_optimize(
        self,
        request: das20200116_models.TurnOffAutoResourceOptimizeRequest,
    ) -> das20200116_models.TurnOffAutoResourceOptimizeResponse:
        runtime = util_models.RuntimeOptions()
        return self.turn_off_auto_resource_optimize_with_options(request, runtime)

    async def turn_off_auto_resource_optimize_async(
        self,
        request: das20200116_models.TurnOffAutoResourceOptimizeRequest,
    ) -> das20200116_models.TurnOffAutoResourceOptimizeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.turn_off_auto_resource_optimize_with_options_async(request, runtime)

    def update_auto_resource_optimize_config_with_options(
        self,
        request: das20200116_models.UpdateAutoResourceOptimizeConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.UpdateAutoResourceOptimizeConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.UpdateAutoResourceOptimizeConfigResponse(),
            self.do_rpcrequest('UpdateAutoResourceOptimizeConfig', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_auto_resource_optimize_config_with_options_async(
        self,
        request: das20200116_models.UpdateAutoResourceOptimizeConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.UpdateAutoResourceOptimizeConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.UpdateAutoResourceOptimizeConfigResponse(),
            await self.do_rpcrequest_async('UpdateAutoResourceOptimizeConfig', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_auto_resource_optimize_config(
        self,
        request: das20200116_models.UpdateAutoResourceOptimizeConfigRequest,
    ) -> das20200116_models.UpdateAutoResourceOptimizeConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_auto_resource_optimize_config_with_options(request, runtime)

    async def update_auto_resource_optimize_config_async(
        self,
        request: das20200116_models.UpdateAutoResourceOptimizeConfigRequest,
    ) -> das20200116_models.UpdateAutoResourceOptimizeConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_auto_resource_optimize_config_with_options_async(request, runtime)
