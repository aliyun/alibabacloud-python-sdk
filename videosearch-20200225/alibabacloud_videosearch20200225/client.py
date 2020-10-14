# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from alibabacloud_tea_rpc.client import Client as RPCClient
from alibabacloud_videosearch20200225 import models as videosearch_20200225_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_tea_util import models as util_models
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient


class Client(RPCClient):
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = "regional"
        self._endpoint_map = {
            "cn-beijing": "multisearch.cn-beijing.aliyuncs.com",
            "cn-hangzhou": "multisearch.cn-hangzhou.aliyuncs.com"
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint("videosearch", self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_storage_history_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return videosearch_20200225_models.GetStorageHistoryResponse().from_map(self.do_request("GetStorageHistory", "HTTPS", "POST", "2020-02-25", "AK", None, request.to_map(), runtime))

    def get_storage_history(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_storage_history_with_options(request, runtime)

    def add_storage_video_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return videosearch_20200225_models.AddStorageVideoTaskResponse().from_map(self.do_request("AddStorageVideoTask", "HTTPS", "POST", "2020-02-25", "AK", None, request.to_map(), runtime))

    def add_storage_video_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_storage_video_task_with_options(request, runtime)

    def add_deletion_video_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return videosearch_20200225_models.AddDeletionVideoTaskResponse().from_map(self.do_request("AddDeletionVideoTask", "HTTPS", "POST", "2020-02-25", "AK", None, request.to_map(), runtime))

    def add_deletion_video_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_deletion_video_task_with_options(request, runtime)

    def get_task_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return videosearch_20200225_models.GetTaskStatusResponse().from_map(self.do_request("GetTaskStatus", "HTTPS", "POST", "2020-02-25", "AK", None, request.to_map(), runtime))

    def get_task_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_task_status_with_options(request, runtime)

    def add_search_video_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return videosearch_20200225_models.AddSearchVideoTaskResponse().from_map(self.do_request("AddSearchVideoTask", "HTTPS", "POST", "2020-02-25", "AK", None, request.to_map(), runtime))

    def add_search_video_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_search_video_task_with_options(request, runtime)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get('regionId')):
            return endpoint_map.get('regionId')
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)
