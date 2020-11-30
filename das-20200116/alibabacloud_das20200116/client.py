# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.core import TeaCore

from alibabacloud_tea_rpc.client import Client as RPCClient
from alibabacloud_das20200116 import models as das20200116_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_tea_util import models as util_models
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient


class Client(RPCClient):
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = 'central'
        self._endpoint_map = {
            'cn-shanghai': 'das.cn-shanghai.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('das', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_event_overview_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return das20200116_models.GetEventOverviewResponse().from_map(self.do_request('GetEventOverview', 'HTTPS', 'POST', '2020-01-16', 'AK', None, TeaCore.to_map(request), runtime))

    def get_event_overview(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_event_overview_with_options(request, runtime)

    def describe_hot_keys_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return das20200116_models.DescribeHotKeysResponse().from_map(self.do_request('DescribeHotKeys', 'HTTPS', 'POST', '2020-01-16', 'AK', None, TeaCore.to_map(request), runtime))

    def describe_hot_keys(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_hot_keys_with_options(request, runtime)

    def get_autonomous_notify_event_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return das20200116_models.GetAutonomousNotifyEventDetailResponse().from_map(self.do_request('GetAutonomousNotifyEventDetail', 'HTTPS', 'POST', '2020-01-16', 'AK', None, TeaCore.to_map(request), runtime))

    def get_autonomous_notify_event_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_autonomous_notify_event_detail_with_options(request, runtime)

    def get_autonomous_notify_events_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return das20200116_models.GetAutonomousNotifyEventsResponse().from_map(self.do_request('GetAutonomousNotifyEvents', 'HTTPS', 'POST', '2020-01-16', 'AK', None, TeaCore.to_map(request), runtime))

    def get_autonomous_notify_events(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_autonomous_notify_events_with_options(request, runtime)

    def create_cache_analysis_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return das20200116_models.CreateCacheAnalysisJobResponse().from_map(self.do_request('CreateCacheAnalysisJob', 'HTTPS', 'POST', '2020-01-16', 'AK', None, TeaCore.to_map(request), runtime))

    def create_cache_analysis_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_cache_analysis_job_with_options(request, runtime)

    def describe_cache_analysis_jobs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return das20200116_models.DescribeCacheAnalysisJobsResponse().from_map(self.do_request('DescribeCacheAnalysisJobs', 'HTTPS', 'POST', '2020-01-16', 'AK', None, TeaCore.to_map(request), runtime))

    def describe_cache_analysis_jobs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cache_analysis_jobs_with_options(request, runtime)

    def describe_cache_analysis_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return das20200116_models.DescribeCacheAnalysisJobResponse().from_map(self.do_request('DescribeCacheAnalysisJob', 'HTTPS', 'POST', '2020-01-16', 'AK', None, TeaCore.to_map(request), runtime))

    def describe_cache_analysis_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cache_analysis_job_with_options(request, runtime)

    def describe_diagnostic_report_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return das20200116_models.DescribeDiagnosticReportListResponse().from_map(self.do_request('DescribeDiagnosticReportList', 'HTTPS', 'POST', '2020-01-16', 'AK', None, TeaCore.to_map(request), runtime))

    def describe_diagnostic_report_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_diagnostic_report_list_with_options(request, runtime)

    def create_diagnostic_report_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return das20200116_models.CreateDiagnosticReportResponse().from_map(self.do_request('CreateDiagnosticReport', 'HTTPS', 'POST', '2020-01-16', 'AK', None, TeaCore.to_map(request), runtime))

    def create_diagnostic_report(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_diagnostic_report_with_options(request, runtime)

    def access_hdminstance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return das20200116_models.AccessHDMInstanceResponse().from_map(self.do_request('AccessHDMInstance', 'HTTPS', 'POST', '2020-01-16', 'AK', None, TeaCore.to_map(request), runtime))

    def access_hdminstance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.access_hdminstance_with_options(request, runtime)

    def sync_hdmaliyun_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return das20200116_models.SyncHDMAliyunResourceResponse().from_map(self.do_request('SyncHDMAliyunResource', 'HTTPS', 'POST', '2020-01-16', 'AK', None, TeaCore.to_map(request), runtime))

    def sync_hdmaliyun_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.sync_hdmaliyun_resource_with_options(request, runtime)

    def get_hdmlast_aliyun_resource_sync_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return das20200116_models.GetHDMLastAliyunResourceSyncResultResponse().from_map(self.do_request('GetHDMLastAliyunResourceSyncResult', 'HTTPS', 'POST', '2020-01-16', 'AK', None, TeaCore.to_map(request), runtime))

    def get_hdmlast_aliyun_resource_sync_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_hdmlast_aliyun_resource_sync_result_with_options(request, runtime)

    def get_endpoint_switch_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return das20200116_models.GetEndpointSwitchTaskResponse().from_map(self.do_request('GetEndpointSwitchTask', 'HTTPS', 'POST', '2020-01-16', 'AK', None, TeaCore.to_map(request), runtime))

    def get_endpoint_switch_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_endpoint_switch_task_with_options(request, runtime)

    def get_hdmaliyun_resource_sync_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return das20200116_models.GetHDMAliyunResourceSyncResultResponse().from_map(self.do_request('GetHDMAliyunResourceSyncResult', 'HTTPS', 'POST', '2020-01-16', 'AK', None, TeaCore.to_map(request), runtime))

    def get_hdmaliyun_resource_sync_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_hdmaliyun_resource_sync_result_with_options(request, runtime)

    def add_hdminstance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return das20200116_models.AddHDMInstanceResponse().from_map(self.do_request('AddHDMInstance', 'HTTPS', 'POST', '2020-01-16', 'AK', None, TeaCore.to_map(request), runtime))

    def add_hdminstance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_hdminstance_with_options(request, runtime)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)
