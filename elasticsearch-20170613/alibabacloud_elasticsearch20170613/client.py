# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_elasticsearch20170613 import models as elasticsearch_20170613_models
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
            'ap-northeast-2-pop': 'elasticsearch.aliyuncs.com',
            'cn-beijing-finance-1': 'elasticsearch.aliyuncs.com',
            'cn-beijing-finance-pop': 'elasticsearch.aliyuncs.com',
            'cn-beijing-gov-1': 'elasticsearch.aliyuncs.com',
            'cn-beijing-nu16-b01': 'elasticsearch.aliyuncs.com',
            'cn-chengdu': 'elasticsearch.aliyuncs.com',
            'cn-edge-1': 'elasticsearch.aliyuncs.com',
            'cn-fujian': 'elasticsearch.aliyuncs.com',
            'cn-haidian-cm12-c01': 'elasticsearch.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'elasticsearch.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'elasticsearch.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'elasticsearch.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'elasticsearch.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'elasticsearch.aliyuncs.com',
            'cn-hangzhou-test-306': 'elasticsearch.aliyuncs.com',
            'cn-hongkong-finance-pop': 'elasticsearch.aliyuncs.com',
            'cn-huhehaote': 'elasticsearch.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'elasticsearch.aliyuncs.com',
            'cn-qingdao-nebula': 'elasticsearch.aliyuncs.com',
            'cn-shanghai-et15-b01': 'elasticsearch.aliyuncs.com',
            'cn-shanghai-et2-b01': 'elasticsearch.aliyuncs.com',
            'cn-shanghai-inner': 'elasticsearch.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'elasticsearch.aliyuncs.com',
            'cn-shenzhen-finance-1': 'elasticsearch.aliyuncs.com',
            'cn-shenzhen-inner': 'elasticsearch.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'elasticsearch.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'elasticsearch.aliyuncs.com',
            'cn-wuhan': 'elasticsearch.aliyuncs.com',
            'cn-wulanchabu': 'elasticsearch.aliyuncs.com',
            'cn-yushanfang': 'elasticsearch.aliyuncs.com',
            'cn-zhangbei': 'elasticsearch.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'elasticsearch.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'elasticsearch.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'elasticsearch.aliyuncs.com',
            'eu-west-1-oxs': 'elasticsearch.aliyuncs.com',
            'me-east-1': 'elasticsearch.aliyuncs.com',
            'rus-west-1-pop': 'elasticsearch.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('elasticsearch', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def activate_zones(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ActivateZonesRequest,
    ) -> elasticsearch_20170613_models.ActivateZonesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.activate_zones_with_options(instance_id, request, headers, runtime)

    async def activate_zones_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ActivateZonesRequest,
    ) -> elasticsearch_20170613_models.ActivateZonesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.activate_zones_with_options_async(instance_id, request, headers, runtime)

    def activate_zones_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ActivateZonesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ActivateZonesResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ActivateZonesResponse(),
            self.do_roarequest('ActivateZones', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/actions/recover-zones', 'json', req, runtime)
        )

    async def activate_zones_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ActivateZonesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ActivateZonesResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ActivateZonesResponse(),
            await self.do_roarequest_async('ActivateZones', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/actions/recover-zones', 'json', req, runtime)
        )

    def add_connectable_cluster(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.AddConnectableClusterRequest,
    ) -> elasticsearch_20170613_models.AddConnectableClusterResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_connectable_cluster_with_options(instance_id, request, headers, runtime)

    async def add_connectable_cluster_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.AddConnectableClusterRequest,
    ) -> elasticsearch_20170613_models.AddConnectableClusterResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.add_connectable_cluster_with_options_async(instance_id, request, headers, runtime)

    def add_connectable_cluster_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.AddConnectableClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.AddConnectableClusterResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.AddConnectableClusterResponse(),
            self.do_roarequest('AddConnectableCluster', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/connected-clusters', 'json', req, runtime)
        )

    async def add_connectable_cluster_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.AddConnectableClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.AddConnectableClusterResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.AddConnectableClusterResponse(),
            await self.do_roarequest_async('AddConnectableCluster', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/connected-clusters', 'json', req, runtime)
        )

    def add_snapshot_repo(
        self,
        instance_id: str,
    ) -> elasticsearch_20170613_models.AddSnapshotRepoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_snapshot_repo_with_options(instance_id, headers, runtime)

    async def add_snapshot_repo_async(
        self,
        instance_id: str,
    ) -> elasticsearch_20170613_models.AddSnapshotRepoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.add_snapshot_repo_with_options_async(instance_id, headers, runtime)

    def add_snapshot_repo_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.AddSnapshotRepoResponse:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.AddSnapshotRepoResponse(),
            self.do_roarequest('AddSnapshotRepo', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/snapshot-repos', 'json', req, runtime)
        )

    async def add_snapshot_repo_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.AddSnapshotRepoResponse:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.AddSnapshotRepoResponse(),
            await self.do_roarequest_async('AddSnapshotRepo', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/snapshot-repos', 'json', req, runtime)
        )

    def cancel_deletion(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.CancelDeletionRequest,
    ) -> elasticsearch_20170613_models.CancelDeletionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.cancel_deletion_with_options(instance_id, request, headers, runtime)

    async def cancel_deletion_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.CancelDeletionRequest,
    ) -> elasticsearch_20170613_models.CancelDeletionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.cancel_deletion_with_options_async(instance_id, request, headers, runtime)

    def cancel_deletion_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.CancelDeletionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.CancelDeletionResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.CancelDeletionResponse(),
            self.do_roarequest('CancelDeletion', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/actions/cancel-deletion', 'json', req, runtime)
        )

    async def cancel_deletion_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.CancelDeletionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.CancelDeletionResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.CancelDeletionResponse(),
            await self.do_roarequest_async('CancelDeletion', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/actions/cancel-deletion', 'json', req, runtime)
        )

    def cancel_logstash_deletion(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.CancelLogstashDeletionRequest,
    ) -> elasticsearch_20170613_models.CancelLogstashDeletionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.cancel_logstash_deletion_with_options(instance_id, request, headers, runtime)

    async def cancel_logstash_deletion_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.CancelLogstashDeletionRequest,
    ) -> elasticsearch_20170613_models.CancelLogstashDeletionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.cancel_logstash_deletion_with_options_async(instance_id, request, headers, runtime)

    def cancel_logstash_deletion_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.CancelLogstashDeletionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.CancelLogstashDeletionResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.CancelLogstashDeletionResponse(),
            self.do_roarequest('CancelLogstashDeletion', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/logstashes/{instance_id}/actions/cancel-deletion', 'json', req, runtime)
        )

    async def cancel_logstash_deletion_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.CancelLogstashDeletionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.CancelLogstashDeletionResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.CancelLogstashDeletionResponse(),
            await self.do_roarequest_async('CancelLogstashDeletion', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/logstashes/{instance_id}/actions/cancel-deletion', 'json', req, runtime)
        )

    def cancel_task(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.CancelTaskRequest,
    ) -> elasticsearch_20170613_models.CancelTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.cancel_task_with_options(instance_id, request, headers, runtime)

    async def cancel_task_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.CancelTaskRequest,
    ) -> elasticsearch_20170613_models.CancelTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.cancel_task_with_options_async(instance_id, request, headers, runtime)

    def cancel_task_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.CancelTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.CancelTaskResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.task_type):
            query['taskType'] = request.task_type
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.CancelTaskResponse(),
            self.do_roarequest('CancelTask', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/actions/cancel-task', 'json', req, runtime)
        )

    async def cancel_task_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.CancelTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.CancelTaskResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.task_type):
            query['taskType'] = request.task_type
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.CancelTaskResponse(),
            await self.do_roarequest_async('CancelTask', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/actions/cancel-task', 'json', req, runtime)
        )

    def capacity_plan(
        self,
        request: elasticsearch_20170613_models.CapacityPlanRequest,
    ) -> elasticsearch_20170613_models.CapacityPlanResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.capacity_plan_with_options(request, headers, runtime)

    async def capacity_plan_async(
        self,
        request: elasticsearch_20170613_models.CapacityPlanRequest,
    ) -> elasticsearch_20170613_models.CapacityPlanResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.capacity_plan_with_options_async(request, headers, runtime)

    def capacity_plan_with_options(
        self,
        request: elasticsearch_20170613_models.CapacityPlanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.CapacityPlanResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.complex_query_available):
            body['complexQueryAvailable'] = request.complex_query_available
        if not UtilClient.is_unset(request.data_info):
            body['dataInfo'] = request.data_info
        if not UtilClient.is_unset(request.metric):
            body['metric'] = request.metric
        if not UtilClient.is_unset(request.usage_scenario):
            body['usageScenario'] = request.usage_scenario
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.CapacityPlanResponse(),
            self.do_roarequest('CapacityPlan', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/assist/actions/capacity-plan', 'json', req, runtime)
        )

    async def capacity_plan_with_options_async(
        self,
        request: elasticsearch_20170613_models.CapacityPlanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.CapacityPlanResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.complex_query_available):
            body['complexQueryAvailable'] = request.complex_query_available
        if not UtilClient.is_unset(request.data_info):
            body['dataInfo'] = request.data_info
        if not UtilClient.is_unset(request.metric):
            body['metric'] = request.metric
        if not UtilClient.is_unset(request.usage_scenario):
            body['usageScenario'] = request.usage_scenario
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.CapacityPlanResponse(),
            await self.do_roarequest_async('CapacityPlan', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/assist/actions/capacity-plan', 'json', req, runtime)
        )

    def close_diagnosis(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.CloseDiagnosisRequest,
    ) -> elasticsearch_20170613_models.CloseDiagnosisResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.close_diagnosis_with_options(instance_id, request, headers, runtime)

    async def close_diagnosis_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.CloseDiagnosisRequest,
    ) -> elasticsearch_20170613_models.CloseDiagnosisResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.close_diagnosis_with_options_async(instance_id, request, headers, runtime)

    def close_diagnosis_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.CloseDiagnosisRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.CloseDiagnosisResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.lang):
            query['lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.CloseDiagnosisResponse(),
            self.do_roarequest('CloseDiagnosis', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/diagnosis/instances/{instance_id}/actions/close-diagnosis', 'json', req, runtime)
        )

    async def close_diagnosis_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.CloseDiagnosisRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.CloseDiagnosisResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.lang):
            query['lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.CloseDiagnosisResponse(),
            await self.do_roarequest_async('CloseDiagnosis', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/diagnosis/instances/{instance_id}/actions/close-diagnosis', 'json', req, runtime)
        )

    def close_https(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.CloseHttpsRequest,
    ) -> elasticsearch_20170613_models.CloseHttpsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.close_https_with_options(instance_id, request, headers, runtime)

    async def close_https_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.CloseHttpsRequest,
    ) -> elasticsearch_20170613_models.CloseHttpsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.close_https_with_options_async(instance_id, request, headers, runtime)

    def close_https_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.CloseHttpsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.CloseHttpsResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.CloseHttpsResponse(),
            self.do_roarequest('CloseHttps', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/actions/close-https', 'json', req, runtime)
        )

    async def close_https_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.CloseHttpsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.CloseHttpsResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.CloseHttpsResponse(),
            await self.do_roarequest_async('CloseHttps', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/actions/close-https', 'json', req, runtime)
        )

    def close_managed_index(
        self,
        instance_id: str,
        index: str,
        request: elasticsearch_20170613_models.CloseManagedIndexRequest,
    ) -> elasticsearch_20170613_models.CloseManagedIndexResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.close_managed_index_with_options(instance_id, index, request, headers, runtime)

    async def close_managed_index_async(
        self,
        instance_id: str,
        index: str,
        request: elasticsearch_20170613_models.CloseManagedIndexRequest,
    ) -> elasticsearch_20170613_models.CloseManagedIndexResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.close_managed_index_with_options_async(instance_id, index, request, headers, runtime)

    def close_managed_index_with_options(
        self,
        instance_id: str,
        index: str,
        request: elasticsearch_20170613_models.CloseManagedIndexRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.CloseManagedIndexResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        index = OpenApiUtilClient.get_encode_param(index)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.CloseManagedIndexResponse(),
            self.do_roarequest('CloseManagedIndex', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/indices/{index}/close-managed', 'json', req, runtime)
        )

    async def close_managed_index_with_options_async(
        self,
        instance_id: str,
        index: str,
        request: elasticsearch_20170613_models.CloseManagedIndexRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.CloseManagedIndexResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        index = OpenApiUtilClient.get_encode_param(index)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.CloseManagedIndexResponse(),
            await self.do_roarequest_async('CloseManagedIndex', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/indices/{index}/close-managed', 'json', req, runtime)
        )

    def create_collector(
        self,
        request: elasticsearch_20170613_models.CreateCollectorRequest,
    ) -> elasticsearch_20170613_models.CreateCollectorResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_collector_with_options(request, headers, runtime)

    async def create_collector_async(
        self,
        request: elasticsearch_20170613_models.CreateCollectorRequest,
    ) -> elasticsearch_20170613_models.CreateCollectorResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_collector_with_options_async(request, headers, runtime)

    def create_collector_with_options(
        self,
        request: elasticsearch_20170613_models.CreateCollectorRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.CreateCollectorResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.CreateCollectorResponse(),
            self.do_roarequest('CreateCollector', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/collectors', 'json', req, runtime)
        )

    async def create_collector_with_options_async(
        self,
        request: elasticsearch_20170613_models.CreateCollectorRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.CreateCollectorResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.CreateCollectorResponse(),
            await self.do_roarequest_async('CreateCollector', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/collectors', 'json', req, runtime)
        )

    def create_data_stream(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.CreateDataStreamRequest,
    ) -> elasticsearch_20170613_models.CreateDataStreamResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_data_stream_with_options(instance_id, request, headers, runtime)

    async def create_data_stream_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.CreateDataStreamRequest,
    ) -> elasticsearch_20170613_models.CreateDataStreamResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_data_stream_with_options_async(instance_id, request, headers, runtime)

    def create_data_stream_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.CreateDataStreamRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.CreateDataStreamResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.CreateDataStreamResponse(),
            self.do_roarequest('CreateDataStream', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/data-streams', 'json', req, runtime)
        )

    async def create_data_stream_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.CreateDataStreamRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.CreateDataStreamResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.CreateDataStreamResponse(),
            await self.do_roarequest_async('CreateDataStream', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/data-streams', 'json', req, runtime)
        )

    def create_data_tasks(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.CreateDataTasksRequest,
    ) -> elasticsearch_20170613_models.CreateDataTasksResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_data_tasks_with_options(instance_id, request, headers, runtime)

    async def create_data_tasks_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.CreateDataTasksRequest,
    ) -> elasticsearch_20170613_models.CreateDataTasksResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_data_tasks_with_options_async(instance_id, request, headers, runtime)

    def create_data_tasks_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.CreateDataTasksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.CreateDataTasksResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.CreateDataTasksResponse(),
            self.do_roarequest('CreateDataTasks', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/data-task', 'json', req, runtime)
        )

    async def create_data_tasks_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.CreateDataTasksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.CreateDataTasksResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.CreateDataTasksResponse(),
            await self.do_roarequest_async('CreateDataTasks', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/data-task', 'json', req, runtime)
        )

    def create_ilmpolicy(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.CreateILMPolicyRequest,
    ) -> elasticsearch_20170613_models.CreateILMPolicyResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_ilmpolicy_with_options(instance_id, request, headers, runtime)

    async def create_ilmpolicy_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.CreateILMPolicyRequest,
    ) -> elasticsearch_20170613_models.CreateILMPolicyResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_ilmpolicy_with_options_async(instance_id, request, headers, runtime)

    def create_ilmpolicy_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.CreateILMPolicyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.CreateILMPolicyResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.CreateILMPolicyResponse(),
            self.do_roarequest('CreateILMPolicy', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/ilm-policies', 'json', req, runtime)
        )

    async def create_ilmpolicy_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.CreateILMPolicyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.CreateILMPolicyResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.CreateILMPolicyResponse(),
            await self.do_roarequest_async('CreateILMPolicy', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/ilm-policies', 'json', req, runtime)
        )

    def create_index_template(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.CreateIndexTemplateRequest,
    ) -> elasticsearch_20170613_models.CreateIndexTemplateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_index_template_with_options(instance_id, request, headers, runtime)

    async def create_index_template_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.CreateIndexTemplateRequest,
    ) -> elasticsearch_20170613_models.CreateIndexTemplateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_index_template_with_options_async(instance_id, request, headers, runtime)

    def create_index_template_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.CreateIndexTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.CreateIndexTemplateResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.CreateIndexTemplateResponse(),
            self.do_roarequest('CreateIndexTemplate', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/index-templates', 'json', req, runtime)
        )

    async def create_index_template_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.CreateIndexTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.CreateIndexTemplateResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.CreateIndexTemplateResponse(),
            await self.do_roarequest_async('CreateIndexTemplate', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/index-templates', 'json', req, runtime)
        )

    def create_instance(
        self,
        request: elasticsearch_20170613_models.CreateInstanceRequest,
    ) -> elasticsearch_20170613_models.CreateInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_instance_with_options(request, headers, runtime)

    async def create_instance_async(
        self,
        request: elasticsearch_20170613_models.CreateInstanceRequest,
    ) -> elasticsearch_20170613_models.CreateInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_instance_with_options_async(request, headers, runtime)

    def create_instance_with_options(
        self,
        request: elasticsearch_20170613_models.CreateInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.CreateInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.CreateInstanceResponse(),
            self.do_roarequest('createInstance', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances', 'json', req, runtime)
        )

    async def create_instance_with_options_async(
        self,
        request: elasticsearch_20170613_models.CreateInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.CreateInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.CreateInstanceResponse(),
            await self.do_roarequest_async('createInstance', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances', 'json', req, runtime)
        )

    def create_logstash(
        self,
        request: elasticsearch_20170613_models.CreateLogstashRequest,
    ) -> elasticsearch_20170613_models.CreateLogstashResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_logstash_with_options(request, headers, runtime)

    async def create_logstash_async(
        self,
        request: elasticsearch_20170613_models.CreateLogstashRequest,
    ) -> elasticsearch_20170613_models.CreateLogstashResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_logstash_with_options_async(request, headers, runtime)

    def create_logstash_with_options(
        self,
        request: elasticsearch_20170613_models.CreateLogstashRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.CreateLogstashResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.CreateLogstashResponse(),
            self.do_roarequest('CreateLogstash', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/logstashes', 'json', req, runtime)
        )

    async def create_logstash_with_options_async(
        self,
        request: elasticsearch_20170613_models.CreateLogstashRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.CreateLogstashResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.CreateLogstashResponse(),
            await self.do_roarequest_async('CreateLogstash', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/logstashes', 'json', req, runtime)
        )

    def create_pipelines(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.CreatePipelinesRequest,
    ) -> elasticsearch_20170613_models.CreatePipelinesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_pipelines_with_options(instance_id, request, headers, runtime)

    async def create_pipelines_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.CreatePipelinesRequest,
    ) -> elasticsearch_20170613_models.CreatePipelinesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_pipelines_with_options_async(instance_id, request, headers, runtime)

    def create_pipelines_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.CreatePipelinesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.CreatePipelinesResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.trigger):
            query['trigger'] = request.trigger
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.CreatePipelinesResponse(),
            self.do_roarequest('CreatePipelines', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/logstashes/{instance_id}/pipelines', 'json', req, runtime)
        )

    async def create_pipelines_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.CreatePipelinesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.CreatePipelinesResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.trigger):
            query['trigger'] = request.trigger
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.CreatePipelinesResponse(),
            await self.do_roarequest_async('CreatePipelines', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/logstashes/{instance_id}/pipelines', 'json', req, runtime)
        )

    def create_snapshot(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.CreateSnapshotRequest,
    ) -> elasticsearch_20170613_models.CreateSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_snapshot_with_options(instance_id, request, headers, runtime)

    async def create_snapshot_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.CreateSnapshotRequest,
    ) -> elasticsearch_20170613_models.CreateSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_snapshot_with_options_async(instance_id, request, headers, runtime)

    def create_snapshot_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.CreateSnapshotRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.CreateSnapshotResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.CreateSnapshotResponse(),
            self.do_roarequest('CreateSnapshot', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/snapshots', 'json', req, runtime)
        )

    async def create_snapshot_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.CreateSnapshotRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.CreateSnapshotResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.CreateSnapshotResponse(),
            await self.do_roarequest_async('CreateSnapshot', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/snapshots', 'json', req, runtime)
        )

    def create_vpc_endpoint(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.CreateVpcEndpointRequest,
    ) -> elasticsearch_20170613_models.CreateVpcEndpointResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_vpc_endpoint_with_options(instance_id, request, headers, runtime)

    async def create_vpc_endpoint_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.CreateVpcEndpointRequest,
    ) -> elasticsearch_20170613_models.CreateVpcEndpointResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_vpc_endpoint_with_options_async(instance_id, request, headers, runtime)

    def create_vpc_endpoint_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.CreateVpcEndpointRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.CreateVpcEndpointResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.CreateVpcEndpointResponse(),
            self.do_roarequest('CreateVpcEndpoint', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/vpc-endpoints', 'json', req, runtime)
        )

    async def create_vpc_endpoint_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.CreateVpcEndpointRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.CreateVpcEndpointResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.CreateVpcEndpointResponse(),
            await self.do_roarequest_async('CreateVpcEndpoint', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/vpc-endpoints', 'json', req, runtime)
        )

    def deactivate_zones(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.DeactivateZonesRequest,
    ) -> elasticsearch_20170613_models.DeactivateZonesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.deactivate_zones_with_options(instance_id, request, headers, runtime)

    async def deactivate_zones_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.DeactivateZonesRequest,
    ) -> elasticsearch_20170613_models.DeactivateZonesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.deactivate_zones_with_options_async(instance_id, request, headers, runtime)

    def deactivate_zones_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.DeactivateZonesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.DeactivateZonesResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DeactivateZonesResponse(),
            self.do_roarequest('DeactivateZones', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/actions/down-zones', 'json', req, runtime)
        )

    async def deactivate_zones_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.DeactivateZonesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.DeactivateZonesResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DeactivateZonesResponse(),
            await self.do_roarequest_async('DeactivateZones', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/actions/down-zones', 'json', req, runtime)
        )

    def delete_collector(
        self,
        res_id: str,
        request: elasticsearch_20170613_models.DeleteCollectorRequest,
    ) -> elasticsearch_20170613_models.DeleteCollectorResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_collector_with_options(res_id, request, headers, runtime)

    async def delete_collector_async(
        self,
        res_id: str,
        request: elasticsearch_20170613_models.DeleteCollectorRequest,
    ) -> elasticsearch_20170613_models.DeleteCollectorResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_collector_with_options_async(res_id, request, headers, runtime)

    def delete_collector_with_options(
        self,
        res_id: str,
        request: elasticsearch_20170613_models.DeleteCollectorRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.DeleteCollectorResponse:
        UtilClient.validate_model(request)
        res_id = OpenApiUtilClient.get_encode_param(res_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DeleteCollectorResponse(),
            self.do_roarequest('DeleteCollector', '2017-06-13', 'HTTPS', 'DELETE', 'AK', f'/openapi/collectors/{res_id}', 'json', req, runtime)
        )

    async def delete_collector_with_options_async(
        self,
        res_id: str,
        request: elasticsearch_20170613_models.DeleteCollectorRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.DeleteCollectorResponse:
        UtilClient.validate_model(request)
        res_id = OpenApiUtilClient.get_encode_param(res_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DeleteCollectorResponse(),
            await self.do_roarequest_async('DeleteCollector', '2017-06-13', 'HTTPS', 'DELETE', 'AK', f'/openapi/collectors/{res_id}', 'json', req, runtime)
        )

    def delete_connected_cluster(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.DeleteConnectedClusterRequest,
    ) -> elasticsearch_20170613_models.DeleteConnectedClusterResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_connected_cluster_with_options(instance_id, request, headers, runtime)

    async def delete_connected_cluster_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.DeleteConnectedClusterRequest,
    ) -> elasticsearch_20170613_models.DeleteConnectedClusterResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_connected_cluster_with_options_async(instance_id, request, headers, runtime)

    def delete_connected_cluster_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.DeleteConnectedClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.DeleteConnectedClusterResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.connected_instance_id):
            query['connectedInstanceId'] = request.connected_instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DeleteConnectedClusterResponse(),
            self.do_roarequest('DeleteConnectedCluster', '2017-06-13', 'HTTPS', 'DELETE', 'AK', f'/openapi/instances/{instance_id}/connected-clusters', 'json', req, runtime)
        )

    async def delete_connected_cluster_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.DeleteConnectedClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.DeleteConnectedClusterResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.connected_instance_id):
            query['connectedInstanceId'] = request.connected_instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DeleteConnectedClusterResponse(),
            await self.do_roarequest_async('DeleteConnectedCluster', '2017-06-13', 'HTTPS', 'DELETE', 'AK', f'/openapi/instances/{instance_id}/connected-clusters', 'json', req, runtime)
        )

    def delete_data_stream(
        self,
        instance_id: str,
        data_stream: str,
        request: elasticsearch_20170613_models.DeleteDataStreamRequest,
    ) -> elasticsearch_20170613_models.DeleteDataStreamResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_data_stream_with_options(instance_id, data_stream, request, headers, runtime)

    async def delete_data_stream_async(
        self,
        instance_id: str,
        data_stream: str,
        request: elasticsearch_20170613_models.DeleteDataStreamRequest,
    ) -> elasticsearch_20170613_models.DeleteDataStreamResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_data_stream_with_options_async(instance_id, data_stream, request, headers, runtime)

    def delete_data_stream_with_options(
        self,
        instance_id: str,
        data_stream: str,
        request: elasticsearch_20170613_models.DeleteDataStreamRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.DeleteDataStreamResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        data_stream = OpenApiUtilClient.get_encode_param(data_stream)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DeleteDataStreamResponse(),
            self.do_roarequest('DeleteDataStream', '2017-06-13', 'HTTPS', 'DELETE', 'AK', f'/openapi/instances/{instance_id}/data-streams/{data_stream}', 'json', req, runtime)
        )

    async def delete_data_stream_with_options_async(
        self,
        instance_id: str,
        data_stream: str,
        request: elasticsearch_20170613_models.DeleteDataStreamRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.DeleteDataStreamResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        data_stream = OpenApiUtilClient.get_encode_param(data_stream)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DeleteDataStreamResponse(),
            await self.do_roarequest_async('DeleteDataStream', '2017-06-13', 'HTTPS', 'DELETE', 'AK', f'/openapi/instances/{instance_id}/data-streams/{data_stream}', 'json', req, runtime)
        )

    def delete_data_task(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.DeleteDataTaskRequest,
    ) -> elasticsearch_20170613_models.DeleteDataTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_data_task_with_options(instance_id, request, headers, runtime)

    async def delete_data_task_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.DeleteDataTaskRequest,
    ) -> elasticsearch_20170613_models.DeleteDataTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_data_task_with_options_async(instance_id, request, headers, runtime)

    def delete_data_task_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.DeleteDataTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.DeleteDataTaskResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DeleteDataTaskResponse(),
            self.do_roarequest('DeleteDataTask', '2017-06-13', 'HTTPS', 'DELETE', 'AK', f'/openapi/instances/{instance_id}/data-task', 'json', req, runtime)
        )

    async def delete_data_task_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.DeleteDataTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.DeleteDataTaskResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DeleteDataTaskResponse(),
            await self.do_roarequest_async('DeleteDataTask', '2017-06-13', 'HTTPS', 'DELETE', 'AK', f'/openapi/instances/{instance_id}/data-task', 'json', req, runtime)
        )

    def delete_ilmpolicy(
        self,
        instance_id: str,
        policy_name: str,
    ) -> elasticsearch_20170613_models.DeleteILMPolicyResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_ilmpolicy_with_options(instance_id, policy_name, headers, runtime)

    async def delete_ilmpolicy_async(
        self,
        instance_id: str,
        policy_name: str,
    ) -> elasticsearch_20170613_models.DeleteILMPolicyResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_ilmpolicy_with_options_async(instance_id, policy_name, headers, runtime)

    def delete_ilmpolicy_with_options(
        self,
        instance_id: str,
        policy_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.DeleteILMPolicyResponse:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        policy_name = OpenApiUtilClient.get_encode_param(policy_name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DeleteILMPolicyResponse(),
            self.do_roarequest('DeleteILMPolicy', '2017-06-13', 'HTTPS', 'DELETE', 'AK', f'/openapi/instances/{instance_id}/ilm-policies/{policy_name}', 'json', req, runtime)
        )

    async def delete_ilmpolicy_with_options_async(
        self,
        instance_id: str,
        policy_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.DeleteILMPolicyResponse:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        policy_name = OpenApiUtilClient.get_encode_param(policy_name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DeleteILMPolicyResponse(),
            await self.do_roarequest_async('DeleteILMPolicy', '2017-06-13', 'HTTPS', 'DELETE', 'AK', f'/openapi/instances/{instance_id}/ilm-policies/{policy_name}', 'json', req, runtime)
        )

    def delete_index_template(
        self,
        instance_id: str,
        index_template: str,
    ) -> elasticsearch_20170613_models.DeleteIndexTemplateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_index_template_with_options(instance_id, index_template, headers, runtime)

    async def delete_index_template_async(
        self,
        instance_id: str,
        index_template: str,
    ) -> elasticsearch_20170613_models.DeleteIndexTemplateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_index_template_with_options_async(instance_id, index_template, headers, runtime)

    def delete_index_template_with_options(
        self,
        instance_id: str,
        index_template: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.DeleteIndexTemplateResponse:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        index_template = OpenApiUtilClient.get_encode_param(index_template)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DeleteIndexTemplateResponse(),
            self.do_roarequest('DeleteIndexTemplate', '2017-06-13', 'HTTPS', 'DELETE', 'AK', f'/openapi/instances/{instance_id}/index-templates/{index_template}', 'json', req, runtime)
        )

    async def delete_index_template_with_options_async(
        self,
        instance_id: str,
        index_template: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.DeleteIndexTemplateResponse:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        index_template = OpenApiUtilClient.get_encode_param(index_template)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DeleteIndexTemplateResponse(),
            await self.do_roarequest_async('DeleteIndexTemplate', '2017-06-13', 'HTTPS', 'DELETE', 'AK', f'/openapi/instances/{instance_id}/index-templates/{index_template}', 'json', req, runtime)
        )

    def delete_instance(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.DeleteInstanceRequest,
    ) -> elasticsearch_20170613_models.DeleteInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_instance_with_options(instance_id, request, headers, runtime)

    async def delete_instance_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.DeleteInstanceRequest,
    ) -> elasticsearch_20170613_models.DeleteInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_instance_with_options_async(instance_id, request, headers, runtime)

    def delete_instance_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.DeleteInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.DeleteInstanceResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.delete_type):
            query['deleteType'] = request.delete_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DeleteInstanceResponse(),
            self.do_roarequest('DeleteInstance', '2017-06-13', 'HTTPS', 'DELETE', 'AK', f'/openapi/instances/{instance_id}', 'json', req, runtime)
        )

    async def delete_instance_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.DeleteInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.DeleteInstanceResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.delete_type):
            query['deleteType'] = request.delete_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DeleteInstanceResponse(),
            await self.do_roarequest_async('DeleteInstance', '2017-06-13', 'HTTPS', 'DELETE', 'AK', f'/openapi/instances/{instance_id}', 'json', req, runtime)
        )

    def delete_logstash(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.DeleteLogstashRequest,
    ) -> elasticsearch_20170613_models.DeleteLogstashResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_logstash_with_options(instance_id, request, headers, runtime)

    async def delete_logstash_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.DeleteLogstashRequest,
    ) -> elasticsearch_20170613_models.DeleteLogstashResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_logstash_with_options_async(instance_id, request, headers, runtime)

    def delete_logstash_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.DeleteLogstashRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.DeleteLogstashResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.delete_type):
            query['deleteType'] = request.delete_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DeleteLogstashResponse(),
            self.do_roarequest('DeleteLogstash', '2017-06-13', 'HTTPS', 'DELETE', 'AK', f'/openapi/logstashes/{instance_id}', 'json', req, runtime)
        )

    async def delete_logstash_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.DeleteLogstashRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.DeleteLogstashResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.delete_type):
            query['deleteType'] = request.delete_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DeleteLogstashResponse(),
            await self.do_roarequest_async('DeleteLogstash', '2017-06-13', 'HTTPS', 'DELETE', 'AK', f'/openapi/logstashes/{instance_id}', 'json', req, runtime)
        )

    def delete_pipelines(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.DeletePipelinesRequest,
    ) -> elasticsearch_20170613_models.DeletePipelinesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_pipelines_with_options(instance_id, request, headers, runtime)

    async def delete_pipelines_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.DeletePipelinesRequest,
    ) -> elasticsearch_20170613_models.DeletePipelinesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_pipelines_with_options_async(instance_id, request, headers, runtime)

    def delete_pipelines_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.DeletePipelinesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.DeletePipelinesResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.pipeline_ids):
            query['pipelineIds'] = request.pipeline_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DeletePipelinesResponse(),
            self.do_roarequest('DeletePipelines', '2017-06-13', 'HTTPS', 'DELETE', 'AK', f'/openapi/logstashes/{instance_id}/pipelines', 'json', req, runtime)
        )

    async def delete_pipelines_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.DeletePipelinesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.DeletePipelinesResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.pipeline_ids):
            query['pipelineIds'] = request.pipeline_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DeletePipelinesResponse(),
            await self.do_roarequest_async('DeletePipelines', '2017-06-13', 'HTTPS', 'DELETE', 'AK', f'/openapi/logstashes/{instance_id}/pipelines', 'json', req, runtime)
        )

    def delete_snapshot_repo(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.DeleteSnapshotRepoRequest,
    ) -> elasticsearch_20170613_models.DeleteSnapshotRepoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_snapshot_repo_with_options(instance_id, request, headers, runtime)

    async def delete_snapshot_repo_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.DeleteSnapshotRepoRequest,
    ) -> elasticsearch_20170613_models.DeleteSnapshotRepoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_snapshot_repo_with_options_async(instance_id, request, headers, runtime)

    def delete_snapshot_repo_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.DeleteSnapshotRepoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.DeleteSnapshotRepoResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.repo_path):
            query['repoPath'] = request.repo_path
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DeleteSnapshotRepoResponse(),
            self.do_roarequest('DeleteSnapshotRepo', '2017-06-13', 'HTTPS', 'DELETE', 'AK', f'/openapi/instances/{instance_id}/snapshot-repos', 'json', req, runtime)
        )

    async def delete_snapshot_repo_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.DeleteSnapshotRepoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.DeleteSnapshotRepoResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.repo_path):
            query['repoPath'] = request.repo_path
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DeleteSnapshotRepoResponse(),
            await self.do_roarequest_async('DeleteSnapshotRepo', '2017-06-13', 'HTTPS', 'DELETE', 'AK', f'/openapi/instances/{instance_id}/snapshot-repos', 'json', req, runtime)
        )

    def delete_vpc_endpoint(
        self,
        instance_id: str,
        endpoint_id: str,
        request: elasticsearch_20170613_models.DeleteVpcEndpointRequest,
    ) -> elasticsearch_20170613_models.DeleteVpcEndpointResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_vpc_endpoint_with_options(instance_id, endpoint_id, request, headers, runtime)

    async def delete_vpc_endpoint_async(
        self,
        instance_id: str,
        endpoint_id: str,
        request: elasticsearch_20170613_models.DeleteVpcEndpointRequest,
    ) -> elasticsearch_20170613_models.DeleteVpcEndpointResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_vpc_endpoint_with_options_async(instance_id, endpoint_id, request, headers, runtime)

    def delete_vpc_endpoint_with_options(
        self,
        instance_id: str,
        endpoint_id: str,
        request: elasticsearch_20170613_models.DeleteVpcEndpointRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.DeleteVpcEndpointResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        endpoint_id = OpenApiUtilClient.get_encode_param(endpoint_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DeleteVpcEndpointResponse(),
            self.do_roarequest('DeleteVpcEndpoint', '2017-06-13', 'HTTPS', 'DELETE', 'AK', f'/openapi/instances/{instance_id}/vpc-endpoints/{endpoint_id}', 'json', req, runtime)
        )

    async def delete_vpc_endpoint_with_options_async(
        self,
        instance_id: str,
        endpoint_id: str,
        request: elasticsearch_20170613_models.DeleteVpcEndpointRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.DeleteVpcEndpointResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        endpoint_id = OpenApiUtilClient.get_encode_param(endpoint_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DeleteVpcEndpointResponse(),
            await self.do_roarequest_async('DeleteVpcEndpoint', '2017-06-13', 'HTTPS', 'DELETE', 'AK', f'/openapi/instances/{instance_id}/vpc-endpoints/{endpoint_id}', 'json', req, runtime)
        )

    def describe_ack_operator(
        self,
        cluster_id: str,
    ) -> elasticsearch_20170613_models.DescribeAckOperatorResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_ack_operator_with_options(cluster_id, headers, runtime)

    async def describe_ack_operator_async(
        self,
        cluster_id: str,
    ) -> elasticsearch_20170613_models.DescribeAckOperatorResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_ack_operator_with_options_async(cluster_id, headers, runtime)

    def describe_ack_operator_with_options(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.DescribeAckOperatorResponse:
        cluster_id = OpenApiUtilClient.get_encode_param(cluster_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DescribeAckOperatorResponse(),
            self.do_roarequest('DescribeAckOperator', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/ack-clusters/{cluster_id}/operator', 'json', req, runtime)
        )

    async def describe_ack_operator_with_options_async(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.DescribeAckOperatorResponse:
        cluster_id = OpenApiUtilClient.get_encode_param(cluster_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DescribeAckOperatorResponse(),
            await self.do_roarequest_async('DescribeAckOperator', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/ack-clusters/{cluster_id}/operator', 'json', req, runtime)
        )

    def describe_collector(
        self,
        res_id: str,
    ) -> elasticsearch_20170613_models.DescribeCollectorResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_collector_with_options(res_id, headers, runtime)

    async def describe_collector_async(
        self,
        res_id: str,
    ) -> elasticsearch_20170613_models.DescribeCollectorResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_collector_with_options_async(res_id, headers, runtime)

    def describe_collector_with_options(
        self,
        res_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.DescribeCollectorResponse:
        res_id = OpenApiUtilClient.get_encode_param(res_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DescribeCollectorResponse(),
            self.do_roarequest('DescribeCollector', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/collectors/{res_id}', 'json', req, runtime)
        )

    async def describe_collector_with_options_async(
        self,
        res_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.DescribeCollectorResponse:
        res_id = OpenApiUtilClient.get_encode_param(res_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DescribeCollectorResponse(),
            await self.do_roarequest_async('DescribeCollector', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/collectors/{res_id}', 'json', req, runtime)
        )

    def describe_connectable_clusters(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.DescribeConnectableClustersRequest,
    ) -> elasticsearch_20170613_models.DescribeConnectableClustersResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_connectable_clusters_with_options(instance_id, request, headers, runtime)

    async def describe_connectable_clusters_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.DescribeConnectableClustersRequest,
    ) -> elasticsearch_20170613_models.DescribeConnectableClustersResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_connectable_clusters_with_options_async(instance_id, request, headers, runtime)

    def describe_connectable_clusters_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.DescribeConnectableClustersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.DescribeConnectableClustersResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.already_set_items):
            query['alreadySetItems'] = request.already_set_items
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DescribeConnectableClustersResponse(),
            self.do_roarequest('DescribeConnectableClusters', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/connectable-clusters', 'json', req, runtime)
        )

    async def describe_connectable_clusters_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.DescribeConnectableClustersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.DescribeConnectableClustersResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.already_set_items):
            query['alreadySetItems'] = request.already_set_items
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DescribeConnectableClustersResponse(),
            await self.do_roarequest_async('DescribeConnectableClusters', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/connectable-clusters', 'json', req, runtime)
        )

    def describe_diagnose_report(
        self,
        instance_id: str,
        report_id: str,
        request: elasticsearch_20170613_models.DescribeDiagnoseReportRequest,
    ) -> elasticsearch_20170613_models.DescribeDiagnoseReportResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_diagnose_report_with_options(instance_id, report_id, request, headers, runtime)

    async def describe_diagnose_report_async(
        self,
        instance_id: str,
        report_id: str,
        request: elasticsearch_20170613_models.DescribeDiagnoseReportRequest,
    ) -> elasticsearch_20170613_models.DescribeDiagnoseReportResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_diagnose_report_with_options_async(instance_id, report_id, request, headers, runtime)

    def describe_diagnose_report_with_options(
        self,
        instance_id: str,
        report_id: str,
        request: elasticsearch_20170613_models.DescribeDiagnoseReportRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.DescribeDiagnoseReportResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        report_id = OpenApiUtilClient.get_encode_param(report_id)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DescribeDiagnoseReportResponse(),
            self.do_roarequest('DescribeDiagnoseReport', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/diagnosis/instances/{instance_id}/reports/{report_id}', 'json', req, runtime)
        )

    async def describe_diagnose_report_with_options_async(
        self,
        instance_id: str,
        report_id: str,
        request: elasticsearch_20170613_models.DescribeDiagnoseReportRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.DescribeDiagnoseReportResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        report_id = OpenApiUtilClient.get_encode_param(report_id)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DescribeDiagnoseReportResponse(),
            await self.do_roarequest_async('DescribeDiagnoseReport', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/diagnosis/instances/{instance_id}/reports/{report_id}', 'json', req, runtime)
        )

    def describe_diagnosis_settings(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.DescribeDiagnosisSettingsRequest,
    ) -> elasticsearch_20170613_models.DescribeDiagnosisSettingsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_diagnosis_settings_with_options(instance_id, request, headers, runtime)

    async def describe_diagnosis_settings_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.DescribeDiagnosisSettingsRequest,
    ) -> elasticsearch_20170613_models.DescribeDiagnosisSettingsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_diagnosis_settings_with_options_async(instance_id, request, headers, runtime)

    def describe_diagnosis_settings_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.DescribeDiagnosisSettingsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.DescribeDiagnosisSettingsResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DescribeDiagnosisSettingsResponse(),
            self.do_roarequest('DescribeDiagnosisSettings', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/diagnosis/instances/{instance_id}/settings', 'json', req, runtime)
        )

    async def describe_diagnosis_settings_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.DescribeDiagnosisSettingsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.DescribeDiagnosisSettingsResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DescribeDiagnosisSettingsResponse(),
            await self.do_roarequest_async('DescribeDiagnosisSettings', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/diagnosis/instances/{instance_id}/settings', 'json', req, runtime)
        )

    def describe_elasticsearch_health(
        self,
        instance_id: str,
    ) -> elasticsearch_20170613_models.DescribeElasticsearchHealthResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_elasticsearch_health_with_options(instance_id, headers, runtime)

    async def describe_elasticsearch_health_async(
        self,
        instance_id: str,
    ) -> elasticsearch_20170613_models.DescribeElasticsearchHealthResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_elasticsearch_health_with_options_async(instance_id, headers, runtime)

    def describe_elasticsearch_health_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.DescribeElasticsearchHealthResponse:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DescribeElasticsearchHealthResponse(),
            self.do_roarequest('DescribeElasticsearchHealth', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/elasticsearch-health', 'json', req, runtime)
        )

    async def describe_elasticsearch_health_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.DescribeElasticsearchHealthResponse:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DescribeElasticsearchHealthResponse(),
            await self.do_roarequest_async('DescribeElasticsearchHealth', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/elasticsearch-health', 'json', req, runtime)
        )

    def describe_ilmpolicy(
        self,
        instance_id: str,
        policy_name: str,
    ) -> elasticsearch_20170613_models.DescribeILMPolicyResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_ilmpolicy_with_options(instance_id, policy_name, headers, runtime)

    async def describe_ilmpolicy_async(
        self,
        instance_id: str,
        policy_name: str,
    ) -> elasticsearch_20170613_models.DescribeILMPolicyResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_ilmpolicy_with_options_async(instance_id, policy_name, headers, runtime)

    def describe_ilmpolicy_with_options(
        self,
        instance_id: str,
        policy_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.DescribeILMPolicyResponse:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        policy_name = OpenApiUtilClient.get_encode_param(policy_name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DescribeILMPolicyResponse(),
            self.do_roarequest('DescribeILMPolicy', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/ilm-policies/{policy_name}', 'json', req, runtime)
        )

    async def describe_ilmpolicy_with_options_async(
        self,
        instance_id: str,
        policy_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.DescribeILMPolicyResponse:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        policy_name = OpenApiUtilClient.get_encode_param(policy_name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DescribeILMPolicyResponse(),
            await self.do_roarequest_async('DescribeILMPolicy', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/ilm-policies/{policy_name}', 'json', req, runtime)
        )

    def describe_index_template(
        self,
        instance_id: str,
        index_template: str,
    ) -> elasticsearch_20170613_models.DescribeIndexTemplateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_index_template_with_options(instance_id, index_template, headers, runtime)

    async def describe_index_template_async(
        self,
        instance_id: str,
        index_template: str,
    ) -> elasticsearch_20170613_models.DescribeIndexTemplateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_index_template_with_options_async(instance_id, index_template, headers, runtime)

    def describe_index_template_with_options(
        self,
        instance_id: str,
        index_template: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.DescribeIndexTemplateResponse:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        index_template = OpenApiUtilClient.get_encode_param(index_template)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DescribeIndexTemplateResponse(),
            self.do_roarequest('DescribeIndexTemplate', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/index-templates/{index_template}', 'json', req, runtime)
        )

    async def describe_index_template_with_options_async(
        self,
        instance_id: str,
        index_template: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.DescribeIndexTemplateResponse:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        index_template = OpenApiUtilClient.get_encode_param(index_template)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DescribeIndexTemplateResponse(),
            await self.do_roarequest_async('DescribeIndexTemplate', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/index-templates/{index_template}', 'json', req, runtime)
        )

    def describe_instance(
        self,
        instance_id: str,
    ) -> elasticsearch_20170613_models.DescribeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_instance_with_options(instance_id, headers, runtime)

    async def describe_instance_async(
        self,
        instance_id: str,
    ) -> elasticsearch_20170613_models.DescribeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_instance_with_options_async(instance_id, headers, runtime)

    def describe_instance_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.DescribeInstanceResponse:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DescribeInstanceResponse(),
            self.do_roarequest('DescribeInstance', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}', 'json', req, runtime)
        )

    async def describe_instance_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.DescribeInstanceResponse:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DescribeInstanceResponse(),
            await self.do_roarequest_async('DescribeInstance', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}', 'json', req, runtime)
        )

    def describe_kibana_settings(
        self,
        instance_id: str,
    ) -> elasticsearch_20170613_models.DescribeKibanaSettingsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_kibana_settings_with_options(instance_id, headers, runtime)

    async def describe_kibana_settings_async(
        self,
        instance_id: str,
    ) -> elasticsearch_20170613_models.DescribeKibanaSettingsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_kibana_settings_with_options_async(instance_id, headers, runtime)

    def describe_kibana_settings_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.DescribeKibanaSettingsResponse:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DescribeKibanaSettingsResponse(),
            self.do_roarequest('DescribeKibanaSettings', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/kibana-settings', 'json', req, runtime)
        )

    async def describe_kibana_settings_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.DescribeKibanaSettingsResponse:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DescribeKibanaSettingsResponse(),
            await self.do_roarequest_async('DescribeKibanaSettings', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/kibana-settings', 'json', req, runtime)
        )

    def describe_logstash(
        self,
        instance_id: str,
    ) -> elasticsearch_20170613_models.DescribeLogstashResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_logstash_with_options(instance_id, headers, runtime)

    async def describe_logstash_async(
        self,
        instance_id: str,
    ) -> elasticsearch_20170613_models.DescribeLogstashResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_logstash_with_options_async(instance_id, headers, runtime)

    def describe_logstash_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.DescribeLogstashResponse:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DescribeLogstashResponse(),
            self.do_roarequest('DescribeLogstash', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/logstashes/{instance_id}', 'json', req, runtime)
        )

    async def describe_logstash_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.DescribeLogstashResponse:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DescribeLogstashResponse(),
            await self.do_roarequest_async('DescribeLogstash', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/logstashes/{instance_id}', 'json', req, runtime)
        )

    def describe_pipeline(
        self,
        instance_id: str,
        pipeline_id: str,
    ) -> elasticsearch_20170613_models.DescribePipelineResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_pipeline_with_options(instance_id, pipeline_id, headers, runtime)

    async def describe_pipeline_async(
        self,
        instance_id: str,
        pipeline_id: str,
    ) -> elasticsearch_20170613_models.DescribePipelineResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_pipeline_with_options_async(instance_id, pipeline_id, headers, runtime)

    def describe_pipeline_with_options(
        self,
        instance_id: str,
        pipeline_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.DescribePipelineResponse:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        pipeline_id = OpenApiUtilClient.get_encode_param(pipeline_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DescribePipelineResponse(),
            self.do_roarequest('DescribePipeline', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/logstashes/{instance_id}/pipelines/{pipeline_id}', 'json', req, runtime)
        )

    async def describe_pipeline_with_options_async(
        self,
        instance_id: str,
        pipeline_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.DescribePipelineResponse:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        pipeline_id = OpenApiUtilClient.get_encode_param(pipeline_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DescribePipelineResponse(),
            await self.do_roarequest_async('DescribePipeline', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/logstashes/{instance_id}/pipelines/{pipeline_id}', 'json', req, runtime)
        )

    def describe_pipeline_management_config(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.DescribePipelineManagementConfigRequest,
    ) -> elasticsearch_20170613_models.DescribePipelineManagementConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_pipeline_management_config_with_options(instance_id, request, headers, runtime)

    async def describe_pipeline_management_config_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.DescribePipelineManagementConfigRequest,
    ) -> elasticsearch_20170613_models.DescribePipelineManagementConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_pipeline_management_config_with_options_async(instance_id, request, headers, runtime)

    def describe_pipeline_management_config_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.DescribePipelineManagementConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.DescribePipelineManagementConfigResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DescribePipelineManagementConfigResponse(),
            self.do_roarequest('DescribePipelineManagementConfig', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/logstashes/{instance_id}/pipeline-management-config', 'json', req, runtime)
        )

    async def describe_pipeline_management_config_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.DescribePipelineManagementConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.DescribePipelineManagementConfigResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DescribePipelineManagementConfigResponse(),
            await self.do_roarequest_async('DescribePipelineManagementConfig', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/logstashes/{instance_id}/pipeline-management-config', 'json', req, runtime)
        )

    def describe_regions(self) -> elasticsearch_20170613_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_regions_with_options(headers, runtime)

    async def describe_regions_async(self) -> elasticsearch_20170613_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_regions_with_options_async(headers, runtime)

    def describe_regions_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.DescribeRegionsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DescribeRegionsResponse(),
            self.do_roarequest('DescribeRegions', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/regions', 'json', req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.DescribeRegionsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DescribeRegionsResponse(),
            await self.do_roarequest_async('DescribeRegions', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/regions', 'json', req, runtime)
        )

    def describe_snapshot_setting(
        self,
        instance_id: str,
    ) -> elasticsearch_20170613_models.DescribeSnapshotSettingResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_snapshot_setting_with_options(instance_id, headers, runtime)

    async def describe_snapshot_setting_async(
        self,
        instance_id: str,
    ) -> elasticsearch_20170613_models.DescribeSnapshotSettingResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_snapshot_setting_with_options_async(instance_id, headers, runtime)

    def describe_snapshot_setting_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.DescribeSnapshotSettingResponse:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DescribeSnapshotSettingResponse(),
            self.do_roarequest('DescribeSnapshotSetting', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/snapshot-setting', 'json', req, runtime)
        )

    async def describe_snapshot_setting_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.DescribeSnapshotSettingResponse:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DescribeSnapshotSettingResponse(),
            await self.do_roarequest_async('DescribeSnapshotSetting', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/snapshot-setting', 'json', req, runtime)
        )

    def describe_templates(
        self,
        instance_id: str,
    ) -> elasticsearch_20170613_models.DescribeTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_templates_with_options(instance_id, headers, runtime)

    async def describe_templates_async(
        self,
        instance_id: str,
    ) -> elasticsearch_20170613_models.DescribeTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_templates_with_options_async(instance_id, headers, runtime)

    def describe_templates_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.DescribeTemplatesResponse:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DescribeTemplatesResponse(),
            self.do_roarequest('DescribeTemplates', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/templates', 'json', req, runtime)
        )

    async def describe_templates_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.DescribeTemplatesResponse:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DescribeTemplatesResponse(),
            await self.do_roarequest_async('DescribeTemplates', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/templates', 'json', req, runtime)
        )

    def describe_xpack_monitor_config(
        self,
        instance_id: str,
    ) -> elasticsearch_20170613_models.DescribeXpackMonitorConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_xpack_monitor_config_with_options(instance_id, headers, runtime)

    async def describe_xpack_monitor_config_async(
        self,
        instance_id: str,
    ) -> elasticsearch_20170613_models.DescribeXpackMonitorConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_xpack_monitor_config_with_options_async(instance_id, headers, runtime)

    def describe_xpack_monitor_config_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.DescribeXpackMonitorConfigResponse:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DescribeXpackMonitorConfigResponse(),
            self.do_roarequest('DescribeXpackMonitorConfig', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/logstashes/{instance_id}/xpack-monitor-config', 'json', req, runtime)
        )

    async def describe_xpack_monitor_config_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.DescribeXpackMonitorConfigResponse:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DescribeXpackMonitorConfigResponse(),
            await self.do_roarequest_async('DescribeXpackMonitorConfig', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/logstashes/{instance_id}/xpack-monitor-config', 'json', req, runtime)
        )

    def diagnose_instance(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.DiagnoseInstanceRequest,
    ) -> elasticsearch_20170613_models.DiagnoseInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.diagnose_instance_with_options(instance_id, request, headers, runtime)

    async def diagnose_instance_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.DiagnoseInstanceRequest,
    ) -> elasticsearch_20170613_models.DiagnoseInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.diagnose_instance_with_options_async(instance_id, request, headers, runtime)

    def diagnose_instance_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.DiagnoseInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.DiagnoseInstanceResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['lang'] = request.lang
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DiagnoseInstanceResponse(),
            self.do_roarequest('DiagnoseInstance', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/diagnosis/instances/{instance_id}/actions/diagnose', 'json', req, runtime)
        )

    async def diagnose_instance_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.DiagnoseInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.DiagnoseInstanceResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['lang'] = request.lang
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DiagnoseInstanceResponse(),
            await self.do_roarequest_async('DiagnoseInstance', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/diagnosis/instances/{instance_id}/actions/diagnose', 'json', req, runtime)
        )

    def estimated_logstash_restart_time(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.EstimatedLogstashRestartTimeRequest,
    ) -> elasticsearch_20170613_models.EstimatedLogstashRestartTimeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.estimated_logstash_restart_time_with_options(instance_id, request, headers, runtime)

    async def estimated_logstash_restart_time_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.EstimatedLogstashRestartTimeRequest,
    ) -> elasticsearch_20170613_models.EstimatedLogstashRestartTimeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.estimated_logstash_restart_time_with_options_async(instance_id, request, headers, runtime)

    def estimated_logstash_restart_time_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.EstimatedLogstashRestartTimeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.EstimatedLogstashRestartTimeResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['force'] = request.force
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.EstimatedLogstashRestartTimeResponse(),
            self.do_roarequest('EstimatedLogstashRestartTime', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/logstashes/{instance_id}/estimated-time/restart-time', 'json', req, runtime)
        )

    async def estimated_logstash_restart_time_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.EstimatedLogstashRestartTimeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.EstimatedLogstashRestartTimeResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['force'] = request.force
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.EstimatedLogstashRestartTimeResponse(),
            await self.do_roarequest_async('EstimatedLogstashRestartTime', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/logstashes/{instance_id}/estimated-time/restart-time', 'json', req, runtime)
        )

    def estimated_restart_time(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.EstimatedRestartTimeRequest,
    ) -> elasticsearch_20170613_models.EstimatedRestartTimeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.estimated_restart_time_with_options(instance_id, request, headers, runtime)

    async def estimated_restart_time_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.EstimatedRestartTimeRequest,
    ) -> elasticsearch_20170613_models.EstimatedRestartTimeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.estimated_restart_time_with_options_async(instance_id, request, headers, runtime)

    def estimated_restart_time_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.EstimatedRestartTimeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.EstimatedRestartTimeResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['force'] = request.force
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.EstimatedRestartTimeResponse(),
            self.do_roarequest('EstimatedRestartTime', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/estimated-time/restart-time', 'json', req, runtime)
        )

    async def estimated_restart_time_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.EstimatedRestartTimeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.EstimatedRestartTimeResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['force'] = request.force
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.EstimatedRestartTimeResponse(),
            await self.do_roarequest_async('EstimatedRestartTime', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/estimated-time/restart-time', 'json', req, runtime)
        )

    def get_cluster_data_information(self) -> elasticsearch_20170613_models.GetClusterDataInformationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_cluster_data_information_with_options(headers, runtime)

    async def get_cluster_data_information_async(self) -> elasticsearch_20170613_models.GetClusterDataInformationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_cluster_data_information_with_options_async(headers, runtime)

    def get_cluster_data_information_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.GetClusterDataInformationResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.GetClusterDataInformationResponse(),
            self.do_roarequest('GetClusterDataInformation', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/cluster/data-information', 'json', req, runtime)
        )

    async def get_cluster_data_information_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.GetClusterDataInformationResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.GetClusterDataInformationResponse(),
            await self.do_roarequest_async('GetClusterDataInformation', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/cluster/data-information', 'json', req, runtime)
        )

    def get_elastictask(
        self,
        instance_id: str,
    ) -> elasticsearch_20170613_models.GetElastictaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_elastictask_with_options(instance_id, headers, runtime)

    async def get_elastictask_async(
        self,
        instance_id: str,
    ) -> elasticsearch_20170613_models.GetElastictaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_elastictask_with_options_async(instance_id, headers, runtime)

    def get_elastictask_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.GetElastictaskResponse:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.GetElastictaskResponse(),
            self.do_roarequest('GetElastictask', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/elastic-task', 'json', req, runtime)
        )

    async def get_elastictask_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.GetElastictaskResponse:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.GetElastictaskResponse(),
            await self.do_roarequest_async('GetElastictask', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/elastic-task', 'json', req, runtime)
        )

    def get_emon_grafana_alerts(
        self,
        project_id: str,
    ) -> elasticsearch_20170613_models.GetEmonGrafanaAlertsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_emon_grafana_alerts_with_options(project_id, headers, runtime)

    async def get_emon_grafana_alerts_async(
        self,
        project_id: str,
    ) -> elasticsearch_20170613_models.GetEmonGrafanaAlertsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_emon_grafana_alerts_with_options_async(project_id, headers, runtime)

    def get_emon_grafana_alerts_with_options(
        self,
        project_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.GetEmonGrafanaAlertsResponse:
        project_id = OpenApiUtilClient.get_encode_param(project_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.GetEmonGrafanaAlertsResponse(),
            self.do_roarequest('GetEmonGrafanaAlerts', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/emon/projects/{project_id}/grafana/proxy/api/alerts', 'json', req, runtime)
        )

    async def get_emon_grafana_alerts_with_options_async(
        self,
        project_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.GetEmonGrafanaAlertsResponse:
        project_id = OpenApiUtilClient.get_encode_param(project_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.GetEmonGrafanaAlertsResponse(),
            await self.do_roarequest_async('GetEmonGrafanaAlerts', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/emon/projects/{project_id}/grafana/proxy/api/alerts', 'json', req, runtime)
        )

    def get_emon_grafana_dashboards(
        self,
        project_id: str,
    ) -> elasticsearch_20170613_models.GetEmonGrafanaDashboardsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_emon_grafana_dashboards_with_options(project_id, headers, runtime)

    async def get_emon_grafana_dashboards_async(
        self,
        project_id: str,
    ) -> elasticsearch_20170613_models.GetEmonGrafanaDashboardsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_emon_grafana_dashboards_with_options_async(project_id, headers, runtime)

    def get_emon_grafana_dashboards_with_options(
        self,
        project_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.GetEmonGrafanaDashboardsResponse:
        project_id = OpenApiUtilClient.get_encode_param(project_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.GetEmonGrafanaDashboardsResponse(),
            self.do_roarequest('GetEmonGrafanaDashboards', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/emon/projects/{project_id}/grafana/proxy/api/search', 'json', req, runtime)
        )

    async def get_emon_grafana_dashboards_with_options_async(
        self,
        project_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.GetEmonGrafanaDashboardsResponse:
        project_id = OpenApiUtilClient.get_encode_param(project_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.GetEmonGrafanaDashboardsResponse(),
            await self.do_roarequest_async('GetEmonGrafanaDashboards', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/emon/projects/{project_id}/grafana/proxy/api/search', 'json', req, runtime)
        )

    def get_emon_monitor_data(
        self,
        project_id: str,
    ) -> elasticsearch_20170613_models.GetEmonMonitorDataResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_emon_monitor_data_with_options(project_id, headers, runtime)

    async def get_emon_monitor_data_async(
        self,
        project_id: str,
    ) -> elasticsearch_20170613_models.GetEmonMonitorDataResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_emon_monitor_data_with_options_async(project_id, headers, runtime)

    def get_emon_monitor_data_with_options(
        self,
        project_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.GetEmonMonitorDataResponse:
        project_id = OpenApiUtilClient.get_encode_param(project_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.GetEmonMonitorDataResponse(),
            self.do_roarequest('GetEmonMonitorData', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/emon/projects/{project_id}/metrics/query', 'json', req, runtime)
        )

    async def get_emon_monitor_data_with_options_async(
        self,
        project_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.GetEmonMonitorDataResponse:
        project_id = OpenApiUtilClient.get_encode_param(project_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.GetEmonMonitorDataResponse(),
            await self.do_roarequest_async('GetEmonMonitorData', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/emon/projects/{project_id}/metrics/query', 'json', req, runtime)
        )

    def get_open_store_usage(
        self,
        instance_id: str,
    ) -> elasticsearch_20170613_models.GetOpenStoreUsageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_open_store_usage_with_options(instance_id, headers, runtime)

    async def get_open_store_usage_async(
        self,
        instance_id: str,
    ) -> elasticsearch_20170613_models.GetOpenStoreUsageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_open_store_usage_with_options_async(instance_id, headers, runtime)

    def get_open_store_usage_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.GetOpenStoreUsageResponse:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.GetOpenStoreUsageResponse(),
            self.do_roarequest('GetOpenStoreUsage', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/openstore/usage', 'json', req, runtime)
        )

    async def get_open_store_usage_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.GetOpenStoreUsageResponse:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.GetOpenStoreUsageResponse(),
            await self.do_roarequest_async('GetOpenStoreUsage', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/openstore/usage', 'json', req, runtime)
        )

    def get_region_configuration(
        self,
        request: elasticsearch_20170613_models.GetRegionConfigurationRequest,
    ) -> elasticsearch_20170613_models.GetRegionConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_region_configuration_with_options(request, headers, runtime)

    async def get_region_configuration_async(
        self,
        request: elasticsearch_20170613_models.GetRegionConfigurationRequest,
    ) -> elasticsearch_20170613_models.GetRegionConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_region_configuration_with_options_async(request, headers, runtime)

    def get_region_configuration_with_options(
        self,
        request: elasticsearch_20170613_models.GetRegionConfigurationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.GetRegionConfigurationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.zone_id):
            query['zoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.GetRegionConfigurationResponse(),
            self.do_roarequest('GetRegionConfiguration', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/region', 'json', req, runtime)
        )

    async def get_region_configuration_with_options_async(
        self,
        request: elasticsearch_20170613_models.GetRegionConfigurationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.GetRegionConfigurationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.zone_id):
            query['zoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.GetRegionConfigurationResponse(),
            await self.do_roarequest_async('GetRegionConfiguration', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/region', 'json', req, runtime)
        )

    def get_suggest_shrinkable_nodes(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.GetSuggestShrinkableNodesRequest,
    ) -> elasticsearch_20170613_models.GetSuggestShrinkableNodesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_suggest_shrinkable_nodes_with_options(instance_id, request, headers, runtime)

    async def get_suggest_shrinkable_nodes_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.GetSuggestShrinkableNodesRequest,
    ) -> elasticsearch_20170613_models.GetSuggestShrinkableNodesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_suggest_shrinkable_nodes_with_options_async(instance_id, request, headers, runtime)

    def get_suggest_shrinkable_nodes_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.GetSuggestShrinkableNodesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.GetSuggestShrinkableNodesResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.node_type):
            query['nodeType'] = request.node_type
        if not UtilClient.is_unset(request.count):
            query['count'] = request.count
        if not UtilClient.is_unset(request.ignore_status):
            query['ignoreStatus'] = request.ignore_status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.GetSuggestShrinkableNodesResponse(),
            self.do_roarequest('GetSuggestShrinkableNodes', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/suggest-shrinkable-nodes', 'json', req, runtime)
        )

    async def get_suggest_shrinkable_nodes_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.GetSuggestShrinkableNodesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.GetSuggestShrinkableNodesResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.node_type):
            query['nodeType'] = request.node_type
        if not UtilClient.is_unset(request.count):
            query['count'] = request.count
        if not UtilClient.is_unset(request.ignore_status):
            query['ignoreStatus'] = request.ignore_status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.GetSuggestShrinkableNodesResponse(),
            await self.do_roarequest_async('GetSuggestShrinkableNodes', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/suggest-shrinkable-nodes', 'json', req, runtime)
        )

    def get_transferable_nodes(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.GetTransferableNodesRequest,
    ) -> elasticsearch_20170613_models.GetTransferableNodesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_transferable_nodes_with_options(instance_id, request, headers, runtime)

    async def get_transferable_nodes_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.GetTransferableNodesRequest,
    ) -> elasticsearch_20170613_models.GetTransferableNodesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_transferable_nodes_with_options_async(instance_id, request, headers, runtime)

    def get_transferable_nodes_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.GetTransferableNodesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.GetTransferableNodesResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.node_type):
            query['nodeType'] = request.node_type
        if not UtilClient.is_unset(request.count):
            query['count'] = request.count
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.GetTransferableNodesResponse(),
            self.do_roarequest('GetTransferableNodes', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/transferable-nodes', 'json', req, runtime)
        )

    async def get_transferable_nodes_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.GetTransferableNodesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.GetTransferableNodesResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.node_type):
            query['nodeType'] = request.node_type
        if not UtilClient.is_unset(request.count):
            query['count'] = request.count
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.GetTransferableNodesResponse(),
            await self.do_roarequest_async('GetTransferableNodes', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/transferable-nodes', 'json', req, runtime)
        )

    def initialize_operation_role(
        self,
        request: elasticsearch_20170613_models.InitializeOperationRoleRequest,
    ) -> elasticsearch_20170613_models.InitializeOperationRoleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.initialize_operation_role_with_options(request, headers, runtime)

    async def initialize_operation_role_async(
        self,
        request: elasticsearch_20170613_models.InitializeOperationRoleRequest,
    ) -> elasticsearch_20170613_models.InitializeOperationRoleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.initialize_operation_role_with_options_async(request, headers, runtime)

    def initialize_operation_role_with_options(
        self,
        request: elasticsearch_20170613_models.InitializeOperationRoleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.InitializeOperationRoleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.InitializeOperationRoleResponse(),
            self.do_roarequest('InitializeOperationRole', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/user/slr', 'json', req, runtime)
        )

    async def initialize_operation_role_with_options_async(
        self,
        request: elasticsearch_20170613_models.InitializeOperationRoleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.InitializeOperationRoleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.InitializeOperationRoleResponse(),
            await self.do_roarequest_async('InitializeOperationRole', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/user/slr', 'json', req, runtime)
        )

    def install_ack_operator(
        self,
        cluster_id: str,
        request: elasticsearch_20170613_models.InstallAckOperatorRequest,
    ) -> elasticsearch_20170613_models.InstallAckOperatorResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.install_ack_operator_with_options(cluster_id, request, headers, runtime)

    async def install_ack_operator_async(
        self,
        cluster_id: str,
        request: elasticsearch_20170613_models.InstallAckOperatorRequest,
    ) -> elasticsearch_20170613_models.InstallAckOperatorResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.install_ack_operator_with_options_async(cluster_id, request, headers, runtime)

    def install_ack_operator_with_options(
        self,
        cluster_id: str,
        request: elasticsearch_20170613_models.InstallAckOperatorRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.InstallAckOperatorResponse:
        UtilClient.validate_model(request)
        cluster_id = OpenApiUtilClient.get_encode_param(cluster_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.InstallAckOperatorResponse(),
            self.do_roarequest('InstallAckOperator', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/ack-clusters/{cluster_id}/operator', 'json', req, runtime)
        )

    async def install_ack_operator_with_options_async(
        self,
        cluster_id: str,
        request: elasticsearch_20170613_models.InstallAckOperatorRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.InstallAckOperatorResponse:
        UtilClient.validate_model(request)
        cluster_id = OpenApiUtilClient.get_encode_param(cluster_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.InstallAckOperatorResponse(),
            await self.do_roarequest_async('InstallAckOperator', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/ack-clusters/{cluster_id}/operator', 'json', req, runtime)
        )

    def install_kibana_system_plugin(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.InstallKibanaSystemPluginRequest,
    ) -> elasticsearch_20170613_models.InstallKibanaSystemPluginResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.install_kibana_system_plugin_with_options(instance_id, request, headers, runtime)

    async def install_kibana_system_plugin_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.InstallKibanaSystemPluginRequest,
    ) -> elasticsearch_20170613_models.InstallKibanaSystemPluginResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.install_kibana_system_plugin_with_options_async(instance_id, request, headers, runtime)

    def install_kibana_system_plugin_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.InstallKibanaSystemPluginRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.InstallKibanaSystemPluginResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.InstallKibanaSystemPluginResponse(),
            self.do_roarequest('InstallKibanaSystemPlugin', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/kibana-plugins/system/actions/install', 'json', req, runtime)
        )

    async def install_kibana_system_plugin_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.InstallKibanaSystemPluginRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.InstallKibanaSystemPluginResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.InstallKibanaSystemPluginResponse(),
            await self.do_roarequest_async('InstallKibanaSystemPlugin', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/kibana-plugins/system/actions/install', 'json', req, runtime)
        )

    def install_logstash_system_plugin(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.InstallLogstashSystemPluginRequest,
    ) -> elasticsearch_20170613_models.InstallLogstashSystemPluginResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.install_logstash_system_plugin_with_options(instance_id, request, headers, runtime)

    async def install_logstash_system_plugin_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.InstallLogstashSystemPluginRequest,
    ) -> elasticsearch_20170613_models.InstallLogstashSystemPluginResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.install_logstash_system_plugin_with_options_async(instance_id, request, headers, runtime)

    def install_logstash_system_plugin_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.InstallLogstashSystemPluginRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.InstallLogstashSystemPluginResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.InstallLogstashSystemPluginResponse(),
            self.do_roarequest('InstallLogstashSystemPlugin', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/logstashes/{instance_id}/plugins/system/actions/install', 'json', req, runtime)
        )

    async def install_logstash_system_plugin_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.InstallLogstashSystemPluginRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.InstallLogstashSystemPluginResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.InstallLogstashSystemPluginResponse(),
            await self.do_roarequest_async('InstallLogstashSystemPlugin', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/logstashes/{instance_id}/plugins/system/actions/install', 'json', req, runtime)
        )

    def install_system_plugin(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.InstallSystemPluginRequest,
    ) -> elasticsearch_20170613_models.InstallSystemPluginResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.install_system_plugin_with_options(instance_id, request, headers, runtime)

    async def install_system_plugin_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.InstallSystemPluginRequest,
    ) -> elasticsearch_20170613_models.InstallSystemPluginResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.install_system_plugin_with_options_async(instance_id, request, headers, runtime)

    def install_system_plugin_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.InstallSystemPluginRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.InstallSystemPluginResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.InstallSystemPluginResponse(),
            self.do_roarequest('InstallSystemPlugin', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/plugins/system/actions/install', 'json', req, runtime)
        )

    async def install_system_plugin_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.InstallSystemPluginRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.InstallSystemPluginResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.InstallSystemPluginResponse(),
            await self.do_roarequest_async('InstallSystemPlugin', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/plugins/system/actions/install', 'json', req, runtime)
        )

    def install_user_plugins(
        self,
        instance_id: str,
    ) -> elasticsearch_20170613_models.InstallUserPluginsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.install_user_plugins_with_options(instance_id, headers, runtime)

    async def install_user_plugins_async(
        self,
        instance_id: str,
    ) -> elasticsearch_20170613_models.InstallUserPluginsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.install_user_plugins_with_options_async(instance_id, headers, runtime)

    def install_user_plugins_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.InstallUserPluginsResponse:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.InstallUserPluginsResponse(),
            self.do_roarequest('InstallUserPlugins', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/plugins/user/actions/install', 'json', req, runtime)
        )

    async def install_user_plugins_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.InstallUserPluginsResponse:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.InstallUserPluginsResponse(),
            await self.do_roarequest_async('InstallUserPlugins', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/plugins/user/actions/install', 'json', req, runtime)
        )

    def interrupt_elasticsearch_task(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.InterruptElasticsearchTaskRequest,
    ) -> elasticsearch_20170613_models.InterruptElasticsearchTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.interrupt_elasticsearch_task_with_options(instance_id, request, headers, runtime)

    async def interrupt_elasticsearch_task_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.InterruptElasticsearchTaskRequest,
    ) -> elasticsearch_20170613_models.InterruptElasticsearchTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.interrupt_elasticsearch_task_with_options_async(instance_id, request, headers, runtime)

    def interrupt_elasticsearch_task_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.InterruptElasticsearchTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.InterruptElasticsearchTaskResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.InterruptElasticsearchTaskResponse(),
            self.do_roarequest('InterruptElasticsearchTask', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/actions/interrupt', 'json', req, runtime)
        )

    async def interrupt_elasticsearch_task_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.InterruptElasticsearchTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.InterruptElasticsearchTaskResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.InterruptElasticsearchTaskResponse(),
            await self.do_roarequest_async('InterruptElasticsearchTask', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/actions/interrupt', 'json', req, runtime)
        )

    def interrupt_logstash_task(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.InterruptLogstashTaskRequest,
    ) -> elasticsearch_20170613_models.InterruptLogstashTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.interrupt_logstash_task_with_options(instance_id, request, headers, runtime)

    async def interrupt_logstash_task_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.InterruptLogstashTaskRequest,
    ) -> elasticsearch_20170613_models.InterruptLogstashTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.interrupt_logstash_task_with_options_async(instance_id, request, headers, runtime)

    def interrupt_logstash_task_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.InterruptLogstashTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.InterruptLogstashTaskResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.InterruptLogstashTaskResponse(),
            self.do_roarequest('InterruptLogstashTask', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/logstashes/{instance_id}/actions/interrupt', 'json', req, runtime)
        )

    async def interrupt_logstash_task_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.InterruptLogstashTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.InterruptLogstashTaskResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.InterruptLogstashTaskResponse(),
            await self.do_roarequest_async('InterruptLogstashTask', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/logstashes/{instance_id}/actions/interrupt', 'json', req, runtime)
        )

    def list_ack_clusters(
        self,
        request: elasticsearch_20170613_models.ListAckClustersRequest,
    ) -> elasticsearch_20170613_models.ListAckClustersResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_ack_clusters_with_options(request, headers, runtime)

    async def list_ack_clusters_async(
        self,
        request: elasticsearch_20170613_models.ListAckClustersRequest,
    ) -> elasticsearch_20170613_models.ListAckClustersResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_ack_clusters_with_options_async(request, headers, runtime)

    def list_ack_clusters_with_options(
        self,
        request: elasticsearch_20170613_models.ListAckClustersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ListAckClustersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.vpc_id):
            query['vpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListAckClustersResponse(),
            self.do_roarequest('ListAckClusters', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/ack-clusters', 'json', req, runtime)
        )

    async def list_ack_clusters_with_options_async(
        self,
        request: elasticsearch_20170613_models.ListAckClustersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ListAckClustersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.vpc_id):
            query['vpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListAckClustersResponse(),
            await self.do_roarequest_async('ListAckClusters', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/ack-clusters', 'json', req, runtime)
        )

    def list_ack_namespaces(
        self,
        cluster_id: str,
        request: elasticsearch_20170613_models.ListAckNamespacesRequest,
    ) -> elasticsearch_20170613_models.ListAckNamespacesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_ack_namespaces_with_options(cluster_id, request, headers, runtime)

    async def list_ack_namespaces_async(
        self,
        cluster_id: str,
        request: elasticsearch_20170613_models.ListAckNamespacesRequest,
    ) -> elasticsearch_20170613_models.ListAckNamespacesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_ack_namespaces_with_options_async(cluster_id, request, headers, runtime)

    def list_ack_namespaces_with_options(
        self,
        cluster_id: str,
        request: elasticsearch_20170613_models.ListAckNamespacesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ListAckNamespacesResponse:
        UtilClient.validate_model(request)
        cluster_id = OpenApiUtilClient.get_encode_param(cluster_id)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListAckNamespacesResponse(),
            self.do_roarequest('ListAckNamespaces', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/ack-clusters/{cluster_id}/namespaces', 'json', req, runtime)
        )

    async def list_ack_namespaces_with_options_async(
        self,
        cluster_id: str,
        request: elasticsearch_20170613_models.ListAckNamespacesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ListAckNamespacesResponse:
        UtilClient.validate_model(request)
        cluster_id = OpenApiUtilClient.get_encode_param(cluster_id)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListAckNamespacesResponse(),
            await self.do_roarequest_async('ListAckNamespaces', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/ack-clusters/{cluster_id}/namespaces', 'json', req, runtime)
        )

    def list_all_node(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ListAllNodeRequest,
    ) -> elasticsearch_20170613_models.ListAllNodeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_all_node_with_options(instance_id, request, headers, runtime)

    async def list_all_node_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ListAllNodeRequest,
    ) -> elasticsearch_20170613_models.ListAllNodeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_all_node_with_options_async(instance_id, request, headers, runtime)

    def list_all_node_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ListAllNodeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ListAllNodeResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.extended):
            query['extended'] = request.extended
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListAllNodeResponse(),
            self.do_roarequest('ListAllNode', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/nodes', 'json', req, runtime)
        )

    async def list_all_node_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ListAllNodeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ListAllNodeResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.extended):
            query['extended'] = request.extended
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListAllNodeResponse(),
            await self.do_roarequest_async('ListAllNode', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/nodes', 'json', req, runtime)
        )

    def list_alternative_snapshot_repos(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ListAlternativeSnapshotReposRequest,
    ) -> elasticsearch_20170613_models.ListAlternativeSnapshotReposResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_alternative_snapshot_repos_with_options(instance_id, request, headers, runtime)

    async def list_alternative_snapshot_repos_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ListAlternativeSnapshotReposRequest,
    ) -> elasticsearch_20170613_models.ListAlternativeSnapshotReposResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_alternative_snapshot_repos_with_options_async(instance_id, request, headers, runtime)

    def list_alternative_snapshot_repos_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ListAlternativeSnapshotReposRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ListAlternativeSnapshotReposResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.already_set_items):
            query['alreadySetItems'] = request.already_set_items
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListAlternativeSnapshotReposResponse(),
            self.do_roarequest('ListAlternativeSnapshotRepos', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/alternative-snapshot-repos', 'json', req, runtime)
        )

    async def list_alternative_snapshot_repos_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ListAlternativeSnapshotReposRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ListAlternativeSnapshotReposResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.already_set_items):
            query['alreadySetItems'] = request.already_set_items
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListAlternativeSnapshotReposResponse(),
            await self.do_roarequest_async('ListAlternativeSnapshotRepos', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/alternative-snapshot-repos', 'json', req, runtime)
        )

    def list_available_es_instance_ids(
        self,
        instance_id: str,
    ) -> elasticsearch_20170613_models.ListAvailableEsInstanceIdsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_available_es_instance_ids_with_options(instance_id, headers, runtime)

    async def list_available_es_instance_ids_async(
        self,
        instance_id: str,
    ) -> elasticsearch_20170613_models.ListAvailableEsInstanceIdsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_available_es_instance_ids_with_options_async(instance_id, headers, runtime)

    def list_available_es_instance_ids_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ListAvailableEsInstanceIdsResponse:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListAvailableEsInstanceIdsResponse(),
            self.do_roarequest('ListAvailableEsInstanceIds', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/logstashes/{instance_id}/available-elasticsearch-for-centralized-management', 'json', req, runtime)
        )

    async def list_available_es_instance_ids_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ListAvailableEsInstanceIdsResponse:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListAvailableEsInstanceIdsResponse(),
            await self.do_roarequest_async('ListAvailableEsInstanceIds', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/logstashes/{instance_id}/available-elasticsearch-for-centralized-management', 'json', req, runtime)
        )

    def list_collectors(
        self,
        request: elasticsearch_20170613_models.ListCollectorsRequest,
    ) -> elasticsearch_20170613_models.ListCollectorsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_collectors_with_options(request, headers, runtime)

    async def list_collectors_async(
        self,
        request: elasticsearch_20170613_models.ListCollectorsRequest,
    ) -> elasticsearch_20170613_models.ListCollectorsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_collectors_with_options_async(request, headers, runtime)

    def list_collectors_with_options(
        self,
        request: elasticsearch_20170613_models.ListCollectorsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ListCollectorsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.res_id):
            query['resId'] = request.res_id
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.instance_id):
            query['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.source_type):
            query['sourceType'] = request.source_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListCollectorsResponse(),
            self.do_roarequest('ListCollectors', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/collectors', 'json', req, runtime)
        )

    async def list_collectors_with_options_async(
        self,
        request: elasticsearch_20170613_models.ListCollectorsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ListCollectorsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.res_id):
            query['resId'] = request.res_id
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.instance_id):
            query['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.source_type):
            query['sourceType'] = request.source_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListCollectorsResponse(),
            await self.do_roarequest_async('ListCollectors', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/collectors', 'json', req, runtime)
        )

    def list_connected_clusters(
        self,
        instance_id: str,
    ) -> elasticsearch_20170613_models.ListConnectedClustersResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_connected_clusters_with_options(instance_id, headers, runtime)

    async def list_connected_clusters_async(
        self,
        instance_id: str,
    ) -> elasticsearch_20170613_models.ListConnectedClustersResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_connected_clusters_with_options_async(instance_id, headers, runtime)

    def list_connected_clusters_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ListConnectedClustersResponse:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListConnectedClustersResponse(),
            self.do_roarequest('ListConnectedClusters', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/connected-clusters', 'json', req, runtime)
        )

    async def list_connected_clusters_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ListConnectedClustersResponse:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListConnectedClustersResponse(),
            await self.do_roarequest_async('ListConnectedClusters', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/connected-clusters', 'json', req, runtime)
        )

    def list_data_streams(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ListDataStreamsRequest,
    ) -> elasticsearch_20170613_models.ListDataStreamsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_data_streams_with_options(instance_id, request, headers, runtime)

    async def list_data_streams_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ListDataStreamsRequest,
    ) -> elasticsearch_20170613_models.ListDataStreamsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_data_streams_with_options_async(instance_id, request, headers, runtime)

    def list_data_streams_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ListDataStreamsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ListDataStreamsResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.is_managed):
            query['isManaged'] = request.is_managed
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListDataStreamsResponse(),
            self.do_roarequest('ListDataStreams', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/data-streams', 'json', req, runtime)
        )

    async def list_data_streams_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ListDataStreamsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ListDataStreamsResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.is_managed):
            query['isManaged'] = request.is_managed
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListDataStreamsResponse(),
            await self.do_roarequest_async('ListDataStreams', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/data-streams', 'json', req, runtime)
        )

    def list_data_tasks(
        self,
        instance_id: str,
    ) -> elasticsearch_20170613_models.ListDataTasksResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_data_tasks_with_options(instance_id, headers, runtime)

    async def list_data_tasks_async(
        self,
        instance_id: str,
    ) -> elasticsearch_20170613_models.ListDataTasksResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_data_tasks_with_options_async(instance_id, headers, runtime)

    def list_data_tasks_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ListDataTasksResponse:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListDataTasksResponse(),
            self.do_roarequest('ListDataTasks', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/data-task', 'json', req, runtime)
        )

    async def list_data_tasks_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ListDataTasksResponse:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListDataTasksResponse(),
            await self.do_roarequest_async('ListDataTasks', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/data-task', 'json', req, runtime)
        )

    def list_default_collector_configurations(
        self,
        request: elasticsearch_20170613_models.ListDefaultCollectorConfigurationsRequest,
    ) -> elasticsearch_20170613_models.ListDefaultCollectorConfigurationsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_default_collector_configurations_with_options(request, headers, runtime)

    async def list_default_collector_configurations_async(
        self,
        request: elasticsearch_20170613_models.ListDefaultCollectorConfigurationsRequest,
    ) -> elasticsearch_20170613_models.ListDefaultCollectorConfigurationsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_default_collector_configurations_with_options_async(request, headers, runtime)

    def list_default_collector_configurations_with_options(
        self,
        request: elasticsearch_20170613_models.ListDefaultCollectorConfigurationsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ListDefaultCollectorConfigurationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.res_type):
            query['resType'] = request.res_type
        if not UtilClient.is_unset(request.res_version):
            query['resVersion'] = request.res_version
        if not UtilClient.is_unset(request.source_type):
            query['sourceType'] = request.source_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListDefaultCollectorConfigurationsResponse(),
            self.do_roarequest('ListDefaultCollectorConfigurations', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/beats/default-configurations', 'json', req, runtime)
        )

    async def list_default_collector_configurations_with_options_async(
        self,
        request: elasticsearch_20170613_models.ListDefaultCollectorConfigurationsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ListDefaultCollectorConfigurationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.res_type):
            query['resType'] = request.res_type
        if not UtilClient.is_unset(request.res_version):
            query['resVersion'] = request.res_version
        if not UtilClient.is_unset(request.source_type):
            query['sourceType'] = request.source_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListDefaultCollectorConfigurationsResponse(),
            await self.do_roarequest_async('ListDefaultCollectorConfigurations', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/beats/default-configurations', 'json', req, runtime)
        )

    def list_diagnose_indices(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ListDiagnoseIndicesRequest,
    ) -> elasticsearch_20170613_models.ListDiagnoseIndicesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_diagnose_indices_with_options(instance_id, request, headers, runtime)

    async def list_diagnose_indices_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ListDiagnoseIndicesRequest,
    ) -> elasticsearch_20170613_models.ListDiagnoseIndicesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_diagnose_indices_with_options_async(instance_id, request, headers, runtime)

    def list_diagnose_indices_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ListDiagnoseIndicesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ListDiagnoseIndicesResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListDiagnoseIndicesResponse(),
            self.do_roarequest('ListDiagnoseIndices', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/diagnosis/instances/{instance_id}/indices', 'json', req, runtime)
        )

    async def list_diagnose_indices_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ListDiagnoseIndicesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ListDiagnoseIndicesResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListDiagnoseIndicesResponse(),
            await self.do_roarequest_async('ListDiagnoseIndices', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/diagnosis/instances/{instance_id}/indices', 'json', req, runtime)
        )

    def list_diagnose_report(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ListDiagnoseReportRequest,
    ) -> elasticsearch_20170613_models.ListDiagnoseReportResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_diagnose_report_with_options(instance_id, request, headers, runtime)

    async def list_diagnose_report_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ListDiagnoseReportRequest,
    ) -> elasticsearch_20170613_models.ListDiagnoseReportResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_diagnose_report_with_options_async(instance_id, request, headers, runtime)

    def list_diagnose_report_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ListDiagnoseReportRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ListDiagnoseReportResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['lang'] = request.lang
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.detail):
            query['detail'] = request.detail
        if not UtilClient.is_unset(request.trigger):
            query['trigger'] = request.trigger
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListDiagnoseReportResponse(),
            self.do_roarequest('ListDiagnoseReport', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/diagnosis/instances/{instance_id}/reports', 'json', req, runtime)
        )

    async def list_diagnose_report_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ListDiagnoseReportRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ListDiagnoseReportResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['lang'] = request.lang
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.detail):
            query['detail'] = request.detail
        if not UtilClient.is_unset(request.trigger):
            query['trigger'] = request.trigger
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListDiagnoseReportResponse(),
            await self.do_roarequest_async('ListDiagnoseReport', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/diagnosis/instances/{instance_id}/reports', 'json', req, runtime)
        )

    def list_diagnose_report_ids(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ListDiagnoseReportIdsRequest,
    ) -> elasticsearch_20170613_models.ListDiagnoseReportIdsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_diagnose_report_ids_with_options(instance_id, request, headers, runtime)

    async def list_diagnose_report_ids_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ListDiagnoseReportIdsRequest,
    ) -> elasticsearch_20170613_models.ListDiagnoseReportIdsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_diagnose_report_ids_with_options_async(instance_id, request, headers, runtime)

    def list_diagnose_report_ids_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ListDiagnoseReportIdsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ListDiagnoseReportIdsResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['lang'] = request.lang
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.trigger):
            query['trigger'] = request.trigger
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListDiagnoseReportIdsResponse(),
            self.do_roarequest('ListDiagnoseReportIds', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/diagnosis/instances/{instance_id}/report-ids', 'json', req, runtime)
        )

    async def list_diagnose_report_ids_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ListDiagnoseReportIdsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ListDiagnoseReportIdsResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['lang'] = request.lang
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.trigger):
            query['trigger'] = request.trigger
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListDiagnoseReportIdsResponse(),
            await self.do_roarequest_async('ListDiagnoseReportIds', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/diagnosis/instances/{instance_id}/report-ids', 'json', req, runtime)
        )

    def list_dict_information(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ListDictInformationRequest,
    ) -> elasticsearch_20170613_models.ListDictInformationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_dict_information_with_options(instance_id, request, headers, runtime)

    async def list_dict_information_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ListDictInformationRequest,
    ) -> elasticsearch_20170613_models.ListDictInformationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_dict_information_with_options_async(instance_id, request, headers, runtime)

    def list_dict_information_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ListDictInformationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ListDictInformationResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.bucket_name):
            query['bucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.key):
            query['key'] = request.key
        if not UtilClient.is_unset(request.analyzer_type):
            query['analyzerType'] = request.analyzer_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListDictInformationResponse(),
            self.do_roarequest('ListDictInformation', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/dict/_info', 'json', req, runtime)
        )

    async def list_dict_information_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ListDictInformationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ListDictInformationResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.bucket_name):
            query['bucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.key):
            query['key'] = request.key
        if not UtilClient.is_unset(request.analyzer_type):
            query['analyzerType'] = request.analyzer_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListDictInformationResponse(),
            await self.do_roarequest_async('ListDictInformation', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/dict/_info', 'json', req, runtime)
        )

    def list_dicts(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ListDictsRequest,
    ) -> elasticsearch_20170613_models.ListDictsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_dicts_with_options(instance_id, request, headers, runtime)

    async def list_dicts_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ListDictsRequest,
    ) -> elasticsearch_20170613_models.ListDictsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_dicts_with_options_async(instance_id, request, headers, runtime)

    def list_dicts_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ListDictsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ListDictsResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.analyzer_type):
            query['analyzerType'] = request.analyzer_type
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListDictsResponse(),
            self.do_roarequest('ListDicts', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/dicts', 'json', req, runtime)
        )

    async def list_dicts_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ListDictsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ListDictsResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.analyzer_type):
            query['analyzerType'] = request.analyzer_type
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListDictsResponse(),
            await self.do_roarequest_async('ListDicts', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/dicts', 'json', req, runtime)
        )

    def list_ecs_instances(
        self,
        request: elasticsearch_20170613_models.ListEcsInstancesRequest,
    ) -> elasticsearch_20170613_models.ListEcsInstancesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_ecs_instances_with_options(request, headers, runtime)

    async def list_ecs_instances_async(
        self,
        request: elasticsearch_20170613_models.ListEcsInstancesRequest,
    ) -> elasticsearch_20170613_models.ListEcsInstancesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_ecs_instances_with_options_async(request, headers, runtime)

    def list_ecs_instances_with_options(
        self,
        request: elasticsearch_20170613_models.ListEcsInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ListEcsInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.ecs_instance_ids):
            query['ecsInstanceIds'] = request.ecs_instance_ids
        if not UtilClient.is_unset(request.ecs_instance_name):
            query['ecsInstanceName'] = request.ecs_instance_name
        if not UtilClient.is_unset(request.tags):
            query['tags'] = request.tags
        if not UtilClient.is_unset(request.vpc_id):
            query['vpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListEcsInstancesResponse(),
            self.do_roarequest('ListEcsInstances', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/ecs', 'json', req, runtime)
        )

    async def list_ecs_instances_with_options_async(
        self,
        request: elasticsearch_20170613_models.ListEcsInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ListEcsInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.ecs_instance_ids):
            query['ecsInstanceIds'] = request.ecs_instance_ids
        if not UtilClient.is_unset(request.ecs_instance_name):
            query['ecsInstanceName'] = request.ecs_instance_name
        if not UtilClient.is_unset(request.tags):
            query['tags'] = request.tags
        if not UtilClient.is_unset(request.vpc_id):
            query['vpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListEcsInstancesResponse(),
            await self.do_roarequest_async('ListEcsInstances', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/ecs', 'json', req, runtime)
        )

    def list_extendfiles(
        self,
        instance_id: str,
    ) -> elasticsearch_20170613_models.ListExtendfilesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_extendfiles_with_options(instance_id, headers, runtime)

    async def list_extendfiles_async(
        self,
        instance_id: str,
    ) -> elasticsearch_20170613_models.ListExtendfilesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_extendfiles_with_options_async(instance_id, headers, runtime)

    def list_extendfiles_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ListExtendfilesResponse:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListExtendfilesResponse(),
            self.do_roarequest('ListExtendfiles', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/logstashes/{instance_id}/extendfiles', 'json', req, runtime)
        )

    async def list_extendfiles_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ListExtendfilesResponse:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListExtendfilesResponse(),
            await self.do_roarequest_async('ListExtendfiles', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/logstashes/{instance_id}/extendfiles', 'json', req, runtime)
        )

    def list_ilmpolicies(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ListILMPoliciesRequest,
    ) -> elasticsearch_20170613_models.ListILMPoliciesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_ilmpolicies_with_options(instance_id, request, headers, runtime)

    async def list_ilmpolicies_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ListILMPoliciesRequest,
    ) -> elasticsearch_20170613_models.ListILMPoliciesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_ilmpolicies_with_options_async(instance_id, request, headers, runtime)

    def list_ilmpolicies_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ListILMPoliciesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ListILMPoliciesResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.policy_name):
            query['policyName'] = request.policy_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListILMPoliciesResponse(),
            self.do_roarequest('ListILMPolicies', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/ilm-policies', 'json', req, runtime)
        )

    async def list_ilmpolicies_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ListILMPoliciesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ListILMPoliciesResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.policy_name):
            query['policyName'] = request.policy_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListILMPoliciesResponse(),
            await self.do_roarequest_async('ListILMPolicies', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/ilm-policies', 'json', req, runtime)
        )

    def list_index_templates(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ListIndexTemplatesRequest,
    ) -> elasticsearch_20170613_models.ListIndexTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_index_templates_with_options(instance_id, request, headers, runtime)

    async def list_index_templates_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ListIndexTemplatesRequest,
    ) -> elasticsearch_20170613_models.ListIndexTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_index_templates_with_options_async(instance_id, request, headers, runtime)

    def list_index_templates_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ListIndexTemplatesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ListIndexTemplatesResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.index_template):
            query['indexTemplate'] = request.index_template
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListIndexTemplatesResponse(),
            self.do_roarequest('ListIndexTemplates', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/index-templates', 'json', req, runtime)
        )

    async def list_index_templates_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ListIndexTemplatesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ListIndexTemplatesResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.index_template):
            query['indexTemplate'] = request.index_template
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListIndexTemplatesResponse(),
            await self.do_roarequest_async('ListIndexTemplates', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/index-templates', 'json', req, runtime)
        )

    def list_instance(
        self,
        request: elasticsearch_20170613_models.ListInstanceRequest,
    ) -> elasticsearch_20170613_models.ListInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_instance_with_options(request, headers, runtime)

    async def list_instance_async(
        self,
        request: elasticsearch_20170613_models.ListInstanceRequest,
    ) -> elasticsearch_20170613_models.ListInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_instance_with_options_async(request, headers, runtime)

    def list_instance_with_options(
        self,
        request: elasticsearch_20170613_models.ListInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ListInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.description):
            query['description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.es_version):
            query['esVersion'] = request.es_version
        if not UtilClient.is_unset(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tags):
            query['tags'] = request.tags
        if not UtilClient.is_unset(request.vpc_id):
            query['vpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            query['zoneId'] = request.zone_id
        if not UtilClient.is_unset(request.payment_type):
            query['paymentType'] = request.payment_type
        if not UtilClient.is_unset(request.instance_category):
            query['instanceCategory'] = request.instance_category
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListInstanceResponse(),
            self.do_roarequest('ListInstance', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/instances', 'json', req, runtime)
        )

    async def list_instance_with_options_async(
        self,
        request: elasticsearch_20170613_models.ListInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ListInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.description):
            query['description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.es_version):
            query['esVersion'] = request.es_version
        if not UtilClient.is_unset(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tags):
            query['tags'] = request.tags
        if not UtilClient.is_unset(request.vpc_id):
            query['vpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            query['zoneId'] = request.zone_id
        if not UtilClient.is_unset(request.payment_type):
            query['paymentType'] = request.payment_type
        if not UtilClient.is_unset(request.instance_category):
            query['instanceCategory'] = request.instance_category
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListInstanceResponse(),
            await self.do_roarequest_async('ListInstance', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/instances', 'json', req, runtime)
        )

    def list_instance_indices(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ListInstanceIndicesRequest,
    ) -> elasticsearch_20170613_models.ListInstanceIndicesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_instance_indices_with_options(instance_id, request, headers, runtime)

    async def list_instance_indices_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ListInstanceIndicesRequest,
    ) -> elasticsearch_20170613_models.ListInstanceIndicesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_instance_indices_with_options_async(instance_id, request, headers, runtime)

    def list_instance_indices_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ListInstanceIndicesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ListInstanceIndicesResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['all'] = request.all
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.is_managed):
            query['isManaged'] = request.is_managed
        if not UtilClient.is_unset(request.is_openstore):
            query['isOpenstore'] = request.is_openstore
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListInstanceIndicesResponse(),
            self.do_roarequest('ListInstanceIndices', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/indices', 'json', req, runtime)
        )

    async def list_instance_indices_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ListInstanceIndicesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ListInstanceIndicesResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['all'] = request.all
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.is_managed):
            query['isManaged'] = request.is_managed
        if not UtilClient.is_unset(request.is_openstore):
            query['isOpenstore'] = request.is_openstore
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListInstanceIndicesResponse(),
            await self.do_roarequest_async('ListInstanceIndices', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/indices', 'json', req, runtime)
        )

    def list_kibana_plugins(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ListKibanaPluginsRequest,
    ) -> elasticsearch_20170613_models.ListKibanaPluginsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_kibana_plugins_with_options(instance_id, request, headers, runtime)

    async def list_kibana_plugins_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ListKibanaPluginsRequest,
    ) -> elasticsearch_20170613_models.ListKibanaPluginsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_kibana_plugins_with_options_async(instance_id, request, headers, runtime)

    def list_kibana_plugins_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ListKibanaPluginsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ListKibanaPluginsResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListKibanaPluginsResponse(),
            self.do_roarequest('ListKibanaPlugins', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/kibana-plugins', 'json', req, runtime)
        )

    async def list_kibana_plugins_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ListKibanaPluginsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ListKibanaPluginsResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListKibanaPluginsResponse(),
            await self.do_roarequest_async('ListKibanaPlugins', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/kibana-plugins', 'json', req, runtime)
        )

    def list_logstash(
        self,
        request: elasticsearch_20170613_models.ListLogstashRequest,
    ) -> elasticsearch_20170613_models.ListLogstashResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_logstash_with_options(request, headers, runtime)

    async def list_logstash_async(
        self,
        request: elasticsearch_20170613_models.ListLogstashRequest,
    ) -> elasticsearch_20170613_models.ListLogstashResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_logstash_with_options_async(request, headers, runtime)

    def list_logstash_with_options(
        self,
        request: elasticsearch_20170613_models.ListLogstashRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ListLogstashResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.description):
            query['description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.version):
            query['version'] = request.version
        if not UtilClient.is_unset(request.owner_id):
            query['ownerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListLogstashResponse(),
            self.do_roarequest('ListLogstash', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/logstashes', 'json', req, runtime)
        )

    async def list_logstash_with_options_async(
        self,
        request: elasticsearch_20170613_models.ListLogstashRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ListLogstashResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.description):
            query['description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.version):
            query['version'] = request.version
        if not UtilClient.is_unset(request.owner_id):
            query['ownerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListLogstashResponse(),
            await self.do_roarequest_async('ListLogstash', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/logstashes', 'json', req, runtime)
        )

    def list_logstash_log(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ListLogstashLogRequest,
    ) -> elasticsearch_20170613_models.ListLogstashLogResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_logstash_log_with_options(instance_id, request, headers, runtime)

    async def list_logstash_log_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ListLogstashLogRequest,
    ) -> elasticsearch_20170613_models.ListLogstashLogResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_logstash_log_with_options_async(instance_id, request, headers, runtime)

    def list_logstash_log_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ListLogstashLogRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ListLogstashLogResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        if not UtilClient.is_unset(request.query):
            query['query'] = request.query
        if not UtilClient.is_unset(request.begin_time):
            query['beginTime'] = request.begin_time
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListLogstashLogResponse(),
            self.do_roarequest('ListLogstashLog', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/logstashes/{instance_id}/search-log', 'json', req, runtime)
        )

    async def list_logstash_log_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ListLogstashLogRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ListLogstashLogResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        if not UtilClient.is_unset(request.query):
            query['query'] = request.query
        if not UtilClient.is_unset(request.begin_time):
            query['beginTime'] = request.begin_time
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListLogstashLogResponse(),
            await self.do_roarequest_async('ListLogstashLog', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/logstashes/{instance_id}/search-log', 'json', req, runtime)
        )

    def list_logstash_plugins(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ListLogstashPluginsRequest,
    ) -> elasticsearch_20170613_models.ListLogstashPluginsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_logstash_plugins_with_options(instance_id, request, headers, runtime)

    async def list_logstash_plugins_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ListLogstashPluginsRequest,
    ) -> elasticsearch_20170613_models.ListLogstashPluginsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_logstash_plugins_with_options_async(instance_id, request, headers, runtime)

    def list_logstash_plugins_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ListLogstashPluginsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ListLogstashPluginsResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.source):
            query['source'] = request.source
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListLogstashPluginsResponse(),
            self.do_roarequest('ListLogstashPlugins', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/logstashes/{instance_id}/plugins', 'json', req, runtime)
        )

    async def list_logstash_plugins_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ListLogstashPluginsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ListLogstashPluginsResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.source):
            query['source'] = request.source
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListLogstashPluginsResponse(),
            await self.do_roarequest_async('ListLogstashPlugins', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/logstashes/{instance_id}/plugins', 'json', req, runtime)
        )

    def list_nodes(
        self,
        res_id: str,
        request: elasticsearch_20170613_models.ListNodesRequest,
    ) -> elasticsearch_20170613_models.ListNodesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_nodes_with_options(res_id, request, headers, runtime)

    async def list_nodes_async(
        self,
        res_id: str,
        request: elasticsearch_20170613_models.ListNodesRequest,
    ) -> elasticsearch_20170613_models.ListNodesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_nodes_with_options_async(res_id, request, headers, runtime)

    def list_nodes_with_options(
        self,
        res_id: str,
        request: elasticsearch_20170613_models.ListNodesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ListNodesResponse:
        UtilClient.validate_model(request)
        res_id = OpenApiUtilClient.get_encode_param(res_id)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.ecs_instance_ids):
            query['ecsInstanceIds'] = request.ecs_instance_ids
        if not UtilClient.is_unset(request.ecs_instance_name):
            query['ecsInstanceName'] = request.ecs_instance_name
        if not UtilClient.is_unset(request.tags):
            query['tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListNodesResponse(),
            self.do_roarequest('ListNodes', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/collectors/{res_id}/nodes', 'json', req, runtime)
        )

    async def list_nodes_with_options_async(
        self,
        res_id: str,
        request: elasticsearch_20170613_models.ListNodesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ListNodesResponse:
        UtilClient.validate_model(request)
        res_id = OpenApiUtilClient.get_encode_param(res_id)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.ecs_instance_ids):
            query['ecsInstanceIds'] = request.ecs_instance_ids
        if not UtilClient.is_unset(request.ecs_instance_name):
            query['ecsInstanceName'] = request.ecs_instance_name
        if not UtilClient.is_unset(request.tags):
            query['tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListNodesResponse(),
            await self.do_roarequest_async('ListNodes', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/collectors/{res_id}/nodes', 'json', req, runtime)
        )

    def list_pipeline(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ListPipelineRequest,
    ) -> elasticsearch_20170613_models.ListPipelineResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_pipeline_with_options(instance_id, request, headers, runtime)

    async def list_pipeline_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ListPipelineRequest,
    ) -> elasticsearch_20170613_models.ListPipelineResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_pipeline_with_options_async(instance_id, request, headers, runtime)

    def list_pipeline_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ListPipelineRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ListPipelineResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.pipeline_id):
            query['pipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListPipelineResponse(),
            self.do_roarequest('ListPipeline', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/logstashes/{instance_id}/pipelines', 'json', req, runtime)
        )

    async def list_pipeline_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ListPipelineRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ListPipelineResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.pipeline_id):
            query['pipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListPipelineResponse(),
            await self.do_roarequest_async('ListPipeline', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/logstashes/{instance_id}/pipelines', 'json', req, runtime)
        )

    def list_pipeline_ids(
        self,
        instance_id: str,
    ) -> elasticsearch_20170613_models.ListPipelineIdsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_pipeline_ids_with_options(instance_id, headers, runtime)

    async def list_pipeline_ids_async(
        self,
        instance_id: str,
    ) -> elasticsearch_20170613_models.ListPipelineIdsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_pipeline_ids_with_options_async(instance_id, headers, runtime)

    def list_pipeline_ids_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ListPipelineIdsResponse:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListPipelineIdsResponse(),
            self.do_roarequest('ListPipelineIds', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/pipeline-ids', 'json', req, runtime)
        )

    async def list_pipeline_ids_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ListPipelineIdsResponse:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListPipelineIdsResponse(),
            await self.do_roarequest_async('ListPipelineIds', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/pipeline-ids', 'json', req, runtime)
        )

    def list_plugins(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ListPluginsRequest,
    ) -> elasticsearch_20170613_models.ListPluginsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_plugins_with_options(instance_id, request, headers, runtime)

    async def list_plugins_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ListPluginsRequest,
    ) -> elasticsearch_20170613_models.ListPluginsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_plugins_with_options_async(instance_id, request, headers, runtime)

    def list_plugins_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ListPluginsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ListPluginsResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.source):
            query['source'] = request.source
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListPluginsResponse(),
            self.do_roarequest('ListPlugins', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/plugins', 'json', req, runtime)
        )

    async def list_plugins_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ListPluginsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ListPluginsResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.source):
            query['source'] = request.source
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListPluginsResponse(),
            await self.do_roarequest_async('ListPlugins', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/plugins', 'json', req, runtime)
        )

    def list_search_log(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ListSearchLogRequest,
    ) -> elasticsearch_20170613_models.ListSearchLogResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_search_log_with_options(instance_id, request, headers, runtime)

    async def list_search_log_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ListSearchLogRequest,
    ) -> elasticsearch_20170613_models.ListSearchLogResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_search_log_with_options_async(instance_id, request, headers, runtime)

    def list_search_log_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ListSearchLogRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ListSearchLogResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        if not UtilClient.is_unset(request.query):
            query['query'] = request.query
        if not UtilClient.is_unset(request.begin_time):
            query['beginTime'] = request.begin_time
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListSearchLogResponse(),
            self.do_roarequest('ListSearchLog', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/search-log', 'json', req, runtime)
        )

    async def list_search_log_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ListSearchLogRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ListSearchLogResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        if not UtilClient.is_unset(request.query):
            query['query'] = request.query
        if not UtilClient.is_unset(request.begin_time):
            query['beginTime'] = request.begin_time
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListSearchLogResponse(),
            await self.do_roarequest_async('ListSearchLog', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/search-log', 'json', req, runtime)
        )

    def list_shard_recoveries(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ListShardRecoveriesRequest,
    ) -> elasticsearch_20170613_models.ListShardRecoveriesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_shard_recoveries_with_options(instance_id, request, headers, runtime)

    async def list_shard_recoveries_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ListShardRecoveriesRequest,
    ) -> elasticsearch_20170613_models.ListShardRecoveriesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_shard_recoveries_with_options_async(instance_id, request, headers, runtime)

    def list_shard_recoveries_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ListShardRecoveriesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ListShardRecoveriesResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.active_only):
            query['activeOnly'] = request.active_only
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListShardRecoveriesResponse(),
            self.do_roarequest('ListShardRecoveries', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/cat-recovery', 'json', req, runtime)
        )

    async def list_shard_recoveries_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ListShardRecoveriesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ListShardRecoveriesResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.active_only):
            query['activeOnly'] = request.active_only
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListShardRecoveriesResponse(),
            await self.do_roarequest_async('ListShardRecoveries', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/cat-recovery', 'json', req, runtime)
        )

    def list_snapshot_repos_by_instance_id(
        self,
        instance_id: str,
    ) -> elasticsearch_20170613_models.ListSnapshotReposByInstanceIdResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_snapshot_repos_by_instance_id_with_options(instance_id, headers, runtime)

    async def list_snapshot_repos_by_instance_id_async(
        self,
        instance_id: str,
    ) -> elasticsearch_20170613_models.ListSnapshotReposByInstanceIdResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_snapshot_repos_by_instance_id_with_options_async(instance_id, headers, runtime)

    def list_snapshot_repos_by_instance_id_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ListSnapshotReposByInstanceIdResponse:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListSnapshotReposByInstanceIdResponse(),
            self.do_roarequest('ListSnapshotReposByInstanceId', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/snapshot-repos', 'json', req, runtime)
        )

    async def list_snapshot_repos_by_instance_id_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ListSnapshotReposByInstanceIdResponse:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListSnapshotReposByInstanceIdResponse(),
            await self.do_roarequest_async('ListSnapshotReposByInstanceId', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/snapshot-repos', 'json', req, runtime)
        )

    def list_tag_resources(
        self,
        request: elasticsearch_20170613_models.ListTagResourcesRequest,
    ) -> elasticsearch_20170613_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_tag_resources_with_options(request, headers, runtime)

    async def list_tag_resources_async(
        self,
        request: elasticsearch_20170613_models.ListTagResourcesRequest,
    ) -> elasticsearch_20170613_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_tag_resources_with_options_async(request, headers, runtime)

    def list_tag_resources_with_options(
        self,
        request: elasticsearch_20170613_models.ListTagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListTagResourcesResponse(),
            self.do_roarequest('ListTagResources', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/tags', 'json', req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: elasticsearch_20170613_models.ListTagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListTagResourcesResponse(),
            await self.do_roarequest_async('ListTagResources', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/tags', 'json', req, runtime)
        )

    def list_tags(
        self,
        request: elasticsearch_20170613_models.ListTagsRequest,
    ) -> elasticsearch_20170613_models.ListTagsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_tags_with_options(request, headers, runtime)

    async def list_tags_async(
        self,
        request: elasticsearch_20170613_models.ListTagsRequest,
    ) -> elasticsearch_20170613_models.ListTagsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_tags_with_options_async(request, headers, runtime)

    def list_tags_with_options(
        self,
        request: elasticsearch_20170613_models.ListTagsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ListTagsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_type):
            query['resourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListTagsResponse(),
            self.do_roarequest('ListTags', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/tags/all-tags', 'json', req, runtime)
        )

    async def list_tags_with_options_async(
        self,
        request: elasticsearch_20170613_models.ListTagsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ListTagsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_type):
            query['resourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListTagsResponse(),
            await self.do_roarequest_async('ListTags', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/tags/all-tags', 'json', req, runtime)
        )

    def list_vpc_endpoints(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ListVpcEndpointsRequest,
    ) -> elasticsearch_20170613_models.ListVpcEndpointsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_vpc_endpoints_with_options(instance_id, request, headers, runtime)

    async def list_vpc_endpoints_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ListVpcEndpointsRequest,
    ) -> elasticsearch_20170613_models.ListVpcEndpointsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_vpc_endpoints_with_options_async(instance_id, request, headers, runtime)

    def list_vpc_endpoints_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ListVpcEndpointsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ListVpcEndpointsResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListVpcEndpointsResponse(),
            self.do_roarequest('ListVpcEndpoints', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/vpc-endpoints', 'json', req, runtime)
        )

    async def list_vpc_endpoints_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ListVpcEndpointsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ListVpcEndpointsResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListVpcEndpointsResponse(),
            await self.do_roarequest_async('ListVpcEndpoints', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/vpc-endpoints', 'json', req, runtime)
        )

    def migrate_to_other_zone(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.MigrateToOtherZoneRequest,
    ) -> elasticsearch_20170613_models.MigrateToOtherZoneResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.migrate_to_other_zone_with_options(instance_id, request, headers, runtime)

    async def migrate_to_other_zone_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.MigrateToOtherZoneRequest,
    ) -> elasticsearch_20170613_models.MigrateToOtherZoneResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.migrate_to_other_zone_with_options_async(instance_id, request, headers, runtime)

    def migrate_to_other_zone_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.MigrateToOtherZoneRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.MigrateToOtherZoneResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.MigrateToOtherZoneResponse(),
            self.do_roarequest('MigrateToOtherZone', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/actions/migrate-zones', 'json', req, runtime)
        )

    async def migrate_to_other_zone_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.MigrateToOtherZoneRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.MigrateToOtherZoneResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.MigrateToOtherZoneResponse(),
            await self.do_roarequest_async('MigrateToOtherZone', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/actions/migrate-zones', 'json', req, runtime)
        )

    def modify_deploy_machine(
        self,
        res_id: str,
        request: elasticsearch_20170613_models.ModifyDeployMachineRequest,
    ) -> elasticsearch_20170613_models.ModifyDeployMachineResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_deploy_machine_with_options(res_id, request, headers, runtime)

    async def modify_deploy_machine_async(
        self,
        res_id: str,
        request: elasticsearch_20170613_models.ModifyDeployMachineRequest,
    ) -> elasticsearch_20170613_models.ModifyDeployMachineResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_deploy_machine_with_options_async(res_id, request, headers, runtime)

    def modify_deploy_machine_with_options(
        self,
        res_id: str,
        request: elasticsearch_20170613_models.ModifyDeployMachineRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ModifyDeployMachineResponse:
        UtilClient.validate_model(request)
        res_id = OpenApiUtilClient.get_encode_param(res_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ModifyDeployMachineResponse(),
            self.do_roarequest('ModifyDeployMachine', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/collectors/{res_id}/actions/modify-deploy-machines', 'json', req, runtime)
        )

    async def modify_deploy_machine_with_options_async(
        self,
        res_id: str,
        request: elasticsearch_20170613_models.ModifyDeployMachineRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ModifyDeployMachineResponse:
        UtilClient.validate_model(request)
        res_id = OpenApiUtilClient.get_encode_param(res_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ModifyDeployMachineResponse(),
            await self.do_roarequest_async('ModifyDeployMachine', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/collectors/{res_id}/actions/modify-deploy-machines', 'json', req, runtime)
        )

    def modify_elastictask(
        self,
        instance_id: str,
    ) -> elasticsearch_20170613_models.ModifyElastictaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_elastictask_with_options(instance_id, headers, runtime)

    async def modify_elastictask_async(
        self,
        instance_id: str,
    ) -> elasticsearch_20170613_models.ModifyElastictaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_elastictask_with_options_async(instance_id, headers, runtime)

    def modify_elastictask_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ModifyElastictaskResponse:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ModifyElastictaskResponse(),
            self.do_roarequest('ModifyElastictask', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/elastic-task', 'json', req, runtime)
        )

    async def modify_elastictask_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ModifyElastictaskResponse:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ModifyElastictaskResponse(),
            await self.do_roarequest_async('ModifyElastictask', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/elastic-task', 'json', req, runtime)
        )

    def modify_instance_maintain_time(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ModifyInstanceMaintainTimeRequest,
    ) -> elasticsearch_20170613_models.ModifyInstanceMaintainTimeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_instance_maintain_time_with_options(instance_id, request, headers, runtime)

    async def modify_instance_maintain_time_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ModifyInstanceMaintainTimeRequest,
    ) -> elasticsearch_20170613_models.ModifyInstanceMaintainTimeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_instance_maintain_time_with_options_async(instance_id, request, headers, runtime)

    def modify_instance_maintain_time_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ModifyInstanceMaintainTimeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ModifyInstanceMaintainTimeResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ModifyInstanceMaintainTimeResponse(),
            self.do_roarequest('ModifyInstanceMaintainTime', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/actions/modify-maintaintime', 'json', req, runtime)
        )

    async def modify_instance_maintain_time_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ModifyInstanceMaintainTimeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ModifyInstanceMaintainTimeResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ModifyInstanceMaintainTimeResponse(),
            await self.do_roarequest_async('ModifyInstanceMaintainTime', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/actions/modify-maintaintime', 'json', req, runtime)
        )

    def modify_white_ips(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ModifyWhiteIpsRequest,
    ) -> elasticsearch_20170613_models.ModifyWhiteIpsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_white_ips_with_options(instance_id, request, headers, runtime)

    async def modify_white_ips_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ModifyWhiteIpsRequest,
    ) -> elasticsearch_20170613_models.ModifyWhiteIpsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_white_ips_with_options_async(instance_id, request, headers, runtime)

    def modify_white_ips_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ModifyWhiteIpsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ModifyWhiteIpsResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not UtilClient.is_unset(request.node_type):
            body['nodeType'] = request.node_type
        if not UtilClient.is_unset(request.network_type):
            body['networkType'] = request.network_type
        if not UtilClient.is_unset(request.modify_mode):
            body['modifyMode'] = request.modify_mode
        if not UtilClient.is_unset(request.white_ip_list):
            body['whiteIpList'] = request.white_ip_list
        if not UtilClient.is_unset(request.white_ip_group):
            body['whiteIpGroup'] = request.white_ip_group
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ModifyWhiteIpsResponse(),
            self.do_roarequest_with_form('ModifyWhiteIps', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/actions/modify-white-ips', 'json', req, runtime)
        )

    async def modify_white_ips_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ModifyWhiteIpsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ModifyWhiteIpsResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not UtilClient.is_unset(request.node_type):
            body['nodeType'] = request.node_type
        if not UtilClient.is_unset(request.network_type):
            body['networkType'] = request.network_type
        if not UtilClient.is_unset(request.modify_mode):
            body['modifyMode'] = request.modify_mode
        if not UtilClient.is_unset(request.white_ip_list):
            body['whiteIpList'] = request.white_ip_list
        if not UtilClient.is_unset(request.white_ip_group):
            body['whiteIpGroup'] = request.white_ip_group
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ModifyWhiteIpsResponse(),
            await self.do_roarequest_with_form_async('ModifyWhiteIps', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/actions/modify-white-ips', 'json', req, runtime)
        )

    def move_resource_group(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.MoveResourceGroupRequest,
    ) -> elasticsearch_20170613_models.MoveResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.move_resource_group_with_options(instance_id, request, headers, runtime)

    async def move_resource_group_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.MoveResourceGroupRequest,
    ) -> elasticsearch_20170613_models.MoveResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.move_resource_group_with_options_async(instance_id, request, headers, runtime)

    def move_resource_group_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.MoveResourceGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.MoveResourceGroupResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.MoveResourceGroupResponse(),
            self.do_roarequest('MoveResourceGroup', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/resourcegroup', 'json', req, runtime)
        )

    async def move_resource_group_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.MoveResourceGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.MoveResourceGroupResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.MoveResourceGroupResponse(),
            await self.do_roarequest_async('MoveResourceGroup', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/resourcegroup', 'json', req, runtime)
        )

    def open_diagnosis(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.OpenDiagnosisRequest,
    ) -> elasticsearch_20170613_models.OpenDiagnosisResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.open_diagnosis_with_options(instance_id, request, headers, runtime)

    async def open_diagnosis_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.OpenDiagnosisRequest,
    ) -> elasticsearch_20170613_models.OpenDiagnosisResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.open_diagnosis_with_options_async(instance_id, request, headers, runtime)

    def open_diagnosis_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.OpenDiagnosisRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.OpenDiagnosisResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.lang):
            query['lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.OpenDiagnosisResponse(),
            self.do_roarequest('OpenDiagnosis', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/diagnosis/instances/{instance_id}/actions/open-diagnosis', 'json', req, runtime)
        )

    async def open_diagnosis_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.OpenDiagnosisRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.OpenDiagnosisResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.lang):
            query['lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.OpenDiagnosisResponse(),
            await self.do_roarequest_async('OpenDiagnosis', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/diagnosis/instances/{instance_id}/actions/open-diagnosis', 'json', req, runtime)
        )

    def open_https(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.OpenHttpsRequest,
    ) -> elasticsearch_20170613_models.OpenHttpsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.open_https_with_options(instance_id, request, headers, runtime)

    async def open_https_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.OpenHttpsRequest,
    ) -> elasticsearch_20170613_models.OpenHttpsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.open_https_with_options_async(instance_id, request, headers, runtime)

    def open_https_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.OpenHttpsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.OpenHttpsResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.OpenHttpsResponse(),
            self.do_roarequest('OpenHttps', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/actions/open-https', 'json', req, runtime)
        )

    async def open_https_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.OpenHttpsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.OpenHttpsResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.OpenHttpsResponse(),
            await self.do_roarequest_async('OpenHttps', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/actions/open-https', 'json', req, runtime)
        )

    def post_emon_try_alarm_rule(
        self,
        project_id: str,
        alarm_group_id: str,
    ) -> elasticsearch_20170613_models.PostEmonTryAlarmRuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.post_emon_try_alarm_rule_with_options(project_id, alarm_group_id, headers, runtime)

    async def post_emon_try_alarm_rule_async(
        self,
        project_id: str,
        alarm_group_id: str,
    ) -> elasticsearch_20170613_models.PostEmonTryAlarmRuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.post_emon_try_alarm_rule_with_options_async(project_id, alarm_group_id, headers, runtime)

    def post_emon_try_alarm_rule_with_options(
        self,
        project_id: str,
        alarm_group_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.PostEmonTryAlarmRuleResponse:
        project_id = OpenApiUtilClient.get_encode_param(project_id)
        alarm_group_id = OpenApiUtilClient.get_encode_param(alarm_group_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.PostEmonTryAlarmRuleResponse(),
            self.do_roarequest('PostEmonTryAlarmRule', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/emon/projects/{project_id}/alarm-groups/{alarm_group_id}/alarm-rules/_test', 'json', req, runtime)
        )

    async def post_emon_try_alarm_rule_with_options_async(
        self,
        project_id: str,
        alarm_group_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.PostEmonTryAlarmRuleResponse:
        project_id = OpenApiUtilClient.get_encode_param(project_id)
        alarm_group_id = OpenApiUtilClient.get_encode_param(alarm_group_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.PostEmonTryAlarmRuleResponse(),
            await self.do_roarequest_async('PostEmonTryAlarmRule', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/emon/projects/{project_id}/alarm-groups/{alarm_group_id}/alarm-rules/_test', 'json', req, runtime)
        )

    def recommend_templates(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.RecommendTemplatesRequest,
    ) -> elasticsearch_20170613_models.RecommendTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.recommend_templates_with_options(instance_id, request, headers, runtime)

    async def recommend_templates_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.RecommendTemplatesRequest,
    ) -> elasticsearch_20170613_models.RecommendTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.recommend_templates_with_options_async(instance_id, request, headers, runtime)

    def recommend_templates_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.RecommendTemplatesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.RecommendTemplatesResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.usage_scenario):
            query['usageScenario'] = request.usage_scenario
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.RecommendTemplatesResponse(),
            self.do_roarequest('RecommendTemplates', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/recommended-templates', 'json', req, runtime)
        )

    async def recommend_templates_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.RecommendTemplatesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.RecommendTemplatesResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.usage_scenario):
            query['usageScenario'] = request.usage_scenario
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.RecommendTemplatesResponse(),
            await self.do_roarequest_async('RecommendTemplates', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/recommended-templates', 'json', req, runtime)
        )

    def reinstall_collector(
        self,
        res_id: str,
        request: elasticsearch_20170613_models.ReinstallCollectorRequest,
    ) -> elasticsearch_20170613_models.ReinstallCollectorResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.reinstall_collector_with_options(res_id, request, headers, runtime)

    async def reinstall_collector_async(
        self,
        res_id: str,
        request: elasticsearch_20170613_models.ReinstallCollectorRequest,
    ) -> elasticsearch_20170613_models.ReinstallCollectorResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.reinstall_collector_with_options_async(res_id, request, headers, runtime)

    def reinstall_collector_with_options(
        self,
        res_id: str,
        request: elasticsearch_20170613_models.ReinstallCollectorRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ReinstallCollectorResponse:
        UtilClient.validate_model(request)
        res_id = OpenApiUtilClient.get_encode_param(res_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ReinstallCollectorResponse(),
            self.do_roarequest('ReinstallCollector', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/collectors/{res_id}/actions/reinstall', 'json', req, runtime)
        )

    async def reinstall_collector_with_options_async(
        self,
        res_id: str,
        request: elasticsearch_20170613_models.ReinstallCollectorRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ReinstallCollectorResponse:
        UtilClient.validate_model(request)
        res_id = OpenApiUtilClient.get_encode_param(res_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ReinstallCollectorResponse(),
            await self.do_roarequest_async('ReinstallCollector', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/collectors/{res_id}/actions/reinstall', 'json', req, runtime)
        )

    def renew_instance(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.RenewInstanceRequest,
    ) -> elasticsearch_20170613_models.RenewInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.renew_instance_with_options(instance_id, request, headers, runtime)

    async def renew_instance_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.RenewInstanceRequest,
    ) -> elasticsearch_20170613_models.RenewInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.renew_instance_with_options_async(instance_id, request, headers, runtime)

    def renew_instance_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.RenewInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.RenewInstanceResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.RenewInstanceResponse(),
            self.do_roarequest('RenewInstance', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/actions/renew', 'json', req, runtime)
        )

    async def renew_instance_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.RenewInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.RenewInstanceResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.RenewInstanceResponse(),
            await self.do_roarequest_async('RenewInstance', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/actions/renew', 'json', req, runtime)
        )

    def renew_logstash(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.RenewLogstashRequest,
    ) -> elasticsearch_20170613_models.RenewLogstashResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.renew_logstash_with_options(instance_id, request, headers, runtime)

    async def renew_logstash_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.RenewLogstashRequest,
    ) -> elasticsearch_20170613_models.RenewLogstashResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.renew_logstash_with_options_async(instance_id, request, headers, runtime)

    def renew_logstash_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.RenewLogstashRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.RenewLogstashResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.RenewLogstashResponse(),
            self.do_roarequest('RenewLogstash', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/logstashes/{instance_id}/actions/renew', 'json', req, runtime)
        )

    async def renew_logstash_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.RenewLogstashRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.RenewLogstashResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.RenewLogstashResponse(),
            await self.do_roarequest_async('RenewLogstash', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/logstashes/{instance_id}/actions/renew', 'json', req, runtime)
        )

    def restart_collector(
        self,
        res_id: str,
        request: elasticsearch_20170613_models.RestartCollectorRequest,
    ) -> elasticsearch_20170613_models.RestartCollectorResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.restart_collector_with_options(res_id, request, headers, runtime)

    async def restart_collector_async(
        self,
        res_id: str,
        request: elasticsearch_20170613_models.RestartCollectorRequest,
    ) -> elasticsearch_20170613_models.RestartCollectorResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.restart_collector_with_options_async(res_id, request, headers, runtime)

    def restart_collector_with_options(
        self,
        res_id: str,
        request: elasticsearch_20170613_models.RestartCollectorRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.RestartCollectorResponse:
        UtilClient.validate_model(request)
        res_id = OpenApiUtilClient.get_encode_param(res_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.RestartCollectorResponse(),
            self.do_roarequest('RestartCollector', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/collectors/{res_id}/actions/restart', 'json', req, runtime)
        )

    async def restart_collector_with_options_async(
        self,
        res_id: str,
        request: elasticsearch_20170613_models.RestartCollectorRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.RestartCollectorResponse:
        UtilClient.validate_model(request)
        res_id = OpenApiUtilClient.get_encode_param(res_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.RestartCollectorResponse(),
            await self.do_roarequest_async('RestartCollector', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/collectors/{res_id}/actions/restart', 'json', req, runtime)
        )

    def restart_instance(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.RestartInstanceRequest,
    ) -> elasticsearch_20170613_models.RestartInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.restart_instance_with_options(instance_id, request, headers, runtime)

    async def restart_instance_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.RestartInstanceRequest,
    ) -> elasticsearch_20170613_models.RestartInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.restart_instance_with_options_async(instance_id, request, headers, runtime)

    def restart_instance_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.RestartInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.RestartInstanceResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['force'] = request.force
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.RestartInstanceResponse(),
            self.do_roarequest('RestartInstance', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/actions/restart', 'json', req, runtime)
        )

    async def restart_instance_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.RestartInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.RestartInstanceResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['force'] = request.force
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.RestartInstanceResponse(),
            await self.do_roarequest_async('RestartInstance', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/actions/restart', 'json', req, runtime)
        )

    def restart_logstash(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.RestartLogstashRequest,
    ) -> elasticsearch_20170613_models.RestartLogstashResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.restart_logstash_with_options(instance_id, request, headers, runtime)

    async def restart_logstash_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.RestartLogstashRequest,
    ) -> elasticsearch_20170613_models.RestartLogstashResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.restart_logstash_with_options_async(instance_id, request, headers, runtime)

    def restart_logstash_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.RestartLogstashRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.RestartLogstashResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['force'] = request.force
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.RestartLogstashResponse(),
            self.do_roarequest('RestartLogstash', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/logstashes/{instance_id}/actions/restart', 'json', req, runtime)
        )

    async def restart_logstash_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.RestartLogstashRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.RestartLogstashResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['force'] = request.force
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.RestartLogstashResponse(),
            await self.do_roarequest_async('RestartLogstash', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/logstashes/{instance_id}/actions/restart', 'json', req, runtime)
        )

    def resume_elasticsearch_task(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ResumeElasticsearchTaskRequest,
    ) -> elasticsearch_20170613_models.ResumeElasticsearchTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.resume_elasticsearch_task_with_options(instance_id, request, headers, runtime)

    async def resume_elasticsearch_task_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ResumeElasticsearchTaskRequest,
    ) -> elasticsearch_20170613_models.ResumeElasticsearchTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.resume_elasticsearch_task_with_options_async(instance_id, request, headers, runtime)

    def resume_elasticsearch_task_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ResumeElasticsearchTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ResumeElasticsearchTaskResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ResumeElasticsearchTaskResponse(),
            self.do_roarequest('ResumeElasticsearchTask', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/actions/resume', 'json', req, runtime)
        )

    async def resume_elasticsearch_task_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ResumeElasticsearchTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ResumeElasticsearchTaskResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ResumeElasticsearchTaskResponse(),
            await self.do_roarequest_async('ResumeElasticsearchTask', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/actions/resume', 'json', req, runtime)
        )

    def resume_logstash_task(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ResumeLogstashTaskRequest,
    ) -> elasticsearch_20170613_models.ResumeLogstashTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.resume_logstash_task_with_options(instance_id, request, headers, runtime)

    async def resume_logstash_task_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ResumeLogstashTaskRequest,
    ) -> elasticsearch_20170613_models.ResumeLogstashTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.resume_logstash_task_with_options_async(instance_id, request, headers, runtime)

    def resume_logstash_task_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ResumeLogstashTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ResumeLogstashTaskResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ResumeLogstashTaskResponse(),
            self.do_roarequest('ResumeLogstashTask', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/logstashes/{instance_id}/actions/resume', 'json', req, runtime)
        )

    async def resume_logstash_task_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ResumeLogstashTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ResumeLogstashTaskResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ResumeLogstashTaskResponse(),
            await self.do_roarequest_async('ResumeLogstashTask', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/logstashes/{instance_id}/actions/resume', 'json', req, runtime)
        )

    def rollover_data_stream(
        self,
        instance_id: str,
        data_stream: str,
        request: elasticsearch_20170613_models.RolloverDataStreamRequest,
    ) -> elasticsearch_20170613_models.RolloverDataStreamResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.rollover_data_stream_with_options(instance_id, data_stream, request, headers, runtime)

    async def rollover_data_stream_async(
        self,
        instance_id: str,
        data_stream: str,
        request: elasticsearch_20170613_models.RolloverDataStreamRequest,
    ) -> elasticsearch_20170613_models.RolloverDataStreamResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.rollover_data_stream_with_options_async(instance_id, data_stream, request, headers, runtime)

    def rollover_data_stream_with_options(
        self,
        instance_id: str,
        data_stream: str,
        request: elasticsearch_20170613_models.RolloverDataStreamRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.RolloverDataStreamResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        data_stream = OpenApiUtilClient.get_encode_param(data_stream)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.RolloverDataStreamResponse(),
            self.do_roarequest('RolloverDataStream', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/data-streams/{data_stream}/rollover', 'json', req, runtime)
        )

    async def rollover_data_stream_with_options_async(
        self,
        instance_id: str,
        data_stream: str,
        request: elasticsearch_20170613_models.RolloverDataStreamRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.RolloverDataStreamResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        data_stream = OpenApiUtilClient.get_encode_param(data_stream)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.RolloverDataStreamResponse(),
            await self.do_roarequest_async('RolloverDataStream', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/data-streams/{data_stream}/rollover', 'json', req, runtime)
        )

    def run_pipelines(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.RunPipelinesRequest,
    ) -> elasticsearch_20170613_models.RunPipelinesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.run_pipelines_with_options(instance_id, request, headers, runtime)

    async def run_pipelines_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.RunPipelinesRequest,
    ) -> elasticsearch_20170613_models.RunPipelinesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.run_pipelines_with_options_async(instance_id, request, headers, runtime)

    def run_pipelines_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.RunPipelinesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.RunPipelinesResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.RunPipelinesResponse(),
            self.do_roarequest('RunPipelines', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/logstashes/{instance_id}/pipelines/action/run', 'json', req, runtime)
        )

    async def run_pipelines_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.RunPipelinesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.RunPipelinesResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.RunPipelinesResponse(),
            await self.do_roarequest_async('RunPipelines', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/logstashes/{instance_id}/pipelines/action/run', 'json', req, runtime)
        )

    def shrink_node(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ShrinkNodeRequest,
    ) -> elasticsearch_20170613_models.ShrinkNodeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.shrink_node_with_options(instance_id, request, headers, runtime)

    async def shrink_node_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ShrinkNodeRequest,
    ) -> elasticsearch_20170613_models.ShrinkNodeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.shrink_node_with_options_async(instance_id, request, headers, runtime)

    def shrink_node_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ShrinkNodeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ShrinkNodeResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.node_type):
            query['nodeType'] = request.node_type
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.ignore_status):
            query['ignoreStatus'] = request.ignore_status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ShrinkNodeResponse(),
            self.do_roarequest('ShrinkNode', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/actions/shrink', 'json', req, runtime)
        )

    async def shrink_node_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ShrinkNodeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ShrinkNodeResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.node_type):
            query['nodeType'] = request.node_type
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.ignore_status):
            query['ignoreStatus'] = request.ignore_status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ShrinkNodeResponse(),
            await self.do_roarequest_async('ShrinkNode', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/actions/shrink', 'json', req, runtime)
        )

    def start_collector(
        self,
        res_id: str,
        request: elasticsearch_20170613_models.StartCollectorRequest,
    ) -> elasticsearch_20170613_models.StartCollectorResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_collector_with_options(res_id, request, headers, runtime)

    async def start_collector_async(
        self,
        res_id: str,
        request: elasticsearch_20170613_models.StartCollectorRequest,
    ) -> elasticsearch_20170613_models.StartCollectorResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.start_collector_with_options_async(res_id, request, headers, runtime)

    def start_collector_with_options(
        self,
        res_id: str,
        request: elasticsearch_20170613_models.StartCollectorRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.StartCollectorResponse:
        UtilClient.validate_model(request)
        res_id = OpenApiUtilClient.get_encode_param(res_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.StartCollectorResponse(),
            self.do_roarequest('StartCollector', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/collectors/{res_id}/actions/start', 'json', req, runtime)
        )

    async def start_collector_with_options_async(
        self,
        res_id: str,
        request: elasticsearch_20170613_models.StartCollectorRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.StartCollectorResponse:
        UtilClient.validate_model(request)
        res_id = OpenApiUtilClient.get_encode_param(res_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.StartCollectorResponse(),
            await self.do_roarequest_async('StartCollector', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/collectors/{res_id}/actions/start', 'json', req, runtime)
        )

    def stop_collector(
        self,
        res_id: str,
        request: elasticsearch_20170613_models.StopCollectorRequest,
    ) -> elasticsearch_20170613_models.StopCollectorResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_collector_with_options(res_id, request, headers, runtime)

    async def stop_collector_async(
        self,
        res_id: str,
        request: elasticsearch_20170613_models.StopCollectorRequest,
    ) -> elasticsearch_20170613_models.StopCollectorResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.stop_collector_with_options_async(res_id, request, headers, runtime)

    def stop_collector_with_options(
        self,
        res_id: str,
        request: elasticsearch_20170613_models.StopCollectorRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.StopCollectorResponse:
        UtilClient.validate_model(request)
        res_id = OpenApiUtilClient.get_encode_param(res_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.StopCollectorResponse(),
            self.do_roarequest('StopCollector', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/collectors/{res_id}/actions/stop', 'json', req, runtime)
        )

    async def stop_collector_with_options_async(
        self,
        res_id: str,
        request: elasticsearch_20170613_models.StopCollectorRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.StopCollectorResponse:
        UtilClient.validate_model(request)
        res_id = OpenApiUtilClient.get_encode_param(res_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.StopCollectorResponse(),
            await self.do_roarequest_async('StopCollector', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/collectors/{res_id}/actions/stop', 'json', req, runtime)
        )

    def stop_pipelines(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.StopPipelinesRequest,
    ) -> elasticsearch_20170613_models.StopPipelinesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_pipelines_with_options(instance_id, request, headers, runtime)

    async def stop_pipelines_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.StopPipelinesRequest,
    ) -> elasticsearch_20170613_models.StopPipelinesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.stop_pipelines_with_options_async(instance_id, request, headers, runtime)

    def stop_pipelines_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.StopPipelinesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.StopPipelinesResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.StopPipelinesResponse(),
            self.do_roarequest('StopPipelines', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/logstashes/{instance_id}/pipelines/action/stop', 'json', req, runtime)
        )

    async def stop_pipelines_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.StopPipelinesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.StopPipelinesResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.StopPipelinesResponse(),
            await self.do_roarequest_async('StopPipelines', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/logstashes/{instance_id}/pipelines/action/stop', 'json', req, runtime)
        )

    def tag_resources(self) -> elasticsearch_20170613_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.tag_resources_with_options(headers, runtime)

    async def tag_resources_async(self) -> elasticsearch_20170613_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.tag_resources_with_options_async(headers, runtime)

    def tag_resources_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.TagResourcesResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.TagResourcesResponse(),
            self.do_roarequest('TagResources', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/tags', 'json', req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.TagResourcesResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.TagResourcesResponse(),
            await self.do_roarequest_async('TagResources', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/tags', 'json', req, runtime)
        )

    def transfer_node(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.TransferNodeRequest,
    ) -> elasticsearch_20170613_models.TransferNodeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.transfer_node_with_options(instance_id, request, headers, runtime)

    async def transfer_node_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.TransferNodeRequest,
    ) -> elasticsearch_20170613_models.TransferNodeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.transfer_node_with_options_async(instance_id, request, headers, runtime)

    def transfer_node_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.TransferNodeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.TransferNodeResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.node_type):
            query['nodeType'] = request.node_type
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.TransferNodeResponse(),
            self.do_roarequest('TransferNode', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/actions/transfer', 'json', req, runtime)
        )

    async def transfer_node_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.TransferNodeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.TransferNodeResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.node_type):
            query['nodeType'] = request.node_type
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.TransferNodeResponse(),
            await self.do_roarequest_async('TransferNode', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/actions/transfer', 'json', req, runtime)
        )

    def trigger_network(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.TriggerNetworkRequest,
    ) -> elasticsearch_20170613_models.TriggerNetworkResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.trigger_network_with_options(instance_id, request, headers, runtime)

    async def trigger_network_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.TriggerNetworkRequest,
    ) -> elasticsearch_20170613_models.TriggerNetworkResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.trigger_network_with_options_async(instance_id, request, headers, runtime)

    def trigger_network_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.TriggerNetworkRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.TriggerNetworkResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not UtilClient.is_unset(request.node_type):
            body['nodeType'] = request.node_type
        if not UtilClient.is_unset(request.network_type):
            body['networkType'] = request.network_type
        if not UtilClient.is_unset(request.action_type):
            body['actionType'] = request.action_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.TriggerNetworkResponse(),
            self.do_roarequest_with_form('TriggerNetwork', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/actions/network-trigger', 'json', req, runtime)
        )

    async def trigger_network_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.TriggerNetworkRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.TriggerNetworkResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not UtilClient.is_unset(request.node_type):
            body['nodeType'] = request.node_type
        if not UtilClient.is_unset(request.network_type):
            body['networkType'] = request.network_type
        if not UtilClient.is_unset(request.action_type):
            body['actionType'] = request.action_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.TriggerNetworkResponse(),
            await self.do_roarequest_with_form_async('TriggerNetwork', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/actions/network-trigger', 'json', req, runtime)
        )

    def uninstall_kibana_plugin(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UninstallKibanaPluginRequest,
    ) -> elasticsearch_20170613_models.UninstallKibanaPluginResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.uninstall_kibana_plugin_with_options(instance_id, request, headers, runtime)

    async def uninstall_kibana_plugin_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UninstallKibanaPluginRequest,
    ) -> elasticsearch_20170613_models.UninstallKibanaPluginResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.uninstall_kibana_plugin_with_options_async(instance_id, request, headers, runtime)

    def uninstall_kibana_plugin_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UninstallKibanaPluginRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UninstallKibanaPluginResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UninstallKibanaPluginResponse(),
            self.do_roarequest('UninstallKibanaPlugin', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/kibana-plugins/actions/uninstall', 'json', req, runtime)
        )

    async def uninstall_kibana_plugin_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UninstallKibanaPluginRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UninstallKibanaPluginResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UninstallKibanaPluginResponse(),
            await self.do_roarequest_async('UninstallKibanaPlugin', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/kibana-plugins/actions/uninstall', 'json', req, runtime)
        )

    def uninstall_logstash_plugin(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UninstallLogstashPluginRequest,
    ) -> elasticsearch_20170613_models.UninstallLogstashPluginResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.uninstall_logstash_plugin_with_options(instance_id, request, headers, runtime)

    async def uninstall_logstash_plugin_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UninstallLogstashPluginRequest,
    ) -> elasticsearch_20170613_models.UninstallLogstashPluginResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.uninstall_logstash_plugin_with_options_async(instance_id, request, headers, runtime)

    def uninstall_logstash_plugin_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UninstallLogstashPluginRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UninstallLogstashPluginResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UninstallLogstashPluginResponse(),
            self.do_roarequest('UninstallLogstashPlugin', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/logstashes/{instance_id}/plugins/actions/uninstall', 'json', req, runtime)
        )

    async def uninstall_logstash_plugin_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UninstallLogstashPluginRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UninstallLogstashPluginResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UninstallLogstashPluginResponse(),
            await self.do_roarequest_async('UninstallLogstashPlugin', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/logstashes/{instance_id}/plugins/actions/uninstall', 'json', req, runtime)
        )

    def uninstall_plugin(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UninstallPluginRequest,
    ) -> elasticsearch_20170613_models.UninstallPluginResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.uninstall_plugin_with_options(instance_id, request, headers, runtime)

    async def uninstall_plugin_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UninstallPluginRequest,
    ) -> elasticsearch_20170613_models.UninstallPluginResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.uninstall_plugin_with_options_async(instance_id, request, headers, runtime)

    def uninstall_plugin_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UninstallPluginRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UninstallPluginResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UninstallPluginResponse(),
            self.do_roarequest('UninstallPlugin', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/plugins/actions/uninstall', 'json', req, runtime)
        )

    async def uninstall_plugin_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UninstallPluginRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UninstallPluginResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UninstallPluginResponse(),
            await self.do_roarequest_async('UninstallPlugin', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/plugins/actions/uninstall', 'json', req, runtime)
        )

    def untag_resources(
        self,
        request: elasticsearch_20170613_models.UntagResourcesRequest,
    ) -> elasticsearch_20170613_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.untag_resources_with_options(request, headers, runtime)

    async def untag_resources_async(
        self,
        request: elasticsearch_20170613_models.UntagResourcesRequest,
    ) -> elasticsearch_20170613_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.untag_resources_with_options_async(request, headers, runtime)

    def untag_resources_with_options(
        self,
        request: elasticsearch_20170613_models.UntagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_keys):
            query['TagKeys'] = request.tag_keys
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UntagResourcesResponse(),
            self.do_roarequest('UntagResources', '2017-06-13', 'HTTPS', 'DELETE', 'AK', f'/openapi/tags', 'json', req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: elasticsearch_20170613_models.UntagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_keys):
            query['TagKeys'] = request.tag_keys
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UntagResourcesResponse(),
            await self.do_roarequest_async('UntagResources', '2017-06-13', 'HTTPS', 'DELETE', 'AK', f'/openapi/tags', 'json', req, runtime)
        )

    def update_admin_password(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateAdminPasswordRequest,
    ) -> elasticsearch_20170613_models.UpdateAdminPasswordResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_admin_password_with_options(instance_id, request, headers, runtime)

    async def update_admin_password_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateAdminPasswordRequest,
    ) -> elasticsearch_20170613_models.UpdateAdminPasswordResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_admin_password_with_options_async(instance_id, request, headers, runtime)

    def update_admin_password_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateAdminPasswordRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UpdateAdminPasswordResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateAdminPasswordResponse(),
            self.do_roarequest('UpdateAdminPassword', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/admin-pwd', 'json', req, runtime)
        )

    async def update_admin_password_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateAdminPasswordRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UpdateAdminPasswordResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateAdminPasswordResponse(),
            await self.do_roarequest_async('UpdateAdminPassword', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/admin-pwd', 'json', req, runtime)
        )

    def update_advanced_setting(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateAdvancedSettingRequest,
    ) -> elasticsearch_20170613_models.UpdateAdvancedSettingResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_advanced_setting_with_options(instance_id, request, headers, runtime)

    async def update_advanced_setting_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateAdvancedSettingRequest,
    ) -> elasticsearch_20170613_models.UpdateAdvancedSettingResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_advanced_setting_with_options_async(instance_id, request, headers, runtime)

    def update_advanced_setting_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateAdvancedSettingRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UpdateAdvancedSettingResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateAdvancedSettingResponse(),
            self.do_roarequest('UpdateAdvancedSetting', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/actions/update-advanced-setting', 'json', req, runtime)
        )

    async def update_advanced_setting_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateAdvancedSettingRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UpdateAdvancedSettingResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateAdvancedSettingResponse(),
            await self.do_roarequest_async('UpdateAdvancedSetting', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/actions/update-advanced-setting', 'json', req, runtime)
        )

    def update_aliws_dict(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateAliwsDictRequest,
    ) -> elasticsearch_20170613_models.UpdateAliwsDictResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_aliws_dict_with_options(instance_id, request, headers, runtime)

    async def update_aliws_dict_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateAliwsDictRequest,
    ) -> elasticsearch_20170613_models.UpdateAliwsDictResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_aliws_dict_with_options_async(instance_id, request, headers, runtime)

    def update_aliws_dict_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateAliwsDictRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UpdateAliwsDictResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateAliwsDictResponse(),
            self.do_roarequest('UpdateAliwsDict', '2017-06-13', 'HTTPS', 'PUT', 'AK', f'/openapi/instances/{instance_id}/aliws-dict', 'json', req, runtime)
        )

    async def update_aliws_dict_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateAliwsDictRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UpdateAliwsDictResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateAliwsDictResponse(),
            await self.do_roarequest_async('UpdateAliwsDict', '2017-06-13', 'HTTPS', 'PUT', 'AK', f'/openapi/instances/{instance_id}/aliws-dict', 'json', req, runtime)
        )

    def update_black_ips(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateBlackIpsRequest,
    ) -> elasticsearch_20170613_models.UpdateBlackIpsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_black_ips_with_options(instance_id, request, headers, runtime)

    async def update_black_ips_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateBlackIpsRequest,
    ) -> elasticsearch_20170613_models.UpdateBlackIpsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_black_ips_with_options_async(instance_id, request, headers, runtime)

    def update_black_ips_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateBlackIpsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UpdateBlackIpsResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not UtilClient.is_unset(request.es_ipblacklist):
            body['esIPBlacklist'] = request.es_ipblacklist
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateBlackIpsResponse(),
            self.do_roarequest_with_form('UpdateBlackIps', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/black-ips', 'json', req, runtime)
        )

    async def update_black_ips_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateBlackIpsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UpdateBlackIpsResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not UtilClient.is_unset(request.es_ipblacklist):
            body['esIPBlacklist'] = request.es_ipblacklist
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateBlackIpsResponse(),
            await self.do_roarequest_with_form_async('UpdateBlackIps', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/black-ips', 'json', req, runtime)
        )

    def update_collector(
        self,
        res_id: str,
        request: elasticsearch_20170613_models.UpdateCollectorRequest,
    ) -> elasticsearch_20170613_models.UpdateCollectorResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_collector_with_options(res_id, request, headers, runtime)

    async def update_collector_async(
        self,
        res_id: str,
        request: elasticsearch_20170613_models.UpdateCollectorRequest,
    ) -> elasticsearch_20170613_models.UpdateCollectorResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_collector_with_options_async(res_id, request, headers, runtime)

    def update_collector_with_options(
        self,
        res_id: str,
        request: elasticsearch_20170613_models.UpdateCollectorRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UpdateCollectorResponse:
        UtilClient.validate_model(request)
        res_id = OpenApiUtilClient.get_encode_param(res_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateCollectorResponse(),
            self.do_roarequest('UpdateCollector', '2017-06-13', 'HTTPS', 'PUT', 'AK', f'/openapi/collectors/{res_id}', 'json', req, runtime)
        )

    async def update_collector_with_options_async(
        self,
        res_id: str,
        request: elasticsearch_20170613_models.UpdateCollectorRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UpdateCollectorResponse:
        UtilClient.validate_model(request)
        res_id = OpenApiUtilClient.get_encode_param(res_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateCollectorResponse(),
            await self.do_roarequest_async('UpdateCollector', '2017-06-13', 'HTTPS', 'PUT', 'AK', f'/openapi/collectors/{res_id}', 'json', req, runtime)
        )

    def update_collector_name(
        self,
        res_id: str,
        request: elasticsearch_20170613_models.UpdateCollectorNameRequest,
    ) -> elasticsearch_20170613_models.UpdateCollectorNameResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_collector_name_with_options(res_id, request, headers, runtime)

    async def update_collector_name_async(
        self,
        res_id: str,
        request: elasticsearch_20170613_models.UpdateCollectorNameRequest,
    ) -> elasticsearch_20170613_models.UpdateCollectorNameResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_collector_name_with_options_async(res_id, request, headers, runtime)

    def update_collector_name_with_options(
        self,
        res_id: str,
        request: elasticsearch_20170613_models.UpdateCollectorNameRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UpdateCollectorNameResponse:
        UtilClient.validate_model(request)
        res_id = OpenApiUtilClient.get_encode_param(res_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateCollectorNameResponse(),
            self.do_roarequest('UpdateCollectorName', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/collectors/{res_id}/actions/rename', 'json', req, runtime)
        )

    async def update_collector_name_with_options_async(
        self,
        res_id: str,
        request: elasticsearch_20170613_models.UpdateCollectorNameRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UpdateCollectorNameResponse:
        UtilClient.validate_model(request)
        res_id = OpenApiUtilClient.get_encode_param(res_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateCollectorNameResponse(),
            await self.do_roarequest_async('UpdateCollectorName', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/collectors/{res_id}/actions/rename', 'json', req, runtime)
        )

    def update_description(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateDescriptionRequest,
    ) -> elasticsearch_20170613_models.UpdateDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_description_with_options(instance_id, request, headers, runtime)

    async def update_description_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateDescriptionRequest,
    ) -> elasticsearch_20170613_models.UpdateDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_description_with_options_async(instance_id, request, headers, runtime)

    def update_description_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateDescriptionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UpdateDescriptionResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateDescriptionResponse(),
            self.do_roarequest('UpdateDescription', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/description', 'json', req, runtime)
        )

    async def update_description_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateDescriptionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UpdateDescriptionResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateDescriptionResponse(),
            await self.do_roarequest_async('UpdateDescription', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/description', 'json', req, runtime)
        )

    def update_diagnosis_settings(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateDiagnosisSettingsRequest,
    ) -> elasticsearch_20170613_models.UpdateDiagnosisSettingsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_diagnosis_settings_with_options(instance_id, request, headers, runtime)

    async def update_diagnosis_settings_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateDiagnosisSettingsRequest,
    ) -> elasticsearch_20170613_models.UpdateDiagnosisSettingsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_diagnosis_settings_with_options_async(instance_id, request, headers, runtime)

    def update_diagnosis_settings_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateDiagnosisSettingsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UpdateDiagnosisSettingsResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.lang):
            query['lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateDiagnosisSettingsResponse(),
            self.do_roarequest('UpdateDiagnosisSettings', '2017-06-13', 'HTTPS', 'PUT', 'AK', f'/openapi/diagnosis/instances/{instance_id}/settings', 'json', req, runtime)
        )

    async def update_diagnosis_settings_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateDiagnosisSettingsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UpdateDiagnosisSettingsResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.lang):
            query['lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateDiagnosisSettingsResponse(),
            await self.do_roarequest_async('UpdateDiagnosisSettings', '2017-06-13', 'HTTPS', 'PUT', 'AK', f'/openapi/diagnosis/instances/{instance_id}/settings', 'json', req, runtime)
        )

    def update_dict(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateDictRequest,
    ) -> elasticsearch_20170613_models.UpdateDictResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_dict_with_options(instance_id, request, headers, runtime)

    async def update_dict_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateDictRequest,
    ) -> elasticsearch_20170613_models.UpdateDictResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_dict_with_options_async(instance_id, request, headers, runtime)

    def update_dict_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateDictRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UpdateDictResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateDictResponse(),
            self.do_roarequest('UpdateDict', '2017-06-13', 'HTTPS', 'PUT', 'AK', f'/openapi/instances/{instance_id}/dict', 'json', req, runtime)
        )

    async def update_dict_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateDictRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UpdateDictResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateDictResponse(),
            await self.do_roarequest_async('UpdateDict', '2017-06-13', 'HTTPS', 'PUT', 'AK', f'/openapi/instances/{instance_id}/dict', 'json', req, runtime)
        )

    def update_extend_config(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateExtendConfigRequest,
    ) -> elasticsearch_20170613_models.UpdateExtendConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_extend_config_with_options(instance_id, request, headers, runtime)

    async def update_extend_config_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateExtendConfigRequest,
    ) -> elasticsearch_20170613_models.UpdateExtendConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_extend_config_with_options_async(instance_id, request, headers, runtime)

    def update_extend_config_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateExtendConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UpdateExtendConfigResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateExtendConfigResponse(),
            self.do_roarequest('UpdateExtendConfig', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/extend-configs/actions/update', 'json', req, runtime)
        )

    async def update_extend_config_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateExtendConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UpdateExtendConfigResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateExtendConfigResponse(),
            await self.do_roarequest_async('UpdateExtendConfig', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/extend-configs/actions/update', 'json', req, runtime)
        )

    def update_extendfiles(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateExtendfilesRequest,
    ) -> elasticsearch_20170613_models.UpdateExtendfilesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_extendfiles_with_options(instance_id, request, headers, runtime)

    async def update_extendfiles_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateExtendfilesRequest,
    ) -> elasticsearch_20170613_models.UpdateExtendfilesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_extendfiles_with_options_async(instance_id, request, headers, runtime)

    def update_extendfiles_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateExtendfilesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UpdateExtendfilesResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateExtendfilesResponse(),
            self.do_roarequest('UpdateExtendfiles', '2017-06-13', 'HTTPS', 'PUT', 'AK', f'/openapi/logstashes/{instance_id}/extendfiles', 'json', req, runtime)
        )

    async def update_extendfiles_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateExtendfilesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UpdateExtendfilesResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateExtendfilesResponse(),
            await self.do_roarequest_async('UpdateExtendfiles', '2017-06-13', 'HTTPS', 'PUT', 'AK', f'/openapi/logstashes/{instance_id}/extendfiles', 'json', req, runtime)
        )

    def update_hot_ik_dicts(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateHotIkDictsRequest,
    ) -> elasticsearch_20170613_models.UpdateHotIkDictsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_hot_ik_dicts_with_options(instance_id, request, headers, runtime)

    async def update_hot_ik_dicts_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateHotIkDictsRequest,
    ) -> elasticsearch_20170613_models.UpdateHotIkDictsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_hot_ik_dicts_with_options_async(instance_id, request, headers, runtime)

    def update_hot_ik_dicts_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateHotIkDictsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UpdateHotIkDictsResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateHotIkDictsResponse(),
            self.do_roarequest('UpdateHotIkDicts', '2017-06-13', 'HTTPS', 'PUT', 'AK', f'/openapi/instances/{instance_id}/ik-hot-dict', 'json', req, runtime)
        )

    async def update_hot_ik_dicts_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateHotIkDictsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UpdateHotIkDictsResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateHotIkDictsResponse(),
            await self.do_roarequest_async('UpdateHotIkDicts', '2017-06-13', 'HTTPS', 'PUT', 'AK', f'/openapi/instances/{instance_id}/ik-hot-dict', 'json', req, runtime)
        )

    def update_ilmpolicy(
        self,
        instance_id: str,
        policy_name: str,
        request: elasticsearch_20170613_models.UpdateILMPolicyRequest,
    ) -> elasticsearch_20170613_models.UpdateILMPolicyResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_ilmpolicy_with_options(instance_id, policy_name, request, headers, runtime)

    async def update_ilmpolicy_async(
        self,
        instance_id: str,
        policy_name: str,
        request: elasticsearch_20170613_models.UpdateILMPolicyRequest,
    ) -> elasticsearch_20170613_models.UpdateILMPolicyResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_ilmpolicy_with_options_async(instance_id, policy_name, request, headers, runtime)

    def update_ilmpolicy_with_options(
        self,
        instance_id: str,
        policy_name: str,
        request: elasticsearch_20170613_models.UpdateILMPolicyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UpdateILMPolicyResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        policy_name = OpenApiUtilClient.get_encode_param(policy_name)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateILMPolicyResponse(),
            self.do_roarequest('UpdateILMPolicy', '2017-06-13', 'HTTPS', 'PUT', 'AK', f'/openapi/instances/{instance_id}/ilm-policies/{policy_name}', 'json', req, runtime)
        )

    async def update_ilmpolicy_with_options_async(
        self,
        instance_id: str,
        policy_name: str,
        request: elasticsearch_20170613_models.UpdateILMPolicyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UpdateILMPolicyResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        policy_name = OpenApiUtilClient.get_encode_param(policy_name)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateILMPolicyResponse(),
            await self.do_roarequest_async('UpdateILMPolicy', '2017-06-13', 'HTTPS', 'PUT', 'AK', f'/openapi/instances/{instance_id}/ilm-policies/{policy_name}', 'json', req, runtime)
        )

    def update_index_template(
        self,
        instance_id: str,
        index_template: str,
        request: elasticsearch_20170613_models.UpdateIndexTemplateRequest,
    ) -> elasticsearch_20170613_models.UpdateIndexTemplateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_index_template_with_options(instance_id, index_template, request, headers, runtime)

    async def update_index_template_async(
        self,
        instance_id: str,
        index_template: str,
        request: elasticsearch_20170613_models.UpdateIndexTemplateRequest,
    ) -> elasticsearch_20170613_models.UpdateIndexTemplateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_index_template_with_options_async(instance_id, index_template, request, headers, runtime)

    def update_index_template_with_options(
        self,
        instance_id: str,
        index_template: str,
        request: elasticsearch_20170613_models.UpdateIndexTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UpdateIndexTemplateResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        index_template = OpenApiUtilClient.get_encode_param(index_template)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateIndexTemplateResponse(),
            self.do_roarequest('UpdateIndexTemplate', '2017-06-13', 'HTTPS', 'PUT', 'AK', f'/openapi/instances/{instance_id}/index-templates/{index_template}', 'json', req, runtime)
        )

    async def update_index_template_with_options_async(
        self,
        instance_id: str,
        index_template: str,
        request: elasticsearch_20170613_models.UpdateIndexTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UpdateIndexTemplateResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        index_template = OpenApiUtilClient.get_encode_param(index_template)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateIndexTemplateResponse(),
            await self.do_roarequest_async('UpdateIndexTemplate', '2017-06-13', 'HTTPS', 'PUT', 'AK', f'/openapi/instances/{instance_id}/index-templates/{index_template}', 'json', req, runtime)
        )

    def update_instance(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateInstanceRequest,
    ) -> elasticsearch_20170613_models.UpdateInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_instance_with_options(instance_id, request, headers, runtime)

    async def update_instance_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateInstanceRequest,
    ) -> elasticsearch_20170613_models.UpdateInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_instance_with_options_async(instance_id, request, headers, runtime)

    def update_instance_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UpdateInstanceResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.ignore_status):
            query['ignoreStatus'] = request.ignore_status
        if not UtilClient.is_unset(request.order_action_type):
            query['orderActionType'] = request.order_action_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateInstanceResponse(),
            self.do_roarequest('UpdateInstance', '2017-06-13', 'HTTPS', 'PUT', 'AK', f'/openapi/instances/{instance_id}', 'json', req, runtime)
        )

    async def update_instance_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UpdateInstanceResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.ignore_status):
            query['ignoreStatus'] = request.ignore_status
        if not UtilClient.is_unset(request.order_action_type):
            query['orderActionType'] = request.order_action_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateInstanceResponse(),
            await self.do_roarequest_async('UpdateInstance', '2017-06-13', 'HTTPS', 'PUT', 'AK', f'/openapi/instances/{instance_id}', 'json', req, runtime)
        )

    def update_instance_charge_type(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateInstanceChargeTypeRequest,
    ) -> elasticsearch_20170613_models.UpdateInstanceChargeTypeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_instance_charge_type_with_options(instance_id, request, headers, runtime)

    async def update_instance_charge_type_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateInstanceChargeTypeRequest,
    ) -> elasticsearch_20170613_models.UpdateInstanceChargeTypeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_instance_charge_type_with_options_async(instance_id, request, headers, runtime)

    def update_instance_charge_type_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateInstanceChargeTypeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UpdateInstanceChargeTypeResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateInstanceChargeTypeResponse(),
            self.do_roarequest('UpdateInstanceChargeType', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/actions/convert-pay-type', 'json', req, runtime)
        )

    async def update_instance_charge_type_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateInstanceChargeTypeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UpdateInstanceChargeTypeResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateInstanceChargeTypeResponse(),
            await self.do_roarequest_async('UpdateInstanceChargeType', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/actions/convert-pay-type', 'json', req, runtime)
        )

    def update_instance_settings(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateInstanceSettingsRequest,
    ) -> elasticsearch_20170613_models.UpdateInstanceSettingsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_instance_settings_with_options(instance_id, request, headers, runtime)

    async def update_instance_settings_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateInstanceSettingsRequest,
    ) -> elasticsearch_20170613_models.UpdateInstanceSettingsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_instance_settings_with_options_async(instance_id, request, headers, runtime)

    def update_instance_settings_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateInstanceSettingsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UpdateInstanceSettingsResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateInstanceSettingsResponse(),
            self.do_roarequest('UpdateInstanceSettings', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/instance-settings', 'json', req, runtime)
        )

    async def update_instance_settings_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateInstanceSettingsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UpdateInstanceSettingsResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateInstanceSettingsResponse(),
            await self.do_roarequest_async('UpdateInstanceSettings', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/instance-settings', 'json', req, runtime)
        )

    def update_kibana_settings(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateKibanaSettingsRequest,
    ) -> elasticsearch_20170613_models.UpdateKibanaSettingsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_kibana_settings_with_options(instance_id, request, headers, runtime)

    async def update_kibana_settings_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateKibanaSettingsRequest,
    ) -> elasticsearch_20170613_models.UpdateKibanaSettingsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_kibana_settings_with_options_async(instance_id, request, headers, runtime)

    def update_kibana_settings_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateKibanaSettingsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UpdateKibanaSettingsResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateKibanaSettingsResponse(),
            self.do_roarequest('UpdateKibanaSettings', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/actions/update-kibana-settings', 'json', req, runtime)
        )

    async def update_kibana_settings_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateKibanaSettingsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UpdateKibanaSettingsResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateKibanaSettingsResponse(),
            await self.do_roarequest_async('UpdateKibanaSettings', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/actions/update-kibana-settings', 'json', req, runtime)
        )

    def update_kibana_white_ips(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateKibanaWhiteIpsRequest,
    ) -> elasticsearch_20170613_models.UpdateKibanaWhiteIpsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_kibana_white_ips_with_options(instance_id, request, headers, runtime)

    async def update_kibana_white_ips_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateKibanaWhiteIpsRequest,
    ) -> elasticsearch_20170613_models.UpdateKibanaWhiteIpsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_kibana_white_ips_with_options_async(instance_id, request, headers, runtime)

    def update_kibana_white_ips_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateKibanaWhiteIpsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UpdateKibanaWhiteIpsResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.modify_mode):
            query['modifyMode'] = request.modify_mode
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateKibanaWhiteIpsResponse(),
            self.do_roarequest('UpdateKibanaWhiteIps', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/kibana-white-ips', 'json', req, runtime)
        )

    async def update_kibana_white_ips_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateKibanaWhiteIpsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UpdateKibanaWhiteIpsResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.modify_mode):
            query['modifyMode'] = request.modify_mode
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateKibanaWhiteIpsResponse(),
            await self.do_roarequest_async('UpdateKibanaWhiteIps', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/kibana-white-ips', 'json', req, runtime)
        )

    def update_logstash(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateLogstashRequest,
    ) -> elasticsearch_20170613_models.UpdateLogstashResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_logstash_with_options(instance_id, request, headers, runtime)

    async def update_logstash_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateLogstashRequest,
    ) -> elasticsearch_20170613_models.UpdateLogstashResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_logstash_with_options_async(instance_id, request, headers, runtime)

    def update_logstash_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateLogstashRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UpdateLogstashResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateLogstashResponse(),
            self.do_roarequest('UpdateLogstash', '2017-06-13', 'HTTPS', 'PUT', 'AK', f'/openapi/logstashes/{instance_id}', 'json', req, runtime)
        )

    async def update_logstash_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateLogstashRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UpdateLogstashResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateLogstashResponse(),
            await self.do_roarequest_async('UpdateLogstash', '2017-06-13', 'HTTPS', 'PUT', 'AK', f'/openapi/logstashes/{instance_id}', 'json', req, runtime)
        )

    def update_logstash_charge_type(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateLogstashChargeTypeRequest,
    ) -> elasticsearch_20170613_models.UpdateLogstashChargeTypeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_logstash_charge_type_with_options(instance_id, request, headers, runtime)

    async def update_logstash_charge_type_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateLogstashChargeTypeRequest,
    ) -> elasticsearch_20170613_models.UpdateLogstashChargeTypeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_logstash_charge_type_with_options_async(instance_id, request, headers, runtime)

    def update_logstash_charge_type_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateLogstashChargeTypeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UpdateLogstashChargeTypeResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateLogstashChargeTypeResponse(),
            self.do_roarequest('UpdateLogstashChargeType', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/logstashes/{instance_id}/actions/convert-pay-type', 'json', req, runtime)
        )

    async def update_logstash_charge_type_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateLogstashChargeTypeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UpdateLogstashChargeTypeResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateLogstashChargeTypeResponse(),
            await self.do_roarequest_async('UpdateLogstashChargeType', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/logstashes/{instance_id}/actions/convert-pay-type', 'json', req, runtime)
        )

    def update_logstash_description(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateLogstashDescriptionRequest,
    ) -> elasticsearch_20170613_models.UpdateLogstashDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_logstash_description_with_options(instance_id, request, headers, runtime)

    async def update_logstash_description_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateLogstashDescriptionRequest,
    ) -> elasticsearch_20170613_models.UpdateLogstashDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_logstash_description_with_options_async(instance_id, request, headers, runtime)

    def update_logstash_description_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateLogstashDescriptionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UpdateLogstashDescriptionResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateLogstashDescriptionResponse(),
            self.do_roarequest('UpdateLogstashDescription', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/logstashes/{instance_id}/description', 'json', req, runtime)
        )

    async def update_logstash_description_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateLogstashDescriptionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UpdateLogstashDescriptionResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateLogstashDescriptionResponse(),
            await self.do_roarequest_async('UpdateLogstashDescription', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/logstashes/{instance_id}/description', 'json', req, runtime)
        )

    def update_logstash_settings(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateLogstashSettingsRequest,
    ) -> elasticsearch_20170613_models.UpdateLogstashSettingsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_logstash_settings_with_options(instance_id, request, headers, runtime)

    async def update_logstash_settings_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateLogstashSettingsRequest,
    ) -> elasticsearch_20170613_models.UpdateLogstashSettingsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_logstash_settings_with_options_async(instance_id, request, headers, runtime)

    def update_logstash_settings_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateLogstashSettingsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UpdateLogstashSettingsResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateLogstashSettingsResponse(),
            self.do_roarequest('UpdateLogstashSettings', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/logstashes/{instance_id}/instance-settings', 'json', req, runtime)
        )

    async def update_logstash_settings_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateLogstashSettingsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UpdateLogstashSettingsResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateLogstashSettingsResponse(),
            await self.do_roarequest_async('UpdateLogstashSettings', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/logstashes/{instance_id}/instance-settings', 'json', req, runtime)
        )

    def update_pipeline_management_config(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdatePipelineManagementConfigRequest,
    ) -> elasticsearch_20170613_models.UpdatePipelineManagementConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_pipeline_management_config_with_options(instance_id, request, headers, runtime)

    async def update_pipeline_management_config_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdatePipelineManagementConfigRequest,
    ) -> elasticsearch_20170613_models.UpdatePipelineManagementConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_pipeline_management_config_with_options_async(instance_id, request, headers, runtime)

    def update_pipeline_management_config_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdatePipelineManagementConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UpdatePipelineManagementConfigResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdatePipelineManagementConfigResponse(),
            self.do_roarequest('UpdatePipelineManagementConfig', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/logstashes/{instance_id}/pipeline-management-config', 'json', req, runtime)
        )

    async def update_pipeline_management_config_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdatePipelineManagementConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UpdatePipelineManagementConfigResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdatePipelineManagementConfigResponse(),
            await self.do_roarequest_async('UpdatePipelineManagementConfig', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/logstashes/{instance_id}/pipeline-management-config', 'json', req, runtime)
        )

    def update_pipelines(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdatePipelinesRequest,
    ) -> elasticsearch_20170613_models.UpdatePipelinesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_pipelines_with_options(instance_id, request, headers, runtime)

    async def update_pipelines_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdatePipelinesRequest,
    ) -> elasticsearch_20170613_models.UpdatePipelinesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_pipelines_with_options_async(instance_id, request, headers, runtime)

    def update_pipelines_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdatePipelinesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UpdatePipelinesResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.trigger):
            query['trigger'] = request.trigger
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdatePipelinesResponse(),
            self.do_roarequest('UpdatePipelines', '2017-06-13', 'HTTPS', 'PUT', 'AK', f'/openapi/logstashes/{instance_id}/pipelines', 'json', req, runtime)
        )

    async def update_pipelines_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdatePipelinesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UpdatePipelinesResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.trigger):
            query['trigger'] = request.trigger
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdatePipelinesResponse(),
            await self.do_roarequest_async('UpdatePipelines', '2017-06-13', 'HTTPS', 'PUT', 'AK', f'/openapi/logstashes/{instance_id}/pipelines', 'json', req, runtime)
        )

    def update_private_network_white_ips(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdatePrivateNetworkWhiteIpsRequest,
    ) -> elasticsearch_20170613_models.UpdatePrivateNetworkWhiteIpsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_private_network_white_ips_with_options(instance_id, request, headers, runtime)

    async def update_private_network_white_ips_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdatePrivateNetworkWhiteIpsRequest,
    ) -> elasticsearch_20170613_models.UpdatePrivateNetworkWhiteIpsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_private_network_white_ips_with_options_async(instance_id, request, headers, runtime)

    def update_private_network_white_ips_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdatePrivateNetworkWhiteIpsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UpdatePrivateNetworkWhiteIpsResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.modify_mode):
            query['modifyMode'] = request.modify_mode
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdatePrivateNetworkWhiteIpsResponse(),
            self.do_roarequest('UpdatePrivateNetworkWhiteIps', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/private-network-white-ips', 'json', req, runtime)
        )

    async def update_private_network_white_ips_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdatePrivateNetworkWhiteIpsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UpdatePrivateNetworkWhiteIpsResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.modify_mode):
            query['modifyMode'] = request.modify_mode
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdatePrivateNetworkWhiteIpsResponse(),
            await self.do_roarequest_async('UpdatePrivateNetworkWhiteIps', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/private-network-white-ips', 'json', req, runtime)
        )

    def update_public_network(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdatePublicNetworkRequest,
    ) -> elasticsearch_20170613_models.UpdatePublicNetworkResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_public_network_with_options(instance_id, request, headers, runtime)

    async def update_public_network_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdatePublicNetworkRequest,
    ) -> elasticsearch_20170613_models.UpdatePublicNetworkResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_public_network_with_options_async(instance_id, request, headers, runtime)

    def update_public_network_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdatePublicNetworkRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UpdatePublicNetworkResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdatePublicNetworkResponse(),
            self.do_roarequest('UpdatePublicNetwork', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/public-network', 'json', req, runtime)
        )

    async def update_public_network_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdatePublicNetworkRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UpdatePublicNetworkResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdatePublicNetworkResponse(),
            await self.do_roarequest_async('UpdatePublicNetwork', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/public-network', 'json', req, runtime)
        )

    def update_public_white_ips(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdatePublicWhiteIpsRequest,
    ) -> elasticsearch_20170613_models.UpdatePublicWhiteIpsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_public_white_ips_with_options(instance_id, request, headers, runtime)

    async def update_public_white_ips_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdatePublicWhiteIpsRequest,
    ) -> elasticsearch_20170613_models.UpdatePublicWhiteIpsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_public_white_ips_with_options_async(instance_id, request, headers, runtime)

    def update_public_white_ips_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdatePublicWhiteIpsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UpdatePublicWhiteIpsResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.modify_mode):
            query['modifyMode'] = request.modify_mode
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdatePublicWhiteIpsResponse(),
            self.do_roarequest('UpdatePublicWhiteIps', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/public-white-ips', 'json', req, runtime)
        )

    async def update_public_white_ips_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdatePublicWhiteIpsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UpdatePublicWhiteIpsResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.modify_mode):
            query['modifyMode'] = request.modify_mode
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdatePublicWhiteIpsResponse(),
            await self.do_roarequest_async('UpdatePublicWhiteIps', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/public-white-ips', 'json', req, runtime)
        )

    def update_read_write_policy(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateReadWritePolicyRequest,
    ) -> elasticsearch_20170613_models.UpdateReadWritePolicyResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_read_write_policy_with_options(instance_id, request, headers, runtime)

    async def update_read_write_policy_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateReadWritePolicyRequest,
    ) -> elasticsearch_20170613_models.UpdateReadWritePolicyResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_read_write_policy_with_options_async(instance_id, request, headers, runtime)

    def update_read_write_policy_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateReadWritePolicyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UpdateReadWritePolicyResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateReadWritePolicyResponse(),
            self.do_roarequest('UpdateReadWritePolicy', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/actions/update-read-write-policy', 'json', req, runtime)
        )

    async def update_read_write_policy_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateReadWritePolicyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UpdateReadWritePolicyResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateReadWritePolicyResponse(),
            await self.do_roarequest_async('UpdateReadWritePolicy', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/actions/update-read-write-policy', 'json', req, runtime)
        )

    def update_snapshot_setting(
        self,
        instance_id: str,
    ) -> elasticsearch_20170613_models.UpdateSnapshotSettingResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_snapshot_setting_with_options(instance_id, headers, runtime)

    async def update_snapshot_setting_async(
        self,
        instance_id: str,
    ) -> elasticsearch_20170613_models.UpdateSnapshotSettingResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_snapshot_setting_with_options_async(instance_id, headers, runtime)

    def update_snapshot_setting_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UpdateSnapshotSettingResponse:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateSnapshotSettingResponse(),
            self.do_roarequest('UpdateSnapshotSetting', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/snapshot-setting', 'json', req, runtime)
        )

    async def update_snapshot_setting_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UpdateSnapshotSettingResponse:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateSnapshotSettingResponse(),
            await self.do_roarequest_async('UpdateSnapshotSetting', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/snapshot-setting', 'json', req, runtime)
        )

    def update_synonyms_dicts(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateSynonymsDictsRequest,
    ) -> elasticsearch_20170613_models.UpdateSynonymsDictsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_synonyms_dicts_with_options(instance_id, request, headers, runtime)

    async def update_synonyms_dicts_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateSynonymsDictsRequest,
    ) -> elasticsearch_20170613_models.UpdateSynonymsDictsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_synonyms_dicts_with_options_async(instance_id, request, headers, runtime)

    def update_synonyms_dicts_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateSynonymsDictsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UpdateSynonymsDictsResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateSynonymsDictsResponse(),
            self.do_roarequest('UpdateSynonymsDicts', '2017-06-13', 'HTTPS', 'PUT', 'AK', f'/openapi/instances/{instance_id}/synonymsDict', 'json', req, runtime)
        )

    async def update_synonyms_dicts_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateSynonymsDictsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UpdateSynonymsDictsResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateSynonymsDictsResponse(),
            await self.do_roarequest_async('UpdateSynonymsDicts', '2017-06-13', 'HTTPS', 'PUT', 'AK', f'/openapi/instances/{instance_id}/synonymsDict', 'json', req, runtime)
        )

    def update_template(
        self,
        instance_id: str,
        template_name: str,
        request: elasticsearch_20170613_models.UpdateTemplateRequest,
    ) -> elasticsearch_20170613_models.UpdateTemplateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_template_with_options(instance_id, template_name, request, headers, runtime)

    async def update_template_async(
        self,
        instance_id: str,
        template_name: str,
        request: elasticsearch_20170613_models.UpdateTemplateRequest,
    ) -> elasticsearch_20170613_models.UpdateTemplateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_template_with_options_async(instance_id, template_name, request, headers, runtime)

    def update_template_with_options(
        self,
        instance_id: str,
        template_name: str,
        request: elasticsearch_20170613_models.UpdateTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UpdateTemplateResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        template_name = OpenApiUtilClient.get_encode_param(template_name)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateTemplateResponse(),
            self.do_roarequest('UpdateTemplate', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/templates/{template_name}', 'json', req, runtime)
        )

    async def update_template_with_options_async(
        self,
        instance_id: str,
        template_name: str,
        request: elasticsearch_20170613_models.UpdateTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UpdateTemplateResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        template_name = OpenApiUtilClient.get_encode_param(template_name)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateTemplateResponse(),
            await self.do_roarequest_async('UpdateTemplate', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/templates/{template_name}', 'json', req, runtime)
        )

    def update_white_ips(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateWhiteIpsRequest,
    ) -> elasticsearch_20170613_models.UpdateWhiteIpsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_white_ips_with_options(instance_id, request, headers, runtime)

    async def update_white_ips_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateWhiteIpsRequest,
    ) -> elasticsearch_20170613_models.UpdateWhiteIpsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_white_ips_with_options_async(instance_id, request, headers, runtime)

    def update_white_ips_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateWhiteIpsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UpdateWhiteIpsResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.modify_mode):
            query['modifyMode'] = request.modify_mode
        body = {}
        if not UtilClient.is_unset(request.es_ipwhitelist):
            body['esIPWhitelist'] = request.es_ipwhitelist
        if not UtilClient.is_unset(request.white_ip_group):
            body['whiteIpGroup'] = request.white_ip_group
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateWhiteIpsResponse(),
            self.do_roarequest_with_form('UpdateWhiteIps', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/white-ips', 'json', req, runtime)
        )

    async def update_white_ips_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateWhiteIpsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UpdateWhiteIpsResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.modify_mode):
            query['modifyMode'] = request.modify_mode
        body = {}
        if not UtilClient.is_unset(request.es_ipwhitelist):
            body['esIPWhitelist'] = request.es_ipwhitelist
        if not UtilClient.is_unset(request.white_ip_group):
            body['whiteIpGroup'] = request.white_ip_group
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateWhiteIpsResponse(),
            await self.do_roarequest_with_form_async('UpdateWhiteIps', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/white-ips', 'json', req, runtime)
        )

    def update_xpack_monitor_config(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateXpackMonitorConfigRequest,
    ) -> elasticsearch_20170613_models.UpdateXpackMonitorConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_xpack_monitor_config_with_options(instance_id, request, headers, runtime)

    async def update_xpack_monitor_config_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateXpackMonitorConfigRequest,
    ) -> elasticsearch_20170613_models.UpdateXpackMonitorConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_xpack_monitor_config_with_options_async(instance_id, request, headers, runtime)

    def update_xpack_monitor_config_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateXpackMonitorConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UpdateXpackMonitorConfigResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateXpackMonitorConfigResponse(),
            self.do_roarequest('UpdateXpackMonitorConfig', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/logstashes/{instance_id}/xpack-monitor-config', 'json', req, runtime)
        )

    async def update_xpack_monitor_config_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpdateXpackMonitorConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UpdateXpackMonitorConfigResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateXpackMonitorConfigResponse(),
            await self.do_roarequest_async('UpdateXpackMonitorConfig', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/logstashes/{instance_id}/xpack-monitor-config', 'json', req, runtime)
        )

    def upgrade_engine_version(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpgradeEngineVersionRequest,
    ) -> elasticsearch_20170613_models.UpgradeEngineVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.upgrade_engine_version_with_options(instance_id, request, headers, runtime)

    async def upgrade_engine_version_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpgradeEngineVersionRequest,
    ) -> elasticsearch_20170613_models.UpgradeEngineVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.upgrade_engine_version_with_options_async(instance_id, request, headers, runtime)

    def upgrade_engine_version_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpgradeEngineVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UpgradeEngineVersionResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        body = {}
        if not UtilClient.is_unset(request.version):
            body['version'] = request.version
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpgradeEngineVersionResponse(),
            self.do_roarequest_with_form('UpgradeEngineVersion', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/actions/upgrade-version', 'json', req, runtime)
        )

    async def upgrade_engine_version_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.UpgradeEngineVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.UpgradeEngineVersionResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        body = {}
        if not UtilClient.is_unset(request.version):
            body['version'] = request.version
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpgradeEngineVersionResponse(),
            await self.do_roarequest_with_form_async('UpgradeEngineVersion', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/actions/upgrade-version', 'json', req, runtime)
        )

    def validate_connection(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ValidateConnectionRequest,
    ) -> elasticsearch_20170613_models.ValidateConnectionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.validate_connection_with_options(instance_id, request, headers, runtime)

    async def validate_connection_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ValidateConnectionRequest,
    ) -> elasticsearch_20170613_models.ValidateConnectionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.validate_connection_with_options_async(instance_id, request, headers, runtime)

    def validate_connection_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ValidateConnectionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ValidateConnectionResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ValidateConnectionResponse(),
            self.do_roarequest('ValidateConnection', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/logstashes/{instance_id}/validate-connection', 'json', req, runtime)
        )

    async def validate_connection_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ValidateConnectionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ValidateConnectionResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ValidateConnectionResponse(),
            await self.do_roarequest_async('ValidateConnection', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/logstashes/{instance_id}/validate-connection', 'json', req, runtime)
        )

    def validate_shrink_nodes(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ValidateShrinkNodesRequest,
    ) -> elasticsearch_20170613_models.ValidateShrinkNodesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.validate_shrink_nodes_with_options(instance_id, request, headers, runtime)

    async def validate_shrink_nodes_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ValidateShrinkNodesRequest,
    ) -> elasticsearch_20170613_models.ValidateShrinkNodesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.validate_shrink_nodes_with_options_async(instance_id, request, headers, runtime)

    def validate_shrink_nodes_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ValidateShrinkNodesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ValidateShrinkNodesResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.node_type):
            query['nodeType'] = request.node_type
        if not UtilClient.is_unset(request.ignore_status):
            query['ignoreStatus'] = request.ignore_status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ValidateShrinkNodesResponse(),
            self.do_roarequest('ValidateShrinkNodes', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/validate-shrink-nodes', 'json', req, runtime)
        )

    async def validate_shrink_nodes_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ValidateShrinkNodesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ValidateShrinkNodesResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.node_type):
            query['nodeType'] = request.node_type
        if not UtilClient.is_unset(request.ignore_status):
            query['ignoreStatus'] = request.ignore_status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ValidateShrinkNodesResponse(),
            await self.do_roarequest_async('ValidateShrinkNodes', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/validate-shrink-nodes', 'json', req, runtime)
        )

    def validate_slr_permission(
        self,
        request: elasticsearch_20170613_models.ValidateSlrPermissionRequest,
    ) -> elasticsearch_20170613_models.ValidateSlrPermissionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.validate_slr_permission_with_options(request, headers, runtime)

    async def validate_slr_permission_async(
        self,
        request: elasticsearch_20170613_models.ValidateSlrPermissionRequest,
    ) -> elasticsearch_20170613_models.ValidateSlrPermissionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.validate_slr_permission_with_options_async(request, headers, runtime)

    def validate_slr_permission_with_options(
        self,
        request: elasticsearch_20170613_models.ValidateSlrPermissionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ValidateSlrPermissionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.rolename):
            query['rolename'] = request.rolename
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ValidateSlrPermissionResponse(),
            self.do_roarequest('ValidateSlrPermission', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/user/servicerolepermission', 'json', req, runtime)
        )

    async def validate_slr_permission_with_options_async(
        self,
        request: elasticsearch_20170613_models.ValidateSlrPermissionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ValidateSlrPermissionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.rolename):
            query['rolename'] = request.rolename
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ValidateSlrPermissionResponse(),
            await self.do_roarequest_async('ValidateSlrPermission', '2017-06-13', 'HTTPS', 'GET', 'AK', f'/openapi/user/servicerolepermission', 'json', req, runtime)
        )

    def validate_transferable_nodes(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ValidateTransferableNodesRequest,
    ) -> elasticsearch_20170613_models.ValidateTransferableNodesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.validate_transferable_nodes_with_options(instance_id, request, headers, runtime)

    async def validate_transferable_nodes_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ValidateTransferableNodesRequest,
    ) -> elasticsearch_20170613_models.ValidateTransferableNodesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.validate_transferable_nodes_with_options_async(instance_id, request, headers, runtime)

    def validate_transferable_nodes_with_options(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ValidateTransferableNodesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ValidateTransferableNodesResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.node_type):
            query['nodeType'] = request.node_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ValidateTransferableNodesResponse(),
            self.do_roarequest('ValidateTransferableNodes', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/validate-transfer-nodes', 'json', req, runtime)
        )

    async def validate_transferable_nodes_with_options_async(
        self,
        instance_id: str,
        request: elasticsearch_20170613_models.ValidateTransferableNodesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> elasticsearch_20170613_models.ValidateTransferableNodesResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.node_type):
            query['nodeType'] = request.node_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ValidateTransferableNodesResponse(),
            await self.do_roarequest_async('ValidateTransferableNodes', '2017-06-13', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/validate-transfer-nodes', 'json', req, runtime)
        )
