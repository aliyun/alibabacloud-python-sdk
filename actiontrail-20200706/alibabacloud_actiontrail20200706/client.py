# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from alibabacloud_tea_rpc.client import Client as RPCClient
from alibabacloud_actiontrail20200706 import models as actiontrail_20200706_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_tea_util import models as util_models
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient


class Client(RPCClient):
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = "regional"
        self._endpoint_map = {
            "ap-northeast-2-pop": "actiontrail.ap-northeast-1.aliyuncs.com",
            "cn-beijing-finance-1": "actiontrail.aliyuncs.com",
            "cn-beijing-finance-pop": "actiontrail.aliyuncs.com",
            "cn-beijing-gov-1": "actiontrail.aliyuncs.com",
            "cn-beijing-nu16-b01": "actiontrail.aliyuncs.com",
            "cn-edge-1": "actiontrail.aliyuncs.com",
            "cn-fujian": "actiontrail.aliyuncs.com",
            "cn-haidian-cm12-c01": "actiontrail.aliyuncs.com",
            "cn-hangzhou-bj-b01": "actiontrail.aliyuncs.com",
            "cn-hangzhou-finance": "actiontrail.aliyuncs.com",
            "cn-hangzhou-internal-prod-1": "actiontrail.aliyuncs.com",
            "cn-hangzhou-internal-test-1": "actiontrail.aliyuncs.com",
            "cn-hangzhou-internal-test-2": "actiontrail.aliyuncs.com",
            "cn-hangzhou-internal-test-3": "actiontrail.aliyuncs.com",
            "cn-hangzhou-test-306": "actiontrail.aliyuncs.com",
            "cn-hongkong-finance-pop": "actiontrail.aliyuncs.com",
            "cn-qingdao-nebula": "actiontrail.aliyuncs.com",
            "cn-shanghai-et15-b01": "actiontrail.aliyuncs.com",
            "cn-shanghai-et2-b01": "actiontrail.aliyuncs.com",
            "cn-shanghai-inner": "actiontrail.aliyuncs.com",
            "cn-shanghai-internal-test-1": "actiontrail.aliyuncs.com",
            "cn-shenzhen-finance-1": "actiontrail.aliyuncs.com",
            "cn-shenzhen-inner": "actiontrail.aliyuncs.com",
            "cn-shenzhen-st4-d01": "actiontrail.aliyuncs.com",
            "cn-shenzhen-su18-b01": "actiontrail.aliyuncs.com",
            "cn-wuhan": "actiontrail.aliyuncs.com",
            "cn-yushanfang": "actiontrail.aliyuncs.com",
            "cn-zhangbei-na61-b01": "actiontrail.aliyuncs.com",
            "cn-zhangjiakou-na62-a01": "actiontrail.aliyuncs.com",
            "cn-zhengzhou-nebula-1": "actiontrail.aliyuncs.com",
            "eu-west-1-oxs": "actiontrail.ap-northeast-1.aliyuncs.com",
            "rus-west-1-pop": "actiontrail.ap-northeast-1.aliyuncs.com"
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint("actiontrail", self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def list_delivery_history_jobs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return actiontrail_20200706_models.ListDeliveryHistoryJobsResponse().from_map(self.do_request("ListDeliveryHistoryJobs", "HTTPS", "POST", "2020-07-06", "AK", None, request.to_map(), runtime))

    def list_delivery_history_jobs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_delivery_history_jobs_with_options(request, runtime)

    def create_delivery_history_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return actiontrail_20200706_models.CreateDeliveryHistoryJobResponse().from_map(self.do_request("CreateDeliveryHistoryJob", "HTTPS", "POST", "2020-07-06", "AK", None, request.to_map(), runtime))

    def create_delivery_history_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_delivery_history_job_with_options(request, runtime)

    def lookup_events_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return actiontrail_20200706_models.LookupEventsResponse().from_map(self.do_request("LookupEvents", "HTTPS", "POST", "2020-07-06", "AK", None, request.to_map(), runtime))

    def lookup_events(self, request):
        runtime = util_models.RuntimeOptions()
        return self.lookup_events_with_options(request, runtime)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get('regionId')):
            return endpoint_map.get('regionId')
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)
